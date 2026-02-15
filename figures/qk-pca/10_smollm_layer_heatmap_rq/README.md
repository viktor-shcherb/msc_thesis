# SmolLM3-3B: r_q Layer-Depth Heatmap Across Training

## File
`figure.png`

## What This Figure Shows

A heatmap where each row is a training checkpoint (10 rows, chronologically ordered top to bottom) and each column is a normalized depth bin (10 bins). Cell values show mean r_q on PC0 for all heads in that (checkpoint, depth) combination. Blue color intensity encodes r_q magnitude.

The figure reveals how Q-position encoding develops across layers during training:

- **Step 40K** (earliest): r_q is already moderate (0.5-0.8) across most layers, with some variation. The RoPE structure is partially present even at this early stage.
- **Step 1.2M onward**: r_q becomes uniformly high (0.75-0.90) across all depths. Layer-wise variation is small.
- **Long-context phases**: r_q tightens further, with values consistently in the 0.85-0.90 range. The layer-wise pattern becomes nearly flat.

A notable feature is that early layers (depth 0.0-0.2) tend to have slightly higher r_q than late layers across most checkpoints. This is consistent with the cross-model analysis, where early layers often show the strongest positional signal.

SmolLM3 has NoPE layers (every 4th layer has no RoPE). These NoPE layers are included in the depth bins — their typically lower r_q values contribute to bin averages, creating the slightly mottled pattern visible at step 40K.

## How It Was Produced

1. **Data source**: `results/smollm3_training_progress/qk.csv`, filtered to PC0.

2. **Depth normalization**: For each checkpoint (model), layer indices are normalized to [0, 1] by dividing by the max layer (35 for SmolLM3-3B, which has 36 layers indexed 0-35) and discretized into 10 bins.

3. **Aggregation**: Mean r_q per (checkpoint, depth_bin).

4. **Visualization**: matplotlib imshow with "Blues" colormap, vmin=0, vmax=1.

5. **Script**: `scripts/generate_report_figures.py`, function `smollm_fig05_layer_heatmap_rq()`.

## Key Takeaway

Q-position encoding on PC0 is established early and uniformly across layers. By step 1.2M, there is minimal layer-wise variation in r_q. This suggests that the Q-position signal is a fundamental, layer-independent property of the post-RoPE Q representation, not something that develops differently across network depth.
