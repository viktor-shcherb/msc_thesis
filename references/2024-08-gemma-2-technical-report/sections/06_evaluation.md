# 6. Evaluation [p. 6]

Both pre-trained and IT models are evaluated over a series of automated benchmarks and human evaluations across a variety of domains. Performance is reported from models of similar sizes that have permissive licenses, or as reported by others. Total parameters, not active parameters, are considered, since total memory usage is often what limits the use of open models on standard devices. [p. 6]

## 6.1. Pre-training Evaluations [p. 6]

### Evaluating the 27B Model

The performance of the 27B model trained without distillation on 13T tokens is evaluated. Results are reported in Table 12, comparing with Qwen1.5 34B (Team, 2024) and LLaMA-3 70B on the HuggingFace evaluation suite. These models were selected based on their ranking on the HuggingFace leaderboard. [p. 6]

The 27B model is observed to be the best in its size category and even competitive with a larger model (LLaMA-3 70B) that is trained for longer. The performance of models trained in a similar fashion improves only logarithmically with their size, so the model is likely in the same Pareto curve as the LLaMA-3 models. However, it is not clear how these differences affect the quality of the resulting IT models. [p. 6]

## Table 12 | HuggingFace benchmark comparison of Gemma-2 27B with LLaMA-3 70B and Qwen1.5 32B [p. 6]

|  | LLaMA-3 70B | Qwen1.5 32B | Gemma-2 27B |
|---|---|---|---|
| MMLU | 79.2 | 74.3 | **75.2** |
| GSM8K | 76.9 | 61.1 | **74.0** |
| ARC-c | 68.8 | 63.6 | **71.4** |
| HellaSwag | 88.0 | 85.0 | **86.4** |
| Winogrande | 85.3 | 81.5 | **83.7** |

The Gemma-2 27B model outperforms Qwen1.5 32B and is only a few percent below LLaMA-3 70B despite being 2.5x smaller and trained on 2/3rds less data. [p. 6]

### Evaluating the 2B and 9B Models

The new 2B and 9B models trained with distillation are compared to previous models and several standard open models in Gemma Team (2024). [p. 6]

A massive improvement in the models compared to previous versions is observed, by up to 10% in some benchmarks for the 9B model. The two 2B models were trained with a similar number of tokens (2T for Gemma 2 and 3T for Gemma 1) and a significant improvement for the new models is still observed. This confirms that distillation significantly improves the quality of models even when trained on the same number of tokens. [p. 6]

## 6.2. Post-training Evaluations [p. 6]

IT models are evaluated on a set of human evaluations as well as standard academic benchmarks. The Gemma 2 models push the frontier for post-trained open-weights models, setting a new state of the art on the LMSYS Chatbot Arena (Chiang et al., 2024). [p. 6]

### LMSYS Chatbot Arena

Gemma 2 Instruction Tuned models were evaluated on the Chatbot Arena (Chiang et al., 2024) in blind side by side evaluations by human raters against other state of the art models. Elo scores are reported in Table 14. Gemma 2.6B, 9B, and 27B strongly outperform all other open models in the same range of parameters, with notably: [p. 6]

- Gemma 27B (Elo 1218) ranked higher than Llama 3 70B (Elo 1206)
- Gemma 9B (Elo 1187) similar as GPT-4-0314 (Elo 1186)
- Gemma 2.6B (Elo 1126) ranked higher than GPT-3.5-Turbo-0613 (Elo 1116)

### Human Preference Evaluations [p. 6–7]

Gemma IT models are also submitted for side-by-side human evaluation studies (independent from the Chatbot Arena). Held-out collections of single-turn prompts that target safety and instruction following (IF) are used. `gpt4o-2024-05-13` is used as the base model. [p. 6]

Large improvements in win rates and preference scores are observed compared against the older Gemma 1.1 7B model. Safety is reported as a win-loss ratio against GPT4o, and single-sided instruction following scores are reported as the ratio of prompts where all instructions are followed. Regardless of their size, Gemma 2 models produce safer, more appropriate prompts on the held-out safety prompt set than GPT4o. [p. 7]

**Table 13** | Comparison of models in the range of 2B to 9B parameters, as well as the 27B model, on a variety of benchmarks [p. 7]

Average is reported on the 8 benchmarks where comparison with LLaMA-3 is possible, and on all benchmarks. Numbers for LLaMA-3 8B are from the HuggingFace leaderboard or their blogpost. Dagger (†): the evaluation used in LLaMA-3 for the baselines, leading to +3% compared to the authors' own evaluation (Gemma-1 7B achieves 44.9% instead of 41.7%, and Mistral 7B 44% instead of 41.2%). Circle (°): the evaluation used in LLaMA-3 for the baselines, leading to +4% compared to the authors' own evaluation for Gemma-1 7B (i.e., 59.0% instead of 55.1%). Asterisk (*): evaluations run by the authors for Gemma 1 (Gemma Team, 2024).

| Benchmark | metric | Gemma-1 2B | Gemma-2 2B | Mistral 7B | LLaMA-3 8B | Gemma-1 7B | Gemma-2 9B | Gemma-2 27B |
|---|---|---|---|---|---|---|---|---|
| MMLU | 5-shot | 42.3 | **52.2** | 62.5 | 66.6 | 64.4 | **71.3** | 75.2 |
| ARC-C | 25-shot | 48.5 | **55.7** | 60.5 | 59.2 | 61.1 | **68.4** | 71.4 |
| GSM8K | 5-shot | 15.1 | **24.3** | 39.6 | 45.7 | 51.8 | **68.6** | 74.0 |
| AGIEval | 3-5-shot | 24.2 | **31.5** | 44.0† | 45.9† | 44.9† | **52.8** | 55.1 |
| DROP | 3-shot, F1 | 48.5 | **51.2** | 63.8* | 58.4 | 56.3 | **69.4** | 74.2 |
| BBH | 3-shot, CoT | 35.2 | **41.9** | 56.0° | 61.1° | 59.0° | **68.2** | 74.9 |
| Winogrande | 5-shot | 66.8 | **71.3** | 78.5 | 76.1 | 79.0 | **80.6** | 83.7 |
| HellaSwag | 10-shot | 71.7 | **72.9** | **83.0** | 82.0 | 82.3 | 81.9 | 86.4 |
| MATH | 4-shot | 11.8 | **16.0** | 12.7 | - | 24.3 | **36.6** | 42.3 |
| ARC-e | 0-shot | 73.2 | **80.6** | 80.5 | - | 81.5 | **88.0** | 88.6 |
| PIQA | 0-shot | 77.3 | **78.4** | **82.2** | - | 81.2 | 81.7 | 83.2 |
| SIQA | 0-shot | 49.7 | **51.9** | 47.0* | - | 51.8 | **53.4** | 53.7 |
| Boolq | 0-shot | 69.4 | **72.7** | 83.2* | - | 83.2 | **84.2** | 84.8 |
| TriviaQA | 5-shot | 53.2 | **60.4** | 62.5 | - | 63.4 | **76.6** | 83.7 |
| NQ | 5-shot | 12.5 | **17.1** | 23.2 | - | 23.0 | **29.2** | 34.5 |
| HumanEval | pass@1 | **22.0** | 20.1 | 26.2 | - | 32.3 | **40.2** | 51.8 |
| MBPP | 3-shot | 29.2 | **30.2** | 40.2* | - | 44.4 | **52.4** | 62.6 |
| Average (8) | | 44.0 | **50.0** | 61.0 | 61.9 | 62.4 | **70.2** | 74.4 |
| Average (all) | | 44.2 | **48.7** | 55.6 | - | 57.9 | **64.9** | 69.4 |

---
[p. 7–8 continued]

### Human Multi-Turn Evaluations [p. 7–8]

The multi-turn capabilities of Gemma 1.1 7B, Gemma 2 2B, 9B, and 27B models were evaluated by tasking human raters to have conversations with the models and follow specified given scenarios. A diverse, held-out set of 500 scenarios was used, each describing a sequence of requests to the model, including measuring instances of brainstorming, making a plan, or learning something new. The average number of user turns is 8.4. [p. 7–8]

Conversations with Gemma 2 models are rated significantly better than Gemma 1.1 in user satisfaction and conversation goal achievement (Table 16). The Gemma 2 models were also better than Gemma 1.1 7B at maintaining high quality of responses for the entire conversation. [p. 8]

### Standard Benchmarks [p. 8]

It has been observed in Llama-3 (AI@Meta, 2024) that instruction fine-tuning can improve the performance of the models on few-shot benchmarks despite not being trained to target few-shot capabilities. A similar improvement is observed across the Gemma 2 models (Table 17). Overall, improvements on the order of several percentage points are observed. The authors conjecture that IT models are better at understanding formatted questions, while pre-trained models are sensitive to formatting. [p. 8]

**Table 14** | Evaluation of Gemma 2 Instruction Tuned models on the Chatbot Arena (Chiang et al., 2024). Models are evaluated against each other through blind side by side evaluations by human raters. Each model is attributed an Elo score. [p. 8]

| Model | Elo | 95% CI | Open | Model | Elo | 95% CI | Open |
|---|---|---|---|---|---|---|---|
| gpt-4o-2024-05-13 | 1286 | +2 / -3 | - | **gemma-2-9b-it** | 1187 | +3 / -5 | + |
| gpt-4o-mini-2024-07-18 | 1279 | +5 / -4 | - | qwen2-72b-instruct | 1187 | +3 / -3 | + |
| claude-3-5-sonnet | 1271 | +3 / -4 | - | gpt-4-0314 | 1186 | +2 / -3 | - |
| gemini-advanced-0514 | 1266 | +2 / -3 | - | qwen1.5-110b-chat | 1161 | +3 / -3 | + |
| llama-3.1-405b-instruct | 1262 | +8 / -7 | + | mistral-large-2402 | 1157 | +3 / -3 | - |
| gemini-1.5-pro-api-0514 | 1261 | +2 / -3 | - | yi-1.5-34b-chat | 1157 | +4 / -3 | - |
| gemini-1.5-pro-api-0409 | 1257 | +3 / -3 | - | reka-flash-21b-20240226 | 1155 | +4 / -4 | - |
| gpt-4-turbo-2024-04-09 | 1256 | +2 / -3 | - | llama-3-8b-instruct | 1151 | +2 / -3 | + |
| gpt-4-1106-preview | 1250 | +3 / -3 | - | command-r | 1148 | +3 / -3 | + |
| claude-3-opus-20240229 | 1248 | +2 / -2 | - | claude-1 | 1148 | +4 / -4 | - |
| athene-70b-0725 | 1245 | +8 / -6 | + | mistral-medium | 1147 | +4 / -4 | - |
| gpt-4-0125-preview | 1245 | +2 / -2 | - | reka-flash-21b-20240226 | 1147 | +3 / -4 | - |
| llama-3.1-70b-instruct | 1244 | +8 / -9 | + | qwen1.5-72b-chat | 1147 | +4 / -4 | + |
| yi-large-preview | 1239 | +3 / -3 | - | mixtral-8x22b-instruct-v0.1 | 1145 | +2 / -3 | + |
| gemini-1.5-flash-api-0514 | 1227 | +3 / -3 | - | claude-2.0 | 1131 | +4 / -6 | - |
| deepseek-v2-api-0628 | 1220 | +6 / -6 | + | gemini-pro-dev-api | 1131 | +4 / -3 | - |
| **gemma-2-27b-it** | 1218 | +4 / -3 | + | zephyr-orpo-141b | 1127 | +10 / -6 | + |
| yi-large | 1212 | +4 / -5 | - | **gemma-2-2b-it** | 1126 | +10 / -10 | + |
| nemotron-4-340b-instruct | 1209 | +3 / -4 | + | qwen1.5-32b-chat | 1125 | +3 / -3 | + |
| bard-jan-24-gemini-pro | 1208 | +5 / -7 | - | mistral-next | 1124 | +5 / -5 | - |
| glm-4-0520 | 1206 | +3 / -5 | - | phi-3-medium-4k-instruct | 1122 | +4 / -4 | + |
| llama-3-70b-instruct | 1206 | +2 / -2 | + | starling-lm-7b-beta | 1118 | +4 / -5 | + |
| claude-3-sonnet | 1200 | +2 / -2 | - | claude-2.1 | 1118 | +3 / -3 | - |
| reka-core-20240501 | 1199 | +3 / -3 | - | gpt-3.5-turbo-0613 | 1116 | +3 / -4 | - |
| command-r-plus | 1189 | +2 / -2 | + | mixtral-8x7b-instruct-v0.1 | 1114 | +0 / -0 | - |

**Table 15** | Instruction following and safety metrics from human raters [p. 8]

| Model | Instruction Following | Safety |
|---|---|---|
| Gemma 1.1 IT 7B | 24.3% +/- 1.9% | 42.8% |
| *Win / Tie / Loss* | | *37.4% / 10.8% / 51.8%* |
| **Gemma 2 IT 2B** | 26.5% +/- 1.8% | **57.5%** |
| *Win / Tie / Loss* | | *53% / 9% / 38%* |
| **Gemma 2 IT 9B** | 34.1% +/- 3.0% | **57.8%** |
| *Win / Tie / Loss* | | *48.2% / 19.2% / 28.3%* |
| **Gemma 2 IT 27B** | 37.7% +/- 2.3% | **55%** |
| *Win / Tie / Loss* | | *49.6% / 10.8% / 39.6%* |

The instruction following metrics are single-sided and do not have win-loss rates. Safety is reported as a win-loss ratio against GPT4o. [p. 8]

**Table 16** | Human evaluations on 500 multi-turn scenarios. Raters attribute a score between 1 and 5 for both overall satisfaction and conversation goal achievement. [p. 8]

| | User satisfaction | Conversation goal achievement |
|---|---|---|
| Gemma 1.1 IT 7B | 3.32 | 3.36 |
| Gemma 2 IT 2B | 3.64 | 3.88 |
| Gemma 2 IT 9B | 4.04 | 4.08 |
| Gemma 2 IT 27B | 4.20 | 4.24 |

**Table 17** | Comparing pre-trained (PT) and instruction fine-tuned (IT) models of different sizes on few-shot benchmarks [p. 8]

| | 2B | | 9B | | 27B | |
|---|---|---|---|---|---|---|
| Model | PT | IT | PT | IT | PT | IT |
| MMLU | 52.2 | **56.1** | 71.3 | **72.3** | 75.2 | **76.2** |
| MBPP | 30.2 | **36.6** | 52.4 | **59.2** | 62.6 | **67.4** |
