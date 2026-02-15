# Layer-Depth Heatmaps: r_k and Bias Strength

## File
`figure.png`

## What This Figure Shows

Two layer-depth heatmaps (top: |r_k| on axis a; bottom: bias_strength x10^3). Rows = 11 models, columns = 10 normalized depth bins (0.0 = first layer, 1.0 = last layer). Cell values are annotated.

The top panel shows that K-position correlation on the drift axis is uniformly high across layers (0.80-0.95) for most models. Qwen3 shows the strongest depth gradient, with early layers encoding K-position most strongly.

The bottom panel shows bias_strength is strongest in early/middle layers and decreases toward the output layers in most models. Qwen3 again shows the steepest depth gradient.

## How It Was Produced

1. **Data source**: `results/rotation/rotated.csv`.
2. **Binning**: Each head's layer index is normalized by the model's max layer to produce a depth fraction in [0, 1], then binned into 10 equal-width bins.
3. **Script**: `scripts/generate_report.py`, function `fig07_layer_heatmaps()`.

## Key Takeaway

Position encoding and recency bias have depth structure: early layers encode position more strongly and produce more bias. This is consistent with the view that early layers handle positional routing while deeper layers focus on content processing.
