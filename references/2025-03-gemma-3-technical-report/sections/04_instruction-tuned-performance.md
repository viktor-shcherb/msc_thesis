# 4.2. Standard benchmarks [p. 5–6]

In Table 6, the authors show the performance of their final models across a variety of benchmarks compared to their previous model iteration, and Gemini 1.5. They do not compare directly with external models that often report their own evaluation settings, since running them in their setting does not guarantee a fair comparison. The authors encourage the reader to follow third-party static leaderboards for a fairer comparison across models. They include additional evaluations of their models on other benchmarks in the appendix.

**Table 6** (p. 6): "Performance of instruction fine-tuned (IT) models compared to Gemini 1.5, Gemini 2.0, and Gemma 2 on zero-shot benchmarks across different abilities."

|                      | Gemini 1.5 |      | Gemini 2.0 |      | Gemma 2 |      |      | Gemma 3 |      |      |      |
|----------------------|------------|------|------------|------|---------|------|------|---------|------|------|------|
|                      | Flash      | Pro  | Flash      | Pro  | 2B      | 9B   | 27B  | 1B      | 4B   | 12B  | 27B  |
| MMLU-Pro             | 67.3       | 75.8 | 77.6       | 79.1 | 15.6    | 46.8 | 56.9 | 14.7    | 43.6 | 60.6 | 67.5 |
| LiveCodeBench        | 30.7       | 34.2 | 34.5       | 36.0 | 1.2     | 10.8 | 20.4 | 1.9     | 12.6 | 24.6 | 29.7 |
| Bird-SQL (dev)       | 45.6       | 54.4 | 58.7       | 59.3 | 12.2    | 33.8 | 46.7 | 6.4     | 36.3 | 47.9 | 54.4 |
| GPQA Diamond         | 51.0       | 59.1 | 60.1       | 64.7 | 24.7    | 28.8 | 34.3 | 19.2    | 30.8 | 40.9 | 42.4 |
| SimpleQA             | 8.6        | 24.9 | 29.9       | 44.3 | 2.8     | 5.3  | 9.2  | 2.2     | 4.0  | 6.3  | 10.0 |
| FACTS Grounding      | 82.9       | 80.0 | 84.6       | 82.8 | 43.8    | 62.0 | 62.4 | 36.4    | 70.1 | 75.8 | 74.9 |
| Global MMLU-Lite     | 73.7       | 80.8 | 83.4       | 86.5 | 41.9    | 64.8 | 68.6 | 34.2    | 54.5 | 69.5 | 75.1 |
| MATH                 | 77.9       | 86.5 | 90.9       | 91.8 | 27.2    | 49.4 | 55.6 | 48.0    | 75.6 | 83.8 | 89.0 |
| HiddenMath           | 47.2       | 52.0 | 63.5       | 65.2 | 1.8     | 10.4 | 14.8 | 15.8    | 43.0 | 54.5 | 60.3 |
| MMMU (val)           | 62.3       | 65.9 | 71.7       | 72.7 | -       | -    | -    | -       | 48.8 | 59.6 | 64.9 |
