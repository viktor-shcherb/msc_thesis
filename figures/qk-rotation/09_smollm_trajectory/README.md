# SmolLM3-3B: 2D Rotation Metrics Across Training

## File
`figure.png`

## What This Figure Shows

Four bar charts tracking key rotation metrics across 10 SmolLM3-3B training checkpoints. Error bars show interquartile range (p25-p75). Bars are colored by training phase: blue = stage 1, green = stage 2, orange = stage 3, red = LC 4k->32k, purple = LC 32k->64k. Vertical dotted lines separate phases.

Panels:
- **|r_k| on axis a**: K-position correlation stays high throughout (~0.86-0.92). Barely changes during long-context training.
- **Separation strength**: Increases during LC (+14%), as the model trades position drift for richer Q/K content separation.
- **Bias strength (x10^3)**: Collapses ~91% during LC (from 19.4 to 1.8), the most dramatic change across all metrics.
- **Plane variance fraction**: Increases during LC (34% -> 39%), as the {a, b} plane captures more of the total variance.

## How It Was Produced

1. **Data source**: `results/smollm3_training_progress/rotated.csv` (3,000 heads: 300 per checkpoint x 10 checkpoints).
2. **Script**: `scripts/generate_report.py`, function `fig11_training_trajectory()`.

## Key Takeaway

Long-context fine-tuning dramatically restructures the 2D geometry: drift slopes collapse (bias_strength drops 10x), but the drift *direction* is preserved (r_k stays ~0.91). Simultaneously, Q/K separation strengthens. The model learns to maintain position awareness (for relative-position attention via RoPE) while eliminating the absolute-position recency bias that would harm long-context performance.
