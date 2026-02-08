# Overview

**Title:** Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality

**Authors:** Tri Dao (alphabetical by last name), Albert Gu

**Affiliations:**
- Tri Dao: Department of Computer Science, Princeton University (tri@tridao.me)
- Albert Gu: Machine Learning Department, Carnegie Mellon University (agu@cs.cmu.edu)

**Venue:** ICML 2024

**Date:** 31 May 2024 (arXiv v1)

**Abstract:**
> "While Transformers have been the main architecture behind deep learning's success in language modeling, state-space models (SSMs) such as Mamba have recently been shown to match or outperform Transformers at small to medium scale. We show that these families of models are actually quite closely related, and develop a rich framework of theoretical connections between SSMs and variants of attention, connected through various decompositions of a well-studied class of structured *semiseparable matrices*. Our state space duality (SSD) framework allows us to design a new architecture (**Mamba-2**) whose core layer is a refinement of Mamba's selective SSM that is 2-8x faster, while continuing to be competitive with Transformers on language modeling." [p. 1]

**Code:** https://github.com/state-spaces/mamba

## Section Headings

1. Introduction
2. Background and Overview
   - 2.1 Structured State Space Models
   - 2.2 Attention
   - 2.3 Structured Matrices
   - 2.4 Overview: Structured State Space Duality
   - 2.5 Notation
3. State Space Models are Structured Matrices
   - 3.1 The Matrix Transformation Form of State Space Models
   - 3.2 Semiseparable Matrices
     - 3.2.1 The Sequentially Semiseparable (SSS) Representation
     - 3.2.2 1-Semiseparable Matrices: the Scalar SSM Recurrence
   - 3.3 State Space Models are Semiseparable Matrices
   - 3.4 Computing State Space Models through Structured Matrix Algorithms
     - 3.4.1 The Linear (Recurrent) Mode
     - 3.4.2 The Quadratic (Naive) Mode
     - 3.4.3 Summary
4. Structured Masked Attention: Generalizing Linear Attention with Structured Matrices
   - 4.1 The Attention Framework
     - 4.1.1 Attention
     - 4.1.2 Self-Attention
     - 4.1.3 Kernel Attention
     - 4.1.4 Masked (Kernel) Attention
   - 4.2 Linear Attention
     - 4.2.1 A Tensor Contraction Proof of Linear Attention
   - 4.3 Structured Masked Attention
     - 4.3.1 Summary: The Dual Forms of Masked Attention
5. State Space Duality
   - 5.1 Scalar-Identity Structured State Space Models
   - 5.2 1-Semiseparable Structured Masked Attention
   - 5.3 Structured State-Space Duality (SSD)
6. A Hardware-Efficient Algorithm for SSD Models
   - 6.1 Diagonal Blocks
   - 6.2 Low-Rank Blocks
   - 6.3 Computational Cost
7. The Mamba-2 Architecture
   - 7.1 Block Design
   - 7.2 Multihead Patterns for Sequence Transformations
   - 7.3 Other SSD Extensions from Linear Attention
8. Systems Optimization for SSMs
   - 8.1 Tensor Parallel
   - 8.2 Sequence Parallelism
   - 8.3 Variable Length
9. Empirical Validation
   - 9.1 Synthetics: Associative Recall
   - 9.2 Language Modeling
     - 9.2.1 Scaling Laws
     - 9.2.2 Downstream Evaluations
     - 9.2.3 Hybrid Models: Combining SSD Layer with MLP and Attention
   - 9.3 Speed Benchmarks
   - 9.4 Architecture Ablations
     - 9.4.1 Block Design
     - 9.4.2 Head Structure
     - 9.4.3 Attention Kernel Approximations
10. Related Work and Discussion
    - 10.1 State Space Models
    - 10.2 Structured Matrices
    - 10.3 (Linear) Attention
    - 10.4 Related Models
11. Conclusion
Acknowledgments
A. Glossary
B. Efficient Algorithms for the Scalar SSM Scan (1-SS Multiplication)
   - B.1 Problem Definition
   - B.2 Classical Algorithms
     - B.2.1 Sequential Recurrence
     - B.2.2 Parallel Associative Scan
   - B.3 Efficient Algorithms via Structured Matrix Decompositions
     - B.3.1 Dilated Mode
     - B.3.2 State-Passing (Chunkwise) Mode
     - B.3.3 Fully Recurrent Mode
     - B.3.4 (Parallel) Block Decomposition Mode
     - B.3.5 Associative Scan Mode
C. Theory Details
   - C.1 Extras: Closure Properties of SSMs
   - C.2 Autoregressive Masked Attention is Semiseparable-Structured Attention
D. Experimental Details
   - D.1 MQAR Details
   - D.2 Scaling Law Details
   - D.3 Downstream Evaluation Details
   - D.4 Ablation Details
