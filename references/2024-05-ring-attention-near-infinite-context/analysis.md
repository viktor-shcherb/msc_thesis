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
models_evaluated: ["llama-7b", "llama-13b"]
key_claims:
  - id: C1
    claim: "Ring Attention enables training sequences up to device count times longer than prior memory-efficient Transformers without approximations or additional overhead"
    evidence: "Table 3, Figure 1, Section 5.1"
    status: supported
    scope: "TPU and GPU clusters with high-bandwidth interconnect"
    magnitude: "8x--512x improvement over prior SOTA depending on hardware"
  - id: C2
    claim: "Ring Attention achieves zero communication overhead by overlapping KV block transfers with blockwise attention computation"
    evidence: "Section 3, Table 4"
    status: supported
    scope: "When block size c >= FLOPS/Bandwidth"
  - id: C3
    claim: "Memory requirement scales with block size c, independent of sequence length s"
    evidence: "Table 1, Section 3"
    status: supported
    magnitude: "6bch bytes total activation per layer vs 2bhs² for vanilla"
  - id: C4
    claim: "Ring Attention enables training sequences exceeding 100 million tokens"
    evidence: "Figure 1, Section 1"
    status: supported
    scope: "Large TPU clusters (TPUv4-1024)"
  - id: C5
    claim: "Ring Attention maintains model flops utilization (MFU) comparable to baselines while enabling much longer context"
    evidence: "Table 4, Section 5.2"
    status: supported
    scope: "7B--65B models on A100 and TPUv4"
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
    detail: "Experiments use LLaMA architecture (3B, 7B, 13B, 30B) to evaluate maximum context length and MFU"
open_questions:
  - question: "How does Ring Attention performance scale with heterogeneous interconnect bandwidths in mixed GPU/TPU clusters?"
    addressed_by: null
  - question: "Can Ring Attention be combined with sparse attention patterns to achieve even longer effective context?"
    addressed_by: null
  - question: "What is the optimal block size selection strategy across different model sizes and hardware configurations?"
    addressed_by: null
---

# Ring Attention with Blockwise Transformers for Near-Infinite Context

**Authors:** Hao Liu, Matei Zaharia, Pieter Abbeel (UC Berkeley)
**Date:** May 2024, ICLR 2024 (arXiv:2310.01889, October 2023)

---

## Core Research Problem

Transformer self-attention has O(n²) memory complexity in sequence length n, making it infeasible to process very long sequences. Even with memory-efficient attention techniques that avoid materializing the full attention matrix, a fundamental bottleneck remains: **storing the output of each layer**. Self-attention involves n-to-n interactions, so the subsequent layer's attention requires access to all prior layer outputs. Without storing these outputs, recomputation would increase costs cubically.

To put the memory demand in perspective: processing 100 million tokens with batch size 1 requires over 1000GB of memory for a modest model with hidden size 1024. Modern GPUs and TPUs typically provide less than 100GB of high-bandwidth memory (HBM), and prospects for significant HBM expansion are limited by physical constraints and manufacturing costs (Section 1, Section 2).

Prior work on memory-efficient Transformers has focused on two approaches: (1) **blockwise computation** that avoids materializing the full attention matrix (Rabe & Staats, 2021; Dao et al., 2022; Liu & Abbeel, 2023), reducing per-layer activation memory from O(n²) to O(n), and (2) **sequence parallelism** that distributes sequences across devices (Li et al., 2023), but incurs significant non-overlapped communication overhead. The combination of these approaches still faces a fundamental limit: each device must eventually store or communicate layer outputs for the full sequence.

The core challenge is: **how to distribute long sequences across multiple devices such that the context length scales linearly with the number of devices, without approximations and without communication overhead.**

---

## Problem Solutions

The paper introduces **Ring Attention**, which combines blockwise parallel computation with a ring communication topology to distribute sequences across devices while fully overlapping communication with computation. The solution rests on three key insights:

1. **Blockwise attention is permutation-invariant in the key-value dimension.** The self-attention between a query block and a group of key-value blocks can be computed in any order, as long as the statistics (max scores, denominators) are combined correctly for rescaling.

2. **Ring topology enables pipelined communication.** By organizing devices in a conceptual ring, each device can send its current key-value blocks to the next device while receiving blocks from the previous device, overlapping communication with computation.

3. **Sufficient arithmetic intensity ensures zero overhead.** When the block size is large enough that blockwise attention computation takes longer than block transfer, the communication is fully hidden behind computation.

---

## Approach Details

### Method

Ring Attention distributes the outer loop of blockwise attention across devices, with each device holding one query block. Key-value blocks rotate around the ring of devices, and each device computes blockwise attention incrementally as it receives new KV blocks.

**Standard attention computation:**

> Attention(Q, K, V) = softmax(QK^T / sqrt(d)) V

**Blockwise Parallel Transformers (BPT) baseline.** Prior work (Liu & Abbeel, 2023) computes both attention and feedforward in a block-by-block manner, reducing maximum activation size per layer from 8bsh (vanilla) to 2bsh, where b is batch size, s is sequence length, and h is hidden dimension. However, BPT still requires storing the full output of each layer.

**Ring-based blockwise attention.** Ring Attention extends BPT by distributing the sequence across N_h hosts:

1. Split input sequence into N_h blocks, one per host
2. Each host computes query, key, value for its local block
3. For each transformer layer:
   - For count = 1 to N_h - 1:
     - Each host computes memory-efficient attention incrementally using local query and current KV blocks
     - Concurrently: send KV blocks to next host, receive KV blocks from previous host
   - Each host computes feedforward on local attention output

The ring topology uses `jax.lax.ppermute` for collective send/receive operations between adjacent hosts (Algorithm 1, Appendix A).

### Key Technical Components

**Arithmetic intensity condition for zero overhead.** Let F be FLOPS per host and B be inter-host bandwidth. For block size c and hidden dimension d:

- Computation: 4dc² FLOPs (2dc² for QK^T scores, 2dc² for score × V)
- Communication: 4cd bytes (2cd for K, 2cd for V)

To overlap communication with computation: 4dc²/F ≥ 4cd/B, which simplifies to:

> c ≥ F/B

The minimal block size equals the ratio of FLOPS to bandwidth (Section 3).

**Memory requirement.** Each host stores:
- 1 block for query
- 2 blocks for current key and value
- 2 blocks for receiving key and value
- 1 block for output

Total: **6bch bytes** of activation memory, where c is block size. This is independent of sequence length s (Table 1).

| Layer Type | Self-Attention | FeedForward | Total |
|---|---|---|---|
| Vanilla | 2bns² | 8bsh | 2bhs² |
| Memory efficient attention | 2bsh + 4bch | 8bsh | 8bsh |
| Memory efficient attn + FFN | 2bsh | 2bsh | 2bsh |
| **Ring Attention** | **6bch** | **2bch** | **6bch** |

**Minimal sequence length requirements.** The model needs sequence length s = 6c (six times minimal block size). Requirements for common hardware (Table 2):

| Hardware | FLOPS (TF) | HBM (GB) | Bandwidth (GB/s) | Min Block Size | Min Seq Len |
|---|---|---|---|---|---|
| A100 NVLink | 312 | 80 | 300 | 1.0K | 6.2K |
| A100 InfiniBand | 312 | 80 | 12.5 | 24.5K | 149.5K |
| TPU v3 | 123 | 16 | 112 | 1.1K | 6.6K |
| TPU v4 | 275 | 32 | 268 | 1.0K | 6.2K |
| TPU v5e | 196 | 16 | 186 | 1.1K | 6.3K |

A100 GPUs with InfiniBand have stricter requirements due to lower bandwidth.

### Experimental Setup

**Model configuration:** LLaMA architecture with 3B, 7B, 13B, and 30B parameter sizes.

**Baselines:**
- Vanilla Transformer (materializes full attention matrix)
- Memory-efficient attention (Rabe & Staats, 2021; Dao et al., 2022)
- Blockwise Parallel Transformer (Liu & Abbeel, 2023)

**Hardware:**
- GPUs: Single DGX A100 (8 GPUs), distributed 32x A100
- TPUs: TPUv3-512, TPUv4-1024, TPUv5e-256

**Training configuration:** Full gradient checkpointing for attention and feedforward. Full precision (not mixed precision) for all experiments. FSDP for model sharding.

**Downstream evaluations:**
- Line retrieval test (Li et al., 2023): Model must retrieve a number from a long document
- ExoRL benchmark: Six RL tasks evaluating in-context learning from trajectories

### Key Results

**Maximum context length (Table 3):**

| Hardware | Model | Vanilla | Mem Eff Attn | BPT | Ring Attention | Improvement |
|---|---|---|---|---|---|---|
| 8x A100 NVLink | 3B | 4K | 32K | 64K | **512K** | 8x |
| 8x A100 NVLink | 7B | 2K | 16K | 32K | **256K** | 8x |
| 8x A100 NVLink | 13B | 2K | 4K | 16K | **128K** | 8x |
| 32x A100 InfiniBand | 7B | 4K | 64K | 128K | **4,096K** | 32x |
| 32x A100 InfiniBand | 13B | 4K | 32K | 64K | **2,048K** | 32x |
| TPUv3-512 | 7B | 1K | 4K | 8K | **2,048K** | 256x |
| TPUv4-1024 | 3B | 8K | 16K | 32K | **16,384K** | 512x |
| TPUv4-1024 | 7B | 4K | 8K | 16K | **8,192K** | 512x |
| TPUv4-1024 | 13B | 4K | 8K | 16K | **4,096K** | 256x |
| TPUv4-1024 | 30B | 2K | 4K | 8K | **2,048K** | 256x |

- Ring Attention scales linearly with device count
- Enables training sequences exceeding 16 million tokens on TPUv4-1024
- 512x improvement over prior SOTA for 3B and 7B models on TPUv4-1024

**Model flops utilization (Table 4, Figure in Section 5.2):**

| Config | BPT Context | Ring Attention Context | MFU Maintained |
|---|---|---|---|
| 7B on 8x A100 | 32K | 256K | Yes |
| 13B on 8x A100 | 16K | 128K | Yes |
| 13B on 32x A100 | 64K | 2,048K | Yes |
| 30B on TPUv4-1024 | 16K | 2,048K | Yes |
| 65B on TPUv4-1024 | 8K | 1,024K | Yes |

Ring Attention maintains MFU comparable to BPT baselines despite training with 8x--128x longer context.

**In-context RL performance (Table 5, ExoRL benchmark):**

| Task | BC-10% | DT | AT+BPT (32 trajs) | AT+BPT (128 trajs) | AT+Ring (128 trajs) |
|---|---|---|---|---|---|
| Walker Stand | 52.91 | 34.54 | 95.45 | OOM | **98.23** |
| Walker Run | 34.81 | 49.82 | 105.88 | OOM | **110.45** |
| Walker Walk | 13.53 | 34.94 | 78.56 | OOM | **78.95** |
| Cheetah Run | 34.66 | 67.53 | 178.75 | OOM | **181.34** |
| Jaco Reach | 23.95 | 18.64 | 87.56 | OOM | **89.51** |
| Cartpole Swingup | 56.82 | 67.56 | 120.56 | OOM | **123.45** |
| **Average** | 36.11 | 45.51 | 111.13 | OOM | **113.66** |

AT + Ring Attention with 128 trajectories outperforms AT + BPT with 32 trajectories (the maximum BPT can handle), demonstrating the benefit of longer context for in-context RL.

**Line retrieval evaluation (Figure 3):**

Ring Attention-13B-512K maintains high accuracy (>95%) even at 500K context length, while GPT-3.5-turbo-16K, Vicuna-13B-16K, and Claude-2-100K degrade significantly beyond their respective context limits.

---

## Limitations and Failure Modes

- **Interconnect bandwidth dependency.** The zero-overhead property requires sufficient bandwidth relative to compute (c ≥ F/B). A100 GPUs with InfiniBand (12.5 GB/s) require 24.5K minimum block size vs. 1K for NVLink (300 GB/s), limiting practical applicability on lower-bandwidth clusters (Table 2).

- **No evaluation of downstream task quality at extreme lengths.** While the paper demonstrates that Ring Attention can train at millions of tokens, the downstream evaluations (line retrieval, ExoRL) use at most 512K tokens. It is unclear whether models effectively utilize information across 10M+ token contexts.

- **Single-machine overhead not characterized.** All experiments use distributed settings; overhead on single-device setups is not reported.

- **No comparison with approximate attention methods.** The paper focuses on exact attention; comparison with sparse or linear attention approximations that might achieve similar practical context lengths with less hardware is not provided.

- **Limited model architectures.** Experiments use only LLaMA-style decoder-only models; applicability to encoder-decoder or bidirectional architectures is not evaluated.

### Scope and Comparability

- **Hardware requirements:** Results assume high-bandwidth interconnects. The 512x improvement on TPUv4-1024 reflects 1024 devices with 268 GB/s ICI bandwidth; different hardware configurations would yield different scaling factors.

- **Comparison baseline:** Improvements are measured against Blockwise Parallel Transformers (BPT), not against other distributed training approaches like DeepSpeed Ulysses or Megatron sequence parallelism.

---

## Conclusions

### Contributions

1. **Linear scaling of context with device count.** Ring Attention enables context length to scale linearly with the number of devices by distributing sequences in a ring topology with overlapped communication. On N devices, if BPT achieves context length s, Ring Attention achieves context length Ns (Section 5.1).

2. **Zero communication overhead through computation overlap.** By leveraging the permutation invariance of blockwise attention's inner loop, Ring Attention pipelines KV block transfers with blockwise computation. When block size exceeds FLOPS/Bandwidth ratio, communication is fully hidden (Section 3).

3. **Memory independent of sequence length.** Ring Attention's activation memory (6bch per layer) depends only on block size c, not sequence length s. This eliminates the fundamental memory bottleneck of storing full layer outputs (Table 1).

4. **Practical demonstration at scale.** Experiments demonstrate training with over 16 million tokens on TPUv4-1024 and over 4 million tokens on 32x A100, representing 256x--512x improvement over prior memory-efficient methods (Table 3).

5. **Downstream task improvements from longer context.** Both in-context RL (ExoRL) and LLM retrieval tasks show improved performance when models can condition on longer sequences enabled by Ring Attention (Table 5, Figure 3).

### Implications

1. **Near-infinite context becomes feasible.** By removing the single-device memory bottleneck, context length is limited only by the number of available devices and training budget, not by memory capacity. [Inference: this enables new applications requiring very long context, such as processing entire codebases, long videos, or scientific datasets.]

2. **Exact attention remains competitive.** Ring Attention achieves extreme context lengths without approximating attention, suggesting that the practical context-length limitations of exact attention are primarily memory constraints rather than computational ones.

3. **Communication-computation overlap is the key enabler.** The critical insight is not distributing sequences per se (prior sequence parallelism does this), but overlapping the communication with blockwise computation. This design pattern may generalize to other distributed computation challenges.

---

## Key Claims

1. **C1: Linear scaling with device count.** Ring Attention enables training sequences up to device count times longer than prior memory-efficient Transformers. On 8x A100, this is 8x improvement (256K vs 32K for 7B); on TPUv4-1024, this is 512x (8,192K vs 16K for 7B) (Table 3, Section 5.1). Status: **supported**.

2. **C2: Zero communication overhead.** When block size c ≥ F/B, communication of KV blocks is fully overlapped with blockwise attention computation. MFU measurements confirm negligible overhead (Table 4, Section 5.2). Status: **supported**.

3. **C3: Memory scales with block size, not sequence length.** Ring Attention requires 6bch bytes of activation per layer, independent of sequence length s, compared to 2bhs² for vanilla Transformers (Table 1, Section 3). Status: **supported**.

4. **C4: Training at 100M+ tokens.** Ring Attention enables training sequences exceeding 100 million tokens without approximations (Figure 1, Section 1). The paper demonstrates 16M+ on TPUv4-1024; extrapolation to 100M+ is based on linear scaling with device count. Status: **supported** (demonstrated at 16M, extrapolated to 100M).

5. **C5: MFU maintained at longer context.** Ring Attention achieves MFU comparable to BPT baselines while training with 8x--128x longer context across 7B--65B models (Table 4, Section 5.2). Status: **supported**.

---

## Open Questions

1. **How does Ring Attention interact with other parallelism strategies?** The paper combines Ring Attention with FSDP; interaction with tensor parallelism is mentioned but not systematically evaluated. Optimal combinations of data/tensor/pipeline/sequence parallelism remain underexplored.

2. **What is the effective utilization of very long context?** While Ring Attention enables training at 16M+ tokens, it is unclear whether current architectures can effectively utilize information across such long distances. Evaluation is limited to 512K tokens.

3. **Can Ring Attention be combined with sparse attention?** For applications where full attention is not necessary, combining Ring Attention's distribution strategy with sparse patterns (e.g., Longformer's local+global) could further extend practical context limits.

4. **How does performance scale with heterogeneous interconnects?** Real-world clusters often have non-uniform bandwidth; the optimal ring topology and block size selection in such settings is not addressed.

---

## Core References and Why They Are Referenced

### Memory-Efficient Attention Foundations

- **Rabe & Staats (2021)** -- *Self-Attention Does Not Need O(n²) Memory.* Foundational work showing attention can be computed without materializing the full attention matrix using the online softmax technique. Ring Attention builds on this for local blockwise computation.

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* Efficient CUDA implementation of memory-efficient attention. Ring Attention is compatible with FlashAttention for local computation on each host.

- **Liu & Abbeel (2023)** -- *Blockwise Parallel Transformer for Large Context Models.* Direct predecessor: computes both attention and feedforward block-by-block, reducing activation memory to 2bsh. Ring Attention extends BPT to distribute across devices.

### Parallelism and Distributed Training

- **Li et al. (2023)** -- *Sequence Parallelism: Long Sequence Training from System Perspective.* Prior work on sequence parallelism using ring topology for attention. Ring Attention differs by using blockwise computation to achieve zero communication overhead, whereas prior ring-based approaches incur non-overlapped communication costs.

- **Jacobs et al. (2023)** -- *DeepSpeed Ulysses: System Optimizations for Enabling Training of Extreme Long Sequence Transformer Models.* Concurrent work on long sequence training. Achieves reduced communication via optimized all-to-all topology but requires gathering full sequence on each device and is restricted by number of attention heads.

### Models and Architectures

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture whose O(n²) attention complexity Ring Attention addresses. Ring Attention preserves exact attention computation while enabling distribution.

- **Touvron et al. (2023)** -- *LLaMA: Open and Efficient Foundation Language Models.* Model architecture used for all experiments (3B, 7B, 13B, 30B sizes).

### Evaluation

- **Li et al. (2023)** -- *How Long Can Open-Source LLMs Truly Promise on Context Length?* Provides the line retrieval test used to evaluate long-context retrieval capability.

- **Yarats et al. (2022)** -- *ExoRL: Don't Change the Algorithm, Change the Data.* Provides the ExoRL benchmark for evaluating in-context reinforcement learning with diverse exploratory data.
