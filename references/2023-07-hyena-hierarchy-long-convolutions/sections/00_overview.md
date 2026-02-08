# Overview

**Title:** Hyena Hierarchy: Towards Larger Convolutional Language Models

**Authors:**
- Michael Poli*,1 (equal contribution)
- Stefano Massaroli*,2 (equal contribution)
- Eric Nguyen1,*
- Daniel Y. Fu1
- Tri Dao1
- Stephen Baccus1
- Yoshua Bengio2
- Stefano Ermon1,† (equal senior authorship)
- Christopher Ré1,† (equal senior authorship)

**Affiliations:**
1. Stanford University
2. Mila and Université de Montréal

**Venue:** arXiv:2302.10866v3 [cs.LG], submitted draft, last compiled April 21, 2023

**Date:** April 19, 2023 (v3)

## Abstract

> "Recent advances in deep learning have relied heavily on the use of large Transformers due to their ability to learn at scale. However, the core building block of Transformers, the attention operator, exhibits quadratic cost in sequence length, limiting the amount of context accessible. Existing subquadratic methods based on low-rank and sparse approximations need to be combined with dense attention layers to match Transformers, indicating a gap in capability. In this work, we propose Hyena, a subquadratic drop-in replacement for attention constructed by interleaving implicitly parametrized long convolutions and data-controlled gating. In recall and reasoning tasks on sequences of thousands to hundreds of thousands of tokens, Hyena improves accuracy by more than 50 points over operators relying on state-spaces and other implicit and explicit methods, matching attention-based models. We set a new state-of-the-art for dense-attention-free architectures on language modeling in standard datasets (WikiText103 and The Pile), reaching Transformer quality with a 20% reduction in training compute required at sequence length 2K. Hyena operators are twice as fast as highly optimized attention at sequence length 8K, and 100x faster at sequence length 64K." [p. 1]

## Section Headings

1. Introduction
2. Preliminaries and Related Work
   - 2.1 Explicit and Implicit Convolutions
   - 2.2 The Self-Attention Operator
3. Hyena: Definition and Properties
   - 3.1 Hyena Recurrences
   - 3.2 Hyena Matrices
   - 3.3 Hyena Filters
   - 3.4 Hyena Algorithm
4. Experiments
   - 4.1 Shrinking the gap on in-context learning
   - 4.2 Language Modeling
   - 4.3 Downstream Evaluation
   - 4.4 Benchmarking
   - 4.5 Large-Scale Image Classification
5. Discussion and Conclusion
6. Acknowledgements
A. Experimental Details
   - A.1 Mechanistic Design Synthetic Benchmarks
   - A.2 Language Modeling
   - A.3 Downstream Evaluation
   - A.4 Image Classification
B. Theoretical Results and Details
   - B.1 Proofs
   - B.2 Analysis of Data-Controlled Mechanisms
C. Discussion and Additional Results
   - C.1 Learning Arithmetic
D. Samples and Visualizations
   - D.1 Hyena Matrices
   - D.2 Hyena Filters
   - D.3 Positional Encoding and Filters Initialization
   - D.4 Downstream Examples
