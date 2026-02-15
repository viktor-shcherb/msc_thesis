# Overview

## Paper Metadata

**Title:** A Survey on Transformer Context Extension: Approaches and Evaluation

**Authors:** Yijun Liu¹, Jinzheng Yu², Yang Xu¹, Zhongyang Li³, Qingfu Zhu¹

**Affiliations:**
- ¹ Research Center for Social Computing and Interactive Robotics, Harbin Institute of Technology
- ² State Key Laboratory of Media Convergence and Communication, Communication University of China
- ³ Huawei Technologies, Co., Ltd.

**Contact:** {yijunliu, qfzhu}@ir.hit.edu.cn

**Venue:** arXiv preprint arXiv:2503.13299v2 [cs.CL]

**Date:** 8 Jul 2025

## Abstract

> "Large language models (LLMs) based on Transformer have been widely applied in the filed of natural language processing (NLP), demonstrating strong performance, particularly in handling short text tasks. However, when it comes to long context scenarios, the performance of LLMs degrades due to some challenges. To alleviate this phenomenon, there is a number of work proposed recently. In this survey, we first list the challenges of applying pre-trained LLMs to process long contexts. Then systematically review the approaches related to long context and propose our taxonomy categorizing them into four main types: positional encoding, context compression, retrieval augmented, and attention pattern. In addition to the approaches, we focus on the evaluation aspect and organize work on data, tasks, and metrics based on existing benchmarks. In addition to the two main parts of approaches and evaluation, we present our viewpoints on the current unsolved issues and potential future directions in the long context domain. To illustrate the current status more theoretically, we also list the main challenges in the field of long context before introducing specific work. Although most existing methods and benchmarks have not corresponded to them, these challenges are still instructive for the development of approaches and evaluation." [p. 1]

## Section Headings

1. Introduction
2. Challenges
   - OOD Problem
   - "Lost in the Middle" Phenomenon
   - Quadratic Complexity
3. Approaches
   - 3.1 Positional Encoding
     - 3.1.1 Variants of RoPE
     - 3.1.2 Attention Bias
   - 3.2 Context Compression
     - 3.2.1 Soft Compression
     - 3.2.2 Hard Compression
   - 3.3 Retrieval Augmented
     - 3.3.1 Retrieval Granularity
     - 3.3.2 Similarity Computation
     - 3.3.3 Positional Encoding
     - 3.3.4 Attention Calculation
   - 3.4 Attention Pattern
     - 3.4.1 Sliding Window
     - 3.4.2 Parallel Context
     - 3.4.3 Sparse Attention
4. Evaluation
   - 4.1 Data
   - 4.2 Tasks
     - 4.2.1 Question Answering
     - 4.2.2 Needle-in-a-Haystack
     - 4.2.3 Statistical Tasks
     - 4.2.4 Code
     - 4.2.5 In-Context Learning
     - 4.2.6 Text Generation
     - 4.2.7 Other Tasks
   - 4.3 Metrics
     - 4.3.1 Algorithmic Metrics
     - 4.3.2 Model-based Metrics
     - 4.3.3 LLM-based Metrics
5. Future Roadmap and Open Problems
   - 5.1 Approaches
   - 5.2 Evaluation
6. Conclusion
7. Limitations
8. References
A. Appendix: Details of Approaches
   - A.1 Positional Encoding
     - A.1.1 Variants of RoPE
     - A.1.2 Attention Bias
   - A.2 Context Compression
     - A.2.1 Soft Compression
     - A.2.2 Hard Compression
   - A.3 Retrieval Augmented
     - A.3.1 Retrieval Granularity
     - A.3.2 Similarity Computation
     - A.3.3 Positional Encoding
     - A.3.4 Attention Calculation
   - A.4 Attention Pattern
     - A.4.1 Sliding Window
     - A.4.2 Parallel Context
     - A.4.3 Sparse Attention
B. Appendix: Details of Evaluation
   - B.1 Data
     - B.1.1 Data Characteristics
     - B.1.2 Knowledge Leakage Issue
   - B.2 Tasks
     - B.2.1 Question Answering
     - B.2.2 Needle-in-a-Haystack
     - B.2.3 Statistical Tasks
     - B.2.4 Code
     - B.2.5 In-Context Learning
     - B.2.6 Text Generation
     - B.2.7 Other Tasks
   - B.3 Metrics
     - B.3.1 Algorithmic Metrics
     - B.3.2 Model-based Metrics
     - B.3.3 LLM-based Metrics
