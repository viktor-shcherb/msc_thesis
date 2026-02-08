# 4.3 Change in self-attention patterns after fine-tuning [p. 5-6]

[p. 5] Fine-tuning has a huge effect on performance, and this section attempts to find out why. To study how attention per head changes on average for each of the target GLUE tasks, cosine similarity is calculated between pre-trained and fine-tuned BERT's flattened arrays of attention weights. The derived similarities are averaged over all the development set examples. If the number of development data examples for a given task exceeded 1000 (QQP, QNLI, MNLI, STS-B), 1000 examples were randomly sampled.

To evaluate contribution of pre-trained BERT to overall performance on the tasks, two configurations of weights initialization are considered: (1) pre-trained BERT weights, and (2) weights randomly sampled from normal distribution.

## Results

[p. 5] Figure 5 shows that for all the tasks except QQP, it is the last two layers that undergo the largest changes compared to the pre-trained BERT model. Table 1 shows that fine-tuned BERT outperforms pre-trained BERT by a significant margin on all the tasks (with an average of 35.9 points of absolute difference). This leads the authors to conclude that the last two layers encode task-specific features that are attributed to the gain of scores, while earlier layers capture more fundamental and low-level information used in fine-tuned models.

BERT with weights initialized from normal distribution and further fine-tuned for a given task consistently produces lower scores than the ones achieved with pre-trained BERT. In fact, for some tasks (STS-B and QNLI), initialization with random weights yields worse performance than pre-trained BERT without fine-tuning.

> "This suggests that pre-trained BERT does indeed contain linguistic knowledge that is helpful for solving these GLUE tasks." [p. 5-6]

These results are consistent with similar studies, e.g., Yosinski et al. (2014)'s results on fine-tuning a convolutional neural network pre-trained on ImageNet or Romanov and Shivade (2018)'s results on transfer learning for medical natural language inference.

## Table 1 (p. 5)

**Table 1** (p. 5): "GLUE task performance of BERT models with different initialization. We report the scores on the validation, rather than test data, so these results differ from the original BERT paper."

| Dataset | Pre-trained | Fine-tuned, initialized with normal distr. | Fine-tuned, initialized with pre-trained | Metric | Size |
|---------|-------------|---------------------------------------------|------------------------------------------|--------|------|
| MRPC    | 0/31.6      | 81.2/68.3                                   | 87.9/82.3                                | F1/Acc | 5.8K |
| STS-B   | 33.1        | 2.9                                          | 82.7                                     | Acc    | 8.6K |
| SST-2   | 49.1        | 80.5                                         | 92                                       | Acc    | 70K  |
| QQP     | 0/60.9      | 0/63.2                                       | 65.2/78.6                                | F1/Acc | 400K |
| RTE     | 52.7        | 52.7                                         | 64.6                                     | Acc    | 2.7K |
| QNLI    | 52.8        | 49.5                                         | 84.4                                     | Acc    | 130K |
| MNLI-m  | 31.7        | 61.0                                         | 78.6                                     | Acc    | 440K |

## Figure 5 (p. 6)

**Figure 5** (p. 6): "Per-head cosine similarity between pre-trained BERT's and fine-tuned BERT's self-attention maps for each of the selected GLUE tasks, averaged over validation dataset examples. Darker colors correspond to greater differences."

Shows a 12 (layers) x 12 (heads) heatmap for each of seven GLUE tasks (MRPC, STS-B, SST-2, QQP, RTE, QNLI, MNLI). For all tasks except QQP, the last two layers (11-12) show visibly darker colors (greater differences from pre-trained), indicating the most change during fine-tuning occurs in the final layers.

## Figure 6 (p. 6)

**Figure 6** (p. 6): "Per-task attention weights to the *[SEP]* (top row) and the *[CLS]* (bottom row) tokens averaged over input sequences' lengths and over dataset examples. Darker colors correspond to greater absolute weights."

Shows two rows of 12x12 heatmaps (layers x heads) for each of seven GLUE tasks. Top row: attention to [SEP]; bottom row: attention to [CLS]. Reveals which heads across layers attend most strongly to these special tokens, with distinct patterns per task.
