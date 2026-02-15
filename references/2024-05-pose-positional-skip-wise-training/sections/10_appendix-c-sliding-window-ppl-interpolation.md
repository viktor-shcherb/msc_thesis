# Appendix C: Sliding Window PPL from Linear / NTK / YaRN Interpolation [p. 14-15]

[p. 14-15] Appendix C expands Table 1 into full interpolation comparison for four settings per interpolation family: Original, PI-only, Full-length, PoSE.

**Table 6** (p. 15): "Perplexity of models trained with different methods using Linear / NTK / YaRN interpolation."

| Method | Train/Target | Gov 2k | Gov 4k | Gov 8k | Gov 16k | Proof 2k | Proof 4k | Proof 8k | Proof 16k |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Original | -/- | 4.74 | >10^3 | >10^3 | >10^3 | 2.83 | >10^3 | >10^3 | >10^3 |
| PI-only (Linear) | -/16k | 43.80 | 43.35 | 45.89 | 54.33 | 25.32 | 24.20 | 24.88 | 29.59 |
| Full-length (Linear) | 16k/16k | 4.87 | 4.70 | 4.61 | 4.59 | 2.93 | 2.71 | 2.58 | 2.53 |
| PoSE (Linear) | 2k/16k | 4.84 | 4.68 | 4.60 | 4.60 | 2.95 | 2.74 | 2.61 | 2.60 |
| PI-only (NTK) | -/16k | 5.62 | 5.61 | 5.80 | 550 | 3.27 | 3.15 | 3.19 | 517 |
| Full-length (NTK) | 16k/16k | 4.78 | 4.63 | 4.57 | 7.24 | 2.93 | 2.71 | 2.61 | 5.66 |
| PoSE (NTK) | 2k/16k | 4.79 | 4.63 | 4.57 | 7.24 | 2.92 | 2.71 | 2.60 | 4.37 |
| PI-only (YaRN) | -/16k | 5.57 | 5.51 | 5.57 | 5.83 | 3.17 | 2.97 | 2.87 | 2.89 |
| Full-length (YaRN) | 16k/16k | 4.78 | 4.62 | 4.54 | 4.53 | 2.90 | 2.68 | 2.56 | 2.52 |
| PoSE (YaRN) | 2k/16k | 4.79 | 4.63 | 4.55 | 4.55 | 2.91 | 2.69 | 2.57 | 2.53 |

[p. 14-15] Text summary: across interpolation families, trend is `Full-length ~= PoSE > PI-only >> Original`; NTK shows an instability spike near 16k, while YaRN alleviates this.
