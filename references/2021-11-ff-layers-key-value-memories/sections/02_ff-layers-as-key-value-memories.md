# 2 Feed-Forward Layers as Unnormalized Key-Value Memories [p. 2-3]

## Feed-forward layers

[p. 2] A transformer language model (Vaswani et al., 2017) is made of intertwined self-attention and feed-forward layers. Each feed-forward layer is a position-wise function, processing each input vector independently. Let x in R^d be a vector corresponding to some input text prefix. The feed-forward layer FF(.) can be expressed as follows (bias terms are omitted):

$$FF(x) = f(x \cdot K^\top) \cdot V \qquad (1)$$

Here, K, V in R^{d_m x d} are parameter matrices, and f is a non-linearity such as ReLU.

## Neural memory

[p. 2] A neural memory (Sukhbaatar et al., 2015) consists of d_m key-value pairs, which the authors call *memories*. Each key is represented by a d-dimensional vector k_i in R^d, and together they form the parameter matrix K in R^{d_m x d}; likewise, the value parameters are V in R^{d_m x d}. Given an input vector x in R^d, a distribution over the keys is computed, and used to compute the expected value:

$$p(k_i | x) \propto \exp(x \cdot k_i)$$

$$MN(x) = \sum_{i=1}^{d_m} p(k_i | x) v_i$$

With matrix notation, a more compact formulation:

$$MN(x) = \text{softmax}(x \cdot K^\top) \cdot V \qquad (2)$$

Footnote 2 [p. 2]: The terms "memory cells" and "memories" are used interchangeably.

## Feed-forward layers emulate neural memory

[p. 2-3] Comparing equations 1 and 2 shows that feed-forward layers are almost identical to key-value neural memories; the only difference is that neural memory uses softmax as the non-linearity f(.), while the canonical transformer does not use a normalizing function in the feed-forward layer.

Key definitions:
- The *hidden dimension* d_m is essentially the number of memories in the layer
- The activation m = f(x . K^T), commonly referred to as the *hidden layer*, is a vector containing an unnormalized non-negative coefficient for each memory
- Each m_i is referred to as the *memory coefficient* of the ith memory cell

[p. 3] Sukhbaatar et al. (2019) make an analogous observation, and incorporate the parameters of the feed-forward layers as persistent memory cells in the self-attention layers. While this reparameterization works in practice, the experiment does not tell us much about the role of feed-forward layers in the canonical transformer. If transformer feed-forward layers are indeed key-value memories, then what memories do they store?

## Conjectures

[p. 3] The authors conjecture that:
- Each key vector k_i captures a particular pattern (or set of patterns) in the input sequence (Section 3)
- Its corresponding value vector v_i represents the distribution of tokens that follows said pattern (Section 4)
