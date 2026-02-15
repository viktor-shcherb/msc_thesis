# Combined QK PCA: Explained Variance by Principal Component

## File
`figure.png`

## What This Figure Shows

A bar chart showing the mean explained variance ratio by PC index (0 through 9) across all 11 models and all heads. Each bar is annotated with its percentage value.

PC0 captures approximately 34% of total combined QK variance — substantially higher than any subsequent PC. PC1 accounts for ~5%, PC2 for ~4%, and remaining PCs each account for less than 3%. The rapid drop-off after PC0 indicates that the combined QK space has one strongly dominant direction.

The high PC0 explained variance is a consequence of two effects compounding in the combined PCA: (1) Q and K vectors occupy geometrically distinct regions of R^d (mean separation ~47 units on PC0, Fisher discriminant ~44), and (2) within each cluster, position creates a strong linear gradient. Both effects are captured by the same principal direction, inflating its variance share relative to single-kind PCA.

## How It Was Produced

1. **Data source**: `results/attention_plasticity/qk.csv`, all rows with PC indices 0-9.

2. **Aggregation**: For each PC index, the mean `explained_variance` column value is computed across all (model, layer, head) combinations.

3. **Visualization**: Simple bar chart with purple color, annotated with percentage labels above each bar.

4. **Script**: `scripts/generate_report_figures.py`, function `fig08_explained_variance()`.

## Key Takeaway

The ~34% variance concentration in PC0 is the basis for the "~25% of total variance is linear in position" calculation. Specifically: PC0 captures 34% of variance, and about 67% of PC0's Q-variance is linear in position (r²_q = 0.80² = 0.64), yielding ~22% of total Q-variance as positional on PC0 alone. Adding contributions from PCs 1-9 brings the total to ~27% for Q and ~14% for K. This means roughly a quarter of the entire Q+K representational space is consumed by encoding token position.
