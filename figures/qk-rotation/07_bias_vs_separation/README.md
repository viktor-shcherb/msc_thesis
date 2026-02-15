# Bias Strength vs Separation Strength (Simpson's Paradox)

## File
`figure.png`

## What This Figure Shows

Three scatter panels (Llama 3.2, Qwen3, Ministral3) plotting bias_strength (y) vs separation_strength (x) per head. Within-family Pearson r is shown in each panel title.

The overall correlation between bias_strength and separation_strength is +0.48, but within Llama 3.2 it reverses to -0.65 (high-bias heads have low separation, and vice versa). Qwen3 shows a positive within-family correlation, and Ministral3 shows no correlation. This is a textbook Simpson's paradox: the between-family confound creates a spurious positive overall correlation.

## How It Was Produced

1. **Data source**: `results/rotation/rotated.csv`, columns `bias_strength`, `separation_strength`.
2. **Script**: `scripts/generate_report.py`, function `fig08_bias_vs_separation()`.

## Key Takeaway

Any cross-family analysis of bias vs separation must stratify by family to avoid the Simpson's paradox. The within-family patterns are genuinely different: Llama shows a trade-off (heads specialize in either position bias or Q/K separation), while Qwen3 supports both simultaneously.
