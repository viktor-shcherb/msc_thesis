# Main results [p. 4-6]

[p. 4] Following Brown et al. (2020), zero-shot and few-shot tasks are considered, reporting results on a total of 20 benchmarks:

- **Zero-shot.** A textual description of the task and a test example are provided. The model either provides an answer using open-ended generation, or ranks the proposed answers.
- **Few-shot.** A few examples of the task (between 1 and 64) and a test example are provided. The model takes this text as input and generates the answer or ranks different options.

LLaMA is compared with other foundation models, namely the non-publicly available language models GPT-3 (Brown et al., 2020), Gopher (Rae et al., 2021), Chinchilla (Hoffmann et al., 2022) and PaLM (Chowdhery et al., 2022), as well as the open-sourced OPT models (Zhang et al., 2022), GPT-J (Wang and Komatsuzaki, 2021), and GPT-Neo (Black et al., 2022). In Section 4, LLaMA is also briefly compared with instruction-tuned models such as OPT-IML (Iyer et al., 2022) and Flan-PaLM (Chung et al., 2022). [p. 4]

LLaMA is evaluated on free-form generation tasks and multiple choice tasks. In the multiple choice tasks, the objective is to select the most appropriate completion among a set of given options, based on a provided context. The completion with the highest likelihood given the provided context is selected. Following Gao et al. (2021), the likelihood normalized by the number of characters in the completion is used, except for certain datasets (OpenBookQA, BoolQ), for which Brown et al. (2020) is followed, selecting a completion based on the likelihood normalized by the likelihood of the completion given "Answer:" as context:

P(completion|context) / P(completion|"Answer:"). [p. 4]

## 3.1 Common Sense Reasoning

[p. 4-5] Eight standard common sense reasoning benchmarks are considered: BoolQ (Clark et al., 2019), PIQA (Bisk et al., 2020), SIQA (Sap et al., 2019), HellaSwag (Zellers et al., 2019), WinoGrande (Sakaguchi et al., 2021), ARC easy and challenge (Clark et al., 2018) and OpenBookQA (Mihaylov et al., 2018). These datasets include Cloze and Winograd style tasks, as well as multiple choice question answering. Evaluation is in the zero-shot setting as done in the language modeling community.

**Table 3** (p. 4): **Zero-shot performance on Common Sense Reasoning tasks.**

| | | BoolQ | PIQA | SIQA | HellaSwag | WinoGrande | ARC-e | ARC-c | OBQA |
|---|---|---|---|---|---|---|---|---|---|
| GPT-3 | 175B | 60.5 | 81.0 | - | 78.9 | 70.2 | 68.8 | 51.4 | 57.6 |
| Gopher | 280B | 79.3 | 81.8 | 50.6 | 79.2 | 70.1 | - | - | - |
| Chinchilla | 70B | 83.7 | 81.8 | 51.3 | 80.8 | 74.9 | - | - | - |
| PaLM | 62B | 84.8 | 80.5 | - | 79.7 | 77.0 | 75.2 | 52.5 | 50.4 |
| PaLM-cont | 62B | 83.9 | 81.4 | - | 80.6 | 77.0 | - | - | - |
| PaLM | 540B | **88.0** | 82.3 | - | 83.4 | **81.1** | 76.6 | 53.0 | 53.4 |
| | | | | | | | | | |
| LLaMA | 7B | 76.5 | 79.8 | 48.9 | 76.1 | 70.1 | 72.8 | 47.6 | 57.2 |
| LLaMA | 13B | 78.1 | 80.1 | 50.4 | 79.2 | 73.0 | 74.8 | 52.7 | 56.4 |
| LLaMA | 33B | 83.1 | 82.3 | 50.4 | 82.8 | 76.0 | **80.0** | **57.8** | 58.6 |
| LLaMA | 65B | 85.3 | **82.8** | **52.3** | **84.2** | 77.0 | 78.9 | 56.0 | **60.2** |

[p. 5] In Table 3, comparison with existing models of various sizes using numbers from the corresponding papers. LLaMA-65B outperforms Chinchilla-70B on all reported benchmarks but BoolQ. Similarly, this model surpasses PaLM-540B everywhere but on BoolQ and WinoGrande. LLaMA-13B model also outperforms GPT-3 on most benchmarks despite being 10x smaller.

## 3.2 Closed-book Question Answering

[p. 5] LLaMA is compared to existing large language models on two closed-book question answering benchmarks: Natural Questions (Kwiatkowski et al., 2019) and TriviaQA (Joshi et al., 2017). For both benchmarks, exact match performance in a closed book setting is reported, i.e., where the models do not have access to documents that contain evidence to answer the question.

**Table 4** (p. 4): **NaturalQuestions.** Exact match performance.

| | | 0-shot | 1-shot | 5-shot | 64-shot |
|---|---|---|---|---|---|
| GPT-3 | 175B | 14.6 | 23.0 | - | 29.9 |
| Gopher | 280B | 10.1 | - | 24.5 | 28.2 |
| Chinchilla | 70B | 16.6 | - | 31.5 | 35.5 |
| | | | | | |
| PaLM | 8B | 8.4 | 10.6 | - | 14.6 |
| PaLM | 62B | 18.1 | 26.5 | - | 27.6 |
| PaLM | 540B | 21.2 | 29.3 | - | 39.6 |
| | | | | | |
| LLaMA | 7B | 16.8 | 18.7 | 22.0 | 26.1 |
| LLaMA | 13B | 20.1 | 23.4 | 28.1 | 31.9 |
| LLaMA | 33B | **24.9** | 28.3 | 32.9 | 36.0 |
| LLaMA | 65B | 23.8 | **31.0** | **35.0** | **39.9** |

**Table 5** (p. 5): **TriviaQA.** Zero-shot and few-shot exact match performance on the filtered dev set.

| | | 0-shot | 1-shot | 5-shot | 64-shot |
|---|---|---|---|---|---|
| Gopher | 280B | 43.5 | - | 57.0 | 57.2 |
| Chinchilla | 70B | 55.4 | - | 64.1 | 64.6 |
| | | | | | |
| LLaMA | 7B | 50.0 | 53.4 | 56.3 | 57.6 |
| LLaMA | 13B | 56.6 | 60.5 | 63.1 | 64.0 |
| LLaMA | 33B | 65.1 | 67.9 | 69.9 | 70.4 |
| LLaMA | 65B | **68.2** | **71.6** | **72.6** | **73.0** |

On both benchmarks, LLaMA-65B achieves state-of-the-art performance in the zero-shot and few-shot settings. The LLaMA-13B is also competitive on these benchmarks with GPT-3 and Chinchilla, despite being 5-10x smaller. This model runs on a single V100 GPU during inference. [p. 5]

## 3.3 Reading Comprehension

[p. 5] Evaluation on the RACE reading comprehension benchmark (Lai et al., 2017). This dataset was collected from English reading comprehension exams designed for middle and high school Chinese students. The evaluation setup from Brown et al. (2020) is followed.

**Table 6** (p. 5): **Reading Comprehension.** Zero-shot accuracy.

| | | RACE-middle | RACE-high |
|---|---|---|---|
| GPT-3 | 175B | 58.4 | 45.5 |
| | | | |
| PaLM | 8B | 57.9 | 42.3 |
| PaLM | 62B | 64.3 | 47.5 |
| PaLM | 540B | **68.1** | 49.1 |
| | | | |
| LLaMA | 7B | 61.1 | 46.9 |
| LLaMA | 13B | 61.6 | 47.2 |
| LLaMA | 33B | 64.1 | 48.3 |
| LLaMA | 65B | 67.9 | **51.6** |

On these benchmarks, LLaMA-65B is competitive with PaLM-540B, and LLaMA-13B outperforms GPT-3 by a few percents. [p. 5]

## 3.4 Mathematical reasoning

[p. 5-6] Evaluation on two mathematical reasoning benchmarks: MATH (Hendrycks et al., 2021) and GSM8k (Cobbe et al., 2021). MATH is a dataset of 12K middle school and high school mathematics problems written in LaTeX. GSM8k is a set of middle school mathematical problems.

In Table 7, comparison with PaLM and Minerva (Lewkowycz et al., 2022). Minerva is a series of PaLM models finetuned on 38.5B tokens extracted from ArXiv and Math Web Pages, while neither PaLM nor LLaMA are finetuned on mathematical data. The numbers for PaLM and Minerva are taken from Lewkowycz et al. (2022). Results compared with and without maj1@k. maj1@k denotes evaluations where *k* samples are generated for each problem and majority voting is performed (Wang et al., 2022).

**Table 7** (p. 6): **Model performance on quantitative reasoning datasets.** For majority voting, the same setup as Minerva is used, with *k* = 256 samples for MATH and *k* = 100 for GSM8k (Minerva 540B uses *k* = 64 for MATH and *k* = 40 for GSM8k).

| | | MATH | +maj1@k | GSM8k | +maj1@k |
|---|---|---|---|---|---|
| PaLM | 8B | 1.5 | - | 4.1 | - |
| PaLM | 62B | 4.4 | - | 33.0 | - |
| PaLM | 540B | 8.8 | - | 56.5 | - |
| | | | | | |
| Minerva | 8B | 14.1 | 25.4 | 16.2 | 28.4 |
| Minerva | 62B | 27.6 | 43.4 | 52.4 | 68.5 |
| Minerva | 540B | 33.6 | **50.3** | **68.5** | **78.5** |
| | | | | | |
| LLaMA | 7B | 2.9 | 6.9 | 11.0 | 18.1 |
| LLaMA | 13B | 3.9 | 8.8 | 17.8 | 29.3 |
| LLaMA | 33B | 7.1 | 15.2 | 35.6 | 53.1 |
| LLaMA | 65B | 10.6 | 20.5 | 50.9 | 69.7 |

On GSM8k, LLaMA-65B outperforms Minerva-62B, although it has not been fine-tuned on mathematical data. [p. 5-6]

## 3.5 Code generation

[p. 6] Evaluation on two code generation benchmarks: HumanEval (Chen et al., 2021) and MBPP (Austin et al., 2021). For both tasks, the model receives the description of the program in a few sentences, as well as a few input-output examples. In HumanEval, it also receives a function signature, and the prompt is formatted as natural code with the textual description and tests in a docstring. The model needs to generate a Python program that fits the description and satisfies the test cases.

**Table 8** (p. 6): **Model performance for code generation.** pass@ score on HumanEval and MBPP reported. HumanEval generations are done in zero-shot and MBBP with 3-shot prompts similar to Austin et al. (2021). Values marked with * are read from figures in Chowdhery et al. (2022).

| pass@ | Params | HumanEval @1 | HumanEval @100 | MBPP @1 | MBPP @80 |
|---|---|---|---|---|---|
| LaMDA | 137B | 14.0 | 47.3 | 14.8 | 62.4 |
| PaLM | 8B | 3.6* | 18.7* | 5.0* | 35.7* |
| PaLM | 62B | 15.9 | 46.3* | 21.4 | 63.2* |
| PaLM-cont | 62B | 23.7 | - | 31.2 | - |
| PaLM | 540B | 26.2 | 76.2 | 36.8 | 75.0 |
| | | | | | |
| LLaMA | 7B | 10.5 | 36.5 | 17.7 | 56.2 |
| LLaMA | 13B | 15.8 | 52.5 | 22.0 | 64.0 |
| LLaMA | 33B | 21.7 | 70.7 | 30.2 | 73.4 |
| LLaMA | 65B | 23.7 | **79.3** | **37.7** | **76.8** |

For a similar number of parameters, LLaMA outperforms other general models such as LaMDA and PaLM, which are not trained or finetuned specifically for code. LLaMA with 13B parameters and more outperforms LaMDA 137B on both HumanEval and MBPP. LLaMA 65B also outperforms PaLM 62B, even when it is trained longer. [p. 6]

The pass@1 results reported in this table were obtained by sampling with temperature 0.1. The pass@100 and pass@80 metrics were obtained with temperature 0.8. Chen et al. (2021) is used to obtain unbiased estimates of the pass@k. [p. 6]

It is possible to improve the performance on code by finetuning on code-specific tokens. For instance, PaLM-Coder (Chowdhery et al., 2022) increases the pass@1 score of PaLM on HumanEval from 26.2% for PaLM to 36%. Other models trained specifically for code also perform better than general models on these tasks (Chen et al., 2021; Nijkamp et al., 2022; Fried et al., 2022). Finetuning on code tokens is beyond the scope of this paper. [p. 6]

## 3.6 Massive Multitask Language Understanding

[p. 6] The massive multitask language understanding benchmark, or MMLU, introduced by Hendrycks et al. (2020), consists of multiple choice questions covering various domains of knowledge, including humanities, STEM and social sciences. Evaluation in the 5-shot setting, using the examples provided by the benchmark. Results reported in Table 9.

**Table 9** (p. 7): **Massive Multitask Language Understanding (MMLU).** Five-shot accuracy.

| | | Humanities | STEM | Social Sciences | Other | Average |
|---|---|---|---|---|---|---|
| GPT-NeoX | 20B | 29.8 | 34.9 | 33.7 | 37.7 | 33.6 |
| GPT-3 | 175B | 40.8 | 36.7 | 50.4 | 48.8 | 43.9 |
| Gopher | 280B | 56.2 | 47.4 | 71.9 | 66.1 | 60.0 |
| Chinchilla | 70B | 63.6 | 54.9 | 79.3 | **73.9** | 67.5 |
| | | | | | | |
| PaLM | 8B | 25.6 | 23.8 | 24.1 | 27.8 | 25.4 |
| PaLM | 62B | 59.5 | 41.9 | 62.7 | 55.8 | 53.7 |
| PaLM | 540B | **77.0** | **55.6** | **81.0** | 69.6 | **69.3** |
| | | | | | | |
| LLaMA | 7B | 34.0 | 30.5 | 38.3 | 38.1 | 35.1 |
| LLaMA | 13B | 45.0 | 35.8 | 53.8 | 53.3 | 46.9 |
| LLaMA | 33B | 55.8 | 46.0 | 66.7 | 63.4 | 57.8 |
| LLaMA | 65B | 61.8 | 51.7 | 72.9 | 67.4 | 63.4 |

On this benchmark, LLaMA-65B is behind both Chinchilla-70B and PaLM-540B by a few percent in average, and across most domains. A potential explanation is that a limited amount of books and academic papers is used in the pre-training data, i.e., ArXiv, Gutenberg and Books3, that sums up to only 177GB, while these models were trained on up to 2TB of books. This large quantity of books used by Gopher, Chinchilla and PaLM may also explain why Gopher outperforms GPT-3 on this benchmark, while it is comparable on other benchmarks. [p. 6-7]

## 3.7 Evolution of performance during training

[p. 7] During training, the performance of the models was tracked on a few question answering and common sense benchmarks, reported in Figure 2. On most benchmarks, the performance improves steadily, and correlates with the training perplexity of the model (see Figure 1). The exceptions are SIQA and WinoGrande. Most notably, on SIQA, a lot of variance in performance is observed, which may indicate that this benchmark is not reliable. On WinoGrande, the performance does not correlate as well with training perplexity: the LLaMA-33B and LLaMA-65B have similar performance during the training. [p. 7]

**Figure 2** (p. 8): "Evolution of performance on question answering and common sense reasoning during training."
Six subplots showing accuracy (y-axis) vs. billion tokens trained (x-axis, 0-1500) for LLaMA 7B, 13B, 33B, 65B and Chinchilla (dashed line). Subplots: TriviaQA (accuracy ~20-70, all LLaMA sizes improve steadily, LLaMA-65B approaches Chinchilla), HellaSwag (~50-84, steady improvement), NaturalQuestions (~0-35, steady improvement), SIQA (~40-52, high variance, no clear trend with scale), WinoGrande (~50-78, LLaMA-33B and 65B converge to similar performance), PIQA (~65-82.5, steady improvement). On all subplots, larger models achieve higher accuracy, and performance generally improves monotonically with training tokens, except SIQA which shows instability.
