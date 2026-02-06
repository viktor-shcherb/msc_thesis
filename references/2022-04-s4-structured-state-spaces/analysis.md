---
title: "Efficiently Modeling Long Sequences with Structured State Spaces"
authors: "Gu, Goel, Ré"
year: 2022
venue: "ICLR 2022"
paper_type: conference-paper
categories: ["state-space-models", "architecture", "attention-efficiency"]
scope: ["long-range dependencies", "sequence modeling", "efficient computation"]
benchmarks_used: ["lra", "perplexity-wikitext103", "enwik8"]
models_introduced: ["s4"]
models_evaluated: ["transformer-base", "longformer-base", "bigbird-base"]
key_claims:
  - id: C1
    claim: "S4 achieves state-of-the-art on all six Long Range Arena tasks, averaging 86.09% compared to less than 60% for all baselines"
    evidence: "Table 4, Section 4.2"
    status: supported
    scope: "LRA benchmark, sequence lengths 1K-16K"
    magnitude: "26+ percentage points over best baseline"
  - id: C2
    claim: "S4 is the first model to solve the Path-X task (length 16384), achieving 96.35% accuracy compared to 50% random guessing for all prior work"
    evidence: "Table 4, Section 4.2"
    status: supported
    scope: "Path-X task only"
    magnitude: "46 percentage points above random"
  - id: C3
    claim: "S4 reduces computation from O(N²L) to O(N+L) and memory from O(NL) to O(N+L) compared to LSSL"
    evidence: "Table 2, Section 3.3, Theorem 3"
    status: supported
    scope: "Theoretical complexity"
    magnitude: "Up to 30× faster, 400× less memory"
  - id: C4
    claim: "S4 achieves 91.13% accuracy on sequential CIFAR-10 without data augmentation, competitive with 2D ResNet-18"
    evidence: "Table 6, Section 4.3"
    status: supported
    scope: "Sequential CIFAR-10, no 2D inductive bias"
  - id: C5
    claim: "S4 performs autoregressive generation 60× faster than Transformers"
    evidence: "Tables 7 and 8, Section 4.3"
    status: supported
    scope: "CIFAR-10 and WikiText-103 generation"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: complementary
    detail: "S4 provides an alternative to Transformer attention for sequence modeling with superior long-range dependency handling"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer uses sparse attention for long sequences; S4 uses state space models, achieving better LRA results"
  - target: 2020-12-bigbird-sparse-attention
    type: complementary
    detail: "BigBird uses sparse attention patterns; S4 outperforms it on all LRA tasks by large margins"
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: complementary
    detail: "RWKV proposes a linear RNN alternative to Transformers; S4 outperforms RWKV on LRA Image (88.65 vs 70.53) and Pathfinder (94.20 vs 58.42) but RWKV scales to 14B parameters for language modeling"
  - target: 2023-07-retnet-retentive-network
    type: complementary
    detail: "RetNet compares with S4/H3 as alternative sequence models; RetNet uses retention with exponential decay rather than structured state spaces, achieving competitive performance at 200M scale"
  - target: 2023-07-hyena-hierarchy-long-convolutions
    type: extended-by
    detail: "Hyena generalizes S4's long convolution approach by replacing SSM-parameterized filters with FFN-based implicit convolutions, matching Transformer quality without attention"
open_questions:
  - question: "Can S4 be combined with attention mechanisms to improve performance on tasks where Transformers excel (e.g., language modeling)?"
    addressed_by: null
  - question: "How does the HiPPO initialization specifically enable learning of long-range dependencies?"
    addressed_by: null
  - question: "Can the NPLR parameterization be extended to other structured matrices beyond HiPPO?"
    addressed_by: null
---
# Efficiently Modeling Long Sequences with Structured State Spaces

**Authors:** Albert Gu, Karan Goel, Christopher Ré (Stanford University)
**Date:** April 2022, ICLR 2022 (Outstanding Paper Honorable Mention), arXiv:2111.00396

---

## Core Research Problem

Modeling long-range dependencies (LRDs) in sequences is a central challenge for sequence models. Real-world time-series data often requires reasoning over tens of thousands of time steps, yet conventional models struggle:

1. **RNNs** suffer from vanishing/exploding gradients despite specialized variants (orthogonal RNNs, Lipschitz RNNs).
2. **CNNs** require dilated convolutions to increase receptive field, which still struggle on very long sequences.
3. **Transformers** have quadratic complexity O(L²) in sequence length L, and efficient variants (Performer, Linear Transformer, BigBird) still perform poorly on challenging LRD benchmarks.

The Long Range Arena (LRA) benchmark (Tay et al., 2021) highlights these limitations: no existing model performs better than random guessing on the Path-X task (length 16384).

A promising alternative is the **state space model (SSM)**:

> x'(t) = Ax(t) + Bu(t)
> y(t) = Cx(t) + Du(t)

Gu et al. (2021) showed that SSMs with special **HiPPO matrices** A can capture LRDs mathematically and empirically. Their Linear State Space Layer (LSSL) achieved 98% on sequential MNIST (vs 60% with random A). However, the LSSL has **prohibitive computational requirements**: O(N²L) operations and O(NL) memory for state dimension N and sequence length L, compared to a theoretical lower bound of Ω(N+L).

**The core challenge is making SSMs computationally practical while preserving their theoretical strengths for long-range dependencies.**

---

## Problem Solutions

S4 (Structured State Space) introduces a new parameterization that reduces SSM computation to near-optimal complexity while maintaining the benefits of HiPPO initialization.

1. **Normal Plus Low-Rank (NPLR) decomposition.** The HiPPO matrix A can be written as A = VΛV* - PQ^T where V is unitary, Λ is diagonal, and P, Q are low-rank factors (rank 1 or 2).

2. **Generating function approach.** Instead of computing the SSM convolution kernel K directly, S4 computes its truncated generating function at roots of unity, then recovers K via inverse FFT.

3. **Woodbury identity.** The generating function involves matrix inverses of A. For DPLR (Diagonal Plus Low-Rank) matrices, the Woodbury identity reduces the inverse to operations on the diagonal component.

4. **Cauchy kernel reduction.** The final computation reduces to evaluating a Cauchy kernel, a well-studied problem with O((N+L)log(N+L)) algorithms via the Fast Multipole Method.

---

## Approach Details

### Method

**State Space Model (SSM).** The continuous-time SSM (Equation 1) maps a 1-D input signal u(t) to an N-dimensional latent state x(t), then projects to a 1-D output y(t):

> x'(t) = Ax(t) + Bu(t)
> y(t) = Cx(t)

The term Du(t) is omitted as it is a simple skip connection.

**HiPPO Matrix.** The key to SSM performance on LRDs is the HiPPO matrix (Equation 2):

> A_nk = -[(2n+1)^(1/2)(2k+1)^(1/2) if n > k; n+1 if n = k; 0 if n < k]

This matrix allows the state x(t) to memorize the history of the input u(t) through optimal polynomial projections.

**Discretization.** To apply SSMs to discrete sequences, the continuous-time model is discretized using the bilinear method with step size Δ (Equation 3):

> x_k = Āx_{k-1} + B̄u_k
> y_k = C̄x_k

where Ā = (I - Δ/2·A)^(-1)(I + Δ/2·A), B̄ = (I - Δ/2·A)^(-1)ΔB, C̄ = C.

**Convolutional View.** The discrete SSM can be written as a convolution (Equation 4):

> y = K̄ * u

where the SSM convolution kernel is K̄ = (C̄B̄, C̄ĀB̄, ..., C̄Ā^(L-1)B̄) ∈ ℝ^L.

**The S4 parameterization.** By Theorem 1, all HiPPO matrices have a Normal Plus Low-Rank (NPLR) representation:

> A = VΛV* - PQ^T = V(Λ - (V*P)(V*Q)*)V*

for unitary V, diagonal Λ, and low-rank factors P, Q ∈ ℝ^(N×r) with r = 1 or r = 2.

### Key Technical Components

**Algorithm 1 (S4 Convolution Kernel).** The algorithm proceeds in five steps:

1. Compute C̃ = (I - Ā^L)*C to truncate the SSM generating function to length L
2. Evaluate a 2×2 block of Cauchy kernels at roots of unity ω
3. Apply the Woodbury identity to correct for the low-rank term
4. Evaluate the generating function K̂(ω) at all L-th roots of unity
5. Apply inverse FFT to recover K̄

**Theorem 2 (S4 Recurrence).** One step of the discrete SSM recurrence can be computed in O(N) operations because the inverse of a DPLR matrix is also DPLR.

**Theorem 3 (S4 Convolution).** Computing the SSM convolution filter K̄ requires only Õ(N+L) operations and O(N+L) space by reduction to 4 Cauchy multiplies.

**Architecture.** An S4 layer defines a map ℝ^L → ℝ^L. For H hidden features, H independent S4 copies are used with a position-wise linear layer for mixing, yielding O(H²) + O(HN) parameters per layer. Nonlinear activations are inserted between layers. The resulting deep S4 model is analogous to a depthwise-separable CNN with global convolution kernels.

**Parameters.** An S4 layer is parameterized by Λ, P, Q, B, C ∈ ℂ^(N×1), comprising 5N trainable parameters. The state size N is typically set to 64.

### Experimental Setup

**Long Range Arena (Section 4.2).** Six tasks with lengths 1K-16K steps:
- ListOps (2K): parsing nested lists
- Text (4K): byte-level text classification
- Retrieval (4K): document similarity
- Image (1K): sequential CIFAR-10 classification
- Pathfinder (1K): path connectivity in images
- Path-X (16K): same as Pathfinder but 128×128 images

Model: 6 layers, H ∈ {64, 128, 256, 512}, N = 64. Optimizer: AdamW with reduced LR (max 0.001) for HiPPO parameters (Λ, P, Q, B, C, Δ). Single A100 GPU.

**Speech Commands (Section 4.2).** SC10 subset: 10-class classification of spoken words. Raw audio (length 16000) following Romero et al. (2021). Model: 6 layers, H = 128.

**WikiText-103 (Section 4.3).** Language modeling benchmark. Architecture: 16 blocks of S4 layers alternated with feedforward layers, H = 1024, adaptive embeddings. Training: AdamW, cosine LR schedule, batch size 1, context 8192, 8× A100 GPUs.

**CIFAR-10 Density Estimation (Section 4.3).** Autoregressive image modeling (3072 RGB subpixels). UNet-style backbone with S4 + feedforward blocks.

**Reproducibility.** Code publicly available at https://github.com/HazyResearch/state-spaces. All models trained on single or 8× A100 GPUs.

### Key Results

**Long Range Arena (Table 4):**

| Model | ListOps | Text | Retrieval | Image | Pathfinder | Path-X | Avg |
|---|---|---|---|---|---|---|---|
| Transformer | 36.37 | 64.27 | 57.46 | 42.44 | 71.40 | ✗ | 53.66 |
| BigBird | 36.05 | 64.02 | 59.29 | 40.83 | 74.87 | ✗ | 54.17 |
| Luna-256 | 37.25 | 64.57 | 79.29 | 47.38 | 77.72 | ✗ | 59.37 |
| **S4** | **59.60** | **86.82** | **90.90** | **88.65** | **94.20** | **96.35** | **86.09** |

- S4 outperforms all baselines on all 6 tasks
- S4 is the first model to solve Path-X (96.35% vs 50% random)
- Average improvement: +26.72 points over best baseline (Luna-256)

**Efficiency Benchmarks (Table 2):**

| Dim | LSSL Speed (ms) | S4 Speed (ms) | LSSL Memory (MB) | S4 Memory (MB) |
|---|---|---|---|---|
| 128 | 9.32 | 4.77 | 222.1 | 5.3 |
| 256 | 20.6 | 3.07 | 1685 | 12.6 |
| 512 | 140.7 | 4.75 | 13140 | 33.5 |

- At dimension 512: 29.6× faster, 392× less memory

**Speech Commands Raw (Table 5):**

| Model | MFCC (161) | Raw (16000) |
|---|---|---|
| Transformer | 90.75 | ✗ |
| CKConv | 95.3 | 71.66 |
| WaveGAN-D | ✗ | 96.25 |
| **S4** | 93.96 | **98.32** |

- S4 achieves 98.32% on raw audio, outperforming specialized speech CNNs with 90× fewer parameters

**Sequential Image Classification (Table 6):**

| Model | sMNIST | pMNIST | sCIFAR |
|---|---|---|---|
| Transformer | 98.9 | 97.9 | 62.2 |
| LipschitzRNN | 99.4 | 96.3 | 64.2 |
| LSSL | 99.53 | 98.76 | 84.65 |
| **S4** | **99.63** | 98.70 | **91.13** |

- Sequential CIFAR-10: 91.13% without 2D inductive bias, competitive with ResNet-18 (89.46% without augmentation)

**WikiText-103 Language Modeling (Table 8):**

| Model | Params | Test ppl | Tokens/sec |
|---|---|---|---|
| Transformer | 247M | 20.51 | 0.8K |
| TaLK Conv | 240M | 23.3 | - |
| **S4** | 249M | **20.95** | **48K** |

- S4 achieves SoTA for attention-free models (within 0.44 ppl of Transformer)
- 60× faster generation than Transformer

**CIFAR-10 Density Estimation (Table 7):**

| Model | bpd | 2D bias | Images/sec |
|---|---|---|---|
| PixelSNAIL | 2.85 | 2D conv + attn | 0.13 |
| S4 (large) | 2.85 | None | 3.36 |

- Matches best autoregressive models without any 2D inductive bias

---

## Limitations and Failure Modes

**Acknowledged by authors (Appendix A):**

1. **Gap to Transformers on language modeling.** S4 achieves 20.95 ppl vs 20.51 for Transformer on WikiText-103. The authors suggest exploring S4-attention combinations.

2. **Limited to 1-D sequences.** The current formulation handles 1-D sequences; extension to higher-dimensional data (images, video) is noted as future work.

**Methodological observations:**

1. **HiPPO initialization is critical.** Ablations (Section 4.4, Figure 4) show that random initialization performs 15+ percentage points worse on sequential CIFAR-10 despite reaching 100% training accuracy. The NPLR parameterization alone does not explain S4's success.

2. **Complex-valued parameters.** The NPLR representation requires complex-valued parameters (Λ, P, Q, B, C ∈ ℂ^N), which may introduce implementation challenges.

3. **Single-task evaluation.** Most experiments use task-specific hyperparameters (Table 11). The extent to which S4 can serve as a truly universal sequence model with fixed hyperparameters is not fully established.

4. **Limited downstream applications.** The paper focuses on benchmarks rather than real-world applications (e.g., speech recognition, machine translation).

---

## Conclusions

### Contributions

1. **NPLR parameterization for SSMs.** S4 introduces Normal Plus Low-Rank decomposition of HiPPO matrices (Theorem 1), enabling stable diagonalization and efficient computation while preserving theoretical properties for long-range dependencies.

2. **Near-optimal computational complexity.** The S4 algorithm (Algorithm 1) achieves Õ(N+L) computation and O(N+L) memory (Theorem 3), matching the theoretical lower bound up to log factors. This is a 30× speed improvement and 400× memory reduction over LSSL (Table 2).

3. **State-of-the-art on long-range dependency benchmarks.** S4 outperforms all prior methods on all six LRA tasks by large margins (+26.72 points average) and is the first model to solve Path-X (Table 4).

4. **Unified sequence model.** S4 achieves strong results across diverse modalities (images, text, audio, time-series) and tasks (classification, generation, forecasting) with minimal architectural changes.

5. **Efficient autoregressive generation.** By switching to its recurrent representation, S4 achieves 60× faster generation than Transformers while maintaining quality (Tables 7, 8).

### Implications

1. **SSMs as a viable alternative to attention.** (Inference) S4 demonstrates that state space models can match or exceed Transformers on many tasks, particularly those requiring long-range reasoning.

2. **Foundation for Mamba and successors.** (Inference) S4's efficient SSM computation directly enabled follow-up work including Mamba, which combines S4's state space formulation with input-dependent selection mechanisms.

3. **HiPPO theory is practically relevant.** The ablations confirm that the continuous-time memorization theory underlying HiPPO translates to significant empirical gains, not just theoretical elegance.

---

## Key Claims

1. **C1: S4 achieves state-of-the-art on all six LRA tasks with 86.09% average accuracy.** All baselines score below 60%. The improvement is consistent across tasks spanning text, images, and structured reasoning. Evidence: Table 4. Status: **supported**.

2. **C2: S4 is the first model to solve Path-X.** All prior models achieve random-guessing performance (50%) on this length-16384 task. S4 achieves 96.35%. Evidence: Table 4. Status: **supported**.

3. **C3: S4 reduces complexity from O(N²L) to Õ(N+L).** The NPLR parameterization enables reduction to Cauchy kernel computation. Empirically, S4 is 30× faster and uses 400× less memory than LSSL at dimension 512. Evidence: Table 2, Theorem 3. Status: **supported**.

4. **C4: S4 achieves 91.13% on sequential CIFAR-10 without 2D inductive bias.** This is competitive with ResNet-18 (89.46% without augmentation) and far exceeds other sequence models (LipschitzRNN: 64.2%). Evidence: Table 6. Status: **supported**.

5. **C5: S4 generates 60× faster than Transformers.** Using its recurrent representation, S4 requires constant memory/computation per time step. Evidence: Tables 7, 8. Status: **supported**.

---

## Open Questions

1. **Can S4 be combined with attention to improve language modeling?** S4 approaches but does not match Transformer perplexity on WikiText-103. Hybrid architectures may capture complementary strengths. **Unresolved.**

2. **Why does HiPPO initialization enable LRD learning?** The ablations show dramatic generalization gaps between HiPPO and random initialization despite similar training accuracy. The mechanistic explanation remains unclear. **Unresolved.**

3. **Can NPLR be extended to other structured matrices?** The paper focuses on HiPPO matrices; whether similar decompositions exist for other useful matrices is not explored. **Unresolved.**

4. **How does S4 scale to modern LLM sizes?** The largest model tested (WikiText-103) has 249M parameters. Scaling behavior to billions of parameters is not established. **Addressed by** subsequent work on Mamba and other SSM variants.

---

## Core References and Why They Are Referenced

### State Space Model Foundations

- **Gu et al. (2020)** -- *HiPPO: Recurrent Memory with Optimal Polynomial Projections.* Introduces the HiPPO framework and special A matrices for continuous-time memorization. S4 builds directly on this theoretical foundation; the HiPPO matrix (Equation 2) is the key to S4's LRD performance.

- **Gu et al. (2021)** -- *Combining Recurrent, Convolutional, and Continuous-Time Models with the LSSL.* Introduces the Linear State Space Layer showing SSMs can address LRDs. S4 solves LSSL's computational bottleneck.

- **Voelker et al. (2019)** -- *Legendre Memory Units.* Derives a non-trainable SSM for neuromorphic computing. Part of the line of work leading to HiPPO and S4.

### Efficient Sequence Models

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer. S4 provides an alternative to self-attention with better scaling for long sequences.

- **Choromanski et al. (2020)** -- *Rethinking Attention with Performers.* Efficient Transformer variant using kernel approximation. S4 outperforms Performer on LRA (86.09% vs 51.18%).

- **Katharopoulos et al. (2020)** -- *Transformers Are RNNs: Fast Autoregressive Transformers with Linear Attention.* Linear Transformer enabling RNN-like inference. S4 benchmarks generation speed against this model.

### Long-Range Dependency Benchmarks

- **Tay et al. (2021)** -- *Long Range Arena: A Benchmark for Efficient Transformers.* Introduces the LRA benchmark with 6 tasks up to length 16K. S4 is the first model to solve all tasks, including Path-X.

- **Arjovsky et al. (2016)** -- *Unitary Evolution Recurrent Neural Networks.* Orthogonal RNNs for addressing vanishing gradients. S4 dramatically outperforms such RNN variants on LRA.

### Numerical Methods

- **Pan (2001, 2015, 2017)** -- Works on structured matrices and Cauchy kernels. S4's core algorithm relies on fast Cauchy matrix-vector multiplication; these references establish the theoretical foundations and O((N+L)log(N+L)) complexity.

- **Woodbury (1950)** -- *Inverting Modified Matrices.* The Woodbury identity enables S4 to handle the low-rank correction in the NPLR representation efficiently.

### Experimental Baselines

- **Romero et al. (2021)** -- *CKConv: Continuous Kernel Convolution for Sequential Data.* Continuous kernel CNN for long sequences. S4 outperforms CKConv on raw speech (98.32% vs 71.66%).

- **Baevski & Auli (2018)** -- *Adaptive Input Representations for Neural Language Modeling.* Provides the Transformer baseline architecture for WikiText-103 experiments.
