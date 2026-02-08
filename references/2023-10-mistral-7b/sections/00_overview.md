# Overview

**Title:** Mistral 7B

**Authors:** Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang, Timothée Lacroix, William El Sayed

**Affiliations:** Mistral AI (all authors)

**Venue:** arXiv preprint arXiv:2310.06825

**Date:** October 10, 2023

**Code:** https://github.com/mistralai/mistral-src
**Webpage:** https://mistral.ai/news/announcing-mistral-7b/

## Abstract

> "We introduce Mistral 7B, a 7-billion-parameter language model engineered for superior performance and efficiency. Mistral 7B outperforms the best open 13B model (Llama 2) across all evaluated benchmarks, and the best released 34B model (Llama 1) in reasoning, mathematics, and code generation. Our model leverages grouped-query attention (GQA) for faster inference, coupled with sliding window attention (SWA) to effectively handle sequences of arbitrary length with a reduced inference cost. We also provide a model fine-tuned to follow instructions, Mistral 7B -- Instruct, that surpasses Llama 2 13B -- chat model both on human and automated benchmarks. Our models are released under the Apache 2.0 license." [p. 1]

## Section Headings

1. Introduction
2. Architectural details
3. Results
4. Instruction Finetuning
5. Adding guardrails for front-facing applications
   - 5.1 System prompt to enforce guardrails
   - 5.2 Content moderation with self-reflection
6. Conclusion
7. Acknowledgements
8. References
