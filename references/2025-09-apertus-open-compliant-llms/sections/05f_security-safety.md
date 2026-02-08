# 5.5 Security And Safety [p. 49–51]

## 5.5.1 General Considerations [p. 49]

[p. 49] As a highly multilingual, fully open model, the safety and security testing of the Apertus model family presents several unique challenges.

**Open-weight.** As an open-weight model family, any security and safety guardrails imparted into the model during pretraining can be reverted through post-training (e.g., Team, 2025). Hence, it cannot be assumed that access to potentially dangerous information acquired by the model from the pretraining data can be mitigated through safety alignment alone. As a result, data compliance measures (e.g., author opt-outs, PII filtering, toxicity filtering) were already implemented *a priori*, during pretraining data construction (Section 3.1).

**Massively Multilingual.** As a highly multilingual model family, Apertus's security and safety should be maintained across supported languages. This task is challenging, given that most safety and security work focuses almost exclusively on English, resulting in poor generalization to other languages (Wang et al., 2024), and in translations serving as effective jailbreaks (Deng et al., 2024; Yong et al., 2023). Consequently, the authors test the safety of their model on available multilingual safety benchmarks (Ning et al., 2025), but still fall short on all languages used in pretraining and post-training datasets.

[p. 49] An additional challenge with massively multilingual models is their novel capacity for information operations in low-resource languages (Kucharavy et al., 2023; Goldstein et al., 2023). Consequently, the authors conducted manual tests for several high-risk scenarios (Section 5.6).

**Helpfulness vs. Safety.** As the Apertus models are intended for wide adoption, they must be useful to broad communities of users. Given that there is a trade-off between model harmlessness and usefulness after tuning (Bai et al., 2022a;b; Röttger et al., 2024), an excessive safety and security emphasis is likely to impede the model utility. This trade-off also means that potentially harmful behaviours are impossible to suppress without making the model useless for certain applications. Consequently, the authors seek a balance in the development between these two properties. Notably, given the post-training guardrail removal risk mentioned above, jailbreak resistance is not pursued, given that it must be delegated to guardrails in production (Majumdar & Vogelsang, 2024).

## 5.5.2 Safety Benchmark Performance [p. 49–51]

[p. 49] Based on the principles outlined above, safety testing is performed using the following benchmarks:

**BBQ** is an English-language common harmful social bias evaluation benchmark (Parrish et al., 2022). It is constructed to elicit implicit biases on common discrimination categories (e.g., Age, Disability, Gender, Ethnicity, etc.), probing for bias in question-answers known to elicit harmful bias. The Apertus-Instruct family performs comparably to other fully-open models, though a bit worse than state-of-the-art open-weight models.

**HarmBench** is a standardized LLM harmful behaviour elicitation benchmark, covering 8 classes of harmful behaviour (Bioweapon, Harassment, General Harm, Chemweapon, Cybercrime, Misinformation, Copyright, Illegal Act; Mazeika et al., 2024). On HarmBench, the Apertus-Instruct family performs worse than most other fully open models, but in line with open-weight models. However, on Direct Requests, the Apertus-Instruct family performs comparably to other fully-open models and better than most open-weight models tested (with the exception of Qwen). Including human jailbreaks, the most basic approaches to LLM jailbreaking, also indicates a performance of the Apertus-Instruct family in line with most open-weight models tested (excluding Qwen).

---
[p. 50 continued]

**Table 26: Post-training Evaluation: Performance of Apertus models on benchmarks assessing safety and security.** The arrows (up, down) show the desired direction for each benchmark.

| Model | BBQ (up) | ToxiGen (up) | HarmBench (down) | HarmBench Direct Request (down) | HarmBench Human Jailbreaks (down) | RealToxicityPrompts LLaMA-Guard3 Subsampled (down) |
|---|---|---|---|---|---|---|
| **Fully Open Models** | | | | | | |
| **Apertus-70B-Instruct** | 67.4 | 70.3 | 31.9 | 10.3 | 36.2 | 0.2 |
| **Apertus-8B-Instruct** | 63.9 | 80.2 | 35.2 | 16.2 | 39.0 | 0.2 |
| ALLaM-7B-Instruct-preview | 57.7 | 84.3 | 7.0 | 2.8 | 7.9 | 1.6 |
| EuroLLM-22B-Instruct-Preview | 66.3 | 82.3 | 8.0 | 5.3 | 8.5 | 0.2 |
| EuroLLM-9B-Instruct | 65.0 | 51.5 | 6.0 | 3.4 | 6.6 | 0.0 |
| K2-Chat | 68.4 | 83.2 | 24.1 | 15.3 | 25.9 | 1.0 |
| marin-8b-instruct | 70.7 | 66.0 | 5.1 | 5.6 | 5.0 | 0.1 |
| Minerva-7B-instruct-v1.0 | 45.7 | 50.7 | 33.9 | 23.8 | 35.9 | 1.3 |
| OLMo-2-0325-32B-Instruct | 76.6 | 78.0 | 22.5 | 9.7 | 25.1 | 0.4 |
| OLMo-2-1124-7B-Instruct | 63.8 | 85.1 | 10.7 | 4.1 | 12.0 | 0.4 |
| salamandra-7b-instruct | 63.9 | 81.3 | 14.5 | 10.3 | 15.4 | 4.2 |
| SmolLM3-3B | 69.5 | 56.7 | 51.1 | 50.6 | 51.2 | 1.7 |
| Teuken-7B-instruct-v0.6 | 57.9 | 56.8 | 45.3 | 53.3 | 43.7 | 0.5 |
| **Open-Weight Models** | | | | | | |
| gemma-3-12b-it | 75.2 | 86.7 | 42.2 | 25.0 | 45.7 | 0.3 |
| gemma-3-27b-it | 74.5 | 86.3 | 49.4 | 29.1 | 53.5 | 0.1 |
| Llama-3.1-8B-Instruct | 73.6 | 84.7 | 38.1 | 18.8 | 42.0 | 0.4 |
| Llama-3.3-70B-Instruct | 72.0 | 87.4 | 38.8 | 24.7 | 41.6 | 0.5 |
| Qwen2.5-72B-Instruct | 70.8 | 86.2 | 10.6 | 13.1 | 10.1 | 0.0 |
| Qwen3-32B | 78.4 | 85.9 | 12.0 | 11.6 | 12.1 | 0.1 |
| Qwen3-8B | 72.9 | 84.0 | 16.2 | 10.3 | 17.4 | 0.2 |

**RealToxicityPrompts** [p. 49–50] is one of the most widely used benchmarks for unprompted toxicity generation in LLMs, considered as representative of real-world usage scenarios in English (Gehman et al., 2020). To integrate it into the benchmark harness, it was sub-sampled to 10% of its size and the toxicity classifier model was switched to Llama-Guard-3-8B (Fedorov et al., 2024) to allow fully-contained execution. This subsample is released^48 as well as the LLaMA-Guard-3-8B implementation.^49 The resulting benchmark, *RealToxicityPrompts-Llama-Subsampled*, while quicker for evaluation, cannot be directly compared with the standard *RealToxicityPrompts* benchmark results. Overall, Apertus models perform well in comparison to other both fully open and open-weight models.

^48: https://huggingface.co/datasets/swiss-ai/realtoxicityprompts/tree/main/realtoxicityprompts_small
^49: LLaMA-Guard-3-8B Implementation

**ToxiGen** [p. 50] is an English benchmark for evaluating the implicit toxicity of LLM generations, as well as the ability of a model to identify that implicit toxicity (Hartvigsen et al., 2022). The version of ToxiGen for evaluating the ability of a model to accurately identify implicit toxicity on a balanced dataset is used. Overall, the family of Apertus-Instruct models is in line with the rest of the fully-open models tested, but performs worse than all open-weight models tested.

**LinguaSafe** [p. 50–51] is a recent multilingual LLM safety benchmark (Ning et al., 2025) across 5 classes and 12 languages: (1) *Crimes*, (2) *Explicit Content*, (3) *Fairness*, (4) *Harm*, and (5) *Privacy*. This benchmark separates detected harmful responses by harm class and language, and includes several mid- and low-resource languages. While Ning et al. (2025) do not report direct evaluation of security-weighted scores (as done in this work), the direct and indirect mean weighted scores are in the range of 21-45% for open-weight models.

**Table 27: Severity-weighted scores for Apertus-70B-Instruct for each harm category across 12 languages.** Lower scores indicate better performance at detecting and handling harmful content. [p. 51]

| Harm Category | ar | bn | cs | en | hu | ko | ms | ru | sr | th | vi | zh |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Crimes & Illegal | 41.14 | 40.83 | 39.84 | 39.09 | 40.28 | 43.99 | 40.21 | 39.76 | 39.16 | 39.39 | 38.14 | 39.66 |
| Explicit Content | 48.67 | 49.33 | 48.20 | 49.56 | 48.93 | 47.91 | 50.39 | 48.06 | 45.04 | 51.70 | 49.56 | 47.76 |
| Fairness & Justice | 56.30 | 50.00 | 55.95 | 57.76 | 55.99 | 51.86 | 54.54 | 56.87 | 54.58 | 56.07 | 57.21 | 56.45 |
| Harm & Misuse | 40.64 | 41.86 | 42.37 | 42.01 | 40.78 | 41.17 | 41.83 | 41.80 | 41.81 | 42.27 | 41.66 | 42.33 |
| Privacy & Property | 49.29 | 50.77 | 52.60 | 55.42 | 57.07 | 51.98 | 54.06 | 51.59 | 52.82 | 54.94 | 51.18 | 52.35 |

**Table 28: Severity-weighted scores for Apertus-8B-Instruct for each harm category across 12 languages.** Lower scores indicate better performance at detecting and handling harmful content. [p. 51]

| Harm Category | ar | bn | cs | en | hu | ko | ms | ru | sr | th | vi | zh |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Crimes & Illegal | 44.64 | 46.10 | 45.50 | 42.46 | 47.26 | 47.29 | 47.41 | 44.18 | 46.06 | 44.09 | 42.80 | 43.11 |
| Explicit Content | 49.58 | 54.79 | 51.83 | 51.11 | 54.62 | 50.42 | 52.99 | 48.14 | 49.18 | 54.81 | 53.44 | 51.25 |
| Fairness & Justice | 59.05 | 59.83 | 61.46 | 59.09 | 61.96 | 59.88 | 62.64 | 59.53 | 63.98 | 59.49 | 61.72 | 59.91 |
| Harm & Misuse | 41.57 | 42.39 | 44.65 | 43.99 | 43.46 | 42.19 | 44.80 | 41.98 | 45.58 | 43.13 | 43.32 | 40.94 |
| Privacy & Property | 52.48 | 55.32 | 59.25 | 58.31 | 58.05 | 55.43 | 55.26 | 54.86 | 60.53 | 53.85 | 55.52 | 51.77 |
