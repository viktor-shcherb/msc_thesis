# 5 Results [p. 28–31]

[p. 28] An extensive series of evaluations of Llama 3 is performed, investigating the performance of: **(1)** the pre-trained language model, **(2)** the post-trained language model, and **(3)** the safety characteristics of Llama 3. The results of these evaluations are presented in separate subsections.

## 5.1 Pre-trained Language Model [p. 28]

[p. 28] Evaluation results for the pre-trained Llama 3 (Section 3) are reported, comparing with various other models of comparable sizes. Results of competitor models are reproduced whenever possible. For non-Llama models, the best score across results that are publicly reported or (where possible) reproduced is reported. The specifics of these evaluations, including configurations such as the number of shots, metrics, and other pertinent hyperparameters and settings, can be accessed on the GitHub repository. The data generated as part of evaluations with publicly available benchmarks is also being released on Huggingface. The quality of the models is evaluated on standard benchmarks (Section 5.1.1), for robustness to changes in multiple-choice question setups (Section 5.1.2), and on adversarial evaluations (Section 5.1.3). A contamination analysis to estimate the extent to which evaluations are impacted by contamination of training data (Section 5.1.4) is also conducted.

### 5.1.1 Standard Benchmarks [p. 28–31]

[p. 28–29] Llama 3 is evaluated on a large number of standard benchmark evaluations shown in Table 8. These evaluations cover eight top-level categories: **(1)** commonsense reasoning; **(2)** knowledge; **(3)** reading comprehension; **(4)** math, reasoning, and problem solving; **(5)** long context; **(6)** code; **(7)** adversarial evaluations; and **(8)** aggregate evaluations.

**Table 8** (p. 29): "Pre-training benchmarks by category. Overview of all benchmarks we use to evaluate pre-trained Llama 3 models, grouped by capability category."

| Category | Benchmarks |
|---|---|
| Reading Comprehension | SQuAD V2 (Rajpurkar et al., 2018), QuAC (Choi et al., 2018), RACE (Lai et al., 2017) |
| Code | HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021) |
| Commonsense reasoning/understanding | CommonSenseQA (Talmor et al., 2019), PiQA (Bisk et al., 2020), SiQA (Sap et al., 2019), OpenBookQA (Mihaylov et al., 2018), WinoGrande (Sakaguchi et al., 2021) |
| Math, reasoning, and problem solving | GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021b), ARC Challenge (Clark et al., 2018), DROP (Dua et al., 2019), WorldSense (Benchekroun et al., 2023) |
| Adversarial | Adv SQuAD (Jia and Liang, 2017), Dynabench SQuAD (Kiela et al., 2021), GSM-Plus (Li et al., 2024c), PAWS (Zhang et al., 2019) |
| Long context | QuALITY (Pang et al., 2022), many-shot GSM8K (An et al., 2023a) |
| Aggregate | MMLU (Hendrycks et al., 2021a), MMLU-Pro (Wang et al., 2024b), AGIEval (Zhong et al., 2023), BIG-Bench Hard (Suzgun et al., 2023) |

**Experimental setup.** [p. 29] For each benchmark, scores for Llama 3 are computed as well as various other pre-trained models of comparable sizes. Where possible, numbers are recomputed with the same pipeline for other models. To ensure a fair comparison, the best score between the computed score and the reported number for that model with comparable or more conservative settings is selected. For some models, it is not possible to (re)compute benchmark values, for instance, because the pre-trained model is not released or because the API does not provide access to log-probabilities. In particular, this is true for all models comparable to Llama 3 405B. Thus, category averages for Llama 3 405B are not reported, which requires that all numbers are available for all benchmarks.

**Significance estimates.** [p. 29] Benchmark scores are estimates of a model's true performance. These estimates have variance because benchmark sets are finite samples drawn from some underlying distribution. Following Madaan et al. (2024b), variance is reported via 95% confidence intervals (CIs), assuming that benchmark scores are Gaussian distributed. While this assumption is incorrect (e.g., benchmark scores are bounded), preliminary bootstrap experiments suggest CIs (for discrete metrics) are a good approximation:

$$CI(S) = 1.96 \times \sqrt{\frac{S \times (1 - S)}{N}}$$

where $S$ is the observed benchmark score (e.g., accuracy or EM) and $N$ the sample size of the benchmark. CIs for benchmark scores that are not simple averages are omitted. Because subsampling is not the only source of variation, CI values lower bound the actual variation in the capability estimate. [p. 29]

**Results for 8B and 70B models.** [p. 29] Figure 12 reports the average performance of Llama 3 8B and 70B on the commonsense reasoning, knowledge, reading comprehension, math and reasoning, and code benchmarks. The results show that Llama 3 8B outperforms competing models in virtually every category, both in terms of per-category win rate and in terms of average per-category performance. Llama 3 70B outperforms its predecessor Llama 2 70B by a large margin on most benchmarks, with the exception of commonsense benchmarks that are likely saturated. Llama 3 70B also outperforms Mixtral 8x22B.

### Figure 12 [p. 30]

**Figure 12** (p. 30): "Performance of pre-trained Llama 3 8B and 70B models on pre-training benchmarks. Results are aggregated by capability category by averaging accuracies across all benchmarks corresponding to that category."

The figure contains two bar charts side by side. The left chart compares ~7B-class models: Llama 2 7B, Llama 3 8B, Mistral 7B, and Gemma 7B across five categories (General/Commonsense, Knowledge, Math and Reasoning, Reading Comprehension, Code). Llama 3 8B (dark blue) achieves the highest bars in most categories, with particularly strong leads in Knowledge, Math and Reasoning, and Code. The right chart compares ~70B-class models: Llama 2 70B, Llama 3 70B, and Mixtral 8x22B. Llama 3 70B (dark blue) leads across all categories, with the largest gap visible in Math and Reasoning and Code (both exceeding ~80), while commonsense benchmarks are clustered tightly around 80-85 across all models.

**Detailed results for all models.** [p. 29–31] Tables 9, 10, 11, 12, 13, and 14 present the benchmark performance of pre-trained Llama 3 8B, 70B, and 405B models on reading comprehension tasks, coding tasks, commonsense understanding tasks, mathematical reasoning tasks, and general tasks. The tables compare Llama 3's performance with that of models of similar size. In particular, Llama 3 405B performs competitively with other models in its class. For long-context, more comprehensive results (including probing tasks like needle-in-a-haystack) are presented in Section 5.2.

**Table 9** (p. 30): "Pre-trained model performance on reading comprehension tasks. Results include 95% confidence intervals."

| | SQuAD | QuAC | RACE |
|---|---|---|---|
| Llama 3 8B | 77.0 +/-0.8 | 44.9 +/-1.1 | 54.3 +/-1.4 |
| Mistral 7B | 73.2 +/-0.8 | 44.7 +/-1.1 | 53.0 +/-1.4 |
| Gemma 7B | **81.8** +/-0.7 | 42.4 +/-1.1 | 48.8 +/-1.4 |
| Llama 3 70B | 81.8 +/-0.7 | **51.1** +/-1.1 | 59.0 +/-1.4 |
| Mixtral 8x22B | **84.1** +/-0.7 | 44.9 +/-1.1 | **59.2** +/-1.4 |
| Llama 3 405B | **81.8** +/-0.7 | **53.6** +/-1.1 | **58.1** +/-1.4 |
| GPT-4 | -- | -- | -- |
| Nemotron 4 340B | -- | -- | -- |
| Gemini Ultra | -- | -- | -- |

**Table 10** (p. 30): "Pre-trained model performance on coding tasks. Results include 95% confidence intervals."

| | HumanEval | MBPP |
|---|---|---|
| Llama 3 8B | **37.2** +/-7.4 | **47.6** +/-4.4 |
| Mistral 7B | 30.5 +/-7.0 | 47.5 +/-4.4 |
| Gemma 7B | 32.3 +/-7.2 | 44.4 +/-4.4 |
| Llama 3 70B | **58.5** +/-7.5 | 66.2 +/-4.1 |
| Mixtral 8x22B | 45.1 +/-7.6 | **71.2** +/-4.0 |
| Llama 3 405B | 61.0 +/-7.5 | **73.4** +/-3.9 |
| GPT-4 | 67.0 +/-7.2 | -- |
| Nemotron 4 340B | 57.3 +/-7.6 | -- |
| Gemini Ultra | **74.4** +/-6.7 | -- |

**Table 11** (p. 31): "Pre-trained model performance on commonsense understanding tasks. Results include 95% confidence intervals."

| | CommonSenseQA | PiQA | SiQA | OpenBookQA | Winogrande |
|---|---|---|---|---|---|
| Llama 3 8B | **75.0** +/-2.5 | 81.0 +/-1.8 | 49.5 +/-2.2 | 45.0 +/-4.4 | 75.7 +/-2.0 |
| Mistral 7B | 71.2 +/-2.6 | **83.0** +/-1.7 | 48.2 +/-2.2 | 47.8 +/-4.4 | **78.1** +/-1.9 |
| Gemma 7B | 74.4 +/-2.5 | 81.5 +/-1.8 | **51.8** +/-2.2 | **52.8** +/-4.4 | 74.7 +/-2.0 |
| Llama 3 70B | **84.1** +/-2.1 | 83.8 +/-1.7 | **52.2** +/-2.2 | 47.6 +/-4.4 | 83.5 +/-1.7 |
| Mixtral 8x22B | 82.4 +/-2.2 | **85.5** +/-1.6 | 51.6 +/-2.2 | **50.8** +/-4.4 | **84.7** +/-1.7 |
| Llama 3 405B | **85.8** +/-2.0 | **85.6** +/-1.6 | **53.7** +/-2.2 | **49.2** +/-4.4 | 82.2 +/-1.8 |
| GPT-4 | -- | -- | -- | -- | 87.5 +/-1.5 |
| Nemotron 4 340B | -- | -- | -- | -- | **89.5** +/-1.4 |

**Table 12** (p. 31): "Pre-trained model performance on math and reasoning tasks. Results include 95% confidence intervals. Diamond-marked values indicate 11-shot. Triangle-marked values indicate variable shot."

| | GSM8K | MATH | ARC-C | DROP | WorldSense |
|---|---|---|---|---|---|
| Llama 3 8B | **57.2** +/-2.7 | 20.3 +/-1.1 | 79.7 +/-2.3 | **59.5** +/-1.0 | 45.5 +/-0.3 |
| Mistral 7B | 52.5 +/-2.7 | 13.1 +/-0.9 | 78.2 +/-2.4 | 53.0 +/-1.0 | 44.9 +/-0.3 |
| Gemma 7B | 46.4 +/-2.7 | **24.3** +/-1.2 | 78.6 +/-2.4 | 56.3 +/-1.0 | **46.0** +/-0.3 |
| Llama 3 70B | 83.7 +/-2.0 | 41.4 +/-1.4 | **92.9** +/-1.5 | **79.6** +/-0.8 | **61.1** +/-0.3 |
| Mixtral 8x22B | **88.4** +/-1.7 | **41.8** +/-1.4 | 91.9 +/-1.6 | 77.5 +/-0.8 | 51.5 +/-0.3 |
| Llama 3 405B | 89.0 +/-1.7 | **53.8** +/-1.4 | 96.1 +/-1.1 | **84.8** +/-0.7 | **63.7** +/-0.3 |
| GPT-4 | **92.0** +/-1.5 | -- | **96.3** +/-1.1 | 80.9 +/-0.8 | -- |
| Nemotron 4 340B | -- | -- | 94.3 +/-1.3 | -- | -- |
| Gemini Ultra | 88.9^diamond +/-1.7 | 53.2 +/-1.4 | -- | 82.4^triangle +/-0.8 | -- |

**Table 13** (p. 31): "Pre-trained model performance on general language tasks. Results include 95% confidence intervals."

| | MMLU | MMLU-Pro | AGIEval | BB Hard |
|---|---|---|---|---|
| Llama 3 8B | **66.7** | **37.1** | **47.8** +/-1.9 | **64.2** +/-1.2 |
| Mistral 7B | 63.6 | 32.5 | 42.7 +/-1.9 | 56.8 +/-1.2 |
| Gemma 7B | 64.3 | 35.1 | 46.0 +/-1.9 | 57.7 +/-1.2 |
| Llama 3 70B | **79.3** | **53.8** | **64.6** +/-1.9 | **81.6** +/-0.9 |
| Mixtral 8x22B | 77.8 | 51.5 | 61.5 +/-1.9 | 79.5 +/-1.0 |
| Llama 3 405B | 85.2 | **61.6** | **71.6** +/-1.8 | **85.9** +/-0.8 |
| GPT-4 | **86.4** | -- | -- | -- |
| Nemotron 4 340B | 81.1 | -- | -- | 85.4 +/-0.9 |
| Gemini Ultra | 83.7 | -- | -- | 83.6 +/-0.9 |

### 5.1.2 Model Robustness [p. 30]

[p. 30] In addition to performance on benchmarks, robustness is an important factor in the quality of pre-trained language models. The robustness of the pre-trained language models to design choices in multiple-choice question (MCQ) setups is investigated. Prior work has reported that model performance can be sensitive to seemingly arbitrary design choices in such setups, for example, model scores and even rankings may change with the order and labels of the in-context examples (Lu et al., 2022; Zhao et al., 2021; Robinson and Wingate, 2023; Liang et al., 2022; Gupta et al., 2024), the exact format of the prompt (Weber et al., 2023b; Mishra et al., 2022), or the answer choice format and order (Alzahrani et al., 2024; Wang et al., 2024a; Zheng et al., 2023). Motivated by this work, the MMLU benchmark is used to evaluate the robustness of the pre-trained models to: **(1)** few-shot label bias, **(2)** label variants, **(3)** answer order, and **(4)** prompt format:

- **Few-shot label bias.** [p. 30] Following Zheng et al. (2023) and Weber et al. (2023a), the impact of the distribution of labels in four-shot examples is investigated. Specifically, settings are considered in which: (1) all few-shot examples have the same label (A A A A); (2) all examples have a different label (A B C D); and (3) there are only two labels present (A A B B and C C D D).

- **Label variants.** [p. 32] Model response to different choice token sets is studied. Two sets proposed by Alzahrani et al. (2024) are considered: a set of common language independent tokens ($ & # @) and a set of rare tokens (oe S z u) that do not have any implicit relative order. Two versions of the canonical labels (A. B. C. D. and A) B) C) D)) and a numerical list (1. 2. 3. 4.) are also considered.

- **Answer order.** [p. 32] Following Wang et al. (2024a), stability of results across different answer orders is computed. All answers in the dataset are remapped according to a fixed permutation. For example, for the permutation A B C D, all answer options with label A and B keep their label, and all answer options with label C get label D, and vice versa.

- **Prompt format.** [p. 32] Variance in performance across five task prompts that differ in the level of information provided is evaluated: one prompt simply asks the model to answer the question, whereas other prompts assert the expertise of the model or that the best answer should be chosen.

**Figure 13** (p. 32): "Robustness of our pre-trained language models to different design choices in the MMLU benchmark. *Left:* Performance for different label variants. *Right:* Performance for different labels present in few-shot examples."

Left panel: A grouped bar chart showing Micro accuracy (y-axis, 30–100) for Llama 3 8B, 70B, and 405B across five label variant conditions on the x-axis: {A. B. C. D.}, {A) B) C) D)}, {1 2 3 4}, {$ & # @}, {oe S z u}. All three models show relatively stable performance across all label variants. Llama 3 405B consistently scores highest (~80–85), Llama 3 70B scores in the mid-70s, and Llama 3 8B scores in the low 60s. Performance drops slightly for the rare token labels but remains within a few percentage points.

Right panel: A grouped bar chart showing Micro accuracy for the three Llama 3 models across four few-shot label conditions: ABCD, AADD, BBCC, AAAA. Llama 3 8B shows the most sensitivity, dropping from ~80 for ABCD to ~45 for AAAA. Llama 3 70B drops from ~80 to ~65. Llama 3 405B is most robust, staying between ~80–90 across all conditions.

**Figure 14** (p. 32): "Robustness of our pre-trained language models to different design choices in the MMLU benchmark. *Left:* Performance for different answer orders. *Right:* Performance for different prompt formats."

Left panel: A scatter plot showing Micro accuracy (y-axis, 60–100) vs. model size (Llama 3 8B, 70B, 405B on x-axis) with points colored by permutation distance (0–4). For Llama 3 8B, accuracy ranges ~62–68 with spread across permutation distances. For Llama 3 70B, accuracy clusters tightly around 78–80 with some spread for higher permutation distances. For Llama 3 405B, accuracy clusters very tightly around 84–86, demonstrating high robustness. Higher permutation distances generally lead to slightly lower accuracy.

Right panel: A box plot showing Micro accuracy (y-axis, 65–85) across the three Llama 3 models for different prompt formats. Llama 3 8B has a box spanning roughly 65–67 with median ~66. Llama 3 70B has a box around 78–80 with a narrow spread. Llama 3 405B has a box around 83–85 with very tight spread, indicating the largest model is most robust to prompt format changes.

[p. 32–33] Figure 13 presents the results of experiments studying robustness of model performance to label variants and few-shot label bias. The results show that the pre-trained language models are very robust to changes in MCQ labels and to the structure of the few-shot prompt labels. This robustness is particularly pronounced for the 405B parameter model. Figure 14 presents the results of the study of robustness to answer order and prompt format. The results further underscore the robustness of the performance of the pre-trained language models, in particular, of Llama 3 405B.

### 5.1.3 Adversarial Benchmarks [p. 33]

[p. 33] In addition to the standard benchmarks, evaluation is performed on several adversarial benchmarks in three areas: question answering, mathematical reasoning, and paraphrase detection. This testing probes the model's capabilities on tasks specifically created to be challenging and can potentially also point to overfitting on benchmarks. For question answering, Adversarial SQuAD (Jia and Liang, 2017) and Dynabench SQuAD (Kiela et al., 2021) are used. For mathematical reasoning, GSM-Plus (Li et al., 2024c) is used. For paraphrase detection, PAWS (Zhang et al., 2019) is used.

**Figure 15** (p. 33): "Adversarial versus non-adversarial performance for question answering, mathematical reasoning, and paraphrase detection benchmarks. *Left:* Results for pre-trained models. *Right:* Results for post-trained models."

Both panels are scatter plots with Non-adversarial score on the x-axis (0.0–1.0) and Adversarial score on the y-axis (0.0–1.0). Points are differentiated by model size (8B small circle, 70B medium circle, 405B large circle) and by category (question answering as circles, paraphrase detection as crosses, mathematical reasoning as squares). A diagonal black line represents parity between adversarial and non-adversarial performance.

Left panel (pre-trained): Question answering points cluster around (0.7–0.85, 0.5–0.7), all below the diagonal — indicating adversarial performance is lower. Paraphrase detection points are at approximately (0.6–0.8, 0.7–0.85), near or above the diagonal. Mathematical reasoning points cluster around (0.5–0.9, 0.3–0.6), well below the diagonal.

Right panel (post-trained): Similar pattern but with generally higher scores. Paraphrase detection points are again near or above the diagonal at approximately (0.7–0.85, 0.7–0.85). Question answering and mathematical reasoning remain below the diagonal.

[p. 33] Figure 15 presents the scores of Llama 3 8B, 70B, and 405B on the adversarial benchmarks as a function of their performance on non-adversarial benchmarks. The non-adversarial benchmarks used are SQuAD (Rajpurkar et al., 2016) for question answering, GSM8K for mathematical reasoning, and QQP (Wang et al., 2017) for paraphrase detection. Each datapoint represents a pair of an adversarial and non-adversarial dataset, and all possible pairs within a category are shown. The diagonal black line represents parity between adversarial and non-adversarial datasets — being on the line would indicate the model has similar performance regardless of the adversarial nature.

[p. 33] On paraphrase detection, neither pre-trained nor post-trained models appear to suffer from the type of adversariality with which PAWS was constructed, marking a substantial step with respect to the previous generation of models. This result confirms the findings of Weber et al. (2023a), who also found that LLMs are less susceptible to the type of spurious correlations found in several adversarial datasets. For mathematical reasoning and question answering, however, the adversarial performances are substantially lower than the non-adversarial performances. This pattern is similar for pre-trained and post-trained models.

### 5.1.4 Contamination Analysis [p. 33–34]

[p. 33] A contamination analysis is conducted to estimate to what extent benchmark scores may be influenced by contamination of the evaluation data in the pre-training corpus. In previous work, several different contamination methods have been used, with various different hyperparameters — Singh et al. (2024) is referenced for an overview. Any of these methods can suffer from false positives and negatives, and how to best run contamination analyses is currently still an open field of research. The authors largely follow the suggestions of Singh et al. (2024).

**Method.** [p. 34] Singh et al. (2024) propose to select contamination detection methods empirically, based on which method results in the largest difference between the 'clean' part of the dataset and the entire dataset, which they call *estimated performance gain*. For all evaluation datasets, examples are scored based on 8-gram overlap, a method that was found by Singh et al. (2024) to be accurate for many datasets. An example of a dataset $D$ is considered to be contaminated if a ratio $\tau_D$ of its tokens are part of an 8-gram occurring at least once in the pre-training corpus. $\tau_D$ is selected separately for each dataset, based on which value shows the maximal significant estimated performance gain across the three model sizes.

**Table 14** (p. 34): "Performance of pre-trained models on long-context tasks. Results include 95% confidence intervals."

| | Llama 3 8B | Llama 3 70B | Llama 3 405B |
|---|---|---|---|
| QuALITY (5-shot) | 56.0 +/-2.1 | 82.8 +/-1.6 | 87.6 +/-1.4 |
| GSM8K (16-shot) | 60.0 +/-9.6 | 83.0 +/-7.4 | 90.0 +/-5.9 |

**Table 15** (p. 34): "Percentage of evaluation sets considered to be contaminated because similar data exists in the training corpus, and the estimated performance gain that may result from that contamination."

| Benchmark | Contam. | Perf. gain est. 8B | Perf. gain est. 70B | Perf. gain est. 405B |
|---|---|---|---|---|
| AGIEval | 98 | 8.5 | 19.9 | 16.3 |
| BIG-Bench Hard | 95 | 26.0 | 36.0 | 41.0 |
| BoolQ | 96 | 4.0 | 4.7 | 3.9 |
| CommonSenseQA | 30 | 0.1 | 0.8 | 0.6 |
| DROP | – | – | – | – |
| GSM8K | 41 | 0.0 | 0.1 | 1.3 |
| HellaSwag | 85 | 14.8 | 14.8 | 14.3 |
| HumanEval | – | – | – | – |
| MATH | 1 | 0.0 | -0.1 | -0.2 |
| MBPP | – | – | – | – |
| MMLU | – | – | – | – |
| MMLU-Pro | – | – | – | – |
| NaturalQuestions | 52 | 1.6 | 0.9 | 0.8 |
| OpenBookQA | 21 | 3.0 | 3.3 | 2.6 |
| PiQA | 55 | 8.5 | 7.9 | 8.1 |
| QuaC | 99 | 2.4 | 11.0 | 6.4 |
| RACE | – | – | – | – |
| SiQA | 63 | 2.0 | 2.3 | 2.6 |
| SQuAD | 0 | 0.0 | 0.0 | 0.0 |
| Winogrande | 6 | -0.1 | -0.1 | -0.2 |
| WorldSense | 73 | -3.1 | -0.4 | 3.9 |

**Results.** [p. 34] Table 15 reports the percentage of evaluation data that is considered contaminated for the maximal estimated performance gain, for all key benchmarks. Numbers are excluded for benchmarks where the results are not significant, for instance, because the clean or contaminated set has too few examples, or because the observed performance gain estimate shows extremely erratic behavior. For some datasets contamination has a large impact, while for others it does not. For example, for PiQA and HellaSwag, both the estimation of contamination and the estimation of performance gain are high. For Natural Questions, on the other hand, the estimated 52% contamination seems to have virtually no effect on the performance. For SQuAD and MATH, low thresholds yield high levels of contamination, but no performance gains. This suggests that contamination is either not helpful for these datasets, or that a larger n is required to obtain a better estimate. For MBPP, HumanEval, MMLU and MMLU-Pro, other contamination detection methods may be needed: even with higher thresholds, 8-gram overlap gives such high contamination scores that it is impossible to get a good performance gain estimate.

## 5.2 Post-trained Language Model [p. 34]

[p. 34] Results for the Llama 3 post-trained models on benchmarks across different capabilities are presented. Similar to pre-training, the data generated as part of evaluations with publicly available benchmarks is being released on Huggingface. Additional details on the eval setup can be found online.

**Benchmarks and metrics.** [p. 34] Table 16 contains an overview of all the benchmarks, organized by capability. Decontamination of the post-training data is applied by running exact match with the prompts from each benchmark. In addition to the standard academic benchmarks, extensive human evaluation is also performed (details in Section 5.3).

**Table 16** (p. 35): "Post-training benchmarks by category. Overview of all benchmarks we use to evaluate post-trained Llama 3 models, ordered by capability."

| Category | Benchmarks |
|---|---|
| General | MMLU (Hendrycks et al., 2021a), MMLU-Pro (Wang et al., 2024b), IFEval (Zhou et al., 2023) |
| Math and reasoning | GSM8K (Cobbe et al., 2021), MATH (Hendrycks et al., 2021b), GPQA (Rein et al., 2023), ARC-Challenge (Clark et al., 2018) |
| Code | HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021), HumanEval+ (Liu et al., 2024a), MBPP EvalPlus (base) (Liu et al., 2024a), MultiPL-E (Cassano et al., 2023) |
| Multilinguality | MGSM (Shi et al., 2022), Multilingual MMLU (internal benchmark) |
| Tool-use | Nexus (Srinivasan et al., 2023), API-Bank (Li et al., 2023b), API-Bench (Patil et al., 2023), BFCL (Yan et al., 2024) |
| Long context | ZeroSCROLLS (Shaham et al., 2023), Needle-in-a-Haystack (Kamradt, 2023), InfiniteBench (Zhang et al., 2024) |

**Experimental setup.** [p. 34] A similar experimental setup to the pre-training phase is employed, conducting a comparative analysis of Llama 3 alongside other models of comparable size and capability. To the extent possible, the performance of other models is evaluated directly, and the results are compared with reported numbers, selecting the best score.

### 5.2.1 General Knowledge and Instruction-Following Benchmarks [p. 35]

[p. 35] Llama 3 is evaluated on benchmarks for general knowledge and instruction-following in Table 2.

**General knowledge.** [p. 35] MMLU (Hendrycks et al., 2021a) and MMLU-Pro (Wang et al., 2024b) are used to evaluate Llama 3's capability on knowledge-based question answering. For MMLU, the macro average of subtask accuracy under the 5-shot standard setting without CoT is reported. MMLU-Pro is an extension of MMLU, incorporating more challenging, reasoning-focused questions, eliminating noisy questions, and expanding the choice set from four to ten options. Given its focus on complex reasoning, 5-shot CoT for MMLU-Pro is reported. All tasks are formatted as generation tasks, similar to simple-evals (OpenAI, 2024).

[p. 35] As shown in Table 2, the 8B and 70B Llama 3 variants outperform other models of similar sizes on both general knowledge tasks. The 405B model outperforms GPT-4 and Nemotron 4 340B, with Claude 3.5 Sonnet leading among larger models.

**Instruction following.** [p. 35] The ability of Llama 3 and other models to follow natural language instructions is assessed on IFEval (Zhou et al., 2023). IFEval comprises approximately 500 "verifiable instructions" such as "write in more than 400 words", which can be verified by heuristics. The average of the prompt-level and instruction-level accuracy, under strict and loose constraints in Table 2 is reported. All Llama 3 variants outperform comparable models across IFEval.

### 5.2.2 Proficiency Exams [p. 35–36]

[p. 35] The models are evaluated on a wide variety of proficiency exams originally designed to test humans. These exams are sourced from publicly available official sources; for some exams, average scores across different exam sets per proficiency exam are reported. Specifically:

- **GRE**: Official GRE Practice Test 1 and 2 (from the Educational Testing Services);
- **LSAT**: Official Preptest 71, 73, 80 and 93;
- **SAT**: 8 exams from The Official SAT Study guide edition 2018;
- **AP**: One official practice exam per subject;
- **GMAT**: Official GMAT Online Exam.

[p. 35–36] Questions in these exams contain both MCQ style and generation questions. Questions accompanied with images are excluded. For the GRE exams that contain questions with multiple correct options, the outputs are qualified as correct only if all the correct options are selected by the model. The evaluations are run using few shot prompting wherever there is more than 1 exam set per exam. The scores for GRE are scaled to be in the range 130–170, and report accuracy for all other exams.

**Table 17** (p. 36): "Performance of Llama 3 models and GPT-4o on a variety of proficiency exams including LSAT, SAT, GMAT, and AP, and GRE tests. For GRE exams, we report normalized score; for all others, we report accuracy. For the bottom two rows corresponding to GRE Quant. and GRE Verbal, we report the scaled scores out of 170."

| Exam | Llama 3 8B | Llama 3 70B | Llama 3 405B | GPT-3.5 Turbo | Nemotron 4 340B | GPT-4o | Claude 3.5 Sonnet |
|---|---|---|---|---|---|---|---|
| LSAT | 53.9 +/-4.9 | 74.2 +/-4.3 | **81.1** +/-3.8 | 54.3 +/-4.9 | 73.7 +/-4.3 | 77.4 +/-4.1 | 80.0 +/-3.9 |
| SAT Reading | 57.4 +/-4.2 | 71.4 +/-3.9 | 74.8 +/-3.7 | 61.3 +/-4.2 | – | 82.1 +/-3.3 | **85.1** +/-3.1 |
| SAT Math | 73.3 +/-4.6 | 91.9 +/-2.8 | 94.9 +/-2.3 | 77.3 +/-4.4 | – | 95.5 +/-2.2 | **95.8** +/-2.1 |
| GMAT Quant. | 56.0 +/-19.5 | 84.0 +/-14.4 | **96.0** +/-7.7 | 36.0 +/-18.8 | 76.0 +/-16.7 | 92.0 +/-10.6 | 92.0 +/-10.6 |
| GMAT Verbal | 65.7 +/-11.4 | 85.1 +/-8.5 | 86.8 +/-8.2 | 65.7 +/-11.4 | 91.0 +/-6.8 | **95.5** +/-5.0 | 92.5 +/-6.3 |
| GRE Physics | 48.0 +/-11.3 | 74.7 +/-9.8 | 80.0 +/-9.1 | 50.7 +/-11.3 | – | 89.3 +/-7.0 | **90.7** +/-6.6 |
| AP Art History | 75.6 +/-12.6 | 84.4 +/-10.6 | **86.7** +/-9.9 | 68.9 +/-13.5 | 71.1 +/-13.2 | 80.0 +/-11.7 | 77.8 +/-12.1 |
| AP Biology | 91.7 +/-11.1 | **100.0** +/-0.0 | **100.0** +/-0.0 | 91.7 +/-11.1 | 95.8 +/-8.0 | 80.0 +/-11.7 | **100.0** +/-0.0 |
| AP Calculus | 57.1 +/-16.4 | 54.3 +/-16.5 | 88.6 +/-10.5 | 62.9 +/-16.0 | 88.6 +/-15.4 | **91.4** +/-9.3 | 88.6 +/-10.5 |
| AP Chemistry | 59.4 +/-17.0 | **96.9** +/-6.0 | 90.6 +/-10.1 | 62.5 +/-16.8 | 68.8 +/-16.1 | 93.8 +/-8.4 | **96.9** +/-6.0 |
| AP English Lang. | 69.8 +/-12.4 | 90.6 +/-7.9 | 94.3 +/-6.2 | 77.4 +/-11.3 | 88.7 +/-8.5 | **98.1** +/-3.7 | 90.6 +/-7.9 |
| AP English Lit. | 59.3 +/-13.1 | 79.6 +/-10.7 | 83.3 +/-9.9 | 53.7 +/-13.3 | **88.9** +/-8.4 | **88.9** +/-8.4 | 85.2 +/-9.5 |
| AP Env. Sci. | 73.9 +/-12.7 | 89.1 +/-9.0 | **93.5** +/-7.1 | 73.9 +/-12.7 | 73.9 +/-12.7 | 89.1 +/-9.0 | 84.8 +/-10.4 |
| AP Macro Eco. | 72.4 +/-11.5 | **98.3** +/-3.3 | **98.3** +/-3.3 | 67.2 +/-12.1 | 91.4 +/-7.2 | 96.5 +/-4.7 | 94.8 +/-5.7 |
| AP Micro Eco. | 70.8 +/-12.9 | 91.7 +/-7.8 | 93.8 +/-6.8 | 64.6 +/-13.5 | 89.6 +/-8.6 | **97.9** +/-4.0 | **97.9** +/-4.0 |
| AP Physics | 57.1 +/-25.9 | 78.6 +/-21.5 | **92.9** +/-13.5 | 35.7 +/-25.1 | 71.4 +/-23.7 | 71.4 +/-23.7 | 78.6 +/-21.5 |
| AP Psychology | 94.8 +/-4.4 | **100.0** +/-0.0 | **100.0** +/-0.0 | 94.8 +/-4.4 | **100.0** +/-0.0 | **100.0** +/-0.0 | **100.0** +/-0.0 |
| AP Statistics | 66.7 +/-17.8 | 59.3 +/-18.5 | 85.2 +/-13.4 | 48.1 +/-18.8 | 77.8 +/-15.7 | 92.6 +/-9.9 | **96.3** +/-7.1 |
| AP US Gov. | 90.2 +/-9.1 | 97.6 +/-4.7 | 97.6 +/-4.7 | 78.0 +/-12.7 | 78.0 +/-12.7 | **100.0** +/-0.0 | **100.0** +/-0.0 |
| AP US History | 78.0 +/-12.7 | **97.6** +/-4.7 | **97.6** +/-4.7 | 85.4 +/-10.8 | 70.7 +/-13.9 | 95.1 +/-6.6 | 95.1 +/-6.6 |
| AP World History | 94.1 +/-7.9 | **100.0** +/-0.0 | **100.0** +/-0.0 | 88.2 +/-10.8 | 85.3 +/-11.9 | **100.0** +/-0.0 | 97.1 +/-5.7 |
| AP Average | 74.1 +/-3.4 | 87.9 +/-2.5 | **93.5** +/-1.9 | 70.2 +/-3.5 | 81.3 +/-3.0 | 93.0 +/-2.0 | 92.2 +/-2.1 |
| GRE Quant. | 152.0 | 158.0 | 162.0 | 155.0 | 161.0 | **166.0** | 164.0 |
| GRE Verbal | 149.0 | 166.0 | 166.0 | 154.0 | 162.0 | **167.0** | **167.0** |

[p. 36] The performance of Llama 3 405B is observed to be very similar to Claude 3.5 Sonnet and GPT-4o. The 70B model has an even more impressive performance — it is significantly better than GPT-3.5 Turbo and beats Nemotron 4 340B on many tests.

### 5.2.3 Coding Benchmarks [p. 36]

[p. 36] Llama 3 is evaluated on code generation on several popular Python and multi-programming language benchmarks. The pass@N metric is used, which evaluates the pass rate for a set of unit tests among N generations. pass@1 is reported.

**Python code generation.** [p. 36] HumanEval (Chen et al., 2021) and MBPP (Austin et al., 2021) are popular benchmarks for Python code generation which focus on relatively simple, self-contained functions. HumanEval+ (Liu et al., 2024a) is an enhanced version of HumanEval, in which more tests are generated to avoid false positives. The MBPP EvalPlus base version (v0.2.0) is a selection of 378 well-formed problems out of the 974 initial problems in all of the original MBPP (train and test) dataset (Liu et al., 2024a). Results for these benchmarks are reported in Table 18. Across the Python variants of these benchmarks, Llama 3 8B and 70B outperform models of similar sizes. For the largest models, Llama 3 405B, Claude 3.5 Sonnet and GPT-4o perform similarly, with GPT-4o showing the strongest results. [p. 36–37]

---
[p. 36–41 continued]

**Table 18** (p. 37): "Pass@1 scores on code generation benchmarks. We report results on HumanEval (Chen et al., 2021), MBPP (Austin et al., 2021), as well as EvalPlus (Liu et al., 2024a) versions of these benchmarks."

| Model | HumanEval | HumanEval+ | MBPP | MBPP EvalPlus (base) |
|---|---|---|---|---|
| Llama 3 8B | **72.6** +/-6.8 | **67.1** +/-7.2 | **60.8** +/-4.3 | **72.8** +/-4.5 |
| Gemma 2 9B | 54.3 +/-7.6 | 48.8 +/-7.7 | 59.2 +/-4.3 | 71.7 +/-4.5 |
| Mistral 7B | 40.2 +/-7.5 | 32.3 +/-7.2 | 42.6 +/-4.3 | 49.5 +/-5.0 |
| Llama 3 70B | **80.5** +/-6.1 | **74.4** +/-6.7 | **75.4** +/-3.8 | **86.0** +/-3.5 |
| Mixtral 8x22B | 75.6 +/-6.6 | 68.3 +/-7.1 | 66.2 +/-4.1 | 78.6 +/-4.1 |
| GPT-3.5 Turbo | 68.0 +/-7.1 | 62.8 +/-7.4 | 71.2 +/-4.0 | 82.0 +/-3.9 |
| Llama 3 405B | 89.0 +/-4.8 | 82.3 +/-5.8 | 78.8 +/-3.6 | 88.6 +/-3.2 |
| GPT-4 | 86.6 +/-5.2 | 77.4 +/-6.4 | 80.2 +/-3.5 | 83.6 +/-3.7 |
| GPT-4o | 90.2 +/-4.5 | **86.0** +/-5.3 | **81.4** +/-3.4 | 87.8 +/-3.3 |
| Claude 3.5 Sonnet | **92.0** +/-4.2 | 82.3 +/-5.8 | 76.6 +/-3.7 | **90.5** +/-3.0 |
| Nemotron 4 340B | 73.2 +/-6.8 | 64.0 +/-7.3 | 75.4 +/-3.8 | 72.8 +/-4.5 |

**Multi-programming language code generation.** [p. 37] To assess code generation capabilities beyond Python, results are reported for the MultiPL-E (Cassano et al., 2023) benchmark, which is based on translations of problems from HumanEval and MBPP. Results for a subset of popular programming languages are reported in Table 19. There is a significant drop in performance compared to the Python counterparts in Table 18. [p. 37]

**Table 19** (p. 37): "Performance of non-Python programming tasks. We report Llama 3 results on MultiPL-E (Cassano et al., 2023)."

| Model | Dataset | C++ | Java | PHP | TS | C# | Shell |
|---|---|---|---|---|---|---|---|
| Llama 3 8B | HumanEval | 52.8 +/-7.7 | 58.2 +/-7.7 | 54.7 +/-7.7 | 56.6 +/-7.7 | 38.0 +/-7.6 | 39.2 +/-7.6 |
| | MBPP | 53.7 +/-4.9 | 54.4 +/-5.0 | 55.7 +/-4.9 | 62.8 +/-4.8 | 43.3 +/-4.9 | 33.0 +/-4.7 |
| Llama 3 70B | HumanEval | 71.4 +/-7.0 | 72.2 +/-7.0 | 67.7 +/-7.2 | 73.0 +/-6.9 | 50.0 +/-7.8 | 51.9 +/-7.8 |
| | MBPP | 65.2 +/-4.7 | 65.3 +/-4.8 | 64.0 +/-4.7 | 70.5 +/-4.5 | 51.0 +/-5.0 | 41.9 +/-4.9 |
| Llama 3 405B | HumanEval | 82.0 +/-5.9 | 80.4 +/-6.2 | 76.4 +/-6.6 | 81.1 +/-6.1 | 54.4 +/-7.8 | 57.6 +/-7.7 |
| | MBPP | 67.5 +/-4.6 | 65.8 +/-4.7 | 76.6 +/-4.2 | 72.6 +/-4.4 | 53.1 +/-5.0 | 43.7 +/-5.0 |

### 5.2.4 Multilingual Benchmarks [p. 37–38]

[p. 37] Llama 3 supports 8 languages — English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai, although the underlying foundation model has been trained on a broader collection of languages. In Table 20, results are shown from evaluating Llama 3 on the multilingual MMLU (Hendrycks et al., 2021a) and Multilingual Grade School Math (MGSM) (Shi et al., 2022) benchmarks.

**Multilingual MMLU.** [p. 37] MMLU questions, few-shot examples, and answers are translated using Google Translate. The task instructions are left in English and the evaluation is performed in a 5-shot setting. In Table 20, average results are reported across German, French, Italian, Portuguese, Hindi, Spanish, and Thai.

**MGSM** (Shi et al., 2022). [p. 38] The same native prompts as in simple-evals (OpenAI, 2024) are used for testing the models in a 0-shot CoT setting. In Table 20, average results across languages covered in the MGSM benchmark are reported.

[p. 38] Llama 3 405B outperforms most other models on MGSM, achieving an average of 91.6%. On MMLU, in line with English MMLU results, Llama 3 405B falls behind GPT-4o by 2%. On the other hand, both Llama 3 70B and 8B models demonstrate strong performance, leading among competitors with a wide margin on both tasks.

**Table 20** (p. 38): "Multilingual benchmarks. For MGSM (Shi et al., 2022), we report 0-shot CoT results for our Llama 3 models. Multilingual MMLU is an internal benchmark with translated MMLU (Hendrycks et al., 2021a) questions and answers into 7 languages — we report 5-shot results averaged across these languages."

| Model | MGSM | Multilingual MMLU |
|---|---|---|
| Llama 3 8B | **68.9** | **58.6** |
| Mistral 7B | 29.9 | 46.8 |
| Gemma 2 9B | 53.2 | – |
| Llama 3 70B | **86.9** | **78.2** |
| GPT-3.5 Turbo | 51.4 | 58.8 |
| Mixtral 8x22B | 71.1 | 64.3 |
| Llama 3 405B | **91.6** | 83.2 |
| GPT-4 | 85.9 | 80.2 |
| GPT-4o | 90.5 | **85.5** |
| Claude 3.5 Sonnet | 91.6 | – |

### 5.2.5 Math and Reasoning Benchmarks [p. 38]

[p. 38] Math and reasoning benchmark results are presented in Table 2. Llama 3 8B outperforms other models of similar sizes on GSM8K, MATH, and GPQA. The 70B model performs significantly better than other models in its class on all the benchmarks. Llama 3 405B is the best in its category on GSM8K and ARC-C, while on MATH, it is the second best model. On GPQA, it is competitive with GPT-4 4o, with Claude 3.5 Sonnet being the best model by a significant margin.

### 5.2.6 Long Context Benchmarks [p. 38–39]

[p. 38] A diverse set of tasks that span various domains and text types is considered. The focus is on sub-tasks that use unbiased evaluation protocols, i.e., accuracy-based metrics rather than n-gram overlapping metrics. Tasks that were found to be of low variance are also prioritized.

- **Needle-in-a-Haystack** (Kamradt, 2023) [p. 38] measures a model's ability to retrieve hidden information inserted in random parts of a long document. Llama 3 models demonstrate perfect needle retrieval performance, successfully retrieving 100% of needles at all document depths and context lengths. Performance on Multi-needle (Table 21), a variation where four needles are inserted in the context and the model must retrieve two of them, is also measured. Llama 3 models achieve near perfect retrieval results.

- **ZeroSCROLLS** (Shaham et al., 2023) [p. 38] is a zero-shot benchmark for natural language understanding over long texts. Numbers on the validation set are reported, as the ground truth answers are not publicly available. Llama 3 405B and 70B models either match or surpass other models on various tasks in this benchmark.

- **InfiniteBench** (Zhang et al., 2024) [p. 38] requires models to understand long dependencies in the context window. Llama 3 is evaluated on En.QA (QA over novels) and En.MC (multiple-choice QA over novels), where the 405B model outperforms all others. The gains are particularly significant on En.QA.

**Table 21** (p. 39): "Long-context benchmarks. For ZeroSCROLLS (Shaham et al., 2023), we report numbers on the validation set. For QuALITY we report exact match, for Qasper - f1 and for SQuALITY - rougeL. We report f1 for InfiniteBench (Zhang et al., 2024) En.QA metric and accuracy for En.MC. For Multi-needle (Kamradt, 2023) we insert 4 needles in the context and test if a model can retrieve 2 needles at different context lengths, we compute average recall across 10 sequence lengths up till 128k."

| | ZeroSCROLLS | | | InfiniteBench | | NIH |
|---|---|---|---|---|---|---|
| | QuALITY | Qasper | SQuALITY | En.QA | En.MC | Multi-needle |
|---|---|---|---|---|---|---|
| Llama 3 8B | **81.0** +/-16.8 | **39.3** +/-18.1 | **15.3** +/-7.9 | **27.1** +/-4.6 | **65.1** +/-6.2 | **98.8** +/-1.2 |
| Llama 3 70B | **90.5** +/-12.6 | **49.0** +/-18.5 | **16.4** +/-8.1 | **36.7** +/-5.0 | **78.2** +/-5.4 | **97.5** +/-1.7 |
| Llama 3 405B | **95.2** +/-9.1 | 49.8 +/-18.5 | 15.4 +/-7.9 | **30.5** +/-4.8 | **83.4** +/-4.8 | 98.1 +/-1.5 |
| GPT-4 | **95.2** +/-9.1 | **50.5** +/-18.5 | 13.2 +/-7.4 | 15.7 +/-3.8 | 72.0 +/-5.8 | **100.0** +/-0.0 |
| GPT-4o | 90.5 +/-12.5 | 49.2 +/-18.5 | **18.8** +/-8.6 | 19.1 +/-4.1 | 82.5 +/-4.9 | **100.0** +/-0.0 |
| Claude 3.5 Sonnet | 90.5 +/-12.6 | 18.5 +/-14.4 | 13.4 +/-7.5 | 11.3 +/-3.3 | – | 90.8 +/-3.2 |

### 5.2.7 Tool Use Performance [p. 38–39]

[p. 38] The models are evaluated on a range of benchmarks for zero-shot tool use (i.e. function calling): Nexus (Srinivasan et al., 2023), API-Bank (Li et al., 2023b), Gorilla API-Bench (Patil et al., 2023), and the Berkeley Function Calling Leaderboard (BFCL) (Yan et al., 2024). Results are shown in Table 22.

[p. 38–39] On Nexus, Llama 3 variants perform the best compared to their counterparts. On the API-Bank, Llama 3 8B and 70B models outperform other models in their category by a significant margin. The 405B model is behind Claude 3.5 Sonnet by only 0.6%. The 405B and 70B models perform competitively on BFCL and are close second in their respective size class. Llama 3 8B performs the best in its category.

**Table 22** (p. 39): "Zero-shot tool use benchmarks. We report function calling accuracy across Nexus (Srinivasan et al., 2023), API-Bank (Li et al., 2023b), API-Bench (Patil et al., 2023), and BFCL (Yan et al., 2024)."

| | Nexus | API-Bank | API-Bench | BFCL |
|---|---|---|---|---|
| Llama 3 8B | **38.5** +/-4.1 | **82.6** +/-3.8 | 8.2 +/-1.3 | **76.1** +/-2.0 |
| Gemma 2 9B | – | 56.5 +/-4.9 | **11.6** +/-1.5 | – |
| Mistral 7B | 24.7 +/-3.6 | 55.8 +/-4.9 | 4.7 +/-1.0 | 60.4 +/-2.3 |
| Llama 3 70B | **56.7** +/-4.2 | **90.0** +/-3.0 | 29.7 +/-2.1 | 84.8 +/-1.7 |
| Mixtral 8x22B | 48.5 +/-4.2 | 73.1 +/-4.4 | 26.0 +/-2.0 | – |
| GPT-3.5 Turbo | 37.2 +/-4.1 | 60.9 +/-4.8 | **36.3** +/-2.2 | **85.9** +/-1.7 |
| Llama 3 405B | **58.7** +/-4.1 | 92.3 +/-2.6 | 35.3 +/-2.2 | 88.5 +/-1.5 |
| GPT-4 | 50.3 +/-4.2 | 89.0 +/-3.1 | 22.5 +/-1.9 | 88.3 +/-1.5 |
| GPT-4o | 56.1 +/-4.2 | 91.3 +/-2.8 | 41.4 +/-2.3 | 80.5 +/-1.9 |
| Claude 3.5 Sonnet | 45.7 +/-4.2 | **92.6** +/-2.6 | **60.0** +/-2.3 | **90.2** +/-1.4 |
| Nemotron 4 340B | – | – | – | 86.5 +/-1.6 |

**Human evaluations on tool use.** [p. 39] Human evaluations are also conducted to test tool use capabilities of the model, with a focus on code execution tasks. 2,000 user prompts related to code execution (without plotting or file uploads), plot generation, and file uploads are collected. These prompts are collected from the LMSys dataset (Chiang et al., 2024), GAIA benchmark (Mialon et al., 2023b), human annotators, and synthetic generation.

[p. 39] Llama 3 405B is compared to GPT-4o using OpenAI's Assistants API. The results are provided in Figure 16. On text-only code execution tasks and plots generation, Llama 3 405B significantly beats GPT-4o. However, it lags behind on the file upload use case.

## 5.3 Human Evaluations [p. 39–40]

[p. 39] In addition to evaluations on standard benchmark sets, a series of human evaluations are performed. These evaluations allow measurement and optimization of more subtle aspects of model performance, such as the model's tone, verbosity, and understanding of nuances and cultural contexts. Well-designed human evaluations closely reflect the user experience, providing insights into how the model performs in real-world scenarios.

**Prompt collection.** [p. 39–40] High-quality prompts spanning a wide range of categories and difficulties are collected. A taxonomy with categories and subcategories capturing as many model capabilities as possible is developed. This taxonomy is used to collect about 7,000 prompts spanning six individual capabilities (English, reasoning, coding, Hindi, Spanish, and Portuguese), and three multiturn capabilities (English, reasoning, and coding). Within each category, prompts are uniformly distributed across subcategories. Each prompt is categorized into one of three difficulty levels, and the prompt collection contains roughly 10% easy prompts, 30% medium prompts, and 60% hard prompts. All human evaluation prompt sets are subject to a thorough quality assurance process. Modeling teams did not have access to the human-evaluation prompts to prevent accidental contamination or overfitting on the test set. [p. 40]

**Evaluation process.** [p. 40] To perform a pairwise human evaluation of two models, human annotators are asked which of two model responses (produced by different models) they prefer. Annotators use a 7-point scale for their ratings, enabling them to indicate whether one model response is much better than, better than, slightly better than, or about the same as the other model response. When an annotator indicates that one model response is better or much better than the other model response, this is considered a "win" for that model. Pairwise comparisons between models are performed, reporting win rates per capability in the prompt set.

**Results.** [p. 40] The human evaluation process is used to compare Llama 3 405B with GPT-4 (0125 API version), GPT-4o (API version), and Claude 3.5 Sonnet (API version). The results of these evaluations are presented in Figure 17. Llama 3 405B performs approximately on par with the 0125 API version of GPT-4, while achieving mixed results (some wins and some losses) compared to GPT-4o and Claude 3.5 Sonnet. On nearly all capabilities, the win rates of Llama 3 and GPT-4 are within the margin of error. On multiturn reasoning and coding tasks, Llama 3 405B outperforms GPT-4 but it underperforms GPT-4 on multilingual (Hindi, Spanish, and Portuguese) prompts. Llama 3 performs on par with GPT-4o on English prompts, on par with Claude 3.5 Sonnet on multilingual prompts, and outperforms Claude 3.5 Sonnet on single and multiturn English prompts. However, it trails Claude 3.5 Sonnet in capabilities such as coding and reasoning. Qualitatively, model performance in human evaluations is heavily influenced by nuanced factors such as model tone, response structure, and verbosity — factors that are being optimized for in the post-training process. Overall, human evaluation results are consistent with those on standard benchmark evaluations: Llama 3 405B is very competitive with leading industry models, making it the best-performing openly available model. [p. 40]

**Limitations.** [p. 40] All human evaluation results underwent a thorough data quality assurance process. However, since it is challenging to define objective criteria for evaluating model responses, human evaluations can still be influenced by personal biases, backgrounds, and preferences of human annotators, which may lead to inconsistent or unreliable results.

**Figure 16** (p. 40): "Human evaluation results for Llama 3 405B vs. GPT-4o on code execution tasks including plotting and file uploads. Llama 3 405B outperforms GPT-4o on code execution (without plotting or file uploads) as well as plot generation, but lags behind in file upload use cases."

A horizontal stacked bar chart with three categories on the y-axis: Text-only Code Execution, Plots Generation, and File Uploads. Each bar shows Win (dark blue), Tie (medium blue), and Loss (light blue) percentages.
- Text-only Code Execution: Win 51.6%, Tie 14.1%, Loss 34.3%
- Plots Generation: Win 54.7%, Tie 14.2%, Loss 31.1%
- File Uploads: Win 22.9%, Tie 12.9%, Loss 64.2%

**Figure 17** (p. 41): "Human evaluation results for the Llama 3 405B model. *Left:* Comparison with GPT-4. *Middle:* Comparison with GPT-4o. *Right:* Comparison with Claude 3.5 Sonnet. All results include 95% confidence intervals and exclude ties."

Three panels of horizontal grouped bar charts, each showing Win (dark blue, top bar) and Loss (light blue, bottom bar) percentages for seven capability categories: English, Reasoning, Coding, Multilingual, Multiturn English, Multiturn Reasoning, Multiturn Coding.

Left panel (vs. GPT-4):
- English: Win 24.1%, Loss 23.6%
- Reasoning: Win 20.5%, Loss 26.0%
- Coding: Win 28.0%, Loss 24.2%
- Multilingual: Win 19.7%, Loss 31.1%
- Multiturn English: Win 19.0%, Loss 15.8%
- Multiturn Reasoning: Win 25.0%, Loss 18.0%
- Multiturn Coding: Win 30.4%, Loss 21.0%

Middle panel (vs. GPT-4o):
- English: Win 22.1%, Loss 24.8%
- Reasoning: Win 16.8%, Loss 30.1%
- Coding: Win 22.0%, Loss 28.0%
- Multilingual: Win 17.4%, Loss 34.7%
- Multiturn English: Win 15.4%, Loss 23.6%
- Multiturn Reasoning: Win 16.0%, Loss 27.4%
- Multiturn Coding: Win 18.2%, Loss 38.2%

Right panel (vs. Claude 3.5 Sonnet):
- English: Win 29.0%, Loss 20.5%
- Reasoning: Win 18.9%, Loss 26.4%
- Coding: Win 22.4%, Loss 28.5%
- Multilingual: Win 29.0%, Loss 24.3%
- Multiturn English: Win 26.0%, Loss 16.0%
- Multiturn Reasoning: Win 24.0%, Loss 27.4%
- Multiturn Coding: Win 20.8%, Loss 30.8%
