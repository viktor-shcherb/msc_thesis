# 2. Model Architecture & Pretraining Recipe [p. 9]

[p. 9]

This section details the architecture and pretraining recipe for the Apertus suite of pretrained models. Key choices include the use of a new xIELU activation function, the AdEMAMix optimizer, QK-Norm, Pre-Norm, and Goldfish loss for memorization mitigation. The authors first provide an overview of the architecture design (Section 2.1), tokenizer (Section 2.2) and the algorithms for the main pretraining stage (Section 2.3). They then describe the ablation studies behind the design choices in Section 2.4, where experiments with their architecture and optimization setup improve efficiency by 30-40% both at 1B and 3B scale and in a short replication of OLMo2 (1B and 7B). This is followed by the details of the long-context extension in Section 2.5. Finally, they provide a retrospective of the final training, designs that did not make it into this version, and future directions in Section 2.6.

**Codebase.** The pretraining codebase^4 is built on NVIDIA's Megatron-LM (Shoeybi et al., 2019). The authors extend the codebase with multiple functionalities (e.g., dataloader format, logging during training) and necessary modifications for their architecture (activation function, loss, optimizer). They also make the pretrain and long context training scripts public.^5

## 2.1 Model Architecture

[p. 9]

**Overview.** The Apertus architecture is a dense decoder-only Transformer (Vaswani et al., 2017; Radford et al., 2018). The basic architecture consists of a deep stack of Transformer blocks. Each block contains a multi-head self-attention mechanism, followed by a feedforward network (MLP), with residual connections and normalization applied around each sublayer. This architecture is adapted across two scales:

- Apertus 8B, with 32 layers and 32 parallel attention heads.
- Apertus 70B, with 80 layers and 64 parallel attention heads.

The main characteristics and hyperparameters of the models are listed in Table 1. Besides established modifications to the original Transformer, such as grouped-query attention (GQA), RoPE, and RMSNorm, the authors improve the architecture efficiency through the use of QK-Norms (Henry et al., 2020; Dehghani et al., 2023) and the activation function xIELU (Huang & Schlag, 2025).

### Table 1

**Table 1** (p. 9): **Apertus Model Architecture Overview.** We adapt our custom Apertus architecture with the xIELU activation function (Huang & Schlag, 2025) across two scales, 8B and 70B. Both models support long contexts up to 65k tokens with grouped-query attention (GQA) for inference efficiency.

| Model | Layers | Dim | MLP Dim | Heads (Q / KV) | Activation | Context Length |
|---|---|---|---|---|---|---|
| Apertus 8B | 32 | 4096 | 21504 | 32/8 | xIELU | 65536 |
| Apertus 70B | 80 | 8192 | 43008 | 64/8 | xIELU | 65536 |

### Architectural modifications

[p. 9-10]

**No biases.** All bias terms are removed from the architecture (Chowdhery et al., 2022).

**Pre-Norm and RMSNorm.** Pre-normalization is used before the residual in the transformer block, which has better training stability than post-normalization (Xiong et al., 2020). LayerNorm (Ba et al., 2016) is replaced with RMSNorm (Zhang & Sennrich, 2019), which has equivalent performance while improving efficiency.

**Rotary Positional Embeddings.** RoPE embeddings (Su et al., 2021) are used with a base Theta = 500,000 during pretraining, which is extended in the long-context phase (Section 2.5). NTK-aware RoPE scaling (Peng et al., 2023) is also employed, following the LLaMA-3 implementation (Grattafiori et al., 2024) in the Transformers library (Wolf et al., 2020).

**Group-Query Attention.** The grouped-query attention (GQA) mechanism (Ainslie et al., 2023) is adopted for inference efficiency, using fewer key-value pairs than query heads without compromising performance.

**Untied Embeddings and Output Weights.** Input embedding weights are not tied to output embedding weights. This improves performance at the cost of using additional memory.

**QK-Norm.** QK-Norm (Henry et al., 2020; Dehghani et al., 2023) is incorporated, which normalizes the queries and keys in the attention layers. QK-Norm improves training stability by preventing excessively large attention logits.

[p. 10]

**xIELU Activation Function.** In the MLP sublayers, the xIELU activation function (Huang & Schlag, 2025) is adopted, defined as

$$\text{xIELU}(x) := \begin{cases} \alpha_p x^2 + 0.5x & \text{if } x > 0, \\ \alpha_n(e^x - 1) - \alpha_n x + 0.5x & \text{if } x \leq 0. \end{cases}$$

where alpha_p and alpha_n are trainable scalars per layer. xIELU is an extension of Squared ReLU (So et al., 2021) to handle negative inputs.

**BoD and EoD tokens.** Every document in the corpus is prepended with a special BoD `<s>` token, and similarly an EoD token `</s>` is appended. Having fixed tokens always present at the beginning of the context (such as `<s>`) have been shown to improve model quality and training stability, serve as attention sinks, and allow to store global knowledge (Raffel et al., 2020; Dong et al., 2024; Xiao et al., 2024; OpenAI et al., 2025). During training, the loss on EoD tokens is masked out and not backpropagated.

**Prevent Cross Document Attention.** Following previous practice, tokens are prevented from attending to tokens in different documents present in the same context window, through the use of attention masks (Raffel et al., 2020; Grattafiori et al., 2024; Bakouch et al., 2025).

**Context length.** Both Apertus 8B and Apertus 70B were trained with a context of 4,096 tokens (about 3,000 words) during pretraining. A long-context extension is then performed to support sequences of up to 65,536 tokens, as detailed in Section 2.5.

**Footnotes:**
- ^4: https://github.com/swiss-ai/Megatron-LM
- ^5: https://github.com/swiss-ai/pretrain-code
