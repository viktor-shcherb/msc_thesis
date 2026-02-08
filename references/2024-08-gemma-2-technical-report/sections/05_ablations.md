# 5. Ablations [p. 5]

This section focuses on the main finding of the work: the impact of knowledge distillation on small language models. [p. 5]

## Distillation versus From Scratch

## Table 6 | Comparison between a 2B model trained over 500B tokens either from scratch or with distillation from a 7B model [p. 5]

|  | from scratch | distilled |
|---|---|---|
| Average (3 bench.) | 60.3 | 67.7 |

In Table 6, distilling from a larger model improves performance compared to training from scratch. 500B is 10x more than the compute-optimal number of tokens for a 2B model. The authors distill from a 7B model to keep a ratio similar to their target distillation from 27B to 9B. [p. 5]

## Impact of Distillation w.r.t. Model Size

## Table 7 | Perplexity measured on a validation set of models of different sizes trained with or without distillation. The teacher has 7B parameters [p. 5]

|  | 200M | 400M | 1B |
|---|---|---|---|
| from scratch | 23 | 19 | 17 |
| distilled (7B) | 21 | 17 | 15 |

In Table 7, the impact of distillation as model size increases is measured. The gain remains as the model size is scaled. In this ablation, the teacher size is kept at 7B and smaller models are trained to simulate the same gap as between the final teacher and student sizes. [p. 5]

## GQA versus MHA

## Table 8 | Comparing the impact of replacing Multi-Head Attention (MHA) with GQA on a 9B model averaged over 4 benchmarks [p. 5]

|  | MHA | GQA |
|---|---|---|
| Average (4 bench.) | 50.3 | 50.8 |

Two instances of the 9B model with MHA or GQA are compared. Overall few changes in performance between both models are observed as measured on several benchmarks. GQA is chosen since it requires fewer parameters and is faster at inference time. [p. 5]

## Wide versus Deep

## Table 9 | Wide versus deep 9B models. Performance on 4 benchmarks, higher is better [p. 5]

|  | Wide | Deep |
|---|---|---|
| Average (4 bench.) | 50.8 | 52.0 |

A deeper 9B network is slightly better than a wider 9B for the same number of parameters. Although the gap is small, it is consistent across benchmarks and warrants the switch to a deeper architecture. [p. 5]

## Changing Sliding Window Size

## Table 10 | Impact of changing the sliding window size at inference time for the 9B model [p. 5]

| sliding window | 4096 | 2048 | 1024 |
|---|---|---|---|
| perplexity (val. set) | 1.63 | 1.63 | 1.64 |

The sliding window size of the local attention layers can be changed during inference with moderate impact on perplexity. Adjusting the size of the sliding window can thus be a leverage for slight inference speed gain. [p. 5]

## Impact of Formatting

Performance variance on MMLU across prompt/evaluation formatting variations is measured. Table 11 shows the standard deviations of MMLU scores for 12 formatting/evaluation combinations, a proxy for undesired performance variability. The Gemma 2 2B models are slightly less format-robust than the larger ones. Notably, Mistral 7B is significantly less robust than the Gemma models. [p. 5]

## Table 11 | Standard deviations of MMLU scores for 12 combinations of formatting and evaluation [p. 5]

|  | Standard Deviation |
|---|---|
| Gemma 1 2B | 1.5 |
| Gemma 2 2B | 2.1 |
| Mistral 7B | 6.9 |
| Gemma 1 7B | 0.7 |
| Gemma 2 9B | 0.9 |
| Gemma 2 27B | 1.0 |
