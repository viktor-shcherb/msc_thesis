# Overview

**Title:** Revealing the Dark Secrets of BERT

**Authors:** Olga Kovaleva, Alexey Romanov, Anna Rogers, Anna Rumshisky

**Affiliations:** Department of Computer Science, University of Massachusetts Lowell, MA 01854

**Contact:** {okovalev, arum, aromanov}@cs.uml.edu

**Venue:** arXiv:1908.08593v2 [cs.CL]

**Date:** 11 Sep 2019

## Abstract

> "BERT-based architectures currently give state-of-the-art performance on many NLP tasks, but little is known about the exact mechanisms that contribute to its success. In the current work, we focus on the interpretation of self-attention, which is one of the fundamental underlying components of BERT. Using a subset of GLUE tasks and a set of handcrafted features-of-interest, we propose the methodology and carry out a qualitative and quantitative analysis of the information encoded by the individual BERT's heads. Our findings suggest that there is a limited set of attention patterns that are repeated across different heads, indicating the overall model overparametrization. While different heads consistently use the same attention patterns, they have varying impact on performance across different tasks. We show that manually disabling attention in certain heads leads to a performance improvement over the regular fine-tuned BERT models." [p. 1]

## Section headings

1. Introduction
2. Related work
3. Methodology
4. Experiments
   - 4.1 BERT's self-attention patterns
   - 4.2 Relation-specific heads in BERT
   - 4.3 Change in self-attention patterns after fine-tuning
   - 4.4 Attention to linguistic features
   - 4.5 Token-to-token attention
   - 4.6 Disabling self-attention heads
5. Discussion
6. Conclusion
7. Acknowledgments
A. Examples of full self-attention maps
