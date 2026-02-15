# SmolLM3-3B: Bias Strength Decomposition During Training

## File
`figure.png`

## What This Figure Shows

Three bar panels decomposing bias_strength = mu_Q^a * alpha_K across 10 SmolLM3-3B training checkpoints:

- **Left (mu_Q^a)**: The Q cluster mean on axis a *increases* during LC training (4.7 -> 6.6, +43%). The Q/K clusters move further apart on the drift axis.
- **Center (alpha_K x10^3)**: The K drift slope *collapses* during LC (4.08 -> 0.27, -93%). This is the dominant driver of the bias reduction.
- **Right (bias_strength x10^3)**: The product drops from 19.4 to 1.8 (-91%), entirely driven by alpha_K shrinkage despite mu_Q^a growth.

## How It Was Produced

1. **Data source**: `results/smollm3_training_progress/rotated.csv`.
2. **Script**: `scripts/generate_report.py`, function `fig12_bias_decomposition()`.

## Key Takeaway

The mechanism of bias reduction during long-context training is precise: the model flattens the drift slopes (alpha_K, alpha_Q) while preserving the drift direction and even increasing Q/K cluster separation. The drift direction a remains meaningful (r_k ~ 0.91), but projections onto a change 10x more slowly per position step. This means RoPE-induced positional encoding is still present, but W_Q and W_K dampen its asymmetric drift component — the part that creates absolute-position recency bias. The symmetric component (shared rotations in the complement) is preserved for relative-position attention.
