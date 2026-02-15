# Overview

## Paper Information

**Title:** Differential Transformer

**Authors:** Tianzhu Ye†‡, Li Dong*†, Yuqing Xia*†, Yutao Sun*†‡, Yi Zhu†, Gao Huang‡, Furu Wei*⋄

**Affiliations:**
- † Microsoft Research
- ‡ Tsinghua University
- * Equal contribution
- ⋄ Corresponding author

**Venue:** Published as a conference paper at ICLR 2025

**URL:** https://aka.ms/GeneralAI

## Abstract

> "Transformer tends to overallocate attention to irrelevant context. In this work, we introduce DIFF Transformer, which amplifies attention to the relevant context while canceling noise. Specifically, the differential attention mechanism calculates attention scores as the difference between two separate softmax attention maps. The subtraction cancels noise, promoting the emergence of sparse attention patterns. Experimental results on language modeling show that DIFF Transformer outperforms Transformer in various settings of scaling up model size and training tokens. More intriguingly, it offers notable advantages in practical applications, such as long-context modeling, key information retrieval, hallucination mitigation, in-context learning, and reduction of activation outliers. By being less distracted by irrelevant context, DIFF Transformer can mitigate hallucination in question answering and text summarization. For in-context learning, DIFF Transformer not only enhances accuracy but is also more robust to order permutation, which was considered as a chronic robustness issue. The results position DIFF Transformer as a highly effective and promising architecture to advance large language models."

## Section Headings

1. Introduction (p. 1)
2. Differential Transformer (p. 2)
   - 2.1 Differential Attention (p. 2)
   - 2.2 Overall Architecture (p. 4)
3. Experiments (p. 4)
   - 3.1 Language Modeling Evaluation (p. 4)
   - 3.2 Scalability Compared with Transformer (p. 5)
   - 3.3 Long-Context Evaluation (p. 5)
   - 3.4 Key Information Retrieval (p. 6)
   - 3.5 In-Context Learning (p. 7)
   - 3.6 Contextual Hallucination Evaluation (p. 8)
   - 3.7 Activation Outliers Analysis (p. 9)
   - 3.8 Ablation Studies (p. 10)
4. Conclusion (p. 10)
Acknowledgement (p. 11)
References (p. 11-14)
Appendix A: Implementation of Differential Attention (p. 15)
Appendix B: Language Modeling Evaluation (p. 16)
Appendix C: Evaluation on Mathematical Reasoning (p. 16-17)
Appendix D: Hyperparameters for Section 3.1 (p. 18)
Appendix E: Hyperparameters for Section 3.2 (p. 18)
Appendix F: Robustness of In-Context Learning (p. 19)
Appendix G: Gradient Flow of DIFF Transformer (p. 20-21)
