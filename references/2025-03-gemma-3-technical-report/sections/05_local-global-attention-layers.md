# 5.2. Local:Global attention layers [p. 6–7]

We measure the impact of changes to local and global self-attention layers on performance and memory consumption during inference.

## Local:Global ratio

In Fig. 3, we compare different ratios of local to global attention layers. 1:1 is used in Gemma 2 models, and 5:1 is used in Gemma 3. We observe minimal impact on perplexity when changing this ratio.

**Figure 3** (p. 6): "Impact of Local:Global ratio on the perplexity on a validation set. The impact is minimal, even with 7-to-1 local to global. This ablation is run with text-only models."

Description: Line plot
- X-axis: Local:Global ratio (1:1, 3:1, 5:1, 7:1)
- Y-axis: Δ Perplexity (ranging from -0.1 to 0.1)
- Two lines shown: 2B and 9B models
- Notable pattern: Both model sizes show perplexity changes remain within ±0.1 across all ratios tested
- Supports claim: Local:Global ratio can be adjusted with minimal impact on model quality

## Sliding window size

In Fig. 4, we compare different sliding window sizes for the local attention layers in different global:local ratio configurations. The sliding window can be reduced significantly without impacting perplexity.

**Figure 4** (p. 7): "Impact of Sliding Window size on perplexity measured on a validation set. We consider 2 2B models, with 1:1 and 1:3 local to global layer ratios. This ablation is run with text-only models."

Description: Line plot
- X-axis: Sliding Window size (512, 1024, 2048, 4096)
- Y-axis: Δ Perplexity (ranging from -0.02 to 0.01)
- Two lines shown: 2B L:G=1:1 (red) and 2B L:G=3:1 (yellow/orange)
- Notable pattern: Both configurations show minimal perplexity change across window sizes, remaining within ±0.01
- Supports claim: Sliding window size can be varied without significantly impacting model quality

## Impact on KV cache memory

In Fig. 5, we show the balance between the memory used by the model and the KV cache during inference with a context of 32k tokens. The "global only" configuration is the standard configuration used across most dense models. The "1:1, sw=4096" is used in Gemma 2. We observe that the "global only" configuration results in a memory overhead of 60%, while this is reduced to less than 15% with 1:3 and sliding windows of 1024 (shown as "1:3 sw=1024").

**Figure 5** (p. 7): "Model versus KV cache memory during inference with a pre-fill KV cache of size 32k. We consider a 2B model with different local to global ratios and sliding window size (L:G and sw). We compare to global only, which is the standard used in Gemma 1 and Llama. This ablation is run with a text-only model."

Description: Stacked bar chart
- X-axis: Five configurations (global only, 1:1 sw=4096, 1:3 sw=1024, 1:3 sw=1024, 1:3 sw=1024)
- Y-axis: Memory usage in MB (up to 5000)
- Two stacked components: Model (yellow) and KV cache (red)
- Notable pattern: Global only shows highest KV cache overhead; 1:3 configurations show significantly reduced KV cache memory
- Supports claim: Local:Global attention with sliding windows reduces KV cache memory overhead from 60% to <15%

In Fig. 6, we compute the memory used by the KV cache as a function of the context length with either our 2B architecture (L:G=5:1, sw=1024) versus a "global only" 2B model.

**Figure 6** (p. 7): "KV cache memory versus context length. We show the memory usage of the KV cache for our architecture (L:G=5:1, sw=1024) and a transformer with global attention only – as used in LLaMa or Gemma 1."

Description: Line plot
- X-axis: Context length (1K, 4K, 8K, 16K, 32K, 64K, 128K)
- Y-axis: KV cache memory in MB
- Two lines: 2B L:G=5:1, sw=1024 (red, lower) and 2B global only (yellow, upper)
- Notable pattern: Global-only configuration shows exponential growth in memory usage, while L:G=5:1 configuration shows much slower linear growth
- Supports claim: The hybrid local:global architecture dramatically reduces KV cache memory requirements at long context lengths
