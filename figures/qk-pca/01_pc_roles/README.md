# Combined QK PCA: Position Correlation by Principal Component

## File
`figure.png`

## What This Figure Shows

A grouped bar chart showing the mean Pearson correlation coefficient between each principal component's projection and token position, separately for Q vectors (r_q, blue) and K vectors (r_k, red). The x-axis shows PC indices 0 through 9; the y-axis shows mean Pearson r with position.

The figure demonstrates that position information is overwhelmingly concentrated in the first principal component (PC0). PC0 shows mean r_q ~ 0.80 and mean r_k ~ 0.48 across all 11 models. PC1 picks up residual Q-position signal (r_q ~ 0.38) but essentially no K-position (r_k ~ -0.03). PCs 2+ show rapidly diminishing position correlations in both Q and K, indicating they capture primarily content (semantic) information.

The asymmetry between Q and K is consistent across all PCs: Q vectors encode position more strongly than K vectors on the leading components. After sign canonicalization (r_q >= 0 by convention), the sign of r_k becomes interpretable: positive means Q and K position gradients are concordant (both increase with position), negative means discordant.

## How It Was Produced

1. **Data source**: `results/attention_plasticity/qk.csv` from the `qk-pca-analysis` repository, containing per-head, per-PC analysis results for 11 models (5 Qwen3, 3 Llama 3.2, 3 Ministral3), totalling 3,239 Q heads.

2. **Analysis pipeline**: For each head (model, layer, head), `pca-analyze` performed combined QK PCA: Q and K vectors (both in R^d) were pooled and a single PCA rotation was fitted on the pooled set (10 components, sklearn). The shared rotation preserves q.k exactly. Q and K subsets were then projected separately through the shared PCA components. For each PC, Pearson r was computed between the PC projection values and token positions, independently for Q (r_q) and K (r_k). Sign canonicalization oriented each PC so that r_q >= 0.

3. **Aggregation**: For each PC index (0-9), the mean r_q and mean r_k were computed across all (model, layer, head) combinations. The bar chart displays these grand means.

4. **Script**: `scripts/generate_report_figures.py`, function `fig04_pc_roles()`.

## Key Takeaway

PC0 alone captures the dominant positional signal. The ~0.80 Q-position correlation and ~0.48 K-position correlation on PC0, combined with PC0's high explained variance (~34%), means that roughly 25% of total Q+K vector variance is attributable to a linear function of token position — all packed into a single principal component. This is the structural fingerprint of rotary positional encoding (RoPE).
