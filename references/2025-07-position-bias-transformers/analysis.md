---
title: "On the Emergence of Position Bias in Transformers"
authors: "Wu, Wang, Jegelka, Jadbabaie"
year: 2025
venue: "ICML 2025"
paper_type: conference-paper
categories: ["position-bias", "position-encoding", "attention-analysis"]
scope: ["theoretical analysis of position bias", "graph-theoretic framework for attention", "causal masking", "RoPE decay analysis", "ALiBi decay analysis", "attention sinks"]
benchmarks_used: []
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "Under causal masking, cumulative context probability converges exponentially to the first token as depth increases, regardless of input content"
    evidence: "Theorem 4.1, Section 4.1"
    status: supported
  - id: C2
    claim: "Attention sinks arise because initial tokens are center nodes in the attention mask graph, whose influence accumulates across layers due to the non-negativity of softmax"
    evidence: "Theorems 4.1-4.3, Appendix K.4, Figures 10-12"
    status: supported
  - id: C3
    claim: "The decay mask (ALiBi) and causal mask produce a non-monotonic cumulative context distribution across layers, with critical point x* = t/(e^m - 1) shifting toward earlier tokens as depth increases"
    evidence: "Theorem 4.5, Section 4.2"
    status: supported
  - id: C4
    claim: "RoPE induces Gaussian-like decay proportional to (i-j)^2 * theta_1^2, substantially weaker than the decay mask's linear exponential decay proportional to (i-j) * m"
    evidence: "Lemma 4.6 vs Lemma 4.4, Section 4.3"
    status: supported
  - id: C5
    claim: "The causal mask does not simulate positional encodings but instead introduces a directional bias toward earlier positions via iterative attention"
    evidence: "Section 5.2, Figure 3"
    status: supported
  - id: C6
    claim: "The lost-in-the-middle U-shaped phenomenon only emerges when training data contains positional bias toward both the beginning and end of sequences"
    evidence: "Section 5.2, Appendix K.3, Figures 3 and 6-8"
    status: supported
  - id: C7
    claim: "Deeper attention consistently amplifies bias toward earlier tokens regardless of PE type, when no residual connections are used"
    evidence: "Figure 2, Figure 4, Section 5.1"
    status: supported
cross_references:
  - target: 2024-02-lost-in-the-middle
    type: formalizes
    detail: "Provides a theoretical framework explaining why the U-shaped position bias documented by Liu et al. occurs, showing it requires both architectural bias (causal mask) and data bias (toward first and last positions)"
  - target: 2024-08-found-in-the-middle
    type: complementary
    detail: "Both address position bias: this paper provides graph-theoretic analysis of its emergence, while Found in the Middle proposes calibration-based mitigation"
  - target: 2024-05-attention-sinks-streaming
    type: formalizes
    detail: "Provides theoretical explanation for attention sinks: they arise because initial tokens are center nodes in the attention mask graph whose influence accumulates across layers (Theorems 4.1-4.3)"
  - target: 2020-07-quantifying-attention-flow
    type: extends
    detail: "The cumulative context probability P^(t)(z_i = j) analyzed here coincides with the attention rollout metric, but this paper treats it as a theoretical object analyzed across arbitrary inputs rather than an empirical visualization tool"
  - target: 2022-04-alibi-train-short-test-long
    type: evaluates
    detail: "Theoretically characterizes ALiBi's decay mask: single-layer exponential decay (Lemma 4.4) and multi-layer non-monotonic trade-off with critical point x* = t/(e^m - 1) (Theorem 4.5)"
  - target: 2024-01-roformer-rope
    type: evaluates
    detail: "Theoretically characterizes RoPE's decay properties: Gaussian-like decay proportional to (i-j)^2 * theta_1^2 per layer (Lemma 4.6), substantially weaker than ALiBi due to small theta_1 ~ 1/10000"
  - target: 2020-04-longformer-long-document-transformer
    type: evaluates
    detail: "Analyzes the sliding-window attention mask: context still converges to the first token but at a slower rate governed by ceil((N-1)/(w-1)) (Theorem 4.2)"
  - target: 2025-11-pos2distill-position-bias-distillation
    type: extended-by
    detail: "Pos2Distill proposes a training-based approach to mitigate position bias, building on the theoretical understanding of its emergence provided here"
  - target: 2025-11-context-length-hurts-performance
    type: complementary
    detail: "Both find that context can hurt performance; this paper analyzes the positional mechanism while that paper measures the empirical effect of context length"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: complementary
    detail: "DroPE addresses position bias by dropping positional embeddings at inference; this paper provides theoretical grounding for why RoPE introduces distance-dependent decay"
  - target: 2022-12-nope-transformers-learn-positions
    type: complementary
    detail: "Haviv et al. conjecture that causal masking enables implicit positional encoding; this paper's analysis (C5) shows the causal mask introduces directional bias toward earlier positions rather than simulating full positional encodings"
  - target: 2023-12-positional-encoding-length-generalization
    type: complementary
    detail: "Kazemnejad et al. hypothesize that NoPE learns relative PE via the causal mask; Wu et al. provide a different perspective showing the causal mask introduces directional position bias rather than simulating PE"
  - target: 2024-07-llama-3-herd-of-models
    type: evaluates
    detail: "Position bias analysis conducted on Llama 3 models"
  - target: 2024-12-transformers-need-glasses-over-squashing
    type: concurrent
    detail: "Both provide theoretical analysis of position-dependent information flow in causal Transformers; Barbero et al. use gradient sensitivity bounds from GNN over-squashing theory while this paper uses graph-theoretic cumulative context probability"
  - target: 2025-07-position-bias-single-dimension-scaling
    type: complementary
    detail: "Both identify causal masking as a source of position bias: this paper proves it theoretically via exponential convergence (Theorem 4.1), while Yu et al. demonstrate it empirically through perturbation experiments on hidden states channels and propose single-channel scaling as mitigation"
  - target: 2025-04-pine-eliminating-position-bias
    type: complementary
    detail: "PINE provides a practical inference-time solution to position bias (bidirectional inter-document attention + importance-based position re-assignment) based on similar mechanistic insights about causal masking and PE-induced bias"
  - target: 2024-08-flenqa-input-length-reasoning
    type: complementary
    detail: "FlenQA empirically demonstrates position-dependent and length-dependent reasoning degradation; this paper provides theoretical grounding for why position bias emerges in causal Transformers"
open_questions:
  - question: "How do residual connections, value projections, and MLPs interact with attention to modulate position bias accumulation across layers?"
    addressed_by: null
  - question: "Does positional bias in natural language training data shape the lost-in-the-middle phenomenon in the same way as in the synthetic setting?"
    addressed_by: null
  - question: "Can the graph-theoretic framework be extended to multi-head attention, where different heads may specialize in different positional patterns?"
    addressed_by: null
  - question: "How does the geometry of token embeddings (anisotropy) influence the emergence and nature of positional bias?"
    addressed_by: null
---
# On the Emergence of Position Bias in Transformers

**Authors:** Xinyi Wu, Yifei Wang, Stefanie Jegelka, Ali Jadbabaie (MIT IDSS & LIDS, MIT CSAIL, TU Munich)
**Date:** July 2025, ICML 2025, PMLR 267 (arXiv:2502.01951)

---

## Core Research Problem

Transformer-based models exhibit systematic **position bias** -- a tendency to focus on certain regions of the input regardless of semantic content. This manifests in several well-documented phenomena: the "lost-in-the-middle" problem where retrieval accuracy degrades for information in the middle of the context (Liu et al., 2024); sensitivity of in-context learning to example ordering (Lu et al., 2022; Min et al., 2022); and attention sinks where initial tokens attract disproportionately high attention (Gu et al., 2025; Xiao et al., 2024). While mitigation strategies such as novel positional encodings (Kazemnejad et al., 2023), alternative masking techniques (Fang et al., 2025; Wang et al., 2024), and bootstrapping (Hou et al., 2024) have been proposed, they remain task-specific and empirically driven.

Prior theoretical work has analyzed attention masks for function approximation (Yun et al., 2020b), rank collapse mitigation (Wu et al., 2023; 2024), and the effect of PEs on length generalization (Kazemnejad et al., 2023), but fundamental questions remain about the mechanisms through which attention masks and positional encodings jointly produce systematic positional biases. The core challenge is: **how do attention masks and positional encodings shape position bias in multi-layer transformers?**

---

## Problem Solutions

The paper develops a **graph-theoretic framework** for analyzing position bias in multi-layer attention, modeling attention masks as directed graphs and tracking cumulative context distributions across layers. The key contributions are:

1. **Causal masking creates inherent primacy bias.** In deeper layers, tokens attend to increasingly contextualized representations of earlier tokens, causing cumulative context probability to converge exponentially toward the first token -- regardless of semantic content (Theorem 4.1). Analogous results hold for sliding-window (Theorem 4.2) and prefix masks (Theorem 4.3).

2. **Relative positional encodings introduce a competing decay effect.** Both the decay mask (ALiBi) and RoPE impose distance-based decay within individual attention layers, but their aggregate effect across multiple layers coupled with the causal mask leads to a **non-monotonic trade-off** between long-term decay and cumulative early-token importance (Theorems 4.5, 4.7).

3. **Training data distribution shapes specific bias patterns.** The "lost-in-the-middle" U-shaped phenomenon only emerges when training data is biased toward both the beginning and end of sequences (Section 5.2).

---

## Approach Details

### Method

The analysis considers single-head masked self-attention networks (SANs) with the layerwise update:

> X^(t+1) = A^(t) X^(t) W_V^(t)

where A^(t) = softmax_G(X^(t) W_Q^(t) (X^(t) W_K^(t))^T / sqrt(d_QK)) and G is the directed graph defining the attention mask. The framework analyzes the **cumulative context probability**:

> P^(t)(z_i = j | X^(0)) = (A^(t) ... A^(0))_{ij}

which quantifies how much of token i's representation at depth t originates from input token j. This quantity coincides with the attention rollout metric of Abnar & Zuidema (2020), but the paper treats it as a theoretical object analyzed across arbitrary inputs to reveal inductive biases, rather than as an empirical visualization tool applied to specific sequences.

Attention masks are formalized as directed graphs G where edge (j, i) means token i attends to token j. A **center node** (Definition 3.1) is a node from which every node in G is reachable. The key property driving the results is that softmax cannot fundamentally disconnect any edge in G -- all attention weights remain strictly positive -- so center nodes accumulate influence across layers.

### Key Technical Components

**Assumptions:**
- **A1:** Bounded query/key weight matrices: max_t {||W_Q^(t)||_2, ||W_K^(t)||_2} <= C.
- **A2:** Bounded cumulative value projection: the sequence {||prod_{t=0}^k W_V^(t)||_2} is bounded, ensuring bounded token trajectories.

**Three attention mask types analyzed:**
- **Causal mask:** Token i attends to all tokens j <= i. Token 1 is the unique center node.
- **Sliding-window mask:** Token i attends to tokens in [max(1, i-w+1), i] for window width w. Token 1 remains the center node but reachability requires ceil((N-1)/(w-1)) hops.
- **Prefix mask:** The first K tokens are visible to all subsequent tokens. All K prefix tokens are center nodes.

**Two relative positional encoding types analyzed:**
- **Decay mask (ALiBi-style):** D_ij = -(i-j)m for j <= i, adding an explicit distance-based bias to attention logits with decay strength m.
- **RoPE:** Applies rotation R^d_{Theta,i} to query/key embeddings proportional to position index, with base angles Theta = {theta_1, ..., theta_{d/2}} where theta_i = 10000^{-2(i-1)/d}.

### Theoretical Analysis

**Causal mask without PE (Theorem 4.1).** For causal attention under A1-A2, for every token i:

> lim_{t->inf} P^(t)(z_i = 1 | X^(0)) = 1

with exponential convergence: P^(t)(z_i = j | X^(0)) <= C(1 - (j-1)epsilon)^t for all 1 < j <= i, where N*epsilon < 1. Context converges to the first token regardless of input content. The proof proceeds by induction using Lemma A.1, which shows that under A1-A2 there exists epsilon > 0 such that A^(t)_{ij} >= epsilon for all edges (j,i) in G (Appendix A).

**Sliding-window mask (Theorem 4.2).** Same convergence to token 1, but at a slower rate:

> P^(t)(z_i = j | X^(0)) <= C(1 - (j-1)epsilon^{ceil((N-1)/(w-1))})^{t/(2*ceil((N-1)/(w-1)))}

Smaller window w slows convergence but does not eliminate first-token dominance. The rate is governed by the number of hops ceil((N-1)/(w-1)) needed for token 1 to reach all other tokens (Appendix B).

**Prefix mask (Theorem 4.3).** Context converges to the K prefix tokens collectively, with each prefix token retaining non-trivial influence:

> lim inf_{t->inf} P^(t)(z_i = k | X^(0)) >= kappa > 0 for all k in [K]

Non-prefix tokens decay exponentially: P^(t)(z_i = j | X^(0)) <= C(1 - (j-K)epsilon)^t for all K < j <= i (Appendix C).

**Decay mask -- single layer (Lemma 4.4).** Exponential decay per layer:

> C_min * e^{-(i-j)m} <= (A^(t)_decay)_{ij} <= C_max * e^{-(i-j)m}

where C_max = e^{(I_max - I_min)}/(1 + e^{-m}) and C_min = (1 - e^{-m}) * e^{(I_min - I_max)}, with I_min, I_max being bounds on the raw attention scores (Appendix D).

**Decay mask -- multi-layer (Theorem 4.5).** The cumulative probability becomes:

> P^(t)_decay(z_i = j | X^(0)) = Theta(binom(t+i-j, i-j) * e^{-(i-j)m})

The function L(x) = log(binom(t+x, x) * e^{-xm}) is **non-monotonic** with critical point x* = t/(e^m - 1) under Stirling's approximation. Increasing decay strength m decreases x* (more recency bias); increasing depth t increases x* (more primacy bias). The proof leverages the fact that in the causal graph there are binom(t+i-j, i-j) paths of length t+1 from token j to token i, all non-decreasing in index (Appendix E).

**RoPE -- single layer (Lemma 4.6).** For d = 2 with the slowest-rotating dimension theta_1, under the condition that original query-key angles |phi^(t)_{i,j}| <= delta * theta_1 and (delta + N - 1)*theta_1 <= pi:

> C_min * e^{-c(i-j)^2 theta_1^2} <= (A^(t)_RoPE)_{ij} <= C_max * e^{-c'(i-j)^2 theta_1^2}

RoPE induces **Gaussian-like decay** in (i-j)^2, substantially weaker than the decay mask's linear exponential because theta_1 is typically ~1/10000 per token (Su et al., 2023; Dubey et al., 2024). The analysis leverages the empirical finding of Barbero et al. (2024b) that LLMs predominantly use slowly-rotating feature dimensions (Appendix F).

**RoPE -- multi-layer (Theorem 4.7).** Combining with causal mask path counting:

> P^(t)_RoPE(z_i = j | X^(0)) = Theta(binom(t+i-j, i-j) * e^{-c(i-j)^2 theta_1^2})

By implicit differentiation, the critical point x* is an increasing function of depth t (deeper models shift bias toward initial tokens) and a decreasing function of theta_1 (larger theta_1 amplifies decay toward nearby tokens) (Appendix H).

**General d >= 2 (Appendix I).** Lemma I.1 and Theorem I.2 generalize to arbitrary even dimension d, with the decay term becoming e^{-c * sum_{l=1}^{d/2} (i-j)^2 alpha_l^2 theta_1^2} where theta_l = alpha_l * theta_1. The assumption A3 requires that all length-2 segments of query and key vectors make non-trivial contributions to the norm.

### Experimental Setup

The paper uses the synthetic data framework of Reddy (2024) for controlled experiments:

- **Task:** Information retrieval -- predict the label y_query of a target x_query given an alternating sequence x_1, y_1, ..., x_n, y_n, x_query.
- **Data:** Gaussian mixture model with K = 2048 classes, L = 32 labels, burstiness B = 4, n = 8 items, d = 64 dimensions, gamma = 0.75.
- **Position bias control:** x_query is either assigned to the class of a specific x_i (position-dependent bias) or randomly assigned (no bias). Different bias conditions tested: first position only, last position only, middle position only, first and last, and no bias.
- **Evaluation:** Novel-class test sequences with 10,000 sequences per condition. Position bias measured as accuracy gap [a, b] - [b, a] between matched sequences where content at positions a and b is identical but the correct position differs. Three pairs tested: [first, middle], [first, last], [middle, last].
- **Architecture:** Single-head attention-only network followed by a 3-layer MLP classifier with ReLU activations and softmax output over L labels.
- **Conditions:** Depths 2, 4, 6 (without residual connections) and 2, 6, 10 (with residual connections). Three PE types: No PE, Decay Mask (m = -log(0.8) ~ 0.223), RoPE (theta_i = 10000^{-2(i-1)/d}).
- **Training:** AdamW optimizer, learning rate 10^{-3}, weight decay 10^{-6}, batch size 128, 100,000 iterations, Tesla V100 GPU.

### Key Results

**Effect of depth and relative PEs (no position bias in training data, no residual connections, Figure 2):**

| PE Type | Depth | First vs. Middle Gap | First vs. Last Gap | Middle vs. Last Gap |
|---|---|---|---|---|
| No PE | 2 | +0.059 | +0.077 | +0.018 |
| No PE | 6 | +0.091 | +0.106 | +0.011 |
| Decay Mask | 2 | -0.055 | -0.073 | -0.003 |
| Decay Mask | 6 | +0.020 | +0.014 | -0.010 |
| RoPE | 2 | +0.002 | -0.002 | -0.009 |
| RoPE | 6 | +0.026 | +0.044 | +0.017 |

Positive values indicate bias toward the earlier position.

- **Deeper attention consistently amplifies bias toward earlier tokens** regardless of PE type (Section 5.1, Figure 4 confirms at depth 4).
- The **decay mask introduces substantially stronger recency bias** than RoPE at shallow depth (depth 2: -0.055 vs. +0.002 for first vs. middle), consistent with the theoretical prediction that decay mask imposes linear exponential decay vs. RoPE's quadratic Gaussian-like decay.
- The **middle vs. last gap is notably smaller** than gaps involving the first position, consistent with Theorem 4.1 predicting that late-sequence tokens become less distinguishable as first-token dominance grows.

**Causal mask and positional information (2-layer, with residual connections, data biased toward first and last positions, Figure 3):**

| PE / Mask | First vs. Middle | First vs. Last | Middle vs. Last |
|---|---|---|---|
| No PE / no mask | -0.002 | 0.000 | -0.001 |
| No PE / causal | +0.276 | +0.308 | -0.006 |
| sin PE / no mask | +0.293 | +0.013 | -0.264 |
| sin PE / causal | +0.316 | +0.078 | -0.238 |
| RoPE / no mask | +0.249 | -0.002 | -0.281 |
| RoPE / causal | +0.472 | +0.433 | -0.241 |

- **The causal mask without PE introduces positional bias only at the first position**, not at the last (first vs. middle: +0.276, first vs. last: +0.308, but middle vs. last: -0.006). This contradicts the hypothesis of Kazemnejad et al. (2023) that the causal mask simulates PE; instead, the causal mask introduces a directional bias toward earlier positions via iterative attention, consistent with Theorem 4.1.
- **With sin PE or RoPE, the model captures biases at both ends**, producing a "lost-in-the-middle" U-shaped pattern (large positive first vs. middle, large negative middle vs. last, moderate first vs. last).
- **The U-shaped pattern requires data bias toward both ends.** It does not appear when training data has no position bias (Figure 2), bias only at the first position (Figure 6), only at the middle (Figure 7), or only at the last position (Figure 8). This demonstrates that the phenomenon involves an interaction between architectural bias and data-dependent learning.

**Attention sinks (Appendix K.4, Figures 10-12).** Despite the simplified setup, attention sinks emerge on center nodes as predicted by Theorems 4.1-4.3:
- Under causal masking: attention sinks on token 1 (Figure 10).
- Under sliding-window masking: attention sinks on the absolute first token (not the first token within each window), especially for larger window sizes (Figure 11).
- Under prefix masking: attention sinks on all K prefix tokens, not just token 1 (Figure 12).

These patterns match observations in real-world LLMs by Gu et al. (2025).

**Residual connections (Figure 5, Appendix K.2).** With residual connections, the relationship between depth and positional bias becomes **non-monotonic** and depends on the PE type and depth regime. For example, No PE with residual connections shows depth 2 gap of +0.247 (first vs. middle) dropping to +0.011 at depth 10, while RoPE shows +0.379 at depth 2 increasing to +0.436 at depth 6 before dropping to +0.179 at depth 10. This suggests residual connections modulate position bias accumulation in ways not captured by the pure attention analysis.

### Fixed-Vocabulary Setting

Appendix L presents results under a fixed-vocabulary setting with anisotropic embeddings (shared component lambda = 0.75). Most findings from the Gaussian mixture setting hold. A key difference is that with residual connections, increasing depth **consistently** amplifies positional bias (Figure 14), unlike the non-monotonic behavior in the Gaussian mixture setting. The authors attribute this to embedding geometry making the task significantly more challenging, suggesting that the geometry of token embeddings can influence the emergence and nature of positional bias.

---

## Limitations and Failure Modes

- **Single-head attention only.** The theoretical analysis is restricted to single-head self-attention networks. Multi-head attention, where different heads may specialize in different positional patterns, is not addressed.
- **No residual connections in theory.** Theorems 4.1-4.7 analyze pure attention without residual connections. The experimental results (Figure 5, Appendix K.2) show that residual connections introduce non-monotonic depth-bias relationships not captured by the theory.
- **No value projections or MLPs in theory.** The framework analyzes only the attention mechanism's context selection (P^(t)). The role of value projections W_V, LayerNorm, and feedforward layers in modulating position bias is not theoretically characterized.
- **Assumption on RoPE dimensions.** Lemma 4.6 assumes d = 2 (only the slowest-rotating dimension is used). The generalization to d >= 2 (Appendix I) requires assumption A3 that all segments contribute non-trivially to the norm. The practical validity of these assumptions in real LLMs is not tested.
- **Synthetic data only.** All experiments use the simplified framework of Reddy (2024) with Gaussian mixtures or fixed vocabularies. No experiments on real language data or pretrained LLMs are conducted. The authors argue that the simplified setup reproduces key phenomena (attention sinks, lost-in-the-middle) but the transfer to full-scale models is assumed, not demonstrated.
- **No mitigation proposed.** The paper provides theoretical analysis but does not propose any method to mitigate position bias.
- **Bounded attention scores assumption.** Assumptions A1-A2 require bounded query/key matrices and bounded cumulative value projections. Whether these hold throughout training of real transformers (especially with learning rate warmup, gradient clipping, etc.) is not verified.

---

## Conclusions

### Contributions

1. **Graph-theoretic framework for position bias.** Developed a rigorous mathematical framework that models attention masks as directed graphs and tracks cumulative context probability P^(t)(z_i = j) across layers, unifying several empirical observations about position bias under a single theoretical lens (Table 1, Section 4).

2. **Causal masking creates inherent primacy bias.** Proved that multi-layer causal attention exponentially concentrates context probability toward the first token as depth increases, regardless of input semantics (Theorem 4.1). This is a structural consequence of the graph topology and the non-negativity of softmax.

3. **Attention sinks explained via center nodes.** Connected the empirically observed attention sink phenomenon to the graph-theoretic property of center nodes: tokens that are reachable by all other tokens accumulate disproportionate influence across layers (Theorems 4.1-4.3, Appendix K.4).

4. **Characterization of the decay mask / causal mask trade-off.** Showed that the decay mask (ALiBi) produces exponential within-layer decay (Lemma 4.4) but non-monotonic cumulative behavior across layers, with critical point x* = t/(e^m - 1) determined by depth t and decay strength m (Theorem 4.5).

5. **Characterization of RoPE's weaker decay.** Showed that RoPE induces Gaussian-like decay proportional to (i-j)^2 * theta_1^2 per layer (Lemma 4.6), substantially weaker than the decay mask's linear exponential, explaining why RoPE-based models still exhibit strong early-token bias. The multi-layer behavior (Theorem 4.7) shows the same non-monotonic trade-off.

6. **Causal mask does not simulate PE.** Provided empirical evidence contradicting the hypothesis of Kazemnejad et al. (2023) that the causal mask simulates PE. The causal mask captures positional bias only when it aligns with the beginning of the sequence, not at arbitrary positions (Section 5.2, Figure 3).

7. **Data distribution shapes the lost-in-the-middle phenomenon.** Demonstrated that the U-shaped performance curve requires training data biased toward both the beginning and end of sequences, establishing that the phenomenon involves an interaction between architectural bias and data distribution (Section 5.2, Appendix K.3).

### Implications

1. **Depth-representation power trade-off.** Deeper attention models improve representational power but simultaneously amplify positional bias, suggesting a fundamental tension in architectural design. [Inference: this tension may constrain how deep pure attention architectures can be made without explicit bias mitigation.]

2. **Design guidelines for attention masks.** The framework suggests that mask topology (specifically, center node structure) determines which positions will attract disproportionate attention. This could guide design of masks with more uniform positional influence. [Speculative: not tested with specific mask designs.]

3. **Training data curation as bias mitigation.** Since the lost-in-the-middle pattern depends on training data distribution, position-aware data curation could potentially mitigate the phenomenon. [Speculative: the paper demonstrates this only in a synthetic setting.]

---

## Key Claims

1. **Causal mask converges context to the first token.** Under assumptions A1-A2, cumulative context probability P^(t)(z_i = 1 | X^(0)) -> 1 as t -> infinity for every token i, with exponential convergence rate (Theorem 4.1, Section 4.1). Status: **supported**.

2. **Attention sinks arise from center node structure.** The disproportionate attention at initial tokens is explained by their role as center nodes in the attention mask graph: token 1 under causal/sliding-window masks, all K prefix tokens under prefix masks. Quantitative measurements using the metric of Gu et al. (2025) over 10,000 sequences confirm this (Theorems 4.1-4.3, Appendix K.4, Figures 10-12). Status: **supported**.

3. **Decay mask and causal mask produce non-monotonic cumulative behavior.** The cumulative probability P^(t)_decay = Theta(binom(t+i-j, i-j) * e^{-(i-j)m}), with critical point x* = t/(e^m - 1). Increasing decay strength m shifts attention to nearby tokens; increasing depth t shifts it to initial tokens (Theorem 4.5, Section 4.2). Status: **supported**.

4. **RoPE's decay is substantially weaker than the decay mask's.** RoPE induces Gaussian-like decay proportional to e^{-c(i-j)^2 theta_1^2} with theta_1 ~ 1/10000, while the decay mask produces exponential decay proportional to e^{-(i-j)m}. At depth 2, the first vs. middle gap is +0.002 for RoPE vs. -0.055 for the decay mask (Lemma 4.4 vs. 4.6, Figure 2). Status: **supported**.

5. **The causal mask does not simulate PE.** When training data is biased toward both first and last positions, the causal mask without PE captures bias only at the first position (first vs. middle: +0.276) but not the last (middle vs. last: -0.006), while sin PE and RoPE capture biases at both ends regardless of mask. If the causal mask simulated PE, it should capture bias at any position (Section 5.2, Figure 3). Status: **supported**.

6. **The lost-in-the-middle phenomenon requires specific data bias.** The U-shaped pattern appears only when training data is biased toward both the first and last positions. It does not appear under no bias, first-only bias, middle-only bias, or last-only bias conditions (Section 5.2, Appendix K.3, Figures 2, 3, 6-8). Status: **supported**.

7. **Deeper attention amplifies bias toward earlier tokens.** Without residual connections, increasing depth from 2 to 6 consistently increases the first vs. middle gap for all PE types: No PE (+0.059 -> +0.091), Decay Mask (-0.055 -> +0.020), RoPE (+0.002 -> +0.026). With residual connections, the relationship becomes non-monotonic (Figure 2, Figure 4, Figure 5, Section 5.1). Status: **supported**.

---

## Open Questions

1. **Role of residual connections in position bias.** Residual connections make the depth-bias relationship non-monotonic in ways not captured by the theory. Extending the framework to account for residual connections, value projections, and MLPs is identified as an important direction (Section 6, Section 5.1). Not yet addressed.

2. **Connection to natural language data distributions.** The authors ask whether positional bias in natural language sequences shapes the lost-in-the-middle phenomenon similarly to the synthetic setting (Appendix K.3). This connects to the primacy-recency effect in human cognition (Glanzer & Cunitz, 1966). Not yet addressed.

3. **Extension to multi-head attention.** The analysis considers only single-head attention. Different heads may develop different positional specializations, as documented in Clark et al. (2019) and Voita et al. (2019). Not yet addressed.

4. **Influence of embedding geometry.** The fixed-vocabulary experiments (Appendix L) show that anisotropic embeddings significantly affect task difficulty and bias patterns compared to the Gaussian mixture setting. The role of embedding geometry in position bias emergence is left open. Not yet addressed.

---

## Core References and Why They Are Referenced

### Attention Mechanism Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational transformer architecture. The paper analyzes position bias as an emergent property of the multi-layer attention mechanism introduced here.
- **Kim et al. (2017)** -- *Structured Attention Networks.* Provides the contextualization formulation (Equation 4) expressing multi-layer attention as a probabilistic context selection process P^(t)(z_i = j).
- **Bahdanau et al. (2015)** -- *Neural Machine Translation by Jointly Learning to Align and Translate.* Originated the concept of contextualization through attention that predates transformers.

### Attention Flow and Graph-Theoretic Analysis

- **Abnar & Zuidema (2020)** -- *Quantifying Attention Flow in Transformers.* Introduces the attention rollout metric that coincides with P^(t)(z_i = j) analyzed here. This paper develops independent theoretical motivation: attention rollout is an empirical visualization tool, while this paper treats the same quantity as a theoretical object analyzed across arbitrary inputs.
- **Barbero et al. (2024a)** -- *Transformers Need Glasses! Information Oversquashing in Language Tasks.* Analyzes attention from a graph perspective, studying information oversquashing. This paper builds on the graph-theoretic approach but focuses on positional bias rather than information bottlenecks.
- **Wu et al. (2023)** -- *Demystifying Oversmoothing in Attention-Based Graph Neural Networks.* Prior work by the same group analyzing attention masks' role in mitigating rank collapse. The graph-theoretic framework developed here extends this line of work.
- **Wu et al. (2024)** -- *On the Role of Attention Masks and LayerNorm in Transformers.* Provides the boundedness result (assumption A2) used in this paper and prior analysis of attention mask effects.

### Position Bias Empirical Evidence

- **Liu et al. (2024)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Documents the U-shaped "lost-in-the-middle" phenomenon, which this paper reproduces in controlled experiments and partially explains through the interplay of causal masking, PE-induced decay, and training data distribution.
- **Xiao et al. (2024)** -- *Efficient Streaming Language Models with Attention Sinks.* Identifies and names the attention sink phenomenon. This paper provides a theoretical explanation: attention sinks arise because initial tokens are center nodes whose influence accumulates across layers.
- **Gu et al. (2025)** -- *When Attention Sink Emerges in Language Models: An Empirical View.* Empirically demonstrates attention sinks on the first token under causal/sliding-window masks and on all prefix tokens under prefix masks. Theorems 4.1-4.3 and Appendix K.4 provide the theoretical counterpart.
- **Wang et al. (2024)** -- *Eliminating Position Bias of Language Models: A Mechanistic Approach.* Empirically observes that both causal masking and RoPE introduce position dependencies. Motivates the theoretical analysis in this paper.

### Positional Encodings

- **Su et al. (2023)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the dominant PE scheme whose decay effects are characterized in Lemma 4.6 and Theorem 4.7.
- **Press et al. (2022)** -- *ALiBi: Train Short, Test Long.* Introduces the decay mask formulation analyzed in Lemma 4.4 and Theorem 4.5.
- **Barbero et al. (2024b)** -- *Round and Round We Go! What Makes Rotary Positional Encodings Useful?* Shows that LLMs predominantly use slowly-rotating RoPE dimensions, motivating the d = 2 analysis and assumption underlying Lemma 4.6.
- **Kazemnejad et al. (2023)** -- *The Impact of Positional Encoding on Length Generalization in Transformers.* Hypothesizes that the causal mask simulates PE. Section 5.2 presents experiments contradicting this hypothesis.

### Attention Mask Architectures

- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Introduces the sliding-window attention mask analyzed in Theorem 4.2.
- **Lewis et al. (2020)** -- *BART.* Representative of models using the prefix mask analyzed in Theorem 4.3.
- **Raffel et al. (2020)** -- *T5.* Another representative encoder-decoder model using the prefix mask.

### Experimental Framework

- **Reddy (2024)** -- *The Mechanistic Basis of Data Dependence and Abrupt Learning in an In-Context Classification Task.* Provides the synthetic data-generating process and simplified self-attention network framework used for all experiments.
