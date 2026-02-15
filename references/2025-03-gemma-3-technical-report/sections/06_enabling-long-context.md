# 5.3. Enabling long context [p. 7]

Instead of training with 128K sequences from scratch, we pre-train our models with 32K sequences and then scale the 4B, 12B, and 27B models up to 128K tokens at the end of pre-training while reseeding RoPE (Chen et al., 2023). We find a scaling factor of 8 to work well in practice. Note that compared to Gemma 2, we have also increased the RoPE base frequency of global self-attention layers from 10k to 1M, while keeping 10k for the local self-attention layers. In Figure 7, we show the impact on perplexity for different context lengths. Our models generalize to 128K, but rapidly degrade as we continue to scale.

**Figure 7** (p. 7): "Long context performance of pre-trained models before and after RoPE rescaling."

Description: Line plot
- X-axis: Context length (16K, 32K, 64K, 128K, 256K, 512K)
- Y-axis: Average perplexity (ranging from 0.54 to 0.70)
- Six lines shown: 4B, 4B + long context, 12B, 12B + long context, 27B, 27B + long context
- Notable patterns:
  - Without long context extension (dashed lines): perplexity increases sharply after 32K
  - With long context extension (solid lines): perplexity remains relatively stable through 128K, then degrades beyond that
  - All model sizes show similar behavior: generalization up to 128K, degradation beyond
- Supports claim: RoPE rescaling enables models to generalize to 128K context length
