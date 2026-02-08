# 2 Pretraining [p. 4]

The pretraining stage involves learning vast amounts of data to acquire a comprehensive understanding of the world and its various complexities, including basic language capabilities and advanced skills such as arithmetic, coding, and logical reasoning.

# 2.1 Data [p. 4-6]

[p. 4-5] The size of data is a crucial factor in developing a robust LLM, as highlighted by Hoffmann et al. (2022) and Touvron et al. (2023b). The dataset is designed to be diverse and cover a wide range of types, domains, and tasks, including public web documents, encyclopedia, books, codes, etc. The dataset is multilingual, with a significant portion in English and Chinese.

## Data preprocessing

[p. 5] A comprehensive data preprocessing procedure was developed:

- **Web data extraction:** Extract text from HTML and use language identification tools to determine the language.
- **Deduplication:** Exact-match deduplication after normalization and fuzzy deduplication using MinHash and LSH algorithms to increase diversity.
- **Quality filtering:** A combination of rule-based and machine-learning-based methods. Multiple models are used to score content, including language models, text-quality scoring models, and models for identifying potentially offensive or inappropriate content. Manual sampling and review from various sources is also performed.
- **Up-sampling:** Selectively up-sample data from certain sources to ensure models are trained on a diverse range of high-quality content.
- **Multi-task instruction data:** Following recent studies (Zeng et al., 2022; Aribandi et al., 2021; Raffel et al., 2020), high-quality instruction data is incorporated into the pretraining process to enhance zero-shot and few-shot performance.
- **Benchmark decontamination:** Following a similar approach as Brown et al. (2020), any instruction samples exhibiting a 13-gram overlap with test set data are meticulously eliminated. Given the large number of downstream tasks, this filtering is not feasible for all tasks; instead, instruction data for reported tasks has undergone a filtering process for accuracy and reliability.

[p. 6] The final dataset contains up to 3 trillion tokens.

**Figure 2** (p. 5): "Performance of GPT-4, GPT-3.5, the previous 13B SOTA, as well as QWEN-14B." A radar chart showing results on 12 datasets covering multiple domains including language understanding, knowledge, reasoning, etc. The 12 axes are: MMLU, C-Eval, AGIEval, Gaokao-Bench, GSM8K, MATH, HumanEval, MBPP, CSQA, HellaSwag, PIQA, BBH. Four models are plotted: GPT-4 (dashed green, outermost), GPT-3.5 (dashed blue), Previous 13B SOTA (green with circles), and Qwen-14B (red with circles). QWEN significantly outperforms the previous SOTA of similar model sizes, but still lags behind both GPT-3.5 and GPT-4. Approximate values read from the chart:

| Benchmark | GPT-4 | GPT-3.5 | Prev 13B SOTA | Qwen-14B |
|---|---|---|---|---|
| MMLU | ~77.5 | ~63.0 | ~50.0 | ~53.0 |
| C-Eval | ~75.0 | ~52.5 | ~32.5 | ~50.0 |
| AGIEval | ~53.75 | ~42.5 | ~25.0 | ~31.25 |
| Gaokao-Bench | ~68.75 | ~52.5 | ~36.25 | ~46.25 |
| GSM8K | ~88.75 | ~67.5 | ~30.0 | ~46.25 |
| MATH | ~45.0 | ~26.25 | ~15.0 | ~20.0 |
| HumanEval | ~78.75 | ~52.5 | ~40.0 | ~46.25 |
| MBPP | ~88.75 | ~67.5 | ~60.0 | ~52.5 |
| CSQA | ~87.5 | ~65.0 | ~42.5 | ~42.5 |
| HellaSwag | ~87.5 | ~85.0 | ~65.0 | ~63.0 |
| PIQA | [unclear: value near outer ring, partially obscured] | [unclear: partially obscured] | ~35.0 | ~60.0 |
| BBH | ~85.0 | ~67.5 | ~42.5 | ~46.25 |

Note: These values are approximate readings from a radar chart and may not be exact.
