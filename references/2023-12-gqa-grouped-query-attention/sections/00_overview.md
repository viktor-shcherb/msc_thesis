# Overview

**Title:** GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints

**Authors:** Joshua Ainslie*, James Lee-Thorp*, Michiel de Jong*†, Yury Zemlyanskiy, Federico Lebron, Sumit Sanghai

*Equal contribution. †University of Southern California. Work done at Google Research.

**Affiliation:** Google Research

**Venue:** arXiv:2305.13245v3 [cs.CL]

**Date:** 23 Dec 2023

## Abstract

> "Multi-query attention (MQA), which only uses a single key-value head, drastically speeds up decoder inference. However, MQA can lead to quality degradation, and moreover it may not be desirable to train a separate model just for faster inference. We (1) propose a recipe for uptraining existing multi-head language model checkpoints into models with MQA using 5% of original pre-training compute, and (2) introduce grouped-query attention (GQA), a generalization of multi-query attention which uses an intermediate (more than one, less than number of query heads) number of key-value heads. We show that uptrained GQA achieves quality close to multi-head attention with comparable speed to MQA." [p. 1]

## Section Headings

1. Introduction
2. Method
   - 2.1 Uptraining
   - 2.2 Grouped-query attention
3. Experiments
   - 3.1 Experimental setup
   - 3.2 Main results
   - 3.3 Ablations
4. Related Work
5. Conclusion
- Limitations
- Acknowledgements
- References
- A Training Stability
