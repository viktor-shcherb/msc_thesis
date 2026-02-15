# Results [p. 6-8]

## Evaluation setup summary [p. 6]

The paper reports internal re-evaluations (same harness/configuration) and compares against similar-scale open-weight families (Qwen 3, Gemma 3).

Benchmarks listed include:

- General: MMLU, MMLU-Redux, ARC-Challenge, RACE High, TriviaQA, NaturalQS, AGIEval
- Math/Code: MATH, GPQA Diamond, MBPP
- Multimodal: MMMU, MathVista
- Post-training: Arena Hard, WildBench, MM MTBench, AIME 2024/2025, HMMT 2025, PhyBench, LiveCodeBench [p. 6]

## 4.1 Pretraining results [p. 6-7]

### Table 2 [p. 7]

**Table 2:** "Comparing Ministral 3 Base models against the Gemma 3 base models and the Qwen 3 base models on pretraining benchmarks."

| Model | MMLU-Redux (5-shot) | TriviaQA (5-shot) | MATH (CoT 2-shot) | AGIEval (5-shot) | Multilingual MMLU (5-shot) |
|---|---:|---:|---:|---:|---:|
| Qwen 3 14B | 83.7 | 70.3 | 62.0 | 66.1 | 75.4 |
| Ministral 3 14B | 82.0 | 74.9 | 67.6 | 64.8 | 74.2 |
| Gemma 3 12B | 76.6 | 78.8 | 48.7 | 58.7 | 69.0 |
| Qwen 3 8B | 79.4 | 63.9 | 57.6 | 59.6 | 70.0 |
| Ministral 3 8B | 79.3 | 68.1 | 62.6 | 59.1 | 70.6 |
| Gemma 3 4B | 62.6 | 64.0 | 29.4 | 43.0 | 51.6 |
| Qwen 3 4B | 75.9 | 53.0 | 40.5 | 57.0 | 67.7 |
| Ministral 3 3B | 73.5 | 59.2 | 60.1 | 51.1 | 65.2 |

### Table 3 [p. 7]

**Table 3:** Ministral 3 Base family vs teacher Mistral Small 3.1 24B.

| Evaluation | Mistral Small 24B | Ministral 3 14B | Ministral 3 8B | Ministral 3 3B |
|---|---:|---:|---:|---:|
| **General** | | | | |
| MMLU (5-shot) | 81.0 | 79.4 | 76.1 | 70.7 |
| MMLU-Redux (5-shot) | 82.7 | 82.0 | 79.3 | 73.5 |
| ARC-Challenge | 91.6 | 89.9 | 88.0 | 85.5 |
| RACE High | 52.1 | 52.3 | 49.7 | 49.3 |
| TriviaQA (5-shot) | 79.3 | 74.9 | 68.1 | 59.2 |
| NaturalQS (5-shot) | 34.4 | 29.9 | 25.8 | 21.9 |
| **Math & Code** | | | | |
| MATH (CoT 2-shot) | 55.8 | 67.6 | 62.6 | 60.1 |
| GPQA Diamond (0-shot) | 36.9 | 39.9 | 39.9 | 33.8 |
| MBPP (3-shot pass@1) | 71.6 | 71.6 | 70.0 | 63.0 |
| **Multilingual MMLU** | | | | |
| European avg. (5-shot) | 78.8 | 76.9 | 73.4 | 68.4 |
| Chinese (5-shot) | 75.7 | 75.1 | 71.3 | 64.1 |
| Japanese (5-shot) | 76.7 | 75.9 | 72.2 | 65.7 |
| Korean (5-shot) | 59.3 | 59.0 | 55.3 | 48.9 |
| **Multimodal** | | | | |
| MMMU (2-shot) | 59.1 | 59.9 | 55.1 | 52.4 |
| MathVista | 51.3 | 43.6 | 35.7 | 23.3 |

Key observations stated by authors [p. 6-7]:

- 14B: stronger on TriviaQA and MATH than Qwen 3 14B, competitive elsewhere.
- 8B: similar pattern; often better than larger Gemma 12B, except TriviaQA.
- 3B: same broad trend with larger gap sensitivity at smaller scale.

## 4.2 Post-training results [p. 7-8]

### Table 4 [p. 8]

**Table 4:** Ministral 3 instruct vs Qwen 3 / Gemma 3 instruct baselines.

| Model | Arena Hard | WildBench | MATH (maj@1) | MM MTBench |
|---|---:|---:|---:|---:|
| Qwen3 14B (Non-Thinking) | 42.7 | 65.1 | 87.00 | N/A |
| Ministral 3 14B | 55.1 | 68.5 | 90.40 | 84.90 |
| Gemma3-12B-Instruct | 43.6 | 63.2 | 85.40 | 67.00 |
| Qwen3-VL-8B-Instruct | 52.8 | 66.3 | 94.60 | 80.00 |
| Ministral 3 8B | 50.9 | 66.8 | 87.60 | 80.80 |
| Gemma3-4B-Instruct | 31.8 | 49.1 | 75.90 | 52.30 |
| Qwen3-VL-4B-Instruct | 43.8 | 56.8 | 90.00 | 80.08 |
| Ministral 3 3B | 30.5 | 56.8 | 83.00 | 78.30 |
| Qwen3-VL-2B-Instruct | 16.3 | 42.2 | 78.60 | 63.60 |

### Table 5 [p. 8]

**Table 5:** Ministral 3 reasoning vs size-matched Qwen 3 reasoning baselines.

| Benchmark | Qwen 3 14B | Ministral 3 14B | Qwen3-VL 8B | Ministral 3 8B | Qwen3-VL 4B | Ministral 3 3B |
|---|---:|---:|---:|---:|---:|---:|
| AIME 2024 | 83.7 | 89.8 | 86.0 | 86.0 | 72.9 | 77.5 |
| AIME 2025 | 73.7 | 85.0 | 79.8 | 78.7 | 69.7 | 72.1 |
| HMMT 2025 | 55.8 | 67.5 | 57.5 | 55.8 | 50.8 | 51.7 |
| GPQA Diamond | 66.3 | 71.2 | 67.1 | 66.8 | 60.1 | 53.4 |
| PhyBench | 22.0 | 26.0 | 22.0 | 20.0 | 9.0 | 15.0 |
| LiveCodeBench v6 | 59.3 | 64.6 | 58.0 | 61.6 | 51.3 | 54.8 |

The paper reports pass@16 for reasoning benchmarks, except LiveCodeBench (pass@5) [p. 8].
