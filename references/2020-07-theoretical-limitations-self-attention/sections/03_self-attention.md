# 3 Self-Attention [p. 3--4]

[p. 3] Self-attention is defined as used in Transformers, following Vaswani et al. (2017), with some notational changes to simplify proofs.

## Input Representation

An input **x** = x_1 ... x_n, where all x_i come from some finite alphabet V, and x_n is an end-of-sequence symbol. The input is encoded into a sequence of input embeddings v_1, ..., v_n using some embedding map V -> R^k. A sequence of positional embeddings p_1, p_2, ... with p_i in R^k is also used. Positional embeddings are independent of the input **x** and can be computed through a predefined scheme or learned for each position in the training data (Vaswani et al., 2017). Input and positional embeddings are combined (e.g., via addition or concatenation) to vectors:

y_i^{(0)} = f(v_i, p_i)  (i = 1, ..., n)

which is referred to as Layer 0.

## Transformer Layers

A transformer has a fixed number L of **layers**; the **activations** y_i^{(k)} at position i of the k-th layer (k = 1, ..., L) are defined as follows. Each layer has a set of H **attention heads**; attention scores for the h-th head are computed as:

$$a_{i,j}^{(k,h)} = f_{k,h}^{att}(y_i^{(k-1)}, y_j^{(k-1)})$$  (1)

where f_{k,h}^{att} combines activations from the previous level into an attention score. This can be implemented, for example, using dot product or additive attention. Specifically, the implementation described by Vaswani et al. (2017, p. 5) linearly transforms the position-wise activations y_i^{(k-1)} separately into 'query' vectors Q y_i^{(k-1)} and 'key' vectors K y_i^{(k-1)} (for some parameter matrices K, Q); the attention score a_{i,j}^{(k,h)} is then implemented as a scaled dot product of query Q y_i^{(k-1)} and key K y_j^{(k-1)}.

The activation of the head is computed by weighting according to attention weights \hat{a}_{i,j}^{(k,h)}:

$$b_{i,k,h} = \sum_{j=1}^{n} \hat{a}_{i,j}^{(k,h)} y_j^{(k-1)}$$  (2)

The paper notes that the implementation described by Vaswani et al. (2017) first linearly transforms the activations y_j^{(k-1)} into 'value vectors' before multiplying with \hat{a}_{i,j}^{(k,h)}; this is mathematically equivalent to applying this linear transformation to b_{i,k,h} as part of the map f^{act} described below.

## Hard and Soft Attention Variants

In the **soft attention** version, the weights \hat{a}_{i,j}^{(k,h)} are obtained by the softmax operation: \hat{a}_{i,\cdot}^{(k,h)} = softmax(a_{i,\cdot}^{(k,h)}).

In the **hard attention** variant (Perez et al., 2019), one takes the actual maximum attention values: \hat{a}_{i,j}^{(k,h)} = delta_{j, argmax_{j'} a_{i,j'}^{(k,h)}}.^1

Footnote 1: When there are multiple positions with maximal attention weight, the one occurring first in the sequence is chosen. The analysis also works under other schemes of resolving ties, such as random selection. [p. 3]

## Per-position Activations

The per-position activations are then computed as:

$$y_i^{(k)} := f^{act}(y_i^{(k-1)}, b_{i,k,1}, ..., b_{i,k,H})$$  (3)

where f^{act} is implemented as a fully-connected feedforward network with a skip-connection (Vaswani et al., 2017) from y_i^{(k-1)} to y_i^{(k)}.

## Hard and Soft Attention in Practice

[p. 4] There is a choice between soft attention and hard attention (Shen et al., 2018b; Perez et al., 2019). The one prior theoretical study of transformers (Perez et al., 2019) assumes hard attention. In practice, soft attention is easier to train with gradient descent; however, analysis studies suggest that attention often concentrates on one or a few positions in trained transformer models (Voita et al., 2019; Clark et al., 2019) and that the most important heads are those that clearly focus on a few positions (Voita et al., 2019), suggesting that attention often behaves like hard attention in practice. The paper examines both hard (Section 5) and soft (Section 6) attention.

## Formalizing Language Recognition

[p. 4] Language recognition is the task of classifying input strings as belonging or not belonging to a formal language. Following Weiss et al. (2018), this is formalized as the sequence-to-sequence task of mapping words to labels 1 ('in the language') and 0 ('not in the language'). Following the construction of transformers in sequence-to-sequence tasks (Vaswani et al., 2017), a softmax probability vector is computed for this label from the last activation y_n^{(L)}, obtained after reading the end-of-sequence symbol.
