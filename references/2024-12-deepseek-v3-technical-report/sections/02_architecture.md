# 2. Architecture [p. 6–10]

The authors first introduce the basic architecture of DeepSeek-V3, featured by Multi-head Latent Attention (MLA) (DeepSeek-AI, 2024c) for efficient inference and DeepSeekMoE (Dai et al., 2024) for economical training. Then, the authors present a Multi-Token Prediction (MTP) training objective, which the authors have observed to enhance the overall performance on evaluation benchmarks. For other minor details not explicitly mentioned, DeepSeek-V3 adheres to the settings of DeepSeek-V2 (DeepSeek-AI, 2024c). [p. 6]

## 2.1. Basic Architecture [p. 6]

The basic architecture of DeepSeek-V3 is still within the Transformer (Vaswani et al., 2017) framework. For efficient inference and economical training, DeepSeek-V3 also adopts MLA and DeepSeekMoE, which have been thoroughly validated by DeepSeek-V2. Compared with DeepSeek-V2, an exception is that the authors additionally introduce an auxiliary-loss-free load balancing strategy (Wang et al., 2024a) for DeepSeekMoE to mitigate the performance degradation induced by the effort to ensure load balance. Figure 2 illustrates the basic architecture of DeepSeek-V3, and the authors will briefly review the details of MLA and DeepSeekMoE in this section. [p. 6]

**Figure 2** (p. 7): "Illustration of the basic architecture of DeepSeek-V3. Following DeepSeek-V2, we adopt MLA and DeepSeekMoE for efficient inference and economical training."

Description: Architecture diagram showing three main components:
- Left panel: Transformer Block structure with Feed-Forward Network, RMSNorm, Attention, and RMSNorm layers
- Top right panel: DeepSeekMoE structure showing Input Hidden, Router with Top-Kr selection, routed experts (1 to Nr) and shared experts, and Output Hidden
- Bottom right panel: Multi-Head Latent Attention (MLA) showing the computation flow from Input Hidden through concatenation, RoPE operations, and attention mechanism to Output Hidden, with notation for cached elements during inference
- Key elements: The diagram shows how compressed latent vectors are computed, concatenated, and processed through attention with RoPE (Rotary Position Embedding)
- Supports claim: Illustrates the efficient inference design via MLA (reduced KV cache) and economical training via DeepSeekMoE (mixture of experts)

### 2.1.1. Multi-Head Latent Attention [p. 7]

For attention, DeepSeek-V3 adopts the MLA architecture. Let d denote the embedding dimension, nh denote the number of attention heads, dh denote the dimension per head, and ht ∈ Rd denote the attention input for the t-th token at a given attention layer. The core of MLA is the low-rank joint compression for attention keys and values to reduce Key-Value (KV) cache during inference:

$$c_t^{KV} = W^{DKV} h_t,$$
(1)

$$[k_{t,1}^C; k_{t,2}^C; ...; k_{t,n_h}^C] = k_t^C = W^{UK} c_t^{KV},$$
(2)

$$[k_t^R] = \text{RoPE}(W^{KR} h_t),$$
(3)

$$k_{t,i} = [k_{t,i}^C; k_t^R],$$
(4)

$$[v_{t,1}^C; v_{t,2}^C; ...; v_{t,n_h}^C] = v_t^C = W^{UV} c_t^{KV},$$
(5)

where $c_t^{KV} \in \mathbb{R}^{d_c}$ is the compressed latent vector for keys and values; $d_c (\ll d_h n_h)$ indicates the KV compression dimension; $W^{DKV} \in \mathbb{R}^{d_c \times d}$ denotes the down-projection matrix; $W^{UK}, W^{UV} \in \mathbb{R}^{d_h n_h \times d_c}$ are the up-projection matrices for keys and values, respectively; $W^{KR} \in \mathbb{R}^{d_h^R \times d}$ is the matrix used to produce the decoupled keys that carry Rotational Position Embedding (RoPE) (Su et al., 2024); RoPE(·) denotes the operation that applies RoPE matrices; and [·; ·] denotes concatenation. Note that for MLA, only the blue-boxed vectors (i.e., $c_t^{KV}$ and $k_t^R$) need to be cached during generation, which results in significantly reduced KV cache while maintaining performance comparable to standard Multi-Head Attention (MHA) (Vaswani et al., 2017). [p. 7-8]

For the attention queries, the authors also perform a low-rank compression, which can reduce the activation memory during training:

$$c_t^Q = W^{DQ} h_t,$$
(6)

$$[q_{t,1}^C; q_{t,2}^C; ...; q_{t,n_h}^C] = q_t^C = W^{UQ} c_t^Q,$$
(7)

$$[q_{t,1}^R; q_{t,2}^R; ...; q_{t,n_h}^R] = q_t^R = \text{RoPE}(W^{QR} c_t^Q),$$
(8)

$$q_{t,i} = [q_{t,i}^C; q_{t,i}^R],$$
(9)

where $c_t^Q \in \mathbb{R}^{d_c^q}$ is the compressed latent vector for queries; $d_c^q (\ll d_h n_h)$ denotes the query compression dimension; $W^{DQ} \in \mathbb{R}^{d_c^q \times d}, W^{UQ} \in \mathbb{R}^{d_h n_h \times d_c^q}$ are the down-projection and up-projection matrices for queries, respectively; and $W^{QR} \in \mathbb{R}^{d_h^R n_h \times d_c^q}$ is the matrix to produce the decoupled queries that carry RoPE. [p. 8]

Ultimately, the attention queries ($q_{i,t}$), keys ($k_{i,t}$), and values ($v_{t,i}^C$) are combined to yield the final attention output $u_t$:

$$o_{t,i} = \sum_{j=1}^t \text{Softmax}_j \left( \frac{q_{t,i}^T k_{j,i}}{\sqrt{d_h + d_h^R}} \right) v_{j,i}^C,$$
(10)

$$u_t = W^O [o_{t,1}; o_{t,2}; ...; o_{t,n_h}],$$
(11)

where $W^O \in \mathbb{R}^{d \times d_h n_h}$ denotes the output projection matrix. [p. 8]

### 2.1.2. DeepSeekMoE with Auxiliary-Loss-Free Load Balancing [p. 8]

**Basic Architecture of DeepSeekMoE.** For Feed-Forward Networks (FFNs), DeepSeek-V3 employs the DeepSeekMoE architecture (Dai et al., 2024). Compared with traditional MoE architectures like GShard (Lepikhin et al., 2021), DeepSeekMoE uses finer-grained experts and isolates some experts as shared ones. Let $u_t$ denote the FFN input of the t-th token, the authors compute the FFN output $h_t'$ as follows:

$$h_t' = u_t + \sum_{i=1}^{N_s} \text{FFN}_i^{(s)}(u_t) + \sum_{i=1}^{N_r} g_{i,t} \text{FFN}_i^{(r)}(u_t),$$
(12)

$$g_{i,t} = \frac{s_{i,t}'}{\sum_{j=1}^{N_r} s_{j,t}'},$$
(13)

$$s_{i,t}' = \begin{cases} s_{i,t}, & s_{i,t} \in \text{Topk}(\{s_{j,t}|1 \leq j \leq N_r\}, K_r), \\ 0, & \text{otherwise}, \end{cases}$$
(14)

$$s_{i,t} = \text{Sigmoid}(u_t^T e_i),$$
(15)

where $N_s$ and $N_r$ denote the numbers of shared experts and routed experts, respectively; $\text{FFN}_i^{(s)}(\cdot)$ and $\text{FFN}_i^{(r)}(\cdot)$ denote the i-th shared expert and the i-th routed expert, respectively; $K_r$ denotes the number of activated routed experts; $g_{i,t}$ is the gating value for the i-th expert; $s_{i,t}$ is the token-to-expert affinity; $e_i$ is the centroid vector of the i-th routed expert; and Topk(·, K) denotes the set comprising K highest scores among the affinity scores calculated for the t-th token and all routed experts. Slightly different from DeepSeek-V2, DeepSeek-V3 uses the sigmoid function to compute the affinity scores, and applies a normalization among all selected affinity scores to produce the gating values. [p. 8-9]

**Auxiliary-Loss-Free Load Balancing.** For MoE models, an unbalanced expert load will lead to routing collapse (Shazeer et al., 2017) and diminish the computational efficiency in scenarios with expert parallelism. Conventional solutions usually rely on the auxiliary loss (Fedus et al., 2021; Lepikhin et al., 2021) to avoid unbalanced load. However, too large an auxiliary loss will impair the model performance (Wang et al., 2024a). To achieve a better tradeoff between load balance and model performance, the authors pioneer an auxiliary-loss-free load balancing strategy (Wang et al., 2024a) to ensure load balance. To be specific, the authors introduce a bias term $b_i$ for each expert and add it to the corresponding affinity scores $s_{i,t}$ to determine the top-K routing:

$$s_{i,t}' = \begin{cases} s_{i,t}, & s_{i,t} + b_i \in \text{Topk}(\{s_{j,t} + b_j | 1 \leq j \leq N_r\}, K_r), \\ 0, & \text{otherwise}. \end{cases}$$
(16)

Note that the bias term is only used for routing. The gating value, which will be multiplied with the FFN output, is still derived from the original affinity score $s_{i,t}$. During training, the authors keep monitoring the expert load on the whole batch of each training step. At the end of each step, the authors will decrease the bias term by γ if its corresponding expert is overloaded, and increase it by γ if its corresponding expert is underloaded, where γ is a hyper-parameter called bias update speed. Through the dynamic adjustment, DeepSeek-V3 keeps balanced expert load during training, and achieves better performance than models that encourage load balance through pure auxiliary losses. [p. 9]

**Complementary Sequence-Wise Auxiliary Loss.** Although DeepSeek-V3 mainly relies on the auxiliary-loss-free strategy for load balance, to prevent extreme imbalance within any single sequence, the authors also employ a complementary sequence-wise balance loss:

$$\mathcal{L}_{\text{Bal}} = \alpha \sum_{i=1}^{N_r} f_i P_i,$$
(17)

$$f_i = \frac{N_r}{K_r T} \sum_{t=1}^T \mathbb{1}\left(s_{i,t} \in \text{Topk}(\{s_{j,t}|1 \leq j \leq N_r\}, K_r)\right),$$
(18)

$$s_{i,t}' = \frac{s_{i,t}}{\sum_{j=1}^{N_r} s_{j,t}},$$
(19)

$$P_i = \frac{1}{T} \sum_{t=1}^T s_{i,t}',$$
(20)

where the balance factor α is a hyper-parameter, which will be assigned an extremely small value for DeepSeek-V3; 1(·) denotes the indicator function; and T denotes the number of tokens in a sequence. The sequence-wise balance loss encourages the expert load on each sequence to be balanced. [p. 9]

**Node-Limited Routing.** Like the device-limited routing used by DeepSeek-V2, DeepSeek-V3 also uses a restricted routing mechanism to limit communication costs during training. In short, the authors ensure that each token will be sent to at most M nodes, which are selected according to the sum of the highest $\frac{K_r}{M}$ affinity scores of the experts distributed on each node. Under this constraint, the MoE training framework can nearly achieve full computation-communication overlap. [p. 10]

**No Token-Dropping.** Due to the effective load balancing strategy, DeepSeek-V3 keeps a good load balance during its full training. Therefore, DeepSeek-V3 does not drop any tokens during training. In addition, the authors also implement specific deployment strategies to ensure inference load balance, so DeepSeek-V3 also does not drop tokens during inference. [p. 10]

## 2.2. Multi-Token Prediction [p. 10]

Inspired by Gloeckle et al. (2024), the authors investigate and set a Multi-Token Prediction (MTP) objective for DeepSeek-V3, which extends the prediction scope to multiple future tokens at each position. On the one hand, such an objective densifies training signals and may improve data efficiency. On the other hand, MTP may enable the model to pre-plan its representations for better prediction of future tokens. Figure 3 illustrates the implementation of MTP. Different from Gloeckle et al. (2024), which parallelly predicts D additional tokens using independent output heads, the authors sequentially predict additional tokens and keep the complete causal chain at each prediction depth. The authors introduce the details of the MTP implementation in this section. [p. 10]

**Figure 3** (p. 10): "Illustration of our Multi-Token Prediction (MTP) implementation. We keep the complete causal chain for the prediction of each token at each depth."

Description: Architecture diagram showing three parallel modules:
- Left: Main Model (Next-Token Prediction) with standard Transformer Block structure
- Middle: MTP Module 1 (Next-Token Prediction)
- Right: MTP Module 2 (Next-Token Prediction)
- Key elements: Each module has an Output Head, Transformer Block, Linear Projection (with concatenation), RMSNorm layers, and Embedding Layer
- All modules process Input Tokens (t1, t2, t3, t4, t5, t6) and Target Tokens
- Cross-Entropy Loss is computed at each level contributing to $\mathcal{L}_{\text{Main}}$, $\mathcal{L}_{\text{MTP}}^1$, and $\mathcal{L}_{\text{MTP}}^2$
- Supports claim: Shows how MTP maintains the complete causal chain at each prediction depth, unlike alternative approaches that use independent output heads

**MTP Modules.** To be specific, the MTP implementation uses D sequential modules to predict D additional tokens. The k-th MTP module consists of a shared embedding layer Emb(·), a shared output head OutHead(·), a Transformer block $\text{TRM}_k(\cdot)$, and a projection matrix $M_k \in \mathbb{R}^{d \times 2d}$. For the i-th input token $t_i$, at the k-th prediction depth, the authors first combine the representation of the i-th token at the $(k-1)$-th depth $h_i^{k-1} \in \mathbb{R}^d$ and the embedding of the $(i+k)$-th token $Emb(t_{i+k}) \in \mathbb{R}^d$ [p. 10-11]

with the linear projection:

$$h_i'^k = M_k[\text{RMSNorm}(h_i^{k-1}); \text{RMSNorm}(\text{Emb}(t_{i+k}))],$$
(21)

where [·; ·] denotes concatenation. Especially, when k = 1, $h_i^{k-1}$ refers to the representation given by the main model. Note that for each MTP module, its embedding layer is shared with the main model. The combined $h_i'^k$ serves as the input of the Transformer block at the k-th depth to produce the output representation at the current depth $h_i^k$:

$$h_{1:T-k}^k = \text{TRM}_k(h_{1:T-k}'^k),$$
(22)

where T represents the input sequence length and [·:·] denotes the slicing operation (inclusive of both the left and right boundaries). Finally, taking $h_i^k$ as the input, the shared output head will compute the probability distribution for the k-th additional prediction token $P_{i+1+k}^k \in \mathbb{R}^V$, where V is the vocabulary size:

$$P_{i+k+1}^k = \text{OutHead}(h_i^k).$$
(23)

The output head OutHead(·) linearly maps the representation to logits and subsequently applies the Softmax(·) function to compute the prediction probabilities of the k-th additional token. Also, for each MTP module, its output head is shared with the main model. The principle of maintaining the causal chain of predictions is similar to that of EAGLE (Li et al., 2024b), but its primary objective is speculative decoding (Leviathan et al., 2023; Xia et al., 2023), whereas the authors utilize MTP to improve training. [p. 11]

**MTP Training Objective.** For each prediction depth, the authors compute a cross-entropy loss $\mathcal{L}_{\text{MTP}}^k$:

$$\mathcal{L}_{\text{MTP}}^k = \text{CrossEntropy}(P_{2+k:T+1}^k, t_{2+k:T+1}) = -\frac{1}{T} \sum_{i=2+k}^{T+1} \log P_i^k[t_i],$$
(24)

where T denotes the input sequence length, $t_i$ denotes the ground-truth token at the i-th position, and $P_i^k[t_i]$ denotes the corresponding prediction probability of $t_i$, given by the k-th MTP module. Finally, the authors compute the average of the MTP losses across all depths and multiply it by a weighting factor λ to obtain the overall MTP loss $\mathcal{L}_{\text{MTP}}$, which serves as an additional training objective for DeepSeek-V3:

$$\mathcal{L}_{\text{MTP}} = \frac{\lambda}{D} \sum_{k=1}^D \mathcal{L}_{\text{MTP}}^k.$$
(25)

**MTP in Inference.** The MTP strategy mainly aims to improve the performance of the main model, so during inference, the authors can directly discard the MTP modules and the main model can function independently and normally. Additionally, the authors can also repurpose these MTP modules for speculative decoding to further improve the generation latency. [p. 11]
