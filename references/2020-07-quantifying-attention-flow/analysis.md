---
title: "Quantifying Attention Flow in Transformers"
authors: "Abnar, Zuidema"
year: 2020
venue: "ACL 2020"
paper_type: conference-paper
categories: ["attention-analysis", "mechanistic-interpretability"]
scope: ["encoder-only Transformers", "attention interpretation", "token attribution"]
benchmarks_used: ["sst-2"]
models_introduced: []
models_evaluated: ["bert-base", "distilbert"]
key_claims:
  - id: C1
    claim: "Raw attention weights become unreliable indicators of input token importance in higher Transformer layers, with correlation to blank-out scores dropping from 0.69 at layer 1 to -0.11 at layer 3 in a 6-layer model"
    evidence: "Table 1, Section 2"
    status: supported
    scope: "6-layer custom Transformer encoder, verb number prediction, 2000 test samples"
    magnitude: "Spearman correlation drops from 0.69 (L1) to -0.11 (L3)"
  - id: C2
    claim: "Attention rollout improves token attribution by recursively multiplying residual-augmented attention matrices, reaching 0.71 correlation with blank-out at the final layer compared to 0.29 for raw attention"
    evidence: "Table 1, Table 2, Section 3-4"
    status: supported
    scope: "6-layer custom Transformer encoder, verb number prediction, 2000 test samples"
    magnitude: "0.71 vs 0.29 Spearman correlation with blank-out at final layer"
  - id: C3
    claim: "Attention flow using maximum flow algorithms provides the most reliable token attribution, reaching 0.70 correlation with blank-out by layer 3 and consistently outperforming rollout on input gradient correlation"
    evidence: "Tables 1-3, Figure 4, Section 4"
    status: supported
    scope: "6-layer custom Transformer encoder and DistilBERT on SST-2, verb number prediction and sentiment analysis"
    magnitude: "0.70 blank-out correlation at L3 (vs 0.51 rollout); 0.61 gradient correlation from L3 (vs 0.54 rollout at L6)"
  - id: C4
    claim: "Attention rollout and attention flow provide complementary views: rollout produces more focused patterns while flow produces more distributed patterns amortized across important tokens"
    evidence: "Figures 1-3, Section 4"
    status: supported
  - id: C5
    claim: "Both methods are task-agnostic and architecture-agnostic, requiring only attention weights as input and applicable post hoc to any self-attention architecture"
    evidence: "Sections 2, 4, 5"
    status: supported
    scope: "Demonstrated on three models (custom Transformer, DistilBERT, BERT) and three tasks (verb prediction, sentiment analysis, pronoun resolution)"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Proposes methods to properly interpret multi-layer attention and residual connections in the Transformer architecture"
  - target: 2019-08-bert-attention-analysis
    type: extends
    detail: "Improves upon raw attention analysis by accounting for cross-layer information mixing that single-layer attention visualizations ignore"
  - target: 2021-12-transformer-circuits-framework
    type: complementary
    detail: "The circuits framework provides exact decomposition of attention contributions for the linear component, while this paper approximates full information flow using only attention weights"
  - target: 2025-07-position-bias-transformers
    type: extended-by
    detail: "Treats the attention rollout quantity P^(t)(z_i = j) as a theoretical object analyzed across arbitrary inputs to reveal inductive biases of attention masks and positional encodings, rather than as an empirical visualization tool"
  - target: 2019-06-bert-pretraining-language-understanding
    type: evaluates
    detail: "Uses BERT-base as the primary model for evaluating attention rollout and attention flow methods"
  - target: 2024-12-transformers-need-glasses-over-squashing
    type: extended-by
    detail: "Barbero et al. extend information flow analysis to decoder-only Transformers, showing how the causal mask creates asymmetric information propagation with over-squashing at the final token"
open_questions:
  - question: "How should attention rollout and flow be adapted for Transformer decoders with causal masking, where natural bias toward initial tokens requires normalization by the receptive field?"
    addressed_by: null
  - question: "Can effective attention weights (Brunner et al., 2020) replace raw attention in the attention graph for more accurate flow estimation?"
    addressed_by: null
  - question: "Can gradient-based attribution methods be combined with attention weights to improve information flow approximation?"
    addressed_by: null
  - question: "How much information flow is captured by attention weights alone vs. the value vectors and feed-forward transformations that are currently ignored?"
    addressed_by: null
---
# Quantifying Attention Flow in Transformers

**Authors:** Samira Abnar, Willem Zuidema (ILLC, University of Amsterdam)
**Date:** July 2020, ACL 2020, DOI:10.18653/v1/2020.acl-main.385 (arXiv:2005.00928)

---

## Core Research Problem

Self-attention in Transformers combines information from attended embeddings into the representation of the focal embedding at the next layer. Across layers, information originating from different tokens gets increasingly mixed: embeddings in higher layers are heavily contextualized and may all carry similar information. As a result, raw attention weights at higher layers become nearly uniform and lose their interpretability as indicators of which input tokens are important for a given prediction.

Prior work on attention visualization (Vaswani et al., 2017; Vig, 2019; Clark et al., 2019) reported raw attention weights without accounting for the fact that each layer's attention operates over already-mixed representations, not the original input tokens. Serrano and Smith (2019) showed that attention weights do not necessarily correspond to the relative importance of input tokens, and Brunner et al. (2020) identified the lack of "token identifiability" in higher-layer embeddings as the root cause. The broader debate about whether attention constitutes explanation (Jain and Wallace, 2019; Wiegreffe and Pinter, 2019; Pruthi et al., 2019) further motivated the need for methods that account for cross-layer information mixing.

The core distinction is between **embedding attention** (layer-local attention weights over contextualized representations) and **token attention** (effective attention from a hidden embedding back to the original input tokens). Raw attention provides the former but not the latter. **The core challenge is: how to compute token attention at any layer by accounting for the recursive mixing of information across all preceding layers and residual connections.**

---

## Problem Solutions

The paper proposes two post hoc methods for computing token attention by recursively incorporating attention weights from all preceding layers. Both model information flow as a Directed Acyclic Graph (DAG) where nodes are input tokens and hidden embeddings, edges are attention connections, and edge weights are attention weights.

1. **Attention rollout** assumes token identities are linearly combined through layers according to attention weights. It computes token attention by recursively multiplying attention matrices from the current layer back to the input, accounting for residual connections via an identity matrix addition.
2. **Attention flow** treats the attention graph as a flow network where edge capacities are attention weights. It uses a maximum flow algorithm to compute the maximum possible flow from each hidden embedding (source) to each input token (sink).
3. **Residual connection integration.** Both methods augment the attention graph with identity connections to represent the residual connections that tie corresponding positions across layers.

---

## Approach Details

### Method

Both methods take as input the raw attention weight matrices from all layers and produce, for each layer, a matrix of token attentions back to the input tokens.

**Residual connection handling.** In a Transformer block with residual connections, the output of layer l+1 is:

> V_{l+1} = V_l + W_att V_l = (W_att + I) V_l

where W_att is the attention matrix and I is the identity matrix. To account for residual connections, the raw attention matrix is augmented with an identity matrix and re-normalized:

> A = 0.5 W_att + 0.5 I

This A replaces the raw attention in both methods. The 0.5 weighting reflects equal contribution from the attention path and the residual (skip) path.

**Multi-head handling.** The paper averages attention weights across all heads at each layer before computing rollout or flow. Appendix A.1 describes how to analyze individual heads: for head k at layer i, compute rollout as:

> A~(i, k) = A(i, k) A~(i)

where A~(i) is the attention rollout computed for layer i with the single-head (averaged) assumption. This avoids the incorrect assumption that there is no mixing of information between heads (mixing occurs in the position-wise feed-forward network).

**Attention rollout.** Given a Transformer with L layers, attention rollout recursively multiplies the residual-augmented attention matrices from all layers below:

> A~(l_i) = A(l_i) A~(l_{i-1})  if i > j
> A~(l_i) = A(l_i)              if i = j

where A~ is the rollout attention, A is the residual-augmented raw attention, and multiplication is matrix multiplication. To compute input attention, set j = 0. The intuition: the weight of each path from a hidden embedding to an input token is the product of all edge weights along that path, and the total token attention is the sum over all paths (computed implicitly by the matrix multiplication).

**Attention flow.** The attention graph is treated as a flow network: a directed graph G = (V, E) with edge capacities C = {c_uv} set to the attention weights. Given source node s (a hidden embedding) and target node t (an input token), the maximum flow algorithm (Cormen et al., 2009) finds the flow f: E -> R that maximizes the total flow from s to t, subject to: (a) **capacity constraint:** |f_uv| <= c_uv for all edges; (b) **flow conservation:** for all nodes except s and t, inflow equals outflow. The key difference from rollout: the weight of a single path is the **minimum** edge weight along that path (the bottleneck), and overlapping paths cannot be simply summed due to shared edges, requiring the maximum flow algorithm.

### Key Technical Components

**Computational complexity.** Attention rollout runs in O(d * n^2) and attention flow in O(d^2 * n^4), where d is the depth (number of layers) and n is the number of tokens. Both are polynomial time.

**Complementary views.** Attention rollout treats attention weights as **proportion factors** and propagates token identities exactly according to these proportions. This produces more focused attention patterns, useful for identifying a single dominant input token. Attention flow treats attention weights as **capacities** and uses as much capacity as possible, computing the maximum possibility of token identity propagation. This produces more distributed patterns where weight is amortized among the set of most-attended tokens, indicating a set of important tokens without sharp distinctions.

**Blank-out attribution.** As a ground-truth proxy for input token importance, blank-out replaces each token one-by-one with UNK and measures the change in predicted probability of the correct class. Spearman's rank correlation between attention-based importance and blank-out scores serves as the primary evaluation metric.

### Experimental Setup

**Primary model (verb number prediction).** A Transformer encoder with GPT-2 Transformer blocks (Radford et al., 2019; Wolf et al., 2019), without causal masking. 6 layers, 8 heads, hidden/embedding size 128. A [CLS] token is added and its final-layer embedding serves as classifier input. Trained on the subject-verb agreement dataset (Linzen et al., 2016), achieving 0.96 accuracy on the task (predicting singular vs. plural verb given a sentence up to the verb position). This task is chosen because it offers a clear hypothesis about which input tokens matter: the subject head noun, not intervening attractors.

**Secondary model (sentiment analysis).** DistilBERT (Sanh et al., 2019) fine-tuned on SST-2 (Socher et al., 2013) from the GLUE benchmark (Wang et al., 2018).

**Tertiary model (pronoun resolution).** Pre-trained BERT (Devlin et al., 2019), used for qualitative analysis of pronoun resolution via masked language modeling.

**Evaluation metrics:**
- Spearman's rank correlation between attention-based importance scores and blank-out scores (2000 test samples for verb prediction).
- Spearman's rank correlation between attention-based importance scores and input gradients (2000 test samples for verb prediction; 100 test samples for DistilBERT).
- Qualitative visualization of attention maps for pronoun resolution.

### Key Results

**Correlation with blank-out scores (verb number prediction, 2000 test samples, Table 1):**

| Method | L1 | L2 | L3 | L4 | L5 | L6 |
|---|---|---|---|---|---|---|
| Raw | 0.69+-0.27 | 0.10+-0.43 | -0.11+-0.49 | -0.09+-0.52 | 0.20+-0.45 | 0.29+-0.39 |
| Rollout | 0.32+-0.26 | 0.38+-0.27 | 0.51+-0.26 | 0.62+-0.26 | 0.70+-0.25 | **0.71+-0.24** |
| Flow | 0.32+-0.26 | 0.44+-0.29 | **0.70+-0.25** | **0.70+-0.22** | **0.71+-0.22** | 0.70+-0.22 |

- Raw attention has high correlation only at layer 1 (0.69) and degrades sharply to negative correlations (-0.11 at L3, -0.09 at L4) before recovering slightly at L6 (0.29).
- Both rollout and flow improve monotonically with depth, reaching 0.70--0.71 at the final layer.
- Attention flow converges faster (0.70 at L3) than rollout (0.70 at L5).
- At layer 1, rollout and flow are identical (0.32) and differ from raw attention (0.69) only due to the residual connection augmentation.

**Correlation with input gradients (verb number prediction, 2000 test samples, Table 2):**

| Method | L1 | L2 | L3 | L4 | L5 | L6 |
|---|---|---|---|---|---|---|
| Raw | 0.53+-0.33 | 0.16+-0.38 | -0.06+-0.42 | 0.00+-0.47 | 0.24+-0.40 | 0.46+-0.35 |
| Rollout | 0.22+-0.31 | 0.27+-0.32 | 0.39+-0.32 | 0.47+-0.32 | 0.53+-0.32 | 0.54+-0.31 |
| Flow | 0.22+-0.31 | 0.31+-0.34 | **0.54+-0.32** | **0.61+-0.28** | **0.60+-0.28** | **0.61+-0.28** |

- The same pattern holds: raw attention degrades in middle layers while rollout and flow improve steadily.
- Attention flow reaches a plateau of ~0.61 from L3 onward; rollout plateaus at ~0.54 from L5.
- Attention flow consistently outperforms rollout on input gradient correlation.

**DistilBERT on SST-2 (correlation with input gradients, 100 test samples, Table 3):**

| Method | L1 | L3 | L5 | L6 |
|---|---|---|---|---|
| Raw | 0.12+-0.21 | 0.09+-0.21 | 0.08+-0.20 | 0.09+-0.21 |
| Rollout | 0.11+-0.19 | 0.12+-0.21 | 0.13+-0.21 | 0.13+-0.20 |
| Flow | 0.11+-0.19 | 0.11+-0.21 | 0.12+-0.22 | **0.14+-0.21** |

- All three methods yield low correlations on this model/task, but rollout and flow still slightly outperform raw attention, particularly at deeper layers.

**Qualitative analysis -- pronoun resolution with pre-trained BERT (Figure 4).** The paper examines attention weights from a [MASK] token to candidate pronoun referents. For "The author talked to Sara about [MASK] book," raw attention at the final layer is inconsistent with the model's prediction, while both rollout and flow correctly assign higher weight to the predicted referent. For "Mary convinced John of [MASK] love," only attention flow is consistent with the model's prediction across all layers.

### Attention Rollout vs. Attention Flow

The main qualitative difference between the two methods (Section 4):

- **Attention rollout** produces more focused patterns because it strictly propagates proportions of token identities. This can be useful for identifying the single most important token but may be overly strict given the many simplifying assumptions.
- **Attention flow** produces more distributed patterns because it treats attention as capacities and computes maximum possible flow. This amortizes weight among the top tokens, making it better at identifying a set of important tokens. The relaxation of attention flow appears to be a useful property, as evidenced by its consistently higher correlations with both blank-out and gradient-based importance scores.

---

## Limitations and Failure Modes

- **Encoder-only analysis.** All experiments use Transformer encoders without causal masking. In Transformer decoders, future tokens are masked, creating a natural bias toward initial tokens. Both rollout and flow will inherit this bias. The authors note that normalization based on the receptive field of attention is needed to apply these methods to decoders, but do not evaluate this (Section 5).
- **Attention-only approximation.** Both methods approximate information flow using only attention weights, ignoring the value vectors and feed-forward transformations that also affect information propagation. This is an acknowledged simplifying assumption.
- **Multi-head averaging.** Averaging attention across heads is a simplification. The individual-head analysis (Appendix A.1) is described but not extensively evaluated.
- **Low correlations on DistilBERT/SST-2.** On DistilBERT fine-tuned for sentiment analysis, all three methods yield very low correlations with input gradients (0.09--0.14, Table 3), suggesting that for some model/task combinations, attention weights (even with rollout or flow correction) provide limited insight into token importance.
- **Feed-forward network ignored.** The residual connection augmentation accounts for the self-attention residual path but does not model information flow through the position-wise feed-forward network, which also transforms and mixes information.

#### Scope and Comparability

- **What was not tested:** Decoder-only (autoregressive) Transformers, models larger than BERT-base, tasks beyond verb prediction / sentiment analysis / pronoun resolution. No evaluation on generation tasks or long-context settings.
- **Primary model is non-standard.** The main quantitative results (Tables 1--2) use a custom 6-layer Transformer encoder with GPT-2 blocks (128 hidden size), not a standard pre-trained model. Results may not directly transfer to deeper or larger architectures.
- **Small evaluation set for DistilBERT.** Table 3 uses only 100 test samples (vs. 2000 for the primary model), limiting statistical power for the SST-2 results.
- **No statistical significance testing.** Results report mean and standard deviation of Spearman correlations across samples but do not test whether differences between methods are statistically significant.
- **Comparability notes.** Other attention analysis papers (Clark et al., 2019; Kovaleva et al., 2019) use standard pre-trained BERT on NLU benchmarks, making direct comparison with this paper's custom model results non-trivial.

---

## Conclusions

### Contributions

1. **Attention rollout method.** Introduced a recursive matrix multiplication procedure that computes token attention by propagating residual-augmented attention matrices across all layers, producing importance scores that improve monotonically with depth (0.71 correlation with blank-out at L6 vs. 0.29 for raw attention; Table 1).

2. **Attention flow method.** Introduced a maximum-flow-based computation that treats the attention graph as a flow network, yielding the highest correlations with both blank-out scores and input gradients across all evaluated layers and consistently outperforming attention rollout (Tables 1--3).

3. **Residual connection modeling.** Showed that augmenting the attention graph with identity connections (A = 0.5 W_att + 0.5 I) to represent residual connections is critical for accurate information flow modeling, as residual connections tie corresponding positions across layers (Section 3).

4. **Empirical demonstration that raw attention is unreliable.** Provided quantitative evidence that raw attention weights degrade sharply in higher layers (correlation with blank-out drops from 0.69 at L1 to -0.11 at L3), supporting prior qualitative observations (Serrano and Smith, 2019; Brunner et al., 2020) with a concrete failure mode (Table 1, Section 2).

5. **Complementary diagnostic tools.** Demonstrated that rollout and flow provide complementary views: rollout identifies the single most important token while flow identifies a set of important tokens (Figures 1--3, Section 4).

### Implications

1. **Raw attention visualizations at higher layers should be interpreted with caution** or replaced by rollout/flow-based visualizations. This applies broadly to any multi-layer self-attention architecture.

2. **The token identifiability problem limits all attention-based interpretability methods.** Even rollout and flow make simplifying assumptions; more accurate methods may require incorporating value vectors and feed-forward transformations. [Inference]

3. **Decoder models require adapted methods.** The causal masking in autoregressive models introduces systematic biases that rollout and flow will propagate. Methods for decoder interpretability need to normalize for receptive field differences. [Noted by authors but not evaluated]

---

## Key Claims

1. **Raw attention degrades in higher layers.** Raw attention of the [CLS] token correlates with blank-out importance at 0.69 at layer 1 but drops to -0.11 at layer 3 and recovers only to 0.29 at layer 6 in a 6-layer Transformer (Table 1, Section 2). Status: **supported**.

2. **Attention rollout improves monotonically with depth.** Rollout correlation with blank-out increases from 0.32 at L1 to 0.71 at L6, consistently outperforming raw attention from layer 2 onward (Table 1, Section 3--4). Status: **supported**.

3. **Attention flow provides the most reliable attribution.** Flow reaches 0.70 correlation with blank-out by layer 3 (vs. 0.51 for rollout) and achieves 0.61 correlation with input gradients from L3 onward (vs. 0.54 for rollout at L6) on the verb prediction task (Tables 1--2, Section 4). Status: **supported**.

4. **Rollout and flow provide complementary views.** Rollout is stricter and produces focused patterns; flow is more relaxed and amortizes weight among important tokens. In the BERT pronoun resolution experiment, rollout and flow agree on one example but only flow is consistent with the model's prediction on the other (Figure 4, Section 4). Status: **supported**.

5. **Both methods are task-agnostic and architecture-agnostic.** They require only attention weights as input and can be applied post hoc to any self-attention architecture without model modification. Demonstrated across three different models and tasks (Sections 2, 4, 5). Status: **supported**.

---

## Open Questions

1. **Decoder adaptation.** How should attention rollout and flow be adapted for Transformer decoders with causal masking? The authors suggest normalizing based on the receptive field of attention (Section 5) but do not evaluate this. Not yet addressed in this reference set.

2. **Effective attention integration.** Would building the attention graph with effective attention weights (Brunner et al., 2020) instead of raw attention improve the accuracy of rollout and flow? Suggested by the authors (Section 5) but not evaluated. Not yet addressed.

3. **Gradient-based adjustment.** Can gradient-based attribution methods (Ancona et al., 2019) be used to adjust attention weights for more accurate flow estimation? Suggested by the authors (Section 5) but not evaluated. Not yet addressed.

4. **Value vector contribution.** How much information flow is captured by attention weights alone vs. the value vectors and feed-forward transformations that are currently ignored? Not yet addressed.

---

## Core References and Why They Are Referenced

### Foundational Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer and self-attention mechanism whose information flow this paper analyzes. The residual connections in the Transformer block (V_{l+1} = V_l + W_att V_l) are central to both proposed methods.
- **Bahdanau et al. (2015)** -- *Neural Machine Translation by Jointly Learning to Align and Translate.* Foundational attention mechanism that the Transformer extends. Referenced as the origin of attention-based sequence models.

### Token Identifiability and Attention Interpretability

- **Brunner et al. (2020)** -- *On Identifiability in Transformers.* Identifies the lack of token identifiability in higher-layer Transformer embeddings, which is the root cause of the problem this paper addresses. The authors suggest using effective attention weights from this work as a future improvement.
- **Serrano and Smith (2019)** -- *Is Attention Interpretable?* Shows that attention weights do not necessarily correspond to the relative importance of input tokens, providing empirical evidence that motivates the proposed methods.
- **Jain and Wallace (2019)** -- *Attention Is Not Explanation.* Argues against equating attention with explanation, part of the debate motivating better attention-based attribution methods.
- **Wiegreffe and Pinter (2019)** -- *Attention Is Not Not Explanation.* Responds to Jain and Wallace, arguing attention can offer meaningful interpretations, supporting the view that improving attention-based attribution is worthwhile.
- **Pruthi et al. (2019)** -- *Learning to Deceive with Attention-Based Explanations.* Shows attention weights can be manipulated, further supporting the case that raw attention should not be used uncritically.

### Attention Visualization and Analysis

- **Clark et al. (2019)** -- *What Does BERT Look At? An Analysis of BERT's Attention.* Analyzes BERT's attention heads for syntactic and semantic functions using raw attention weights. This paper proposes rollout and flow as improvements over such raw attention analysis.
- **Vig (2019)** -- *Visualizing Attention in Transformer-Based Language Models.* Provides attention visualization tools using raw attention. The paper reproduces raw attention visualizations (Figure 1a) and shows their limitations.

### Models and Datasets

- **Radford et al. (2019)** -- *Language Models Are Unsupervised Multitask Learners.* GPT-2 Transformer blocks used in the primary verb prediction model architecture.
- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* Pre-trained BERT model used for qualitative pronoun resolution experiments.
- **Sanh et al. (2019)** -- *DistilBERT, a Distilled Version of BERT.* DistilBERT model used for the secondary sentiment analysis experiments on SST-2.
- **Linzen et al. (2016)** -- *Assessing the Ability of LSTMs to Learn Syntax-Sensitive Dependencies.* Provides the subject-verb agreement dataset used as the primary evaluation task, chosen because it offers a clear hypothesis about which input tokens are important.
- **Socher et al. (2013)** -- *Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank.* SST-2 dataset used for the DistilBERT evaluation.
- **Wang et al. (2018)** -- *GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding.* GLUE benchmark containing the SST-2 task.

### Graph Algorithms

- **Cormen et al. (2009)** -- *Introduction to Algorithms.* Provides the maximum flow algorithm framework used in attention flow. The formal definition of flow networks (capacity constraints, flow conservation) comes from this textbook.
