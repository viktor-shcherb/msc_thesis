# NTK-Aware "By Parts" Interpolation Correction - PR #1 [https://github.com/jquesnelle/scaled-rope/pull/1]

**Type:** github-repo
**Fetched:** 2026-02-08
**Priority:** primary

## PR Metadata

- **Author:** bloc97
- **Repository:** jquesnelle/yarn (originally jquesnelle/scaled-rope)
- **Created:** July 7, 2023
- **Merged:** July 9, 2023
- **Commits:** 2 (1f8d29c: initial implementation, 8129a54: added original_max_position_embeddings parameter)

## Description

This PR introduces an improved RoPE scaling method that addresses limitations in both linear interpolation (PI) and the original NTK-aware approach. The method applies different interpolation strategies to different frequency bands of RoPE.

## Four Key Improvements

### 1. Performance Gains
Reduces perplexity across all context lengths on non-finetuned models. Improvements are especially pronounced at higher context sizes with lower alpha values.

### 2. Parameter Simplification
Eliminates the alpha parameter that "inconsistently predicted effective context length across models." Replaces it with an intuitive `scale` parameter matching linear interpolation conventions (e.g., `scale=2` extends 2048 context to 4096).

### 3. Extrapolation Stabilization
Fixes the extrapolation regime that previously broke fine-tunes when alpha was suboptimally set, enabling easier fine-tuning without parameter search.

### 4. Method Generalization
Encompasses extrapolation, NTK-aware, and linear interpolation as special cases. Setting `ntk_factor` and `extrapolation_factor` to zero produces results "identical to linear interpolation."

## Implementation Parameters

- **`scale`**: Used identically to linear interpolation. `scale=2` extends 2048 base context to 4096.
- **`extrapolation_factor`**: For validation purposes only; leave unchanged unless necessary.
- **`ntk_factor`**: For validation purposes only; leave unchanged unless necessary.
- **`original_max_position_embeddings`**: Denotes the pretrained model's original context size (2048 for LLaMA). Critical: "max_position_embeddings is assumed to be the original pretrained model context size" to avoid breaking functionality.

## New File

Added `LlamaPartNTKScaledRotaryEmbedding.py` implementing the piecewise NTK-aware scaling.

## Technical Approach

The method divides RoPE frequency dimensions into three regimes:
1. **High-frequency dimensions** (short wavelengths): extrapolation regime -- keep original RoPE frequencies unchanged
2. **Low-frequency dimensions** (long wavelengths): interpolation regime -- apply PI-like scaling
3. **Intermediate dimensions**: smooth transition between the two regimes

This piecewise approach captures the best of both methods:
- High-frequency components preserve local positional information (extrapolation benefits)
- Low-frequency components properly scale for longer contexts (interpolation benefits)

## Downstream Impact

The PR was merged and subsequently influenced:
- HuggingFace Transformers (rope_scaling support)
- llama.cpp
- exllama
- Other major LLM frameworks adopting rope scaling improvements
