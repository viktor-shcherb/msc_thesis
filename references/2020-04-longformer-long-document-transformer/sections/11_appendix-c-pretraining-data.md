# C Pretraining Data [p. 14-15]

[p. 14] In order to allow the model to learn long dependencies in pretraining, a corpus of long documents was compiled. Some of these data sources were also included in the original RoBERTa pretraining including the Books corpus (Zhu et al., 2015) plus English Wikipedia. Additionally included:
- One third of a subset of the Realnews dataset (Zellers et al., 2019) with documents longer than 1,200 tokens
- One third of the Stories (Trinh and Le, 2018) corpus

The goal was to include a mix of long and short documents to both allow the model to learn longer dependencies while not forgetting information from the original RoBERTa pretraining.

## Table 13: Pretraining data [p. 15]

| Source | Tokens | Avg doc len |
|---|---|---|
| Books (Zhu et al., 2015) | 0.5B | 95.9K |
| English Wikipedia | 2.1B | 506 |
| Realnews (Zellers et al., 2019) | 1.8B | 1.7K |
| Stories (Trinh and Le, 2018) | 2.1B | 7.8K |
