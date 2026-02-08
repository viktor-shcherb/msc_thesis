# 1 Introduction [p. 1-2]

[p. 1] Scaling up the context length of Transformers [18] is a challenge, since the attention layer has runtime and memory requirements quadratic in the input sequence length. Ideally, going beyond the standard 2k sequence length limit is needed to train models to understand books, high resolution images, and long-form videos.

Several recent language models with much longer context than before: GPT-4 [12] with context length 32k, MosaicML's MPT with context length 65k, and Anthropic's Claude with context length 100k. Emerging use cases such as long document querying and story writing have demonstrated a need for models with such long context.

To reduce the computational requirement of attention on such long context, numerous methods have been proposed to approximate attention [2, 3, 4, 8, 9, 14, 19, 20]. Though these methods have seen some use cases, as far as the authors know, most large-scale training runs still use standard attention. Motivated by this, Dao et al. [5] proposed to reorder the attention computation and leverage classical techniques (tiling, recomputation) to significantly speed it up and reduce memory usage from quadratic to linear in sequence length. This yields 2-4x wall-clock time speedup over optimized baselines, up to 10-20x memory saving, with no approximation. As a result FlashAttention has seen wide adoption in large-scale training and inference of Transformers.

Footnote 1: FlashAttention-2 is available at https://github.com/Dao-AILab/flash-attention

[p. 2] However, as context length increases even more, FlashAttention is still not nearly as efficient as other primitives such as matrix-multiply (GEMM). In particular, while FlashAttention is already 2-4x faster than a standard attention implementation, the forward pass only reaches 30-50% of the theoretical maximum FLOPs/s of the device (Fig. 5), while the backward pass is even more challenging, reaching only 25-35% of maximum throughput on A100 GPU (Fig. 6). In contrast, optimized GEMM can reach up to 80-90% of the theoretical maximum device throughput.

Through careful profiling, the authors observe that FlashAttention still has suboptimal work partitioning between different thread blocks and warps on the GPU, causing either low-occupancy or unnecessary shared memory reads/writes.

Building on FlashAttention, FlashAttention-2 is proposed with better parallelism and work partitioning to address these challenges:

1. In Section 3.1, the algorithms are tweaked to reduce the number of non-matmul FLOPs while not changing the output. While the non-matmul FLOPs only account for a small fraction of the total FLOPs, they take longer to perform as GPUs have specialized units for matrix multiply, and as a result the matmul throughput can be up to 16x higher than non-matmul throughput. It is thus important to reduce non-matmul FLOPs and spend as much time as possible doing matmul FLOPs.

2. The authors propose to parallelize both the forward pass and backward pass along the sequence length dimension, in addition to the batch and number of heads dimension. This increases occupancy (utilization of GPU resources) in the case where the sequences are long (and hence batch size is often small).

3. Even within one block of attention computation, the work is partitioned between different warps of a thread block to reduce communication and shared memory reads/writes.

In Section 4, the authors empirically validate that FlashAttention-2 yields significant speedup compared to even FlashAttention. Benchmarks on different settings (with or without causal mask, different head dimensions) show that FlashAttention-2 achieves around 2x speedup over FlashAttention, reaching up to 73% of the theoretical max throughput in the forward pass, and up to 63% of the theoretical max throughput in the backward pass. When used end-to-end to train GPT-style models, they reach training speed of up to 225 TFLOPs/s per A100 GPU.
