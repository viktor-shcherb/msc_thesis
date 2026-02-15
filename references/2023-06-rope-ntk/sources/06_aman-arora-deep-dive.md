# How LLMs Scaled from 512 to 2M Context: A Technical Deep Dive [https://amaarora.github.io/posts/2025-09-21-rope-context-extension.html]

**Type:** blog-post
**Fetched:** 2026-02-08
**Priority:** supplementary

## Overview

Aman Arora's technical deep dive places NTK-aware scaling within the broader history of RoPE context extension methods, from original RoPE through PI, NTK-aware, dynamic NTK, NTK-by-parts, and YaRN.

## NTK-Aware Scaling Explanation

### Core Formula

The NTK-aware scaling adjusts the base frequency parameter. The blog presents this as:

> `theta_d = base * alpha^(2d/d_model)`

where alpha is a scaling factor that adapts to the target context length. Note: this is the blog's own notation for how the scaled base modifies per-dimension frequencies. The equivalent formulation from the EleutherAI blog uses `b' = b * s^(|D|/(|D|-2))` with `theta_d = b'^(-2d/|D|)`, where the negative exponent reflects that higher dimensions have lower frequencies in standard RoPE convention.

### Key Principle

Rather than uniformly interpolating positions (as PI does), NTK-aware scaling recognizes that different frequency dimensions should scale differently:

> "The problem with linear interpolation" is that it treats all frequencies equally, but lower-frequency dimensions encode long-range position information that shouldn't be compressed as aggressively.

### NTK Theory Connection

The NTK theory insight is that frequency-based scaling aligns with how neural networks process positional information at different scales:
- Higher frequencies capture local structure
- Lower frequencies handle global context

## Dynamic NTK Coverage

The blog emphasizes that dynamic NTK "adapts to sequence length" rather than committing to a single context extension factor. This eliminates the need to choose between short and long sequence performance.

## NTK-By-Parts Strategy

The blog describes the three-regime approach:
1. **High-frequency dimensions** (short wavelengths): Extrapolation -- keep original RoPE frequencies unchanged
2. **Mid-frequency dimensions**: Smooth interpolation between the two extremes
3. **Low-frequency dimensions** (long wavelengths): Interpolation -- apply PI-like position compression

The blog notes:

> "The multi-scale problem" acknowledges that no single strategy works optimally across all frequency bands simultaneously.

## Production Adoption

The blog notes:

> "Most modern LLMs today such as Qwen, DeepSeek, LLaMA, gpt-oss are finetuned using YaRN to enable context length expansion only utilising a small percentage of the pre-trained dataset."

This indicates NTK-aware approaches (via YaRN) form the foundation for current production context extension systems.

## Historical Context

The blog traces the evolution:
1. RoPE (Su et al., 2021) -- original positional encoding
2. Position Interpolation (Chen et al., 2023) -- uniform scaling via position compression
3. NTK-Aware Scaling (bloc97, June 2023) -- frequency-aware nonuniform scaling
4. Dynamic NTK (emozilla, June 2023) -- sequence-length-adaptive scaling
5. NTK-by-parts (bloc97, July 2023) -- piecewise frequency-dependent scaling
6. YaRN (Peng et al., 2023/ICLR 2024) -- formalization combining all above with temperature scaling
