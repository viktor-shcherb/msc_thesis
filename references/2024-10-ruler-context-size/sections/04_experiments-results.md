# Experiments & Results [p. 6]

## Models & Inference Setup

[p. 6] The authors select 17 long-context LLMs, including 15 open-source models and two closed-source models (Gemini-1.5-Pro and GPT-4), covering diverse model sizes (7B to 8x22B with MoE architecture) and claimed context lengths (32K to 1M). Complete information about these models is included in Appendix A.

All models are evaluated using vLLM (Kwon et al., 2023), an LLM serving system with efficient KV cache memory management. For all models, inference is run in BFloat16 on 8 NVIDIA A100 GPUs with greedy decoding.

## Task Configurations

[p. 6] All models are tested on 13 tasks ranging diverse complexities from the four categories of RULER. The test configurations have been selected (shown in Appendix B) based on a task correlational study described in Appendix C. The authors select these tasks as most models perform decently at short context size of 4K tokens. The main goal is to see whether models can maintain such good performance with the scaling of context length.

For each task, each model is evaluated with 500 examples generated for each length from the series (4K, 8K, 16K, 32K, 64K, 128K), while complying with each model's necessary chat template. To prevent the model from refusing to answer a query or generating explanations, the task input is appended with an answer prefix and the check is on the presence of the target output with recall-based accuracy.

## Effective Context Size

[p. 6] The authors notice large performance degradation in all models as input length increases in RULER. To determine the maximum context size a model can *effectively* handle, they grade each model with a fixed threshold, passing which indicates satisfactory performance at the length of evaluation. The performance of Llama2-7b model at the 4K context length is used as the threshold. Table 3 reports the maximum length exceeding the threshold as the "effective length" along with the "claimed length".

## Model Ranking Criteria

[p. 6] While the threshold-based grading reveals the discrepancy between claimed and effective length, it lacks details for fine-grained model comparisons. The authors use a weighted average score to aggregate model performance across various context sizes. Two weighting schemes are used:

- **wAvg. (inc):** weight linearly increases with sequence length (simulates scenarios where longer sequences dominate usage).
- **wAvg. (dec):** weight linearly decreases with sequence length (simulates scenarios where shorter sequences dominate usage).

Ideally, the weight for each length should be determined by the length distribution of model usage.

## Main Results

[p. 6] The results of 17 long-context LMs are included in comparison with the Llama2-7B baseline in Table 3. The performance at a certain length is the average of all 13 tasks in RULER. Key observations:

- The closed-source model Gemini-1.5-Pro outperforms the rest of the models by a large margin, with the effective length greater than the maximum length tested.
- Pressure testing this model with harder version of RULER can be interesting to follow up in the future.
- For the rest of the models, while they achieve nearly perfect performance on the passkey retrieval and the vanilla NIAH task (shown in Appendix E), all of them exhibit large degradation in RULER as sequence length increases and they fail to maintain performance above the Llama2-7B baseline at their claimed length.
- The top-ranked open-source models (Llama3.1, Qwen2 and Command-R-plus) share common configurations, such as having larger model sizes and using larger base frequencies in RoPE (Xiong et al., 2023).
- Large training context window is not always necessary for good long context performance -- top-ranked open-source models contain both brute-force context scaling (Llama3.1 trained on 128K context length) and inference-time length extrapolation (Qwen2 trained on 32K context length).
- The less performant models also include those trained on much larger context size (e.g., LWM and GradientAI/Llama3 both on 1M context length).
- Although LWM achieves a higher rank than Mistral-v0.2 when longer sequences receive larger weight (wAvg. inc) and shows less degradation as the context size increases, it performs worse than Llama2-7B even at 4K. This result suggests a trade-off in evaluation between absolute performance on short sequences and the relative degradation with the scaling of context size.
- More analysis on the model size and maximum training length is provided in Section 6.

**Table 3** (p. 7): Long Context Performance (%) of selected models evaluated at length from 4K to 128K. Each score is computed by averaging accuracy of 13 tasks in RULER. The effective context length is the maximum length passing the Llama2-7B performance at 4K (85.6%) threshold, shown underlined. Weighted average score (wAvg.) aggregates performance across all context sizes, with the weights linearly increasing (inc) or decreasing (dec) to simulate length distribution of real-world usage. Rank of each model is in the subscript.

| Models | Claimed Length | Effective Length | 4K | 8K | 16K | 32K | 64K | 128K | Avg. | wAvg. (inc) | wAvg. (dec) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Llama2 (7B) | 4K | - | 85.6 | | | | | | | | |
| Gemini-1.5-Pro | 1M | >128K | 96.7 | 95.8 | 96.0 | 95.9 | 95.9 | 94.4 | 95.8 | 95.5(1st) | 96.1(1st) |
| GPT-4 | 128K | 64K | 96.6 | 96.3 | 95.2 | 93.2 | 87.0 | 81.2 | 91.6 | 89.0(2nd) | 94.1(2nd) |
| Llama3.1 (70B) | 128K | 64K | 96.5 | 95.8 | 95.4 | 94.8 | 88.4 | 66.6 | 89.6 | 85.5(4th) | 93.7(3rd) |
| Qwen2 (72B) | 128K | 32K | 96.9 | 96.1 | 94.9 | 94.1 | 79.8 | 53.7 | 85.9 | 79.6(9th) | 92.3(4th) |
| Command-R-plus (104B) | 128K | 32K | 95.6 | 95.2 | 94.2 | 92.0 | 84.3 | 63.1 | 87.4 | 82.7(7th) | 92.1(5th) |
| GLM4 (9B) | 1M | 64K | 94.7 | 92.8 | 92.1 | 89.9 | 86.7 | 83.1 | 89.9 | 88.0(3rd) | 91.7(6th) |
| Llama3.1 (8B) | 128K | 32K | 95.5 | 93.8 | 91.6 | 87.4 | 84.7 | 77.0 | 88.3 | 85.4(5th) | 91.3(7th) |
| GradientAI/Llama3 (70B) | 1M | 16K | 95.1 | 94.4 | 90.8 | 85.4 | 80.9 | 72.1 | 86.5 | 82.8(6th) | 90.3(8th) |
| Mixtral-8x22B (39B/141B) | 64K | 32K | 95.6 | 94.9 | 93.4 | 90.9 | 84.7 | 31.7 | 81.9 | 73.5(11th) | 90.3(9th) |
| Yi (34B) | 200K | 32K | 93.3 | 92.2 | 91.3 | 87.5 | 83.2 | 77.3 | 87.5 | 84.8(8th) | 90.1(10th) |
| Phi3-medium (14B) | 128K | 32K | 93.3 | 93.2 | 91.1 | 86.8 | 78.6 | 46.1 | 81.5 | 74.8(10th) | 88.3(11th) |
| Mistral-v0.2 (7B) | 32K | 16K | 93.6 | 91.2 | 87.2 | 75.4 | 49.0 | 13.8 | 68.4 | 55.6(13th) | 81.2(12th) |
| LWM (7B) | 1M | <4K | 82.3 | 78.4 | 73.7 | 69.1 | 68.1 | 65.0 | 72.8 | 69.9(12th) | 75.7(13th) |
| DBRX (36B/132B) | 32K | 8K | 95.1 | 93.8 | 83.6 | 63.1 | 2.4 | 0.0 | 56.3 | 38.0(14th) | 74.7(14th) |
| Together (7B) | 32K | 4K | 88.2 | 81.1 | 69.4 | 63.0 | 0.0 | 0.0 | 50.3 | 33.8(15th) | 66.7(15th) |
| LongChat (7B) | 32K | <4K | 84.7 | 79.9 | 70.8 | 59.3 | 0.0 | 0.0 | 49.1 | 33.1(16th) | 65.2(16th) |
| LongAlpaca (13B) | 32K | <4K | 60.6 | 57.0 | 56.6 | 43.6 | 0.0 | 0.0 | 36.3 | 24.7(17th) | 47.9(17th) |

Footnotes:
- Footnote 5 [p. 6]: See Appendix D for model and tasks templates details.
- Footnote 6 [p. 6]: Performance of base models and breakdown by task categories can be found in Appendix F.
