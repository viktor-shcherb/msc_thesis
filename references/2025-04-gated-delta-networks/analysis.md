---
title: "Gated Delta Networks: Improving Mamba2 with Delta Rule"
authors: "Yang, Kautz, Hatamizadeh"
year: 2025
venue: "ICLR 2025"
paper_type: conference-paper
categories: ["architecture", "attention-efficiency", "state-space-models"]
scope: ["linear recurrent models", "gated delta rule", "hardware-efficient chunkwise training", "hybrid attention architectures"]
benchmarks_used: ["perplexity-wikitext103", "lambada", "piqa", "hellaswag", "winogrande", "arc", "boolq", "siqa", "longbench", "perplexity-govreport", "perplexity-qmsum", "perplexity-pg19", "niah"]
models_introduced: ["gated-deltanet-1.3b", "gated-deltanet-h1-1.3b", "gated-deltanet-h2-1.3b"]
models_evaluated: ["mamba-1.4b"]
key_claims:
  - id: C1
    claim: "Gated DeltaNet consistently outperforms Mamba2 and DeltaNet across language modeling, commonsense reasoning, in-context retrieval, length extrapolation, and long-context understanding"
    evidence: "Tables 2-5, Figure 2"
    status: supported
    scope: "1.3B parameters, 100B tokens training, FineWeb-Edu"
    magnitude: "55.32 vs 54.89 (Mamba2) vs 52.14 (DeltaNet) avg on LM+reasoning benchmarks (Table 3)"
  - id: C2
    claim: "Gating and delta rule are complementary: gating enables rapid memory erasure while delta rule enables targeted memory updates"
    evidence: "Table 2, Section 3.2"
    status: supported
    scope: "S-NIAH synthetic benchmarks at 1.3B scale"
  - id: C3
    claim: "Gated delta rule introduces only marginal overhead over the original delta rule, achieving essentially the same training throughput as DeltaNet"
    evidence: "Figure 3, Section 4"
    status: supported
    scope: "1.3B models on single H100 GPU"
    magnitude: "~same tokens/sec as DeltaNet; both 2-3K tokens/sec slower than Mamba2"
  - id: C4
    claim: "Hybrid Gated DeltaNet models with sliding window attention further improve over pure recurrent models"
    evidence: "Tables 3-5"
    status: supported
    scope: "1.3B parameters, SWA window size 2K"
    magnitude: "Gated DeltaNet-H2 avg 56.18 vs 55.32 pure Gated DeltaNet on LM+reasoning (Table 3)"
  - id: C5
    claim: "Gated DeltaNet achieves the lowest overall perplexity across tasks among RNN models in length extrapolation up to 20K tokens"
    evidence: "Figure 2"
    status: supported
    scope: "6 long-context benchmarks, trained at 4K, evaluated up to 20K"
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
    type: evaluated-by
    detail: "TTT-E2E evaluates Gated DeltaNet as a baseline at 3B scale; finds it does not scale with context length as well as full attention beyond 32K"
open_questions:
  - question: "How does Gated DeltaNet scale beyond 1.3B parameters to 7B+ model sizes?"
    addressed_by: null
  - question: "Can the gated delta rule benefit from negative eigenvalues or high-rank transition matrices (Grazzi et al., 2024; Siems et al., 2025)?"
    addressed_by: null
  - question: "How does Gated DeltaNet compare to nonlinear recurrence methods like TTT and Titans?"
    addressed_by: 2025-12-ttt-e2e-long-context
---

# Gated Delta Networks: Improving Mamba2 with Delta Rule

**Authors:** Songlin Yang, Jan Kautz, Ali Hatamizadeh (MIT CSAIL, NVIDIA)
**Date:** April 2025, ICLR 2025 (arXiv:2412.06464)

---

## Core Research Problem

Linear Transformers replace softmax attention with kernelized dot-product linear attention, reducing inference memory requirements by reframing attention as a linear RNN with matrix-valued states. While early linear Transformers underperformed standard Transformers, recent models incorporating data-dependent gating---such as GLA (Yang et al., 2024a) and Mamba2 (Dao & Gu, 2024a)---have narrowed the gap. However, challenges persist in managing information over long sequences, particularly for **in-context retrieval** tasks where standard Transformers maintain their advantage (Arora et al., 2023a; 2024a; Jelassi et al., 2024; Wen et al., 2024; Akyurek et al., 2024).

Linear Transformers can be interpreted as implementing an outer-product-based key-value association memory (Smolensky, 1990). The number of orthogonal key-value pairs they can store is **bounded** by the model's dimensionality. When the sequence length exceeds this capacity, "memory collisions" become inevitable, hindering exact retrieval (Schlag et al., 2021a).

Two distinct mechanisms have been explored to address this:

1. **Gating** (as in Mamba2): A gated update rule S_t = α_t S_{t-1} + v_t k_t^T, where α_t ∈ (0,1) uniformly decays all key-value associations. This enables adaptive memory control but treats all stored associations equally during forgetting.

2. **Delta rule** (as in DeltaNet): An update rule S_t = S_{t-1}(I - β_t k_t k_t^T) + β_t v_t k_t^T that selectively replaces one key-value pair at a time. This enables precise memory modification but lacks the ability to rapidly clear outdated or irrelevant information during context switches.

**The core challenge is: how to combine the complementary advantages of gating (bulk memory erasure) and the delta rule (targeted memory updates) in a hardware-efficient manner.**

---

## Problem Solutions

The paper proposes the **gated delta rule**, a simple formulation that combines both mechanisms:

1. **Unified update rule.** Introduce a data-dependent gating term α_t into the delta rule: S_t = S_{t-1}(α_t(I - β_t k_t k_t^T)) + β_t v_t k_t^T. Setting α_t → 0 clears memory; setting α_t → 1 recovers the pure delta rule.

2. **Hardware-efficient chunkwise parallel algorithm.** Extend Yang et al. (2024b)'s WY-representation-based algorithm for DeltaNet to incorporate gating terms, preserving chunkwise parallelism for efficient GPU training.

3. **Hybrid architectures.** Combine Gated DeltaNet layers with sliding window attention (SWA) and/or Mamba2 layers to exploit complementary strengths of local attention and linear recurrence.

---

## Approach Details

### Method

#### Gated Delta Rule (Eq. 10)

The proposed state update is:

> **S_t = S_{t-1} (α_t (I - β_t k_t k_t^T)) + β_t v_t k_t^T**

where:
- **S_t** ∈ R^{d_v × d_k} is the recurrent state (matrix-valued memory)
- **α_t** ∈ (0, 1) is a data-dependent scalar gating term controlling state decay
- **β_t** ∈ (0, 1) is the "writing strength" for the delta rule update
- **k_t**, **v_t** are key and value vectors at position t
- Output: **o_t = S_t q_t** where **q_t** is the query vector

This formulation unifies gating and delta rule advantages:
- The gating term α_t enables **adaptive memory management** (bulk decay)
- The delta update structure (I - β_t k_t k_t^T) enables **targeted key-value association learning**

#### Online Learning Interpretation

The paper frames recurrent state updates as closed-form solutions to online learning objectives (Table 1, following Liu et al., 2024):

| Method | Online Learning Objective | Online Update |
|--------|--------------------------|---------------|
| Linear Attention | ‖S_t - S_{t-1}‖²_F - 2⟨S_t k_t, v_t⟩ | S_t = S_{t-1} + v_t k_t^T |
| Mamba2 | ‖S_t - α_t S_{t-1}‖²_F - 2⟨S_t k_t, v_t⟩ | S_t = α_t S_{t-1} + v_t k_t^T |
| DeltaNet | ‖S_t - S_{t-1}‖²_F - 2⟨S_t k_t, β_t(v_t - S_{t-1} k_t)⟩ | S_t = S_{t-1}(I - β_t k_t k_t^T) + β_t v_t k_t^T |
| **Gated DeltaNet** | ‖S_t - α_t S_{t-1}‖²_F - 2⟨S_t k_t, β_t(v_t - α_t S_{t-1} k_t)⟩ | S_t = S_{t-1}(α_t(I - β_t k_t k_t^T)) + β_t v_t k_t^T |

From the fast weight programming perspective (Irie et al., 2022a), the state S can be interpreted as a (fast) weight matrix optimizing the online regression objective L(S_t) = ½‖S_t k_t - v_t‖² via test-time stochastic gradient descent. The gated delta rule adds **adaptive weight decay** (α_t) to this SGD update.

### Key Technical Components

#### Hardware-Efficient Chunkwise Training (Section 3.3)

The gated delta rule recurrence is partially expanded over chunks of size C:

> S^r_{[t]} = S_{[t]} ∏_{i=1}^{r} α^i_{[t]}(I - β^i_{[t]} k^i_{[t]} k^{iT}_{[t]}) + Σ_{i=1}^{r} (β^i_{[t]} v^i_{[t]} k^{iT}_{[t]} ∏_{j=i+1}^{r} α^j_{[t]}(I - β^j_{[t]} k^j_{[t]} k^{jT}_{[t]}))

The cumulative products of generalized Householder matrices are optimized using the classical WY representation (Bischof & Loan, 1985). By the UT transform (Joffrain et al., 2006), the W and U matrices are computed as:

> T̃_{[t]} = [I + strictLower(diag(β_{[t]})(Γ_{[t]} ⊙ K_{[t]} K^T_{[t]}))]^{-1} diag(β_{[t]})

> W̃_{[t]} = T̃_{[t]} K_{[t]}, Ũ_{[t]} = T̃_{[t]} V_{[t]}

The final chunkwise state update and output computation:

> S_{[t+1]} = S̄_{[t]} + (Ũ_{[t]} - W̃_{[t]} S̄^T_{[t]})^T K̄_{[t]}

> O_{[t]} = Q̃_{[t]} S̄^T_{[t]} + (Q_{[t]} K^T_{[t]} ⊙ M)(Ũ_{[t]} - W̃_{[t]} S̄^T_{[t]})

where arrows denote decay-adjusted versions of vectors and matrices. These equations are rich in matrix multiplications, enabling tensor-core-based GPU optimization.

#### Gated DeltaNet Architecture (Section 3.4)

The token mixer block follows LLaMA's macro architecture:
- **Query/Key path:** Linear projection → short convolution → SiLU activation → L2 normalization
- **Value path:** Linear projection → short convolution → SiLU activation
- **α, β:** Linear projection only (following Sun et al., 2023a)
- **Output:** Normalization → gating → output projection with SiLU

Full model stacks token mixer layers with SwiGLU MLP layers.

#### Hybrid Models (Section 3.4)

- **Gated DeltaNet-H1:** Alternates Gated DeltaNet layers with SWA layers
- **Gated DeltaNet-H2:** Stacks Mamba2 + Gated DeltaNet + SWA layers

The hybrid variants address the limitation that linear recurrent models struggle with local context modeling and retrieval due to fixed state size (Arora et al., 2024a).

### Experimental Setup

**Training:** All models trained identically with 1.3B parameters on 100B tokens from FineWeb-Edu (Penedo et al., 2024). AdamW optimizer with peak learning rate 4e-4, weight decay 0.1, gradient clipping 1.0. Cosine annealing schedule with 1B token warm-up. Batch size 0.5M tokens. Llama2 tokenizer with vocabulary size 32,000. Training sequence length 4K tokens; SWA window size 2K.

**Model details:** 400M and 1.3B parameter variants trained. Primary comparisons at 1.3B scale.

**Baselines:** RetNet (Sun et al., 2023a), HGRN2 (Qin et al., 2024b), Mamba (Gu & Dao, 2023), Mamba2 (Dao & Gu, 2024b), Samba (Ren et al., 2024), DeltaNet (Yang et al., 2024b), Transformer++.

**Evaluation domains:**
1. Language modeling perplexity (WikiText-103, LAMBADA)
2. Zero-shot commonsense reasoning (PIQA, HellaSwag, WinoGrande, ARC-e, ARC-c, SocialIQA, BoolQ)
3. In-context retrieval (S-NIAH from RULER; real-world recall tasks from Arora et al., 2024b)
4. Length extrapolation (perplexity on GovReport, QMSum, NarrativeQA, Qasper, CodeParrot, PG19 at 4K-20K)
5. Long-context understanding (LongBench, 14 tasks)

### Key Results

#### Synthetic In-Context Retrieval (S-NIAH, Table 2)

| Model | S-NIAH-1 1K/2K/4K/8K | S-NIAH-2 1K/2K/4K/8K | S-NIAH-3 1K/2K/4K |
|-------|------------------------|------------------------|---------------------|
| DeltaNet | 97.4 / 96.8 / 99.0 / 98.8 | 98.4 / 45.6 / 18.6 / 14.4 | 85.2 / 47.0 / 22.4 |
| Mamba2 | 99.2 / 98.8 / 65.4 / 30.4 | 99.4 / 98.8 / 56.2 / 17.0 | 64.4 / 47.6 / 4.6 |
| **Gated DeltaNet** | **98.4 / 88.4 / 91.4 / 91.8** | **100.0 / 99.8 / 92.2 / 29.6** | **86.6 / 84.2 / 27.6** |

**Key findings from S-NIAH analysis (Section 3.2):**
- **S-NIAH-1 (passkey retrieval):** Decay hurts memory retention. DeltaNet achieves near-perfect across all lengths; Mamba2 degrades beyond 2K due to excessive decay. Gated DeltaNet's degradation is less severe.
- **S-NIAH-2 (number in haystack):** Gating facilitates filtering. DeltaNet's performance drops at longer sequences due to memory collision. Mamba2 and Gated DeltaNet maintain better performance through gating mechanisms that filter irrelevant information.
- **S-NIAH-3 (UUID in haystack):** Delta rule helps memorization. Mamba2 drops quickly; Gated DeltaNet performs better, verifying superior memorization ability.

#### Language Modeling and Commonsense Reasoning (Table 3)

| Model | Wiki. ppl↓ | LMB. ppl↓ | LMB. acc↑ | PIQA↑ | Hella.↑ | Wino.↑ | ARC-e↑ | ARC-e_n↑ | SIQA↑ | BoolQ↑ | Avg.↑ |
|-------|-----------|-----------|-----------|-------|---------|--------|--------|----------|-------|--------|-------|
| *Recurrent models* | | | | | | | | | | | |
| RetNet | 19.08 | 17.27 | 40.52 | 70.07 | 49.16 | 54.14 | 67.34 | 33.78 | **40.78** | 60.39 | 52.02 |
| HGRN2 | 19.10 | 17.69 | 39.54 | 70.45 | 49.53 | 52.80 | 69.40 | 35.32 | 40.63 | 56.66 | 51.79 |
| Mamba | 17.92 | 15.06 | 43.98 | 71.32 | 52.91 | 52.95 | 69.52 | 35.40 | 37.76 | 61.13 | 53.12 |
| Mamba2 | **16.56** | 12.56 | 45.66 | 71.87 | 55.67 | 55.24 | **72.47** | 37.88 | 40.20 | 60.13 | 54.89 |
| DeltaNet | 17.71 | 16.88 | 42.46 | 70.72 | 50.93 | 53.35 | 68.47 | 35.66 | 40.22 | 55.29 | 52.14 |
| **Gated DeltaNet** | 16.42 | **12.17** | **46.65** | **72.25** | **55.76** | **57.45** | 71.21 | **38.39** | 40.63 | **60.24** | **55.32** |
| *Hybrid models* | | | | | | | | | | | |
| Transformer++ | 18.53 | 18.32 | 42.60 | 70.02 | 50.23 | 53.51 | 68.83 | 35.10 | 40.66 | 57.09 | 52.25 |
| Samba | 16.13 | 13.39 | 44.94 | **70.94** | **53.42** | **55.56** | 68.81 | 36.17 | 39.96 | **62.11** | 54.00 |
| **Gated DeltaNet-H1** | 16.07 | 12.12 | 47.73 | 72.57 | 56.53 | **58.40** | **71.25** | **40.10** | **41.40** | **63.21** | **56.40** |
| **Gated DeltaNet-H2** | **15.91** | **12.55** | **48.76** | **72.19** | **56.88** | 57.77 | 71.33 | 39.07 | **41.91** | 61.55 | **56.18** |

Gated DeltaNet consistently outperforms all linear recurrent models. Hybrid variants further improve, with H1 achieving the best average.

#### Real-World In-Context Retrieval (Table 4)

| Model | SWDE | SQD | FDA | TQA | NQ | Drop | Avg |
|-------|------|-----|-----|-----|----|------|-----|
| *Recurrent models* | | | | | | | |
| RetNet | 14.0 | 28.5 | 7.0 | 54.4 | 16.2 | 17.3 | 22.9 |
| Mamba2 | 19.1 | 33.6 | **25.3** | **61.0** | **20.8** | 19.2 | 29.8 |
| DeltaNet | 17.9 | 30.9 | 18.4 | 53.9 | 17.3 | 18.6 | 26.2 |
| **Gated DeltaNet** | **25.4** | **34.8** | 23.7 | **60.0** | 20.0 | **19.8** | **30.6** |
| *Hybrid models* | | | | | | | |
| Transformer++ | 29.5 | 38.0 | **52.2** | 58.3 | **22.5** | **21.6** | **37.0** |
| Samba | 33.0 | 39.2 | 50.5 | 57.7 | 23.5 | 20.2 | 37.3 |
| **Gated DeltaNet-H1** | 35.6 | 39.7 | 52.0 | 60.1 | 24.6 | 22.2 | 39.0 |
| **Gated DeltaNet-H2** | **38.2** | **40.4** | **50.7** | **63.3** | **24.8** | **23.3** | **40.1** |

Gated DeltaNet outperforms both DeltaNet and Mamba2 among pure recurrent models. Hybrid Gated DeltaNet-H2 achieves the best overall recall performance, outperforming even Transformer++.

#### Long-Context Understanding (LongBench, Table 5)

Average across 14 LongBench tasks:

| Model | Avg |
|-------|-----|
| RetNet | 13.2 |
| Mamba2 | 13.5 |
| DeltaNet | 13.6 |
| **Gated DeltaNet** | **16.6** |
| Transformer++ | 11.0 |
| Samba | 15.9 |
| **Gated DeltaNet-H1** | **17.8** |
| **Gated DeltaNet-H2** | **18.4** |

Gated DeltaNet shows consistent advantages in single-doc QA, few-shot in-context learning, and code tasks on LongBench.

#### Training Throughput (Figure 3)

On a single H100 GPU at 1.3B scale:
- Transformer++ achieves highest throughput at short sequences (2K×16 batch) due to Flash-Attention-2 optimization
- Gated DeltaNet achieves essentially the same throughput as DeltaNet (~same tokens/sec)
- Both are slightly slower than Mamba2 (by 2-3K tokens/sec) due to more expressive transition matrices
- Gated DeltaNet-H1 maintains competitive throughput across all sequence lengths, outperforming standalone Mamba at longer sequences

---

## Limitations and Failure Modes

### Acknowledged Limitations

1. **Scale.** Experiments limited to 1.3B parameters on 100B tokens. Scaling behavior at 7B+ is unknown.

2. **Real-world retrieval gap.** The improvement margin of Gated DeltaNet over Mamba2 on real-world retrieval tasks (Table 4: 30.6 vs 29.8 avg) is smaller than on synthetic S-NIAH benchmarks (Table 2). The authors attribute this to instruction-unaligned small language models being prone to repetition errors, which are independent of the update rule choice (Section 4, citing Arora et al., 2024b, Appendix E).

3. **Throughput trade-off.** Gated DeltaNet and DeltaNet are slightly slower than Mamba2 due to their more expressive identity-plus-low-rank transition matrices vs Mamba2's diagonal matrices (Figure 3).

4. **Delta rule theoretical limitations.** The delta rule faces theoretical limitations (Irie et al., 2023) and shows only moderate performance on real-world datasets (Yang et al., 2024b), suggesting room for further improvement.

### Scope and Comparability

**What was not tested:**
- Models larger than 1.3B parameters
- Instruction tuning, RLHF, or chat applications
- Comparison with nonlinear recurrence methods (TTT, Titans) at scale
- Evaluation on RULER or other standardized multi-task long-context benchmarks beyond LongBench

**Comparability notes:**
- All models trained on identical data (100B tokens, FineWeb-Edu) with same tokenizer (Llama2, 32K vocab)
- Transformer++ baseline uses modern recipe but trained at same 1.3B scale, enabling fair comparison
- Hybrid models use 2K SWA window; Samba also uses 2K window for comparability

---

## Conclusions

### Contributions

1. **Gated delta rule.** Proposed a simple unified state update rule combining Mamba2's gated decay with DeltaNet's targeted memory replacement (Eq. 10). Demonstrated through S-NIAH analysis that gating and delta rule are complementary: gating enables filtering, delta rule enables memorization (Table 2, Section 3.2).

2. **Hardware-efficient chunkwise algorithm.** Extended Yang et al. (2024b)'s WY-representation-based parallel algorithm to incorporate gating terms, maintaining DeltaNet-level training throughput while adding gating capabilities (Figure 3, Section 3.3).

3. **Consistent improvements across benchmarks.** Gated DeltaNet outperforms Mamba2 and DeltaNet on language modeling, commonsense reasoning, in-context retrieval, length extrapolation, and long-context understanding at 1.3B scale (Tables 2-5, Figure 2).

4. **Effective hybrid architectures.** Introduced Gated DeltaNet-H1 (with SWA) and H2 (with Mamba2 + SWA), which further improve performance while maintaining competitive training throughput (Tables 3-5, Figure 3).

### Implications

1. **Combining update rules is effective.** The success of unifying gating and delta rule suggests that future linear recurrent architectures should incorporate multiple complementary memory mechanisms rather than relying on a single update rule.

2. **Practical adoption.** Gated DeltaNet has been adopted by Qwen3 (Qwen Team, 2025) and Kimi Linear (Kimi Team, 2025), demonstrating its practical value for production-scale models. Kimi Linear further extends the approach with channel-wise gating.

3. **Hybrid architectures remain beneficial.** Even with improved recurrent mechanisms, hybridizing with attention continues to provide gains, particularly for retrieval-intensive tasks (speculative: this gap may narrow with further improvements to linear recurrent models).

---

## Key Claims

1. **C1:** Gated DeltaNet consistently outperforms Mamba2 and DeltaNet across language modeling, commonsense reasoning, in-context retrieval, length extrapolation, and long-context understanding (Tables 2-5, Figure 2). Supported by comprehensive evaluation at 1.3B scale on 100B tokens with identical training setup.

2. **C2:** Gating and delta rule are complementary mechanisms---gating enables rapid memory erasure while delta rule facilitates targeted updates (Table 2, Section 3.2). Supported by controlled S-NIAH experiments showing each mechanism excels in different settings (S-NIAH-1 vs S-NIAH-2/3).

3. **C3:** Gated delta rule introduces only marginal overhead over the original delta rule (Figure 3, Section 4). Supported by throughput comparison on single H100 GPU showing essentially identical tokens/sec to DeltaNet.

4. **C4:** Hybrid Gated DeltaNet models with sliding window attention further improve over pure recurrent models (Tables 3-5). Supported by results showing H1 and H2 outperform pure Gated DeltaNet and other hybrids (Samba) across all evaluation domains.

5. **C5:** Gated DeltaNet achieves the lowest overall perplexity across tasks among RNN models in length extrapolation up to 20K tokens (Figure 2). Supported by perplexity curves on 6 long-context benchmarks; note that results are mixed across individual tasks but Gated DeltaNet is most robust overall.

---

## Open Questions

1. **Scaling beyond 1.3B.** All experiments use 1.3B parameters on 100B tokens. Does the advantage of Gated DeltaNet over Mamba2 persist or widen at 7B+ scale? Qwen3 and Kimi Linear adopt the approach at larger scales, but controlled comparisons are not available in this paper.

2. **Nonlinear extensions.** The paper mentions that nonlinear recurrence methods (TTT, Titans) offer more expressive alternatives but sacrifice parallelism. Can Gated DeltaNet be extended with nonlinear elements while preserving chunkwise training efficiency?

3. **Negative eigenvalues and high-rank transitions.** Recent work on negative eigenvalues (Grazzi et al., 2024) and DeltaProduct (multiple Householder products; Siems et al., 2025) could enhance Gated DeltaNet's expressiveness. The paper notes these are compatible but does not evaluate them.

4. **Optimal hybrid ratios.** The paper explores two specific hybrid configurations (H1, H2) but does not systematically search over attention-to-recurrence ratios or layer patterns. Subsequent work like Kimi Linear finds 3:1 KDA-to-attention is optimal for their setting.

---

## Core References and Why They Are Referenced

### Delta Rule Foundations

- **Widrow et al. (1960)** -- *Adaptive Switching Circuits.* Introduces the delta rule (Widrow-Hoff learning rule), the foundational update mechanism that Gated DeltaNet extends.

- **Schlag et al. (2021a)** -- *Linear Transformers Are Secretly Fast Weight Programmers.* Interprets linear Transformers as fast weight programmers and connects the delta rule to this framework; DeltaNet builds on this perspective.

- **Yang et al. (2024b)** -- *Parallelizing Linear Transformers with the Delta Rule over Sequence Length.* Introduces hardware-efficient chunkwise parallel training for DeltaNet using the WY representation. Gated DeltaNet directly extends this algorithm with gating terms.

### Gated Linear RNN Foundations

- **Dao & Gu (2024a/b)** -- *Transformers Are SSMs.* Introduces Mamba2, which uses the gated update rule S_t = α_t S_{t-1} + v_t k_t^T. Gated DeltaNet combines this gating with the delta rule.

- **Yang et al. (2024a)** -- *Gated Linear Attention Transformers with Hardware-Efficient Training.* GLA introduces data-dependent gating to linear attention with efficient training. Gated DeltaNet extends this line by adding the delta rule.

### Online Learning Framework

- **Liu et al. (2024)** -- *Longhorn: State Space Models Are Amortized Online Learners.* Provides the unifying online learning framework used to interpret recurrent state updates as closed-form optimization solutions (Table 1).

### Evaluated Baselines

- **Sun et al. (2023a)** -- *RetNet: Retentive Network.* Evaluated baseline; uses data-independent exponential decay.

- **Qin et al. (2024b)** -- *HGRN2: Gated Linear RNNs with State Expansion.* Evaluated baseline; hierarchically gated recurrent model.

- **Ren et al. (2024)** -- *Samba: Simple Hybrid State Space Models.* Evaluated hybrid baseline combining Mamba with SWA.

### Synthetic Benchmarks

- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* Provides S-NIAH benchmark suite used for controlled analysis of gating vs delta rule tradeoffs (Table 2).

- **Arora et al. (2024b)** -- *Just Read Twice: Closing the Recall Gap for Recurrent Language Models.* Provides real-world recall-intensive tasks used for evaluation (Table 4).
