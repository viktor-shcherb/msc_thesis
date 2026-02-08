# 2 Background: Attention, Multi-headed Attention, and Masking [p. 2-3]

This section lays out the notational groundwork regarding attention and describes the method for masking out attention heads.

## 2.1 Single-headed Attention [p. 2]

The paper focuses on scaled bilinear attention (Luong et al., 2015), the variant most commonly used in MHA layers. Given a sequence of $n$ $d$-dimensional vectors $\mathbf{x} = x_1, \ldots, x_n \in \mathbb{R}^d$, and a query vector $q \in \mathbb{R}^d$, the attention layer parametrized by $W_k, W_q, W_v, W_o \in \mathbb{R}^{d \times d}$ computes the weighted sum:

$$\text{Att}_{W_k, W_q, W_v, W_o}(\mathbf{x}, q) = W_o \sum_{i=1}^{n} \alpha_i W_v x_i$$

where:

$$\alpha_i = \text{softmax}\left(\frac{q^\top W_q^\top W_k x_i}{\sqrt{d}}\right)$$

In self-attention, every $x_i$ is used as the query $q$ to compute a new sequence of representations, whereas in sequence-to-sequence models $q$ is typically a decoder state while $\mathbf{x}$ corresponds to the encoder output.

## 2.2 Multi-headed Attention [p. 2]

In multi-headed attention (MHA), $N_h$ independently parameterized attention layers are applied in parallel to obtain the final result:

$$\text{MHAtt}(\mathbf{x}, q) = \sum_{h=1}^{N_h} \text{Att}_{W_k^h, W_q^h, W_v^h, W_o^h}(\mathbf{x}, q) \tag{1}$$

where $W_k^h, W_q^h, W_v^h \in \mathbb{R}^{d_h \times d}$ and $W_o^h \in \mathbb{R}^{d \times d_h}$. When $d_h = d$, MHA is strictly more expressive than vanilla attention. However, to keep the number of parameters constant, $d_h$ is typically set to $\frac{d}{N_h}$, in which case MHA can be seen as an ensemble of low-rank vanilla attention layers (footnote 2). In the following, $\text{Att}_h(x)$ is used as a shorthand for the output of head $h$ on input $x$.

To allow the different attention heads to interact with each other, transformers apply a non-linear feed-forward network over the MHA's output, at each transformer layer (Vaswani et al., 2017).

> Footnote 2: "This notation, equivalent to the 'concatenation' formulation from Vaswani et al. (2017), is used to ease exposition in the following sections." [p. 2]

## 2.3 Masking Attention Heads [p. 3]

To perform ablation experiments on the heads, the formula for MHAtt is modified:

$$\text{MHAtt}(\mathbf{x}, q) = \sum_{h=1}^{N_h} \xi_h \text{Att}_{W_k^h, W_q^h, W_v^h, W_o^h}(\mathbf{x}, q)$$

where the $\xi_h$ are mask variables with values in $\{0, 1\}$. When all $\xi_h$ are equal to 1, this is equivalent to the formulation in Equation 1. In order to mask head $h$, simply set $\xi_h = 0$.
