# H. Results on All Tasks for All Model Sizes [p. 63-67]

## Table H.1

**Table H.1** (p. 63): "Scores for every task, setting and model that we investigate in this paper."

The table reports Zero-Shot, One-Shot, and Few-Shot results across all 8 GPT-3 model sizes (Small, Med, Large, XL, 2.7B, 6.7B, 13B, 175B) plus a 175B (test server) column for few-shot. Columns are grouped: Name, Metric, Split, Fine-tune SOTA, K, then Zero-Shot scores (8 models), One-Shot scores (8 models), and Few-Shot scores (8 models + test server).

Due to the extreme density of the table (over 50 rows and ~27 numeric columns each), the full table is reproduced below in grouped sub-tables by task category. All numbers are read directly from the PDF.

### Cloze and Completion Tasks

| Name | Metric | Split | Fine-tune SOTA | K | Zero-Shot ||| One-Shot ||| Few-Shot |||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | Small | ... | 175B | Small | ... | 175B | Small | ... | 175B |

**HellaSwag**
- Metric: acc, Split: dev, SOTA: 85.6, K=20
- Zero-Shot: 33.7 / 43.6 / 51.0 / 54.7 / 62.8 / 67.4 / 70.9 / 78.9
- One-Shot: 33.0 / 42.9 / 50.5 / 53.5 / 61.9 / 66.5 / 70.0 / 78.1
- Few-Shot: 33.5 / 43.1 / 51.3 / 54.9 / 62.9 / 67.3 / 71.3 / 79.3

**LAMBADA** (acc)
- Metric: acc, Split: test, SOTA: 68.0, K=15
- Zero-Shot: 42.7 / 54.3 / 60.4 / 63.6 / 67.1 / 70.3 / 72.5 / 76.2
- One-Shot: 22.0 / 47.1 / 53.6 / 58.3 / 63.1 / 65.4 / 69.0 / 72.5
- Few-Shot: 22.0 / 40.4 / 63.2 / 57.0 / 78.1 / 79.1 / 81.3 / 86.4

**LAMBADA** (ppl)
- Metric: ppl, Split: test, SOTA: 8.63, K=15
- Zero-Shot: 18.6 / 9.09 / 6.53 / 5.44 / 4.60 / 4.00 / 3.56 / 3.00
- One-Shot: 163.0 / 11.6 / 8.29 / 6.46 / 5.53 / 4.64 / 4.06 / 3.35
- Few-Shot: 163.0 / 27.6 / 6.63 / 7.45 / 2.89 / 2.56 / 2.16 / 1.92

**StoryCloze**
- Metric: acc, Split: test, SOTA: 91.8, K=70
- Zero-Shot: 63.3 / 68.5 / 72.4 / 73.4 / 77.2 / 77.7 / 79.5 / 83.2
- One-Shot: 62.3 / 68.7 / 72.3 / 74.2 / 77.3 / 78.0 / 79.0 / 84.7
- Few-Shot: 62.3 / 70.2 / 73.9 / 76.1 / 80.0 / 81.2 / 83.0 / 87.7

### Question Answering

**NQs**
- Metric: acc, Split: test, SOTA: 44.5, K=64
- Zero-Shot: 0.64 / 1.75 / 2.71 / 4.40 / 5.79 / 7.84 / 14.4 / 14.6
- One-Shot: 1.19 / 3.07 / 4.79 / 5.43 / 8.73 / 9.78 / 13.7 / 23.0
- Few-Shot: 1.72 / 4.46 / 7.89 / 9.72 / 13.2 / 17.0 / 21.0 / 29.9

**TriviaQA**
- Metric: acc, Split: dev, SOTA: 68.0, K=64
- Zero-Shot: 4.15 / 7.61 / 14.0 / 19.7 / 31.3 / 38.7 / 41.8 / 64.3
- One-Shot: 4.19 / 12.9 / 20.5 / 26.5 / 35.9 / 44.4 / 51.3 / 68.0
- Few-Shot: 6.96 / 16.3 / 26.5 / 32.1 / 42.3 / 51.6 / 57.5 / 71.2

**WebQs**
- Metric: acc, Split: test, SOTA: 45.5, K=64
- Zero-Shot: 1.77 / 3.20 / 4.33 / 4.63 / 7.92 / 7.73 / 8.22 / 14.4
- One-Shot: 2.56 / 6.20 / 8.51 / 9.15 / 14.5 / 15.1 / 19.0 / 20.3
- Few-Shot: 5.46 / 12.6 / 15.9 / 19.6 / 24.8 / 27.7 / 33.5 / 41.5

### Translation

**Ro->En 16**
- Metric: BLEU-mb, Split: test, SOTA: 39.9, K=64
- Zero-Shot: 2.08 / 2.71 / 3.09 / 3.15 / 16.3 / 8.34 / 20.2 / 19.9
- One-Shot: 0.55 / 15.4 / 23.0 / 26.3 / 30.6 / 33.2 / 35.6 / 38.6
- Few-Shot: 1.25 / 20.7 / 25.8 / 29.2 / 33.1 / 34.8 / 37.0 / 39.5

**Ro->En 16** (BLEU-sb)
- Metric: BLEU-sb, Split: test, K=64
- Zero-Shot: 2.39 / 3.08 / 3.49 / 3.56 / 16.8 / 8.78 / 20.5 / 20.9
- One-Shot: 0.65 / 19.5 / 23.6 / 26.8 / 31.3 / 34.2 / 36.7 / 40.0
- Few-Shot: 1.40 / 21.3 / 26.6 / 30.1 / 34.3 / 36.2 / 38.4 / 41.3

**En->Ro 16**
- Metric: BLEU-mb, Split: test, SOTA: 38.5, K=64
- Zero-Shot: 2.14 / 2.65 / 2.53 / 2.50 / 3.46 / 4.24 / 5.32 / 14.1
- One-Shot: 0.35 / 3.30 / 7.89 / 8.72 / 12.5 / 15.1 / 17.3 / 20.6
- Few-Shot: 1.25 / 5.90 / 8.43 / 10.7 / 14.4 / 16.3 / 18.0 / 21.0

**En->Ro 16** (BLEU-sb)
- Metric: BLEU-sb, Split: test, K=64
- Zero-Shot: 2.61 / 3.11 / 3.07 / 3.09 / 4.26 / 5.31 / 6.43 / 18.0
- One-Shot: 0.55 / 3.90 / 9.15 / 10.3 / 15.7 / 18.2 / 20.8 / 28.4
- Few-Shot: 1.64 / 7.40 / 10.9 / 12.9 / 17.2 / 19.6 / 21.8 / 25.8

**Fr->En 14**
- Metric: BLEU-mb, Split: test, SOTA: 35.0, K=64
- Zero-Shot: 1.81 / 2.53 / 3.47 / 3.13 / 20.6 / 15.1 / 21.8 / 21.2
- One-Shot: 1.28 / 15.9 / 23.7 / 26.3 / 29.0 / 30.5 / 30.2 / 33.7
- Few-Shot: 4.98 / 25.5 / 28.5 / 31.1 / 33.7 / 34.9 / 36.6 / 39.2

**Fr->En 14** (BLEU-sb)
- Metric: BLEU-sb, Split: test, K=64
- Zero-Shot: 2.29 / 2.99 / 3.90 / 3.60 / 21.5 / 15.5 / 22.4 / 21.9
- One-Shot: 1.50 / 16.3 / 24.4 / 27.0 / 9.00 / 31.6 / 31.4 / 35.6
- Few-Shot: 5.30 / 26.2 / 29.5 / 32.2 / 35.1 / 36.4 / 38.3 / 41.4

**En->Fr 14**
- Metric: BLEU-mb, Split: test, K=64
- Zero-Shot: 1.74 / 2.16 / 2.73 / 2.15 / 15.1 / 8.82 / 12.0 / 25.2
- One-Shot: 0.49 / 8.00 / 14.8 / 15.9 / 20.3 / 23.1 / 24.9 / 28.3
- Few-Shot: 4.09 / 14.5 / 19.3 / 21.5 / 24.9 / 27.3 / 29.3 / 33.6

**En->Fr 14** (BLEU-sb)
- Metric: BLEU-sb, Split: test, K=64
- Zero-Shot: 2.44 / 2.75 / 3.54 / 2.82 / 19.3 / 11.4 / 15.3 / 31.3
- One-Shot: 0.81 / 10.0 / 18.2 / 19.3 / 24.7 / 28.3 / 30.1 / 34.1
- Few-Shot: 5.31 / 18.0 / 23.6 / 26.1 / 30.3 / 33.3 / 35.5 / 39.9

**De->En 16**
- Metric: BLEU-mb, Split: test, SOTA: 40.2, K=64
- Zero-Shot: 2.06 / 3.27 / 3.41 / 3.63 / 21.5 / 17.3 / 23.0 / 27.2
- One-Shot: 0.83 / 16.2 / 22.5 / 24.7 / 26.2 / 30.7 / 33.0 / 30.4
- Few-Shot: 3.25 / 22.7 / 26.6 / 30.1 / 34.9 / 33.7 / 34.8 / 37.3 / 40.6

**De->En 16** (BLEU-sb)
- Metric: BLEU-sb, Split: test, K=64
- Zero-Shot: 2.39 / 3.27 / 3.85 / 4.04 / 22.5 / 18.2 / 24.4 / 28.6
- One-Shot: 0.93 / 17.1 / 23.4 / 25.8 / 29.2 / 31.9 / 34.5 / 32.1
- Few-Shot: 3.60 / 23.8 / 27.5 / 30.5 / 34.1 / 36.5 / 39.1 / 43.0

**En->De 16**
- Metric: BLEU-mb, Split: test, K=64
- Zero-Shot: 1.70 / 2.27 / 2.31 / 2.43 / 12.9 / 8.66 / 10.4 / 24.6
- One-Shot: 0.50 / 7.00 / 12.9 / 13.1 / 18.3 / 20.9 / 22.5 / 26.2
- Few-Shot: 3.42 / 12.3 / 15.4 / 17.1 / 20.9 / 23.0 / 26.6 / 29.7

**En->De 16** (BLEU-sb)
- Metric: BLEU-sb, Split: test, K=64
- Zero-Shot: 2.09 / 2.65 / 2.75 / 2.92 / 13.7 / 9.36 / 11.0 / 25.3
- One-Shot: 0.54 / 7.40 / 13.4 / 13.4 / 18.8 / 21.7 / 23.3 / 27.3
- Few-Shot: 1.29 / 19.6 / 16.1 / 17.7 / 21.7 / 24.1 / 27.1 / 30.9

### Winograd-Style Tasks

**Winograd**
- Metric: acc, Split: test, SOTA: 93.8, K=7
- Zero-Shot: 66.3 / 72.9 / 74.7 / 76.9 / 82.4 / 85.7 / 87.9 / 88.3
- One-Shot: 63.4 / 68.5 / 72.9 / 76.9 / 82.4 / 84.6 / 86.1 / 89.7
- Few-Shot: 63.4 / 67.4 / 73.6 / 76.9 / 84.3 / 85.4 / 82.4 / 88.6

**Winogrande**
- Metric: acc, Split: dev, SOTA: 84.6, K=50
- Zero-Shot: 52.0 / 52.1 / 57.4 / 58.7 / 62.3 / 64.5 / 67.9 / 70.2
- One-Shot: 51.2 / 53.0 / 58.3 / 59.1 / 61.7 / 65.8 / 66.9 / 73.2
- Few-Shot: 51.3 / 52.6 / 57.5 / 61.2 / 62.6 / 67.4 / 70.0 / 77.7

### Common Sense Reasoning

**PIQA**
- Metric: acc, Split: dev, SOTA: 77.1, K=50
- Zero-Shot: 64.6 / 70.2 / 72.9 / 75.1 / 75.6 / 78.0 / 78.5 / 81.0
- One-Shot: 64.3 / 69.3 / 71.8 / 74.4 / 74.3 / 76.3 / 77.8 / 80.5
- Few-Shot: 64.3 / 69.4 / 72.0 / 74.3 / 75.4 / 77.8 / 79.9 / 82.3

**ARC (Challenge)**
- Metric: acc, Split: test, SOTA: 78.5, K=50
- Zero-Shot: 26.6 / 29.5 / 31.8 / 35.5 / 38.0 / 41.4 / 43.7 / 51.4
- One-Shot: 25.5 / 30.2 / 31.6 / 36.4 / 38.4 / 41.5 / 43.1 / 53.2
- Few-Shot: 25.8 / 28.4 / 32.3 / 36.7 / 39.5 / 43.4 / 48.1 / 51.5

**ARC (Easy)**
- Metric: acc, Split: test, SOTA: 92.0, K=50
- Zero-Shot: 43.6 / 46.5 / 53.0 / 53.8 / 58.2 / 60.2 / 63.6 / 68.8
- One-Shot: 42.7 / 48.2 / 54.6 / 55.9 / 60.3 / 62.6 / 66.8 / 71.2
- Few-Shot: 42.7 / 51.0 / 58.1 / 59.1 / 62.1 / 65.8 / 69.1 / 70.1

**OpenBookQA**
- Metric: acc, Split: test, SOTA: 87.2, K=100
- Zero-Shot: 35.6 / 43.2 / 45.2 / 46.8 / 51.0 / 50.4 / 55.6 / 57.6
- One-Shot: 37.0 / 39.8 / 46.2 / 46.4 / 53.4 / 55.0 / 55.8 / 58.8
- Few-Shot: 37.0 / 43.6 / 48.0 / 50.6 / 55.6 / 55.2 / 60.4 / 65.4

### Reading Comprehension

**QuAC**
- Metric: f1, Split: dev, SOTA: 74.4, K=5
- Zero-Shot: 21.2 / 26.8 / 31.0 / 30.1 / 34.7 / 36.1 / 38.4 / 41.5
- One-Shot: 24.1 / 26.9 / 31.9 / 32.3 / 37.4 / 39.0 / 40.6 / 43.4
- Few-Shot: 24.1 / 29.3 / 34.2 / 34.2 / 38.2 / 39.9 / 40.9 / 44.3

**RACE-h**
- Metric: acc, Split: test, SOTA: 90.0, K=10
- Zero-Shot: 35.2 / 37.9 / 40.1 / 40.9 / 42.4 / 44.1 / 44.6 / 45.5
- One-Shot: 34.3 / 37.3 / 40.0 / 42.0 / 43.8 / 44.3 / 44.8 / 45.9
- Few-Shot: 34.3 / 37.0 / 40.4 / 41.1 / 42.3 / 44.7 / 45.1 / 45.8

**RACE-m**
- Metric: acc, Split: test, SOTA: 93.1, K=10
- Zero-Shot: 42.1 / 47.2 / 52.1 / 52.3 / 54.7 / 54.4 / 56.7 / 58.4
- One-Shot: 42.3 / 47.3 / 51.7 / 55.2 / 56.1 / 54.7 / 56.9 / 57.4
- Few-Shot: 42.3 / 47.0 / 50.7 / 55.4 / 56.4 / 57.0 / 59.5 / 60.4

**SQuADv2**
- Metric: em, Split: dev, SOTA: 90.7, K=16
- Zero-Shot: 22.6 / 32.8 / 33.9 / 43.1 / 43.6 / 45.4 / 49.0 / 52.6
- One-Shot: 25.1 / 37.5 / 37.9 / 47.9 / 47.9 / 51.1 / 56.6 / 60.1
- Few-Shot: 27.5 / 40.5 / 39.2 / 53.5 / 50.0 / 56.6 / 62.6 / 69.8

**SQuADv2** (f1)
- Metric: f1, Split: dev, SOTA: 93.0, K=16
- Zero-Shot: 28.3 / 40.2 / 41.4 / 50.3 / 51.0 / 52.7 / 56.3 / 59.5
- One-Shot: 30.1 / 43.6 / 44.1 / 54.0 / 54.1 / 57.1 / 61.8 / 65.4
- Few-Shot: 32.1 / 45.3 / 44.9 / 58.7 / 55.9 / 61.2 / 67.7 / 69.8

**CoQA**
- Metric: f1, Split: dev, SOTA: 90.7, K=5
- Zero-Shot: 34.5 / 55.0 / 64.8 / 63.5 / 71.1 / 72.8 / 78.3 / 81.5
- One-Shot: 30.5 / 52.1 / 66.6 / 66.1 / 71.8 / 75.1 / 77.9 / 84.0
- Few-Shot: [unclear: first three values in CoQA few-shot row (Small/Med/Large) read as 4.09/16.3/19.3 which seems implausibly low; may be misaligned rows in dense table] / 68.5 / 73.2 / 71.2 / 79.3 / 85.0

**DROP**
- Metric: f1, Split: dev, SOTA: 89.1, K=20
- Zero-Shot: 9.40 / 13.6 / 14.4 / 16.4 / 19.7 / 17.0 / 24.0 / 23.6
- One-Shot: 11.7 / 18.1 / 20.9 / 23.0 / 26.4 / 27.3 / 29.0 / 34.3
- Few-Shot: 12.9 / 18.7 / 24.0 / 25.6 / 26.9 / 27.9 / 32.3 / 36.5

### SuperGLUE

**BoolQ**
- Metric: acc, Split: dev, SOTA: 91.0, K=32
- Zero-Shot: 49.7 / 60.3 / 58.9 / 62.4 / 67.1 / 65.4 / 66.2 / 60.5
- One-Shot: 62.6 / 61.7 / 60.4 / 63.7 / 68.4 / 68.7 / 69.0 / 76.7
- Few-Shot: 43.1 / 60.6 / 62.6 / 64.1 / 70.3 / 70.0 / 72.5 / 76.4

**CB** (acc)
- Metric: acc, Split: dev, SOTA: 96.9, K=32
- Zero-Shot: 32.1 / 32.1 / 8.93 / 19.6 / 19.6 / 28.6 / 19.6 / 46.4
- One-Shot: 55.4 / 53.6 / 53.6 / 48.2 / 57.1 / 33.9 / 55.4 / 64.3
- Few-Shot: 42.9 / 58.9 / 53.6 / 66.9 / 67.9 / 66.1 / 68.1 / 82.1

**CB** (f1)
- Metric: f1, Split: dev, SOTA: 93.9, K=32
- Zero-Shot: 0.00 / 29.3 / 11.4 / 17.4 / 22.4 / 25.1 / 20.3 / 42.8
- One-Shot: 60.1 / 39.8 / 45.6 / 37.5 / 45.7 / 38.5 / 44.6 / 52.5
- Few-Shot: 26.1 / 40.4 / 32.6 / 46.3 / 45.7 / 44.6 / 46.0 / 57.2

**COPA**
- Metric: acc, Split: dev, SOTA: 94.8, K=32
- Zero-Shot: 66.0 / 68.0 / 73.0 / 77.0 / 76.0 / 80.0 / 84.0 / 91.0
- One-Shot: 62.0 / 64.0 / 66.0 / 71.0 / 76.0 / 82.0 / 85.0 / 87.0
- Few-Shot: 67.0 / 64.0 / 72.0 / 77.0 / 83.0 / 83.0 / 86.0 / 92.0

**RTE**
- Metric: acc, Split: dev, SOTA: 92.5, K=32
- Zero-Shot: 47.7 / 49.8 / 48.4 / 56.0 / 46.6 / 55.2 / 62.8 / 63.5
- One-Shot: 53.1 / 47.3 / 49.5 / 49.5 / 54.9 / 54.9 / 56.7 / 30.4
- Few-Shot: 52.3 / 48.4 / 46.9 / 50.9 / 56.3 / 49.5 / 46.8 / 72.9

**WiC**
- Metric: acc, Split: dev, SOTA: 76.1, K=32
- Zero-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00
- One-Shot: 50.0 / 50.3 / 50.3 / 49.2 / 49.4 / 50.3 / 50.0 / 48.6
- Few-Shot: 49.8 / 55.0 / 53.0 / 51.6 / 51.1 / 51.1 / 55.3 / 49.4

**WSC**
- Metric: acc, Split: dev, SOTA: 93.8, K=32
- Zero-Shot: 59.6 / 56.7 / 65.4 / 61.5 / 66.3 / 60.4 / 64.4 / 64.3
- One-Shot: 58.7 / 58.7 / 60.6 / 62.5 / 66.3 / 64.3 / 69.2 / 64.2
- Few-Shot: 58.7 / 60.6 / 54.8 / 60.9 / 62.5 / 67.3 / 75.0 / 75.0

**MultiRC** (acc)
- Metric: acc, Split: dev, SOTA: 62.3, K=32
- Zero-Shot: 4.72 / 9.63 / 12.3 / 13.5 / 14.3 / 18.4 / 24.2 / 27.6
- One-Shot: 4.72 / 9.65 / 12.3 / 13.6 / 14.3 / 18.4 / 24.2 / 27.6
- Few-Shot: 6.09 / 11.8 / 16.8 / 20.8 / 24.7 / 23.8 / 25.0 / 32.5

**MultiRC** (f1a)
- Metric: f1a, Split: dev, SOTA: 88.2, K=32
- Zero-Shot: 57.0 / 59.7 / 60.4 / 59.9 / 60.0 / 64.5 / 71.4 / 72.9
- One-Shot: 57.0 / 59.7 / 60.4 / 59.9 / 60.0 / 64.5 / 71.4 / 72.9
- Few-Shot: 45.0 / 59.6 / 64.2 / 65.4 / 69.6 / 64.9 / 69.3 / 74.8

**ReCoRD** (acc)
- Metric: acc, Split: dev, SOTA: 92.5, K=32
- Zero-Shot: 70.8 / 78.5 / 82.1 / 84.1 / 86.2 / 87.3 / 89.5 / 89.0 / 90.2
- One-Shot: 69.8 / 77.0 / 81.7 / 83.9 / 85.9 / 88.0 / 88.9 / 90.2
- Few-Shot: 69.8 / 77.2 / 81.1 / 83.1 / 86.0 / 87.9 / 88.9 / 90.0 / 90.1

**ReCoRD** (f1)
- Metric: f1, Split: dev, SOTA: 93.3, K=32
- Zero-Shot: 71.9 / 79.2 / 82.8 / 85.2 / 87.3 / 89.5 / 90.4 / 91.0
- One-Shot: 70.7 / 77.8 / 81.6 / 83.9 / 86.8 / 88.8 / 89.7 / 91.2
- Few-Shot: 71.9 / 77.9 / 82.1 / 84.0 / 87.5 / 88.8 / 89.8 / 90.1

**SuperGLUE** (average)
- Metric: average, Split: dev, SOTA: 89.0, K=32
- Zero-Shot: 40.6 / 47.4 / 46.8 / 49.6 / 50.1 / 52.3 / 54.5 / 58.2
- One-Shot: 54.4 / 55.1 / 56.7 / 57.8 / 61.2 / 59.7 / 64.3 / 68.9
- Few-Shot: 50.2 / 52.6 / 56.8 / 60.0 / 64.3 / 63.6 / 66.3 / 71.8

### NLI

**ANLI R1**
- Metric: acc, Split: test, SOTA: 73.8, K=50
- Zero-Shot: 33.4 / 34.2 / 33.4 / 33.4 / 34.2 / 32.4 / 32.3 / 34.6
- One-Shot: 32.1 / 31.6 / 31.9 / 34.6 / 30.6 / 31.6 / 32.7 / 32.0
- Few-Shot: 32.1 / 32.5 / 30.9 / 32.5 / 33.5 / 33.1 / 33.3 / 36.8

**ANLI R2**
- Metric: acc, Split: test, SOTA: 50.7, K=50
- Zero-Shot: 33.2 / 31.9 / 33.3 / 33.3 / 33.8 / 33.3 / 35.5 / 35.4
- One-Shot: 35.7 / 33.7 / 33.2 / 32.7 / 32.7 / 33.9 / 33.9 / 33.9
- Few-Shot: 35.7 / 33.8 / 32.1 / 41.3 / 26.6 / 33.2 / 32.6 / 34.0

**ANLI R3**
- Metric: acc, Split: test, SOTA: 48.3, K=50
- Zero-Shot: 33.6 / 34.0 / 33.8 / 33.4 / 35.3 / 34.8 / 34.4 / 34.5
- One-Shot: 35.0 / 32.6 / 33.0 / 39.3 / 34.1 / 33.1 / 33.2 / 35.3
- Few-Shot: 35.0 / 34.4 / 35.1 / 36.7 / 30.2 / 33.9 / 34.5 / 40.2

### Arithmetic

**2D+**
- Metric: acc, Split: n/a, K=50
- Zero-Shot: 0.70 / 0.65 / 0.70 / 0.85 / 1.10 / 2.54 / 15.4 / 76.9
- One-Shot: 2.00 / 0.55 / 3.15 / 4.00 / 12.1 / 19.6 / 73.0 / 99.6
- Few-Shot: 2.00 / 4.10 / 3.50 / 4.50 / 8.90 / 11.9 / 55.5 / 100.0

**2D-**
- Metric: acc, Split: n/a, K=50
- Zero-Shot: 0.70 / 1.25 / 1.25 / 1.25 / 1.60 / 7.60 / 12.6 / 58.0
- One-Shot: 1.15 / 0.95 / 1.45 / 3.95 / 8.15 / 11.5 / 44.6 / 86.4
- Few-Shot: 1.15 / 1.45 / 2.25 / 2.70 / 7.35 / 13.6 / 52.6 / 75.8

**2Dx**
- Metric: acc, Split: n/a, K=50
- Zero-Shot: 0.10 / 0.10 / 0.05 / 0.10 / 0.10 / 0.25 / 1.40 / 29.2
- One-Shot: 0.15 / 0.00 / 0.10 / 0.30 / 0.45 / 0.95 / 14.5 / 48.5
- Few-Shot: 0.15 / 0.45 / 0.30 / 0.55 / 0.75 / 5.49 / 9.80 / 49.4

**3D+**
- Metric: acc, Split: n/a, K=50
- Zero-Shot: 0.05 / 0.05 / 0.05 / 0.05 / 0.05 / 0.45 / 1.35 / 48.3
- One-Shot: 0.05 / 0.15 / 0.25 / 0.30 / 0.55 / 1.60 / 5.18 / 75.8
- Few-Shot: 0.05 / 0.10 / 0.15 / 0.05 / 0.65 / 1.05 / 9.20 / 100.0

**3D-**
- Metric: acc, Split: n/a, K=50
- Zero-Shot: 0.05 / 0.05 / 0.00 / 0.05 / 0.05 / 0.05 / 0.15 / 4.00
- One-Shot: 0.00 / 0.05 / 0.10 / 0.00 / 0.00 / 0.10 / 0.80 / 14.0
- Few-Shot: 0.00 / 0.05 / 0.05 / 0.05 / 0.05 / 0.15 / 0.40 / 25.5

**4D+**
- Metric: acc, Split: n/a, K=50
- Zero-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.10 / 7.50
- One-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.05 / 0.50 / 14.0
- Few-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.05 / 0.40 / 26.8

**4D-**
- Metric: acc, Split: n/a, K=50
- Zero-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.65
- One-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.05 / 0.05 / 3.45
- Few-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.05 / 5.30

**5D+**
- Metric: acc, Split: n/a, K=50
- Zero-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.80
- One-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 3.75
- Few-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.90

**5D-**
- Metric: acc, Split: n/a, K=50
- Zero-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.80
- One-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.05 / 3.75
- Few-Shot: 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.00 / 0.90

**1DC** (Single Digit Composite)
- Metric: acc, Split: n/a, K=50
- Zero-Shot: 2.20 / 2.25 / 2.65 / 2.10 / 2.55 / 3.80 / 6.15 / 19.8
- One-Shot: 1.55 / 2.35 / 3.35 / 2.35 / 4.75 / 9.15 / 11.0 / 27.3
- Few-Shot: 1.35 / 2.90 / 2.70 / 2.85 / 4.25 / 6.10 / 17.05 / 29.2

### Word Scrambling and Manipulation Tasks

**Cycled Letters**
- Metric: acc, Split: n/a, K=100
- Zero-Shot: 0.62 / 0.71 / 2.85 / 0.00 / 0.63 / 1.35 / 2.58 / 6.06
- One-Shot: 1.67 / 4.36 / 5.68 / 6.46 / 6.25 / 9.41 / 15.1 / 21.7
- Few-Shot: 4.69 / 9.27 / 10.7 / 14.5 / 16.7 / 21.9 / 27.7 / 37.9

**Anagrams 1**
- Metric: acc, Split: n/a, K=100
- Zero-Shot: 0.10 / 0.14 / 0.40 / 0.00 / 0.27 / 0.69 / 1.16 / 2.28
- One-Shot: 0.21 / 0.61 / 1.12 / 1.27 / 1.60 / 2.72 / 3.72 / 8.62
- Few-Shot: 0.50 / 1.27 / 2.13 / 3.05 / 1.81 / 5.49 / 8.38 / 18.15

**Anagrams 2**
- Metric: acc, Split: n/a, K=100
- Zero-Shot: 0.81 / 1.21 / 2.69 / 0.01 / 1.71 / 3.75 / 4.53 / 8.91
- One-Shot: 1.19 / 2.62 / 4.70 / 4.77 / 6.97 / 10.2 / 14.6 / 25.9
- Few-Shot: 1.94 / 4.80 / 7.59 / 9.87 / 12.6 / 18.9 / 25.6 / 39.7

**Symbol Insertion**
- Metric: acc, Split: n/a, K=100
- Zero-Shot: 0.00 / 0.00 / 0.10 / 0.00 / 0.05 / 0.42 / 0.89 / 8.26
- One-Shot: 0.03 / 0.05 / 0.57 / 1.18 / 1.67 / 3.46 / 6.62 / 45.4
- Few-Shot: 0.11 / 0.28 / 2.19 / 4.18 / 6.61 / 11.0 / 27.3 / 67.2

**Reversed Words**
- Metric: acc, Split: n/a, K=100
- Zero-Shot: 0.00 / 0.01 / 0.01 / 0.01 / 0.02 / 0.03 / 0.03 / 0.09
- One-Shot: 0.02 / 0.01 / 0.01 / 0.00 / 0.05 / 0.07 / 0.11 / 0.48
- Few-Shot: 0.00 / 0.05 / 0.00 / 0.17 / 0.24 / 0.30 / 0.42 / 0.44

### SAT Analogies

**SAT Analogies**
- Metric: acc, Split: n/a, K=20
- Zero-Shot: 35.6 / 39.0 / 45.2 / 44.1 / 50.0 / 49.2 / 52.7 / 53.7
- One-Shot: 30.5 / 41.2 / 43.1 / 46.5 / 55.1 / 54.3 / 53.5 / 59.1
- Few-Shot: 30.5 / 40.4 / 42.8 / 40.6 / 48.4 / 51.9 / 53.5 / 65.2

---

## Figures

### Figure H.1

**Figure H.1** (p. 64): "All results for all SuperGLUE tasks."

The figure contains 10 sub-plots arranged in a 4x3 grid (with 2 positions empty), one for each SuperGLUE task: BoolQ, CB (accuracy), CB (F1), COPA, RTE, WiC, WSC, MultiRC (accuracy), MultiRC (F1a), ReCoRD (accuracy), and ReCoRD (F1a). Each sub-plot shows accuracy (y-axis) vs. parameters in LM (billions) on the x-axis, with three lines for Zero-Shot (blue), One-Shot (orange), and Few-Shot (K=32, green). Reference lines mark Fine-tune SOTA, BERT Large, and Random Guessing levels where applicable.

Key trends visible:
- BoolQ: Few-shot overtakes zero-shot at large scales, reaching ~76% for 175B
- CB accuracy: Volatile at small scales, few-shot reaches ~82% at 175B
- CB F1: Similar volatility, few-shot reaches ~57% at 175B
- COPA: Steady increase, few-shot reaches ~92% at 175B, near fine-tune SOTA
- RTE: Erratic at smaller scales, few-shot jumps to ~73% at 175B
- WiC: Zero-shot stays at 0% across all sizes; one-shot and few-shot hover near 50% (chance level)
- WSC: Gradual increase, few-shot reaches ~75% at 175B
- MultiRC accuracy: Gradual increase, few-shot reaches ~33% at 175B
- MultiRC F1a: Gradual increase, few-shot reaches ~75% at 175B
- ReCoRD accuracy: Strong performance, few-shot reaches ~90% at 175B
- ReCoRD F1a: Strong performance, few-shot reaches ~90% at 175B

### Figure H.2

**Figure H.2** (p. 64): "Results for SAT task."

The figure shows a single plot with accuracy (y-axis) vs. parameters in LM (billions) on the x-axis. Three lines are shown: Zero-Shot, One-Shot, and Few-Shot (K=26). Reference lines for Human and Random Guessing are included. Performance increases steadily with scale. Few-shot reaches approximately 65% at 175B, while Human performance is around 57% and Random Guessing is ~20%.

### Figure H.3

**Figure H.3** (p. 64): "All results for all Winograd tasks."

The figure contains 3 sub-plots: SAT Analogies, Winogrande, and Winograd. Each shows accuracy vs. parameters with Zero-Shot, One-Shot, and Few-Shot lines.
- Winogrande: Steady increase, few-shot (K=56) reaches ~77% at 175B. Fine-tuned SOTA and Human reference lines shown. Fine-tuned RoBERTa-Large also marked.
- Winograd: All three settings converge to ~88-89% at 175B with few-shot (K=7). Fine-tune SOTA reference line at ~94%.

### Figure H.4

**Figure H.4** (p. 65): "All results for all Arithmetic tasks."

The figure contains 11 sub-plots in a 4x3 grid arrangement:
1. **Arithmetic (few-shot)** overview: Shows all arithmetic task types on one plot (Two Digit Addition, Two Digit Subtraction, Three Digit Addition, Three Digit Subtraction, Four Digit Addition, Four Digit Subtraction, Five Digit Addition, Five Digit Subtraction, Two Digit Multiplication, Single Digit Three Ops). Accuracy vs. parameters. Two-digit tasks perform best, reaching near 100% at 175B. Five-digit tasks remain near 0%.
2. **Two Digit Addition**: Three lines (Zero/One/Few-Shot K=100). Few-shot reaches ~100% at 175B.
3. **Two Digit Multiplication**: Three lines (Zero/One/Few-Shot K=100). Few-shot reaches ~30% at 175B.
4. **Two Digit Subtraction**: Three lines. Few-shot reaches ~80-90% at 175B.
5. **Three Digit Addition**: Three lines (K=100). Few-shot reaches ~100% at 175B.
6. **Three Digit Subtraction**: Three lines (K=100). Few-shot reaches ~50% at 175B.
7. **Four Digit Addition**: Three lines (K=50). Few-shot reaches ~25% at 175B.
8. **Four Digit Subtraction**: Three lines (K=50). Few-shot reaches ~15% at 175B.
9. **Five Digit Addition**: Three lines (K=50). Performance near 0% across all sizes, slight uptick at 175B to ~5-8%.
10. **Five Digit Subtraction**: Three lines (K=100). Performance near 0%, slight increase at 175B to ~5-10%.
11. **Single Digit Three Ops**: Three lines (K=100). Few-shot reaches ~20% at 175B.

### Figure H.5

**Figure H.5** (p. 65): "All results for all Cloze and Completion tasks."

The figure contains 3 sub-plots: HellaSwag, LAMBADA, and StoryCloze. Each shows accuracy vs. parameters with Zero-Shot, One-Shot, and Few-Shot lines plus reference levels.
- **HellaSwag**: Steady increase. Few-shot (K=20) reaches ~79% at 175B. Fine-tune SOTA at ~86%, Human at ~95%, Fine-tuned BERT-Large at ~50%, Random Guessing at ~25%.
- **LAMBADA**: Steep increase. Few-shot (K=15) reaches ~86% at 175B. Human at ~95%, Zero-Shot SOTA at ~70%.
- **StoryCloze**: Steady increase. Few-shot (K=70) reaches ~88% at 175B. Fine-tuned SOTA at ~92%.

### Figure H.6

**Figure H.6** (p. 66): "All results for all Common Sense Reasoning tasks."

The figure contains 3 sub-plots: PhysicalQA (PIQA), ARC Challenge, and OpenBookQA. Each shows accuracy vs. parameters with Zero-Shot, One-Shot, and Few-Shot lines.
- **PhysicalQA**: Steady increase. Few-shot (K=50) reaches ~82% at 175B. Fine-tuned SOTA at ~84%, Human at ~95%, Random Guessing at ~50%.
- **ARC Challenge**: Steady increase. Few-shot (K=50) reaches ~51% at 175B. Fine-tuned SOTA at ~80%.
- **OpenBookQA**: Moderate increase. Few-shot (K=100) reaches ~65% at 175B. Fine-tuned SOTA at ~87%.

### Figure H.7

**Figure H.7** (p. 66): "All results for all QA tasks."

The figure contains 3 sub-plots: NaturalQuestions (T5 splits), TriviaQA, and WebQS. Each shows accuracy vs. parameters.
- **NaturalQuestions**: Steady increase. Few-shot (K=64) reaches ~30% at 175B. Fine-tuned SOTA at ~44%.
- **TriviaQA**: Strong increase. Few-shot (K=64) reaches ~71% at 175B. Fine-tuned SOTA at ~68%.
- **WebQS**: Moderate increase. Few-shot (K=64) reaches ~42% at 175B.

### Figure H.8

**Figure H.8** (p. 66): "All results for all Reading Comprehension tasks."

The figure contains 6 sub-plots: QuAC, RACE-h, RACE-m, SQuADv2, CoQA, and DROP. Each shows accuracy/F1 vs. parameters.
- **QuAC**: Moderate increase. Few-shot (K=5) reaches ~44% F1 at 175B. Fine-tuned SOTA at ~74%.
- **RACE-h**: Slight increase. Few-shot (K=10) reaches ~46% at 175B. Fine-tuned SOTA at ~90%.
- **RACE-m**: Moderate increase. Few-shot (K=10) reaches ~58% at 175B. Fine-tuned SOTA at ~93%.
- **SQuADv2**: Strong increase. Few-shot (K=10) reaches ~70% EM at 175B. Fine-tuned SOTA at ~90%, Human at ~87%.
- **CoQA**: Strong increase. Few-shot (K=5) reaches ~85% F1 at 175B. Fine-tuned SOTA at ~91%.
- **DROP**: Moderate increase. Few-shot (K=20) reaches ~37% F1 at 175B. Fine-tuned SOTA at ~89%.

### Figure H.9

**Figure H.9** (p. 66): "All results for all ANLI rounds."

The figure contains 3 sub-plots: ANLI Round1, ANLI Round2, and ANLI Round3. Each shows accuracy vs. parameters.
- **ANLI Round1**: Mostly flat performance across all scales. Few-shot (K=90) hovers around 33-37% at 175B. Fine-tuned SOTA (Fine-tuned 888M/T5-Large) at ~73%. Fine-tuned BERT-Large at ~60%. Random Guessing at ~33%.
- **ANLI Round2**: Mostly flat. Few-shot (K=80) hovers around 33-35% at 175B. Fine-tuned SOTA at ~50%. Fine-tuned RoBERTa-Large shown. Random Guessing at ~33%.
- **ANLI Round3**: Mostly flat. Few-shot (K=80) hovers around 33-40% at 175B. Fine-tuned SOTA at ~48%. Fine-tuned RoBERTa/BERT-Large shown. Random Guessing at ~33%.

All three ANLI rounds show performance hovering near the 33% random-chance baseline across all model sizes and evaluation settings (zero-shot, one-shot, and few-shot).

### Figure H.10

**Figure H.10** (p. 67): "All results for all Scramble tasks."

The figure contains 6 sub-plots arranged in a 2x3 grid:

- **cycle letters**: Accuracy vs. parameters. Three lines: Zero-Shot, One-Shot, and Few-Shot (K=100). Performance increases with scale. Few-shot reaches ~37% at 175B. One-shot reaches ~22% at 175B. Zero-shot reaches ~6% at 175B.
- **Wordscramble (few-shot)**: A single plot showing all scramble task variants in few-shot setting: cycle letters, mid word 1 anagrams, mid word 2 anagrams, random insertion, reversed words. Cycle letters and mid word 2 anagrams perform best; random insertion shows the steepest climb at large scales (~67% at 175B); reversed words remains near 0% across all scales.
- **mid word 1 anagrams**: Three lines (Zero-Shot, One-Shot, Few-Shot K=100). Performance increases modestly. Few-shot reaches ~14% at 175B.
- **mid word 2 anagrams**: Three lines (Zero-Shot, One-Shot, Few-Shot K=100). Performance increases. Few-shot reaches ~40% at 175B.
- **random insertion**: Three lines (Zero-Shot, One-Shot, Few-Shot K=100). Strong scaling. Few-shot reaches ~67% at 175B. One-shot reaches ~45% at 175B.
- **reversed words**: Three lines (Zero-Shot, One-Shot, Few-Shot K=100). Performance remains near 0% across all model sizes, with the largest model reaching only ~0.4-0.5% accuracy.

### Figure H.11

**Figure H.11** (p. 67): "All results for all Translation tasks."

The figure contains 12 sub-plots arranged in a 4x3 grid, showing translation performance for six language pairs across two metrics (SacreBLEU and Multi-BLEU). Each sub-plot shows accuracy (BLEU score, y-axis) vs. parameters in LM (billions, x-axis) with three lines: Zero-Shot, One-Shot, and Few-Shot (K=64).

**SacreBLEU sub-plots (top two rows):**
- **German -> English (SacreBLEU)**: Few-shot reaches ~40% at 175B. Zero-shot shows a jump at medium scales (~22% at 2.7B) then plateaus.
- **English -> German (SacreBLEU)**: Few-shot reaches ~30% at 175B. Zero-shot shows a jump at 2.7B (~14%) then climbs to ~25% at 175B.
- **English -> French (SacreBLEU)**: Few-shot reaches ~40% at 175B. Zero-shot jumps at 2.7B (~19%) then climbs to ~31%.
- **French -> English (SacreBLEU)**: Few-shot reaches ~41% at 175B. Zero-shot jumps at 2.7B (~22%) then plateaus.
- **English -> Romanian (SacreBLEU)**: Few-shot reaches ~26% at 175B. One-shot reaches ~28% at 175B.
- **Romanian -> English (SacreBLEU)**: Few-shot reaches ~41% at 175B. One-shot reaches ~40%.

**Multi-BLEU sub-plots (bottom two rows):**
- **German -> English (Multi-BLEU)**: Few-shot reaches ~37% at 175B.
- **English -> German (Multi-BLEU)**: Few-shot reaches ~30% at 175B.
- **English -> French (Multi-BLEU)**: Few-shot reaches ~34% at 175B.
- **French -> English (Multi-BLEU)**: Few-shot reaches ~39% at 175B.
- **English -> Romanian (Multi-BLEU)**: Few-shot reaches ~21% at 175B.
- **Romanian -> English (Multi-BLEU)**: Few-shot reaches ~40% at 175B.

All translation sub-plots show consistent patterns: zero-shot performance often exhibits a notable jump at medium model sizes (around 2.7B parameters), particularly for X->English directions; few-shot and one-shot consistently outperform zero-shot; and performance scales smoothly with model size in the few-shot and one-shot settings.
