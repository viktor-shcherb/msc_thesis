---
title: "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned"
authors: "Voita, Talbot, Moiseev, Sennrich, Titov"
year: 2019
venue: "ACL 2019"
paper_type: conference-paper
categories: ["attention-analysis", "pruning-and-sparsity"]
scope: ["Transformer encoder self-attention in NMT"]
benchmarks_used: ["wmt-translation"]
models_introduced: []
models_evaluated: ["transformer-base"]
key_claims:
  - id: C1
    claim: "Only a small subset of encoder attention heads are important for translation: 10 out of 48 on WMT EN-RU (-0.15 BLEU) and 4 out of 48 on OpenSubtitles EN-RU (-0.25 BLEU)"
    evidence: "Section 6.2.1, Figure 7"
    status: supported
  - id: C2
    claim: "Three types of specialized heads emerge consistently across language pairs: positional (attending to adjacent tokens), syntactic (tracking dependency relations), and rare-word (attending to least frequent tokens)"
    evidence: "Section 5, Figures 1c, 2b, 2d, Table 1"
    status: supported
  - id: C3
    claim: "Specialized heads are the last to be pruned by the differentiable L0 method, confirming their importance independently of LRP"
    evidence: "Section 6.2.2, Figure 8"
    status: supported
  - id: C4
    claim: "Encoder self-attention heads are the most compressible attention type; decoder-encoder attention heads are the least compressible"
    evidence: "Section 6.3.2, Figure 9"
    status: supported
  - id: C5
    claim: "Models trained from scratch with the same sparse head configuration underperform pruned models by 0.15-0.50 BLEU"
    evidence: "Section 6.3.1, Table 2"
    status: supported
  - id: C6
    claim: "When heads are pruned, remaining heads acquire additional functions (function drift): positional heads begin tracking syntactic dependencies"
    evidence: "Section 6.2.2, Figure 8"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Analyzes the multi-head attention mechanism of the Transformer base architecture and shows most heads are redundant"
  - target: 2019-08-bert-attention-analysis
    type: concurrent
    detail: "Both analyze attention head specialization; Voita et al. study NMT encoders while Clark et al. study BERT"
  - target: 2019-12-sixteen-heads-better-than-one
    type: concurrent
    detail: "Both demonstrate heads can be pruned; Michel et al. take a more task-agnostic approach across BERT and NMT"
  - target: 2019-11-dark-secrets-of-bert
    type: concurrent
    detail: "Both study attention patterns; Kovaleva et al. analyze BERT attention for NLU tasks while Voita et al. analyze Transformer encoder attention for NMT"
  - target: 2021-12-transformer-circuits-framework
    type: complementary
    detail: "Elhage et al. provide a mathematical framework (QK/OV circuit decomposition) explaining how specialized head types arise from circuit structure; they note Voita et al.'s rare-word heads may be related to skip-trigram heads"
  - target: 2021-11-ff-layers-key-value-memories
    type: complementary
    detail: "Geva et al. analyze feed-forward layers (the remaining two-thirds of parameters) as key-value memories, complementing this paper's analysis of attention heads"
  - target: 2022-03-in-context-learning-induction-heads
    type: complementary
    detail: "Olsson et al. extend the head specialization literature by identifying induction heads in autoregressive language models"
open_questions:
  - question: "How does target language morphology systematically affect which syntactic relations are learned by encoder attention heads?"
    addressed_by: null
  - question: "How does the differentiable L0 head pruning method compare to alternative model compression techniques (distillation, quantization) for NMT?"
    addressed_by: null
  - question: "What interpretable functions do decoder self-attention heads play?"
    addressed_by: null
  - question: "Do larger Transformer models or non-translation tasks exhibit different head specialization patterns?"
    addressed_by: null
---

# Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned

**Authors:** Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, Ivan Titov (Yandex, University of Amsterdam, University of Edinburgh, University of Zurich, Moscow Institute of Physics and Technology)
**Date:** July 2019, ACL 2019, arXiv:1905.09418

---

## Core Research Problem

The Transformer architecture (Vaswani et al., 2017) uses multi-head self-attention as its core mechanism. Multi-head attention was shown to improve over single-head attention by almost 1 BLEU point at the same model size (Vaswani et al., 2017), suggesting that different heads learn complementary representations. However, prior analyses of multi-head attention either averaged attention weights over all heads at a given position (Voita et al., 2018) or focused only on maximum attention weights (Tang et al., 2018). Neither method accounts for the varying importance of individual heads, obscuring the roles played by individual heads which, as this paper shows, influence generated translations to differing extents.

The gap is twofold. First, there is no established method for quantifying the contribution of individual attention heads to overall model performance. Second, even if important heads can be identified, it is unclear whether the remaining heads play vital but less easily defined roles, or are simply redundant. **The core challenge is: do individual encoder attention heads play specialized, interpretable roles, and can the remaining heads be removed without significant loss in translation quality?**

---

## Problem Solutions

The paper provides both an analysis of what individual attention heads do and a method for pruning redundant heads:

1. **Identification of specialized head roles.** Using layer-wise relevance propagation (LRP) and head confidence analysis, the paper shows that a small number of heads are disproportionately important, and these heads play consistent, linguistically interpretable roles: positional attention, syntactic attention, and rare-word attention.
2. **A differentiable pruning method for attention heads.** The paper adapts the Hard Concrete relaxation of L0 regularization (Louizos et al., 2018) from weight-level to head-level pruning, enabling continuous pruning from a converged model.
3. **Empirical confirmation of redundancy.** Pruning 38 out of 48 encoder heads on EN-RU WMT results in only 0.15 BLEU drop, and specialized heads are the last to be pruned, independently confirming their importance.

---

## Approach Details

### Method

The paper proceeds in two phases: (1) identifying and characterizing important heads via LRP and manual analysis, and (2) pruning heads using differentiable L0 regularization.

**Phase 1: Head Identification.** Layer-wise relevance propagation (LRP), adapted from Ding et al. (2017), computes the relative contribution of neurons at one point in a network to neurons at another. The paper uses LRP to evaluate how much each attention head at each layer contributes to the top-1 logit predicted by the model. Head relevance for a given prediction is the sum of relevances of its neurons, normalized over heads in a layer. The final relevance is the average over all generation steps on a development set (Appendix A).

Head **confidence** is defined as the average of the maximum attention weight (excluding EOS), averaged over tokens in a development set. A confident head assigns a high proportion of its attention to a single token. LRP-computed relevance agrees to a reasonable extent with confidence, with one notable exception: the most important head in the first layer (the rare-word head) has high LRP relevance but low average maximum attention weight (Section 4, Figures 1a, 1b).

**Phase 2: Pruning.** The standard multi-head attention output

> MultiHead(Q, K, V) = Concat_i(head_i) W^O

is modified to include scalar gates:

> MultiHead(Q, K, V) = Concat_i(g_i * head_i) W^O

where g_i are input-independent, head-specific scalar parameters. The goal is L0 regularization on these gates, but L0 is non-differentiable. Instead, each g_i is drawn from a Hard Concrete distribution (Louizos et al., 2018) -- a parameterized family of mixed discrete-continuous distributions over [0, 1] with non-zero probability mass at both 0 and 1. The Hard Concrete is obtained by stretching the binary Concrete (Gumbel-softmax) distribution from support (0, 1) to (-epsilon, 1 + epsilon) and clamping values below 0 to 0 and above 1 to 1 (Section 6.1, Figure 6a).

The relaxed L0 regularizer is:

> L_C(phi) = sum_{i=1}^{h} (1 - P(g_i = 0 | phi_i))

The full training objective is:

> L(theta, phi) = L_xent(theta, phi) + lambda * L_C(phi)

where theta are the original Transformer parameters, L_xent is the cross-entropy translation loss, and lambda controls the sparsity level. The reparameterization trick (Kingma and Welling, 2014; Rezende et al., 2014) enables backpropagation through the sampling process. Gate values are resampled for each batch during training. The model converges to solutions where gates are either almost completely closed (P(g_i = 0) ≈ 1) or completely open (P(g_i = 1) ≈ 1), the latter not being explicitly encouraged -- the noise from sampling pushes the network away from intermediate values. At test time, gates are binarized based on which of P(g_i = 0) and P(g_i = 1) is larger (Section 6.1).

### Key Technical Components

**Three types of specialized heads:**

1. **Positional heads:** A head is classified as "positional" if at least 90% of the time its maximum attention weight is assigned to a specific relative position (in practice -1 or +1, i.e., adjacent tokens). These are among the most confident and most LRP-important heads. Average maximum attention weight exceeds 0.8 for every positional head across all language pairs (Section 5.1, Figures 1c, 2b, 2d).

2. **Syntactic heads:** A head is classified as "syntactic" if its accuracy on a specific dependency relation is at least 10% above a positional baseline that uses the most frequent relative position for that relation. Accuracy is measured as the fraction of times the head's maximum attention weight (excluding EOS) falls on a token in the given dependency relation, evaluated against CoreNLP parses (Manning et al., 2014) on 50K held-out English sentences. Relations evaluated: nominal subject (nsubj), direct object (dobj), adjectival modifier (amod), adverbial modifier (advmod). Multiple heads can track the same relation (Section 5.2, Table 1).

3. **Rare-word heads:** In all models, one head in the first layer is judged by LRP to be much more important than any other head in that layer. This head points to the least frequent tokens in the sentence. For OpenSubtitles, among sentences where the least frequent token is not in the top-500 most frequent, this head points to the rarest token in 66% of cases and to one of the two least frequent in 83% of cases. For WMT, it points to one of the two least frequent in more than 50% of such cases (Section 5.3, Figure 5).

**Pruning protocol:** Pruning starts from a converged model trained without the L_C penalty. Gates are added and training continues with the full objective. By varying lambda, models with different numbers of retained heads are obtained. In encoder-only pruning experiments, decoder parameters are fixed to prevent function migration (Section 6.2). In preliminary experiments, fine-tuning a trained model gave 0.2--0.6 BLEU better results than applying the regularized objective or training with the same number of heads from scratch (footnote 8).

**Function drift under pruning:** When fewer heads remain, some functions "drift" to other heads. Positional heads begin tracking syntactic dependencies, acquiring multiple roles. The model with 17 retained encoder heads preserves all identified specialized functions (positional, syntactic, rare-word) despite 2/3 of heads being pruned (Section 6.2.2, Figure 8).

### Experimental Setup

**Model architecture:** Transformer base (Vaswani et al., 2017) with N = 6 layers in both encoder and decoder, h = 8 attention heads per layer (48 total per attention type), d_model = 512, d_ff = 2048 (Appendix B.2).

**Training:** Adam optimizer with beta_1 = 0.9, beta_2 = 0.98, epsilon = 10^-9. Learning rate schedule: lrate = scale * min(step_num^-0.5, step_num * warmup_steps^-1.5) with warmup_steps = 16,000, scale = 4. Batch size of approximately 16,000 source tokens. BPE vocabularies of about 32,000 tokens (Appendix B).

**Data:**

| Language Pair | Dataset | Training Size |
|---|---|---|
| EN-RU | WMT (excl. UN, Paracrawl) | 2.5M sentence pairs |
| EN-DE | WMT | 2.5M sentence pairs |
| EN-FR | WMT | 2.5M sentence pairs |
| EN-RU | OpenSubtitles2018 | 6M sentence pairs |

For OpenSubtitles, only sentence pairs with relative time overlap of subtitle frames >= 0.9 are used to reduce noise. Syntactic evaluation uses 50K held-out English sentences from WMT EN-FR data (Section 3).

**Evaluation:** BLEU score for translation quality; LRP for head importance; dependency accuracy for syntactic analysis against CoreNLP parses (Section 5.2.1).

### Key Results

**Encoder head pruning (EN-RU):**

| Dataset | Total Encoder Heads | Retained Heads | BLEU Drop |
|---|---|---|---|
| WMT | 48 | 10 | -0.15 |
| OpenSubtitles | 48 | 4 | -0.25 |

- 10 out of 48 encoder heads suffice on the more complex WMT task (Section 6.2.1, Figure 7).
- Only 4 encoder heads suffice on the simpler OpenSubtitles domain.
- If all heads in a layer are pruned, only the residual connection remains (footnote 9).

**All-attention pruning (EN-RU, WMT, 2.5M):**

| Heads (enc/dec/dec-enc) | BLEU (from trained) | BLEU (from scratch) |
|---|---|---|
| 48/48/48 (baseline) | 29.6 | 29.6 |
| 14/31/30 | 29.62 | 29.47 |
| 12/21/25 | 29.36 | 28.95 |
| 8/13/15 | 29.06 | 28.56 |
| 5/9/12 | 28.90 | 28.41 |

**All-attention pruning (EN-RU, OpenSubtitles, 6M):**

| Heads (enc/dec/dec-enc) | BLEU (from trained) | BLEU (from scratch) |
|---|---|---|
| 48/48/48 (baseline) | 32.4 | 32.4 |
| 27/31/46 | 32.24 | 32.23 |
| 13/17/31 | 32.23 | 31.98 |
| 6/9/13 | 32.27 | 31.84 |

- Almost 3/4 of encoder heads and more than 1/3 of decoder self-attention and decoder-encoder heads can be pruned on WMT with no noticeable BLEU loss (Table 2).
- More than half of all heads can be pruned with at most 0.25 BLEU drop.
- Models trained from scratch with the same sparse configuration consistently underperform pruned models by 0.15--0.50 BLEU (Table 2), consistent with observations from model compression literature (Zhu and Gupta, 2017; Gale et al., 2019).

**Syntactic head accuracy (EN-RU):**

| Dependency | Direction | Best Head (WMT) | Baseline (WMT) | Best Head (OpenSub) | Baseline (OpenSub) |
|---|---|---|---|---|---|
| nsubj | v -> s | 45 | 35 | 77 | 45 |
| nsubj | s -> v | 52 | 35 | 70 | 45 |
| dobj | v -> o | 78 | 41 | 61 | 46 |
| dobj | o -> v | 73 | 41 | 84 | 46 |
| amod | noun -> adj.m. | 74 | 72 | 81 | 80 |
| amod | adj.m. -> noun | 82 | 72 | 81 | 80 |
| advmod | v -> adv.m. | 48 | 46 | 38 | 33 |
| advmod | adv.m. -> v | 52 | 46 | 42 | 33 |

- The strongest syntactic heads track dobj and nsubj relations substantially above the positional baseline (Table 1).
- Subject-verb accuracy is higher on OpenSubtitles, hypothesized to be due to greater variety of grammatical person in subtitle data: 32%/21%/47% first/second/third person vs. 6%/3%/91% in WMT (footnote 4, Section 5.2.2).
- Syntactic accuracy patterns are consistent across language pairs (EN-RU, EN-DE, EN-FR) on WMT (Figure 4).

### Relative Importance of Attention Types

The model preferentially prunes **encoder self-attention** heads first, while **decoder-encoder attention** heads are the most resistant to pruning (Figure 9). Decoder self-attention heads (functioning as a target-side language model) fall between the two, with importance varying by domain: they are almost as important as decoder-encoder heads for WMT (average sentence length 24 tokens) and slightly more important than encoder self-attention for OpenSubtitles (average sentence length 8 tokens) (Section 6.3.2).

Within the decoder, self-attention heads are retained more readily in **lower layers**, while decoder-encoder attention heads are retained in **higher layers** (Figure 10). This suggests lower decoder layers are primarily responsible for language modeling, while higher layers are primarily responsible for conditioning on the source sentence (Section 6.3.2).

---

## Limitations and Failure Modes

- **Restricted to Transformer base on translation.** All experiments use the 6-layer, 8-head Transformer base model on machine translation. Larger models, other architectures, or non-translation tasks may exhibit different head specialization and pruning patterns (Section 8).
- **Limited syntactic evaluation.** Only four dependency relations (nsubj, dobj, amod, advmod) are evaluated, and ground truth relies on CoreNLP parses rather than gold annotations (Section 5.2.1).
- **Decoder self-attention not analyzed.** The paper focuses primarily on encoder self-attention; functions of decoder self-attention heads are not characterized (Section 2).
- **Target language morphology effect unclear.** The paper notes that relations with strong target morphology are among those most accurately learned, but states that "it is not possible to draw any strong conclusions" about the impact of target language morphology (Section 5.2.2).
- **Fixed head count per layer.** All models use 8 heads per layer. The paper does not explore whether different layer-specific head counts would be optimal if allowed from the start.
- **amod and advmod heads near baseline.** For amod and advmod relations, the best head accuracy exceeds the positional baseline by only 1--10 percentage points in most cases (Table 1), making it harder to claim these heads have truly specialized syntactic functions beyond positional proximity.

---

## Conclusions

### Contributions

1. **Identification of specialized attention head functions.** Using LRP and manual analysis, the paper identifies three consistent head types in Transformer encoder self-attention: positional (attending to adjacent tokens with >0.8 average max attention weight), syntactic (tracking nsubj and dobj relations 10--40% above positional baselines), and rare-word (attending to least frequent tokens in 66%+ of cases). These roles are consistent across three language pairs and two domains (Sections 5.1--5.3).

2. **Differentiable head-level L0 pruning method.** The paper adapts the Hard Concrete distribution (Louizos et al., 2018) from weight-level to head-level pruning, providing a principled method for determining how many and which heads are needed. Gates converge to binary values without explicit encouragement (Section 6.1).

3. **Demonstration of massive encoder redundancy.** Pruning 38 of 48 encoder heads costs only 0.15 BLEU on WMT EN-RU; on OpenSubtitles, 4 heads suffice with 0.25 BLEU loss. Specialized heads are pruned last, independently confirming LRP findings (Section 6.2).

4. **Characterization of attention type importance.** When pruning all attention types, encoder self-attention is the most compressible, decoder-encoder attention the least, and decoder self-attention's importance varies with domain and sentence length (Section 6.3.2, Figure 9).

5. **Evidence that pruned models outperform retrained sparse models.** Models trained from scratch with pruned configurations consistently underperform pruned models by 0.15--0.50 BLEU, confirming at the head level that sparse architectures benefit from dense pretraining (Table 2).

### Implications

1. **Multi-head attention is over-parameterized for NMT.** The finding that the vast majority of heads can be removed suggests that the standard Transformer uses far more heads than necessary, at least for translation. This has practical implications for model compression and inference efficiency. [Inference: the paper demonstrates this for NMT specifically; generalization to other tasks is not tested.]

2. **Functional specialization is an emergent property of training.** The consistency of head roles across language pairs and domains suggests that positional and syntactic functions emerge reliably from the translation objective, not from explicit supervision. [Inference: the paper shows correlation, not causation -- these roles may be artifacts of the training data distribution.]

3. **Compression may not require retraining from scratch.** The gap between pruned and retrained-from-scratch models suggests that dense training followed by pruning is a more effective compression strategy than training sparse models directly, consistent with lottery ticket findings in other domains.

---

## Key Claims

1. **Only a small subset of encoder heads matter for translation.** On WMT EN-RU, 10 out of 48 encoder heads are sufficient to stay within 0.15 BLEU of the full model; on OpenSubtitles EN-RU, 4 out of 48 suffice within 0.25 BLEU (Section 6.2.1, Figure 7). **Status: supported.**

2. **Three specialized head types emerge consistently.** Positional heads (>90% max attention to adjacent token, >0.8 average max weight), syntactic heads (>10% above positional baseline for nsubj, dobj), and one rare-word head in the first layer (pointing to rarest token in 66% of filtered cases on OpenSubtitles) appear across EN-RU, EN-DE, EN-FR on WMT and EN-RU on OpenSubtitles (Section 5, Table 1, Figures 1c, 2b, 2d). **Status: supported.**

3. **Specialized heads are pruned last.** The differentiable L0 method independently confirms LRP rankings: heads with identified positional and syntactic functions are the most resistant to pruning. A model retaining 17 heads preserves all identified functions (Section 6.2.2, Figure 8). **Status: supported.**

4. **Encoder self-attention is the most compressible attention type.** When pruning all attention types, the model preferentially removes encoder self-attention heads first. Decoder-encoder attention heads are the most resistant (Section 6.3.2, Figure 9). **Status: supported.**

5. **Pruned models outperform retrained sparse models.** Models trained from scratch with the same head configuration as pruned models consistently underperform by 0.15--0.50 BLEU (Table 2, Section 6.3.1). **Status: supported.**

6. **Function drift occurs under compression.** When heads are pruned, remaining heads acquire additional roles: positional heads begin tracking syntactic dependencies (Section 6.2.2, Figure 8). **Status: supported.**

---

## Open Questions

1. **How does target language morphology systematically affect syntactic head accuracy?** The paper observes that nsubj accuracy is higher on OpenSubtitles (more person variety: 32%/21%/47% first/second/third) than WMT (6%/3%/91%), but leaves proper analysis to future work (Section 5.2.2). Not addressed by subsequent work in this directory.

2. **How does head pruning compare to alternative NMT compression methods?** The paper notes this as future work (Section 8). Not directly addressed.

3. **What interpretable functions do decoder self-attention heads play?** The paper analyzes only encoder self-attention in detail. Decoder self-attention heads are characterized only by their aggregate pruning behavior (Section 6.3.2). Not addressed.

4. **Do larger models or non-translation tasks exhibit different specialization patterns?** All experiments use Transformer base on translation. Whether the same head types emerge in larger models or on classification, summarization, or language modeling tasks is unknown. Partially addressed by Clark et al. (2019) for BERT on NLU tasks and by Olsson et al. (2022) for induction heads in language models.

---

## Core References and Why They Are Referenced

### Transformer Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer and multi-head attention mechanism that is the subject of this paper's analysis. Provides the baseline architecture (6-layer, 8-head, d_model=512) and the finding that 8 heads outperform 1 head by ~1 BLEU at the same model size.

### Prior Attention Analysis in NMT

- **Voita et al. (2018)** -- *Context-Aware Neural Machine Translation Learns Anaphora Resolution.* Prior work by the same first author that analyzed attention weights by averaging over heads. This paper moves beyond averaging to per-head analysis.
- **Tang et al. (2018)** -- *Why Self-Attention? A Targeted Evaluation of Neural Machine Translation Architectures.* Analyzed maximum attention weights across heads. Like Voita et al. (2018), does not account for varying head importance.
- **Raganato and Tiedemann (2018)** -- *An Analysis of Encoder Representations in Transformer-Based Machine Translation.* Uses encoder self-attention weights to induce tree structures and computes unlabeled attachment scores. Does not evaluate specific dependency relations per head or consider how different heads specialize to different relations.

### LRP and Interpretability

- **Ding et al. (2017)** -- *Visualizing and Understanding Neural Machine Translation.* Proposes the LRP method for NMT that this paper adapts to measure per-head contribution to top-1 logit predictions.
- **Bach et al. (2015)** -- *On Pixel-Wise Explanations for Non-Linear Classifier Decisions by Layer-Wise Relevance Propagation.* Original LRP method for image classifiers that the NMT adaptation builds on.
- **Bau et al. (2019)** -- *Identifying and Controlling Important Neurons in Neural Machine Translation.* Identifies important individual neurons in NMT. This paper operates at the coarser granularity of entire attention heads rather than individual neurons.

### Sparsification and Pruning

- **Louizos et al. (2018)** -- *Learning Sparse Neural Networks Through L0 Regularization.* Introduces the Hard Concrete distribution and differentiable L0 relaxation for pruning individual weights. This paper adapts the method to prune entire attention heads.
- **Zhu and Gupta (2017)** -- *To Prune, or Not to Prune.* Shows that sparse architectures from pruning cannot be retrained from scratch to the same performance. This paper confirms this finding at the attention-head level.
- **Gale et al. (2019)** -- *The State of Sparsity in Deep Neural Networks.* Further evidence that pruned models outperform models trained from scratch with the same sparse structure.

### Stochastic Relaxations

- **Maddison et al. (2017)** -- *The Concrete Distribution.* Introduces the Concrete (Gumbel-softmax) distribution that the Hard Concrete distribution is derived from.
- **Jang et al. (2017)** -- *Categorical Reparameterization with Gumbel-Softmax.* Concurrently introduces the same Gumbel-softmax relaxation used as the basis for Hard Concrete gates.
- **Kingma and Welling (2014)** -- *Auto-Encoding Variational Bayes.* Provides the reparameterization trick used to backpropagate through the stochastic gate sampling.

### Linguistic Analysis of NMT

- **Belinkov et al. (2017a)** -- *What Do Neural Machine Translation Models Learn About Morphology?* Evaluates morphological information in NMT representations, part of the broader probing program motivating this paper.
- **Bisazza and Tump (2018)** -- *The Lazy Encoder.* Shows that the target language determines which information gets encoded, consistent with this paper's observation that syntactic head accuracy varies with target language and domain.

### Data and Tools

- **Manning et al. (2014)** -- *The Stanford CoreNLP Natural Language Processing Toolkit.* Provides the dependency parses used as ground truth for evaluating syntactic head accuracy.
- **Sennrich et al. (2016)** -- *Neural Machine Translation of Rare Words with Subword Units.* Provides the BPE encoding used for data preprocessing (~32,000 token vocabularies).
- **Lison et al. (2018)** -- *OpenSubtitles2018.* Provides the OpenSubtitles corpus used for the EN-RU domain comparison experiments.
