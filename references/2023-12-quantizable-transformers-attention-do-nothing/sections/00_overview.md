# Overview

**Title:** Quantizable Transformers: Removing Outliers by Helping Attention Heads Do Nothing

**Authors:** Yelysei Bondarenko, Markus Nagel, Tijmen Blankevoort

**Affiliations:**
- Qualcomm AI Research (an initiative of Qualcomm Technologies, Inc.)
- Amsterdam, The Netherlands

**Contact:** {ybond, markusn, tijmen}@qti.qualcomm.com

**Venue:** 37th Conference on Neural Information Processing Systems (NeurIPS 2023)

**Date:** 9 Nov 2023 (arXiv v2: 2306.12929v2)

**Source code:** https://github.com/qualcomm-ai-research/outlier-free-transformers

## Abstract

> "Transformer models have been widely adopted in various domains over the last years, and especially large language models have advanced the field of AI significantly. Due to their size, the capability of these networks has increased tremendously, but this has come at the cost of a significant increase in necessary compute. Quantization is one of the most effective ways to reduce the computational time and memory consumption of neural networks. Many studies have shown, however, that modern transformer models tend to learn strong outliers in their activations, making them difficult to quantize. To retain acceptable performance, the existence of these outliers requires activations to be in higher bitwidth or the use of different numeric formats, extra fine-tuning, or other workarounds. We show that strong outliers are related to very specific behavior of attention heads that try to learn a "no-op" or just a partial update of the residual. To achieve the exact zeros needed in the attention matrix for a no-update, the input to the softmax is pushed to be larger and larger during training, causing outliers in other parts of the network. Based on these observations, we propose two simple (independent) modifications to the attention mechanism - *clipped softmax* and *gated attention*. We empirically show that models pre-trained using our methods learn significantly smaller outliers while maintaining and sometimes even improving the floating-point task performance. This enables us to quantize transformers to full INT8 quantization of the activations without any additional effort. We demonstrate the effectiveness of our methods on both language models (BERT, OPT) and vision transformers. Our source code is available at https://github.com/qualcomm-ai-research/outlier-free-transformers." [p. 1]

## Section Headings

1. Introduction
2. Background and related work
3. Outlier analysis
4. Method
   - 4.1 Clipped softmax
   - 4.2 Gated attention
5. Experiments
   - 5.1 The impact of clipped softmax hyperparameters ($\gamma$ and $\zeta$)
   - 5.2 Clipped softmax $\gamma$ vs. sequence length
   - 5.3 The impact of bias initialization in gated attention
   - 5.4 Main results
   - 5.5 Qualitative results
6. Discussion
7. Conclusions
A. Additional graphs from outlier analysis
   - A.1 BERT
   - A.2 ViT
B. Detailed results
   - B.1 Gating architectures
   - B.2 BERT
   - B.3 OPT
   - B.4 ViT
   - B.5 The impact of clipped softmax hyperparameters ($\gamma$ and $\zeta$) on ViT
   - B.6 Fine-tuning experiment
   - B.7 Low-bit quantization results
C. Experimental details
   - C.1 BERT
   - C.2 OPT pre-training
   - C.3 ViT pre-training
   - C.4 Quantization settings
D. Compute cost
