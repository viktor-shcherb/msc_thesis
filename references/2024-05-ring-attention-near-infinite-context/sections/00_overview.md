# Overview

**Title:** Ring Attention with Blockwise Transformers for Near-Infinite Context

**Authors:** Hao Liu, Matei Zaharia, Pieter Abbeel

**Affiliations:**
- Hao Liu — UC Berkeley (hao.liu@cs.berkeley.edu)
- Matei Zaharia — UC Berkeley
- Pieter Abbeel — UC Berkeley

**Venue:** Preprint (arXiv:2310.01889v4)

**Date:** 27 Nov 2023

**Code:** https://github.com/lhao499/llm_large_context

## Abstract

> "Transformers have emerged as the architecture of choice for many state-of-the-art AI models, showcasing exceptional performance across a wide range of AI applications. However, the memory demands imposed by Transformers limit their ability to handle long sequences, thereby posing challenges in utilizing videos, actions, and other long-form sequences and modalities in complex environments. We present a novel approach, Ring Attention with Blockwise Transformers (Ring Attention), which leverages blockwise computation of self-attention and feedforward to distribute long sequences across multiple devices while fully overlapping the communication of key-value blocks with the computation of blockwise attention. Our approach enables training and inference of sequences that are up to device count times longer than those achievable by prior memory-efficient Transformers, without resorting to approximations or incurring additional communication and computation overheads. Extensive experiments on language modeling and reinforcement learning tasks demonstrate the effectiveness of our approach in allowing millions of tokens context size and improving performance." [p. 1]

## Section Headings

1. Introduction
2. Large Context Memory Constraint
3. Ring Attention with Blockwise Parallel Transformers
4. Setting
5. Results
   - 5.1 Evaluating Max Context Size
   - 5.2 Evaluating Model Flops Utilization
   - 5.3 Impact on In Context RL Performance
   - 5.4 Impact on LLM Performance
6. Related Work
7. Conclusion
- Acknowledgments
- Appendix A: Code
- Appendix B: Experiment Details
  - B.1 Evaluation of context length
  - B.2 Evaluation of MFU
  - B.3 Evaluation on line retrieval
- Appendix C: Inference requirement
- Appendix D: Training FLOPs Scaling of Context Size
