# Overview

**Title:** YaRN: Efficient Context Window Extension of Large Language Models

**Authors:**
- Bowen Peng (Nous Research) [Reddit: /u/bloc97, GitHub: bloc97]
- Jeffrey Quesnelle (Nous Research) [Reddit: /u/emozilla, X: @theemozilla, GitHub: jquesnelle]
- Honglu Fan (EleutherAI; University of Geneva)
- Enrico Shippole [X: @EnricoShippole, GitHub: conceptofmind]

**Venue:** arXiv preprint (arXiv:2309.00071v2). Preprint. Under review.

**Date:** 1 Nov 2023 (v2)

**Code:** https://github.com/jquesnelle/yarn

## Abstract

> "Rotary Position Embeddings (RoPE) have been shown to effectively encode positional information in transformer-based language models. However, these models fail to generalize past the sequence length they were trained on. We present YaRN (Yet another RoPE extensioN method), a compute-efficient method to extend the context window of such models, requiring 10x less tokens and 2.5x less training steps than previous methods. Using YaRN, we show that LLaMA models can effectively utilize and extrapolate to context lengths much longer than their original pre-training would allow, while also surpassing previous the state-of-the-art at context window extension. In addition, we demonstrate that YaRN exhibits the capability to extrapolate beyond the limited context of a fine-tuning dataset. The models fine-tuned using YaRN have been made available and reproduced online up to 128k context length at https://github.com/jquesnelle/yarn" [p. 1]

## Section Headings

1. Introduction
2. Background and Related Work
   - 2.1 Rotary Position Embeddings
   - 2.2 Position Interpolation
   - 2.3 Additional Notation
   - 2.4 Related work
3. Methodology
   - 3.1 Loss of High Frequency information - "NTK-aware" interpolation
   - 3.2 Loss of Relative Local Distances - "NTK-by-parts" interpolation
   - 3.3 Dynamic Scaling - "Dynamic NTK" interpolation
   - 3.4 YaRN
4. Experiments
   - 4.1 Training
   - 4.2 Extrapolation and Transfer Learning
   - 4.3 Evaluation
     - 4.3.1 Long Sequence Language Modeling
     - 4.3.2 Passkey Retrieval
     - 4.3.3 Standardized Benchmarks
5. Conclusion
6. Reproducibility
A. Additional details on interpolation methods
   - A.1 Short notes on the deduction of "NTK-aware" interpolation
   - A.2 The impact of pre-softmax scaling of YaRN on perplexity
B. Additional tables and charts
   - B.1 GovReport evaluations
   - B.2 Passkey Retrieval
   - B.3 Dynamic scaling on models without any fine-tuning
   - B.4 Mistral
