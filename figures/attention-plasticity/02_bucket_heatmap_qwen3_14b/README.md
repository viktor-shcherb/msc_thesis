# Attention Plasticity Heatmap: Qwen3-14B

## File
`figure.png`

## Panel group
Figures 01–04 form a 2x2 comparison panel: Ministral3-14B, Qwen3-14B, Llama-3.2-3B, Llama-3.2-11B.

## What This Figure Shows

A 2D heatmap of attention plasticity as a function of inter-key distance (x-axis) and key-to-query distance (y-axis). Color encodes plasticity: yellow = high (content wins), dark = low (position wins).

Qwen3-14B shows a clear diagonal gradient from warm top-left to dark bottom-right. The dark region (plasticity <0.4) begins at ~50K inter-key distance and deepens toward the extreme corner. Compared to Ministral3-14B (same parameter count), Qwen3 loses content-based discrimination at significantly shorter inter-key separations.

The pattern is remarkably consistent across Qwen3 model scales: Qwen3-0.6B, 4B, 8B, and 14B all exhibit the same 2D shape, shifted slightly in absolute values. The architecture determines the plasticity geometry; scale adjusts the overall level.

## How It Was Produced

1. **Data source**: Post-RoPE Q/K vectors from `viktoroo/sniffed-qk`, captured via `qk-sniffer` on LongBench-Pro 128K+ samples.
2. **Computation**: Pairwise plasticity 4p(1-p) binned by inter-key distance and key-to-query distance.
3. **Tool**: `attention-plasticity` CLI, `bucket_heatmap.png` output.

## Key Takeaway

Qwen3-14B represents the middle ground: stronger 2D gradient than Ministral3 but less extreme than Llama. The same-size comparison with Ministral3-14B (both 14B) isolates the effect of architecture and training recipe on plasticity structure, independent of model scale. Qwen3's LBP score (37.11) is close to Ministral3-14B's (40.14), but the steeper plasticity gradient (ap_drop 0.161 vs 0.068) suggests more vulnerability at longer contexts.
