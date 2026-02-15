# Per-Head Plasticity Profile: Ministral3-3B

## File
`figure.png`

## Panel group
Figures 05–07 form a 1x3 comparison panel: Ministral3-3B, Qwen3-4B, Llama-3.2-3B.

## What This Figure Shows

Per-bucket attention plasticity vs token position for all attention heads in Ministral3-3B. Gray lines are individual heads; the red line is the mean across all heads.

Ministral3-3B displays a tight gray bundle with low inter-head variance. Nearly all heads decline gently and uniformly from ~0.7 at position 0 to ~0.58 at position 128K. Few outlier heads fall below 0.4. The architecture produces homogeneous attention behavior — all heads maintain similar plasticity levels throughout the context.

## How It Was Produced

1. **Data source**: Post-RoPE Q/K vectors from `viktoroo/sniffed-qk` on LongBench-Pro 128K+ samples.
2. **Computation**: Per-head plasticity computed in position buckets, then plotted as individual traces with mean overlay.
3. **Tool**: `attention-plasticity` CLI, `plasticity.png` output.

## Key Takeaway

Ministral3's uniformly plastic heads contrast sharply with Qwen3's bimodal head population and Llama's converging heads. The low inter-head variance suggests the training recipe produces attention heads that all contribute to content-based retrieval, rather than specializing some heads for position-based patterns and others for content. This homogeneity may explain the flat ap_drop (0.072) — no subpopulation of heads degrades rapidly at distance.
