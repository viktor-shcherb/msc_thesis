# Overview

**Title:** Efficient Streaming Language Models with Attention Sinks

**Authors:**
- Guangxuan Xiao (Massachusetts Institute of Technology)
- Yuandong Tian (Meta AI)
- Beidi Chen (Carnegie Mellon University)
- Song Han (Massachusetts Institute of Technology; NVIDIA)
- Mike Lewis (Meta AI)

*Part of the work done during an internship at Meta AI.

**Venue:** Published as a conference paper at ICLR 2024

**Date:** arXiv v4: 7 Apr 2024 (original submission: 2309.17453)

**Code:** https://github.com/mit-han-lab/streaming-llm

## Abstract

> "Deploying Large Language Models (LLMs) in streaming applications such as multi-round dialogue, where long interactions are expected, is urgently needed but poses two major challenges. Firstly, during the decoding stage, caching previous tokens' Key and Value states (KV) consumes extensive memory. Secondly, popular LLMs cannot generalize to longer texts than the training sequence length. Window attention, where only the most recent KVs are cached, is a natural approach --- but we show that it fails when the text length surpasses the cache size. We observe an interesting phenomenon, namely *attention sink*, that keeping the KV of initial tokens will largely recover the performance of window attention. In this paper, we first demonstrate that the emergence of *attention sink* is due to the strong attention scores towards initial tokens as a 'sink' even if they are not semantically important. Based on the above analysis, we introduce StreamingLLM, an efficient framework that enables LLMs trained with a *finite length* attention window to generalize to *infinite sequence length* without any fine-tuning. We show that StreamingLLM can enable Llama-2, MPT, Falcon, and Pythia to perform stable and efficient language modeling with up to 4 million tokens and more. In addition, we discover that adding a placeholder token as a dedicated attention sink during pre-training can further improve streaming deployment. In streaming settings, StreamingLLM outperforms the sliding window recomputation baseline by up to 22.2x speedup. Code and datasets are provided in the link." [p. 1]

## Section Headings

1. Introduction
2. Related Work
3. StreamingLLM
   - 3.1 The Failure of Window Attention and Attention Sinks
   - 3.2 Rolling KV Cache with Attention Sinks
   - 3.3 Pre-Training LLMs with Attention Sinks
4. Experiments
   - 4.1 Language Modeling on Long Texts Across LLM Families and Scales
   - 4.2 Results of Pre-Training with a Sink Token
   - 4.3 Results on Streaming Question Answering with Instruction-tuned Models
   - 4.4 Ablation Studies
   - 4.5 Efficiency Results
5. Conclusion
- Reproducibility Statement
- Impact Statement
- Acknowledgements
- Appendix A: Discussions
- Appendix B: Additional Related Works
- Appendix C: Accuracy on StreamEval with Increasing Query-Answer Line Distance
- Appendix D: Long-Range Benchmark Evaluation
- Appendix E: Llama-2-7B Attention Visualization on Longer Sequences
- Appendix F: Quantitative Analysis of Attention Sinks in Long Inputs
- Appendix G: Llama-2-70B Attention Visualization
- Appendix H: Attention Sinks in Encoder Transformers
- Appendix I: Using More Sink Tokens in the Pre-Training Stage
