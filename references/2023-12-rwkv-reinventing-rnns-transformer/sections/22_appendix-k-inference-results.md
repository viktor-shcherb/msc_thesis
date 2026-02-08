# K Inference Results [p. 23-25]

[p. 23-25]

Figures 13 and 14 illustrate, respectively, the results on time (s) and memory (RAM, VRAM) requirements for LLM inference in *float32* precision. The following model families and sizes are benchmarked:

- **RWKV**: 169m, 430m, 1.4b, 3b, 7b, 14b
- **Bloom** (Scao et al., 2022): 560m, 1b, 3b
- **OPT** (Zhang et al., 2022): 125m, 350m, 1.3b, 2.7b, 6.7b, 13b
- **GPT-Neo** (Black et al., 2021): 125m, 1.3b, 2.7b
- **Pythia** (Biderman et al., 2023b): 160m, 410m, 1.4b, 2.8b, 6.7b, 12b

**Figure 13** (p. 24): "Text generation inference memory (CPU RAM, GPU VRAM) for LLMs. Model parameters are not accounted."
- Two subplots side by side: CPU memory (left) and GPU VRAM (right).
- Both plot Peak Memory (GB) for 512 tokens (excluding model parameters) on the y-axis vs. # Params on the x-axis (log scale, from ~10^8 to ~10^10).
- CPU subplot: y-axis ranges from 0 to ~14 GB. All transformer models (bloom-cpu, gpt-neo-cpu, opt-cpu, pythia-cpu) show memory growing with model size, with bloom-cpu reaching the highest (~13 GB at 3b). RWKV (rwkv-4-pile-cpu) stays consistently low, remaining near ~1 GB across all model sizes up to 14b.
- GPU subplot: y-axis ranges from 0 to ~20 GB. Transformer models show steeply increasing VRAM (bloom-cuda, gpt-neo-cuda, opt-cuda, pythia-cuda all rising). RWKV (rwkv-4-pile-cuda) again remains low and nearly flat, staying below ~2.5 GB even at 14b parameters.
- This demonstrates RWKV's constant memory complexity during inference, in contrast to the growing memory requirements of transformer models.

**Figure 14** (p. 25): "Text generation inference time for LLMs."
- Two subplots side by side: CPU time (left) and GPU time (right).
- CPU subplot: y-axis is CPU time (s) for 512 tokens, ranging from 0 to ~2000s. x-axis is # Params (log scale). Transformer models show increasing inference time, with bloom-cpu being the slowest (~2000s at 3b). RWKV (rwkv-4-pile-cpu) is substantially faster, though its time still increases with model size.
- GPU subplot: y-axis is GPU time (s) for 512 tokens, ranging from 0 to ~250s. Transformer models increase steeply, with bloom-cuda reaching ~250s at 3b. RWKV (rwkv-4-pile-cuda) remains near the bottom, with inference time growing only slowly with model size.
- The results confirm RWKV's efficiency advantage for autoregressive text generation, particularly at larger model scales.
