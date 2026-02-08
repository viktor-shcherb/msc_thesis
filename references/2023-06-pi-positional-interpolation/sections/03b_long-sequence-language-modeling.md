# 3.2 Long Sequence Language Modeling [p. 6–8]

[p. 6] The authors evaluate the long sequence language modeling performance of their extended models and baselines on two datasets:
- **Book corpus (PG-19)** (Rae et al., 2020)
- **Cleaned Arxiv Math proof-pile dataset** (Azerbayev et al., 2022)

## Evaluation Setup

- **PG-19:** whole test split consisting of 100 documents
- **Proof-pile:** a random subsample of 128 documents with at least 32768 SentencePiece (Kudo & Richardson, 2018) tokens, truncated to the first 32768 tokens for each test document
- **Metric:** perplexity at various context window sizes using a sliding window approach following Press et al. (2022) with stride $S = 256$

## Table 1: Evaluation perplexity on PG19 dataset (Rae et al., 2020) [p. 7]

FT: Direct Fine-tuning. PI: Position Interpolation.

| Size | Context Window | Method | 2048 | 4096 | 8192 | 16384 | 32768 |
|------|---------------|--------|------|------|------|-------|-------|
| 7B | 2048 | None | 7.20 | >10^3 | >10^3 | >10^3 | >10^3 |
| 7B | 8192 | FT | 7.21 | 7.34 | 7.69 | - | - |
| 7B | 8192 | PI | 7.13 | 6.96 | 6.95 | - | - |
| 7B | 16384 | PI | 7.11 | 6.93 | 6.82 | 6.83 | - |
| 7B | 32768 | PI | 7.23 | 7.04 | 6.91 | 6.80 | 6.77 |
| 13B | 2048 | None | 6.59 | - | - | - | - |
| 13B | 8192 | FT | 6.56 | 6.57 | 6.69 | - | - |
| 13B | 8192 | PI | 6.55 | 6.42 | 6.42 | - | - |
| 13B | 16384 | PI | 6.56 | 6.42 | 6.31 | 6.32 | - |
| 13B | 32768 | PI | 6.54 | 6.40 | 6.28 | 6.18 | 6.09 |
| 33B | 2048 | None | 5.82 | - | - | - | - |
| 33B | 8192 | FT | 5.88 | 5.99 | 6.21 | - | - |
| 33B | 8192 | PI | 5.82 | 5.69 | 5.71 | - | - |
| 33B | 16384 | PI | 5.87 | 5.74 | 5.67 | 5.68 | - |
| 65B | 2048 | None | 5.49 | - | - | - | - |
| 65B | 8192 | PI | 5.42 | 5.32 | 5.37 | - | - |

> "Model fine-tuned with PI shows progressively lower perplexity with longer context window, showing that PI can leverage long context well, while the perplexity of FT increases over longer window." [p. 7]

Note that overall the perplexity is higher compared to Table 2 since PG19 has very different writing styles. [p. 7]

## Table 2: Evaluation perplexity on Arxiv Math Proof-pile dataset (Azerbayev et al., 2022) [p. 8]

FT: Direct Fine-tuning. PI: Position Interpolation.

| Size | Context Window | Method | 2048 | 4096 | 8192 | 16384 | 32768 |
|------|---------------|--------|------|------|------|-------|-------|
| 7B | 2048 | None | 2.77 | - | - | - | - |
| 7B | 8192 | FT | 2.85 | 2.74 | 2.73 | - | - |
| 7B | 8192 | PI | 2.79 | 2.57 | 2.39 | - | - |
| 7B | 16384 | PI | 2.79 | 2.57 | 2.37 | 2.25 | - |
| 7B | 32768 | PI | 2.82 | 2.59 | 2.39 | 2.24 | 2.48 |
| 13B | 2048 | None | 2.66 | - | - | - | - |
| 13B | 8192 | FT | 2.71 | 2.56 | 2.50 | - | - |
| 13B | 8192 | PI | 2.67 | 2.47 | 2.30 | - | - |
| 13B | 16384 | PI | 2.68 | 2.47 | 2.29 | 2.18 | - |
| 13B | 32768 | PI | 2.68 | 2.46 | 2.28 | 2.15 | 2.35 |
| 33B | 2048 | None | 2.49 | - | - | - | - |
| 33B | 8192 | FT | 2.56 | 2.48 | 2.47 | - | - |
| 33B | 8192 | PI | 2.50 | 2.32 | 2.18 | - | - |
| 33B | 16384 | PI | 2.53 | 2.34 | 2.18 | 2.07 | - |
| 65B | 2048 | None | 2.42 | - | - | - | - |
| 65B | 8192 | PI | 2.43 | 2.26 | 2.12 | - | - |

## Results Summary

[p. 6] Models extended with Position Interpolation enjoy a significantly improved perplexity from longer context window sizes. Key perplexity reductions when increasing context window size from 2048 to 16384:
- LLaMA 7B: -0.28 and -0.5 reductions of perplexity on both datasets
- LLaMA 13B: -0.27 and -0.48 reductions
- LLaMA 33B: -0.14 and -0.42 reductions
- LLaMA 65B: -0.12 and -0.3 reductions by extending to the 8192 context window size

A consistent trend of models achieving better perplexity with longer context windows is observed. This trend extends to 32768 window size without diminishing on the PG-19 dataset for LLaMA 7B and 13B models. This indicates that their method may enable extension to even longer context windows. [p. 6]

In contrast, models extended via the direct fine-tuning method have shown regression (up to +0.48) or minor improvement (up to -0.12) on the perplexity at longer context windows. This indicates that models extended this way have limited capability of making use of context windows longer than their pre-trained settings. [p. 6]

A minor degradation of the perplexity on the original context window of 2048 is seen for extended models in some cases. For example, on the Proof-pile dataset, a degradation ranging from 0.01 to 0.05 across all models extended with Position Interpolation. A small degradation of performance within original evaluation context window is expected since Position Interpolation forces position encodings in original context window to reside in a much narrower region, which may negatively affect the language model's performance. More benchmark results on the original context window size are presented in Section 3.4. [p. 6–7]

## Perplexity vs. Fine-tuning Steps

[p. 7] Table 3 reports the relationship between perplexity and the number of fine-tuning steps for LLaMA 7B model extending to 8192 and 16384 context window sizes using Position Interpolation, evaluated on the PG19 dataset.

### Table 3: Evaluation perplexity on PG19 dataset (Rae et al., 2020) with respect to the number of fine-tuning steps using Position Interpolation [p. 8]

| Size | Context Window | 0 | 200 | 400 | 600 | 800 | 1000 |
|------|---------------|-------|------|------|------|------|------|
| 7B | 8192 | 16.10 | 7.12 | 7.10 | 7.02 | 6.99 | 6.95 |
| 7B | 16384 | 112.13 | 7.05 | 6.93 | 6.88 | 6.84 | 6.83 |

Key observations [p. 7]:
- At step 0 (without fine-tuning), the model can exhibit certain language modeling capability, as indicated by < 20 perplexity for extending to 8192 context window (in contrast, the direct extrapolation method leads to > 10^3 perplexity).
- With fine-tuning, the perplexity improves quickly.
- At 200 steps the models surpassed the original model's perplexity on 2048 context window size, indicating the models gaining ability of effectively using sequences longer than the pre-training settings for language modeling.
- At 1000 steps, the models have improved steadily and achieve a significantly better perplexity.
