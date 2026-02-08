# 4 Experiments [p. 6]

## 4.1 Benchmarking Results on LongBench and LongBench-E [p. 6]

### Experiment Setup

[p. 6] 8 popular LLMs evaluated that feature long context capability:
- **GPT-3.5-Turbo-16k** (OpenAI, 2022a)
- **Llama2-7B-chat-4k** (Touvron et al., 2023)
- **LongChat-v1.5-7B-32k** (Li et al., 2023)
- **XGen-7B-8k** (Nijkamp et al., 2023)
- **InternLM-7B-8k** (Team, 2023)
- **ChatGLM2-6B** (Du et al., 2022; Zeng et al., 2023)
- **ChatGLM2-6B-32k**: trained based on ChatGLM2-6B, with a 32k context length during alignment and position interpolation (Chen et al., 2023)
- **Vicuna-v1.5-7B-16k** (Zheng et al., 2023a)

LongChat-v1.5-7B-32k and Vicuna-v1.5-7B-16k are fine-tuned from Llama2-7B, with supervised fine-tuning and linear RoPE scaling.

### Evaluation Protocol

Assessment conducted in a zero-shot setting, except for few-shot learning tasks where few-shot examples are provided as part of the long context. Input format prompt and maximum output length are detailed in Appendix.

When input length L surpasses the maximum context length M of a model (indicated by the suffix of its name), the input sequence S is truncated from the middle since the front and end of the sequence may contain crucial information such as the instruction or question:

S_{1:L} -> [S_{1:floor(M/2)}; S_{L-floor(M/2)-1:L}]

Greedy decoding is used for reproducibility. Chat models typically have specific prompts that induce dialogue-like responses; during evaluation, these prompts are avoided in few-shot learning and code completion tasks since answers should be generated in a completion style rather than a chat style.

Metrics for each dataset are shown in Table 1. For tasks built on previous datasets, the metrics are consistent with those used in the original work. F1 and ROUGE-L (Lin, 2004) are

## Table 2 [p. 6]

**Table 2** (p. 6): "Results (%) on single-doc QA, multi-doc QA and summarization tasks."

| Model | 1-1 | 1-2 | 1-3 | 1-4 | Avg | 2-1 | 2-2 | 2-3 | 2-4 | Avg | 3-1 | 3-2 | 3-3 | 3-4 | Avg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GPT-3.5-Turbo-16k | 23.6 | 43.3 | 52.3 | 61.2 | 45.1 | 51.6 | 37.7 | 26.9 | 28.7 | 36.2 | 29.5 | 23.4 | 26.7 | 16.0 | 23.9 |
| Llama2-7B-chat-4k | 18.7 | 19.2 | 36.8 | 11.9 | 21.7 | 25.4 | 32.8 | 9.4 | 5.2 | 18.2 | 27.3 | 20.8 | 25.8 | 0.2 | 18.5 |
| LongChat-v1.5-7B-32k | 16.9 | 27.7 | 41.4 | 29.1 | 28.8 | 31.5 | 20.6 | 9.7 | 19.5 | 20.3 | 30.8 | 22.7 | 26.4 | 9.9 | 22.5 |
| XGen-7B-8k | 18.0 | 18.1 | 37.7 | 14.8 | 22.1 | 29.7 | 21.1 | 10.3 | 11.0 | 18.0 | 27.3 | 20.5 | 26.2 | 2.2 | 19.0 |
| InternLM-7B-8k | 12.1 | 16.7 | 23.4 | 33.6 | 21.4 | 28.7 | 22.8 | 9.0 | 11.1 | 17.9 | 9.7 | 15.9 | 22.8 | 12.4 | 15.2 |
| ChatGLM2-6B | 11.8 | 22.5 | 35.0 | 33.2 | 25.6 | 22.4 | 20.1 | 6.1 | 16.3 | 16.2 | 23.2 | 21.1 | 25.2 | 14.5 | 21.0 |
| ChatGLM2-6B-32k | 21.1 | 31.5 | 46.2 | 51.6 | 37.6 | 45.1 | 34.0 | 21.9 | 37.6 | 34.7 | 32.4 | 24.0 | 26.5 | 16.2 | 24.8 |
| Vicuna-v1.5-7B-16k | 19.4 | 26.1 | 38.5 | 43.0 | 31.8 | 25.3 | 20.8 | 9.8 | 19.3 | 18.8 | 27.9 | 22.8 | 27.2 | 15.1 | 23.2 |

## Table 3 [p. 6]

**Table 3** (p. 6): "Results (%) on few-shot learning, synthetic, and code tasks. 'Overall' is computed by the macro-average (the mean of 'Avg') over major task categories. This is computed on English (EN) tasks, Chinese (ZH) tasks, and all (All) tasks, code tasks are included in both languages."

| Model | 4-1 | 4-2 | 4-3 | 4-4 | Avg | 5-1 | 5-2 | 5-3 | Avg | 6-1 | 6-2 | Avg | EN | ZH | All |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GPT-3.5-Turbo-16k | 68.0 | 91.4 | 41.7 | 29.2 | 57.6 | 4.5 | 71.0 | 77.5 | 51.0 | 54.7 | 53.6 | 54.1 | 44.0 | 44.5 | 44.7 |
| Llama2-7B-chat-4k | 61.5 | 77.8 | 40.7 | 19.8 | 49.9 | 2.1 | 9.8 | 0.5 | 4.1 | 52.4 | 43.8 | 48.1 | 31.0 | 14.3 | 26.8 |
| LongChat-v1.5-7B-32k | 63.5 | 82.3 | 34.2 | 23.2 | 50.8 | 1.0 | 30.5 | 7.6 | 13.0 | 53.0 | 55.3 | 54.1 | 34.3 | 23.9 | 31.6 |
| XGen-7B-8k | 65.5 | 77.8 | 25.3 | 20.5 | 47.3 | 2.1 | 8.5 | 3.5 | 4.7 | 38.6 | 38.6 | 38.6 | 28.3 | 15.1 | 25.0 |
| InternLM-7B-8k | 52.0 | 77.8 | 21.2 | 15.2 | 41.6 | 3.0 | 6.0 | 0.9 | 3.3 | 44.1 | 28.8 | 36.4 | 24.2 | 18.3 | 22.6 |
| ChatGLM2-6B | 44.5 | 70.6 | 29.5 | 20.8 | 41.3 | 2.5 | 3.0 | 6.5 | 4.0 | 49.0 | 43.2 | 46.1 | 26.6 | 22.9 | 25.7 |
| ChatGLM2-6B-32k | 62.5 | 78.7 | 36.3 | 27.7 | 51.3 | 1.5 | 77.0 | 64.5 | 47.7 | 55.6 | 49.9 | 52.7 | 40.9 | 41.7 | 41.4 |
| Vicuna-v1.5-7B-16k | 71.5 | 86.2 | 40.8 | 28.8 | 56.8 | 6.5 | 4.5 | 5.0 | 5.3 | 51.0 | 43.5 | 47.3 | 31.9 | 26.4 | 30.5 |

---
[p. 7 continued]

### Metrics (continued)

F1 and ROUGE-L (Lin, 2004) are two popular N-gram based metrics widely adopted in QA and summarization tasks. Edit Sim (Levenshtein distance) is popularly used in code generation evaluation (Svyatkovskiy et al., 2020). For few-shot learning tasks, the first line of the response is extracted. For the two code completion tasks, the first line of model generation that is not a comment is extracted. The code and datasets are available at https://github.com/THUDM/LongBench.

### Results on LongBench

[p. 7] Tables 2 and 3 report the performance (%) on all datasets in LongBench. Additionally, Figure 4 presents a radar plot depicting the models' abilities on the 6 major tasks. For better visualization, the maximum score across all models on each task is scaled to 100 in the radar plot.

Key findings:

1. There is still a performance gap on long context tasks between open-sourced models of smaller size and the commercial model (GPT-3.5-Turbo-16k).
2. Models benefit from scaled positional embedding and continued training on longer context, as ChatGLM2-6B-32k and LongChat-v1.5-7B-32k obtain relative improvements of 62% and 19%, respectively.
3. The authors further analyze the multi-task property of LongBench by the inter-task correlation among and across each category of tasks in Appendix D. They find higher correlations for performance on tasks of the same category or language.

### Truncation Size Experiment

[p. 7] To study whether models with a longer maximum length truly benefit from utilizing longer context, experiments are conducted with GPT-Turbo-3.5-16k, ChatGLM2-6B-32k, and Vicuna-v1.5-7B-16k with truncation sizes of 4k and 8k on LongBench. The macro-average scores across all tasks with varying truncation sizes are depicted in Figure 2. Here, "maximum length" denotes truncation at the model's maximum length configuration.

GPT-Turbo-3.5-16k and ChatGLM2-6B-32k obtain higher scores under a larger truncation size, suggesting they can better make use of a longer context. This confirms that the benchmark indeed necessitates long context modeling — using truncated information alone is insufficient for successfully completing the tasks in LongBench. On the other hand, the performance of LLMs on LongBench can be further improved by enhancing their long context modeling capabilities.

**Figure 2** (p. 7): "Avg score (%) under different truncation size."

Bar chart showing average scores for three models under three truncation settings (4k truncation, 8k truncation, Maximum length):
- GPT-3.5-Turbo-16k: 39.1 (4k), 41.5 (8k), 44.7 (max) — bar labels read 44.7 and 44.2 at top of group
- ChatGLM2-6B-32k: 35.4 (4k), 39.3 (8k), 41.4 (max)
- Vicuna-v1.5-7B-16k: 30.5 (4k), 30.3 (8k), 30.2 (max) — scores remain essentially flat

### Results on LongBench-E

[p. 7-8] While LongBench facilitates measurement of an overall multi-task ability on tasks that require long context understanding, LongBench-E focuses more on measuring how the model's performance changes under different context lengths within the same task. As introduced in Sec 3.2.2, LongBench-E contains a subset of datasets included in LongBench, featuring more evenly distributed context lengths. Figure 3 reports the macro-average scores (%) on data in length ranges of 0-4k, 4k-8k, and 8k+ (results on all datasets in Table 9).

> "One can derive a model's long context ability from the slope of the curve — a significant drop in performance on data of greater length, as indicated by a steeper curve, points to the model's limitations in effectively handling long text modeling." [p. 8]

From the results on LongBench-E:
- ChatGLM2-6B-32k and LongChat-v1.5-7B-32k are more robust to longer context length, with a relative drop of 4% and 7% from 0-4k to 8k+ respectively.
- Despite GPT-3.5-Turbo-16k demonstrating impressive overall performance across all tasks, it still struggles on longer contexts (-17% from 0-4k to 8k+), leaving room for future development on long context modeling.

**Figure 3** (p. 7): "Average score (%) under different context length on LongBench-E."

Line chart with x-axis showing length ranges (0-4k, 4k-8k, 8k+) and y-axis showing Avg Score (25-45). Lines for 8 models:
- GPT-3.5-Turbo-16k starts highest (~47) but drops steeply to ~39 at 8k+
- ChatGLM2-6B-32k starts ~40 and drops slightly to ~38
- LongChat-v1.5-7B-32k starts ~37 and drops slightly to ~34
- Other models (Llama2-7B-chat-4k, XGen-7B-8k, InternLM-7B-8k, ChatGLM2-6B, Vicuna-v1.5-7B-16k) cluster in the 25-35 range with varying slopes

**Figure 4** (p. 7, referenced): Radar plot depicting the models' abilities on the 6 major tasks. Maximum score across all models on each task is scaled to 100. [Figure not directly visible in this window's pages but described in text.]

## 4.2 Impact of Context Compression Techniques [p. 8-9]

[p. 8] The authors further explore the impact of context compression techniques on LongBench, including retrieval-based context compression and summarization-based context compression.

### Retrieval-Based Compression

Retrieval is widely used in augmenting language models with external memory (Khandelwal et al., 2020; Borgeaud et al., 2022; Izacard et al., 2022b). This application can be extended to consider longer contexts, such as documents or books, as forms of external memory, from which relevant information can be retrieved using a specific query.

Given a long context, it is first split into chunks with a default size of M words (or characters on Chinese datasets), then a specific retriever is used to compute the embedding of the text chunks and the query, and only the top-N chunks are concatenated according to the cosine similarity of their embeddings to the query embedding. The top-N chunks as the compressed context, together with the query, are then fed into the model to produce an answer. A similar pipeline is also implemented in LangChain.

Experiments conducted with three retrievers — OpenAI Embedding (text-embedding-ada-002 (OpenAI, 2022b)), Contriever (Izacard et al., 2022a), and BM25 — alongside two chunk sizes of 200 and 500. For comparison under the same context length, the top-7 and top-3 chunks are taken when chunk sizes are 200 and 500 respectively. Table 4 reports the results on QA tasks in LongBench.

### Table 4 [p. 8]

**Table 4** (p. 8): "Retrieval-based context compression results (%) on LongBench. E, C, B denote different retrieval methods, namely text-embedding-ada-002, Contriever, and BM25. M x N indicates the retrieval of the top-N segments when split into chunks by M words. For every model and every dataset, the best performance over all retrieval methods is in **bold**."

| Retriever | 1-1 | 1-2 | 1-3 | 1-4 | 2-1 | 2-2 | 2-3 | 2-4 | Avg |
|---|---|---|---|---|---|---|---|---|---|
| *GPT-3.5-Turbo-16k* | | | | | | | | | |
| w/o retrieval | 23.6 | 43.3 | 52.3 | 61.2 | 51.6 | 37.7 | 26.9 | 28.7 | **40.7** |
| E-200x7 | 21.8 | 38.1 | 52.8 | 53.6 | 46.6 | **44.9** | 30.4 | 30.7 | 39.9 |
| E-500x3 | 21.8 | 39.6 | 50.3 | 55.9 | 49.3 | 38.6 | 23.3 | 30.4 | 38.6 |
| C-200x7 | 18.3 | 35.6 | **54.3** | 52.4 | 47.0 | 39.5 | 25.2 | 30.5 | 37.8 |
| C-500x3 | 20.3 | 35.7 | 48.7 | 51.2 | 47.7 | 39.1 | 21.9 | 30.7 | **36.9** |
| B-200x7 | 14.1 | 28.6 | 30.1 | 55.0 | 38.3 | 29.0 | 18.1 | 29.6 | 30.3 |
| B-500x3 | 14.5 | 30.4 | 31.3 | 55.1 | 37.2 | 35.1 | 11.7 | 29.9 | 30.6 |
| *Llama2-7B-chat-4k* | | | | | | | | | |
| w/o retrieval | 18.7 | 19.2 | 36.8 | 11.9 | 25.4 | 32.8 | 9.4 | 5.2 | 19.9 |
| E-200x7 | **20.0** | **25.7** | 40.3 | 13.9 | 34.7 | 34.4 | 17.3 | 5.5 | **24.0** |
| E-500x3 | 17.7 | 25.2 | 38.9 | 12.0 | **34.9** | 32.8 | 15.5 | 5.0 | 22.7 |
| C-200x7 | 18.3 | 23.8 | **41.8** | 10.8 | 33.6 | 34.5 | 17.2 | 5.0 | 23.1 |
| C-500x3 | 17.1 | 22.5 | 39.5 | 9.9 | 34.6 | **35.0** | 14.1 | 4.7 | 22.2 |
| B-200x7 | 12.3 | 19.6 | 25.9 | 13.1 | 29.2 | 25.9 | 9.1 | 5.1 | 17.5 |
| B-500x3 | 14.7 | 20.4 | 26.2 | 13.5 | 23.1 | 29.7 | 7.9 | 5.0 | 17.6 |
| *ChatGLM2-6B-32k* | | | | | | | | | |
| w/o retrieval | 21.1 | 31.5 | **46.2** | **51.7** | **45.1** | 34.0 | 21.9 | 37.6 | **36.1** |
| E-200x7 | 19.4 | **33.3** | 40.9 | 48.3 | 41.2 | 32.9 | **22.8** | 36.7 | 34.4 |
| E-500x3 | 14.6 | 31.2 | 40.5 | 46.3 | 39.4 | 31.5 | 20.2 | **38.1** | 32.7 |
| C-200x7 | 15.1 | 32.9 | 43.1 | 45.8 | 38.3 | 32.3 | 16.9 | 35.5 | 32.5 |
| C-500x3 | 12.9 | 29.6 | 41.1 | 49.2 | 38.1 | 33.2 | 17.5 | 37.8 | 32.4 |
| B-200x7 | 12.5 | 20.1 | 23.8 | 50.2 | 28.7 | 24.3 | 10.9 | 35.0 | 25.7 |
| B-500x3 | 11.2 | 20.5 | 25.4 | **51.9** | 27.7 | 27.6 | 12.2 | 35.6 | 26.5 |

Key findings:
1. text-embedding-ada-002 performs best among the three retrievers, while the open-sourced Contriever results are closer to text-embedding-ada-002 and superior to BM25.
2. In general, splitting the long context into shorter chunks and retrieving more chunks results in better performance.
3. Under the best retrieval method, the improvements for the three models are -2%, 21%, and -5%, respectively. Moreover, even after retrieval, the performance of Llama2-7B-chat-4k still lags behind the other two models.

> "The results suggest that the retrieval technique can only serve as a performance compensation for models that cannot well model long context, and is not a shortcut to solving long context understanding tasks." [p. 8]

### Summarization-Based Compression

[p. 8-9] The authors also study the effect of using model-generated summary as a context compression technique. Specifically, the model is first utilized to generate a brief summary for each text chunk, and the summaries are concatenated together as the compressed context. Experiments are on the summarization tasks in LongBench.

### Table 5 [p. 8]

**Table 5** (p. 8): "Summarization-based context compression results (%) on LongBench."

| Model | 3-1 | 3-2 | 3-3 | 3-4 | Avg |
|---|---|---|---|---|---|
| GPT-3.5-Turbo-16k | 29.5 | 23.4 | 26.7 | 16.0 | 23.9 |
| GPT-3.5-Turbo-16k+Summ | 17.9 | 16.6 | 17.9 | 19.7 | 18.0 |
| Llama2-7B-chat-4k | 27.3 | 20.8 | 25.8 | 0.2 | 18.5 |
| Llama2-7B-chat-4k+Summ | 12.8 | 16.6 | 4.6 | 0.6 | 8.6 |
| ChatGLM2-6B-32k | 32.4 | 24.0 | 26.5 | 16.2 | 24.8 |
| ChatGLM2-6B-32k+Summ | 17.6 | 15.9 | 14.9 | 17.2 | 16.4 |

This compression method improves performance of the models only on the VCSUM task (3-4), since the data in VCSUM are longer than in the other three datasets.

## 4.3 Context Understanding or Memorization? [p. 9]

[p. 9] Since the model may have potentially encountered the long context during pre-training, it may rely on memorization rather than context understanding to answer the question. The authors conduct an experiment to assess the degree to which these tasks rely on memorization rather than long context understanding capability.

Specifically, the context is withheld from the model, posing only questions to it, and evaluating its performance. Table 6 shows the results for GPT-3.5-Turbo-16k, Llama2-7B-chat-4k, and ChatGLM2-6B-32k on the Single-Doc QA and Multi-Doc QA datasets in LongBench.

### Table 6 [p. 9]

**Table 6** (p. 9): "Assessing context understanding vs. memorization."

Numbers in parentheses show the improvement of the with-context version over the without-context version.

| Model | NarrativeQA | Qasper | MultiFieldQA-en | MultiFieldQA-zh | HotpotQA | 2WikiMQA | MuSiQue | DuReader |
|---|---|---|---|---|---|---|---|---|
| GPT-3.5-Turbo-16k (w/o context) | 4.7 | 12.4 | 15.7 | 10.9 | 31.7 | 28.9 | 15.0 | 17.1 |
| GPT-3.5-Turbo-16k | 23.6 (+18.9) | 43.3 (+30.9) | 52.3 (+36.6) | 61.2 (+50.3) | 51.6 (+19.9) | 37.7 (+8.8) | 26.9 (+11.9) | 28.7 (+11.6) |
| Llama2-7B-chat-4k (w/o context) | 7.9 | 12.5 | 16.4 | 5.1 | 25.5 | 28.2 | 9.8 | 2.6 |
| Llama2-7B-chat-4k | 18.7 (+10.8) | 19.2 (+6.7) | 36.8 (+20.4) | 11.9 (+6.8) | 25.4 (-0.1) | 32.8 (+4.6) | 9.4 (-0.4) | 5.2 (+2.6) |
| ChatGLM2-6B-32k (w/o context) | 8.9 | 14.2 | 12.5 | 20.4 | 17.0 | 19.9 | 7.7 | 16.9 |
| ChatGLM2-6B-32k | 21.1 (+12.2) | 31.5 (+17.3) | 46.2 (+33.7) | 51.6 (+31.2) | 45.1 (+28.1) | 34.0 (+14.1) | 21.9 (+14.2) | 37.6 (+20.7) |

The memorization performance (w/o context) on HotpotQA, 2WikiMultihopQA, and MuSiQue is relatively high. This is likely because these datasets are derived from Wikipedia, a common source for training prevalent LLMs.

The delta score (original score minus the score when context is absent) addresses the memorization phenomenon (Yu et al., 2024), and could also serve as an important indicator for a model's long context understanding ability.
