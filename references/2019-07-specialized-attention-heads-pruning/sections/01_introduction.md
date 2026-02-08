# 1 Introduction [p. 1-2]

The Transformer (Vaswani et al., 2017) has become the dominant modeling paradigm in neural machine translation. It follows the encoder-decoder framework using stacked multi-head self-attention and fully connected layers. [p. 1]

Multi-head attention was shown to make more efficient use of the model's capacity: performance of the model with 8 heads is almost 1 BLEU point higher than that of a model of the same size with single-head attention (Vaswani et al., 2017). The Transformer achieved state-of-the-art results in recent shared translation tasks (Bojar et al., 2018; Niehues et al., 2018). [p. 1]

Despite the model's widespread adoption and recent attempts to investigate the kinds of information learned by the model's encoder (Raganato and Tiedemann, 2018), the analysis of multi-head attention and its importance for translation is challenging. Previous analysis of multi-head attention considered the average of attention weights over all heads at a given position or focused only on the maximum attention weights (Voita et al., 2018; Tang et al., 2018), but neither method explicitly takes into account the varying importance of different heads. This obscures the roles played by individual heads which influence translations to differing extents. [p. 1]

The paper attempts to answer the following questions: [p. 1]

- To what extent does translation quality depend on individual encoder heads?
- Do individual encoder heads play consistent and interpretable roles? If so, which are the most important ones for translation quality?
- Which types of model attention (encoder self-attention, decoder self-attention or decoder-encoder attention) are most sensitive to the number of attention heads and on which layers?
- Can we significantly reduce the number of attention heads while preserving translation quality?

The approach starts by identifying the most important heads in each encoder layer using layer-wise relevance propagation (Ding et al., 2017). For heads judged to be important, they characterize the roles they perform. Three types of role are observed: [p. 1]

1. **Positional:** heads attending to an adjacent token
2. **Syntactic:** heads attending to tokens in a specific syntactic dependency relation
3. **Rare words:** heads pointing to the least frequent tokens in the sentence

To understand whether remaining heads are vital or redundant, the authors introduce a pruning method based on Louizos et al. (2018). While the L_0 regularizer cannot be directly incorporated as a penalty term, a differentiable relaxation can be used. Heads are pruned in a continuous learning scenario starting from the converged full model. [p. 2]

Key findings: [p. 2]

- Only a small subset of heads are important for translation
- Important heads have one or more specialized and interpretable functions in the model
- The functions correspond to attention to neighbouring words and to tokens in specific syntactic dependency relations
