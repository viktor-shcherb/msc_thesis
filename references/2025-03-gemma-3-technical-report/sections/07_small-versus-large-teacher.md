# 5.4. Small versus large teacher [p. 7–8]

A common finding is that, to train a small model, it is preferable to distill from a smaller teacher.

**Figure 8** (p. 8): "Small versus large teacher. Relative difference of perplexity when using a small and large teacher as a function of the token size of training. Smaller number means training from a larger teacher is better."

Description: Line plot
- X-axis: Total training tokens (B) on log scale (10^1 to 10^2)
- Y-axis: Δ Perplexity (ranging from -0.006 to 0.002)
- Single declining curve (red)
- Notable pattern: For short training horizons (lower token counts), smaller teacher is better (positive Δ); for longer training (higher token counts), larger teacher is better (negative Δ)
- Crossover point appears around 30-40B tokens
- Supports claim: The optimal teacher size depends on training duration

We suspect this is because these studies are often performed in settings where the regularization effect of using a worse teacher outperforms the benefits of using a better teacher. We train a student with 2 teachers of different sizes, one large and one small, for different training horizons. In Fig. 8, we observe that for short training horizons, the smaller teacher is better, but the trend is reversed for longer training.
