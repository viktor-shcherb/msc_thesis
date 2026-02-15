# References

## Cited works

### Mistral 7B Paper (arXiv:2310.06825)

**Jiang et al. (2023)** — *Mistral 7B.*

Referenced throughout as the foundational technical paper describing the architecture shared between v0.1 and v0.2. The paper details grouped-query attention (GQA), sliding window attention (SWA), and the original model's performance benchmarks. Cited in HuggingFace model cards as the primary source for architectural specifications.

### Llama 2 and Llama 1 Models

**Meta AI (2023, 2022)** — *Llama 2 13B and Llama 1 34B models.*

Used as comparison baselines in the original Mistral 7B announcement. The v0.1 blog post states that Mistral 7B "outperforms Llama 2 13B on all benchmarks" and "outperforms Llama 1 34B on many benchmarks," with performance on reasoning, comprehension, and STEM tasks equivalent to "a Llama 2 model more than 3x its size."

### MT-Bench Evaluation Framework

**Zheng et al. (2023)** — *MT-Bench: Multi-turn conversation benchmark.*

Used as the primary evaluation metric for the instruction-tuned variant. La Plateforme blog reports Mistral-7B-Instruct-v0.2 achieves a score of 7.6 on MT-Bench, compared to 8.3 for Mixtral 8x7B (mistral-small) and 8.6 for mistral-medium.

### Mixtral 8x7B

**Mistral AI (2023)** — *Mixtral 8x7B mixture-of-experts model.*

Mentioned in the La Plateforme blog as the model serving the mistral-small endpoint (MT-Bench score 8.3). Also referenced in the Hacker News discussion where community members questioned why Mistral released a non-MoE model given Mixtral's success.

### FlashAttention and xFormers

**Dao et al. (2022), Meta AI** — *FlashAttention and xFormers optimization libraries.*

Mentioned in the original Mistral 7B blog post as optimization techniques that enable 2x speed improvement for 16k sequence length with 4k sliding window in the v0.1 model.
