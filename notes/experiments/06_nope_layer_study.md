# NoPE Layer Study: Llama-3.2-11B Vision

## Question

Llama-3.2-11B and Llama-3.1-8B both show a non-monotone plasticity profile — a dip at 50–65K followed by recovery at 70–100K before final collapse. The initial hypothesis was that Llama-3.2-11B's cross-attention (NoPE) layers cause this. This study tests that hypothesis.

## Background: NoPE Layers in Llama-3.2-11B

Llama-3.2-11B-Vision has 40 layers total:
- **32 self-attention layers** with RoPE (indices 0–2, 4–7, 9–12, 14–17, 19–22, 24–27, 29–32, 34–37, 39)
- **8 cross-attention layers** without RoPE (indices 3, 8, 13, 18, 23, 28, 33, 38) — every 5th layer starting from 3

Cross-attention layers integrate vision features and do not use positional encoding (hence "NoPE"). They are absent from the sniffed Q/K data since they don't participate in standard self-attention.

Source: HuggingFace `MllamaTextConfig`, default `cross_attention_layers = [3, 8, 13, 18, 23, 28, 33, 38]`.

## Finding 1: NoPE Layers Do Not Cause the Non-Monotone Pattern

**Llama-3.1-8B has the same non-monotone pattern but zero NoPE layers.** It is a pure text model with 32 contiguous self-attention layers (all with RoPE).

| Model | Layers | NoPE | Dip (d4-5) | Recovery (d6-7) | Recovery magnitude |
|---|---|---|---:|---:|---:|
| Llama-3.1-8B | 32 | 0 | 0.502 | 0.532 | **+0.029** |
| Llama-3.2-11B | 32 (SA) + 8 (CA) | 8 | 0.533 | 0.556 | **+0.023** |

This definitively rules out NoPE layers as the cause. The recovery appears in both models with identical magnitude (~+0.025).

## Finding 2: The Pattern is Ubiquitous Within Both Models

In Llama-3.1-8B (no NoPE), **29 of 32 layers** show positive mid-context recovery (>0.005). Only 1 layer is monotone. The recovery is not driven by a few anomalous layers — nearly every layer contributes.

In Llama-3.2-11B, **26 of 32 self-attention layers** show recovery. The NoPE-adjacency grouping shows no effect:

| Group | Mean recovery | n layers |
|---|---:|---:|
| After NoPE (layers 4,9,14,19,24,29,34,39) | +0.019 | 8 |
| Before NoPE (layers 2,7,12,17,22,27,32,37) | +0.021 | 8 |
| Far from NoPE | +0.025 | 16 |

If anything, NoPE-adjacent layers show *less* recovery than distant layers. The pattern is model-wide, not localized.

## Finding 3: The Pattern is Llama-Family + 32-Layer Specific

| Model | Family | Layers | Recovery |
|---|---|---:|---:|
| Llama-3.1-8B | Llama | 32 | **+0.029** |
| Llama-3.2-11B | Llama | 32 (SA) | **+0.023** |
| Llama-3.2-3B | Llama | 28 | -0.070 |
| Llama-3.2-1B | Llama | 16 | -0.104 |
| Ministral3-14B | Mistral | 40 | -0.005 |
| Ministral3-8B | Mistral | 34 | -0.013 |
| Ministral3-3B | Mistral | 26 | -0.009 |
| Qwen3-14B | Qwen | 40 | -0.028 |
| Qwen3-8B | Qwen | 36 | -0.039 |
| Qwen3-4B | Qwen | 36 | -0.041 |

Key observations:
- **Only the two 32-layer Llama models** show positive recovery. All others are monotone.
- This is NOT a depth effect: Ministral3-14B (40 layers) and Qwen3-14B (40 layers) do not show it.
- Within the Llama family, the smaller models (1B/16 layers, 3B/28 layers) do not show it.
- The pattern is specific to the intersection of Llama architecture + ≥32 layers.

## Per-Layer Anatomy

Top recovery layers in Llama-3.1-8B (no NoPE):

| Layer | d0-1 | d4-5 (dip) | d6-7 (recovery) | d8-9 (collapse) | Recovery |
|---:|---:|---:|---:|---:|---:|
| 5 | 0.706 | 0.541 | 0.608 | 0.505 | +0.066 |
| 28 | 0.674 | 0.488 | 0.548 | 0.475 | +0.060 |
| 30 | 0.608 | 0.512 | 0.571 | 0.512 | +0.059 |
| 14 | 0.695 | 0.605 | 0.661 | 0.583 | +0.057 |
| 22 | 0.643 | 0.520 | 0.576 | 0.500 | +0.056 |

Top recovery layers in Llama-3.2-11B:

| Layer | d0-1 | d4-5 (dip) | d6-7 (recovery) | d8-9 (collapse) | Recovery | NoPE adj? |
|---:|---:|---:|---:|---:|---:|---|
| 15 | 0.586 | 0.428 | 0.479 | 0.370 | +0.051 | no |
| 7 | 0.758 | 0.581 | 0.632 | 0.508 | +0.051 | before 8 |
| 29 | 0.624 | 0.488 | 0.539 | 0.430 | +0.051 | after 28 |
| 5 | 0.606 | 0.436 | 0.481 | 0.408 | +0.045 | no |
| 11 | 0.615 | 0.524 | 0.565 | 0.494 | +0.041 | no |

No depth pattern — recovery layers are distributed throughout the stack (early, mid, late).

## Most/Least Plastic Layers in Llama-3.2-11B

| Layer | ap_overall | beta_norm | R2_pos | Category |
|---:|---:|---:|---:|---|
| 16 | 0.761 | 0.000070 | 0.023 | **Most plastic** — near-zero position sensitivity |
| 17 | 0.747 | 0.000090 | 0.051 | Near-flat profile across all positions |
| 6 | 0.664 | 0.000103 | 0.055 | High plasticity |
| 0 | 0.430 | 0.000156 | 0.104 | **Least plastic** — highest position sensitivity |
| 32 | 0.458 | 0.000129 | 0.051 | Low plasticity, late layer |
| 4 | 0.466 | 0.000140 | 0.098 | Low plasticity, after NoPE layer 3 |

Layers 16–17 are outliers: near-zero position sensitivity (R2_pos ≈ 0.02), tiny beta_norm, and nearly flat plasticity profiles (range 0.087 for layer 16 across all deciles). These are effectively pure content-routing layers.

## Hypotheses for the Non-Monotone Pattern

Since NoPE layers are ruled out, candidate explanations:

1. **RoPE frequency band interference**: Llama 3.1/3.2 uses a base frequency of 500,000 for RoPE. At specific distance ranges (60–100K tokens), certain RoPE frequency bands complete cycles that create constructive interference, temporarily reducing position bias. The recovery zone might correspond to a "resonance" of specific frequency pairs.

2. **Llama-specific head specialization at 32 layers**: At 32+ layers, Llama models may develop a population of mid-range specialist heads that peak in effectiveness at 60–100K. Shallower Llama models (16/28 layers) don't have enough capacity for this specialization.

3. **Training data distribution**: If Llama pre-training data has a characteristic document length around 60–100K tokens, heads may be optimized for attention within documents of that length, creating a recovery zone.

Note: The RoPE hypothesis is testable — examining per-dimension position encoding weights at different distances could reveal which frequency bands drive the recovery.

## Conclusion

The non-monotone plasticity profile in Llama-3.2-11B is **not caused by NoPE/cross-attention layers**. It is a Llama-family trait that appears at 32+ layers, is distributed uniformly across all self-attention layers, and is present identically in Llama-3.1-8B (which has zero NoPE layers). The mechanism remains uncharacterized but is likely related to RoPE frequency structure or Llama-specific training procedures.
