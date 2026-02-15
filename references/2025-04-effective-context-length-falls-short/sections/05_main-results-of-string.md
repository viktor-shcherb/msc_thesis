# 4.2 Main Results of STRING [p. 7–10]

[p. 7]

In this section, we evaluate the effectiveness of STRING across three widely recognized long-context benchmarks: Needle-in-a-Haystack (NIAH) (gkamradt, 2023), RULER (Hsieh et al., 2024), and InfiniteBench (Zhang et al., 2024d). These tasks enable us to assess STRING's performance across a broad spectrum of practical scenarios. We also provide some case studies in Tables 7 and 6 in the Appendix.

---
[p. 8 continued]

## Baselines [p. 8]

We primarily compare STRING with the original position embedding RoPE used in mainstream Large Language Models. Additionally, we evaluate RoPE against several effective extrapolation baselines. Specifically, we compare with the following training-free extrapolation methods: NTK-Aware RoPE (LocalLLaMA, 2023b;a), YaRN (Peng et al., 2023), ReRoPE (Su, 2023), Self-Extend (Jin et al., 2024), and DCA (An et al., 2024b). These extrapolation refers to testing LLMs on sequence lengths beyond their training lengths while STRING focus on improving the performance within the training context size. NTK-Aware RoPE, YaRN, Self-Extend, and DCA modify the position matrix to avoid unseen positions. We reproduced the results using their official repositories. When testing these extrapolation baselines, we modify the training length of the model to 2/3 of the original length and set the extrapolation scaling factor to L_test/L_train = 3/2, meaning the test sequence length is 1.5 times the training length. All the hyperparameters remain the same as in their paper. Our findings indicate that although extrapolation methods can extend the model's capability to handle longer sequences, the performance improvements are still limited within the original training length.

## Needle-in-a-Haystack [p. 8]

Table 1: Needle-in-a-haystack (4 needles) results of 7 base models across various methods (columns reordered from smallest to largest average) where Ltrain means the size of the training context window. All the models were tested using their training context length. The number of test cases is 500.

| Model | Ltrain | ReRoPE | NTK | RoPE_origin | Self-Extend | YaRN | DCA | STRING |
|-------|--------|--------|-----|-------------|-------------|------|-----|--------|
| TinyLlama-1.3B (ours) | 2k | 62.8 | 62.0 | 56.6 | 60.2 | 68.6 | 74.4 | **84.6** |
| TinyLlama-1.1B-3T | 2k | 77.2 | 79.8 | 69.8 | 83.2 | 88.0 | 80.2 | **97.2** |
| Llama-2-7B | 4k | 98.6 | 98.6 | 98.0 | 95.4 | 98.0 | 91.6 | **100.0** |
| Llama-3-8B | 8k | 99.6 | 100.0 | 99.8 | 99.8 | 100.0 | 99.9 | **99.6** |
| LWM-7B-base | 32k | 25.2 | 19.4 | 31.8 | 24.0 | 22.2 | 28.8 | **50.4** |
| Mistral-7B-base | 32k | 54.5 | 42.2 | 52.8 | 54.2 | 48.2 | 64.2 | **73.0** |
| Llama-3.1-8B | 128k | 53.6 | 71.2 | 66.0 | 65.8 | 68.8 | 72.8 | **95.2** |
| **Average** | – | 67.3 | 67.6 | 67.8 | 69.6 | 70.5 | 73.1 | **85.7** |

Needle-in-a-Haystack Needle-in-a-Haystack (gkamradt, 2023) (NIAH) is the most popular long-context task, extensively utilized in recent studies (Zheng et al., 2024; Liu et al., 2024b). As reported by Hsieh et al. (2024); Wang et al. (2024b), the single needle retrieval is no longer a challenging task for current LLMs, and we adopt the multi-needle setting following Llama 3.1 (Llama Team, 2024) and the input example can be found in Table 5. We verify the effectiveness of our method on seven community models with training context windows from 2K to 128K. Across all seven models, LargeWorldModel (LWM-7B-base) (Liu et al., 2024a), Mistral 7B (Mistral.AI, 2024), and Llama 3.1 8B (Llama Team, 2024) are continually pretrained on longer contexts. On models with various training context lengths, STRING consistently outperforms other methods, achieving the highest scores on each model. Notably, STRING improves model performance by a wide margin, reaching 85.7% compared to the next best method, DCA, at 73.1%, and the original RoPE at only 67.8%.

## RULER [p. 8]

The RULER benchmark (Hsieh et al., 2024) encompasses a variety of synthetic tasks, including eight variants of Needle-in-a-Haystack (NIAH), as well as tasks involving variable tracking, counting, and long-context question answering. The evaluation code and metrics are from their official repository⁴. The primary results are presented in Table 2. The results on Llama3.1-8B reveal that, except for our proposed method STRING, all other extrapolation approaches fail to achieve performance improvements. Since our method does not require additional training, we are able to validate its effectiveness on larger models. STRING approach consistently yields remarkable enhancements: a 15-point improvement on Llama3.1 70B and over a 30-point improvement on Qwen2 72B compared to the baseline. Furthermore, our approach achieved state-of-the-art performance on the RULER benchmark for open-source models. Notably, after applying STRING, both Llama3.1 70B and Qwen2 72B surpass GPT-4-128K in average performance. The remarkable performance gain on large models demonstrates that the frequent positions in large models may possess a stronger potential for modeling long-range dependencies. Additionally, we also demonstrate that both Llama3.1 and Qwen2 can be effectively boosted to an effective sequence length of 100K on RULER by STRING (the last block in Table 2).

¹https://github.com/hsiehjackson/RULER

---
[p. 9 continued]

Table 2: Performance of various models and methods on RULER with a tested at a sequence length of 128K. The RULER benchmark consists of 500 test cases for each task) categorized into Needle-in-a-Haystack (NIAH), Variable Tracing (VT), Aggregation, and Question Answering (QA). We report the average scores for each category as well as the overall average across all 13 tasks. **Effective** denotes the actual effective context length as defined in RULER, indicating whether the model surpasses the performance of Llama2 (Touvron et al., 2023b), and **Claimed** represents the sequence length reported by the model.

| Models | Effective/Claimed | NIAH | VT | Aggregation | QA | Avg. (13 tasks) |
|--------|-------------------|------|-----|-------------|-----|-----------------|
| Llama2-chat | 4K / 4K | 96.9 | 89.7 | 84.8 | 49.7 | 85.6 |
| GPT-4-1106-preview | 64K / 128K | 84.8 | 99.6 | 79.7 | 59.0 | 81.2 |
| GLM4 (*Open-source best*) | 64K / 1M | 94.4 | 97.7 | 49.7 | 63.6 | 83.1 |
| LWM (7B) | 4K / 128K | 83.4 | 15.2 | 29.1 | 52.6 | 65.0 |
| Phi3-medium (14B) | 8K / 128K | 51.3 | 26.0 | 43.5 | 38.0 | 46.1 |
| Llama3.1 (8B) | 32K / 128K | 92.6 | 70.4 | 36.2 | 58.8 | 77.0 |
| + YaRN | 32K / 128K | 94.7 | 39.8 | 38.2 | 58.8 | 76.3 |
| + DCA | 32K / 128K | 89.5 | 62.5 | 39.2 | 55.2 | 74.4 |
| + Self-Extend | 32K / 128K | 94.9 | 65.0 | 37.3 | 49.8 | 76.8 |
| + ReRoPE | 32K / 128K | 90.0 | 56.3 | 38.7 | 56.9 | 74.4 |
| + STRING | 32K / 128K | 94.0 | 88.1 | 37.6 | 62.7 | 80.0 |
| Yi (34B) | 32K / 200K | 90.2 | 76.8 | 43.4 | 59.9 | 77.3 |
| GradientAI/Llama3 (70B) | 16K / 1M | 84.9 | 56.2 | 41.4 | 59.8 | 72.1 |
| Mixtral (8x22B) | 32K / 64K | 23.8 | 0.0 | 69.7 | 40.8 | 31.7 |
| Command-R-plus (104B) | 32K / 128K | 65.7 | 97.2 | 59.5 | 39.2 | 63.1 |
| Llama3.1 (70B) | 64K / 128K | 78.9 | 59.2 | 39.8 | 47.6 | 66.6 |
| + STRING | 100K / 128K | 92.7 | 95.6 | 50.0 | **63.0** | **81.7** |
| Qwen2 (72B) | 64K / 128K | 48.0 | 79.0 | 70.3 | 47.2 | 53.7 |
| + STRING (*new SOTA*) | 100K / 128K | 91.2 | **98.4** | **83.7** | 52.2 | **84.6** |
| **Test Length: 100K** | | | | | | |
| Llama3.1-STRING (70B) | 100K / 128K | 94.6 | 97.8 | 72.1 | 67.3 | 87.2 |
| Qwen2-STRING (72B) | 100K / 128K | 93.9 | 97.7 | 88.1 | 57.8 | 87.8 |

## InfiniteBench [p. 9]

Table 3: Comparison of STRING with three leading commercial long-context models on InfiniteBench. Each model is evaluated using a maximum context length of 128K.

| Tasks | **Commercial Models** | | | **Llama3.1 8B** | | **Llama3.1 70B** | |
|-------|---------|----------|-----------|------------|--------|--------------|--------|
| | GPT-4 | Claude2 | Kimi-chat | RoPEtrain | STRING | RoPEtrain | STRING |
| En.Sum | 14.73 | 14.45 | 17.93 | 26.00 | **28.22** | 26.89 | 27.64 |
| En.QA | 22.22 | 11.97 | 16.52 | 10.05 | 10.20 | 13.68 | 16.73 |
| En.MC | 67.25 | 62.88 | 72.49 | 65.50 | 70.30 | 76.41 | **81.98** |
| En.Dia | 8.50 | **46.50** | 11.50 | 20.00 | 19.50 | 18.00 | 30.50 |
| Retr.PassKey | 100.00 | 97.80 | 98.14 | 100.00 | **100.00** | 100.00 | **100.00** |
| Retr.Number | 100.00 | 98.14 | 94.42 | 99.32 | 99.89 | 100.00 | **100.00** |
| Retr.KV | 89.00 | 65.40 | 53.60 | 42.00 | 83.00 | 2.22 | 76.07 |
| Code.debug | 39.59 | 2.28 | 18.02 | 22.84 | 26.90 | 29.20 | 32.80 |
| Math.find | 60.00 | 32.29 | 12.57 | 32.18 | 34.87 | 40.92 | 46.28 |
| **Avg.** | 55.69 | 47.96 | 43.91 | 46.43 | **52.54** | 45.25 | **56.88** |

InfiniteBench InfiniteBench (Zhang et al., 2024d) encompasses a variety of real-world tasks, including long-context question answering (QA), multiple-choice QA, mathematical problem-solving, long-dialogue QA, long-context summarization, retrieval tasks, and code debugging.

The evaluation code and metrics are sourced from the official repository⁵. The results for commercial models are from Zhang et al. (2024d). We compare our method, STRING, with the original position

²https://github.com/OpenBMB/InfiniteBench

---
[p. 10 continued]

embedding, RoPE, across two scales of Llama3.1: 8B and 70B parameters. The results are presented in Table 3. STRING demonstrates significant improvements for both models; for instance, we enhance the performance of Llama3.1 70B by 11.63 points, establishing a new state-of-the-art for open-source models. On InfiniteBench, our method also surpasses the performance of strong baseline GPT-4-128K and significantly outperforms Claude-2 and Kimi-chat.

**Figure 7** (p. 10): "Ablation study on the local window W and shifted offset S where L is the training length."

Description: Two line charts showing ablation study results
- Key elements: (a) Shows performance vs. local window W with S = L/3. Four lines for TinyLlama-2K, Llama-2-4K, LWM-7B-32K, and Llama-3.1-128K. X-axis ranges from RoPE to 512, Y-axis shows performance from ~0 to 100. (b) Shows performance vs. shifted offset S with W = 128. X-axis shows shifted offset from L/5 to L/2, Y-axis shows performance.
- Notable patterns: (a) Performance improves when W ≥ 32, with model achieving significant improvement compared to original RoPE method. As long as W ≪ S, further increasing W does not cause a performance drop. (b) As S increases, more position indices are discarded. Performance increases with the growth of S. However, the curve slowed down when S exceeded L/3, indicating that at least the last 33% to 50% of the position can be overwritten.
- Supports claim: The hyperparameters W and S can be set effectively across different models with the guidelines W ≥ 32 and L/7 ≤ S ≤ L/2.

## Ablation Study [p. 10]

We conduct an ablation study on the Needle-in-a-Haystack (4 needles) task to examine the impact of two main hyperparameters in our STRING: the local window size W and the shifted offset size S. The experimental results are shown in Figure 7. We increase the local window size from 4 to 512 and find that when W ≥ 32, the model achieves a significant improvement compared to the original RoPE method. Furthermore, as long as W ≪ S, further increasing W does not cause a performance drop. For the shifted offset S, we experiment with values ranging from L/5 to L/2. As S increases, more position indices are discarded. We observe that within this range, the performance increased with the growth of S. However, the curve slowed down when S exceeded L/3, indicating that at least the last 33% to 50% of the position can be overwritten.
