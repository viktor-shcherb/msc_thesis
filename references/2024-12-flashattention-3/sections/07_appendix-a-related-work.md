# A Related Work [p. 17]

## Attention variants and distributed attention

Ever since attention became popular with the Transformer architecture [59], there has been a large body of work on approximating attention to scale it to longer sequences. These approximation methods can generally be categorized into two classes: sparse and low-rank.

**Sparse attention:** Only computes some entries of the attention matrix (estimated K and V) and assumes that other entries are zero. Different methods have different ways of choosing which entries should be zero, either with a fixed pattern [12], with a sliding window [6], or with a dynamic pattern through hashing [28] or routing [47].

**Low-rank approach:** Instead constructs the attention matrix as a low-rank structure, and apply a pointwise nonlinearity to the query and key [27] with random projection [13, 44, 61]. One can also combine the sparse and low-rank approximation for better quality [10, 63].

However, these approximation methods typically do not offer the same model quality as standard attention [56], and so most large-scale models do not employ these techniques.

There are other variants of attention aimed at reducing the size of the KV cache to improve inference efficiency. **Multi-query attention [51]** and **grouped query attention [3]** both reduce the number of heads of K and V, and multiple query heads interact with the same key and value head. **Multi-head latent attention [19]** parameterizes the K and V as low-rank projections of a shared latent matrix to further reduce the KV cache size. These approaches do not change the core computation softmax(QK^T)V during training and simply change how Q, K, V are obtained. As a result, any efficiency or accuracy improvement to the standard attention computation benefits these methods.

To extend to even longer context, attention computation can be distributed across multiple GPUs. Methods such as **Ring attention [31, 32]** and variants [8] can reach a context length of up to 1 million. They use FlashAttention (or FlashAttention-2) as a primitive, and so the improvement from FlashAttention-3 would benefit these distributed attention methods as well.

## Alternative architectures

Motivated by the limitations of attention, a variety of alternative architectures have been proposed. They build on the connection between linear attention [27] and recurrent neural networks (RNNs). **RWKV [42], H3 [18], MEGA [35], Retnet [55]** enhance the expressivity of the simple cumulative sum in linear attention with more sophisticated recurrences. **Mamba [22]** and **xLSTM [5]** use learnable weighting for the recurrence and can match the quality of Transformers in language modeling at small or medium scale. These approaches can be connected to generalizations of linear attention through the lens of the structure of the token-mixing matrix [16]. These models have started to see some traction, seeing usage in some medium to large-scale models such as **Jamba [2]**, **Zamba [64]**, **Megalodon [36]**, and **Mamba2-hybrid [60]**. But the highest quality, >65M+ parameter RNN-based models still employ many layers of attention. We expect that techniques to speed up attention presented in this work will be useful to speedup these alternative architectures.

## Low-precision attention

Quantization is a promising approach to speed up attention, but they have mostly focused on reducing the space for KV cache for inference efficiency. **QuIP [9]** and **QuIP# [58]** use incoherent processing to reduce the quantization, and we adapted this technique for FP8 FlashAttention-3. Recent work suggests that for inference the KV cache is highly compressible down to 4-, 3-, or even 2-bits [26, 33]. However, quantization during training is still challenging as higher precision is typically required for stable training.

## Hardware-aware Algorithms

Our work presented in this paper focuses on the micro-architecture specific tuning to leverage new instruction sets and adopt a natively asynchronous programming model. There are other orthogonal axes for hardware-aware algorithm co-design being explored. A recent example of this is **LeanAttention [49]**, which reorganizes the GPU kernel compute (the generation phase as primary bottlenecks for inference and optimizes it via a smarter load balancing strategy similar to Stream-K and Lightning [41] to achieve nearly peak occupancy. There is a large literature on optimizing GEMM for specific hardware that employs many of the same techniques. As an example, **Abdelfattah et al. [1]** presents a high performance batched GEMM kernel on K40c Graphics Processing Units (GPU) for both fixed and variable sizes, proposing specialized GEMM designs and a comprehensive autotuning process to deliver state-of-the-art performance.
