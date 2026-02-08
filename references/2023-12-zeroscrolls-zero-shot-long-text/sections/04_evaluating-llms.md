# 4 Evaluating State-of-the-Art LLMs [p. 5–6]

[p. 5] Using ZeroSCROLLS, the authors conduct, to the best of their knowledge, the first systematic LLMs zero-shot performance comparison over tasks that require long text understanding.

## 4.1 Models

[p. 5] Both open-source models and closed products available via APIs are evaluated. Greedy decoding is applied to all models, and further research into other decoding strategies is left to future work. Table 2 shows the selection of models evaluated.

**Table 2** (p. 5): "State of the art LLMs we evaluate. Exact parameter counts of closed models are not publicly available."

| Model | Params | Maximum Length | Open/Closed |
|---|---|---|---|
| T0pp | 11B | 8,192 | Open |
| Flan-T5 | 11B | 8,192 | Open |
| Flan-UL2 | 20B | 8,192 | Open |
| DaVinci003 | -- | 4,096 | Closed |
| ChatGPT | -- | 4,096 | Closed |
| Claude | -- | 8,192 | Closed |
| GPT-4 | -- | 8,192 | Closed |

**Open Source Models** [p. 5] The authors experiment with **Flan-T5-xxl** (Wei et al., 2022a) and **Flan-UL2**, the instruction-tuned versions of T5 (Raffel et al., 2020) and UL2 (Tay et al., 2023), as well as **T0pp** (Sanh et al., 2022), an LM-adapted (Lester et al., 2021) version of T5 that was finetuned on various NLP tasks for zero shot generalization. For all open-source models a maximum input length of 8,192 tokens is used (larger contexts were unstable). Shorter context lengths and smaller variants of Flan-T5 are also experimented with. [p. 5]

**Closed Models (Products)** [p. 5–6] Using product APIs, the authors evaluate **Claude** v1.3 from Anthropic, **DaVinci003**, **ChatGPT** v0301, and **GPT-4** v0314 (OpenAI, 2023) from OpenAI. The maximal context length of these models includes both input and output. [p. 5–6]

**Task-Specific Models** [p. 6] To compare general-purpose LLMs (zero-shot) to task-specific models (fine-tuned), predictions by **CoLT5-xl** (Ainslie et al., 2023) are used, a transformer allocating more resources to important tokens, with a maximum input length of 16,384 tokens and the current state of the art on SCROLLS. [p. 6]

**Naive Baselines** [p. 6] Simple baselines are implemented for all tasks:
- For GovReport, SummScreenFD, QMSum, SQuALITY and NarrativeQA: select random spans from the input document of 500, 200, 50, 120 and 4 words respectively.
- For Qasper: randomly decide whether to use one of its fixed choices ("Yes", "No", "Unanswerable") or choose a random span of 15 words.
- For MuSiQue: use "Unanswerable" for every instance.
- For QuALITY: randomly select an option from A, B, C, or D.
- For SpaceDigest: always use 50%.
- For BookSumSort: use the trivial permutation "1, 2, 3, ..., n." [p. 6]

**Human Performance** [p. 6] Human performance figures are provided for 6 of the 10 tasks. For SQuALITY, Wang et al. (2022) estimate human performance by comparing one reference against the other three. Similarly, for Qasper and NarrativeQA, inter-annotator F1 is calculated on the ZeroSCROLLS subsets. The human scores reported by Pang et al. (2022) are used on the full QuALITY test set, while for MuSiQue, statistics on answerable and non-answerable sets from Trivedi et al. (2022) are combined. For SpaceDigest, the authors use their own human annotations (Section 3.1.3) to estimate exponential similarity over 50 reviews. [p. 6]

## 4.2 Main Results

[p. 6] Table 3 shows the results for every model on every ZeroSCROLLS task, along with the average.

**Table 3** (p. 6): "The ZeroSCROLLS leaderboard, at the time of writing. The dataset abbreviations stand for: GovReport, SummScreenFD, QMSum, SQuALITY, Qasper, NarrativeQA, QuALITY, MuSiQue, SpaceDigest, BookSumSort."

| Model | Tokens | GvRp R_geo | SSFD R_geo | QMsm R_geo | SQAL R_geo | Qspr F1 | Nrtv F1 | QALT AC | MuSQ F1 | SpDg ES | BkSS C_idx | Avg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Baselines** | | | | | | | | | | | | |
| Naive | -- | 22.6 | 6.7 | 6.7 | 10.5 | 6.1 | 2.1 | 26.6 | 20.0 | 45.0 | 50.0 | *19.6* |
| Human | -- | -- | -- | -- | 23.6 | 67.7 | 58.2 | 93.5 | 74.8 | 93.3 | -- | -- |
| **Open Source Models** | | | | | | | | | | | | |
| T0pp | 8192 | 7.1 | 9.6 | 7.2 | 3.9 | 25.0 | 18.7 | 21.4 | 35.3 | 15.2 | 0.0 | *14.3* |
| Flan-T5 | 8192 | 17.6 | 7.8 | 11.0 | 8.0 | 48.3 | 19.3 | 75.2 | 46.8 | 48.7 | 16.4 | *29.9* |
| Flan-UL2 | 8192 | 16.1 | 11.5 | 13.6 | 5.7 | **56.9** | 25.5 | 75.6 | **51.3** | 36.0 | 14.0 | *30.6* |
| **Closed Models** | | | | | | | | | | | | |
| DaVinci003 | 4096 | 21.7 | 16.1 | 16.9 | 22.0 | 52.7 | 24.6 | 69.0 | 33.5 | 31.3 | 49.5 | *33.7* |
| ChatGPT | 4096 | 21.3 | 16.1 | 15.6 | 20.4 | 49.3 | 25.1 | 66.6 | 27.1 | 49.1 | 49.8 | *34.0* |
| Claude | 8000 | 24.2 | 16.1 | 14.6 | 21.0 | 52.3 | **32.6** | 84.8 | 36.1 | 61.6 | 47.4 | *39.1* |
| GPT-4 | 8192 | **26.3** | **17.3** | **18.5** | **22.6** | 50.7 | 27.6 | **89.2** | 41.1 | **62.8** | **60.5** | ***41.7*** |
| **Fine-tuned Models** | | | | | | | | | | | | |
| CoLT5 | 16384 | 41.0 | 20.0 | 22.5 | -- | 53.1 | 31.0 | 47.0 | -- | -- | -- | -- |

The overall best model is GPT-4 with an average score of 41.7, and its closest competitor is Claude with 39.1, both significantly higher than the other models. [p. 6]

**Summarization** [p. 6] There is a clear trend where the open-source models lag behind product-grade LLMs, and GPT-4 reaches the highest ROUGE scores on all four datasets. However, zero-shot LLMs struggle to compete with models fine-tuned per dataset (CoLT5) on those tasks, with some gap on SummScreenFD and QMSum, and a dramatic difference on GovReport (41.0 compared to 26.3). In SQuALITY, GPT-4 is only one point away from the lower bound on human performance. [p. 6]

**Question Answering** [p. 6] A different trend is seen in question answering. GPT-4 achieves the best result on only one dataset, QuALITY, where it scores 89.2, close to human performance of 93.5. Flan-UL2 sets the high scores for Qasper and MuSiQue, while Claude has the best F1 on NarrativeQA, 5 points more than GPT-4. The authors' analysis reveals that GPT-4 does not conform to the required answer format, resulting in a lower score. [p. 6]

---
[p. 7 continued]

**Aggregation** [p. 7] The new SpaceDigest and BookSumSort datasets enrich ZeroSCROLLS with challenges that explicitly require aggregating information across the sequence. Results indicate that both tasks are difficult for current LLMs. Performance figures for SpaceDigest show that even though sentiment analysis, counting, and divisions are all "easy" tasks for contemporary models, their combination can be quite challenging; only Claude and GPT-4 significantly outperform the naive baseline. The situation is even more dire in BookSumSort, where only GPT-4 outperforms the naive baseline. [p. 7]

## 4.3 Impact of Model Size and Input Length

[p. 7] The authors discuss the effects of increasing model size (parameters) and context length (tokens). As one may expect, both dimensions improve performance on ZeroSCROLLS, suggesting that the benchmark does indeed necessitate complex reasoning over long sequences.

**Model Size** [p. 7] The upper section of Table 4 shows results of Flan-T5 of various sizes, ranging from S (60M parameters) to XXL (11B parameters). As expected, increasing model size drives performance upwards across almost all tasks.

**Input Length** [p. 7] The middle and lower sections of Table 4 show the effect of increasing the maximum number of input tokens for Flan-T5 and Claude. In general, increasing the number of tokens helps the models perform the tasks better. Claude is able to utilize the extra tokens more consistently, which results in an almost 3 point increment to its average score when going from 4k to 8k tokens. Interestingly, Flan-T5 also achieves higher scores on longer inputs in many cases, despite being trained on much shorter sequences. [p. 7]

**Table 4** (p. 7): "Performance of Flan-T5 across model sizes, and Flan-T5 and Claude across input lengths."

| Model | Tokens | GvRp R_geo | SSFD R_geo | QMsm R_geo | SQAL R_geo | Qspr F1 | Nrtv F1 | QALT AC | MuSQ F1 | SpDg ES | BkSS C_idx | Avg |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Flan-T5 Across Model Sizes** | | | | | | | | | | | | |
| Flan-T5-s | 8192 | 7.6 | 4.2 | 8.3 | 3.8 | 18.5 | 11.6 | 34.6 | 21.0 | 0.0 | 0.0 | *11.0* |
| Flan-T5-b | 8192 | 5.4 | 5.1 | 9.7 | 5.6 | 14.2 | 16.5 | 48.4 | 26.9 | 0.0 | 0.3 | *13.2* |
| Flan-T5-l | 8192 | 6.9 | 6.8 | 9.7 | 5.7 | 33.6 | 20.1 | 62.4 | 33.1 | 48.0 | 0.3 | *22.7* |
| Flan-T5-xl | 8192 | 15.2 | 7.2 | 10.2 | 6.6 | 46.6 | **21.6** | 69.6 | 42.8 | 32.8 | 2.2 | *25.5* |
| Flan-T5-xxl | 8192 | **17.6** | **7.8** | **11.0** | **8.0** | **48.3** | 19.3 | **75.2** | **46.8** | **48.7** | **16.4** | ***29.9*** |
| **Flan-T5-xxl Across Input Lengths** | | | | | | | | | | | | |
| Flan-T5-xxl | 512 | 10.0 | 7.9 | 10.4 | 6.1 | 15.3 | 17.6 | 48.2 | 26.0 | 20.8 | 9.0 | *17.1* |
| Flan-T5-xxl | 1024 | 12.1 | 9.4 | 10.1 | 6.3 | 25.5 | 18.9 | 53.2 | 30.3 | 28.7 | 13.4 | *20.8* |
| Flan-T5-xxl | 2048 | 14.0 | **10.0** | 11.0 | 6.8 | 35.7 | 20.9 | 59.8 | 40.6 | 35.0 | 14.7 | *24.9* |
| Flan-T5-xxl | 4096 | 17.3 | 9.1 | **11.8** | 7.4 | 46.5 | **22.2** | 70.8 | **46.8** | 44.1 | 15.1 | *29.1* |
| Flan-T5-xxl | 8192 | **17.6** | 7.8 | 11.0 | **8.0** | **48.3** | 19.3 | **75.2** | **46.8** | **48.7** | **16.4** | ***29.9*** |
| **Claude Across Input Lengths** | | | | | | | | | | | | |
| Claude | 4096 | 23.0 | 15.0 | 14.3 | 20.2 | 47.7 | 31.7 | 76.8 | 35.8 | 61.1 | 37.6 | *36.3* |
| Claude | 8000 | **24.2** | **16.1** | **14.6** | **21.0** | **52.3** | **32.6** | **84.8** | **36.1** | **61.6** | **47.4** | ***39.1*** |

**Figure 4** (p. 7): "Human evaluation (accuracy) over 100 questions from NarrativeQA, Qasper, and MuSiQue, comparing GPT-4 to the highest scoring model of each dataset."

The bar chart shows human-judged accuracy for three QA datasets. For NarrativeQA: Claude 39%, GPT-4 53%. For Qasper: Flan-UL2 69%, GPT-4 80%. For MuSiQue: Flan-UL2 51%, GPT-4 47%. This supports the claim that GPT-4 performs better than Claude and Flan-UL2 on NarrativeQA and Qasper by human evaluation despite lower automatic scores, but on MuSiQue Flan-UL2 edges out GPT-4 even by human judgment. [p. 7]
