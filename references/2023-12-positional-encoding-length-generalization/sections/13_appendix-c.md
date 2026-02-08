# Appendix C: Proofs [p. 19-21]

[p. 19] This section provides proof of why NoPE can implicitly learn both absolute and relative positions. It refers the reader to Appendix B.1 for the notation and definitions used.

## C.1 Absolute Positional Encoding in NoPE [p. 19-21]

[p. 19] This section discusses how NoPE can recover absolute positions in the hidden state. The proof is inspired by Weiss et al. (2021); Lindner et al. (2023) and relies on the causal attention mask in the decoder-only Transformer and the softmax function to recover absolute positions.

> **Theorem 1 (Absolute Encoding).** *Let $\boldsymbol{x} = [\texttt{<bos>}, x_1, \ldots, x_T]$ be an input sequence of length $T + 1$ to the model. Then, the first layer of $f_\theta$ can recover absolute positions $[1, \ldots, T + 1]$ in the hidden state $\boldsymbol{H}^{(1)}$. That is, there exist $\boldsymbol{W}_Q$, $\boldsymbol{W}_K$, $\boldsymbol{W}_V$, $\boldsymbol{W}_O$, $\boldsymbol{W}_1$, and $\boldsymbol{W}_2$ such that the self-attention and feedforward operations in the first layer compute absolute positions and write it to the next hidden state.* [p. 19]

### Proof

[p. 19] The proof only specifies the weights of a single attention head in the first layer (and additionally the parameterization of feedforward sub-layer). In this parameterization, only the first three dimensions of the hidden states are required. The rest of the heads, as long as they do not override the first three dimensions, can be arbitrary. This does not impose any challenges as Transformers used in practice usually have a very large model dimension $d$. The proof provides the construction of the weights and then verifies that they can recover absolute positions.

**Step 1: Construct word embedding matrix $\boldsymbol{W}_E \in \mathbb{R}^{d \times V}$**

[p. 19] Each column is the embedding of a token in the vocabulary. $\boldsymbol{W}_E$ is constructed such that it always sets the first dimension of every embedding vector to be 1. Additionally, it sets the second dimension to 1 if and only if the token is `<bos>`. Otherwise, it sets it to zero. The third dimension of all embedding vectors is set to zero. Other dimensions can take any arbitrary values. Without loss of generality, assume `<bos>` is the first token in the vocabulary, i.e. the first column. Then:

$$\boldsymbol{W}_E = \begin{bmatrix} 1 & 1 & 1 & \cdots & 1 \\ 1 & 0 & 0 & \cdots & 0 \\ 0 & 0 & 0 & \cdots & 0 \\ e_{4,1} & e_{4,2} & e_{4,3} & \cdots & e_{4,V} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ e_{d,1} & e_{d,2} & e_{d,2} & \cdots & e_{d,V} \end{bmatrix}_{d \times V} \tag{17}$$

where $e_{d,i} \in \mathbb{R}$.

**Step 2: Construct attention weights $\boldsymbol{W}_Q, \boldsymbol{W}_K, \boldsymbol{W}_V, \boldsymbol{W}_O$**

[p. 20] For head dimensions $h \geq 1$, the weights of the first attention head in the first layer are constructed as:

$$\boldsymbol{W}_K = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 1 & 0 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 1 & 0 & \cdots & 0 \end{bmatrix}_{h \times d} \qquad \boldsymbol{W}_V = \begin{bmatrix} 0 & 1 & 0 & \cdots & 0 \\ 0 & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & \cdots & 0 \end{bmatrix}_{h \times d} \tag{18}$$

$\boldsymbol{W}_K$ reads from the first dimension of the hidden state, which is initialized with 1 using the embedding matrix. Since all word embeddings have one in their first dimension, this parameterization will result in all key vectors to be the same. Moreover, $\boldsymbol{W}_V$ reads from the second dimension of the hidden state, which is initialized with 1 if the token is `<bos>`. So, the value vector will have 1 in its first dimension only if the corresponding token is `<bos>`.

$\boldsymbol{W}_Q$ can be any arbitrary matrix. $\boldsymbol{W}_O$ will write the result of the attention to the third dimension of the hidden state and can be constructed as:

$$\boldsymbol{W}_O = \begin{bmatrix} 0 & 0 & 0 & 0 & \cdots & 0 \\ 0 & 0 & 0 & 0 & \cdots & 0 \\ 1 & 0 & 0 & 0 & \cdots & 0 \\ 0 & 0 & 0 & 0 & \cdots & 0 \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & 0 & 0 & \cdots & 0 \end{bmatrix}_{d \times h} \tag{19}$$

**Step 3: Verify position recovery**

[p. 20] Now, verify that for any input sequence $\boldsymbol{x} = [\texttt{<bos>}, x_1, \ldots, x_T]$, the first layer can recover absolute positions $[1, \ldots, T + 1]$ in the hidden state $\boldsymbol{H}^{(1)}$. This is verified for column $t$ of $\boldsymbol{H}^{(1)}$, showing that absolute position information is available in the third dimension of $\boldsymbol{h}_t^{(1)}$.

First, use the word embedding matrix $\boldsymbol{W}_E$ to compute the embedding $\boldsymbol{H}^{(0)}$:

$$\boldsymbol{H}^{(0)} = \boldsymbol{W}_E \boldsymbol{X} = \begin{bmatrix} 1 & 1 & 1 & \cdots & 1 \\ 1 & 0 & 0 & \cdots & 0 \\ 0 & 0 & 0 & \cdots & 0 \\ e_{4,1} & e_{4,2} & e_{4,3} & \cdots & e_{4,V} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ e_{d,1} & e_{d,2} & e_{d,2} & \cdots & e_{d,V} \end{bmatrix}_{d \times (T+1)} \tag{20}$$

The attention computation at position $1 \leq t \leq T + 1$. First, use $\boldsymbol{W}_Q$ to compute the query vector $\boldsymbol{q}_t$ by applying $\boldsymbol{q}_t = \boldsymbol{W}_Q \boldsymbol{h}_t^{(0)}$:

$$\boldsymbol{q}_t = [q_1, q_2, q_3, \ldots, q_h]^\top \tag{21}$$

Since $\boldsymbol{W}_Q$ can be any arbitrary matrix, $q_j \in \mathbb{R}$ can take any arbitrary value. Next, compute the key vectors by applying $\boldsymbol{k}_i = \boldsymbol{W}_K \boldsymbol{h}_i^{(0)}$:

$$\boldsymbol{k}_1 = \begin{pmatrix} 1 \\ 1 \\ \vdots \\ 1 \end{pmatrix} \quad \boldsymbol{k}_2 = \begin{pmatrix} 1 \\ 1 \\ \vdots \\ 1 \end{pmatrix} \quad \cdots \quad \boldsymbol{k}_t = \begin{pmatrix} 1 \\ 1 \\ \vdots \\ 1 \end{pmatrix} \tag{22}$$

All key vectors are the same and only need to be computed up to position $t$ as the attention mask is causal, i.e. a query can only look at positions $\leq t$. Next, compute the attention weight vectors $\boldsymbol{\alpha}$:

$$\boldsymbol{\alpha} = [\langle \boldsymbol{q}_t, \boldsymbol{k}_1 \rangle, \langle \boldsymbol{q}_t, \boldsymbol{k}_2 \rangle, \ldots, \langle \boldsymbol{q}_t, \boldsymbol{k}_t \rangle]^\top \tag{23}$$
$$= [\alpha^*, \alpha^*, \ldots, \alpha^*]^\top \tag{24}$$

[p. 21] where $\alpha^* = q_1 + q_2 + \ldots + q_h$. Next, apply softmax to compute the attention probabilities. Since all $\boldsymbol{\alpha}^i$'s are the same:

$$\hat{\boldsymbol{\alpha}} = \text{softmax}(\boldsymbol{\alpha}) = \left[\frac{1}{t}, \frac{1}{t}, \ldots, \frac{1}{t}\right]^\top \tag{25}$$

Now, compute the value vectors by applying $\boldsymbol{v}_i = \boldsymbol{W}_V \boldsymbol{h}_i^{(0)}$:

$$\boldsymbol{v}_1 = \begin{pmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix} \quad \boldsymbol{v}_2 = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} \quad \cdots \quad \boldsymbol{v}_t = \begin{pmatrix} 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix} \tag{26}$$

Finally, compute the output of the attention head by applying $\boldsymbol{W}_O$:

$$\boldsymbol{o}_t = \boldsymbol{W}_O \left( \sum_{i \leq t} \hat{\alpha}_i \boldsymbol{v}_i \right) = \boldsymbol{W}_O \left( \frac{1}{t} \sum_{i \leq t} \boldsymbol{v}_i \right) = \boldsymbol{W}_O \begin{pmatrix} 1/t \\ 0 \\ \vdots \\ 0 \end{pmatrix}_h = \begin{pmatrix} 0 \\ 0 \\ 1/t \\ 0 \\ \vdots \\ 0 \end{pmatrix}_d \tag{27}$$

Thus, the output of the constructed attention head recovers the absolute position information and writes it to the third dimension of output.

The proof used the decoder-only property of Transformer implicitly in Equation (23), which helped restrict attention to positions $\leq t$. So, the lengths of the attended sequence are always $t$. Moreover, the presence of `<bos>` token in the input sequence helped anchor the absolute position information. This is not a problem as in practice models are often prompted with some instructions which can act as `<bos>` token. [p. 21]

With this information available to the rest of the network, the feedforward sub-layer, with sufficient hidden width, can recover the absolute positions $[1, 2, \ldots, T+1]$ from the third dimension of attention output. This is because the feedforward sub-layer is MLP with ReLU activation. So, it can learn any arbitrary function (Park et al., 2020). The layer-norm operation can be bypassed as explained by Akyurek et al. (2023). $\square$

## C.2 Relative Positional Encoding in NoPE [p. 21]

[p. 21] This section shows that if the hidden state contains absolute positional information as explained in the previous section, then the attention mechanism in all subsequent layers can implement a relative positional encoding. It refers to Appendices B.1 and C.1 for the notation and definitions.

> **Theorem 2 (Relative Encoding).** *Suppose that the hidden state $\boldsymbol{H}^{(1)}$ contains absolute positional information, as stated in Theorem 1, and assume that it is not overwritten by any subsequent layers. Then, the self-attention in all subsequent layers can implement a relative positional encoding: there exists a parameterization of $f_\theta$ such that, for $l \geq 2$, the attention dot product between query $\boldsymbol{q}_t$ and key $\boldsymbol{k}_i$ at positions $t$ and $i$ ($t \geq i$) can be expressed as:*
>
> $$\langle \boldsymbol{q}_t, \boldsymbol{k}_i \rangle = f_{\text{cnt}}(\boldsymbol{q}_t, \boldsymbol{k}_i) + f_{\text{rel}}(t - i) \tag{1}$$
>
> *where $f_{\text{cnt}}$ is a function of their content, and $f_{\text{rel}}$ is a function of their relative distance.* [p. 21]

### Proof

[p. 21-23] The proof only specifies a few entries of weight matrices for attention heads in layers $l \geq 2$, which does not impose any challenges for Transformers used in practice as they usually have a very large model dimension $d$. Moreover, absolute positions must be available in the third dimension of the hidden state as explained in Theorem 1. To show NoPE can implement relative encoding, it is only necessary to prove that its attention dot product depends on the relative distance between tokens (see Appendix B.1 for an overview of relative encoding methods). The rest of the proof provides the construction of the weights and then verifies that they can implement relative position encoding.

**Weight construction:**

[p. 22] For head dimension $h \geq 2$, construct the weights $\boldsymbol{W}_Q, \boldsymbol{W}_K$ of the attention heads in the second layers and above:

$$\boldsymbol{W}_Q = \begin{bmatrix} 1 & 0 & 0 & 0 & \cdots & 0 \\ 0 & 0 & -1 & 0 & \cdots & 0 \\ w_{3,1} & w_{3,2} & w_{3,3} & w_{3,4} & \cdots & w_{3,d} \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ w_{h,1} & w_{h,2} & w_{h,3} & w_{h,4} & \cdots & w_{h,d} \end{bmatrix}_{h \times d} \tag{28}$$

$$\boldsymbol{W}_V = \begin{bmatrix} 0 & 0 & 1 & 0 & \cdots & 0 \\ 1 & 0 & 0 & 0 & \cdots & 0 \\ w'_{3,1} & w'_{3,2} & w'_{3,3} & w'_{3,4} & \cdots & w'_{3,d} \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ w'_{h,1} & w'_{h,2} & w'_{h,3} & w'_{h,4} & \cdots & w'_{h,d} \end{bmatrix}_{h \times d} \tag{29}$$

[Note: The PDF labels Eq. (29) as $\boldsymbol{W}_V$, but the surrounding text states "we construct the weights $\boldsymbol{W}_Q, \boldsymbol{W}_K$" and that "$\boldsymbol{W}_V$ and $\boldsymbol{W}_O$ can take any arbitrary values." The matrix structure in Eq. (29) is consistent with $\boldsymbol{W}_K$ (it produces the key vectors in Eq. (32)), suggesting a labeling error in the paper.]

where $w_{i,j}, w'_{i,j} \in \mathbb{R}$ can take any arbitrary value. Their corresponding $\boldsymbol{W}_V$ and $\boldsymbol{W}_O$ can take any arbitrary values as long as they do not override the first three dimensions of the residual stream.

**Verification:**

[p. 22] Now verify that for any input sequence $\boldsymbol{x} = [\texttt{<bos>}, x_1, \ldots, x_T]$, the attention dot product between query $\boldsymbol{q}_t$ and key $\boldsymbol{k}_i$ at positions $t$ and $i$ ($t \geq i$) will depend on the relative distance between tokens.

First, assume that absolute positions are computed in the hidden state $\boldsymbol{H}^{(l)}$ for $l \geq 1$, as stated in Theorem 1. Specifically,

$$\boldsymbol{H}^{(l)} = \begin{bmatrix} 1 & 1 & 1 & 1 & \cdots & 1 \\ 1 & 0 & 0 & 0 & \cdots & 0 \\ 1 & 2 & 3 & 4 & \cdots & T+1 \\ h_{4,1} & h_{4,2} & h_{4,3} & h_{4,4} & \cdots & h_{4,T+1} \\ \vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\ h_{d,1} & h_{d,2} & h_{d,3} & h_{d,4} & \cdots & h_{d,T+1} \end{bmatrix}_{d \times (T+1)} \tag{30}$$

where $h_{i,j} \in \mathbb{R}$ can be any arbitrary value as the first three dimensions of the hidden state are reserved for PE computation. The rest of the dimensions can take any arbitrary values as in regular computation of Transformers.

The attention computations at position $1 \leq t \leq T + 1$. Use $\boldsymbol{W}_Q$ to compute the query vector $\boldsymbol{q}_t$ by applying $\boldsymbol{q}_t = \boldsymbol{W}_Q \boldsymbol{h}_t^{(l)}$:

$$\boldsymbol{q}_t = [1, -t, q_3, \ldots, q_h]^\top \tag{31}$$

where $q_j \in \mathbb{R}$ can take any arbitrary value. Next, compute the key vectors by applying $\boldsymbol{k}_i = \boldsymbol{W}_K \boldsymbol{h}_i^{(l)}$:

$$\boldsymbol{k}_1 = \begin{pmatrix} 1 \\ 1 \\ k_{3,1} \\ \vdots \\ k_{h,1} \end{pmatrix} \quad \boldsymbol{k}_2 = \begin{pmatrix} 2 \\ 1 \\ k_{3,2} \\ \vdots \\ k_{h,2} \end{pmatrix} \quad \boldsymbol{k}_3 = \begin{pmatrix} 3 \\ 1 \\ k_{3,3} \\ \vdots \\ k_{h,3} \end{pmatrix} \quad \cdots \quad \boldsymbol{k}_t = \begin{pmatrix} t \\ 1 \\ k_{3,t} \\ \vdots \\ k_{h,t} \end{pmatrix} \tag{32}$$

where $k_{(\cdot,\cdot)} \in \mathbb{R}$ can have any arbitrary value. So, for $\boldsymbol{k}_i$:

$$\boldsymbol{k}_i = [i, 1, k_{3,i}, \ldots, k_{h,i}]^\top \tag{33}$$

[p. 23] Next, present the attention dot product between $\boldsymbol{q}_t$ and $\boldsymbol{k}_i$:

$$\langle \boldsymbol{q}_t, \boldsymbol{k}_i \rangle = 1 \cdot i + (-t) \cdot 1 + q_3 \cdot k_{3,i} + \cdots + q_h \cdot k_{h,i} \tag{34}$$

$$= i - t + \sum_{j=3}^{h} q_j \cdot k_{j,i} \tag{35}$$

$$= \left( \sum_{j=3}^{h} q_j \cdot k_{j,i} \right) - (t - i) \tag{36}$$

$$= f_{\text{cnt}}(\boldsymbol{q}_t, \boldsymbol{k}_i) + f_{\text{rel}}(t - i) \tag{37}$$

Thus, the dot product between $\boldsymbol{q}_t$ and $\boldsymbol{k}_i$ depends on the relative distance between tokens (assuming the rest of the terms do not cancel out which can be easily avoided by setting the respective weights in Equations (28) and (29)). Note that the proof uses the linear spacing between tokens, but the MLP the first layer can write any arbitrary function of absolute positions to the third dimension of the hidden state, which enables more complex relative encoding schemes. $\square$
