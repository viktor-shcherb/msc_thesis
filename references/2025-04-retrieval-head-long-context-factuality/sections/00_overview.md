# Overview

## Paper Metadata

**Title:** Retrieval Head Mechanistically Explains Long-Context Factuality

**Authors:**
- Wenhao Wu (Peking University, wayneswu@pku.edu.cn)
- Yizhong Wang (University of Washington)
- Guangxuan Xiao (MIT)
- Hao Peng (UIUC, haopeng@illinois.edu)
- Yao Fu (University of Edinburgh, yao.fu@ed.ac.uk)

**Venue/Date:** arXiv:2404.15574v1 [cs.CL] 24 Apr 2024

**URL:** https://github.com/nightdessert/Retrieval_Head

## Abstract

> Despite the recent progress in long-context large language models (LLMs), it remains elusive how those transformer-based language models acquire the capability to retrieve relevant information from arbitrary locations within the long context. This paper aims to address this question. Our systematic investigation across 4 model families, 6 model scales, and 3 types of finetuning reveals that a special type of attention heads are largely responsible for retrieving information from long context, which we dub *retrieval heads*. We identify important and intriguing properties of retrieval heads: (1) *universal*: all the explored models with long-context capability have a set of retrieval heads; (2) *sparse*: only a small portion (less than 5%) of the attention heads are retrieval. (3) *intrinsic*: retrieval heads already exist in models pretrained on short context. When extending the context length to 32-128K by continual pretraining, it is still the same set of heads that perform information retrieval. (4) *dynamically activated*: take Llama-2 7B for example, 12 retrieval heads always attend to the required information no matter how the context is changed. The rest of the retrieval heads are activated in different contexts. (5) *causal*: completely pruning retrieval heads leads to failure in retrieving relevant information and results in hallucination, while pruning random non-retrieval heads does not affect the model's retrieval ability. We further show that retrieval heads strongly influence chain-of-thought (CoT) reasoning, where the model needs to frequently refer back the question and previously-generated context. Conversely, tasks where the model directly generates the answer using its intrinsic knowledge are less impacted by masking out retrieval heads. These observations collectively explain which internal part of the model seeks information from the input tokens. We believe our insights on retrieval heads foster future research on reducing hallucination, improving reasoning, and compressing the KV cache.

## Section Headings

- Abstract
- 1 Introduction
- 2 Detecting Retrieval Head
- 3 Basic Properties of Retrieval Heads
  - 3.1 Universal and Sparse
  - 3.2 Dynamically Activated Based on Tokens and Contexts
  - 3.3 Intrinsic
- 4 Influence on Downstream Tasks
  - 4.1 Retrieval Heads Explains Factuality in Needle-in-a-Haystack
  - 4.2 Influence on Extractive QA
  - 4.3 Chain-of-Thought Reasoning also Requires Retrieval Heads
- 5 Discussions
- 6 Conclusions
- References
