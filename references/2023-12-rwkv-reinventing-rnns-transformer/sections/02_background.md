# 2 Background [p. 2-3]

The authors briefly review the fundamentals of RNNs and Transformers.

## 2.1 Recurrent Neural Networks (RNNs)

[p. 2]

Popular RNN architectures such as LSTM (Hochreiter and Schmidhuber, 1997) and GRU (Chung et al., 2014) are characterized by the following formulation (shown for LSTM, others can be reasoned similarly):

$$f_t = \sigma_g(W_f x_t + U_f h_{t-1} + b_f), \quad (1)$$

Forget gate.

$$i_t = \sigma_g(W_i x_t + U_i h_{t-1} + b_i), \quad (2)$$

Input gate.

$$o_t = \sigma_g(W_o x_t + U_o h_{t-1} + b_o), \quad (3)$$

Output gate.

$$\tilde{c}_t = \sigma_c(W_c x_t + U_c h_{t-1} + b_c), \quad (4)$$

Candidate cell state.

$$c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t, \quad (5)$$

Cell state update.

$$h_t = o_t \odot \sigma_h(c_t). \quad (6)$$

Hidden state output.

Although RNNs can be factored into two linear blocks ($W$ and $U$) and an RNN-specific block (1)-(6), as noted by Bradbury et al. (2017), the data dependency relying on previous time steps prohibits parallelizing these typical RNNs.

## 2.2 Transformers and AFT

[p. 2-3]

Introduced by Vaswani et al. (2017), Transformers are the dominant architecture for several NLP tasks. Instead of operating on sequences step-by-step like RNNs, Transformers rely on attention mechanisms to capture relationships between all input and all output tokens:

$$\text{Attn}(Q, K, V) = \text{softmax}(QK^\top)V, \quad (7)$$

Standard attention mechanism, where the multi-headness and scaling factor $\frac{1}{\sqrt{d_k}}$ is omitted for convenience. The core $QK^\top$ multiplication is an ensemble of pairwise attention scores between each token in a sequence, which can be decomposed as vector operations:

[p. 3]

$$\text{Attn}(Q, K, V)_t = \frac{\sum_{i=1}^{T} e^{q_t^\top k_i} \odot v_i}{\sum_{i=1}^{T} e^{q_t^\top k_i}}. \quad (8)$$

Attention decomposed as vector operations for a single output position $t$.

AFT (Zhai et al., 2021), alternately formulates:

$$\text{Attn}^+(W, K, V)_t = \frac{\sum_{i=1}^{t} e^{w_{t,i} + k_i} \odot v_i}{\sum_{i=1}^{t} e^{w_{t,i} + k_i}}, \quad (9)$$

where $\{w_{t,i}\} \in R^{T \times T}$ is the learned pair-wise position biases, and each $w_{t,i}$ is a scalar.

Inspired by AFT, RWKV takes a similar approach. However, for simplicity, it modifies the interaction weights so that it can be transformed into an RNN. Each $w_{t,i}$ in RWKV is a channel-wise time decay vector multiplied by the relative position and traced backward from current time as it decays:

$$w_{t,i} = -(t - i)w, \quad (10)$$

where $w \in (R_{\geq 0})^d$, with $d$ the number of channels. The authors require $w$ to be non-negative to ensure that $e^{w_{t,i}} \leq 1$ and the per-channel weights decay backwards in time.
