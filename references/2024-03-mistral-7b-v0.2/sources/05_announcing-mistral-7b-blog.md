# Mistral AI Blog — Announcing Mistral 7B (September 2023)

**URL:** https://mistral.ai/news/announcing-mistral-7b
**Type:** blog-post
**Fetched:** 2026-02-15
**Priority:** supplementary

## Purpose

This blog post announces the original Mistral 7B v0.1 model and provides baseline specifications for comparison with v0.2.

## Model Parameters

- **Size**: 7.3B parameters
- **License**: Apache 2.0 (unrestricted use)

## Architecture Details — v0.1

### Sliding Window Attention (SWA)

The key architectural feature of v0.1 that was removed in v0.2:

> "Sliding Window Attention (SWA)": Each layer attends to the previous 4,096 hidden states

The blog explains the mechanism:

> "a token `i` at layer `k` attends to tokens `[i-sliding_window, i]` at layer `k-1`"

### Grouped-Query Attention (GQA)

- **Grouped-query attention (GQA)**: Enables faster inference

This feature was retained in v0.2.

### Memory Efficiency

The sliding window attention in v0.1 provided:
- Fixed attention span allows cache limitation to 4,096 tokens using rotating buffers
- Achieves 50% cache memory savings for 8,192-token sequences without quality degradation
- Linear compute cost of O(sliding_window.seq_len)

## Performance Metrics — v0.1

### Benchmark Performance

The blog states the model:

> "outperforms Llama 2 13B on all benchmarks"

> "outperforms Llama 1 34B on many benchmarks"

On reasoning, comprehension, and STEM tasks, Mistral 7B performs equivalently to a Llama 2 model:

> "more than 3x its size"

### Inference Speed

- 2x speed improvement for 16k sequence length with 4k window (with FlashAttention/xFormers optimizations)

### Chat Fine-tuning

> Mistral 7B Instruct outperforms all 7B models on MT-Bench and matches 13B chat model performance

## Comparison: v0.1 vs v0.2

**v0.1 specifications (from this blog):**
- Context window: 8K tokens (implied from sliding window and memory efficiency discussion)
- Sliding window attention: 4,096 tokens
- RoPE theta: 10,000 (standard value, not explicitly stated in blog)

**v0.2 changes:**
- Context window: Expanded to 32K tokens (4x increase)
- Sliding window attention: Removed
- RoPE theta: Increased to 1,000,000
