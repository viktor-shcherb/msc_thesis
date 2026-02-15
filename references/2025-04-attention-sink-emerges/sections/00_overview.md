# Overview

**Title:** When Attention Sink Emerges in Language Models: An Empirical View

**Authors:** Xiangming Gu^1,2, Tianyu Pang^1, Chao Du^1, Qian Liu^1, Fengzhuo Zhang^1,2, Cunxiao Du^1, Ye Wang^1,2, Min Lin^1

**Affiliations:**
- ^1 Sea AI Lab, Singapore
- ^2 National University of Singapore

**Contact:** {guxm, tianyupang, duchao, liuqian, zhangfz, ducx, linmin}@sea.com; wangye@comp.nus.edu.sg

**Venue:** Published as a conference paper at ICLR 2025

**Code:** https://github.com/sail-sg/Attention-Sink

**Abstract:**

> Auto-regressive Language Models (LMs) assign significant attention to the first token, even if it is not semantically important, which is known as **attention sink**. This phenomenon has been widely adopted in applications such as streaming/long context generation, KV cache optimization, inference acceleration, model quantization, and others. Despite its widespread use, a deep understanding of attention sink in LMs is still lacking. In this work, we first demonstrate that attention sink exist universally in auto-regressive LMs with various inputs, even in small models. Furthermore, attention sink is observed to emerge during the LM pre-training, motivating us to investigate how optimization, data distribution, loss function, and model architecture in LM pre-training influence its emergence. We highlight that attention sink emerges after effective optimization on sufficient training data. The sink position is highly correlated with the loss function and data distribution. Most importantly, we find that attention sink acts more like key biases, *storing extra attention scores*, which could be non-informative and not contribute to the value computation. We also observe that this phenomenon (at least partially) stems from tokens' inner dependence on attention scores as a result of softmax normalization. After relaxing such dependence by replacing softmax attention with other attention operations, such as sigmoid attention without normalization, attention sinks do not emerge in LMs up to 1B parameters. The code is available at https://github.com/sail-sg/Attention-Sink.

## Section Headings

1. Introduction [p. 1]
2. Preliminaries on LMs and attention sink [p. 2-3]
3. Properties of attention sink [p. 4-6]
   - 3.1 The first token acts as biases [p. 4]
   - 3.2 Measuring attention sink [p. 4-5]
   - 3.3 Attention sink under different inputs [p. 5]
   - 3.4 Attention sink under different LMs [p. 5]
4. Effects of optimization on attention sink [p. 5-6]
5. Effects of data distribution $p_{\text{Data}}$ on attention sink [p. 6]
6. Effects of loss function $\mathcal{L}$ on attention sink [p. 7]
7. Effects of model architecture $p_\theta$ on attention sink [p. 7-10]
   - 7.1 Positional embedding [p. 7-8]
   - 7.2 Pre-norm and post-norm structure [p. 8]
   - 7.3 Attention biases [p. 8-9]
   - 7.4 Attention operation [p. 9-10]
8. Future work [p. 10]
References [p. 11-14]
A. Related Work [p. 15]
   - A.1 Attention sink phenomenon
   - A.2 Attention sink and activation outliers
   - A.3 Understanding and mitigate attention sink
   - A.4 Applications of attention sink
B. Detailed formulations of positional embedding [p. 16]
C. Attention sink in open-sourced LMs [p. 17-25]
   - C.1 How positional embedding relates to attention sink
   - C.2 Attention sink under different data domains
   - C.3 Attention sink under different pre-trained LMs
   - C.4 Huggingface links for open-sourced LMs
D. More experiments in LM pre-training [p. 26-30]
   - D.1 Optimization
   - D.2 Data distribution
   - D.3 FFN design
   - D.4 Attention design
E. More experiments in LM after pre-training [p. 31]
