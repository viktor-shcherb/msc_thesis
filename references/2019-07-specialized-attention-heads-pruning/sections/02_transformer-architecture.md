# 2 Transformer Architecture [p. 2-3]

This section briefly describes the Transformer architecture (Vaswani et al., 2017) introducing the terminology used in the rest of the paper. [p. 2]

The Transformer is an encoder-decoder model that uses stacked self-attention and fully connected layers for both the encoder and decoder. The encoder consists of N layers, each containing two sub-layers: (a) a multi-head self-attention mechanism, and (b) a feed-forward network. [p. 2]

The multi-head attention mechanism relies on scaled dot-product attention, which operates on a query Q, a key K and a value V:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V \quad (1)$$

where $d_k$ is the key dimensionality. In self-attention, queries, keys and values come from the output of the previous layer. [p. 2]

The multi-head attention mechanism obtains $h$ (i.e. one per head) different representations of ($Q$, $K$, $V$), computes scaled dot-product attention for each representation, concatenates the results, and projects the concatenation through a feed-forward layer:

$$\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V) \quad (2)$$

$$\text{MultiHead}(Q, K, V) = \text{Concat}_i(\text{head}_i) W^O \quad (3)$$

where the $W_i$ and $W^O$ are parameter matrices. [p. 3]

The second component of each layer of the Transformer network is a feed-forward network. The authors propose using a two-layer network with a ReLU activation. [p. 3]

Analogously, each layer of the decoder contains the two sub-layers mentioned above as well as an additional multi-head attention sub-layer. This additional sub-layer receives the output of the encoder as its keys and values. [p. 3]

The Transformer uses multi-head attention in three different ways: encoder self-attention, decoder self-attention and decoder-encoder attention. This work concentrates primarily on encoder self-attention. [p. 3]
