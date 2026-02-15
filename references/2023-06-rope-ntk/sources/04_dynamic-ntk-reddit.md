# Dynamic NTK Reddit Post (emozilla) [https://www.reddit.com/r/LocalLLaMA/comments/14mrgpr/dynamically_scaled_rope_further_increases/]

**Type:** reddit-thread
**Fetched:** 2026-02-08
**Priority:** supplementary

Note: Reddit is not directly fetchable. Content reconstructed from secondary sources (EleutherAI blog, Aman Arora deep dive, YaRN paper, HuggingFace discussions).

## Post Title

"Dynamically Scaled RoPE further increases performance of long context LLaMA with zero fine-tuning"

## Author

Reddit user u/emozilla

## Date

Approximately June 29, 2023 (shortly after bloc97's original NTK-aware post)

## Core Idea

Dynamic NTK addresses a key limitation of static NTK-aware scaling: the fixed alpha parameter means the model either scales well for long sequences or short sequences, but not both simultaneously. emozilla proposed adjusting the scaling factor dynamically based on the actual sequence length at inference time.

## Dynamic Scaling Formula

The dynamic scaling adjusts alpha based on current sequence length:

> `s = l'/L` if `l'/L > 1`, else `1`

where:
- `l'` is the current sequence length being processed
- `L` is the original model context length (e.g., 2048 for LLaMA)

From the Aman Arora deep dive, the scaling formula is described as:

> "set scale to original model context length / current sequence length" with adjustment: "scaling of alpha is set to (alpha * current sequence length / original model context length) - (alpha - 1)"

## Key Advantage

Dynamic NTK eliminates the tradeoff between short and long sequence performance. The model automatically adapts scaling to whatever sequence length it needs to process.

## Performance

From EleutherAI blog:

> "dynamic NTK interpolation works exceptionally well on models pretrained on L without any finetuning"

This makes dynamic NTK particularly attractive for inference-time context extension where no fine-tuning budget is available.

## Adoption

Dynamic NTK-aware scaling was adopted in production by:
- **Qwen models** (Alibaba): Use dynamic NTK-aware scaling for context extension
- **HuggingFace Transformers**: Supported as a `rope_scaling` type option
- Various open-source inference frameworks (llama.cpp, vLLM)

## Relationship to Other Methods

Dynamic NTK combines with the NTK-aware base frequency scaling from bloc97's original contribution. The "dynamic" aspect is an inference-time wrapper that can be applied to any static scaling method. In the YaRN paper taxonomy, Dynamic NTK is referenced as a precursor approach that YaRN improves upon.
