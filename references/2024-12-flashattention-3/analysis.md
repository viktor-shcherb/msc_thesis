---
title: "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision"
authors: "Shah, Bikshandi, Zhang, Thakkar, Ramani, Dao"
year: 2024
venue: "NeurIPS 2024"
paper_type: conference-paper
categories: ["attention-efficiency", "architecture", "quantization"]
scope: ["exact attention on NVIDIA Hopper H100 GPU", "FP16 and FP8 precision", "warp-specialization and asynchronous execution", "forward and backward pass"]
benchmarks_used: []
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "FlashAttention-2 achieves only 35% utilization on H100 GPU compared to 80-90% for optimized GEMM kernels"
    evidence: "Section 1, Abstract"
    status: supported
    scope: "H100 GPU, FlashAttention-2 implementation without Hopper-specific instructions"
    magnitude: "35% vs 80-90% utilization"
  - id: C2
    claim: "FlashAttention-3 achieves 1.5-2.0x speedup over FlashAttention-2 in the FP16 forward pass on H100"
    evidence: "Abstract, Section 4.1, Figure 5"
    status: supported
    scope: "H100 SXM5 GPU, FP16, sequence lengths 512-16K, head dimensions 64/128/256, without and with causal mask"
    magnitude: "1.5-2.0x speedup, reaching up to 740 TFLOPs/s (75% utilization)"
  - id: C3
    claim: "FlashAttention-3 FP16 reaches up to ~756 TFLOPs/s (75% utilization) on H100"
    evidence: "Figure 5e (head dim 256, no causal mask, seqlen 16K)"
    status: supported
    scope: "H100 SXM5 GPU, head dimension 256, no causal mask, long sequence lengths"
    magnitude: "~756 TFLOPs/s, 75% of 989 TFLOPs/s theoretical max"
  - id: C4
    claim: "FlashAttention-3 FP8 reaches close to 1.2 PFLOPs/s on H100"
    evidence: "Figure 7a (head dim 256, no causal mask, seqlen 16K)"
    status: supported
    scope: "H100 SXM5 GPU, FP8, head dimension 256, no causal mask"
    magnitude: "~1,171 TFLOPs/s"
  - id: C5
    claim: "FP8 FlashAttention-3 with block quantization and incoherent processing achieves 2.6x lower numerical error than baseline FP8 with per-tensor quantization"
    evidence: "Section 4.3, Table 3"
    status: supported
    scope: "Simulated outlier features (entries drawn from N(0,1) + N(0,100)*Bernoulli(0.001))"
    magnitude: "RMSE 9.1e-3 vs 2.4e-2 (2.6x lower)"
  - id: C6
    claim: "Non-matmul operations (exponential for softmax) have 256x lower throughput than matmul on H100"
    evidence: "Section 3.1"
    status: supported
    scope: "H100 SXM5 GPU, FP16 matmul vs special functions"
    magnitude: "989 TFLOPs/s matmul vs 3.9 TFLOPs/s special functions (256x ratio)"
  - id: C7
    claim: "Warp-specialization and GEMM-softmax pipelining together improve performance from 570 to 661 TFLOPs/s"
    evidence: "Table 2, Section 4.2"
    status: supported
    scope: "FP16, non-causal, batch=4, seqlen=8448, nheads=16, hdim=128"
    magnitude: "16% improvement (570 to 661 TFLOPs/s, 3.538 ms vs 4.105 ms)"
  - id: C8
    claim: "FlashAttention-3 achieves 1.5-1.75x speedup over FlashAttention-2 in the FP16 backward pass"
    evidence: "Section 4.1, Figure 6"
    status: supported
    scope: "H100 SXM5 GPU, FP16, head dimensions 64 and 128, sequence lengths 512-16K, without causal mask"
    magnitude: "1.5-1.75x speedup, up to ~581 TFLOPs/s at hdim=128"
  - id: C9
    claim: "Pingpong scheduling improves FP16 forward pass performance from 570 TFLOPs/s to 620-640 TFLOPs/s"
    evidence: "Section 3.1"
    status: supported
    scope: "FP16 forward pass, head dimension 128, sequence length 8192"
    magnitude: "570 to 620-640 TFLOPs/s"
cross_references:
  - target: 2024-05-flashattention-2
    type: extends
    detail: "Direct follow-up that improves H100 utilization from 35% to 75% through asynchrony and low-precision techniques"
  - target: 2022-12-flashattention
    type: extends
    detail: "Builds on the original IO-aware tiling strategy and online softmax from FlashAttention"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Provides highly optimized implementation of standard Transformer multi-head attention"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer uses sparse attention patterns; FlashAttention-3 provides efficient exact attention"
  - target: 2020-12-bigbird-sparse-attention
    type: complementary
    detail: "BigBird uses sparse attention; FlashAttention-3 makes exact attention competitive at moderate sequence lengths"
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: complementary
    detail: "RWKV is an alternative architecture; paper notes FlashAttention-3 techniques may speed up such architectures too"
  - target: 2024-05-mamba-selective-state-spaces
    type: complementary
    detail: "Mamba is an alternative architecture; paper notes highest quality large models still use attention layers"
  - target: 2023-12-gqa-grouped-query-attention
    type: complementary
    detail: "FlashAttention-3 supports GQA and MQA with adjusted tensor indexing"
open_questions:
  - question: "How do the techniques generalize to other hardware accelerators beyond Hopper GPUs (e.g., AMD MI300, future NVIDIA architectures)?"
    addressed_by: null
  - question: "What are the effects of low-precision FP8 attention on large-scale model training quality?"
    addressed_by: null
  - question: "Can the FP8 kernel be improved with persistent kernel design and load balancing for better performance with causal masking and short sequences?"
    addressed_by: null
  - question: "How should FlashAttention-3 be optimized for LLM inference workloads?"
    addressed_by: null
  - question: "What speedups and accuracy trade-offs exist for FP8 in the backward pass?"
    addressed_by: null
---
# FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision

**Authors:** Jay Shah, Ganesh Bikshandi (Colfax Research), Ying Zhang (Meta), Vijay Thakkar (NVIDIA, Georgia Tech), Pradeep Ramani (NVIDIA), Tri Dao (Princeton University, Together AI)
**Date:** December 2024, NeurIPS 2024 Spotlight (arXiv:2407.08608)

---

## Core Research Problem

The attention mechanism in the Transformer architecture is the primary computational bottleneck for large language models and long-context applications, scaling quadratically in sequence length. FlashAttention-2 (Dao, 2023) introduced IO-aware attention that fuses the entire attention computation into a single GPU kernel, reducing memory reads/writes. However, FlashAttention-2 achieves only **35% utilization on the H100 GPU**, while optimized matrix-multiplication (GEMM) kernels reach 80-90% utilization on the same hardware (Section 1).

The root cause is that FlashAttention-2's algorithm adheres to a **simplified synchronous execution model** and makes no explicit use of two key capabilities in modern GPUs:

1. **Asynchrony.** The Hopper architecture separates matrix multiplication (Tensor Cores via WGMMA) and memory loading (Tensor Memory Accelerator -- TMA) from the core CUDA execution pipeline. FlashAttention-2 does not exploit this separation to overlap computation and data movement.

2. **Low precision.** FP8 Tensor Cores on Hopper deliver 2x the throughput per SM compared to FP16/BF16, but FlashAttention-2 does not target FP8 (Section 2.2).

A further challenge is the **throughput imbalance between matmul and non-matmul operations.** H100 achieves 989 TFLOPs/s for FP16 matmul but only 3.9 TFLOPs/s for special functions such as the exponential needed for softmax (Section 3.1). For attention with head dimension 128, there are 512x more matmul FLOPs than exponential operations, but the exponential has 256x lower throughput, meaning exponential can consume **50% of the cycle time** relative to matmul. This ratio worsens with FP8 since matmul throughput doubles while exponential throughput remains fixed.

**The core challenge is: how to redesign FlashAttention to exploit asynchronous execution between matmul and softmax on Hopper, and how to leverage low-precision FP8 while maintaining numerical accuracy.**

---

## Problem Solutions

FlashAttention-3 introduces three main techniques to close the utilization gap on Hopper GPUs:

1. **Producer-consumer asynchrony via warp-specialization:** Split data movement (TMA loads) and computation (Tensor Core GEMMs) into separate warps, enabling overlap of memory and instruction issue latencies through a circular shared-memory buffer.

2. **Hiding softmax under asynchronous GEMMs:** Overlap the low-throughput non-GEMM operations in softmax with asynchronous WGMMA instructions through (a) **pingpong scheduling** across warpgroups and (b) a **2-stage GEMM-softmax pipeline** within a single warpgroup.

3. **Hardware-accelerated low-precision GEMM:** Target FP8 Tensor Cores with in-kernel layout transformations, **block quantization**, and **incoherent processing** to mitigate accuracy loss from quantization, especially in the presence of outlier features.

---

## Approach Details

### Method

Standard attention computes (Section 2.1):

> **S** = sigma * **Q** **K**^T, **P** = softmax(**S**), **O** = **P** **V**

where **Q**, **K**, **V** in R^(N x d), sigma = 1/sqrt(d), and softmax is applied row-wise. FlashAttention-3 maintains the same tiling and online softmax approach as FlashAttention-2 -- computing attention in blocks without materializing the full N x N matrices **S** and **P** to HBM -- but redesigns the execution to exploit Hopper's asynchronous hardware.

The forward pass is embarrassingly parallel over batch size, number of heads, and query blocks. At the CTA (thread block) level, each CTA processes one query tile **Q**_i to compute the corresponding output tile **O**_i.

### Key Technical Components

#### 1. Producer-Consumer Asynchrony via Warp-Specialization (Section 3.1)

The warps within a CTA are divided into **producer** and **consumer** roles:

**Producer warpgroup:**
- Deallocates registers (via `setmaxnreg`) since TMA needs minimal registers
- Issues TMA loads of **Q**_i and {**K**_j, **V**_j} from HBM to shared memory
- Manages an s-stage circular SMEM buffer with barrier synchronization
- Due to TMA asynchrony, issuing loads does not stall on completion of prior loads

**Consumer warpgroup:**
- Reallocates freed registers (via `setmaxnreg`) for larger RMEM share
- Initializes **O**_i = 0, l_i = 0, m_i = -infinity on-chip
- In the mainloop over key/value blocks j = 0,...,T_r - 1:
  - Waits for **K**_j, computes **S**_i^(j) = **Q**_i **K**_j^T (SS-GEMM via WGMMA)
  - Computes online softmax: m_i, **P~**_i^(j), l_i
  - Waits for **V**_j, computes **O**_i update with rescaling (RS-GEMM via WGMMA)
- Final: **O**_i = diag(l_i)^(-1) **O**_i, L_i = m_i + log(l_i)

This is Algorithm 1 in the paper.

#### 2. Pingpong Scheduling (Section 3.1)

With two consumer warpgroups, synchronization barriers (`bar.sync`) force the GEMMs of warpgroup 1 to be scheduled before warpgroup 2. This causes:
- Softmax of warpgroup 1 to execute while warpgroup 2 performs its GEMMs
- Then roles swap: warpgroup 2 does softmax while warpgroup 1 does GEMMs

**Impact:** Performance improves from **570 TFLOPs/s to 620-640 TFLOPs/s** for FP16 forward with head dimension 128 and sequence length 8192 (Section 3.1).

#### 3. Intra-Warpgroup 2-Stage GEMM-Softmax Pipelining (Section 3.2)

Even within one warpgroup, sequential dependencies between softmax and GEMMs can be broken by pipelining across iterations. In the mainloop (Algorithm 2, iteration j):

- Line 9: Compute **S**_next = **Q**_i **K**_j^T using WGMMA. **Commit but do not wait.**
- Line 11: Compute **O**_i += **P**_cur **V**_{j-1} using WGMMA. **Commit but do not wait.**
- Line 13: While WGMMAs execute asynchronously, compute m_i, **P**_next, l_i from **S**_next
- Line 14: Wait for the PV WGMMA, then rescale **O**_i

This overlaps the second WGMMA of iteration j (line 11) with softmax from iteration j+1 (line 13).

**SASS analysis (Appendix B.2)** confirms the compiler generates overlapped code as expected: the first WGMMA is interleaved with softmax and FP32-to-FP16 conversion, while the second WGMMA is not overlapped with other instructions.

**Register pressure trade-off:** The 2-stage pipeline requires extra B_r x B_c x sizeof(float) registers for **S**_next, limiting maximum block sizes.

#### 4. 3-Stage Pipelining (Appendix B.3)

A 3-stage variant attempts to further overlap the second WGMMA with softmax. However, it performs worse in practice because (a) the compiler does not cooperate -- SASS shows only the first WGMMA is overlapped with softmax -- and (b) it requires even more registers (an extra **P**_i and scale_o of size B_r x B_c x sizeof(input_data_type) + B_r x sizeof(float)), forcing smaller block sizes.

#### 5. FP8 Low-Precision Support (Section 3.3)

**Layout transformations for FP8 WGMMA:**

FP8 WGMMA on Hopper only accepts k-major input operands (unlike FP16 which also accepts nn-major). Since **V** is typically contiguous in the head dimension, FlashAttention-3 performs **in-kernel transpose** of **V** tiles using LDSM (ldmatrix) and STSM (stmatrix) instructions, which collectively load/store 128-byte blocks and can transpose layouts. The transpose is executed in the producer warpgroup and can be overlapped with the two consumer WGMMAs.

Additionally, the FP32 accumulator layout of an FP8 WGMMA differs from the FP8 operand layout (Figures 3-4). **Byte permute instructions** transform the first WGMMA's accumulator into a column-major format suitable for the second WGMMA, and the in-kernel transpose writes a matching row permutation of the **V** tile.

**Block quantization:** Instead of per-tensor scaling (one scalar per tensor), FlashAttention-3 keeps **one scalar per block** of size B_r x d or B_c x d. Since the algorithm naturally operates on blocks, scaling each block of **S** incurs no additional computation cost.

**Incoherent processing:** Multiply **Q** and **K** by a random orthogonal matrix **M** before FP8 quantization:

> (**QM**)(**KM**)^T = **QMM**^T**K**^T = **QK**^T (since **MM**^T = **I**)

This spreads out outlier values across entries, reducing quantization error. Following Chee et al. (2024) -- *QuIP* and Tseng et al. (2024) -- *QuIP#*, **M** is chosen as the product of random diagonal matrices of +/-1 and a Hadamard matrix, computable in O(d log d) instead of O(d^2), and fuseable with rotary embedding at no extra cost.

#### 6. Backward Pass with Warp-Specialization (Appendix B.1)

The backward pass uses a more sophisticated warp-specialization pattern than the forward pass. Beyond producer and consumer roles, it includes a dedicated **dQ-writer warp** that atomically accumulates dQ_i^(local) from each thread block to the global dQ in HBM using a semaphore. This avoids blocking the consumer warps during the memory-contentious dQ accumulation. The backward pass mainloop computes five GEMMs per iteration: S_i^(j) = Q_i K_j^T (SS-GEMM), dP_i^(j) = dO_i V_j^T (SS-GEMM), dV_j += P^T dO_i (RS-GEMM), dK_j += dS^T Q_i (RS-GEMM), and dQ_i^(local) = dS_i^(j) K_j (SS-GEMM).

### Experimental Setup

**Hardware:** H100 80GB SXM5 GPU (700W), clock speed fixed to 1830 MHz for reproducible benchmarks. All results averaged over 100 runs (Appendix C.1).

**Software:** CUDA 12.3, cuDNN 9.1.1.17, CUTLASS 3.5, FlashAttention 2.5.8, Triton nightly 3.0.0, PyTorch 2.3.0 (Appendix C.1).

**Attention benchmarks:**
- Sequence lengths: 512, 1K, 2K, 4K, 8K, 16K
- Batch size: set so total tokens = 16K
- Hidden dimension: 2048
- Head dimensions: 64, 128, or 256 (i.e., 32, 16, or 8 heads)
- For FP8 with sequence length >= 4K, lengths are divisible by 132 (number of SMs) to avoid wave quantization

**FLOPs calculation:**
- Forward pass: 4 x seqlen^2 x head_dim x num_heads
- With causal mask: divide by 2
- Backward pass: 2.5x forward FLOPs (5 matmuls vs 2)

**Baselines:** Standard attention (PyTorch), FlashAttention-2, FlashAttention-2 in Triton (with H100-specific instructions), cuDNN 9 (vendor-optimized, closed-source)

**Ablation:** Fixed configuration (batch=4, seqlen=8448, nheads=16, hdim=128), FP16, non-causal

**Numerical error:** Entries of Q, K, V drawn from N(0,1) + N(0,100) * Bernoulli(0.001) to simulate outlier features. Reference implementation in FP64. RMSE metric.

**Reproducibility:** Code open-sourced at https://github.com/Dao-AILab/flash-attention under permissive license. Hardware settings (fixed clock speed), software versions, and averaging procedure are documented. No variance estimates reported across runs (limited evidence for variability characterization).

### Key Results

**FP16 Forward Pass (H100 SXM5, approximate TFLOPS/s read from Figure 5):**

| Setting | FlashAttention-2 | cuDNN | FlashAttention-3 |
|---------|------------------|-------|------------------|
| No causal, d=64, 16K | [not in notes] | [not in notes] | ~497 |
| Causal, d=64, 16K | [not in notes] | [not in notes] | ~475 |
| No causal, d=128, 16K | [not in notes] | [not in notes] | ~649 |
| Causal, d=128, 16K | [not in notes] | [not in notes] | ~616 |
| No causal, d=256, 16K | [not in notes] | [not in notes] | ~756 |
| Causal, d=256, 16K | [not in notes] | [not in notes] | ~642 |

- FlashAttention-3 is **1.5-2.0x faster** than FlashAttention-2 in the forward pass, reaching up to **~756 TFLOPs/s (75% of 989 TFLOPs/s theoretical max)** at head dimension 256 (Figure 5, Section 4.1).
- FlashAttention-3 consistently achieves the highest speeds across all settings. Performance improvements are most pronounced at longer sequence lengths (8K, 16K) (Figure 5).
- Standard attention performs significantly worse, typically <200 TFLOPs/s (Figure 5).
- For medium and long sequences (1K+), FlashAttention-3 surpasses cuDNN (Section 4.1) (single GPU, single configuration per setting, no variance reported -- moderate evidence).

**FP16 Backward Pass (H100 SXM5, approximate TFLOPs/s from Figure 6):**

| Setting | FlashAttention-3 |
|---------|------------------|
| No causal, d=64, 16K | ~476 |
| No causal, d=128, 16K | ~581 |

- FlashAttention-3 achieves **1.5-1.75x speedup** over FlashAttention-2 in the backward pass (Section 4.1, Figure 6). The performance gap increases with sequence length (tested on 2 head dimensions without causal mask only -- limited evidence for causal backward pass).

**FP8 Forward Pass (H100 SXM5, approximate TFLOPs/s from Figure 7 and Appendix C.2 Figure 9):**

| Setting | Triton | cuDNN | FlashAttention-3 |
|---------|--------|-------|------------------|
| No causal, d=64, 16K | [not in notes] | [not in notes] | ~615 |
| Causal, d=64, 16K | [not in notes] | [not in notes] | ~575 |
| No causal, d=128, 16K | [not in notes] | [not in notes] | ~1,000 |
| Causal, d=128, 16K | [not in notes] | [not in notes] | ~850 |
| No causal, d=256, 16K | [not in notes] | [not in notes] | ~1,171 |
| Causal, d=256, 16K | [not in notes] | [not in notes] | ~1,056 |

- FlashAttention-3 FP8 reaches close to **1.2 PFLOPs/s** (~1,171 TFLOPs/s at head dim 256 without causal mask, Figure 7a).
- FlashAttention-3 consistently outperforms Triton and cuDNN across all FP8 configurations. The advantage is most pronounced at longer sequences and larger head dimensions (Appendix C.2).
- **Limitation:** For head dimensions 128 and 256 with causal masking, FP8 FlashAttention-3 is competitive with but sometimes behind cuDNN (footnote 2 in Section 1), partly because the FP8 kernel lacks persistent kernel design and load balancing (footnote 10 in Section 5).

**Ablation Study (Table 2, FP16, non-causal, batch=4, seqlen=8448, nheads=16, hdim=128):**

| Configuration | Time | TFLOPs/s |
|---------------|------|----------|
| FlashAttention-3 (full) | 3.538 ms | 661 |
| No GEMM-Softmax Pipelining, with Warp-Specialization | 4.021 ms | 582 |
| GEMM-Softmax Pipelining, No Warp-Specialization | 4.105 ms | 570 |

- Both warp-specialization and GEMM-softmax pipelining contribute to the speedup. Without either, performance is 570 TFLOPs/s; with both, it reaches 661 TFLOPs/s (Section 4.2, Table 2). This is a **16% improvement** from the combined techniques (single configuration -- limited evidence for generality across settings).

**Numerical Error (Table 3, with simulated outlier features):**

| Method | RMSE |
|--------|------|
| Standard attention FP16 | 3.2e-4 |
| FlashAttention-2 FP16 | 1.9e-4 |
| FlashAttention-3 FP16 | 1.9e-4 |
| Baseline FP8 (per-tensor quantization) | 2.4e-2 |
| FlashAttention-3 FP8 (block quant + incoherent) | 9.1e-3 |
| FlashAttention-3 FP8 (no block quantization) | 9.3e-3 |
| FlashAttention-3 FP8 (no incoherent processing) | 2.4e-2 |

- In FP16, both FlashAttention-2 and FlashAttention-3 achieve **1.7x lower RMSE** than standard attention because intermediate softmax results are kept in FP32 (Section 4.3).
- In FP8, FlashAttention-3 with block quantization and incoherent processing achieves **2.6x lower RMSE** (9.1e-3 vs 2.4e-2) compared to baseline FP8 with per-tensor quantization (Table 3).
- Ablation shows **incoherent processing is the critical component**: without it, RMSE reverts to 2.4e-2 (same as baseline). Removing block quantization alone has modest impact (9.3e-3 vs 9.1e-3) (Table 3, single distribution tested -- limited evidence for other outlier patterns).

---

## Limitations and Failure Modes

1. **Hopper-specific.** The techniques are designed for and validated on NVIDIA Hopper H100 architecture. Generalization to other hardware (e.g., AMD MI300) is discussed as plausible but not validated (Section 5).

2. **FP8 kernel lacks persistent design.** FP16 FlashAttention-3 uses a persistent kernel and load balancing, but the FP8 kernel does not. This partly explains why FP8 FlashAttention-3 underperforms cuDNN for small sequence lengths and causal masking (footnote 10, Section 5).

3. **FP8 causal masking performance.** For head dimensions 128 and 256 with causal masking, FP8 FlashAttention-3 is behind cuDNN. For head dimension 64, FP8 is ahead; for dimensions 128 and 256 without causal masking, it is at par (footnote 2, Section 1).

4. **LLM inference not optimized.** The paper focuses on training workloads; inference optimization with different batch sizes and memory access patterns is left for future work (Section 5).

5. **Effects of FP8 on large-scale training unknown.** The paper validates FP8 accuracy on synthetic benchmarks with simulated outliers but does not evaluate effects on actual large-scale model training quality (Section 5).

6. **3-stage pipelining underperforms.** The more aggressive 3-stage pipeline does not improve over 2-stage because the compiler fails to overlap the second WGMMA with softmax, and the extra register pressure forces smaller block sizes (Appendix B.3).

7. **[Inferred]** No variance estimates reported across benchmark runs. While 100 repetitions are averaged, no standard deviations or confidence intervals are provided.

8. **[Inferred]** Manual tuning required for block sizes and pipeline parameters across different head dimensions and precisions.

9. **[Inferred]** Backward pass benchmarked only for head dimensions 64 and 128 without causal masking (Figure 6), leaving causal backward pass and head dimension 256 backward pass performance unknown.

### Scope and Comparability

- **What was not tested:** End-to-end training throughput with FlashAttention-3 in a full model; LLM inference latency; multi-GPU distributed attention; actual model training quality with FP8 attention; non-Hopper hardware; backward pass with FP8; backward pass with causal masking.
- **Comparability notes:** cuDNN is closed-source, so implementation details cannot be compared directly. GPU clock speed is fixed to 1830 MHz, which is below the boost clock; results at different clock speeds may differ. FP8 baselines use per-tensor quantization (the simplest approach); more sophisticated per-channel or per-token quantization baselines are not included. The FLOPs calculation counts all operations including those skipped by causal masking (dividing by 2 for causal), which is a standard but potentially imprecise accounting.

---

## Conclusions

### Contributions

1. **Identified and diagnosed the utilization gap.** Showed that FlashAttention-2 achieves only 35% utilization on H100 because it does not exploit asynchronous execution or low-precision capabilities.

2. **Warp-specialized producer-consumer asynchrony.** Developed a scheme that separates TMA data movement and Tensor Core computation into separate warps with dynamic register reallocation via `setmaxnreg`.

3. **Pingpong scheduling for inter-warpgroup overlap.** Demonstrated that scheduling GEMMs of one warpgroup while the other computes softmax improves performance from 570 to 620-640 TFLOPs/s for FP16 forward (Section 3.1).

4. **2-stage GEMM-softmax pipeline for intra-warpgroup overlap.** Designed a pipeline that breaks sequential dependencies between iterations, overlapping the second WGMMA with next-iteration softmax (Algorithm 2).

5. **FP8 support with block quantization and incoherent processing.** Enabled FP8 Tensor Cores through in-kernel V transpose, byte permute accumulator layout transformation, and two accuracy techniques that reduce FP8 error by 2.6x (Table 3).

6. **1.5-2.0x forward pass speedup, 1.5-1.75x backward pass speedup.** Reached up to ~756 TFLOPs/s FP16 (75% utilization) and ~1.2 PFLOPs/s FP8 on H100.

### Implications

1. **Exact attention approaches hardware ceiling.** At 75% utilization, exact attention is approaching the efficiency of pure GEMM kernels (80-90%), which substantially reduces the practical incentive for approximate attention methods at moderate sequence lengths.

2. **FP8 training viability.** Block quantization and incoherent processing demonstrate a path toward FP8 attention in training, though large-scale validation remains needed (speculative).

3. **Portable design principles.** Although demonstrated on Hopper, the asynchrony-first algorithm design should apply to any GPU architecture with robust asynchronous execution and low-precision capabilities (speculative, per footnote 1 in Section 1).

4. **Benefits to distributed and variant attention.** Since Ring attention and similar distributed methods use FlashAttention as a primitive, the 1.5-2.0x speedup directly benefits these approaches. Similarly, MQA, GQA, and MLA all benefit since they share the same core softmax(QK^T)V computation (Appendix A).

---

## Key Claims

**C1. FlashAttention-2 achieves only 35% utilization on H100.** Compared to 80-90% for optimized GEMM kernels (Section 1, Abstract). Scope: H100 GPU. Status: **supported**.

**C2. FlashAttention-3 achieves 1.5-2.0x speedup over FlashAttention-2 in FP16 forward pass.** Across head dimensions 64, 128, 256, with and without causal masking, on H100 SXM5 (Figure 5, Section 4.1). Tested across 6 head-dim/masking configurations and 6 sequence lengths (moderate evidence). Status: **supported**.

**C3. FlashAttention-3 FP16 reaches ~756 TFLOPs/s (75% utilization).** At head dimension 256 without causal mask at 16K sequence length (Figure 5e). Single GPU, single configuration at peak (limited evidence for peak claim). Status: **supported**.

**C4. FlashAttention-3 FP8 reaches ~1.2 PFLOPs/s.** At head dimension 256 without causal mask (~1,171 TFLOPs/s, Figure 7a). Single configuration at peak (limited evidence). Status: **supported**.

**C5. FP8 FlashAttention-3 achieves 2.6x lower numerical error than baseline.** RMSE 9.1e-3 vs 2.4e-2 for per-tensor quantization baseline (Table 3). Scope: simulated outlier distribution N(0,1) + N(0,100)*Bernoulli(0.001). Single distribution tested (limited evidence for generality). Status: **supported**.

**C6. Non-matmul operations have 256x lower throughput on H100.** 989 TFLOPs/s for FP16 matmul vs 3.9 TFLOPs/s for special functions (Section 3.1). Derived from hardware specifications (strong evidence). Status: **supported**.

**C7. Combined warp-specialization and GEMM-softmax pipelining yield 16% improvement.** From 570 to 661 TFLOPs/s (Table 2). Single configuration (batch=4, seqlen=8448, nheads=16, hdim=128, FP16, non-causal) -- limited evidence for generality. Status: **supported**.

**C8. FlashAttention-3 achieves 1.5-1.75x speedup in FP16 backward pass.** Up to ~581 TFLOPs/s at head dim 128 (Figure 6). Tested on 2 head dimensions without causal mask (limited evidence). Status: **supported**.

**C9. Pingpong scheduling improves performance from 570 to 620-640 TFLOPs/s.** For FP16 forward with head dimension 128 and sequence length 8192 (Section 3.1). Reported as general observation, not rigorously ablated in isolation (limited evidence). Status: **supported**.

---

## Open Questions

1. **Hardware generalization.** The techniques are developed for Hopper GPUs. How well do they generalize to other architectures with asynchronous execution and low-precision support (e.g., AMD MI300, NVIDIA Blackwell with FP4)?

2. **Large-scale FP8 training.** The accuracy of FP8 attention is validated on synthetic benchmarks with simulated outliers. What are the effects on actual large-scale model training quality across diverse tasks?

3. **FP8 kernel improvements.** Can persistent kernel design and better load balancing improve FP8 performance, especially for causal masking and smaller sequence lengths where cuDNN currently leads?

4. **Inference optimization.** The paper focuses on training workloads. How should FlashAttention-3 be adapted for LLM inference with different batch sizes, memory access patterns, and latency constraints?

5. **Backward pass FP8.** The paper only benchmarks FP8 for the forward pass. What speedups and accuracy trade-offs exist for FP8 in the backward pass?

---

## Core References and Why They Are Referenced

### FlashAttention Lineage

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* The original IO-aware attention algorithm that introduced tiling to fuse all attention operations into a single GPU kernel, avoiding intermediate reads/writes to HBM.

- **Dao (2023)** -- *FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning.* The direct predecessor. Restructured the algorithm to parallelize over the sequence length dimension and iterate the inner loop over key/value blocks. Achieves 35% utilization on H100 -- the gap that FlashAttention-3 addresses.

- **Rabe & Staats (2021)** -- *Self-Attention Does Not Need O(n^2) Memory.* Showed attention can be computed in O(n) memory, a foundational observation for the FlashAttention line of work.

### GPU Architecture and Optimization

- **NVIDIA (2024)** -- *CUDA Programming Guide and PTX ISA Version 8.4.* Documents TMA, WGMMA, setmaxnreg, and other Hopper-specific instructions that FlashAttention-3 relies on.

- **Bauer et al. (2011)** -- *CudaDMA: Optimizing GPU Memory Bandwidth via Warp Specialization.* Introduced the warp-specialization concept of dividing warps into producer and consumer roles for data movement and computation.

- **Thakkar et al. (2023)** -- *CUTLASS.* The NVIDIA template library providing WGMMA and TMA abstractions used in FlashAttention-3's implementation.

- **Luo et al. (2024)** -- *Benchmarking and Dissecting the Nvidia Hopper GPU Architecture.* Provides shared memory bandwidth measurements (128 bytes per clock per SM) used to derive the 31 TB/s SMEM bandwidth figure in Table 1.

- **NVIDIA (2024)** -- *Accelerating Transformers with cuDNN 9.* cuDNN's H100-optimized attention kernels serve as a key baseline.

### Low-Precision and Quantization

- **Chee et al. (2024)** -- *QuIP: 2-bit Quantization of Large Language Models with Guarantees.* Introduced incoherent processing for weight quantization, adapted by FlashAttention-3 for FP8 attention.

- **Tseng et al. (2024)** -- *QuIP#: Even Better LLM Quantization with Hadamard Incoherence and Lattice Codebooks.* Refined incoherent processing with Hadamard matrices (O(d log d) multiplication), directly adopted by FlashAttention-3.

- **Micikevicius et al. (2022)** -- *FP8 Formats for Deep Learning.* Defines the e4m3 and e5m2 FP8 formats supported by Hopper Tensor Cores.

- **Dettmers et al. (2022)** -- *LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale.* Documents outlier features in LLMs that motivate FlashAttention-3's block quantization and incoherent processing.

- **Sun et al. (2024)** -- *Massive Activations in Large Language Models.* Further documents outlier activations in LLMs, motivating the synthetic outlier distribution used in accuracy validation.

### Transformer and Attention Variants

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture whose multi-head attention mechanism FlashAttention-3 optimizes.

- **Shazeer (2019)** -- *Fast Transformer Decoding: One Write-Head Is All You Need.* Introduced multi-query attention (MQA), supported by FlashAttention-3 with adjusted tensor indexing.

- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models.* Introduced grouped-query attention (GQA), also supported by FlashAttention-3.

### Alternative Architectures (Context)

- **Gu & Dao (2023)** -- *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* State space model alternative; the paper notes that highest-quality large RNN-based models still employ attention layers.

- **Peng et al. (2023)** -- *RWKV: Reinventing RNNs for the Transformer Era.* Linear-complexity alternative; the paper argues FlashAttention-3 techniques may benefit these architectures.

### Efficient and Distributed Attention (Context)

- **Liu et al. (2023)** -- *Ring Attention with Blockwise Transformers for Near-Infinite Context.* Distributed attention using FlashAttention as a primitive; directly benefits from FlashAttention-3 speedups.

- **Spector et al. (2024)** -- *ThunderKittens.* Hopper-specific tile-based attention implementation referenced as concurrent work showing Hopper-specific instructions can speed up attention.

- **Golden et al. (2024)** -- *Is Flash Attention Stable?* Motivates the numerical error validation in Section 4.3.
