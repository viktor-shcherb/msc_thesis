# Background [p. 4–5]

[p. 4–5] The paper discusses how φ(Q)(φ(K^T)^T), where φ represents a non-negative feature-map function, can be computed as an RNN in O(1) time per step by adding φ(k_i^T)v_i to a recurrent state at each time step i, or trained in parallel much like MHA. This accomplishes the main goals outlined above, but naive linear attention suffers from significantly reduced performance compared to MHA-based transformers.

## Attention Free Transformer (AFT)

[p. 5] A modified form of linear attention, the Attention Free Transformer (AFT) (Zhai et al., 2021), paved the way for the RWKV architecture, by using a number of attention heads equal to the size of the feature dimension and incorporating a set of learned pairwise positional biases, denoted as w:

$$\text{AFTAttn}_i = \sigma_q(q_i) \odot \frac{\sum_{j=1}^{i} \exp(k_j + w_{i,j}) \odot v_j}{\sum_{j=1}^{i} \exp(k_j + w_{i,j})}$$ (1)

where σ_q is an activation function.

## RWKV-4

[p. 5] RWKV-4 reformulates the AFT equation by replacing the pair-wise positional biases with a channel-wise vector of additive weight decay rates w. It also adds a bonus term u to offset the weight of only the current input specially:

$$\text{wkv}_i = \frac{\sum_{j=1}^{i-1} \exp(-(i-1-j)w + k_j) \odot v_j + \exp(u + k_i) \odot v_i}{\sum_{j=1}^{i-1} \exp(-(i-1-j)w + k_j) + \exp(u + k_i)}$$ (2)

[p. 5] RWKV-4 also adds token-shift and gating to both attention and feed-forward sub-blocks of transformer, and small embedding initialization to quickly arrive at well-distributed token embeddings. Combining all of these architectural changes led RWKV-4 to become the first RNN to rival the performance of Transformers, while maintaining fast parallelizable training and O(1) time complexity per token.

## Recent Developments in RNNs

[p. 5] There has been a recent revival of RNNs in NLP research (Tiezzi et al., 2024). HGRN(Qin et al., 2023) is a recent time-parallelizable data-dependent RNN that employs input and forget gates. TransNormer(Qin et al., 2022) applies RMSNorm to linear attention to bound its output. Other new time-parallelizable data-dependent RNNs have also been invented concurrently with our work including GLA (Yang et al., 2023) and Griffin (De et al., 2024).

## State Space Models (SSMs)

[p. 5] State Space Models (SSMs) employ a hidden state of basis function weights to model an approximation of the input function (Gu et al., 2021), updating that hidden state via a differential equation. Earlier SSMs (Gu et al., 2022) were historically computed using long convolutions in O(N log N) time per sequence, but could also be formulated as a recurrent network. Recently, it has been shown that SSMs can be parallelized across the time dimension via techniques including associative scan (Smith et al., 2023). A new class of SSMs including concurrently with our work (Katsch, 2023; Gu & Dao, 2023) that feature data-dependent A and B terms, which function similarly to the data-dependent dynamic recurrence used in Finch.
