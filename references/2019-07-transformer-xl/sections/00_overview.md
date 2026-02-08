# Overview

**Title:** Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context

**Authors:** Zihang Dai*^{1,2}, Zhilin Yang*^{1,2}, Yiming Yang^1, Jaime Carbonell^1, Quoc V. Le^2, Ruslan Salakhutdinov^1
(*Equal contribution. Order determined by swapping the one in Yang et al. (2017).)

**Affiliations:** ^1 Carnegie Mellon University, ^2 Google Brain

**Contact:** {dzihang, zhiliny, yiming, jgc, rsalakhu}@cs.cmu.edu, qvl@google.com

**Date:** 2 Jun 2019 (arXiv:1901.02860v3)

**Code:** https://github.com/kimiyoung/transformer-xl (TensorFlow and PyTorch)

## Abstract

> "Transformers have a potential of learning longer-term dependency, but are limited by a fixed-length context in the setting of language modeling. We propose a novel neural architecture Transformer-XL that enables learning dependency beyond a fixed length without disrupting temporal coherence. It consists of a segment-level recurrence mechanism and a novel positional encoding scheme. Our method not only enables capturing longer-term dependency, but also resolves the context fragmentation problem. As a result, Transformer-XL learns dependency that is 80% longer than RNNs and 450% longer than vanilla Transformers, achieves better performance on both short and long sequences, and is up to 1,800+ times faster than vanilla Transformers during evaluation. Notably, we improve the state-of-the-art results of bpc/perplexity to 0.99 on enwiki8, 1.08 on text8, 18.3 on WikiText-103, 21.8 on One Billion Word, and 54.5 on Penn Treebank (without finetuning). When trained only on WikiText-103, Transformer-XL manages to generate reasonably coherent, novel text articles with thousands of tokens. Our code, pretrained models, and hyperparameters are available in both Tensorflow and PyTorch." [p. 1]

## Section headings

1. Introduction
2. Related Work
3. Model
   - 3.1 Vanilla Transformer Language Models
   - 3.2 Segment-Level Recurrence with State Reuse
   - 3.3 Relative Positional Encodings
4. Experiments
   - 4.1 Main Results
   - 4.2 Ablation Study
   - 4.3 Relative Effective Context Length
   - 4.4 Generated Text
   - 4.5 Evaluation Speed
5. Conclusions
A. Ablation Study with Memory Constraints
B. Efficient Computation of the Attention with Relative Positional Embedding
C. Details About RECL
D. Attention Visualization
E. Generated Text
