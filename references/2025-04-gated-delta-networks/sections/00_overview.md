# Overview

## Paper Information

**Title:** Gated Delta Networks: Improving Mamba2 with Delta Rule

**Authors:**
- Songlin Yang (MIT CSAIL, yangsl66@mit.edu) - equal contribution, work done during internship at NVIDIA
- Jan Kautz (NVIDIA, jkautz@nvidia.com)
- Ali Hatamizadeh (NVIDIA, ahatamizadeh@nvidia.com) - equal contribution

**Venue:** Published as a conference paper at ICLR 2025

**Code:** https://github.com/NVlabs/GatedDeltaNet

## Abstract

> "Linear Transformers have gained attention as efficient alternatives to standard Transformers, but their performance in retrieval and long-context tasks has been limited. To address these limitations, recent work has explored two distinct mechanisms: gating for adaptive memory control and the delta update rule for precise memory modifications. We observe that these mechanisms are complementary—gating enables rapid memory erasure while the delta rule facilitates targeted updates. Building on this insight, we introduce the gated delta rule and develop a parallel training algorithm optimized for modern hardware. Our proposed architecture, Gated DeltaNet, consistently surpasses existing models like Mamba2 and DeltaNet across multiple benchmarks, including language modeling, commonsense reasoning, in-context retrieval, length extrapolation, and long-context understanding. We further enhance performance by developing hybrid architectures that combine Gated DeltaNet layers with sliding window attention or Mamba2 layers, achieving improved training efficiency and superior task performance." [p. 1]

## Section Headings

- Abstract
- 1 Introduction
- 2 Preliminary
  - 2.1 Mamba2: Linear Attention with Decay
  - 2.2 Delta Networks: Linear Attention with Delta Rule
- 3 Gated Delta Networks
  - 3.1 Formulation: Gated Delta Rule
  - 3.2 Case Study: Single Needle in a Haystack (S-NIAH)
  - 3.3 Algorithm: Hardware-efficient Chunkwise Training
  - 3.4 Gated Delta Networks and Hybrid Models
- 4 Experiments
- 5 Related Work
- 6 Conclusion
- Acknowledgment
- References
- Appendix A: Extended WY Representation for Gated Delta Rule
- Appendix B: Experiment Contunued
  - B.1 Evaluation
  - B.2 Ablation Study
