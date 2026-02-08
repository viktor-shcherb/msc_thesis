# Overview

**Title:** Ada-LEval: Evaluating long-context LLMs with length-adaptable benchmarks

**Authors:** Chonghua Wang^{2*}, Haodong Duan^{1\dagger}, Songyang Zhang^1, Dahua Lin^1, Kai Chen^{1\ddagger}

**Affiliations:**
- 1: Shanghai AI Laboratory
- 2: Shanghai Jiao Tong University

\* The work was done during an internship at Shanghai AI Laboratory; \dagger Project Lead; \ddagger Corresponding Author.

**Venue:** arXiv:2404.06480v2 [cs.CL]

**Date:** 10 Apr 2024

**Code:** https://github.com/open-compass/Ada-LEval

**Abstract:**
> "Recently, the large language model (LLM) community has shown increasing interest in enhancing LLMs' capability to handle extremely long documents. As various long-text techniques and model architectures emerge, the precise and detailed evaluation of models' long-text capabilities has become increasingly important. Existing long-text evaluation benchmarks, such as L-Eval and LongBench, construct long-text test sets based on open-source datasets, focusing mainly on QA and summarization tasks. These datasets include test samples of varying lengths (from 2k to 32k+) entangled together, making it challenging to assess model capabilities across different length ranges. Moreover, they do not cover the ultra-long settings (100k+ tokens) that the latest LLMs claim to achieve. In this paper, we introduce Ada-LEval, a length-adaptable benchmark for evaluating the long-context understanding of LLMs. Ada-LEval includes two challenging subsets, TSort and BestAnswer, which enable a more reliable evaluation of LLMs' long context capabilities. These benchmarks support intricate manipulation of the length of test cases, and can easily produce text samples up to 128k tokens. We evaluate 4 state-of-the-art closed-source API models and 6 open-source models with Ada-LEval. The evaluation results demonstrate the limitations of current LLMs, especially in ultra-long-context settings. Our code is available at https://github.com/open-compass/Ada-LEval." [p. 1]

## Section headings

1. Introduction
2. Related Work
   - 2.1 Long-Context Techniques
   - 2.2 Long-Context Language Models
   - 2.3 Long-Context Benchmarks
3. Ada-LEval
   - 3.1 Task Definition
   - 3.2 Source Data Collection
   - 3.3 Test Case Building
4. Evaluation Results
   - 4.1 Experiment Setup
   - 4.2 Long-Context Evaluation Results
   - 4.3 Error Breakdown
   - 4.4 Ultra-Long-Context Evaluation Results
   - 4.5 Ablation Study
     - 4.5.1 Perplexity Evaluation on TSort
     - 4.5.2 Position Bias in BestAnswer
     - 4.5.3 Scalable Position Embeddings
     - 4.5.4 Comparison with Other Long-Context Benchmarks
5. Conclusion
6. Limitations
- Acknowledgement
- Appendix A: Test Case Building Statistics
- Appendix B: Evaluation Setups
