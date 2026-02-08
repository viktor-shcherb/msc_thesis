# 1 Introduction [p. 1-3]

[p. 1]

Transformer models [82] have emerged as the most widely used architecture in applications such as natural language processing and image classification. Transformers have grown larger [5] and deeper [83], but equipping them with longer context remains difficult [80], since the self-attention module at their heart has time and memory complexity quadratic in sequence length.

Many approximate attention methods have aimed to reduce the compute and memory requirements of attention. These range from sparse-approximation [51, 74] to low-rank approximation [12, 50, 84], and their combinations [3, 9, 92]. Although these methods reduce the compute requirements to linear or near-linear in sequence length, many do not display wall-clock speedup against standard attention and have not gained wide adoption. One main reason is that they focus on FLOP reduction (which may not correlate with wall-clock speed) and tend to ignore overheads from memory access (IO).

The authors argue that a missing principle is making attention algorithms *IO-aware* [1] -- carefully accounting for reads and writes to different levels of fast and slow memory (e.g., between fast GPU on-chip SRAM and relatively slow GPU high bandwidth memory, or HBM [45], Figure 1 left).

[p. 2]

On modern GPUs, compute speed has out-paced memory speed [61, 62, 63], and most operations in Transformers are bottlenecked by memory accesses [43]. IO-aware algorithms have been critical for similar memory-bound operations, such as database joins [71], image processing [70], numerical linear algebra [4], and more [40, 85]. However, common Python interfaces to deep learning such as PyTorch and TensorFlow do not allow fine-grained control of memory access.

## Proposal

FlashAttention computes exact attention with far fewer memory accesses. The main goal is to avoid reading and writing the attention matrix to and from HBM. Two well-established techniques are applied:

1. **Tiling:** Restructure the attention computation to split the input into blocks and make several passes over input blocks, incrementally performing the softmax reduction.
2. **Recomputation:** Store the softmax normalization factor from the forward pass to quickly recompute attention on-chip in the backward pass, which is faster than reading the intermediate attention matrix from HBM.

FlashAttention is implemented in CUDA to achieve fine-grained control over memory access and fuses all the attention operations into one GPU kernel. Even with increased FLOPs due to recomputation, the algorithm both **runs faster** (up to 7.6x on GPT-2 [67], Figure 1 right) and **uses less memory** -- linear in sequence length -- than standard attention, thanks to the massively reduced amount of HBM access.

## IO Complexity

The IO complexity of FlashAttention requires $O(N^2 d^2 M^{-1})$ HBM accesses where $d$ is the head dimension and $M$ is the size of SRAM, as compared to $\Omega(Nd + N^2)$ of standard attention. For typical values of $d$ and $M$, FlashAttention requires many times fewer HBM accesses compared to standard attention (up to 9x fewer, as shown in Fig. 2). The authors also provide a lower bound, showing that no exact attention algorithm can asymptotically improve on the number of HBM accesses over all SRAM sizes.

## Block-Sparse FlashAttention

FlashAttention can serve as a useful primitive for realizing the potential of approximate attention algorithms by overcoming their issues with memory access overhead. As a proof of concept, the authors implement block-sparse FlashAttention, a sparse attention algorithm that is 2-4x faster than even FlashAttention, scaling up to sequence length of 64k. Block-sparse FlashAttention has better IO complexity than FlashAttention by a factor proportional to the sparsity ratio. Further extensions to other operations (attention on multi-GPU, kernel regression, block-sparse matrix multiply) are discussed in Section 5. FlashAttention is open-sourced.

[p. 3]

## Key Contributions (stated by authors)

- **Faster Model Training.** FlashAttention trains Transformer models faster in wall-clock time. They train BERT-large (seq. length 512) 15% faster than the training speed record in MLPerf 1.1 [58], GPT2 (seq. length 1K) 3x faster than baseline implementations from HuggingFace [87] and Megatron-LM [77], and long-range arena (seq. length 1K-4K) 2.4x faster than baselines.

- **Higher Quality Models.** FlashAttention scales Transformers to longer sequences, improving quality and enabling new capabilities. They observe a 0.7 improvement in perplexity on GPT-2 and 6.4 points of lift from modeling longer sequences on long-document classification [13]. FlashAttention enables the first Transformer that can achieve better-than-chance performance on the Path-X [80] challenge, solely from using a longer sequence length (16K). Block-sparse FlashAttention enables a Transformer to scale to even longer sequences (64K), resulting in the first model that can achieve better-than-chance performance on Path-256.

- **Benchmarking Attention.** FlashAttention is up to 3x faster than the standard attention implementation across common sequence lengths from 128 to 2K and scales up to 64K. Up to sequence length of 512, FlashAttention is both faster and more memory-efficient than any existing attention method, whereas for sequence length beyond 1K, some approximate attention methods (e.g., Linformer) start to become faster. On the other hand, block-sparse FlashAttention is faster than all existing approximate attention methods that they know of.

**Figure 1** (p. 2): "Left: FlashAttention uses tiling to prevent materialization of the large N x N attention matrix (dotted box) on (relatively) slow GPU HBM. In the outer loop (red arrows), FlashAttention loops through blocks of the K and V matrices and loads them to fast on-chip SRAM. In each block, FlashAttention loops over blocks of Q matrix (blue arrows), loading them to SRAM, and writing the output of the attention computation back to HBM. Right: Speedup over the PyTorch implementation of attention on GPT-2. FlashAttention does not read and write the large N x N attention matrix to HBM, resulting in an 7.6x speedup on the attention computation."

The figure shows:
- **Left panel:** GPU memory hierarchy diagram showing SRAM (19 TB/s, 20 MB), HBM (1.5 TB/s, 40 GB), and Main Memory/DRAM (12.8 GB/s, >1 TB). The FlashAttention tiling scheme is illustrated with K^T (d x N) and V (N x d) being loaded in an outer loop, Q (N x d) loaded in an inner loop, computation done on SRAM, and output sm(QK^T)V (N x d) written to HBM.
- **Right panel:** Bar chart comparing PyTorch vs FlashAttention attention time on GPT-2. PyTorch shows ~15ms total (broken down into Matmul, Dropout, Softmax, Mask, Matmul components). FlashAttention shows ~2ms total as a single "Fused Kernel."
