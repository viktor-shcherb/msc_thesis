# Overview

**Title:** InfiniteBench: Extending Long Context Evaluation Beyond 100K Tokens

**Authors:** Xinrong Zhang, Yingfa Chen, Shengding Hu, Zihang Xu, Junhao Chen, Moo Khai Hao, Xu Han, Zhen Leng Thai, Shuo Wang, Zhiyuan Liu, Maosong Sun

**Affiliations:**
- Department of Computer Science and Technology, Tsinghua University, Beijing, China

**Contact:** zxr19@mails.tsinghua.edu.cn

**Venue:** arXiv preprint (arXiv:2402.13718v3)

**Date:** 24 Feb 2024

**Code:** https://github.com/OpenBMB/InfiniteBench
**Data:** https://huggingface.co/datasets/xinrongzhang2022/InfiniteBench

## Abstract

> "Processing and reasoning over long contexts is crucial for many practical applications of Large Language Models (LLMs), such as document comprehension and agent construction. Despite recent strides in making LLMs process contexts with more than 100K tokens, there is currently a lack of a standardized benchmark to evaluate this long-context capability. Existing public benchmarks typically focus on contexts around 10K tokens, limiting the assessment and comparison of LLMs in processing longer contexts. In this paper, we propose InfiniteBench, the first LLM benchmark featuring an average data length surpassing 100K tokens. InfiniteBench comprises synthetic and realistic tasks spanning diverse domains, presented in both English and Chinese. The tasks in InfiniteBench are designed to require well understanding of long dependencies in contexts, and make simply retrieving a limited number of passages from contexts not sufficient for these tasks. In our experiments, based on InfiniteBench, we evaluate the state-of-the-art proprietary and open-source LLMs tailored for processing long contexts. The results indicate that existing long context LLMs still require significant advancements to effectively process 100K+ context. We further present three intriguing analyses regarding the behavior of LLMs processing long context. Our code and data is released." [p. 1]

## Section Headings

1. Introduction
2. Related Work
3. InfiniteBench
   - 3.1 Realistic Context
     - 3.1.1 Novel
     - 3.1.2 Dialogue
     - 3.1.3 Code
   - 3.2 Synthetic Context
     - 3.2.1 Retrieve
     - 3.2.2 Code
     - 3.2.3 Math
4. Experiments
   - 4.1 Baselines
   - 4.2 Experimental Setup
   - 4.3 Main Result
5. Analysis
   - 5.1 Length Ablation
   - 5.2 Lost in the Middle
   - 5.3 Context Recalling
6. Conclusions
   - Limitations
   - Ethics Statement
References
