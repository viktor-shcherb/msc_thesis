# Attention Plasticity Heatmap: Ministral3-14B

## File
`figure.png`

## Panel group
Figures 01–04 form a 2x2 comparison panel: Ministral3-14B, Qwen3-14B, Llama-3.2-3B, Llama-3.2-11B.

## What This Figure Shows

A 2D heatmap of attention plasticity as a function of inter-key distance (x-axis: how far apart two competing keys are) and key-to-query distance (y-axis: how far the keys are from the query position). Color encodes plasticity: yellow = high (content determines which key wins), dark purple/black = low (position determines which key wins). The triangular shape arises from geometric constraints.

Ministral3-14B shows a strikingly warm/uniform pattern. The high-plasticity region (>0.55) fills nearly the entire triangle. The dark corner is confined to extreme inter-key distances (>90K tokens) at moderate key-to-query distances. This model maintains content-based attention discrimination even when competing keys are 80K+ tokens apart.

## How It Was Produced

1. **Data source**: Post-RoPE Q/K vectors from `viktoroo/sniffed-qk`, captured via `qk-sniffer` on LongBench-Pro 128K+ samples.
2. **Computation**: For each pair of keys at positions j1, j2 with a query at position i, plasticity = 4p(1-p) where p = P(query prefers k1 over k2). Binned by inter-key distance |j1-j2| and key-to-query distance.
3. **Tool**: `attention-plasticity` CLI, `bucket_heatmap.png` output.

## Key Takeaway

Ministral3-14B's flat 2D plasticity structure explains its best-in-class LongBench Pro score (40.14) among sniffed models. The attention mechanism remains flexible across the full 128K context — position bias never dominates content signal, even at extreme key separations. The 3B and 8B Ministral3 models show nearly identical 2D structure, suggesting the architecture determines the geometry.
