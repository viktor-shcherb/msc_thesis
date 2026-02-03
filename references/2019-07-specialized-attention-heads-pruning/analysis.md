# Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned

**Authors:** Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, Ivan Titov (Yandex, University of Amsterdam, University of Edinburgh, University of Zurich, Moscow Institute of Physics and Technology)
**Date:** July 2019, ACL 2019, arXiv:1905.09418

---

## Core Research Problem

The Transformer architecture (Vaswani et al., 2017) relies on multi-head self-attention as its core mechanism. Multi-head attention was shown to improve performance over single-head attention by almost 1 BLEU point at the same model size (Vaswani et al., 2017), suggesting that different heads learn complementary representations. However, prior analysis of multi-head attention either averaged attention weights over all heads at a given position (Voita et al., 2018) or focused only on maximum attention weights (Tang et al., 2018), neither method accounting for the varying importance of individual heads. This obscures whether each head contributes meaningfully to the model's predictions or whether many heads are redundant.

The fundamental gap is twofold. First, there is no method for quantifying the contribution of individual attention heads to overall model performance beyond indirect probing. Second, even if important heads can be identified, it is unclear whether the remaining heads play vital but less interpretable roles, or whether they are simply redundant. **The core challenge is: do individual encoder attention heads play specialized, interpretable roles in the Transformer, and can the remaining heads be removed without significant loss in translation quality?**

---

## Problem Solutions

The paper provides both an analysis of what individual attention heads do and a method for pruning redundant heads. The key contributions are:

1. **Identification of specialized head roles.** Using layer-wise relevance propagation (LRP) and confidence analysis, the paper shows that a small number of heads are disproportionately important, and that these heads play consistent, linguistically interpretable roles: positional attention (attending to adjacent tokens), syntactic attention (tracking dependency relations), and rare-word attention (attending to infrequent tokens).
2. **A differentiable pruning method for attention heads.** The paper introduces a method based on stochastic gates with a Hard Concrete relaxation of the L0 penalty (Louizos et al., 2018), adapted from weight-level pruning to head-level pruning. This allows continuous pruning starting from a converged model.
3. **Empirical evidence of massive redundancy.** On the English-Russian WMT task, pruning 38 out of 48 encoder heads results in only 0.15 BLEU drop. Specialized heads are the last to be pruned, confirming their importance.

---

## Approach Details

### Method

The paper proceeds in two phases: (1) identifying and characterizing important heads using LRP and manual analysis, and (2) pruning heads using a differentiable relaxation of L0 regularization.

**Phase 1: Head Identification.** Layer-wise relevance propagation (LRP) computes the relative contribution of neurons at one layer to neurons at another. The paper adapts LRP (originally from Ding et al., 2017) to measure how much each attention head contributes to the top-1 logit predicted by the model. Head relevance for a given prediction is the sum of relevances of its neurons, normalized over heads in a layer, averaged over all generation steps on a development set.

Head **confidence** is defined as the average of the maximum attention weight (excluding EOS), averaged over tokens in the development set. A confident head is one that usually assigns a high proportion of its attention to a single token.

**Phase 2: Pruning.** The standard multi-head attention output

> MultiHead(Q, K, V) = Concat_i(head_i) W^O

is modified to include scalar gates:

> MultiHead(Q, K, V) = Concat_i(g_i * head_i) W^O

where g_i are input-independent, head-specific scalar parameters. The goal is to apply L0 regularization to these gates, pushing unimportant gates to exactly zero. Since L0 is non-differentiable, the paper uses the Hard Concrete distribution (Louizos et al., 2018) -- a parameterized family of mixed discrete-continuous distributions over [0, 1] with non-zero probability mass at both 0 and 1.

The Hard Concrete distribution is obtained by stretching the binary Concrete (Gumbel-softmax) distribution from support (0, 1) to (-epsilon, 1 + epsilon) and then clamping values below 0 to 0 and above 1 to 1. The relaxed L0 regularizer is:

> L_C(phi) = sum_{i=1}^{h} (1 - P(g_i = 0 | phi_i))

The full training objective is:

> L(theta, phi) = L_xent(theta, phi) + lambda * L_C(phi)

where theta are the original Transformer parameters, L_xent is the cross-entropy translation loss, and lambda controls the sparsity level. The reparameterization trick (Kingma and Welling, 2014) enables backpropagation through the sampling process. Gate values are resampled for each batch during training. At test time, gates converge to binary values (either ~0 or ~1), so the model operates as a standard Transformer with a subset of heads.

### Key Technical Components

**Three types of specialized heads:**

1. **Positional heads:** Heads where at least 90% of the time the maximum attention weight is assigned to a specific relative position (in practice, -1 or +1, i.e., attending to adjacent tokens). These have average maximum attention weight exceeding 0.8 for all language pairs.
2. **Syntactic heads:** Heads that track specific dependency relations (nsubj, dobj, amod, advmod) with accuracy at least 10% above a positional baseline that uses the most frequent relative position for the relation. Accuracy is measured as the fraction of times the head's maximum attention weight (excluding EOS) falls on a token in the given dependency relation. Dependency structures are obtained from CoreNLP (Manning et al., 2014).
3. **Rare-word heads:** In all models, one head in the first layer is judged by LRP to be much more important than any other head in that layer. This head points to the least frequent token in the sentence: for OpenSubtitles, it points to the rarest token in 66% of cases (or one of the two rarest in 83%) among sentences where the least frequent token is not in the top-500 most frequent.

**Pruning protocol:** The pruning starts from a converged model trained without the L_C penalty. Gates are added and training continues with the full objective. During encoder-only pruning, decoder parameters are fixed to prevent function migration. By varying lambda, models with different numbers of retained heads are obtained.

**Function drift under pruning:** When fewer heads remain, some functions "drift" to other heads. For example, positional heads begin tracking syntactic dependencies, acquiring multiple roles as the model becomes more compressed.

### Experimental Setup

**Model architecture:** Transformer base (Vaswani et al., 2017) with N = 6 layers in both encoder and decoder, h = 8 attention heads per layer, d_model = 512, d_ff = 2048. BPE vocabularies of ~32,000 tokens.

**Training:** Adam optimizer with beta_1 = 0.9, beta_2 = 0.98, epsilon = 10^-9. Learning rate schedule with warmup_steps = 16,000, scale = 4. Batch size of ~16,000 source tokens.

**Data:**

| Language Pair | Dataset | Training Size |
|---|---|---|
| EN-RU | WMT (excl. UN, Paracrawl) | 2.5M sentence pairs |
| EN-DE | WMT | 2.5M sentence pairs |
| EN-FR | WMT | 2.5M sentence pairs |
| EN-RU | OpenSubtitles2018 | 6M sentence pairs |

**Evaluation:** BLEU score on translation; head importance via LRP; dependency accuracy for syntactic analysis (nsubj, dobj, amod, advmod) evaluated on 50K held-out English sentences from WMT EN-FR data.

### Key Results

**Encoder head pruning (EN-RU):**

| Dataset | Total Encoder Heads | Retained Heads | BLEU Drop |
|---|---|---|---|
| WMT | 48 | 10 | -0.15 |
| OpenSubtitles | 48 | 4 | -0.25 |

- For the more complex WMT task, 10 out of 48 encoder heads suffice to stay within 0.15 BLEU of the full model.
- For the simpler OpenSubtitles domain, only 4 encoder heads suffice for a 0.25 BLEU drop.
- A model retaining 17 heads preserves all identified specialized functions (positional, syntactic, rare-word).

**All-attention pruning (EN-RU, WMT):**

| Heads (enc/dec/dec-enc) | BLEU (from trained) | BLEU (from scratch) |
|---|---|---|
| 48/48/48 (baseline) | 29.60 | 29.60 |
| 14/31/30 | 29.62 | 29.47 |
| 12/21/25 | 29.36 | 28.95 |
| 8/13/15 | 29.06 | 28.56 |
| 5/9/12 | 28.90 | 28.41 |

**All-attention pruning (EN-RU, OpenSubtitles):**

| Heads (enc/dec/dec-enc) | BLEU (from trained) | BLEU (from scratch) |
|---|---|---|
| 48/48/48 (baseline) | 32.40 | 32.40 |
| 27/31/46 | 32.24 | 32.23 |
| 13/17/31 | 32.23 | 31.98 |
| 6/9/13 | 32.27 | 31.84 |

- Almost 3/4 of encoder heads and more than 1/3 of decoder self-attention and decoder-encoder attention heads can be pruned with no noticeable BLEU loss on WMT.
- More than half of all heads can be pruned with at most 0.25 BLEU drop.
- Models trained from scratch with the same sparse configuration consistently underperform the pruned models (0.15--0.50 BLEU gap), consistent with the lottery ticket hypothesis and model compression literature (Zhu and Gupta, 2017; Gale et al., 2019).

**Syntactic head accuracy (EN-RU):**

| Dependency | Direction | Best Head (WMT) | Baseline (WMT) | Best Head (OpenSub) | Baseline (OpenSub) |
|---|---|---|---|---|---|
| nsubj | v -> s | 45% | 35% | 77% | 45% |
| nsubj | s -> v | 52% | 35% | 70% | 45% |
| dobj | v -> o | 78% | 41% | 61% | 46% |
| dobj | o -> v | 73% | 41% | 84% | 46% |
| amod | noun -> adj | 74% | 72% | 81% | 80% |
| advmod | v -> adv | 48% | 46% | 38% | 33% |

- The strongest syntactic heads track dobj and nsubj relations substantially above the positional baseline. The subject-verb relation is tracked more accurately on OpenSubtitles, hypothesized to be due to greater variety of grammatical person in subtitle data (32%/21%/47% first/second/third person vs. 6%/3%/91% in WMT).

### Relative Importance of Attention Types

The model preferentially prunes **encoder self-attention** heads first, while **decoder-encoder attention** heads are the most resistant to pruning (without them, no translation can happen). Decoder self-attention heads (functioning as a target-side language model) fall between the two, with importance varying by domain: they are nearly as important as decoder-encoder heads for WMT (longer sentences, 24 tokens average) and slightly more important than encoder self-attention for OpenSubtitles (shorter sentences, 8 tokens average).

Within the decoder, self-attention heads are retained more readily in lower layers, while decoder-encoder attention heads are retained in higher layers. This suggests lower decoder layers are primarily responsible for language modeling, while higher layers are primarily responsible for conditioning on the source sentence.

### Limitations

- Analysis is restricted to the Transformer base model on the translation task. Larger models or different tasks (e.g., language modeling) may exhibit different head specialization patterns.
- Syntactic evaluation uses only four dependency relations (nsubj, dobj, amod, advmod) and relies on CoreNLP parses as ground truth.
- The paper does not investigate decoder self-attention head functions in detail.
- The connection between head specialization and target language morphology is noted but not rigorously analyzed.
- Models are trained with a fixed number of heads (8 per layer). The paper does not explore whether different layer-specific head counts would emerge if allowed.

---

## Conclusions

1. **Only a small subset of attention heads matter.** LRP analysis and pruning experiments converge on the same finding: in a 6-layer, 8-head Transformer encoder, only about 10 heads (out of 48) are necessary for near-baseline translation quality. The vast majority of heads are redundant.

2. **Important heads play specialized, interpretable roles.** The most important heads fall into three categories: positional (attending to adjacent tokens, >0.8 average maximum attention weight), syntactic (tracking dependency relations like nsubj and dobj at 20--40% above positional baselines), and rare-word (attending to the least frequent tokens in the sentence). These roles are consistent across language pairs (EN-RU, EN-DE, EN-FR) and domains (WMT, OpenSubtitles).

3. **Specialized heads are pruned last.** The differentiable L0 pruning method independently confirms the LRP findings: heads with clearly identifiable positional and syntactic functions are the most resistant to pruning, directly demonstrating their importance to the translation task.

4. **Encoder self-attention is the most compressible attention type.** When pruning all attention types simultaneously, the model preferentially removes encoder self-attention heads first. Decoder-encoder attention heads are the most resistant to pruning, while decoder self-attention importance varies with sentence length and domain.

5. **Pruned models outperform retrained sparse models.** Models with pruned configurations trained from scratch consistently underperform the pruned models by 0.15--0.50 BLEU, showing that the full model's learned representations provide an initialization advantage that sparse training from scratch cannot match.

6. **Function drift under compression.** As heads are pruned, the remaining heads acquire additional roles. Positional heads begin tracking syntactic dependencies, demonstrating that the Transformer's capacity for functional specialization is flexible and that individual heads can serve multiple linguistic functions when necessary.

---

## Core References and Why They Are Referenced

### Transformer Architecture and Attention

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer and multi-head attention mechanism that is the subject of this paper's analysis. Provides the baseline architecture (6-layer, 8-head) and the finding that 8 heads outperform 1 head by ~1 BLEU.

### Attention Analysis in NMT

- **Voita et al. (2018)** -- *Context-Aware Neural Machine Translation Learns Anaphora Resolution.* Prior work by the same first author that analyzed attention weights by averaging over heads. This paper moves beyond averaging to per-head analysis.
- **Tang et al. (2018)** -- *Why Self-Attention? A Targeted Evaluation of Neural Machine Translation Architectures.* Analyzed maximum attention weights across heads. Like Voita et al. (2018), does not account for varying head importance.
- **Raganato and Tiedemann (2018)** -- *An Analysis of Encoder Representations in Transformer-Based Machine Translation.* Uses encoder self-attention weights to induce tree structures and computes unlabeled attachment scores. Does not evaluate specific dependency relations or per-head specialization.
- **Ding et al. (2017)** -- *Visualizing and Understanding Neural Machine Translation.* Proposes the LRP method for NMT that this paper adapts to measure per-head contribution to the model's top-1 logit predictions.

### Sparsification and Pruning

- **Louizos et al. (2018)** -- *Learning Sparse Neural Networks Through L0 Regularization.* Introduces the Hard Concrete distribution and differentiable L0 relaxation for pruning individual weights. This paper adapts the method to prune entire attention heads rather than individual weights.
- **Zhu and Gupta (2017)** -- *To Prune, or Not to Prune: Exploring the Efficacy of Pruning for Model Compression.* Shows that sparse architectures from pruning cannot be retrained from scratch to the same performance. This paper confirms this finding at the attention-head level.
- **Gale et al. (2019)** -- *The State of Sparsity in Deep Neural Networks.* Further evidence that pruned models outperform models trained from scratch with the same sparse structure.

### Stochastic Relaxations

- **Maddison et al. (2017)** -- *The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables.* Introduces the Concrete (Gumbel-softmax) distribution that the Hard Concrete distribution is derived from.
- **Jang et al. (2017)** -- *Categorical Reparameterization with Gumbel-Softmax.* Concurrently introduces the same Gumbel-softmax relaxation used as the basis for Hard Concrete gates.

### Neuron-Level Analysis

- **Bau et al. (2019)** -- *Identifying and Controlling Important Neurons in Neural Machine Translation.* Identifies important individual neurons in NMT. This paper operates at the coarser granularity of entire attention heads rather than individual neurons.

### Linguistic Analysis of NMT

- **Belinkov et al. (2017a)** -- *What Do Neural Machine Translation Models Learn About Morphology?* Evaluates morphological information in NMT representations. Part of the broader program of linguistic probing that motivates this paper's analysis.
- **Bisazza and Tump (2018)** -- *The Lazy Encoder.* Shows that the target language determines which information gets encoded, consistent with this paper's observation that syntactic head accuracy varies with target language morphology and domain.

### Data and Tools

- **Manning et al. (2014)** -- *The Stanford CoreNLP Natural Language Processing Toolkit.* Provides the dependency parses used as ground truth for evaluating syntactic head accuracy.
- **Sennrich et al. (2016)** -- *Neural Machine Translation of Rare Words with Subword Units.* Provides the BPE encoding used for data preprocessing (~32,000 token vocabularies).
- **Lison et al. (2018)** -- *OpenSubtitles2018.* Provides the OpenSubtitles corpus used for the EN-RU domain comparison experiments.
