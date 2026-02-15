---
title: "A Mathematical Framework for Transformer Circuits"
authors: "Elhage, Nanda, Olsson, Henighan, Joseph, Mann, Askell, Bai, Chen, Conerly, DasSarma, Drain, Ganguli, Hatfield-Dodds, Hernandez, Jones, Kernion, Lovitt, Ndousse, Amodei, Brown, Clark, Kaplan, McCandlish, Olah"
year: 2021
venue: "Transformer Circuits Thread (Anthropic)"
paper_type: informal
categories: ["mechanistic-interpretability", "attention-analysis", "in-context-learning"]
scope: ["attention-only transformers", "mathematical decomposition", "0-2 layer models"]
benchmarks_used: []
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "Attention heads can be decomposed into two independent low-rank circuits: a QK circuit (W_Q^T W_K) determining attention patterns and an OV circuit (W_O W_V) determining what information is moved"
    evidence: "Attention Heads as Information Movement section, tensor product derivation"
    status: supported
    scope: "attention-only transformers (no MLPs, no layer norm, no biases), decoder-only architecture"
    magnitude: "qualitative — exact mathematical decomposition, not an approximation"
  - id: C2
    claim: "One-layer attention-only transformers are an ensemble of bigram and skip-trigram models, with skip-trigram tables directly readable from weights via W_E^T W_QK W_E (QK circuit) and W_U W_OV W_E (OV circuit)"
    evidence: "One-Layer Attention-Only Transformers section, path expansion"
    status: supported
    scope: "one-layer attention-only transformers, ~50K vocabulary, d_head=64"
    magnitude: "qualitative — complete analytical decomposition into interpretable terms"
  - id: C3
    claim: "Most attention heads in one-layer models are copying heads: 10 out of 12 heads in the analyzed model have significantly positive OV eigenvalues, consistent with copying behavior"
    evidence: "Detecting Copying Behavior section, eigenvalue histogram"
    status: supported
    scope: "single one-layer model with 12 heads, d_head=64"
    magnitude: "10 out of 12 heads (83%) show significantly positive OV eigenvalues"
  - id: C4
    claim: "Two-layer attention-only transformers use K-composition between a previous token head and induction heads to implement in-context pattern completion: [a][b]...[a] -> [b]"
    evidence: "Induction Heads section, composition diagram, random token experiments"
    status: supported
    scope: "two-layer attention-only transformer, verified on both natural text and random repeated sequences"
    magnitude: "qualitative — mechanism verified on completely random token sequences (off-distribution)"
  - id: C5
    claim: "Induction heads require at least two layers of attention and cannot be implemented by a single attention head"
    evidence: "Induction Heads section, mechanistic analysis of K-composition requirement"
    status: supported
    scope: "attention-only transformers, standard softmax attention"
    magnitude: "qualitative — proven by mechanistic argument (K-composition requires cross-layer interaction)"
  - id: C6
    claim: "V-composition (virtual attention heads) has a small marginal effect in the analyzed two-layer model, while K-composition is the dominant form of composition"
    evidence: "Term Importance Analysis section, ablation algorithm"
    status: supported
    scope: "single two-layer attention-only model, ablation on language modeling loss"
    magnitude: "V-composition (Order 2) contributes 0.3 nats vs. 5.2 nats for Order 1 terms"
  - id: C7
    claim: "The residual stream acts as a shared communication channel with no privileged basis; all components read from and write to it via linear projections, enabling clean additive decomposition"
    evidence: "Virtual Weights and the Residual Stream section"
    status: supported
    scope: "general transformer architecture with residual connections"
    magnitude: "qualitative — follows from linearity of projections and additive residual structure"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Provides a mathematical decomposition of the Transformer architecture into interpretable QK/OV circuits and path expansions"
  - target: 2019-07-specialized-attention-heads-pruning
    type: complementary
    detail: "Voita et al. empirically identify specialized head types (positional, syntactic, rare-word); the circuits framework provides a mathematical basis for understanding how such specialization arises from QK/OV circuit structure"
  - target: 2019-12-sixteen-heads-better-than-one
    type: formalizes
    detail: "The QK/OV decomposition provides mechanistic explanation for why some heads can be pruned: heads with small OV eigenvalues contribute little to output"
  - target: 2020-07-quantifying-attention-flow
    type: extends
    detail: "Provides an exact decomposition of information flow in the linear component, whereas attention rollout approximates flow using only attention weights"
  - target: 2021-11-ff-layers-key-value-memories
    type: complementary
    detail: "Both provide mechanistic interpretations of Transformer components; Geva et al. focus on FFN layers while this paper focuses on attention heads. The circuits paper explicitly acknowledges MLP layers as a major gap in its analysis"
  - target: 2022-03-in-context-learning-induction-heads
    type: extended-by
    detail: "Olsson et al. build on this framework to study induction heads in large models, showing they are a key driver of in-context learning at all scales"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "QK/OV circuit analysis helps explain attention sink formation: when the QK circuit produces no strong match, residual attention mass falls on globally visible tokens"
  - target: 2025-04-retrieval-head-long-context-factuality
    type: extended-by
    detail: "Wu et al. extend the circuits program by identifying retrieval heads — a specific subnet implementing conditional retrieval from long context, analogous to how induction heads implement pattern completion"
  - target: 2025-04-attention-sink-emerges
    type: complementary
    detail: "Gu et al. show the first token's key vectors act as implicit biases in the QK circuit, absorbing excess attention probability mass — a specific mechanistic role for the first token within the QK/OV circuit framework"
  - target: 2022-09-transformerlens-library-mechanistic-interpretability
    type: complementary
    detail: "TransformerLens packages circuits-style model inspection and intervention workflows into reusable tooling, making this framework operational for day-to-day mechanistic analysis"
  - target: 2022-12-locating-editing-factual-associations-gpt
    type: complementary
    detail: "Meng et al. extends mechanistic circuit-style causal analysis into direct factual editing by introducing the ROME rank-one intervention on GPT MLP layers"
open_questions:
  - question: "How can the framework be extended to include MLP layers, which constitute two-thirds of standard transformer parameters?"
    addressed_by: null
  - question: "Do the identified circuits (induction heads, skip-trigrams) remain the dominant mechanisms in large-scale models with both attention and MLP layers?"
    addressed_by: 2022-03-in-context-learning-induction-heads
  - question: "How does superposition in the residual stream affect interpretability, given that computational dimensions far exceed residual stream dimensions?"
    addressed_by: null
  - question: "Can the skip-trigram 'bugs' arising from the factored QK/OV representation be quantified in terms of loss, and do they persist in larger models?"
    addressed_by: null
  - question: "What is the right summary statistic or matrix decomposition for formalizing 'copying' behavior in OV circuits?"
    addressed_by: null
---

# A Mathematical Framework for Transformer Circuits

**Authors:** Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah (Anthropic)
**Date:** December 2021, Transformer Circuits Thread

**Type:** Web-based research article (not a formal peer-reviewed paper)
**URL:** https://transformer-circuits.pub/2021/framework/index.html

---

## Core Research Problem

Transformer language models are deployed in increasingly broad real-world applications (GPT-3, LaMDA, Codex, Gopher), yet their internal computations remain opaque. Even years after training, both creators and users routinely discover model capabilities -- including problematic behaviors -- they were previously unaware of. This opacity poses a fundamental challenge: if the computations a model performs cannot be reverse-engineered, its behavior cannot be reliably predicted or controlled.

Prior interpretability work has either treated models as black boxes (probing, behavioral evaluation) or focused on vision models. The Distill Circuits thread (Olah et al., 2020) proposed reverse-engineering neural networks by identifying features and circuits, but applied this to convolutional architectures. Extending this to transformers is more challenging because: (1) the attention mechanism creates complex token-to-token information flow absent in feedforward architectures, (2) the residual stream enables composition across layers, making individual components harder to isolate, and (3) the vocabulary size and sequence-level computation introduce combinatorial complexity not present in image classification. Prior analysis of attention heads either averaged weights over all heads at a given position or focused only on maximum attention weights, neither accounting for the varying importance of individual heads.

**The core challenge is: how to develop a rigorous mathematical framework that decomposes transformer computations into interpretable, composable circuits, enabling mechanistic understanding of the algorithms transformers learn.**

---

## Problem Solutions

The paper introduces a mathematical framework for understanding transformers by exploiting their extensive linear structure. The key insight is that if one freezes the attention patterns (the only nonlinear component), the entire transformer becomes a linear map from token embeddings to output logits -- and this map can be decomposed into a sum of interpretable terms corresponding to end-to-end "paths" through the model. The solution rests on three pillars:

1. **The residual stream as a shared communication channel.** All transformer layers read from and write to the same high-dimensional residual stream via linear projections. The residual stream at any point is the sum of the original embedding and all prior layer outputs, enabling clean additive decomposition. It has no privileged basis -- one could rotate it by rotating all interacting matrices without changing model behavior.

2. **Attention heads as pairs of independent low-rank circuits.** Each attention head performs two separable computations: a QK circuit (W_Q^T W_K) that determines the attention pattern, and an OV circuit (W_O W_V) that determines what information is moved when a token is attended to. Keys, queries, and values are superficial intermediary byproducts; the fundamental objects are the low-rank bilinear forms W_QK and W_OV.

3. **Composition of attention heads across layers.** In multi-layer models, the output of one head can feed into the query, key, or value computation of a later head, creating Q-composition, K-composition, and V-composition. This enables multi-step algorithms that no single head can implement, most notably **induction heads** -- two-head circuits implementing a basic form of in-context learning.

---

## Approach Details

### Method

The framework studies **attention-only transformers** -- autoregressive, decoder-only transformers with MLP layers, layer normalization, and biases removed. This simplification preserves the core attention mechanism while making the model fully amenable to linear-algebraic analysis (layer norm can be merged into adjacent weights up to a constant scalar; biases in attention-only models mostly multiply out to biases on the logits).

The central mathematical tool is **tensor product notation**. A single attention head's output is written as:

> h(x) = (A ⊗ W_OV) x

where A = softmax(x^T W_Q^T W_K x) is the attention pattern matrix, W_OV = W_O W_V is the combined output-value matrix, x is the matrix of residual stream vectors, and (A ⊗ W) x denotes A acting on the position dimension while W acts on the vector-per-token dimension. The mixed product property (A ⊗ B)(C ⊗ D) = (AC) ⊗ (BD) enables clean composition across layers.

**Zero-layer transformer.** The complete logit map is simply:

> T = W_U W_E

This can only approximate bigram log-likelihoods, since no information moves between positions. The paper notes an analogy to Levy & Goldberg (2014)'s observation that early word embeddings approximate matrix factorizations of log-likelihood matrices. In larger models, the W_U W_E term fills in residual bigram statistics not captured by other terms (e.g., "Barack" → "Obama").

**One-layer transformer decomposition.** The path expansion yields:

> T = Id ⊗ W_U W_E + Σ_h A^h ⊗ (W_U W^h_OV W_E)

The first term is the **direct path** (bigram statistics). Each attention head term separates into two [n_vocab, n_vocab] matrices: the QK circuit W_E^T W^h_QK W_E (attention score for every query-key token pair) and the OV circuit W_U W^h_OV W_E (effect of each attended-to token on output logits). Together, these implement **skip-trigrams** of the form [source]...[destination][out].

**Two-layer transformer decomposition.** Adding a second layer introduces composition terms:

> T = Id ⊗ W_U W_E + Σ_h A^h ⊗ (W_U W^h_OV W_E) + Σ_{h2,h1} (A^{h2} A^{h1}) ⊗ (W_U W^{h2}_OV W^{h1}_OV W_E)

The third term represents **virtual attention heads** from V-composition: the composed attention pattern A^{h2} A^{h1} and composed OV matrix W^{h2}_OV W^{h1}_OV define a new effective head. Q-composition and K-composition also occur but affect the attention patterns of second-layer heads rather than creating separable virtual heads. The QK circuit for a second-layer head expands into a 6-dimensional tensor (a (4,2)-tensor) with terms of the form A_q ⊗ A_k ⊗ W, where A_q describes query-side information movement, A_k describes key-side information movement, and W describes how they produce attention scores.

### Key Technical Components

**QK circuit (W_Q^T W_K):** Determines the attention pattern. The full QK circuit in token space, W_E^T W_QK W_E, reveals which token pairs have high mutual attention. Positive eigenvalues indicate the head attends to tokens with similar features; negative eigenvalues indicate dissimilar-feature attention.

**OV circuit (W_O W_V):** Determines how attended-to tokens affect output logits. The full OV circuit W_U W_OV W_E maps source tokens to logit changes at the destination. The eigenvalue decomposition M = USV = W_OV gives: right singular vectors V describe which subspace of the residual stream is "read in," and left singular vectors U describe which subspace results are "written to." Heads where this circuit has large positive eigenvalues are **copying heads** (attending to a token increases that token's logit). The paper finds that positive eigenvalues are a useful (though imperfect) summary statistic for copying: matrices with all positive eigenvalues map some tokens to increasing their own logits "on average," but non-orthogonal eigenvectors can create pathological exceptions.

**Three types of composition:**
- **Q-composition:** Output of a layer-1 head feeds into the query of a layer-2 head, modifying *what* the layer-2 head looks for.
- **K-composition:** Output of a layer-1 head feeds into the key of a layer-2 head, modifying *how* tokens advertise themselves to the layer-2 head.
- **V-composition:** Output of a layer-1 head feeds into the value of a layer-2 head, creating virtual attention heads with composed attention patterns and OV maps.

Q- and K-composition affect attention patterns (more expressive than reducible operations), while V-composition composes information movement (creating separable virtual heads).

**Induction heads:** The central algorithmic discovery. An induction head is a two-head circuit in a two-layer model implementing the pattern [a][b]...[a] → [b]:
1. A **previous token head** in layer 1 attends to the immediately preceding position and copies its identity into the residual stream at each position.
2. An **induction head** in layer 2 uses K-composition so that its keys encode "what token preceded me" (from the layer-1 output). Its queries encode "what is the current token." When the current token [a] matches a previous token [a], the induction head attends to the position *after* that previous [a] and copies the next token [b] forward via its OV circuit.

The minimal mechanism creates a term Id ⊗ A^{h_{-1}} ⊗ W in the QK circuit, where A^{h_{-1}} is the previous token attention pattern and W is a "same matching" matrix (positive eigenvalues). This algorithm is verified on **completely random repeated token sequences** (totally off-distribution), confirming that induction heads do not rely on learned statistics but implement a genuine pattern-matching algorithm. The paper also notes that in other 2-layer models, some induction circuits use heads attending to "the last several tokens" rather than just the previous token, creating A^{h_{-1}} ⊗ A^{h_{-2}} ⊗ W terms for matching further back.

**Skip-trigram "bugs":** Because one-layer skip-trigrams are in factored form between QK and OV, the model cannot capture arbitrary three-way interactions. If a single head encodes both "keep...in → mind" and "keep...at → bay," it must also increase probability of "keep...in → bay" and "keep...at → mind." The paper presents this as an early demonstration of using interpretability to understand model failures.

**Superposition and residual stream bandwidth:** The residual stream has far fewer dimensions than the total number of computational dimensions. A single MLP layer typically has 4x more neurons than the residual stream has dimensions. At layer 25 of a 50-layer transformer, 100x more neurons precede the residual stream than it has dimensions, trying to communicate with 100x more neurons after it. The paper calls residual stream vectors "bottleneck activations" and expects them to be unusually challenging to interpret. There are hints that some MLP neurons and attention heads perform "memory management," reading information from the residual stream and writing out its negation.

**Composition measurement:** The degree of composition between two heads is measured by the Frobenius norm of the product of relevant matrices, divided by the norms of the individual matrices. For K-composition: ||W^{h2}_QK W^{h1}_OV||_F / (||W^{h2}_QK||_F ||W^{h1}_OV||_F). The expected value for random matrices of the same shapes is subtracted as a baseline.

**Term importance analysis:** An ablation algorithm measures the marginal loss effect of nth-order terms (paths through V-composition of n attention heads). The procedure freezes attention patterns from a forward pass, then iteratively replaces head outputs with saved values to limit path depth. Differences in observed loss between ablations give the marginal effect of each order.

### Experimental Setup

- **Models:** Custom attention-only transformers with 0, 1, and 2 layers, trained on a standard language modeling corpus. The paper does not use standard pretrained models (GPT, BERT) but trains custom attention-only models to enable clean mathematical analysis. Models use ~50,000 token vocabularies. Specific configurations analyzed include a 12-head model with d_head=64 and a 32-head model with d_head=128 for one-layer analysis, and a model with specific layer-1 and layer-2 heads for two-layer analysis.
- **Position encoding:** A mechanism similar to shortformer that does not place positional information into the residual stream (similar to rotary attention in this property).
- **Analysis methods:** Eigenvalue decomposition of QK and OV circuits to classify head behavior; ablation studies using the term importance algorithm; Frobenius norm-based composition measurement; direct inspection of expanded weight matrices (QK and OV circuits in token space).
- **Evaluation:** Language modeling loss (cross-entropy).
- **Reproducibility:** No code or model weights are publicly released. Training corpus, learning rate, number of training steps, and hardware are not specified in the source material. Random seeds are not reported. The mathematical framework itself is reproducible from the equations, but the specific empirical observations (eigenvalue distributions, composition scores, ablation numbers) depend on unreleased model weights.

### Key Results

**Copying behavior in one-layer models** (single 12-head model with d_head=64, no variance across seeds reported — limited evidence for the specific 10/12 count):

| Metric | Result |
|---|---|
| Heads with significantly positive OV eigenvalues (copying) | 10 out of 12 |
| Behavior | Most heads dedicate enormous capacity to copying: OV circuit maps attended-to token to increased probability of the same token |

The analysis also reveals that attention heads implement diverse skip-trigrams beyond copying, including language-specific patterns (Python syntax, LaTeX commands, HTML entities, URL schemes, English phrases like "keep...at → bay"), and a class of heads handling tokenization edge cases (words split differently with/without preceding space).

**Composition in two-layer models** (single two-layer model, composition diagram initially had a bug that was later corrected — limited evidence, single model):

In the analyzed two-layer model, the composition analysis (after correction) shows:
- **K-composition** is the dominant form, primarily between one previous token head in layer 1 and several induction heads in layer 2.
- Additional K-composition exists with a head attending to the last several tokens (revealed by the corrected composition diagram).
- **V-composition** (virtual attention heads) has small marginal effect in this model.
- **Q-composition** is not significant in this particular model.
- Most second-layer heads are not involved in substantive composition and function as additional skip-trigram heads.

**Induction head verification** (multiple lines of evidence in a single model — moderate-to-strong evidence for the mechanism, though limited to one model size/configuration):

Induction heads are verified via multiple lines of evidence:
- Attention patterns on natural text (Harry Potter) show off-diagonal lines corresponding to attending to previous occurrences of the current token.
- On **completely random repeated token sequences**, induction heads correctly attend to the token following the previous copy (the strongest test, as no distributional statistics apply).
- Both QK and OV eigenvalue summary statistics place all induction heads in the extreme positive corner: QK circuits show "same matching" (positive eigenvalues from K-composition term) and OV circuits show copying (positive eigenvalues).

**Term importance by path order** (single model, single ablation procedure with frozen attention patterns — limited evidence):

The ablation-based term importance analysis shows that second-order virtual attention head terms (V-composition) contribute minimally. The paper concludes that for understanding two-layer attention-only models, one should focus on individual attention head terms (especially second-layer heads) and the direct path, rather than virtual heads. This conclusion applies specifically to the OV circuit; it does not rule out the importance of Q- and K-composition, which are indeed crucial for induction heads.

---

## Limitations and Failure Modes

- **Attention-only models exclude MLPs.** MLPs constitute approximately two-thirds of parameters in standard transformers and are entirely excluded from the analysis. The authors explicitly acknowledge this as a "very dramatic simplification" and "a major weakness of our work." MLP neurons have been much harder to develop hypotheses for, with the exception of neurons at ~5% depth which often respond to clusters of short phrases with similar meanings. The paper speculates this difficulty may be due to superposition.
- **Small model scale.** The analysis focuses on models with 0-2 layers. The combinatorial explosion of paths in deeper models makes exhaustive decomposition infeasible. Whether the identified circuits remain dominant in large-scale models is left as an open question (partially addressed by the follow-up induction heads paper).
- **Frozen attention patterns assumption.** The linear decomposition assumes frozen attention patterns. In practice, attention patterns depend on the input via softmax, and the interaction between the nonlinear softmax and the linear structure is not fully captured.
- **Composition diagram bug.** A bug in an underlying library for low-rank matrix computations affected the attention head composition diagram. Instead of computing ||W^{h2T}_Q W^{h2}_K W^{h1}_O W^{h1}_V||_F, the code computed a permuted product. The corrected diagram reveals more composition than originally reported, including additional heads composing with a "last several tokens" head. The original K-composition finding with the previous token head remains valid, but the quantitative picture of composition was incomplete.
- **Eigenvalue summary statistic limitations.** The paper uses positive eigenvalues as evidence for copying behavior but acknowledges this is imperfect. Matrices with all positive eigenvalues can still map some individual tokens to decreasing their own logits due to non-orthogonal eigenvectors. The paper states they are "not confident that the eigenvalue summary statistic... is the best possible summary statistic for detecting 'copying' or 'matching' matrices."
- **Enormous expanded weight matrices.** Even for one-layer models, the expanded OV and QK matrices have ~2.5 billion entries (50,000 x 50,000). The paper describes the result as a "compressed Chinese room" where algorithmic mystery is stripped away but the model is too large to hold in one's head. Further work on summarization techniques is needed.
- **No direct applicability to encoder or bidirectional models.** All analysis uses autoregressive, decoder-only transformers. The paper briefly speculates about how induction heads might manifest in bidirectional models but does not analyze them.

#### Scope and Comparability

- **What was not tested:** Standard pretrained models (GPT-2, BERT, GPT-3) are not analyzed; all experiments use custom-trained attention-only transformers. Models with MLP layers (which constitute ~2/3 of standard transformer parameters) are excluded. Models beyond 2 layers are not studied. Encoder-only and encoder-decoder architectures are not addressed. Non-English data is not discussed. No models larger than ~50K vocabulary are analyzed. No comparison with standard interpretability methods (probing, attention rollout with MLP contributions, gradient-based attribution) is provided.
- **Comparability notes:** The attention-only transformer is a non-standard architecture that removes MLPs, biases, and layer normalization — results may not transfer directly to standard transformers. The paper's composition measurements use Frobenius norm ratios corrected against random baselines, which differs from alternative composition metrics in subsequent work. The ablation procedure freezes attention patterns (removing nonlinearity) and measures loss in nats, which is not directly comparable to perplexity-based evaluations. The "previous token head" and "induction head" terminology is introduced here and adopted by subsequent work (e.g., Olsson et al., 2022), but the exact definitions are specific to attention-only models and may require adaptation for models with MLPs that can also shift positional information.

---

## Conclusions

### Contributions

1. **Mathematical framework decomposing transformers into interpretable paths.** By exploiting the linear structure of the residual stream and the additive nature of attention heads, the paper shows that transformer computations (with frozen attention patterns) decompose into a sum of end-to-end paths, each corresponding to an interpretable operation: direct path (bigrams), individual heads (skip-trigrams), and composed heads (virtual attention heads) (path expansion sections).

2. **QK/OV circuit decomposition of attention heads.** The paper demonstrates that each attention head implements two independent low-rank circuits: W_QK determines the attention pattern (which tokens attend to which) and W_OV determines the effect of attention (what information is transferred). These can be analyzed independently via eigenstructure to classify head behavior (Attention Heads as Information Movement section).

3. **Discovery of induction heads.** The paper identifies and mechanistically explains induction heads -- two-head circuits using K-composition to implement in-context pattern matching [a][b]...[a] → [b]. This provides a concrete example of a learned algorithm that requires compositional depth: it cannot be implemented by a single attention head (Induction Heads section).

4. **Residual stream as communication channel.** The paper establishes a conceptual framework where the residual stream is a shared high-dimensional communication channel with no privileged basis, through which all components communicate via linear read/write operations. This additive structure is what enables the path decomposition (Virtual Weights and the Residual Stream section).

5. **Complete characterization of 0- and 1-layer models.** Zero-layer models are shown to approximate bigram log-likelihoods. One-layer models are reduced to an ensemble of bigram and skip-trigram models, with all parameters contextualized as functions over tokens that can be directly read from weights (Zero-Layer and One-Layer sections).

6. **Term importance analysis method.** The paper introduces an ablation algorithm for measuring the marginal contribution of nth-order composition terms, enabling empirical verification of which composition types matter in practice (Term Importance Analysis section).

### Implications

1. **Mechanistic interpretability of transformers is tractable for attention-based circuits.** Even in the presence of MLP layers, attention heads operate on the residual stream and can interact directly with each other and embeddings. Interpretable attention-only circuits exist within larger models. [Inference: the paper demonstrates this for toy models; the extent of tractability in production-scale models requires further validation.]

2. **Compositional depth enables qualitatively different algorithms.** The transition from one-layer (look-up tables of skip-trigrams) to two-layer (algorithmic pattern matching via induction heads) suggests that depth does not merely add capacity but enables fundamentally new computational strategies. [Inference: this is demonstrated for the specific case of induction heads; whether other qualitative transitions occur at greater depths is speculative.]

3. **Superposition is a central challenge for interpretability.** The mismatch between residual stream dimensions and computational dimensions suggests that representations are stored in superposition, making the residual stream a bottleneck activation that is challenging to interpret directly. [Inference: the paper identifies this as a problem but does not resolve it; subsequent work on toy models of superposition elaborated on this hypothesis.]

4. **Attention head composition is sparse in small models.** Most second-layer heads in the analyzed model do not participate in substantive composition, functioning instead as additional skip-trigram heads. Induction heads represent a specific, powerful use of composition that "outcompetes" potential alternatives. [Inference: whether composition remains sparse in larger models is unknown.]

---

## Key Claims

1. **Attention heads implement two independent circuits.** The QK circuit (W_Q^T W_K) determines the attention pattern and the OV circuit (W_O W_V) determines the effect of attending. These are separable: the QK circuit is a bilinear form over residual stream vectors, while the OV circuit is a linear map (Attention Heads as Information Movement section). This is a mathematical identity that holds for all attention-only transformers by construction (strong evidence — analytical proof, not empirical). **Status: supported.**

2. **One-layer attention-only transformers implement skip-trigrams.** The path expansion decomposes a one-layer model into a direct path (bigrams via W_U W_E) and per-head skip-trigram terms (A^h ⊗ W_U W^h_OV W_E), with QK and OV circuits directly readable from weights as [n_vocab, n_vocab] matrices (One-Layer section, path expansion). Analytical result verified by direct weight inspection on a single 12-head model (strong evidence for mathematical claim; single model for empirical patterns). **Status: supported.**

3. **Most one-layer attention heads are copying heads.** 10 out of 12 heads in the analyzed model have significantly positive eigenvalues in the OV circuit, consistent with copying behavior where attending to a token increases that token's logit (Detecting Copying Behavior section, eigenvalue histogram). Single model configuration, no variance across seeds or model sizes reported (limited evidence — one model, one training run). **Status: supported.**

4. **Induction heads in two-layer models implement in-context pattern completion via K-composition.** A previous token head in layer 1 composes with induction heads in layer 2 through K-composition: keys encode "what token preceded me," queries encode "what is the current token," implementing [a][b]...[a] → [b]. Verified on completely random repeated sequences (Induction Heads section, random token experiments). Multiple lines of evidence: natural text attention patterns, random token sequences, composition score analysis, QK/OV eigenvalue analysis (strong evidence for this model). **Status: supported.**

5. **Induction heads require at least two layers of attention.** The induction algorithm depends on K-composition between two heads across layers. No single head can simultaneously shift keys by one position and match them to the current token (Induction Heads section, mechanistic analysis). Analytical argument from the structure of K-composition (strong evidence — mechanistic proof for attention-only models). **Status: supported.**

6. **V-composition has small marginal effect in the analyzed two-layer model.** The term importance ablation shows that virtual attention head terms (second-order paths through V-composition) contribute minimally to loss reduction (0.3 nats vs. 5.2 nats for Order 1), while individual head terms (especially second-layer) dominate. K-composition is the important form of composition (Term Importance Analysis section). Single model, single ablation procedure with frozen attention patterns (limited evidence — one model, one evaluation method). **Status: supported.**

7. **The residual stream is a linear communication channel with no privileged basis.** All transformer components communicate through the residual stream via linear read/write operations. The stream is the sum of all prior outputs and the original embedding, enabling path decomposition. One could rotate it arbitrarily without changing model behavior (Virtual Weights and the Residual Stream section). Analytical property of the architecture (strong evidence — follows from linear algebra of residual connections). **Status: supported.**

---

## Open Questions

1. **How can the framework be extended to include MLP layers?** MLP layers constitute approximately two-thirds of standard transformer parameters. The paper explicitly identifies this as its major weakness. MLP neurons are harder to interpret, possibly due to superposition. MLP layers have a "fairly clean" mechanistic story (path expansion of pre-activations yields W^m_I W_E + Σ_h A^h ⊗ W^m_I W^h_OV W_E), but progress requires individually interpretable neurons. Not fully resolved; subsequent work on superposition (Toy Models of Superposition) and sparse autoencoders has made partial progress.

2. **Do induction heads and the circuits framework scale to large models?** The paper analyzes only 0-2 layer models. Addressed by Olsson et al. (2022) (`2022-03-in-context-learning-induction-heads`), which shows induction heads are present in large models and are a key driver of in-context learning, with K-composition with a previous token head as the basic building block -- the same mechanism identified here.

3. **How does superposition affect residual stream interpretability?** The residual stream has far fewer dimensions than computational dimensions (neurons, head results), creating extreme bandwidth pressure. The paper labels residual stream vectors "bottleneck activations" and predicts they will be unusually challenging to interpret. Not fully addressed; subsequent work on Toy Models of Superposition (Elhage et al., 2022) elaborated on the phenomenon.

4. **Can skip-trigram "bugs" from factored QK/OV representation be quantified?** The factored form means heads encoding "keep...in → mind" and "keep...at → bay" must also increase "keep...in → bay." The paper asks how much performance these bugs cost but does not investigate further. Not addressed by subsequent work in this directory.

5. **What is the right formalization of "copying" in OV circuits?** The paper uses positive eigenvalues as a summary statistic but acknowledges limitations (non-orthogonal eigenvectors create edge cases). Alternative approaches (diagonal entries, top-k self-prediction frequency) are mentioned but none is identified as fully robust. Not definitively resolved.

---

## Core References and Why They Are Referenced

### Mechanistic Interpretability Foundations

- **Olah et al. (2020)** -- *Zoom In: An Introduction to Circuits.* Introduces the Circuits framework for mechanistic interpretability, originally applied to vision models (InceptionV1). The transformer circuits paper extends this framework to attention-based architectures, adapting the goal of identifying interpretable features and circuits to the linear structure of the residual stream.

- **Olah et al. (2017)** -- *Feature Visualization.* Foundational work on understanding what individual neurons compute via optimization. The transformer circuits paper builds on this tradition but notes that the approach must be significantly rethought for transformers due to attention, the residual stream, and bilinear forms.

### Transformer Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer with multi-head self-attention, the residual stream, and the query-key-value decomposition that the mathematical framework reinterprets. The paper shows the standard "concatenate and multiply" formulation is mathematically equivalent to independently additive heads.

- **Radford et al. (2019)** -- *Language Models are Unsupervised Multitask Learners (GPT-2).* Demonstrates that autoregressive transformers can learn diverse capabilities from unsupervised pre-training. The transformer circuits paper seeks to mechanistically explain how such capabilities are implemented.

### Attention Analysis

- **Clark et al. (2019)** -- *What Does BERT Look At? An Analysis of BERT's Attention.* Early work analyzing attention patterns in transformers, identifying syntactic and positional heads. The mathematical framework provides a more rigorous basis for understanding why such patterns arise from QK/OV circuit structure.

- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting.* Identifies specialized head types (positional, syntactic, rare-word) in encoder models. The paper notes that Voita et al.'s rare-word heads might be similar to the skip-trigram heads it identifies.

### In-Context Learning

- **Brown et al. (2020)** -- *Language Models are Few-Shot Learners (GPT-3).* Demonstrates in-context learning in large models. The transformer circuits paper provides a mechanistic explanation via induction heads, at least in small models.

### Attention Criticism

- **Jain & Wallace (2019)** -- *Attention is not Explanation.* Critiques naive interpretation of attention weights as explanations. The framework offers a typology of ways attention interpretation can be misleading: Q-, K-, and V-composition create higher-order terms that don't map to naive attention pattern reading. Induction heads exemplify this: their attention pattern is informative, but understanding requires recognizing K-composition with a previous token head.

### Mathematical Foundations

- **Levy & Goldberg (2014)** -- *Neural Word Embedding as Implicit Matrix Factorization.* Shows word embeddings approximate factorizations of log-likelihood matrices. The paper draws an analogy: the zero-layer transformer T = W_U W_E similarly factorizes bigram statistics.

- **Dong et al. (2021)** -- *Attention is not All You Need.* Considers paths through self-attention networks, deriving the same structure found in the path expansion of logits. The paper acknowledges that many of its mathematical observations are not individually novel but are leveraged in a new way for mechanistic interpretability.
