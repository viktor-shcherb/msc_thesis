# C Additional experiment results [p. 13]

## Different model formulations

[p. 13] To approximate (1), in addition to linear models as shown in (2), the authors also investigate log-linear models, which is defined as

$$\log \text{Attn}(x^{\text{doc}}, k) = \text{rel}(x^{\text{doc}}) + \text{bias}(k) + \epsilon, \quad (7)$$

where $\epsilon$ is a noise. They compute rank correlation as described in Sec. 3. The result is shown in Table 4. The log-linear model and linear are competitive to each other, which all result in rank correlation above 0.75.

**Table 4** (p. 13): Rank correlations of linear and log-linear models.

| Model form of $f$ | Rank correlation |
|-------------------|-----------------|
| Linear            | 0.76            |
| Log-linear        | 0.75            |

## Experiment tables

Table 5 shows the exact numbers in the experiments.

**Table 5** (p. 14): Our proposed attention intervention by calibrated attention stably improves models' RAG performances compared to existing re-ordering based baselines.

|              |        |                                    | Gold position in 10 documents |       |       |       | Gold position in 20 documents |       |       |       |
|--------------|--------|------------------------------------|------|-------|-------|-------|------|-------|-------|-------|
| Dataset      | Model  | Method                             | 1st  | 5th   | 10th  | Avg.  | 1st  | 10th  | 20th  | Avg.  |
| NaturalQuestion | Vicuna | Vanilla attention               | 74.35 | 54.83 | 52.01 | 60.39 | 71.93 | 47.34 | 50.65 | 56.64 |
|              |        | Calibrated attention               | 70.84 | 62.61 | 55.78 | 63.07 | 66.40 | 56.19 | 51.75 | 58.11 |
|              |        | Attention sorting                  | 72.54 | 59.54 | 63.12 | 65.06 | 69.37 | 56.91 | 62.41 | 62.89 |
|              |        | Prompt reordering                  | -     | -     | -     | 64.63 | -     | -     | -     | 58.68 |
|              |        | LongLLMLingua-$r_k$                | -     | -     | -     | 63.95 | -     | -     | -     | 59.92 |
|              |        | LongLLMLingua-$r_k$ + Cal.         | -     | -     | -     | 66.17 | -     | -     | -     | 62.22 |
| NaturalQuestion | Tulu   | Vanilla attention               | 70.50 | 48.81 | 49.26 | 56.19 | 56.94 | 35.32 | 46.59 | 46.28 |
|              |        | Calibrated attention               | 71.52 | 57.13 | 63.54 | 64.06 | 57.17 | 43.08 | 61.5  | 53.91 |
|              |        | Attention sorting                  | 62.52 | 56.43 | 63.2  | 60.71 | 45.57 | 43.12 | 45.04 | 44.57 |
|              |        | Prompt reordering                  | -     | -     | -     | 58.77 | -     | -     | -     | 44.64 |
|              |        | LongLLMLingua-$r_k$                | -     | -     | -     | 56.39 | -     | -     | -     | 43.90 |
|              |        | LongLLMLingua-$r_k$ + Cal.         | -     | -     | -     | 61.31 | -     | -     | -     | 47.34 |
| SynthWiki    | Vicuna | Vanilla attention                  | 65.15 | 48.68 | 68.58 | 60.80 | 53.73 | 43.63 | 60.20 | 52.52 |
|              |        | Calibrated attention               | 68.58 | 53.83 | 74.14 | 65.52 | 57.77 | 51.21 | 68.78 | 59.25 |
|              |        | Attention sorting                  | 67.37 | 64.14 | 67.57 | 66.36 | 60.60 | 51.55 | 61.31 | 57.82 |
|              |        | Prompt reordering                  | -     | -     | -     | 70.20 | -     | -     | -     | 62.22 |
|              |        | LongLLMLingua-$r_k$                | -     | -     | -     | 70.50 | -     | -     | -     | 62.42 |
|              |        | LongLLMLingua-$r_k$ + Cal.         | -     | -     | -     | 73.43 | -     | -     | -     | 66.96 |
| SynthWiki    | Tulu   | Vanilla attention                  | 92.22 | 81.51 | 94.34 | 89.35 | 80.40 | 60.30 | 95.75 | 78.81 |
|              |        | Calibrated attention               | 92.92 | 87.77 | 95.25 | 91.98 | 82.22 | 75.15 | 96.14 | 84.50 |
|              |        | Attention sorting                  | 92.92 | 92.82 | 93.83 | 93.19 | 94.04 | 93.53 | 95.05 | 94.20 |
|              |        | Prompt reordering                  | -     | -     | -     | 94.04 | -     | -     | -     | 95.55 |
|              |        | LongLLMLingua-$r_k$                | -     | -     | -     | 94.04 | -     | -     | -     | 95.45 |
|              |        | LongLLMLingua-$r_k$ + Cal.         | -     | -     | -     | 94.44 | -     | -     | -     | 95.75 |
