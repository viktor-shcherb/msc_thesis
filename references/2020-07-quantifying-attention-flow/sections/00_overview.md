# Overview [p. 1–8]

**Title:** Quantifying Attention Flow in Transformers

**Authors:** Samira Abnar, Willem Zuidema

**Affiliations:** ILLC, University of Amsterdam

**Venue:** arXiv preprint arXiv:2005.00928v2

**Date:** 31 May 2020

## Abstract

> "In the Transformer model, 'self-attention' combines information from attended embeddings into the representation of the focal embedding in the next layer. Thus, across layers of the Transformer, information originating from different tokens gets increasingly mixed. This makes attention weights unreliable as explanations probes. In this paper, we consider the problem of quantifying this flow of information through self-attention. We propose two methods for approximating the attention to input tokens given attention weights, *attention rollout* and *attention flow*, as post hoc methods when we use attention weights as the relative relevance of the input tokens. We show that these methods give complementary views on the flow of information, and compared to raw attention, both yield higher correlations with importance scores of input tokens obtained using an ablation method and input gradients." [p. 1]

## Section headings

1. Introduction
2. Setups and Problem Statement
3. Attention Rollout and Attention Flow
4. Analysis and Discussion
5. Conclusion
A. Appendices
   A.1 Single Head Analysis
