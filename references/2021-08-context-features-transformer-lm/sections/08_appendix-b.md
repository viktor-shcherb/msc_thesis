# B Longer Context Window [p. 11-12]

[p. 11-12] Here the authors report the results of repeating the experiments of Sections 3.1 and 3.2 with ablated contexts of size 1024 tokens instead of 512 tokens in order to verify that the behavior observed is not specific to the size of context window chosen.

**Figure 6** (p. 12): "Effect of **word order** on usable information. Bar labels show 'change in ablated likelihood (ablated information)'. The x axis shows ablated likelihood. Error bars represent 95% confidence intervals. Ablated contexts contain 1024 tokens, but results are consistent with results on 512-token contexts."

Figure 6 has two sub-figures:

**(a) Mid-range condition (first 256 tokens after ablation):**
| Ablation | Ablated likelihood (bits) | Change (ablated information) |
|---|---|---|
| full information | 4.16 (0%) | -- |
| sent. shuf. | ~4.17 | +0.06 (21%) |
| shuf. within sent. | ~4.18 | +0.08 (29%) |
| shuffle all | ~4.20 | +0.14 (49%) |
| replace w/ old | ~4.22 | +0.21 (73%) |
| no information | 4.45 (100%) | -- |

**(b) Long-range condition (tokens 256-512 after ablation):**
| Ablation | Ablated likelihood (bits) | Change (ablated information) |
|---|---|---|
| full information | 4.16 (0%) | -- |
| sent. shuf. | ~4.16 | +0.01 (24%) |
| shuf. within sent. | ~4.17 | +0.04 (65%) |
| shuffle all | ~4.17 | +0.06 (88%) |
| no information | 4.22 (100%) | -- |
| replace w/ old | ~4.17 | +0.06 (100%) |

**Figure 7** (p. 12): "Effect of **word identity** on usable information. Labels are as in Fig. 6. Ablated contexts contain 1024 tokens, but results are consistent with results on 512-token contexts."

Figure 7 has two sub-figures:

**(a) Mid-range condition (first 256 tokens after ablation):**
| Ablation | Ablated likelihood (bits) | Change (ablated information) |
|---|---|---|
| N&VB&ADJ | ~4.16 | +0.00 (-4%) |
| full information | 4.16 (0%) | -- |
| N&VB | ~4.17 | +0.05 (17%) |
| N | ~4.18 | +0.07 (23%) |
| named entities | ~4.20 | +0.12 (41%) |
| func. words | ~4.22 | +0.22 (76%) |
| no information | 4.45 (100%) | -- |

**(b) Long-range condition (tokens 256-512 after ablation):**
| Ablation | Ablated likelihood (bits) | Change (ablated information) |
|---|---|---|
| N&VB&ADJ | ~4.16 | +0.00 (-4%) |
| full information | 4.16 (0%) | -- |
| N&VB | ~4.16 | +0.00 (2%) |
| N | ~4.16 | +0.01 (15%) |
| named entities | ~4.18 | +0.03 (48%) |
| no information | 4.22 (100%) | -- |
| func. words | ~4.23 | +0.07 (114%) |

Note: In the long-range condition of Figure 7, N&VB&ADJ again shows a slight improvement over full information (negative ablated information), consistent with the 512-token results in Section 3.2. The func. words ablation exceeds 100% in the long-range condition, indicating performance worse than the no information baseline.
