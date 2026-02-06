---
title: "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning"
authors: "Dao"
year: 2024
venue: "ICLR 2024"
paper_type: "conference-paper"
categories: ["attention-efficiency", "architecture"]
scope: ["exact attention", "GPU optimization", "training efficiency", "work partitioning"]
benchmarks_used: []
models_introduced: []
models_evaluated: ["GPT-2"]
key_claims:
  - id: C1
    claim: "FlashAttention achieves only 25-40% of theoretical maximum FLOPs/s due to suboptimal work partitioning between thread blocks and warps"
    evidence: "Section 1, Figure 5, Figure 6"
    status: supported
  - id: C2
    claim: "FlashAttention-2 achieves 2× speedup over FlashAttention by reducing non-matmul FLOPs, parallelizing over sequence length, and improving warp-level work partitioning"
    evidence: "Section 4.1, Figures 4-6"
    status: supported
  - id: C3
    claim: "FlashAttention-2 reaches 50-73% of theoretical maximum FLOPs/s on A100, approaching GEMM efficiency"
    evidence: "Abstract, Section 4.1: up to 230 TFLOPs/s forward pass"
    status: supported
  - id: C4
    claim: "Non-matmul FLOPs are 16× more expensive than matmul FLOPs on modern GPUs due to specialized compute units (Tensor Cores)"
    evidence: "Section 3.1: A100 has 312 TFLOPs/s matmul vs 19.5 TFLOPs/s non-matmul"
    status: supported
  - id: C5
    claim: "FlashAttention-2 achieves up to 225 TFLOPs/s per A100 GPU (72% model FLOPs utilization) for end-to-end GPT training"
    evidence: "Table 1: GPT3-2.7B 8k context"
    status: supported
  - id: C6
    claim: "Parallelizing over sequence length dimension increases occupancy for long sequences with small batch sizes"
    evidence: "Section 3.2"
    status: supported
  - id: C7
    claim: "Avoiding the 'split-K' warp partitioning scheme reduces shared memory reads/writes and yields speedup"
    evidence: "Section 3.3, Figure 3"
    status: supported
cross_references:
  - target: 2022-12-flashattention
    type: extends
    detail: "Direct follow-up that improves GPU utilization from 25-40% to 50-73% through better parallelism and work partitioning"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Provides a highly optimized implementation of the standard Transformer attention mechanism"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer uses sparse attention patterns; FlashAttention-2 provides an efficient exact attention primitive"
  - target: 2020-12-bigbird-sparse-attention
    type: complementary
    detail: "BigBird uses sparse attention; FlashAttention-2 makes exact attention competitive for moderate lengths"
  - target: 2024-12-flashattention-3
    type: extended-by
    detail: "FlashAttention-3 improves H100 utilization from 35% to 75% through warp-specialized asynchrony, GEMM-softmax pipelining, and FP8 low-precision"
open_questions:
  - question: "Can H100-specific optimizations (TMA, 4th-gen Tensor Cores, FP8) provide an additional 1.5-2× speedup?"
    addressed_by: 2024-12-flashattention-3
  - question: "Can auto-tuning replace manual block size selection across different head dimensions?"
    addressed_by: null
  - question: "How can FlashAttention-2 be combined with high-level algorithmic changes (local, dilated, block-sparse attention) for even longer contexts?"
    addressed_by: null
---
# FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning

**Authors:** Tri Dao (Princeton University, Stanford University)
**Date:** May 2024, ICLR 2024 (arXiv:2307.08691)

---

## Core Research Problem

FlashAttention (Dao et al., 2022) introduced IO-aware attention that reduces memory reads/writes and achieves 2-4× speedup over standard attention implementations. However, FlashAttention still achieves only **25-40% of the theoretical maximum FLOPs/s** on A100 GPUs, while optimized matrix-multiply (GEMM) operations can reach 80-90%.

Through profiling, the author identifies the root cause: **suboptimal work partitioning** between different thread blocks and warps on the GPU. This causes either:
1. **Low occupancy** (underutilization of GPU streaming multiprocessors)
2. **Unnecessary shared memory reads/writes** (communication overhead between warps)

**The core challenge is: how to partition attention computation across thread blocks and warps to maximize GPU utilization while maintaining the IO-aware properties of FlashAttention.**

---

## Problem Solutions

FlashAttention-2 introduces three key optimizations:

1. **Reduce non-matmul FLOPs.** Since Tensor Cores provide 16× higher throughput for matmul (312 TFLOPs/s) than non-matmul operations (19.5 TFLOPs/s), minimize time spent on non-matmul operations.

2. **Parallelize over sequence length.** In addition to parallelizing over batch and heads, parallelize over the sequence length dimension to increase occupancy when sequences are long (and batch sizes small).

3. **Better warp-level work partitioning.** Avoid the "split-K" scheme that requires inter-warp communication through shared memory. Instead, partition Q across warps while keeping K and V shared.

---

## Approach Details

### Method

Standard attention computes:

> S = QK^T ∈ R^(N×N), P = softmax(S) ∈ R^(N×N), O = PV ∈ R^(N×d)

FlashAttention-2 maintains the same tiling and recomputation approach as FlashAttention, but optimizes the implementation.

### Key Technical Components

#### 1. Algorithm Tweaks to Reduce Non-Matmul FLOPs

**Observation:** On A100, matmul throughput is 312 TFLOPs/s while non-matmul FP32 throughput is only 19.5 TFLOPs/s. Each non-matmul FLOP is effectively **16× more expensive** than a matmul FLOP.

**Tweak 1: Delayed scaling.** Instead of rescaling both terms of the output update at each iteration:

> O^(2) = diag(ℓ^(1)/ℓ^(2))^(-1) O^(1) + diag(ℓ^(2))^(-1) e^(S^(2)-m^(2)) V^(2)

Maintain an "un-scaled" version and only scale once at the end:

> Õ^(2) = diag(e^(m^(1)-m^(2)))^(-1) Õ^(1) + e^(S^(2)-m^(2)) V^(2)
> O = diag(ℓ^(last))^(-1) Õ^(last)

**Tweak 2: Store only logsumexp.** Instead of saving both max m^(j) and sum of exponentials ℓ^(j) for the backward pass, store only the logsumexp:

> L^(j) = m^(j) + log(ℓ^(j))

#### 2. Parallelization Strategy

**FlashAttention (original):** Parallelizes over batch size and number of heads. One thread block processes one attention head.

**FlashAttention-2:** Additionally parallelizes over the **sequence length dimension**.

**Forward pass:** The outer loop (over row blocks of Q) is embarrassingly parallel. Different row blocks are scheduled on different thread blocks with no inter-block communication needed.

**Backward pass:** Parallelize over column blocks. The only shared computation is updating dQ, which uses **atomic adds** for inter-block communication.

**Impact:** When batch size × number of heads < 108 (number of SMs on A100), parallelizing over sequence length improves occupancy.

#### 3. Warp-Level Work Partitioning

**FlashAttention (original) "split-K" scheme:**
- Split K and V across 4 warps
- Each warp computes a slice of QK^T
- Warps must communicate through shared memory to combine results

**FlashAttention-2 scheme:**
- Split Q across 4 warps
- Keep K and V accessible by all warps
- Each warp computes its slice of QK^T and multiplies with shared V
- **No inter-warp communication needed**

**Result:** Reduced shared memory reads/writes yield speedup.

#### 4. Causal Masking Optimizations

1. **Skip zero blocks:** For blocks where all column indices exceed row indices (approximately half the blocks), skip computation entirely. Yields 1.7-1.8× speedup over non-causal attention.

2. **Selective masking:** Only apply causal mask to blocks on the diagonal (where row and column indices overlap). Other blocks either computed fully or skipped entirely.

#### 5. Block Size Tuning

Block sizes typically {64, 128} × {64, 128}, depending on head dimension d and device shared memory size.

Constraints:
- Larger blocks reduce shared memory loads/stores
- Too large blocks cause register spilling or exceed shared memory capacity
- Currently tuned manually per head dimension (16, 32, 64, 128)

### Theoretical Analysis

**Correctness:** FlashAttention-2 returns the exact same output as standard attention O = softmax(QK^T)V with no approximation.

**FLOPs:** O(N²d) FLOPs, same as FlashAttention.

**Memory:** O(N) additional memory beyond inputs and output (for storing logsumexp L).

### Support for Attention Variants

**Multi-query attention (MQA) and grouped-query attention (GQA):** Multiple query heads attend to the same K/V head. FlashAttention-2 handles this by manipulating indices rather than duplicating K/V. In backward pass, gradients dK and dV are summed across duplicated heads.

### Experimental Setup

**Attention benchmarks:**
- A100 80GB SXM4 GPU
- Sequence lengths: 512, 1K, 2K, 4K, 8K, 16K
- Batch size: set so total tokens = 16K
- Hidden dimension: 2048
- Head dimensions: 64 or 128 (32 or 16 heads)

**End-to-end training:**
- GPT-style models: 1.3B and 2.7B parameters
- Context lengths: 2K and 8K
- Hardware: 8×A100 80GB SXM

**FLOPs calculation:**
- Forward pass: 4 × seqlen² × head_dim × num_heads
- Backward pass: 2.5 × forward FLOPs (5 matmuls vs 2)
- With causal mask: divide by 2

### Key Results

**Attention kernel benchmarks (A100):**

| Setting | FlashAttention | FlashAttention-2 | Speedup |
|---------|----------------|------------------|---------|
| Forward, no causal, d=64, 16K | 104 TFLOPs/s | 192 TFLOPs/s | 1.8× |
| Forward, no causal, d=128, 16K | 73 TFLOPs/s | 223 TFLOPs/s | 3.1× |
| Forward, causal, d=64, 16K | 94 TFLOPs/s | 183 TFLOPs/s | 1.9× |
| Forward, causal, d=128, 16K | 71 TFLOPs/s | 197 TFLOPs/s | 2.8× |
| Backward, no causal, d=64, 16K | 113 TFLOPs/s | 170 TFLOPs/s | 1.5× |
| Backward, no causal, d=128, 16K | 88 TFLOPs/s | 196 TFLOPs/s | 2.2× |
| Backward, causal, d=64, 16K | 98 TFLOPs/s | 166 TFLOPs/s | 1.7× |
| Backward, causal, d=128, 16K | 89 TFLOPs/s | 186 TFLOPs/s | 2.1× |

FlashAttention-2 reaches up to **230 TFLOPs/s (73% of theoretical max)** on A100.

**Comparison with other implementations (forward + backward, A100):**

| Implementation | Speedup vs PyTorch |
|----------------|-------------------|
| PyTorch (standard) | 1.0× |
| FlashAttention | 2-3× |
| xformers (cutlass) | 2-3× |
| FlashAttention Triton | 2-3× |
| FlashAttention-2 | **3-10×** |

**End-to-end GPT training (8×A100):**

| Model | Without FlashAttention | FlashAttention | FlashAttention-2 |
|-------|------------------------|----------------|------------------|
| GPT3-1.3B 2K context | 142 TFLOPs/s | 189 TFLOPs/s | 196 TFLOPs/s |
| GPT3-1.3B 8K context | 72 TFLOPs/s | 170 TFLOPs/s | 220 TFLOPs/s |
| GPT3-2.7B 2K context | 149 TFLOPs/s | 189 TFLOPs/s | 205 TFLOPs/s |
| GPT3-2.7B 8K context | 80 TFLOPs/s | 175 TFLOPs/s | **225 TFLOPs/s** |

FlashAttention-2 achieves **72% model FLOPs utilization** (225 TFLOPs/s per A100).

**H100 GPU results:**
- Without H100-specific optimizations, FlashAttention-2 reaches up to **335 TFLOPs/s**
- Expected 1.5-2× additional speedup with TMA, 4th-gen Tensor Cores, FP8

---

## Limitations and Failure Modes

1. **Requires custom CUDA kernels.** Each attention variant requires reimplementation in CUDA, limiting portability.

2. **Manual block size tuning.** Block sizes must be tuned per head dimension. Auto-tuning would reduce this manual labor.

3. **Head dimension constraints.** Supports head dimensions 16, 32, 64, 128. Other dimensions require additional kernel implementations.

4. **No H100 optimizations yet.** Does not use TMA, 4th-gen Tensor Cores, or FP8 on H100 GPUs.

5. **Single-GPU scope.** Analysis focuses on single-GPU optimization. Multi-GPU settings add inter-GPU communication complexity.

---

## Conclusions

### Contributions

1. **Identified inefficiency source.** Diagnosed that FlashAttention's suboptimal performance (25-40% utilization) stems from work partitioning, not IO complexity.

2. **Algorithm tweaks.** Reduced non-matmul FLOPs through delayed scaling and storing only logsumexp.

3. **Sequence-length parallelism.** Added parallelization over sequence length to improve occupancy for long sequences.

4. **Warp partitioning.** Replaced "split-K" scheme with Q-splitting to eliminate inter-warp communication.

5. **2× speedup.** Achieved 2× speedup over FlashAttention, reaching 50-73% of theoretical maximum throughput.

6. **72% model utilization.** Demonstrated 225 TFLOPs/s (72% MFU) for end-to-end GPT training.

### Implications

1. **Longer context at same cost.** 2× speedup means training 16K context models at the cost of 8K context models.

2. **Approaching GEMM efficiency.** At 73% utilization, attention is no longer as far behind GEMM (80-90%), reducing the incentive for approximate attention methods at moderate sequence lengths.

3. **Foundation for future optimizations.** Identified clear paths for further improvement: H100-specific optimizations, auto-tuning, combination with sparse attention patterns.

---

## Key Claims

**C1. FlashAttention utilization gap.** FlashAttention reaches only 25-40% of theoretical maximum FLOPs/s (forward 30-50%, backward 25-35%), while GEMM reaches 80-90% (Section 1, Figures 5-6). Status: **supported**.

**C2. 2× speedup over FlashAttention.** FlashAttention-2 achieves around 2× speedup through algorithm tweaks, sequence-length parallelism, and better warp partitioning (Section 4.1, Figure 4). Status: **supported**.

**C3. 50-73% theoretical max throughput.** FlashAttention-2 reaches up to 230 TFLOPs/s in forward pass (73% of A100's 312 TFLOPs/s theoretical max) and up to 196 TFLOPs/s in backward pass (63%) (Figures 5-6). Status: **supported**.

**C4. Non-matmul FLOPs 16× more expensive.** A100 provides 312 TFLOPs/s for FP16/BF16 matmul but only 19.5 TFLOPs/s for non-matmul FP32, making each non-matmul FLOP 16× more expensive (Section 3.1). Status: **supported**.

**C5. 72% model FLOPs utilization.** End-to-end GPT-2.7B training with 8K context reaches 225 TFLOPs/s per A100, which is 72% model FLOPs utilization (Table 1). Status: **supported**.

**C6. Sequence-length parallelism improves occupancy.** Parallelizing over sequence length helps when batch × heads < 108 SMs, which occurs for long sequences with small batches (Section 3.2). Status: **supported**.

**C7. Avoiding split-K reduces shared memory overhead.** Partitioning Q instead of K/V across warps eliminates the need for inter-warp communication through shared memory (Section 3.3, Figure 3). Status: **supported**.

---

## Open Questions

1. **H100 optimizations.** Can TMA (Tensor Memory Accelerator), 4th-gen Tensor Cores, and FP8 provide the expected 1.5-2× additional speedup on H100?

2. **Auto-tuning.** Can auto-tuning replace manual block size selection for different head dimensions and GPU architectures?

3. **Combination with sparse attention.** How can FlashAttention-2's low-level optimizations be combined with high-level algorithmic changes (local, dilated, block-sparse attention) for even longer contexts?

4. **Multi-GPU extension.** How should work partitioning be adapted for multi-GPU settings with inter-GPU communication?

---

## Core References and Why They Are Referenced

### FlashAttention Foundations

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* The predecessor paper that FlashAttention-2 directly extends. Introduced IO-aware attention with tiling and recomputation.

- **Rabe & Staats (2021)** -- *Self-Attention Does Not Need O(n²) Memory.* Showed attention can be computed with O(n) memory using tiling. FlashAttention built on this.

- **Milakov & Gimelshein (2018)** -- *Online Normalizer Calculation for Softmax.* Technique for computing softmax incrementally that both FlashAttention and FlashAttention-2 use.

### GPU Architecture and Optimization

- **Jia et al. (2018, 2021)** -- *Dissecting the Nvidia Volta/Ampere GPU Architecture.* Microbenchmarking studies that inform understanding of GPU memory hierarchy and compute throughput.

- **Tillet et al. (2019)** -- *Triton.* The Triton implementation of FlashAttention suggested the loop reordering and sequence-length parallelization that FlashAttention-2 adopts.

### Transformer and Attention

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Original Transformer architecture whose attention mechanism FlashAttention-2 optimizes.

- **Shazeer (2019)** -- *Fast Transformer Decoding: One Write-Head Is All You Need.* Introduced multi-query attention (MQA), which FlashAttention-2 supports.

- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models.* Introduced grouped-query attention (GQA), which FlashAttention-2 supports.

### Efficient Attention Methods (Context)

- **Beltagy et al. (2020)** -- *Longformer.* Sparse attention baseline.
- **Zaheer et al. (2020)** -- *Big Bird.* Sparse attention baseline.
- **Kitaev et al. (2020)** -- *Reformer.* Efficient attention baseline.
- **Choromanski et al. (2020)** -- *Performers.* Linear attention baseline.

### Training Infrastructure

- **Shoeybi et al. (2019)** -- *Megatron-LM.* Provides the FLOPs calculation formula used for model FLOPs utilization metrics.
