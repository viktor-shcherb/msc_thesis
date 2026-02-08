# A Appendices [p. 8]

## A.1 Single Head Analysis

[p. 8] For analysing attention weights with a multi-head setup, one could either analyze attention heads separately, or average all heads and have a single attention graph. However, treating attention heads separately could potentially mean assuming there is no mixing of information between heads, which is not true as heads are combined in the position-wise feed-forward network on top of self-attention in a Transformer block.

It is possible to analyse the role of each head in isolation of all other heads using attention rollout and attention flow. To not make the assumption that there is no mixing of information between heads, for computing the "input attention", all the layers below the layer of interest are treated as single head layers, i.e., the attentions of all heads in the layers below are summed.

For example, attention rollout for head $k$ at layer $i$ can be computed as:

$$\tilde{A}(i, k) = A(i, k) \tilde{A}(i)$$

where $\tilde{A}(i)$ is attention rollout computed for layer $i$ with the single head assumption.
