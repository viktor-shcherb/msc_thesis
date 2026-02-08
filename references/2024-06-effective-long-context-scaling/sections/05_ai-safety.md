# AI Safety [p. 11]

## Evaluation on Safety Benchmarks [p. 11]

[p. 11] Despite excellent performance on various downstream tasks, large language models are prone to generating harmful, misinformative, and biased contents (Lin et al., 2021; Hartvigsen et al., 2022; Dhamala et al., 2021; Ji et al., 2023). Long-context language models can process extended inputs in their context window, but at the same time, they also face a higher risk of jailbreak, especially through means such as prompt injection (Greshake et al., 2023).

[p. 11] The safety capability of the instruction fine-tuned model is evaluated using three standard academic benchmarks: TruthfulQA (Lin et al., 2021), ToxiGen (Hartvigsen et al., 2022), and BOLD (Dhamala et al., 2021), similar to (Touvron et al., 2023). The focus is on the largest instruction fine-tuned model variant (i.e., 70B) and comparison with both open sourced LLMs (Falcon-instruct (Almazrouei et al., 2023), MPT-instruct (MosaicML, 2023a)) and propriety LLMs (GPT-3.5, GPT-4 (OpenAI, 2023), Claude-2 (Anthropic, 2023)) in Table 12.

[p. 11] The instruction fine-tuned model maintains similar safety performance compared to LLAMA 2 CHAT and is safer and less biased compared to other open-source LLMs such as Falcon-instruct and MPT-instruct. AI safety is a complex domain and it can be extremely difficult to comprehensively evaluate all safety aspects of instruction fine-tuned model with three benchmarks. However, the authors hope this analysis can serve as a pilot study and provide directional signals on long-context large language models' safety performance, which are not discussed in other works on the same topic (Tworkowski et al., 2023b; Ding et al., 2023; Chen et al., 2023). The community also lacks dedicated safety benchmarks for long-context large language model evaluation and the authors plan to invest in this direction in future work.

### TruthfulQA [p. 11]

[p. 11] The instruction fine-tuned model is evaluated on TruthfulQA (Lin et al., 2021) to benchmark its factuality. The benchmark consists of 817 questions covering 38 categories including health, law, finance, and politics (Lin et al., 2021). Similar to (Touvron et al., 2023), few-shot prompts with 6 random QA pairs are used for generation and then two fine-tuned GPT-3 models are leveraged to classify the outputs. The percentage of generations that are both truthful and informative is reported as the final metric in Table 12.

---
[p. 12 continued]

### ToxiGen [p. 12]

[p. 12] The toxicity of the instruction fine-tuned model is measured using ToxiGen (Hartvigsen et al., 2022) where the percentage of toxic and hateful generations against 13 minority groups is checked. Following (Touvron et al., 2023), prompts where annotators disagree with each other on the target demographic group are filtered out. The default ToxiGen classifier fine-tuned based on RoBERTa (Liu et al., 2019) is used to evaluate the level of toxicity of the model's outputs. The percentage of toxic generations across all groups is reported in Table 12.

### BOLD [p. 12]

[p. 12] Bias in Open-Ended Language Dataset (BOLD) (Dhamala et al., 2021) is used to quantify how biased the models are against people from different demographic groups. This dataset consists of 23,679 prompts extracted from English Wikipedia covering five domains including race, gender, religion, political ideology and profession with 43 subgroups in total. Following Touvron et al. (2023), prompts belonging to Hinduism and Atheism religious subgroups are excluded as they only feature 12 and 29 prompts, respectively. After generations are inferred from each model, the Valence Aware Dictionary and Sentiment Reasoner (VADER) (Hutto and Gilbert, 2014) is leveraged to perform sentiment analysis with a score ranging between -1 and 1. A positive score corresponds to a positive sentiment towards the subgroup mentioned in the prompt and vice versa. A sentiment score close to 0 indicates neutral sentiment which is desired. The average sentiment score across 43 demographic subgroups is reported as the final metric for BOLD in Table 12.

### Safety Benchmark Results [p. 12]

**Table 12** (p. 12): Evaluation of fine-tuned LLMs on three safety benchmarks. For TruthfulQA, the percentage of generations that are both truthful and informative (the higher the better). For ToxiGen, the percentage of toxic generations across all groups (the smaller the better). For BOLD, the average sentiment score across 43 demographic groups (the closer to 0 the better).

| | Model Size | TruthfulQA ↑ | ToxiGen ↓ | BOLD ↓ |
|---|---|---|---|---|
| GPT-3.5-turbo | - | 78.46 | 0.01 | 0.50 |
| GPT-3.5-turbo-16k | - | 75.15 | 0.07 | 0.49 |
| Claude-2 | - | 62.66 | 0.05 | 0.46 |
| GPT4 | - | **80.66** | 0.03 | 0.43 |
| Falcon-instruct | 40B | 57.41 | 3.3 | 0.39 |
| MPT-instruct | 30B | 42.71 | 16.85 | **0.34** |
| LLAMA 2 CHAT | 70B | 64.14 | 0.01 | 0.41 |
| LLAMA 2 LONG CHAT | 70B | 60.95 | **0.00** | 0.40 |

## Red Teaming Exercises [p. 12]

[p. 12] Currently there is no open-sourced safety benchmark designed for long-context understanding. To ensure that the models are safe in long context use scenarios, internal red teaming is performed to better understand the vulnerability of the chat model. The model is attacked by feeding long contexts (e.g., long conversations) to it, followed by adversarial prompts covering risky areas including illicit and criminal conducts (e.g., terrorism, theft, and human trafficking), hateful and harmful behaviors (e.g., defamation, self-harm, eating disorders, and discrimination), and unqualified advice (Touvron et al., 2023). Through manual inspection, no significant risks are observed compared to LLAMA 2 CHAT (Touvron et al., 2023). The authors plan to invest more in new attack vectors against long context large models in future work.
