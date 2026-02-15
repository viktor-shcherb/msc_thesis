# Layer-Depth Heatmap: Mean r_k on PC0

## File
`figure.png`

## What This Figure Shows

A heatmap where each row is a model (11 models) and each column is a normalized depth bin (10 bins). Cell values show the mean r_k (Pearson correlation between PC0 K-projection and token position) for all heads in that depth bin. Color intensity (red scale) encodes r_k magnitude from 0 to 1.

This figure contrasts sharply with the r_q heatmap, revealing that **K-position encoding on PC0 is far more heterogeneous than Q-position encoding**:

- **Small Qwen3** (0.6B, 1.7B) show uniformly low r_k (0.11-0.35) across all layers. K vectors barely encode position on PC0 in these models — their positional K information resides on later PCs.
- **Larger Qwen3** (4B, 8B, 14B) and **Llama 3.2** show moderate r_k (0.40-0.73), with Llama models peaking in early layers and declining with depth.
- **Ministral3** models show moderate r_k (0.30-0.65), with the 8B model having somewhat higher values than the 3B and 14B.

The key contrast with the r_q heatmap is that r_k differentiates model families far more strongly than r_q does. While all models agree on high Q-position encoding, they diverge substantially on whether K vectors co-encode position on the same leading PC.

## How It Was Produced

1. **Data source**: `results/attention_plasticity/qk.csv`, filtered to PC0 (`pc == 0`).

2. **Depth normalization**: Same as r_q heatmap — layer indices normalized to [0, 1] and discretized into 10 bins.

3. **Aggregation**: Within each (model, depth_bin), the mean r_k is computed.

4. **Visualization**: matplotlib imshow with "Reds" colormap, vmin=0, vmax=1.

5. **Script**: `scripts/generate_report_figures.py`, function `fig06_layer_heatmap_k()` via helper `_layer_heatmap()`.

## Key Takeaway

The r_k heatmap is the clearest evidence that model families handle K-position encoding differently. Small Qwen3 models concentrate K-position information on later PCs (not PC0), while Llama and larger Qwen3 models co-encode Q and K position on the same leading component. This has direct implications for how position enters the attention dot product: when both r_q and r_k are high on PC0, the alpha*beta interaction term creates a position-by-position attention bias (favoring nearby or distant keys depending on sign). When r_k is low on PC0, position enters attention primarily through the mu_Q amplification of whatever K-position gradient exists — a fundamentally different mechanism.
