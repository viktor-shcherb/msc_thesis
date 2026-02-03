# Transformer Feed-Forward Layers Are Key-Value Memories

**Authors:** Mor Geva, Roei Schuster, Jonathan Berant, Omer Levy (Tel-Aviv University, Allen Institute for AI, Cornell Tech)
**Date:** November 2021, EMNLP 2021, arXiv:2012.14913

---

## Core Research Problem

Transformer-based language models (Vaswani et al., 2017) rely on intertwined self-attention and feed-forward layers. While self-attention has been extensively analyzed -- with studies characterizing specialized attention heads (Voita et al., 2019), attention patterns in BERT (Clark et al., 2019), and structural properties of attention (Vig and Belinkov, 2019) -- self-attention accounts for only a third of a typical transformer's parameters (4d^2 per layer, where d is the model's hidden dimension). The remaining two-thirds of the parameter budget (8d^2 per layer) are spent on position-wise feed-forward layers, yet their function in the network remains under-explored.

Prior work by Sukhbaatar et al. (2019) noted the theoretical similarity between feed-forward layers and key-value memories, and reparameterized feed-forward parameters as persistent memory cells in the self-attention layers. However, this reparameterization experiment did not characterize what information these layers actually store or how they contribute to the model's predictions.

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

The paper establishes the key-value memory interpretation by comparing the mathematical form of feed-forward layers with neural memories. A feed-forward layer processes an input vector x in R^d as:

> FF(x) = f(x * K^T) * V

where K, V in R^{d_m x d} are parameter matrices and f is a non-linearity such as ReLU. A neural memory (Sukhbaatar et al., 2015) computes:

> MN(x) = softmax(x * K^T) * V

The only difference is the non-linearity: neural memory uses softmax (producing a normalized distribution over keys), while the standard transformer uses ReLU (producing unnormalized non-negative coefficients). The hidden dimension d_m is the number of memories in the layer. The activation m = f(x * K^T), commonly called the hidden layer, is a vector of **memory coefficients**, one per memory cell.

The paper then investigates three questions empirically: (1) what patterns do keys detect, (2) what distributions do values encode, and (3) how do individual memory cells compose to form the model's output.

### Key Technical Components

**Key pattern analysis (Section 3).** For each sampled key k^l_i (the i-th key in layer l), the authors compute the memory coefficient ReLU(x^l_j * k^l_i) for every prefix x_1, ..., x_j of every sentence in the WikiText-103 training set. The top-25 prefixes with the highest memory coefficients (called **trigger examples**) are retrieved. Human experts (NLP graduate students) then annotate these trigger examples, identifying repetitive patterns and classifying each as "shallow" (e.g., recurring n-grams) or "semantic" (e.g., recurring topic).

**Value distribution analysis (Section 4).** Each value vector v^l_i is converted into a probability distribution over the vocabulary by multiplying by the output embedding matrix E and applying softmax:

> p^l_i = softmax(v^l_i * E)

The distribution p^l_i is uncalibrated (since v^l_i is normally scaled by the input-dependent memory coefficient), but the ranking it induces is invariant to the coefficient. The **agreement rate** measures how often the value's top-ranked token matches the next token in the key's top-1 trigger example.

**Intra-layer memory composition (Section 5.1).** The feed-forward layer output is the sum of value vectors weighted by their memory coefficients plus a bias term:

> y^l = sum_i ReLU(x^l * k^l_i) * v^l_i + b^l

The paper measures (a) what fraction of the d_m = 4096 memories are "active" (non-zero coefficient) per example, and (b) how often the layer's top prediction differs from every individual memory's top prediction (zero-agreement rate).

**Inter-layer prediction refinement (Section 5.2).** The residual connection propagates information across layers:

> x^l = LayerNorm(r^l)
> y^l = FF(x^l)
> o^l = y^l + r^l

The paper tracks how often the residual's top prediction top(r^l) matches the model's final output top(o^L), and decomposes each layer's behavior into four cases: (1) the output matches the residual (residual), (2) the output matches the feed-forward layer (ffn), (3) the output matches both (agreement), or (4) the output matches neither (composition).

### Experimental Setup

**Model:** The 16-layer transformer language model of Baevski and Auli (2019), with d = 1024, d_m = 4096, and 247M parameters, trained on WikiText-103 (Merity et al., 2017) using the fairseq toolkit. The model uses adaptive softmax and adaptive input representations.

**Dataset:** WikiText-103, a collection of over 100M tokens extracted from Wikipedia. Sentences are segmented using spaCy.

**Key analysis sample:** 160 keys (10 random keys per layer x 16 layers), with top-25 trigger examples per key annotated by human experts.

**Value analysis:** Agreement rate computed across all 65,536 keys (4096 per layer x 16 layers). The 100 values with highest max(p^l_i) across all layers are analyzed in detail.

**Composition analysis:** 4,000 randomly-sampled prefixes from the validation set (not the training set, since the goal is to characterize inference-time behavior).

### Key Results

**Keys capture human-interpretable patterns:**

- Experts identified at least one pattern for every sampled key, with an average of 3.6 patterns per key.
- 65%--80% of retrieved trigger prefixes were associated with at least one identified pattern.

**Layer-wise pattern distribution:**

| Layer Range | Dominant Pattern Type | Example |
|---|---|---|
| 1--9 (lower) | Shallow (n-grams, shared last word) | k^1_449: ends with "substitutes" |
| 10--16 (upper) | Semantic (topic, relations) | k^16_1935: TV shows |

- Removing the last token from trigger examples has the largest impact on memory coefficients across all layers (10%--70% decrease), confirming that keys are strongly correlated with suffix patterns.
- In upper layers, removing the last token has less impact than in lower layers, consistent with upper-layer keys capturing semantic rather than shallow patterns.

**Value-key agreement in upper layers:**

| Layer Range | Agreement Rate (top-1 prediction) |
|---|---|
| 1--10 | ~0% |
| 11--16 | Rises to 3.5% |
| Random baseline | 0.0004% |

- The agreement rate in layers 11--16 is orders of magnitude above the random baseline (3.5% vs. 0.0004%), showing non-trivial predictive power.
- Among the 100 values with highest max(p^l_i), 97 out of 100 are in the upper layers (11--16), and 46 out of 100 have at least one trigger example agreeing with the value's top prediction.

**Intra-layer memory composition:**

| Observation | Value |
|---|---|
| Active memories per layer | 10%--50% of 4096 dimensions |
| Zero-agreement rate (layer output differs from all memories) | >= 68% across all layers |

- The number of active memories drops toward layer 10, coinciding with the transition from shallow to semantic patterns.
- In at least 68% of examples, the layer's final prediction differs from every individual memory's top prediction, demonstrating that layer outputs are compositional.
- When a single memory does agree with the layer output, 60% of cases involve common stop words ("the", "of") and 43% involve short prefixes (<5 tokens).

**Inter-layer prediction refinement:**

- Roughly a third of the model's final predictions are already determined in the bottom few layers (top(r^l) = top(o^L)).
- From layer 10 onward, the fraction of examples where the residual predicts the final output grows rapidly.
- In the vast majority of examples, the layer output matches the residual's prediction (residual + agreement cases dominate).
- When the residual's prediction does change, it rarely changes to the feed-forward layer's prediction. Instead, a "compromise" prediction emerges from composing the two distributions (composition case).
- Manual analysis of 100 random last-layer composition cases: 66 resulted in semantically distant changes (e.g., "people" -> "same"), 34 in semantically related changes (e.g., "later" -> "earlier", "gastric" -> "stomach").

### Limitations

- All experiments are conducted on a single model (16-layer, 247M parameters) trained on a single dataset (WikiText-103). Generalization to larger models, different architectures, or different tasks (e.g., BERT, machine translation) is hypothesized but not verified.
- The key pattern analysis relies on human annotation of a sample of 160 keys out of 65,536 total. Automated pattern identification is not attempted.
- The value-to-distribution projection assumes all layers operate in the same embedding space, which the authors acknowledge is a simplification. The lower layers' lack of key-value agreement may be due to embedding space misalignment rather than absence of meaningful structure.
- The analysis is limited to next-token prediction in an autoregressive language model. Encoder-only models (BERT) and sequence-to-sequence models are not examined.
- The memory coefficient is unnormalized (ReLU, not softmax), so the interpretation as a probability distribution over memories is approximate.

---

## Conclusions

1. **Feed-forward layers are key-value memories.** The first parameter matrix acts as keys that detect input patterns, and the second acts as values that store output distributions. This interpretation is mathematically grounded (the only difference from neural memory is the non-linearity) and empirically validated through pattern analysis and value-distribution projection.

2. **Keys detect human-interpretable patterns with a shallow-to-semantic gradient.** Lower-layer keys are triggered by shallow patterns (n-grams, shared suffixes), while upper-layer keys respond to semantic patterns (topics, relations). This corroborates prior findings on layer-wise feature encoding in deep contextualized models (Peters et al., 2018; Jawahar et al., 2019).

3. **Values encode next-token distributions in upper layers.** When projected onto the output vocabulary, value vectors in layers 11--16 predict the next token of their corresponding key's trigger examples at rates orders of magnitude above chance (3.5% vs. 0.0004%). This suggests upper-layer memory cells directly store input-to-output mappings.

4. **Layer outputs are compositional, not dominated by single memories.** In at least 68% of examples, the layer's prediction differs from every individual memory's prediction. Each layer combines hundreds of active memories (10%--50% of 4096 dimensions) to produce a distribution qualitatively different from any single memory.

5. **Residual connections refine predictions across layers.** The model builds its final output incrementally: roughly a third of predictions are determined in the bottom layers, with the rest refined through upper layers. Feed-forward layers act more as "veto" mechanisms -- shifting probability mass away from the residual's current top prediction -- than as direct overrides.

6. **Implications for interpretability, privacy, and architecture design.** The key-value memory framework opens avenues for automating pattern identification for interpretability, analyzing training-data memorization for privacy (white-box membership inference), and understanding when correct patterns are identified but suppressed during aggregation.

---

## Core References and Why They Are Referenced

### Neural Memory Foundations

- **Sukhbaatar et al. (2015)** -- *End-to-End Memory Networks.* Introduces the neural memory formulation (key-value pairs with softmax-weighted aggregation) that the paper shows feed-forward layers emulate.
- **Sukhbaatar et al. (2019)** -- *Augmenting Self-Attention with Persistent Memory.* Makes the analogous observation that feed-forward layers resemble key-value memories and reparameterizes them as persistent memory cells in self-attention. This paper goes further by analyzing what these memories actually store.

### Transformer Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer architecture with interleaved self-attention and feed-forward layers. Provides the mathematical formulation (Equation 1) that the paper compares to neural memory.

### Attention Analysis (Complementary Work on the Other Half of Parameters)

- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned.* Analyzes the function of self-attention heads (the other third of transformer parameters). This paper complements that work by analyzing feed-forward layers (the remaining two-thirds).
- **Clark et al. (2019)** -- *What Does BERT Look At? An Analysis of BERT's Attention.* Analyzes BERT's attention patterns. Part of the body of attention analysis work that motivates the question of what feed-forward layers do.

### Layer-Wise Representation Analysis

- **Peters et al. (2018)** -- *Deep Contextualized Word Representations.* Shows that lower layers in deep contextualized models capture syntactic features while upper layers capture semantic features. The paper's finding that lower-layer keys detect shallow patterns and upper-layer keys detect semantic patterns corroborates this.
- **Jawahar et al. (2019)** -- *What Does BERT Learn About the Structure of Language?* Provides further evidence of the shallow-to-semantic gradient across layers. Cited to support the layer-wise pattern distribution findings.
- **Tenney et al. (2019)** -- *BERT Rediscovers the Classical NLP Pipeline.* Shows that BERT layers recapitulate the classical NLP pipeline from syntax to semantics. Part of the broader evidence for layer-wise specialization.

### Model and Data

- **Baevski and Auli (2019)** -- *Adaptive Input Representations for Neural Language Modeling.* Provides the 16-layer, 247M-parameter transformer language model (trained on WikiText-103 with adaptive softmax) used in all experiments.
- **Merity et al. (2017)** -- *Pointer Sentinel Mixture Models.* Introduces the WikiText-103 dataset (100M+ tokens from Wikipedia) used for training and trigger example retrieval.

### Neuron-Level Interpretability

- **Durrani et al. (2020)** -- *Analyzing Individual Neurons in Pre-trained Language Models.* Analyzes individual neuron functionality in pretrained models. Related but operates at a finer granularity (individual neurons vs. entire memory cells/dimensions).
- **Mu and Andreas (2020)** -- *Compositional Explanations of Neurons.* Proposes compositional explanations for neuron behavior. Part of the broader neuron analysis literature that this paper extends to the memory-cell level.

#### Cross-References in Available Papers

- **Voita et al. (2019)** is analyzed in `2019-07-specialized-attention-heads-pruning`. That paper focuses on attention heads (one-third of parameters) and demonstrates that most heads are redundant while a few play specialized roles. Geva et al. (2021) complements this by analyzing feed-forward layers (two-thirds of parameters) and showing they function as pattern-detecting key-value memories. Both papers contribute to understanding the division of labor between attention and feed-forward components in transformers.
