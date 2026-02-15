# 4 Empirical Validation [p. 9]

[p. 9] We use the primitives from CUTLASS [57] such as WGMMA and TMA abstractions to implement FLASHATTENTION-3 and evaluate its efficiency and accuracy.

## Overview of validation approach [p. 9]

The empirical validation consists of three main components:

- **Benchmarking attention.** We measure the runtime of FLASHATTENTION-3 across different sequence lengths and compare it to a standard implementation in PyTorch, FLASHATTENTION-2, FLASHATTENTION-2 in Triton (which uses H100-specific instructions), as well as a vendor's implementation of FLASHATTENTION-2 optimized for H100 GPUs. We confirm that FLASHATTENTION-3 is up to 2.0× faster than FLASHATTENTION-2 and 1.5× faster than FLASHATTENTION-2 in Triton. FLASHATTENTION-3 reaches up to 740 TFLOPS/s, 75% of the theoretical maximum TFLOPS/s on H100 GPUs.

- **Ablation study.** We confirm that our algorithmic improvements with warp-specialization and GEMM-softmax pipelining contribute to the speedup of FLASHATTENTION-3.

- **Accuracy of FP8 attention.** We validate that block quantization and incoherent processing reduces the numerical error of FP8 FLASHATTENTION-3 by 2.6×.
