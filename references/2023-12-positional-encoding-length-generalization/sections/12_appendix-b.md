# Appendix B: Background [p. 16-19]

## B.1 Preliminaries [p. 16-17]

[p. 16] This section lays the groundwork and introduces the notation used throughout the paper. It is referred to in Appendices C.1 and C.2.

Let $f_\theta$ be a decoder-only Transformer model, where $\theta$ denotes the full set of model parameters. $f_\theta$ processes the input sequence $\boldsymbol{x} = [x_0, x_1, \ldots, x_T]$ and maps it to the output sequence $\boldsymbol{y} = [y_0, y_1, \ldots, y_T]$ by applying a sequence of Transformer layers. Being decoder-only means the attention mechanism in each layer is causal, i.e. the attention weights are computed based on the previous positions only.

The layer $\text{TLayer}^{(l)}(\boldsymbol{H}^{(l-1)}; \theta_l)$, consisting of self-attention heads and a feed-forward sub-layer, reads the previous hidden state $\boldsymbol{H}^{(l-1)}$ and produces the hidden state at layer $l$: $\boldsymbol{H}^l$, where $l$ is the layer index, and $\theta_l$ is the set of parameters of the $l$-th layer. Each hidden state $\boldsymbol{H}^{(l)} \in \mathbb{R}^{d \times (T+1)}$ is a matrix where column $t$, denoted as $\boldsymbol{h}_t^{(l)}$, is the hidden state at position $t$.

A layer $l$ is parameterized by a set of parameters $\theta_l = \{(W_Q^m, W_K^m, W_V^m, W_O^m)_m, W_1, W_2\}$, where $W_Q^m, W_K^m, W_V^m \in \mathbb{R}^{h \times d}$ and $W_O^m \in \mathbb{R}^{d \times h}$ are the query, key, value, and output matrices of the $m$-th head, respectively. $W_1, W_2 \in \mathbb{R}^{d \times k \cdot d}$ are the weight matrices of the feed-forward sub-layer. $d$ denotes the model's hidden state size, $h$ is the attention dimension (where $h = \frac{d}{\# \text{ heads}}$), and $k$ is a multiplier of the hidden state size in the feed-forward sub-layer (it is usually set to 4 in common implementations of the Transformer). The layer index $l$ and the attention head index $m$ are dropped when clear from context.

The Transformer layer $\text{TLayer}^{(l)}$ processes each column of $\boldsymbol{H}^{(l-1)}$ independently and in parallel to produce the output. The computation of the $t$-th column of $\boldsymbol{H}^{(l)}$ is as follows:

$$\boldsymbol{h}_t^{(l)} = \text{FF}(\lambda(\boldsymbol{a}_t + \boldsymbol{h}_t^{(l-1)})) + \boldsymbol{a}_t + \boldsymbol{h}_t^{(l-1)} \tag{3}$$

where FF is the feed-forward sub-layer, $\lambda$ is layer normalization, and $\boldsymbol{a}_t \in \mathbb{R}^d$ is the output of the multi-head self-attention sub-layer at position $t$. Specifically, $\boldsymbol{a}_t$ is computed as:

$$\boldsymbol{a}_t = \sum_m \text{Attn}^{(m)}(\boldsymbol{h}_t^{(l-1)}, \boldsymbol{H}^{(l-1)}) \tag{4}$$

where $\text{Attn}^{(m)}$ is the $m$-th attention head. Let $o_t \in \mathbb{R}^d$ denote the output of an attention head at position $t$. Then, $\boldsymbol{o}_t$ is computed as:

$$\boldsymbol{o}_t = \boldsymbol{W}_O \left( \sum_{i \leq t} \hat{\alpha}_i \boldsymbol{v}_i \right) \tag{5}$$

where $\hat{\boldsymbol{\alpha}} = \text{softmax}(\boldsymbol{\alpha}) \in \mathbb{R}^{(t+1)}$, and $\boldsymbol{\alpha}$ is the attention weight vector such that:

$$\boldsymbol{\alpha} = [\langle \boldsymbol{q}_t, \boldsymbol{k}_0 \rangle, \langle \boldsymbol{q}_t, \boldsymbol{k}_1 \rangle, \ldots, \langle \boldsymbol{q}_t, \boldsymbol{k}_t \rangle]^\top \tag{6}$$

[p. 17] where $\boldsymbol{q}_t = \boldsymbol{W}_Q \boldsymbol{h}_t^{(l-1)} \in \mathbb{R}^h$, $\boldsymbol{k}_i = \boldsymbol{W}_K \boldsymbol{h}_i^{(l-1)} \in \mathbb{R}^h$, and $\boldsymbol{v}_i = \boldsymbol{W}_V \boldsymbol{h}_i^{(l-1)} \in \mathbb{R}^h$. $\langle \cdot, \cdot \rangle$ denotes the dot product operation.

The feed-forward sub-layer $\text{FF}(\cdot) \in \mathbb{R}^d$ is a two-layer MLP:

$$\text{FF}(\boldsymbol{x}) = \boldsymbol{W}_2 \sigma(\boldsymbol{W}_1^\top \boldsymbol{x}) \tag{7}$$

where $\sigma$ is a non-linear activation function (usually ReLU or GeLU (Hendrycks and Gimpel, 2020)). Additionally, $\lambda(\cdot) \in \mathbb{R}^d$ is layer normalization (Ba et al., 2016). The authors take the *additive* view of attention heads in Equation (4) (Elhage et al., 2021) instead of *concatenate and multiple* view (Vaswani et al., 2017) as it is easier to understand and analyze, noting they are mathematically equivalent (Elhage et al., 2021).

The hidden state is initialized with a learned embedding of the input sequence $\boldsymbol{H}^{(0)} = \boldsymbol{W}_E \boldsymbol{X}$, where $\boldsymbol{W}_E \in \mathbb{R}^{d \times V}$ is the embedding matrix and $\boldsymbol{X} \in \mathbb{R}^{V \times (T+1)}$ is the one-hot encoded input sequence. $V$ is the vocabulary size.

## B.2 Positional Encoding [p. 17-19]

[p. 17] Almost all positional encoding methods can be explained and formulated as how they implement the dot product operation in Equation (6). This section explains how the dot product $\langle \boldsymbol{q}_t, \boldsymbol{k}_i \rangle$ is implemented in different positional encoding schemes.

### Absolute Positional Encoding (APE)

[p. 17] APE involves assigning a position vector $\boldsymbol{p}_i$ to each absolute position $i$ and combining them with word embeddings before inputting them into the model. APE first modifies how the hidden state is initialized:

$$\boldsymbol{H}^{(0)} = \boldsymbol{W}_E \boldsymbol{X} + \boldsymbol{W}_P \boldsymbol{P} \tag{8}$$

where $\boldsymbol{W}_P \in \mathbb{R}^{d \times T}$ is the positional embedding matrix and $\boldsymbol{P} \in \mathbb{R}^{V_p \times (T+1)}$ is the one-hot encoded absolute position sequence. $V_p$ is the maximum absolute position. Therefore, the hidden state at column $j$ is:

$$\boldsymbol{h}_j^{(0)} = \boldsymbol{e}_j + \boldsymbol{p}_j \tag{9}$$

where $\boldsymbol{e}_j \in \mathbb{R}^d$ is the word embedding of token $x_j$ and $\boldsymbol{p}_j \in \mathbb{R}^d$ is the positional embedding for position $j$. Then, the dot product for the first layer in Equation (6) is computed as:

$$\langle \boldsymbol{q}_t, \boldsymbol{k}_i \rangle = \langle \boldsymbol{W}_Q \boldsymbol{h}_t^{(0)}, \boldsymbol{W}_K \boldsymbol{h}_i^{(0)} \rangle$$
$$= \langle \boldsymbol{W}_Q (\boldsymbol{e}_t + \boldsymbol{p}_t), \boldsymbol{W}_K (\boldsymbol{e}_i + \boldsymbol{p}_i) \rangle$$
$$= (\boldsymbol{W}_Q (\boldsymbol{e}_t + \boldsymbol{p}_t))^\top (\boldsymbol{W}_K (\boldsymbol{e}_i + \boldsymbol{p}_i))$$
$$= \boldsymbol{e}_t^\top \boldsymbol{W}_Q^\top \boldsymbol{W}_K \boldsymbol{e}_i + \boldsymbol{e}_t^\top \boldsymbol{W}_Q^\top \boldsymbol{W}_K \boldsymbol{p}_i$$
$$+ \boldsymbol{p}_t^\top \boldsymbol{W}_Q^\top \boldsymbol{W}_K \boldsymbol{e}_i + \boldsymbol{p}_t^\top \boldsymbol{W}_Q^\top \boldsymbol{W}_K \boldsymbol{p}_i \tag{10}$$

[p. 18] In the learned variant of APE, $\boldsymbol{p}_j \in \mathbb{R}^d$ is learned during training. In the sinusoidal variant, $\boldsymbol{p}_j$ is calculated using a non-parametric function. Specifically, $\boldsymbol{p}_j$ is computed as:

$$\boldsymbol{p}_j = \left[\sin(\omega_1 \cdot j), \cos(\omega_1 \cdot j), \sin(\omega_2 \cdot j), \cos(\omega_2 \cdot j), \ldots, \sin(\omega_{d/2} \cdot j), \cos(\omega_{d/2} \cdot j)\right]^\top \tag{11}$$

where $\omega_i = \frac{1}{10000^{2i/d}}$.

### T5's Relative PE

[p. 18] The Relative bias in T5 is a type of relative positional encoding that initially calculates the relative distance $(t - i)$ between tokens at positions $t$ and $i$. This distance is then transformed into a scalar bias value $b$ and is incorporated into the dot product between the query and key. $b$ is learned during training. Thus, the dot product in every layer can be written as:

$$\langle \boldsymbol{q}_t, \boldsymbol{k}_i \rangle = \boldsymbol{q}_t^\top \boldsymbol{k}_i + b_{\text{bucket}(t-i)} \tag{12}$$

where

$$\text{bucket}(n) = \begin{cases} n & \text{if } n < \frac{\mathcal{B}}{2} \\ \frac{\mathcal{B}}{2} + \left\lfloor \frac{\log\left(\frac{n}{\mathcal{B}/2}\right)}{\log\left(\frac{\mathcal{D}}{\mathcal{B}/2}\right)} \times \frac{\mathcal{B}}{2} \right\rfloor & \text{if } \frac{\mathcal{B}}{2} \leq n < \mathcal{D} \\ \mathcal{B} - 1 & \text{if } n \geq \mathcal{D} \end{cases}$$

This function maps the relative distance $d$ to a bucket index, which will be used to look up the weight corresponding to that bucket. $\mathcal{B}$ is the number of buckets, $\mathcal{D}$ is the maximum distance. It assigns half of the buckets to distances smaller than $\frac{\mathcal{D}}{2}$ with linear spacing and the other half to distances larger than $\frac{\mathcal{D}}{2}$ with logarithmic spacing. The weight for distances larger than $\mathcal{D}$ is the same. This is to facilitate generalization to unseen distances. In the original implementation of T5, $\mathcal{B} = 32$ and $\mathcal{D} = 128$.

An example of the bucket function with $\mathcal{B} = 5$ and $\mathcal{D} = 6$:

Input relative distance matrix:

```
0  0  0  0  0  0  0  0  0  0
1  0  0  0  0  0  0  0  0  0
2  1  0  0  0  0  0  0  0  0
3  2  1  0  0  0  0  0  0  0
4  3  2  1  0  0  0  0  0  0
5  4  3  2  1  0  0  0  0  0
6  5  4  3  2  1  0  0  0  0
7  6  5  4  3  2  1  0  0  0
8  7  6  5  4  3  2  1  0  0
9  8  7  6  5  4  3  2  1  0
```

Output bucket index matrix (after applying bucket function):

```
0  0  0  0  0  0  0  0  0  0
1  0  0  0  0  0  0  0  0  0
2  1  0  0  0  0  0  0  0  0
2  2  1  0  0  0  0  0  0  0
3  2  2  1  0  0  0  0  0  0
3  3  2  2  1  0  0  0  0  0
4  3  3  2  2  1  0  0  0  0
4  4  3  3  2  2  1  0  0  0
4  4  4  3  3  2  2  1  0  0
4  4  4  4  3  3  2  2  1  0
```

The left matrix shows the input relative distances and the right matrix shows the corresponding bucket indices after applying the bucket function.

### ALiBi

[p. 18] Similar to T5's Relative PE, ALiBi subtracts a scalar bias from the attention score. As the distance between the query and key tokens increases, the bias grows linearly. Specifically, the dot product in every layer can be written as:

$$\langle \boldsymbol{q}_t, \boldsymbol{k}_i \rangle = \boldsymbol{q}_t^\top \boldsymbol{k}_i - (t - i) \cdot C^{(m+1)} \tag{13}$$

where $m$ is head index and $C$ is a constant defined as:

$$C = 2^{-2^{-\log_2(\# \text{ heads} + 3)}}$$

For example, if the number of heads is 8, then we have $\frac{1}{2}, \frac{1}{2^2}, \ldots, \frac{1}{2^8}$ (Press et al., 2022).

### Rotary

[p. 18-19] Rotary is a relative PE that applies a rotation to the query and key representations based on their absolute positions before dot product attention. Due to this rotation, the attention dot product relies solely on the relative distance between tokens.

First, formulating Rotary for model dimension $d = 2$, the positional encoding defines the dot product as:

$$\langle \boldsymbol{q}_t, \boldsymbol{k}_i \rangle = \langle \text{Rot}(\boldsymbol{q}_t, t), \text{Rot}(\boldsymbol{k}_i, i) \rangle$$
$$= \langle \boldsymbol{R}^{t\theta} \boldsymbol{q}_t, \boldsymbol{R}^{i\theta} \boldsymbol{k}_i \rangle$$
$$= (\boldsymbol{R}^{t\theta} \boldsymbol{q}_t)^\top (\boldsymbol{R}^{i\theta} \boldsymbol{k}_i)$$
$$= \boldsymbol{q}_t^\top (\boldsymbol{R}^{(t\theta)})^\top \boldsymbol{R}^{i\theta} \boldsymbol{k}_i$$
$$= \boldsymbol{q}_t^\top \boldsymbol{R}^{(i-t)\theta} \boldsymbol{k}_i \tag{14}$$

where $\boldsymbol{R}^{t\theta}$ is a rotation matrix that rotates $\boldsymbol{x}$ by $t\theta$ radians:

$$\boldsymbol{R}^{n\theta} = \begin{bmatrix} \cos(n\theta) & -\sin(n\theta) \\ \sin(n\theta) & \cos(n\theta) \end{bmatrix} \tag{15}$$

[p. 19] For $d > 2$, Rotary applies the same approach on every two consecutive dimensions of $\boldsymbol{q}_t$ and $\boldsymbol{k}_i$, but with different $\theta$ angles. Refer to Su et al. (2021) for the exact formulation.

### NoPE

[p. 19] NoPE does not explicitly encode positional encodings. So, the dot product in every layer can be written as:

$$\langle \boldsymbol{q}_t, \boldsymbol{k}_i \rangle = \boldsymbol{q}_t^\top \boldsymbol{k}_i \tag{16}$$
