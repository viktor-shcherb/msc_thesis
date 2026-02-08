# 1 Introduction [p. 2]

Transformer [VSP+17] has become the de facto architecture for large language models [BMR+20], which was initially proposed to overcome the sequential training issue of recurrent models [HS97]. However, training parallelism of Transformers is at the cost of inefficient inference, because of the O(N) complexity per step and memory-bound key-value cache [Sha19], which renders Transformers unfriendly to deployment. The growing sequence length increases GPU memory consumption as well as latency and reduces inference speed. [p. 2]

Numerous efforts have continued to develop the next-generation architecture, aiming at retaining training parallelism and competitive performance as Transformers while having efficient O(1) inference. It is challenging to achieve the above goals simultaneously, i.e., the so-called "impossible triangle" as shown in Figure 2. [p. 2]

Three main strands of research are identified: [p. 2]

1. **Linearized attention** [KVPF20] approximates standard attention scores exp(q . k) with kernels phi(q) . phi(k), so that autoregressive inference can be rewritten in a recurrent form. However, the modeling capability and performance are worse than Transformers, which hinders the method's popularity.

2. **Recurrent models** — the second strand returns to recurrent models for efficient inference while sacrificing training parallelism. As a remedy, element-wise operators [PAA+23] are used for acceleration, however, representation capacity and performance are harmed.

3. **Replacing attention with other mechanisms**, such as S4 [GGR21], and its variants [DFS+22, PMN+23]. None of the previous work can break through the impossible triangle, resulting in no clear winner compared with Transformers.

The authors propose retentive networks (RetNet), achieving low-cost inference, efficient long-sequence modeling, Transformer-comparable performance, and parallel model training simultaneously. They introduce a multi-scale retention mechanism to substitute multi-head attention, which has three computation paradigms: parallel, recurrent, and chunkwise recurrent representations. [p. 2]

- The parallel representation empowers training parallelism to utilize GPU devices fully.
- The recurrent representation enables efficient O(1) inference in terms of memory and computation. The deployment cost and latency can be significantly reduced. The implementation is greatly simplified without key-value cache tricks.
- The chunkwise recurrent representation can perform efficient long-sequence modeling. It parallelly encodes each local block for computation speed while recurrently encoding the global blocks to save GPU memory.

Experimental results on language modeling show that RetNet is consistently competitive in terms of both scaling curves and in-context learning. The inference cost of RetNet is length-invariant. For a 7B model and 8k sequence length, RetNet decodes 8.4x faster and saves 70% of memory than Transformers with key-value caches. During training, RetNet achieves 25-50% memory saving and 7x acceleration than standard Transformer and an advantage towards highly-optimized FlashAttention [DFE+22]. RetNet's inference latency is insensitive to batch size, allowing enormous throughput. [p. 2]

## Figures

**Figure 1** (p. 1): "Retentive network (RetNet) achieves low-cost inference (i.e., GPU memory, throughput, and latency), training parallelism, and favorable scaling curves compared with Transformer. Results of inference cost are reported with 8k as input length. Figure 6 shows more results on different sequence lengths."

Left panel ("Inference Cost"): Three bar chart comparisons between Transformer (grey) and RetNet (green):
- GPU Memory (GB): Transformer ~40, RetNet ~12 (3.4x reduction)
- Throughput (wps): Transformer ~150, RetNet ~300 (8.4x improvement, though the bars show ~2x, the label says 8.4X)
- Latency (ms): Transformer ~300, RetNet ~20 (15.6x reduction)

Right panel ("Scaling Curve"): Line plot of LM Perplexity vs. Model Size (B) at sizes 1, 3, 7. RetNet (green) shows lower perplexity than Transformer (grey) at larger model sizes, with the curves converging/crossing as model size increases.

**Figure 2** (p. 2): "RetNet makes the 'impossible triangle' possible, which achieves training parallelism, good performance, and low inference cost simultaneously."

Shows a Penrose triangle (impossible triangle) with three vertices labeled: "Low-Cost Inference", "Training Parallelism", and "Strong Performance". RetNet is positioned inside the triangle achieving all three properties. Various architectures are positioned along the edges: Linear Transformer, Recurrent Network along the top edges; Transformer at the bottom. RetNet sits centrally, indicating it achieves all three simultaneously.
