# NTK-Aware Scaled RoPE Reddit Post [https://www.reddit.com/r/LocalLLaMA/comments/14lz7j5/ntkaware_scaled_rope_allows_llama_models_to_have/]

**Type:** reddit-thread
**Fetched:** 2026-02-08
**Priority:** primary

Note: Reddit is not directly fetchable. Content reconstructed from multiple secondary sources that quote and describe the original post (EleutherAI blog, HuggingFace issues, x-transformers issue #171, Aman Arora deep dive, YaRN paper).

## Post Title

"NTK-Aware Scaled RoPE allows LLaMA models to have extended (8k+) context size without any fine-tuning and minimal perplexity degradation"

## Author

Reddit user u/bloc97 (later identified as Bowen Peng, first author of the YaRN paper)

## Date

Posted approximately June 28-29, 2023 on r/LocalLLaMA

## Core Insight

The post observed that Position Interpolation (PI) by Chen et al. (2023) scales all RoPE frequency dimensions uniformly by a factor `1/s`, where `s = L'/L` is the ratio of extended context length to original context length. Inspired by Neural Tangent Kernel (NTK) theory, bloc97 recognized that:

> Deep neural networks have trouble learning high-frequency information if the input dimension is low without the corresponding embeddings having high-frequency components.

Uniformly compressing all frequencies "may prevent the model from learning high-frequency features." The fix: scale high frequencies less and low frequencies more, spreading the interpolation pressure across multiple dimensions.

## Method: Modifying the Base Frequency

Instead of scaling position indices (as PI does), NTK-aware scaling modifies the base frequency parameter of RoPE. Standard RoPE uses:

> `theta_d = base^(-2d/|D|)` where `base = 10000`

NTK-aware scaling replaces `base` with a scaled base `b'`:

> `b' = b * s^(|D|/(|D|-2))`

where:
- `b` is the original base (10000)
- `s = L'/L` is the scaling factor
- `|D|` is the embedding dimension

This is equivalent to setting `g(m) = m` and `h(theta_d) = b'^(-2d/|D|)` in the general RoPE modification framework.

## Alpha Parameter

The post introduced an alpha parameter (`alpha`) controlling the degree of context extension. With `alpha = 8`, the method extends context 8x (e.g., from 2048 to 16384+). The perplexity comparison showed NTK-aware scaling (alpha=8) maintaining much lower perplexity than Position Interpolation on longer sequences without any fine-tuning.

## Implementation

The post claimed only **3 lines of code** need to change in the RoPE implementation. The modification replaces the fixed `base = 10000` with the scaled base `b'`.

## Perplexity Results

From secondary sources describing the post's perplexity plots:
- **Without fine-tuning:** NTK-aware scaling shows better (lower) perplexity than PI on longer sequences
- The post included a plot comparing:
  - Gray baseline (scale=1, original model)
  - Blue dashed line: linear interpolation / Position Interpolation (scale=4)
  - Green solid line: NTK-aware scaling (alpha=8)
- NTK-aware maintained substantially lower perplexity across extended context lengths

## Community Impact

The post generated significant community engagement on r/LocalLLaMA:
- Rapidly adopted by open-source LLM community
- Integrated into HuggingFace Transformers (PR #24653), llama.cpp, text-generation-inference, vLLM, and exllama
- Referenced in Meta's Code Llama and Alibaba's Qwen technical reports
- Spawned follow-up contributions: Dynamic NTK (emozilla), NTK-by-parts (bloc97)
