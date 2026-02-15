# Attention Plasticity Heatmap: Llama-3.2-3B

## File
`figure.png`

## Panel group
Figures 01–04 form a 2x2 comparison panel: Ministral3-14B, Qwen3-14B, Llama-3.2-3B, Llama-3.2-11B.

## What This Figure Shows

A 2D heatmap of attention plasticity as a function of inter-key distance (x-axis) and key-to-query distance (y-axis). Color encodes plasticity: yellow = high (content wins), dark = low (position wins).

Llama-3.2-3B shows the most extreme contrast of any model. The dark region (plasticity <0.3) starts at ~40K inter-key distance — earlier than any other family — and reaches values below 0.2 in the bottom-right corner. The warm region is confined to small inter-key distances (<30K) regardless of key-to-query distance.

This model has the steepest ap_drop (0.230) and the lowest LongBench Pro score (15.71) among all sniffed models with benchmark data.

## How It Was Produced

1. **Data source**: Post-RoPE Q/K vectors from `viktoroo/sniffed-qk`, captured via `qk-sniffer` on LongBench-Pro 128K+ samples.
2. **Computation**: Pairwise plasticity 4p(1-p) binned by inter-key distance and key-to-query distance.
3. **Tool**: `attention-plasticity` CLI, `bucket_heatmap.png` output.

## Key Takeaway

Llama-3.2-3B demonstrates the failure mode: when position bias dominates content signal at moderate inter-key distances, the model cannot perform content-based retrieval over long contexts. The 2D heatmap makes this failure more precise than 1D profiles — the critical variable is inter-key distance, not just absolute position. Two relevant keys that are far apart in the context will be resolved by position rather than content, regardless of where the query is.
