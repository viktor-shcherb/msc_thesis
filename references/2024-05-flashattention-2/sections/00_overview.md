# FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning

**Authors:** Tri Dao
**Affiliations:**
- Department of Computer Science, Princeton University
- Department of Computer Science, Stanford University

**Contact:** trid@cs.stanford.edu
**Date:** July 18, 2023
**Venue:** arXiv preprint (arXiv:2307.08691v1)

## Abstract

> "Scaling Transformers to longer sequence lengths has been a major problem in the last several years, promising to improve performance in language modeling and high-resolution image understanding, as well as to unlock new applications in code, audio, and video generation. The attention layer is the main bottleneck in scaling to longer sequences, as its runtime and memory increase quadratically in the sequence length. FlashAttention [5] exploits the asymmetric GPU memory hierarchy to bring significant memory saving (linear instead of quadratic) and runtime speedup (2-4x compared to optimized baselines), with no approximation. However, FlashAttention is still not nearly as fast as optimized matrix-multiply (GEMM) operations, reaching only 25-40% of the theoretical maximum FLOPs/s. We observe that the inefficiency is due to suboptimal work partitioning between different thread blocks and warps on the GPU, causing either low-occupancy or unnecessary shared memory reads/writes. We propose FlashAttention-2, with better work partitioning to address these issues. In particular, we (1) tweak the algorithm to reduce the number of non-matmul FLOPs (2) parallelize the attention computation, even for a single head, across different thread blocks to increase occupancy, and (3) within each thread block, distribute the work between warps to reduce communication through shared memory. These yield around 2x speedup compared to FlashAttention, reaching 50-73% of the theoretical maximum FLOPs/s on A100 and getting close to the efficiency of GEMM operations. We empirically validate that when used end-to-end to train GPT-style models, FlashAttention-2 reaches training speed of up to 225 TFLOPs/s per A100 GPU (72% model FLOPs utilization)." [p. 1]

## Section Headings

1. Introduction
2. Background
   - 2.1 Hardware characteristics
   - 2.2 Standard Attention Implementation
   - 2.3 FlashAttention
     - 2.3.1 Forward pass
     - 2.3.2 Backward pass
3. FlashAttention-2: Algorithm, Parallelism, and Work Partitioning
   - 3.1 Algorithm
     - 3.1.1 Forward pass
     - 3.1.2 Backward pass
   - 3.2 Parallelism
   - 3.3 Work Partitioning Between Warps
4. Empirical Validation
   - 4.1 Benchmarking Attention
   - 4.2 End-to-end Performance
5. Discussion and Future Directions
Acknowledgments
