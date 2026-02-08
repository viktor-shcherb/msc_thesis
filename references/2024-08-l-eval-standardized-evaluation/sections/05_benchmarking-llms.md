# 5 Benchmarking LLMs with L-Eval [p. 7–9]

[p. 7] This section lists 16 baseline models and the results on both open-ended and closed-ended tasks. Generally, there are considerable gaps between open-source models and commercial models. A detailed description of baseline models can be found in Section A.1. The prompt templates for each task are available in Section B. All experiments use FlashAttention (Dao et al., 2022) on a single NVIDIA A800 GPU. The document input is truncated from the right. [p. 7]

## 5.1 Baselines

[p. 7]

**Commercial Models:**
1. Claude-100k developed by Anthropic
2. GPT-4-32k, OpenAI's most powerful long context model
3. Turbo-4k-0613
4. Turbo-16k-0613, the snapshot of GPT-3.5 from June 13th 2023 which can handle up to 4k/16k input tokens

**Open-source Models:**
5. Llama1 (Touvron et al., 2023a), a widely used open-source model developed by Meta AI with a 2k pre-training length
6. Vicuna1.3 (Chiang et al., 2023), tuned on shareGPT based on Llama1
7. Longchat-16k, the long context version of Vicuna1.3 using PI
8. Llama2, the next version of Llama with 4k pre-training context
9. Llama2-chat, a finetuned version for dialogue usage
10. Llama2-NTK, extending the context length of Llama2-chat with NTK-aware RoPE
11. Vicuna1.5-16k (Zheng et al., 2023), the long context version of Llama2 using PI & ShareGPT
12. Longchat1.5-32k, the 32k context version of Llama2 using PI & ShareGPT
13. Chatglm2-8k, the second version of the Chatglm (Du et al., 2022)
14. Chatglm2-32k, the 32k context length version
15. XGen-8k-inst (Nijkamp et al., 2023), an 8k context models developed by Salesforce
16. MPT-7B-StoryWriter-65k, based on MPT-7B and ALiBi with a context length of 65k tokens on a subset of Books3 dataset

**Retriever:** The dense retriever is implemented with the OpenAI AdaEmbedding as the dense retriever and BM25 as the sparse retriever to extract 4 pieces of most related 1k-chunked documents, which are further provided as the context to answer questions. [p. 7]

## 5.2 Main Results

[p. 7–9]

The performance of LCLMs on closed-ended tasks is shown Table 3. As for open-ended tasks, the 96-question subset is tested (Table 4) with GPT-4 evaluation. Results from n-gram metrics on all test sets and the rankings of LLMs can be found in Section A.3. [p. 7]

Key observations from the main results:
- GPT-4-32k clearly outperforms all other models by a very significant margin, establishing SOTA in L-Eval closed-ended tasks. [p. 7]
- There is still a near **20-points gap** between the best open-source 16k models and Turbo-16k. [p. 7]
- As for open-ended tasks, since the input texts are generally longer and a global understanding of the context is required, Claude-100k, with the longest context length, surpasses all baseline models including GPT-4-32k. [p. 7]
- Although results of n-gram metrics indicate that open-source LCLMs have achieved performance close to GPT-Turbo on open-ended tasks, the evaluation outcomes from both LLM (Table 4) and human judges (Table 5) reveal that there is still a significant gap between them. [p. 8]
- Retrieval-based methods based on Turbo-4k fall short in comparison to encoding the entire context (Turbo-16k), as certain tasks are difficult to address through simple retrieval. [p. 8]

**Table 3** (p. 8): "Exam evaluation results on **closed-ended tasks** for current LCLMs. **Ret.** indicates whether we use retrieve-based algorithms for the base model. **Tokens** denotes the maximum number of input tokens we feed into the model. ↓/↑ indicates a remarkable decrease/increase in performance, compared to using the original short context counterpart. * indicates the model is not further trained."

| Model                        | Ret. | Tokens | Coursera | GSM   | QuALITY | TOEFL | CodeU | SFiction | Avg.  |
|------------------------------|------|--------|----------|-------|---------|-------|-------|----------|-------|
| Claude1.3-100k               | ✗    | 100k   | 60.03    | 88.00 | 73.76   | 83.64 | 17.77 | 72.65    | 65.97 |
| GPT-4-32k                    | ✗    | 32k    | **75.58**| **96.00** | **82.17** | **84.38** | **25.55** | **74.99** | **73.11** |
| Turbo-16k-0613               | ✗    | 16k    | 63.51    | 84.00 | 61.38   | 78.43 | 12.22 | 64.84    | 60.73 |
| AdaEmb-Turbo-4k-0613         | ✓    | 4k     | 61.77    | 23.00 | 58.91   | 76.95 | 6.66  | 71.09    | 49.73 |
| BM25-Turbo-4k-0613           | ✓    | 4k     | 63.80    | 23.00 | 59.40   | 75.09 | 5.55  | 71.09    | 49.65 |
| *Truncating input tokens to the pretraining context length* | | | | | | | | | |
| Llama1-7b-2k (w/o SFT)      | ✗    | 2k     | 13.37    | 7.00  | 21.78   | 30.85 | 1.11  | 35.15    | 19.22 |
| Vicuna1.3-7b-2k              | ✗    | 2k     | 34.73    | 19.00 | 32.67   | 43.49 | 1.11  | 60.93    | 30.01 |
| Llama2-7b-4k (w/o SFT)      | ✗    | 4k     | 20.05    | 2.00  | 28.71   | 24.53 | 0.00  | 40.62    | 19.31 |
| Llama2-7b-chat               | ✗    | 4k     | 29.21    | 19.00 | 37.62   | 51.67 | 1.11  | 54.68    | 33.12 |
| Llama2-13b-chat              | ✗    | 4k     | 35.75    | **39.00** | **42.57** | **60.96** | 1.11  | 54.68    | **39.01** |
| Chatglm2-6b-8k               | ✗    | 2k     | **43.75** | 13.00 | 40.59   | 53.90 | 2.22  | 54.68    | 34.69 |
| XGen-7b-8k (2k-4k-8k)       | ✗    | 2k     | 26.59    | 3.00  | 35.15   | 44.23 | 1.11  | 48.43    | 26.41 |
| *Truncating input tokens to the further finetuning context length* | | | | | | | | | |
| Chatglm2-6b-32k              | ✗    | 32k    | **47.81** | 27.00↓ | 45.04   | 55.01 | 2.22  | 57.02    | 39.01↓ |
| Longchat1.5-7b-32k           | ✗    | 32k    | 32.99    | 18.00 | 37.62   | 39.77 | 3.33  | 57.02    | 31.45 |
| Longchat-7b-16k              | ✗    | 16k    | 29.74    | 10.00↓ | 33.66   | 47.95 | 3.33  | **64.84** | 31.58 |
| Vicuna1.5-7b-16k             | ✗    | 16k    | 38.66    | 19.00 | 39.60   | 55.39 | **5.55** | 60.15    | 36.39↑ |
| Llama2-7b-NTK*               | ✗    | 16k    | 32.71    | 19.00 | 33.16   | 52.78 | 0.00  | **64.84** | 33.74 |
| Longchat-13b-16k             | ✗    | 16k    | 31.39    | 15.00 | 40.59   | 55.39 | 2.22  | **64.84** | 34.90 |
| Vicuna1.5-13b-16k            | ✗    | 16k    | 40.69    | 36.00 | **53.96**↑ | **68.40**↑ | 0.00  | 61.71    | **43.46**↑ |
| Llama2-13b-NTK*              | ✗    | 16k    | 36.48    | 11.00↓ | 35.64   | 54.64 | 1.11  | 63.28    | 33.69 |
| Llama2-13b-NTK(Dyn)*         | ✗    | 16k    | 30.08    | **43.00** | 41.58   | 64.31 | 1.11  | 35.15    | 35.87 |
| Chatglm2-6b-8k               | ✗    | 8k     | 42.15    | 18.00 | 44.05   | 54.64 | 2.22  | 54.68    | 35.95 |
| XGen-7b-8k                   | ✗    | 8k     | 29.06    | 16.00 | 33.66   | 42.37 | 3.33  | 41.40    | 27.63 |
| MPT-7b-65k                   | ✗    | 8k     | 25.23    | 8.00  | 25.24   | 17.84 | 0.00  | 39.06    | 19.22 |

**Table 4** (p. 9): "In comparing various models to Turbo-16k-0613 on **open-ended tasks**. We evaluate these models on the 96-question subset using GPT-4 and two subsets (85+96 questions) using GPT-3.5. We reduce the positional biases by swapping paired predictions, so the GPT-4 evaluator is used in 96×2 evaluation rounds, while the GPT3.5 evaluator is used in 181×2 rounds."

| Model                        | Ret. | Tokens | GPT-4 wins | GPT-4 ties | GPT-4 win-rate % | GPT-3.5 wins | GPT-3.5 ties | GPT-3.5 win-rate % | R-L   |
|------------------------------|------|--------|------------|------------|-------------------|--------------|--------------|---------------------|-------|
| Claude1.3-100k               | ✗    | 100k   | **96**     | 42         | **60.94**         | 189          | 34           | **58.68**           | 28.22 |
| GPT-4-32k                    | ✗    | 32k    | 76         | 56         | 54.16             | 171          | 50           | 56.32               | 36.18 |
| Turbo-16k-0613               | ✗    | 4k     | 0          | 192        | 50.00             | 0            | 362          | 50.00               | 28.61 |
| Turbo-4k-0613                | ✗    | 4k     | 38         | 69         | 39.83↓            | 109          | 61           | 41.39               | 26.90 |
| AdaEmb-Turbo-4k-0613         | ✓    | 4k     | 61         | 56         | 46.84             | 123          | 77           | 45.36               | 26.09 |
| BM25-Turbo-4k-0613           | ✓    | 4k     | 50         | 69         | 44.01             | 125          | 78           | 45.30               | 26.83 |
| *Truncating input tokens to the pretraining context length* | | | | | | | | | |
| Vicuna1.3-7b-2k              | ✗    | 2k     | 29         | 55         | 29.42             | 97           | 42           | 34.91               | 16.17 |
| Longchat-7b-16k              | ✗    | 2k     | 26         | 63         | 29.94             | 87           | 38           | 31.26               | 19.77 |
| Llama2-7b-chat               | ✗    | 4k     | 48         | 58         | 40.10             | 127          | 44           | 42.45               | 24.25 |
| Llama2-13b-chat              | ✗    | 4k     | **51**     | 61         | **42.44**         | **143**      | 49           | **47.85**           | 24.07 |
| *Truncating input tokens to the further finetuning context length* | | | | | | | | | |
| Chatglm2-6b-32k              | ✗    | 32k    | 28         | 60         | 30.20             | 53           | 65           | 24.63               | 22.04 |
| Longchat1.5-7b-32k           | ✗    | 32k    | **38**     | 53         | 33.59             | 136          | 37           | 44.91               | 21.21 |
| Longchat-7b-16k              | ✗    | 16k    | 36         | 56         | 33.68↑            | 108          | 42           | 37.94               | 20.59 |
| Vicuna1.5-7b-16k             | ✗    | 16k    | 22         | 54         | 25.52↓            | 102          | 52           | 37.86               | 18.05 |
| Llama2-7b-NTK*               | ✗    | 16k    | 18         | 49         | 22.13             | 58           | 35           | 23.59               | 11.50 |
| Longchat-13b-16k             | ✗    | 16k    | 36         | 59         | **34.11**         | **128**      | 24           | 40.11               | 18.98 |
| Vicuna1.5-13b-16k            | ✗    | 16k    | 36         | 59         | **34.11**↓        | 116          | 43           | **40.92**           | 19.69 |
| Llama2-13b-NTK*              | ✗    | 16k    | 31         | 52         | 29.68             | 91           | 44           | 34.55               | 15.63 |
| Llama2-13b-NTK(Dyn)*         | ✗    | 16k    | 23         | 48         | 24.47             | 55           | 64           | 26.60               | 11.62 |
| Chatglm2-6b-8k               | ✗    | 8k     | 18         | 64         | 26.04             | 86           | 54           | 32.84               | 18.19 |
| XGen-7b-8k                   | ✗    | 8k     | 24         | 62         | 28.64             | 89           | 72           | 36.02               | 20.51 |

### Fine-tuning longer offers benefits for closed-ended tasks but falls short in open-ended tasks

[p. 8] In Table 3, for open-source models using scaled positional embedding, Longchat and Vicuna1.5-16k obviously outperform their original version Vicuna-2k and Llama2-chat. The results suggest that further tuning on longer input from a model with short pretraining context length does benefit long context modeling. However, according to Table 4, unlike results on closed-ended tasks, the best model Vicuna1.5-13b-16k only wins Turbo-16k by 34%, **8 points lower** than its short version Llama2-13b. Llama2-13b-chat (Touvron et al., 2023a) is still the strongest open-source baseline, indicating that current LCLMs simply based on scaled position embedding may not be enough for these challenging open generation tasks. [p. 8]

Based on human evaluation, although scaled position embedding techniques such as NTK (LocalLLaMA, 2023b) or PI (Sun et al., 2022) effectively extend models' context length, the models tend to get lost when facing lengthy input tokens and are unable to follow the instruction. These outputs are classified as "invalid outputs". [p. 8]

To investigate model performance on different context lengths, the 85-question subset is split into 2 parts: PART-A contains samples with less than 4k tokens, and PART-B more than 4k tokens. The number of invalid outputs from Llama2/Vicuna1.5-16k and Turbo/Turbo-16k are compared in Figure 4. Results show that the number of invalid outputs from Turbo-16k remains a very small amount on both PART-A and PART-B while the invalid outputs from Llama2-16k dramatically increase with samples with longer input. Thus, LCLMs are less capable of following instructions on open-ended tasks for long contexts, compared with closed-ended tasks, such as multiple choice. A possible reason is that the pertaining or SFT corpus is highly likely to contain many training samples with similar question styles. This strongly enhances their instruction-following ability on closed-ended tasks. [p. 8–9]

**Figure 4** (p. 8): "Number of invalid outputs from Llama2 and Turbo."
Stacked bar chart with two groups on x-axis: PART-A (Length<4k) and PART-B (Length>4k). Four series: Llama2-4k, Llama2-16k, Turbo-4k, Turbo-16k. Y-axis is "Number of low quality outputs" ranging from 0 to 35. Key observations: For PART-A, Llama2-16k has ~8% invalid, Llama2-4k ~7%, Turbo-4k ~7%, Turbo-16k ~5%. For PART-B, Llama2-16k has ~25% (dramatic increase), Llama2-4k ~10%, Turbo-4k ~10%, Turbo-16k ~5% (remains stable). The figure shows that Llama2-16k's invalid outputs increase substantially with longer inputs while Turbo-16k remains robust.

### Performance on retrieval tasks contradicts reasoning tasks

[p. 9] The most popular NTK-aware positional embedding methods increase the base 10,000 in the vanilla RoPE to implement extrapolation without further fine-tuning. However, the performance on topic retrieval tasks does not match the reasoning capability over lengthy context. As can be seen from Figure 5, when the base is increased from 20,000 to 160,000, there is a continuous improvement on topic retrieval. However, performance on math reasoning tasks with lengthy examples exhibits a completely opposite trend, indicating that it is challenging for the model to maintain its reasoning abilities when increasing the base. In contrast, the performance on retrieval tasks seems to remain unaffected after the base reaches 60,000. [p. 9]

Further analysis in Section A.3 includes full results of n-gram metrics on open-ended tasks, the rankings of current LLMs, NTK-aware positional embedding and retrieval-based systems. [p. 9]

**Figure 5** (p. 9): "Test retrieval ability and reasoning ability with NTK base."
Line chart with NTK-base (×10^4) on x-axis (values: 2, 4, 6, 8, 12, 16) and Accuracy(%) on y-axis (0 to 60). Two lines: "GSM100 (Dishes)" (solid red line with circles) and "Topic retrieval" (dashed blue line with triangles). Topic retrieval increases from ~10% at base 2×10^4 to ~55% at base 6×10^4, then plateaus around 55%. GSM100 starts at ~40% at base 2×10^4 and steadily decreases to ~15% at base 16×10^4. The figure demonstrates that increasing the NTK base improves retrieval but degrades reasoning.
