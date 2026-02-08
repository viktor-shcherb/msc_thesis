# 3.3 Automatic and Human Evaluation of Aligned Models [p. 11–12]

[p. 11] To showcase the effectiveness of the aligned models, a comparison is conducted with other aligned models on well-established benchmarks, including MMLU (Hendrycks et al., 2020), C-Eval (Huang et al., 2023), GSM8K (Cobbe et al., 2021), HumanEval (Chen et al., 2021), and BBH (Suzgun et al., 2022).

## Evaluation setup

[p. 11] Besides the widely used few-shot setting, the aligned models are also tested in the zero-shot setting to demonstrate how well the models follow instructions. The prompt in a zero-shot setting consists of an instruction and a question without any previous examples in the context. The results of the baselines are collected from their official reports and OpenCompass (OpenCompass Team, 2023).

> "The results in Table 5 demonstrate the effectiveness of our aligned models in understanding human instructions and generating appropriate responses." [p. 11]

**Table 5: Performance of aligned models on widely-used benchmarks.** Both zero-shot and few-shot performance are reported. [p. 12]

| Model | Params | MMLU 0-shot / 5-shot | C-Eval 0-shot / 5-shot | GSM8K 0-shot / 8-shot | HumanEval 0-shot | BBH 0-shot / 3-shot |
|---|---|---|---|---|---|---|
| *Proprietary models* | | | | | | |
| GPT-3.5 | - | - / 69.1 | - / 52.5 | - / 78.2 | 73.2 | - / 70.1 |
| GPT-4 | - | - / **83.0** | - / **69.9** | - / **91.4** | **86.6** | - / **86.7** |
| *Open-source models* | | | | | | |
| ChatGLM2 | 6B | 45.5 / 46.0 | 50.1 / 52.6 | - / 28.8 | 11.0 | - / 32.7 |
| InternLM-Chat | 7B | - / 51.1 | - / 53.6 | - / 33.0 | 14.6 | - / 32.5 |
| Baichuan2-Chat | 7B | - / 52.9 | - / 55.6 | - / 32.8 | 13.4 | - / 35.8 |
| | 13B | - / 57.3 | - / 56.7 | - / 55.3 | 17.7 | - / 49.9 |
| LLAMA 2-CHAT | 7B | - / 46.2 | - / 31.9 | - / 26.3 | 12.2 | - / 35.6 |
| | 13B | - / 54.6 | - / 36.2 | - / 37.1 | 18.9 | - / 40.1 |
| | 70B | - / 63.8 | - / 44.3 | - / 59.3 | 32.3 | - / 60.8 |
| QWEN-CHAT | 1.8B | 42.4 / 43.9 | 50.7 / 50.3 | 27.8 / 19.5 | 14.6 | 27.1 / 25.0 |
| | 7B | 55.8 / 57.0 | 59.7 / 59.3 | 50.3 / 54.1 | 37.2 | 39.6 / 46.7 |
| | 14B | 64.6 / **66.5** | 69.8 / **71.7** | **60.1** / 59.3 | **43.9** | 46.9 / **58.7** |

[p. 12] QWEN-14B-Chat outperforms all other models except ChatGPT (OpenAI, 2022) and LLAMA 2-CHAT-70B (Touvron et al., 2023b) in all datasets, including MMLU (Hendrycks et al., 2020), C-Eval (Huang et al., 2023), GSM8K (Cobbe et al., 2021), HumanEval (Chen et al., 2021), and BBH (Suzgun et al., 2022). In particular, QWEN's performance in HumanEval, which measures the quality of generated codes, is significantly higher than that of other open-source models.

[p. 12] Moreover, QWEN's performance is consistently better than that of open-source models of similar size, such as LLaMA2 (Touvron et al., 2023b), ChatGLM2 (ChatGLM2 Team, 2023), InternLM (InternLM Team, 2023), and Baichuan2 (Yang et al., 2023). This suggests that the alignment approach, which involves fine-tuning the model on a large dataset of human conversations, has been effective in improving the model's ability to understand and generate human-like language.

## Limitations of benchmark evaluation

[p. 12] The authors express reservations about the ability of traditional benchmark evaluation to accurately measure the performance and potential of chat models trained with alignment techniques in the current landscape. The results mentioned provide some evidence of competitive standing, but they believe it is crucial to develop new evaluation methods specifically tailored to aligned models.

## Human evaluation

[p. 12] A carefully curated dataset of 300 instructions in Chinese is created, covering a wide range of topics, including knowledge, language understanding, creative writing, coding, and mathematics. Models evaluated:
- QWEN-CHAT-7B (SFT version)
- QWEN-CHAT-14B (SFT version)
- QWEN-CHAT-14B (RLHF version)
- GPT-3.5
- GPT-4

Footnote 4: To obtain the results from the models, the OpenAI APIs of GPT-3.5-turbo-0613 and GPT-4-0613 are used. [p. 12]

For each instruction, three annotators rank the model responses by the overall score of helpfulness, informativeness, validity, and other relevant factors.

**Figure 4** (p. 13): **"Results of the human evaluation for chat models."** The figure compares Qwen-7B-Chat (SFT), Qwen-14B-Chat (SFT), Qwen-14B-Chat (RLHF), and GPT-4 against GPT-3.5. Each bar segment represents the percentage of wins, ties, and losses, from bottom to top. Categories shown on x-axis: Average, Knowledge, Language Understanding, Creative Writing, Math, Coding. On average, the RLHF model outperforms the SFT model. The dataset consists of 300 Chinese instructions.

Key data points from Figure 4 (approximate percentages, wins/ties/losses vs GPT-3.5):
- **Average:** Qwen-7B (SFT): 28.3/28.7/43.0; Qwen-14B (SFT): 32.3/30.7/37.0; Qwen-14B (RLHF): 34.4/34.0/31.6 [unclear: exact split difficult to read]; GPT-4: 54.0/22.8/23.2 [unclear: approximate]
- The RLHF model outperforms the SFT models by significant margins
- GPT-4 outperforms all other models across all categories

[p. 13] The experimental results clearly demonstrate that the RLHF model outperforms the SFT models by significant margins, indicating that RLHF can encourage the model to generate responses that are more preferred by humans. In terms of overall performance, the RLHF model significantly outperforms the SFT models, falling behind GPT-4. This indicates the effectiveness of RLHF for aligning to human preference. A case study with examples from different models is included in Appendix A.2.2.

> "Nonetheless, it remains difficult to accurately capture the gap between our models and the proprietary models. As such, a more extensive and rigorous assessment is required for the chat models." [p. 13]
