# F Small Init Embedding [p. 18]

[p. 18]

This section presents the experimental validation of small initialization embedding. The experimental setup is as follows:

- **Baseline configuration:** Parameters are initialized using a normal distribution with a mean of 0.0 and a standard deviation of 0.02, which is a commonly used initialization method in models like BERT and GPT.
- **Small init emb configuration:** Parameters are initialized using a uniform distribution with a range of 1e-4, which is slightly different from RWKV where a normal distribution with a standard deviation of 1e-4 is used. The authors note this difference is negligible and does not affect the conclusions.
- **Batch size:** 400

**Figure 9** (p. 18): "Effect of small initialization embedding."
- The figure shows two training loss curves plotted against training steps (x-axis: 0 to 50,000 steps; y-axis: Loss from ~4 to ~11). The blue curve (Baseline) and orange curve (Small Init Emb) both start around loss 11. The small init emb curve exhibits a faster rate of decrease and convergence compared to the traditional initialization using a normal distribution. Both curves converge to approximately the same final loss near 4.5, but the small init emb curve reaches lower loss values earlier in training.
