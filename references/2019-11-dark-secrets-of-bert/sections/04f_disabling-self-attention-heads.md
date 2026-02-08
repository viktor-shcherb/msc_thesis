# 4.6 Disabling self-attention heads [p. 7-8]

[p. 7] Since there does seem to be a certain degree of specialization for different heads, the authors investigated the effects of disabling different heads in BERT and the resulting effects on task performance. Since BERT relies heavily on the learned attention weights, they define disabling a head as modifying the attention values of a head to be constant *a = 1/L* for every token in the input sentence, where *L* is the length of the sentence. Thus, every token receives the same attention, effectively disabling the learned attention patterns while maintaining the information flow of the original model. Note that by using this framework, an arbitrary number of heads can be disabled, ranging from a single head per model to the whole layer or multiple layers.

## Results

[p. 7-8] The experiments suggest that certain heads have a detrimental effect on the overall performance of BERT, and this trend holds for all the chosen tasks. Unexpectedly, disabling some heads leads *not* to a drop in accuracy, as one would expect, but to an increase in performance. This effect is different across tasks and datasets. While disabling some heads improves the results, disabling the others hurts the results.

[p. 8] However, it is important to note that across all tasks and datasets, disabling some heads leads to an increase in performance. The gain from disabling a single head is different for different tasks, ranging from the minimum absolute gain of 0.1% for STS-B, to the maximum of 1.2% for MRPC (see Figure 8). In fact, for some tasks, such as MRPC and RTE, disabling a *random* head gives, on average, *an increase* in performance.

Furthermore, disabling a whole layer, that is, all 12 heads in a given layer, also improves the results. Figure 9 shows the resulting model performance on the target GLUE tasks when different layers are disabled. Notably, disabling the first layer in the RTE task gives a significant boost, resulting in an absolute performance gain of 3.2%. However, effects of this operation vary across tasks, and for QNLI and MNLI, it produces a performance drop of up to -0.2%.

## Figure 8 (p. 8)

**Figure 8** (p. 8): "Performance of the model while disabling one head at a time. The orange line indicates the baseline performance with no disabled heads. Darker colors correspond to greater performance scores."

Shows a 12 (layers) x 12 (heads) heatmap for each of seven GLUE tasks (MRPC, STS-B, SST-2, QQP, RTE, QNLI, MNLI). Below each heatmap, individual head accuracy values are printed. An orange horizontal line marks the baseline. Several heads exceed baseline when disabled, indicating that their removal improves performance.

Baseline and per-head-disabled performance values visible in the figure:

| Task | Baseline (orange line) | Min head score | Max head score |
|------|----------------------|----------------|----------------|
| MRPC | ~0.85 | 0.79 | 0.882 |
| STS-B | ~0.88 | 0.856 | 0.889 |
| SST-2 | ~0.92 | 0.318 | 0.922 |
| QQP | ~0.88 | 0.877 | 0.882 |
| RTE | ~0.58 | 0.509 | 0.592 |
| QNLI | ~0.84 | 0.507 | 0.856 |
| MNLI | ~0.83 | 0.830 | 0.841 |

## Figure 9 (p. 8)

**Figure 9** (p. 8): "Performance of the model while disabling one layer (that is, all 12 heads in this layer) at a time. The orange line indicates the baseline performance with no disabled layers. Darker colors correspond to greater performance scores."

Shows a column of 12 cells (one per layer) for each of seven GLUE tasks, with per-layer performance values. Key values visible in the figure:

| Layer | MRPC  | STS-B | SST-2 | QQP   | RTE   | QNLI  | MNLI  |
|-------|-------|-------|-------|-------|-------|-------|-------|
| 1     | —     | —     | —     | —     | 0.617 | 0.914 | —     |
| 2     | —     | —     | —     | —     | —     | —     | —     |
| 3     | 0.879 | 0.887 | 0.918 | —     | 0.876 | 0.906 | 0.892 |
| 4     | —     | —     | —     | —     | —     | —     | —     |
| 5     | —     | —     | —     | —     | —     | —     | —     |
| 6     | —     | —     | —     | —     | —     | —     | —     |
| 7     | 0.871 | 0.884 | 0.914 | —     | 0.5916| 0.871 | 0.823 |
| 8     | —     | —     | —     | —     | —     | —     | —     |
| 9     | 0.863 | 0.881 | 0.910 | 0.853 | 0.5915| 0.849 | 0.815 |
| 10    | —     | —     | —     | —     | —     | —     | —     |
| 11    | —     | —     | —     | —     | —     | —     | —     |
| 12    | 0.854 | 0.878 | 0.905 | 0.857 | 0.574 | 0.828 | 0.807 |

Note: Cells marked "—" had values not clearly legible in the figure. The numbers shown are those that were printed in the figure panels. The general trend is that performance tends to decrease as later layers are disabled, except for the RTE task where disabling layer 1 yields the best performance (0.617 vs. baseline ~0.584).

[p. 8] The readable values from the figure confirm:
- MRPC: layer 3 = 0.8817 [unclear: approximate], layer 12 = 0.854
- RTE: layer 1 = 0.617 (best, 3.2% absolute gain), layer 12 = 0.574
- QNLI: layer 1 = 0.914, layer 12 = 0.828
- MNLI: layer 9 = 0.815 [unclear: exact], layer 12 = 0.807
