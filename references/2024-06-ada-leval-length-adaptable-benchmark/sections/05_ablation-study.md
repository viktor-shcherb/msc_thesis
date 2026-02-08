# Ablation Study [p. 7–9]

## Perplexity Evaluation on TSort [p. 7]

Perplexity (PPL) evaluation is frequently adopted to assess the capability of LLMs. During inference, models compute the perplexity of multiple candidates and the one with the lowest perplexity is selected as the inference result. For TSort, the authors create 24 candidates for perplexity computation, each candidate is a permutation of the 4 text segments. [p. 7]

PPL-based evaluation is conducted for open-source LLMs on 2k, 4k and 8k text length settings. Table 7 exhibits the PPL-Eval result on TSort. When text segments are arranged in the correct order, a significantly lower perplexity score can usually be observed (footnote 5: "One potential cause is that the chapters have been used for pretraining"), resulting in the high TSort accuracy. However, when the sorting task is presented as QAs where LLMs are asked to directly output the correct order, the performance significantly deteriorates, indicating the limited instruction following capabilities of existing LLMs. [p. 7]

**Table 7** (p. 7): Perplexity Evaluation Results on **TSort** for open-source LLMs.

| TSort (PPL Eval) | 2k | 4k | 8k |
|---|---|---|---|
| LongChat-7b-v1.5-32k | 60.9 | 68.3 | 77.4 |
| ChatGLM2-6B-32k | 40.5 | 53.5 | 57.5 |
| ChatGLM3-6B-32k | 50.1 | 57.0 | 59.3 |
| Vicuna-7b-v1.5-16k | 70.1 | 78.3 | 77.7 |
| Vicuna-13b-v1.5-16k | 79.3 | 86.7 | 89.2 |
| Random Guess | 4.2 | 4.2 | 4.2 |

## Position Bias in BestAnswer [p. 7–8]

To study the position bias of existing LLMs, in BestAnswer, the authors keep questions and answer candidates the same and alter the position of groundtruth answers. Specifically, they manually set the groundtruth answer at the beginning, in the middle, or at the rear of all answers and then perform the evaluation. Table 8 displays the evaluation results. [p. 7]

> "**All models demonstrate significant position bias in choosing the most helpful answer.**" [p. 8]

Most models achieve much better accuracy when the most helpful answer presents at the beginning. Claude-2 has some unique behaviors: it performs the best when the groundtruth is positioned at the rear across 4 of 5 different settings. As the input length increases, the position bias becomes more obvious. For instance, Vicuna-7b-v1.5-16k demonstrates relatively uniform accuracy under the 1k setting. However, when the input length extends to 16k tokens, the model's performance remains stable only when the best answer is at the front. [p. 8]

**Table 8** (p. 8): Results of LLMs on **BestAnswer** where the best answer is set at the front, in the middle and at the rear of all answers. Pos denotes the position of the best answer.

| BestAnswer | Pos | 1k | 2k | 4k | 8k | 16k |
|---|---|---|---|---|---|---|
| GPT-4-Turbo-1106 | front | 76.5 | 82.5 | 86.5 | 90.0 | 82.0 |
| GPT-4-Turbo-1106 | mid | 74.5 | 68.0 | 60.0 | 38.0 | 38.5 |
| GPT-4-Turbo-1106 | rear | 57.5 | 46.6 | 44.0 | 40.5 | 26.5 |
| GPT-3.5-Turbo-1106 | front | 77.0 | 80.5 | 77.0 | 46.5 | 2.5 |
| GPT-3.5-Turbo-1106 | mid | 64.5 | 48.5 | 32.0 | 9.5 | 0.5 |
| GPT-3.5-Turbo-1106 | rear | 37.5 | 19.0 | 8.5 | 6.0 | 3.5 |
| Claude-2 | front | 34.0 | 19.0 | 14.5 | 50.0 | 6.0 |
| Claude-2 | mid | 49.0 | 35.5 | 21.5 | 13.0 | 5.0 |
| Claude-2 | rear | 59.0 | 36.5 | 26.0 | 11.0 | 9.5 |
| LongChat-7b-v1.5-32k | front | 24.1 | 5.0 | 12.1 | 33.6 | 29.0 |
| LongChat-7b-v1.5-32k | mid | 32.7 | 13.6 | 0.2 | 0.2 | 0.0 |
| LongChat-7b-v1.5-32k | rear | 29.8 | 1.9 | 0.0 | 0.1 | 0.1 |
| ChatGLM2-6B-32k | front | 30.0 | 31.5 | 46.2 | 10.5 | 0.5 |
| ChatGLM2-6B-32k | mid | 27.7 | 10.4 | 1.0 | 0.1 | 0.1 |
| ChatGLM2-6B-32k | rear | 28.5 | 12.4 | 2.6 | 4.1 | 0.0 |
| ChatGLM3-6B-32k | front | 48.9 | 34.3 | 37.6 | 35.8 | 19.0 |
| ChatGLM3-6B-32k | mid | 41.9 | 22.3 | 5.3 | 0.9 | 0.1 |
| ChatGLM3-6B-32k | rear | 28.8 | 5.4 | 3.7 | 8.8 | 2.9 |
| Vicuna-7b-v1.5-16k | front | 29.3 | 8.9 | 14.0 | 37.6 | 25.4 |
| Vicuna-7b-v1.5-16k | mid | 32.8 | 13.6 | 0.0 | 0.0 | 0.2 |
| Vicuna-7b-v1.5-16k | rear | 34.2 | 2.1 | 0.0 | 0.0 | 0.7 |
| Vicuna-13b-v1.5-16k | front | 52.5 | 51.4 | 58.6 | 81.7 | 11.8 |
| Vicuna-13b-v1.5-16k | mid | 64.5 | 29.2 | 1.5 | 0.5 | 0.3 |
| Vicuna-13b-v1.5-16k | rear | 34.2 | 2.4 | 0.0 | 0.0 | 13.4 |

## Scalable Position Embeddings [p. 8–9]

Scalable position embeddings have shown their value in extending context window while requiring minimal or no fine-tuning steps. Existing position embedding methods for context window extension can be categorized into two major categories: position interpolation and length extrapolation. NTK-aware Scaled RoPE utilizes the advantage of both methods by changing the base of RoPE. ReRoPE and Leaky ReRoPE (Su, 2023) design a window size to control the application of scalable position embeddings directly. [p. 8]

The study is conducted on Vicuna-v1.5 models (Zheng et al., 2023), which are Llama 2 fine-tuned with 4k context window. Original models (4k context window) are adopted as the baseline across all settings. Table 9 shows the result of different position embedding methods on the BestAnswer benchmark. [p. 8-9]

> "**scalable position embeddings do improve the long-context modeling capability**" [p. 9]

All methods enhance the accuracy under the 8k setting, which is beyond the original context window. Concurrently, the model performance under short settings (1k, *e.g.*) is basically retained. NTK-aware Scaled RoPE diminishes performance on 1k context length, but outperforms other two methods on longer context. The advantage of these methods is more obvious on Vicuna-13b-v1.5. Moreover, comparing to their 16k versions, which utilize Flash Attention and are further trained on high-quality 16k length conversation data, advanced scalable position embeddings still achieve comparable performance. [p. 9]

**Table 9** (p. 9): Results of Vicuna-v1.5 with different context window extrapolation methods on **BestAnswer**. 'Original (4k) / (16k)' denotes the original Vicuna model trained with 4k / 16k context lengths. In the reported 'X/Y', X indicates the accuracy while Y indicates the accuracy which cases failed to follow the instruction are excluded.

| Vicuna-7b-v1.5 | 1k | 2k | 4k | 8k |
|---|---|---|---|---|
| ReRoPE | 39.6/39.6 | 11.6/11.6 | 4.7/5.4 | 2.3/3.2 |
| Leaky ReRoPE | 39.9/39.9 | 11.2/11.2 | 5.1/5.7 | 1.3/2.0 |
| NTK | 32.5/32.5 | 10.7/10.7 | 5.8/5.8 | 3.9/3.9 |
| Original(4k) | 39.5/39.5 | 9.8/11.0 | 4.2/5.5 | 0.0/0.0 |
| Original(16k) | 37.0/39.5 | 11.1/11.1 | 5.8/5.8 | 2.5/2.7 |
| Vicuna-13b-v1.5 | 1k | 2k | 4k | 8k |
| ReRoPE | 49.2/49.2 | 22.5/22.5 | 9.2/10.0 | 1.5/2.8 |
| Leaky ReRoPE | 49.3/49.3 | 23.8/23.8 | 8.7/9.8 | 1.3/2.6 |
| NTK | 43.8/43.8 | 23.0/23.0 | 11.1/11.1 | 2.3/2.3 |
| Original(4k) | 49.1/49.1 | 17.7/17.7 | 5.9/5.9 | 0.1/1.0 |
| Original(16k) | 53.4/53.4 | 29.2/29.2 | 13.1/13.5 | 2.6/2.7 |

## Comparison with Other Long-Context Benchmarks [p. 9]

Ada-LEval is compared with other long-context benchmarks to validate that these benchmarks require much more overall text understanding to complete the task than traditional long-context benchmarks. [p. 9]

A task is regarded to require models to understand text comprehensively if the performances of models decrease sharply when the text is truncated. TSort task meets this requirement since truncating any segment will lead to an incorrect answer. [p. 9]

To exhibit the BestAnswer requires more comprehensive text understanding than traditional QA and summarization tasks, an experiment is conducted on BestAnswer (16k version) and 2 classic long-context datasets: NarrativeQA (LongBench subset, QA task) and GovReport (LongBench subset, summarization task). The metric for NarrativeQA is F1 score and metric for GovReport is Rouge-L. The performance of GPT-4-Turbo-1106 is evaluated on all 3 datasets. Each test case is truncated into 2k, 4k and 8k version as the input. The full version is also provided for comparison. [p. 9]

**Table 10** (p. 9): Results of GPT-4-Turbo on different long-context benchmarks.

| Benchmark | 2k | 4k | 8k | Full | Avg #tokens |
|---|---|---|---|---|---|
| BestAnswer | 11.0 | 20.0 | 31.5 | 44.0 | 15646 |
| NarrativeQA | 24.7 | 25.6 | 29.7 | 33.1 | 10276 |
| GovReport | 30.7 | 32.4 | 33.6 | 30.9 | 29872 |

From Table 10, the performance of GPT-4-Turbo on BestAnswer decreases more dramatically than NarrativeQA and GovReport when text is truncated. Notably, the performance on GovReport even increases when text is truncated into 4k and 8k. Therefore, the Ada-LEval benchmarks require more full-text comprehension than traditional QA and summarization tasks. [p. 9]
