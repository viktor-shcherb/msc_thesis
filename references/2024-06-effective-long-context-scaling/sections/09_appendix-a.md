# A More Results [p. 17–18]

## Comparison with Open-Source Long-Context Models (32k Prompt Length) [p. 17]

**Table 13** (p. 17): Comparison of our models with open-source long-context models on research benchmarks *using a maximum prompt length of 32,768 tokens*.

| Model | Prompt length | NarrativeQA F1 (0-shot) | Qasper F1 (2-shot) | QuALITY EM (2-shot) | QMSum ROUGE-geo* (1-shot) |
|---|---|---|---|---|---|
| Yarn-7B-128k | 16k | 20.9 | 26.2 | 32.3 | 11.4 |
| Together-7B-32k | 16k | 23.3 | 27.3 | 41.2 | 12.6 |
| Yarn-13B-128k | 16k | 23.4 | 27.1 | 46.4 | 11.9 |
| Yarn-7B-128k | 32k | 24.0 | 26.2 | 30.4 | 13.6 |
| Together-7B-32k | 32k | 24.7 | 27.3 | 41.3 | 14.2 |
| Yarn-13B-128k | 32k | 25.5 | 27.1 | 48.0 | 13.8 |
| LLAMA 2 LONG 7B | 16k | 21.9 | 27.8 | 43.2 | 14.9 |
| LLAMA 2 LONG 13B | 16k | 25.6 | 31.2 | 57.6 | 15.7 |
| LLAMA 2 LONG 7B | 32k | 24.4 | 28.7 | 43.6 | 15.9 |
| LLAMA 2 LONG 13B | 32k | **27.4** | **31.6** | **59.0** | **17.0** |

## Decomposed MMLU Results [p. 17]

**Table 14** (p. 17): Decomposed MMLU results.

| Model | Humanities | STEM | Social Sciences | Other |
|---|---|---|---|---|
| LLAMA 2 LONG 7B | 54.8 | 35.7 | 58.4 | 53.2 |
| LLAMA 2 LONG 13B | 69.0 | 44.4 | 71.3 | 65.8 |
| LLAMA 2 LONG 34B | 73.5 | 49.9 | 78.4 | 69.3 |
| LLAMA 2 LONG 70B | 80.1 | 55.5 | 84.4 | 74.9 |

## Coding, Math, and QA Results [p. 17]

**Table 15** (p. 17): Results on HumanEval (0-shot), MBPP (3-shot), MATH (4-shot), GSM8K (8-shot), NaturalQuestions (5-shot) and TriviaQA-wiki (5-shot).

| Model | HumanEval | MBPP | MATH | GSM8K | NQ | TQA |
|---|---|---|---|---|---|---|
| LLAMA 2 LONG 7B | 18.3 | 23.0 | 4.22 | 16.8 | 27.5 | 74.4 |
| LLAMA 2 LONG 13B | 19.5 | 31.8 | 8.38 | 34.6 | 32.5 | 81.1 |
| LLAMA 2 LONG 34B | 22.6 | 37.2 | 10.6 | 47.4 | 35.0 | 85.6 |
| LLAMA 2 LONG 70B | 32.9 | 46.8 | 17.2 | 65.4 | 39.8 | 88.2 |

## Commonsense Reasoning Decomposed Results [p. 17]

**Table 16** (p. 17): Commonsense reasoning decomposed results. We use the same number of shots and evaluation metrics for all tasks as LLAMA 2.

| Model | PIQA | SIQA | HellaSwag | WinoGrande | ARC-e | ARC-c | OBQA | CSQA |
|---|---|---|---|---|---|---|---|---|
| LLAMA 2 LONG 7B | 78.9 | 48.7 | 77.8 | 70.4 | 76.2 | 52.0 | 59.0 | 61.0 |
| LLAMA 2 LONG 13B | 81.6 | 50.7 | 81.2 | 74.1 | 77.7 | 51.4 | 55.6 | 70.4 |
| LLAMA 2 LONG 34B | 82.6 | 51.7 | 83.8 | 77.5 | 79.7 | 54.8 | 60.2 | 77.0 |
| LLAMA 2 LONG 70B | 83.3 | 52.8 | 85.7 | 79.6 | 80.3 | 58.4 | 59.6 | 81.9 |

## Additional Long-Context Tasks from L-Eval [p. 18]

**Table 17** (p. 18): Evaluation on additional long-context tasks from L-Eval. We report the official metrics defined in An et al. (2023) and the results of compared models are directly taken from the paper.

| Model | Coursera | TPO | TopicRetrieval | FinQA | ContractQA | NaturalQuestions |
|---|---|---|---|---|---|---|
| Claude 1.3 100k | 60.2 | 83.6 | 70.6 | - | - | - |
| gpt-3.5-turbo-16k | 59.7 | 69.9 | 69.3 | 45.4 | 24.9 | 45.9 |
| *Best open models reported in An et al. (2023)* | | | | | | |
| longchat-13b-16k | 36.8 | 55.4 | 33.3 | 37.9 | 21.1 | 22.8 |
| chatglm2-6b-8k | 47.2 | 54.6 | 10.0 | 34.8 | 16.4 | 17.6 |
| LLAMA 2 LONG CHAT | 52.9 | **81.8** | **76.0** | **47.3** | **25.5** | **66.7** |

[p. 18] LLAMA 2 LONG CHAT underlines are bold in the original, indicating best results on TPO, TopicRetrieval, FinQA, ContractQA, and NaturalQuestions among the models compared. Claude 1.3 100k achieves the highest Coursera score (60.2).

## Data Mix Ablation on Retrieval Task [p. 18]

**Figure 7** (p. 18): "FIRST-SENTENCE-RETRIEVAL performance of models trained with different data mixes."

The figure shows ROUGE-L (y-axis, 0 to 100) vs. Task length (x-axis: 256, 1k, 2k, 4k, 8k, 10k, 12k, 14k, 16k, 20k, 24k, 28k, 30k). Four lines are plotted:
- **Llama-2 data mix** (blue): maintains near-100 ROUGE-L across all task lengths up to 30k
- **Llama-2 data mix: remove long text data** (orange/red): maintains near-100 across most lengths but drops sharply around 28k-30k to approximately 60-70
- **Llama-2 data mix: upsample long text data** (green): maintains near-100 across all task lengths, nearly identical to the blue line
- **Llama-2-Long data mix** (red/dark): maintains near-100 across all task lengths up to 30k

All four data mix variants perform similarly well on the FIRST-SENTENCE-RETRIEVAL task across most lengths, with only the "remove long text data" variant showing degradation at the longest lengths.
