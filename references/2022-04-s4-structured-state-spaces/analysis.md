---
title: "Efficiently Modeling Long Sequences with Structured State Spaces"
authors: "Gu, Goel, Ré"
year: 2022
venue: "ICLR 2022"
paper_type: conference-paper
categories: ["state-space-models", "architecture", "attention-efficiency"]
scope: ["long-range dependencies", "sequence modeling", "efficient computation"]
benchmarks_used: ["lra", "perplexity-wikitext103"]
models_introduced: ["s4"]
models_evaluated: ["transformer-base", "longformer-base", "bigbird-base", "linear-transformer"]
key_claims:
  - id: C1
    claim: "S4 achieves state-of-the-art on all six Long Range Arena tasks, averaging 86.09% compared to less than 60% for all baselines"
    evidence: "Table 4, Section 4.2"
    status: supported
    scope: "LRA benchmark, sequence lengths 1K-16K, single A100 GPU"
    magnitude: "86.09% average vs 59.37% best baseline (Luna-256), +26.72 points"
  - id: C2
    claim: "S4 is the first model to solve the Path-X task (length 16384), achieving 96.35% accuracy compared to 50% random guessing for all prior work"
    evidence: "Table 4, Section 4.2"
    status: supported
    scope: "Path-X task only, length 16384"
    magnitude: "96.35% vs 50% random guessing, +46.35 points"
  - id: C3
    claim: "S4 reduces computation from O(N^2 L) to O-tilde(N+L) and memory from O(NL) to O(N+L) compared to LSSL"
    evidence: "Table 2, Section 3.3, Theorem 3"
    status: supported
    scope: "Theoretical complexity for DPLR matrices; empirical benchmarks at dimensions 128-512"
    magnitude: "29.6x faster and 392x less memory at dimension 512 (Table 2)"
  - id: C4
    claim: "S4 achieves 91.13% accuracy on sequential CIFAR-10 without data augmentation or 2D inductive bias, competitive with 2D ResNet-18"
    evidence: "Table 6, Section 4.3"
    status: supported
    scope: "Sequential CIFAR-10, no 2D inductive bias, 6 layers H=1024"
    magnitude: "91.13% vs 89.46% ResNet-18 (no augmentation); 93.16% vs 95.62% (with augmentation)"
  - id: C5
    claim: "S4 performs autoregressive generation 60x faster than Transformers on both CIFAR-10 and WikiText-103"
    evidence: "Tables 7 and 8, Section 4.3"
    status: supported
    scope: "CIFAR-10 density estimation and WikiText-103 language modeling generation"
    magnitude: "60x faster: 48K vs 0.8K tokens/sec on WikiText-103; 20.84 vs 0.32 images/sec on CIFAR-10 (base model 65.1x)"
  - id: C6
    claim: "S4 achieves 98.32% on raw speech classification (SC10), outperforming all baselines including specialized speech CNNs with 90x fewer parameters"
    evidence: "Table 5, Section 4.2"
    status: supported
    scope: "SC10 subset of Speech Commands, raw audio length 16000, single GPU"
    magnitude: "98.32% vs 96.25% WaveGAN-D (90x more parameters) vs 71.66% CKConv"
  - id: C7
    claim: "S4 outperforms the Informer on 40/50 time-series forecasting settings across 5 tasks"
    evidence: "Table 9, Section 4.3, Tables 13-14"
    status: supported
    scope: "Univariate long-sequence forecasting on ETTh1, ETTh2, ETTm1, Weather, ECL"
    magnitude: "40/50 settings best; e.g. 37% MSE reduction on 30-day weather forecasting"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: complementary
    detail: "S4 provides an alternative to Transformer attention for sequence modeling with superior long-range dependency handling"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer uses sparse attention for long sequences; S4 uses state space models, achieving better LRA results"
  - target: 2020-12-bigbird-sparse-attention
    type: complementary
    detail: "BigBird uses sparse attention patterns; S4 outperforms it on all LRA tasks by large margins (86.09% vs 54.17% average)"
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: complementary
    detail: "RWKV proposes a linear RNN alternative to Transformers; S4 is the foundational SSM work that inspired the broader non-attention sequence model line"
  - target: 2023-07-retnet-retentive-network
    type: complementary
    detail: "RetNet uses retention with exponential decay rather than structured state spaces; both provide alternatives to Transformer attention"
  - target: 2023-07-hyena-hierarchy-long-convolutions
    type: extended-by
    detail: "Hyena generalizes S4's long convolution approach by replacing SSM-parameterized filters with FFN-based implicit convolutions, matching Transformer quality without attention"
open_questions:
  - question: "Can S4 be combined with attention mechanisms to improve performance on tasks where Transformers excel (e.g., language modeling)?"
    addressed_by: null
  - question: "How does the HiPPO initialization specifically enable learning of long-range dependencies, given the large generalization gap despite similar training accuracy?"
    addressed_by: null
  - question: "Can the NPLR parameterization be extended to other structured matrices beyond HiPPO?"
    addressed_by: null
  - question: "How does S4 scale to modern LLM sizes (billions of parameters)?"
    addressed_by: null
---
# Efficiently Modeling Long Sequences with Structured State Spaces

**Authors:** Albert Gu, Karan Goel, Christopher Ré (Stanford University)
**Date:** April 2022, ICLR 2022 (Outstanding Paper Honorable Mention), arXiv:2111.00396

---

## Core Research Problem

Modeling long-range dependencies (LRDs) in sequences is a central challenge for sequence models. Real-world time-series data often requires reasoning over tens of thousands of time steps, yet conventional models struggle:

1. **RNNs** suffer from vanishing/exploding gradients despite specialized variants (orthogonal RNNs, Lipschitz RNNs) (Section 1).
2. **CNNs** require dilated convolutions to increase receptive field, which still struggle on very long sequences (Section 1).
3. **Transformers** have quadratic complexity O(L^2) in sequence length L, and efficient variants (Performer, Linear Transformer, BigBird) still perform poorly on challenging LRD benchmarks (Section 1).

The Long Range Arena (LRA) benchmark (Tay et al., 2021) highlights these limitations: no existing model performs better than random guessing on the Path-X task (length 16384) (Section 1, Table 4).

A promising alternative is the **state space model (SSM)** (Equation 1):

> x'(t) = Ax(t) + Bu(t)
> y(t) = Cx(t) + Du(t)

Gu et al. (2020) showed that SSMs with special **HiPPO matrices** A can capture LRDs mathematically and empirically. Their Linear State Space Layer (LSSL) (Gu et al., 2021) achieved 98% on sequential MNIST (vs 60% with random A). However, the LSSL has **prohibitive computational requirements**: O(N^2 L) operations and O(NL) memory for state dimension N and sequence length L, compared to a theoretical lower bound of Omega(N+L) (Section 1).

**The core challenge is making SSMs computationally practical while preserving their theoretical strengths for long-range dependencies.**

---

## Problem Solutions

S4 (Structured State Space) introduces a new parameterization that reduces SSM computation to near-optimal complexity while maintaining the benefits of HiPPO initialization.

1. **Normal Plus Low-Rank (NPLR) decomposition.** The HiPPO matrix A can be written as A = V Lambda V* - PQ^T where V is unitary, Lambda is diagonal, and P, Q are low-rank factors (rank 1 or 2) (Theorem 1).

2. **Generating function approach.** Instead of computing the SSM convolution kernel K-bar directly, S4 computes its truncated generating function at roots of unity, then recovers K-bar via inverse FFT (Section 3.2).

3. **Woodbury identity.** The generating function involves matrix inverses of A. For DPLR (Diagonal Plus Low-Rank) matrices, the Woodbury identity reduces the inverse to operations on the diagonal component (Section 3.2, Proposition 4).

4. **Cauchy kernel reduction.** The final computation reduces to evaluating a Cauchy kernel 1/(omega_j - lambda_k), a well-studied problem with stable O((N+L)log(N+L)) algorithms via the Fast Multipole Method (Section 3.3, Proposition 5).

---

## Approach Details

### Method

**State Space Model (SSM).** The continuous-time SSM (Equation 1) maps a 1-D input signal u(t) to an N-dimensional latent state x(t), then projects to a 1-D output y(t):

> x'(t) = Ax(t) + Bu(t)
> y(t) = Cx(t)

The term Du(t) is omitted as it is a simple skip connection (Section 2.1).

**HiPPO Matrix.** The key to SSM performance on LRDs is the HiPPO matrix (Equation 2):

> A_nk = -[(2n+1)^(1/2)(2k+1)^(1/2) if n > k; n+1 if n = k; 0 if n < k]

This matrix allows the state x(t) to memorize the history of the input u(t) through optimal polynomial projections. Using HiPPO improved sequential MNIST from 60% to 98% over a random A matrix (Section 2.2).

**Discretization.** To apply SSMs to discrete sequences, the continuous-time model is discretized using the bilinear method with step size Delta (Equation 3):

> x_k = A-bar x_{k-1} + B-bar u_k
> y_k = C-bar x_k

where A-bar = (I - Delta/2 * A)^(-1)(I + Delta/2 * A), B-bar = (I - Delta/2 * A)^(-1) Delta B, C-bar = C (Section 2.3).

**Convolutional View.** The discrete SSM can be written as a convolution (Equation 4):

> y = K-bar * u

where the SSM convolution kernel is K-bar = (C-bar B-bar, C-bar A-bar B-bar, ..., C-bar A-bar^(L-1) B-bar) in R^L (Equation 5). This can be computed with FFTs provided K-bar is known -- computing K-bar efficiently is the focus of the theoretical contributions (Section 2.4).

**The S4 parameterization.** By Theorem 1, all HiPPO matrices have a Normal Plus Low-Rank (NPLR) representation:

> A = V Lambda V* - PQ^T = V(Lambda - (V*P)(V*Q)*)V*

for unitary V in C^(NxN), diagonal Lambda, and low-rank factors P, Q in R^(Nxr) with r = 1 or r = 2. In particular, the HiPPO-LegS matrix (Equation 2) is NPLR with r = 1 (Section 3.2, Theorem 1).

### Key Technical Components

**Algorithm 1 (S4 Convolution Kernel).** The algorithm proceeds in five steps (Section 3.3):

1. Compute C-tilde = (I - A-bar^L)* C to truncate the SSM generating function to length L
2. Evaluate a 2x2 block of Cauchy kernels at roots of unity omega: [[k_00, k_01], [k_10, k_11]] = [C-tilde, Q]* (2/Delta * (1-omega)/(1+omega) - Lambda)^(-1) [B, P]
3. Apply the Woodbury identity to correct for the low-rank term: K-hat(omega) = 2/(1+omega) [k_00 - k_01(1 + k_11)^(-1) k_10]
4. Evaluate K-hat at all L-th roots of unity
5. Apply inverse FFT to recover K-bar

**Architecture.** An S4 layer defines a map from R^L to R^L. For H hidden features, H independent S4 copies are used with a position-wise linear layer for mixing, yielding O(H^2) + O(HN) parameters per layer. Nonlinear activations are inserted between layers. The resulting deep S4 model is analogous to a **depthwise-separable CNN with global convolution kernels** (Section 3.4).

**Parameters.** An S4 layer is parameterized by Lambda, P, Q, B, C in C^(Nx1), comprising **5N trainable parameters**. The state size N is typically set to 64 (Section 3.4, Appendix D.2).

**Dual computation modes.** S4 can operate as either (1) a convolution for efficient parallel training or (2) a recurrence for efficient autoregressive inference with constant memory per step. This flexibility comes from the SSM's mathematical structure (Figure 1, Table 1).

### Theoretical Analysis

**Lemma 3.1 (Conjugation Equivalence).** SSMs (A, B, C) and (V^(-1) A V, V^(-1) B, C V) compute the same operator u -> y, but with a change of basis by V in the state x. This motivates putting A into a canonical form (Section 3.1).

**Lemma 3.2 (Diagonalization Instability).** The HiPPO matrix is diagonalized by V_ij = C(i+j, i-j), which has entries of magnitude up to 2^(4N/3). This exponential growth makes naive diagonalization numerically infeasible (Section 3.1).

**Theorem 1 (NPLR Structure).** All HiPPO matrices (LegS, LegT, LagT) have a Normal Plus Low-Rank representation with rank r = 1 or r = 2. The proof is constructive: for HiPPO-LegS, adding the rank-1 matrix (1/2)(2n+1)^(1/2)(2k+1)^(1/2) yields (1/2)I + S where S is skew-symmetric (hence normal) (Appendix C.1).

**Theorem 2 (S4 Recurrence).** One step of the discrete SSM recurrence can be computed in **O(N) operations** because the inverse of a DPLR matrix is also DPLR (via the Woodbury identity). The discretized A-bar = A_1 A_0 is a product of two DPLR matrices (Section 3.3, Appendix C.2).

**Theorem 3 (S4 Convolution).** Computing the SSM convolution filter K-bar requires only **O-tilde(N+L) operations** and **O(N+L) space** by reduction to 4 Cauchy multiplies. This is near-optimal given the Omega(N+L) lower bound (Section 3.3, Appendix C.3).

### Experimental Setup

**Long Range Arena (Section 4.2).** Six tasks with lengths 1K-16K steps:
- ListOps (2K): parsing nested lists
- Text (4K): byte-level text classification
- Retrieval (4K): document similarity
- Image (1K): sequential CIFAR-10 classification
- Pathfinder (1K): path connectivity in images
- Path-X (16K): same as Pathfinder but 128x128 images

Model: 6 layers, H in {64, 128, 256, 512}, N = 64. Optimizer: AdamW with plateau LR schedule; reduced LR (max 0.001) for HiPPO parameters (Lambda, P, Q, B, C, Delta). Hardware: single A100 GPU (Table 11).

**Speech Commands (Section 4.2).** SC10 subset: 10-class classification of spoken words. Raw audio (length 16000) following Romero et al. (2021). Model: 6 layers, H = 128 (Table 11).

**WikiText-103 (Section 4.3).** Language modeling benchmark. Architecture: 16 blocks of S4 layers alternated with feedforward layers, H = 1024, adaptive embeddings with cutoffs 20000/40000/200000. Two S4 layers per block with GLU activation. Training: AdamW, cosine LR schedule (max 800K steps), LR 0.0005, batch size 1 per GPU, context 8192, dropout 0.25, weight decay 0.1, 8x A100 GPUs (Appendix D.3.2).

**CIFAR-10 Density Estimation (Section 4.3).** Autoregressive image modeling (3072 RGB subpixels). UNet-style backbone with S4 + feedforward blocks, downsampling rates 3, 4, 4. Base model: B=8 blocks, H=128. Large model: B=16 blocks, H=192. LAMB optimizer, LR 0.005. Softmax loss with input embeddings (Appendix D.3.1).

**Sequential Image Classification (Section 4.3).** sMNIST, pMNIST, sCIFAR-10. For CIFAR-10: 6 layers, H=1024, LayerNorm, dropout 0.25 (Table 11).

**Time-Series Forecasting (Section 4.3).** 5 datasets: ETTh1, ETTh2, ETTm1, Weather, ECL. S4 treats forecasting as a masked sequence-to-sequence transformation. Context window concatenated with mask of forecast length; last F outputs used as predictions (Appendix D.3.5, Figure 5).

**Reproducibility.** Code publicly available at https://github.com/HazyResearch/state-spaces. All models trained on single or 8x A100 GPUs. Updated results for LRA and WikiText-103 documented in Appendix D.5. Single run per configuration, no variance reported (limited evidence for statistical significance).

### Key Results

**Long Range Arena (Table 4):**

| Model | ListOps | Text | Retrieval | Image | Pathfinder | Path-X | Avg |
|---|---|---|---|---|---|---|---|
| Transformer | 36.37 | 64.27 | 57.46 | 42.44 | 71.40 | X | 53.66 |
| BigBird | 36.05 | 64.02 | 59.29 | 40.83 | 74.87 | X | 54.17 |
| Performer | 18.01 | 65.40 | 53.82 | 42.77 | 77.05 | X | 51.18 |
| Luna-256 | 37.25 | 64.57 | 79.29 | 47.38 | 77.72 | X | 59.37 |
| **S4** | **59.60** | **86.82** | **90.90** | **88.65** | **94.20** | **96.35** | **86.09** |

X denotes failure on the task (random guessing or inability to run). These are the updated results (Table 10 shows original S4 results averaged 80.48%; updated results are 86.09%).

- S4 outperforms all 14 baselines on all 6 tasks (Table 10 has full results for all 14 Transformer variants plus follow-up models)
- S4 is the **first model to solve Path-X** (96.35% vs 50% random for all prior work)
- Average improvement: +26.72 points over best baseline (Luna-256 at 59.37%)
- Evidence covers 6 tasks across text, image, and structural reasoning (strong evidence for breadth)

**Efficiency Benchmarks (Table 2, S4 vs LSSL):**

| Dim | LSSL Speed (ms) | S4 Speed (ms) | LSSL Memory (MB) | S4 Memory (MB) |
|---|---|---|---|---|
| 128 | 9.32 | 4.77 | 222.1 | 5.3 |
| 256 | 20.6 | 3.07 | 1685 | 12.6 |
| 512 | 140.7 | 4.75 | 13140 | 33.5 |

- At dimension 512: **29.6x faster, 392x less memory** (Table 2)
- S4 speed stays nearly constant across dimensions (4.75-4.77 ms) while LSSL scales quadratically

**Efficiency Benchmarks (Table 3, S4 vs Efficient Transformers):**

| Model | Speed (L=1024) | Mem (L=1024) | Speed (L=4096) | Mem (L=4096) |
|---|---|---|---|---|
| Transformer | 1x | 1x | 1x | 1x |
| Performer | 1.23x | 0.43x | 3.79x | 0.086x |
| Linear Trans. | **1.58x** | **0.37x** | **5.35x** | **0.067x** |
| S4 | **1.58x** | 0.43x | 5.19x | 0.091x |

- S4 is competitive with the most efficient Transformer variants (Linear Transformer, Performer) in speed and memory, while achieving dramatically better accuracy on LRA (limited evidence: parameter-matched setting only)

**Speech Commands Raw (Table 5):**

| Model | MFCC (161) | Raw (16000) | 0.5x |
|---|---|---|---|
| Transformer | 90.75 | X | X |
| CKConv | 95.3 | 71.66 | 65.96 |
| WaveGAN-D | X | 96.25 | X |
| LSSL | 93.58 | X | X |
| **S4** | 93.96 | **98.32** | **96.30** |

- S4 achieves **98.32%** on raw audio, outperforming specialized speech CNNs with **90x fewer parameters** (0.3M vs 26.3M for WaveGAN-D)
- S4 adapts to **0.5x frequency change without retraining** (96.30%), demonstrating the continuous-time advantage of SSMs (Table 5)
- All RNN and Transformer baselines fail on raw audio (>= 70% error or computationally infeasible) (limited evidence: single SC10 subset)

**Sequential Image Classification (Table 6):**

| Model | sMNIST | pMNIST | sCIFAR |
|---|---|---|---|
| Transformer | 98.9 | 97.9 | 62.2 |
| LipschitzRNN | 99.4 | 96.3 | 64.2 |
| LSSL | 99.53 | 98.76 | 84.65 |
| **S4** | **99.63** | 98.70 | **91.13** |

- Sequential CIFAR-10: **91.13%** without 2D inductive bias, competitive with ResNet-18 (89.46% without augmentation, 95.62% with augmentation vs S4's 93.16% with augmentation) (Section 4.3)
- S4 is much more robust to normalization choice: 90.46% with LayerNorm vs ResNet-18's 79.52% with LayerNorm (Section 4.3)
- Note: LSSL slightly better on pMNIST (98.76 vs 98.70)

**WikiText-103 Language Modeling (Table 8):**

| Model | Params | Test ppl | Tokens/sec |
|---|---|---|---|
| Transformer | 247M | **20.51** | 0.8K (1x) |
| TaLK Conv | 240M | 23.3 | - |
| Dynamic Conv | 255M | 25.0 | - |
| **S4** | 249M | **20.95** | **48K (60x)** |

- S4 achieves SoTA for attention-free models (within 0.44 ppl of Transformer), improving over TaLK Conv by 2.35 ppl (Table 8)
- **60x faster generation** than Transformer using recurrent mode (48K vs 0.8K tokens/sec)
- Updated from original result (21.28 ppl) by retraining with batch size 1 and context 8192 (Appendix D.5)

**CIFAR-10 Density Estimation (Table 7):**

| Model | bpd | 2D bias | Images/sec |
|---|---|---|---|
| Transformer | 3.47 | None | 0.32 (1x) |
| PixelCNN++ | 2.92 | 2D conv | 19.19 (60x) |
| PixelSNAIL | 2.85 | 2D conv + attn | 0.13 (0.4x) |
| Sparse Trans. | 2.80 | 2D sparse attn | - |
| **S4** (base) | 2.92 | **None** | **20.84 (65.1x)** |
| **S4** (large) | **2.85** | **None** | 3.36 (10.5x) |

- S4 (large) matches **PixelSNAIL at 2.85 bpd** without any 2D inductive bias (Table 7)
- S4 (base) achieves **65.1x faster generation** than Transformer while matching PixelCNN++ in bpd

**Time-Series Forecasting (Table 9, longest horizons):**

| Dataset | S4 MSE | S4 MAE | Informer MSE | Informer MAE |
|---|---|---|---|---|
| ETTh1 (720) | **0.116** | **0.271** | 0.269 | 0.435 |
| ETTh2 (720) | **0.187** | **0.358** | 0.277 | 0.431 |
| ETTm1 (672) | **0.292** | **0.466** | 0.512 | 0.644 |
| Weather (720) | **0.245** | **0.375** | 0.359 | 0.466 |
| ECL (960) | **0.432** | **0.497** | 0.582 | 0.608 |

- S4 outperforms Informer and all other baselines on **40/50 settings** across 5 univariate forecasting tasks (Tables 13-14, Appendix D.3.5)
- S4 is particularly strong on the longest forecast horizons (e.g., **37% MSE reduction** on 30-day weather forecasting)
- S4 uses a simple masked sequence-to-sequence approach vs Informer's specialized encoder-decoder architecture (Figure 5)
- Note: Informer wins on some short-horizon settings (e.g., ETTh2 horizon 24: 0.093 vs 0.095) (moderate evidence: 5 datasets, 10 horizons each)

### SSM Ablations

**HiPPO initialization is critical** (Section 4.4, Figures 3-4). On sequential CIFAR-10 with 100K parameters:

- When A is trained, all initializations (HiPPO, random, diagonal) reach near-perfect training accuracy, but **validation accuracies are separated by over 15%**: HiPPO achieves ~70% while random achieves ~55% (Figure 3).
- Random NPLR matrices still do not perform well, validating that S4's effectiveness comes from the **HiPPO initialization, not the NPLR parameterization** (Figure 4a).
- With 0.1 dropout, the full S4 method achieves **84.27% test accuracy** with just 100K parameters (Figure 4b).

---

## Limitations and Failure Modes

**Acknowledged by authors (Appendix A):**

1. **Gap to Transformers on language modeling.** S4 achieves 20.95 ppl vs 20.51 for Transformer on WikiText-103 (Table 8). The authors suggest exploring S4-attention combinations as future work.

2. **Limited to 1-D sequences.** The current formulation handles 1-D sequences; extension to higher-dimensional data (images, video) is noted as future work.

3. **Implementation uses naive O(NL) Cauchy kernel.** Although asymptotically faster algorithms exist (Proposition 5), the current implementation uses the naive O(NL) algorithm parallelized on GPUs via the pykeops library. The authors believe a dedicated CUDA implementation can be more efficient (Appendix A, Implementation).

**[Inferred] Additional limitations:**

4. **[Inferred]** HiPPO initialization is critical but poorly understood. Ablations (Section 4.4, Figure 3) show a >15 percentage point generalization gap between HiPPO and random initialization despite reaching 100% training accuracy. The mechanistic explanation for why HiPPO enables generalization remains unclear.

5. **[Inferred]** Complex-valued parameters. The NPLR representation requires complex-valued parameters (Lambda, P, Q, B, C in C^N), which introduces implementation complexity and potential numerical challenges. Follow-up work (Goel et al., 2022, reference [14]) found that S4 can suffer from numerical instabilities when A has eigenvalues on the right half-plane, requiring a fix from Lambda - PQ* to Lambda - PP* (Section 3.4).

6. **[Inferred]** Single-task hyperparameter tuning. Most experiments use task-specific hyperparameters (Table 11). The extent to which S4 can serve as a truly universal sequence model with fixed hyperparameters is not fully established.

7. **[Inferred]** No variance estimates reported. Results appear to be single runs per configuration; no confidence intervals or standard deviations are provided, limiting statistical confidence.

#### Scope and Comparability

- **What was not tested:** S4 was not evaluated at scales beyond 249M parameters, not tested on machine translation, not evaluated on non-English languages, and not tested on decoder-only language model pretraining (the WikiText-103 setup uses adaptive embeddings following a specific Transformer baseline).
- **Comparability notes:** The LRA results in Table 4 are **updated** results from follow-up papers [19, 20] with minor hyperparameter changes from the original (which averaged 80.48% in Table 10). The WikiText-103 result is also updated (original: 21.28 ppl, updated: 20.95 ppl with batch size 1, context 8192). When comparing with other papers citing S4 LRA results, the original vs updated distinction matters. The Speech Commands results use the SC10 (10-class) subset, not the full 35-class dataset; the authors recommend citing Table 11 from [19] for Speech Commands baselines (Appendix D.5).

---

## Conclusions

### Contributions

1. **NPLR parameterization for SSMs.** S4 introduces Normal Plus Low-Rank decomposition of HiPPO matrices (Theorem 1), enabling stable diagonalization and efficient computation while preserving theoretical properties for long-range dependencies. All three HiPPO variants (LegS, LegT, LagT) are shown to be NPLR with rank 1 or 2.

2. **Near-optimal computational complexity.** The S4 algorithm (Algorithm 1) achieves O-tilde(N+L) computation and O(N+L) memory (Theorem 3), matching the theoretical lower bound up to log factors. Empirically, this is a **29.6x speed improvement and 392x memory reduction** over LSSL at dimension 512 (Table 2).

3. **State-of-the-art on long-range dependency benchmarks.** S4 outperforms all prior methods on all six LRA tasks by large margins (+26.72 points average) and is the **first model to solve Path-X** at 96.35% (Table 4).

4. **Unified sequence model across modalities.** S4 achieves strong results across diverse modalities (images, text, audio, time-series) and tasks (classification, generation, forecasting) with minimal architectural changes, including: 91.13% on sequential CIFAR-10, 98.32% on raw speech, 2.85 bpd on CIFAR density estimation, 20.95 ppl on WikiText-103, and best results on 40/50 time-series forecasting settings.

5. **Efficient autoregressive generation.** By switching to its recurrent representation (Theorem 2), S4 achieves **60x faster generation** than Transformers while maintaining quality (Tables 7, 8).

6. **Continuous-time adaptability.** S4 adapts to changes in sampling frequency without retraining, achieving 96.30% at 0.5x frequency on SC10 (Table 5).

### Implications

1. **SSMs as a viable alternative to attention.** (Inference) S4 demonstrates that state space models can match or exceed Transformers on many tasks, particularly those requiring long-range reasoning, establishing SSMs as a serious competing paradigm to attention-based models.

2. **Foundation for Mamba and successors.** (Inference) S4's efficient SSM computation directly enabled follow-up work including H3, Hyena, and Mamba, which combine S4's state space formulation with input-dependent selection mechanisms.

3. **HiPPO theory is practically relevant.** The ablations (Section 4.4) confirm that the continuous-time memorization theory underlying HiPPO translates to significant empirical gains, not just theoretical elegance. The >15% generalization gap between HiPPO and random initialization (despite identical training accuracy) is strong evidence for the importance of principled initialization.

---

## Key Claims

1. **C1: S4 achieves state-of-the-art on all six LRA tasks with 86.09% average accuracy.** All baselines score below 60% (best: Luna-256 at 59.37%). The improvement is consistent across tasks spanning text, images, and structured reasoning (6 tasks, strong evidence for breadth). Evidence: Table 4, Table 10. Scope: LRA benchmark, sequence lengths 1K-16K. Magnitude: +26.72 points over best baseline. Status: **supported**.

2. **C2: S4 is the first model to solve Path-X.** All 14 prior models achieve random-guessing performance (50%) on this length-16384 task. S4 achieves 96.35%. Evidence: Table 4. Scope: Path-X task only. Magnitude: +46.35 points over random guessing. Status: **supported**.

3. **C3: S4 reduces complexity from O(N^2 L) to O-tilde(N+L).** The NPLR parameterization enables reduction to Cauchy kernel computation via the Woodbury identity. Empirically, S4 is 29.6x faster and uses 392x less memory than LSSL at dimension 512. Evidence: Table 2, Theorem 3. Scope: theoretical complexity for DPLR matrices; empirical at dimensions 128-512. Magnitude: 29.6x speed, 392x memory reduction. Status: **supported**.

4. **C4: S4 achieves 91.13% on sequential CIFAR-10 without 2D inductive bias.** This is competitive with ResNet-18 (89.46% without augmentation; 95.62% with augmentation vs S4's 93.16%). Evidence: Table 6, Section 4.3. Scope: sequential CIFAR-10, 6 layers, H=1024. Magnitude: 91.13% vs 89.46% ResNet-18 (no augmentation). Status: **supported**.

5. **C5: S4 generates 60x faster than Transformers.** Using its recurrent representation, S4 requires constant memory/computation per time step. On WikiText-103: 48K vs 0.8K tokens/sec. On CIFAR-10: 20.84 vs 0.32 images/sec (base model). Evidence: Tables 7, 8. Scope: CIFAR-10 and WikiText-103 generation. Magnitude: 60x (WikiText-103), 65.1x (CIFAR-10 base). Status: **supported**.

6. **C6: S4 achieves 98.32% on raw speech classification, outperforming specialized speech CNNs.** WaveGAN-D achieves 96.25% but with 90x more parameters (26.3M vs 0.3M) and many more architectural heuristics. Evidence: Table 5, Section 4.2. Scope: SC10 10-class subset, raw audio length 16000, single GPU. Magnitude: 98.32% vs 96.25% WaveGAN-D. Status: **supported** (single benchmark, limited evidence for generalization to broader speech tasks).

7. **C7: S4 outperforms Informer on 40/50 time-series forecasting settings.** Across 5 univariate datasets with 5 horizons each (plus 5 multivariate datasets), S4 sets the best results on 40 out of 50 settings. Evidence: Table 9, Tables 13-14. Scope: univariate long-sequence forecasting on ETTh1, ETTh2, ETTm1, Weather, ECL. Magnitude: 40/50 settings best (22/25 univariate, 18/25 multivariate). Status: **supported** (strong evidence: 50 settings across 5 tasks).

---

## Open Questions

1. **Can S4 be combined with attention to improve language modeling?** S4 approaches but does not match Transformer perplexity on WikiText-103 (20.95 vs 20.51). Hybrid architectures may capture complementary strengths. The authors explicitly note this as future work (Appendix A). **Unresolved.**

2. **Why does HiPPO initialization enable LRD learning?** The ablations show dramatic generalization gaps between HiPPO and random initialization (>15 percentage points) despite identical training accuracy. The mechanistic explanation remains unclear (Section 4.4). **Unresolved.**

3. **Can NPLR be extended to other structured matrices?** The paper focuses on the three HiPPO matrices (LegS, LegT, LagT); whether similar decompositions exist for other useful matrices is not explored. **Unresolved.**

4. **How does S4 scale to modern LLM sizes?** The largest model tested (WikiText-103) has 249M parameters. Scaling behavior to billions of parameters is not established. **Addressed by** subsequent work on H3, Hyena, and Mamba, which scale SSM-based models to larger sizes.

---

## Core References and Why They Are Referenced

### State Space Model Foundations

- **Gu et al. (2020)** -- *HiPPO: Recurrent Memory with Optimal Polynomial Projections.* Introduces the HiPPO framework and special A matrices for continuous-time memorization. S4 builds directly on this theoretical foundation; the HiPPO matrix (Equation 2) is the key to S4's LRD performance. Also provides HiPPO-RNN baseline (Table 12).

- **Gu et al. (2021)** -- *Combining Recurrent, Convolutional, and Continuous-Time Models with the LSSL.* Introduces the Linear State Space Layer showing SSMs can address LRDs. S4 solves LSSL's computational bottleneck (O(N^2 L) to O-tilde(N+L)). Also proposed a theoretically fast algorithm shown to be numerically unstable (Appendix B.2).

- **Voelker et al. (2019)** -- *Legendre Memory Units.* Derives a non-trainable SSM motivated from neuromorphic spiking models. Part of the line of work leading to HiPPO and S4. LMU baseline appears in Table 12.

### Efficient Sequence Models

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer. S4 provides an alternative to self-attention with better scaling for long sequences. Transformer is the primary baseline across all experiments.

- **Choromanski et al. (2020)** -- *Rethinking Attention with Performers.* Efficient Transformer variant using kernel approximation. S4 outperforms Performer on LRA (86.09% vs 51.18%). Performer baseline used in efficiency benchmarks (Table 3) and Speech Commands (Table 5).

- **Katharopoulos et al. (2020)** -- *Transformers Are RNNs: Fast Autoregressive Transformers with Linear Attention.* Linear Transformer enabling RNN-like inference. S4 benchmarks generation speed against this model (Table 7) and efficiency (Table 3).

### Long-Range Dependency Benchmarks

- **Tay et al. (2021)** -- *Long Range Arena: A Benchmark for Efficient Transformers.* Introduces the LRA benchmark with 6 tasks up to length 16K. S4 is the first model to solve all tasks, including Path-X. LRA serves as the primary evaluation for S4's long-range capability.

- **Arjovsky et al. (2016)** -- *Unitary Evolution Recurrent Neural Networks.* Orthogonal RNNs for addressing vanishing gradients. S4 dramatically outperforms such RNN variants on LRA and sequential image classification benchmarks.

### Numerical Methods

- **Pan (2001, 2015, 2017)** -- Works on structured matrices and Cauchy kernels. S4's core algorithm relies on fast Cauchy matrix-vector multiplication; these references establish the theoretical foundations and O((N+L)log^2(N+L)) or O((N+L)log(N+L)log(1/epsilon)) complexity (Proposition 5).

- **Woodbury (1950)** -- *Inverting Modified Matrices.* The Woodbury identity enables S4 to handle the low-rank correction in the NPLR representation efficiently, converting DPLR matrix inverses to diagonal matrix inverses (Proposition 4).

### Experimental Baselines

- **Romero et al. (2021)** -- *CKConv: Continuous Kernel Convolution for Sequential Data.* Continuous kernel CNN for long sequences. S4 outperforms CKConv on raw speech (98.32% vs 71.66%). CKConv also serves as baseline on sequential image tasks (Table 6).

- **Baevski & Auli (2018)** -- *Adaptive Input Representations for Neural Language Modeling.* Provides the Transformer baseline architecture for WikiText-103 experiments. S4 uses the same backbone with self-attention replaced by S4 layers.

- **Zhou et al. (2021)** -- *Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting.* Specialized Transformer architecture for time-series forecasting. S4 outperforms Informer on 40/50 settings using a simple masked sequence-to-sequence approach (Tables 9, 13, 14).

- **Donahue et al. (2019)** -- *Adversarial Audio Synthesis (WaveGAN).* Provides the WaveGAN discriminator baseline for raw speech classification (96.25% with 90x more parameters than S4).
