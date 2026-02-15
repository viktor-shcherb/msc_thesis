---
title: "Gated Delta Networks: Improving Mamba2 with Delta Rule"
authors: "Yang, Kautz, Hatamizadeh"
year: 2025
venue: "ICLR 2025"
paper_type: conference-paper
categories: ["architecture", "attention-efficiency", "state-space-models"]
scope: ["linear recurrent models", "gated delta rule", "hardware-efficient chunkwise training", "hybrid attention architectures"]
benchmarks_used: ["perplexity-wikitext103", "lambada", "piqa", "hellaswag", "winogrande", "arc", "boolq", "siqa", "ruler", "niah", "longbench", "perplexity-govreport", "perplexity-qmsum", "perplexity-pg19", "squad", "triviaqa", "natural-questions", "drop"]
models_introduced: ["gated-deltanet-1.3b", "gated-deltanet-h1-1.3b", "gated-deltanet-h2-1.3b"]
models_evaluated: ["mamba-1.4b", "retnet-1.3b"]
key_claims:
  - id: C1
    claim: "Gated DeltaNet consistently outperforms Mamba2 and DeltaNet across language modeling, commonsense reasoning, in-context retrieval, length extrapolation, and long-context understanding"
    evidence: "Tables 2-5, Figure 2"
    status: supported
    scope: "1.3B parameters, 100B tokens training, FineWeb-Edu, identical training setup"
    magnitude: "55.32 vs 52.69 (Mamba2) vs 52.14 (DeltaNet) avg on LM+reasoning benchmarks (Table 3)"
  - id: C2
    claim: "Gating and delta rule are complementary: gating enables rapid memory erasure while delta rule enables targeted memory updates"
    evidence: "Table 2, Section 3.2"
    status: supported
    scope: "S-NIAH synthetic benchmarks at 1.3B scale, 1K-8K sequence lengths"
    magnitude: "S-NIAH-2 4K: Gated DeltaNet 92.2 vs DeltaNet 18.6 vs Mamba2 58.2"
  - id: C3
    claim: "Gated delta rule introduces only marginal overhead over the original delta rule, achieving essentially the same training throughput as DeltaNet"
    evidence: "Figure 3, Section 4"
    status: supported
    scope: "1.3B models on single H100 GPU, 2K-16K sequence lengths"
    magnitude: "~same tokens/sec as DeltaNet; both 2-3K tokens/sec slower than Mamba2"
  - id: C4
    claim: "Hybrid Gated DeltaNet models with sliding window attention further improve over pure recurrent models"
    evidence: "Tables 3-5"
    status: supported
    scope: "1.3B parameters, SWA window size 2K"
    magnitude: "Gated DeltaNet-H2 avg 56.48 vs 55.32 pure Gated DeltaNet on LM+reasoning (Table 3)"
  - id: C5
    claim: "Gated DeltaNet achieves the lowest overall perplexity across tasks among RNN models in length extrapolation up to 20K tokens"
    evidence: "Figure 2"
    status: supported
    scope: "6 long-context benchmarks, trained at 4K, evaluated up to 20K"
    magnitude: "lowest overall perplexity, though mixed results on individual tasks"
  - id: C6
    claim: "Short convolution and output gate are crucial architectural components, while L2 normalization is essential for training stability"
    evidence: "Table S.1, Appendix B.2"
    status: supported
    scope: "400M parameters, 15B tokens ablation"
    magnitude: "removing short conv: 27.35->28.95 avg ppl; removing output gate: 27.35->29.12 avg ppl; L1-norm vs L2-norm: ~30 vs ~27.5 avg ppl"
  - id: C7
    claim: "Among hybrid layer orderings, Mamba2 + Gated DeltaNet + SWA produces the best results"
    evidence: "Table S.2, Appendix B.2"
    status: supported
    scope: "500M parameters, 15B tokens, 4 layer orderings tested"
    magnitude: "48.73 avg acc vs 47.54-47.92 for other orderings"
cross_references:
  - target: 2024-05-mamba-selective-state-spaces
    type: extends
    detail: "Gated DeltaNet unifies Mamba2's gated update rule with the delta rule, achieving better memory management than either alone"
  - target: 2022-04-s4-structured-state-spaces
    type: extends
    detail: "S4 provides foundational SSM framework; Gated DeltaNet operates in the linear recurrent model family that evolved from SSMs"
  - target: 2017-12-attention-is-all-you-need
    type: complementary
    detail: "Gated DeltaNet replaces softmax attention with gated delta rule recurrence; hybrid variants combine it with sliding window attention"
  - target: 2025-10-kimi-linear-attention
    type: extended-by
    detail: "Kimi Linear extends Gated DeltaNet with fine-grained channel-wise gating (KDA) instead of head-wise gating, achieving further improvements at scale"
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: complementary
    detail: "RWKV is a concurrent linear RNN approach; both address attention inefficiency but with different update rules (time-decay vs delta rule)"
  - target: 2023-07-retnet-retentive-network
    type: evaluates
    detail: "RetNet is an evaluated baseline; Gated DeltaNet outperforms RetNet on all benchmarks (Table 3: 55.32 vs 52.02 avg)"
  - target: 2024-08-longbench-bilingual-benchmark
    type: uses-benchmark
    detail: "LongBench is used for long-context understanding evaluation across 14 tasks (Table 5)"
  - target: 2025-12-ttt-e2e-long-context
    type: complementary
    detail: "TTT-E2E evaluates Gated DeltaNet as a baseline at 3B scale; finds it does not scale with context length as well as full attention beyond 32K"
open_questions:
  - question: "How does Gated DeltaNet scale beyond 1.3B parameters to 7B+ model sizes?"
    addressed_by: null
  - question: "Can the gated delta rule benefit from negative eigenvalues or high-rank transition matrices (Grazzi et al., 2024; Siems et al., 2025)?"
    addressed_by: null
  - question: "How does Gated DeltaNet compare to nonlinear recurrence methods like TTT and Titans?"
    addressed_by: 2025-12-ttt-e2e-long-context
  - question: "What is the optimal ratio of attention layers to recurrent layers in hybrid architectures?"
    addressed_by: null
---

# Gated Delta Networks: Improving Mamba2 with Delta Rule

**Authors:** Songlin Yang, Jan Kautz, Ali Hatamizadeh (MIT CSAIL, NVIDIA)
**Date:** April 2025, ICLR 2025 (arXiv:2412.06464)
**Code:** https://github.com/NVlabs/GatedDeltaNet

---

## Core Research Problem

Linear Transformers replace softmax attention with kernelized dot-product linear attention, reducing inference memory requirements by reframing attention as a linear RNN with matrix-valued states. While early linear Transformers underperformed standard Transformers, recent models incorporating data-dependent gating---such as GLA (Yang et al., 2024a) and Mamba2 (Dao & Gu, 2024a)---have narrowed the gap. However, challenges persist in managing information over long sequences, particularly for **in-context retrieval** tasks where standard Transformers maintain their advantage (Arora et al., 2023a; 2024a; Jelassi et al., 2024; Wen et al., 2024; Akyurek et al., 2024) (Section 1).

Linear Transformers can be interpreted as implementing an outer-product-based key-value association memory (Smolensky, 1990). The number of orthogonal key-value pairs they can store is **bounded** by the model's dimensionality. When the sequence length exceeds this capacity, "memory collisions" become inevitable, hindering exact retrieval (Schlag et al., 2021a) (Section 1).

Two distinct mechanisms have been explored to address this:

1. **Gating** (as in Mamba2): A gated update rule S_t = alpha_t S_{t-1} + v_t k_t^T, where alpha_t in (0,1) uniformly decays all key-value associations. This enables adaptive memory control but treats all stored associations equally during forgetting---if the model needs to forget a specific key-value association, all pairs are equally forgotten (Section 1).

2. **Delta rule** (as in DeltaNet): An update rule S_t = S_{t-1}(I - beta_t k_t k_t^T) + beta_t v_t k_t^T that selectively replaces one key-value pair at a time. This enables precise memory modification but lacks the ability to rapidly clear outdated or irrelevant information, especially when there is more information than slots to be erased (Section 1).

**The core challenge is: how to combine the complementary advantages of gating (bulk memory erasure) and the delta rule (targeted memory updates) in a hardware-efficient manner.**

---

## Problem Solutions

The paper proposes the **gated delta rule**, a simple formulation that combines both mechanisms:

1. **Unified update rule.** Introduce a data-dependent gating term alpha_t into the delta rule: S_t = S_{t-1}(alpha_t(I - beta_t k_t k_t^T)) + beta_t v_t k_t^T. Setting alpha_t -> 0 clears memory; setting alpha_t -> 1 recovers the pure delta rule (Section 3.1, Eq. 10).

2. **Hardware-efficient chunkwise parallel algorithm.** Extend Yang et al. (2024b)'s WY-representation-based algorithm for DeltaNet to incorporate gating terms, preserving chunkwise parallelism for efficient GPU training (Section 3.3).

3. **Hybrid architectures.** Combine Gated DeltaNet layers with sliding window attention (SWA) and/or Mamba2 layers to exploit complementary strengths of local attention and linear recurrence (Section 3.4).

---

## Approach Details

### Method

#### Gated Delta Rule (Section 3.1, Eq. 10)

The proposed state update is:

> **S_t = S_{t-1} (alpha_t (I - beta_t k_t k_t^T)) + beta_t v_t k_t^T**

where:
- **S_t** in R^{d_v x d_k} is the recurrent state (matrix-valued memory)
- **alpha_t** in (0, 1) is a data-dependent scalar gating term controlling state decay
- **beta_t** in (0, 1) is the "writing strength" for the delta rule update
- **k_t**, **v_t** are key and value vectors at position t
- Output: **o_t = S_t q_t** where **q_t** is the query vector

This formulation unifies gating and delta rule advantages:
- The gating term alpha_t enables **adaptive memory management** (bulk decay)
- The delta update structure (I - beta_t k_t k_t^T) enables **targeted key-value association learning**

#### Online Learning Interpretation (Section 3.1, Table 1)

The paper frames recurrent state updates as closed-form solutions to online learning objectives, following Liu et al. (2024):

| Method | Online Learning Objective | Online Update |
|--------|--------------------------|---------------|
| Linear Attention | \|\|S_t - S_{t-1}\|\|^2_F - 2<S_t k_t, v_t> | S_t = S_{t-1} + v_t k_t^T |
| Mamba2 | \|\|S_t - alpha_t S_{t-1}\|\|^2_F - 2<S_t k_t, v_t> | S_t = alpha_t S_{t-1} + v_t k_t^T |
| DeltaNet | \|\|S_t - S_{t-1}\|\|^2_F - 2<S_t k_t, beta_t(v_t - S_{t-1} k_t)> | S_t = S_{t-1}(I - beta_t k_t k_t^T) + beta_t v_t k_t^T |
| **Gated DeltaNet** | \|\|S_t - alpha_t S_{t-1}\|\|^2_F - 2<S_t k_t, beta_t(v_t - alpha_t S_{t-1} k_t)> | S_t = S_{t-1}(alpha_t(I - beta_t k_t k_t^T)) + beta_t v_t k_t^T |

Mamba2 and Gated DeltaNet introduce an adaptive scaling factor alpha_t that relaxes the regularization term, allowing controlled deviations between S_t and S_{t-1}, enabling dynamic memory management through selective forgetting (Section 3.1).

From the fast weight programming perspective (Irie et al., 2022a), the state S can be interpreted as a (fast) weight matrix optimizing the online regression objective L(S_t) = 1/2 \|\|S_t k_t - v_t\|\|^2 via test-time stochastic gradient descent. The gated delta rule adds **adaptive weight decay** (alpha_t) to this SGD update, a technique widely used in deep learning (Krogh & Hertz, 1991; Andriushchenko et al., 2023). Concurrently, Titans (Behrouz et al., 2024) demonstrated the effectiveness of incorporating weight decay in RNN test-time SGD updates (Section 3.1).

### Key Technical Components

#### Hardware-Efficient Chunkwise Training (Section 3.3)

The gated delta rule recurrence is partially expanded over chunks of size C (Section 3.3):

> S^r_{[t]} = S_{[t]} (prod_{i=1}^{r} alpha^i_{[t]}(I - beta^i_{[t]} k^i_{[t]} k^{iT}_{[t]})) + sum_{i=1}^{r} (beta^i_{[t]} v^i_{[t]} k^{iT}_{[t]} prod_{j=i+1}^{r} alpha^j_{[t]}(I - beta^j_{[t]} k^j_{[t]} k^{jT}_{[t]}))

The cumulative products of generalized Householder matrices are optimized using the classical WY representation (Bischof & Loan, 1985). By the UT transform (Joffrain et al., 2006), the extended WY representation matrices are computed via (Section 3.3):

> T_tilde_{[t]} = [I + strictLower(diag(beta_{[t]})(Gamma_{[t]} odot K_{[t]} K^T_{[t]}))]^{-1} diag(beta_{[t]})

> U_tilde_{[t]} = T_tilde_{[t]} V_{[t]}

The final chunkwise state update and output computation:

> S_{[t+1]} = S_bar_{[t]} + (U_tilde_{[t]} - W_tilde_{[t]} S_bar^T_{[t]})^T K_bar_{[t]}

> O_{[t]} = Q_tilde_{[t]} S_bar^T_{[t]} + (Q_{[t]} K^T_{[t]} odot M)(U_tilde_{[t]} - W_tilde_{[t]} S_bar^T_{[t]})

where arrows denote decay-adjusted versions of vectors and matrices. These equations are rich in matrix multiplications, enabling tensor-core-based GPU optimization (Section 3.3).

The correctness of the extended WY representation for the gated delta rule is proved by mathematical induction in Appendix A, showing that S_t = sum_{i=1}^{t} (gamma_t / gamma_i) u_i k_i^T where u_t = beta_t(v_t - sum_{i=1}^{t-1} (gamma_t / gamma_i) u_i k_i^T k_t).

#### Gated DeltaNet Architecture (Section 3.4)

The token mixer block follows LLaMA's macro architecture:
- **Query/Key path:** Linear projection -> short convolution -> SiLU activation -> L2 normalization
- **Value path:** Linear projection -> short convolution -> SiLU activation
- **alpha, beta:** Linear projection only (following Sun et al., 2023a)
- **Output:** Normalization -> gating -> output projection with SiLU

Full model stacks token mixer layers with SwiGLU MLP layers.

#### Hybrid Models (Section 3.4)

- **Gated DeltaNet-H1:** Alternates Gated DeltaNet layers with SWA layers (each interleaved with MLP layers)
- **Gated DeltaNet-H2:** Stacks Mamba2 + Gated DeltaNet + SWA layers (each interleaved with MLP layers)

The hybrid variants address the limitation that linear recurrent models struggle with local context modeling and retrieval due to fixed state size (Arora et al., 2024a).

#### Theoretical Analysis

The paper does not present formal theorems but provides two theoretical perspectives:

1. **Online learning framework** (Section 3.1, Table 1): Each linear RNN variant corresponds to a specific online learning objective. The gated delta rule combines the adaptive forgetting of Mamba2's objective with the more expressive regression loss of DeltaNet.

2. **Fast weight programming / SGD interpretation** (Section 3.1): The delta rule is equivalent to one-step SGD on L(S_t) = 1/2 \|\|S_t k_t - v_t\|\|^2. The gated delta rule adds weight decay alpha_t to this update.

3. **Extended WY representation proof** (Appendix A): Formal induction proof that the gated delta rule can be expressed in the WY representation form, enabling the chunkwise parallel algorithm.

### Experimental Setup

**Training:** All models trained identically with 1.3B parameters on 100B tokens from FineWeb-Edu (Penedo et al., 2024). AdamW optimizer with peak learning rate 4e-4, weight decay 0.1, gradient clipping 1.0. Cosine annealing schedule with 1B token warm-up. Batch size 0.5M tokens. Llama2 tokenizer with vocabulary size 32,000. Training sequence length 4K tokens; SWA window size 2K (Section 4).

**Model details:** 400M and 1.3B parameter variants trained. Primary comparisons at 1.3B scale. Ablation studies at 400M scale on 15B tokens (Appendix B.2).

**Baselines:** RetNet (Sun et al., 2023a), HGRN2 (Qin et al., 2024b), Mamba (Gu & Dao, 2023), Mamba2 (Dao & Gu, 2024b), Samba (Ren et al., 2024), DeltaNet (Yang et al., 2024b), Transformer++ (Section 4).

**Evaluation domains** (Section 4, Appendix B.1):
1. Language modeling perplexity (WikiText-103, LAMBADA)
2. Zero-shot commonsense reasoning (PIQA, HellaSwag, WinoGrande, ARC-e, ARC-c, SocialIQA, BoolQ)
3. In-context retrieval -- synthetic: S-NIAH from RULER (Hsieh et al., 2024); real-world: recall tasks from Arora et al. (2024b) including SWDE, SQuAD, FDA, TriviaQA, NQ, Drop
4. Length extrapolation (perplexity on GovReport, QMSum, NarrativeQA, Qasper, CodeParrot, PG19 at 4K-20K)
5. Long-context understanding (LongBench, 14 tasks)

**Reproducibility:** Code is available at https://github.com/NVlabs/GatedDeltaNet. All models evaluated using lm-evaluation-harness (Gao et al., 2021). Seeds are not reported; single run per configuration (limited evidence). Evaluation details for recall tasks follow Arora et al. (2024b) formatting prompts.

### Key Results

#### Synthetic In-Context Retrieval (S-NIAH, Table 2, Section 3.2)

| Model | S-NIAH-1 1K/2K/4K/8K | S-NIAH-2 1K/2K/4K/8K | S-NIAH-3 1K/2K/4K |
|-------|------------------------|------------------------|---------------------|
| DeltaNet | 97.4 / 96.8 / 99.0 / 98.8 | 93.4 / 45.6 / 18.6 / 14.4 | 85.2 / 47.0 / 22.4 |
| Mamba2 | 99.2 / 98.8 / 65.4 / 30.4 | 99.4 / 98.8 / 58.2 / 17.0 | 64.4 / 47.6 / 4.6 |
| **Gated DeltaNet** | **98.4 / 88.4 / 91.4 / 91.8** | **100.0 / 99.8 / 92.2 / 29.6** | **86.6 / 84.2 / 27.6** |

**Key findings from S-NIAH analysis (Section 3.2):**
- **S-NIAH-1 (passkey retrieval):** **Decay hurts memory retention.** DeltaNet achieves near-perfect across all lengths; Mamba2 degrades significantly beyond 2K due to excessive decay of historical information. Gated DeltaNet's degradation is less severe than Mamba2's thanks to gating control.
- **S-NIAH-2 (number in haystack):** **Gating facilitates filtering.** DeltaNet's performance drops significantly at longer sequences due to memory collision from poor memory clearance. Mamba2 and Gated DeltaNet maintain better performance through gating mechanisms that filter irrelevant information. Gated DeltaNet achieves 92.2 at 4K vs 58.2 (Mamba2) and 18.6 (DeltaNet).
- **S-NIAH-3 (UUID in haystack):** **Delta rule helps memorization.** Values change from numbers to UUIDs, testing complex pattern memorization. Mamba2 drops quickly (4.6 at 4K); Gated DeltaNet performs better (27.6 at 4K), verifying that the delta rule enables better memorization ability.

#### Language Modeling and Commonsense Reasoning (Table 3)

| Model | Wiki. ppl | LMB. ppl | LMB. acc | PIQA | Hella. | Wino. | ARC-e | ARC-c | SIQA | BoolQ | Avg. |
|-------|-----------|----------|----------|------|--------|-------|-------|-------|------|-------|------|
| *Recurrent models* | | | | | | | | | | | |
| RetNet | 19.08 | 17.27 | 40.52 | 70.07 | 49.16 | 54.14 | 67.34 | 33.78 | 40.78 | 60.39 | 52.02 |
| HGRN2 | 19.10 | 17.69 | 39.54 | 70.45 | 49.53 | 52.80 | 69.40 | 35.32 | 40.83 | 56.66 | 51.79 |
| Mamba | 17.92 | 15.96 | 43.98 | 71.32 | 52.91 | 52.95 | 69.57 | 35.40 | 39.89 | 61.13 | 53.12 |
| Mamba2 | 18.25 | 16.52 | 42.65 | 70.62 | 50.64 | 52.25 | 67.42 | 33.79 | 40.72 | 60.43 | 52.69 |
| DeltaNet | 17.71 | 16.38 | 42.46 | 70.72 | 50.94 | 53.43 | 68.47 | 35.66 | 40.22 | 55.29 | 52.14 |
| **Gated DeltaNet** | **16.42** | **12.17** | **46.65** | **72.25** | **55.76** | 52.45 | **71.21** | **38.39** | 40.25 | **60.24** | **55.32** |
| *Hybrid models* | | | | | | | | | | | |
| Transformer++ | 18.53 | 18.32 | 42.60 | 70.02 | 50.23 | 53.51 | 68.83 | 35.10 | 40.66 | 57.09 | 52.25 |
| Samba | 16.13 | 13.29 | 44.94 | 70.94 | 53.42 | 55.56 | 68.81 | 36.17 | 39.96 | 62.17 | 54.00 |
| **Gated DeltaNet-H1** | 16.07 | 12.13 | 47.73 | 72.57 | 56.53 | **58.40** | 71.25 | **40.10** | **41.40** | **63.33** | **56.40** |
| **Gated DeltaNet-H2** | **15.71** | 12.25 | 46.96 | 72.36 | 56.33 | 57.77 | **71.59** | 39.69 | **42.25** | 60.21 | **56.48** |

Gated DeltaNet outperforms all linear recurrent models by a substantial margin (55.32 avg vs next-best Mamba 53.12). Hybrid variants further improve, with H2 achieving the best average (56.48) (tested on 7 reasoning benchmarks plus 2 LM metrics, strong evidence from controlled comparison with identical training).

#### Real-World In-Context Retrieval (Table 4)

| Model | SWDE | SQD | FDA | TQA | NQ | Drop | Avg |
|-------|------|-----|-----|-----|----|------|-----|
| *Recurrent models* | | | | | | | |
| RetNet | 14.0 | 28.5 | 7.0 | 54.4 | 16.2 | 17.3 | 22.9 |
| HGRN2 | 8.3 | 25.3 | 4.8 | 51.2 | 14.2 | 16.9 | 20.1 |
| Mamba | 9.8 | 25.8 | 3.7 | 54.3 | 14.9 | 17.4 | 21.0 |
| Mamba2 | 19.1 | 33.6 | **25.3** | **61.0** | **20.8** | 19.2 | 29.8 |
| DeltaNet | 17.9 | 30.9 | 18.4 | 53.9 | 17.3 | 18.6 | 26.2 |
| **Gated DeltaNet** | **25.4** | **34.8** | 23.7 | 60.0 | 20.0 | **19.8** | **30.6** |
| *Hybrid models* | | | | | | | |
| Transformer++ | 29.5 | 38.0 | **52.2** | 58.3 | 22.5 | 21.6 | 37.0 |
| Samba | 33.0 | 39.2 | 50.5 | 57.7 | 23.5 | 20.2 | 37.4 |
| **Gated DeltaNet-H1** | 35.6 | 39.7 | 52.0 | 60.1 | 24.6 | 22.5 | 39.0 |
| **Gated DeltaNet-H2** | **38.2** | **40.4** | 50.7 | **63.3** | **24.8** | **23.3** | **40.1** |

Gated DeltaNet outperforms both DeltaNet and Mamba2 among pure recurrent models (30.6 vs 29.8 vs 26.2 avg). The improvement margin is smaller than on synthetic S-NIAH benchmarks (Table 2). The authors attribute this to instruction-unaligned small language models being prone to repetition errors, which are the primary source of errors in these tasks and are independent of the update rule choice (Section 4, citing Arora et al., 2024b, Appendix E). Hybrid Gated DeltaNet-H2 achieves the best overall recall performance (40.1), outperforming Transformer++ (37.0) and Samba (37.4).

#### Long-Context Understanding (LongBench, Table 5)

| Model | Single-Doc QA | Multi-Doc QA | Summarization | Few-shot | Code | Avg |
|-------|---------------|--------------|---------------|----------|------|-----|
| *Recurrent models* | | | | | | |
| RetNet | 12.1 10.7 19.1 | 10.7 18.0 5.8 | 4.8 15.8 7.9 | 19.0 18.0 12.8 | 14.1 17.9 | 13.2 |
| HGRN2 | 10.7 12.1 19.1 | 11.3 15.7 6.0 | 5.2 15.1 9.2 | 16.0 15.8 10.3 | 18.6 20.8 | 13.5 |
| Mamba | 12.0 10.7 20.4 | 10.1 16.2 6.0 | 2.7 15.9 8.4 | 21.5 21.9 11.2 | 17.9 19.6 | 14.6 |
| Mamba2 | 13.1 10.3 20.6 | 10.9 18.0 5.7 | 4.5 15.2 9.1 | 19.1 19.6 8.7 | 16.1 17.0 | 13.7 |
| DeltaNet | 11.3 11.3 18.8 | 11.8 15.1 6.7 | 6.7 14.5 7.4 | 13.0 23.6 8.4 | 17.6 20.6 | 13.5 |
| **Gated DeltaNet** | **14.1 14.0 23.3** | 13.7 14.4 5.8 | **7.5 16.4 7.9** | **30.0** 22.4 **23.0** | **18.7 22.1** | **16.6** |
| *Hybrid models* | | | | | | |
| Transformer++ | 11.8 9.3 10.0 | 10.9 4.2 6.1 | 7.4 15.8 6.6 | 16.9 13.5 3.9 | 17.2 18.7 | 11.0 |
| Samba | 12.5 12.6 25.4 | 11.2 19.7 6.8 | 9.1 15.7 11.0 | 20.0 23.7 22.8 | 18.3 24.1 | 15.9 |
| **Gated DeltaNet-H1** | 14.5 12.3 26.6 | 12.9 23.6 6.7 | 12.1 17.5 12.8 | 23.5 23.9 28.8 | 19.5 19.2 | **17.8** |
| **Gated DeltaNet-H2** | **22.2 15.0 27.1** | 12.7 20.6 7.5 | 10.4 16.2 12.0 | **30.5** 22.2 27.9 | 19.9 **23.1** | **18.4** |

Gated DeltaNet shows consistent advantages in single-doc QA, few-shot in-context learning, and code tasks on LongBench (Section 4). The improvement of Gated DeltaNet (16.6) over Mamba2 (13.7) and DeltaNet (13.5) is substantial. Hybrid Gated DeltaNet-H2 achieves the best overall average (18.4), with particularly strong single-doc QA performance (22.2 on NQA vs 14.1 for pure Gated DeltaNet).

#### Training Throughput (Figure 3)

On a single H100 GPU at 1.3B scale (Section 4):
- Transformer++ achieves highest throughput at short sequences (2Kx16 batch, ~55K tokens/sec) due to Flash-Attention-2 optimization, but drops steeply to ~27K tokens/sec at 16Kx2
- Gated DeltaNet achieves essentially the same throughput as DeltaNet (~48-50K tokens/sec)
- Both are slightly slower than Mamba2 (by 2-3K tokens/sec) due to more expressive identity-plus-low-rank transition matrices vs Mamba2's diagonal matrices
- Gated DeltaNet-H1 maintains competitive throughput across all sequence lengths, outperforming standalone Mamba at longer sequences
- Hybrid approaches combining 2K window-size SWA with other token mixers demonstrate higher throughput than standalone mixers at short sequences

#### Ablation Study (Appendix B.2, Tables S.1 and S.2)

Ablation studies at 400M parameters on 15B tokens (Table S.1):

| Gated DeltaNet Ablations (400M) | Avg-PPL | Avg-Acc |
|----------------------------------|---------|---------|
| Gated DeltaNet w. Head Dim 128 | 27.35 | 47.26 |
| w. naive Delta Rule | 30.87 | 45.12 |
| w/o. Short Conv | 28.95 | 46.16 |
| w/o. Output Gate | 29.12 | 45.46 |
| w/o. Output Norm | 27.55 | 47.07 |
| w. L1-norm & ReLU | 30.79 | 45.92 |
| w. L1-norm & 1+ELU | 30.34 | 46.05 |
| w. L1-norm & SiLU | 30.18 | 46.09 |
| w. L2-norm & ReLU | 27.67 | 46.94 |
| w. L2-norm & 1+ELU | 27.58 | 47.17 |
| w. Head Dim 64 | 28.31 | 46.35 |
| w. Head Dim 256 | 27.13 | 47.38 |

**Key ablation findings** (Appendix B.2):
- **Short convolution and output gate are crucial:** Removing short conv degrades ppl from 27.35 to 28.95; removing output gate degrades to 29.12 (moderate evidence: single 400M ablation)
- **L2 normalization essential for training:** L1-norm variants perform substantially worse (~30 ppl vs ~27.5 ppl), while choice of feature map is less influential
- **SiLU consistently outperforms** other activations, aligning with Qin et al. (2023a)
- **Head dimension 128 is optimal trade-off:** Dim 64 underperforms (28.31 ppl, 46.35 acc) while dim 256 offers marginal improvement (27.13 ppl, 47.38 acc) at higher cost
- **Naive delta rule (without gating) severely underperforms:** 30.87 ppl vs 27.35, confirming the value of gating

Hybrid layer ordering ablation at 500M parameters (Table S.2):

| Layer Ordering | Avg-Acc |
|----------------|---------|
| Gated DeltaNet + SWA + Mamba2 | 47.88 |
| Gated DeltaNet + Mamba2 + SWA | 47.54 |
| Mamba2 + SWA + Gated DeltaNet | 47.92 |
| **Mamba2 + Gated DeltaNet + SWA** | **48.73** |

The Mamba2 + Gated DeltaNet + SWA ordering (used for H2) produces the best results, outperforming other orderings by 0.8-1.2 points (moderate evidence: single scale, 500M/15B tokens).

---

## Limitations and Failure Modes

### Acknowledged Limitations

1. **Scale.** Experiments limited to 1.3B parameters on 100B tokens. Scaling behavior at 7B+ is unknown (Section 6).

2. **Real-world retrieval gap.** The improvement margin of Gated DeltaNet over Mamba2 on real-world retrieval tasks (Table 4: 30.6 vs 29.8 avg, a difference of only 0.8 points) is much smaller than on synthetic S-NIAH benchmarks (Table 2). The authors attribute this to instruction-unaligned small language models being prone to repetition errors, which are independent of the update rule choice (Section 4, citing Arora et al., 2024b, Appendix E).

3. **Throughput trade-off.** Gated DeltaNet and DeltaNet are slightly slower than Mamba2 due to their more expressive identity-plus-low-rank transition matrices vs Mamba2's diagonal matrices (Figure 3, Section 4).

4. **Delta rule theoretical limitations.** The delta rule faces theoretical limitations (Irie et al., 2023) and shows only moderate performance on real-world datasets (Yang et al., 2024b), suggesting room for further improvement (Section 5).

5. **[Inferred]** All evaluations use zero-shot or few-shot without instruction tuning. Performance differences may change substantially after instruction tuning or RLHF alignment.

6. **[Inferred]** Length extrapolation results are "mixed" across individual tasks (Section 4, Figure 2 description). Gated DeltaNet is described as "relatively more robust" rather than uniformly better, indicating task-dependent behavior.

7. **[Inferred]** Single run per configuration with no variance estimates reported, making it difficult to assess statistical significance of the observed improvements (limited evidence).

### Scope and Comparability

**What was not tested:**
- Models larger than 1.3B parameters (ablations at 400M/500M only)
- Instruction tuning, RLHF, or chat applications
- Comparison with nonlinear recurrence methods (TTT, Titans) at scale
- Evaluation on RULER full benchmark or other standardized multi-task long-context benchmarks beyond LongBench
- Non-English languages
- Generation tasks (only evaluation/retrieval tasks tested)

**Comparability notes:**
- All models trained on identical data (100B tokens, FineWeb-Edu) with same tokenizer (Llama2, 32K vocab), enabling fair comparison within the paper
- Transformer++ baseline uses modern recipe but trained at same 1.3B scale
- Hybrid models use 2K SWA window; Samba also uses 2K window for comparability
- Real-world retrieval tasks use input truncated to 2K tokens (Table 4 caption)
- S-NIAH results are zero-shot (Table 2 caption)

---

## Conclusions

### Contributions

1. **Gated delta rule.** Proposed a simple unified state update rule combining Mamba2's gated decay with DeltaNet's targeted memory replacement (Eq. 10, Section 3.1). Demonstrated through controlled S-NIAH analysis that gating and delta rule are complementary: gating enables filtering of irrelevant information, delta rule enables precise memorization of complex patterns (Table 2, Section 3.2).

2. **Hardware-efficient chunkwise algorithm.** Extended Yang et al. (2024b)'s WY-representation-based parallel algorithm to incorporate gating terms, maintaining DeltaNet-level training throughput while adding gating capabilities (Figure 3, Section 3.3, Appendix A).

3. **Consistent improvements across benchmarks.** Gated DeltaNet outperforms Mamba2 and DeltaNet on language modeling (WikiText-103 ppl 16.42 vs 18.25 and 17.71), commonsense reasoning (55.32 vs 52.69 and 52.14 avg), in-context retrieval (30.6 vs 29.8 and 26.2 avg on real-world tasks), and long-context understanding (16.6 vs 13.7 and 13.5 avg on LongBench) at 1.3B scale with identical training (Tables 2-5, Figure 2).

4. **Effective hybrid architectures.** Introduced Gated DeltaNet-H1 (with SWA) and H2 (with Mamba2 + SWA), which further improve performance (H2: 56.48 avg on reasoning, 40.1 on retrieval, 18.4 on LongBench) while maintaining competitive training throughput (Tables 3-5, Figure 3).

5. **Systematic ablation.** Provided component ablations establishing the importance of short convolution, output gating, L2 normalization, and optimal hybrid layer ordering (Tables S.1-S.2, Appendix B.2).

### Implications

1. **Combining update rules is effective.** The success of unifying gating and delta rule suggests that future linear recurrent architectures should incorporate multiple complementary memory mechanisms rather than relying on a single update rule.

2. **Practical adoption.** Gated DeltaNet has been adopted by Qwen3 (Qwen Team, 2025) and Kimi Linear (Kimi Team, 2025), demonstrating its practical value for production-scale models. Kimi Linear further extends the approach with channel-wise gating.

3. **Hybrid architectures remain beneficial.** Even with improved recurrent mechanisms, hybridizing with attention continues to provide gains, particularly for retrieval-intensive tasks (speculative: this gap may narrow with further improvements to linear recurrent models).

4. **Online learning framework is productive.** The perspective of viewing recurrent state updates through the lens of online learning objectives (Table 1) provides principled guidance for designing new update rules, as demonstrated by the systematic connection between Mamba2, DeltaNet, Longhorn, and Gated DeltaNet.

---

## Key Claims

1. **C1:** Gated DeltaNet consistently outperforms Mamba2 and DeltaNet across language modeling, commonsense reasoning, in-context retrieval, length extrapolation, and long-context understanding (Tables 2-5, Figure 2). Supported by comprehensive evaluation at 1.3B scale on 100B tokens with identical training setup across 7 baselines. Scope: 1.3B parameters, FineWeb-Edu, Llama2 tokenizer. Magnitude: 55.32 vs 52.69 (Mamba2) vs 52.14 (DeltaNet) avg on reasoning benchmarks; 16.6 vs 13.7 (Mamba2) vs 13.5 (DeltaNet) on LongBench avg. Evidence is strong across multiple domains but limited to single scale.

2. **C2:** Gating and delta rule are complementary mechanisms---gating enables rapid memory erasure while delta rule facilitates targeted updates (Table 2, Section 3.2). Supported by controlled S-NIAH experiments showing each mechanism excels in different settings: DeltaNet excels at S-NIAH-1 (retention), Mamba2 at S-NIAH-2 (filtering), and Gated DeltaNet combines both advantages. Scope: S-NIAH synthetic benchmarks, 1K-8K, 1.3B scale. Magnitude: S-NIAH-2 at 4K: Gated DeltaNet 92.2 vs DeltaNet 18.6 vs Mamba2 58.2. Evidence is from synthetic benchmarks only (moderate evidence).

3. **C3:** Gated delta rule introduces only marginal overhead over the original delta rule (Figure 3, Section 4). Supported by throughput comparison on single H100 GPU showing essentially identical tokens/sec to DeltaNet across sequence lengths from 2K to 16K. Scope: 1.3B models, single H100 GPU. Magnitude: ~same tokens/sec as DeltaNet; both 2-3K tokens/sec slower than Mamba2. Single hardware configuration (limited evidence for generalization).

4. **C4:** Hybrid Gated DeltaNet models with sliding window attention further improve over pure recurrent models (Tables 3-5). Supported by results showing H1 and H2 outperform pure Gated DeltaNet and other hybrids (Samba, Transformer++) across all evaluation domains. Scope: 1.3B parameters, SWA window size 2K. Magnitude: H2 avg 56.48 vs 55.32 pure Gated DeltaNet vs 54.00 Samba on reasoning (Table 3); H2 40.1 vs 30.6 vs 37.4 on retrieval (Table 4). Tested across 5 evaluation domains (strong evidence for this scale).

5. **C5:** Gated DeltaNet achieves the lowest overall perplexity across tasks among RNN models in length extrapolation up to 20K tokens (Figure 2, Section 4). Supported by perplexity curves on 6 long-context benchmarks; authors note "mixed results in length extrapolation" but that Gated DeltaNet exhibits "relatively more robust performance." Scope: 6 benchmarks, trained at 4K, evaluated up to 20K. Magnitude: qualitative "lowest overall" -- individual task numbers not tabulated. Limited evidence: mixed results on individual tasks.

6. **C6:** Short convolution and output gate are crucial architectural components, while L2 normalization is essential for training stability (Table S.1, Appendix B.2). Supported by systematic ablation at 400M scale. Scope: 400M parameters, 15B tokens. Magnitude: removing short conv: 27.35->28.95 ppl; removing output gate: 27.35->29.12 ppl; L1-norm: ~30 ppl vs L2-norm: ~27.5 ppl. Moderate evidence: single scale ablation.

7. **C7:** Among hybrid layer orderings, Mamba2 + Gated DeltaNet + SWA produces the best results (Table S.2, Appendix B.2). Supported by comparison of 4 orderings at 500M/15B tokens. Scope: 500M parameters, 15B tokens. Magnitude: 48.73 avg acc vs 47.54-47.92 for alternatives. Limited evidence: single scale, single training budget.

---

## Open Questions

1. **Scaling beyond 1.3B.** All experiments use 1.3B parameters on 100B tokens. Does the advantage of Gated DeltaNet over Mamba2 persist or widen at 7B+ scale? Qwen3 and Kimi Linear adopt the approach at larger scales, but controlled comparisons are not available in this paper.

2. **Negative eigenvalues and high-rank transitions.** The paper notes that it is possible to set beta_t in (0, 2) to allow negative eigenvalues and unlock state-tracking abilities (Grazzi et al., 2024; footnote, Section 2.2), and that multiple products of Householder transition matrices (Siems et al., 2025) could enhance expressiveness. These are described as compatible but are not evaluated.

3. **Nonlinear recurrence comparison.** The paper discusses TTT (Sun et al., 2024a) and Titans (Behrouz et al., 2024) as more expressive alternatives using nonlinear regression objectives, but notes they sacrifice parallelism. Can Gated DeltaNet be extended with nonlinear elements while preserving chunkwise efficiency? Partially addressed by subsequent work: TTT-E2E (2025-12-ttt-e2e-long-context) evaluates Gated DeltaNet as a baseline and finds it does not scale with context length as well as full attention beyond 32K.

4. **Optimal hybrid ratios.** The paper explores two specific hybrid configurations (H1, H2) with ablation on layer ordering (Table S.2) but does not systematically search over attention-to-recurrence ratios. Subsequent work like Kimi Linear finds 3:1 KDA-to-attention is optimal for their setting.

---

## Core References and Why They Are Referenced

### Delta Rule Foundations

- **Widrow et al. (1960)** -- *Adaptive Switching Circuits.* Introduces the delta rule (Widrow-Hoff learning rule), the foundational update mechanism that Gated DeltaNet extends.

- **Schlag et al. (2021a)** -- *Linear Transformers Are Secretly Fast Weight Programmers.* Interprets linear Transformers as fast weight programmers and connects the delta rule to this framework; establishes the memory collision problem with linear attention and demonstrates DeltaNet's superior associative recall.

- **Yang et al. (2024b)** -- *Parallelizing Linear Transformers with the Delta Rule over Sequence Length.* Introduces hardware-efficient chunkwise parallel training for DeltaNet using the WY representation. Gated DeltaNet directly extends this algorithm with gating terms.

### Gated Linear RNN Foundations

- **Dao & Gu (2024a/b)** -- *Transformers Are SSMs.* Introduces Mamba2, which uses the gated update rule S_t = alpha_t S_{t-1} + v_t k_t^T and the state space duality (SSD) framework. Gated DeltaNet combines this gating with the delta rule.

- **Yang et al. (2024a)** -- *Gated Linear Attention Transformers with Hardware-Efficient Training.* GLA introduces data-dependent gating to linear attention with efficient training via chunkwise parallelism and extended WY representation. Gated DeltaNet extends this line by adding the delta rule.

### Online Learning Framework

- **Liu et al. (2024)** -- *Longhorn: State Space Models Are Amortized Online Learners.* Provides the unifying online learning framework used to interpret recurrent state updates as closed-form optimization solutions (Table 1). Longhorn's update rule closely resembles the delta update rule.

### Fast Weight Programming

- **Irie et al. (2022a)** -- *The Dual Form of Neural Networks Revisited.* Provides the fast weight programming perspective used to interpret the hidden state as a weight matrix being optimized via test-time SGD.

### Evaluated Baselines

- **Sun et al. (2023a)** -- *RetNet: Retentive Network.* Evaluated baseline; uses data-independent exponential decay. Gated DeltaNet outperforms across all benchmarks (52.02 vs 55.32 avg, Table 3).

- **Qin et al. (2024b)** -- *HGRN2: Gated Linear RNNs with State Expansion.* Evaluated baseline; hierarchically gated recurrent model with state expansion.

- **Ren et al. (2024)** -- *Samba: Simple Hybrid State Space Models.* Evaluated hybrid baseline combining Mamba with SWA. Gated DeltaNet-H2 outperforms Samba across all domains.

- **Gu & Dao (2023)** -- *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* The original Mamba architecture, evaluated as a baseline.

### Synthetic Benchmarks

- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* Provides S-NIAH benchmark suite used for controlled analysis of gating vs delta rule tradeoffs (Table 2).

- **Arora et al. (2024b)** -- *Just Read Twice: Closing the Recall Gap for Recurrent Language Models.* Provides real-world recall-intensive tasks (SWDE, SQuAD, FDA, TriviaQA, NQ, Drop) used for evaluation (Table 4) and task formatting prompts.

### Long-Context Evaluation

- **Bai et al. (2023)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* Provides the 14-task long-context benchmark used for evaluation (Table 5).

### Concurrent and Related Work

- **Behrouz et al. (2024)** -- *Titans: Learning to Memorize at Test Time.* Concurrent work demonstrating weight decay in RNN test-time SGD updates; uses nonlinear recurrence which sacrifices parallelism.

- **Grazzi et al. (2024)** -- *Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues.* Proposes extending beta range to (0, 2) for negative eigenvalues, enabling state tracking. Compatible with Gated DeltaNet but not evaluated in this paper.

- **Siems et al. (2025)** -- *DeltaProduct: Multiple Householder Products for High-Rank Transformations.* Proposes multiple products of Householder transition matrices for higher-rank transformations. Compatible with Gated DeltaNet.
