# Overview

**Title:** Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned

**Authors:** Elena Voita (Yandex, Russia; University of Amsterdam, Netherlands), David Talbot (Yandex, Russia), Fedor Moiseev (Yandex, Russia; Moscow Institute of Physics and Technology, Russia), Rico Sennrich (University of Edinburgh, Scotland; University of Zurich, Switzerland), Ivan Titov (University of Edinburgh, Scotland; University of Amsterdam, Netherlands)

**Venue:** arXiv:1905.09418v2 [cs.CL]

**Date:** 7 Jun 2019

**Code:** https://github.com/lena-voita/the-story-of-heads

## Abstract

> "Multi-head self-attention is a key component of the Transformer, a state-of-the-art architecture for neural machine translation. In this work we evaluate the contribution made by individual attention heads in the encoder to the overall performance of the model and analyze the roles played by them. We find that the most important and confident heads play consistent and often linguistically-interpretable roles. When pruning heads using a method based on stochastic gates and a differentiable relaxation of the L_0 penalty, we observe that specialized heads are last to be pruned. Our novel pruning method removes the vast majority of heads without seriously affecting performance. For example, on the English-Russian WMT dataset, pruning 38 out of 48 encoder heads results in a drop of only 0.15 BLEU." [p. 1]

## Sections

1. Introduction
2. Transformer Architecture
3. Data and Setting
4. Identifying Important Heads
5. Characterizing Heads
   - 5.1 Positional Heads
   - 5.2 Syntactic Heads
     - 5.2.1 Methodology
     - 5.2.2 Results
   - 5.3 Rare Words
6. Pruning Attention Heads
   - 6.1 Method
   - 6.2 Pruning Encoder Heads
     - 6.2.1 Quantitative Results: BLEU Score
     - 6.2.2 Functions of Retained Heads
   - 6.3 Pruning All Types of Attention Heads
     - 6.3.1 Quantitative Results: BLEU Score
     - 6.3.2 Heads Importance
7. Related Work
8. Conclusions
A. Layer-wise Relevance Propagation
   - A.1 General Idea
   - A.2 Formal Rules
   - A.3 Head Relevance
B. Experimental Setup
   - B.1 Data Preprocessing
   - B.2 Model Parameters
   - B.3 Optimizer
