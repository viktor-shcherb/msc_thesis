# On the Emergence of Position Bias in Transformers

**Authors:** Xinyi Wu, Yifei Wang, Stefanie Jegelka, Ali Jadbabaie (MIT IDSS & LIDS, MIT CSAIL, TU Munich)
**Date:** July 2025, ICML 2025 (arXiv:2502.01951)

---

## Core Research Problem

Transformer-based models exhibit systematic **position bias** -- a tendency to focus on certain regions of the input regardless of semantic content. This manifests in several well-documented phenomena: the "lost-in-the-middle" problem where retrieval accuracy degrades for information in the middle of the context (Liu et al., 2024); sensitivity of in-context learning to example ordering (Lu et al., 2022; Min et al., 2022); and attention sinks where initial tokens attract disproportionately high attention (Gu et al., 2025; Xiao et al., 2024). While mitigation strategies such as novel positional encodings (Kazemnejad et al., 2023), alternative masking techniques (Fang et al., 2025; Wang et al., 2024), and bootstrapping (Hou et al., 2024) have been proposed, they remain task-specific and empirically driven. Prior theoretical work has analyzed attention masks for function approximation (Yun et al., 2020b), rank collapse mitigation (Wu et al., 2023; 2024), and the effect of PEs on length generalization (Kazemnejad et al., 2023), but fundamental questions remain about the mechanisms through which attention masks and positional encodings jointly produce systematic positional biases. The core challenge is: **how do attention masks and positional encodings shape position bias in multi-layer transformers?**

---

## Problem Solutions

The paper develops a **graph-theoretic framework** for analyzing position bias in multi-layer attention, modeling attention masks as directed graphs and tracking cumulative context distributions across layers. The framework yields two key insights:

1. **Causal masking inherently biases attention toward earlier positions.** In deeper layers, tokens attend to increasingly contextualized representations of earlier tokens, causing cumulative context probability to converge exponentially toward the first token -- regardless of semantic content (Theorem 4.1). Analogous results hold for sliding-window and prefix masks (Theorems 4.2, 4.3).

2. **Relative positional encodings introduce a competing decay effect.** The decay mask and RoPE both impose distance-based decay within individual attention layers, but their aggregate effect across multiple layers coupled with the causal mask leads to a **non-monotonic trade-off** between long-term decay and cumulative early-token importance (Theorems 4.5, 4.7).

---

## Approach Details

### Method

The analysis considers single-head masked self-attention networks (SANs) with the layerwise update:

> X^(t+1) = A^(t) X^(t) W_V^(t)

where A^(t) = softmax_G(X^(t) W_Q^(t) (X^(t) W_K^(t))^T / sqrt(d_QK)) and G is the directed graph defining the attention mask. The framework analyzes the **cumulative context probability**:

> P^(t)(z_i = j | X^(0)) = (A^(t) ... A^(0))_{ij}

which quantifies how much of token i's representation at depth t originates from input token j. This quantity coincides with the attention rollout metric of Abnar & Zuidema (2020), but the paper treats it as a theoretical object analyzed across arbitrary inputs to reveal inductive biases, rather than as an empirical visualization tool.

Attention masks are formalized as directed graphs G where edge (j, i) means token i attends to token j. A **center node** is a node from which every node in G is reachable. The key property driving the results is that softmax cannot fundamentally disconnect any edge in G (all attention weights remain strictly positive), so center nodes accumulate influence across layers.

### Key Technical Components

**Assumptions:**
- **A1:** Bounded query/key weight matrices: max_t {||W_Q^(t)||_2, ||W_K^(t)||_2} <= C.
- **A2:** Bounded cumulative value projection: the sequence {||prod_{t=0}^k W_V^(t)||_2} is bounded, ensuring bounded token trajectories.

**Three attention mask types analyzed:**
- **Causal mask:** Token i attends to all tokens j <= i. Token 1 is the unique center node.
- **Sliding-window mask:** Token i attends to tokens in [max(1, i-w+1), i] for window width w. Token 1 remains the center node but reachability requires ceil((N-1)/(w-1)) hops.
- **Prefix mask:** The first K tokens are prefix tokens visible to all subsequent tokens. All K prefix tokens are center nodes.

**Two relative positional encoding types analyzed:**
- **Decay mask (ALiBi-style):** D_ij = -(i-j)m for j <= i, adding an explicit distance-based bias to attention logits with strength m.
- **RoPE:** Applies rotation R^d_{Theta,i} to query/key embeddings proportional to position index, with base angles Theta = {theta_1, ..., theta_{d/2}}.

### Theoretical Analysis

**Causal mask without PE (Theorem 4.1):** For causal attention under A1-A2, for every token i:

> lim_{t->inf} P^(t)(z_i = 1 | X^(0)) = 1

with exponential convergence: P^(t)(z_i = j | X^(0)) <= C(1 - (j-1)epsilon)^t for all 1 < j <= i. Context converges to the first token regardless of input content.

**Sliding-window mask (Theorem 4.2):** Same convergence to token 1, but at a slower rate governed by ceil((N-1)/(w-1)): P^(t)(z_i = j | X^(0)) <= C(1 - (j-1)epsilon^{ceil((N-1)/(w-1))})^{t/(2*ceil((N-1)/(w-1)))}. Smaller window w mitigates early-token bias but does not eliminate it.

**Prefix mask (Theorem 4.3):** Context converges to the K prefix tokens collectively, with each prefix token retaining non-trivial influence: lim inf_{t->inf} P^(t)(z_i = k | X^(0)) >= kappa > 0 for all k in [K]. Non-prefix tokens decay exponentially.

**Decay mask -- single layer (Lemma 4.4):** Exponential decay per layer: C_min * e^{-(i-j)m} <= (A^(t)_decay)_ij <= C_max * e^{-(i-j)m}.

**Decay mask -- multi-layer (Theorem 4.5):** The cumulative probability becomes:

> P^(t)_decay(z_i = j | X^(0)) = Theta(binom(t+i-j, i-j) * e^{-(i-j)m})

The function L(x) = log(binom(t+x, x) * e^{-xm}) is **non-monotonic** with critical point x* = t/(e^m - 1). Increasing decay strength m decreases x* (more recency bias); increasing depth t increases x* (more primacy bias).

**RoPE -- single layer (Lemma 4.6):** For d = 2 with the slowest-rotating dimension theta_1, under the condition that original query-key angles |phi^(t)_{i,j}| <= delta * theta_1 and (delta + N - 1)theta_1 <= pi:

> C_min * e^{-c(i-j)^2 theta_1^2} <= (A^(t)_RoPE)_ij <= C_max * e^{-c'(i-j)^2 theta_1^2}

RoPE induces Gaussian-like decay in (i-j)^2, substantially weaker than the decay mask's linear exponential because theta_1 is typically ~1/10000 per token.

**RoPE -- multi-layer (Theorem 4.7):**

> P^(t)_RoPE(z_i = j | X^(0)) = Theta(binom(t+i-j, i-j) * e^{-c(i-j)^2 theta_1^2})

The critical point x* is an increasing function of depth t and a decreasing function of theta_1. Larger theta_1 amplifies decay (more focus on nearby tokens); deeper models shift x* further, increasing primacy bias.

**General d >= 2 (Appendix I):** Lemma I.1 and Theorem I.2 generalize the RoPE results to arbitrary even dimension d, with the decay term becoming e^{-c * sum_{l=1}^{d/2} (i-j)^2 alpha_l^2 theta_1^2} where theta_l = alpha_l * theta_1. The analysis leverages the empirical finding of Barbero et al. (2024b) that LLMs predominantly use slowly-rotating feature dimensions, making the effective d/2 small.

### Experimental Setup

The paper uses the synthetic data framework of Reddy (2024) for controlled experiments:

- **Task:** Information retrieval -- predict the label y_query of a target x_query given an alternating sequence x_1, y_1, ..., x_n, y_n, x_query.
- **Data:** Gaussian mixture model with K = 2048 classes, L = 32 labels, burstiness B = 4, n = 8 items, d = 64 dimensions, gamma = 0.75.
- **Position bias control:** x_query is either assigned to the class of a specific x_i (introducing position bias) or randomly assigned (no position bias in data).
- **Evaluation:** Novel-class test sequences with 10,000 sequences per condition. Position bias is measured as accuracy gap [a, b] - [b, a] between matched sequences where only the correct position differs.
- **Architecture:** Single-head attention-only network followed by a 3-layer MLP classifier with ReLU and softmax.
- **Conditions:** Depths 2, 4, 6 (without residual connections) and 2, 6, 10 (with residual connections). Three PE types: No PE, Decay Mask (m = -log(0.8) ~ 0.223), RoPE (theta_i = 10000^{-2(i-1)/d}).
- **Training:** AdamW optimizer, learning rate 10^{-3}, weight decay 10^{-6}, batch size 128, 100K iterations, Tesla V100 GPU.

### Key Results

**Effect of depth and relative PEs (no position bias in training data, no residual connections):**

| PE Type | Depth | First vs. Middle Gap | First vs. Last Gap | Middle vs. Last Gap |
|---|---|---|---|---|
| No PE | 2 | +0.059 | +0.077 | +0.018 |
| No PE | 6 | +0.091 | +0.106 | +0.011 |
| Decay Mask | 2 | -0.055 | -0.073 | -0.003 |
| Decay Mask | 6 | +0.020 | +0.014 | -0.010 |
| RoPE | 2 | +0.002 | -0.002 | -0.009 |
| RoPE | 6 | +0.026 | +0.044 | +0.017 |

Positive values indicate bias toward earlier positions.

- Deeper attention consistently amplifies bias toward earlier tokens regardless of PE type.
- The decay mask introduces substantially stronger recency bias than RoPE at shallow depth, consistent with theory.
- The middle vs. last gap is notably smaller than the first vs. middle/last gaps, consistent with Theorem 4.1 predicting that late-sequence tokens become less distinguishable as early-token dominance grows.

**Causal mask and positional information (with residual connections, data biased toward first and last positions):**

| PE / Mask | First vs. Middle | First vs. Last | Middle vs. Last |
|---|---|---|---|
| No PE / no mask | -0.002 | 0.000 | -0.001 |
| No PE / causal | +0.276 | +0.308 | -0.006 |
| sin PE / no mask | +0.293 | +0.013 | -0.264 |
| sin PE / causal | +0.316 | +0.078 | -0.238 |
| RoPE / no mask | +0.249 | -0.002 | -0.281 |
| RoPE / causal | +0.472 | +0.433 | -0.241 |

- The causal mask without PE captures positional bias only at the first position, not at the last. This contradicts the hypothesis of Kazemnejad et al. (2023) that the causal mask simulates PE; instead, the causal mask introduces a bias toward earlier positions via iterative attention, consistent with Theorem 4.1.
- With sin PE or RoPE, the model captures biases at both ends, producing a "lost-in-the-middle" U-shaped pattern.
- The "lost-in-the-middle" phenomenon only emerges when training data is biased toward both first and last positions; it does not appear when training data has no position bias or bias only at a single position.

**Attention sinks:** Despite the simplified setup, attention sinks emerge on center nodes as predicted by Theorems 4.1--4.3: on token 1 under causal masking, on token 1 under sliding-window masking (especially for larger window sizes), and on all K prefix tokens under prefix masking. These patterns match observations in real-world LLMs by Gu et al. (2025).

**Residual connections:** With residual connections, the relationship between depth and positional bias becomes non-monotonic and depends on the PE type and depth regime. This suggests residual connections modulate position bias accumulation in ways not captured by the pure attention analysis.

---

## Conclusions

1. **Causal masking creates an inherent primacy bias.** Multi-layer causal attention exponentially concentrates context probability toward the first token as depth increases, regardless of input semantics. This is a structural consequence of the graph topology of the causal mask and the non-negativity of softmax.

2. **Attention sinks arise from center node structure.** The disproportionate attention allocated to initial tokens is not an arbitrary artifact but a natural consequence of these tokens being center nodes in the attention graph -- reachable (directly or indirectly) by all other tokens.

3. **Relative PEs create a competing decay effect.** Both the decay mask and RoPE introduce distance-based decay within individual layers, partially counteracting the causal mask's primacy bias. However, across multiple layers the cumulative importance of early tokens creates a non-monotonic trade-off between local decay and global primacy.

4. **RoPE's decay is substantially weaker than the decay mask's.** RoPE induces Gaussian-like decay proportional to (i-j)^2 theta_1^2 with theta_1 ~ 1/10000, while the decay mask produces exponential decay proportional to (i-j)m. This explains why RoPE-based models still exhibit strong early-token bias.

5. **The causal mask does not simulate positional encodings.** Contrary to the hypothesis of Kazemnejad et al. (2023), the causal mask does not inherently implement PE but instead introduces a directional bias toward earlier positions via iterative attention. It captures positional bias only when that bias aligns with the beginning of the sequence.

6. **Training data distribution shapes the "lost-in-the-middle" phenomenon.** The U-shaped performance curve only emerges when training data contains positional bias toward both the beginning and end of sequences, suggesting that the phenomenon involves an interaction between architectural bias and data-dependent learning.

7. **Depth-representation power trade-off.** While deeper attention models improve representational power, they simultaneously amplify positional bias toward initial tokens, underscoring the need to balance depth and positional bias in architectural design.

---

## Core References and Why They Are Referenced

### Attention Mechanism Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational transformer architecture. The paper analyzes position bias as an emergent property of the multi-layer attention mechanism introduced here.
- **Kim et al. (2017)** -- *Structured Attention Networks.* Provides the contextualization formulation (Equation 4) used to express multi-layer attention as a probabilistic context selection process.
- **Abnar & Zuidema (2020)** -- *Quantifying Attention Flow in Transformers.* Introduces the attention rollout metric that coincides with the cumulative context probability P^(t) analyzed in this paper, though the motivation differs: attention rollout is an empirical visualization tool, whereas this paper treats it as a theoretical object.

### Position Bias Empirical Evidence

- **Liu et al. (2024)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Documents the U-shaped "lost-in-the-middle" phenomenon, which this paper reproduces in controlled experiments and partially explains through the interplay of causal masking and PE-induced decay.
- **Xiao et al. (2024)** -- *Efficient Streaming Language Models with Attention Sinks.* Identifies and names the attention sink phenomenon. This paper provides a theoretical explanation: attention sinks arise because initial tokens are center nodes in the attention graph whose influence accumulates across layers.
- **Gu et al. (2025)** -- *When Attention Sink Emerges in Language Models: An Empirical View.* Empirically demonstrates that attention sinks appear on the first token under causal/sliding-window masks and on all prefix tokens under prefix masks. Theorems 4.1--4.3 provide the theoretical counterpart to these observations.

### Positional Encodings

- **Su et al. (2023)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the dominant PE scheme whose decay effects are characterized in Lemma 4.6 and Theorem 4.7.
- **Press et al. (2022)** -- *ALiBi: Train Short, Test Long.* Introduces the decay mask formulation (Equation 2) analyzed in Lemma 4.4 and Theorem 4.5.
- **Barbero et al. (2024b)** -- *Round and Round We Go! What Makes Rotary Positional Encodings Useful?* Shows that LLMs predominantly use slowly-rotating RoPE dimensions, motivating the d = 2 analysis and the assumption underlying Lemma 4.6.

### Causal Mask and Positional Information

- **Kazemnejad et al. (2023)** -- *The Impact of Positional Encoding on Length Generalization in Transformers.* Hypothesizes that the causal mask simulates PE through specific weight matrices. Section 5.2 presents experiments contradicting this hypothesis, showing the causal mask introduces a directional bias rather than simulating PE.
- **Wang et al. (2024)** -- *Eliminating Position Bias of Language Models: A Mechanistic Approach.* Empirically observes that both causal masking and RoPE introduce position dependencies in LLMs, motivating the theoretical analysis in this paper.

### Graph-Theoretic Analysis of Attention

- **Barbero et al. (2024a)** -- *Transformers Need Glasses! Information Oversquashing in Language Tasks.* Analyzes attention from a graph perspective, studying information oversquashing. This paper builds on the graph-theoretic approach but focuses on positional bias rather than information bottlenecks.
- **Wu et al. (2023)** -- *Demystifying Oversmoothing in Attention-Based Graph Neural Networks.* Prior work by the same group analyzing attention masks' role in mitigating rank collapse. The graph-theoretic framework developed here extends this line of work to study positional bias.
- **Wu et al. (2024)** -- *On the Role of Attention Masks and LayerNorm in Transformers.* Analyzes the role of attention masks and LayerNorm, providing the boundedness result (assumption A2) used in this paper.

### Experimental Framework

- **Reddy (2024)** -- *The Mechanistic Basis of Data Dependence and Abrupt Learning in an In-Context Classification Task.* Provides the synthetic data-generating process and simplified self-attention network framework used for all experiments.

### Attention Mask Architectures

- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Introduces the sliding-window attention mask analyzed in Theorem 4.2.
- **Lewis et al. (2020)** -- *BART: Denoising Sequence-to-Sequence Pre-training.* Representative of models using the prefix mask analyzed in Theorem 4.3.
- **Raffel et al. (2020)** -- *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5).* Another representative encoder-decoder model using the prefix mask.

#### Cross-References in Available Papers

- **Lost in the Middle (`2024-02-lost-in-the-middle`):** Liu et al. (2024) is cited extensively as the primary empirical documentation of the U-shaped positional bias phenomenon. This paper provides a partial theoretical explanation: the primacy component of the U-shape arises from the causal mask's convergence toward early tokens (Theorem 4.1), while the recency component is driven by the distance-based decay of relative PEs (Lemma 4.4, 4.6). Section 5.2 further shows that the full "lost-in-the-middle" U-shape only emerges when training data contains positional bias at both ends.
- **Attention Sinks (`2024-05-attention-sinks-streaming`):** Xiao et al. (2024) is cited as identifying the attention sink phenomenon. This paper provides its theoretical explanation: attention sinks are a consequence of center nodes in the mask graph accumulating influence across layers (Theorems 4.1--4.3). The paper also validates that replacing softmax with ReLU (which can disconnect graph edges) mitigates attention sinks, as observed by Gu et al. (2025) and consistent with Xiao et al.'s analysis linking sinks to SoftMax normalization.
