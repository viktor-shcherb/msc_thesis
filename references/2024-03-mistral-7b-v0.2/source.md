# Mistral 7B v0.2

**Authors:** Mistral AI (no individual authors credited for this release)
**Affiliation:** Mistral AI, Paris, France

## Publication Status

- **arXiv preprint:** None (model weights release only)
- **Peer-reviewed:** No
- **Conference/Journal:** None
- **Status:** Informal community contribution (model weight release with no accompanying paper)

Mistral 7B v0.2 is an updated version of the Mistral 7B base model, released as model weights on Hugging Face without a separate technical report. The instruction-tuned variant (Mistral-7B-Instruct-v0.2) was first released on December 11, 2023, alongside the "La Plateforme" announcement. The base model weights (Mistral-7B-v0.2) were released on March 23, 2024 at the Mistral AI hackathon in San Francisco (hosted at SHACK15).

The key architectural changes from v0.1 are:
- Context window expanded from 8K to 32K tokens
- RoPE theta increased to 1,000,000 (from 10,000 in v0.1)
- Sliding window attention removed (v0.1 used a 4,096-token sliding window)

All other architectural details (7.3B parameters, grouped-query attention, byte-fallback BPE tokenizer) remain unchanged from the original Mistral 7B described in arXiv:2310.06825.

## Preferred Citation

Cite the original Mistral 7B paper and note the v0.2 model release:

> Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D. S., de las Casas, D., ... & El Sayed, W. (2023). Mistral 7B. arXiv:2310.06825.

For the v0.2 base model specifically, reference the Hugging Face model card:

> Mistral AI. (2024). Mistral-7B-v0.2. Hugging Face model release. https://huggingface.co/mistral-community/Mistral-7B-v0.2

## Notes

- The Mistral-7B-Instruct-v0.2 (instruction-tuned) was released three months before the base model weights were made public.
- The base model weights were originally hosted at `https://models.mistralcdn.com/mistral-7b-v0-2/mistral-7B-v0.2.tar` and later converted to Hugging Face format by the community (`mistral-community/Mistral-7B-v0.2`).
- No official `mistralai/Mistral-7B-v0.2` repository exists on Hugging Face; only the instruct variant (`mistralai/Mistral-7B-Instruct-v0.2`) is hosted under the official organization.

## Links

- Original paper (Mistral 7B v0.1): https://arxiv.org/abs/2310.06825
- Model (Instruct v0.2): https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2
- Model (Base v0.2, community conversion): https://huggingface.co/mistral-community/Mistral-7B-v0.2
- Blog post (La Plateforme, December 2023): https://mistral.ai/news/la-plateforme
- Announcement tweet (March 2024 base release): https://x.com/MistralAILabs/status/1771670765521281370
- Code: https://github.com/mistralai/mistral-src
