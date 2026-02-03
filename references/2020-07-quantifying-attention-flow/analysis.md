# Quantifying Attention Flow in Transformers

**Authors:** Samira Abnar, Willem Zuidema (ILLC, University of Amsterdam)
**Date:** July 2020, ACL 2020, DOI:10.18653/v1/2020.acl-main.385 (arXiv:2005.00928)

---

## Core Research Problem

Self-attention in Transformers combines information from attended embeddings into the representation of the focal embedding at the next layer. Across layers, information originating from different tokens gets increasingly mixed: embeddings in higher layers are heavily contextualized and may all carry similar information. As a result, raw attention weights at higher layers become nearly uniform and lose their interpretability as indicators of which input tokens are important for a given prediction. Serrano and Smith (2019) showed that attention weights do not necessarily correspond to the relative importance of input tokens, and Brunner et al. (2020) identified the lack of "token identifiability" in higher-layer embeddings as the root cause.

Prior work on attention visualization (Vaswani et al., 2017; Vig, 2019; Clark et al., 2019) reported raw attention weights without accounting for the fact that each layer's attention operates over already-mixed representations, not the original input tokens. These "embedding attentions" (layer-local attention weights) cannot be directly read as "token attentions" (attention to original input tokens) because they ignore how information propagates through intermediate layers and residual connections. The debate around whether attention is explanation (Jain and Wallace, 2019; Wiegreffe and Pinter, 2019) further motivated the need for methods that account for cross-layer information mixing. **The core challenge is: how to compute the effective attention from higher-layer embeddings back to input tokens, taking into account the recursive mixing of information across all preceding layers and residual connections.**

---

## Problem Solutions

The paper proposes two post hoc methods for computing "token attention" -- the effective attention from any hidden embedding back to the original input tokens -- by recursively incorporating attention weights from all preceding layers. Both methods model information flow as a Directed Acyclic Graph (DAG) where nodes are input tokens and hidden embeddings, edges are attention connections, and edge weights are attention weights.

1. **Attention rollout** assumes token identities are linearly combined through layers according to attention weights. It computes token attention by recursively multiplying attention matrices from the current layer back to the input, accounting for residual connections via an identity matrix addition.
2. **Attention flow** treats the attention graph as a flow network where edge capacities are attention weights. It uses a maximum flow algorithm to compute the maximum possible flow from each hidden embedding (source) to each input token (sink).
3. **Residual connection integration.** Both methods augment the attention graph with identity connections to represent residual connections, which tie corresponding positions across layers and are critical for accurate information flow modeling.

---

## Approach Details

### Method

Both methods take as input the raw attention weight matrices from all layers and produce, for each layer, a matrix of token attentions back to the input tokens.

**Residual connection handling.** In a Transformer block with residual connections, the output of layer l+1 is:

> V_{l+1} = V_l + W_att V_l = (W_att + I) V_l

To account for residual connections, the raw attention matrix is augmented with an identity matrix and re-normalized:

> A = 0.5 W_att + 0.5 I

where W_att is the raw attention matrix and I is the identity matrix. This A replaces the raw attention in both methods.

**Multi-head handling.** For simplicity, the paper averages attention weights across all heads at each layer before computing rollout or flow. Appendix A.1 describes how to analyze individual heads: for head k at layer i, compute rollout as `A~(i, k) = A(i, k) A_bar(i)`, where `A_bar(i)` is the rollout computed with averaged (single-head) attention up to layer i. This avoids the incorrect assumption that there is no mixing of information between heads (which occurs in the position-wise feed-forward network).

**Attention rollout.** Given a Transformer with L layers, attention rollout recursively multiplies the (residual-augmented) attention matrices from all layers below:

> A~(l_i) = A(l_i) A~(l_{i-1})  if i > j
> A~(l_i) = A(l_i)              if i = j

where A~ is the rollout attention, A is the residual-augmented raw attention, and multiplication is matrix multiplication. To compute input attention, set j = 0. The intuition: the weight of each path from a hidden embedding to an input token is the product of all edge weights along that path, and the total token attention is the sum over all paths (computed implicitly by the matrix multiplication).

**Attention flow.** The attention graph is treated as a flow network: a directed graph G = (V, E) with edge capacities C = {c_uv} set to the attention weights. Given source node s (a hidden embedding) and target node t (an input token), the maximum flow algorithm (Cormen et al., 2009) finds the flow f: E -> R that maximizes the total flow from s to t, subject to: (a) capacity constraint: |f_uv| <= c_uv for all edges; (b) flow conservation: inflow equals outflow at every node except s and t. The key difference from rollout is that the weight of a single path is the minimum edge weight along that path (the bottleneck), and overlapping paths cannot be simply summed (to avoid overflow on shared edges), so the maximum flow algorithm is needed.

### Key Technical Components

**Computational complexity.** Attention rollout runs in O(d * n^2) and attention flow in O(d^2 * n^4), where d is the depth (number of layers) and n is the number of tokens. Both are polynomial time.

**Complementary views.** Attention rollout treats attention weights as proportion factors and propagates token identities exactly according to these proportions. This makes rollout stricter and produces more focused attention patterns. Attention flow treats attention weights as capacities and uses as much capacity as possible, computing the maximum possibility of token identity propagation. This makes flow more relaxed and produces attention patterns that are amortized among the set of most-attended tokens, indicating a set of important tokens without sharp distinctions between them.

**Blank-out attribution.** As a ground-truth proxy for input token importance, blank-out replaces each token one-by-one with UNK and measures the change in predicted probability of the correct class. Spearman's rank correlation between attention-based importance and blank-out scores serves as the primary evaluation metric.

### Experimental Setup

**Primary model (verb number prediction).** A Transformer encoder with GPT-2 Transformer blocks (Radford et al., 2019; Wolf et al., 2019), without causal masking. 6 layers, 8 heads, hidden/embedding size 128. A [CLS] token is added and its final-layer embedding serves as classifier input. Trained on the subject-verb agreement dataset (Linzen et al., 2016), achieving 0.96 accuracy on the task (predicting singular vs. plural verb given a sentence up to the verb position).

**Secondary model (sentiment analysis).** DistilBERT (Sanh et al., 2019) fine-tuned on SST-2 (Socher et al., 2013) from the GLUE benchmark (Wang et al., 2018).

**Tertiary model (pronoun resolution).** Pre-trained BERT (Devlin et al., 2019), used for qualitative analysis of pronoun resolution via masked language modeling.

**Evaluation metrics:**
- Spearman's rank correlation between attention-based importance scores and blank-out scores (2000 test samples for verb prediction, 100 for DistilBERT).
- Spearman's rank correlation between attention-based importance scores and input gradients.
- Qualitative visualization of attention maps.

### Key Results

**Correlation with blank-out scores (verb number prediction, 2000 test samples):**

| Method | L1 | L2 | L3 | L4 | L5 | L6 |
|---|---|---|---|---|---|---|
| Raw | 0.69+-0.27 | 0.10+-0.43 | -0.11+-0.49 | -0.09+-0.52 | 0.20+-0.45 | 0.29+-0.39 |
| Rollout | 0.32+-0.26 | 0.38+-0.27 | 0.51+-0.26 | 0.62+-0.26 | 0.70+-0.25 | **0.71+-0.24** |
| Flow | 0.32+-0.26 | 0.44+-0.29 | **0.70+-0.25** | **0.70+-0.22** | **0.71+-0.22** | 0.70+-0.22 |

- Raw attention has high correlation only at layer 1 (0.69) and degrades sharply to negative correlations (-0.11 at L3, -0.09 at L4) before recovering slightly at L6 (0.29).
- Both rollout and flow improve monotonically with depth, reaching 0.70--0.71 at the final layer.
- Attention flow converges faster (0.70 at L3) than rollout (0.70 at L5).

**Correlation with input gradients (verb number prediction, 2000 test samples):**

| Method | L1 | L2 | L3 | L4 | L5 | L6 |
|---|---|---|---|---|---|---|
| Raw | 0.53+-0.33 | 0.16+-0.38 | -0.06+-0.42 | 0.00+-0.47 | 0.24+-0.40 | 0.46+-0.35 |
| Rollout | 0.22+-0.31 | 0.27+-0.32 | 0.39+-0.32 | 0.47+-0.32 | 0.53+-0.32 | 0.54+-0.31 |
| Flow | 0.22+-0.31 | 0.31+-0.34 | **0.54+-0.32** | **0.61+-0.28** | **0.60+-0.28** | **0.61+-0.28** |

- The same pattern holds: raw attention degrades in middle layers, while rollout and flow improve steadily.
- Attention flow reaches a plateau of ~0.61 from L3 onward; rollout plateaus at ~0.54 from L5.
- Attention flow consistently outperforms rollout on input gradient correlation.

**DistilBERT on SST-2 (correlation with input gradients, 100 test samples):**

| Method | L1 | L3 | L5 | L6 |
|---|---|---|---|---|
| Raw | 0.12+-0.21 | 0.09+-0.21 | 0.08+-0.20 | 0.09+-0.21 |
| Rollout | 0.11+-0.19 | 0.12+-0.21 | 0.13+-0.21 | 0.13+-0.20 |
| Flow | 0.11+-0.19 | 0.11+-0.21 | 0.12+-0.22 | **0.14+-0.21** |

- All three methods yield low correlations on this model/task, but rollout and flow still slightly outperform raw attention, particularly at deeper layers.

**Qualitative analysis -- pronoun resolution with pre-trained BERT.** The paper examines attention weights from a [MASK] token to candidate pronoun referents. For "The author talked to Sara about [MASK] book," raw attention at the final layer is inconsistent with the model's prediction, while both rollout and flow correctly assign higher weight to the predicted referent. For "Mary convinced John of [MASK] love," only attention flow is consistent with the model's prediction across all layers.

### Attention Rollout vs. Attention Flow

The main qualitative difference between the two methods:
- **Attention rollout** produces more focused patterns because it strictly propagates proportions of token identities. This can be useful for identifying the single most important token but may be overly strict given the simplifying assumptions.
- **Attention flow** produces more distributed patterns because it treats attention as capacities and computes maximum possible flow. This amortizes weight among the top tokens, making it better at identifying a set of important tokens. The relaxation of attention flow appears to be a useful property, as evidenced by its consistently higher correlations with both blank-out and gradient-based importance scores.

### Limitations

- All analysis is for Transformer encoders without causal masking. In Transformer decoders, future tokens are masked, creating a bias toward initial tokens. To apply these methods to decoders, normalization based on the receptive field of attention is needed.
- The methods approximate information flow using only attention weights, ignoring the value vectors and feed-forward transformations that also affect information propagation.
- Averaging attention across heads is a simplification; the individual-head analysis in Appendix A.1 is not extensively evaluated.

---

## Conclusions

1. **Raw attention becomes unreliable at higher layers.** In a 6-layer Transformer, raw attention weights of the [CLS] token show high correlation with token importance at layer 1 (0.69 with blank-out) but degrade to near-zero or negative correlations in middle layers (-0.11 at L3), reflecting the increasing contextualization and loss of token identifiability in deeper embeddings.

2. **Attention rollout improves token attribution by accounting for cross-layer propagation.** By recursively multiplying residual-augmented attention matrices, rollout produces token attention scores that improve monotonically with depth, reaching 0.71 correlation with blank-out at the final layer compared to 0.29 for raw attention.

3. **Attention flow provides the most reliable token attribution.** Treating the attention graph as a flow network and computing maximum flow yields consistently higher correlations with both blank-out scores and input gradients compared to both raw attention and rollout. Attention flow reaches 0.70 correlation with blank-out by layer 3 and plateaus at 0.61 for input gradient correlation from layer 3 onward.

4. **Residual connections are critical for accurate information flow modeling.** Both methods augment attention matrices with identity matrices to represent residual connections (A = 0.5 W_att + 0.5 I), which tie corresponding positions across layers. Without this, the methods would ignore a major pathway for information preservation through the network.

5. **The two methods offer complementary views.** Rollout is stricter and produces more focused attention patterns, useful for identifying single dominant input tokens. Flow is more relaxed and identifies a set of important tokens without sharp distinctions, which empirically correlates better with ground-truth importance.

6. **Task-agnostic and architecture-agnostic.** Both methods require only attention weights as input and can be applied post hoc to any self-attention architecture. They do not modify the model or require retraining, making them practical diagnostic tools for visualization and debugging.

---

## Core References and Why They Are Referenced

### Foundational Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer and self-attention mechanism whose information flow this paper analyzes. The residual connections in the Transformer block (V_{l+1} = V_l + W_att V_l) are central to both proposed methods.
- **Bahdanau et al. (2015)** -- *Neural Machine Translation by Jointly Learning to Align and Translate.* Foundational attention mechanism that the Transformer extends. Referenced as the origin of attention-based models.

### Token Identifiability and Attention Interpretability

- **Brunner et al. (2020)** -- *On Identifiability in Transformers.* Identifies the lack of token identifiability in higher-layer Transformer embeddings, which is the root cause of the problem this paper addresses. Motivates the need to track information back to the input layer.
- **Serrano and Smith (2019)** -- *Is Attention Interpretable?* Shows that attention weights do not necessarily correspond to the relative importance of input tokens. Provides empirical evidence that raw attention is unreliable, motivating the proposed methods.
- **Jain and Wallace (2019)** -- *Attention Is Not Explanation.* Argues against equating attention with explanation. Part of the debate that motivates the need for better attention-based attribution methods.
- **Wiegreffe and Pinter (2019)** -- *Attention Is Not Not Explanation.* Responds to Jain and Wallace, arguing attention can offer meaningful interpretations. Supports the view that improving attention-based attribution (as this paper does) is worthwhile.
- **Pruthi et al. (2019)** -- *Learning to Deceive with Attention-Based Explanations.* Shows attention weights can be manipulated, further supporting the case that raw attention should not be used uncritically.

### Attention Visualization and Analysis

- **Clark et al. (2019)** -- *What Does BERT Look At? An Analysis of BERT's Attention.* Analyzes BERT's attention heads for syntactic and semantic functions using raw attention. This paper argues that raw attention is insufficient and proposes rollout and flow as improvements.
- **Vig (2019)** -- *Visualizing Attention in Transformer-Based Language Models.* Provides attention visualization tools that use raw attention. The paper starts by reproducing raw attention visualizations (Figure 1a) and showing their limitations.

### Models and Datasets

- **Radford et al. (2019)** -- *Language Models Are Unsupervised Multitask Learners.* GPT-2 Transformer blocks used in the primary verb prediction model architecture.
- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* Pre-trained BERT model used for qualitative pronoun resolution experiments.
- **Linzen et al. (2016)** -- *Assessing the Ability of LSTMs to Learn Syntax-Sensitive Dependencies.* Provides the subject-verb agreement dataset used as the primary evaluation task, chosen because it offers a clear hypothesis about which input tokens are important.
- **Sanh et al. (2019)** -- *DistilBERT, a Distilled Version of BERT.* DistilBERT model used for the secondary sentiment analysis experiments.
- **Socher et al. (2013)** -- *Recursive Deep Models for Semantic Compositionality Over a Sentiment Treebank.* SST-2 dataset used for the DistilBERT evaluation.

### Graph Algorithms

- **Cormen et al. (2009)** -- *Introduction to Algorithms.* Provides the maximum flow algorithm framework used in attention flow. The formal definition of flow networks (capacity constraints, flow conservation) comes from this textbook.

#### Cross-References in Available Papers

- **Clark et al. (2019)** is available as `2019-08-bert-attention-analysis`. Abnar and Zuidema explicitly cite Clark et al. as an example of raw attention visualization. Both papers investigate attention patterns in Transformer models, but Clark et al. focus on identifying specialized head functions using raw attention, while Abnar and Zuidema argue that raw attention is unreliable in higher layers and propose rollout and flow as corrections. Clark et al.'s finding that attention heads encode syntactic relations (Table 1, 94.3% for determiners at head 8-11) uses raw attention, and it would be informative to re-evaluate those results using attention rollout or flow.
- **Voita et al. (2019)** is available as `2019-07-specialized-attention-heads-pruning`. Although not directly cited in Abnar and Zuidema, Voita et al.'s identification of positional, syntactic, and rare-word heads in NMT encoders raises the same question: how reliable are the raw attention patterns used to identify these head functions when information mixes across layers? Attention rollout and flow could be applied to re-examine whether the specialized heads identified by Voita et al. retain their roles when cross-layer propagation is accounted for.
- **Michel et al. (2019)** is available as `2019-12-sixteen-heads-better-than-one`. Michel et al.'s gradient-based head importance score (I_h) measures how much removing a head affects the loss, which is conceptually related to Abnar and Zuidema's blank-out attribution (measuring how much removing an input token affects the output). Both approaches quantify importance through ablation, but at different granularities (heads vs. input tokens).
- **Kovaleva et al. (2019)** is available as `2019-11-dark-secrets-of-bert`. Kovaleva et al.'s taxonomy of BERT attention patterns (Vertical, Diagonal, Block, Heterogeneous) is based on raw attention maps. Their finding that many heads produce "Vertical" patterns (attending to [CLS]/[SEP]) may be related to the uniform attention problem in higher layers that Abnar and Zuidema identify; applying attention rollout or flow could reveal whether these patterns reflect genuine information routing or artifacts of token identity loss.
