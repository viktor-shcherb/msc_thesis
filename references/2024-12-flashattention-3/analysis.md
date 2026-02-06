---
title: "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision"
authors: "Shah, Bikshandi, Zhang, Thakkar, Ramani, Dao"
year: 2024
venue: "NeurIPS 2024"
paper_type: "conference-paper"
categories: ["attention-efficiency", "architecture"]
scope: ["exact attention", "GPU optimization", "Hopper architecture", "FP8 low-precision", "warp-specialization", "asynchronous execution"]
benchmarks_used: []
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "FlashAttention-2 achieves only 35% utilization on H100 GPU compared to 80-90% for optimized GEMM kernels"
    evidence: "Section 1, Abstract"
    status: supported
    scope: "H100 GPU"
    magnitude: "35% vs 80-90% utilization"
  - id: C2
    claim: "FlashAttention-3 achieves 1.5-2.0× speedup over FlashAttention-2 in the forward pass with FP16"
    evidence: "Abstract, Section 4.1, Figure 5"
    status: supported
    scope: "H100 GPU, sequence lengths 512-16K"
    magnitude: "1.5-2.0× speedup"
  - id: C3
    claim: "FlashAttention-3 FP16 reaches up to 740 TFLOPs/s (75% utilization) on H100"
    evidence: "Abstract, Section 4.1, Figure 5"
    status: supported
    scope: "H100 SXM5 GPU, head dimension 256"
    magnitude: "740 TFLOPs/s, 75% of theoretical max"
  - id: C4
    claim: "FlashAttention-3 FP8 reaches close to 1.2 PFLOPs/s on H100"
    evidence: "Abstract, Section 4.1, Figure 7"
    status: supported
    scope: "H100 SXM5 GPU, head dimension 256"
    magnitude: "~1.2 PFLOPs/s"
  - id: C5
    claim: "FP8 FlashAttention-3 with block quantization and incoherent processing achieves 2.6× lower numerical error than baseline FP8 attention with per-tensor quantization"
    evidence: "Section 4.3, Table 3"
    status: supported
    scope: "Simulated outlier features (0.1% entries with 10× larger values)"
    magnitude: "2.6× lower RMSE (9.1e-3 vs 2.4e-2)"
  - id: C6
    claim: "Non-matmul operations (exponential for softmax) have 256× lower throughput than matmul on H100"
    evidence: "Section 3.1: 989 TFLOPs/s matmul vs 3.9 TFLOPs/s special functions"
    status: supported
    scope: "H100 SXM5 GPU"
    magnitude: "989 TFLOPs/s vs 3.9 TFLOPs/s"
  - id: C7
    claim: "Warp-specialization and GEMM-softmax pipelining together improve performance from 570 to 661 TFLOPs/s"
    evidence: "Table 2, Section 4.2"
    status: supported
    scope: "FP16, non-causal, batch=4, seqlen=8448, nheads=16, hdim=128"
    magnitude: "16% improvement (570→661 TFLOPs/s)"
cross_references:
  - target: 2024-05-flashattention-2
    type: extends
    detail: "Direct follow-up that improves H100 utilization from 35% to 75% through asynchrony and low-precision techniques"
  - target: 2022-12-flashattention
    type: extends
    detail: "Builds on the IO-aware tiling strategy from original FlashAttention"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Provides highly optimized implementation of standard Transformer attention"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer uses sparse attention patterns; FlashAttention-3 provides efficient exact attention"
  - target: 2020-12-bigbird-sparse-attention
    type: complementary
    detail: "BigBird uses sparse attention; FlashAttention-3 makes exact attention competitive"
open_questions:
  - question: "How do the techniques generalize to other hardware accelerators beyond Hopper GPUs?"
    addressed_by: null
  - question: "What are the effects of low-precision FP8 attention on large-scale training quality?"
    addressed_by: null
  - question: "Can the FP8 kernel be improved with persistent kernel design and load balancing for better performance with causal masking?"
    addressed_by: null
  - question: "How should FlashAttention-3 be optimized for LLM inference workloads?"
    addressed_by: null
---
# FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision

**Authors:** Jay Shah, Ganesh Bikshandi, Ying Zhang, Vijay Thakkar, Pradeep Ramani, Tri Dao (Colfax Research, Meta, NVIDIA, Georgia Tech, Princeton University, Together AI)
**Date:** December 2024, NeurIPS 2024 (arXiv:2407.08608)

---

## Core Research Problem

FlashAttention-2 introduced IO-aware attention that reduces memory reads/writes and achieves significant speedup over standard attention. However, FlashAttention-2 achieves only **35% utilization on the H100 GPU**, while optimized matrix-multiplication (GEMM) kernels reach 80-90% utilization on the same hardware.

The root cause is that FlashAttention-2's algorithm adheres to a **simplified synchronous model** and makes no explicit use of two key capabilities in modern GPUs:

1. **Asynchrony:** Hardware specialization separates matrix multiplication (Tensor Cores) and memory loading (Tensor Memory Accelerator - TMA) from CUDA cores. FlashAttention-2 does not exploit this separation.

2. **Low precision:** FP8 support in Hopper provides 2× throughput compared to FP16/BF16, but FlashAttention-2 does not target FP8 Tensor Cores.

Additionally, non-matmul operations like softmax (exponential function) have dramatically lower throughput than matmul: **989 TFLOPs/s for FP16 matmul vs only 3.9 TFLOPs/s for special functions** on H100. For attention with head dimension 128, there are 512× more matmul FLOPs than exponential operations, but exponential has 256× lower throughput—so exponential can consume 50% of the cycle time compared to matmul.

**The core challenge is: how to redesign FlashAttention to exploit asynchronous execution between matmul and softmax, and how to leverage low-precision FP8 while maintaining numerical accuracy.**

---

## Problem Solutions

FlashAttention-3 introduces three main techniques to speed up attention on Hopper GPUs:

1. **Producer-consumer asynchrony:** Warp-specialized software pipelining splits data movement (TMA) and computation (Tensor Cores) into separate warps, enabling overlap of memory and instruction issue latencies.

2. **Hiding softmax under asynchronous GEMMs:** Overlap the low-throughput non-GEMM operations in softmax with asynchronous WGMMA instructions for GEMM through a 2-stage pipeline.

3. **Hardware-accelerated low-precision GEMM:** Target FP8 Tensor Cores with block quantization and incoherent processing to mitigate accuracy loss.

---

## Approach Details

### Method

Standard attention computes:

> S = αQK^T ∈ R^(N×N), P = softmax(S) ∈ R^(N×N), O = PV ∈ R^(N×d)

where α = 1/√d is the scaling factor. FlashAttention-3 maintains the same tiling approach as FlashAttention-2 but redesigns the implementation for Hopper's asynchronous execution model.

### Key Technical Components

#### 1. Producer-Consumer Asynchrony via Warp-Specialization

The forward pass parallelizes over batch size, number of heads, and query sequence length. At the CTA (thread block) level:

**Producer warpgroup:**
- Deallocates registers (since TMA needs minimal registers)
- Issues TMA loads of Q_i, K_j, V_j from HBM to shared memory
- Manages an s-stage circular SMEM buffer with barrier synchronization

**Consumer warpgroup:**
- Reallocates registers freed by producer (via `setmaxnreg`)
- Performs WGMMA operations (SS-GEMM and RS-GEMM)
- Executes softmax computation

The asynchronous nature of WGMMA and TMA, combined with Hopper's `setmaxnreg` for dynamic register reallocation between warpgroups, enables effective overlap.

#### 2. Pingpong Scheduling

To overlap softmax of one warpgroup with GEMM of another:

- Use synchronization barriers (`bar.sync`) to schedule GEMMs of warpgroup 1 before warpgroup 2
- Softmax of warpgroup 1 executes while warpgroup 2 performs GEMMs
- Roles swap: warpgroup 2 does softmax while warpgroup 1 does GEMMs

**Impact:** Performance improves from 570 TFLOPs/s to 620-640 TFLOPs/s for FP16 forward with head dimension 128 and sequence length 8192.

#### 3. Intra-Warpgroup GEMM-Softmax Pipelining (2-Stage)

Within a single warpgroup, overlap instructions by pipelining across iterations:

In the mainloop (iteration j):
- Compute S_next = Q_i K_j^T using WGMMA (commit but don't wait)
- Compute O_i = O_i + P̃_cur V_{j-1} using WGMMA (commit but don't wait)
- While WGMMAs execute asynchronously, compute m_i, P̃_next, ℓ_i from S_next
- Wait for WGMMAs, then rescale O_i

This overlaps the second WGMMA of iteration j with softmax operations from iteration j+1.

**Register pressure trade-off:** The 2-stage pipeline requires extra B_r × B_c × sizeof(float) registers for S_next, limiting block size choices.

#### 4. FP8 Low-Precision Support

**Layout transformations:** FP8 WGMMA on Hopper only supports k-major operand format, but V is typically head-dimension contiguous. FlashAttention-3 performs in-kernel transpose of V tiles using LDSM/STSM instructions.

Additionally, FP32 accumulator and FP8 operand layouts differ. Byte permute instructions transform the first WGMMA's accumulator for the second WGMMA, and the in-kernel transpose writes a matching row permutation of V.

**Block quantization:** Instead of per-tensor scaling, keep one scalar per block of size B_r × d or B_c × d. Scale each block of S during computation at no extra cost since FlashAttention naturally operates on blocks.

**Incoherent processing:** Multiply Q and K with a random orthogonal matrix M before quantizing to FP8:

> (QM)(KM)^T = QK^T (since MM^T = I)

This "spreads out" outliers since each entry of QM or KM becomes a random sum of entries, reducing quantization error. Following Chee et al. (2024) and Tseng et al. (2024), M is chosen as the product of random diagonal matrices of ±1 and a Hadamard matrix, computable in O(d log d) and fuseable with rotary embedding.

### Theoretical Analysis

**Correctness:** FlashAttention-3 computes the exact same output as standard attention O = softmax(QK^T)V with no approximation (for FP16). FP8 introduces quantization error controlled by block quantization and incoherent processing.

**FLOPs:** O(N²d), same as FlashAttention and FlashAttention-2.

**Memory:** O(N) additional memory for logsumexp L.

### Experimental Setup

**Hardware:** H100 80GB SXM5 GPU (700W), clock speed fixed to 1830 MHz

**Attention benchmarks:**
- Sequence lengths: 512, 1K, 2K, 4K, 8K, 16K
- Batch size: set so total tokens = 16K
- Hidden dimension: 2048
- Head dimensions: 64, 128, or 256 (32, 16, or 8 heads)

**FLOPs calculation:**
- Forward pass: 4 × seqlen² × head_dim × num_heads
- With causal mask: divide by 2
- Backward pass: 2.5 × forward FLOPs (5 matmuls vs 2)

**Software:**
- CUDA 12.3, cuDNN 9.1.1.17, CUTLASS 3.5
- FlashAttention 2.5.8, Triton nightly 3.0.0
- PyTorch 2.3.0

**Baselines:**
- Standard attention (PyTorch)
- FlashAttention-2
- FlashAttention-2 in Triton (with H100-specific instructions)
- cuDNN 9 (vendor-optimized for H100)

### Key Results

**FP16 Forward Pass (H100 SXM5):**

| Setting | FlashAttention-2 | cuDNN | FlashAttention-3 | FA3 Speedup |
|---------|------------------|-------|------------------|-------------|
| No causal, d=64, 16K | 324 TFLOPs/s | 413 TFLOPs/s | 497 TFLOPs/s | 1.53× |
| Causal, d=64, 16K | 299 TFLOPs/s | 388 TFLOPs/s | 473 TFLOPs/s | 1.58× |
| No causal, d=128, 16K | 370 TFLOPs/s | 595 TFLOPs/s | 648 TFLOPs/s | 1.75× |
| Causal, d=128, 16K | 335 TFLOPs/s | 539 TFLOPs/s | 616 TFLOPs/s | 1.84× |
| No causal, d=256, 16K | 326 TFLOPs/s | 581 TFLOPs/s | **756 TFLOPs/s** | 2.32× |
| Causal, d=256, 16K | 298 TFLOPs/s | 509 TFLOPs/s | 642 TFLOPs/s | 2.15× |

FlashAttention-3 reaches up to **740 TFLOPs/s (75% of theoretical max)** on H100.

**FP16 Backward Pass (H100 SXM5):**

| Setting | FlashAttention-2 | cuDNN | FlashAttention-3 | FA3 Speedup |
|---------|------------------|-------|------------------|-------------|
| No causal, d=64, 16K | 291 TFLOPs/s | 433 TFLOPs/s | 474 TFLOPs/s | 1.63× |
| No causal, d=128, 16K | 322 TFLOPs/s | 516 TFLOPs/s | 561 TFLOPs/s | 1.74× |

FlashAttention-3 achieves **1.5-1.75× speedup** over FlashAttention-2 in the backward pass.

**FP8 Forward Pass (H100 SXM5):**

| Setting | Triton | cuDNN | FlashAttention-3 |
|---------|--------|-------|------------------|
| No causal, d=64, 16K | 511 TFLOPs/s | 438 TFLOPs/s | 613 TFLOPs/s |
| No causal, d=128, 16K | 635 TFLOPs/s | 1003 TFLOPs/s | 1008 TFLOPs/s |
| No causal, d=256, 16K | 903 TFLOPs/s | 1139 TFLOPs/s | **1171 TFLOPs/s** |
| Causal, d=256, 16K | 663 TFLOPs/s | 1099 TFLOPs/s | 1024 TFLOPs/s |

FlashAttention-3 FP8 reaches close to **1.2 PFLOPs/s** on H100.

**Ablation Study (FP16, non-causal, batch=4, seqlen=8448, nheads=16, hdim=128):**

| Configuration | Time | TFLOPs/s |
|---------------|------|----------|
| FlashAttention-3 (full) | 3.538 ms | 661 |
| No GEMM-Softmax Pipelining, with Warp-Specialization | 4.021 ms | 582 |
| GEMM-Softmax Pipelining, No Warp-Specialization | 4.105 ms | 570 |

Both warp-specialization and GEMM-softmax pipelining contribute to the speedup.

**Numerical Error (with simulated outliers: N(0,1) + N(0,100)·Bernoulli(0.001)):**

| Method | RMSE |
|--------|------|
| Standard attention FP16 | 3.2e-4 |
| FlashAttention-2 FP16 | 1.9e-4 |
| FlashAttention-3 FP16 | 1.9e-4 |
| Baseline FP8 (per-tensor quantization) | 2.4e-2 |
| FlashAttention-3 FP8 (block quant + incoherent) | **9.1e-3** |
| FlashAttention-3 FP8 (no block quant) | 9.3e-3 |
| FlashAttention-3 FP8 (no incoherent processing) | 2.4e-2 |

FP8 FlashAttention-3 achieves **2.6× lower error** than baseline FP8 attention.

---

## Limitations and Failure Modes

1. **Hopper-specific.** The techniques are designed for NVIDIA Hopper architecture. Generalization to other hardware accelerators is discussed but not validated.

2. **FP8 kernel lacks persistent design.** FP16 FlashAttention-3 uses a persistent kernel and load balancing, but FP8 does not. This partly explains why FP8 underperforms cuDNN for small sequence lengths and causal masking.

3. **FP8 causal masking performance.** For head dimensions 128 and 256 with causal masking, FP8 FlashAttention-3 is behind cuDNN.

4. **LLM inference not optimized.** The paper focuses on training workloads; inference optimization is left for future work.

5. **Effects of FP8 on large-scale training unknown.** The paper validates FP8 accuracy on synthetic benchmarks but does not evaluate effects on actual large-scale model training quality.

6. **Manual tuning required.** Block sizes and other parameters are tuned manually for different head dimensions.

### Scope and Comparability

- **What was not tested:** End-to-end training throughput, LLM inference, multi-GPU distributed attention, actual model training quality with FP8.
- **Comparability notes:** Benchmarks use fixed GPU clock speed (1830 MHz) to reduce variability. cuDNN is closed-source, so implementation details cannot be compared directly.

---

## Conclusions

### Contributions

1. **Identified utilization gap.** Diagnosed that FlashAttention-2 achieves only 35% utilization on H100 due to not exploiting asynchrony and low-precision capabilities.

2. **Warp-specialized asynchrony.** Developed producer-consumer warp-specialization scheme that separates data movement (TMA) and computation (Tensor Cores) into separate warps.

3. **GEMM-softmax pipelining.** Designed 2-stage pipeline that overlaps low-throughput softmax operations with asynchronous WGMMA instructions.

4. **FP8 support with accuracy techniques.** Enabled FP8 Tensor Cores through layout transformations, block quantization, and incoherent processing.

5. **1.5-2.0× speedup.** Achieved significant speedup over FlashAttention-2, reaching 75% of theoretical maximum throughput on H100.

6. **2.6× lower FP8 error.** Demonstrated that block quantization and incoherent processing substantially reduce numerical error for FP8 attention.

### Implications

1. **Longer context at same cost.** 2× speedup enables training models with longer context windows without proportional cost increase.

2. **Exact attention remains competitive.** At 75% utilization, exact attention is close to GEMM efficiency, reducing the incentive for approximate attention methods at moderate sequence lengths.

3. **FP8 training viability.** Block quantization and incoherent processing may enable FP8 attention in large-scale training, though further validation is needed.

4. **Portable techniques.** Although demonstrated on Hopper, the asynchrony and low-precision techniques should apply to other hardware with similar capabilities.

---

## Key Claims

**C1. FlashAttention-2 achieves only 35% utilization on H100.** Compared to 80-90% for optimized GEMM kernels, this represents a significant efficiency gap (Section 1, Abstract). Status: **supported**.

**C2. FlashAttention-3 achieves 1.5-2.0× speedup over FlashAttention-2.** In the forward pass with FP16 on H100 across sequence lengths 512-16K (Abstract, Section 4.1, Figure 5). Status: **supported**.

**C3. FlashAttention-3 FP16 reaches 740 TFLOPs/s (75% utilization).** On H100 SXM5 with head dimension 256 (Figure 5e). Status: **supported**.

**C4. FlashAttention-3 FP8 reaches ~1.2 PFLOPs/s.** On H100 SXM5 with head dimension 256, without causal masking (Figure 7). Status: **supported**.

**C5. FP8 FlashAttention-3 achieves 2.6× lower numerical error.** Compared to baseline FP8 attention with per-tensor quantization, when using block quantization and incoherent processing (Table 3: RMSE 9.1e-3 vs 2.4e-2). Status: **supported**.

**C6. Non-matmul operations have 256× lower throughput on H100.** H100 has 989 TFLOPs/s for FP16 matmul but only 3.9 TFLOPs/s for special functions like exponential (Section 3.1). Status: **supported**.

**C7. Warp-specialization and GEMM-softmax pipelining together contribute 16% improvement.** From 570 to 661 TFLOPs/s (Table 2, Section 4.2). Status: **supported**.

---

## Open Questions

1. **Hardware generalization.** The techniques are developed for Hopper GPUs. How well do they generalize to other architectures with asynchronous execution and low-precision support (e.g., AMD MI300, future NVIDIA architectures)?

2. **Large-scale FP8 training.** The accuracy of FP8 attention is validated on synthetic benchmarks. What are the effects on actual large-scale model training quality?

3. **Inference optimization.** The paper focuses on training. How should FlashAttention-3 be adapted for LLM inference workloads with different batch sizes and memory access patterns?

4. **FP8 kernel improvements.** Can persistent kernel design and better load balancing improve FP8 performance, especially for causal masking and smaller sequence lengths?

5. **Backward pass FP8.** The paper only benchmarks FP8 for the forward pass. What speedups and accuracy trade-offs exist for FP8 backward pass?

---

## Core References and Why They Are Referenced

### FlashAttention Lineage

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* The original FlashAttention paper that introduced IO-aware tiling and recomputation.

- **Dao (2023)** -- *FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning.* The direct predecessor that FlashAttention-3 extends, achieving 25-40% utilization on A100.

- **Rabe & Staats (2021)** -- *Self-Attention Does Not Need O(n²) Memory.* Showed attention can be computed with O(n) memory using tiling.

### GPU Architecture and Optimization

- **NVIDIA (2024)** -- *CUDA Programming Guide and PTX ISA.* Documents TMA, WGMMA, and other Hopper-specific instructions used in the implementation.

- **Bauer et al. (2011)** -- *CudaDMA: Optimizing GPU Memory Bandwidth via Warp Specialization.* Introduced warp-specialization concept that FlashAttention-3 applies.

- **NVIDIA CUTLASS** -- Provides WGMMA and TMA abstractions used for implementation.

- **Luo et al. (2024)** -- *Benchmarking and Dissecting the Nvidia Hopper GPU Architecture.* Provides shared memory bandwidth measurements used in the paper.

### Low-Precision and Quantization

- **Chee et al. (2024)** -- *QuIP: 2-bit Quantization of Large Language Models with Guarantees.* Introduced incoherent processing technique adapted for FP8 attention.

- **Tseng et al. (2024)** -- *QuIP#: Even Better LLM Quantization with Hadamard Incoherence.* Refined incoherent processing with Hadamard matrices used in FlashAttention-3.

- **Micikevicius et al. (2022)** -- *FP8 Formats for Deep Learning.* Defines FP8 formats supported by Hopper Tensor Cores.

- **Dettmers et al. (2022)** -- *LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale.* Documents outlier features in LLMs that motivate block quantization.

### Transformer and Attention

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Original Transformer architecture whose attention mechanism FlashAttention-3 optimizes.

- **Shazeer (2019)** -- *Fast Transformer Decoding: One Write-Head Is All You Need.* Introduced multi-query attention (MQA), supported by FlashAttention-3.

- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models.* Introduced grouped-query attention (GQA), supported by FlashAttention-3.

### Efficient Attention (Context)

- **Beltagy et al. (2020)** -- *Longformer.* Sparse attention baseline.
- **Zaheer et al. (2020)** -- *Big Bird.* Sparse attention baseline.
- **Choromanski et al. (2020)** -- *Performers.* Linear attention baseline.
- **Kitaev et al. (2020)** -- *Reformer.* Efficient attention baseline.

### Alternative Architectures (Context)

- **Gu & Dao (2023)** -- *Mamba: Linear-Time Sequence Modeling.* State space model alternative to attention.
- **Dao & Gu (2024)** -- *Transformers are SSMs.* Connects Transformers and state space models.
