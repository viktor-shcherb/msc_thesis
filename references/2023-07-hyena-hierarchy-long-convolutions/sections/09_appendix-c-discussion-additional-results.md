# C Discussion and Additional Results [p. 24-25]

## Vocabulary size scaling

[p. 24]

Table C.1 showcases an interesting correlation between associative recall performance and loss on The Pile. In this case, the sequence length for associative recall is fixed to 2048, the same sequence length used to train all models on The Pile. [p. 24]

The authors observe a similar phenomenon on other slices of tasks from their mechanistic design benchmarks, indicating that it may be possible to derive predictive laws for performance at scale, based on fast experimentation on synthetic tasks with models of 1 or 2 layers. Surprisingly, performance on their language synthetics appears to be further linked to performance as attention replacement in other domains (Appendix A.4 for results on image classification). [p. 24]

**Table C.1:** Hyena accuracy on associative recall with varying vocabulary size 10, 20, 30, 40 in relation to test loss on The Pile after 5 billion tokens. The authors note a correlation between the two performance metrics, suggesting that slices of their mechanistic design synthetics may be potentially predictive of performance at scale. [p. 24]

| Model | Acc @ 10 | Acc @ 20 | Acc @ 30 | Acc @ 40 | Loss @ 5B on The Pile |
|---|---|---|---|---|---|
| Conv1d | 32 | 11 | 10 | 8 | 4.21 |
| AFT-conv | 55 | 21 | 12 | 10 | 3.57 |
| H3 | 92 | 60 | 13 | 10 | 2.69 |
| Transformer | 100 | 100 | 92 | 82 | 2.59 |
| Hyena | 100 | 100 | 98 | 85 | 2.59 |

## Single layer recall

[p. 25]

All experiments on synthetic tasks default to 2 layer models. The authors choose 2 as it is the canonical number for mechanistic analysis of Transformers (Elhage et al., 2021) based on *circuits*. Interestingly, a single layer of Hyena (width 64) is capable of performing associative recall, solving the task completely even in the challenging setting with vocabulary size 40. Reverse engineering exactly how the single Hyena operator is able to perform recall is left for future work. [p. 25]

## C.1 Learning Arithmetic

[p. 25]

The authors showcase an additional task in their mechanistic design benchmark: learning arithmetic. They train Hyena models of increasing depth (1, 2 and 3 layers) on a dataset of $D_n$-digit addition. As an example, a 3-digit addition input sample is given by the sequence:

$$1, 2, 3, 9, 5, 4, 1, 0, 7, 7$$

where the first 6 digits contain the two 3 digits numbers to add, and the last 4 the result. The models are optimized using standard autoregressive training i.e., predicting the next token, since they are causal. In particular, they optimize models to learn a map $x \mapsto y$ where $x$ is the original prompt without the last element, and $y$ equal to $x$ shifted right by one position. They mask the first $2D_n - 1$ elements of the loss for each sequence since they contain predictions for addends and not results. [p. 25]

Results are reported in Figure C.1. A single layer of Hyena is able to learn to perform addition with up to 4 digits. Longer numbers require deeper models. In their experiments, alternative architectures such as AFT-conv struggle to learn arithmetic, signaling a cap in capability. [p. 25]

**Figure C.1** (p. 25): "Test loss and accuracy of Hyena on addition with different numbers of digits and model depths. Each plot reports the results of a different experiment, with the curve tracing test results during training."

The figure is a 3x4 grid of plots. Rows correspond to model depths (Layers: 1, 2, 3) and columns correspond to digit counts (Digits: 2, 4, 8, 16). Each plot has x-axis "epochs" (0-80) and y-axis (0-3). Two curves are shown per plot (test loss in one color, accuracy in another). Key observations:
- Layers=1, Digits=2: both loss and accuracy converge quickly (loss to ~0, accuracy to ~1 by epoch 20)
- Layers=1, Digits=4: similar convergence pattern
- Layers=1, Digits=8: loss drops but does not fully converge; accuracy remains low
- Layers=1, Digits=16: no convergence
- Layers=2, Digits=2 and 4: quick convergence
- Layers=2, Digits=8: converges around epoch 40-60
- Layers=2, Digits=16: partial convergence
- Layers=3, Digits=2 and 4: quick convergence
- Layers=3, Digits=8: converges
- Layers=3, Digits=16: converges around epoch 40-60
