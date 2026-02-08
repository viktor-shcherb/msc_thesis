# 2. Architecture [p. 6]

[p. 6] DeepSeek-V2 is still in the Transformer architecture (Vaswani et al., 2017), where each Transformer block consists of an attention module and a Feed-Forward Network (FFN). However, for both the attention module and the FFN, innovative architectures are designed and employed:

- **For attention:** MLA is designed, which utilizes low-rank key-value joint compression to eliminate the bottleneck of inference-time key-value cache, thus supporting efficient inference.
- **For FFNs:** The DeepSeekMoE architecture (Dai et al., 2024) is adopted, a high-performance MoE architecture that enables training strong models at an economical cost.

An illustration of the architecture is presented in Figure 2. Unless specifically stated, DeepSeek-V2 follows the settings of DeepSeek 67B (DeepSeek-AI, 2024) for other details (e.g., layer normalization and the activation function in FFNs). [p. 6]

## 2.1 Multi-Head Latent Attention: Boosting Inference Efficiency

[p. 6] Conventional Transformer models usually adopt Multi-Head Attention (MHA) (Vaswani et al., 2017), but during generation, its heavy Key-Value (KV) cache becomes the bottleneck that limits inference efficiency. To reduce the KV cache, Multi-Query Attention (MQA) (Shazeer, 2019) and Grouped-Query Attention (GQA) (Ainslie et al., 2023) are proposed. They require a smaller magnitude of KV cache, but their performance does not match MHA (ablation provided in Appendix D.1).

For DeepSeek-V2, an innovative attention mechanism called Multi-head Latent Attention (MLA) is designed. Equipped with low-rank key-value joint compression, MLA achieves better performance than MHA, but requires a significantly smaller amount of KV cache. A comparison between MLA and MHA is provided in Appendix D.2. [p. 6]

### 2.1.1 Preliminaries: Standard Multi-Head Attention

[p. 6] The standard MHA mechanism is introduced as background. Let $d$ be the embedding dimension, $n_h$ be the number of attention heads, $d_h$ be the dimension per head, and $\mathbf{h}_t \in \mathbb{R}^d$ be the attention input of the $t$-th token at an attention layer. Standard MHA first produces $\mathbf{q}_t, \mathbf{k}_t, \mathbf{v}_t \in \mathbb{R}^{d_h n_h}$ through three matrices $W^Q, W^K, W^V \in \mathbb{R}^{d_h n_h \times d}$, respectively:

$$\mathbf{q}_t = W^Q \mathbf{h}_t, \tag{1}$$

$$\mathbf{k}_t = W^K \mathbf{h}_t, \tag{2}$$

$$\mathbf{v}_t = W^V \mathbf{h}_t, \tag{3}$$

where Eq. (1) computes the query vector, Eq. (2) computes the key vector, and Eq. (3) computes the value vector, all by linear projection of the input hidden state.

---
[p. 7 continued]

Then, $\mathbf{q}_t, \mathbf{k}_t, \mathbf{v}_t$ will be sliced into $n_h$ heads for the multi-head attention computation:

$$[\mathbf{q}_{t,1}; \mathbf{q}_{t,2}; ...; \mathbf{q}_{t,n_h}] = \mathbf{q}_t, \tag{4}$$

$$[\mathbf{k}_{t,1}; \mathbf{k}_{t,2}; ...; \mathbf{k}_{t,n_h}] = \mathbf{k}_t, \tag{5}$$

$$[\mathbf{v}_{t,1}; \mathbf{v}_{t,2}; ...; \mathbf{v}_{t,n_h}] = \mathbf{v}_t, \tag{6}$$

where Eqs. (4)-(6) slice the concatenated query, key, and value vectors into per-head components.

$$\mathbf{o}_{t,i} = \sum_{j=1}^{t} \text{Softmax}_j \left( \frac{\mathbf{q}_{t,i}^T \mathbf{k}_{j,i}}{\sqrt{d_h}} \right) \mathbf{v}_{j,i}, \tag{7}$$

where Eq. (7) computes the attention output for head $i$ at position $t$ using scaled dot-product attention over all positions $j \leq t$.

$$\mathbf{u}_t = W^O [\mathbf{o}_{t,1}; \mathbf{o}_{t,2}; ...; \mathbf{o}_{t,n_h}], \tag{8}$$

where $\mathbf{q}_{t,i}, \mathbf{k}_{t,i}, \mathbf{v}_{t,i} \in \mathbb{R}^{d_h}$ denote the query, key, and value of the $i$-th attention head, respectively; $W^O \in \mathbb{R}^{d \times d_h n_h}$ denotes the output projection matrix. During inference, all keys and values need to be cached to accelerate inference, so MHA needs to cache $2n_h d_h l$ elements for each token. In model deployment, this heavy KV cache is a large bottleneck that limits the maximum batch size and sequence length. [p. 7]

**Figure 3** (p. 7): "Simplified illustration of Multi-Head Attention (MHA), Grouped-Query Attention (GQA), Multi-Query Attention (MQA), and Multi-head Latent Attention (MLA). Through jointly compressing the keys and values into a latent vector, MLA significantly reduces the KV cache during inference."

The figure shows four side-by-side diagrams comparing attention mechanisms. Each has rows for Queries, Keys, and Values, with hatched regions indicating what is cached during inference:
- **MHA:** All heads have distinct keys and values (all hatched/cached).
- **GQA:** Keys and values are shared among groups of heads (fewer hatched key/value blocks).
- **MQA:** A single key and value shared across all heads (minimal hatched blocks).
- **MLA:** All heads have distinct queries but keys and values are produced via projection from a single "Compressed Latent KV" vector (only the compressed latent KV is hatched/cached, with an arrow labeled "projection" from it to the keys and values).

### 2.1.2 Low-Rank Key-Value Joint Compression

[p. 7] The core of MLA is the low-rank joint compression for keys and values to reduce KV cache:

$$\mathbf{c}_t^{KV} = W^{DKV} \mathbf{h}_t, \tag{9}$$

where Eq. (9) compresses the input hidden state into a low-dimensional latent vector for keys and values.

$$\mathbf{k}_t^C = W^{UK} \mathbf{c}_t^{KV}, \tag{10}$$

where Eq. (10) up-projects the compressed latent vector to produce the key.

$$\mathbf{v}_t^C = W^{UV} \mathbf{c}_t^{KV}, \tag{11}$$

where Eq. (11) up-projects the compressed latent vector to produce the value.

Here $\mathbf{c}_t^{KV} \in \mathbb{R}^{d_c}$ is the compressed latent vector for keys and values; $d_c (\ll d_h n_h)$ denotes the KV compression dimension; $W^{DKV} \in \mathbb{R}^{d_c \times d}$ is the down-projection matrix; and $W^{UK}, W^{UV} \in \mathbb{R}^{d_h n_h \times d_c}$ are the up-projection matrices for keys and values, respectively. During inference, MLA only needs to cache $\mathbf{c}_t^{KV}$, so its KV cache has only $d_c l$ elements, where $l$ denotes the number of layers. In addition, during inference, since $W^{UK}$ can be absorbed into $W^Q$, and $W^{UV}$ can be absorbed into $W^O$, we even do not need to compute keys and values out for attention. Figure 3 intuitively illustrates how the KV joint compression in MLA reduces the KV cache. [p. 7]

---
[p. 8 continued]

Moreover, in order to reduce the activation memory during training, low-rank compression is also performed for the queries, even if it cannot reduce the KV cache:

$$\mathbf{c}_t^Q = W^{DQ} \mathbf{h}_t, \tag{12}$$

where Eq. (12) compresses the input hidden state into a low-dimensional latent vector for queries.

$$\mathbf{q}_t^C = W^{UQ} \mathbf{c}_t^Q, \tag{13}$$

where Eq. (13) up-projects the compressed latent vector to produce the query.

Here $\mathbf{c}_t^Q \in \mathbb{R}^{d_c'}$ is the compressed latent vector for queries; $d_c' (\ll d_h n_h)$ denotes the query compression dimension; and $W^{DQ} \in \mathbb{R}^{d_c' \times d}$, $W^{UQ} \in \mathbb{R}^{d_h n_h \times d_c'}$ are the down-projection and up-projection matrices for queries, respectively. [p. 8]

### 2.1.3 Decoupled Rotary Position Embedding

[p. 8] Following DeepSeek 67B (DeepSeek-AI, 2024), the authors intend to use Rotary Position Embedding (RoPE) (Su et al., 2024) for DeepSeek-V2. However, RoPE is incompatible with low-rank KV compression. To be specific, RoPE is position-sensitive for both keys and queries. If RoPE is applied for the keys $\mathbf{k}_t^C$, $W^{UK}$ in Equation 10 will be coupled with a position-sensitive RoPE matrix. In this way, $W^{UK}$ cannot be absorbed into $W^Q$ any more during inference, since a RoPE matrix related to the currently generating token will lie between $W^Q$ and $W^{UK}$ and matrix multiplication does not obey a commutative law. As a result, we must recompute the keys for all the prefix tokens during inference, which will significantly hinder the inference efficiency. [p. 8]

As a solution, the decoupled RoPE strategy is proposed that uses additional multi-head queries $\mathbf{q}_{t,i}^R \in \mathbb{R}^{d_h^R}$ and a shared key $\mathbf{k}_t^R \in \mathbb{R}^{d_h^R}$ to carry RoPE, where $d_h^R$ denotes the per-head dimension of the decoupled queries and key. Equipped with the decoupled RoPE strategy, MLA performs the following computation:

$$[\mathbf{q}_{t,1}^R; \mathbf{q}_{t,2}^R; ...; \mathbf{q}_{t,n_h}^R] = \mathbf{q}_t^R = \text{RoPE}(W^{QR} \mathbf{c}_t^Q), \tag{14}$$

where Eq. (14) produces the decoupled multi-head RoPE queries from the compressed query latent.

$$\mathbf{k}_t^R = \text{RoPE}(W^{KR} \mathbf{h}_t), \tag{15}$$

where Eq. (15) produces the shared decoupled RoPE key directly from the input hidden state.

$$\mathbf{q}_{t,i} = [\mathbf{q}_{t,i}^C; \mathbf{q}_{t,i}^R], \tag{16}$$

where Eq. (16) concatenates the compressed query component and the RoPE query component for each head.

$$\mathbf{k}_{t,i} = [\mathbf{k}_{t,i}^C; \mathbf{k}_t^R], \tag{17}$$

where Eq. (17) concatenates the compressed key component and the shared RoPE key for each head.

$$\mathbf{o}_{t,i} = \sum_{j=1}^{t} \text{Softmax}_j \left( \frac{\mathbf{q}_{t,i}^T \mathbf{k}_{j,i}}{\sqrt{d_h + d_h^R}} \right) \mathbf{v}_{j,i}^C, \tag{18}$$

where Eq. (18) computes scaled dot-product attention using the concatenated queries and keys (dimension $d_h + d_h^R$) and the compressed values.

$$\mathbf{u}_t = W^O [\mathbf{o}_{t,1}; \mathbf{o}_{t,2}; ...; \mathbf{o}_{t,n_h}], \tag{19}$$

where Eq. (19) applies the output projection to the concatenated per-head outputs.

Here $W^{QR} \in \mathbb{R}^{d_h^R n_h \times d_c'}$ and $W^{KR} \in \mathbb{R}^{d_h^R \times d}$ are matrices to produce the decoupled queries and key, respectively; $\text{RoPE}(\cdot)$ denotes the operation that applies RoPE matrices; and $[\cdot ; \cdot]$ denotes the concatenation operation. During inference, the decoupled key should also be cached. Therefore, DeepSeek-V2 requires a total KV cache containing $(d_c + d_h^R)l$ elements. [p. 8]

The complete computation process of MLA with full formulas is also organized and provided in Appendix C.

### 2.1.4 Comparison of Key-Value Cache

[p. 8-9] A comparison of the KV cache per token among different attention mechanisms is demonstrated in Table 1. MLA requires only a small amount of KV cache, equal to GQA with only 2.25 groups, but can achieve stronger performance than MHA.

**Table 1** | Comparison of the KV cache per token among different attention mechanisms. $n_h$ denotes the number of attention heads, $d_h$ denotes the dimension per attention head, $l$ denotes the number of layers, $n_g$ denotes the number of groups in GQA, and $d_c$ and $d_h^R$ denote the KV compression dimension and the per-head dimension of the decoupled queries and key in MLA, respectively. The amount of KV cache is measured by the number of elements, regardless of the storage precision. For DeepSeek-V2, $d_c$ is set to $4d_h$ and $d_h^R$ is set to $\frac{d_h}{2}$. So, its KV cache is equal to GQA with only 2.25 groups, but its performance is stronger than MHA. [p. 9]

| Attention Mechanism | KV Cache per Token (# Element) | Capability |
|---|---|---|
| Multi-Head Attention (MHA) | $2n_h d_h l$ | Strong |
| Grouped-Query Attention (GQA) | $2n_g d_h l$ | Moderate |
| Multi-Query Attention (MQA) | $2d_h l$ | Weak |
| MLA (Ours) | $(d_c + d_h^R)l \approx \frac{9}{2} d_h l$ | Stronger |
