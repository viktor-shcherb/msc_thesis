# Overview

**Title:** LLaMA: Open and Efficient Foundation Language Models

**Authors:** Hugo Touvron\*, Thibaut Lavril\*, Gautier Izacard\*, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave\*, Guillaume Lample\*

**Affiliation:** Meta AI

**Venue:** arXiv:2302.13971 [cs.CL]

**Date:** 27 Feb 2023

**Correspondence:** {htouvron, thibautlav, gizacard, egrave, glample}@meta.com

**Code:** https://github.com/facebookresearch/llama

## Abstract

> "We introduce LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. We train our models on trillions of tokens, and show that it is possible to train state-of-the-art models using publicly available datasets exclusively, without resorting to proprietary and inaccessible datasets. In particular, LLaMA-13B outperforms GPT-3 (175B) on most benchmarks, and LLaMA-65B is competitive with the best models, Chinchilla-70B and PaLM-540B. We release all our models to the research community." [p. 1]

## Section headings

1. Introduction
2. Approach
   - 2.1 Pre-training Data
   - 2.2 Architecture
   - 2.3 Optimizer
   - 2.4 Efficient implementation
3. Main results
   - 3.1 Common Sense Reasoning
   - 3.2 Closed-book Question Answering
   - 3.3 Reading Comprehension
   - 3.4 Mathematical reasoning
   - 3.5 Code generation
   - 3.6 Massive Multitask Language Understanding
   - 3.7 Evolution of performance during training
4. Instruction Finetuning
5. Bias, Toxicity and Misinformation
   - 5.1 RealToxicityPrompts
   - 5.2 CrowS-Pairs
   - 5.3 WinoGender
   - 5.4 TruthfulQA
6. Carbon footprint
7. Related work
8. Conclusion
9. Acknowledgements
A. Question Answering
B. MMLU
C. Generations from LLaMA-65B
D. Generations from LLaMA-I
