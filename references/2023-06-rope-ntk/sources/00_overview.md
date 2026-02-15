# NTK-Aware Scaled RoPE

**Author(s):** bloc97 (Bowen Peng)
**Type:** Community contribution (Reddit post + GitHub PR)
**Date:** June 2023
**Primary URL:** https://www.reddit.com/r/LocalLLaMA/comments/14lz7j5/ntkaware_scaled_rope_allows_llama_models_to_have/

## Summary

NTK-Aware Scaled RoPE is a method for extending the context window of RoPE-based large language models (e.g., LLaMA) without fine-tuning. The key insight, inspired by Neural Tangent Kernel (NTK) theory, is that instead of uniformly scaling all RoPE frequency dimensions (as in Position Interpolation), one should scale high frequencies less and low frequencies more. This is achieved by modifying the base frequency parameter rather than the position indices, requiring only a 3-line code change. The method was later extended by the same author into "NTK-by-parts" interpolation and formalized in the YaRN paper (Peng et al., ICLR 2024).

## Source structure

1. **Original Reddit post** (primary) -- The founding contribution: NTK-aware scaling idea, alpha parameter, perplexity results, 3-line code change
2. **EleutherAI blog post** (primary) -- Mathematical formulation with equations, comparison with PI, NTK-by-parts and dynamic NTK explanations
3. **NTK-by-parts GitHub PR** (primary) -- Follow-up improvement: piecewise frequency-dependent scaling, parameter simplification, implementation
4. **Dynamic NTK Reddit post** (supplementary) -- emozilla's dynamic scaling variant where alpha adjusts based on sequence length
5. **HuggingFace TGI issue #512** (supplementary) -- Production implementation discussion, integration into HuggingFace ecosystem
6. **Aman Arora deep dive** (supplementary) -- Technical explanation and context within the broader RoPE extension landscape
