# I Using More Sink Tokens in the Pre-Training Stage [p. 21]

[p. 21]

Section 3.3 illustrated that incorporating a single dedicated sink token in the pre-training stage does not affect model performance but enhances streaming performance by centralizing attention sinks to one token. This section delves into whether adding additional sink tokens during pre-training could further optimize the performance of pre-trained language models. [p. 21]

As depicted in Figure 15, incorporating either one or two sink tokens during pre-training results in pre-training loss curves that closely resemble those of the baseline (vanilla) model. However, as detailed in Table 9, the introduction of a second sink token does not yield substantial improvements in performance across most benchmark tasks. [p. 21]

Further analysis, as shown in Table 10, reveals that the inclusion of additional sink tokens does not enhance streaming performance. Interestingly, the model appears to rely on both sink tokens to maintain stable streaming performance. These findings suggest that while a single sink token is adequate for improving streaming performance, adding more sink tokens does not lead to further enhancements in overall language model performance. This contrasts with findings in Vision Transformers (ViTs) (Darcet et al., 2023), where multiple "registers" have been found to be beneficial. [p. 21]

**Figure 15** (p. 21): "Pre-training loss curves of models with 0, 1, and 2 sink tokens."

The figure shows a line plot with X-axis: k Steps (0 to ~140), Y-axis: Training Loss (~2.5 to ~2.8). Three curves are plotted:
- Vanilla (green): baseline model with no sink tokens
- + Sink Token (red): model with 1 sink token
- + 2 Sink Tokens (orange): model with 2 sink tokens
All three curves follow similar trajectories, starting around 2.75-2.8 and decreasing to approximately 2.5 by 140k steps. The curves are nearly overlapping, indicating that adding sink tokens does not meaningfully change the pre-training loss dynamics.

**Table 9** (p. 21): "Zero-shot accuracy (in %) across 7 NLP benchmarks, including ARC-[Challenge, Easy], HellaSwag, LAMBADA, OpenbookQA, PIQA, and Winogrande."

| Methods | ARC-c | ARC-e | HS | LBD | OBQA | PIQA | WG |
|---|---|---|---|---|---|---|---|
| Vanilla | 18.6 | 45.2 | 29.4 | 39.6 | 16.0 | 62.2 | 50.1 |
| + 1 Sink Token | **19.6** | **45.6** | **29.8** | **39.9** | **16.6** | 62.6 | **50.8** |
| + 2 Sink Tokens | 18.7 | 45.6 | 29.6 | 37.5 | 15.8 | **64.3** | 50.4 |

Bold values indicate the best result per column. The + 1 Sink Token model achieves the best or tied-best performance on most benchmarks (ARC-c, ARC-e, HS, LBD, OBQA, WG), while + 2 Sink Tokens only leads on PIQA. Overall, a second sink token provides no consistent improvement.

**Table 10** (p. 21): "Comparison of vanilla attention with prepending a zero token and a learnable sink token during pre-training. Cache config x+y denotes adding x initial tokens with y recent tokens. Perplexity is evaluated on the first sample in the PG19 test set."

| | Cache Config | | | |
|---|---|---|---|---|
| | 0+1024 | 1+1023 | 2+1022 | 4+1020 |
| Vanilla | 27.87 | 18.49 | 18.05 | 18.05 |
| + 1 Sink Token | 1235 | **18.01** | 18.01 | 18.02 |
| + 2 Sink Tokens | 1262 | 25.73 | 18.05 | 18.05 |

For the Vanilla model, removing all initial tokens (0+1024) yields perplexity 27.87, while including even 1 initial token (1+1023) drops it to 18.49, and including 2+ (2+1022 and 4+1020) brings it to 18.05. For + 1 Sink Token, the 0+1024 configuration yields extremely high perplexity (1235) because the sink token is excluded, but 1+1023 achieves the best perplexity of 18.01. For + 2 Sink Tokens, 0+1024 also yields very high perplexity (1262), and 1+1023 (including only one of the two sink tokens) yields 25.73, but including both (2+1022) restores perplexity to 18.05. This demonstrates that the model learns to rely on all its sink tokens, and excluding any of them degrades streaming performance.
