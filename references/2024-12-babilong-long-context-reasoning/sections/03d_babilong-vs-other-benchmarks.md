# 3.4 BABILong and Other Benchmarks [p. 7-8]

## Introduction to benchmark comparison [p. 7]

Here, we analyze how models performance on BABILong benchmark differs from MMLU (Hendrycks et al., 2020) and RULER (Hsieh et al., 2024). The MMLU benchmark measures various branches of knowledge in LLMs, whereas RULER, a recently proposed long-context benchmark, shares a similar "needle-in-a-haystack" concept with BABILong. One notable difference is that RULER's "needles" (such as adjectives, nouns, numbers, uuids) and long "haystack" contexts are more synthetic, consisting of randomly repeated sentences, except for tasks based on the SQuAD (Rajpurkar et al., 2016) and HotPotQA (Yang et al., 2018) datasets or using Paul Graham essays. [p. 7-8]

**Figure 4** (p. 8): "BABILong is similar to MMLU (Hendrycks et al., 2020) on short lengths and captures differences in models behavior for longer contexts. MMLU is a relatively short benchmark, with samples up to 1k tokens in length. BABILong has a higher correlation with MMLU on short contexts (0K) than RULER (Hsieh et al., 2024). However, RULER maintains a high correlation regardless of task length, with an even higher correlation at 64K, while BABILong's correlation with MMLU decreases as the length increases. This may indicate that BABILong is better at capturing differences in models behavior at different context lengths."

Description: Multi-panel scatter plot figure comparing model performance across benchmarks:
- Top-left panel: Shows correlation between BABILong Tasks 1-5 and RULER across different task lengths (0 to 120 thousand tokens). Line plot shows decreasing correlation from ~0.95 at short lengths to ~0.4 at 120k tokens.
- Top-right panels: Two scatter plots showing RT² correlations (0.950 and 0.928) between metrics at different lengths, with data points for various models labeled.
- Bottom panels: Six scatter plots comparing different benchmark pairs (BABILong QA2 0K, QA1-5 0K, QA1-5 <= 128K) against MMLU and RULER at various lengths (0K, 64K, 6K, 8K). Each plot shows correlation coefficients (RT²) ranging from 0.390 to 0.910, with models plotted as points and diagonal trend lines.

Key findings from scatter plots:
- BABILong 0K shows high correlation with MMLU (RT² = 0.88 for QA2, 0.700 for QA1-5)
- Correlation between BABILong and RULER varies by length: 0.928 at 64K, lower at other lengths
- Models cluster differently depending on context length
- Short context performance (0K) is more correlated with MMLU than long context performance

Supports claim: BABILong captures differences in model behavior starting from lengths as small as 2K tokens, while RULER requires lengths of at least 128K tokens to show significant differentiation from relatively short MMLU benchmark [p. 8].

## Correlation analysis [p. 8]

We collect results from multiple models on MMLU, BABILong, and RULER at lengths ranging from 0K (BABILong without texts from PG19) to 128K tokens. In the upper-left part of Figure 4, we show the correlation between scores on BABILong and RULER for different task lengths with adding the MMLU benchmark. At shorter lengths, BABILong exhibits a high correlation with MMLU, which diminishes as the length increases. Conversely, RULER shows a nearly constant correlation with MMLU, regardless of the length. The best correlated RULER lengths with MMLU are 64K and the average of all lengths (<=128K). Compared to RULER, the highest correlation of BABILong scores with MMLU is in length 0K, which is expected since MMLU is a relatively short benchmark with examples up to 1K tokens. Comparing the most correlated BABILong lengths (<=0K) and RULER lengths (<=128K and 64K) shows much lower values: 0.928 vs. 0.435 and 0.910 vs. 0.455, respectively. [p. 8]

## BABILong sensitivity to context length [p. 8]

These results show that BABILong can detect differences in models behavior starting from lengths as small as 2K tokens, while RULER requires lengths of at least 128K tokens to show significant differentiation from relatively short MMLU benchmark. [p. 8]
