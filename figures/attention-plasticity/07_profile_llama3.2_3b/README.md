# Per-Head Plasticity Profile: Llama-3.2-3B

## File
`figure.png`

## Panel group
Figures 05–07 form a 1x3 comparison panel: Ministral3-3B, Qwen3-4B, Llama-3.2-3B.

## What This Figure Shows

Per-bucket attention plasticity vs token position for all attention heads in Llama-3.2-3B. Gray lines are individual heads; the red line is the mean across all heads.

Llama-3.2-3B starts with a wide gray spread similar to Qwen3-4B — heterogeneous heads with some near 0.8 and others near 0.3. But unlike Qwen3, the gray lines converge at distance: past 100K tokens, nearly all heads cluster around 0.45, erasing individual differences. Position bias eventually dominates every head, including those that were highly plastic at short distances.

The mean (red line) declines steeply from ~0.75 to ~0.45, the largest drop of any model.

## How It Was Produced

1. **Data source**: Post-RoPE Q/K vectors from `viktoroo/sniffed-qk` on LongBench-Pro 128K+ samples.
2. **Computation**: Per-head plasticity computed in position buckets, then plotted as individual traces with mean overlay.
3. **Tool**: `attention-plasticity` CLI, `plasticity.png` output.

## Key Takeaway

The convergence effect is diagnostic: even content-specialized heads cannot maintain flexibility at 100K+ in Llama-3.2-3B. This distinguishes it from Qwen3 (where some heads remain plastic throughout) and Ministral3 (where all heads remain plastic). The convergence to ~0.45 at distance matches the LBP score cliff — this model's worst-in-class benchmark performance (15.71) reflects a regime where no head can perform content-based retrieval at distance.
