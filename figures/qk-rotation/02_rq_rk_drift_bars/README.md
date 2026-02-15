# Q vs K Position Correlation on the Drift Axis

## File
`figure.png`

## What This Figure Shows

A grouped bar chart showing mean |r_q| (blue) and |r_k| (red) on axis a across all 11 models. The drift axis a is the direction proportional to Cov(X, t) in the pooled Q+K space.

The key finding: **K encodes position more strongly than Q on the drift axis** (mean |r_k| = 0.87, mean |r_q| = 0.74). This reverses the asymmetry seen in combined QK PCA (where r_q > r_k on PC0), because the drift axis aligns with position *covariance* rather than maximum *total variance*. Since PC0 is dominated by the large Q/K cluster separation, PCA conflates position encoding with Q/K identity, understating K's position signal.

## How It Was Produced

1. **Data source**: `results/rotation/rotated.csv` (3,239 heads across 11 models).
2. **Script**: `scripts/generate_report.py`, function `fig01_rq_rk_bars()`.

## Key Takeaway

The drift axis reveals that keys are the primary carriers of position information in the asymmetric RoPE drift component — the opposite conclusion from PCA. This distinction matters for the attention score model: the dominant position bias term is mu_Q^a * alpha_K * j, where alpha_K (the K drift slope) is the mechanistically relevant quantity.
