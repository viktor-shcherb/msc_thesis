# Appendix B: Analysis of Chunk Number N [p. 13-14]

[p. 13-14] Appendix B analyzes coverage probability of relative positions for context extension `2,048 -> 16,384` as chunk count varies.

**Figure 5** (p. 13): "Coverage probability for each relative position in a single training example (2k -> 16k)."

Description:
- Curves for Original, 2 chunks, 3 chunks, RandPos.
- Original: probability ~1 within <=2,048 and ~0 beyond.
- More chunks: lower coverage in original range but increased coverage in extended range [2,048, 16,383].
- RandPos (2,048 chunks) approaches near-uniform high coverage across distances.

**Figure 6** (p. 14): "Python Code used for calculating coverage probability of each relative position in Figure 5."

Description:
- Three code snippets simulate position-distance coverage for 2-chunk, 3-chunk, and RandPos sampling.
- Monte Carlo estimation loop accumulates visit probabilities over sampled chunk layouts.

**Table 5** (p. 14): "Comparison of different chunk numbers ... Proof-pile perplexity."

| Chunk number | 2k | 4k | 8k | 16k |
|---|---:|---:|---:|---:|
| 1 | 2.83 | >10^3 | >10^3 | >10^3 |
| 2 | 2.95 | 2.74 | 2.61 | 2.60 |
| 3 | 2.93 | 2.72 | 2.60 | 2.59 |
| 2048 (RandPos limit) | 7.26 | 6.83 | 6.76 | 7.73 |

[p. 14] Reported trade-off:
- Increasing chunks improves extension coverage/perplexity beyond original context.
- Extremely large chunk counts harm overall modeling due to large deviation from pre-training positional structure.
