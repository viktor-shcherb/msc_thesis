# Introduction [p. 1–2]

## Background and Motivation

Transformer (Vaswani et al., 2017) has garnered significant research interest in recent years, with the decoder-only Transformer emerging as the de facto standard for large language models (LLMs) [p. 1]. At the heart of Transformer is the attention mechanism, which employs the softmax function to weigh the importance of different tokens in a sequence [p. 1]. However, recent studies (Kamradt, 2023; Liu et al., 2024b) show that LLMs face challenges in accurately retrieving key information from context [p. 1].

## Problem Statement: Attention Noise

As illustrated on the left side of Figure 1, the visualization shows attention scores assigned to different parts of the context by a Transformer [p. 1]. The task is to retrieve an answer embedded in the middle of a pile of documents [p. 1]. The visualization reveals that Transformer tends to allocate only a small proportion of attention scores to the correct answer, while disproportionately focusing on irrelevant context [p. 1].

The experiments in Section 3 further substantiate that Transformers struggle with such capabilities [p. 1]. The issue arises from non-relevant context scores being irrelevant but still draws the model's attention to irrelevant context, which ultimately drowns out the correct answer [p. 1]. The authors term these extraneous scores as **attention noise** [p. 1].

**Figure 1** (p. 1): "Transformer often over-attends to irrelevant context (i.e., attention noise). DIFF Transformer amplifies attention to answer spans and cancels noise, enhancing the capability of context modeling."

Description: Three-panel bar chart visualization comparing normalized attention scores
- **Left panel (Transformer):** Shows attention distribution with values: BOS=0.32, Context=0.18, ANSWER=0.03, Context=0.34, Query=0.13. Shows low signal-to-noise ratio with "Attention Noise" labeled.
- **Middle panel (Differential Transformer - This Work):** Shows values: BOS=0.19, Context=0.01, ANSWER=0.31, Context=0.01, Query=0.48. Shows high signal-to-noise ratio.
- **Right panel (Multi-Needle Retrieval):** Bar chart showing accuracy comparison - Transformer at 55%, Differential Transformer at 80% for 85% context length.
- Supports claim: DIFF Transformer assigns significantly higher scores (0.31 vs 0.03) to the correct answer and much lower scores to irrelevant context compared to Transformer [p. 1].

## Proposed Solution: Differential Transformer [p. 1–2]

The authors introduce Differential Transformer (a.k.a. DIFF Transformer), a foundation architecture for large language models [p. 2]. The differential attention mechanism is proposed to cancel attention noise with differential denoising [p. 2].

Specifically, the method splits the query and key vectors into two groups and computes two separate softmax attention maps [p. 2]. Then the result of subtracting these two maps is regarded as attention scores [p. 2]. The differential attention eliminates attention noise, encouraging models to focus on critical information [p. 2]. The approach is analogous to noise-canceling headphones and differential amplifiers in electrical engineering, where the difference between two signals cancels out common-mode noise [p. 2].

In the middle of Figure 1, the authors present the normalized distribution of attention scores for DIFF Transformer [p. 2]. The results show that DIFF Transformer assigns significantly higher scores to the correct answer and much lower scores to irrelevant context compared to Transformer [p. 2]. The right side of Figure 1 shows that the proposed method achieves notable improvements in retrieval capability [p. 2].

## Experimental Results Summary [p. 2]

The authors conduct extensive experiments on language modeling [p. 2]. They scale up DIFF Transformer in terms of parameter count, training tokens, and context length [p. 2]. The scaling curves indicate that DIFF Transformer requires only about 65% of model size or training tokens needed by Transformer to achieve comparable language modeling performance [p. 2]. Moreover, DIFF Transformer outperforms Transformer in various downstream tasks [p. 2].

The long-sequence evaluation also shows that DIFF Transformer is highly effective in utilizing the increasing context [p. 2]. In addition, the experimental results demonstrate that DIFF Transformer has advantages for large language models [p. 2]. For example, the proposed method substantially outperforms Transformer in key information retrieval, hallucination mitigation, in-context learning, and information extraction [p. 2]. DIFF Transformer also reduces outliers in model activations, which provides new opportunities for quantization [p. 2]. The findings establish DIFF Transformer as an effective and distinctive foundation architecture for large language models [p. 2].
