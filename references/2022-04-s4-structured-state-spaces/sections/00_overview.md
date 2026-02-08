# Overview

**Title:** Efficiently Modeling Long Sequences with Structured State Spaces

**Authors:** Albert Gu, Karan Goel, and Christopher Ré

**Affiliations:** Department of Computer Science, Stanford University

**Contact:** {albertgu, krng}@stanford.edu, chrismre@cs.stanford.edu

**Venue:** arXiv:2111.00396v3 [cs.LG]

**Date:** 5 Aug 2022

**Code:** https://github.com/HazyResearch/state-spaces

## Abstract

> "A central goal of sequence modeling is designing a single principled model that can address sequence data across a range of modalities and tasks, particularly on long-range dependencies. Although conventional models including RNNs, CNNs, and Transformers have specialized variants for capturing long dependencies, they still struggle to scale to very long sequences of 10000 or more steps. A promising recent approach proposed modeling sequences by simulating the fundamental state space model (SSM) x'(t) = Ax(t) + Bu(t), y(t) = Cx(t) + Du(t), and showed that for appropriate choices of the state matrix A, this system could handle long-range dependencies mathematically and empirically. However, this method has prohibitive computation and memory requirements, rendering it infeasible as a general sequence modeling solution. We propose the Structured State Space sequence model (S4) based on a new parameterization for the SSM, and show that it can be computed much more efficiently than prior approaches while preserving their theoretical strengths. Our technique involves conditioning A with a low-rank correction, allowing it to be diagonalized stably and reducing the SSM to the well-studied computation of a Cauchy kernel. S4 achieves strong empirical results across a diverse range of established benchmarks, including (i) 91% accuracy on sequential CIFAR-10 with no data augmentation or auxiliary losses, on par with a larger 2-D ResNet, (ii) substantially closing the gap to Transformers on image and language modeling tasks, while performing generation 60x faster (iii) SoTA on every task from the Long Range Arena benchmark, including solving the challenging Path-X task of length 16k that all prior work fails on, while being as efficient as all competitors." [p. 1]

## Section Headings

1. Introduction [p. 1-3]
2. Background: State Spaces [p. 3-4]
   - 2.1 State Space Models: A Continuous-time Latent State Model [p. 3]
   - 2.2 Addressing Long-Range Dependencies with HiPPO [p. 3-4]
   - 2.3 Discrete-time SSM: The Recurrent Representation [p. 4]
   - 2.4 Training SSMs: The Convolutional Representation [p. 4]
3. Method: Structured State Spaces (S4) [p. 5-6]
   - 3.1 Motivation: Diagonalization [p. 5]
   - 3.2 The S4 Parameterization: Normal Plus Low-Rank [p. 5-6]
   - 3.3 S4 Algorithms and Computational Complexity [p. 6]
   - 3.4 Architecture Details of the Deep S4 Layer [p. 7]
4. Experiments [p. 7-11]
   - 4.1 S4 Efficiency Benchmarks [p. 7-8]
   - 4.2 Learning Long Range Dependencies [p. 8-9]
   - 4.3 S4 as a General Sequence Model [p. 9-10]
   - 4.4 SSM Ablations: the Importance of HiPPO [p. 11]
5. Conclusion [p. 12]
Acknowledgments [p. 12]
References [p. 13-15]
A. Discussion [p. 16]
   - Related Work
   - Implementation
   - Limitations and Future Directions
B. Numerical Instability of LSSL [p. 16-19]
   - B.1 HiPPO Diagonalization [p. 17-18]
   - B.2 Fast but Unstable LSSL Algorithm [p. 18-19]
C. S4 Algorithm Details [p. 19-25]
   - C.1 NPLR Representations of HiPPO Matrices [p. 19-20]
   - C.2 Computing the S4 Recurrent View [p. 21]
   - C.3 Computing the Convolutional View [p. 22-25]
D. Experiment Details and Full Results [p. 25-32]
   - D.1 Benchmarking [p. 25]
   - D.2 Long-Range Dependencies [p. 26-27]
   - D.3 General Sequence Modeling [p. 27-30]
     - D.3.1 CIFAR Density Estimation [p. 28]
     - D.3.2 WikiText-103 Language Modeling [p. 28]
     - D.3.3 Autoregressive Generation Speed [p. 28-29]
     - D.3.4 Pixel-Level Sequential Image Classification [p. 29]
     - D.3.5 Time Series Forecasting compared to Informer [p. 30]
   - D.4 Visualizations [p. 30]
   - D.5 Reproduction [p. 30-31]
