# Overview

**Title:** Training Compute-Optimal Large Language Models

**Authors:** Jordan Hoffmann\*, Sebastian Borgeaud\*, Arthur Mensch\*, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals and Laurent Sifre\*
(\*Equal contributions)

**Affiliations:** DeepMind

**Corresponding authors:** {jordanhoffmann|sborgeaud|amensch|sifre}@deepmind.com

**Date:** 29 Mar 2022 (arXiv:2203.15556v1)

**Copyright:** 2023 DeepMind. All rights reserved.

## Abstract

> "We investigate the optimal model size and number of tokens for training a transformer language model under a given compute budget. We find that current large language models are significantly undertrained, a consequence of the recent focus on scaling language models whilst keeping the amount of training data constant. By training over 400 language models ranging from 70 million to over 16 billion parameters on 5 to 500 billion tokens, we find that for compute-optimal training, the model size and the number of training tokens should be scaled equally: for every doubling of model size the number of training tokens should also be doubled. We test this hypothesis by training a predicted compute-optimal model, Chinchilla, that uses the same compute budget as Gopher but with 70B parameters and 4x more more data. Chinchilla uniformly and significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large range of downstream evaluation tasks. This also means that Chinchilla uses substantially less compute for fine-tuning and inference, greatly facilitating downstream usage. As a highlight, Chinchilla reaches a state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater than a 7% improvement over Gopher." [p. 1]

## Section headings

1. Introduction
2. Related Work
3. Estimating the optimal parameter/training tokens allocation
   - 3.1 Approach 1: Fix model sizes and vary number of training tokens
   - 3.2 Approach 2: IsoFLOP profiles
   - 3.3 Approach 3: Fitting a parametric loss function
   - 3.4 Optimal model scaling
4. *Chinchilla*
   - 4.1 Model and training details
   - 4.2 Results
     - 4.2.1 Language modelling
     - 4.2.2 MMLU
     - 4.2.3 Reading comprehension
     - 4.2.4 BIG-bench
     - 4.2.5 Common sense
     - 4.2.6 Closed-book question answering
     - 4.2.7 Gender bias and toxicity
5. Discussion & Conclusion
6. Acknowledgements
References
