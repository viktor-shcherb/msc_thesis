# Source Manifest

## Sources

### 1. Original NTK-Aware Scaled RoPE Reddit post
- **URL:** https://www.reddit.com/r/LocalLLaMA/comments/14lz7j5/ntkaware_scaled_rope_allows_llama_models_to_have/
- **Type:** reddit-thread
- **Extract:** Full post text including mathematical derivation of NTK-aware scaling, the key insight about high-frequency vs low-frequency components, the alpha parameter, code modifications, perplexity results, and community discussion in comments
- **Priority:** primary

### 2. EleutherAI blog post "Extending the RoPE"
- **URL:** https://blog.eleuther.ai/yarn/
- **Type:** blog-post
- **Extract:** Mathematical formulation of NTK-aware interpolation (b' = b * s^(|D|/(|D|-2))), comparison with linear interpolation (PI), perplexity results with and without fine-tuning, explanation of why uniform frequency scaling is suboptimal from NTK theory perspective
- **Priority:** primary

### 3. NTK-by-parts interpolation PR
- **URL:** https://github.com/jquesnelle/scaled-rope/pull/1
- **Type:** github-repo
- **Extract:** Technical details of NTK-by-parts correction: how different frequency components get different scaling, the scale parameter replacing alpha, implementation details, and the unification of extrapolation/NTK-aware/linear interpolation as special cases
- **Priority:** primary

### 4. Dynamic NTK Reddit post (emozilla)
- **URL:** https://www.reddit.com/r/LocalLLaMA/comments/14mrgpr/dynamically_scaled_rope_further_increases/
- **Type:** reddit-thread
- **Extract:** Dynamic scaling approach where alpha adjusts based on sequence length, perplexity comparisons with static NTK-aware, adoption in Qwen and other models
- **Priority:** supplementary

### 5. HuggingFace text-generation-inference issue #512
- **URL:** https://github.com/huggingface/text-generation-inference/issues/512
- **Type:** github-repo
- **Extract:** Technical discussion of implementing NTK-aware RoPE in production, any additional implementation details or results shared
- **Priority:** supplementary

### 6. Aman Arora deep dive on RoPE context extension
- **URL:** https://amaarora.github.io/posts/2025-09-21-rope-context-extension.html
- **Type:** blog-post
- **Extract:** Technical explanation of NTK-aware scaling derivation, comparison with PI and other methods, visual illustrations of frequency scaling behavior
- **Priority:** supplementary
