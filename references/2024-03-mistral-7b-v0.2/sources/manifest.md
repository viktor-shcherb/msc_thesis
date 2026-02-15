# Source Manifest

## Sources

### 1. Hugging Face Model Card — Mistral-7B-Instruct-v0.2
- **URL:** https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2
- **Type:** documentation
- **Extract:** Model specifications (32K context, RoPE theta=1e6, no sliding window), performance claims (MT-Bench 7.6), architecture details, intended use, and license (Apache 2.0)
- **Priority:** primary

### 2. Hugging Face Model Card — Mistral-7B-v0.2 (community conversion)
- **URL:** https://huggingface.co/mistral-community/Mistral-7B-v0.2
- **Type:** documentation
- **Extract:** Base model weight availability, conversion process from original Mistral CDN weights, community adoption metrics
- **Priority:** primary

### 3. Mistral AI Blog — La Plateforme (December 11, 2023)
- **URL:** https://mistral.ai/news/la-plateforme
- **Type:** blog-post
- **Extract:** Initial announcement of Mistral-7B-Instruct-v0.2 alongside the La Plateforme API service; context for the December 2023 instruct model release
- **Priority:** primary

### 4. Mistral AI Labs Tweet — Mistral 7B v0.2 Base Release (March 23, 2024)
- **URL:** https://x.com/MistralAILabs/status/1771670765521281370
- **Type:** other
- **Extract:** Official announcement of the base model release with explicit specification list (32K context, RoPE theta=1e6, no sliding window); links to fine-tuning guide
- **Priority:** primary

### 5. Mistral AI Blog — Announcing Mistral 7B (September 2023)
- **URL:** https://mistral.ai/news/announcing-mistral-7b
- **Type:** blog-post
- **Extract:** Original Mistral 7B v0.1 specifications for comparison; sliding window attention details (4,096 tokens), original 8K context, RoPE theta=10,000
- **Priority:** supplementary

### 6. Original Mistral 7B Paper — arXiv:2310.06825
- **URL:** https://arxiv.org/abs/2310.06825
- **Type:** other
- **Extract:** Full technical details of the Mistral 7B architecture shared between v0.1 and v0.2 (GQA, SwiGLU, byte-fallback BPE tokenizer, 7.3B parameters, 32 layers, 4096 hidden dim); benchmark results for v0.1 baseline
- **Priority:** supplementary

### 7. Hacker News Discussion — Mistral AI Announce 7B v0.2 Base Model Release
- **URL:** https://news.ycombinator.com/item?id=39802932
- **Type:** other
- **Extract:** Community discussion on the March 2024 base model release; context on why base weights were released three months after the instruct variant
- **Priority:** supplementary
