---
title: "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness"
authors: "Dao, Fu, Ermon, Rudra, Ré"
year: 2022
venue: "NeurIPS 2022"
paper_type: "conference-paper"
categories: ["attention-efficiency", "architecture"]
scope: ["exact attention", "GPU memory optimization", "training efficiency"]
benchmarks_used: ["lra"]
models_introduced: []
models_evaluated: ["BERT-large", "GPT-2"]
key_claims:
  - id: C1
    claim: "Standard attention is memory-bound: memory accesses, not FLOPs, determine runtime"
    evidence: "Section 2.1, Figure 2 left (HBM R/W dominates runtime)"
    status: supported
  - id: C2
    claim: "FlashAttention requires O(N²d²M⁻¹) HBM accesses compared to Θ(Nd + N²) for standard attention"
    evidence: "Theorem 2, Section 3.2"
    status: supported
  - id: C3
    claim: "FlashAttention is optimal: no exact attention algorithm can asymptotically improve on HBM accesses"
    evidence: "Proposition 3, proof in Appendix C"
    status: supported
  - id: C4
    claim: "FlashAttention trains BERT-large 15% faster than the MLPerf 1.1 speed record"
    evidence: "Table 1: 17.4 ± 1.4 min vs 20.0 ± 1.5 min on 8×A100 GPUs"
    status: supported
  - id: C5
    claim: "FlashAttention achieves up to 3× speedup on GPT-2 training over HuggingFace baseline"
    evidence: "Table 2: GPT-2 small 3.5×, GPT-2 medium 3.0× speedup"
    status: supported
  - id: C6
    claim: "FlashAttention memory scales linearly with sequence length, up to 20× more efficient than standard attention"
    evidence: "Figure 3 right, Table 21"
    status: supported
  - id: C7
    claim: "FlashAttention enables the first Transformer to achieve better-than-chance on Path-X (16K) and Path-256 (64K)"
    evidence: "Table 6: 61.4% on Path-X, 63.1% on Path-256 (chance is 50%)"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Provides an IO-aware implementation of the standard Transformer attention mechanism"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer uses sparse attention patterns; FlashAttention provides an efficient exact attention primitive that can be combined with sparsity"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "ALiBi addresses length extrapolation through position encoding; FlashAttention addresses computational efficiency of attention"
  - target: 2024-05-flashattention-2
    type: extended-by
    detail: "FlashAttention-2 improves GPU utilization from 25-40% to 50-73% through better parallelism and work partitioning"
  - target: 2024-05-ring-attention-near-infinite-context
    type: extended-by
    detail: "Ring Attention builds on memory-efficient attention techniques, using blockwise computation locally on each host and overlapping inter-host KV communication to enable context lengths scaling with device count"
  - target: 2024-12-flashattention-3
    type: extended-by
    detail: "FlashAttention-3 achieves 75% H100 utilization through warp-specialized asynchrony, GEMM-softmax pipelining, and FP8 low-precision support"
  - target: 2024-05-mamba-selective-state-spaces
    type: complementary
    detail: "Mamba (co-authored by Tri Dao) proposes an alternative to attention entirely using selective SSMs; both address Transformer efficiency but FlashAttention optimizes exact attention IO while Mamba eliminates quadratic attention altogether"
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: complementary
    detail: "RWKV achieves linear time and constant memory by replacing attention with channel-wise time decay; FlashAttention retains quadratic time but makes exact attention IO-efficient"
  - target: 2023-07-retnet-retentive-network
    type: complementary
    detail: "RetNet compares training efficiency against FlashAttention-optimized Transformers, claiming competitive throughput with vanilla PyTorch; both address Transformer efficiency but from opposite directions"
  - target: 2025-04-differential-transformer
    type: complementary
    detail: "DIFF Transformer provides a FlashAttention-compatible implementation of its differential attention mechanism, leveraging FlashAttention's IO-aware tiling for efficient training and inference"
open_questions:
  - question: "How can FlashAttention be extended to multi-GPU settings with efficient inter-GPU communication?"
    addressed_by: null
  - question: "Can the IO-aware approach be compiled from high-level code rather than requiring custom CUDA kernels?"
    addressed_by: null
  - question: "How do the benefits scale to even larger models (10B+ parameters)?"
    addressed_by: null
  - question: "Can GPU utilization be improved beyond 25-40% of theoretical maximum?"
    addressed_by: 2024-05-flashattention-2
---
# FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

**Authors:** Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré (Stanford University, University at Buffalo)
**Date:** December 2022, NeurIPS 2022 (arXiv:2205.14135)

---

## Core Research Problem

Transformers have become the dominant architecture in NLP and vision, but their self-attention mechanism has time and memory complexity quadratic in sequence length, making long sequences prohibitively expensive. Many approximate attention methods (sparse, low-rank, or combinations) have been proposed to reduce compute complexity to linear or near-linear, but they often fail to achieve wall-clock speedup against standard attention.

The authors identify a missing principle: **IO-awareness**. Existing methods focus on reducing FLOPs, but on modern GPUs, compute speed has outpaced memory speed, making most Transformer operations **memory-bound** rather than compute-bound. The bottleneck is reading and writing data between different levels of the GPU memory hierarchy:

- **GPU SRAM (on-chip):** ~19 TB/s bandwidth, ~20 MB size (A100)
- **GPU HBM (high bandwidth memory):** ~1.5 TB/s bandwidth, 40-80 GB size (A100)

Standard attention implementations materialize the N×N attention matrix S and P to HBM, requiring O(N²) memory accesses. For typical models where N >> d (e.g., GPT-2 with N=1024, d=64), this dominates runtime.

**The core challenge is: computing exact attention with sub-quadratic HBM accesses while maintaining numerical correctness and supporting the backward pass for training.**

---

## Problem Solutions

The paper introduces **FlashAttention**, an IO-aware exact attention algorithm with two key techniques:

1. **Tiling.** Split the inputs Q, K, V into blocks that fit in SRAM. Compute attention output incrementally by maintaining running statistics (max and sum) for the softmax normalization. This avoids materializing the full N×N attention matrix.

2. **Recomputation.** Instead of storing the O(N²) attention matrix for the backward pass, store only the output O and softmax normalization statistics (m, ℓ). Recompute the attention matrix on-the-fly during the backward pass from blocks of Q, K, V in SRAM. Despite more FLOPs, this is faster due to reduced HBM access.

---

## Approach Details

### Method

Standard attention computes:

> S = QK^T ∈ R^(N×N), P = softmax(S) ∈ R^(N×N), O = PV ∈ R^(N×d)

where softmax is applied row-wise. Standard implementations write S and P to HBM.

FlashAttention restructures this computation to avoid materializing S and P. The key insight is that softmax can be decomposed across blocks using the identity:

> m(x) = max_i x_i, f(x) = [e^(x_1-m(x)) ... e^(x_B-m(x))], ℓ(x) = Σ_i f(x)_i, softmax(x) = f(x)/ℓ(x)

For concatenated vectors x = [x^(1) x^(2)]:

> m(x) = max(m(x^(1)), m(x^(2)))
> ℓ(x) = e^(m(x^(1))-m(x)) ℓ(x^(1)) + e^(m(x^(2))-m(x)) ℓ(x^(2))

By tracking statistics (m, ℓ), softmax can be computed one block at a time.

### Key Technical Components

**Block sizes.** Given SRAM size M:

> B_c = ⌈M/4d⌉, B_r = min(⌈M/4d⌉, d)

These ensure blocks of K, V (size B_c × d) and Q, O (size B_r × d) and S (size B_r × B_c) fit in SRAM.

**Algorithm structure (forward pass).** The outer loop iterates over K, V blocks (index j). The inner loop iterates over Q blocks (index i). For each (i,j) pair:
1. Load K_j, V_j, Q_i, O_i, ℓ_i, m_i from HBM to SRAM
2. Compute S_ij = Q_i K_j^T on chip
3. Compute local softmax statistics m̃_ij, P̃_ij, ℓ̃_ij
4. Update global statistics: m_i^new = max(m_i, m̃_ij), ℓ_i^new = e^(m_i-m_i^new) ℓ_i + e^(m̃_ij-m_i^new) ℓ̃_ij
5. Update output: O_i ← diag(ℓ_i^new)^(-1) (diag(ℓ_i) e^(m_i-m_i^new) O_i + e^(m̃_ij-m_i^new) P̃_ij V_j)
6. Write O_i, ℓ_i, m_i back to HBM

**Backward pass.** Store only O, ℓ, m (and PRNG state for dropout). Recompute S_ij and P_ij from Q_i, K_j during backward. Use the identity D_i = P_i:^T dP_i: = do_i^T o_i to avoid reducing over vectors of size N.

**Kernel fusion.** All operations (matrix multiply, softmax, masking, dropout) are fused into a single CUDA kernel, avoiding repeated HBM reads/writes.

### Theoretical Analysis

**IO complexity (Theorem 2).** Let N be sequence length, d be head dimension, M be SRAM size with d ≤ M ≤ Nd:
- Standard attention: Θ(Nd + N²) HBM accesses
- FlashAttention: Θ(N²d²M^(-1)) HBM accesses

For typical values (d=64-128, M≈100KB), d² << M, so FlashAttention requires many times fewer HBM accesses.

**Lower bound (Proposition 3).** No exact attention algorithm can achieve o(N²d²M^(-1)) HBM accesses for all M ∈ [d, Nd]. FlashAttention is asymptotically optimal.

**Memory requirement (Theorem 1).** FlashAttention requires O(N) additional memory beyond inputs and output (for storing ℓ and m), compared to O(N²) for standard attention.

### Extension: Block-Sparse FlashAttention

Given a block sparsity mask M ∈ {0,1}^((N/B_r)×(N/B_c)), skip zero blocks in the algorithm. IO complexity becomes:

> Θ(Nd + N²d²M^(-1)s)

where s is the fraction of nonzero blocks. For large N, typical sparsity patterns use s = N^(-1/2) or s = N^(-1) log N, yielding O(N√N) or O(N log N) complexity.

### Experimental Setup

**BERT-large training.** 16 layers, 1024 hidden, 16 heads, 340M parameters. Wikipedia dataset. LAMB optimizer, lr=3.75e-3, batch size 448, trained until 72.0% validation accuracy on masked LM. 8×A100-80GB GPUs.

**GPT-2 training.** Small (117M) and medium (345M) models. OpenWebText dataset. AdamW optimizer, lr=6e-4 (small) / 1.5e-4 (medium), effective batch size 512, 400K steps. 8×A100-40GB GPUs.

**Long-Range Arena (LRA).** Five tasks with sequence lengths 1K-4K: ListOps, Text, Retrieval, Image, Pathfinder. Follow hyperparameters from Tay et al. (2020) and Xiong et al. (2021).

**Long document classification.** MIMIC-III (medical discharge summaries, avg 2,395 tokens) and ECtHR (legal cases, avg 2,197 tokens). Fine-tune pretrained RoBERTa with repeated positional embeddings.

**Path-X and Path-256.** Classify whether two points in 128×128 (Path-X, 16K tokens) or 256×256 (Path-256, 64K tokens) images are connected. Pretrain on Path-64, transfer with interpolated positional embeddings.

### Key Results

**Training speed:**

| Model | Implementation | Time | Speedup |
|-------|----------------|------|---------|
| BERT-large | Nvidia MLPerf 1.1 | 20.0 ± 1.5 min | 1.0× |
| BERT-large | FlashAttention | 17.4 ± 1.4 min | 1.15× |
| GPT-2 small | HuggingFace | 9.5 days | 1.0× |
| GPT-2 small | Megatron-LM | 4.7 days | 2.0× |
| GPT-2 small | FlashAttention | 2.7 days | 3.5× |
| GPT-2 medium | HuggingFace | 21.0 days | 1.0× |
| GPT-2 medium | Megatron-LM | 11.5 days | 1.8× |
| GPT-2 medium | FlashAttention | 6.9 days | 3.0× |

**Long-Range Arena (accuracy):**

| Model | ListOps | Text | Retrieval | Image | Pathfinder | Avg | Speedup |
|-------|---------|------|-----------|-------|------------|-----|---------|
| Transformer | 36.0 | 63.6 | 81.6 | 42.3 | 72.7 | 59.3 | - |
| FlashAttention | 37.6 | 63.9 | 81.4 | 43.5 | 72.7 | 59.8 | 2.4× |
| Block-sparse FlashAttention | 37.0 | 63.0 | 81.3 | 43.6 | 73.3 | 59.6 | 2.8× |
| Linformer | 35.6 | 55.9 | 77.7 | 37.8 | 67.6 | 54.9 | 2.5× |
| Performer | 36.8 | 63.6 | 82.2 | 42.1 | 69.9 | 58.9 | 1.8× |

FlashAttention matches or exceeds standard attention accuracy while being 2.4× faster.

**Longer context quality (GPT-2 small on OpenWebText):**

| Context length | Perplexity | Training time |
|----------------|------------|---------------|
| 1K (Megatron) | 18.2 | 4.7 days |
| 1K (FlashAttention) | 18.2 | 2.7 days |
| 2K (FlashAttention) | 17.6 | 3.0 days |
| 4K (FlashAttention) | 17.5 | 3.6 days |

GPT-2 with 4K context is 30% faster than Megatron with 1K context while achieving 0.7 better perplexity.

**Long document classification (micro-F1):**

| Sequence length | 512 | 1024 | 2048 | 4096 | 8192 | 16384 |
|-----------------|-----|------|------|------|------|-------|
| MIMIC-III | 52.8 | 50.7 | 51.7 | 54.6 | 56.4 | 57.1 |
| ECtHR | 72.2 | 74.3 | 77.1 | 78.6 | 80.7 | 79.2 |

Longer sequences yield +4.3 points on MIMIC-III and +8.5 points on ECtHR.

**Path-X and Path-256 (first Transformer to solve):**

| Model | Path-X (16K) | Path-256 (64K) |
|-------|--------------|----------------|
| Transformer (standard) | ✗ | ✗ |
| All approximate methods | ✗ | ✗ |
| FlashAttention | 61.4% | ✗ |
| Block-sparse FlashAttention | 56.0% | 63.1% |

(Chance is 50%; ✗ indicates OOM or random performance)

**Runtime and memory benchmarks (A100, batch 16, 8 heads, d=64):**

FlashAttention is up to 3× faster than PyTorch attention for sequences up to 2K. Memory footprint scales linearly with sequence length—up to 20× more efficient than standard attention (e.g., 836 MB vs 17,024 MB at N=4096).

---

## Limitations and Failure Modes

1. **Requires custom CUDA kernels.** Each attention variant requires reimplementation in CUDA, limiting portability and ease of modification. Not transferable across GPU architectures without adaptation.

2. **Head dimension constraints.** Current implementation supports head dimensions 16, 32, 64, 128. Other dimensions would require additional kernel implementations.

3. **Not always faster at short sequences.** At sequence length 128, FlashAttention's overhead can make it comparable to or slightly slower than optimized baselines like Apex FMHA (Table 7).

4. **Single-GPU optimization.** The IO analysis is for a single GPU. Multi-GPU settings introduce inter-GPU communication that adds another memory hierarchy level.

5. **Approximate methods eventually cross over.** For sequences beyond 1K, some approximate methods (Linformer) start to become faster in raw runtime, though they sacrifice exactness.

6. **Block-sparse patterns fixed.** The sparsity pattern must be determined before training. Dynamic or content-dependent sparsity is not supported.

---

## Conclusions

### Contributions

1. **IO-aware attention.** First to argue that memory access, not FLOPs, is the bottleneck for attention and to design an algorithm optimized for IO complexity.

2. **Asymptotically optimal algorithm.** FlashAttention achieves O(N²d²M^(-1)) HBM accesses and proves this is optimal for exact attention.

3. **Practical speedups.** Demonstrates 2-4× wall-clock speedup on real training tasks (BERT, GPT-2, LRA) while maintaining exact computation.

4. **Linear memory footprint.** Reduces memory from O(N²) to O(N), enabling much longer sequences (up to 64K tokens demonstrated).

5. **Enabling longer context.** The memory and speed efficiency enables training with longer sequences, improving quality (0.7 perplexity on GPT-2, 6.4 points on document classification).

6. **First Path-X/Path-256 solutions.** Enables the first Transformer models to achieve better-than-chance on these long-range benchmarks.

### Implications

1. **IO-awareness as a design principle.** The success of FlashAttention suggests that future algorithm design should consider memory hierarchy, not just FLOP counts.

2. **Exact vs. approximate attention.** FlashAttention shows that exact attention can be made efficient enough to be competitive with or faster than approximate methods for many sequence lengths, questioning the need for approximations at moderate lengths.

3. **Foundation for longer context.** By reducing the memory bottleneck, FlashAttention opens the path for training with much longer contexts, which subsequent work has built upon.

---

## Key Claims

**C1. Attention is memory-bound.** The runtime of standard attention is determined by HBM accesses (40.3 GB) rather than compute (66.6 GFLOPs). FlashAttention reduces HBM accesses to 4.4 GB, achieving 7.3 ms runtime vs 41.7 ms (Figure 2 left). Status: **supported**.

**C2. IO complexity reduction.** Standard attention: Θ(Nd + N²) HBM accesses. FlashAttention: Θ(N²d²M^(-1)) HBM accesses. For d=64, M=100KB, this is up to 9× fewer accesses (Theorem 2, Figure 2). Status: **supported**.

**C3. Optimality.** No exact attention algorithm can asymptotically improve on O(N²d²M^(-1)) HBM accesses for all SRAM sizes (Proposition 3). Status: **supported**.

**C4. BERT training speedup.** FlashAttention trains BERT-large to 72% validation accuracy in 17.4 ± 1.4 minutes vs Nvidia's MLPerf 1.1 record of 20.0 ± 1.5 minutes, a 15% improvement (Table 1). Status: **supported**.

**C5. GPT-2 training speedup.** Up to 3.5× speedup over HuggingFace (GPT-2 small: 2.7 vs 9.5 days) and 1.7-2× over Megatron (Table 2). Status: **supported**.

**C6. Linear memory scaling.** Memory footprint grows linearly with sequence length: 209 MB at N=1024, 836 MB at N=4096, 13,376 MB at N=65536. Standard attention would require 1,184 MB, 17,024 MB, and OOM respectively (Table 21). Status: **supported**.

**C7. Path-X and Path-256 first solutions.** FlashAttention achieves 61.4% on Path-X (16K sequence), block-sparse FlashAttention achieves 63.1% on Path-256 (64K sequence). All prior Transformers achieved random performance or OOM (Table 6). Status: **supported**.

---

## Open Questions

1. **Multi-GPU IO-aware methods.** How can the IO-aware approach extend to multi-GPU training with efficient inter-GPU communication? The current analysis is optimal for single-GPU.

2. **Compilation from high-level code.** Can attention algorithms be written in PyTorch and automatically compiled to IO-aware CUDA implementations, similar to Halide for image processing?

3. **Scaling to larger models.** How do the benefits of FlashAttention scale to 10B+ parameter models with different attention dynamics?

4. **Dynamic sparsity.** Can the block-sparse extension support content-dependent or learned sparsity patterns rather than fixed patterns?

---

## Core References and Why They Are Referenced

### Hardware and IO Complexity Foundations

- **Aggarwal & Vitter (1988)** -- *The Input/Output Complexity of Sorting.* Foundational work on IO complexity analysis that FlashAttention builds upon.
- **Williams et al. (2009)** -- *Roofline: An Insightful Visual Performance Model.* Introduces arithmetic intensity as the key metric for compute-bound vs memory-bound operations.

### Transformer and Attention

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer architecture and standard attention that FlashAttention optimizes.
- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers.* BERT-large is a key benchmark for training speedup.
- **Radford et al. (2019)** -- *Language Models Are Unsupervised Multitask Learners (GPT-2).* GPT-2 is a key benchmark for training speedup and quality.

### Efficient Attention Methods (Baselines)

- **Kitaev et al. (2020)** -- *Reformer: The Efficient Transformer.* Sparse attention via locality-sensitive hashing; used as baseline.
- **Choromanski et al. (2020)** -- *Rethinking Attention with Performers.* Low-rank attention approximation; used as baseline.
- **Wang et al. (2020)** -- *Linformer: Self-Attention with Linear Complexity.* Low-rank projection of keys and values; used as baseline.
- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Sparse attention with local + global patterns; used as baseline.
- **Zaheer et al. (2020)** -- *Big Bird: Transformers for Longer Sequences.* Combines sparse patterns; used as baseline.
- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Block-sparse attention; inspiration for block-sparse FlashAttention.

### Memory-Efficient Attention

- **Rabe & Staats (2021)** -- *Self-Attention Does Not Need O(n²) Memory.* Shows attention can be computed with O(n) memory using tiling/recomputation. FlashAttention builds on this but focuses on reducing IO, achieving faster runtime rather than just memory reduction.
- **Milakov & Gimelshein (2018)** -- *Online Normalizer Calculation for Softmax.* Technique for computing softmax incrementally that FlashAttention uses.

### Benchmarks

- **Tay et al. (2020)** -- *Long Range Arena: A Benchmark for Efficient Transformers.* Provides the LRA benchmark including Path-X.
- **Mattson et al. (2020)** -- *MLPerf Training Benchmark.* BERT training benchmark that FlashAttention beats by 15%.
