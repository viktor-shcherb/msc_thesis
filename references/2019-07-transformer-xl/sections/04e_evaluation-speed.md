# 4.5 Evaluation Speed [p. 9]

The evaluation speed of Transformer-XL is compared with the vanilla Transformer model (Al-Rfou et al., 2018). As shown in Table 9, due to the state reuse scheme, Transformer-XL achieves an up to 1,874 times speedup during evaluation. [p. 9]

**Table 9** (p. 9): Slowdown in terms of running time during evaluation. Evaluation is based on per-token time on one GPU.

| Attn Len | How much Al-Rfou et al. (2018) is slower |
|---|---|
| 3,800 | 1,874x |
| 2,800 | 1,409x |
| 1,800 | 773x |
| 800 | 363x |
