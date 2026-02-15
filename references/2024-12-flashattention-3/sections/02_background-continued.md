# 2 Background (continued) [p. 4]

## 2.2 GPU hardware characteristics and execution model (continued)

[p. 4] Hardware support for asynchrony allows for warp-specialized kernels, where the warps of a CTA are divided into producer or consumer roles that only ever issue data movement or computation. Generically, this improves the compiler's ability to generate optimal instruction schedules [4]. In addition, Hopper supports the dynamic reallocation of registers between warps by setmaxnreg [40, §7.13], so that consumer warps doing MMAs can obtain a larger share of RMEM than those just issuing TMA (for which only a single thread is needed).

### Low-precision number formats

[p. 4] Modern GPUs have specialized hardware units for accelerating low-precision computation. For example, the WGMMA instruction can target the FP8 Tensor Cores on Hopper to deliver 2x the throughput per SM when compared to FP16 or BF16.

[p. 4] However, correctly invoking FP8 WGMMA entails understanding the layout constraints on its operands. Given a GEMM call to multiply A×B^⊤ for an M × K-matrix A and an N × K-matrix B, we say that the A or B operand is row-major if it is contiguous in the M-dimension and K-dimension, and column-major if it instead contiguous in the inner K-dimension. Then for FP16 WGMMA, both nn-major and k-major input operands are accepted for operands in SMEM, but for FP8 WGMMA, only k-major input operands are accepted, and in some layouts such as attention where one wants to fuse back-to-back GEMMs in a single kernel, clashing FP32 accumulator and FP8 operand layouts pose an obstacle to invoking dependent FP8 WGMMAs.

[p. 4] In the context of attention, these layout restrictions entail certain modifications to the design of an FP8 algorithm, which we describe in §3.3.

## 2.3 Standard Attention and Flash Attention [p. 4]

[p. 4] Following Dao et al. [17], we let **standard attention** denote an implementation of attention on the GPU that materializes the intermediate matrices **S** and **P** to HBM. The main idea of FLASHATTENTION was to leverage a local version of the softmax reduction to avoid these intermediate reads/writes and fuse attention into a single kernel. Local softmax corresponds to lines 18-19 of the consumer mainloop in Algorithm 1 (together with the rescalings of blocks of **O**. The simple derivation that this procedure indeed computes **O** can be found in [15, §2.3.1].

# 3 FlashAttention-3: Algorithm [p. 4]

[p. 4] In this section, we describe the FLASHATTENTION-3 algorithm. For simplicity, we focus on the forward pass, with the backward pass algorithm described in Appendix B.1. We first indicate how to integrate warp-specialization with a circular SMEM buffer into the base design of FLASHATTENTION-2. We then explain how to exploit asynchrony of WGMMA to define an overlapped GEMM-softmax 2-stage pipeline. Finally, we describe the modifications needed for FP8, both in terms of layout conformance and accuracy via block quantization and incoherent processing.
