# 2 Retentive Networks [p. 3-6]

Retentive network (RetNet) is stacked with L identical blocks, which follows a similar layout (i.e., residual connection, and pre-LayerNorm) as in Transformer [VSP+17]. Each RetNet block contains two modules: a multi-scale retention (MSR) module, and a feed-forward network (FFN) module. [p. 3]

Given an input sequence x = x_1 ... x_{|x|}, RetNet encodes the sequence in an autoregressive way. The input vectors {x_i}_{i=1}^{|x|} is first packed into X^0 = [x_1, ..., x_{|x|}] in R^{|x| x d_model}, where d_model is hidden dimension. Then contextualized vector representations X^l = RetNet_l(X^{l-1}), l in [1, L] are computed. [p. 3]

## 2.1 Retention

[p. 3]

The retention mechanism has a dual form of recurrence and parallelism, so the models can be trained in a parallel way while recurrently conducting inference.

Given input X in R^{|x| x d_model}, project it to a one-dimensional function v(n) = X_n . w_V. Consider a sequence modeling problem that maps v(n) -> o(n) through states s_n. Let v_n, o_n denote v(n), o(n) for simplicity. The mapping is formulated in a recurrent manner:

$$s_n = A s_{n-1} + K_n^\top v_n, \qquad A \in \mathbb{R}^{d \times d}, K_n \in \mathbb{R}^{1 \times d}$$
$$o_n = Q_n s_n = \sum_{m=1}^{n} Q_n A^{n-m} K_m^\top v_m, \qquad Q_n \in \mathbb{R}^{1 \times d} \tag{1}$$

where we map v_n to the state vector s_n, and then implement a linear transform to encode sequence information recurrently. [p. 3]

Next, the projection Q_n, K_n is made content-aware:

$$Q = X W_Q, \quad K = X W_K \tag{2}$$

where W_Q, W_K in R^{d x d} are learnable matrices. [p. 3]

The matrix A = Lambda(gamma e^{i theta}) Lambda^{-1} is diagonalized, where gamma, theta in R^d. Then A^{n-m} = Lambda(gamma e^{i theta})^{n-m} Lambda^{-1}. By absorbing Lambda into W_Q and W_K, Equation (1) can be rewritten as:

$$o_n = \sum_{m=1}^{n} Q_n (\gamma e^{i\theta})^{n-m} K_m^\top v_m$$
$$= \sum_{m=1}^{n} (Q_n (\gamma e^{i\theta})^n)(K_m (\gamma e^{i\theta})^{-m})^\top v_m \tag{3}$$

where Q_n(gamma e^{i theta})^n, K_m(gamma e^{i theta})^{-m} is known as xPos [SDP+22], i.e., a relative position embedding proposed for Transformer. gamma is further simplified as a scalar, and Equation (3) becomes:

$$o_n = \sum_{m=1}^{n} \gamma^{n-m} (Q_n e^{in\theta})(K_m e^{im\theta})^\dagger v_m \tag{4}$$

where † is the conjugate transpose. The formulation is easily parallelizable within training instances. [p. 3]

In summary, the authors start with recurrent modeling as shown in Equation (1), and then derive its parallel formulation in Equation (4). The original mapping v(n) -> o(n) is considered as vectors and the retention mechanism is obtained. [p. 3]

### The Parallel Representation of Retention

[p. 3]

As shown in Figure 3a, the retention layer is defined as:

$$Q = (X W_Q) \odot \Theta, \quad K = (X W_K) \odot \overline{\Theta}, \quad V = X W_V$$
$$\Theta_n = e^{in\theta}, \quad D_{nm} = \begin{cases} \gamma^{n-m}, & n \geq m \\ 0, & n < m \end{cases}$$
$$\text{Retention}(X) = (Q K^\top \odot D) V \tag{5}$$

where Theta_bar is the complex conjugate of Theta, and D in R^{|x| x |x|} combines causal masking and exponential decay along relative distance as one matrix. Similar to self-attention, the parallel representation enables training the models with GPUs efficiently. [p. 3]

### The Recurrent Representation of Retention

[p. 4]

As shown in Figure 3b, the proposed mechanism can also be written as recurrent neural networks (RNNs), which is favorable for inference. For the n-th timestep, the output is recurrently obtained as:

$$S_n = \gamma S_{n-1} + K_n^\top V_n$$
$$\text{Retention}(X_n) = Q_n S_n, \quad n = 1, \cdots, |x| \tag{6}$$

where Q, K, V, gamma are the same as in Equation (5). [p. 4]

### The Chunkwise Recurrent Representation of Retention

[p. 4]

A hybrid form of parallel representation and recurrent representation is available to accelerate training, especially for long sequences. Input sequences are divided into chunks. Within each chunk, the parallel representation (Equation (5)) is followed. Cross-chunk information is passed following the recurrent representation (Equation (6)). Let B denote the chunk length. The retention output of the i-th chunk is computed via:

$$Q_{[i]} = Q_{Bi:B(i+1)}, \quad K_{[i]} = K_{Bi:B(i+1)}, \quad V_{[i]} = V_{Bi:B(i+1)}$$
$$R_i = K_{[i]}^\top (V_{[i]} \odot \zeta) + \gamma^B R_{i-1}, \quad \zeta_j = \gamma^{B-j-1}$$
$$\text{Retention}(X_{[i]}) = \underbrace{(Q_{[i]} K_{[i]}^\top \odot D) V_{[i]}}_{\text{Inner-Chunk}} + \underbrace{(Q_{[i]} R_{i-1}) \odot \xi}_{\text{Cross-Chunk}}, \quad \xi_{ij} = \gamma^{i+1} \tag{7}$$

where [i] indicates the i-th chunk, i.e., x_{[i]} = [x_{(i-1)B+1}, ..., x_{iB}]. [p. 4]

## 2.2 Gated Multi-Scale Retention

[p. 4]

h = d_model / d retention heads are used in each layer, where d is the head dimension. The heads use different parameter matrices W_Q, W_K, W_V in R^{d x d}. Moreover, **multi-scale retention (MSR)** assigns different gamma for each head. For simplicity, gamma is set identical among different layers and kept fixed. A swish gate [HG16, RZL17] is added to increase the non-linearity of retention layers. Formally, given input X, the layer is defined as:

$$\gamma = 1 - 2^{-5 - \text{arange}(0, h)} \in \mathbb{R}^h$$
$$\text{head}_i = \text{Retention}(X, \gamma_i)$$
$$Y = \text{GroupNorm}_h(\text{Concat}(\text{head}_1, \cdots, \text{head}_h))$$
$$\text{MSR}(X) = (\text{swish}(X W_G) \odot Y) W_O \tag{8}$$

where W_G, W_O in R^{d_model x d_model} are learnable parameters, and GroupNorm [WH18] normalizes the output of each head, following SubLN proposed in [SPP+19]. The heads use multiple gamma scales, which results in different variance statistics. So the head outputs are normalized separately. [p. 4]

The pseudocode of retention is summarized in Figure 4. [p. 4]

### Retention Score Normalization

[p. 5]

The scale-invariant nature of GroupNorm is utilized to improve the numerical precision of retention layers. Specifically, multiplying a scalar value within GroupNorm does not affect outputs and backward gradients, i.e., GroupNorm(alpha * head_i) = GroupNorm(head_i). Three normalization factors are implemented in Equation (5): [p. 5]

1. Normalize QK^T as QK^T / sqrt(d).
2. Replace D with D_tilde_{nm} = D_{nm} / sqrt(sum_{i=1}^{n} D_{ni}).
3. Let R denote the retention scores R = QK^T odot D, normalize it as R_tilde_{nm} = R_{nm} / max(|sum_{i=1}^{n} R_{ni}|, 1).

Then the retention output becomes Retention(X) = R_tilde V. The above tricks do not affect the final results while stabilizing the numerical flow of both forward and backward passes, because of the scale-invariant property. [p. 5]

## 2.3 Overall Architecture of Retention Networks

[p. 5]

For an L-layer retention network, multi-scale retention (MSR) and feed-forward network (FFN) are stacked to build the model. The input sequence {x_i}_{i=1}^{|x|} is transformed to vectors by a word embedding layer. The packed embeddings X^0 = [x_1, ..., x_{|x|}] in R^{|x| x d_model} are used as the input and the model output X^L is computed:

$$Y^l = \text{MSR}(\text{LN}(X^l)) + X^l$$
$$X^{l+1} = \text{FFN}(\text{LN}(Y^l)) + Y^l \tag{9}$$

where LN(.) is LayerNorm [BKH16]. The FFN part is computed as FFN(X) = gelu(X W_1) W_2, where W_1, W_2 are parameter matrices. [p. 5]

### Training

[p. 5]

The parallel (Equation (5)) and chunkwise recurrent (Equation (7)) representations are used during the training process. The parallelization within sequences or chunks efficiently utilizes GPUs to accelerate computation. Chunkwise recurrence is especially useful for long-sequence training, which is efficient in terms of both FLOPs and memory consumption. [p. 5]

### Inference

[p. 6]

The recurrent representation (Equation (6)) is employed during inference, which nicely fits autoregressive decoding. The O(1) complexity reduces memory and inference latency while achieving equivalent results. [p. 6]

## 2.4 Relation to and Differences from Previous Methods

[p. 6]

Table 1 compares RetNet with previous methods from various perspectives. The comparison results echo the "impossible triangle" presented in Figure 2. RetNet has linear memory complexity for long sequences due to the chunkwise recurrent representation. Comparisons with specific methods: [p. 6]

**Transformer** — The parallel representation of retention shares similar spirits as Transformers [VSP+17]. The most related Transformer variant is Lex Transformer [SDP+22] which implements xPos as position embeddings. As described in Equation (3), the derivation of retention aligns with xPos. In comparison with attention, retention removes softmax and enables recurrent formulation, which significantly benefits inference. [p. 6]

**S4** — Unlike Equation (2), if Q_n and K_n are content-unaware, the formulation can be degenerated to S4 [GGR21], where O = (QK^T, QAK^T, .., QA^{|x|-1}K^T) * V. [p. 6]

**Linear Attention** — The variants typically use various kernels phi(q_i) phi(k_j) / sum_{n=1}^{|x|} phi(q_i) phi(k_n) to replace the softmax function. However, linear attention struggles to effectively encode position information, rendering the models less performant. The authors reexamine sequence modeling from scratch, rather than aiming at approximating softmax. [p. 6]

**AFT/RWKV** — Attention Free Transformer (AFT) simplifies dot-product attention to element-wise operations and moves softmax to key vectors. RWKV replaces AFT's position embeddings with exponential decay and runs the models recurrently for training and inference. In comparison, retention preserves high-dimensional states to encode sequence information, which contributes to expressive ability and better performance. [p. 6]

**xPos/RoPE** — Compared with relative position embedding methods proposed for Transformers, Equation (3) presents a similar formulation as xPos [SDP+22] and RoPE [SLP+21]. [p. 6]

**Sub-LayerNorm** — As shown in Equation (8), the retention layer uses Sub-LayerNorm [WMH+22] to normalize outputs. Because the multi-scale modeling leads to different variances for the heads, the original LayerNorm is replaced with GroupNorm. [p. 6]

## Figures

**Figure 3** (p. 4): "Dual form of RetNet. 'GN' is short for GroupNorm."

(a) Parallel representation: A diagram showing input X feeding into Q, K, V projections. Q and K undergo a transposed dot product, element-wise multiplied with D (the causal decay mask), then multiplied by V. The result passes through GN (GroupNorm) to produce output O. The flow is: X -> Q, K, V -> (QK^T odot D)V -> GN -> O.

(b) Recurrent representation: A diagram showing input X_n feeding into V_n, K_n, Q_n projections. K_n and V_n are combined via outer product. The recurrent state S_{n-1} is scaled by gamma and added to K_n^T V_n to produce S_n. The output O_n is computed as Q_n times S_n. Shows the recurrent state loop S_{n-1} -> gamma -> + K_n^T V_n -> S_n.

**Figure 4** (p. 5): "Pseudocode for the three computation paradigms of retention."

Contains Python-style pseudocode for three functions:

```python
def ParallelRetention(
    q, # bsz * num_head * len * qk_dim
    k, # bsz * num_head * len * qk_dim
    v, # bsz * num_head * len * v_dim
    decay_mask # num_head * len * len
):
    retention = q @ k.transpose(-1, -2)
    retention = retention * decay_mask
    output = retention @ v
    output = group_norm(output)
    return output

def RecurrentRetention(
    q, k, v, # bsz * num_head * len * qkv_dim
    past_kv, # bsz * num_head * qk_dim * v_dim
    decay # num_head * 1 * 1
):
    current_kv = decay * past_kv + k.unsqueeze(
        -1) * v.unsqueeze(-2)
    output = torch.sum(q.unsqueeze(-1) *
        current_kv, dim=-2)
    output = group_norm(output)
    return output, current_kv

def ChunkwiseRetention(
    q, k, v, # bsz * num_head * chunk_size * qkv_dim
    past_kv, # bsz * num_head * qk_dim * v_dim
    decay_mask, # num_head * chunk_size * chunk_size
    chunk_decay, # num_head * 1 * 1
    inner_decay, # num_head * chunk_size
):
    retention = q @ k.transpose(-1, -2)
    retention = retention * decay_mask
    inner_retention = retention @ v
    cross_retention = (q @ past_kv) * inner_decay
    retention = inner_retention + cross_retention
    output = group_norm(retention)
    current_kv = chunk_decay * past_kv + k.transpose(-1, -2) @ v
    return output, current_kv
```

## Tables

**Table 1** (p. 6): "Model comparison from various perspectives. RetNet achieves training parallelization, constant inference cost, linear long-sequence memory complexity, and good performance."

| Architectures | Training Parallelization | Inference Cost | Long-Sequence Memory Complexity | Performance |
|---|---|---|---|---|
| Transformer | Yes | O(N) | O(N^2) | Very Good |
| Linear Transformer | Yes | O(1) | O(N) | Poor |
| Recurrent NN | No | O(1) | O(N) | Poor |
| RWKV | No | O(1) | O(N) | Good |
| H3/S4 | Yes | O(1) | O(N log N) | Good |
| Hyena | Yes | O(N) | O(N log N) | Good |
| RetNet | Yes | O(1) | O(N) | Very Good |

Note: "Yes" = checkmark, "No" = cross, "Good" = single checkmark, "Very Good" = double checkmark, "Poor" = cross in the original table.
