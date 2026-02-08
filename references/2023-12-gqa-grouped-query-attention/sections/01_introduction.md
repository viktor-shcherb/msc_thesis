# 1 Introduction [p. 1]

Autoregressive decoder inference is a severe bottleneck for Transformer models due to the memory bandwidth overhead from loading decoder weights and all attention keys and values at every decoding step (Shazeer, 2019; Pope et al., 2022; de Jong et al., 2022). The memory bandwidth from loading keys and values can be sharply reduced through *multi-query attention* (Shazeer, 2019), which uses multiple query heads but single key and value heads. [p. 1]

However, multi-query attention (MQA) can lead to quality degradation and training instability, and it may not be feasible to train separate models optimized for quality and inference. Moreover, while some language models already use multi-query attention, such as PaLM (Chowdhery et al., 2022), many do not, including publicly available language models such as T5 (Raffel et al., 2020) and LLaMA (Touvron et al., 2023). [p. 1]

## Contributions

Two contributions for faster inference with large language models: [p. 1]

1. Show that language model checkpoints with multi-head attention (MHA) can be *uptrained* (Komatsuzaki et al., 2022) to use MQA with a small fraction of original training compute. This presents a cost-effective method to obtain fast multi-query as well as high-quality MHA checkpoints. [p. 1]

2. Propose grouped-query attention (GQA), an interpolation between multi-head and multi-query attention with single key and value heads *per subgroup of query heads*. Show that uptrained GQA achieves quality close to multi-head attention while being almost as fast as multi-query attention. [p. 1]
