# Tokenizer & Model [p. 3-5]

[p. 3] This section introduces the tokenizer and model design of Qwen2, detailing the model architecture and configurations for different model sizes.

## Tokenizer [p. 3]

[p. 3] Following Qwen (Bai et al., 2023a), Qwen2 employs the identical tokenizer based on **byte-level byte-pair encoding**. This tokenizer exhibits high encoding efficiency, as evidenced by its better compression rate relative to alternatives, facilitating the multilingual capabilities of Qwen2.

Models of all sizes employ a common vocabulary consisting of **151,643 regular tokens and 3 control tokens**. Due to considerations in distributed training, the effective size for the embeddings is larger.

## Model Architecture [p. 4]

[p. 4] The Qwen2 series fundamentally constitutes large language models based on the Transformer architecture, featuring self-attention with causal masks (Vaswani et al., 2017). The series encompasses dense language models of 4 scales and a Mixture-of-Experts (MoE) model.

### Qwen2 Dense Model [p. 4]

[p. 4] The architecture of the Qwen2 dense models comprises multiple Transformer layers, each equipped with causal attention mechanisms and feed-forward neural networks (FFNs). Key differences from Qwen:

**Grouped Query Attention (GQA):** Qwen2 adopts Grouped Query Attention (GQA, Ainslie et al., 2023) instead of conventional multi-head attention (MHA). GQA optimizes KV cache usage during inference, significantly enhancing throughput. Detailed KV head configurations for various model sizes are reported in Section 2.2.3.

**Dual Chunk Attention with YARN:** To expand the context window, Qwen2 implements Dual Chunk Attention (DCA, An et al., 2024), which segments long sequences into chunks of manageable lengths. If the input can be handled in a chunk, DCA produces the same result as the original attention. Otherwise, DCA facilitates effective capture of relative positional information between tokens within and across chunks, thereby improving long context performance. YARN (Peng et al., 2023) is also employed to rescale the attention weights for better length extrapolation.

Additional architectural choices following Qwen:
- **SwiGLU** (Dauphin et al., 2017) for activation
- **Rotary Positional Embeddings (RoPE, Su et al., 2024)** for positional embedding
- **QKV bias** (Su, 2023) for attention
- **RMSNorm** (Jiang et al., 2023b) and **pre-normalization** for training stability

### Qwen2 Mixture-of-experts Model [p. 4-5]

[p. 4] The architecture of Qwen2 MoE models closely mirrors that of Qwen1.5-MoE-A2.7B (Qwen Team, 2024c). As a substitute for the original FFN, the MoE FFN consists of *n* individual FFNs, each serving as an expert. Each token is directed to a specific expert *E_i* for computation based on probabilities assigned by a gated network *G*:

$$\mathbf{p} = \text{softmax}(G(\mathbf{x})),  \quad (1)$$

$$\mathbf{y} = \sum_{i \in \text{top}_k(\mathbf{p})} \mathbf{p}_i E_i(\mathbf{x}).  \quad (2)$$

Equation (1) computes the routing probabilities over all experts via softmax of the gating network output. Equation (2) computes the final output as a weighted sum of the top-k selected experts' outputs.

**Expert Granularity** [p. 4]: The key structural difference between MoE models and dense models is that MoE layers incorporate multiple FFNs, each serving as an individual expert. One straightforward strategy to transition from a dense architecture to an MoE architecture is to set the parameters of each expert equal to those of a single FFN from the original dense model (e.g., transitioning from Mistral-7B (Jiang et al., 2023a) to Mixtral 8x7B (Jiang et al., 2024), involving activating two of the eight experts at a time). Differently, Qwen2 employs **fine-grained experts** (Dai et al., 2024), creating smaller-scale experts while activating a greater number of experts simultaneously. Given an equal total number of expert parameters and activated parameters, fine-grained experts offer a richer set of expert combinations, facilitating more diverse and dynamic expert utilization, thereby enhancing overall performance and adaptability.

**Expert Routing** [p. 4]: The design of expert routing mechanisms is crucial for MoE model performance. There has been a notable trend towards integrating both **shared and routing-specific experts** within MoE layers (Rajbhandari et al., 2022; Dai et al., 2024). Qwen2 adopts this approach, facilitating shared experts across various tasks while reserving others for selective use in specific routing scenarios. The introduction of shared and specialized experts offers a more adaptable and efficient method for developing MoE routing mechanisms.

**Expert Initialization** [p. 5]: Experts are initialized in a way similar to upcycling (Komatsuzaki et al., 2023), leveraging the weights of a dense model. The approach emphasizes diversification among fine-grained experts to enhance representational breadth. Given the designated expert intermediate size *h_E*, the number of experts *n*, and the original FFN intermediate size *h_FFN*, the FFN is replicated ceil(*n* x *h_E* / *h_FFN*) times. This replication ensures compatibility with the specified number of experts while accommodating any arbitrary expert intermediate size. To promote diversity within each FFN copy, parameters are shuffled along the intermediate dimension, guaranteeing unique characteristics for each fine-grained expert across different FFN copies. These experts are then extracted from the FFN copies, and remaining dimensions are discarded. For each fine-grained expert, **50% of its parameters are randomly reinitialized**, introducing additional stochasticity into expert initialization to enhance exploration during training.

### Model Configuration [p. 5]

[p. 5] The Qwen2 series consists of models of 5 sizes: Qwen2-0.5B, Qwen2-1.5B, Qwen2-7B, Qwen2-57B-A14B, and Qwen2-72B. Qwen2-57B-A14B is upscaled from Qwen2-7B. Notably, Qwen2 models demonstrate a substantially lower Key-Value (KV) size per token relative to Qwen1.5 models, translating into a reduced memory footprint, particularly advantageous in long-context inference tasks.

**Table 1** (p. 5): Architecture of Qwen2 dense and MoE models. For MoE models, 57B-A14B denotes that the model has 57B parameters in total and for each token 14B parameters are active, the Intermediate size denotes that of each expert, and # Activated Experts excludes the shared experts.

| Configuration | 0.5B | 1.5B | 7B | 72B | 57B-A14B |
|---|---|---|---|---|---|
| Hidden Size | 896 | 1,536 | 3,584 | 8,192 | 3,584 |
| # Layers | 24 | 28 | 28 | 80 | 28 |
| # Query Heads | 14 | 12 | 28 | 64 | 28 |
| # KV Heads | 2 | 2 | 4 | 8 | 4 |
| Head Size | 64 | 128 | 128 | 128 | 128 |
| Intermediate Size | 4,864 | 8,960 | 18,944 | 29,568 | 2,560 |
| # Routed Experts | - | - | - | - | 64 |
| # Activated Experts | - | - | - | - | 8 |
| # Shared Experts | - | - | - | - | 8 |
| Embedding Tying | True | True | False | False | False |
| Vocabulary Size | 151,646 | 151,646 | 151,646 | 151,646 | 151,646 |
| # Trained Tokens | 12T | 7T | 7T | 7T | 4.5T |
