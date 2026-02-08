# 3.4 Benchmarks on Original Context Window Size [p. 9–10]

[p. 9] The authors evaluate the models extended by Position Interpolation on several standard benchmark tasks within the original context window size of 2048. The evaluation results are listed in Table 5.

From the results, models extended to 8192 produce comparable results on the original benchmark which is designed for a much smaller context window, with a degradation of up to 2% on the benchmark tasks, for both 7B and 33B model sizes. Models extended to longer context windows regressed more on the benchmarks, but still in reasonable ranges for most tasks. [p. 9]

The authors also note that the choice of fine-tuning datasets does not seem to lead significant difference in the benchmark performances, which may be due to the limited number of fine-tuning steps used in their method. The regression on benchmark tasks is consistent with their observation on perplexity regression in Section 3.2. [p. 9]

## Table 5: Zero-shot performance on a subset of LLaMA Benchmarks [p. 10]

Models extended by Position Interpolation comparable performance as the original models, except for BoolQ dataset that may require models to pay close attention to word ordering in a short reference paragraph.

| Model Size | Context Window | Fine-tune on | BoolQ | PIQA | Race-M | Race-H | WinoGrande |
|-----------|---------------|-------------|-------|------|--------|--------|------------|
| 7B | 2048 | None | 76.1 | 78.9 | 55.7 | 42.2 | 69.6 |
| 7B | 8192 | Pile | 73.2 | 78.2 | 53.8 | 41.7 | 69.0 |
| 7B | 16384 | Pile | 69.8 | 77.6 | 53.3 | 40.9 | 67.8 |
| 7B | 32768 | Pile | 64.7 | 77.2 | 50.1 | 39.6 | 66.9 |
| 7B | 8192 | RedPajama | 75.5 | 77.4 | 54.5 | 41.5 | 68.1 |
| 33B | 2048 | None | 81.6 | 80.2 | 61.1 | 45.9 | 76.2 |
| 33B | 8192 | Pile | 80.2 | 80.7 | 60.2 | 45.7 | 75.9 |
