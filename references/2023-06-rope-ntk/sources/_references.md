# References

## Cited works

- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* The original RoPE paper that defines the rotary position encoding that NTK-aware scaling modifies. Explicitly cited in source 06 (historical timeline); discussed by name ("RoPE", "standard RoPE") throughout sources 01, 02, 03.

- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* Position Interpolation (PI), the direct predecessor that NTK-aware scaling improves upon. PI uniformly scales position indices; NTK-aware instead scales the base frequency. Explicitly cited in sources 01, 06; discussed as "PI" / "Position Interpolation" / "linear interpolation" in sources 02, 03, 04.

- **Peng et al. (2023/2024)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* The formal paper (ICLR 2024) that incorporates NTK-aware scaling (Definition 1), NTK-by-parts, and temperature scaling. bloc97 (Bowen Peng) is first author. Cited in sources 00, 02 (as arXiv:2309.00071), 06.

- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* The base model architecture on which NTK-aware scaling was demonstrated. Discussed by product name ("LLaMA") in sources 01, 03, 04, 05 but not formally cited by author.

- **Rozière et al. (2023)** -- *Code Llama: Open Foundation Models for Code.* Meta's code model that adopted NTK-aware/dynamic NTK scaling. Referenced by product name ("Code Llama") in source 01 as evidence of industrial adoption.

- **Bai et al. (2023)** -- *Qwen Technical Report.* Alibaba's model series that adopted Dynamic NTK-aware scaling for context extension. Referenced by product name ("Qwen") in sources 04, 06.
