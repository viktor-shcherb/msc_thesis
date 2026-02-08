# 4 Why Self-Attention [p. 6]

This section compares various aspects of self-attention layers to the recurrent and convolutional layers commonly used for mapping one variable-length sequence of symbol representations (x_1, ..., x_n) to another sequence of equal length (z_1, ..., z_n), with x_i, z_i in R^d, such as a hidden layer in a typical sequence transduction encoder or decoder. [p. 6]

Three desiderata motivating the use of self-attention: [p. 6]

1. Total computational complexity per layer.
2. The amount of computation that can be parallelized, as measured by the minimum number of sequential operations required.
3. The path length between long-range dependencies in the network. Learning long-range dependencies is a key challenge in many sequence transduction tasks. One key factor affecting the ability to learn such dependencies is the length of the paths forward and backward signals have to traverse in the network. The shorter these paths between any combination of positions in the input and output sequences, the easier it is to learn long-range dependencies [12].

The authors compare the maximum path length between any two input and output positions in networks composed of the different layer types. [p. 6]

As noted in Table 1, a self-attention layer connects all positions with a constant number of sequentially executed operations, whereas a recurrent layer requires O(n) sequential operations. In terms of computational complexity, self-attention layers are faster than recurrent layers when the sequence length n is smaller than the representation dimensionality d. [p. 6]

---
[p. 7 continued]

This is most often the case with sentence representations used by state-of-the-art models in machine translations, such as word-piece [38] and byte-pair [31] representations. To improve computational performance for tasks involving very long sequences, self-attention could be restricted to considering only a neighborhood of size r in the input sequence centered around the respective output position. This would increase the maximum path length to O(n/r). The authors plan to investigate this approach further in future work. [p. 7]

A single convolutional layer with kernel width k < n does not connect all pairs of input and output positions. Doing so requires a stack of O(n/k) convolutional layers in the case of contiguous kernels, or O(log_k(n)) in the case of dilated convolutions [18], increasing the length of the longest paths between any two positions in the network. Convolutional layers are generally more expensive than recurrent layers, by a factor of k. Separable convolutions [6], however, decrease the complexity considerably, to O(k * n * d + n * d^2). Even with k = n, however, the complexity of a separable convolution is equal to the combination of a self-attention layer and a point-wise feed-forward layer, the approach taken in this model. [p. 7]

As a side benefit, self-attention could yield more interpretable models. The authors inspect attention distributions from their models and present and discuss examples in the appendix. Individual attention heads clearly learn to perform different tasks, and many appear to exhibit behavior related to the syntactic and semantic structure of the sentences. [p. 7]
