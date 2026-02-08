# Overview

**Title:** LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens

**Authors:** Yiran Ding*, Li Lyna Zhang, Chengruidong Zhang, Yuanyuan Xu*, Ning Shang, Jiahang Xu, Fan Yang, Mao Yang

**Affiliations:**
- Microsoft Research
- *Yiran Ding: Hangzhou Dianzi University (work done during internship)
- *Yuanyuan Xu: University of Science and Technology of China

**Correspondence:** Li Lyna Zhang <lzhani@microsoft.com>

**Venue:** arXiv:2402.13753v1 [cs.CL]

**Date:** 21 Feb 2024

**Code:** https://github.com/microsoft/LongRoPE

## Abstract

> "Large context window is a desirable feature in large language models (LLMs). However, due to high fine-tuning costs, scarcity of long texts, and catastrophic values introduced by new token positions, current extended context windows are limited to around 128k tokens. This paper introduces LongRoPE that, for the first time, extends the context window of pre-trained LLMs to an impressive 2048k tokens, with up to only 1k fine-tuning steps at within 256k training lengths, while maintaining performance at the original short context window. This is achieved by three key innovations: (i) we identify and exploit two forms of non-uniformities in positional interpolation through an efficient search, providing a better initialization for fine-tuning and enabling an 8x extension in non-fine-tuning scenarios; (ii) we introduce a progressive extension strategy that first fine-tunes a 256k length LLM and then conducts a second positional interpolation on the fine-tuned extended LLM to achieve a 2048k context window; (iii) we readjust LongRoPE on 8k length to recover the short context window performance. Extensive experiments on LLaMA2 and Mistral across various tasks demonstrate the effectiveness of our method. Models extended via LongRoPE retain the original architecture with minor modifications to the positional embedding, and can reuse most pre-existing optimizations. Code will be available at https://github.com/microsoft/LongRoPE" [p. 1]

## Section Headings

1. Introduction
2. Non-uniformity in Positional Interpolation
   - 2.1. Preliminary
   - 2.2. Study on Non-uniform Positional Interpolation
3. LongRoPE
   - 3.1. Problem Formulation
   - 3.2. Searching the Non-uniform Position Interpolation
   - 3.3. Extending LLM Context Window to 2048K
4. Experiments
   - 4.1. Setup
   - 4.2. Main Results
   - 4.3. Ablation Results
5. Related Works
6. Conclusion
Broader Impacts
A. Appendix
   - A.1. Settings
   - A.2. Additional Details on Fine-tuning
   - A.3. Additional Details on the Search
