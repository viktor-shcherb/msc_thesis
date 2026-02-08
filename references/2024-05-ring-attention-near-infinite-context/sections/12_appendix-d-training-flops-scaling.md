# D Training FLOPs Scaling of Context Size [p. 16]

[p. 16] Given that the proposed approach unlocks the possibility of training with a context size exceeding 100 million tokens and allows for linear scaling of the context size based on the number of devices, it is essential to understand how the training FLOPs per dataset scale with the context size. While a larger context size results in a higher number of FLOPs, the increased ratio does not scale quadratically because the number of tokens remains fixed. The results are presented in Figure 5, which showcases various model sizes and context lengths, representing different computational budgets. The figure shows the ratio of FLOPs for larger context lengths compared to the same model with a shorter 4K context size.

The per sequence FLOPs are calculated using $(24bsh^2 + 4bs^2h)n$ where $h$ is model hidden dimension, $b$ is batch size, $s$ is total sequence length, and $n$ is number of layers. The per dataset FLOPs ratio is then given by:

$$\frac{(24bs_2h^2 + 4bs_2^2h)}{(24bs_1h^2 + 4bs_1^2h)} / \frac{s_2}{s_1} = \frac{(6h + s_2)}{(6h + s_1)}$$

where $s_2$ and $s_1$ are new and old context lengths.

Model sizes and their hidden dimensions are as follows:
- LLaMA-7B (4096)
- LLaMA-13B (5140)
- LLaMA-33B (7168)
- LLaMA-65B (8192)
- GPT3-175B (12288)
- 1TB (36864)

These model configurations are from LLaMA [36] and GPT-3 [3] papers, except the 1TB model size and dimension were defined by the authors.

**Figure 5** (p. 16): "The per dataset training FLOPs cost ratio relative to a 4k context size, considering different model dimensions. On the x-axis, you'll find the context length, where, for example, 32x(128k) denotes a context length of 128k, 32x the size of the same model's 4k context length."

The figure is a heatmap with Model Size on the y-axis (7B, 13B, 33B, 65B, 175B, 1TB) and Context Length on the x-axis (2x/8K, 4x/16K, 8x/32K, 16x/64K, 32x/128K, 64x/256K, 256x/1M, 3072x/10M, 32768x/100M). A color bar on the right indicates the FLOPs ratio (log scale, 1 to 5000). Values in each cell:

| Model Size | 2x (8K) | 4x (16K) | 8x (32K) | 16x (64K) | 32x (128K) | 64x (256K) | 256x (1M) | 3072x (10M) | 32768x (100M) |
|---|---|---|---|---|---|---|---|---|---|
| 1TB | 1.0 | 1.1 | 1.1 | 1.3 | 1.6 | 2.1 | 5.6 | 56.8 | 596.8 |
| 175B | 1.1 | 1.2 | 1.4 | 1.8 | 2.6 | 4.3 | 14.4 | 162.6 | 1725.6 |
| 65B | 1.1 | 1.2 | 1.5 | 2.2 | 3.4 | 5.8 | 20.6 | 237.2 | 2521.5 |
| 33B | 1.1 | 1.3 | 1.6 | 2.3 | 3.7 | 6.5 | 23.2 | 268.0 | 2850.3 |
| 13B | 1.1 | 1.4 | 1.8 | 2.8 | 4.6 | 8.4 | 31.0 | 362.3 | 3855.9 |
| 7B | 1.1 | 1.4 | 2.0 | 3.1 | 5.4 | 10.0 | 37.4 | 439.7 | 4682.0 |

As depicted in Figure 5, scaling up small models to a 1M context size results in approximately 20-40 times more FLOPs, and even more for 10M and 100M token context sizes. However, as the model sizes increase, the cost ratio decreases. For instance, scaling up the 170B model from 4K to 10M incurs 162.6x higher per dataset FLOPs, despite the context size being 3072 times longer.
