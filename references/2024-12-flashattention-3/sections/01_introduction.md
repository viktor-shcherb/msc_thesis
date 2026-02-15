# 1 Introduction [p. 1-2]

## Core Problem

[p. 1] For the Transformer architecture [59], the attention mechanism constitutes the primary computational bottleneck, since computing the self-attention scores of queries and keys has quadratic scaling in the sequence length. Scaling attention to longer context raises new challenges (modeling over long documents [24, 43, 50] and files in large codebases [30, 48]), new modalities (high-resolution images [11], audio [23], video [25]), and new applications (user interaction with long history [33], agent workflow with long horizon [62]). This has generated significant interest in testing attention efficiency in the ML community, including by approximation [14, 27, 56] and software optimization ([17, 29, 45]), or even alternative architectures [22, 42, 55].

## Prior Work on Flash Attention

[p. 1-2] In this work, we build on the second of Dao et al. [17] on I/O-aware attention algorithms that integrate knowledge of the GPU's execution model and hardware characteristics into their high-level design. In [17], Dao et al. introduced FLASHATTENTION, a novel tiling strategy for parallelizing attention that changes intermediate reads/writes to slow global memory through fusing all of the attention operations into a single GPU kernel. Dao [15] restructured the algorithm as FLASHATTENTION-2 to also parallelize over the sequence length dimension and performs the inner loop of the forward pass over blocks of the key and value matrices, thus improving the occupancy and distribution of work on the GPU. However, we observe that FLASHATTENTION-2 nonetheless achieves poor utilization on newer GPUs relative to optimized matrix-multiplication (GEMM) kernels, such as 35% vs. 80-90% on the Hopper H100 GPU. Partially, this may be attributed to implementation-level differences, such as not using Hopper-specific instructions in place of Ampere ones when targeting the Tensor Cores. Several work such as ThunderKitten [52] and cuDNN 9 [39] has shown that with Hopper-specific instructions and tile-based abstractions, one can speedup attention computation and simplify the implementation.

## FlashAttention-2 Limitations

[p. 2] More fundamentally, FLASHATTENTION-2's algorithm adheres to a simplified synchronous model and makes no explicit use of asynchrony and low-precision in its design. Asynchrony is a result of hardware specialization to accelerate the most important operations in a ML workload: specific hardware units performing matrix multiplication (Tensor Cores or memory loading (Tensor Memory Accelerator – TMA) separate from the core of the CUDA cores performing logic, integer, and floating point computation. Low precision such as FP8 in Hopper and FP4 in Blackwell, continuing the trend of FP16 (Pascal in 2017) and BF16 (Ampere in 2020), is a proven technique to get double or quadruple throughput in the same power and chip area. We review the capabilities afforded by Hopper in these directions in §2.2. The technical challenge is to redesign FLASHATTENTION-2 to make use of these hardware features: asynchrony requires overlapping computation between input and output even though one depends on the output of the other, and low-precision requires care to minimize quantization error, especially in the case of outlier features in LLMs [20, 54].

## FlashAttention-3 Contributions

[p. 2] To this end, we propose FLASHATTENTION-3, which contributes and synthesizes three new ideas to further improve performance on newer GPU architectures¹:

1. **Producer-Consumer asynchrony:** We define a warp-specialized software pipelining scheme that exploits the asynchronous execution of data movement Tensor Memory Accelerator (TMA), splitting producers and consumers of data into separate warps, thereby extending the algorithm's ability to hide memory and instruction issue latencies.

2. **Hiding softmax under asynchronous block-wise GEMMs:** We overlap the computationally low-throughput non-GEMM operations involved in softmax, such as floating point multiply-add and exponentiation, with the asynchronous WGMMA instructions for GEMM. As part of this, we rework the FLASHATTENTION-2 algorithm to circumvent certain sequential dependencies between softmax and the GEMMs. For example, in the 2-stage version of our algorithm, while softmax executes on one block of the scores matrix, WGMMA executes in the asynchronous proxy to compute the next block.

3. **Hardware-accelerated low-precision GEMM:** We adapt the forward pass algorithm to allow for targeting the FP8 Tensor Cores for GEMM, nearly doubling the measured TFLOPs/s. This requires bridging the different layout conformance requirements of WGMMA in terms of how blocks of FP32 accumulator and FP8 operand matrices are assumed to be laid out in memory. We use the techniques of block quantization and incoherent processing to mitigate the numerical accuracy cost resulting from moving to FP8 precision.

## Empirical Validation

[p. 2] To validate our method empirically, we benchmark FLASHATTENTION-3 on the H100 SXM5 GPU over a range of parameters and show that (1) FP16 achieves 1.5-2.0× speedup over FLASHATTENTION-2 in the forward pass (reaching up to 740 TFLOPs/s) and 1.5-1.8× in the backward pass (up to 450 TFLOPs/s), and (3) for large sequence length, FP16 outperforms and FP8 are competitive², with a state-of-the-art implementation of attention from NVIDIA's cuDNN library. We also validate that FP16 FLASHATTENTION-3 yields the same numerical error as FLASHATTENTION-2 and other baseline attention implementations is intermediate results (e.g., softmax rescaling) are kept in FP32. Moreover, FP8 FLASHATTENTION-3 with block quantization and incoherent processing is 2.6× more accurate than standard attention with per-tensor quantization in cases with outlier features.

[p. 2] We open-source FLASHATTENTION-3 with a permissive license³ and plan to integrate it with PyTorch and Hugging Face libraries to benefit the largest number of researchers and developers.

---

**Footnotes:**

¹ We describe our results in the context of NVIDIA's Hopper architecture. However, our algorithm is operative for any GPU architecture with sufficiently robust asynchronous execution and low-precision capabilities.

² More precisely, for head dimension 64 FLASHATTENTION-3 FP8 is ahead, while for head dimensions 128 and 256 it is at par for these cases without causal masking and behind with causal masking.

³ FLASHATTENTION-3 is available at https://github.com/Dao-AILab/flash-attention
