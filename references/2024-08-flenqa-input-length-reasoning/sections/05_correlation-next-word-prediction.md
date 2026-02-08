# 5 Correlation with Next Word Prediction [p. 7]

[p. 7] Perplexity is used as the main benchmark to show that models utilize their entire input (Anil et al., 2023; Jiang et al., 2024; Ding et al., 2024). However, it was shown that performance on downstream tasks does not necessarily correlate with model perplexity (Liu et al., 2023a; Xia et al., 2022; Tay et al., 2022). The authors use the flexibility of their dataset to understand the correlation between perplexity and reasoning accuracy.

In closed models, full vocabulary token probabilities are not accessible, so model perplexity cannot be measured. Instead, they resort to measuring next word accuracy on their data. They prompt models to complete the next word in a given text, and the output is correct if it is an exact match to the true next word. They use the samples in their dataset (without the questions) as the text and compare the results to the reasoning performance on the same samples.

Their method finds similar trends on the next word prediction task to those shown in other works (Anil et al., 2023; Jiang et al., 2024), namely accuracy increases as input is longer. However, as shown in Figure 6, next word accuracy correlates negatively with reasoning on FlenQA.

> "next word accuracy correlates negatively with reasoning on FlenQA" [p. 7]

Footnote 6: ρ_Pearson = −0.95, p = 0.01

This implies that measuring next word prediction and, similarly, perplexity, cannot substitute downstream task evaluation on long inputs.

**Figure 6** (p. 7): "Next word accuracy correlates negatively with the reasoning accuracy on FlenQA. Each point reflects the performance across 300 samples. Gemini-Pro is not included as it answered empty replies to the next word prediction task at any length."
- Title: "Reasoning and Next Word Accuracy"
- X-axis: Input length (# tokens), values: 250, 500, 1000, 1500, 2000, 2500, 3000
- Y-axis: Accuracy, range approximately 0.5 to 1.0
- Dotted lines for Next Word Prediction, solid lines for Reasoning
- Lines for GPT3.5, GPT4, Mistral Medium, Mixtral 8x7B, Gemini Pro (reasoning only)
- Next word prediction accuracy (dotted lines) increases with input length for all models shown, while reasoning accuracy (solid lines) decreases. The two sets of curves cross, demonstrating the negative correlation. GPT4 reasoning stays highest among reasoning lines. Mixtral 8x7B next word prediction rises steeply.
