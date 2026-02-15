# Layer-Depth Heatmap: Mean r_q on PC0

## File
`figure.png`

## What This Figure Shows

A heatmap where each row is a model (11 models: 5 Qwen3, 3 Llama 3.2, 3 Ministral3) and each column is a normalized depth bin (0.0 to 0.9, in 10 equal bins). Cell values show the mean r_q (Pearson correlation between PC0 Q-projection and token position) for all heads in that depth bin. Color intensity (blue scale) encodes r_q magnitude from 0 to 1. Each cell is annotated with its numeric value.

The figure reveals how Q-position encoding varies across network depth:

- **All models show uniformly high r_q** (>= 0.59 at every depth), confirming that PC0 reliably captures Q-position regardless of layer.
- **Small Qwen3** (0.6B, 1.7B) peak in early layers (r_q ~ 0.91) with slight decline toward late layers (~0.70).
- **Medium Qwen3** (4B, 8B) show a notable mid-layer dip (r_q ~ 0.59), recovering in later layers. This suggests mid-network layers temporarily repurpose the leading PC for content processing.
- **Llama 3.2** models are relatively uniform (r_q ~ 0.78-0.89) across depth.
- **Ministral3** models show a distinctive U-shape: high in early layers, dipping in middle layers, recovering toward the end.

## How It Was Produced

1. **Data source**: `results/attention_plasticity/qk.csv`, filtered to PC0 (`pc == 0`).

2. **Depth normalization**: For each model, layer indices are divided by the model's maximum layer index to produce normalized depth in [0, 1]. This depth is discretized into 10 equal bins (0.0-0.1, 0.1-0.2, ..., 0.9-1.0).

3. **Aggregation**: Within each (model, depth_bin), the mean r_q is computed across all heads in that bin.

4. **Visualization**: matplotlib imshow with "Blues" colormap, vmin=0, vmax=1. Cell annotations show the mean value to 2 decimal places.

5. **Script**: `scripts/generate_report_figures.py`, function `fig05_layer_heatmap_q()` via helper `_layer_heatmap()`.

## Key Takeaway

Q-position encoding on PC0 is a near-universal property: it holds across all layers, all model families, and all model sizes. The mid-layer dip in medium Qwen3 models is the only notable deviation, suggesting a region where the network prioritizes content over position in its leading variance direction. This universality supports the interpretation of PC0 as capturing a fundamental structural property of post-RoPE Q vectors rather than an artifact of specific architectures.
