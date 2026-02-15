# Overview

## Paper Information

**Title:** Eliminating Position Bias of Language Models: A Mechanistic Approach

**Authors:**
- Ziqi Wang¹ (ziqiw9@illinois.edu)
- Hanlin Zhang²
- Xiner Li³
- Kuan-Hao Huang¹,³
- Chi Han¹
- Shuiwang Ji³
- Sham M. Kakade²
- Hao Peng¹
- Heng Ji¹

**Affiliations:**
1. University of Illinois Urbana-Champaign
2. Harvard University
3. Texas A&M University

**Venue:** ICLR 2025 (Published as a conference paper at ICLR 2025)

**ArXiv ID:** 2407.01100v3

**Date:** 31 Mar 2025

## Abstract

> "Position bias has proven to be a prevalent issue of modern language models (LMs), where the models prioritize content based on its position within the given context. This bias often leads to unexpected model failures and hurts performance, robustness, and reliability across various applications. A simple mechanistic analysis attributes the position bias to two components employed in nearly all state-of-the-art LMs: causal attention and position embedding. Based on the analysis, we propose to eliminate position bias (e.g., different retrieved documents' relative orders in QA affect performance) with a training-free zero-shot approach. Our method changes the causal attention to bidirectional attention between documents and utilizes model attention values to decide the relative orders of documents instead of using the order provided in input prompts, therefore enabling Position-iNvariant inferencE (PINE) at the document level. By eliminating position bias, models achieve better performance and reliability in downstream tasks, including LM-as-a-judge, retrieval-augmented QA, molecule generation, and math reasoning. Notably, PINE is especially useful when adapting LMs for evaluating reasoning pairs: it consistently provides 8 to 10 percentage points performance gains, making Llama-3-70B-Instruct perform even better than GPT-4-0125-preview and GPT-4o-2024-08-06 on the RewardBench reasoning set."

## Section Headings

1. Introduction
2. Related Work
3. Methodology
   - 3.1 Formulation
   - 3.2 Causal Attention and Position Embedding Are The Cause of Position Bias
   - 3.3 PINE: Inter-Document Position-Invariant Inference via Bidirectional Attention
   - 3.4 Discussion
4. Experiment
   - 4.1 Settings
   - 4.2 Results on LM-as-a-Judge
   - 4.3 Results on Retrieval-Augmented Question-Answering
   - 4.4 Results on Molecule Generation and Math Reasoning
   - 4.5 Computational Overhead
5. Conclusion, Limitations and Future Work
6. Reproducibility Statement
7. Acknowledgment
8. References
9. Appendix A: Another Example of Position Bias in VLMs
10. Appendix B: Complete Proof
11. Appendix C: Statistics of Position Bias in RewardBench
12. Appendix D: Full Results of RewardBench (pp. 16-22)
13. Appendix E: Implementation Details (pp. 23-24)
14. Appendix F: Qualitative Examples (pp. 24-28)
