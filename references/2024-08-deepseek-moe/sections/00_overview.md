# Overview

**Title:** DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models

**Authors:** Damai Dai\*^{1,2}, Chengqi Deng^1, Chenggang Zhao\*^{1,3}, R.X. Xu^1, Huazuo Gao^1, Deli Chen^1, Jiashi Li^1, Wangding Zeng^1, Xingkai Yu\*^{1,4}, Y. Wu^1, Zhenda Xie^1, Y.K. Li^1, Panpan Huang^1, Fuli Luo^1, Chong Ruan^1, Zhifang Sui^2, Wenfeng Liang^{dagger}

**Affiliations:**
- ^1 DeepSeek-AI
- ^2 National Key Laboratory for Multimedia Information Processing, Peking University
- ^3 Institute for Interdisciplinary Information Sciences, Tsinghua University
- ^4 National Key Laboratory for Novel Software Technology, Nanjing University

\* Contribution during internship at DeepSeek-AI.

**Contact:** {daidamai, szf}@pku.edu.cn, {wenfeng.liang}@deepseek.com

**Code:** https://github.com/deepseek-ai/DeepSeek-MoE

**Venue:** arXiv:2401.06066v1 [cs.CL]

**Date:** 11 Jan 2024

## Abstract

> "In the era of large language models, Mixture-of-Experts (MoE) is a promising architecture for managing computational costs when scaling up model parameters. However, conventional MoE architectures like GShard, which activate the top-K out of N experts, face challenges in ensuring expert specialization, i.e. each expert acquires non-overlapping and focused knowledge. In response, we propose the DeepSeekMoE architecture towards ultimate expert specialization. It involves two principal strategies: (1) finely segmenting the experts into mN ones and activating mK from them, allowing for a more flexible combination of activated experts; (2) isolating K_s experts as shared ones, aiming at capturing common knowledge and mitigating redundancy in routed experts. Starting from a modest scale with 2B parameters, we demonstrate that DeepSeekMoE 2B achieves comparable performance with GShard 2.9B, which has 1.5x expert parameters and computation. In addition, DeepSeekMoE 2B nearly approaches the performance of its dense counterpart with the same number of total parameters, which set the upper bound of MoE models. Subsequently, we scale up DeepSeekMoE to 16B parameters and show that it achieves comparable performance with LLaMA2 7B, with only about 40% of computations. Further, our preliminary efforts to scale up DeepSeekMoE to 145B parameters consistently validate its substantial advantages over the GShard architecture, and show its performance comparable with DeepSeek 67B, using only 28.5% (maybe even 18.2%) of computations." [p. 1]

## Section Headings

1. Introduction
2. Preliminaries: Mixture-of-Experts for Transformers
3. DeepSeekMoE Architecture
   - 3.1. Fine-Grained Expert Segmentation
   - 3.2. Shared Expert Isolation
   - 3.3. Load Balance Consideration
4. Validation Experiments
   - 4.1. Experimental Setup
     - 4.1.1. Training Data and Tokenization
     - 4.1.2. Infrastructures
     - 4.1.3. Hyper-Parameters
     - 4.1.4. Evaluation Benchmarks
   - 4.2. Evaluations
   - 4.3. DeepSeekMoE Aligns Closely with the Upper Bound of MoE Models
   - 4.4. Ablation Studies
   - 4.5. Analysis on Expert Specialization
5. Scaling up to DeepSeekMoE 16B
   - 5.1. Experimental Setup
     - 5.1.1. Training Data and Tokenization
     - 5.1.2. Hyper-Parameters
     - 5.1.3. Evaluation Benchmarks
   - 5.2. Evaluations
     - 5.2.1. Internal Comparison with DeepSeek 7B
     - 5.2.2. Comparison with Open Source Models
6. Alignment for DeepSeekMoE 16B
   - 6.1. Experimental Setup
   - 6.2. Evaluations
7. DeepSeekMoE 145B Ongoing
   - 7.1. Experimental Setup
   - 7.2. Evaluations
8. Related Work
9. Conclusion
Appendices
   - A. Overview of Hyper-Parameters
   - B. Comparing DeepSeekMoE with Larger Models
   - C. Training Benchmark Curves of DeepSeekMoE 16B
