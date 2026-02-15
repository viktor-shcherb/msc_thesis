# Introduction [p. 1]

Xiao et al. (2023b) showed that Large Language models (LLMs) allocate significant attention to the initial tokens, irrespective of their semantic relevance. This phenomenon is termed **attention sink** and has widespread applications, including streaming/long context generation (Xiao et al., 2023b; Han et al., 2024; Yang et al., 2024), KV cache optimization (Ge et al., 2023; Wan et al., 2024; Wu & Tu, 2024), efficient inference (Zhang et al., 2024b; Chen et al., 2024), model quantization (Liu et al., 2024b; Huang et al., 2024), and others [p. 1].

A seminal of works attempted to understand attention sink. Among them, Cancedda (2024) clarified that attention sink primarily appears only on the first token. They attributed the phenomenon to the large norm of hidden states of the first token. This is referred to as *massive activations* (very few activations exhibit extremely large values compared to others) in Sun et al. (2024). Besides, Sun et al. (2024); Yu et al. (2024) observed that attention sink may also appear in several word tokens carrying limited semantic information and having no fixed position. Despite the above research efforts, a deep understanding of attention sink is still absent. Therefore, we conduct a comprehensive study to investigate when attention sink emerges. Full discussions on related work are deferred to Appendix A [p. 1].

Based on open-sourced auto-regressive LMs, the authors show that the first token acts as biases: the angles between the first key and queries of other tokens are typically small, leading to attention sink. Additionally, attention sink is observed to emerge during the LM pre-training before continual instruction tuning (Ouyang et al., 2022). This motivates the focus on the LM pre-training, whose objective can be formulated as [p. 1-2]:

$$\min_\theta \mathbb{E}_{\mathbf{X} \sim p_{\text{data}}} [\mathcal{L}(p_\theta(\mathbf{X}))].$$
(1)

The paper investigates how optimization (Section 4), data distribution (Section 5), loss function (Section 6), and model architecture (Section 7) influence the emergence of attention sink. The following conclusions are reached [p. 2]:

- Attention sink emerges after LMs are trained effectively on sufficient training data. It appears less obvious in LMs trained with small learning rates. While weight decay encourages the emergence of attention sink.
- The sink position is highly related to the loss function and data distribution and can be shifted to other positions rather than the first token.
- Attention sink acts more like key biases, storing extra attention and meanwhile not contributing to the value computation. This phenomenon (at least partially) stems from tokens' inner dependence on attention scores due to the softmax normalization. After relaxing such dependence by replacing softmax attention with other attention operations, e.g., sigmoid attention without normalization, attention sinks do not emerge in LMs up to 1B parameters.

**Footnotes:**
- Work done during Xiangming Gu's internship at Sea AI Lab.
- Correspondence to Tianyu Pang and Ye Wang.
