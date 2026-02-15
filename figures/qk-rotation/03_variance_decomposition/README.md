# Variance Decomposition: 2D Plane vs Complement

## File
`figure.png`

## What This Figure Shows

A stacked bar chart showing the fraction of total Q+K variance captured by each component: axis a (red, drift/position), axis b (blue, separation/semantic), and the complement (gray, d-2 dimensions). Shown for all 11 models.

The {a, b} plane captures ~38% of total variance on average (range: 29-46%), despite being only 2 of 64-128 dimensions. Axis b consistently captures more variance than axis a (in 88% of heads), reflecting the large Q/K cluster separation. The remaining ~62% is spread across the complement's d-2 dimensions, which contain RoPE rotation planes (non-linear position encoding) and content information.

## How It Was Produced

1. **Data source**: `results/rotation/rotated.csv`, columns `var_frac_a`, `var_frac_b`.
2. **Script**: `scripts/generate_report.py`, function `fig05_variance_decomposition()`.

## Key Takeaway

Two purposefully constructed dimensions capture over a third of the representational space. This is comparable to what PCA achieves with PC0+PC1 (~38%), but the rotation model's axes have guaranteed interpretability: axis a captures exactly the linear position covariance, and axis b captures the maximum Q-K separation orthogonal to position.
