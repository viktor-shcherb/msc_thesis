# K-to-Q Drift Slope Ratio

## File
`figure.png`

## What This Figure Shows

A bar chart showing the median ratio |alpha_K| / |alpha_Q| per model. Values above the dashed line (ratio = 1) indicate that K-vector projections on axis a change faster per position step than Q-vector projections.

Keys drift 1.8x faster than queries on average (median across all heads). The ratio varies by family: Qwen3 small models show extreme ratios (~8x), Ministral3 is nearly balanced (~1x), and Llama 3.2 is intermediate (~2x).

## How It Was Produced

1. **Data source**: `results/rotation/rotated.csv`, columns `alpha_q`, `alpha_k`.
2. **Script**: `scripts/generate_report.py`, function `fig03_slope_ratio()`.

## Key Takeaway

The K-drift slope directly feeds into the recency bias mechanism through the term mu_Q^a * alpha_K * j. Models with larger |alpha_K| / |alpha_Q| ratios have position bias that is more K-driven — the bias depends primarily on key position rather than query position. This asymmetry arises from how W_Q and W_K project the RoPE-induced drift differently onto the shared drift axis.
