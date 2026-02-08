---
title: "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning"
authors: "Dao"
year: 2024
venue: "ICLR 2024"
paper_type: conference-paper
categories: ["attention-efficiency", "architecture"]
scope: ["exact attention", "GPU optimization", "training efficiency", "work partitioning"]
benchmarks_used: []
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "FlashAttention achieves only 25-40% of theoretical maximum FLOPs/s on A100 due to suboptimal work partitioning between thread blocks and warps"
    evidence: "Section 1, Figures 5-6"
    status: supported
    scope: "A100 80GB SXM4, FP16/BF16, head dimensions 64 and 128"
    magnitude: "forward 30-50%, backward 25-35% of theoretical max"
  - id: C2
    claim: "FlashAttention-2 achieves around 2x speedup over FlashAttention through algorithm tweaks, sequence-length parallelism, and better warp partitioning"
    evidence: "Section 4.1, Figure 4"
    status: supported
    scope: "A100 80GB SXM4, sequence lengths 512-16K, head dimensions 64 and 128"
    magnitude: "1.7-3.0x faster than FlashAttention, 3-10x faster than standard PyTorch"
  - id: C3
    claim: "FlashAttention-2 reaches up to 73% of theoretical maximum FLOPs/s on A100 in the forward pass and up to 63% in the backward pass"
    evidence: "Figures 5-6"
    status: supported
    scope: "A100 80GB SXM4, sequence length 16K, head dimension 128, no causal mask"
    magnitude: "up to 225 TFLOPs/s forward (73% of 312 TFLOPs/s), up to 196 TFLOPs/s backward (63%)"
  - id: C4
    claim: "Non-matmul FLOPs are 16x more expensive than matmul FLOPs on A100 due to specialized Tensor Core compute units"
    evidence: "Section 3.1"
    status: supported
    scope: "A100 GPU, FP16/BF16 matmul vs FP32 non-matmul"
    magnitude: "312 TFLOPs/s matmul vs 19.5 TFLOPs/s non-matmul = 16x ratio"
  - id: C5
    claim: "FlashAttention-2 achieves up to 225 TFLOPs/s per A100 GPU (72% model FLOPs utilization) for end-to-end GPT-style training"
    evidence: "Table 1, Section 4.2"
    status: supported
    scope: "GPT3-2.7B, 8K context, 8xA100 80GB SXM, FLOPs formula from Megatron-LM"
    magnitude: "225 TFLOPs/s (72% MFU), 1.3x over FlashAttention, 2.8x over baseline"
  - id: C6
    claim: "Parallelizing over the sequence length dimension increases GPU occupancy for long sequences with small batch sizes"
    evidence: "Section 3.2"
    status: supported
    scope: "when batch_size x num_heads < 108 SMs on A100"
    magnitude: "qualitative -- enables full SM utilization for long-sequence workloads"
  - id: C7
    claim: "Splitting Q across warps instead of K/V eliminates inter-warp shared memory communication and yields speedup"
    evidence: "Section 3.3, Figure 3"
    status: supported
    scope: "4-warp thread blocks, forward and backward pass"
    magnitude: "qualitative -- removes shared memory synchronization overhead vs split-K scheme"
  - id: C8
    claim: "Causal masking optimization skips approximately half of the attention blocks, yielding 1.7-1.8x speedup over non-causal attention"
    evidence: "Section 3.1.1"
    status: supported
    scope: "large sequence lengths where roughly half of blocks can be skipped"
    magnitude: "1.7-1.8x speedup compared to non-causal attention"
  - id: C9
    claim: "Running FlashAttention-2 on H100 without H100-specific optimizations reaches up to 335 TFLOPs/s"
    evidence: "Section 4.1, Figure 7"
    status: supported
    scope: "H100 80GB SXM5, no TMA or 4th-gen Tensor Core or FP8 optimizations"
    magnitude: "up to 335 TFLOPs/s (forward+backward); expected 1.5-2x further with H100-specific instructions"
cross_references:
  - target: 2022-12-flashattention
    type: extends
    detail: "Direct follow-up that improves GPU utilization from 25-40% to 50-73% through better parallelism and work partitioning"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Provides a highly optimized implementation of the standard Transformer attention mechanism"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer uses sparse attention patterns; FlashAttention-2 provides an efficient exact attention primitive that reduces the need for approximation at moderate lengths"
  - target: 2020-12-bigbird-sparse-attention
    type: complementary
    detail: "BigBird uses sparse attention; FlashAttention-2 makes exact attention competitive at moderate sequence lengths"
  - target: 2024-12-flashattention-3
    type: extended-by
    detail: "FlashAttention-3 improves H100 utilization from 35% to 75% through warp-specialized asynchrony, GEMM-softmax pipelining, and FP8 low-precision"
open_questions:
  - question: "Can H100-specific optimizations (TMA, 4th-gen Tensor Cores, FP8) provide the expected 1.5-2x additional speedup?"
    addressed_by: 2024-12-flashattention-3
  - question: "Can auto-tuning replace manual block size selection across different head dimensions and GPU architectures?"
    addressed_by: null
  - question: "How can FlashAttention-2 be combined with high-level algorithmic changes (local, dilated, block-sparse attention) for even longer contexts?"
    addressed_by: null
  - question: "How should work partitioning be adapted for multi-GPU settings with inter-GPU communication?"
    addressed_by: null
---

# FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning

**Authors:** Tri Dao (Department of Computer Science, Princeton University; Department of Computer Science, Stanford University)
**Date:** May 2024, ICLR 2024 (arXiv:2307.08691)

---

## Core Research Problem

FlashAttention (Dao et al., 2022) introduced an IO-aware attention algorithm that reduces memory reads/writes by tiling and recomputation, achieving 2-4x wall-clock speedup over standard attention with no approximation and linear instead of quadratic memory. However, FlashAttention still achieves only **25-40% of the theoretical maximum FLOPs/s** on A100 GPUs (forward pass 30-50%, backward pass 25-35%), while optimized matrix-multiply (GEMM) operations reach 80-90% (Section 1, Figures 5-6).

Through careful profiling, the author identifies the root cause as **suboptimal work partitioning** between thread blocks and warps on the GPU, which produces two symptoms:
1. **Low occupancy** -- underutilization of GPU streaming multiprocessors (SMs) when batch size times number of heads is small relative to the 108 SMs on A100.
2. **Unnecessary shared memory reads/writes** -- the "split-K" warp partitioning scheme in FlashAttention requires inter-warp communication through shared memory.

A further contributing factor is that modern GPUs have specialized compute units (Tensor Cores) that make matmul operations **16x faster** than non-matmul operations (312 TFLOPs/s vs 19.5 TFLOPs/s on A100). FlashAttention spends a non-trivial fraction of time on non-matmul FLOPs (rescaling, softmax statistics), which disproportionately slows execution.

**The core challenge is: how to partition attention computation across thread blocks and warps to maximize GPU utilization while maintaining the IO-aware, exact-computation properties of FlashAttention.**

---

## Problem Solutions

FlashAttention-2 introduces three complementary optimizations that together yield around 2x speedup over FlashAttention:

1. **Reduce non-matmul FLOPs.** Tweak the online softmax algorithm to defer rescaling until the end of the loop and store only the logsumexp (not separate max and sum of exponentials), reducing the number of expensive non-matmul operations.

2. **Parallelize over sequence length.** In addition to parallelizing over batch size and number of heads, distribute the outer loop across the sequence length dimension to increase GPU occupancy when sequences are long and batch sizes are small.

3. **Better warp-level work partitioning.** Replace the "split-K" scheme (splitting K and V across warps, requiring inter-warp shared memory communication) with a scheme that splits Q across warps while sharing K and V, eliminating inter-warp synchronization.

---

## Approach Details

### Method

Standard attention computes:

> S = QK^T in R^(N x N), P = softmax(S) in R^(N x N), O = PV in R^(N x d)

FlashAttention-2 maintains the same tiling and recomputation approach as FlashAttention but optimizes the GPU implementation at three levels: algorithm-level FLOPs reduction, thread-block-level parallelism, and warp-level work partitioning.

### Key Technical Components

#### 1. Algorithm Tweaks to Reduce Non-Matmul FLOPs

**Observation:** On A100, matmul throughput is **312 TFLOPs/s** (FP16/BF16) while non-matmul FP32 throughput is only **19.5 TFLOPs/s**. Each non-matmul FLOP is effectively **16x more expensive** than a matmul FLOP (Section 3.1).

**Tweak 1 -- Delayed rescaling.** In the original FlashAttention online softmax, both terms of the output update are rescaled by diag(l^(2))^(-1) at each iteration:

> O^(2) = diag(l^(1)/l^(2))^(-1) O^(1) + diag(l^(2))^(-1) e^(S^(2) - m^(2)) V^(2)

FlashAttention-2 instead maintains an "un-scaled" version and only divides once at the end:

> O_tilde^(2) = diag(e^(m^(1) - m^(2))) O_tilde^(1) + e^(S^(2) - m^(2)) V^(2)

> O = diag(l^(last))^(-1) O_tilde^(last)

This reduces the number of non-matmul rescaling operations per inner loop iteration (Section 3.1.1).

**Tweak 2 -- Store only logsumexp.** Instead of saving both the max m^(j) and sum of exponentials l^(j) for the backward pass, store only:

> L^(j) = m^(j) + log(l^(j))

This reduces the memory footprint for the backward pass from two vectors to one (Section 3.1.1).

The full FlashAttention-2 forward pass (Algorithm 1, Section 3.1.1) proceeds as:
1. Divide Q into T_r = ceil(N/B_r) row blocks and K, V into T_c = ceil(N/B_c) column blocks.
2. For each row block i (outer loop, parallelized across thread blocks):
   - Load Q_i from HBM to SRAM.
   - Initialize O_i = 0, l_i = 0, m_i = -inf.
   - For each column block j (inner loop):
     - Load K_j, V_j from HBM to SRAM.
     - Compute S_i^(j) = Q_i K_j^T (matmul on Tensor Cores).
     - Update running max: m_i^(j) = max(m_i^(j-1), rowmax(S_i^(j))).
     - Compute P_tilde_i^(j) = exp(S_i^(j) - m_i^(j)) and update l_i^(j).
     - Update O_i^(j) = diag(e^(m_i^(j-1) - m_i^(j))) O_i^(j-1) + P_tilde_i^(j) V_j.
   - Final scaling: O_i = diag(l_i^(T_c))^(-1) O_i^(T_c).
   - Compute and store logsumexp: L_i = m_i^(T_c) + log(l_i^(T_c)).
3. Return O and L.

#### 2. Parallelization Strategy

**FlashAttention (original):** Parallelizes over batch size and number of heads only. One thread block processes one attention head. This is efficient when batch_size x num_heads >= 80, but underutilizes the GPU when this product is small (Section 3.2).

**FlashAttention-2 forward pass:** The outer loop over row blocks of Q is **embarrassingly parallel** -- different row blocks are scheduled on different thread blocks with **no inter-block communication**. This adds parallelism over the sequence length dimension (Section 3.2).

**FlashAttention-2 backward pass:** Parallelizes over column blocks. The only shared computation is updating dQ, which requires **atomic adds** for inter-block communication (Algorithm 2, Section 3.1.2). The backward pass outer loop iterates over K/V column blocks j, and for each j iterates over Q row blocks i, computing:
- S_i^(j) = Q_i K_j^T
- P_i^(j) = exp(S_ij - L_i)
- dV_j += (P_i^(j))^T dO_i
- dP_i^(j) = dO_i V_j^T
- dS_i^(j) = P_i^(j) * (dP_i^(j) - D_i) where D = rowsum(dO * O)
- dQ_i += dS_i^(j) K_j (via atomic adds)
- dK_j += dS_i^(j)^T Q_i

**Impact:** When batch_size x num_heads < 108 (number of SMs on A100), parallelizing over sequence length improves occupancy. The loop reordering idea (outer loop over rows, inner loop over columns) was first suggested and implemented by Phil Tillet in the Triton implementation (Section 3.2).

#### 3. Warp-Level Work Partitioning

**FlashAttention "split-K" scheme (Figure 3a):**
- Split K and V across 4 warps; Q accessible by all warps.
- Each warp computes a slice of QK^T, then multiplies with its slice of V.
- Warps must **write intermediate results to shared memory, synchronize, and add** -- this communication overhead is costly (Section 3.3).

**FlashAttention-2 scheme (Figure 3b):**
- Split **Q** across 4 warps; K and V accessible by all warps.
- Each warp computes its slice of QK^T and multiplies with the shared V.
- **No inter-warp communication needed** -- each warp independently produces its output slice (Section 3.3).

The backward pass similarly avoids "split-K" where possible, though some synchronization remains due to the more complex dependency structure among Q, K, V, O, dO, dQ, dK, dV (Section 3.3).

#### 4. Causal Masking Optimizations

For autoregressive language modeling, a causal mask sets S_ij = -inf when j > i. FlashAttention-2 exploits the block structure:

1. **Skip zero blocks:** For blocks where all column indices exceed all row indices (approximately half the blocks for large N), skip computation entirely. This yields **1.7-1.8x speedup** over non-causal attention (Section 3.1.1).

2. **Selective masking:** Apply the causal mask only to the diagonal blocks (where row and column indices overlap). All other computed blocks are either fully computed or fully skipped (Section 3.1.1).

#### 5. Block Size Tuning

Block sizes are typically {64, 128} x {64, 128}, depending on head dimension d and device shared memory. Larger blocks reduce shared memory loads/stores but may cause register spilling or exceed shared memory capacity. The author manually tunes for each head dimension (16, 32, 64, 128) since there are only 4 choices, but notes auto-tuning would be beneficial (Section 3.3).

#### 6. Support for Attention Variants

**Multi-query attention (MQA)** and **grouped-query attention (GQA):** Multiple query heads attend to the same K/V head. FlashAttention-2 handles this by manipulating indices rather than duplicating K/V tensors. In the backward pass, gradients dK and dV are summed across the duplicated query heads (Section 3.1.2).

### Theoretical Analysis

**Correctness:** FlashAttention-2 returns the exact same output as standard attention O = softmax(QK^T)V, with **no approximation**. The proof follows directly from FlashAttention (Dao et al., 2022, Theorem 1) (Section 3.1.1).

**FLOPs:** O(N^2 d), same as standard attention and FlashAttention (Section 3.1.1).

**Memory:** O(N) additional memory beyond inputs and output, for storing the logsumexp vector L (Section 3.1.1).

### Experimental Setup

**Attention kernel benchmarks (Section 4.1):**
- **GPU:** A100 80GB SXM4
- **Sequence lengths:** 512, 1K, 2K, 4K, 8K, 16K
- **Batch size:** set so total tokens = 16K (i.e., batch_size = 16K / seqlen)
- **Hidden dimension:** 2048
- **Head dimensions:** 64 (32 heads) or 128 (16 heads)
- **Comparisons:** PyTorch standard attention, FlashAttention, xformers (CUTLASS), FlashAttention Triton

**FLOPs calculation for attention benchmarks (Section 4.1):**

> Forward FLOPs = 4 x seqlen^2 x head_dim x num_heads

With causal mask, divide by 2. Backward FLOPs = 2.5 x forward FLOPs (5 matmuls vs 2 in forward).

**End-to-end GPT training (Section 4.2):**
- **Models:** GPT-3 style, 1.3B and 2.7B parameters
- **Context lengths:** 2K and 8K
- **Hardware:** 8 x A100 80GB SXM

**End-to-end FLOPs calculation (following Megatron-LM, Shoeybi et al., 2019):**

> FLOPs = 6 x seqlen x num_params + 12 x num_layers x hidden_dim x seqlen^2

The first term is weight-input multiplication; the second is attention. The authors do not divide the attention term by 2 for causal masking, for consistency with prior literature (Section 4.2).

**H100 benchmarks:** FlashAttention-2 was also run on H100 80GB SXM5 without H100-specific optimizations (no TMA, no 4th-gen Tensor Cores, no FP8) (Section 4.1).

**Reproducibility:** Code is publicly available at https://github.com/Dao-AILab/flash-attention. The paper uses the CUTLASS 3.x library for implementation. No random seeds are relevant (deterministic kernel benchmarking). Hardware specifications are fully reported.

### Key Results

**Attention forward + backward speed on A100 (Figure 4, TFLOPs/s):**

Without causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 36      | 91             | 90       | 58        | 132  |
| 1K      | 40      | 102            | 73       | 76        | 162  |
| 2K      | 43      | 104            | 98       | 102       | 171  |
| 4K      | 43      | 108            | 101      | 104       | 175  |
| 8K      | OOM     | 110            | 101      | 73        | 176  |
| 16K     | OOM     | 46             | 46       | 110       | 176  |

Without causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 53      | 74             | 78       | 57        | 131  |
| 1K      | 63      | 91             | 85       | 75        | 181  |
| 2K      | 63      | 95             | 90       | 79        | 196  |
| 4K      | 63      | 95             | 86       | 82        | 201  |
| 8K      | OOM     | 98             | 95       | 83        | 203  |
| 16K     | OOM     | 45             | 95       | 83        | 203  |

With causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 15      | 58             | 59       | 38        | 88   |
| 1K      | 16      | 70             | 60       | 75        | 119  |
| 2K      | 17      | 77             | 79       | 68        | 140  |
| 4K      | 18      | 87             | 78       | 73        | 158  |
| 8K      | OOM     | 92             | 92       | 80        | 165  |
| 16K     | OOM     | 18             | 57       | 97        | 171  |

With causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 23      | 53             | 58       | 28        | 99   |
| 1K      | 28      | 72             | 62       | 61        | 131  |
| 2K      | 32      | 81             | 76       | 74        | 155  |
| 4K      | 32      | 87             | 80       | 80        | 182  |
| 8K      | OOM     | 91             | 92       | 83        | 189  |
| 16K     | OOM     | 19             | 31       | 92        | 189  |

**Attention forward-only speed on A100 (Figure 5, TFLOPs/s):**

Without causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 29      | 91             | 94       | 94        | 128  |
| 1K      | 34      | 94             | 97       | 100       | 149  |
| 2K      | 35      | 99             | 97       | 152       | 193  |
| 4K      | 37      | 104            | 100      | 152       | 192  |
| 8K      | OOM     | 106            | 104      | 152       | 192  |
| 16K     | OOM     | 37             | 37       | 152       | 192  |

Without causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 42      | 69             | 56       | 102       | 122  |
| 1K      | 60      | 69             | 63       | 71        | 157  |
| 2K      | 63      | 71             | 67       | 71        | 200  |
| 4K      | 73      | 122            | 120      | 122       | 224  |
| 8K      | OOM     | 122            | 122      | 160       | 222  |
| 16K     | OOM     | 73             | 122      | 163       | 225  |

With causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 10      | 78             | 82       | 71        | 115  |
| 1K      | 10      | 82             | 89       | 88        | 131  |
| 2K      | 10      | 89             | 92       | 91        | 167  |
| 4K      | 10      | 91             | 94       | 93        | 177  |
| 8K      | OOM     | 94             | 93       | 106       | 181  |
| 16K     | OOM     | 10             | 10       | 106       | 185  |

With causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 15      | 49             | 59       | 63        | 108  |
| 1K      | 18      | 63             | 68       | 70        | 126  |
| 2K      | 19      | 88             | 76       | 115       | 133  |
| 4K      | 19      | 80             | 91       | 115       | 148  |
| 8K      | OOM     | 70             | 92       | 111       | 148  |
| 16K     | OOM     | 19             | 71       | 111       | 148  |

FlashAttention-2 reaches up to **225 TFLOPs/s in forward pass** (Figure 5b, no causal, d=128, 16K), which is **73% of the A100's 312 TFLOPs/s theoretical maximum**.

**Attention backward-only speed on A100 (Figure 6, TFLOPs/s):**

Without causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 39      | 91             | 90       | 32        | 120  |
| 1K      | 43      | 81             | 82       | 48        | 152  |
| 2K      | 44      | 87             | 86       | 88        | 163  |
| 4K      | 49      | 88             | 87       | 112       | 169  |
| 8K      | OOM     | 31             | 31       | 122       | 170  |
| 16K     | OOM     | 88             | 87       | 113       | 170  |

Without causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 39      | 78             | 58       | 56        | 114  |
| 1K      | 73      | 73             | 74       | 77        | 175  |
| 2K      | 84      | 86             | 88       | 84        | 187  |
| 4K      | 89      | 89             | 87       | 89        | 193  |
| 8K      | OOM     | 90             | 90       | 97        | 196  |
| 16K     | OOM     | 81             | 82       | 91        | 196  |

With causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 19      | 58             | 46       | 39        | 81   |
| 1K      | 21      | 70             | 68       | 40        | 111  |
| 2K      | 24      | 76             | 71       | 85        | 149  |
| 4K      | 23      | 53             | 53       | 67        | 160  |
| 8K      | OOM     | 26             | 26       | 98        | 166  |
| 16K     | OOM     | 68             | 68       | 98        | 166  |

With causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | xformers | FA Triton | FA-2 |
|---------|---------|----------------|----------|-----------|------|
| 512     | 30      | 59             | 33       | 43        | 90   |
| 1K      | 37      | 65             | 71       | 58        | 122  |
| 2K      | 43      | 75             | 80       | 80        | 145  |
| 4K      | 48      | 83             | 83       | 53        | 165  |
| 8K      | OOM     | 40             | 63       | 89        | 175  |
| 16K     | OOM     | 87             | 84       | 89        | 186  |

FlashAttention-2 reaches up to **196 TFLOPs/s in the backward pass** (Figure 6b, no causal, d=128, 8K-16K), which is **63% of theoretical maximum**.

**Key attention benchmark takeaways (Section 4.1):**
- FlashAttention-2 is **1.7-3.0x faster** than FlashAttention across settings (tested on A100, sequence lengths 512-16K, head dimensions 64 and 128, with and without causal mask -- strong evidence across multiple configurations).
- FlashAttention-2 is **1.3-2.5x faster** than FlashAttention in Triton.
- FlashAttention-2 is **3-10x faster** than standard PyTorch attention.
- The speedup is largest for head dimension 128 (more matmul-dominated).

**End-to-end GPT training speed on 8xA100 (Table 1, TFLOPs/s per GPU):**

| Model | Without FlashAttention | FlashAttention | FlashAttention-2 |
|-------|------------------------|----------------|------------------|
| GPT3-1.3B 2K context | 142 | 189 | 196 |
| GPT3-1.3B 8K context | 72 | 170 | 220 |
| GPT3-2.7B 2K context | 149 | 189 | 205 |
| GPT3-2.7B 8K context | 80 | 175 | **225** |

FlashAttention-2 achieves **225 TFLOPs/s per A100 = 72% model FLOPs utilization** for GPT3-2.7B with 8K context, representing **1.3x speedup** over FlashAttention and **2.8x speedup** over the baseline without FlashAttention (Table 1, tested across 2 model sizes and 2 context lengths -- moderate evidence).

**Attention forward + backward speed on H100 (Figure 7, TFLOPs/s):**

Without causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | FA-2 |
|---------|---------|----------------|------|
| 512     | 62      | 157            | 215  |
| 1K      | 72      | 136            | 254  |
| 2K      | 81      | 163            | 274  |
| 4K      | 85      | 161            | 288  |
| 8K      | OOM     | 166            | 294  |
| 16K     | OOM     | 188            | 295  |

Without causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | FA-2 |
|---------|---------|----------------|------|
| 512     | 93      | 127            | 248  |
| 1K      | 122     | 143            | 320  |
| 2K      | 127     | 143            | 326  |
| 4K      | 131     | 160            | 315  |
| 8K      | OOM     | 167            | 318  |
| 16K     | OOM     | 139            | 318  |

With causal mask, head dimension 64:

| Seq len | PyTorch | FlashAttention | FA-2 |
|---------|---------|----------------|------|
| 512     | 26      | 104            | 141  |
| 1K      | 29      | 123            | 192  |
| 2K      | 31      | 136            | 232  |
| 4K      | 31      | 138            | 257  |
| 8K      | 32      | 149            | 273  |
| 16K     | 32      | 156            | 284  |

With causal mask, head dimension 128:

| Seq len | PyTorch | FlashAttention | FA-2 |
|---------|---------|----------------|------|
| 512     | 40      | 98             | 163  |
| 1K      | 50      | 126            | 221  |
| 2K      | 57      | 106            | 265  |
| 4K      | 61      | 104            | 294  |
| 8K      | 63      | 135            | 308  |
| 16K     | 63      | 137            | 328  |

On H100, FlashAttention-2 reaches up to **335 TFLOPs/s** (causal, d=128, 16K) without any H100-specific optimizations. The author expects **1.5-2x additional speedup** with TMA, 4th-gen Tensor Cores, and FP8 (Section 4.1). Note: the H100 figure peaks at 328 TFLOPs/s for the causal d=128 setting; the 335 figure from the text may reference a slightly different configuration or rounding.

---

## Limitations and Failure Modes

1. **Requires custom CUDA kernels.** Each attention variant (standard, causal, MQA, GQA) requires reimplementation in CUDA, limiting portability and ease of extension (Section 5).

2. **Manual block size tuning.** Block sizes must be manually tuned per head dimension and device. The author notes auto-tuning would reduce this labor but leaves it to future work (Section 3.3).

3. **Head dimension constraints.** Supports head dimensions 16, 32, 64, 128. Other dimensions require additional kernel implementations (Section 3.3).

4. **No H100-specific optimizations.** The evaluated version does not use TMA, 4th-gen Tensor Cores, or FP8. These are expected to provide 1.5-2x further speedup (Section 5).

5. **[Inferred]** Single-GPU scope. All experiments are on single-GPU (or 8-GPU with data parallelism for end-to-end training). Multi-GPU settings with tensor or pipeline parallelism add inter-GPU communication complexity not addressed.

6. **[Inferred]** Limited model scale evaluation. End-to-end training is evaluated on only two model sizes (1.3B and 2.7B) and two context lengths (2K and 8K). It is unclear whether the same utilization improvements hold at larger scales (e.g., 70B+) or longer contexts (e.g., 32K+).

7. **[Inferred]** No evaluation on non-A100/H100 hardware. All benchmarks use Nvidia A100 or H100. Performance characteristics on AMD GPUs or other accelerators may differ substantially.

#### Scope and Comparability

- **What was not tested:** Models larger than 2.7B parameters; context lengths beyond 16K for kernel benchmarks and 8K for end-to-end training; non-Nvidia hardware; attention patterns beyond dense and causal (e.g., local, dilated, block-sparse); FP8 or INT8 precision; inference-only latency measurements (all benchmarks measure throughput).
- **Comparability notes:** The FLOPs utilization metric uses the Megatron-LM formula without halving attention FLOPs for causal masking, following convention. This means the 72% MFU figure is computed against a theoretical maximum that counts FLOPs that are not actually performed, making it a conservative estimate. Comparisons to standard PyTorch attention include cases where PyTorch runs out of memory (OOM), inflating the apparent speedup. The xformers comparison uses the CUTLASS implementation, which differs from xformers' current default backend.

---

## Conclusions

### Contributions

1. **Diagnosed the utilization gap.** Identified through profiling that FlashAttention's 25-40% utilization stems from suboptimal work partitioning, not from IO complexity -- establishing that the bottleneck is computational organization rather than memory bandwidth (Section 1).

2. **Reduced non-matmul overhead.** Tweaked the online softmax algorithm with delayed rescaling and logsumexp-only storage, reducing the proportion of time spent on 16x-slower non-matmul operations (Section 3.1).

3. **Introduced sequence-length parallelism.** Added parallelization over the sequence length dimension for both forward and backward passes, improving GPU occupancy for long-sequence workloads (Section 3.2).

4. **Eliminated inter-warp communication.** Replaced the "split-K" warp partitioning scheme with Q-splitting that eliminates shared memory synchronization between warps (Section 3.3).

5. **Achieved 2x speedup and 50-73% utilization.** Demonstrated up to 225 TFLOPs/s forward pass and 196 TFLOPs/s backward pass on A100, representing 73% and 63% of theoretical maximum respectively (Figures 5-6).

6. **Demonstrated 72% model FLOPs utilization.** End-to-end GPT-3-style training reaches 225 TFLOPs/s per A100 (Table 1).

7. **Added MQA and GQA support.** Handled multi-query and grouped-query attention through index manipulation rather than tensor duplication (Section 3.1.2).

### Implications

1. **Longer context at same cost.** The 2x attention speedup means training 16K context models at approximately the cost of 8K context models (Section 5).

2. **Reduced motivation for approximate attention.** At 73% utilization, exact attention is no longer far behind GEMM efficiency (80-90%), reducing the incentive for approximate attention methods at moderate sequence lengths (speculative -- depends on workload).

3. **Foundation for H100-era optimizations.** The paper identifies clear paths for further improvement: H100-specific hardware features (TMA, 4th-gen Tensor Cores, FP8) and combination with sparse attention patterns for even longer contexts (Section 5).

---

## Key Claims

**C1. FlashAttention utilization gap.** FlashAttention reaches only 25-40% of theoretical maximum FLOPs/s: forward pass 30-50%, backward pass 25-35% on A100, while GEMM reaches 80-90% (Section 1, Figures 5-6). **Scope:** A100 80GB SXM4, FP16/BF16, head dimensions 64 and 128. **Magnitude:** 30-50% forward, 25-35% backward. Status: **supported** (demonstrated across 4 settings x 6 sequence lengths -- strong evidence).

**C2. 2x speedup over FlashAttention.** FlashAttention-2 achieves around 2x speedup through algorithm tweaks, sequence-length parallelism, and better warp partitioning (Section 4.1, Figure 4). **Scope:** A100 80GB SXM4, sequence lengths 512-16K, head dimensions 64 and 128. **Magnitude:** 1.7-3.0x faster than FlashAttention; 3-10x faster than standard PyTorch. Status: **supported** (tested across 4 settings x 6 sequence lengths, with and without causal mask -- strong evidence).

**C3. 50-73% theoretical max throughput.** FlashAttention-2 reaches up to 225 TFLOPs/s in forward pass (73% of A100's 312 TFLOPs/s) and up to 196 TFLOPs/s in backward pass (63%) (Figures 5-6). **Scope:** A100 80GB SXM4, no causal mask, head dimension 128, sequence length 16K (forward peak) and 8K-16K (backward peak). **Magnitude:** 225 TFLOPs/s forward (73%), 196 TFLOPs/s backward (63%). Status: **supported** (peak values from specific settings; lower percentages for other configurations).

**C4. Non-matmul FLOPs 16x more expensive.** A100 provides 312 TFLOPs/s for FP16/BF16 matmul but only 19.5 TFLOPs/s for non-matmul FP32, making each non-matmul FLOP 16x more expensive (Section 3.1). **Scope:** A100 GPU, FP16/BF16 matmul vs FP32 non-matmul. **Magnitude:** 312/19.5 = 16x ratio. Status: **supported** (hardware specification, not an empirical claim).

**C5. 72% model FLOPs utilization.** End-to-end GPT3-2.7B training with 8K context reaches 225 TFLOPs/s per A100, which is 72% model FLOPs utilization (Table 1). **Scope:** GPT3-2.7B, 8K context, 8xA100 80GB SXM. **Magnitude:** 225 TFLOPs/s = 72% MFU; 1.3x over FlashAttention (175 TFLOPs/s), 2.8x over baseline (80 TFLOPs/s). Status: **supported** (tested across 2 model sizes x 2 context lengths -- moderate evidence; no variance reported, single hardware configuration).

**C6. Sequence-length parallelism improves occupancy.** Parallelizing over sequence length helps when batch_size x num_heads < 108 SMs on A100, which occurs for long sequences with small batches (Section 3.2). **Scope:** when batch_size x num_heads < number of SMs. **Magnitude:** qualitative -- no isolated ablation reported. Status: **supported** (architectural reasoning; no ablation separating this optimization from the others -- limited direct evidence).

**C7. Avoiding split-K reduces shared memory overhead.** Partitioning Q instead of K/V across warps eliminates inter-warp shared memory communication (Section 3.3, Figure 3). **Scope:** 4-warp thread blocks, forward and backward pass. **Magnitude:** qualitative -- no isolated ablation reported. Status: **supported** (architectural reasoning with correctness proof; no ablation separating this optimization -- limited direct evidence).

**C8. Causal masking optimization yields 1.7-1.8x speedup.** Skipping blocks where all column indices exceed row indices (approximately half of blocks) produces 1.7-1.8x speedup over non-causal attention (Section 3.1.1). **Scope:** large sequence lengths where roughly half of blocks can be skipped. **Magnitude:** 1.7-1.8x speedup. Status: **supported** (observable in Figure 4 comparing causal vs non-causal settings -- moderate evidence).

**C9. H100 performance without specific optimizations.** Running FlashAttention-2 on H100 without using TMA, 4th-gen Tensor Cores, or FP8 reaches up to 335 TFLOPs/s (Section 4.1, Figure 7). **Scope:** H100 80GB SXM5, no H100-specific optimizations. **Magnitude:** up to 335 TFLOPs/s; expected 1.5-2x further with H100-specific instructions. Status: **supported** (tested across 4 settings x 6 sequence lengths on H100 -- strong evidence for the measurement; the expected 1.5-2x further improvement is unvalidated projection).

---

## Open Questions

1. **H100 optimizations.** Can TMA (Tensor Memory Accelerator), 4th-gen Tensor Cores, and FP8 provide the expected 1.5-2x additional speedup on H100? *Addressed by FlashAttention-3 (Dao et al., 2024).*

2. **Auto-tuning.** Can auto-tuning replace manual block size selection for different head dimensions and GPU architectures? *Unresolved.*

3. **Combination with sparse attention.** How can FlashAttention-2's low-level optimizations be combined with high-level algorithmic changes (local, dilated, block-sparse attention) for even longer contexts? *Unresolved.*

4. **Multi-GPU extension.** How should work partitioning be adapted for multi-GPU settings with inter-GPU communication? *Unresolved.*

---

## Core References and Why They Are Referenced

### FlashAttention Foundations

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* The direct predecessor. Introduced IO-aware attention with tiling and recomputation, achieving 2-4x speedup and linear memory. FlashAttention-2 extends this by optimizing GPU-level work partitioning.

- **Rabe & Staats (2021)** -- *Self-Attention Does Not Need O(n^2) Memory.* Showed attention can be computed with O(n) memory using tiling. FlashAttention built on this insight.

- **Milakov & Gimelshein (2018)** -- *Online Normalizer Calculation for Softmax.* The online softmax technique that both FlashAttention and FlashAttention-2 use to compute softmax incrementally without materializing the full attention matrix.

### GPU Architecture and Optimization

- **Jia et al. (2018, 2021)** -- *Dissecting the Nvidia Volta/Ampere GPU Architecture via Microbenchmarking.* Provides the hardware specifications (SRAM bandwidth, SM counts, compute throughput) used to reason about FlashAttention-2's performance.

- **Tillet et al. (2019)** -- *Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations.* Phil Tillet's Triton implementation of FlashAttention suggested the loop reordering (outer loop over rows) and sequence-length parallelization that FlashAttention-2 adopts.

### Transformer and Attention Variants

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture whose attention mechanism FlashAttention-2 optimizes.

- **Shazeer (2019)** -- *Fast Transformer Decoding: One Write-Head Is All You Need.* Introduced multi-query attention (MQA), which FlashAttention-2 supports through index manipulation.

- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.* Introduced grouped-query attention (GQA), also supported by FlashAttention-2.

### Efficient Attention Methods (Context)

- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Sparse attention baseline. FlashAttention-2's efficiency reduces the need for such approximations at moderate lengths.
- **Zaheer et al. (2020)** -- *Big Bird: Transformers for Longer Sequences.* Sparse attention baseline.
- **Kitaev et al. (2020)** -- *Reformer: The Efficient Transformer.* Efficient attention baseline using locality-sensitive hashing.
- **Choromanski et al. (2020)** -- *Rethinking Attention with Performers.* Linear attention baseline using random feature maps.

### Training Infrastructure

- **Shoeybi et al. (2019)** -- *Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism.* Provides the FLOPs calculation formula used for model FLOPs utilization metrics in the end-to-end evaluation.

### Implementation Libraries

- **Lefaudeux et al. (2022)** -- *xformers: A Modular and Hackable Transformer Modelling Library.* Provides the CUTLASS-based attention implementation used as a baseline comparison. Daniel Haziza's implementation in xformers motivated aspects of FlashAttention-2.
