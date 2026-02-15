# Effects of loss function $\mathcal{L}$ on attention sink [p. 7]

[p. 7]

## Weight decay [p. 7]

The loss function becomes $\mathcal{L} = \sum_{t=2}^{T} \log p_\theta(x_t|x_{<t}) + \gamma \|\theta\|_2^2$ when introducing weight decay ratio $\gamma$. As indicated in Table 2($\gamma = 0$) in the loss function, attention sink still emerges in LMs. Then a larger $\gamma$ encourages more heads to have attention sink. But further increasing weight decay hurts the optimization, leading to less obvious or even no attention sink [p. 7].

## Prefix language modeling [p. 7]

Since the first token is not predicted in the auto-regressive loss function, it could be considered as the prefix token. Then the original auto-regressive loss can be generalized into the formula $\mathcal{L} = \sum_{t=p+1}^{C} \log p_\theta(x_t|x_{p+1:t-1}, x_{1:p})$, with the prefix length $p = 1$. Motivated by Wang et al. (2022), we consider $p > 1$ and the causal mask visualized in Figure 5(*Left*). Although this design does not affect the emergence of attention sink, it shifts the sink position. In Figure 5(*Middle*), the attention sink only appears on one prefix token among these prefix tokens instead of on the first token only. Massive activations also appear on the corresponding sink token [p. 7].

## Shifted window attention [p. 7]

Motivated by the shifted window attention adopted in Mistral-7B, we further explore the effects of window size on attention sink. With shifted window attention, the loss function becomes $\mathcal{L} = \sum_{t=2}^{T} \log p_\theta(x_t|x_{t-w:t-1})$, where $w$ refers to the window size. As shown in Figure 6(*Left*) and (*Middle*), with shifted window attention, we find that if $t \leq w$, the $t$-th token can still "look at" the first token, and LMs still have attention sink on the first token. When $t > w$, the $t$-th token can only attend up to the $t - w + 1$-th token. Although this token becomes the "first token" for the $t$-th token, typically it has no attention sink. We have similar observations in Mistral-7B. Additionally, from Figure 6(*Right*), smaller window size prevents the emergence of attention sink [p. 7].

**Figure 6** (p. 7): "(*Left*) Shifted window attention pattern. (*Middle*) In LMs with window attention, attention sink appears on the first token, but not on the "first token" within each window. (*Right*) Attention sink tends to emerge when the window size is large enough"

Description: Three panels illustrating shifted window attention effects
- Left: Visualization of shifted window attention pattern with window size $w = 256$, showing causal mask with diagonal band structure. Annotations show "Sink" region (first token accessible to early positions) and "No Sink" region (where positions can only see recent $w$ tokens)
- Middle: Heatmap of attention weights (0.0 to 1.0 color scale) under shifted window attention
- Right: Dual-axis line plot showing train loss, valid loss (left axis), and sink percentage (right axis) vs. window size (64, 128, 256, 512, 1024). Shows attention sink emerges when window size ≥ 256
- Supports claim: Window size affects attention sink emergence; sink appears on absolute first token, not relative "first token" within windows

**Takeaways** (from box on p. 7, bottom):
1. Weight decay encourages the emergence of attention sink
2. With prefix language modeling, attention sink appears among the prefix tokens rather than the first token only
3. With shifted window attention, attention sink appears on the "absolute" first token, not the "relative" first token. Smaller window size prevents the emergence of attention sink
