# 3.3 Position-wise Feed-Forward Networks [p. 5]

In addition to attention sub-layers, each layer in the encoder and decoder contains a fully connected feed-forward network, applied to each position separately and identically. This consists of two linear transformations with a ReLU activation in between. [p. 5]

**Equation (2):**

FFN(x) = max(0, x W_1 + b_1) W_2 + b_2

Computes a two-layer feed-forward network with ReLU activation, applied position-wise. [p. 5]

While the linear transformations are the same across different positions, they use different parameters from layer to layer. Another way of describing this is as two convolutions with kernel size 1. The dimensionality of input and output is d_model = 512, and the inner-layer has dimensionality d_ff = 2048. [p. 5]

# 3.4 Embeddings and Softmax [p. 5]

Learned embeddings are used to convert input tokens and output tokens to vectors of dimension d_model. The usual learned linear transformation and softmax function are used to convert the decoder output to predicted next-token probabilities. The same weight matrix is shared between the two embedding layers and the pre-softmax linear transformation, similar to [30]. In the embedding layers, those weights are multiplied by sqrt(d_model). [p. 5]

# 3.5 Positional Encoding [p. 6]

Since the model contains no recurrence and no convolution, positional information must be injected to make use of the order of the sequence. "Positional encodings" are added to the input embeddings at the bottoms of the encoder and decoder stacks. The positional encodings have the same dimension d_model as the embeddings so the two can be summed. There are many choices of positional encodings, learned and fixed [9]. [p. 6]

The authors use sine and cosine functions of different frequencies: [p. 6]

PE_(pos, 2i) = sin(pos / 10000^{2i / d_model})

PE_(pos, 2i+1) = cos(pos / 10000^{2i / d_model})

where pos is the position and i is the dimension. Each dimension of the positional encoding corresponds to a sinusoid. The wavelengths form a geometric progression from 2 pi to 10000 * 2 pi. [p. 6]

This function was chosen because the authors hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset k, PE_{pos+k} can be represented as a linear function of PE_{pos}. [p. 6]

The authors also experimented with using learned positional embeddings [9] and found that the two versions produced nearly identical results (see Table 3 row (E)). The sinusoidal version was chosen because it may allow the model to extrapolate to sequence lengths longer than those encountered during training. [p. 6]

## Tables

**Table 1** (p. 6): `"Maximum path lengths, per-layer complexity and minimum number of sequential operations for different layer types. n is the sequence length, d is the representation dimension, k is the kernel size of convolutions and r the size of the neighborhood in restricted self-attention."`

| Layer Type | Complexity per Layer | Sequential Operations | Maximum Path Length |
|---|---|---|---|
| Self-Attention | O(n^2 * d) | O(1) | O(1) |
| Recurrent | O(n * d^2) | O(n) | O(n) |
| Convolutional | O(k * n * d^2) | O(1) | O(log_k(n)) |
| Self-Attention (restricted) | O(r * n * d) | O(1) | O(n/r) |
