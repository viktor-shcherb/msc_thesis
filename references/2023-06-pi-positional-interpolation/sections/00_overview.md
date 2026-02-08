# Overview

**Title:** Extending Context Window of Large Language Models via Position Interpolation

**Authors:** Shouyuan Chen, Sherman Wong, Liangjian Chen, Yuandong Tian

**Affiliations:**
- Shouyuan Chen — Meta Platforms Inc.
- Sherman Wong — Meta Platforms Inc.
- Liangjian Chen — Meta Platforms Inc.
- Yuandong Tian — Meta Platforms Inc.

**Venue:** arXiv preprint arXiv:2306.15595v2

**Date:** 28 Jun 2023

**Abstract:**
> "We present Position Interpolation (PI) that extends the context window sizes of RoPE-based (Su et al., 2021) pretrained LLMs such as LLaMA (Touvron et al., 2023) models to up to 32768 with minimal fine-tuning (within 1000 steps), while demonstrating strong empirical results on various tasks that require long context, including passkey retrieval, language modeling, and long document summarization from LLaMA 7B to 65B. Meanwhile, the extended model by Position Interpolation preserve quality relatively well on tasks within its original context window. To achieve this goal, Position Interpolation linearly down-scales the input position indices to match the original context window size, rather than extrapolating beyond the trained context length which may lead to catastrophically high attention scores that completely ruin the self-attention mechanism. Our theoretical study shows that the upper bound of interpolation is at least ~600x smaller than that of extrapolation, further demonstrating its stability. Models extended via Position Interpolation retain its original architecture and can reuse most pre-existing optimization and infrastructure." [p. 1]

## Section Headings

1. Introduction
2. Method
   - 2.1 Background: Rotary Position Embedding (RoPE)
   - 2.2 Direct Extrapolation
   - 2.3 Proposed Approach: Position Interpolation (PI)
3. Experiments
   - 3.1 Setup
   - 3.2 Long Sequence Language Modeling
   - 3.3 Measuring Effective Context Window Size through Passkey Retrieval
   - 3.4 Benchmarks on Original Context Window Size
   - 3.5 Long Document Summarization
4. Related Work
5. Conclusions
- Acknowledgements
- Appendix A: Proof
- Appendix B: Visualization of Quantities in Extrapolation Bound
- Appendix C: Code
  - C.1 Code for Fig. 2
  - C.2 Code for Fig. 5
