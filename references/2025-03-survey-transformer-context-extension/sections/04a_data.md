# 4.1 Data [p. 6]

In order to explore what data should be used to test model's ability to process long context, we conduct a statistical analysis of datasets in existing benchmarks and summarize their data characteristics [p. 6].

The evaluation of a model's long context capability requires not only the long data but also its data diversity and quality. As shown in Table 1, we focus on three characteristics of the datasets in existing long context benchmarks:
1. Length level
2. Total number of examples
3. The domain it covers [p. 6]

## Benchmark Statistics

Table 1 shows statistics on data characteristics of datasets in existing long context benchmarks [p. 6].

| Benchmark | Length Level | #Examples | Domain |
|-----------|--------------|-----------|---------|
| SCROLLS (Shaham et al., 2022) | 1k~4k | 119,495 | Literature, Dialog |
| ZeroSCROLLS (Shaham et al., 2023) | 0k~16k | 4,378 | Wiki, Literature, Dialog |
| LongBench (Bai et al., 2023) | 0k~4k, 4k~8k, >8k | 4,750 | Wiki, Literature, Dialog, Report, Code, News |
| LooGLE (Li et al., 2023a) | 0k~24k | 776 | Wiki, Paper |
| BAMBOO (Dong et al., 2023a) | 0k~4k, 4k~16k | 1,502 | Wiki, Dialog, Report, Code, Paper |
| LongICLBench (Li et al., 2024c) | 2k~50k | 3,000 | Dialog, News, Common Sense |
| L-Eval (An et al., 2023) | 3k~200k | 411 | Literature, Dialog, News, Paper, Common Sense |
| Ada-LEval (Wang et al., 2024a) | 1k~128k | 117,500 | Literature, Code |
| ∞Bench (Zhang et al., 2024) | 0k~200k | 3,946 | Literature, Dialog, Code |
| NeedleBench (Li et al., 2024b) | 1k~4k/8k/12k/128k/200k/1m+ | - | Wiki, Literature, Dialog, Report, Code, News |
| LV-Eval (Yuan et al., 2024) | 0k~16k/32k/64k/128k/256k | 1,729 | Wiki, Literature, Dialog, Report, Code, News, Paper |

**Note on Table 1:** Length level represents the range of token lengths in the dataset used in the benchmark. #Examples refers to the total number of examples. Domain denotes the data sources. The corresponding contents are directly extracted or calculated from the original papers [p. 6].

## Data Categorization by Length

Given that current models mainly within context windows exceeding 100k tokens, we categorize benchmarks based on this threshold. Benchmarks with contexts exceeding 100K tokens are listed in the lower part [p. 6].

## Knowledge Leakage Issue

Besides, we also discuss about knowledge leakage issue, which need to be addressed when constructing the dataset, in the Appendix B.1.2 [p. 6].
