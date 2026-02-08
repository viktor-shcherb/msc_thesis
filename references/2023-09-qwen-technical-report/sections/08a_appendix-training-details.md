# A Appendix [p. 36]

## A.1 More Training Details [p. 36]

### A.1.1 Data Format for QWEN-CHAT [p. 36]

[p. 36] Different from conventional pretraining based on autoregressive next-token prediction, despite using a similar training task, there should be a specially designed data format for SFT and RLHF to build a conversational AI assistant model. Common formats include "human-assistant" and ChatML formats.

One of the earliest examples of the human-assistant format comes from Anthropic (Bai et al., 2022b), which adds a special phrase `"\n\nhuman: "` in front of the user input and `"\n\nassistant: "` in front of the assistant response. It is easy for the base language model to transfer to the pattern of conversational AI. However, as the specific phrases are common words, it might be hard for the model to disambiguate from these words in other contexts.

Instead, the authors turned to the ChatML format proposed by OpenAI (footnote 5, p. 36). This format allows the use of special tokens, i.e., `"<im_start>"` and `"<im_end>"`, that do not appear in pretraining, and thus resolve the aforementioned problem.

**ChatML Format example:**

```
<|im_start|>system
You are a helpful assistant.<|im_end|>
<|im_start|>user
Hello!<|im_end|>
<|im_start|>assistant
Hello! How can I assist you today?<|im_end|>
```

## A.2 Evaluation [p. 36]

### A.2.1 Automatic Evaluation [p. 36]

[p. 36] To provide a whole picture of the performance of the QWEN model series, detailed performance of the models as well as baselines is illustrated in the comprehensive benchmark evaluation proposed by OpenCompass Team (2023). Results are reported in multiple tables based on the officially provided categories, including examination, language, knowledge, understanding, and reasoning. In terms of the performance of the baseline models, the higher results between the reported ones and those on the leaderboard are reported.

**Examination** [p. 36] The models are evaluated on a series of datasets relevant to examination. The datasets include:

- **MMLU** (Hendrycks et al., 2020): Massive Multi-task Language Understanding is designed for measuring language understanding capabilities. 5-shot results reported.
- **C-Eval** (Huang et al., 2023): A Chinese evaluation dataset spanning 52 diverse disciplines. 5-shot results reported.
- **CMMLU** (Li et al., 2023c): Designed for assessing language understanding capabilities in Chinese. 5-shot results reported.
- **AGIEval** (Zhong et al., 2023a): A benchmark consisting of human-centric examinations, including college entrance exams, law school admission tests, math competitions, and lawyer qualification tests. Zero-shot results reported.
- **Gaokao-Bench** (Zhang et al., 2023b): A benchmark with Gaokao (Chinese college-entrance examination) questions. Zero-shot results reported.
- **ARC** (Clark et al., 2018): A dataset consisting of grade-school level, multiple-choice science questions. It includes an easy set and a challenge set, referred to as ARC-e and ARC-c. Zero-shot results reported.

---
[p. 37 continued]

In terms of MMLU, the detailed results are reported in Table 13. In terms of C-Eval, the results are reported in Table 14. For the rest of the datasets, the results are reported in Table 15. Note that AGIEval includes the parts of Chinese and English, while LLAMA 2 only reported the results in the English part, so the results on OpenCompass are used. Additionally, while CMMLU, AGIEval, and Gaokao-Bench are related to Chinese, and MPT, Falcon, and the LLaMA series were not optimized for Chinese, these models achieved low performance on the datasets. [p. 38]

**Table 13: Results on MMLU.** All are tested with five-shot accuracy. Reported results of the other models are provided for comparison. [p. 37]

| Model | Params | Average | STEM | Social Sciences | Humanities | Others |
|---|---|---|---|---|---|---|
| MPT | 7B | 26.8 | 25.3 | 27.1 | 26.7 | 28.2 |
| MPT | 30B | 46.9 | 39.0 | 52.8 | 44.5 | 52.9 |
| Falcon | 7B | 26.2 | 26.2 | 24.7 | 26.4 | 27.4 |
| Falcon | 40B | 55.4 | 45.5 | 65.4 | 49.3 | 65.0 |
| ChatGLM2 | 6B | 47.9 | 41.2 | 54.4 | 43.7 | 54.5 |
| ChatGLM2 | 12B | 56.2 | 48.2 | 65.1 | 52.6 | 60.9 |
| InternLM | 7B | 51.0 | - | - | - | - |
| Baichuan2 | 7B | 54.2 | - | - | - | - |
| Baichuan2 | 13B | 59.2 | - | - | - | - |
| XVERSE | 13B | 55.1 | 44.5 | 64.4 | 50.5 | 62.9 |
| LLaMA | 7B | 35.1 | 30.5 | 38.3 | 34.0 | 38.1 |
| LLaMA | 13B | 46.9 | 35.8 | 53.8 | 45.0 | 53.3 |
| LLaMA | 33B | 57.8 | 46.0 | 66.7 | 55.8 | 63.4 |
| LLaMA | 65B | 63.4 | 51.7 | 72.9 | 61.8 | 67.4 |
| LLAMA 2 | 7B | 45.3 | 36.4 | 51.2 | 42.9 | 52.2 |
| LLAMA 2 | 13B | 54.8 | 44.1 | 62.6 | 52.8 | 61.1 |
| LLAMA 2 | 34B | 62.6 | 52.1 | 71.8 | 59.4 | 69.2 |
| LLAMA 2 | 70B | 68.9 | 58.0 | 80.3 | 65.0 | 74.6 |
| QWEN | 1.8B | 44.6 | 39.6 | 50.0 | 40.4 | 51.0 |
| QWEN | 7B | 58.2 | 50.2 | 68.6 | 52.5 | 64.9 |
| QWEN | 14B | **66.3** | **59.4** | **76.2** | **60.9** | **71.8** |

**Table 14: Leaderboard results of C-Eval.** Results of both proprietary models and open-source models are included. Note that there are a number of models on the leaderboard with very few details; in terms of proprietary models, only the results of GPT-3.5, GPT-4, InternLM and ChatGLM2 are reported. [p. 37]

*Proprietary models:*

| Model | Params | Avg. | Avg. (Hard) | STEM | Social Sciences | Humanities | Others |
|---|---|---|---|---|---|---|---|
| GPT-3.5 | - | 54.4 | 41.4 | 52.9 | 61.8 | 50.9 | 53.6 |
| GPT-4 | - | 68.7 | **54.9** | **67.1** | 77.6 | 64.5 | 67.8 |
| InternLM | 123B | 68.8 | 50.0 | 63.5 | 81.4 | 72.7 | 63.0 |
| ChatGLM2 | - | **71.1** | 50.0 | 64.4 | **81.6** | **73.7** | **71.3** |

*Open-source models:*

| Model | Params | Avg. | Avg. (Hard) | STEM | Social Sciences | Humanities | Others |
|---|---|---|---|---|---|---|---|
| ChatGLM2 | 6B | 51.7 | 37.1 | 48.6 | 60.5 | 51.3 | 49.8 |
| InternLM | 7B | 52.8 | 37.1 | 48.0 | 67.4 | 55.4 | 45.8 |
| Baichuan2 | 7B | 54.0 | - | - | - | - | - |
| Baichuan2 | 13B | 58.1 | - | - | - | - | - |
| XVERSE | 13B | 54.7 | 33.5 | 45.6 | 66.2 | 58.3 | 56.9 |
| QWEN | 1.8B | 54.7 | 41.8 | 50.8 | 69.9 | 56.3 | 46.2 |
| QWEN | 7B | 63.5 | 46.4 | 57.7 | 78.1 | 66.6 | 57.8 |
| QWEN | 14B | **72.1** | **53.7** | **65.7** | **85.4** | **75.3** | **68.4** |

**Table 15: Results on the other datasets of examination.** Specifically, results on CMMLU, AGIEval, ARC-e, and ARC-c are reported. [p. 38]

| Model | Params | CMMLU | AGIEval | Gaokao-Bench | ARC-e | ARC-c |
|---|---|---|---|---|---|---|
| MPT | 7B | 25.9 | 21.3 | 19.8 | 70.2 | 42.6 |
| Falcon | 7B | - | - | - | 70.0 | 42.4 |
| ChatGLM2 | 6B | 49.3 | 39.0 | 46.4 | 73.0 | 61.0 |
| InternLM | 7B | 51.8 | 36.9 | 43.0 | 78.7 | 69.5 |
| InternLM | 20B | 59.0 | 44.6 | 45.5 | 86.1 | 81.7 |
| Baichuan2 | 7B | 57.1 | 42.7 | 47.5 | 54.7 | 32.5 |
| Baichuan2 | 13B | 62.0 | 48.2 | 54.3 | 61.9 | 38.0 |
| LLaMA | 7B | 26.8 | 20.6 | 21.3 | 72.3 | 47.6 |
| LLaMA | 13B | 31.5 | 22.0 | 20.4 | 74.8 | 52.7 |
| LLaMA | 33B | 36.0 | 33.5 | 18.9 | 80.0 | 67.5 |
| LLaMA | 65B | 40.6 | 33.9 | 19.1 | 80.6 | 69.5 |
| LLAMA 2 | 7B | 31.8 | 21.8 | 18.9 | 75.2 | 45.9 |
| LLAMA 2 | 13B | 38.4 | 30.9 | 18.2 | 77.3 | 60.3 |
| LLAMA 2 | 70B | 53.6 | 40.2 | 23.3 | 85.9 | 78.3 |
| StableBeluga2 | 70B | 51.8 | 41.6 | 40.9 | 91.2 | 86.1 |
| QWEN | 1.8B | 49.3 | 36.9 | 44.9 | 71.6 | 53.2 |
| QWEN | 7B | 62.2 | 45.8 | 52.5 | 84.0 | 75.3 |
| QWEN | 14B | **71.0** | **52.3** | **61.9** | **90.3** | **84.4** |

**Knowledge and Understanding** [p. 38] The models are evaluated on a series of datasets relevant to knowledge and natural language understanding. The datasets include:

- **BoolQ** (Clark et al., 2019): A QA dataset where the questions are about passages of Wikipedia, and the model should answer yes or no to the given possible answer. Zero-shot results reported.
- **CommonsenseQA** (Talmor et al., 2019): A dataset of multiple-choice question answering that assesses the understanding of commonsense knowledge. 8-shot results reported.
- **NaturalQuestions** (Kwiatkowski et al., 2019): A dataset of QA where the questions are from users and the answers are verified by experts. Zero-shot results reported.
- **LAMBADA** (Paperno et al., 2016): A dataset to evaluate language understanding by word prediction. It consists of passages related to human subjects. Zero-shot results reported.

Results are reported in Table 16.

**Table 16: Results on the datasets concerning knowledge and understanding.** Specifically, results on BoolQ, CommonsenseQA, NaturalQuestions, and LAMBADA are reported. [p. 39]

| Model | Params | BoolQ | CommonsenseQA | NaturalQuestions | LAMBADA |
|---|---|---|---|---|---|
| MPT | 7B | 75.0 | 61.8 | 11.6 | 70.0 |
| Falcon | 7B | 67.5 | 20.8 | 15.7 | - |
| ChatGLM2 | 6B | 79.0 | 65.4 | 9.7 | 54.3 |
| InternLM | 7B | 64.1 | 59.8 | 8.9 | 67.0 |
| InternLM | 20B | 87.5 | 70.6 | 25.2 | 71.8 |
| XVERSE | 13B | 64.2 | 62.2 | 0.3 | 48.2 |
| Baichuan2 | 7B | 63.2 | 63.0 | 9.4 | 73.3 |
| Baichuan2 | 13B | 67.0 | 65.6 | 16.3 | 74.0 |
| LLaMA | 7B | 76.5 | 64.9 | 16.8 | 73.3 |
| LLaMA | 13B | 78.7 | 67.4 | 20.2 | 75.2 |
| LLaMA | 33B | 84.4 | 72.5 | 30.9 | 77.2 |
| LLaMA | 65B | 86.6 | 74.1 | 33.4 | 77.7 |
| LLAMA 2 | 7B | 77.4 | 66.5 | 19.1 | 73.3 |
| LLAMA 2 | 13B | 82.4 | 67.3 | **24.9** | **76.5** |
| LLAMA 2 | 70B | 87.7 | 78.5 | 34.2 | 78.9 |
| StableBeluga2 | 70B | 89.4 | 72.6 | 25.1 | 71.3 |
| QWEN | 1.8B | 68.0 | 60.1 | 3.2 | 58.4 |
| QWEN | 7B | 76.4 | 66.8 | 17.4 | 67.9 |
| QWEN | 14B | **86.2** | **70.3** | 23.9 | 71.1 |

**Reasoning** [p. 38–39] The evaluation results on the datasets concerning reasoning are reported, focusing on natural language reasoning. For the others, such as mathematics and coding, as those detailed results have already been illustrated, they are not reported here repeatedly. The datasets for evaluation include:

- **HellaSwag** (Zellers et al., 2019): A commonsense natural language inference (NLI) dataset, where the questions are easy for humans but struggling for previous language models. Zero-shot results reported.
- **PIQA** (Bisk et al., 2020): An NLI dataset assessing physical knowledge. Zero-shot results reported.
- **SIQA** (Sap et al., 2019): An NLI dataset evaluating social commonsense intelligence. Zero-shot results reported. [p. 39]
- **OCNLI** (Hu et al., 2020): An NLI dataset focusing on Chinese. Zero-shot results reported. [p. 39]

Results are reported in Table 17.

**Table 17: Results on the datasets related to natural language reasoning.** Specifically, results on HellaSwag, PIQA, SIQA, and OCNLI are reported. [p. 39]

| Model | Params | HellaSwag | PIQA | SIQA | OCNLI |
|---|---|---|---|---|---|
| MPT | 7B | 76.4 | 80.6 | 48.5 | 30.0 |
| Falcon | 7B | 74.1 | 76.7 | 47.2 | - |
| ChatGLM2 | 6B | 57.0 | 69.6 | 64.3 | 33.1 |
| InternLM | 7B | 70.6 | 77.9 | 60.5 | 37.5 |
| InternLM | 20B | 78.1 | 80.3 | 72.8 | 42.5 |
| Baichuan2 | 7B | 67.0 | 76.2 | 44.4 | 30.3 |
| Baichuan2 | 13B | 70.8 | 78.1 | 44.3 | 30.0 |
| LLaMA | 7B | 76.1 | 79.8 | 48.9 | 33.6 |
| LLaMA | 13B | 79.2 | 80.1 | 52.5 | 32.1 |
| LLaMA | 33B | 82.8 | 82.3 | 57.8 | 30.7 |
| LLaMA | 65B | 84.2 | 82.8 | 61.2 | 44.9 |
| LLAMA 2 | 7B | 77.2 | 78.8 | 48.5 | 32.1 |
| LLAMA 2 | 13B | 80.7 | 80.5 | 54.8 | 34.1 |
| LLAMA 2 | 70B | 85.3 | 82.8 | 64.8 | 46.5 |
| StableBeluga2 | 70B | 84.1 | 83.3 | 78.1 | 48.3 |
| QWEN | 1.8B | 56.7 | 73.3 | 56.1 | 39.0 |
| QWEN | 7B | 75.1 | 77.9 | 69.9 | 47.4 |
| QWEN | 14B | 79.9 | 77.9 | 77.9 | 57.9 |
