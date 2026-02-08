---
title: "Ring Attention with Blockwise Transformers for Near-Infinite Context"
authors: "Liu, Zaharia, Abbeel"
year: 2024
venue: "ICLR 2024"
paper_type: conference-paper
categories: ["attention-efficiency", "architecture"]
scope: ["distributed training", "sequence parallelism", "memory efficiency", "exact attention"]
benchmarks_used: []
models_introduced: []
models_evaluated: ["llama-7b", "llama-13b", "llama-65b"]
key_claims:
  - id: C1
    claim: "Ring Attention enables training sequences up to device count times longer than prior memory-efficient Transformers without approximations or additional overhead"
    evidence: "Table 3, Section 5.1"
    status: supported
    scope: "LLaMA 3B--30B on TPU and GPU clusters with high-bandwidth interconnect, using FSDP"
    magnitude: "8x on 8xA100 NVLink, 32x on 32xA100 InfiniBand, 128x--512x on TPU pods"
  - id: C2
    claim: "Ring Attention achieves zero communication overhead by overlapping KV block transfers with blockwise attention computation"
    evidence: "Section 3, Table 4, Section 5.2"
    status: supported
    scope: "When block size c >= FLOPS/Bandwidth, tested on A100 NVLink/InfiniBand and TPUv3/v4/v5e"
    magnitude: "MFU comparable to BPT baseline across 7B--65B models"
  - id: C3
    claim: "Memory requirement per host scales with block size c, independent of sequence length s"
    evidence: "Table 1, Section 3"
    status: supported
    scope: "General property of Ring Attention architecture, assuming bfloat16 precision"
    magnitude: "6bch bytes total activation per layer vs 2bhs^2 for vanilla Transformer"
  - id: C4
    claim: "Ring Attention enables training sequences exceeding 100 million tokens"
    evidence: "Figure 1, Section 1, Section 7"
    status: supported
    scope: "Large TPU clusters; demonstrated at 16M+ on TPUv4-1024, 100M+ extrapolated via linear scaling"
    magnitude: "16,384K tokens demonstrated for 3B on TPUv4-1024; 100M+ extrapolated"
  - id: C5
    claim: "Ring Attention maintains model flops utilization (MFU) comparable to baselines while enabling much longer context"
    evidence: "Table 4, Section 5.2"
    status: supported
    scope: "7B--65B models on 8xA100, 32xA100, and TPUv4-1024"
    magnitude: "MFU within comparable range of BPT despite 8x--128x longer context"
  - id: C6
    claim: "Longer context via Ring Attention improves in-context RL performance"
    evidence: "Table 5, Section 5.3"
    status: supported
    scope: "ExoRL benchmark, 350M AT model, 6 tasks, single comparison (32 vs 128 trajectories)"
    magnitude: "Average return 113.66 (128 trajs with Ring Attention) vs 111.13 (32 trajs with BPT)"
  - id: C7
    claim: "Ring Attention enables long-context LLM retrieval at 512K tokens with high accuracy"
    evidence: "Figure 3, Section 5.4"
    status: supported
    scope: "LLaMA-13B finetuned on ShareGPT, line retrieval test only, single model single run"
    magnitude: "~90% accuracy at 500K tokens vs GPT-3.5/Vicuna/Claude-2 which degrade beyond their context limits"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Ring Attention reorganizes the computation of standard Transformer attention for distributed execution while preserving exact attention computation"
  - target: 2022-12-flashattention
    type: extends
    detail: "Builds on memory-efficient attention techniques; Ring Attention uses blockwise computation locally on each host and overlaps inter-host KV communication"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer uses sparse attention patterns to reduce complexity; Ring Attention distributes exact full attention across devices for even longer contexts"
  - target: 2023-02-llama-open-efficient-foundation
    type: evaluates
    detail: "Experiments use LLaMA architecture (3B, 7B, 13B, 30B) and 65B model to evaluate maximum context length and MFU"
open_questions:
  - question: "How does Ring Attention interact with other parallelism strategies (tensor parallelism, pipeline parallelism) beyond FSDP?"
    addressed_by: null
  - question: "Can current architectures effectively utilize information across 10M+ token contexts enabled by Ring Attention?"
    addressed_by: null
  - question: "Can Ring Attention be combined with sparse attention patterns to further extend practical context limits?"
    addressed_by: null
  - question: "How does performance scale with heterogeneous interconnect bandwidths in mixed GPU/TPU or non-uniform clusters?"
    addressed_by: null
  - question: "What is the optimal block size selection strategy across different model sizes and hardware configurations?"
    addressed_by: null
---

# Ring Attention with Blockwise Transformers for Near-Infinite Context

**Authors:** Hao Liu, Matei Zaharia, Pieter Abbeel (UC Berkeley, Databricks)
**Date:** May 2024, ICLR 2024 (arXiv:2310.01889, October 2023)

---

## Core Research Problem

Transformer self-attention has O(n^2) memory complexity in sequence length n, making it infeasible to process very long sequences. Even with memory-efficient attention techniques that avoid materializing the full attention matrix, a fundamental bottleneck remains: **storing the output of each layer**. Self-attention involves n-to-n interactions, so the subsequent layer's attention requires access to all prior layer outputs. Without storing these outputs, recomputation would increase computational costs cubically, as every output must be recomputed for each sequence element (Section 1).

To put the memory demand in perspective: processing 100 million tokens with batch size 1 requires over 1000GB of memory for a modest model with hidden size 1024. Modern GPUs and TPUs typically provide less than 100GB of high-bandwidth memory (HBM), and prospects for significant HBM expansion are limited by physical constraints and manufacturing costs (Section 2).

Prior work on memory-efficient Transformers has focused on two approaches: (1) **blockwise computation** that avoids materializing the full attention matrix (Milakov & Gimelshein, 2018; Rabe & Staats, 2021; Dao et al., 2022; Liu & Abbeel, 2023), reducing per-layer activation memory from O(n^2) to O(n), and (2) **sequence parallelism** that distributes sequences across devices (Li et al., 2023), but incurs significant non-overlapped communication overhead. Even the combination of these approaches faces a fundamental limit: each device must eventually store or communicate layer outputs for the full sequence. Prior work on ring topology for self-attention (Li et al., 2023) incurs non-overlapped communication overheads that render it infeasible for large-context scenarios (Section 1, Section 6).

The core challenge is: **how to distribute long sequences across multiple devices such that the context length scales linearly with the number of devices, without approximations and without communication overhead.**

---

## Problem Solutions

The paper introduces **Ring Attention**, which combines blockwise parallel computation with a ring communication topology to distribute sequences across devices while fully overlapping communication with computation. The solution rests on three key insights:

1. **Blockwise attention is permutation-invariant in the key-value dimension.** The self-attention between a query block and a group of key-value blocks can be computed in any order, as long as the statistics (max scores, denominators) are combined correctly for rescaling (Section 3).

2. **Ring topology enables pipelined communication.** By organizing devices in a conceptual ring, each device can send its current key-value blocks to the next device while receiving blocks from the previous device, overlapping communication with computation (Section 3, Figure 2).

3. **Sufficient arithmetic intensity ensures zero overhead.** When the block size is large enough that blockwise attention computation takes longer than block transfer, the communication is fully hidden behind computation (Section 3).

---

## Approach Details

### Method

Ring Attention distributes the outer loop of blockwise attention across devices, with each device holding one query block. Key-value blocks rotate around the ring of devices, and each device computes blockwise attention incrementally as it receives new KV blocks.

**Standard attention computation** (Section 2):

> Attention(Q, K, V) = softmax(QK^T / sqrt(d)) V

where Q, K, V are in R^{s x d}, s is sequence length, d is head dimension, and softmax is applied row-wise.

**Feedforward network** (Section 2):

> FFN(x) = max(0, xW_1 + b_1)W_2 + b_2

**Blockwise Parallel Transformers (BPT) baseline.** Prior work (Liu & Abbeel, 2023) computes both attention and feedforward in a block-by-block manner, reducing maximum activation size per layer to **2bsh** (from 8bsh for vanilla feedforward), where b is batch size, s is sequence length, and h is hidden dimension. However, BPT still requires storing the full output of each layer (Section 2).

**Ring-based blockwise attention (Algorithm 1).** Ring Attention extends BPT by distributing the sequence across N_h hosts:

1. Split input sequence into N_h blocks, one per host
2. Each host computes query, key, value for its local block
3. For each transformer layer:
   - For count = 1 to N_h - 1:
     - Each host computes memory-efficient attention incrementally using local query and current KV blocks
     - Concurrently: send KV blocks to next host, receive KV blocks from previous host (via `jax.lax.ppermute`)
   - Each host computes memory-efficient feedforward on local attention output

The ring topology uses `jax.lax.ppermute` for collective send/receive operations between adjacent hosts. This overlapping mechanism applies to both forward and backward passes (Section 3, Algorithm 1, Appendix A).

### Key Technical Components

**Arithmetic intensity condition for zero overhead.** Let F be FLOPS per host and B be inter-host bandwidth. For block size c and hidden dimension d (Section 3):

- Computation: 4dc^2 FLOPs (2dc^2 for QK^T scores, 2dc^2 for score x V)
- Communication: 4cd bytes (2cd for K, 2cd for V)

The projections of queries, keys, values, and blockwise feedforward are excluded since they only add compute complexity without communication costs -- this simplification leads to a more stringent condition. To overlap communication with computation: 4dc^2/F >= 4cd/B, which simplifies to:

> c >= F/B

The minimal block size equals the ratio of FLOPS to bandwidth.

**Memory requirement (Table 1).** Each host stores:
- 1 block for query
- 2 blocks for current key and value
- 2 blocks for receiving key and value
- 1 block for output

Total: **6bch bytes** of activation memory, where c is block size. This is independent of sequence length s. The blockwise feedforward has maximum activation size of 2bch (Liu & Abbeel, 2023). Total maximum activation remains 6bch.

| Layer Type | Self-Attention | FeedForward | Total |
|---|---|---|---|
| Vanilla | 2bns^2 | 8bsh | 2bhs^2 |
| Memory efficient attention | 2bsh + 4bch | 8bsh | 8bsh |
| Memory efficient attn + FFN | 2bsh | 2bsh | 2bsh |
| **Ring Attention** | **6bch** | **2bch** | **6bch** |

(Table 1, Section 3. b = batch size, h = hidden dimension, n = number of heads, s = sequence length, c = block size. Numbers are bytes per layer assuming bfloat16.)

**Minimal sequence length requirements (Table 2).** The model needs sequence length s = 6c (six times the minimal block size). Requirements for common hardware:

| Hardware | FLOPS (TF) | HBM (GB) | Bandwidth (GB/s) | Min Block Size (x1e3) | Min Seq Len (x1e3) |
|---|---|---|---|---|---|
| A100 NVLink | 312 | 80 | 300 | 1.0 | 6.2 |
| A100 InfiniBand | 312 | 80 | 12.5 | 24.5 | 149.5 |
| TPU v3 | 123 | 16 | 112 | 1.1 | 6.6 |
| TPU v4 | 275 | 32 | 268 | 1.0 | 6.2 |
| TPU v5e | 196 | 16 | 186 | 1.1 | 6.3 |

(Table 2, Section 3. Interconnect bandwidth is unidirectional between hosts: NVLink/InfiniBand for GPUs, ICI for TPUs.)

A100 GPUs with InfiniBand have stricter requirements (149.5K minimum sequence length) due to lower bandwidth (12.5 GB/s vs 300 GB/s for NVLink). Requirements are 6K--10K for TPUs and GPUs with high-bandwidth interconnect, which are easy to meet with data and tensor parallelism.

**Inference applicability (Appendix C).** While the paper focuses on training (which is more memory-demanding), Ring Attention also applies to autoregressive inference. For inference, the overlap condition becomes:

> d^2/F >= 2 * d^2/B, i.e., B/F >= 2

For a LLaMA 7B on 32x TPUv5e (bandwidth 186 GB/s, FLOPS 196 TF, assuming 40% MFU), B/F = 2.4, satisfying the condition. This enables 32x larger context for inference without overhead.

### Experimental Setup

**Model configuration:** LLaMA architecture with 3B, 7B, 13B, and 30B parameter sizes. Table 4/MFU evaluation additionally tests 65B (Section 4, Section 5.2).

**Baselines** (Section 4):
- Vanilla Transformer -- materializes full attention matrix
- Memory-efficient attention (Rabe & Staats, 2021; Dao et al., 2022)
- Blockwise Parallel Transformer (Liu & Abbeel, 2023)

**Hardware** (Section 4):
- GPUs: Single DGX A100 (8 GPUs), distributed 32x A100
- TPUs: TPUv3-512, TPUv4-1024, TPUv5e-256

**Training configuration** (Section 4, Appendix B):
- Full gradient checkpointing for attention and feedforward (using `nothing_saveable` as checkpointing policy)
- For TPUs: matmul in bfloat16 with weight accumulation in float32
- For GPUs: all operations in float32
- FSDP for model sharding
- Batch size: 2M tokens on GPU, 4M tokens on TPU (for MFU evaluation)

**Downstream evaluations** (Section 5.3, 5.4):
- **ExoRL benchmark** (Yarats et al., 2022): Six RL tasks evaluating in-context learning from diverse exploratory trajectories. AT model with 350M parameters. Comparison at 32 vs 128 trajectories (each trajectory = 1000 x 4 = 4000 tokens).
- **Line retrieval test** (Li et al., 2023): Model must retrieve a number from a long document. LLaMA-13B finetuned on ShareGPT (125K cleaned conversations) on 32x A100 GPUs, context limited to 512K due to compute budget.

**Reproducibility:** Code available at https://github.com/lhao499/llm_large_context. Hardware-specific configurations (TPU/GPU) are described. No seeds reported. Single runs per configuration, no variance estimates provided (limited evidence for downstream tasks).

### Key Results

**Maximum context length (Table 3, Section 5.1).** Evaluated using FSDP with matching total batch sizes in tokens across methods. On n devices with FSDP, baselines achieve sequence length l; Ring Attention extends to nl/m with m sequences, keeping total tokens the same (tested across 4 model sizes and 5 hardware configs -- strong hardware breadth):

| Hardware | Model | Vanilla | Mem Eff Attn | BPT | Ring Attention | Improvement |
|---|---|---|---|---|---|---|
| 8x A100 NVLink | 3B | 4K | 32K | 64K | **512K** | 8x |
| 8x A100 NVLink | 7B | 2K | 16K | 32K | **256K** | 8x |
| 8x A100 NVLink | 13B | 2K | 4K | 16K | **128K** | 8x |
| 32x A100 InfiniBand | 7B | 4K | 64K | 128K | **4,096K** | 32x |
| 32x A100 InfiniBand | 13B | 4K | 32K | 64K | **2,048K** | 32x |
| TPUv3-512 | 7B | 1K | 4K | 8K | **2,048K** | 256x |
| TPUv3-512 | 13B | 1K | 2K | 8K | **1,024K** | 128x |
| TPUv4-1024 | 3B | 8K | 16K | 32K | **16,384K** | 512x |
| TPUv4-1024 | 7B | 4K | 8K | 16K | **8,192K** | 512x |
| TPUv4-1024 | 13B | 4K | 8K | 16K | **4,096K** | 256x |
| TPUv4-1024 | 30B | 2K | 4K | 8K | **2,048K** | 256x |
| TPUv5e-256 | 3B | 4K | 8K | 32K | **4,096K** | 128x |
| TPUv5e-256 | 7B | 2K | 8K | 16K | **2,048K** | 128x |

- Ring Attention scales **linearly** with device count: 8x improvement on 8 A100s, 32x on 32 A100s, 256x--512x on TPU pods.
- Enables training sequences exceeding 16 million tokens on TPUv4-1024 for 3B model.
- With 32 A100 GPUs, achieves over 4 million tokens for 7B model (Section 5.1).

**Model flops utilization (Table 4 / Figure, Section 5.2).** Ring Attention trains with much longer context, increasing self-attention FLOPs relative to feedforward. Since self-attention has lower MFU than feedforward, Ring Attention is expected to have somewhat lower MFU. Results show the actual MFU matches the expected MFU closely, confirming negligible communication overhead (tested across 5 configurations, moderate evidence):

| Config | Compute | BPT Context | Ring Attention Context |
|---|---|---|---|
| 7B | 8x A100 | 32K | 256K |
| 13B | 8x A100 | 16K | 128K |
| 13B | 32x A100 | 64K | 2,048K |
| 30B | TPUv4-1024 | 16K | 2,048K |
| 65B | TPUv4-1024 | 8K | 1,024K |

All configurations show MFU in the ~30--35% range for both BPT and Ring Attention, with Ring Attention actual MFU matching the expected MFU (Figure in Section 5.2). Ring Attention enables 8x--128x longer context with negligible MFU degradation.

**In-context RL performance (Table 5, Section 5.3).** ExoRL benchmark with AT (Algorithm Transformer) model. AT + ME (memory-efficient attention) goes OOM for all tasks with 32 trajectories. AT + BPT handles 32 trajectories but OOMs at 128. Ring Attention enables 128 trajectories (single comparison, no variance reported -- limited evidence):

| ExoRL Task | BC-10% | DT | AT+ME (32 trajs) | AT+BPT (32 trajs) | AT+BPT (128 trajs) | AT+RA (128 trajs) |
|---|---|---|---|---|---|---|
| Walker Stand | 52.91 | 34.54 | OOM | 95.45 | OOM | **98.23** |
| Walker Run | 34.81 | 49.82 | OOM | 105.88 | OOM | **110.45** |
| Walker Walk | 13.53 | 34.94 | OOM | 78.56 | OOM | **78.95** |
| Cheetah Run | 34.66 | 67.53 | OOM | 178.75 | OOM | **181.34** |
| Jaco Reach | 23.95 | 18.64 | OOM | 87.56 | OOM | **89.51** |
| Cartpole Swingup | 56.82 | 67.56 | OOM | 120.56 | OOM | **123.45** |
| **Total Average** | **36.11** | **45.51** | OOM | **111.13** | OOM | **113.66** |

AT + Ring Attention with 128 trajectories outperforms AT + BPT with 32 trajectories (the maximum BPT can handle before OOM), achieving total average return of 113.66 vs 111.13. This demonstrates the benefit of longer context for in-context RL, though the improvement is modest (2.3% average gain, single run per configuration).

**Line retrieval evaluation (Figure 3, Section 5.4).** LLaMA-13B finetuned with Ring Attention to 512K context on ShareGPT data, evaluated on the line retrieval test (single model, single finetuning run -- limited evidence):

- **Ring Attention-13B-512K** maintains high accuracy (~90%) across all context lengths from 4K to 500K.
- **GPT-3.5-turbo-16K** maintains near-perfect accuracy up to 16K but cannot handle longer contexts.
- **Vicuna-13B-16K** starts near 1.0 at 4K but drops to ~0.6 at 12K.
- **Claude-2-100K** maintains near-perfect accuracy up to ~64K, slight drop to ~0.9 at 100K.

Ring Attention-13B stands out by maintaining retrieval capability at 500K tokens, far beyond any baseline's context limit.

### Training FLOPs Scaling Analysis

Appendix D analyzes how training FLOPs per dataset scale with context size. Per-sequence FLOPs are (24bsh^2 + 4bs^2h)n, yielding a per-dataset FLOPs ratio when changing context length from s_1 to s_2:

> FLOPs ratio = (6h + s_2) / (6h + s_1)

Key observations from the heatmap (Figure 5, Appendix D):

| Model Size | 8x (32K) | 32x (128K) | 256x (1M) | 3072x (10M) |
|---|---|---|---|---|
| 7B (h=4096) | 2.0 | 5.4 | 37.4 | 439.7 |
| 13B (h=5140) | 1.8 | 4.6 | 31.0 | 362.3 |
| 65B (h=8192) | 1.5 | 3.4 | 20.6 | 237.2 |
| 175B (h=12288) | 1.4 | 2.6 | 14.4 | 162.6 |

Larger models have more favorable scaling because the hidden dimension h dominates over s in the ratio formula. Scaling 7B to 1M context costs 37.4x more per-dataset FLOPs despite 256x more context. The cost ratio decreases with model size: 175B at 10M context costs only 162.6x more FLOPs despite 3072x longer context.

---

## Limitations and Failure Modes

All limitations below are **[Inferred]** -- the paper does not explicitly acknowledge limitations in a dedicated section.

- **[Inferred] Interconnect bandwidth dependency.** The zero-overhead property requires sufficient bandwidth relative to compute (c >= F/B). A100 GPUs with InfiniBand (12.5 GB/s) require 24.5K minimum block size and 149.5K minimum sequence length vs. 1.0K block size and 6.2K sequence length for NVLink (300 GB/s), severely limiting applicability on lower-bandwidth clusters (Table 2).

- **[Inferred] No evaluation of downstream task quality at extreme lengths.** While the paper demonstrates training at millions of tokens, the downstream evaluations (line retrieval, ExoRL) use at most 512K tokens. Whether models effectively utilize information across 10M+ token contexts is not demonstrated.

- **[Inferred] No comparison with approximate attention methods.** The paper focuses on exact attention. Comparison with sparse attention (e.g., Longformer, BigBird) or linear attention approximations that might achieve similar practical context lengths with fewer devices is not provided.

- **[Inferred] Limited model architectures.** Experiments use only LLaMA-style decoder-only models; applicability to encoder-decoder or bidirectional architectures is not evaluated.

- **[Inferred] Single runs, no variance estimates.** All downstream experiments (ExoRL, line retrieval) appear to use single runs without variance reporting. The ExoRL improvement (113.66 vs 111.13 average return) is modest and could fall within run-to-run variance.

- **[Inferred] Limited downstream evaluation.** Only two downstream tasks are evaluated (ExoRL with 6 sub-tasks, and line retrieval). No evaluation on standard NLP benchmarks (summarization, question answering, etc.) at long context.

### Scope and Comparability

- **[Inferred] What was not tested:** Models beyond LLaMA architecture; encoder-decoder models; non-English evaluation; mixed-precision training effects on memory savings; contexts beyond 512K for downstream quality evaluation; comparison with DeepSpeed Ulysses or Megatron sequence parallelism on the same benchmarks.

- **[Inferred] Comparability notes:** The 512x improvement on TPUv4-1024 reflects 1024 devices with 268 GB/s ICI bandwidth; different hardware configurations yield different scaling factors. Context length improvements are measured against BPT (Liu & Abbeel, 2023), not against concurrent distributed training approaches. The ExoRL comparison is between 32 trajectories (BPT limit) and 128 trajectories (Ring Attention), conflating the method improvement with the data quantity improvement.

---

## Conclusions

### Contributions

1. **Linear scaling of context with device count.** Ring Attention enables context length to scale linearly with the number of devices by distributing sequences in a ring topology with overlapped communication. On N devices, if BPT achieves context length s, Ring Attention achieves context length Ns. Demonstrated across 5 hardware configurations and 4 model sizes (Table 3, Section 5.1).

2. **Zero communication overhead through computation-communication overlap.** By leveraging the permutation invariance of blockwise attention's inner loop, Ring Attention pipelines KV block transfers with blockwise computation. When block size exceeds the FLOPS/Bandwidth ratio, communication is fully hidden. MFU measurements confirm negligible overhead across 5 configurations (Section 3, Table 4).

3. **Memory independent of sequence length.** Ring Attention's activation memory (6bch per layer) depends only on block size c, not sequence length s. This eliminates the fundamental memory bottleneck of storing full layer outputs (Table 1, Section 3).

4. **Practical demonstration at scale.** Experiments demonstrate training with over 16 million tokens on TPUv4-1024 (3B model) and over 4 million tokens on 32x A100 (7B model), representing 128x--512x improvement over prior memory-efficient methods (Table 3).

5. **Downstream task improvements from longer context.** In-context RL (ExoRL) shows improved performance (113.66 vs 111.13 average return) when conditioning on 128 vs 32 trajectories. Line retrieval maintains ~90% accuracy at 500K tokens (Table 5, Figure 3).

### Implications

1. **Near-infinite context becomes feasible.** By removing the single-device memory bottleneck, context length is limited only by the number of available devices and training budget, not by memory capacity. [Inference: this enables new applications requiring very long context, such as processing entire codebases, long videos, or scientific datasets, as the authors suggest in Section 7.]

2. **Exact attention remains competitive at extreme lengths.** Ring Attention achieves extreme context lengths without approximating attention, suggesting that the practical context-length limitations of exact attention are primarily memory constraints rather than computational ones.

3. **Communication-computation overlap is the key enabler.** The critical insight is not distributing sequences per se (prior sequence parallelism does this), but overlapping the communication with blockwise computation. This design pattern may generalize to other distributed computation challenges.

---

## Key Claims

1. **C1: Linear scaling with device count.** Ring Attention enables training sequences up to device count times longer than prior memory-efficient Transformers. On 8x A100, this is 8x improvement (e.g., 256K vs 32K for 7B); on TPUv4-1024, this is 512x (8,192K vs 16K for 7B) (Table 3, Section 5.1). Tested across 4 model sizes (3B--30B) and 5 hardware configurations (strong hardware evidence). Status: **supported**. Scope: LLaMA architecture with FSDP on tested hardware configs. Magnitude: 8x--512x depending on device count and interconnect.

2. **C2: Zero communication overhead.** When block size c >= F/B, communication of KV blocks is fully overlapped with blockwise attention computation. MFU measurements confirm negligible overhead across 7B--65B models on A100 and TPUv4 (Table 4, Section 5.2). Tested across 5 model-hardware combinations (moderate evidence). Status: **supported**. Scope: requires sufficient block size relative to FLOPS/bandwidth ratio. Magnitude: MFU within comparable range of BPT baseline (~30--35%).

3. **C3: Memory scales with block size, not sequence length.** Ring Attention requires 6bch bytes of activation per layer, independent of sequence length s, compared to 2bhs^2 for vanilla Transformers (Table 1, Section 3). This is an analytical result, not empirical (strong theoretical evidence). Status: **supported**. Scope: general architecture property assuming bfloat16. Magnitude: 6bch vs 2bhs^2.

4. **C4: Training at 100M+ tokens.** Ring Attention enables training sequences exceeding 100 million tokens without approximations (Section 1, Section 7). The paper demonstrates 16M+ on TPUv4-1024 for 3B; extrapolation to 100M+ is based on linear scaling with device count (demonstrated scaling property + extrapolation, moderate evidence). Status: **supported** (demonstrated at 16M, extrapolated to 100M).

5. **C5: MFU maintained at longer context.** Ring Attention achieves MFU comparable to BPT baselines while training with 8x--128x longer context across 7B--65B models on multiple hardware configurations (Table 4, Section 5.2). Tested across 5 configurations (moderate evidence). Status: **supported**. Scope: tested hardware and model sizes only. Magnitude: MFU comparable at 8x--128x context extension.

6. **C6: Longer context improves in-context RL.** AT + Ring Attention with 128 trajectories outperforms AT + BPT with 32 trajectories on ExoRL, achieving 113.66 vs 111.13 average return across 6 tasks (Table 5, Section 5.3). Single run per configuration, no variance reported (limited evidence). Status: **supported**. Scope: ExoRL benchmark, 350M AT model, 6 tasks. Magnitude: 2.3% average return improvement (113.66 vs 111.13).

7. **C7: Long-context retrieval at 512K.** Ring Attention-13B finetuned to 512K maintains ~90% accuracy on line retrieval at 500K tokens, while GPT-3.5-turbo-16K, Vicuna-13B-16K, and Claude-2-100K degrade beyond their respective context limits (Figure 3, Section 5.4). Single model, single finetuning run (limited evidence). Status: **supported**. Scope: line retrieval test only, LLaMA-13B on ShareGPT. Magnitude: ~90% accuracy at 500K tokens.

---

## Open Questions

1. **How does Ring Attention interact with other parallelism strategies?** The paper combines Ring Attention with FSDP; interaction with tensor parallelism is mentioned (Section 5.2 header) but not systematically evaluated. Optimal combinations of data/tensor/pipeline/sequence parallelism remain underexplored. Not addressed by subsequent work in references/.

2. **Can current architectures effectively utilize very long context?** While Ring Attention enables training at 16M+ tokens, it is unclear whether current Transformer architectures can effectively utilize information across such long distances. Downstream evaluation is limited to 512K tokens. Not addressed by subsequent work in references/.

3. **Can Ring Attention be combined with sparse attention?** For applications where full attention is not necessary, combining Ring Attention's distribution strategy with sparse patterns (e.g., Longformer's local+global) could further extend practical context limits. Not addressed by subsequent work in references/.

4. **How does performance scale with heterogeneous interconnects?** Real-world clusters often have non-uniform bandwidth; the optimal ring topology and block size selection in such settings is not addressed. Not addressed by subsequent work in references/.

5. **What is the optimal block size selection strategy?** The paper derives the minimum block size c = F/B but does not explore whether larger block sizes offer advantages or how to optimize block size across different model sizes and hardware configurations. Not addressed by subsequent work in references/.

---

## Core References and Why They Are Referenced

### Memory-Efficient Attention Foundations

- **Milakov & Gimelshein (2018)** -- *Online Normalizer Calculation for Softmax.* Introduces the tiling technique enabling blockwise computation of self-attention without materializing the full attention matrix. Foundational for the blockwise computation that Ring Attention builds on.

- **Rabe & Staats (2021)** -- *Self-Attention Does Not Need O(n^2) Memory.* Shows attention can be computed without materializing the full attention matrix using online softmax. Ring Attention uses this for local blockwise computation on each host. Baseline in all experiments.

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* Efficient CUDA implementation of memory-efficient attention. Ring Attention is compatible with FlashAttention for local computation on each host. Baseline in all experiments.

- **Liu & Abbeel (2023)** -- *Blockwise Parallel Transformer for Large Context Models.* Direct predecessor: computes both attention and feedforward block-by-block, reducing activation memory to 2bsh. Ring Attention extends BPT to distribute across devices via ring topology. Primary baseline in all experiments.

### Parallelism and Distributed Training

- **Li et al. (2023)** -- *Sequence Parallelism: Long Sequence Training from System Perspective.* Prior work on sequence parallelism using ring topology for attention. Ring Attention differs by using blockwise computation to achieve zero communication overhead, whereas this approach incurs non-overlapped communication costs.

- **Jacobs et al. (2023)** -- *DeepSpeed Ulysses: System Optimizations for Enabling Training of Extreme Long Sequence Transformer Models.* Concurrent work on long sequence training. Achieves reduced communication via optimized all-to-all topology but is restricted by number of attention heads and requires gathering full sequence on each device.

- **Korthikanti et al. (2022)** -- *Reducing Activation Recomputation in Large Transformer Models.* Prior work on sequence parallelism mentioned as context for distributed training approaches.

### Models and Architectures

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture whose O(n^2) attention complexity Ring Attention addresses. Ring Attention preserves exact attention computation while enabling distribution. Vanilla Transformer is the weakest baseline in all experiments.

- **Touvron et al. (2023)** -- *LLaMA: Open and Efficient Foundation Language Models.* Model architecture used for all experiments (3B, 7B, 13B, 30B, 65B sizes). Also used for FLOPs scaling analysis in Appendix D.

### Evaluation and Applications

- **Li et al. (2023)** -- *How Long Can Open-Source LLMs Truly Promise on Context Length?* Provides the line retrieval test used to evaluate long-context retrieval capability (Section 5.4).

- **Yarats et al. (2022)** -- *Don't Change the Algorithm, Change the Data: Exploratory Data for Offline Reinforcement Learning.* Provides the ExoRL benchmark for evaluating in-context reinforcement learning with diverse exploratory data (Section 5.3).

- **Liu & Abbeel (2023)** -- *Emergent Agentic Transformer from Chain of Hindsight Experience.* Provides the AT (Algorithm Transformer) model used as the RL baseline architecture (Section 5.3).

### Overlapping Communication with Computation

- **Danalis et al. (2005, 2009)** -- *Transformations to Parallel Codes for Communication-Computation Overlap* and *MPI-Aware Compiler Optimizations.* HPC literature on overlapping communication with computation that informs Ring Attention's design principle.

- **Wang et al. (2022)** -- *Overlap Communication with Dependent Computation via Decomposition in Large Deep Learning Models.* Concurrent work on communication-computation overlap in deep learning.
