# In-context Learning and Induction Heads

**Authors:** Catherine Olsson, Nelson Elhage, Neel Nanda, Nicholas Joseph, Nova DasSarma, Tom Henighan, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Scott Johnston, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah (Anthropic)
**Date:** March 2022, Transformer Circuits Thread (arXiv:2209.11895)

---

## Core Research Problem

Large transformer language models exhibit **in-context learning**: tokens later in the context are easier to predict than tokens earlier in the context, and this ability can be leveraged for few-shot task adaptation without weight updates. While in-context learning was compellingly demonstrated in GPT-3 (Brown et al., 2020) and studied in terms of scaling laws by Kaplan et al. (2020), the **internal mechanism** responsible for this capability was unknown. Prior work by Elhage et al. (2021) on mechanistic interpretability of transformers identified "induction heads" -- attention heads that complete token sequences like `[A][B]...[A]` -> `[B]` -- in small 2-layer attention-only models, but it was unclear whether these simple circuits could account for the much richer in-context learning behavior observed in large models with hundreds of layers and billions of parameters. The presence of MLP layers and many-layer composition makes it much harder to mathematically pin down precise circuitry in large models. The core challenge is: **determining whether induction heads constitute the mechanism for the majority of all in-context learning in large transformer models, and if so, how a simple pattern-completion circuit generalizes to implement abstract in-context behaviors.**

---

## Problem Solutions

The paper presents preliminary and indirect evidence for the hypothesis that induction heads might constitute the mechanism for the majority of all in-context learning in large transformer models. The key idea is that induction heads perform **"fuzzy" or "nearest neighbor" pattern completion**, completing `[A*][B*]...[A]` -> `[B]` where `A*` ≈ `A` and `B*` ≈ `B` in some abstract embedding space.

The solution is built on six complementary lines of evidence:

1. **Macroscopic co-occurrence:** Induction heads form during an abrupt "phase change" early in training, at precisely the same point where in-context learning dramatically improves.
2. **Macroscopic co-perturbation:** Modifying the architecture to shift when induction heads can form causes the improvement in in-context learning to shift in a precisely matching way.
3. **Direct ablation:** Knocking out induction heads at test-time in small models greatly decreases in-context learning.
4. **Specific examples of generality:** Induction heads in large models implement sophisticated behaviors including literal copying, translation, and abstract pattern matching.
5. **Mechanistic plausibility:** The reverse-engineered mechanism of induction heads (OV copying circuit + QK prefix-matching circuit via K-composition) naturally generalizes to more abstract pattern matching.
6. **Continuity from small to large models:** All measurements are smoothly continuous across model scales, suggesting the same mechanism operates at all sizes.

---

## Approach Details

### Method

The paper defines **in-context learning** following Kaplan et al. (2020) as decreasing loss at increasing token indices, and operationalizes it with a simple heuristic:

> **In-context learning score** = Loss(token 500) - Loss(token 50), averaged over dataset examples.

This score is negative when the model predicts later tokens better than earlier ones.

An **induction head** is formally defined as an attention head exhibiting two properties on repeated random token sequences:

1. **Prefix matching:** The head attends back to previous tokens that were followed by the current and/or recent tokens.
2. **Copying:** The head's output increases the logit corresponding to the attended-to token.

These properties are measured empirically using dedicated head activation evaluators on repeated sequences of 25 random tokens (repeated 4 times). In practice, induction heads form a clear cluster of heads exhibiting both properties with much greater than random chance.

The paper studies 34 decoder-only transformer language models over the course of training, including more than 50,000 attention head ablations.

### Key Technical Components

#### Smeared Key Architecture

To test whether induction heads are the minimal mechanism for in-context learning (Argument 2), the authors introduce a "smeared key" modification. Standard transformers require two layers for induction heads because the key vector must contain information about the preceding token, which requires composition of attention heads across layers. The smeared key architecture bypasses this requirement:

> k_j^h = σ(α^h) k_j^h + (1 - σ(α^h)) k_{j-1}^h

where α^h is a trainable real parameter per head h, and σ(α^h) ∈ [0,1] interpolates between the key for the current token and the previous token. This allows a single attention layer to implement induction heads.

**Results:** With smeared keys, one-layer models undergo a phase change (which they never do in the standard architecture), and two-layer models undergo the phase change earlier. This confirms the prediction that induction heads are the minimal mechanism for the large improvement in in-context learning.

#### Ablation Methodology

The paper uses **pattern-preserving ablation** rather than full ablation:

1. Run the model once, saving all attention patterns.
2. Run the model a second time, replacing the ablated head's result vector with a zero vector while forcing all attention patterns to match the first run.

This preserves a head's contribution to later heads' attention patterns while removing its contribution to output vectors. In attention-only models, this is equivalent to subtracting all terms containing the ablated head from the output logits.

#### Mechanistic Reverse Engineering (from prior work)

Induction heads consist of two attention heads in different layers working together:

- **Previous token head** (layer 0): Copies information from each token into the next token's representation via its OV circuit.
- **Induction head** (layer 1+): Uses K-composition with the previous token head to create a QK-Circuit term of the form:

> Id ⊗ h_prev ⊗ W

where W has positive eigenvalues. This term causes the induction head to compare the current token with every earlier position's preceding token and attend where they match.

**Copying** is implemented by the OV circuit having a "copying matrix" with positive eigenvalues, causing the head to increase the logit of the token it attends to.

An alternative "pointer-arithmetic" mechanism exists in GPT-2, where the earlier head's W_OV circuit copies the positional embedding of a previous copy of the current token, and the induction head uses Q-composition to rotate that position forward by one.

#### Per-Token Loss Analysis

To visualize how models evolve during training, the authors apply PCA to "per-token loss vectors": for each model snapshot, they collect log-likelihoods on a consistent set of 10,000 random tokens (one per example sequence), forming a vector that is then projected onto the first two principal components computed jointly across all snapshots of all models. This reveals that training trajectories **pivot orthogonally** during the phase change -- the primary deviation from models' basic training trajectory.

### Experimental Setup

**Model series (34 models total across 4 series):**

| Series | Layers | Parameters | MLPs | Notes |
|---|---|---|---|---|
| Small attention-only | 1--6 | -- | No | d_model = 768, 12 heads/layer |
| Small with MLPs | 1--6 | -- | Yes | d_model = 768, 12 heads/layer |
| Full-scale | 4--40 | 13M--13B | Yes | d_model = 128 * n_layer |
| Smeared key | 1--2 | -- | No | Same as small + smeared key modification |

**Full-scale model properties:**

| n_layer | Parameters | d_model | Heads/layer | d_head |
|---|---|---|---|---|
| 4 | 13M | 512 | 8 | 64 |
| 6 | 42M | 768 | 12 | 64 |
| 10 | 200M | 1280 | 20 | 64 |
| 16 | 810M | 2048 | 32 | 64 |
| 24 | 2.7B | 3072 | 48 | 64 |
| 40 | 13B | 5120 | 40 | 128 |

All models use a context window of 8192 tokens, a 2^16 token vocabulary, and positional embeddings similar to Press et al. (2020). Small models were trained for 10,000 steps (~10 billion tokens) with 200 snapshots saved at 50-step intervals. Full-scale models had 14--15 snapshots saved at exponential step intervals (2^5 through 2^17).

**Training data:** Filtered common crawl and internet books (described in Askell et al., 2021), including approximately 10% Python code. Small models were also trained on an alternate books-only dataset. Models trained on the same dataset saw the same examples in the same order.

**Evaluation:** 10,000 randomly-selected examples (512 tokens each), held consistent across all snapshots and models. Ablations evaluated on all examples for each training checkpoint (>50,000 total ablations across small models).

### Key Results

#### Evidence Strength by Model Class

| Claim | Small Attention-Only | Small with MLPs | Large Models |
|---|---|---|---|
| Contributes Some | Strong, Causal | Strong, Causal | Medium, Correlational & Mechanistic |
| Contributes Majority | Strong, Causal | Medium, Causal | Medium, Correlational |

#### Phase Change Characteristics (Argument 1)

During a narrow window early in training (roughly 2.5--5 billion tokens, about 1--2% of training for large models), four phenomena co-occur:

- In-context learning score improves abruptly from ~-0.15 nats to ~-0.4 nats, then remains constant for the rest of training.
- Induction heads form (prefix matching scores rise sharply).
- Loss undergoes a visible "bump" -- the only non-convex region of the training curve.
- Per-token loss PCA trajectories pivot orthogonally.

The one-layer model is the consistent exception: it shows none of these phenomena, as induction heads require composition across at least two layers. The phase change does not coincide with any scheduled hyperparameter change (learning rate warmup ends at ~1.5 billion tokens; weight decay changes at ~5 billion tokens).

#### Ablation Results (Argument 3)

In small attention-only models, **almost all in-context learning comes from induction heads**. Ablating induction heads (colored dark in the paper's plots) accounts for nearly the entire in-context learning score, while ablating most other heads slightly increases in-context learning (because removing "normal prediction" capacity leaves more room for in-context learning to show an effect). This result holds from the start of the phase change through the end of training.

In models with MLPs, ablation evidence is suggestive but less conclusive because in-context learning could also arise from interactions between MLP and attention layers.

#### Induction Head Behaviors in 13B Model (Argument 4)

| Head | Layer Depth | Copying Score | Prefix Matching Score | Behavior |
|---|---|---|---|---|
| Literal copying head | 21 / 40 | 0.89 | 0.75 | Copies repeated text sequences verbatim |
| Translation head | 7 / 40 | 0.20 | 0.85 | Translates between English, French, German |
| Pattern-matching head | 8 / 40 | 0.69 | 0.94 | Learns function from (category, item) -> label |

All three heads simultaneously satisfy the formal definition of induction head (literal copying on random sequences) while also performing their more abstract behaviors. The translation head attends along a "meandering off-diagonal" due to different word orders and token lengths across languages. The pattern-matching head allocates about 65% of its attention from colon tokens to semantically correct positions on category-labeling tasks.

#### Unexplained Curiosities

- **Constant in-context learning score across scales:** After the phase change, the in-context learning score (~0.4 nats) is nearly identical for models from 2 layers to 13B parameters. Large models gain their advantage over small models in the first ~10 tokens of context, then reduce loss by a roughly fixed additional amount. The authors interpret this as the same in-context learning being "harder" (more nats per improvement) from a lower baseline.
- **Loss derivative order inversion:** The derivative of loss with respect to log(training tokens) shows that small models improve faster than large models before the phase change, but the opposite is true after -- and this inversion coincides with the phase change.

### Limitations

- Evidence is **strong and causal** for small attention-only models but only **correlational** for large models with MLPs.
- Ablations were not performed on full-scale models due to computational cost (scales as O(N^1.33) with model size).
- The phase change co-occurrence could be driven by a shared latent variable (e.g., the model learning to compose layers through the residual stream) rather than direct causation from induction heads.
- The constant in-context learning score does not guarantee that the underlying mechanisms remain constant; later training may introduce additional mechanisms that maintain the same score from a lower baseline.
- The authors did not observe mesa-optimizers, but cannot rule out more complex mechanisms in large models.

---

## Conclusions

1. **Induction heads as the primary mechanism for in-context learning in small models:** In small attention-only transformers, ablation experiments show that induction heads account for nearly all measured in-context learning. This is strong, causal evidence that these pattern-completion circuits (`[A][B]...[A]` -> `[B]`) are the mechanistic source of the model's ability to improve predictions from context.

2. **A training phase change links induction heads to in-context learning across scales:** All multi-layer transformers undergo an abrupt phase change early in training (roughly 2.5--5 billion tokens) during which induction heads form, in-context learning dramatically improves, the loss curve shows a visible bump, and per-token loss PCA trajectories pivot. This co-occurrence is observed across 34 models spanning four architectural series from 1 to 40 layers.

3. **Architectural intervention confirms the causal role of induction heads:** The smeared key architecture, which enables induction heads in one-layer models by interpolating between current and previous token keys, causes the phase change to occur in one-layer models (where it otherwise never occurs) and earlier in two-layer models. This interventional evidence strengthens the argument beyond correlation.

4. **Induction heads in large models implement abstract pattern matching:** Induction heads in a 13B parameter model simultaneously perform literal copying on random sequences and exhibit sophisticated behaviors including translation and category-based pattern matching. These behaviors follow the form `[A*][B*]...[A]` -> `[B]` where matching is in abstract embedding space, not just token identity.

5. **The mechanism naturally generalizes through abstract representations:** The reverse-engineered QK circuit (K-composition with a previous token head, producing a term Id ⊗ h_prev ⊗ W with positive eigenvalues) implements prefix matching by comparing the current token with preceding tokens at earlier positions. When operating on abstract representations from earlier layers (where, e.g., the same word in different languages maps to similar vectors), this same mechanism naturally implements fuzzy or analogical matching.

6. **The phase change bridges mechanistic interpretability and scaling laws:** The induction head phase change is the first known case where a macroscopic property of neural network training (the loss bump, visible in aggregated loss over thousands of tokens) can be explained at the level of individual circuits. This provides a concrete link between the microscopic domain of interpretability and the macroscopic domain of scaling laws and learning dynamics.

7. **Safety-relevant implications of phase changes and in-context learning:** The abrupt formation of in-context learning ability during training demonstrates that neural network capabilities can emerge discontinuously. In-context learning allows model behavior to "change" during inference without weight updates, which is relevant to concerns about mesa-optimization and unexpected behavioral adaptation. The authors did not find evidence of mesa-optimizers; the mechanism appears to be induction heads rather than an internal optimization algorithm.

---

## Core References and Why They Are Referenced

### Foundational Framework

- **Elhage et al. (2021)** -- *A Mathematical Framework for Transformer Circuits.* The direct predecessor to this work. Introduced the mathematical decomposition of transformers into OV and QK circuits, first identified induction heads in 2-layer attention-only models, and developed the K-composition framework used throughout this paper to explain how induction heads implement prefix matching.

- **Brown et al. (2020)** -- *Language Models Are Few-Shot Learners (GPT-3).* Demonstrated emergent in-context learning and few-shot task performance in large language models. Represents the "few-shot learning" conception of in-context learning that this paper extends to a mechanistic explanation.

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Origin of the "loss at different token indices" formalization of in-context learning used throughout this paper. Also observed that 1-layer transformers do not follow the same scaling laws as deeper models, which this paper potentially explains via the absence of induction heads.

### Interpretability and Circuits

- **Cammarata et al. (2020)** -- *Thread: Circuits.* The broader Circuits research program on mechanistic interpretability of neural networks, which established the framework of studying features and circuits. Induction heads are framed as circuits in this tradition.

- **Olah et al. (2020)** -- *Zoom In: An Introduction to Circuits.* Introduced the concept of universality in circuits -- that different models develop the same features and circuits. Induction heads are presented as a universal circuit that appears across transformer models of all sizes.

### Attention Head Analysis

- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned.* Concurrent work identifying specialized attention heads (syntactic, positional, rare-word-sensitive) in NMT and showing many heads can be pruned. Referenced in Related Work as part of the literature on attention head patterns that induction heads extend to a circuit-level understanding.

- **Clark et al. (2019)** -- *What Does BERT Look At? An Analysis of BERT's Attention.* Analyzed BERT's 144 attention heads for syntactic and semantic functions. Referenced alongside Voita et al. as representative of the attention head analysis literature. The implicit hypothesis of universal attention patterns (e.g., "previous token" heads forming across models) is extended by this paper's claim that induction heads are a universal circuit.

### In-Context Learning Studies

- **O'Connor & Andreas (2021)** -- *What Context Features Can Transformer Language Models Use?* Found that preserving word order in contexts is important, consistent with the induction head hypothesis. However, some of their experiments (suggesting removing all words except nouns can improve loss) are in tension with the hypothesis.

- **Xie et al. (2021)** -- *An Explanation of In-context Learning as Implicit Bayesian Inference.* Proposed a theoretical model of in-context learning as implicit Bayesian inference using Hidden Markov Models. Found LSTMs outperform Transformers on their synthetic HMM data, which the authors attribute to HMM structure not benefiting from induction heads.

### Phase Changes and Discontinuous Behavior

- **Power et al. (2022)** -- *Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets.* Most analogous prior work on phase changes during training. The induction head phase change differs by having a mechanistic explanation at the circuit level.

- **Hubinger et al. (2021)** -- *Risks from Learned Optimization in Advanced Machine Learning Systems.* Introduced the concept of mesa-optimization, which motivated studying whether in-context learning involves an internal optimization algorithm. This paper finds that induction heads, not mesa-optimizers, are the mechanism.

### Learning Dynamics

- **Saxe et al. (2014)** -- *Exact Solutions to the Nonlinear Dynamics of Learning in Deep Linear Neural Networks.* Provided closed-form solutions for learning dynamics in linear networks, finding independent paths through the network that evolve during training (analogous to circuits). Referenced as a potential theoretical bridge between circuit-level interpretability and training dynamics.

### Training Data and Models

- **Askell et al. (2021)** -- *A General Language Assistant as a Laboratory for Alignment.* Describes the training data distribution and full-scale model architecture used in this paper.

- **Press et al. (2020)** -- *Shortformer: Better Language Modeling Using Shorter Inputs.* The small models and smeared key models use a positional embedding variant similar to this work.

### External Replications

- **Scherlis (Redwood Research)** -- Replicated induction heads in 2-layer attention-only transformers. Replacing the previous-token head's attention scores with exact previous-token attention recovered 99% of loss difference. Replacing the induction head's scores with `[A][B]...[A]` matching recovered ~65%, and including `[A][B][C]...[A][B]` -> `[C]` matching recovered an additional ~10%.

- **Lieberum (University of Amsterdam)** -- Found induction heads in GPT-2 and GPT-Neo starting in the mid-depth region using the paper's empirical criterion. For GPT-2-XL, head 20 in layer 21 appears to be an induction head; for GPT-Neo-2.7B, head 0 in layer 12.

#### Cross-References in Available Papers

- **Voita et al. (2019) (`2019-07-specialized-attention-heads-pruning`):** Referenced as [26] in this paper's Related Work section on attention head analysis. Both papers study specialized attention heads, but this paper extends the analysis from behavioral characterization to circuit-level mechanistic explanation. Voita et al.'s finding that specialized heads survive pruning is consistent with this paper's finding that induction heads are functionally important (ablating them greatly reduces in-context learning).

- **Clark et al. (2019) (`2019-08-bert-attention-analysis`):** Referenced as [27] in this paper's Related Work section. Clark et al. identified syntactic specialization in BERT's attention heads and found that heads default to attending to [SEP] when their function is not applicable. This paper's induction heads represent a different kind of specialized head -- one defined by an algorithmic pattern-completion behavior rather than a specific syntactic relation -- but both papers contribute to the broader picture of attention heads developing specialized functions without explicit supervision.
