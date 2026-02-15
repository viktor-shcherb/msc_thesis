# r_q vs r_k Scatter for Combined QK PCA PC0

## File
`figure.png`

## What This Figure Shows

A scatter plot of sign-canonicalized r_q (x-axis) versus r_k (y-axis) for every Q head's PC0, colored by model. Each point represents one attention head's leading principal component from the combined QK PCA. Dashed lines at r = 0.3 and r = 0.7 delineate the taxonomy thresholds used to classify heads.

The figure reveals the joint distribution of Q-position and K-position signal strength across heads and models:

- **Llama 3.2** (red) clusters in the top-right quadrant: high r_q (0.7-1.0) and high r_k (0.5-0.9). These are strongly concordant position-dominated heads.
- **Qwen3** (blue) shows a bimodal pattern: larger models (4B, 8B, 14B) cluster similarly to Llama, while smaller models (0.6B, 1.7B) spread vertically at high r_q but low r_k — Q-positional heads where K does not encode position on PC0.
- **Ministral3** (green) occupies the moderate range: r_q ~ 0.6-0.9 with r_k ~ 0.3-0.7, rarely reaching the extreme corners. This produces the high "mixed" classification rate (77-84%).

The horizontal line at r_k = 0 is important: points above it have concordant Q/K position gradients (both increase with position), while points below have discordant gradients. Very few heads fall below r_k = -0.3 on PC0.

## How It Was Produced

1. **Data source**: `results/attention_plasticity/qk.csv`, filtered to PC0 only (`pc == 0`).

2. **Analysis pipeline**: Each point corresponds to one (model, layer, head) combination. The r_q and r_k values come from the combined QK PCA with sign canonicalization: the PCA eigenvector for each PC was oriented so that r_q >= 0, making the sign of r_k interpretable as concordant (positive) or discordant (negative) relative to Q's position gradient.

3. **Color coding**: Points are colored by model family — blue for Qwen3, red for Llama 3.2, green for Ministral3.

4. **Taxonomy thresholds**: Dashed lines at r = 0.3 and r = 0.7 (and their negatives for r_k) define the five head categories: position-dominated (r_q > 0.7 and |r_k| > 0.7), Q-positional (r_q > 0.7, |r_k| < 0.3), K-positional (r_q < 0.3, |r_k| > 0.7), content-focused (r_q < 0.3, |r_k| < 0.3), and mixed (everything else).

5. **Script**: `scripts/generate_report_figures.py`, function `fig07_rq_vs_rk_scatter()`.

## Key Takeaway

The scatter reveals that model families occupy distinct regions of the (r_q, r_k) plane. This has direct implications for how position enters the attention score: heads with both high r_q and high r_k contribute a strong alpha*beta (position x position) interaction term, while heads with high r_q but low r_k rely primarily on the mu_Q amplification mechanism for positional bias. The near-absence of points in the bottom-left (content-focused) region means very few heads have escaped positional encoding on their leading PC.
