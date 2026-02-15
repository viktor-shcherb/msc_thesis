# Per-Head Plasticity Profile: Qwen3-4B

## File
`figure.png`

## Panel group
Figures 05–07 form a 1x3 comparison panel: Ministral3-3B, Qwen3-4B, Llama-3.2-3B.

## What This Figure Shows

Per-bucket attention plasticity vs token position for all attention heads in Qwen3-4B. Gray lines are individual heads; the red line is the mean across all heads.

Qwen3-4B displays a wide gray spread revealing a bimodal head population: a bundle of highly plastic heads near 0.8–1.0 that maintain flexibility across the full context, and a bundle of position-locked heads near 0.2–0.3 that are rigid from the start. The mean (red line) threads between these two populations, declining from ~0.75 to ~0.50 as the proportion of position-dominated heads increases with distance.

## How It Was Produced

1. **Data source**: Post-RoPE Q/K vectors from `viktoroo/sniffed-qk` on LongBench-Pro 128K+ samples.
2. **Computation**: Per-head plasticity computed in position buckets, then plotted as individual traces with mean overlay.
3. **Tool**: `attention-plasticity` CLI, `plasticity.png` output.

## Key Takeaway

Qwen3-4B's bimodal head population reveals functional specialization: some heads perform content-based retrieval (high plasticity) while others encode positional structure (low plasticity). The mean plasticity decline is driven not by all heads degrading uniformly, but by the balance shifting as distance-sensitive heads lose flexibility. This heterogeneity is consistent across Qwen3 scales (0.6B–14B) and contrasts with Ministral3's homogeneous heads.
