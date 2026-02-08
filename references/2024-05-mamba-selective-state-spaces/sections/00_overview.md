# Overview

**Title:** Mamba: Linear-Time Sequence Modeling with Selective State Spaces

**Authors:** Albert Gu\*^1 and Tri Dao\*^2 (\*Alphabetical by first name)

**Affiliations:**
1. Machine Learning Department, Carnegie Mellon University
2. Department of Computer Science, Princeton University

**Contact:** agu@cs.cmu.edu, tri@tridao.me

**Venue:** arXiv:2312.00752v2 [cs.LG]

**Date:** 31 May 2024

## Abstract

> "Foundation models, now powering most of the exciting applications in deep learning, are almost universally based on the Transformer architecture and its core attention module. Many subquadratic-time architectures such as linear attention, gated convolution and recurrent models, and structured state space models (SSMs) have been developed to address Transformers' computational inefficiency on long sequences, but they have not performed as well as attention on important modalities such as language. We identify that a key weakness of such models is their inability to perform content-based reasoning, and make several improvements. First, simply letting the SSM parameters be functions of the input addresses their weakness with discrete modalities, allowing the model to selectively propagate or forget information along the sequence length dimension depending on the current token. Second, even though this change prevents the use of efficient convolutions, we design a hardware-aware parallel algorithm in recurrent mode. We integrate these selective SSMs into a simplified end-to-end neural network architecture without attention or even MLP blocks (Mamba). Mamba enjoys fast inference (5x higher throughput than Transformers) and linear scaling in sequence length, and its performance improves on real data up to million-length sequences. As a general sequence model backbone, Mamba achieves state-of-the-art performance across several modalities such as language, audio, and genomics. On language modeling, our Mamba-3B model outperforms Transformers of the same size and matches Transformers twice its size, both in pretraining and downstream evaluation." [p. 1]

## Section Headings

1. Introduction
2. State Space Models
3. Selective State Space Models
   - 3.1 Motivation: Selection as a Means of Compression
   - 3.2 Improving SSMs with Selection
   - 3.3 Efficient Implementation of Selective SSMs
     - 3.3.1 Motivation of Prior Models
     - 3.3.2 Overview of Selective Scan: Hardware-Aware State Expansion
   - 3.4 A Simplified SSM Architecture
   - 3.5 Properties of Selection Mechanisms
     - 3.5.1 Connection to Gating Mechanisms
     - 3.5.2 Interpretation of Selection Mechanisms
   - 3.6 Additional Model Details
4. Empirical Evaluation
   - 4.1 Synthetic Tasks
     - 4.1.1 Selective Copying
     - 4.1.2 Induction Heads
   - 4.2 Language Modeling
     - 4.2.1 Scaling Laws
     - 4.2.2 Downstream Evaluations
   - 4.3 DNA Modeling
     - 4.3.1 Scaling: Model Size
     - 4.3.2 Scaling: Context Length
     - 4.3.3 Synthetic Species Classification
   - 4.4 Audio Modeling and Generation
     - 4.4.1 Long-Context Autoregressive Pretraining
     - 4.4.2 Autoregressive Speech Generation
   - 4.5 Speed and Memory Benchmarks
   - 4.6 Model Ablations
     - 4.6.1 Architecture
     - 4.6.2 Selective SSM
5. Discussion
6. Conclusion
Acknowledgments
A. Discussion: Selection Mechanism
B. Related Work
   - B.1 S4 Variants and Derivatives
   - B.2 SSM Architectures
   - B.3 Relationship to RNNs
   - B.4 Linear Attention
   - B.5 Long Context Models
C. Mechanics of Selective SSMs
D. Hardware-aware Algorithm For Selective SSMs
E. Experimental Details and Additional Results
   - E.1 Synthetic Tasks
   - E.2 Language Modeling
     - E.2.1 Scaling Law Details
     - E.2.2 Additional Scaling Law Ablations
     - E.2.3 Downstream Evaluation Details
   - E.3 DNA Modeling
     - E.3.1 Pretraining Details
     - E.3.2 Scaling: Model Size Details
     - E.3.3 Scaling: Context Length Details
     - E.3.4 Species (Great Apes) Classification
   - E.4 Audio Details
     - E.4.1 YouTubeMix Audio Pretraining
     - E.4.2 SC09 Speech Generation
   - E.5 Efficiency Benchmark
