# Attention Plasticity Heatmap: Llama-3.2-11B

## File
`figure.png`

## Panel group
Figures 01–04 form a 2x2 comparison panel: Ministral3-14B, Qwen3-14B, Llama-3.2-3B, Llama-3.2-11B.

## What This Figure Shows

A 2D heatmap of attention plasticity as a function of inter-key distance (x-axis) and key-to-query distance (y-axis). Color encodes plasticity: yellow = high (content wins), dark = low (position wins).

Llama-3.2-11B exhibits a uniquely non-smooth pattern that differs from all other models. Instead of a clean diagonal gradient, dark patches appear at specific distance combinations (~16K and ~25K inter-key distance at certain key-to-query ranges) without affecting neighboring cells. A bright recovery zone is visible around key-to-query distances 57K–65K, where plasticity increases before collapsing again at 120K+.

This non-monotone structure matches the anomalous decile profile observed in the aggregate data (Table 4 in `05_benchmark_connection.md`): plasticity dips at 40–50% of context, recovers at 60–80%, then collapses at 90–100%.

## How It Was Produced

1. **Data source**: Post-RoPE Q/K vectors from `viktoroo/sniffed-qk`, captured via `qk-sniffer` on LongBench-Pro 128K+ samples.
2. **Computation**: Pairwise plasticity 4p(1-p) binned by inter-key distance and key-to-query distance.
3. **Tool**: `attention-plasticity` CLI, `bucket_heatmap.png` output.

## Key Takeaway

Llama-3.2-11B is a vision-language model with NoPE (no position encoding) layers interleaved with standard RoPE layers. The non-smooth plasticity structure — dark patches at characteristic distance scales and a mid-context recovery zone — is consistent with NoPE layers creating interference patterns at specific distance multiples. This architectural feature produces qualitatively different attention geometry that cannot be captured by smooth position-dependent models.
