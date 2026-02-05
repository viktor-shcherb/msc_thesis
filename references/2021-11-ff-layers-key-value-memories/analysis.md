---
title: "Transformer Feed-Forward Layers Are Key-Value Memories"
authors: "Geva, Schuster, Berant, Levy"
year: 2021
venue: "EMNLP 2021"
paper_type: conference-paper
categories: ["mechanistic-interpretability"]
scope: ["Transformer FFN layers", "knowledge storage in language models"]
benchmarks_used: []
models_introduced: []
models_evaluated: ["transformer-base"]
key_claims:
  - id: C1
    claim: "Feed-forward layers are mathematically equivalent to unnormalized key-value memories, differing from neural memory only in the non-linearity (ReLU vs softmax)"
    evidence: "Section 2, comparison of Equations 1 and 2"
    status: supported
  - id: C2
    claim: "Keys capture human-interpretable input patterns: experts identified at least one pattern for every sampled key, with an average of 3.6 patterns per key and 65-80% of trigger examples covered"
    evidence: "Section 3.2, Figure 2"
    status: supported
  - id: C3
    claim: "Lower layers (1-9) detect shallow patterns (n-grams, shared last word) while upper layers (10-16) detect semantic patterns (topics, relations)"
    evidence: "Section 3.2, Figure 2, Table 1"
    status: supported
  - id: C4
    claim: "Values in upper layers (11-16) induce output distributions that agree with key trigger patterns at 3.5%, orders of magnitude above the 0.0004% random baseline"
    evidence: "Section 4, Figure 4"
    status: supported
  - id: C5
    claim: "Feed-forward layer outputs are compositional: in at least 68% of examples, the layer's top prediction differs from every individual memory's top prediction"
    evidence: "Section 5.1, Figure 8"
    status: supported
  - id: C6
    claim: "The model refines predictions across layers via residual connections, with roughly a third of predictions determined in the bottom layers and the rest refined through upper layers"
    evidence: "Section 5.2, Figure 9"
    status: supported
  - id: C7
    claim: "When the residual's prediction changes at a layer, it rarely changes to the FFN layer's prediction; instead a compromise prediction emerges from composing the two distributions"
    evidence: "Section 5.2, Figure 11"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Analyzes the feed-forward layers of the Transformer architecture, showing they function as key-value memories"
  - target: 2019-07-specialized-attention-heads-pruning
    type: complementary
    detail: "Voita et al. analyze the function of attention heads (one-third of parameters); Geva et al. analyze feed-forward layers (the remaining two-thirds)"
  - target: 2019-08-bert-attention-analysis
    type: complementary
    detail: "Clark et al. analyze BERT's attention patterns; Geva et al. analyze the complementary FFN component"
  - target: 2021-12-transformer-circuits-framework
    type: complementary
    detail: "Both provide mechanistic interpretations of Transformer components; Elhage et al. decompose attention into QK/OV circuits while Geva et al. characterize FFN layers as key-value memories"
  - target: 2022-03-in-context-learning-induction-heads
    type: complementary
    detail: "Olsson et al. identify attention-based mechanisms for in-context learning; Geva et al. characterize the complementary role of FFN layers in storing input-output mappings"
  - target: 2025-04-retrieval-head-long-context-factuality
    type: complementary
    detail: "Wu et al. build on the FFN-stores-knowledge / attention-implements-algorithms distinction, showing retrieval heads in the attention layers specifically implement conditional copy-paste from context while FFN layers store intrinsic knowledge"
open_questions:
  - question: "Does the embedding space transform across layers, and if so, how does the interplay between FFN and attention layers drive this transformation?"
    addressed_by: null
  - question: "Do the key-value memory findings generalize beyond autoregressive language models to BERT encoders and neural translation models?"
    addressed_by: null
  - question: "Can the pattern-identification process be automated to provide scalable interpretability of FFN memories?"
    addressed_by: null
  - question: "Can memory cells facilitate white-box membership inference attacks on training data?"
    addressed_by: null
---

# Transformer Feed-Forward Layers Are Key-Value Memories

**Authors:** Mor Geva, Roei Schuster, Jonathan Berant, Omer Levy (Tel-Aviv University, Allen Institute for AI, Cornell Tech)
**Date:** November 2021, EMNLP 2021, arXiv:2012.14913

---

## Core Research Problem

Transformer-based language models (Vaswani et al., 2017) rely on intertwined self-attention and feed-forward layers. While much literature has been devoted to analyzing the function of self-attention layers -- characterizing specialized attention heads (Voita et al., 2019), BERT's attention patterns (Clark et al., 2019), and the structure of attention in language models (Vig and Belinkov, 2019) -- self-attention accounts for only a third of a typical transformer's parameters (4d^2 per layer, where d is the hidden dimension). The remaining two-thirds of the parameter budget (8d^2 per layer) are spent on position-wise feed-forward layers, yet their role in the network remains under-explored.

Sukhbaatar et al. (2019) noted the theoretical similarity between feed-forward layers and key-value memories, and reparameterized feed-forward parameters as persistent memory cells in the self-attention layers. While this reparameterization works in practice, the experiment does not characterize what information these layers actually store or how they contribute to the model's predictions.

**The core challenge is: what function do feed-forward layers serve in a transformer language model, and what information do they store?**

---

## Problem Solutions

The paper proposes that feed-forward layers operate as unnormalized key-value memories, where the first parameter matrix acts as keys and the second as values. The key contributions are:

1. **Keys capture human-interpretable input patterns.** Each key vector correlates with specific textual patterns in the training data -- shallow patterns (e.g., n-grams) in lower layers and semantic patterns (e.g., topics) in upper layers.
2. **Values represent next-token distributions.** Each value vector, when projected onto the output vocabulary, induces a distribution that correlates with the next-token distribution of the corresponding key's trigger patterns, particularly in upper layers.
3. **Memory composition and residual refinement.** The model's output is formed by first composing hundreds of active memories within each layer (intra-layer composition), then refining predictions across layers via residual connections (inter-layer refinement).

---

## Approach Details

### Method

The paper establishes the key-value memory interpretation by comparing the mathematical form of feed-forward layers with neural memories. A feed-forward layer processes an input vector x in R^d as (bias terms omitted):

> FF(x) = f(x * K^T) * V

where K, V in R^{d_m x d} are parameter matrices and f is a non-linearity such as ReLU. A neural memory (Sukhbaatar et al., 2015) computes:

> MN(x) = softmax(x * K^T) * V

The only difference is the non-linearity: neural memory uses softmax (producing a normalized distribution over keys), while the standard transformer uses ReLU (producing unnormalized non-negative coefficients). The hidden dimension d_m is the number of memories in the layer. The activation m = f(x * K^T), commonly called the hidden layer, is a vector of **memory coefficients**, one per memory cell (Section 2, Equations 1--2).

The paper then investigates three questions empirically: (1) what patterns do keys detect (Section 3), (2) what distributions do values encode (Section 4), and (3) how do individual memory cells compose to form the model's output (Section 5).

### Key Technical Components

**Key pattern analysis (Section 3).** For each sampled key k^l_i (the i-th key in layer l), the authors compute the memory coefficient ReLU(x^l_j * k^l_i) for every prefix x_1, ..., x_j of every sentence in the WikiText-103 training set. The top-25 prefixes with the highest memory coefficients (called **trigger examples**) are retrieved. Human experts (NLP graduate students) annotated these trigger examples, identifying repetitive patterns (patterns had to occur in at least 3 prefixes) and classifying each as "shallow" (e.g., recurring n-grams, shared last word) or "semantic" (e.g., recurring topic). Each key and its top-25 prefixes were annotated by one expert (Section 3.1).

**Token ablation analysis (Section 3.2).** To further quantify key sensitivity, 1,600 random keys (100 per layer) were sampled, and for each key's top-50 trigger examples, the first, last, or a random token was removed. The change in memory coefficient was measured. Removing the last token had the largest impact across all layers (10%--70% decrease), confirming keys are strongly correlated with suffix patterns. In upper layers, removing the last token has less impact, consistent with upper-layer keys capturing semantic rather than shallow patterns (Figure 3).

**Value distribution analysis (Section 4).** Each value vector v^l_i is converted into a probability distribution over the vocabulary by multiplying by the output embedding matrix E and applying softmax:

> p^l_i = softmax(v^l_i * E)

The distribution p^l_i is uncalibrated (since v^l_i is normally scaled by the input-dependent memory coefficient), but the ranking it induces is invariant to the coefficient. This conversion assumes that all layers operate in the same embedding space -- acknowledged by the authors as a simplification. In practice, the adaptive softmax of Baevski and Auli (2019) is used to compute probabilities. The **agreement rate** measures how often the value's top-ranked token (argmax(p^l_i)) matches the next token in the key's top-1 trigger example (w^l_i).

**Detecting predictive values (Section 4).** To identify values with high agreement automatically, the authors analyzed max(p^l_i) across all layers and dimensions. Values with higher maximum probabilities are more likely to agree with their key's top trigger example (Figure 6). The 100 values with highest max(p^l_i) were selected for detailed analysis.

**Intra-layer memory composition (Section 5.1).** The feed-forward layer output is the sum of value vectors weighted by their memory coefficients plus a bias term:

> y^l = sum_i ReLU(x^l * k^l_i) * v^l_i + b^l

The paper defines top(h) = argmax(h * E) as the top prediction from any vector, and measures: (a) what fraction of the d_m = 4096 memories are "active" (non-zero coefficient) per example, and (b) the **zero-agreement rate**: how often the condition top(v^l_i) != top(y^l) holds for all i (i.e., the layer's prediction differs from every individual memory's prediction).

**Inter-layer prediction refinement (Section 5.2).** The residual connection propagates information across layers (including from self-attention layers):

> x^l = LayerNorm(r^l)
> y^l = FF(x^l)
> o^l = y^l + r^l

The paper tracks how often top(r^l) = top(o^L) (the residual's top prediction matches the model's final output), and decomposes each layer's behavior into four cases: (1) **residual**: output matches the residual but not the FFN (top(o^l) = top(r^l) != top(y^l)), (2) **ffn**: output matches the FFN but not the residual (top(o^l) = top(y^l) != top(r^l)), (3) **agreement**: output matches both (top(o^l) = top(r^l) = top(y^l)), or (4) **composition**: output matches neither (top(r^l) != top(o^l) != top(y^l)). By construction, there are no cases where the residual and FFN agree but the output does not.

### Experimental Setup

**Model:** The 16-layer transformer language model of Baevski and Auli (2019), with d = 1024, d_m = 4096, and 247M parameters, trained on WikiText-103 (Merity et al., 2017) using the fairseq toolkit. The model uses adaptive softmax and adaptive input representations. The specific checkpoint is `transformer_lm.wiki103.adaptive` (Appendix B).

**Dataset:** WikiText-103, a collection of over 100M tokens extracted from Wikipedia. Sentences are segmented using spaCy (Appendix B).

**Key analysis sample:** 160 keys (10 random keys per layer x 16 layers), with top-25 trigger examples per key annotated by human experts (Section 3.1).

**Token ablation:** 1,600 keys (100 per layer), with top-50 trigger examples per key (Section 3.2).

**Value analysis:** Agreement rate computed across all 65,536 keys (4096 per layer x 16 layers). The 100 values with highest max(p^l_i) across all layers are analyzed in detail (Section 4).

**Composition analysis:** 4,000 randomly-sampled prefixes from the validation set (not the training set, since the goal is to characterize inference-time behavior) (Section 5).

### Key Results

**Keys capture human-interpretable patterns (Section 3.2):**

- Experts identified at least one pattern for every sampled key, with an average of 3.6 patterns per key.
- 65%--80% of retrieved trigger prefixes were associated with at least one identified pattern (Figure 2).

**Layer-wise pattern distribution (Section 3.2, Figure 2, Table 1):**

| Layer Range | Dominant Pattern Type | Example |
|---|---|---|
| 1--9 (lower) | Shallow (n-grams, shared last word) | k^1_449: ends with "substitutes" |
| 6 (middle) | Shallow + semantic | k^6_2546: military context, ends with "base"/"bases" |
| 10--16 (upper) | Semantic (topic, relations) | k^16_1935: TV shows |

**Token ablation (Section 3.2, Figure 3):**

| Token Removed | Impact on Memory Coefficient |
|---|---|
| Last token | 10%--70% decrease (largest impact across all layers) |
| First token | Smaller decrease |
| Random token | Intermediate decrease |

- In upper layers, removing the last token has less impact than in lower layers, supporting the finding that upper-layer keys capture semantic rather than shallow patterns.

**Value-key agreement (Section 4, Figure 4):**

| Layer Range | Agreement Rate (top-1 prediction) |
|---|---|
| 1--10 | ~0% |
| 11--16 | Rises to 3.5% |
| Random baseline | 0.0004% |

- The agreement rate in layers 11--16 is orders of magnitude above the random baseline (3.5% vs. 0.0004%).
- Among the 100 values with highest max(p^l_i), 97 out of 100 are in the upper layers (11--16), and 46 out of 100 have at least one trigger example agreeing with the value's top prediction (Section 4, Table 2).
- The rank of the next token of a trigger example in the value's distribution decreases (i.e., gets higher probability) through the layers (Figure 5).

**Example value predictions (Section 4, Table 2):**

| Value | Prediction | Precision@50 | Example Trigger |
|---|---|---|---|
| v^15_222 | "each" | 68% | "But when bees and wasps resemble each" |
| v^15_881 | "part" | 92% | "Comet served only briefly with the fleet, owing in large part" |
| v^16_2070 | "line" | 84% | "Sailing from Lorient in October 1805 with one ship of the line" |
| v^16_752 | "played" | 16% | "...where Padukone was cast as the supportive girlfriend of a depressed man (played" |
| v^13_2601 | "extratropical" | 4% | "...low pressure weather systems (large scale storms such as extratropical" |

**Intra-layer memory composition (Section 5.1):**

| Observation | Value |
|---|---|
| Active memories per layer | 10%--50% of 4096 dimensions (Figure 7) |
| Zero-agreement rate | >= 68% across all layers (Figure 8) |

- The number of active memories drops toward layer 10, coinciding with the transition from shallow to semantic patterns (Figure 7).
- In at least 68% of examples, the layer's final prediction differs from every individual memory's top prediction, demonstrating that layer outputs are compositional (Figure 8).
- When a single memory does agree with the layer output, 60% of cases involve common stop words ("the", "of") and 43% involve short prefixes (<5 tokens), suggesting very common patterns may be "cached" in individual memory cells (Section 5.1).

**Inter-layer prediction refinement (Section 5.2):**

- Roughly a third of the model's final predictions are already determined in the bottom few layers (top(r^l) = top(o^L)), growing rapidly from layer 10 onward (Figure 9).
- The probability mass assigned by the residual to the final prediction also increases monotonically through the layers (Figure 10).
- In the vast majority of examples, the layer output matches the residual's prediction (residual + agreement cases dominate) (Figure 11).
- When the residual's prediction does change, it rarely changes to the feed-forward layer's prediction. Instead, a "compromise" prediction emerges from composing the two distributions (composition case), suggesting feed-forward layers act as **"veto" mechanisms** that shift probability mass away from the residual's top prediction (Figure 11).
- Manual analysis of 100 random last-layer composition cases: 66 resulted in semantically distant changes (e.g., "people" -> "same"), 34 in semantically related changes (e.g., "later" -> "earlier", "gastric" -> "stomach") (Section 5.2).

---

## Limitations and Failure Modes

- **Single model and dataset.** All experiments are conducted on one model (16-layer, 247M parameters) trained on one dataset (WikiText-103). Generalization to larger models, different architectures (e.g., BERT, seq2seq), or different tasks is hypothesized but not verified (Section 7).
- **Small key sample for human annotation.** The key pattern analysis relies on human annotation of 160 keys out of 65,536 total (0.24%). Automated pattern identification is not attempted (Section 3.1).
- **Embedding space assumption.** The value-to-distribution projection assumes all layers operate in the same embedding space, which the authors acknowledge is a simplification. The lower layers' lack of key-value agreement may be due to embedding space misalignment rather than absence of meaningful structure (Section 4).
- **Limited to autoregressive language modeling.** The analysis is restricted to next-token prediction. Encoder-only models (BERT) and sequence-to-sequence models are not examined (Section 7).
- **Unnormalized coefficients.** The memory coefficient is unnormalized (ReLU, not softmax), so the interpretation as a probability distribution over memories is approximate. The uncalibrated probability distributions from values can only be examined by ranking, not absolute probability values (Section 2, Section 4).
- **No causal interventions.** The paper establishes correlations between keys and patterns, and between values and next-token distributions, but does not perform causal experiments (e.g., editing or ablating specific memory cells to verify their functional role).

---

## Conclusions

### Contributions

1. **Feed-forward layers are key-value memories.** The first parameter matrix acts as keys that detect input patterns, and the second acts as values that store output distributions. This interpretation is mathematically grounded (the only difference from neural memory is ReLU vs. softmax non-linearity) and empirically validated through pattern analysis and value-distribution projection (Section 2).

2. **Keys detect human-interpretable patterns with a shallow-to-semantic gradient.** Lower-layer keys (1--9) are triggered by shallow patterns (n-grams, shared suffixes), while upper-layer keys (10--16) respond to semantic patterns (topics, relations). Experts identified patterns for every sampled key, with 3.6 patterns per key on average and 65%--80% trigger example coverage (Section 3).

3. **Values encode next-token distributions in upper layers.** When projected onto the output vocabulary, value vectors in layers 11--16 predict the next token of their corresponding key's trigger examples at 3.5% agreement, orders of magnitude above the 0.0004% random baseline. 97 of the 100 most predictive values are in layers 11--16 (Section 4).

4. **Layer outputs are compositional, not dominated by single memories.** In at least 68% of examples, the layer's prediction differs from every individual memory's prediction. Each layer combines hundreds of active memories (10%--50% of 4096 dimensions) to produce a distribution qualitatively different from any single memory (Section 5.1).

5. **Residual connections refine predictions across layers.** The model builds its final output incrementally: roughly a third of predictions are determined in the bottom layers, with the rest refined through upper layers. Feed-forward layers act more as "veto" mechanisms -- shifting probability mass away from the residual's current top prediction -- than as direct overrides (Section 5.2).

### Implications

1. **Feed-forward layers store input-output mappings.** The correlation between key patterns and value distributions in upper layers suggests that individual memory cells directly store mappings from input contexts to predicted outputs, functioning as a form of learned factual storage. [Inference: the paper shows correlation, not causation; whether editing these memories can reliably modify model behavior is untested.]

2. **The framework may apply beyond language modeling.** The mathematical equivalence between FFN layers and key-value memories holds for any transformer model (BERT encoders, translation models). The authors expect qualitative findings to generalize but do not verify this empirically (Section 7).

3. **Implications for data privacy.** Memory cells that store input-output mappings could facilitate white-box membership inference attacks, as specific training examples may be identifiable through their associated memory patterns (Section 7, citing Nasr et al., 2019). [Speculative: no privacy experiments are conducted.]

4. **Potential for automated interpretability.** Automating the pattern-identification process could provide scalable interpretability methods for large transformer models (Section 7). [Speculative: the paper uses manual annotation only.]

---

## Key Claims

1. **Feed-forward layers are mathematically equivalent to unnormalized key-value memories.** The FFN computation FF(x) = f(x * K^T) * V differs from neural memory MN(x) = softmax(x * K^T) * V only in the non-linearity. The hidden dimension d_m corresponds to the number of memory cells, and the activation vector m = f(x * K^T) contains the memory coefficients (Section 2, Equations 1--2). **Status: supported.**

2. **Keys capture human-interpretable patterns.** Experts identified at least one pattern for every sampled key (160 keys, 10 per layer), with an average of 3.6 patterns per key. 65%--80% of the top-25 trigger examples were associated with at least one identified pattern (Section 3.2, Figure 2). **Status: supported.**

3. **Lower layers detect shallow patterns; upper layers detect semantic patterns.** Layers 1--9 are dominated by shallow patterns (n-grams, shared last word); layers 10--16 are characterized by semantic patterns (topics, relations). Removing the last token from trigger examples decreases memory coefficients by 10%--70%, with less impact in upper layers (Section 3.2, Figure 2, Figure 3, Table 1). **Status: supported.**

4. **Values in upper layers encode next-token distributions.** The agreement rate between value top predictions and key trigger next-tokens rises from ~0% in layers 1--10 to 3.5% in layers 11--16, compared to a 0.0004% random baseline. 97 of the 100 values with highest max(p^l_i) are in layers 11--16; 46 of these have at least one trigger example matching the value's top prediction (Section 4, Figure 4, Figure 6). **Status: supported.**

5. **Layer outputs are compositional.** In at least 68% of examples, the feed-forward layer's top prediction (top(y^l)) differs from every individual memory's top prediction (top(v^l_i)). When single memories do agree with the layer, 60% involve stop words and 43% involve short prefixes (<5 tokens) (Section 5.1, Figure 8). **Status: supported.**

6. **Predictions are refined incrementally via residual connections.** Roughly a third of the model's final predictions are determined in the bottom few layers. From layer 10 onward, the fraction of examples where top(r^l) = top(o^L) grows rapidly (Section 5.2, Figure 9). **Status: supported.**

7. **Feed-forward layers act as veto mechanisms rather than overrides.** When the residual's top prediction changes after interaction with the FFN layer, it rarely changes to the FFN's prediction. Instead, a compromise prediction emerges that equals neither (composition case). In 100 random last-layer composition examples, 66 produced semantically distant changes and 34 produced semantically related changes (Section 5.2, Figure 11). **Status: supported.**

---

## Open Questions

1. **Does the embedding space transform across layers?** The increasing key-value agreement from lower to upper layers suggests the output space may change across layers. The paper notes this transformation cannot be explained solely by FFN layers (if the model only did key-value look-ups with weighted addition, a single embedding space would be more natural) and may involve the interplay between FFN and attention layers (Section 7). Not addressed by subsequent work in this directory.

2. **Do the findings generalize beyond autoregressive language modeling?** The mathematical equivalence between FFN and key-value memory holds for any transformer, but the empirical findings (pattern types, value agreement rates, composition behavior) are demonstrated only on one LM. Verification on BERT, translation models, and larger models is explicitly left for future work (Section 7). Not directly addressed.

3. **Can pattern identification be automated?** The paper relies on human expert annotation of 160 keys. Automating this process could enable scalable interpretability (Section 7). Not addressed.

4. **Can memory cells facilitate training-data privacy attacks?** The paper raises the possibility that memory cells storing input-output mappings could enable white-box membership inference (Section 7, citing Nasr et al., 2019). Not addressed.

---

## Core References and Why They Are Referenced

### Neural Memory Foundations

- **Sukhbaatar et al. (2015)** -- *End-to-End Memory Networks.* Introduces the neural memory formulation (key-value pairs with softmax-weighted aggregation) that the paper shows feed-forward layers emulate. Provides the mathematical framework (Equation 2) for the comparison.
- **Sukhbaatar et al. (2019)** -- *Augmenting Self-Attention with Persistent Memory.* Makes the analogous observation that feed-forward layers resemble key-value memories and reparameterizes them as persistent memory cells in self-attention. Geva et al. go further by analyzing what these memories actually store.

### Transformer Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer architecture with interleaved self-attention and feed-forward layers. Provides the mathematical formulation of FFN layers (Equation 1) and the parameter budget analysis (4d^2 for attention, 8d^2 for FFN per layer).

### Attention Analysis (Complementary Work on the Other Half of Parameters)

- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned.* Analyzes the function of self-attention heads (the other third of transformer parameters). This paper complements that work by analyzing feed-forward layers (the remaining two-thirds).
- **Clark et al. (2019)** -- *What Does BERT Look At? An Analysis of BERT's Attention.* Analyzes BERT's attention patterns. Part of the body of attention analysis work that motivates the question of what feed-forward layers do.
- **Vig and Belinkov (2019)** -- *Analyzing the Structure of Attention in a Transformer Language Model.* Analyzes attention structure in a language model. Cited alongside Voita et al. and Clark et al. as prior work focused on attention.

### Layer-Wise Representation Analysis

- **Peters et al. (2018)** -- *Deep Contextualized Word Representations.* Shows that lower layers in deep contextualized models capture syntactic features while upper layers capture semantic features. The finding that lower-layer keys detect shallow patterns and upper-layer keys detect semantic patterns corroborates this.
- **Jawahar et al. (2019)** -- *What Does BERT Learn About the Structure of Language?* Provides further evidence of the shallow-to-semantic gradient across layers. Cited to support the layer-wise pattern distribution findings.
- **Tenney et al. (2019)** -- *BERT Rediscovers the Classical NLP Pipeline.* Shows that BERT layers recapitulate the classical NLP pipeline from syntax to semantics. Part of the broader evidence for layer-wise specialization.
- **Liu et al. (2019)** -- *Linguistic Knowledge and Transferability of Contextual Representations.* Further evidence that lower and upper layers capture different linguistic properties. Cited alongside Peters et al. and Jawahar et al. for the shallow-to-semantic gradient.

### Model and Data

- **Baevski and Auli (2019)** -- *Adaptive Input Representations for Neural Language Modeling.* Provides the 16-layer, 247M-parameter transformer language model (d = 1024, d_m = 4096, adaptive softmax, trained on WikiText-103 with fairseq) used in all experiments.
- **Merity et al. (2017)** -- *Pointer Sentinel Mixture Models.* Introduces the WikiText-103 dataset (100M+ tokens from Wikipedia) used for training and trigger example retrieval.

### Neuron-Level Interpretability

- **Durrani et al. (2020)** -- *Analyzing Individual Neurons in Pre-trained Language Models.* Analyzes individual neuron functionality in pretrained models. Related but operates at a finer granularity (individual neurons vs. entire memory cells/dimensions).
- **Mu and Andreas (2020)** -- *Compositional Explanations of Neurons.* Proposes compositional explanations for neuron behavior. Part of the broader neuron analysis literature that this paper extends to the memory-cell level.

### Privacy and Security

- **Nasr et al. (2019)** -- *Comprehensive Privacy Analysis of Deep Learning.* Provides the white-box membership inference attack framework that the paper's discussion section cites as a potential application of understanding memory cells.
