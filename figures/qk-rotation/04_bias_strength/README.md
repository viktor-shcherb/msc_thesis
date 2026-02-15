# Bias Strength Distribution by Model Family

## File
`figure.png`

## What This Figure Shows

Three histogram panels (one per family: Qwen3, Llama 3.2, Ministral3) showing the distribution of bias_strength = mu_Q^a * alpha_K across heads. A vertical red dashed line marks zero. Values are scaled by 10^3 for readability.

The key finding: **99.0% of all 3,239 heads have positive bias_strength**, meaning later key positions receive systematically higher attention scores. This is universal recency bias, arising from the geometry of the Q/K embedding space. Only 31 heads show negative (primacy) bias.

The sign of bias_strength is invariant to axis orientation: flipping a changes both mu_Q^a and alpha_K in sign, leaving their product unchanged.

## How It Was Produced

1. **Data source**: `results/rotation/rotated.csv`, column `bias_strength`.
2. **Script**: `scripts/generate_report.py`, function `fig04_bias_strength()`.

## Key Takeaway

Recency bias is not a training artifact or architectural quirk — it is a near-universal geometric property of the Q/K embedding space. The mechanism is precise: the Q cluster mean on the drift axis (mu_Q^a) amplifies the K-position slope (alpha_K), creating a term mu_Q^a * alpha_K * j that grows linearly with key position j. This is the mechanistic origin of the "lost in the middle" phenomenon.
