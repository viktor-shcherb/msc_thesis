# 2.3 Optimizer & Training Recipe [p. 11]

### Table 2

**Table 2** (p. 11): **Apertus Main Training Hyperparameters.** Our pretraining runs use the AdEMAMix optimizer with the WSD schedule. For both models, we double the global batch size in middle stages of training. More detailed hyperparameters are provided in C.4.

| Model | Optimizer | Sequence | Batch Size (Tokens) | Steps | Max LR | Tokens |
|---|---|---|---|---|---|---|
| Apertus 8B | AdEMAMix | 4096 | 4.2M -> 8.4M | 2.6M | 1.1e-4 | 15T |
| Apertus 70B | AdEMAMix | 4096 | 8.4M -> 16.8M | 1.1M | 1.0e-5 | 15T |

## Overview

[p. 11]

The authors introduce multiple changes to current pretraining recipes to prevent memorization (using the Goldfish loss; Hans et al., 2024), improve efficiency (with AdEMAMix; Pagliardini et al., 2025), and facilitate continual training (with the WSD learning rate schedule; Zhai et al., 2022; Hu et al., 2024; Hägele et al., 2024).

## Goldfish Loss for Memorization Mitigation

[p. 11]

Verbatim regurgitation of training data is a significant concern in LLMs, as it raises both copyright (Chang et al., 2023; Karamolegkou et al., 2023) and privacy risks (Huang et al., 2022). The authors adopt the goldfish loss in place of cross-entropy loss, which reduces memorisation while having minimal impact on performance in terms of perplexity and other downstream benchmarks (Hans et al., 2024). The goldfish loss computes the causal language modeling objective on only a subset of tokens based on a mask G in {0, 1}^L, and is defined as

$$\mathcal{L}(\boldsymbol{\theta}) = -\frac{1}{|G|} \sum_{i=1}^{L} G_i(x_i) \log P_{\boldsymbol{\theta}}(x_i | x_{<i}),$$

where L is the sequence length, x_i is the i-th token and x_{<i} is the preceding context. The binary mask G is randomly sampled for each batch during training. Algorithm 1 details their implementation of goldfish loss. In practice, they front-load token masking during data loading rather than during pretraining for efficiency. Through calibration detailed by Xu (2025), they identify an optimal configuration of a 2% token masking rate (k = 50) and a 50-token context window for hashing (h = 50), which effectively suppresses verbatim memorization without compromising downstream performance.^8

## AdEMAMix

[p. 11]

The authors train using the AdEMAMix optimizer (Pagliardini et al., 2025), which is a first for an LLM at this scale. AdEMAMix improves upon existing gradient-based training algorithms that rely on Exponential Moving Averages (EMA) of gradients, such as Adam (Kingma & Ba, 2014; Loshchilov & Hutter, 2017), by adding a long-term EMA in the form of an additional momentum vector. This addition better leverages old gradients for faster convergence, especially for long training runs. Their optimizer benchmarking

---
[p. 11–12 continued]

results demonstrate that AdEMAMix consistently scales more favourably with model size, training duration, and batch size than other widely used alternatives (Semenov et al., 2025).

## Learning Rate Schedule

[p. 12]

The authors employ the Warmup-Stable-Decay (WSD) learning rate (LR) schedule (Hu et al., 2024; Zhai et al., 2022). This schedule allows for continual training, since the full length does not have to be specified in advance (Hägele et al., 2024; Schaipp et al., 2025). It has already been validated to scale by various models (Liu et al., 2024; Bai et al., 2025) and allows them to continue pretraining without rewarming the learning rate in the future. They extended the initial planned training phase of 9T tokens thanks to no schedule change being required. LR warmup for both models starts from 0.1 the peak LR and is linearly increased for 16.8B tokens.

## Batch Size and Sequence Length

[p. 12]

To maximise efficiency, they employ a sequence length of 4096 tokens and an initial batch size of 1024 (4.2M tokens) and 2048 (8.4M tokens) for the 8B and 70B models, respectively. After 8T tokens for the 8B model and 4.4T for the 70B, they intentionally doubled both the number of nodes and the batch size at this stage, while keeping the learning rate unchanged. This results in minimal throughput degradation, as shown in Figure 11 of Section 6. Increasing the batch size has been shown to be beneficial in later stages of training (similar to a learning rate decrease) and increase hardware efficiency, allowing training models that perform better under the same FLOP budget (Smith et al., 2018; McCandlish et al., 2018; Merrill et al., 2025).

## Cooldown

[p. 12]

For the final learning rate annealing, the authors opt for a negative square root shape (also denoted 1-sqrt), which reliably outperforms a standard linear shape by balancing the loss landscape exploration (Hägele et al., 2024; Dremov et al., 2025). For both model sizes, the cooldown coincides with a change in the data mixture for the highest-quality sources at 13.5T consumed tokens (Section 3). The final learning rate is set to a factor of 0.1 of the respective maximum in order to facilitate downstream finetuning (i.e., long context extension and SFT) with lower initial gradient norms and instability.

**Footnotes:**
- ^8: Ablations in Appendix Figure F.3 and Table F.5.
