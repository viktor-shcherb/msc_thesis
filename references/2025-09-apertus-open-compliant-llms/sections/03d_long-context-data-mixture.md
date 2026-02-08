# 3.4 Long Context Data Mixture [p. 23–25]

[p. 23] The long-context pretraining relied on a carefully curated mixture of datasets. The mixture was designed to remain close to the data distribution used in the cooldown phase of [p. 25] pretraining, while deliberately increasing the proportion of long documents to improve training efficiency for extended contexts. The mixture comprised the following components:

- **Pretraining Stage 5** (Section 3): Served as the backbone of the mixture, ensuring continuity with the cooldown phase distribution.

- **FineWeb-Long**: Derived from FineWeb-HQ (top 10% highest quality) and its multilingual extension, FineWeb-2-HQ (top 10% highest quality). To focus on long-context capabilities, only documents exceeding 4k tokens are retained, which were further bucketed into length ranges: 4k-8k, 8k-16k, 16k-32k, 32k-64k, and >64k.

- **Institutional Books 1.0:**^32 A corpus of public-domain books, restricted to works published after 1900 to mitigate distribution shift. The texts, digitized via OCR, include quality scores used to filter low-quality scans. Additional heuristics removed non-content artifacts such as page numbers, tables of contents, and boilerplate text. The final cleaned dataset contains 28.7B tokens.

[p. 25] The approximate mixture ratio across all training phases was 70% Stage 5, 20% FineWeb-Long, and 10% Institutional Books. The dominance of Stage 5 data, paired with the modest inclusion of Institutional Books, preserved alignment with the cooldown distribution. To further optimize long-context learning, upsampling to longer documents from FineWeb-HQ and FineWeb-2-HQ was applied. A detailed breakdown, including token counts by phase, is provided in Table 8.

### Table 8: Data Mixture for Long Context Training [p. 25]

> "shown in billions of tokens. Each column represents a distinct training phase with progressively longer context lengths and a specific subset of long documents from the FineWeb-Long dataset. Documents are not repeated across phases."

| Data Source | 8k (4k-8k) | 16k (8k-16k) | 32k (16k-32k) | 64k (32k-64k) |
|---|---|---|---|---|
| Pretraining Stage 5 | 55.80 | 41.31 | 41.62 | 20.74 |
| FineWeb-Long | 15.87 | 11.83 | 12.09 | 5.58 |
| Institutional Books | 6.88 | 5.15 | 5.16 | 2.96 |
| **Total Tokens (B)** | **78.55** | **58.29** | **58.88** | **29.28** |

---

**Footnotes:**
- ^32: huggingface.co/datasets/institutional/institutional-books-1.0
