# Introduction [p. 1–3]

## Position Bias Problem

Language models (LMs) (Brown et al., 2020; Chowdhery et al., 2022; Touvron et al., 2023; Achiam et al., 2023) demonstrate impressive performance in general language tasks such as dialogue (Thoppilan et al., 2022), reasoning (Chowdhery et al., 2022), and schema induction (Li et al., 2023) [p. 1]. However, they tend to favor content at certain positions (Zheng et al., 2024b,a; Wang et al., 2023; Dominguez Olmedo et al., 2023; Zhu et al., 2023; Chen et al., 2024b; Liu et al., 2024), which harms complex reasoning (Chen et al., 2024b), long-context understanding (Liu et al., 2024) and model-based evaluation (Zheng et al., 2024b) [p. 1].

For example, in LM-as-a-judge settings, models tend to favor one of two candidate responses when it is presented at different positions, which hurts their reliability when being used as evaluators [p. 1]. Figure 1 (upper) shows a vision-document QA recognition example where the target content is presented at the bottom of the image, with additional examples in Appendix A [p. 1].

Different from *ad hoc* solutions from previous works (Ratner et al., 2023; Cai et al., 2023; Hao et al., 2022; Junqing et al., 2023; Zhu et al., 2023), the authors seek to understand the causes of position bias and propose to eliminate (not just mitigate) the position bias without training and searching [p. 1].

## Methodology Overview

The paper starts by analyzing the key components of state-of-the-art LMs – Causal Attention and Position Embedding. They are the key to the success of Transformers (Vaswani et al., 2017), and are also the only two operations in Transformers (Vaswani et al., 2017) that will bring undesirable position bias [p. 1]. This is because other operations do not change representations when position changes (Section 3.2) [p. 1].

Moreover, the authors find an interesting phenomenon through simple experiments: **the most popular Rotary Position Embedding (Su et al., 2024) is shown to have recency bias (Su et al., 2024; Peysakhovich & Lerer, 2023) due to its long-form attention weight decay w.r.t. the increase of relative positions, and the causal attention prefers bidirectional region propagation, enabling models to pay more attention to distant content** [p. 2]. Figure 1 (lower left) shows this retrieval-augmented QA (Liu et al., 2024) experiment. The bar chart data shows that the orange and yellow area reflects the position bias of causal attention and RoPE. Since the yellow area is mostly wider at the beginning and the orange area generally becomes wider in the middle of Figure 1 (except for the data point), this shows that the causal attention generally tends to favor distant content, while RoPE generally tends to favor nearby content [p. 2].²

## PINE Approach

Since attention and position embedding are the causes of position bias, the authors propose PINE that can eliminate position bias by manipulating causal attention and RoPE to attend to different content equally [p. 2]. They take the retrieval-augmented QA (Liu et al., 2024) as an example, a task requiring LMs to answer questions based on retrieved documents. The orders of retrieved documents should not affect the final results [p. 2].

To achieve this, PINE makes document attention bidirectional so that the attention mask will equally attend to all documents [p. 2]. Next, they compute importance scores between documents and use them to re-assign document positions so that positions in the original inputs are discarded. They prove the resulting approach is **Position-iNvariant inferencE (PINE)** w.r.t. documents in a **training-free/zero-shot** manner [p. 2].

## Empirical Validation

To justify the effectiveness of PINE, the authors select four tasks [p. 2]:

1. **LM-as-a-judge** (Zheng et al., 2024b), which prompts LMs to choose the more helpful one from two given responses to a question
2. **Retrieval-augmented question-answering** (Liu et al., 2024)
3. **Molecule generation** based on provided properties
4. **Math reasoning**

In different tasks, "documents" have different meanings: responses in LM-as-a-judge, properties in molecule generation, and conditions in math reasoning [p. 2]. Notably, the authors find their method especially useful when evaluating reasoning pairs: PINE with Llama-3-70B-Instruct performs even better than GPT-4-0125-preview and GPT-4o-2024-08-06 on the RewardBench (Lambert et al., 2024a) reasoning set [p. 2].

## Summary

In summary [p. 2]:

- The authors first revisit the causes of position bias in transformers: causal attention and position encoding (Section 3.2), and then propose a training-free approach dubbed PINE that can eliminate (with proof) the position bias given documents presumed to be position-invariant (Section 3.3) [p. 3].

- Four popular tasks across the general domain to expert domains (chemistry and math) show PINE can bring performance gains consistently across different models and sizes [p. 3].

---

**Figure 1** (p. 2): "Motivating examples showing how position bias affects model outputs."

Description: Multi-part figure showing position bias manifestations
- **Upper panel:** LM-as-a-judge example where LMs are asked to select a more helpful one from two given responses. Shows that LMs are prone to prefer the response positioned at the beginning of the input prompt.
- **Lower Left:** Retrieval-augmented QA example with Llama-3-8B-Instruct presented with 20 documents to answer a question, with only one document (the gold-standard document) containing the correct answer. The blue curve represents inference without inter-document attention (RoPE position encodings are kept, a concrete implementation is shown in the middle of Figure 1). The bar chart shows position bias: the yellow and orange area reflects the position brought by causal attention and RoPE. Causal attention generally favors distant content, but RoPE prefers nearby content.
- **Right panel:** Prompt VLMs (Fuyu-8B (Bavishi et al., 2023)) to compute the loss on the ground truth token. Shows that models have lower losses (black color) when images are presented at the bottom.

Notable patterns: The figure demonstrates a consistent pattern that models show systematic position preferences across different modalities and tasks.

Supports claim: Demonstrates the prevalence and impact of position bias in modern LMs across multiple task types.

² More supporting experiments to this hypothesis in Section 4.3
