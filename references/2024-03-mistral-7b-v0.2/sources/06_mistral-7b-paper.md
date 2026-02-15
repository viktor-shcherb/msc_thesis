# Original Mistral 7B Paper — arXiv:2310.06825

**URL:** https://arxiv.org/abs/2310.06825
**Type:** other
**Fetched:** 2026-02-15
**Priority:** supplementary

## Purpose

This paper provides the full technical details of the Mistral 7B architecture that is shared between v0.1 and v0.2, with only the context extension mechanisms differing between versions.

## Model Size

**7 billion parameters** (referred to as 7.3B parameters in other sources)

## Key Architectural Features

The paper describes two main architectural innovations:

### 1. Grouped-Query Attention (GQA)

> "Grouped-query attention (GQA) for faster inference"

This feature is retained in both v0.1 and v0.2.

### 2. Sliding Window Attention (SWA)

> "Sliding window attention (SWA) to effectively handle sequences of arbitrary length with reduced inference cost"

This feature was present in v0.1 but removed in v0.2.

## Performance Context

The abstract states that Mistral 7B:

> "outperforms Llama 2 13B across all evaluated benchmarks, and Llama 1 34B in reasoning, mathematics, and code generation."

For the instruction-tuned variant:

> "surpasses the Llama 2 13B -- Chat model both on human and automated benchmarks."

## Architectural Details Not in Abstract

The arXiv abstract page does not include the following detailed specifications (which are documented in the full paper PDF and confirmed by other sources in this reference set):
- Specific layer count: 32 layers (per full paper / other sources)
- Hidden dimension: 4096 (per full paper / other sources)
- Activation function: SwiGLU (per full paper / other sources)
- Tokenizer: byte-fallback BPE (per full paper / other sources)
- Detailed benchmark comparison tables

## Publication Details

- **arXiv ID**: 2310.06825
- **Publication Date**: October 10, 2023
- **Paper URL**: https://arxiv.org/abs/2310.06825

## Architecture Shared Between v0.1 and v0.2

*Note: The following details are compiled from the full paper and cross-referenced with other sources in this reference set (see `05_announcing-mistral-7b-blog.md`). They are not available on the arXiv abstract page alone.*

All core architectural components remain unchanged between v0.1 and v0.2:
- 7.3B parameters
- Grouped-query attention (GQA)
- SwiGLU activation
- Byte-fallback BPE tokenizer
- 32 layers
- 4096 hidden dimensions

The only changes in v0.2 are related to context extension:
- Sliding window attention removed
- RoPE theta increased from 10,000 to 1,000,000
- Context window expanded from 8K to 32K tokens
