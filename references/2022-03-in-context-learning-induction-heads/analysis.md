---
title: "In-context Learning and Induction Heads"
authors: "Olsson, Elhage, Nanda, Joseph, DasSarma, Henighan, Mann, Askell, Bai, Chen, Conerly, Drain, Ganguli, Hatfield-Dodds, Hernandez, Johnston, Jones, Kernion, Lovitt, Ndousse, Amodei, Brown, Clark, Kaplan, McCandlish, Olah"
year: 2022
venue: "Transformer Circuits Thread (arXiv:2209.11895)"
paper_type: informal
categories: ["mechanistic-interpretability", "in-context-learning", "attention-analysis"]
scope: ["induction head mechanism", "in-context learning", "training phase changes", "attention head circuits", "training dynamics"]
benchmarks_used: []
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "Induction heads are the primary mechanism for in-context learning in small attention-only transformers, as ablating them accounts for nearly all measured in-context learning"
    evidence: "Argument 3 ablation plots, Model Analysis Table"
    status: supported
  - id: C2
    claim: "A phase change early in training (~2.5-5 billion tokens) co-occurs with induction head formation, abrupt improvement in in-context learning, a loss curve bump, and a PCA trajectory pivot across all multi-layer models studied"
    evidence: "Argument 1, Model Analysis Table across 4 model series and 34 models"
    status: supported
  - id: C3
    claim: "The smeared key architecture causes the phase change in one-layer models (where it never occurs in standard architecture) and earlier in two-layer models, confirming induction heads as the minimal mechanism for the in-context learning improvement"
    evidence: "Argument 2, smeared key model series in Model Analysis Table"
    status: supported
  - id: C4
    claim: "Induction heads in a 13B parameter model implement abstract pattern matching including translation and category-based labeling while simultaneously satisfying the formal definition of induction head on random sequences"
    evidence: "Argument 4, 13B model head analysis table (copying scores 0.20--0.89, prefix matching scores 0.75--0.94)"
    status: supported
  - id: C5
    claim: "In-context learning score (~0.4 nats) is approximately constant across model sizes from 2 layers to 13B parameters after the phase change, under varying definitions of the score"
    evidence: "Unexplained Curiosities section, in-context learning score sensitivity analysis plot"
    status: supported
  - id: C6
    claim: "The mechanism underlying in-context learning is induction heads rather than mesa-optimization; no evidence of mesa-optimizers was observed"
    evidence: "Discussion, Safety Implications section"
    status: unvalidated
cross_references:
  - target: 2021-12-transformer-circuits-framework
    type: extends
    detail: "Builds directly on the mathematical framework for transformer circuits, extending the understanding of induction heads from 2-layer attention-only models to 34 models across scales up to 13B parameters"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Studies internal circuits of the Transformer architecture, specifically induction heads formed through multi-layer attention composition in the QK and OV circuits"
  - target: 2019-07-specialized-attention-heads-pruning
    type: complementary
    detail: "Voita et al.'s finding that specialized attention heads survive pruning is consistent with induction heads being functionally important; both papers identify specialized attention head roles"
  - target: 2019-08-bert-attention-analysis
    type: complementary
    detail: "Clark et al.'s identification of syntactic head specialization in BERT complements the circuit-level understanding of induction heads; both establish that attention heads develop specialized functions"
  - target: 2021-11-ff-layers-key-value-memories
    type: complementary
    detail: "Geva et al. study feed-forward layers as key-value memories while this paper studies attention heads as pattern-completion circuits; together they characterize both major component types in transformers"
  - target: 2025-03-longiclbench-long-in-context-learning
    type: complementary
    detail: "LongICLBench measures the practical limits of ICL scaling with up to 174 classes and 50K tokens, complementing the mechanistic understanding of ICL via induction heads"
  - target: 2025-04-retrieval-head-long-context-factuality
    type: extended-by
    detail: "Wu et al. extend the concept of specialized attention heads from induction heads (pattern matching for ICL) to retrieval heads (conditional copy-paste from arbitrary context positions for long-context factuality)"
  - target: 2021-08-context-features-transformer-lm
    type: complementary
    detail: "O'Connor & Andreas find that preserving word order matters for context utilization (consistent with induction head hypothesis), but retaining only nouns can improve long-range predictions (partially in tension with the hypothesis)"
open_questions:
  - question: "Do induction heads account for the majority of in-context learning in large models with MLPs, or do additional mechanisms (other composition heads, MLP-attention interactions) contribute substantially?"
    addressed_by: null
  - question: "Why is the in-context learning score approximately constant (~0.4 nats) across model sizes after the phase change?"
    addressed_by: null
  - question: "Do other Q-composition and K-composition mechanisms form simultaneously during the phase change, and what fraction of in-context learning do they account for in large models?"
    addressed_by: null
  - question: "Why does the loss derivative order invert at the phase change, with small models improving faster before and large models improving faster after?"
    addressed_by: null
  - question: "Does the mechanism of in-context learning change over training even as the in-context learning score remains constant?"
    addressed_by: null
---
# In-context Learning and Induction Heads

**Authors:** Catherine Olsson, Nelson Elhage, Neel Nanda, Nicholas Joseph, Nova DasSarma, Tom Henighan, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Scott Johnston, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Chris Olah (Anthropic)
**Date:** March 2022, Transformer Circuits Thread (arXiv:2209.11895)
**Type:** Transformer Circuits Thread article (not a formal peer-reviewed paper)

---

## Core Research Problem

Large transformer language models exhibit **in-context learning**: tokens later in the context are easier to predict than tokens earlier in the context, and this ability can be leveraged for few-shot task adaptation without weight updates. While in-context learning was compellingly demonstrated in GPT-3 (Brown et al., 2020) and formalized in terms of loss at different token indices by Kaplan et al. (2020), the **internal mechanism** responsible for this capability was unknown.

Prior work by Elhage et al. (2021) -- *A Mathematical Framework for Transformer Circuits* -- identified "induction heads" in small 2-layer attention-only models: attention heads that complete token sequences like `[A][B]...[A]` -> `[B]` through a circuit of two attention heads (a "previous token head" and the induction head proper). For 2-layer attention-only models, induction heads were shown to be the primary source of in-context learning. However, the presence of many layers and MLP layers in large models makes it much more difficult to mathematically pin down precise circuitry. Whether these simple circuits could account for the much richer in-context learning behavior observed in models with billions of parameters remained an open question.

The core challenge is: **determining whether induction heads constitute the mechanism for the majority of all in-context learning in large transformer models, and if so, how a simple pattern-completion circuit generalizes to implement abstract in-context behaviors.**

---

## Problem Solutions

The paper presents preliminary and indirect evidence for the hypothesis that induction heads might constitute the mechanism for the majority of all in-context learning in large transformer models. The key idea is that induction heads perform **"fuzzy" or "nearest neighbor" pattern completion**, completing `[A*][B*]...[A]` -> `[B]` where `A*` is similar to `A` and `B*` is similar to `B` in some abstract embedding space.

The solution is built on six complementary lines of evidence:

1. **Macroscopic co-occurrence:** Induction heads form during an abrupt "phase change" early in training, at precisely the same point where in-context learning dramatically improves.
2. **Macroscopic co-perturbation:** Modifying the architecture to shift when induction heads can form causes the improvement in in-context learning to shift in a precisely matching way.
3. **Direct ablation:** Knocking out induction heads at test-time in small models greatly decreases in-context learning.
4. **Specific examples of generality:** Induction heads in large models implement sophisticated behaviors including literal copying, translation, and abstract pattern matching.
5. **Mechanistic plausibility:** The reverse-engineered mechanism of induction heads naturally generalizes to more abstract pattern matching when operating on abstract representations.
6. **Continuity from small to large models:** All measurements are smoothly continuous across model scales, suggesting the same mechanism operates at all sizes.

---

## Approach Details

### Method

The paper defines **in-context learning** following Kaplan et al. (2020) as decreasing loss at increasing token indices, and operationalizes it with a simple heuristic:

> **In-context learning score** = Loss(token 500) - Loss(token 50), averaged over dataset examples.

This score is negative when the model predicts later tokens better than earlier ones. The 500th and 50th token indices were chosen somewhat arbitrarily (the 500th token is near the end of a length-512 context; the 50th is far enough that basic text properties are established while still being near the start), but the authors show that varying these numbers does not change the conclusions.

An **induction head** is formally defined as an attention head exhibiting two properties on a repeated random sequence of tokens (25 random tokens repeated 4 times):

1. **Prefix matching:** The head attends back to previous tokens that were followed by the current and/or recent tokens.
2. **Copying:** The head's output increases the logit corresponding to the attended-to token.

In practice, induction heads form a clear cluster of heads exhibiting both properties with much greater than random chance. The paper studies 34 decoder-only transformer language models over the course of training, including more than 50,000 attention head ablations.

### Key Technical Components

#### Smeared Key Architecture

To test whether induction heads are the minimal mechanism for in-context learning (Argument 2), the authors introduce a "smeared key" modification. Standard transformers require two layers for induction heads because the key vector must contain information about the preceding token, which requires composition of attention heads across layers. The smeared key architecture bypasses this requirement:

> k_j^h = sigma(alpha^h) * k_j^h + (1 - sigma(alpha^h)) * k_{j-1}^h

where alpha^h is a trainable real parameter per head h, and sigma(alpha^h) in [0,1] interpolates between the key for the current token and the previous token. The key vector for the first token is unchanged.

**Results:** With smeared keys, one-layer models undergo a phase change (which they never do in the standard architecture), and two-layer models undergo the phase change earlier. This confirms the prediction that induction heads are the minimal mechanism for the large improvement in in-context learning.

#### Ablation Methodology

The paper uses **pattern-preserving ablation** rather than full ablation:

1. Run the model once, saving all attention patterns.
2. Run the model a second time, replacing the ablated head's result vector with a zero vector while forcing all attention patterns to match the first run.

This preserves a head's contribution to later heads' attention patterns while removing its contribution to output vectors. In attention-only models, this is equivalent to subtracting all terms containing the ablated head from the output logits (because with frozen attention patterns, each head's action is purely linear).

The cost of a full set of ablations scales superlinearly with model size at O(N^1.33), since there are O(N^0.33) heads and each ablation is O(N) where N is the number of parameters.

#### Mechanistic Reverse Engineering (from prior work)

Induction heads consist of two attention heads in different layers working together:

- **Previous token head** (layer 0): Copies information from each token into the next token's representation via its OV circuit.
- **Induction head** (layer 1+): Uses K-composition with the previous token head to create a QK-Circuit term of the form:

> Id (tensor product) h_prev (tensor product) W

where W has positive eigenvalues. This term causes the induction head to compare the current token with every earlier position's preceding token and attend where they match.

**Copying** is implemented by the OV circuit having a "copying matrix" with positive eigenvalues, causing the head to increase the logit of the token it attends to.

An alternative **"pointer-arithmetic" mechanism** exists in GPT-2: the earlier head's W_OV circuit copies the positional embedding of a previous copy of the current token, and the induction head uses Q-composition to rotate that position forward by one. This mechanism is not available to the models studied in this paper, as they do not add positional information into the residual stream.

#### Per-Token Loss Analysis

To visualize how models evolve during training, the authors apply PCA to "per-token loss vectors": for each model snapshot, they collect log-likelihoods on a consistent set of 10,000 random tokens (one per example sequence), forming a vector that is then projected onto the first two principal components computed jointly across all snapshots of all models. This reveals that training trajectories **pivot orthogonally** during the phase change -- the primary deviation from models' basic training trajectory.

### Experimental Setup

**Model series (34 models total across 4 series):**

| Series | Layers | Parameters | MLPs | Notes |
|---|---|---|---|---|
| Small attention-only | 1--6 | -- | No | d_model = 768, 12 heads/layer |
| Small with MLPs | 1--6 | -- | Yes | d_model = 768, 12 heads/layer |
| Full-scale | 4--40 | 13M--13B | Yes | d_model = 128 * n_layer, dense + local attention |
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

All models use a context window of 8192 tokens, a 2^16 token vocabulary, and positional embeddings similar to Press et al. (2020). The full-scale models have both dense and local attention heads. Small models were trained for 10,000 steps (~10 billion tokens) with 200 snapshots saved at 50-step intervals. Full-scale models had 14--15 snapshots saved at exponential step intervals (2^5 through 2^17).

**Training data:** Filtered common crawl and internet books (described in Askell et al., 2021), including approximately 10% Python code. Small models were also trained on an alternate books-only dataset to verify that the phase change is not dataset-dependent. All models trained on a given dataset saw the same examples in the same order. Models never saw the same training data twice.

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

The one-layer model is the consistent exception: it shows none of these phenomena, as induction heads require composition across at least two layers. The phase change does not coincide with any scheduled hyperparameter change (learning rate warmup ends at ~1.5 billion tokens; weight decay changes at ~5 billion tokens, beyond the phase change window).

Training on a different dataset (books-only) produces the same phase change pattern, indicating it is not an artifact of the training data.

Qualitative analysis of per-token losses on the first paragraph of Harry Potter shows the expected behavior: tokens in repeated sequences (e.g., "The Dursleys") are predicted better after the phase change, while tokens that break a previously-seen pattern (e.g., "Mrs Potter" after two instances of "Mrs Dursley") are predicted worse.

#### Smeared Key Results (Argument 2)

| Architecture | 1-Layer | 2-Layer |
|---|---|---|
| Vanilla | No phase change | Phase change at ~2.5--5B tokens |
| Smeared key | Phase change occurs | Phase change occurs earlier |

The per-argument evidence table for Argument 2 rates the evidence as Medium, Interventional for small models and Weak, Interventional for large models.

#### Ablation Results (Argument 3)

In small attention-only models, **almost all in-context learning comes from induction heads**. Ablating induction heads (colored dark in the paper's plots) accounts for nearly the entire in-context learning score, while ablating most other heads slightly increases in-context learning. This effect arises because removing "normal prediction" capacity leaves more room for in-context learning to show an effect -- some tokens can be predicted by both mechanisms. This result holds from the start of the phase change through the end of training.

In models with MLPs, ablation evidence is suggestive but less conclusive because in-context learning could also arise from interactions between MLP and attention layers. Ablations were not performed on full-scale models due to computational cost.

#### Induction Head Behaviors in 13B Model (Argument 4)

| Head | Layer Depth | Copying Score | Prefix Matching Score | Behavior |
|---|---|---|---|---|
| Literal copying head | 21 / 40 | 0.89 | 0.75 | Copies repeated text sequences verbatim |
| Translation head | 7 / 40 | 0.20 | 0.85 | Translates between English, French, German |
| Pattern-matching head | 8 / 40 | 0.69 | 0.94 | Learns function from (category, item) -> label |

Note: The table above lists the pattern-matching head at layer depth 8/40, while the text in the paper (Behavior 3 section) describes it as "found at layer 26 of our 40-layer model." This is a discrepancy in the paper; the table values are used here.

All three heads simultaneously satisfy the formal definition of induction head (literal copying on random sequences) while also performing their more abstract behaviors. The translation head attends along a "meandering off-diagonal" due to different word orders and token lengths across languages. The logit attribution for the translation head is not perfectly sharp -- the head's output likely needs further processing by later layers, but on net the direct logit attributions show evidence of contributing to correct translation. The pattern-matching head allocates about 65% of its attention from colon tokens to semantically correct positions on category-labeling tasks using templates: (month)(animal):0, (month)(fruit):1, (color)(animal):2, (color)(fruit):3.

#### Where Induction Heads Form in Models

In small attention-only models, induction heads form in the last layer. In small models with MLPs, by 5--6 layers, they form more in the second-to-last layer. In full-scale models (24L, 40L), the majority of induction heads form before the halfway point in model depth.

#### Unexplained Curiosities

- **Constant in-context learning score across scales:** After the phase change, the in-context learning score (~0.4 nats) is nearly identical for models from 2 layers to 13B parameters. Large models gain all their advantage over small models very early in the context -- in fact, the majority of the difference forms in the first ten tokens. They then reduce loss by a roughly fixed additional amount over the remainder. The authors interpret this as the same in-context learning being "harder" (more nats per improvement) from a lower baseline. The constancy is robust to varying the definition of the score (e.g., using Loss(final token) - Loss(i_ctx) for various i_ctx values).
- **Loss derivative order inversion:** The derivative of loss with respect to log(training tokens) shows that small models improve faster than large models before the phase change, but the opposite is true after -- and this inversion coincides with the phase change.
- **Additional curiosities:** The 6-layer attention-only model has a non-induction head that ablates similarly to reversing the phase change; the 4-layer MLP model ablations are unusually diffuse; the 6-layer MLP model has a loss spike and one induction head whose ablation has the opposite expected effect on in-context learning; full-scale models above 16 layers show "anti-copying prefix-search" heads that score well on prefix matching but negatively on copying.

---

## Limitations and Failure Modes

- **Evidence degrades with model scale.** Evidence is **strong and causal** for small attention-only models but only **correlational** for large models with MLPs. The authors are explicit that the claim is preliminary and indirect for large models (Abstract, Argument 6).
- **No ablations on full-scale models.** Ablations were not performed on full-scale models due to computational cost (scales as O(N^1.33) with model size). The strongest causal evidence is therefore limited to small models.
- **Shared latent variable confound.** The phase change co-occurrence could be driven by a shared latent variable (e.g., the model learning to compose layers through the residual stream) rather than direct causation from induction heads. Perhaps other mechanisms also form during the phase change that also require composition of multiple heads.
- **Constant score does not guarantee constant mechanism.** The constant in-context learning score (~0.4 nats) after the phase change does not necessarily mean that the underlying mechanisms of in-context learning are constant. The metric measures a relative loss between token index 500 and 50, and the model's performance at token 50 improves over training time. Reducing the loss a fixed amount from a lower baseline is likely harder, and may be driven by additional mechanisms as training time goes on.
- **MLP-attention interactions complicate ablation interpretation.** In models with MLPs, in-context learning could arise from interactions between MLP and attention layers. Ablating an attention head might shift the statistics of an MLP layer and "break" neurons by shifting their effective bias, or an important MLP mechanism might rely on two attention heads but function with one if the other is ablated.
- **Low time resolution for large models.** Full-scale models have only 14--15 snapshots saved at exponential intervals. Co-occurrence when one has only 15 points in time is less surprising and weaker evidence.
- **No evidence of mesa-optimizers, but cannot rule out.** The authors did not observe mesa-optimizers, but cannot rule out more complex mechanisms in large models.
- **Single training run per model.** All results are based on a single training run per model configuration, without repetition.
- **Argument at transition vs. end of training.** The argument that induction heads account for most in-context learning at the transition point of the phase change is more solid than the argument that they account for most at the end of training -- a lot could be changing during training even as the score remains constant.

---

## Conclusions

### Contributions

1. **Causal evidence that induction heads drive in-context learning in small models.** In small attention-only transformers, ablation experiments show that induction heads account for nearly all measured in-context learning. This constitutes strong, causal evidence that pattern-completion circuits (`[A][B]...[A]` -> `[B]`) are the mechanistic source of the model's ability to improve predictions from context (Argument 3, Model Analysis Table).

2. **Discovery of a training phase change linked to induction head formation.** All multi-layer transformers undergo an abrupt phase change early in training (roughly 2.5--5 billion tokens) during which induction heads form, in-context learning dramatically improves, the loss curve shows a visible bump, and per-token loss PCA trajectories pivot. This co-occurrence is observed across 34 models spanning four architectural series from 1 to 40 layers (Argument 1, Model Analysis Table).

3. **Interventional confirmation via smeared key architecture.** The smeared key architecture, which enables induction heads in one-layer models by interpolating between current and previous token keys, causes the phase change to occur in one-layer models (where it otherwise never occurs) and earlier in two-layer models. This interventional evidence strengthens the argument beyond correlation (Argument 2).

4. **Demonstration that induction heads implement abstract pattern matching.** Induction heads in a 13B parameter model simultaneously perform literal copying on random sequences and exhibit sophisticated behaviors including translation and category-based pattern matching. These behaviors follow the form `[A*][B*]...[A]` -> `[B]` where matching is in abstract embedding space, not just token identity (Argument 4).

5. **Mechanistic account of induction head generalization.** The reverse-engineered QK circuit (K-composition with a previous token head, producing a term Id (tensor product) h_prev (tensor product) W with positive eigenvalues) implements prefix matching by comparing the current token with preceding tokens at earlier positions. When operating on abstract representations from earlier layers, this same mechanism naturally implements fuzzy or analogical matching (Argument 5).

6. **First mechanistic account of a phase change in machine learning.** The induction head phase change is the first known case where a macroscopic property of neural network training (the loss bump, visible in aggregated loss) can be explained at the level of individual circuits. This provides a concrete link between the microscopic domain of interpretability and the macroscopic domain of scaling laws and learning dynamics (Discussion).

### Implications

1. **Induction heads may be the primary in-context learning mechanism at all scales.** The continuity of all measurements from small to large models (Argument 6) suggests that the same mechanism operates at all sizes, though this is extrapolation and the evidence is only correlational for large models. [Inference, explicitly acknowledged as preliminary]

2. **In-context learning may be a safety-relevant capability.** In-context learning allows model behavior to "change" during inference without weight updates, which is relevant to concerns about mesa-optimization and unexpected behavioral adaptation. The authors found no evidence of mesa-optimizers; the mechanism appears to be induction heads rather than an internal optimization algorithm. [Noted by authors]

3. **Phase changes may be generalizable.** Neural network capabilities can emerge discontinuously during training, as demonstrated by the abrupt formation of in-context learning. Studying phase changes "up close" with mechanistic understanding could contain generalizable lessons for anticipating and addressing safety problems in future systems. [Speculative]

4. **One-layer model scaling law exceptions may be explained.** Kaplan et al. (2020) found that 1-layer transformers do not follow the same scaling laws as deeper transformers. The absence of induction heads in 1-layer models is a plausible explanation. [Inference]

5. **Phase change as a "Rosetta stone."** The induction head phase change may bridge mechanistic interpretability, learning dynamics, and scaling laws -- three lines of research that are typically studied independently. [Noted by authors]

---

## Key Claims

1. **Induction heads are the primary mechanism for in-context learning in small attention-only models.** In these models, ablating induction heads accounts for nearly the entire in-context learning score, and no other heads contribute meaningfully to in-context learning (Argument 3, Model Analysis Table ablation plots). Status: **supported**.

2. **A phase change early in training co-occurs with induction head formation and in-context learning improvement across all multi-layer models.** Across 34 models spanning 4 series, from 2 layers to 13B parameters, trained on two different datasets, the same co-occurrence is observed at roughly 2.5--5 billion tokens. The one-layer model is the consistent exception (Argument 1, Model Analysis Table). Status: **supported**.

3. **The smeared key architecture confirms induction heads as the minimal mechanism for the in-context learning improvement.** One-layer smeared key models undergo a phase change (which never occurs in standard one-layer models), and two-layer smeared key models undergo it earlier (Argument 2). Status: **supported**.

4. **Induction heads in large models implement abstract pattern matching.** Three heads in the 13B model (copying score 0.20--0.89, prefix matching score 0.75--0.94) perform literal copying, cross-lingual translation, and category-based labeling while simultaneously satisfying the formal definition of induction head (Argument 4, Table in Argument 4 section). Status: **supported**.

5. **In-context learning score is approximately constant across model sizes after the phase change.** The in-context learning score (~0.4 nats, defined as loss at token 500 minus loss at token 50) is nearly identical for models from 2 layers to 13B parameters. This holds under varying definitions of the score. Large models gain their advantage in the first ~10 tokens of context (Unexplained Curiosities section). Status: **supported**.

6. **The induction head mechanism is not mesa-optimization.** The observed mechanism is pattern-completion via K-composition and OV copying circuits, not an internal optimization algorithm. No evidence of mesa-optimizers was found (Discussion, Safety Implications). Status: **unvalidated** (absence of evidence is not definitive, especially for large models).

---

## Open Questions

1. **Majority mechanism in large models.** Do induction heads account for the majority of in-context learning in large models with MLPs, or do additional mechanisms (other composition heads, MLP-attention interactions) contribute substantially? The paper acknowledges this as the key open question, with only correlational evidence for large models. Not yet addressed in this reference set.

2. **Constant in-context learning score.** Why is the in-context learning score approximately constant (~0.4 nats) across model sizes after the phase change? The authors suggest that larger models gain their advantage in the first ~10 tokens (using world knowledge rather than in-context learning), then reduce loss by a "harder" fixed amount from a lower baseline. But the precise mechanism behind this constancy remains unexplained. Not yet addressed.

3. **Other composition mechanisms.** Do other Q-composition and K-composition mechanisms form simultaneously during the phase change? Larger models have more heads and could express non-induction composition mechanisms that small models cannot afford. If all "composition heads" form simultaneously, non-induction heads could account for a larger fraction of in-context learning in large models. Not yet addressed.

4. **Loss derivative order inversion.** Why does the loss derivative order invert at the phase change (small models improve faster before, large models improve faster after)? Not yet addressed.

5. **Mechanism evolution during training.** Does the mechanism of in-context learning change over the course of training even as the in-context learning score remains constant? The argument that induction heads account for most in-context learning at the transition point is more solid than the argument that they account for most at the end of training. Not yet addressed.

---

## Core References and Why They Are Referenced

### Foundational Framework

- **Elhage et al. (2021)** -- *A Mathematical Framework for Transformer Circuits.* The direct predecessor to this work. Introduced the mathematical decomposition of transformers into OV and QK circuits, first identified induction heads in 2-layer attention-only models, and developed the K-composition framework used throughout this paper to explain how induction heads implement prefix matching.

- **Brown et al. (2020)** -- *Language Models Are Few-Shot Learners (GPT-3).* Demonstrated emergent in-context learning and few-shot task performance in large language models. Represents the "few-shot learning" conception of in-context learning that this paper extends to a mechanistic explanation. Also observed that specific task abilities (e.g., arithmetic) can change abruptly with model size, relevant to the phase change discussion.

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Origin of the "loss at different token indices" formalization of in-context learning used throughout this paper. Also observed that 1-layer transformers do not follow the same scaling laws as deeper models, which this paper potentially explains via the absence of induction heads.

### Interpretability and Circuits

- **Cammarata et al. (2020)** -- *Thread: Circuits.* The broader Circuits research program on mechanistic interpretability of neural networks, which established the framework of studying features and circuits. Induction heads are framed as circuits in this tradition.

- **Olah et al. (2020)** -- *Zoom In: An Introduction to Circuits.* Introduced the concept of universality in circuits -- that different models develop the same features and circuits. Induction heads are presented as a universal circuit that appears across transformer models of all sizes.

### Attention Head Analysis

- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned.* Identified specialized attention heads (syntactic, positional, rare-word-sensitive) in NMT and showed many heads can be pruned. Referenced as part of the literature on attention head patterns that induction heads extend to a circuit-level understanding.

- **Clark et al. (2019)** -- *What Does BERT Look At? An Analysis of BERT's Attention.* Analyzed BERT's 144 attention heads for syntactic and semantic functions. Referenced alongside Voita et al. as representative of the attention head analysis literature. The implicit hypothesis of universal attention patterns (e.g., "previous token" heads forming across models) is extended by this paper's claim that induction heads are a universal circuit.

### In-Context Learning Studies

- **O'Connor & Andreas (2021)** -- *What Context Features Can Transformer Language Models Use?* Found that preserving word order in contexts is important, consistent with the induction head hypothesis. However, some of their experiments (suggesting removing all words except nouns can improve loss) are in tension with the hypothesis, though only in experiments where models were retrained on modified data.

- **Xie et al. (2021)** -- *An Explanation of In-context Learning as Implicit Bayesian Inference.* Proposed a theoretical model of in-context learning as implicit Bayesian inference using Hidden Markov Models. Found LSTMs outperform Transformers on their synthetic HMM data, which the authors attribute to HMM structure not benefiting from induction heads.

### Phase Changes and Discontinuous Behavior

- **Power et al. (2022)** -- *Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets.* Most analogous prior work on phase changes during training. The induction head phase change differs by having a mechanistic explanation at the circuit level. As far as the authors know, induction heads are the first case where a mechanistic account has been provided for a phase change in machine learning.

- **Hubinger et al. (2021)** -- *Risks from Learned Optimization in Advanced Machine Learning Systems.* Introduced the concept of mesa-optimization, which motivated studying whether in-context learning involves an internal optimization algorithm. This paper finds that induction heads, not mesa-optimizers, are the mechanism.

### Learning Dynamics

- **Saxe et al. (2014)** -- *Exact Solutions to the Nonlinear Dynamics of Learning in Deep Linear Neural Networks.* Provided closed-form solutions for learning dynamics in linear networks, finding independent paths through the network that evolve during training. Referenced as a potential theoretical bridge between circuit-level interpretability and training dynamics -- these paths might be thought of as circuits.

### Training Data and Models

- **Askell et al. (2021)** -- *A General Language Assistant as a Laboratory for Alignment.* Describes the training data distribution and full-scale model architecture used in this paper.

- **Press et al. (2020)** -- *Shortformer: Better Language Modeling Using Shorter Inputs.* The small models and smeared key models use a positional embedding variant similar to this work.

### External Replications

- **Scherlis (Redwood Research)** -- Replicated induction heads in 2-layer attention-only transformers. Replacing the previous-token head's attention scores with exact previous-token attention recovered 99% of loss difference. Replacing the induction head's scores with `[A][B]...[A]` matching recovered ~65%, and including `[A][B][C]...[A][B]` -> `[C]` matching recovered an additional ~10%.

- **Lieberum (University of Amsterdam)** -- Found induction heads in GPT-2 and GPT-Neo starting in the mid-depth region using the paper's empirical criterion. For GPT-2-XL, head 20 in layer 21 appears to be an induction head; for GPT-Neo-2.7B, head 0 in layer 12.
