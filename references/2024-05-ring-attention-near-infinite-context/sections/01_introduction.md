# 1 Introduction [p. 1-2]

[p. 1] Transformers [37] have become the backbone of many state-of-the-art AI systems. They achieve success through self-attention and position-wise feedforward mechanisms. However, scaling up context length is a challenge [29] because self-attention has memory cost quadratic in the input sequence length.

Large context Transformers are essential for processing books, high-resolution images, long videos, complex codebases, interconnected web content, and scientific data. Emerging use cases of language models with expanded context include:
- GPT-3.5 [32] with context length 16K
- GPT-4 [29] with context length 32k
- MosaicML's MPT [25] with context length 65k
- Anthropic's Claude [1] with context length 100k

There has been surging research interest in reducing memory cost. One line of research leverages the observation that the softmax matrix in self-attention can be computed without materializing the full matrix [24], leading to blockwise computation of self-attention and feedforward [30, 9, 23] without making approximations. Despite the reduced memory, a significant challenge remains: storing the output of each layer is necessary because self-attention involves interactions among all elements (n to n interactions). The subsequent layer's self-attention relies on accessing all prior layer outputs. Failing to store them would increase computational costs cubically, as every output must be recomputed for each sequence element.

[p. 2] These components facilitate efficient capture of long-range dependencies and enable scalability through highly parallel computations. Processing 100 million tokens with batch size 1 requires over 1000GB of memory for a modest model with hidden size 1024 — much greater than the capacity of contemporary GPUs and TPUs, which typically have less than 100GB of high-bandwidth memory (HBM).

The key observation is that by performing self-attention and feedforward network computations in a blockwise fashion [23], sequence dimensions can be distributed across multiple devices, allowing concurrent computation and communication. The results of computing attention on a block-by-block basis are invariant to the ordering of blockwise computations. The method distributes the outer loop of computing blockwise attention among hosts, with each device managing its respective input block. For the inner loop, every device computes blockwise attention and feedforward operations specific to its designated input block. Host devices form a conceptual ring: during the inner loop, each device sends a copy of its key-value blocks to the next device in the ring while simultaneously receiving key-value blocks from the previous one. As long as block computations take longer than block transfers, overlapping these processes results in no added overhead compared to standard transformers.

The use of a ring topology for computing self-attention has been studied in prior work [21] but it incurs non-overlapped communication overheads similar to sequence parallelism, making it infeasible for large context sizes. This work utilizes blockwise parallel transformers [23] to substantially reduce memory costs, enabling zero-overhead scaling of context size across tens of millions of tokens during both training and inference, and allowing for arbitrarily large context size.

The authors evaluate effectiveness on language modeling benchmarks. Experiments show that Ring Attention can reduce the memory requirements of Transformers, enabling training of more than 500 times longer sequences than prior memory efficient state-of-the-arts and enabling training of sequences that exceed 100 million in length without making approximations to attention. Ring Attention eliminates the memory constraints imposed by individual devices, empowering training and inference of sequences with lengths that scale in proportion to the number of devices, essentially achieving near-infinite context size.

**Contributions** are twofold: (a) proposing a memory efficient transformers architecture that allows context length to scale linearly with the number of devices while maintaining performance, eliminating the memory bottleneck imposed by individual devices, and (b) demonstrating effectiveness through extensive experiments.

**Figure 1** (p. 2): "Maximum context length under end-to-end large-scale training on TPUv4-1024. Baselines are vanilla transformers [37], memory efficient transformers [30], and memory efficient attention and feedforward (blockwise parallel transformers) [23]. Our proposed approach Ring Attention allows training up to device count times longer sequence than baselines and enables the training of sequences that exceed millions in length without making approximations nor adding any overheads to communication and computation."

Bar chart with log-scale y-axis (Max Context Size) and x-axis showing Model Size (3B, 7B, 13B, 30B). Four methods are compared:
- Vanilla — lowest context sizes, around 2K-4K across model sizes
- Memory Efficient Attn — moderate improvement, around 4K-16K
- Memory Efficient Attn and FFN — further improvement, around 16K-65K
- Ring Attention — highest context sizes, reaching approximately 10M for 3B and scaling down for larger models

Ring Attention achieves orders of magnitude larger context sizes than all baselines across all model sizes.
