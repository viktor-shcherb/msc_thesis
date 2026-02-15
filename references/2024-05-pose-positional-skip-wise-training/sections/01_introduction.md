# Introduction [p. 1-2]

[p. 1] LLMs are bounded by pre-defined context windows and degrade when input exceeds training length. The paper frames long-context adaptation as extending a pre-trained model from original window `Lc` to target window `Lt`.

[p. 1] Prior context extension based on position interpolation (Chen et al., 2023a; kaiokendev, 2023; Peng et al., 2023) still uses full-length fine-tuning at target length and is expensive because attention compute grows quadratically with sequence length.

[p. 1] Example compute claim: extending LLaMA from 2k to 8k used 32 A100 GPUs, and larger contexts used 128 A100 GPUs (citing Chen et al., 2023a).

[p. 2] Core proposal: **Positional Skip-wisE (PoSE)** decouples train length from target length by simulating long-input positional patterns while training only at original context length.

[p. 2] Claimed advantages:
- Memory/time efficiency: fixed train length avoids full quadratic target-length fine-tuning cost.
- Extreme extension potential: reported up to `2k -> 128k` on LLaMA (64x extension).
- Compatibility: works with multiple RoPE-based models (LLaMA, LLaMA2, GPT-J, Baichuan) and interpolation strategies (Linear, NTK, YaRN).

[p. 2] The paper states PoSE can "theoretically extend context window to an infinite length" with practical limits set by inference memory and systems optimizations (FlashAttention, xFormers, vLLM).

**Figure 1** (p. 2): "Position indices of Full-length fine-tuning v.s. PoSE fine-tuning for extending the context window size from 2,048 to 8,192."

Description: schematic comparing direct 8192-token full-length training vs 2048-token PoSE training with chunked position-index skips.
- Key elements: top row full-length contiguous indices `0..8191`; bottom rows PoSE examples with two chunks and skip offsets.
- Notable patterns: PoSE examples cover non-contiguous target positions while preserving contiguous indices inside each chunk.
- Supports claim: PoSE can expose the model to long-range positions without full-length training inputs.
