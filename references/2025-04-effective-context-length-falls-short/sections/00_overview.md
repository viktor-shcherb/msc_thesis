# Overview

**Title:** Why Does the Effective Context Length of LLMs Fall Short?

**Authors:** Chenxin An¹'*, Jun Zhang², Ming Zhong³, Lei Li¹, Shansan Gong¹, Yao Luo², Jingjing Xu², Lingpeng Kong¹

**Affiliations:**
- ¹ The University of Hong Kong
- ² ByteDance Inc.
- ³ University of Illinois Urbana-Champaign

*Work done during internship at ByteDance Inc.

**Venue/Date:** arXiv:2410.18745v1 [cs.CL] 24 Oct 2024

**Code:** https://github.com/HKUNLP/STRING

## Abstract

> "Advancements in distributed training and efficient attention mechanisms have significantly expanded the context window sizes of large language models (LLMs). However, recent work reveals that the effective context lengths of open-source LLMs often fall short, typically not exceeding half of their training lengths. In this work, we attribute this limitation to the left-skewed frequency distribution of relative positions formed in LLMs pretraining and post-training stages, which impedes their ability to effectively gather distant information. To address this challenge, we introduce ShifTed Rotray position embeddING (STRING). STRING shifts well-trained positions to overwrite the original ineffective positions during inference, enhancing performance within their existing training lengths. Experimental results show that without additional training, STRING dramatically improves the performance of the latest large-scale models, such as Llama3.1 70B and Qwen2 72B, by over 10 points on popular long-context benchmarks RULER and InfiniteBench, establishing new state-of-the-art results for open-source LLMs. Compared to commercial models, Llama 3.1 70B with STRING even achieves better performance than GPT-4-128K and clearly surpasses Claude 2 and Kimi-chat." [p. 1]

## Section Headings

- 1 Introduction
- 2 Left-Skewed Position Frequency Distribution
  - 2.1 Position Embeddings in LLMs
  - 2.2 Relative Position Matrix and Position Frequency
- 3 A Probing Experiment on Position Frequency and Model Effective Length
- 4 Shifted Rotary Position Embedding
  - 4.1 Manipulating the Position Matrix
  - 4.2 Main Results of STRING
- 5 Related Work
- 6 Conclusion
- References
- A Appendix
  - A.1 Applying STRING on Llama3.1 128K
  - A.2 Pretraining Setup
  - A.3 Efficiency Test of STRING
  - A.4 Limitations
  - Algorithm 2: Pseudocode of merge_diag_shifted
  - Table 4: Needle-in-a-Haystack Performance Across Document Depths
  - Table 5: Needle-in-a-Haystack Input Format
  - Table 6: Case Study - QA on Llama3 Report (Section 3 Questions)
  - Table 7: Case Study - QA on Llama3 Report (Section 4 Questions)
