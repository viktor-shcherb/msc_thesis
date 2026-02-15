# Mistral 7B v0.2

**Author(s):** Mistral AI (no individual authors credited)
**Type:** Model weight release
**Date:** March 2024 (base model), December 2023 (instruct model)
**Primary URL:** https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

## Summary

Mistral 7B v0.2 is an updated version of the Mistral 7B model that extends the context window from 8K to 32K tokens by increasing the RoPE theta parameter to 1,000,000 and removing the sliding window attention mechanism. Released as model weights without a technical paper, the instruction-tuned variant was released in December 2023 and the base model in March 2024.

## Source structure

This reference compiles information from multiple sources:

1. **Hugging Face Model Card (Instruct v0.2)** — Official model specifications, performance metrics, and usage documentation for the instruction-tuned variant
2. **Hugging Face Model Card (Base v0.2 community)** — Community-converted base model weights with adoption information
3. **La Plateforme Blog Post (December 2023)** — Initial announcement context for the instruct model release
4. **Mistral AI Labs Tweet (March 2024)** — Official announcement of base model release with explicit specifications
5. **Announcing Mistral 7B Blog Post (September 2023)** — Original v0.1 specifications for comparison
6. **Original Mistral 7B Paper (arXiv:2310.06825)** — Full architectural details shared between v0.1 and v0.2
7. **Hacker News Discussion** — Community context on the staggered release timeline
