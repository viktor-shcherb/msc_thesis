# Overview

**Title:** Compressive Transformers for Long-Range Sequence Modelling

**Authors:** Jack W. Rae\* (DeepMind, CoMPLEX UCL), Anna Potapenko\* (DeepMind), Siddhant M. Jayakumar (DeepMind), Chloe Hillier (DeepMind), Timothy P. Lillicrap (DeepMind, CoMPLEX UCL)

\* Authors contributed equally.

**Affiliations:** DeepMind, London, UK; CoMPLEX, Computer Science, University College London, UK.

**Correspondence:** {jwrae, apotapenko}@google.com

**Date:** arXiv:1911.05507v1, 13 Nov 2019

**Venue:** arXiv preprint

## Abstract

> "We present the Compressive Transformer, an attentive sequence model which compresses past memories for long-range sequence learning. We find the Compressive Transformer obtains state-of-the-art language modelling results in the WikiText-103 and Enwik8 benchmarks, achieving 17.1 ppl and 0.97 bpc respectively. We also find it can model high-frequency speech effectively and can be used as a memory mechanism for RL, demonstrated on an object matching task. To promote the domain of long-range sequence learning, we propose a new open-vocabulary language modelling benchmark derived from books, PG-19." [p. 1]

## Section Headings

1. Introduction
2. Related Work
3. Model
   - 3.1 Description
   - 3.2 Compression Functions and Losses
   - 3.3 Temporal Range
4. PG-19 Benchmark
   - 4.1 Related Datasets
   - 4.2 Statistics
5. Experiments
   - 5.1 PG-19
   - 5.2 Enwik8
   - 5.3 WikiText-103
   - 5.4 Compressibility of Layers
   - 5.5 Attention
   - 5.5.1 Optimisation Schedule
   - 5.6 Speech
   - 5.7 Reinforcement Learning
6. Conclusion
7. Supplementary Materials
   - A. Compression Across Layers
   - B. Comparison of Compressed Memory Sizes
   - C. PG-19 Preprocessing
   - D. PG-19 Topics
   - E. PG-19 Samples
