# Instruction-tuned Model [p. 12–16]

[p. 12] To critically evaluate instruction-tuned models, the authors implement a multifaceted approach. Assessments of foundational skills and human preferences are conducted using open datasets and benchmarks. Detailed in-house examinations further probe model competencies in key areas. A particular focus is placed on assessing long context capability. Safety measures include multilingual safety assessments and red teaming exercises.

## Open Benchmark Evaluation [p. 12–13]

[p. 12] To comprehensively evaluate the quality of instruction-tuned models, the authors compile automatic and human evaluation to assess the capabilities and human preference. For the evaluation of basic capabilities, similar datasets as in the pre-trained model evaluation are applied, targeting natural language understanding, coding, mathematics, and reasoning. Specifically, they evaluate on MMLU, MMLU-Pro, GPQA, and Theorem QA for language understanding and knowledge, HumanEval, MBPP, MultiPL-E, and LiveCodeBench v1 (Jain et al., 2024) for coding, GSM8K and MATH for mathematics. Additionally, human preference alignment and instruction following are assessed by evaluating on benchmarks including MT-Bench (Zheng et al., 2023), Arena-Hard (Li et al., 2024), AlignBench (Liu et al., 2023b), MixEval (Ni et al., 2024) whose results approximate those of Chatbot Arena, and IFEval (Zhou et al., 2023)^4 for instruction following.

^4 For simplicity, the authors report the results of the subset *strict-prompt*.

### Qwen2-72B-Instruct [p. 12–13]

[p. 12] Qwen2-72B-Instruct is compared against instruction-tuned models including Mixtral-8x22B-Instruct, Llama-3-70B-Instruct, as well as Qwen1.5-72B-Chat. The results are presented in Table 6. A strong base language model can help boost the downstream performance of the instruction-tuned model. Specifically, Qwen2-72B-Instruct outshines its peers in areas such as language understanding, coding, and mathematics, with the exception of GPQA and MBPP. Regarding human preference alignment and instruction following, Qwen2-72B has significant advantages over the baselines. The authors assume this achievement is attributed to both the high-quality pre-trained model and improvements in both data and training techniques for post-training.

**Table 6: Performance of 70B+ instruction-tuned models.** [p. 13] We compare Qwen2-72B-Instruct with Mixtral-8x22B-Instruct, Llama-3-70B-Instruct, Qwen1.5-72B-Chat, and Qwen1.5-110B-Chat. "-Instruct" or "-Chat" is omitted in the table. Qwen2-72B-Instruct demonstrates advantages in core capabilities, and superior performance in human preference alignment.

| Datasets | Mixtral-8x22B | Llama-3-70B | Qwen1.5-72B | Qwen1.5-110B | Qwen2-72B |
|---|---|---|---|---|---|
| | *English* | | | | |
| MMLU | 74.0 | 82.0 | 75.6 | 76.5 | **82.3** |
| MMLU-Pro | 56.1 | 56.2 | 51.7 | 50.5 | **64.4** |
| GPQA | **49.7** | 41.9 | 39.4 | 32.8 | 42.4 |
| Theorem QA | 40.8 | 42.5 | 28.8 | 18.8 | **44.4** |
| | *Coding* | | | | |
| HumanEval | 73.8 | 81.7 | 71.3 | 74.4 | **86.0** |
| MBPP | 75.9 | **82.3** | 71.9 | 76.4 | 80.2 |
| MultiPL-E | 61.1 | 63.4 | 48.1 | 55.4 | **69.2** |
| LiveCodeBench *v1* | 21.8 | 29.3 | 17.9 | 25.3 | **35.7** |
| | *Mathematics* | | | | |
| GSM8K | 89.1 | 93.0 | 82.7 | 84.5 | **93.2** |
| MATH | 47.4 | 50.4 | 42.5 | 42.0 | **69.0** |
| | *Alignment* | | | | |
| MT-Bench | 8.66 | 8.95 | 8.61 | 8.88 | **9.12** |
| MixEval | 82.3 | 84.0 | 84.1 | 85.7 | **86.7** |
| Arena-Hard | 36.4 | 41.1 | 36.1 | 39.8 | **48.1** |
| IFEval *strict-prompt* | 67.1 | 77.3 | 55.8 | 57.5 | **77.6** |
| AlignBench | - | 7.42 | 7.28 | 7.87 | **8.27** |

### Qwen2-57B-A14B-Instruct [p. 13–14]

[p. 13] For medium-size models, Qwen2-57B-A14B-Instruct is compared with Mixtral-8x7B-Instruct, another MoE baseline, as well as dense SOTA models with over 30 billion parameters, e.g., Yi-1.5-34B-Chat and Qwen1.5-32B-Chat. The results are provided in Table 7. Compared with Qwen1.5-32B-Chat, Qwen2-57B-A14B-Instruct reaches superior performance in almost all benchmarks, and compared with the 30B SOTA model Yi-1.5-34B-Chat, Qwen2-57B-A14B-Instruct has gained advantages in most evaluations except for those for mathematics. In terms of the evaluation for alignment, the advantages of Qwen2-57B-A14B-Instruct are notably evident.

**Table 7: Performance of 30B+ dense and 40B+ MoE instruction-tuned models.** [p. 14] We compare Qwen2-57B-A14B-Instruct with the similar-size MoE model Mixtral-8x7B-Instruct, 30B dense models such as Yi-1.5-34B-Chat and Qwen1.5-32B-Chat. "-Instruct" or "-Chat" is omitted in the table. Qwen2-57B-A14B-Instruct is competitive with the recent SOTA 30B dense models, and significantly outcompetes the MoE baseline.

| Datasets | Mixtral-8x7B | Yi-1.5-34B | Qwen1.5-32B | Qwen2-57B-A14B |
|---|---|---|---|---|
| Architecture | MoE | Dense | Dense | MoE |
| # Act Params | 12B | 32B | 34B | 14B |
| # Params | 47B | 32B | 32B | 57B |
| | *English* | | | |
| MMLU | 71.4 | **76.8** | 74.8 | 75.4 |
| MMLU-Pro | 43.3 | 52.3 | 46.4 | **52.8** |
| GPQA | - | - | 30.8 | **34.3** |
| Theorem QA | - | - | 30.9 | **33.1** |
| | *Coding* | | | |
| HumanEval | 45.1 | 75.2 | 68.3 | **79.9** |
| MBPP | 59.5 | **74.6** | 67.9 | 70.9 |
| MultiPL-E | - | - | 50.7 | **66.4** |
| LiveCodeBench *v1* | 12.3 | - | 15.2 | **25.5** |
| | *Mathematics* | | | |
| GSM8K | 65.7 | **90.2** | 83.6 | 85.3 |
| MATH | 30.7 | **50.1** | 42.4 | 49.1 |
| | *Alignment* | | | |
| MT-Bench | 8.30 | 8.50 | 8.30 | **8.55** |
| MixEval | 70.0 | 81.7 | 81.0 | **82.3** |
| IFEval *strict-prompt* | - | - | 50.3 | **59.9** |
| AlignBench | 5.70 | 7.20 | 7.19 | **7.36** |

### Qwen2-7B-Instruct [p. 13, 15]

[p. 13] Within the spectrum of 7B to 9B models, Qwen2-7B-Instruct is compared with Llama-3-8B-Instruct, Yi-1.5-9B-Chat, GLM-4-9B-Chat, and Qwen1.5-7B-Chat. The results can be found in Table 8. Qwen2-7B-Instruct demonstrates substantial advancements compared to its predecessor, Qwen1.5-7B-Chat, across comprehensive evaluations, notably achieving higher scores in coding and mathematics-related tasks. Compared with the recent SOTA model, Llama-3-8B-Instruct, Qwen2-7B-Instruct demonstrates competitive performance and specifically it achieves superior performance in coding. Nonetheless, in terms of instruction following, Qwen2-7B-Instruct greatly falls behind the competitor. To address this limitation, the authors plan to augment the 7B model's instruction-following ability by enhancing the quality of post-training data, ensuring a more robust understanding and execution of complex commands.

**Table 8: Performance of 7B+ instruction-tuned models.** [p. 15] We compare Qwen2-7B-Instruct with the recent SOTA models with 7-9 billion parameters, including Llama-3-8B-Instruct, Yi-1.5-9B-Chat, GLM-4-9B-Chat, and Qwen1.5-7B-Chat. "-Instruct" or "-Chat" is omitted in the table. Qwen2-7B-Instruct demonstrates competitive performance against Llama-3-8B-Instruct.

| Datasets | Llama-3-8B | Yi-1.5-9B | GLM-4-9B | Qwen1.5-7B | Qwen2-7B |
|---|---|---|---|---|---|
| | *English* | | | | |
| MMLU | 68.4 | 69.5 | **72.4** | 59.5 | 70.5 |
| MMLU-Pro | 41.0 | - | - | 29.1 | **44.1** |
| GPQA | 34.2 | - | - | 27.8 | **34.3** |
| Theorem QA | 23.0 | - | - | 14.1 | **25.3** |
| | *Coding* | | | | |
| HumanEval | 62.2 | 66.5 | 71.8 | 46.3 | **79.9** |
| MBPP | **67.9** | - | - | 48.9 | 67.2 |
| MultiPL-E | 48.5 | - | - | 27.2 | **59.1** |
| LiveCodeBench *v1* | 17.3 | - | - | 6.0 | **26.6** |
| | *Mathematics* | | | | |
| GSM8K | 79.6 | 84.8 | 79.6 | 60.3 | **85.7** |
| MATH | 30.0 | 47.7 | 50.6 | 23.2 | **52.9** |
| | *Alignment* | | | | |
| MT-Bench | 8.05 | 8.20 | 8.35 | 7.60 | **8.41** |
| MixEval | 75.0 | 74.2 | - | 71.4 | **76.5** |
| IFEval *strict-prompt* | **72.1** | - | 69.0 | 38.3 | 54.7 |
| AlignBench | 6.20 | 6.90 | 7.01 | 6.20 | **7.21** |

### Qwen2-1.5B-Instruct and Qwen2-0.5B-Instruct [p. 13, 15]

[p. 13] In the context of smaller models, Qwen2-0.5B-Instruct is compared with Qwen1.5-0.5B-Chat, and Qwen2-1.5B-Instruct with Qwen1.5-1.8B-Chat. Notably, the complexity of certain datasets designed for larger models exceeds the capabilities of these smaller models; thus, the analysis focuses on a selected subset. As detailed in Table 9, the Qwen2 models demonstrate a marked advantage over their predecessors in both core capabilities and instruction-following tasks. The achievement mainly attributes to the scaling of pre-training data. Consequently, the results affirm that data scaling remains an effective strategy for enhancing model performance, even in the domain of sub-billion parameter models.

**Table 9: Performance of smaller instruction-tuned models.** [p. 15] We compare both Qwen2-0.5B-Instruct and Qwen2-1.5B-Instruct with Qwen1.5-0.5B-Chat and Qwen2-1.8B-Chat. "-Instruct" or "-Chat" is omitted in the table. Compared with the similar-size baselines, Qwen2 significant surpasses the performance of Qwen1.5.

| Datasets | Qwen1.5-0.5B | Qwen2-0.5B | Qwen1.5-1.8B | Qwen2-1.5B |
|---|---|---|---|---|
| MMLU | 35.0 | **37.9** | 43.7 | **52.4** |
| HumanEval | 10.4 | **29.9** | 27.4 | **47.0** |
| MBPP | 14.5 | **37.8** | 28.6 | **51.9** |
| GSM8K | 11.3 | **40.1** | 35.3 | **61.6** |
| IFEval *strict-prompt* | 14.6 | **20.0** | 16.8 | **29.0** |

## In-house Automatic Evaluation [p. 14, 16]

[p. 14] Despite a number of open benchmark datasets for the evaluation, the authors believe that it is far from sufficient to fully comprehend the capabilities of LLMs. Specifically, they have made a series of in-house datasets that assess different capabilities of the models, e.g., knowledge understanding, text generation, coding, etc. The evaluation is in Chinese and English. The results are gathered in Table 10 and Table 11, respectively.

### Chinese Evaluation [p. 14]

[p. 14] For the evaluations in Chinese, the focus is on comparing the performance of Qwen2 models with the Qwen1.5 counterparts. For the small models, Qwen2-1.5B-Instruct generally outperforms Qwen1.5-1.8B-Chat in almost all the evaluations even with fewer parameters. In terms of the comparison of 7B models, the advantages of Qwen2 are more significant. Noteworthy is Qwen2-72B's superior performance to Qwen1.5-110B-Chat, despite the latter's greatly more parameters. The MoE model displays superior performance across most domains relative to Qwen1.5-32B-Chat, excluding knowledge understanding. This discrepancy may be attributed to a short of pre-training tokens. In the near future, the authors are about to continue the pre-training of the MoE model to discover its scaling behaviors.

**Table 10: Performances of Qwen2-Instruct models on our in-house Chinese automatic evaluation benchmark.** [p. 16] Scores of Qwen2 models surpassing their comparable-sized Qwen1.5 counterparts are in bold. Qwen2-57B-A14B-Instruct is compared with Qwen1.5-32B-Chat.

| Models | Knowledge | Exam | Comprehension | Coding | Math | Reasoning | Avg. |
|---|---|---|---|---|---|---|---|
| | *Proprietary LLMs* | | | | | | |
| GPT-4o-2024-05-13 | 66.68 | 69.04 | 76.85 | 59.58 | 71.16 | 69.94 | 68.87 |
| Qwen-Max-0428 | 76.65 | 74.80 | 73.66 | 49.48 | 66.01 | 70.84 | 68.57 |
| | *Qwen1.5 Series* | | | | | | |
| Qwen1.5-0.5B-Chat | 28.55 | 36.99 | 29.70 | 3.82 | 13.10 | 25.47 | 22.94 |
| Qwen1.5-1.8B-Chat | 30.31 | 44.98 | 44.81 | 6.86 | 29.85 | 34.61 | 31.90 |
| Qwen1.5-4B-Chat | 33.67 | 47.17 | 50.44 | 14.05 | 36.20 | 39.98 | 36.92 |
| Qwen1.5-MoE-A2.7B-Chat | 52.76 | 60.49 | 52.84 | 19.34 | 38.45 | 43.07 | 44.49 |
| Qwen1.5-7B-Chat | 56.77 | 59.36 | 55.50 | 18.85 | 46.41 | 48.77 | 47.61 |
| Qwen1.5-14B-Chat | 63.35 | 66.13 | 60.06 | 28.19 | 54.80 | 50.20 | 53.79 |
| Qwen1.5-32B-Chat | 68.63 | 67.59 | 64.67 | 35.28 | 60.62 | 62.87 | 59.94 |
| Qwen1.5-72B-Chat | 71.52 | 70.04 | 66.70 | 38.22 | 63.09 | 61.30 | 61.81 |
| Qwen1.5-110B-Chat | 76.26 | 74.00 | 71.25 | 44.25 | 64.92 | 64.47 | 65.86 |
| | *Qwen2 Series* | | | | | | |
| Qwen2-0.5B-Instruct | 28.18 | **38.09** | **35.90** | **9.40** | **21.20** | **25.61** | **26.40** |
| Qwen2-1.5B-Instruct | **35.46** | **51.93** | **44.70** | **14.05** | **34.58** | **35.94** | **36.11** |
| Qwen2-7B-Instruct | **61.54** | **66.66** | **59.63** | **34.74** | **60.99** | **58.22** | **56.96** |
| Qwen2-57B-A14B-Instruct | 64.15 | **73.67** | **67.52** | **40.66** | **63.90** | **59.89** | **61.63** |
| Qwen2-72B-Instruct | **76.19** | **75.65** | **74.72** | **49.53** | **70.80** | **70.59** | **69.58** |

### English Evaluation [p. 14, 16]

[p. 14] For English, the authors compare Qwen2 with both Qwen1.5 and Llama-3. Similarly, the small models of Qwen2 significantly outcompete the Qwen1.5 counterparts. However, in comparison with Llama-3-70B, Qwen2-72B-Instruct is falling behind by small margins especially in comprehension and coding. The authors assume both the amount of English tokens for pre-training and the quantity and diversity of data for post-training lead to the performance gap in English.

**Table 11: Performances of Qwen2-Instruct models on our in-house English automatic evaluation benchmark.** [p. 16] Scores of Qwen2 models surpassing their comparable-sized Qwen1.5 and Llama-3 counterparts are in bold. Qwen2-57B-A14B-Instruct is compared with Qwen1.5-32B-Chat.

| Models | Knowledge | Comprehension | Coding | Math | Avg. |
|---|---|---|---|---|---|
| | *Proprietary LLMs* | | | | |
| GPT-4o-2024-05-13 | 87.29 | 76.30 | 55.87 | 84.99 | 76.11 |
| Qwen-Max-0428 | 80.73 | 71.63 | 48.76 | 79.12 | 70.06 |
| | *Qwen1.5 Series* | | | | |
| Qwen1.5-0.5B-Chat | 30.12 | 25.44 | 1.78 | 15.48 | 18.21 |
| Qwen1.5-1.8B-Chat | 40.37 | 41.87 | 4.99 | 29.71 | 29.23 |
| Qwen1.5-4B-Chat | 51.44 | 50.16 | 15.45 | 44.83 | 40.47 |
| Qwen1.5-MoE-A2.7B-Chat | 61.64 | 54.79 | 21.28 | 50.46 | 47.04 |
| Qwen1.5-7B-Chat | 64.86 | 58.61 | 20.79 | 54.24 | 49.62 |
| Qwen1.5-14B-Chat | 74.41 | 59.80 | 28.18 | 66.91 | 57.32 |
| Qwen1.5-32B-Chat | 76.38 | 64.70 | 37.39 | 73.04 | 62.88 |
| Qwen1.5-72B-Chat | 77.59 | 67.58 | 37.30 | 73.76 | 64.06 |
| Qwen1.5-110B-Chat | 78.29 | 70.17 | 44.12 | 78.87 | 67.86 |
| | *Llama-3 Series* | | | | |
| Llama-3-8B-Instruct | 71.01 | 64.71 | 42.56 | 65.82 | 61.03 |
| Llama-3-70B-Instruct | 83.06 | 76.31 | 57.18 | 79.70 | 74.06 |
| | *Qwen2 Series* | | | | |
| Qwen2-0.5B-Instruct | **43.19** | **29.57** | **6.95** | **31.52** | **27.81** |
| Qwen2-1.5B-Instruct | **56.03** | **45.08** | **17.61** | **50.44** | **42.29** |
| Qwen2-7B-Instruct | **73.75** | 63.09 | **36.41** | **75.67** | **62.23** |
| Qwen2-57B-A14B-Instruct | **76.80** | **67.92** | **42.37** | **77.04** | **66.03** |
| Qwen2-72B-Instruct | 83.00 | 73.58 | 53.03 | **82.15** | 72.94 |

## Long Context Capabilities [p. 15–16]

[p. 15] Three methods to evaluate long context capabilities are employed: the Needle in a Haystack (NIAH, Kamradt, 2023), NeedleBench (OpenCompass Contributors, 2023), and LV-Eval (Yuan et al., 2024).

### Needle in a Haystack [p. 15]

[p. 15] This experiment assesses a model's proficiency in pinpointing facts within voluminous texts. Texts with 8K, 16K, ..., 128K tokens in length were crafted, with facts strategically positioned at varying depths. Each depth interval, e.g., from 0% to 10%, encompassed two instances. For contexts over 32K, YARN (Peng et al., 2023) was applied in this evaluation. As illustrated in Figure 1, Qwen2-72B-Instruct exhibits exceptional accuracy in retrieving information from the entire 128K context. Coupled with its inherent strength, this model emerges as the optimal choice for processing extensive texts, assuming sufficient resources are accessible. Additionally, models within the same series showcases remarkable performance across different context lengths. Precisely, Qwen2-7B-Instruct achieves a high level of accuracy in handling contexts up to 128K tokens. Meanwhile, Qwen2-57B-A14B-Instruct manages contexts up to 64K tokens proficiently, and the two smaller models in the Qwen2 series could support contexts of 32K tokens.

**Figure 1** (p. 17): "Performance of Qwen2 instruction-tuned models on Needle in A Haystack Test. All models that supports context lengths above 32k tokens integrates the YARN mechanism."

The figure contains five heatmap panels, one per model. The x-axis is "Context Length (# of Tokens)" ranging from 8k to 128k; the y-axis is "Placed Fact Document Depth" from bottom of document to top of document. Color scale ranges from 0% (red) to 50% (orange/yellow) to 100% (green) accuracy of retrieval.

- **Qwen2-72B-Instruct**: Near-perfect (green) accuracy across the full 128k context and all document depths.
- **Qwen2-7B-Instruct**: Near-perfect (green) accuracy across the full 128k context and all depths, with a single small orange/yellow patch around 32k–40k context at mid-document depth.
- **Qwen2-57B-A14B-Instruct**: Near-perfect (green) accuracy up to approximately 56k–64k context. Beyond 64k, shows a green/yellow patch near the top of the context range, suggesting slight degradation.
- **Qwen2-1.5B-Instruct**: Near-perfect (green) accuracy up to approximately 32k context. Beyond 32k there is a visible green patch indicating maintained performance but the heatmap ends at 32k.
- **Qwen2-0.5B-Instruct**: Near-perfect (green) accuracy up to approximately 24k–32k context, with some degradation patches visible at longer lengths.

---
[p. 17–18 continued]

### NeedleBench [p. 17–18]

[p. 18] NeedleBench ups the challenge on NIAH by including multiple facts (two to five) in passages, necessitating simultaneous identification and multi-hop reasoning. Table 12 reveals that the integration of YARN and DCA (An et al., 2024) notably improves Qwen2 models' long-context abilities. Qwen2-7B-Instruct surpasses ChatGLM4-9B-1M (Zeng et al., 2024), which claims a 1M context length. Moreover, Qwen2-72B-Instruct demonstrates strong performance, with an accuracy reduction of just 6 points, compared to ChatGLM4-9B-1M, which shows a more pronounced decline of 11 points, particularly given its lower initial accuracy.

### LV-Eval [p. 18]

[p. 18] LV-Eval comprises 11 diverse QA datasets that demand comprehension of multiple pieces of evidence at once. To rectify the shortcomings of its original metric, which was excessively stringent and led to a high rate of false negatives, the authors adopt the keyword recall as the reported score. As shown in Table 12, integrating YARN and DCA substantially bolsters the long-context competencies of Qwen2 models on LV-Eval. Qwen2-7B-Instruct achieves parity with ChatGLM4-9B-1M, albeit with a more noticeable decline at extended contexts. Moreover, Qwen2-72B-Instruct demonstrates strong performance across all lengths, confirming its proficiency in handling long-context tasks.

**Table 12: Performance of Qwen2-72B-Instruct and Qwen2-7B-Instruct on NeedleBench and LV-Eval.** [p. 17] +*YARN*+*DCA* does not change the model behavior within 32k tokens.

| Datasets | NeedleBench | | | | LV-Eval | | | | |
|---|---|---|---|---|---|---|---|---|---|
| | 8k | 32k | 128k | 256k | 16k | 32k | 64k | 128k | 256k |
| ChatGLM4-9B-1M | 56.61 | 49.15 | 44.30 | 45.29 | 46.40 | 43.23 | 42.92 | 40.41 | 36.95 |
| Qwen2-7B-Instruct + YARN + DCA | 87.07 | 73.64 | 38.77 / 66.32 | 2.92 / 60.71 | 49.77 | 46.93 | 28.03 / 42.14 | 11.01 / 36.64 | 0.55 / 34.72 |
| Qwen2-72B-Instruct + YARN + DCA | **91.90** | **92.01** | 73.05 / **90.27** | 17.13 / **85.21** | **58.82** | **56.70** | 42.92 / **53.03** | 31.79 / **48.83** | 2.88 / **42.35** |

*Note: Where two values are shown (x / y), x is the score without YARN+DCA and y is the score with YARN+DCA. Bold values indicate best performance.*

## Multilingual Evaluation [p. 18]

[p. 18] For the multilingual evaluation, the authors implement a comprehensive human evaluation for the assessment of multilingual capabilities. Specifically, they design diverse test cases assessing different capabilities of large language models, with test cases in a number of languages. For the annotators, they invite one professional annotator for each language who majors in the language for the evaluation. For each test case, the annotator grades the response from the model with a score from 1 to 5.

[p. 18] From Table 13, it can be found that on average Qwen2-72B-Instruct significantly outperforms GPT-3.5-Turbo and it is competitive with GPT-4-Turbo and slightly falls behind Claude-3-Opus. This shows that the multilingual pre-training and instruction tuning data contribute to the multilingual capabilities of Qwen2-72B-Instruct and it is competitive with most state-of-the-art proprietary LLMs.

**Table 13: Performance of Qwen2-72B-Instruct and proprietary LLMs in multilingual human evaluation.** [p. 18] We compare Qwen2-72B-Instruct with GPT-3.5-Turbo-1106, GPT-4-Turbo-0409, GPT-4o-0513, Claude-3-Opus-0229. Scores range from 1 to 5. Overall, Qwen2-72B-Instruct performs substantially better than GPT-3.5-Turbo but there is progress to be made to be competitive with the proprietary models released in the last 6 months.

| Language | GPT-3.5-Turbo | GPT-4-Turbo | GPT-4o | Claude-3-Opus | Qwen2-72B-Instruct |
|---|---|---|---|---|---|
| Arabic | 2.52 | 3.44 | 3.55 | 4.15 | 3.86 |
| French | 3.47 | 4.19 | 4.16 | 4.23 | 4.01 |
| Indonesian | 3.56 | 4.09 | 4.39 | 4.40 | 3.83 |
| Japanese | 2.75 | 3.68 | 3.72 | 3.85 | 3.63 |
| Korean | 2.37 | 4.24 | 4.40 | 4.23 | 4.14 |
| Portuguese | 3.37 | 3.86 | 3.89 | 4.09 | 3.97 |
| Russian | 3.24 | 4.27 | 4.32 | 4.25 | 4.15 |
| Spanish | 4.07 | 4.08 | 4.26 | 4.31 | 4.10 |
| Thai | 3.38 | 4.11 | 4.09 | 4.01 | 3.75 |
| Vietnamese | 3.90 | 3.84 | 4.14 | 3.98 | 3.91 |
| Average | 3.16 | 3.98 | 4.09 | 4.15 | 3.93 |

## Safety & Responsibility [p. 18–19]

[p. 18] LLMs with openly accessible weights effectively accelerate the development of the research as well as their applications. Moreover, the authors believe that it is crucial to build safe and responsible LLMs so that the effect of the misuse of AI technologies could be significantly alleviated.

[p. 18–19] The authors implement a multilingual safety evaluation that tests the LLMs in different languages. Specifically, they assess the safety performance of the models in the topics about illegal behaviors, fraud, pornography, and privacy. They have collected prompts prone to jail-breaking and use them to test whether the models can provide safe responses by rejection.

[p. 19] The results are presented in Table 14, where the proportion of harmful responses generated by the models are shown and the lower, the better. It can be observed that Qwen2-72B-Instruct performs better than the proprietary model, GPT-4, and significantly outperforms the open-weight model, Mixtral-8x22B-Instruct. However, the authors believe that there is still much room for our model to improve to be a safer and more responsible model, especially in terms of pornography, which is a conventionally difficult category to differentiate even for humans.

**Table 14: Performance of models in safety evaluation.** [p. 19] We compare Qwen2-72B-Instruct with GPT-4 and Mixtral-8x22B-Instruct. The lower, the better. Qwen2-72B-Instruct rejected more prompts with risks than the competitors.

| Risk Category | GPT-4 | Mixtral-8x22B | Qwen2-72B-Instruct |
|---|---|---|---|
| Illegal | 0.00 | 6.87 | 0.00 |
| Fraud | 3.40 | 8.49 | 2.41 |
| Pornography | 23.63 | 33.82 | 22.91 |
| Privacy | 3.37 | 15.03 | 2.47 |

## Contamination Analysis [p. 19–20]

[p. 19] For large language models, what counts as contamination and how to run contamination analysis remain an active area of research (Ravaut et al., 2024; Golchin & Surdeanu, 2024; Sainz et al., 2023). The authors first introduce how they try to decontaminate the training corpora against the evaluation datasets, and then estimate the extent to which benchmark scores are influenced by the remaining contamination.

[p. 19] During the construction of the pre-training and post-training datasets, they exclude potentially contaminated data using n-gram matching. However, they found that this approach may lead to a high false negative rate, because there could be commonly used expressions, especially in mathematical and coding data. Therefore, they also applied another constraint based on the longest common subsequence (LCS). Specifically, they first remove all symbols and punctuation from both the test and training sequences and perform tokenization. For a training sequence **s_t**, they remove it if there is a test sequence **s_e** such that |LCS(**s_t**, **s_e**)| >= 13 and |LCS(**s_t**, **s_e**)| >= 0.6 x min(|**s_t**|, |**s_e**|).

[p. 19–20] To assess the potential effects of leaking data on the test performance, the authors follow OpenAI (2023) to construct a *strict non-contaminated* test set to check if there is significant performance degradation after *strict decontamination*. Specifically, they construct the non-contaminated test set by excluding any sample which has 13-gram overlap with the pre-training or the post-training data (without constraint on LCS), and then compute the corresponding metric on the test set.

[p. 20] The results are presented in Table 15. Although some datasets exhibit a high percentage of contamination under the strict criterion, the authors noticed that most of the identified *contaminated* samples are false positives, primarily stemming from the mathematics and coding datasets. It is likely that certain code snippets and mathematical equations are so common that they do not provide any meaningful advantage in solving the test data. Furthermore, the analysis shows that the performance of the Qwen2 models remains consistent between the original and non-contaminated test data, suggesting that the potential issue of data contamination does not significantly impact the model's performance.

**Table 15: Contamination Analysis.** [p. 19] The *contaminated* samples in this table are identified using a *strict criterion*: any test sample with a 13-gram overlap with the pre-training or post-training data is considered contaminated. We report the percentage of contaminated samples as well as the model performance on both the original and non-contaminated test sets.

| Test set | Percent of Contamination | Qwen2-72B-Instruct | | | Qwen2-7B-Instruct | | |
|---|---|---|---|---|---|---|---|
| | | Original | Non-Contam. | Delta | Original | Non-Contam. | Delta |
| MMLU | 11.2% | 82.3 | 83.2 | 0.9 | 70.5 | 71.3 | 0.8 |
| MMLU-Pro | 11.6% | 64.4 | 65.6 | 1.2 | 44.1 | 46.5 | 2.4 |
| GPQA | 1.0% | 42.4 | 41.8 | 0.6 | 34.3 | 34.1 | -0.2 |
| HumanEval | 75.0% | 86.0 | 87.0 | 1.0 | 79.9 | 87.8 | 7.9 |
| MBPP | 29.6% | 80.2 | 79.7 | 0.5 | 67.2 | 69.0 | 1.8 |
| MultiPL-E | 37.7% | 69.2 | 69.2 | 0.0 | 59.1 | 58.9 | -0.2 |
| GSM8K | 0.7% | 93.2 | 92.8 | -0.4 | 85.7 | 85.6 | -0.1 |
| Math | 31.7% | 69.0 | 74.6 | 5.6 | 52.9 | 57.6 | 4.7 |
| IFEval | 0.9% | 77.6 | 77.4 | -0.2 | 54.7 | 53.7 | -1.0 |
