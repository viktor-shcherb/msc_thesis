# Appendix F. Additional Evaluations on Math and Code [p. 32-34]

[p. 32] The evaluation employs the SC-Math6 corpus, which consists of thousands of Chinese math problems. DeepSeek-V2 Chat (RL) outperforms all Chinese LLMs, including both open-source and close-source models. [p. 32]

**Table 11** (p. 33): "SC-Math6 Model Reasoning Level. 'R Level' stands for Reasoning Level, 'Comp. Score' stands for Comprehensive Score, 'Reas. Steps Score' stands for Reasoning Steps Score, and 'OvrAcc Score' stands for Overall Accuracy Score."

| Model Name | R Level | Comp. Score | Reas. Steps Score | OvrAcc Score |
|---|---|---|---|---|
| GPT-4-1106-Preview | **5** | 90.71 | 91.65 | 89.77 |
| GPT-4 | **5** | 88.40 | 89.10 | 87.71 |
| DeepSeek-V2 Chat (RL) | **5** | 83.35 | 85.73 | **84.54** |
| Ernie-bot 4.0 | **5** | 85.60 | 86.82 | 84.38 |
| Qwen-110B-Chat | **5** | 83.25 | 84.93 | 84.09 |
| GLM-4 | **5** | 84.24 | 85.72 | 82.77 |
| Xinghuo 3.5 | **5** | 83.73 | 85.37 | 82.09 |
| Qwen-72B-Chat | 4 | 78.42 | 80.07 | 79.25 |
| ChatGLM-Turbo | 4 | 57.70 | 60.32 | 55.09 |
| GPT-3.5-Turbo | 4 | 57.05 | 59.61 | 54.50 |
| Qwen-14B-Chat | 4 | 53.12 | 55.99 | 50.26 |
| ChatGLM3-6B | 3 | 40.90 | 44.20 | 37.60 |
| Xinghuo 3.0 | 3 | 40.08 | 45.27 | 34.89 |
| Baichuan2-13B-Chat | 3 | 39.40 | 42.63 | 36.18 |
| Ernie-3.5-turbo | 2 | 25.19 | 27.70 | 22.67 |
| Chinese-Alpaca2-13B | 2 | 20.55 | 22.52 | 18.58 |

[p. 33] We further share more results in Figure 5 on HumanEval and LiveCodeBench, where the questions of LiveCodeBench are selected from the period between September 1st, 2023, and April 1st, 2024. As shown in the figure, DeepSeek-V2 Chat (RL) demonstrates considerable proficiency in LiveCodeBench, achieving a Pass@1 score that even surpasses some giant models. This performance highlights the strong capability of DeepSeek-V2 Chat (RL) in tackling live coding tasks. [p. 33]

**Figure 5** (p. 34): "Evaluation results on HumanEval and LiveCodeBench. The questions of LiveCodeBench are selected from the period between September 1st, 2023 and April 1st, 2024."

The figure is a scatter plot with x-axis "HumanEval (Pass@1)" ranging from ~65 to 90 and y-axis "LiveCodeBench (Pass@1)" ranging from ~15 to 45. Models shown (approximate coordinates):
- GPT-4-Turbo-1106: (~86, ~41) -- top right
- GPT-4-0613: (~82, ~36)
- Claude Opus: (~83, ~34)
- DeepSeek-V2-Chat-RL: (~81, ~33) -- marked with a star
- LLaMA3-70B-Chat: (~78, ~31)
- Claude Sonnet: (~71, ~27)
- Mistral Large: (~72, ~26)
- Claude Haiku: (~75, ~26)
- Mixtral 8x22B: (~77, ~25)
- Qwen Max: (~83, ~24)
- Qwen1.5 72B: (~66, ~20)
- DeepSeek 67B: (~74, ~18)

DeepSeek-V2 Chat (RL) achieves LiveCodeBench performance comparable to Claude Opus and LLaMA3-70B-Chat while using far fewer activated parameters. The dashed lines are approximate reference lines.
