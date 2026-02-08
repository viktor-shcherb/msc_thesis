# Evaluation Results [p. 5-6]

## Experiment Setup [p. 5]

Models evaluated under **long-context** settings:
- 4 proprietary models: (1) GPT-4-Turbo-0125, (2) GPT-4-Turbo-1106, (3) GPT-3.5-Turbo-1106, (4) Claude-2
- 6 open-source models: (5) LongChat-7b-v1.5-32k (Zheng et al., 2023), (6) ChatGLM2-6B-32k (Zeng et al., 2022), (7) ChatGLM3-6B-32k (Zeng et al., 2022), (8) Vicuna-7b-v1.5-16k (Zheng et al., 2023), (9) Vicuna-13b-v1.5-16k (Zheng et al., 2023), (10) InternLM2-7b (Cai et al., 2024)

Due to the inferior performance of open-source LLMs under long-context settings, only models with good performance (GPT-4-Turbo, Claude-2, *etc.*) are evaluated under ultra-long-context settings.

**Evaluation details:**
- Open-source LLMs: 1000-testcase subset for evaluation under each length setting
- Proprietary models: 200-testcase subset (sampled from the 1000-testcase set) for long-context settings, 50-testcase subset for ultra-long-context settings (due to costly API)
- All experiments conducted using the open-source LLM evaluation platform OpenCompass (Contributors, 2023)
- Zero-shot setting for all evaluation
- A "random guess" baseline provided
- Instruction following rate and copy instruction rate measured on both tasks

Instruction following rate: whether LLM outputs follow the pre-defined format. Copy instruction rate: whether the LLM outputs the same answer as in-context example provides.

## Long-Context Evaluation Results [p. 5-6]

**Table 2** (p. 5): TSort results under long-context settings. The number of segments N = 4 for TSort evaluation, thus random guess accuracy is roughly 4.2% (1 / 24).

| TSort | 2k | 4k | 8k | 16k |
|---|---|---|---|---|
| GPT-4-Turbo-0125 | 15.5 | **16.5** | **8.5** | **5.5** |
| GPT-4-Turbo-1106 | **18.5** | 15.5 | 7.5 | 3.5 |
| GPT-3.5-Turbo-1106 | 4.0 | 4.5 | 4.5 | **5.5** |
| Claude-2 | 5.0 | 5.0 | 4.5 | 3.0 |
| LongChat-7b-v1.5-32k | 5.3 | 5.0 | 3.1 | 2.5 |
| ChatGLM2-6B-32k | 0.9 | 0.7 | 0.2 | 0.9 |
| ChatGLM3-6B-32k | 2.3 | 2.4 | 2.0 | 0.7 |
| Vicuna-7b-v1.5-16k | 5.3 | 2.2 | 2.3 | 1.7 |
| Vicuna-13b-v1.5-16k | 5.4 | 5.0 | 2.4 | 3.1 |
| InternLM2-7b | 5.1 | 3.9 | 5.1 | 4.3 |
| Random Guess | 4.2 | 4.2 | 4.2 | 4.2 |

**TSort analysis** [p. 5]: This evaluation underscores the complexity of TSort, highlighting its intricate nature that necessitates comprehensive understanding and reasoning across long text. Under settings from 2,000 to 8,000 tokens, only the most powerful proprietary model GPT-4-Turbo outputs the correct order of texts with a significant higher probability compared to the random baseline. When the context window expands to 16,000, the quality of GPT-4-Turbo's predictions also deteriorates to the random guess level. Other LLMs, encompassing both proprietary and open-source models, all display similar performance compared to random guess (even under the relative short 2k setting). The TSort task posts a severe challenge to existing LLMs.

**Table 3** (p. 6): BestAnswer results under long-context settings. For a question with N candidate answers, random guess accuracy is defined as 1/N. The random guess accuracy over a long-context setting is the average of random guess accuracy for all questions within the test set.

| BestAnswer | 1k | 2k | 4k | 6k | 8k | 12k | 16k |
|---|---|---|---|---|---|---|---|
| GPT-4-Turbo-0125 | 73.5 | **73.5** | 65.5 | **63.0** | **56.5** | **52.5** | **44.5** |
| GPT-4-Turbo-1106 | **74.0** | **73.5** | **67.5** | 59.5 | 53.5 | 49.5 | 44.0 |
| GPT-3.5-Turbo-1106 | 61.5 | 48.5 | 41.5 | 29.5 | 17.0 | 2.5 | 2.5 |
| Claude-2 | 65.0 | 43.5 | 23.5 | 15.0 | 17.0 | 12.0 | 11.0 |
| LongChat-7b-v1.5-32k | 32.4 | 10.7 | 5.7 | 3.1 | 1.9 | 1.6 | 0.8 |
| ChatGLM2-6B-32k | 31.2 | 10.9 | 4.5 | 1.6 | 1.6 | 0.0 | 0.3 |
| ChatGLM3-6B-32k | 39.8 | 18.8 | 9.0 | 5.0 | 3.4 | 0.9 | 0.5 |
| Vicuna-7b-v1.5-16k | 37.0 | 11.1 | 5.8 | 3.2 | 1.8 | 1.9 | 1.0 |
| Vicuna-13b-v1.5-16k | 53.4 | 29.2 | 13.1 | 4.3 | 2.2 | 1.4 | 0.9 |
| InternLM2-7b | 58.6 | 49.5 | 33.9 | 12.3 | 13.4 | 2.0 | 0.8 |
| Random Guess | 26.7 | 10.1 | 4.5 | 3.0 | 2.3 | 1.4 | 1.1 |

**BestAnswer analysis** [p. 5-6]: GPT-4-Turbo establishes the state-of-the-art on the BestAnswer benchmark. It achieves an outstanding 44.5% accuracy under the 16k long-context setting, where around 100 distractor answers exist for each question. Among other proprietary models, Claude-2 achieves the second best accuracy 11% under the 16k setting. GPT-3.5-Turbo-1106, while outperforming Claude-2 under some relative short settings (2k, 4k, 6k), demonstrates performance similar to random guess under the 16k setting. There is a considerable performance gap between proprietary models and open-source models on BestAnswer. Although some models like Vicuna-13b-v1.5-16k and InternLM2-7b perform well under short settings, a dramatic accuracy decline can be observed when text length becomes larger.

## Error Breakdown [p. 6]

Most errors on TSort and BestAnswer can be attributed to two categories:
1. The LLM fails to follow the provided instruction and does not output a valid answer. (A valid answer contains a permutation of N segment numbers on TSort and at least one designation of answers on BestAnswer.)
2. The LLM does output a valid answer, but it simply copies the example answer provided in the in-context example.

**Figure 2** (p. 7): "The instruction following rate of LLMs on TSort (Left) and BestAnswer (Right) under long-context settings. GPT-4-Turbo on TSort and all proprietary models on BestAnswer achieve 100% instruction following rate across all long-context settings, thus not displayed."
- Left panel (TSort): X-axis = Context Length (#Tokens, from 2k to 16k), Y-axis = Instruction Following Rate (0%-100%). Models plotted: GPT-3.5-Turbo-1106, Claude-2, LongChat-7b-v1.5-32k, ChatGLM2-6B-32k, ChatGLM3-6B-32k, Vicuna-7b-v1.5-16k, Vicuna-13b-v1.5-16k. Claude-2 maintains near 100% across all lengths. GPT-3.5-Turbo-1106 starts near 80% at 2k but drops. LongChat starts near 100% at 2k but declines to ~20% at 16k. ChatGLM models show low instruction following rates across all lengths. Vicuna-7b drops sharply from ~60% at 2k to near 0% at 8k-16k.
- Right panel (BestAnswer): X-axis = Context Length (#Tokens, from 1k to 16k), Y-axis = Instruction Following Rate (0%-100%). Similar pattern: Claude-2 maintains near 100%. Most open-source models decline as text length increases. ChatGLM2 and ChatGLM3 show very low rates especially at longer contexts.

Figure 2 displays instruction following rate on TSort and BestAnswer. Tables 4 and 5 provide detailed statistics about the copy instruction rate on TSort and BestAnswer.

**Table 4** (p. 6): The copy instruction rate of LLMs on **TSort** under long-context settings. **Expectation** means the ratio of test cases for which the in-context example answer is exactly the correct one.

| CopyInst Rate | 2k | 4k | 8k | 16k |
|---|---|---|---|---|
| GPT-4-Turbo-1106 | 25.0 | 22.0 | 10.5 | 1.0 |
| GPT-3.5-Turbo-1106 | 30.0 | 25.5 | 64.5 | 73.3 |
| Claude-2 | 99.5 | 95.0 | 97.4 | 96.9 |
| Expectation | 5.0 | 5.0 | 5.0 | 5.5 |
| LongChat-7b-v1.5-32k | 100.0 | 99.8 | 99.1 | 100.0 |
| ChatGLM2-6B-32k | 11.3 | 13.8 | 10.5 | 81.3 |
| ChatGLM3-6B-32k | 21.6 | 54.8 | 88.0 | 88.1 |
| Vicuna-7b-v1.5-16k | 100.0 | 100.0 | 59.4 | 33.3 |
| Vicuna-13b-v1.5-16k | 96.6 | 99.0 | 12.2 | 3.1 |
| Expectation | 5.3 | 5.0 | 5.4 | 5.2 |

**Table 5** (p. 6): The copy instruction rate of LLMs on **BestAnswer** under long-context settings. **Expectation** means the ratio of test cases for which the in-context example answer is exactly the correct one.

| CopyInst Rate | 1k | 2k | 4k | 6k | 8k | 12k | 16k |
|---|---|---|---|---|---|---|---|
| GPT-4-Turbo-1106 | 12.5 | 8.5 | 5.0 | 5.5 | 6.0 | 2.0 | 2.0 |
| GPT-3.5-Turbo-1106 | 16.5 | 22.5 | 18.5 | 16.0 | 11.5 | 2.0 | 0.0 |
| Claude-2 | 21.5 | 25.5 | 40.5 | 41.0 | 42.5 | 49.0 | 55.0 |
| Expectation | 13.0 | 7.0 | 3.0 | 2.0 | 2.5 | 1.5 | 1.5 |
| LongChat-7b-v1.5-32k | 67.4 | 94.7 | 89.5 | 97.8 | 70.6 | 49.4 | 13.0 |
| ChatGLM2-6B-32k | 36.5 | 43.7 | 35.8 | 27.2 | 24.4 | 35.5 | 44.7 |
| ChatGLM3-6B-32k | 47.9 | 66.1 | 33.3 | 30.4 | 22.5 | 24.8 | 16.7 |
| Vicuna-7b-v1.5-16k | 63.1 | 96.2 | 91.8 | 47.9 | 66.6 | 27.8 | 17.9 |
| Vicuna-13b-v1.5-16k | 27.8 | 45.8 | 55.3 | 19.8 | 3.4 | 5.6 | 11.1 |
| Expectation | 14.4 | 10.0 | 5.1 | 2.3 | 1.7 | 1.3 | 1.2 |

**Error analysis summary** [p. 6]: The state-of-the-art GPT-4-Turbo maintains a relatively low copy instruction rate and impeccable instruction following rate on both tasks. Error instances of Claude-2, LongChat and Vicuna models are predominantly due to elevated Copy Instruction Rate, while ChatGLM models suffer from low instruction following rate. It is worth noting that all models, with the sole exception of GPT-4-Turbo, find it more difficult to follow the instruction on both tasks as text length increases.

## Ultra-Long-Context Evaluation Results [p. 6]

Models evaluated under ultra-long-context settings: (1) GPT-4-Turbo-0125, (2) GPT-4-Turbo-1106, (3) Claude-2, (4) Claude-2.1. InternLM2-7b also evaluated on BestAnswer benchmark under ultra-long-context settings. Due to high API calling expense, 50 samples tested under each ultra-long context setting. Table 6 demonstrates the result.

Though the evaluated models claim that they can understand long text up to 100,000+ tokens (a whole book with hundreds of pages, *e.g.*), they suffer from a dramatic decline on their performance under ultra-long-context settings, comparing to their long-context performance. [p. 6-7]

**Table 6** (p. 7): Results of LLMs on TSort and BestAnswer benchmarks in ultra-long context settings.

| Benchmark | Model | 32k | 64k | 128k |
|---|---|---|---|---|
| TSort | GPT-4-Turbo-0125 | 2.0 | 4.0 | 2.0 |
| TSort | GPT-4-Turbo-1106 | **6.0** | **6.0** | **6.0** |
| TSort | Claude-2 | 0.0 | 0.0 | / |
| TSort | Claude-2.1 | 0.0 | 0.0 | 0.0 |
| TSort | Random Guess | 4.2 | 4.2 | 4.2 |
| BestAnswer | GPT-4-Turbo-0125 | **30.0** | 0.0 | 0.0 |
| BestAnswer | GPT-4-Turbo-1106 | 16.0 | 0.0 | 0.0 |
| BestAnswer | Claude-2 | 4.0 | 0.0 | / |
| BestAnswer | Claude-2.1 | 4.0 | 0.0 | 0.0 |
| BestAnswer | InternLM2-7b | 0.5 | **0.5** | 0.0 |
| BestAnswer | Random Guess | 0.6 | 0.3 | 0.1 |

For the TSort task, GPT-4-Turbo is able to achieve a random guess level accuracy, while Claude fails to give any correct answers. For BestAnswer, the performance of all three models falls sharply from 16k to 32k text length. Meanwhile, they cannot give any correct answer when the text length is greater than 32k. [p. 7]
