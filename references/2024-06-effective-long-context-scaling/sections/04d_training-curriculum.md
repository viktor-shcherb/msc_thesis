# Training Curriculum [p. 10–11]

## Motivation [p. 10]

[p. 10] Continual pretraining has demonstrated its efficacy, but an open question remains: does pretraining from scratch with long sequences yield better performance than continual pretraining? This section studies different training curricula and investigates if continual pretraining can offer competitive performance with less computation budget.

## Experimental Setup [p. 10]

[p. 10] A 7B model is pretrained with 32,768 sequence length from start to end as baseline. Then various two-stage training curricula are explored where training begins with 4,096 sequence length and switches to 32,768 when the model completes 20%, 40%, 80% of the whole training process. For all cases, the same number of total training tokens is used and the number of tokens per each gradient update remains constant (4 million tokens) by adjusting the batch size and sequence length accordingly.

## Results on Long-Context Tasks [p. 10]

[p. 10] Models are evaluated on the long-text QA tasks used in Section 4.2 and the final models' perplexity on different validation corpora is reported.

**Table 10** (p. 10): Comparison of models with different training curricula on long context QA tasks.

| Pretrain Curriculum | FLOPs | NarrativeQA F1 | Qasper F1 | Quality EM | QMSum ROUGE-geo |
|---|---|---|---|---|---|
| 32k from scratch | 3.783 x 10^22 | 18.5 | 28.6 | 37.9 | 11.46 |
| 4k->32k @ 20% | 3.405 x 10^22 | 20.0 | 28.1 | 38.8 | 12.09 |
| 4k->32k @ 40% | 3.026 x 10^22 | 20.1 | 27.0 | 37.4 | 12.44 |
| 4k->32k @ 80% | 2.270 x 10^22 | 18.5 | 25.0 | 38.3 | 11.00 |

## Perplexity Results [p. 11]

**Table 11** (p. 11): Perplexity evaluation of models with different training curricula on three validation sets.

| Model | CC | Books | Wikipedia |
|---|---|---|---|
| 32k from scratch | 7.67 | 6.52 | 4.31 |
| 4k->32k @ 20% | 7.59 | 6.46 | 4.26 |
| 4k->32k @ 40% | 7.59 | 6.46 | 4.25 |
| 4k->32k @ 80% | 7.59 | 6.49 | 4.25 |

## Key Findings [p. 10–11]

[p. 10–11] As shown in Table 10 and Table 11, continual pretraining from short context models can easily save around 40% FLOPs while imposing almost no loss on performance. These results align with the training loss curves observed from each run in Figure 6 — the models can quickly adapt to the increased sequence length and get to similar loss scale.

**Figure 6** (p. 11): "Smoothed loss curves for the training curriculum ablation."

Two subplots:

Left panel: "losses for models trained with a fixed context window."
- Y-axis: Train loss (range 1.7 to 2.5)
- X-axis: Train steps (10k to 100k)
- Three lines: 4k, 8k, 32k. All decrease monotonically. The 4k line is consistently lowest, 8k in the middle, 32k highest — consistent with longer sequences being harder.

Right panel: "training curricula where we switch the context length from 4,096 to 32,768 at different stages indicated by the dashed lines."
- Y-axis: Train loss (range 1.7 to 2.5)
- X-axis: Train steps (10k to 100k)
- Four lines: 32k (baseline), 4k->32k @ 20%, 4k->32k @ 40%, 4k->32k @ 80%. The curriculum models initially follow the 4k loss curve (lower loss), then show a brief spike when switching to 32k before quickly converging to similar loss values as the 32k-from-scratch model within a few thousand steps.
