# 3.2 Attention [p. 3-5]

An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key. [p. 3-4]

## Figures

**Figure 2** (p. 4): `"(left) Scaled Dot-Product Attention. (right) Multi-Head Attention consists of several attention layers running in parallel."`
Left diagram shows the flow: Q, K, V inputs -> MatMul (Q, K) -> Scale -> Mask (opt.) -> SoftMax -> MatMul (with V) -> output. Right diagram shows: V, K, Q inputs -> each passes through a Linear layer -> fed into h parallel Scaled Dot-Product Attention blocks -> Concat -> Linear -> output. [p. 4]

## 3.2.1 Scaled Dot-Product Attention [p. 4]

The input consists of queries and keys of dimension d_k, and values of dimension d_v. The dot products of the query with all keys are computed, divided by sqrt(d_k), and a softmax function is applied to obtain the weights on the values. [p. 4]

In practice, the attention function is computed on a set of queries simultaneously, packed into a matrix Q. Keys and values are packed into matrices K and V. [p. 4]

**Equation (1):**

Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V

Computes scaled dot-product attention: the dot-product similarity between queries and keys is scaled by 1/sqrt(d_k) before softmax normalization, then applied as weights to V. [p. 4]

The two most commonly used attention functions are additive attention [2] and dot-product (multiplicative) attention. Dot-product attention is identical to the authors' algorithm except for the scaling factor of 1/sqrt(d_k). Additive attention computes the compatibility function using a feed-forward network with a single hidden layer. The two are similar in theoretical complexity, but dot-product attention is much faster and more space-efficient in practice since it can be implemented using highly optimized matrix multiplication code. [p. 4]

For small values of d_k, the two mechanisms perform similarly. For larger values of d_k, additive attention outperforms dot-product attention without scaling [3]. The authors suspect that for large d_k, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients (footnote 1: assuming q and k components are independent random variables with mean 0 and variance 1, their dot product q . k = sum_{i=1}^{d_k} q_i k_i has mean 0 and variance d_k). To counteract this, the dot products are scaled by 1/sqrt(d_k). [p. 4]

## 3.2.2 Multi-Head Attention [p. 4-5]

Instead of performing a single attention function with d_model-dimensional keys, values, and queries, the authors found it beneficial to linearly project the queries, keys, and values h times with different, learned linear projections to d_k, d_k, and d_v dimensions, respectively. On each of these projected versions, the attention function is performed in parallel, yielding d_v-dimensional output values. These are concatenated and once again projected, resulting in the final values (Figure 2). [p. 4-5]

Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this. [p. 5]

**Equations (multi-head attention):**

MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O

where head_i = Attention(Q W_i^Q, K W_i^K, V W_i^V)

Computes h parallel attention operations on linearly-projected versions of Q, K, V, then concatenates and projects the results. [p. 5]

**Parameter matrices:**
- W_i^Q in R^{d_model x d_k}
- W_i^K in R^{d_model x d_k}
- W_i^V in R^{d_model x d_v}
- W^O in R^{h d_v x d_model}

In this work: h = 8 parallel attention layers (heads). d_k = d_v = d_model / h = 64. Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality. [p. 5]

## 3.2.3 Applications of Attention in our Model [p. 5]

The Transformer uses multi-head attention in three different ways: [p. 5]

1. **Encoder-decoder attention layers:** Queries come from the previous decoder layer; memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence, mimicking typical encoder-decoder attention mechanisms in sequence-to-sequence models such as [38, 2, 9]. [p. 5]

2. **Encoder self-attention layers:** All of the keys, values, and queries come from the same place -- the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder. [p. 5]

3. **Decoder self-attention layers:** Each position in the decoder can attend to all positions in the decoder up to and including that position. Leftward information flow is prevented to preserve the auto-regressive property. This is implemented by masking out (setting to -infinity) all values in the input of the softmax which correspond to illegal connections. See Figure 2. [p. 5]
