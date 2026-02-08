# Overview

**Title:** Retentive Network: A Successor to Transformer for Large Language Models

**Authors:** Yutao Sun*†‡, Li Dong*†, Shaohan Huang†, Shuming Ma†, Yuqing Xia†, Jilong Xue†, Jianyong Wang‡, Furu Wei†◇
- † Microsoft Research
- ‡ Tsinghua University
- \* Equal contribution
- ◇ Corresponding author

**Venue:** arXiv:2307.08621v4

**Date:** 9 Aug 2023

**URL:** https://aka.ms/GeneralAI

**Code:** https://aka.ms/retnet

## Abstract

> "In this work, we propose Retentive Network (RetNet) as a foundation architecture for large language models, simultaneously achieving training parallelism, low-cost inference, and good performance. We theoretically derive the connection between recurrence and attention, and then propose the retention mechanism for sequence modeling, which supports three computation paradigms, i.e., parallel, recurrent, and chunkwise recurrent. Specifically, the parallel representation allows for training parallelism. The recurrent representation enables low-cost O(1) inference, which improves decoding throughput, latency, and GPU memory without sacrificing performance. The chunkwise recurrent representation facilitates efficient long-sequence modeling with linear complexity, where each chunk is encoded parallelly while recurrently summarizing the chunks. Experimental results on language modeling show that RetNet achieves favorable scaling results, parallel training, low-cost deployment, and efficient inference. The intriguing properties make RetNet a strong successor to Transformer for large language models. Code will be available at https://aka.ms/retnet." [p. 1]

## Section Headings

1. Introduction
2. Retentive Networks
   - 2.1 Retention
   - 2.2 Gated Multi-Scale Retention
   - 2.3 Overall Architecture of Retention Networks
   - 2.4 Relation to and Differences from Previous Methods
3. Experiments
   - 3.1 Setup
   - 3.2 Comparisons with Transformer
   - 3.3 Training Cost
   - 3.4 Inference Cost
   - 3.5 Comparison with Transformer Variants
   - 3.6 Ablation Studies
4. Conclusion
Acknowledgement
A. Hyperparameters
B. Grouped Results of Different Context Lengths
