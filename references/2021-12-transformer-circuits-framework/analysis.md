# A Mathematical Framework for Transformer Circuits

**Authors:** Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah (Anthropic)
**Date:** December 2021, Transformer Circuits Thread

**Type:** Web-based research article (not a formal peer-reviewed paper)
**URL:** https://transformer-circuits.pub/2021/framework/index.html

---

## Core Research Problem

Transformer-based language models are increasingly deployed in real-world applications, yet their internal computations remain opaque. Even years after training, both creators and users routinely discover unexpected model capabilities -- including problematic behaviors -- they were previously unaware of. This opacity poses a fundamental challenge for safety and controllability: if we cannot understand what computations a model performs, we cannot reliably predict or control its behavior.

Prior work on interpreting neural networks has largely treated models as black boxes, analyzing input-output behavior (probing, behavioral evaluations) rather than reverse-engineering the internal algorithms. The Circuits framework (Olah et al., 2020) proposed studying neural networks by identifying meaningful features and the circuits connecting them, but applied this primarily to vision models (CNNs). Extending this approach to transformers is more challenging because: (1) the attention mechanism creates complex token-to-token information flow that is absent in feedforward architectures, (2) the residual stream enables composition across layers in ways that make individual components harder to isolate, and (3) the vocabulary size and sequence-level computation introduce combinatorial complexity not present in image classification.

The core challenge is: **how to develop a rigorous mathematical framework that decomposes transformer computations into interpretable, composable circuits, enabling mechanistic understanding of what algorithms transformers learn.**

---

## Problem Solutions

The paper introduces a mathematical framework for understanding transformers by exploiting their extensive linear structure. The key insight is that if one freezes the attention patterns (the nonlinear component), the entire transformer becomes a linear map from token embeddings to output logits -- and this map can be decomposed into a sum of interpretable terms corresponding to "paths" through the model. The solution rests on three pillars:

1. **The residual stream as a shared communication channel.** All transformer layers read from and write to the same high-dimensional residual stream via linear projections. This means the residual stream at any point is simply the sum of the original embedding and all prior layer outputs, enabling clean additive decomposition.

2. **Attention heads as pairs of independent low-rank circuits.** Each attention head performs two largely independent computations: a QK (query-key) circuit that determines the attention pattern (which tokens attend to which), and an OV (output-value) circuit that determines what information is moved when a token is attended to. The intermediate query, key, and value vectors are superficial byproducts; the fundamental objects are the low-rank bilinear forms W_Q^T W_K and W_O W_V.

3. **Composition of attention heads across layers.** In multi-layer models, the output of one attention head can feed into the query, key, or value computation of a head in a later layer, creating three types of composition (Q-composition, K-composition, V-composition). This enables multi-step algorithms that no single head could implement alone, most notably **induction heads** -- two-head circuits that implement a basic form of in-context learning.

---

## Approach Details

### Method

The framework studies **attention-only transformers** -- standard decoder-only transformers with MLP layers, layer normalization, and biases removed. This simplification preserves the core attention mechanism while making the model fully amenable to linear-algebraic analysis (since layer norm and biases can be folded into adjacent weight matrices).

The central mathematical tool is the **tensor product notation**. A single attention head's output is written as:

> h(x) = (A ⊗ W_OV) X

where A = softmax(X^T W_Q^T W_K X) is the attention pattern matrix, W_OV = W_O W_V is the combined output-value matrix, X is the matrix of token embeddings from the residual stream, and (A ⊗ W) X = A X W^T. The mixed-product property (A ⊗ B)(C ⊗ D) = (AC) ⊗ (BD) enables clean composition of terms across layers.

**One-layer transformer decomposition.** The complete map from input tokens to output logits decomposes as:

> T = Id ⊗ W_U W_E + Σ_h A^h ⊗ W_U W^h_OV W_E

The first term is the **direct path** (token embedding → unembedding, bypassing attention entirely), which encodes bigram statistics. The second term sums over all attention heads h, where each head implements a **skip-trigram**: the destination token's logits are influenced by source tokens weighted by the attention pattern, with the effect of each source token determined by W_U W^h_OV W_E.

**Two-layer transformer decomposition.** Adding a second layer introduces composition terms:

> T = Id ⊗ W_U W_E + Σ_h A^h ⊗ (W_U W^h_OV W_E) + Σ_{h2,h1} (A^{h2} A^{h1}) ⊗ (W_U W^{h2}_OV W^{h1}_OV W_E)

The third term represents **virtual attention heads** created through V-composition: the combined attention pattern A^{h2} A^{h1} and combined OV matrix W^{h2}_OV W^{h1}_OV define a new effective head that neither physical head implements alone. Q-composition and K-composition also occur but affect the attention patterns of second-layer heads rather than creating separable virtual heads.

### Key Technical Components

- **QK circuit (W_Q^T W_K):** Determines the attention pattern. For a given head, this is a low-rank bilinear form over the residual stream. The eigenstructure of W_E^T W_Q^T W_K W_E (the "full QK circuit" in token space) reveals which token pairs have high mutual attention. Positive eigenvalues indicate the head attends to tokens with similar features; negative eigenvalues indicate dissimilar-feature attention.

- **OV circuit (W_O W_V):** Determines how attended-to tokens affect the output logits. The full OV circuit W_U W_OV W_E maps source tokens to logit changes at the destination. Heads where this matrix has large positive diagonal entries are **copying heads** (attending to a token increases that token's logit). Heads with large off-diagonal entries implement token-level associations.

- **Three types of composition:**
  - **Q-composition:** Output of a layer-1 head feeds into the query of a layer-2 head, modifying *what* the layer-2 head looks for.
  - **K-composition:** Output of a layer-1 head feeds into the key of a layer-2 head, modifying *how* tokens advertise themselves to the layer-2 head.
  - **V-composition:** Output of a layer-1 head feeds into the value of a layer-2 head, creating virtual attention heads with composed attention patterns and OV maps.

- **Induction heads:** The central algorithmic discovery. An induction head is a two-head circuit in a two-layer model that implements the following algorithm: given a current token [A], search the context for a previous occurrence of [A], then copy the token that followed it. The mechanism works through K-composition:
  1. A **previous token head** in layer 1 attends to the immediately preceding token and copies its identity into the residual stream at each position.
  2. An **induction head** in layer 2 uses K-composition so that its keys encode "what token preceded me" (from the layer-1 output). Its queries encode "what is the current token." When the current token [A] matches a previous token [A], the induction head attends to the position *after* that previous [A] and copies it forward via its OV circuit.

  This implements a form of in-context learning: the model can predict [B] after [A] even if the [A][B] bigram never appeared in training, as long as it appeared earlier in the context. The paper notes that induction heads require at least two layers -- they cannot be implemented by a single attention head.

### Experimental Setup

- **Models:** Attention-only transformers with 0, 1, and 2 layers, trained on a standard language modeling corpus. The paper does not use standard pretrained models (GPT, BERT) but trains custom attention-only models to enable clean mathematical analysis.
- **Analysis methods:** Eigenvalue decomposition of QK and OV circuits to classify head behavior; ablation studies (zeroing out individual heads and measuring loss change); path-based loss decomposition to quantify the contribution of each term in the expansion.
- **Evaluation:** Language modeling loss (cross-entropy in nats) on the training distribution.

### Key Results

**Loss decomposition by path order:**

| Path Order | Description | Loss Reduction (nats) |
|---|---|---|
| Order 0 | Direct path (bigram statistics) | 1.8 |
| Order 1 | Single attention heads (skip-trigrams) | 5.2 |
| Order 2 | Composed heads (V-composition) | 0.3 |

- The **direct path** accounts for bigram-level predictions (e.g., "Barack" → "Obama").
- **Single attention heads** (order 1) contribute the majority of the loss reduction, implementing skip-trigram patterns where a source token influences a destination token's prediction through attention.
- **V-composition** (order 2, virtual attention heads) contributes a smaller but measurable amount. The paper initially underestimated the importance of Q-composition and K-composition, later issuing a correction noting these are more significant than originally reported.

**Head type taxonomy in one-layer models:**

- **Previous token heads:** Attend primarily to the immediately preceding position (high attention on position -1). These are precursors to the layer-1 component of induction circuits.
- **Copying heads:** The OV circuit has strongly positive eigenvalues, meaning attending to a token increases that same token's logit.
- **Skip-trigram heads:** Implement context-dependent token predictions that go beyond bigrams (e.g., "keep...at → bay").

**Induction heads in two-layer models:**

- Induction heads emerge only in models with at least two layers, confirming the theoretical prediction that the induction algorithm requires composition.
- The QK circuit of induction heads shows strongly positive eigenvalues (consistent with matching the current token to previous occurrences), and the OV circuit shows copying behavior (strongly positive eigenvalues, copying the attended-to token's identity to the output).
- K-composition between a previous token head and an induction head is the primary mechanism, validated by the head interaction matrix.

### Limitations

- The framework applies cleanly only to **attention-only** transformers. MLPs constitute approximately two-thirds of parameters in standard transformers and are excluded from the analysis. The authors acknowledge this as a major limitation, as MLPs likely implement important computations (e.g., factual knowledge storage).
- The analysis focuses on **small models** (1--2 layers). The combinatorial explosion of paths in deeper models makes exhaustive decomposition infeasible. Whether the identified circuits (induction heads, skip-trigrams) remain the dominant mechanisms in large-scale models is an open question.
- The paper assumes **frozen attention patterns** for the linear decomposition. In practice, attention patterns depend on the input, and the interaction between the nonlinear softmax and the linear structure is not fully captured.
- The later **correction** regarding composition indicates the original analysis underestimated Q-composition and K-composition, suggesting the framework's quantitative conclusions about composition importance should be treated cautiously.

---

## Conclusions

1. **Transformers have extensive exploitable linear structure.** By freezing attention patterns, the entire transformer becomes a linear map decomposable into a sum of interpretable paths from input tokens to output logits. This decomposition reveals that individual attention heads and their compositions correspond to distinct, identifiable computations.

2. **Attention heads implement two independent circuits.** The QK circuit determines the attention pattern (which tokens attend to which), and the OV circuit determines the effect of attention (what information is transferred). These circuits can be analyzed independently via their eigenstructure to classify head behavior (copying, previous-token, skip-trigram).

3. **The residual stream is the central organizing concept.** All transformer components communicate through the shared residual stream via linear read/write operations. This additive structure enables clean decomposition and explains how information flows across layers.

4. **Composition across layers enables qualitatively new algorithms.** Three types of composition (Q, K, V) allow pairs of attention heads to implement computations that no single head can. V-composition creates "virtual attention heads" with composed attention patterns, while Q- and K-composition modify the attention computation of later heads based on earlier heads' outputs.

5. **Induction heads are a concrete example of a learned algorithm.** The two-head induction circuit -- a previous token head composing with a copying head via K-composition -- implements in-context pattern matching and copying. This provides a mechanistic explanation for in-context learning in small models and demonstrates that at least two layers of attention are necessary for this capability.

6. **Zero- and one-layer models are limited to statistical patterns.** Zero-layer models can only capture bigram statistics. One-layer models add skip-trigrams (context-dependent bigrams mediated by attention) but cannot implement multi-step algorithms. Genuine algorithmic behavior (in-context learning) requires the compositional power of two or more layers.

---

## Core References and Why They Are Referenced

### Mechanistic Interpretability Foundations

- **Olah et al. (2020)** -- *Zoom In: An Introduction to Circuits.* Introduces the Circuits framework for mechanistic interpretability of neural networks, originally applied to vision models. The transformer circuits paper extends this framework to attention-based architectures, inheriting the goal of identifying interpretable features and circuits.

- **Olah et al. (2017)** -- *Feature Visualization.* Foundational work on understanding what individual neurons in neural networks compute. The transformer circuits paper builds on this tradition of reverse-engineering neural network components.

### Transformer Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer architecture with multi-head self-attention, the residual stream, and the query-key-value decomposition that the mathematical framework analyzes.

- **Radford et al. (2019)** -- *Language Models are Unsupervised Multitask Learners (GPT-2).* Demonstrates that autoregressive transformers can learn diverse capabilities from unsupervised pre-training. The transformer circuits paper seeks to explain *how* such capabilities are mechanistically implemented.

### Attention Analysis

- **Clark et al. (2019)** -- *What Does BERT Look At? An Analysis of BERT's Attention.* Early work analyzing attention patterns in transformers, identifying syntactic heads and positional heads. The mathematical framework provides a more rigorous basis for understanding *why* heads develop particular attention patterns by analyzing the QK and OV circuits.

- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, and the Rest Can Be Pruned.* Identifies specialized attention head types (positional, syntactic, rare-word heads) in encoder models. The transformer circuits paper provides a complementary mathematical account of how specialized heads arise from the QK/OV circuit structure.

### In-Context Learning

- **Brown et al. (2020)** -- *Language Models are Few-Shot Learners (GPT-3).* Demonstrates that large language models can perform tasks from in-context examples without fine-tuning. The transformer circuits paper provides a mechanistic explanation for how in-context learning can work via induction heads, at least in small models.

#### Cross-References in Available Papers

- **Specialized Attention Heads and Pruning (`2019-07-specialized-attention-heads-pruning`):** Voita et al. (2019) identify specialized head types (positional, syntactic, rare-word) in encoder transformers and show most heads can be pruned. The mathematical framework provides a complementary decoder-focused analysis, explaining head specialization through the eigenstructure of QK and OV circuits rather than through behavioral probing.

- **BERT Attention Analysis (`2019-08-bert-attention-analysis`):** Clark et al. (2019) analyze BERT's attention patterns and find heads attending to specific syntactic relations. The transformer circuits paper goes beyond pattern description to explain *why* particular patterns emerge, grounded in the mathematical structure of the QK circuit.

- **Dark Secrets of BERT (`2019-11-dark-secrets-of-bert`):** Kovaleva et al. (2019) observe that many BERT attention heads show repetitive patterns (diagonal, vertical, block) with limited linguistic function. The mathematical framework explains vertical attention patterns (attending to specific positions) as a natural consequence of positional heads, and the prevalence of "non-linguistic" patterns as heads serving structural roles (analogous to the attention sink phenomenon later identified by Xiao et al., 2023).

- **Sixteen Heads Better Than One (`2019-12-sixteen-heads-better-than-one`):** Michel et al. (2019) show that many attention heads can be pruned at inference time with minimal performance loss. The mathematical framework's decomposition into independent QK/OV circuits provides a theoretical basis for this observation: heads whose OV circuit has small eigenvalues contribute little to the output regardless of their attention pattern.

- **Quantifying Attention Flow (`2020-07-quantifying-attention-flow`):** Abnar and Zuidema (2020) propose attention rollout and attention flow methods to trace information propagation through transformer layers. The mathematical framework's path decomposition provides an exact (rather than approximate) account of information flow, but only for the linear component with frozen attention patterns.

- **Attention Sinks (`2024-05-attention-sinks-streaming`):** Xiao et al. (2023) discover that LLMs allocate disproportionate attention to initial tokens regardless of semantic content. The mathematical framework's analysis of attention heads as QK/OV circuits helps explain this: when the QK circuit produces no strong match for the current query, the softmax normalization forces residual attention mass onto the most globally visible tokens (initial positions in autoregressive models), a structural rather than semantic phenomenon.
