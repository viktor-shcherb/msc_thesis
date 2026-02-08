# Appendix C: Additional Ablation Studies [p. 16]

## C.1 Effect of Number of Training Steps

[p. 16] Figure 5 presents MNLI Dev accuracy after fine-tuning from a checkpoint that has been pre-trained for k steps. This allows answering the following questions:

1. **Question:** Does BERT really need such a large amount of pre-training (128,000 words/batch * 1,000,000 steps) to achieve high fine-tuning accuracy?
   **Answer:** Yes, BERT_BASE achieves almost 1.0% additional accuracy on MNLI when trained on 1M steps compared to 500k steps.

2. **Question:** Does MLM pre-training converge slower than LTR pre-training, since only 15% of words are predicted in each batch rather than every word?
   **Answer:** The MLM model does converge slightly slower than the LTR model. However, in terms of absolute accuracy the MLM model begins to outperform the LTR model almost immediately.

### Figure 5

**Figure 5** (p. 16): "Ablation over number of training steps. This shows the MNLI accuracy after fine-tuning, starting from model parameters that have been pre-trained for k steps. The x-axis is the value of k."

- X-axis: Pre-training Steps (Thousands), ranging from ~200 to 1,000
- Y-axis: MNLI Dev Accuracy, ranging from ~76 to ~84
- Two lines plotted:
  - BERT_BASE (Masked LM): triangle markers, starts around 78 at 200k steps, rises to about 84 at 1M steps, with a curve that continues to increase but with diminishing returns
  - BERT_BASE (Left-to-Right): circle markers, starts around 76.5 at 200k steps, rises to about 83.5 at 1M steps
- The MLM line is consistently above the LTR line after approximately 200k steps, with both curves showing continued improvement through 1M steps

## C.2 Ablation for Different Masking Procedures

[p. 16] In Section 3.1, the paper mentions that BERT uses a mixed strategy for masking the target tokens when pre-training with the masked language model (MLM) objective. This section is an ablation study to evaluate the effect of different masking strategies.

The purpose of the masking strategies is to reduce the mismatch between pre-training and fine-tuning, as the `[MASK]` symbol never appears during the fine-tuning stage. Dev results for both MNLI and NER are reported. For NER, both fine-tuning and feature-based approaches are reported, as the mismatch is expected to be amplified for the feature-based approach since the model will not have the chance to adjust the representations.

### Table 8: Ablation over different masking strategies

[p. 16] In the table, MASK means that the target token is replaced with the `[MASK]` symbol for MLM; SAME means that the target token is kept as is; RND means that the target token is replaced with another random token. The numbers in the left part of the table represent the probabilities of the specific strategies used during MLM pre-training (BERT uses 80%, 10%, 10%). The right part of the table represents the Dev set results. For the feature-based approach, the last 4 layers of BERT are concatenated as the features, which was shown to be the best approach in Section 5.3.

| MASK | SAME | RND | MNLI Fine-tune | NER Fine-tune | NER Feature-based |
|---|---|---|---|---|---|
| 80% | 10% | 10% | 84.2 | 95.4 | 94.9 |
| 100% | 0% | 0% | 84.3 | 94.9 | 94.0 |
| 80% | 0% | 20% | 84.1 | 95.2 | 94.6 |
| 80% | 20% | 0% | 84.4 | 95.2 | 94.7 |
| 0% | 20% | 80% | 83.7 | 94.8 | 94.6 |
| 0% | 0% | 100% | 83.6 | 94.9 | 94.6 |

### Key findings

[p. 16] Fine-tuning is surprisingly robust to different masking strategies. However, as expected, using only the MASK strategy was problematic when applying the feature-based approach to NER. Interestingly, using only the RND strategy performs much worse than the BERT strategy (80/10/10) as well.
