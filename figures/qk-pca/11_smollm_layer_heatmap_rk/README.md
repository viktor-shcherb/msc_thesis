# SmolLM3-3B: r_k Layer-Depth Heatmap Across Training

## File
`figure.png`

## What This Figure Shows

A heatmap where each row is a training checkpoint and each column is a normalized depth bin. Cell values show mean r_k on PC0. Red color intensity encodes r_k magnitude.

This figure contrasts with the r_q heatmap in revealing much more layer-wise and temporal variation in K-position encoding:

- **Step 40K**: r_k shows substantial layer variation (0.2-0.7), with no consistent depth pattern yet.
- **Steps 1.2M-3.44M** (mid/late stage 1): r_k strengthens and develops a depth pattern — early layers (0.0-0.3) show higher r_k (0.5-0.7) than late layers (0.3-0.5).
- **Stages 2-3**: The early-layer r_k advantage persists and slightly strengthens.
- **Long-context phases**: r_k overall decreases (the drop visible in the position signal figure), but the layer-wise gradient persists — early layers remain the strongest K-position encoders. Late-layer r_k drops to 0.3-0.4 in some bins.

The depth-dependent r_k pattern suggests that early layers establish a stronger K-position signal on PC0, while deeper layers increasingly allocate K variance to content rather than position.

## How It Was Produced

1. **Data source**: `results/smollm3_training_progress/qk.csv`, filtered to PC0.

2. **Depth normalization and aggregation**: Same methodology as the r_q heatmap.

3. **Visualization**: matplotlib imshow with "Reds" colormap, vmin=0, vmax=1.

4. **Script**: `scripts/generate_report_figures.py`, function `smollm_fig06_layer_heatmap_rk()`.

## Key Takeaway

K-position encoding on PC0 is fundamentally more dynamic than Q-position encoding — it varies more across layers, changes more during training, and responds differently to long-context fine-tuning. The early-layer K-position advantage (higher r_k in shallow layers) is consistent with the idea that early layers handle more "structural" processing (position, syntax) while deeper layers shift toward semantic content. The r_k drop during long-context training is most pronounced in deep layers, suggesting these layers are where the model most aggressively repurposes K capacity from position to content when adapting to longer contexts. This layer-wise heterogeneity in K-position encoding may be a key factor in determining which layers are bottlenecks for effective context length.
