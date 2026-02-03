# Revealing the Dark Secrets of BERT

**Authors:** Olga Kovaleva, Alexey Romanov, Anna Rogers, Anna Rumshisky (University of Massachusetts Lowell)
**Date:** November 2019, EMNLP-IJCNLP 2019 (arXiv:1908.08593)

---

## Core Research Problem

BERT-based architectures achieve state-of-the-art performance on many NLP tasks, but the exact mechanisms that contribute to their success remain unclear. Self-attention is the fundamental component distinguishing Transformers from prior RNN-based architectures, yet little is known about what information individual attention heads encode, how attention patterns change during fine-tuning, and whether all heads are necessary.

Prior work has probed BERT's linguistic knowledge at the representation level -- Goldberg (2019) tested subject-verb agreement, Jawahar et al. (2019) examined layer-wise linguistic structure, Liu et al. (2019) studied transferability of contextual representations -- but none has systematically analyzed the self-attention mechanism itself across multiple tasks. Separately, work on neural network pruning (Frankle & Carlin, 2018) and head pruning (Michel et al., 2019; Voita et al., 2019) suggests Transformers are overparameterized, but the nature and distribution of redundant attention patterns had not been characterized.

**The core challenge is to understand what information BERT's individual self-attention heads encode, how this information relates to linguistic structure, and whether the model's 144 heads (12 layers x 12 heads) are all necessary.**

---

## Problem Solutions

The paper proposes a methodology for qualitative and quantitative analysis of BERT's self-attention weights, applied to the bert-base-uncased model (12 layers, 12 heads, 110M parameters) across seven GLUE tasks.

1. **Taxonomy of attention patterns.** A classification of self-attention maps into five recurring types (Vertical, Diagonal, Vertical+Diagonal, Block, Heterogeneous), trained via a CNN classifier on ~400 manually annotated maps.
2. **Probing for linguistic features.** Analysis of whether individual heads encode frame-semantic relations (using FrameNet), syntactic roles, and token-level features (nouns, verbs, pronouns, subjects, objects, negation).
3. **Head disabling experiments.** Systematic evaluation of model performance when individual heads or entire layers are disabled by replacing learned attention weights with uniform distributions.

---

## Approach Details

### Method

All experiments use bert-base-uncased (12-layer, 768-hidden, 12-heads, 110M parameters). For a given input of length L, each head in every layer produces an L x L self-attention weight matrix. The authors extract and analyze these matrices across seven GLUE tasks: MRPC, STS-B, SST-2, QQP, RTE, QNLI, and MNLI. Fine-tuning follows the original BERT parameters: batch size 32, 3 epochs.

### Key Technical Components

**Attention pattern taxonomy.** Manual inspection revealed five recurring self-attention map types:

| Pattern | Description |
|---|---|
| Vertical | Attention concentrated on [CLS] and [SEP] tokens |
| Diagonal | Attention to previous/following tokens |
| Vertical+Diagonal | Mixture of the above two |
| Block | Intra-sentence attention (for paired-sentence tasks) |
| Heterogeneous | Variable, input-dependent patterns |

A CNN classifier (8 convolutional layers, ReLU) was trained on ~400 manually annotated attention maps, achieving F1 = 0.86. This classifier was used to estimate the proportion of each pattern type across tasks using up to 1000 validation examples per task.

**Frame-semantic relation probing.** Using 473 filtered FrameNet sentences (frame elements <= 3 tokens, sentences <= 12 tokens, linked elements >= 2 tokens apart), the authors tested whether any of the 144 heads preferentially attend between frame-evoking predicates and their core frame elements.

**Attention to linguistic features.** For each head, the sum of attention weights assigned to tokens of a given type (nouns, verbs, pronouns, subjects, objects, negation, [CLS], [SEP]) from all other tokens was computed and normalized by sequence length.

**Head disabling.** Disabling a head means replacing its attention weights with a uniform distribution: `a = 1/L` for every token. This preserves the information flow of the original model while removing learned attention patterns. Any number of heads can be disabled simultaneously, from a single head to all 12 heads in a layer.

### Experimental Setup

**Model:** bert-base-uncased, 110M parameters, PyTorch implementation.

**Tasks (7 GLUE tasks):**

| Task | Type | Metric | Size |
|---|---|---|---|
| MRPC | Paraphrase detection | F1/Acc | 5.8K |
| STS-B | Semantic similarity | Acc | 8.6K |
| SST-2 | Sentiment analysis | Acc | 70K |
| QQP | Question pair detection | F1/Acc | 400K |
| RTE | Textual entailment | Acc | 2.7K |
| QNLI | QA-based NLI | Acc | 130K |
| MNLI-m | Multi-genre NLI | Acc | 440K |

### Key Results

**Attention pattern distribution.** The five pattern types are consistently repeated across heads and tasks. The estimated upper bound on "Heterogeneous" heads (those that could encode meaningful linguistic information) ranges from 32% (MRPC) to 61% (QQP). The remainder attends primarily to special tokens or adjacent tokens.

**Frame-semantic relations.** Only 2 out of 144 heads show attention patterns correlated with FrameNet frame-semantic relations. Their averaged maximum attention weights (0.201 and 0.209) exceed the 99th percentile of the distribution across all heads. However, these two heads do not appear to be important for any GLUE task -- disabling either one does not reduce accuracy.

**Fine-tuning changes.** For all tasks except QQP, the last two layers undergo the largest attention changes compared to pre-trained BERT (measured by cosine similarity of flattened attention weight arrays). Earlier layers remain largely unchanged. Fine-tuning improves performance by an average of 35.9 absolute points over pre-trained BERT.

| Initialization | MRPC (F1) | STS-B | SST-2 | QQP (F1) | RTE | QNLI | MNLI-m |
|---|---|---|---|---|---|---|---|
| Pre-trained (no fine-tuning) | 0 | 33.1 | 49.1 | 0 | 52.7 | 52.8 | 31.7 |
| Random init + fine-tuning | 81.2 | 2.9 | 80.5 | 0 | 52.7 | 49.5 | 61.0 |
| Pre-trained + fine-tuning | 87.9 | 82.7 | 92.0 | 65.2 | 64.6 | 84.4 | 78.6 |

**Attention to linguistic features.** The dominant vertical attention patterns correspond predominantly to [CLS] and [SEP] tokens, not to linguistically meaningful features. Earlier layers attend more to [CLS]; later layers attend more to [SEP]. Attention to nouns, direct objects, and negation tokens is detectable but negligible compared to [CLS] and [SEP] weights.

**Head disabling -- single heads:**

| Task | Baseline | Best (1 head disabled) | Gain |
|---|---|---|---|
| MRPC (F1/Acc) | 87.9/82.3 | 89.4/-- | +1.2 |
| STS-B | 88.9 | 89.1 | +0.1 |
| SST-2 | 92.0 | 93.8 | +0.2 |
| QQP (F1/Acc) | 65.2/78.6 | --/88.3 | -- |
| RTE | 59.6 | 61.7 | +3.2 (layer) |
| QNLI | 91.4 | 91.6 | +0.2 |
| MNLI-m | 83.9 | 84.1 | +0.2 |

- **Disabling certain heads improves performance on all tasks.** The gain ranges from +0.1% (STS-B) to +1.2% (MRPC) for single-head disabling.
- For MRPC and RTE, disabling a random head gives, on average, an increase in performance.
- **Disabling entire layers can also improve results.** Disabling the first layer in RTE yields a +3.2% absolute gain. However, for QNLI and MNLI, layer disabling produces drops of up to -0.2%.

**Cross-sentence word matching.** STS-B and RTE fine-tuned models both rely on the same pair of heads (head 1 in layer 4, head 12 in layer 2). Manual inspection reveals these heads assign high attention weights to words appearing in both input sentences, suggesting word-by-word comparison is a key strategy for these tasks.

### Limitations

- Analysis is limited to bert-base-uncased (12 layers). Larger BERT variants may exhibit different patterns.
- Only English is studied. The diagonal attention pattern may be less dominant in verb-final or free-word-order languages where dependent elements are not adjacent.
- The attention pattern taxonomy is coarse; "Heterogeneous" is a catch-all category that may contain further structure.
- Token-to-token attention experiments for noun-pronoun and verb-subject relations were confounded by the diagonal (adjacent-token) attention pattern, making it difficult to separate syntactic relations from proximity effects.

---

## Conclusions

1. **Limited set of recurring attention patterns.** BERT's 144 heads encode only five distinct attention pattern types, with many heads repeating the same patterns. This indicates significant overparameterization.

2. **Heterogeneous heads are a minority.** Only 32--61% of heads (depending on the task) produce potentially linguistically informative "Heterogeneous" patterns; the rest attend primarily to special tokens or adjacent tokens.

3. **Fine-tuning changes mainly the last two layers.** Cosine similarity analysis shows earlier layers remain close to the pre-trained model, while the last two layers encode task-specific features responsible for the large fine-tuning performance gains (average +35.9 points).

4. **Disabling heads can improve performance.** Across all seven GLUE tasks, there exist heads whose removal improves accuracy (up to +3.2% for disabling layer 1 in RTE). This provides direct evidence of overparameterization and suggests model pruning as a practical optimization direction.

5. **Frame-semantic heads are not task-critical.** The two heads (out of 144) that encode frame-semantic relations are not important for any GLUE task, implying that fine-tuned BERT does not rely on this form of semantic knowledge for classification.

6. **Vertical attention is driven by special tokens, not linguistic features.** The prominent vertical stripe patterns in attention maps correspond to [CLS] and [SEP] tokens rather than to nouns, verbs, or other linguistically meaningful categories.

---

## Core References and Why They Are Referenced

### Transformer and BERT Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduced the Transformer architecture and multi-head self-attention mechanism that is the subject of this paper's analysis.
- **Devlin et al. (2018)** -- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* The model being analyzed. Provides the pre-trained bert-base-uncased checkpoint and fine-tuning procedure used throughout.

### BERT Interpretability

- **Goldberg (2019)** -- *Assessing BERT's Syntactic Abilities.* Showed BERT can model subject-verb agreement; also observed that smaller BERT achieves better syntax scores, supporting the overparameterization finding.
- **Jawahar et al. (2019)** -- *What Does BERT Learn About the Structure of Language?* Extended Goldberg's work to multiple layers and tasks, showing intermediate layers capture rich linguistic information.
- **Liu et al. (2019)** -- *Linguistic Knowledge and Transferability of Contextual Representations.* Found that middle Transformer layers are most transferable and higher layers are less task-specific than in RNNs.
- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned.* Independently found that only a small subset of heads is important in the original Transformer on translation tasks, consistent with this paper's findings on BERT.
- **Michel et al. (2019)** -- *Are Sixteen Heads Really Better Than One?* Demonstrated that Transformer layers can be reduced to a single head without significant degradation, further supporting the overparameterization thesis.

### Neural Network Pruning

- **Frankle & Carbin (2018)** -- *The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks.* Showed complex architectures can be significantly reduced without performance loss, providing theoretical context for the head disabling experiments.

### Evaluation

- **Wang et al. (2018)** -- *GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding.* Provides the seven evaluation tasks used throughout the paper.
- **Baker et al. (1998)** -- *The Berkeley FrameNet Project.* Source of the frame-semantic annotations used to probe whether BERT heads encode predicate-argument relations.

#### Cross-References in Available Papers

This paper predates the long-context evaluation work in the references directory. However, its findings on attention pattern redundancy and overparameterization in Transformer models are foundational observations that inform later work on long-context behavior:

- **DRoPE (2025-12-drope-dropping-positional-embeddings):** DRoPE's technique of dropping positional embeddings at certain layers relates to this paper's finding that not all layers/heads contribute equally -- earlier layers capture low-level features while later layers encode task-specific patterns. Both papers demonstrate that Transformer components can be selectively modified or disabled without performance loss.
- **Lost in the Middle (2024-02-lost-in-the-middle):** This paper's observation that attention concentrates on [CLS]/[SEP] tokens (positional extremes of the input) is an early precursor to the lost-in-the-middle phenomenon, where models favor information at the beginning and end of long contexts.
- **Context Length Hurts Performance (2025-11-context-length-hurts-performance):** The finding that BERT's attention patterns are dominated by special tokens and adjacent-token patterns, with only a minority of heads encoding heterogeneous (potentially informative) patterns, provides mechanistic context for why scaling context length does not straightforwardly improve comprehension.
