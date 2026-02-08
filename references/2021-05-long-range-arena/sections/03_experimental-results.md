# 3 Experimental Results [p. 5-6]

## 3.1 Models [p. 5]

The evaluation is based on ten recently proposed efficient Transformer models. Aside from the standard vanilla Transformer (Vaswani et al., 2017) and a simple local attention baseline, the models compared are:

1. Sparse Transformers (Child et al., 2019)
2. Longformers (Beltagy et al., 2020)
3. Linformers (Wang et al., 2020)
4. Reformers (Kitaev et al., 2020)
5. Sinkhorn Transformers (Tay et al., 2020b)
6. Synthesizers (Tay et al., 2020a)
7. BigBird (Zaheer et al., 2020)
8. Linear Transformers (Katharopoulos et al., 2020)
9. Performers (Choromanski et al., 2020a)

The authors believe these ten models represent a diverse cross-section of recent efficient Transformer models.

## 3.2 Philosophy Behind the Benchmark [p. 5-6]

[p. 5-6] The authors note that it is non-trivial and almost impossible to conduct a perfectly fair evaluation of all models. The large search space motivates them to follow a set of fixed hyperparameters (number of layers, heads, embedding dimensions, etc.) for all models. The best performance and relative order of the models may change if hyperparameters were aggressively tuned for all models. Hence, the results are not meant to be a final authoritative document on which xformer is the best. Instead, the paper provides a starting point for future research and strives to be as **fair** as possible. The code is released with all hyperparameters and implementation details. The paper is intended to be a living document. The authors also implemented all models to the best of their abilities and often consulted with the original developers of the included models.

## 3.3 Quantitative Results [p. 6]

Based on the results, the authors observe that (1) all proposed tasks in LRA are considerably challenging, and (2) there are meaningful differences in model performance across different xformer models.

**Table 1** (p. 6): "Experimental results on Long-Range Arena benchmark. Best model is in boldface and second best is underlined. All models do not learn anything on Path-X task, contrary to the Pathfinder task and this is denoted by FAIL. This shows that increasing the sequence length can cause seriously difficulties for model training. We leave Path-X on this benchmark for future challengers but do not include it on the Average score as it has no impact on relative performance."

| Model | ListOps | Text | Retrieval | Image | Pathfinder | Path-X | Avg |
|---|---|---|---|---|---|---|---|
| Transformer | 36.37 | 64.27 | 57.46 | 42.44 | 71.40 | FAIL | 54.39 |
| Local Attention | 15.82 | 52.98 | 53.39 | 41.46 | 66.63 | FAIL | 46.06 |
| Sparse Trans. | 17.07 | 63.58 | **59.59** | **44.24** | 71.71 | FAIL | 51.24 |
| Longformer | 35.63 | 62.85 | 56.89 | 42.22 | 69.71 | FAIL | 53.46 |
| Linformer | 35.70 | 53.94 | 52.27 | 38.56 | <u>76.34</u> | FAIL | 51.36 |
| Reformer | **37.27** | 56.10 | 53.40 | 38.07 | 68.50 | FAIL | 50.67 |
| Sinkhorn Trans. | 33.67 | 61.20 | 53.83 | 41.23 | 67.45 | FAIL | 51.39 |
| Synthesizer | <u>36.99</u> | 61.68 | 54.67 | 41.61 | 69.45 | FAIL | 52.88 |
| BigBird | 36.05 | 64.02 | <u>59.29</u> | 40.83 | 74.87 | FAIL | **55.01** |
| Linear Trans. | 16.13 | **65.90** | 53.09 | 42.34 | 75.30 | FAIL | 50.55 |
| Performer | 18.01 | <u>65.40</u> | 53.82 | <u>42.77</u> | **77.05** | FAIL | 51.41 |
| Task Avg (Std) | 29 (9.7) | 61 (4.6) | 55 (2.6) | 41 (1.8) | 72 (3.7) | FAIL | 52 (2.4) |

### Results on ListOps [p. 6]

The ListOps task (10-way classification) has proven to be reasonably difficult with the best models obtaining only 37%. The considerable gap to random chance shows that models are indeed learning the task. The inductive bias of the xformer model plays a substantial role: approximately half the xformer models are able to get > 30% performance while the remainder only get slightly above random chance. This may imply that certain efficiency-inspired inductive biases may be better at handling hierarchical data than others. The results suggest that kernel-based models (e.g., Performer, Linear Transformers) are possibly not as effective on hierarchically structured data.

### Results on Text Classification [p. 6]

Byte-level classification is shown to be difficult and challenging especially when no pretraining or contextual embeddings are used. The best model only obtains 65.90 accuracy. The Linear Transformer performs well on this task, along with the Performer model. Contrary to the ListOps task, it seems like fast kernel-based models do well on this task.

### Results on Retrieval [p. 6]

The scores of different models on this task are also rather low (average of 55%), indicating the difficulty of the task. The vanilla Transformer model only achieves 57.46% accuracy with some xformer variants scoring very close to random chance. The best performing model is the Sparse Transformer and the second best is BigBird. The authors find that models that follow fixed sparse patterns tend to do well on this task. Models that are based on low-rank factorization and kernels perform relatively worse.

---
[p. 7 continued]

### Results on Image Classification [p. 7]

On the image classification task, most models perform quite similarly (low variance amongst model performance). The best model on this task is the Sparse Transformer, followed by the Performer. Linformer and Reformers do not do well on this task. On a related note, the authors also observed most of models struggle generalizing to the test set even though they manage to overfit the training set. While they extensively tried different regularization techniques on every single model, there is a rather large gap between their performance on train and test set (more details in Appendix).

### Results on Pathfinder / Path-X [p. 7]

Results show that all models achieve reasonable performance on the Pathfinder task. The average performance is 72 and the best model Performer obtains 77.05% accuracy. The Local Attention model performs the worse out of all models.

All models failed to solve the Path-X task, achieving at best 50%. The authors find this intriguing because this is essentially an identical task to the standard Pathfinder, albeit with much longer sequence lengths. Hence, they observe that the extreme length of the task can significantly obstruct a model from learning anything meaningful. Path-X is left in the benchmark suite, hoping to spur future progress in modeling sequences at extreme lengths.

## 3.4 Efficiency Benchmarks [p. 7]

The authors report efficiency metrics of their runs. For simplicity, they use the byte-level text classification benchmark and report run times and memory consumption of the sequence lengths {1K, 2K, 3K, 4K}. They use a batch size of 32 for all runs and conduct experiments on 4x4 TPU V3 Chips. They emphasize that this is again largely conditioned on hardware and implementation details (more details can be found in the appendix).

### Results on Speed [p. 7]

**Table 2** (p. 7): "Benchmark results of all Xformer models with a consistent batch size of 32 across all models. We report relative speed increase/decrease in comparison with the vanilla Transformer in brackets besides the steps per second. Memory usage refers to per device memory usage across each TPU device. Benchmarks are run on 4x4 TPU V3 Chips."

| Model | Steps per second ||| | Peak Memory Usage (GB) |||
| | 1K | 2K | 3K | 4K | 1K | 2K | 3K | 4K |
|---|---|---|---|---|---|---|---|---|
| Transformer | 8.1 | 4.9 | 2.3 | 1.4 | 0.85 | 2.65 | 5.51 | 9.48 |
| Local Attention | 9.2 (1.1x) | 8.4 (1.7x) | 7.4 (3.2x) | 7.4 (5.3x) | 0.42 | 0.76 | 1.06 | 1.37 |
| Linformer | <u>9.3</u> (1.2x) | 9.1 (1.9x) | 8.5 (3.7x) | 7.7 (5.5x) | **0.37** | **0.55** | 0.99 | **0.99** |
| Reformer | 4.4 (0.5x) | 2.2 (0.4x) | 1.5 (0.7x) | 1.1 (0.8x) | 0.48 | 0.99 | 1.53 | 2.28 |
| Sinkhorn Trans. | 9.1 (1.1x) | 7.9 (1.6x) | 6.6 (2.9x) | 5.3 (3.8x) | 0.47 | 0.83 | 1.13 | 1.48 |
| Synthesizer | 8.7 (1.1x) | 5.7 (1.2x) | 6.6 (2.9x) | 1.9 (1.4x) | 0.65 | 1.98 | 4.09 | 6.99 |
| BigBird | 7.4 (0.9x) | 3.9 (0.8x) | 2.7 (1.2x) | 1.5 (1.1x) | 0.77 | 1.49 | 2.18 | 2.88 |
| Linear Trans. | 9.1 (1.1x) | <u>9.3</u> (1.9x) | 8.6 (3.7x) | 7.8 (5.6x) | **0.37** | 0.57 | **0.80** | 1.03 |
| Performer | **9.5** (1.2x) | **9.4** (1.9x) | **8.7** (3.8x) | **8.0** (5.7x) | **0.37** | 0.59 | <u>0.82</u> | <u>1.06</u> |

Low-rank and kernel-based models are generally the fastest. The overall fastest model is the Performer (Choromanski et al., 2020a), which is 5.7x faster than Transformers on the 4K sequence length. Linformer (Wang et al., 2020) and Linear Transformers (Katharopoulos et al., 2020) come in a close second and are almost as fast as Performers (at 5.5 to 5.6x faster). Based on the authors' implementation, the slowest model is the Reformer model (Kitaev et al., 2020) that is about 80% the speed of vanilla Transformer at 4K sequence lengths and half the speed at 1K sequence length.

### Results on Memory Consumption [p. 7-8]

[p. 7] The model with the smallest memory footprint in the benchmarks is the Linformer model, coming in at 0.99GB per TPU device as compared to 9.48GB per TPU device for the vanilla Transformers at N = 4K. That is about a 10x reduction in memory footprint. Similar to speed, Performers and Linear Transformers are also relatively compact and are almost as compact as Linformers. Other models (Local Attention, Reformers, BigBird, Synthesizers) are still less memory hungry compared to vanilla Transformers but are relatively less efficient [p. 8] (memory consumption wise) compared to Linformers, Performers, and Linear Transformers. The memory consumption of models such as Linformer and Performer scales very well, with the memory usage at 3K and 4K being approximately equal.

## 3.5 Overall Results: No One-Size-Fits-All [p. 8]

Based on the analysis, the best qualitative performance in terms of LRA score, i.e. integrated across all five tasks, is the BigBird model. While BigBird does not do extremely well on any individual task compared to other models, it has consistently good performance across all tasks. Performers and Linear Transformers have strong performance on some tasks but their average is lowered by the ListOps task. Figure 3 shows the trade-off between qualitative performance, model speed, and memory footprint. While BigBird performs well, its speed is almost similar to the vanilla Transformer. On the other hand, a model like Local Attention is fast at the cost of lower quantitative performance. Among these models, the kernel-based variants, i.e., Performer, Linformer, and Linear Transformer seem to be able to make a better trade-off in terms of speed and performance, while having reasonable memory usage.

**Figure 3** (p. 8): "Performance (y axis), speed (x axis), and memory footprint (size of the circles) of different models."
- Scatter plot with x-axis "Speed (examples per sec)" (range ~50 to ~350) and y-axis "LRA Score" (range ~44 to ~56). Circle size represents memory footprint.
- BigBird: highest LRA Score (~55.0), low speed (~50), large circle (high memory).
- Transformer: LRA Score ~54.4, low speed (~50), large circle.
- Synthesizer: LRA Score ~53, speed ~100, medium-large circle.
- Reformer: LRA Score ~50.5, speed ~50, medium circle.
- Sinkhorn: LRA Score ~51.4, speed ~150, medium circle.
- Linformer: LRA Score ~51.4, speed ~225, small circle (low memory).
- Performer: LRA Score ~51.4, speed ~300, small circle.
- Linear Transformer: LRA Score ~50.5, speed ~250, small-medium circle.
- Local Attention: LRA Score ~46, speed ~225, medium circle.
- Key insight: kernel-based models (Performer, Linformer, Linear Transformer) cluster in the upper-right region with small circles, indicating good speed-performance-memory trade-offs. BigBird and Transformer are in the upper-left with large circles (slow, memory-heavy but highest quality).
