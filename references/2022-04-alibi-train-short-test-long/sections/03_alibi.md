# 3 Attention with Linear Biases (ALiBi) [p. 5-6]

## Figure 3

**Figure 3** (p. 5): "When computing attention scores for each head, our linearly biased attention method, ALiBi, adds a constant bias (right) to each attention score ($\mathbf{q}_i \cdot \mathbf{k}_j$, left). As in the unmodified attention sublayer, the softmax function is then applied to these scores, and the rest of the computation is unmodified. **m is a head-specific scalar** that is set and not learned throughout training. We show that our method for setting $m$ values generalizes to multiple text domains, models and training compute budgets. When using ALiBi, we do *not* add positional embeddings at the bottom of the network."

The figure shows two matrices being added together then multiplied by scalar $m$:
- Left matrix: standard query-key dot product attention scores ($q_i \cdot k_j$) forming a lower-triangular matrix (causal mask)
- Right matrix: a lower-triangular matrix of position biases with values 0 on the diagonal, $-1$ on the first subdiagonal, $-2$ on the second subdiagonal, etc. (i.e., $[0], [-1, 0], [-2, -1, 0], [-3, -2, -1, 0], [-4, -3, -2, -1, 0]$)
- The right matrix is multiplied by head-specific scalar $m$

## Method Description [p. 5]

[p. 5]

In the transformer model of Vaswani et al. (2017), position embeddings are added to the word embeddings at the bottom of the network. For an input subsequence of length $L$, the attention sublayer computes the attention scores for the $i$th query $\mathbf{q}_i \in \mathbb{R}^{1 \times d}$, ($1 \leq i \leq L$) in each head, given the first $i$ keys $\mathbf{K} \in \mathbb{R}^{i \times d}$, where $d$ is the head dimension:

$$\text{softmax}(\mathbf{q}_i \mathbf{K}^\top)$$

These attention scores are then multiplied by the values to return the output of the attention sublayer. [p. 5]

When using ALiBi, no position embeddings are added at any point in the network. The only modification is after the query-key dot product, where a static, non-learned bias is added:

$$\text{softmax}(\mathbf{q}_i \mathbf{K}^\top + m \cdot [-(i-1), ..., -2, -1, 0])$$

where scalar $m$ is a head-specific slope fixed before training. Figure 3 offers a visualization. [p. 5]

Note: The ALiBi bias is not multiplied by the $\sqrt{d_k}$ scaling factor from Equation 1 of Vaswani et al. (2017) (footnote 10). [p. 5]

## Slope Values [p. 5]

[p. 5]

For models with 8 heads, the slopes are the geometric sequence: $\frac{1}{2^1}, \frac{1}{2^2}, ..., \frac{1}{2^8}$. [p. 5]

For models that require 16 heads, the 8 slopes are interpolated by geometrically averaging every consecutive pair, resulting in the geometric sequence that starts at $\frac{1}{\sqrt{2}}$ and has the ratio of $\frac{1}{\sqrt{2}}$: $\frac{1}{2^{0.5}}, \frac{1}{2^1}, \frac{1}{2^{1.5}}, ..., \frac{1}{2^8}$. [p. 5]

In general, for $n$ heads, the set of slopes is the geometric sequence that starts at $2^{-\frac{8}{n}}$ and uses that same value as its ratio. [p. 5]

In Section 4, the authors observe that this set of slopes works on a wide variety of text domains and model sizes. Therefore, they do not believe that it is necessary to tune these slope values every time a new model is trained on a new dataset. This makes ALiBi similar to the sinusoidal approach, where the hyperparameters (the start and end of the geometric progression of wavelengths) were set once by Vaswani et al. (2017) and then reused in different models of different sizes on different datasets. [p. 5]

## Properties of ALiBi [p. 5]

[p. 5]

ALiBi has an inductive bias towards recency; it penalizes attention scores between distant query-key pairs, with the penalty increasing as the distance between a key and a query grows. The different heads increase their penalties at different rates, depending on the slope magnitude. [p. 5]

The authors initially experimented with making the slopes trainable, but this did not yield strong extrapolation results. A brief manual exploration of around ten slope sets led to the discovery of the set of slopes that was finally picked. The main insight from this exploration is that the slope sets that work best are those with slopes in the $(0, 1)$ range, with the slopes' density increasing as we get closer to 0. The method is also found to be robust to slope choice. Even randomly sampling from the exponential distribution worked well in some cases (although that method had high variance). [p. 5]

Note: Trainable slopes also slowed down the training speed by 3% (footnote 11). [p. 5]

Since ALiBi is a relative position method, it adds position information at every layer to the keys and queries but not to the values, as is done in the T5 bias and rotary methods. The authors hypothesize that these properties might be beneficial for extrapolation. [p. 5]

## Implementation [p. 6]

[p. 6]

ALiBi is easy to implement, with all changes accomplished in a few lines of code. It is implemented by modifying the mask matrix by adding the linear biases to it (in practice, when training a transformer LM, query $\mathbf{q}_i$ attends only to keys 1 to $i$; this is implemented by adding a mask matrix to the query-key dot product before the softmax operation is applied). This means that there is no runtime penalty when using this method since no operations are added to the network. [p. 6]

Compared to the sinusoidal model trained on the same input lengths, ALiBi incurs a memory increase (up to 100MB in some experiments): in the unmodified transformer, the mask is of size $L \times L$; when using ALiBi, the mask is a slightly larger $n \times L \times L$ (where $n$ is the number of heads) since the linear biases added for each head uses a different slope. But, as shown, ALiBi enables training on much smaller sequences while still achieving (and occasionally surpassing) results obtained using sinusoidal embeddings on longer sequences, which saves multiple gigabytes of memory. [p. 6]
