# Evaluation [p. 8–11]

[p. 8] To thoroughly assess the Qwen2 models, consisting of both base and instruction-tuned models, a comprehensive evaluation protocol is implemented. This protocol examines a range of competencies, including general knowledge understanding, language comprehension, generation, coding, mathematics, reasoning, and additional areas of expertise. Specifically, base models are assessed using established benchmark datasets for large language models (LLMs), with responses elicited through few-shot prompting, unless specified otherwise. For instruction-tuned models, in addition to benchmark evaluations, human preference assessments are prioritized.

## Base Language Models [p. 8–11]

[p. 8] The evaluation of the base language models of the Qwen2 series covers benchmark datasets for knowledge and basic capabilities, as well as multilingual benchmark datasets to evaluate their support of languages. As there are multiple model sizes, they are compared with the state-of-the-art (SOTA) models of similar or larger sizes.

### Core Capabilities [p. 8–11]

**Benchmarks and Evaluation Protocol** [p. 8]

The common practice of evaluating the core capabilities of base language models is the implementation of benchmark dataset evaluation with few-shot or zero-shot prompting. The evaluation mainly focuses on model performance of natural language understanding, general question answering, coding, mathematics, scientific knowledge, reasoning, etc.

The datasets for evaluation include:
- **English**: MMLU (Hendrycks et al., 2021a) (5-shot), MMLU-Pro (Wang et al., 2024) (5-shot), GPQA (Rein et al., 2023) (5-shot), Theorem QA (Chen et al., 2023a) (5-shot), BBH (Suzgun et al., 2023) (3-shot), HellaSwag (Zellers et al., 2019) (10-shot), Winogrande (Sakaguchi et al., 2021) (5-shot), TruthfulQA (Lin et al., 2022a) (0-shot), ARC-C (Clark et al., 2018) (25-shot), HumanEval (Chen et al., 2021) (0-shot), MBPP (Austin et al., 2021) (0-shot), EvalPlus (Liu et al., 2023a) (0-shot), MultiPL-E (Cassano et al., 2023) (0-shot on Python, C++, Java, PHP, TypeScript, C#, Bash, and JavaScript), GSM8K (Cobbe et al., 2021) (5-shot), MATH (Hendrycks et al., 2021b) (4-shot), C-Eval (Huang et al., 2023) (5-shot), and CMMLU (Li et al., 2023) (5-shot)
- **Multilingual** grouped into four categories:
  - (a) **Exam**: M3Exam (5-shot, only examples that require no image), IndoMMLU (Koto et al., 2023) (3-shot), ruMMLU (Fenogenova et al., 2024) (5-shot), and translated MMLU (Chen et al., 2023b) (5-shot on Arabic, Spanish, French, Portuguese, German, Italian, Japanese, and Korean)
  - (b) **Understanding**: BELEBELE (Bandarkar et al., 2023) (5-shot), XCOPA (Ponti et al., 2020) (5-shot), XWinograd (Muennighoff et al., 2023) (5-shot), XStoryCloze (Lin et al., 2022b) (0-shot) and PAWS-X (Yang et al., 2019) (5-shot)
  - (c) **Mathematics**: MGSM (Goyal et al., 2022) (8-shot CoT)
  - (d) **Translation**: Flores-101 (Goyal et al., 2022) (5-shot)

### Qwen2-72B [p. 9]

[p. 9] Qwen2-72B is compared with competitive baseline open-weight models, including Mixtral-8x22B (Jiang et al., 2024), Llama-3-70B (AI@Meta, 2024), as well as Qwen1.5-72B (Qwen Team, 2024a) and Qwen1.5-110B (Qwen Team, 2024b). The results are reported in Table 2.

Qwen2-72B outperforms Llama-3-70B in general **knowledge understanding** on both MMLU and MMLU-Pro, achieving accuracy improvements of 4.7 and 2.8, respectively. In **scientific** assessments, Qwen2-72B demonstrates superiority over Llama-3-70B with enhancements of 1.6 and 9.8 on GPQA and Theorem QA. Upon enrichment of **coding** data, Qwen2-72B exhibits a significant 18.3 and 10.0 percentage point advantage over Qwen1.5-72B in HumanEval and MBPP evaluations. Enhanced **mathematics**-related data allows Qwen2-72B to outperform Qwen1.5-72B by 10.0 and 17.0 percentage points in the GSM8K and MATH benchmarks. Qwen2-72B displays **reasoning** capabilities equivalent to Llama-3-70B, considering BBH, Winogrande, and ARC-C, attributable to its improved coding and mathematical data. In assessing language understanding in **Chinese**, Qwen2-72B significantly outperforms Mixtral-8x22B and Llama-3-70B, and also outperforms Qwen1.5-72B.

**Table 2: Performance of the 70B+ models.** [p. 9] We compare Qwen2-72B with the baselines, including Mixtral-8x22B, Llama-3-70B, Qwen1.5-110B, and Qwen1.5-72B. For most datasets, Qwen2-72B demonstrates advantages over the baselines.

| Datasets | Mixtral-8x22B | Llama-3-70B | Qwen1.5-72B | Qwen1.5-110B | Qwen2-72B |
|---|---|---|---|---|---|
| | *English* | | | | |
| MMLU | 77.8 | 79.5 | 77.5 | 80.4 | **84.2** |
| MMLU-Pro | 49.5 | 52.8 | 45.8 | 49.4 | **55.6** |
| GPQA | 34.3 | 36.3 | 36.3 | 35.9 | **37.9** |
| Theorem QA | 35.9 | 32.3 | 29.3 | 34.9 | **43.1** |
| BBH | 78.9 | 81.0 | 65.5 | 74.8 | **82.4** |
| HellaSwag | **88.7** | 88.0 | 86.0 | 87.5 | 87.6 |
| Winogrande | 85.0 | **85.3** | 83.0 | 83.5 | 85.1 |
| ARC-C | **70.7** | 68.8 | 65.9 | 69.6 | 68.9 |
| TruthfulQA | 51.0 | 45.6 | **59.6** | 49.6 | 54.8 |
| | *Coding* | | | | |
| HumanEval | 46.3 | 48.2 | 46.3 | 54.3 | **64.6** |
| MBPP | 71.7 | 70.4 | 66.9 | 70.9 | **76.9** |
| EvalPlus | 54.1 | 54.8 | 52.9 | 57.7 | **65.4** |
| MultiPL-E | 46.7 | 46.3 | 41.8 | 52.7 | **59.6** |
| | *Mathematics* | | | | |
| GSM8K | 83.7 | 83.0 | 79.5 | 85.4 | **89.5** |
| MATH | 41.7 | 42.5 | 34.1 | 49.6 | **51.1** |
| | *Chinese* | | | | |
| C-Eval | 54.6 | 65.2 | 84.1 | 89.1 | **91.0** |
| CMMLU | 53.4 | 67.2 | 83.5 | 88.3 | **90.1** |
| | *Multilingual* | | | | |
| Exam | 63.5 | 70.0 | 66.4 | 75.6 | **76.6** |
| Understanding | 77.7 | 79.9 | 78.2 | 78.2 | **80.7** |
| Mathematics | 62.9 | 67.1 | 61.7 | 64.4 | **76.0** |
| Translation | 23.3 | **38.0** | 35.6 | 36.2 | 37.8 |

### Qwen2-57B-A14B [p. 9–10]

[p. 9] For the evaluation of the MoE model, Qwen2-57B-A14B is compared against baselines of similar sizes. These baselines include other MoE models, such as Mixtral-8x7B (Jiang et al., 2024) and Jamba (Lieber et al., 2024), and dense models, such as Yi-1.5-34B (Young et al., 2024) and Qwen1.5-32B (Qwen Team, 2024a), both of which have approximately 30 billion parameters. The results are shown in Table 3.

[p. 10] Qwen2-57B-A14B, which activates 14 billion parameters, is anticipated to match the performance of a 30 billion parameter dense equivalent Qwen2 model. The evaluation reveals that Qwen2-57B-A14B performs comparably to Yi-1.5-34B in natural language understanding tasks. Moreover, it outperforms the baseline models in coding and mathematics tasks. Additionally, Qwen2-57B-A14B demonstrates robust Chinese language understanding capabilities, rivaling the larger Qwen2-72B model. In essence, Qwen2-57B-A14B is an efficient model that, while activating only 14 billion parameters per forward pass, maintains the performance level of a 30 billion parameter dense model.

**Table 3: Performance of the 30B+ dense models and 40B+ MoE models.** [p. 10] Qwen2-57B-A14B, an MoE model with a total of 57 billion parameters and 14 billion activated parameters, is designed to match the performance of 30 billion parameter dense models. This comparison includes dense model baselines: Yi-1.5-34B and Qwen1.5-32B, as well as MoE baselines: Mixtral-8x7B and Jamba. Results demonstrate that Qwen2-57B-A14B achieves competitive performance overall, with a notable superiority in coding and mathematics tasks.

| Datasets | Jamba | Mixtral-8x7B | Yi-1.5-34B | Qwen1.5-32B | Qwen2-57B-A14B |
|---|---|---|---|---|---|
| Architecture | MoE | MoE | Dense | Dense | MoE |
| # Act Params | 12B | 12B | 32B | 34B | 14B |
| # Params | 52B | 47B | 32B | 34B | 57B |
| | *English* | | | | |
| MMLU | 67.4 | 71.8 | **77.1** | 74.3 | 76.5 |
| MMLU-Pro | - | 41.0 | **48.3** | 44.0 | 43.0 |
| GPQA | - | 29.2 | - | 30.8 | **34.3** |
| Theorem QA | - | 23.2 | - | 28.8 | **33.5** |
| BBH | 45.4 | 50.3 | **76.4** | 66.8 | 67.0 |
| HellaSwag | **87.1** | 86.5 | 85.9 | 85.0 | 85.2 |
| Winogrande | 82.5 | 81.9 | **84.9** | 81.5 | 79.5 |
| ARC-C | 64.4 | **66.0** | 65.6 | 63.6 | 64.1 |
| TruthfulQA | 46.4 | 51.1 | 53.9 | 57.4 | **57.7** |
| | *Coding* | | | | |
| HumanEval | 29.3 | 37.2 | 46.3 | 43.3 | **53.0** |
| MBPP | - | 63.9 | 65.5 | 64.2 | **71.9** |
| EvalPlus | - | 46.4 | 51.9 | 50.4 | **57.2** |
| MultiPL-E | - | 39.0 | 39.5 | 38.5 | **49.8** |
| | *Mathematics* | | | | |
| GSM8K | 59.9 | 62.5 | **82.7** | 76.8 | 80.7 |
| MATH | - | 30.8 | 41.7 | 36.1 | **43.0** |
| | *Chinese* | | | | |
| C-Eval | - | - | - | 83.5 | **87.7** |
| CMMLU | - | - | 84.8 | 82.3 | **88.5** |
| | *Multilingual* | | | | |
| Exam | - | 56.1 | 58.3 | 61.6 | **65.5** |
| Understanding | - | 70.7 | 73.9 | 76.5 | **77.0** |
| Mathematics | - | 45.0 | 49.3 | 56.1 | **62.3** |
| Translation | - | 29.8 | 30.0 | 33.5 | **34.5** |

### Qwen2-7B [p. 10–11]

[p. 10] The 7B model is widely utilized, as it enables the execution in 16-bit floating points on accelerators equipped with 16GB memory. The focus is on comparing this model with other leading 7B models, including Llama-3-8B, which has recently demonstrated exceptional performance in the Chatbot Arena (Chiang et al., 2024). This comparison also includes Mistral-7B-v0.2 (Jiang et al., 2023a), Gemma-7B (Mesnard et al., 2024), and Qwen1.5-7B (Qwen Team, 2024a).

[p. 11] The results can be found in Table 4. Qwen2-7B demonstrates superior performance across most datasets compared to other models, particularly excelling in coding tasks, mathematics, and Chinese language tasks. It also shows strong performance in multilingual understanding and exams. This indicates that Qwen2-7B has been optimized for a wide range of language and logic-based tasks, showcasing its versatility and advanced capabilities.

**Table 4: Performance of the 7B+ models.** [p. 11] We compare Qwen2-7B with previously released state-of-the-art 7B+ models including Mistral-7B, Gemma-7B, Llama-3-8B, and our previous Qwen1.5-7B. Qwen2-7B demonstrates significant advantages over the baselines in most of the evaluation datasets.

| Datasets | Mistral-7B | Gemma-7B | Llama-3-8B | Qwen1.5-7B | Qwen2-7B |
|---|---|---|---|---|---|
| | *English* | | | | |
| MMLU | 64.2 | 64.6 | 66.6 | 61.0 | **70.3** |
| MMLU-Pro | 30.9 | 33.7 | 35.4 | 29.9 | **40.0** |
| GPQA | 24.7 | 25.7 | 25.8 | 26.7 | **31.8** |
| Theorem QA | 19.2 | 21.5 | 22.1 | 14.2 | **31.1** |
| BBH | 56.1 | 55.1 | 57.7 | 40.2 | **62.6** |
| HellaSwag | **83.2** | 82.2 | 82.1 | 78.5 | 80.7 |
| Winogrande | 78.4 | **79.0** | 77.4 | 71.3 | 77.0 |
| ARC-C | 60.0 | **61.1** | 59.3 | 54.2 | 60.6 |
| TruthfulQA | 42.2 | 44.8 | 44.0 | 51.1 | **54.2** |
| | *Coding* | | | | |
| HumanEval | 29.3 | 37.2 | 33.5 | 36.0 | **51.2** |
| MBPP | 51.1 | 50.6 | 53.9 | 51.6 | **65.9** |
| Evalplus | 36.4 | 39.6 | 40.3 | 40.0 | **54.2** |
| MultiPL-E | 29.4 | 29.7 | 22.6 | 28.1 | **46.3** |
| | *Mathematics* | | | | |
| GSM8K | 52.2 | 46.4 | 56.0 | 62.5 | **79.9** |
| MATH | 13.1 | 24.3 | 20.5 | 20.3 | **44.2** |
| | *Chinese* | | | | |
| C-Eval | 47.4 | 43.6 | 49.5 | 74.1 | **83.2** |
| CMMLU | - | - | 50.8 | 73.1 | **83.9** |
| | *Multilingual* | | | | |
| Exam | 47.1 | 42.7 | 52.3 | 47.7 | **59.2** |
| Understanding | 63.3 | 58.3 | 68.6 | 67.6 | **72.0** |
| Mathematics | 26.3 | 39.1 | 36.3 | 37.3 | **57.5** |
| Translation | 23.3 | 31.2 | **31.9** | 28.4 | 31.5 |

### Qwen2-1.5B and Qwen2-0.5B [p. 11]

[p. 11] To evaluate the performance of the smaller models, specifically Qwen2-1.5B and Qwen2-0.5B, they are compared against established baselines: Phi-2 (Abdin et al., 2024), Gemma-2B (Mesnard et al., 2024), and Qwen1.5-1.8B (Qwen Team, 2024a). The results are given in Table 5.

In language understanding, Qwen2-1.5B outperforms Phi-2, a model trained on textbook-like data. For coding tasks, Qwen2-0.5B matches the performance of Gemma-2B and Qwen1.5-1.8B, while Qwen2-1.5B surpasses these baselines, except for Phi-2. Both Qwen2 models exhibit superior performance in mathematics compared to their competitors. In terms of general reasoning, Phi-2 generally outperforms all others, which to some extent reflects the significance of textbook data for reasoning capabilities. In TruthfulQA, Qwen2-1.5B performs the best, demonstrating that smaller models do not necessarily suffer from hallucination. In Chinese language understanding, both Qwen2 models outperform all the others, a trend consistent with larger models in their respective comparisons.

[p. 11] In general, the Qwen2 series demonstrates superior performance against the baselines across different model sizes. Notably, Qwen2-72B exhibits the highest performance among all Qwen2 models, underscoring the efficacy of model size scaling.

**Table 5: Performance of the smaller models.** [p. 12] We compare our Qwen2-0.5B and Qwen2-1.5B with the previous SOTA small models including Phi-2, Gemma-2B and Qwen1.5-1.8B. Qwen2-0.5B with a much smaller model size achieves competitive performance, and Qwen2-1.5B significantly outperforms Qwen2-0.5B.

| Datasets | Phi-2 | Gemma-2B | Qwen1.5-1.8B | Qwen2-0.5B | Qwen2-1.5B |
|---|---|---|---|---|---|
| # Non-Emb Params | 2.5B | 2.0B | 1.2B | 0.3B | 1.2B |
| | *English* | | | | |
| MMLU | 52.7 | 42.3 | 46.8 | 45.4 | **56.5** |
| MMLU-Pro | - | 15.9 | - | 14.7 | 21.8 |
| Theorem QA | - | - | - | 8.9 | **15.0** |
| BBH | **43.4** | 35.2 | 24.2 | 28.4 | 37.2 |
| HellaSwag | **73.1** | 71.4 | 61.4 | 49.3 | 66.6 |
| Winogrande | **74.4** | 66.8 | 60.3 | 56.8 | 66.2 |
| ARC-C | **61.1** | 48.5 | 37.9 | 31.5 | 43.9 |
| TruthfulQA | 44.5 | 33.1 | 39.4 | 39.7 | **45.9** |
| | *Coding* | | | | |
| HumanEval | **47.6** | 22.0 | 20.1 | 22.0 | 31.1 |
| MBPP | **55.0** | 29.2 | 18.0 | 22.0 | 37.4 |
| | *Mathematics* | | | | |
| GSM8K | 57.2 | 17.7 | 38.4 | 36.5 | **58.5** |
| MATH | 3.5 | 11.8 | 10.1 | 10.7 | **21.7** |
| | *Chinese* | | | | |
| C-Eval | 23.4 | 28.0 | 59.7 | 58.2 | **70.6** |
| CMMLU | 24.2 | - | 57.8 | 55.1 | **70.3** |
