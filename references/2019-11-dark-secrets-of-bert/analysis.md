---
title: "Revealing the Dark Secrets of BERT"
authors: "Kovaleva, Romanov, Rogers, Rumshisky"
year: 2019
venue: "EMNLP-IJCNLP 2019"
paper_type: conference-paper
categories: ["attention-analysis", "probing-and-analysis", "pruning-and-sparsity"]
scope: ["BERT-base-uncased", "GLUE tasks", "English"]
benchmarks_used: ["glue"]
models_introduced: []
models_evaluated: ["bert-base"]
key_claims:
  - id: C1
    claim: "BERT exhibits five recurring self-attention pattern types (Vertical, Diagonal, Vertical+Diagonal, Block, Heterogeneous) that repeat across heads and tasks"
    evidence: "Section 4.1, Figures 1-2, CNN classifier with F1=0.86"
    status: supported
  - id: C2
    claim: "The upper bound on potentially linguistically informative Heterogeneous heads ranges from 32% (MRPC) to 61% (QQP)"
    evidence: "Section 4.1, Figure 2"
    status: supported
  - id: C3
    claim: "Only 2 out of 144 heads encode information correlated with FrameNet frame-semantic relations, with averaged max attention weights of 0.201 and 0.209 (>99th percentile), and these heads are not important for any GLUE task"
    evidence: "Section 4.2, Section 5, Figure 3"
    status: supported
  - id: C4
    claim: "Fine-tuning primarily changes the last two BERT layers; fine-tuned BERT outperforms pre-trained BERT by an average of 35.9 absolute points on GLUE"
    evidence: "Section 4.3, Figure 5, Table 1"
    status: supported
  - id: C5
    claim: "Disabling certain attention heads improves performance on all seven GLUE tasks, with single-head gains from +0.1% (STS-B) to +1.2% (MRPC) and up to +3.2% from disabling layer 1 on RTE"
    evidence: "Section 4.6, Figures 8-9"
    status: supported
  - id: C6
    claim: "Vertical attention patterns correspond predominantly to [CLS] and [SEP] tokens rather than linguistically meaningful features such as nouns, verbs, or negation"
    evidence: "Section 4.4, Figure 6"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: evaluates
    detail: "Analyzes the self-attention mechanism from the Transformer architecture as instantiated in BERT"
  - target: 2019-07-specialized-attention-heads-pruning
    type: concurrent
    detail: "Both papers find most attention heads are dispensable; Voita et al. study the original Transformer on translation, Kovaleva et al. study BERT on GLUE"
  - target: 2019-08-bert-attention-analysis
    type: concurrent
    detail: "Both papers independently analyze BERT attention patterns; Clark et al. focus on syntactic dependency relations, Kovaleva et al. propose a five-class pattern taxonomy"
  - target: 2019-12-sixteen-heads-better-than-one
    type: concurrent
    detail: "Both papers demonstrate attention head redundancy; Michel et al. show layers can be reduced to a single head, Kovaleva et al. show disabling heads can improve performance"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer cites this work's finding that BERT attention is predominantly local to justify sliding window attention design"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "The finding that attention concentrates on [CLS] and [SEP] special tokens is thematically related to the attention sink phenomenon later identified in autoregressive LLMs"
  - target: 2023-12-landmark-attention-infinite-context
    type: complementary
    detail: "Landmark attention cites this work's finding that attention is predominantly local to motivate block-level rather than token-level retrieval"
  - target: 2019-06-bert-pretraining-language-understanding
    type: evaluates
    detail: "Analyzes self-attention patterns in the BERT model introduced by Devlin et al."
  - target: 2025-04-attention-sink-emerges
    type: complementary
    detail: "Gu et al. extend the finding that BERT attention concentrates on [CLS]/[SEP] to auto-regressive LMs, identifying softmax normalization as the mechanism underlying both BERT's vertical patterns and autoregressive attention sinks"
open_questions:
  - question: "Do the same five attention pattern types hold in verb-final languages and those with free word order, where subject-predicate relations would not coincide with adjacent-token patterns?"
    addressed_by: null
  - question: "What is the optimal sub-architecture for BERT after pruning redundant heads, and can pruning be automated?"
    addressed_by: null
  - question: "What wider range of semantic and syntactic relations beyond FrameNet are captured by individual BERT heads?"
    addressed_by: null
---

# Revealing the Dark Secrets of BERT

**Authors:** Olga Kovaleva, Alexey Romanov, Anna Rogers, Anna Rumshisky (University of Massachusetts Lowell)
**Date:** November 2019, EMNLP-IJCNLP 2019 (arXiv:1908.08593)

---

## Core Research Problem

BERT-based architectures achieve state-of-the-art performance on many NLP tasks, but the exact mechanisms that contribute to their success remain unclear. Self-attention is the fundamental component distinguishing Transformers from prior RNN-based architectures, yet little is known about what information individual attention heads encode, how attention patterns change during fine-tuning, and whether all 144 heads (12 layers × 12 heads) are necessary.

Prior work probed BERT's linguistic knowledge at the representation level: Goldberg (2019) tested subject-verb agreement, Jawahar et al. (2019) examined layer-wise linguistic structure, and Liu et al. (2019) studied transferability of contextual representations. However, none had systematically analyzed the self-attention mechanism itself across multiple tasks. Concurrently, work on neural network pruning (Frankle & Carbin, 2018) and head pruning (Voita et al., 2019; Michel et al., 2019) suggested Transformers are overparameterized, but the nature and distribution of redundant attention patterns had not been characterized for BERT.

**The core challenge is to understand what information BERT's individual self-attention heads encode, how this relates to linguistic structure, and whether the model's 144 heads are all necessary for downstream task performance.**

---

## Problem Solutions

The paper proposes a methodology for qualitative and quantitative analysis of BERT's self-attention weights, applied to bert-base-uncased across seven GLUE tasks.

1. **Taxonomy of attention patterns.** Classification of self-attention maps into five recurring types (Vertical, Diagonal, Vertical+Diagonal, Block, Heterogeneous) using a CNN classifier trained on ~400 manually annotated maps.
2. **Probing for linguistic features.** Analysis of whether individual heads encode frame-semantic relations (using FrameNet), and whether attention to specific token types (nouns, verbs, pronouns, subjects, objects, negation) is linguistically meaningful or dominated by special tokens.
3. **Head disabling experiments.** Systematic evaluation of model performance when individual heads or entire layers are disabled by replacing learned attention weights with uniform distributions.

---

## Approach Details

### Method

All experiments use bert-base-uncased (12-layer, 768-hidden, 12-heads, 110M parameters). For a given input of length L, each head in every layer produces an L × L self-attention weight matrix. The authors extract and analyze these matrices across seven GLUE tasks: MRPC, STS-B, SST-2, QQP, RTE, QNLI, and MNLI-m. Fine-tuning follows the original BERT parameters: batch size 32, 3 epochs (Section 3). Two GLUE tasks were excluded: CoLA (due to low human performance of 66.4 from methodological issues, and its exclusion from the upcoming SuperGLUE) and the Winograd Schema Challenge (due to small dataset size).

### Key Technical Components

**Attention pattern taxonomy.** Manual inspection revealed five recurring self-attention map types (Section 4.1, Figure 1):

| Pattern | Description |
|---|---|
| Vertical | Attention concentrated on [CLS] and [SEP] tokens |
| Diagonal | Attention to previous/following tokens |
| Vertical+Diagonal | Mixture of the above two |
| Block | Intra-sentence attention for paired-sentence tasks (e.g., RTE, MRPC) |
| Heterogeneous | Highly variable, input-dependent patterns with no distinct structure |

The Heterogeneous category is defined as the complement of the other four, making the taxonomy exhaustive. The authors hypothesize that Heterogeneous patterns are "more likely to capture interpretable linguistic features, necessary for language understanding" (Section 4.1). The first three types are attributed to language model pre-training.

A **CNN classifier** (8 convolutional layers, ReLU activations) was trained on ~400 manually annotated self-attention maps, achieving **F1 = 0.86** on the annotated dataset. The annotated data was somewhat unbalanced, with the Vertical class accounting for 30% of samples. This classifier was used to estimate the proportion of each pattern type across tasks using up to 1000 validation examples per task (Section 4.1).

**Frame-semantic relation probing.** Using 473 filtered FrameNet sentences (frame elements ≤ 3 tokens, sentences ≤ 12 tokens, linked elements ≥ 2 tokens apart), the authors tested whether any of the 144 pre-trained BERT heads preferentially attend between frame-evoking predicates and their core frame elements. For each sentence and each head, the maximum absolute attention weight among token pairs corresponding to the annotated semantic link was extracted, then averaged over all examples. This strategy identifies heads that prioritize features correlated with frame-semantic relations (Section 4.2).

**Attention to linguistic features.** For each head, the sum of attention weights assigned to a token of interest (nouns, verbs, pronouns, subjects, objects, negation, [CLS], [SEP]) from all other tokens was computed and normalized by sequence length. When multiple tokens of the same type were present, the maximum value was taken. Input sentences not containing a given feature were disregarded. Maps were compared between pre-trained and fine-tuned BERT to detect task-specific changes (Section 4.4).

**Token-to-token attention.** The authors investigated verb-subject and noun-pronoun attention patterns, as well as the attention distribution of the [CLS] token in the final layer, since BERT uses the [CLS] representation for classification (Section 4.5).

**Head disabling.** Disabling a head means replacing its attention weights with a uniform distribution:

> a = 1/L for every token

where L is the sentence length. This preserves the information flow of the original model while removing learned attention patterns. Any number of heads can be disabled simultaneously, from a single head to all 12 heads in a layer (Section 4.6).

### Experimental Setup

**Model:** bert-base-uncased, 110M parameters, PyTorch implementation (HuggingFace).

**Tasks (7 GLUE tasks):**

| Task | Type | Metric | Train Size |
|---|---|---|---|
| MRPC | Paraphrase detection | F1/Acc | 5.8K |
| STS-B | Semantic textual similarity | Acc | 8.6K |
| SST-2 | Sentiment analysis | Acc | 70K |
| QQP | Question pair detection | F1/Acc | 400K |
| RTE | Textual entailment | Acc | 2.7K |
| QNLI | QA-based NLI | Acc | 130K |
| MNLI-m | Multi-genre NLI (matched) | Acc | 440K |

**Fine-tuning:** Batch size 32, 3 epochs, following Devlin et al. (2018). All results are reported on the validation set (Section 3).

**Evaluation configurations for fine-tuning comparison (Section 4.3):**
1. Pre-trained BERT (no fine-tuning)
2. Random initialization + fine-tuning
3. Pre-trained initialization + fine-tuning

### Key Results

**Attention pattern distribution (Section 4.1, Figure 2).** The five pattern types are consistently repeated across different heads and tasks. The estimated upper bound on Heterogeneous heads (those that could encode meaningful linguistic information) varies by task:

| Task | Heterogeneous (upper bound) |
|---|---|
| MRPC | ~32% |
| QQP | ~61% |

MRPC has the lowest and QQP the highest proportion of Heterogeneous heads. The remaining heads attend primarily to special tokens, adjacent tokens, or intra-sentence boundaries (Figure 2).

**Frame-semantic relations (Section 4.2, Figure 3).** Only **2 out of 144 heads** show attention patterns correlated with FrameNet frame-semantic relations. Their averaged maximum attention weights (**0.201 and 0.209**) exceed the 99th percentile of the distribution across all heads. Both heads show high attention weight between frame-evoking predicates and their experiencers (e.g., high weight for "he" while processing "agitated" in "He was becoming agitated," frame "Emotion_directed"). However, these two heads do not appear important for any GLUE task -- disabling either one does not reduce accuracy (Section 5).

**Fine-tuning changes (Section 4.3, Figure 5, Table 1).** For all tasks except QQP, the last two layers undergo the largest attention changes compared to pre-trained BERT (measured by cosine similarity of flattened attention weight arrays). Fine-tuned BERT outperforms pre-trained BERT by an average of **35.9 absolute points**.

| Initialization | MRPC (F1/Acc) | STS-B | SST-2 | QQP (F1/Acc) | RTE | QNLI | MNLI-m |
|---|---|---|---|---|---|---|---|
| Pre-trained (no fine-tuning) | 0/31.6 | 33.1 | 49.1 | 0/60.9 | 52.7 | 52.8 | 31.7 |
| Random init + fine-tuning | 81.2/68.3 | 2.9 | 80.5 | 0/63.2 | 52.7 | 49.5 | 61.0 |
| Pre-trained + fine-tuning | 87.9/82.3 | 82.7 | 92.0 | 65.2/78.6 | 64.6 | 84.4 | 78.6 |

Random initialization + fine-tuning consistently produces lower scores than pre-trained + fine-tuning. For STS-B and QNLI, random initialization yields worse performance than pre-trained BERT without any fine-tuning, indicating that pre-trained weights contain linguistic knowledge essential for these tasks (Table 1).

**Attention to linguistic features (Section 4.4, Figure 6).** The dominant vertical attention patterns correspond predominantly to **[CLS] and [SEP] tokens, not linguistically meaningful features**. There is a consistent cross-task trend: earlier layers attend more to [CLS], later layers attend more to [SEP]. The SST-2 task shows higher absolute [SEP] weights because its inputs contain only one sentence (one [SEP] token instead of two).

Fine-tuning does produce some increased attention to nouns and direct objects (MRPC, RTE, QQP) and negation tokens (QNLI), but these weights remain negligible compared to special tokens. The authors conclude that "the striped attention maps generally come from BERT pre-training tasks rather than from task-specific linguistic reasoning" (Section 4.4).

**Token-to-token attention (Section 4.5, Figure 7).** Investigations of noun-pronoun and verb-subject attention links coincided with diagonally structured attention maps. The authors attribute this to English syntax where dependent elements frequently appear adjacent, making it difficult to distinguish syntactic relations from the diagonal (previous/following token) pattern. For the [CLS] token in the output layer, [SEP] receives the most attention for most tasks except STS-B, RTE, and QNLI, where punctuation tokens receive the greatest attention.

**Head disabling -- single heads (Section 4.6, Figure 8):**

Disabling certain heads improves performance on **all seven GLUE tasks**. The gain ranges from +0.1% (STS-B) to +1.2% (MRPC) for single-head disabling:

| Task | Baseline | Best (1 head disabled) | Gain |
|---|---|---|---|
| MRPC (F1/Acc) | 87.9/82.3 | 89.4/-- | +1.2 |
| STS-B | 88.9 | 89.1 | +0.1 |
| SST-2 | 92.0 | 93.8 | +0.2 |
| QQP (Acc) | 78.6 | 88.3 | -- |
| RTE | 59.6 | 61.7 | +2.1 |
| QNLI | 91.4 | 91.6 | +0.2 |
| MNLI-m | 83.9 | 84.1 | +0.2 |

- For MRPC and RTE, disabling a random head gives, on average, an increase in performance (Section 4.6).

**Head disabling -- whole layers (Section 4.6, Figure 9):**

Disabling all 12 heads in a given layer also improves results in some configurations. Notably, disabling the first layer in RTE yields an **absolute performance gain of 3.2%**. However, for QNLI and MNLI, layer disabling produces drops of up to **-0.2%**.

**Cross-sentence word matching (Section 5).** Both STS-B and RTE fine-tuned models rely on the same pair of heads: **head 1 in layer 4** and **head 12 in layer 2**. Manual inspection reveals these heads assign high attention weights to words appearing in both input sentences, suggesting a word-by-word comparison strategy for these tasks. The authors were not able to find a conceptually similar interpretation of heads important for other tasks.

---

## Limitations and Failure Modes

- **Single model, single size.** Analysis is limited to bert-base-uncased (12 layers, 110M parameters). Larger BERT variants (e.g., bert-large with 24 layers and 16 heads) may exhibit different patterns (Section 6).
- **English only.** The diagonal attention pattern may be less dominant in verb-final or free-word-order languages where dependent elements are not adjacent. The authors note English may have "relatively lower variety of self-attention patterns, as the subject-predicate relation happens to coincide with the following-previous token pattern" (Section 6).
- **Coarse taxonomy.** The Heterogeneous category is a catch-all for patterns not matching the other four classes and may contain further sub-structure that the classification approach cannot distinguish.
- **Adjacency confound in probing.** Token-to-token experiments for noun-pronoun and verb-subject relations were confounded by the diagonal (adjacent-token) attention pattern, making it impossible to separate syntactic relations from proximity effects (Section 4.5).
- **Limited FrameNet probing scope.** Only frame-semantic relations from FrameNet were probed; other types of syntactic and semantic relations may be captured differently. The authors note "a wider range of relations remains to be investigated" (Section 4.2).
- **CNN classifier accuracy.** The attention pattern classifier achieves F1 = 0.86, meaning approximately 14% of attention maps may be misclassified, introducing noise into the pattern distribution estimates.
- **No automated pruning method.** The paper demonstrates that disabling heads can help but does not propose an automated pruning procedure or optimized sub-architecture.

---

## Conclusions

### Contributions

1. **Five-class attention pattern taxonomy.** Established that BERT's 144 heads encode only five distinct attention pattern types, with many heads repeating the same patterns across tasks. A CNN classifier (F1 = 0.86) enables automated classification of attention maps (Section 4.1, Figures 1-2).

2. **Quantified overparameterization via Heterogeneous head analysis.** Showed that only 32-61% of heads produce potentially linguistically informative patterns; the remainder attend primarily to special tokens or adjacent tokens (Section 4.1, Figure 2).

3. **Fine-tuning localizes to the last two layers.** Demonstrated via cosine similarity analysis that earlier layers remain close to the pre-trained model while the last two layers encode task-specific features responsible for the average 35.9-point fine-tuning gain (Section 4.3, Figure 5, Table 1).

4. **Head disabling as evidence of overparameterization.** Showed that disabling individual heads or entire layers can improve performance on all seven GLUE tasks, with gains up to +3.2% absolute (Section 4.6, Figures 8-9).

5. **[CLS]/[SEP] dominance in vertical attention.** Established that the prominent vertical stripe patterns in attention maps correspond to special tokens rather than linguistically meaningful categories (Section 4.4, Figure 6).

6. **Frame-semantic heads are dispensable.** Identified two heads (out of 144) encoding FrameNet-correlated information, but showed they are not important for any GLUE task (Sections 4.2, 5, Figure 3).

### Implications

1. **Model pruning direction.** The redundancy across heads suggests that BERT can be significantly compressed through attention head pruning without performance loss, and potentially with performance gains. This supports the broader overparameterization thesis of Frankle & Carbin (2018).

2. **Pre-trained representations are essential.** The large performance gap between random-init fine-tuning and pre-trained fine-tuning (Table 1) indicates that BERT's pre-trained representations contain linguistic knowledge that cannot be easily recovered through task-specific fine-tuning alone. For STS-B and QNLI, random-init fine-tuning performs worse than pre-trained BERT with no fine-tuning at all.

3. **Attention maps may not reflect linguistic reasoning.** The dominance of [CLS]/[SEP] patterns and the dispensability of frame-semantic heads suggest that BERT's attention mechanism may not directly encode the linguistic knowledge that drives its performance. [Inference: this implication is consistent with the findings but not explicitly stated by the authors.]

---

## Key Claims

1. **C1: Five recurring attention patterns.** BERT exhibits five self-attention pattern types (Vertical, Diagonal, Vertical+Diagonal, Block, Heterogeneous) that repeat across different heads and tasks. A CNN classifier trained on ~400 annotated maps achieves F1 = 0.86 (Section 4.1, Figures 1-2). **Status: supported.**

2. **C2: Heterogeneous heads are a minority.** The estimated upper bound on potentially linguistically informative Heterogeneous heads ranges from 32% (MRPC) to 61% (QQP) depending on the task (Section 4.1, Figure 2). **Status: supported.**

3. **C3: Frame-semantic heads are not task-critical.** Only 2 out of 144 pre-trained BERT heads encode information correlated with FrameNet relations (averaged max attention weights 0.201 and 0.209, >99th percentile), but disabling either head does not reduce accuracy on any GLUE task (Sections 4.2, 5, Figure 3). **Status: supported.**

4. **C4: Fine-tuning changes mainly the last two layers.** Cosine similarity analysis shows the last two layers undergo the largest attention changes during fine-tuning (except for QQP). Fine-tuned BERT outperforms pre-trained BERT by an average of 35.9 absolute points across seven GLUE tasks (Section 4.3, Figure 5, Table 1). **Status: supported.**

5. **C5: Disabling heads can improve performance.** Across all seven GLUE tasks, there exist heads whose removal improves accuracy. Single-head gains range from +0.1% (STS-B) to +1.2% (MRPC); disabling layer 1 in RTE yields +3.2% absolute gain. For MRPC and RTE, disabling a random head on average improves performance (Section 4.6, Figures 8-9). **Status: supported.**

6. **C6: Vertical attention is driven by special tokens.** The prominent vertical stripe patterns in attention maps correspond to [CLS] and [SEP] tokens rather than linguistically meaningful features. Earlier layers attend more to [CLS], later layers to [SEP]. Attention to nouns, objects, and negation is detectable but negligible compared to special tokens (Section 4.4, Figure 6). **Status: supported.**

---

## Open Questions

1. **Cross-linguistic attention patterns.** Do the same five attention pattern types hold in verb-final languages (e.g., Japanese, Korean) and those with free word order (e.g., Russian, Finnish), where subject-predicate relations would not coincide with adjacent-token patterns? The authors note English may have "relatively lower variety of self-attention patterns" due to this confound (Section 6). *Unresolved.*

2. **Optimal pruned sub-architecture.** What is the minimal subset of heads that preserves or improves performance for each task, and can this be determined automatically? The paper demonstrates the potential but does not propose an automated method (Section 6). *Unresolved.*

3. **Broader relation probing.** What range of semantic and syntactic relations beyond FrameNet frame-semantics are captured by individual BERT heads? The authors note "a wider range of relations remains to be investigated" (Section 4.2). *Unresolved.*

---

## Core References and Why They Are Referenced

### Transformer and BERT Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduced the Transformer architecture and multi-head self-attention mechanism that is the subject of this paper's analysis.
- **Devlin et al. (2018)** -- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* The model being analyzed. Provides the pre-trained bert-base-uncased checkpoint, fine-tuning procedure, and hyperparameters used throughout.

### BERT Interpretability and Probing

- **Goldberg (2019)** -- *Assessing BERT's Syntactic Abilities.* Demonstrated BERT models subject-verb agreement; also observed that smaller BERT achieves better syntax scores, supporting the overparameterization finding.
- **Jawahar et al. (2019)** -- *What Does BERT Learn About the Structure of Language?* Extended Goldberg's work to multiple layers and tasks, supporting the claim that BERT's intermediate layers capture rich linguistic information.
- **Liu et al. (2019)** -- *Linguistic Knowledge and Transferability of Contextual Representations.* Found that middle Transformer layers are most transferable and higher layers are less task-specific than RNNs, consistent with the fine-tuning localization finding in this paper.
- **Tang et al. (2018)** -- *Why Self-Attention? A Targeted Evaluation of Neural Machine Translation Architectures.* Argued that self-attention models outperform CNN- and RNN-based models on word sense disambiguation due to their ability to extract semantic features.

### Attention Head Pruning and Overparameterization

- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned.* Independently found that only a small subset of heads is important in the original Transformer on translation tasks, consistent with this paper's findings on BERT.
- **Michel et al. (2019)** -- *Are Sixteen Heads Really Better Than One?* Demonstrated that Transformer layers can be reduced to a single head without significant degradation, further supporting the overparameterization thesis.
- **Frankle & Carbin (2018)** -- *The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks.* Showed complex architectures can be significantly reduced without performance loss, providing theoretical context for the head disabling experiments.
- **Adhikari et al. (2019)** -- *Rethinking Complex Neural Network Architectures for Document Classification.* Showed a simple BiLSTM without attention achieves competitive results on document classification, questioning the necessity of complex architectures.
- **Wu et al. (2019)** -- *Pay Less Attention with Lightweight and Dynamic Convolutions.* Proposed a more lightweight convolution-based architecture that outperforms self-attention, providing further evidence of unnecessary complexity in the self-attention mechanism.

### Evaluation and Linguistic Resources

- **Wang et al. (2018)** -- *GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding.* Provides the seven evaluation tasks used throughout the paper.
- **Baker et al. (1998)** -- *The Berkeley FrameNet Project.* Source of the frame-semantic annotations used to probe whether BERT heads encode predicate-argument relations.

### Transfer Learning

- **Yosinski et al. (2014)** -- *How Transferable Are Features in Deep Neural Networks?* Results on fine-tuning pre-trained ConvNets on ImageNet provide context for understanding BERT's layer-wise fine-tuning behavior.
- **Romanov & Shivade (2018)** -- *Lessons from Natural Language Inference in the Clinical Domain.* Results on transfer learning for medical NLI support the finding that pre-trained representations are essential for downstream tasks.
