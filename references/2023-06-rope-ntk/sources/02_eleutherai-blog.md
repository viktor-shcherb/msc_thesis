# Extending the RoPE - EleutherAI Blog [https://blog.eleuther.ai/yarn/]

**Type:** blog-post
**Fetched:** 2026-02-08
**Priority:** primary

## Overview

EleutherAI's blog post provides a detailed mathematical treatment of RoPE scaling methods including NTK-aware interpolation. The post frames the methods using a general modification framework and provides formal definitions.

## General RoPE Modification Framework

All RoPE extension methods can be expressed through a general framework:

> `f'_W(x_m, m, theta_d) = f_W(x_m, g(m), h(theta_d))`

where `g(m)` modifies positions and `h(theta_d)` modifies frequency components.

## Position Interpolation (PI) Definition

PI uses:
- `g(m) = m/s` (positions are compressed by scale factor)
- `h(theta_d) = theta_d` (frequencies unchanged)

where `s = L'/L` is the ratio of new context length to original.

## NTK-Aware Interpolation Definition

NTK-aware uses:
- `g(m) = m` (positions unchanged)
- `h(theta_d) = b'^(-2d/|D|)` (frequencies modified via base scaling)

with the scaled base:

> `b' = b * s^(|D|/(|D|-2))`

## NTK Theory Motivation

The blog explains the NTK theory connection:

> "deep neural networks have trouble learning high-frequency information if the input dimension is low without the corresponding embeddings having high-frequency components"

Position Interpolation uniformly reduces all frequencies by `1/s`, which:

> "may prevent the model from learning high-frequency features"

NTK-aware interpolation addresses this by:

> "spread[ing] interpolation pressure across multiple dimensions by scaling high frequencies less and low frequencies more"

## Performance Comparison (Without Fine-tuning vs With Fine-tuning)

Key finding from the blog:

- **Without fine-tuning:** NTK-aware shows "better (lower) perplexity than PI on longer sequences"
- **After fine-tuning:** NTK-aware interpolation "performs worse than PI after finetuning on longer context data"

This observation -- that NTK-aware is superior zero-shot but inferior after fine-tuning -- was one of the motivations for developing the NTK-by-parts hybrid approach.

## NTK-by-Parts Extension

The blog presents the NTK-by-parts hybrid approach that combines the benefits of both PI and NTK-aware scaling. The key formula:

> `h(theta_d) = (1 - gamma) * (theta_d / s) + gamma * theta_d`

where `gamma(r)` is a ramp function defined piecewise:

> `gamma(r) = 0` if `r < alpha`; `gamma(r) = 1` if `r > beta`; `gamma(r) = (r - alpha) / (beta - alpha)` otherwise

with recommended parameters `alpha = 1, beta = 32` for Llama models.

### Wavelength Concept

Wavelength at dimension `d`:

> `lambda_d = 2 * pi * b'^(2d/|D|)`

This represents the number of tokens needed for a full rotation at that frequency dimension. NTK-by-parts interpolates wavelengths from unmodified RoPE values to PI values across dimensions.

### Ramp Function Behavior

- Dimensions with short wavelengths (high frequency): `gamma -> 1` (extrapolation, keep original frequencies)
- Dimensions with long wavelengths (low frequency): `gamma -> 0` (interpolation, apply PI-like scaling)
- Intermediate dimensions: smooth transition

## Dynamic NTK

The blog describes dynamic NTK inference-time scaling:

> `s = l'/L` if `l'/L > 1`, else `1`

where `l'` is the current sequence length at inference time.

Key finding:

> "dynamic NTK interpolation works exceptionally well on models pretrained on L without any finetuning"

## Experimental Visualizations

The blog includes loss curve visualizations across 256-token sliding windows for:
- LLaMA models
- Mistral-7B fine-tunes

These show YaRN (NTK-by-parts + temperature scaling) outperforming PI and standard NTK-aware approaches across context lengths.

## Relationship to YaRN

The blog explicitly connects these community contributions to the formal YaRN paper (arXiv:2309.00071), noting that YaRN combines:
1. NTK-by-parts interpolation
2. Attention temperature scaling, with the temperature factor determined by:
   > `sqrt(1/t) = 0.1 * ln(s) + 1`
   This modifies the softmax from `softmax(q_m^T k_n / sqrt(|D|))` to `softmax(q_m^T k_n / (t * sqrt(|D|)))`.
3. Fine-tuning on extended context data

For non-Llama models, the NTK-by-parts parameters require tuning. Example: Mistral-7B (128k context) uses `a = 0.07, b = 1.0` in the parametric temperature form.
