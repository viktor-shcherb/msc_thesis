# Overview

**Title:** RoFormer: Enhanced Transformer with Rotary Position Embedding

**Authors:**
- Jianlin Su (Zhuiyi Technology Co., Ltd., Shenzhen)
- Yu Lu (Zhuiyi Technology Co., Ltd., Shenzhen)
- Shengfeng Pan (Zhuiyi Technology Co., Ltd., Shenzhen)
- Ahmed Murtadha (Zhuiyi Technology Co., Ltd., Shenzhen)
- Bo Wen (Zhuiyi Technology Co., Ltd., Shenzhen)
- Yunfeng Liu (Zhuiyi Technology Co., Ltd., Shenzhen)

**Venue:** arXiv:2104.09864v5 [cs.CL]

**Date:** November 9, 2023

**Abstract:**

> "Position encoding recently has shown effective in the transformer architecture. It enables valuable supervision for dependency modeling between elements at different positions of the sequence. In this paper, we first investigate various methods to integrate positional information into the learning process of transformer-based language models. Then, we propose a novel method named Rotary Position Embedding(RoPE) to effectively leverage the positional information. Specifically, the proposed RoPE encodes the absolute position with a rotation matrix and meanwhile incorporates the explicit relative position dependency in self-attention formulation. Notably, RoPE enables valuable properties, including the flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capability of equipping the linear self-attention with relative position encoding. Finally, we evaluate the enhanced transformer with rotary position embedding, also called RoFormer, on various long text classification benchmark datasets. Our experiments show that it consistently overcomes its alternatives. Furthermore, we provide a theoretical analysis to explain some experimental results. RoFormer is already integrated into Huggingface: https://huggingface.co/docs/transformers/model_doc/roformer." [p. 1]

**Keywords:** Pre-trained Language Models, Position Information Encoding, Pre-training, Natural Language Processing.

## Section Headings

1. Introduction
2. Background and Related Work
   - 2.1 Preliminary
   - 2.2 Absolute position embedding
   - 2.3 Relative position embedding
3. Proposed approach
   - 3.1 Formulation
   - 3.2 Rotary position embedding
     - 3.2.1 A 2D case
     - 3.2.2 General form
   - 3.3 Properties of RoPE
   - 3.4 Theoretical Explanation
     - 3.4.1 Derivation of RoPE under 2D
     - 3.4.2 Computational efficient realization of rotary matrix multiplication
     - 3.4.3 Long-term decay of RoPE
4. Experiments and Evaluation
   - 4.1 Machine Translation
     - 4.1.1 Experimental Settings
     - 4.1.2 Implementation details
     - 4.1.3 Results
   - 4.2 Pre-training Language Modeling
     - 4.2.1 Experimental Settings
     - 4.2.2 Implementation details
     - 4.2.3 Results
   - 4.3 Fine-tuning on GLUE tasks
     - 4.3.1 Experimental Settings
     - 4.3.2 Implementation details
     - 4.3.3 Results
   - 4.4 Performer with RoPE
     - 4.4.1 Implementation details
     - 4.4.2 Results
   - 4.5 Evaluation on Chinese Data
     - 4.5.1 Implementation
     - 4.5.2 Pre-training
     - 4.5.3 Downstream Tasks & Dataset
     - 4.5.4 Results
     - 4.5.5 Limitations of the work
5. Conclusions
