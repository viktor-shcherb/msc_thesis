---
title: "What Does BERT Look At? An Analysis of BERT's Attention"
authors: "Clark, Khandelwal, Levy, Manning"
year: 2019
venue: "BlackboxNLP Workshop at ACL 2019"
paper_type: workshop-paper
categories: ["attention-analysis", "probing-and-analysis"]
scope: ["BERT-base (uncased)", "English text"]
benchmarks_used: ["penn-treebank", "conll-coreference"]
models_introduced: []
models_evaluated: ["bert-base"]
key_claims:
  - id: C1
    claim: "Individual BERT attention heads specialize to specific dependency relations with high accuracy (det 94.3%, dobj 86.8%, auxpass 82.5%, poss 80.5%)"
    evidence: "Table 1, Section 4.2"
    status: supported
    scope: "BERT-base (uncased), English WSJ, Stanford Dependencies"
    magnitude: "det 94.3%, dobj 86.8%, auxpass 82.5%, poss 80.5%"
  - id: C2
    claim: "Attention to [SEP] tokens functions as a learned no-op mechanism when a head's specialized function is not applicable"
    evidence: "Section 3.2, Figures 2-3, Figure 5"
    status: supported
    scope: "BERT-base (uncased), layers 6-10"
  - id: C3
    claim: "An attention-based probing classifier achieves 77 UAS at dependency parsing, showing substantial syntactic information in BERT's attention maps"
    evidence: "Table 3, Section 5"
    status: supported
    scope: "PTB dev set, Stanford Dependencies"
    magnitude: "77 UAS (vs. 58 UAS best baseline)"
  - id: C4
    claim: "A single attention head (5-4) achieves 65% antecedent selection accuracy on CoNLL-2012 coreference, outperforming string-matching baselines by >10 points"
    evidence: "Table 2, Section 4.3"
    status: supported
    scope: "CoNLL-2012, documents truncated to 128 tokens"
    magnitude: "65% accuracy, >10 points over string-matching baseline"
  - id: C5
    claim: "Attention heads in the same layer tend to exhibit similar behavior, as shown by Jensen-Shannon Divergence clustering"
    evidence: "Section 6, Figure 6"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Analyzes attention in BERT, which is built on the Transformer encoder architecture"
  - target: 2019-07-specialized-attention-heads-pruning
    type: concurrent
    detail: "Both study specialized attention heads; Clark et al. focus on BERT while Voita et al. study NMT encoders"
  - target: 2019-11-dark-secrets-of-bert
    type: complementary
    detail: "Kovaleva et al. extend this attention analysis with a broader pattern taxonomy across GLUE tasks in BERT"
  - target: 2019-12-sixteen-heads-better-than-one
    type: concurrent
    detail: "Michel et al. show many BERT heads can be pruned; the important surviving heads tend to be those with identified behaviors, consistent with this paper's findings"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer cites this work's finding of strong local bias in BERT attention to motivate copy initialization of position embeddings when extending from 512 to 4,096 positions"
  - target: 2022-03-in-context-learning-induction-heads
    type: complementary
    detail: "Olsson et al. extend attention head analysis to autoregressive models, identifying induction heads as specialized circuits for in-context learning; both papers establish that individual attention heads develop specialized functions"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Both address how Transformers distribute attention across positions; Clark et al. find positional biases in BERT heads that foreshadow the positional biases in context utilization"
  - target: 2018-07-sharp-nearby-fuzzy-far-away
    type: extends
    detail: "Extends the context utilization analysis from LSTMs to BERT attention patterns, finding positional biases that echo the nearby-vs-far distinction; Khandelwal is a co-author on both papers"
  - target: 2019-06-bert-pretraining-language-understanding
    type: evaluates
    detail: "Analyzes the attention heads of the BERT model introduced by Devlin et al."
open_questions:
  - question: "Do the same syntactic head specializations emerge in other languages beyond English?"
    addressed_by: null
  - question: "What is the functional role of the many attention heads without identified interpretable behaviors?"
    addressed_by: 2019-12-sixteen-heads-better-than-one
  - question: "Why do heads within the same layer develop similar attention distributions despite multi-head attention being designed for diversity?"
    addressed_by: null
  - question: "Does BERT-large exhibit the same pattern of head specialization as BERT-base?"
    addressed_by: null
---

# What Does BERT Look At? An Analysis of BERT's Attention

**Authors:** Kevin Clark, Urvashi Khandelwal, Omer Levy, Christopher D. Manning (Stanford University, Facebook AI Research)
**Date:** August 2019, BlackboxNLP Workshop at ACL 2019, DOI:10.18653/v1/W19-4828 (arXiv:1906.04341)

---

## Core Research Problem

Large pre-trained neural networks such as BERT achieve strong performance across NLP tasks when fine-tuned, but it is not fully understood what linguistic knowledge they acquire from unlabeled data. Most prior analysis has focused on either model outputs -- e.g., evaluating language model surprisal on carefully constructed inputs to test subject-verb agreement (Linzen et al., 2016; Gulordava et al., 2018) -- or internal vector representations using probing classifiers (Adi et al., 2017; Belinkov et al., 2017; Tenney et al., 2018, 2019; Liu et al., 2019). These approaches cannot directly reveal what role attention mechanisms play in encoding linguistic structure. Attention weights have a natural interpretation (how much a particular word is weighted when computing the next representation for another word), yet prior work on attention and syntax (Raganato and Tiedemann, 2018; Marecek and Rosa, 2018) only reported aggregate results without investigating individual heads for specific relations or using probing classifiers. The core challenge is: **characterizing what linguistic knowledge is captured in the attention maps of pre-trained Transformers, and whether individual attention heads learn to perform specific syntactic and semantic functions without explicit supervision.**

---

## Problem Solutions

The paper proposes a set of analysis methods for attention mechanisms and applies them to BERT-base (12 layers, 12 heads each, 144 heads total). The key contributions are:

1. **Surface-level attention pattern taxonomy:** A systematic characterization of how BERT's 144 attention heads behave, identifying patterns such as attending to delimiter tokens ([SEP], [CLS]), specific positional offsets (next/previous token), punctuation, and broad bag-of-words-like attention.
2. **Head-level probing for syntax and coreference:** Treating each attention head as a zero-parameter classifier (most-attended-to word = prediction) and evaluating on dependency parsing and coreference resolution, revealing that specific heads specialize to specific linguistic relations with high accuracy.
3. **Attention-based probing classifiers:** A novel family of probing classifiers that take attention maps (rather than hidden states) as input, achieving 77 UAS at dependency parsing and demonstrating that substantial syntactic information is captured in BERT's attention.

---

## Approach Details

### Method

The analysis uses BERT-base (uncased), which has 12 layers with 12 attention heads each (144 heads total). Attention heads are denoted `<layer>-<head>`. The standard Transformer attention computation is:

> alpha_ij = exp(q_i^T k_j) / sum_l exp(q_i^T k_l)

> o_i = sum_j alpha_ij v_j

where q_i, k_j, v_j are the query, key, and value vectors obtained by linear transformations of the input vectors h_i.

The analysis proceeds in four stages: (1) surface-level pattern analysis, (2) probing individual heads for dependency syntax, (3) probing individual heads for coreference resolution, and (4) training attention-based probing classifiers over head combinations.

**Token-to-word conversion:** Since BERT uses byte-pair tokenization (~8% of words are split into multiple tokens), token-token attention maps are converted to word-word maps. For attention *to* a split word, attention weights over its tokens are summed. For attention *from* a split word, attention weights over its tokens are averaged. These transformations preserve the property that attention from each word sums to 1.

### Key Technical Components

#### Surface-Level Attention Patterns (Section 3)

Attention maps are extracted over 1000 random Wikipedia segments (at most 128 tokens each, formatted as `[CLS]<paragraph-1>[SEP]<paragraph-2>[SEP]`). Input words are not masked out, unlike during BERT's training.

**Relative position patterns (Section 3.1):**
- Most heads put little attention on the current token.
- Four heads (in layers 2, 4, 7, and 8) on average put >50% of their attention on the previous token.
- Five heads (in layers 1, 2, 2, 3, and 6) put >50% of their attention on the next token.
- These positional heads are concentrated in earlier layers.

**Attending to separator tokens (Section 3.2):**
- Over half of BERT's attention in layers 6--10 focuses on [SEP] (expected baseline: ~1/64 for a token appearing twice in 128 tokens) (Figure 2).
- Early heads (layers 1--2) attend to [CLS]; middle heads (layers 6--10) attend to [SEP]; deep heads (layers 11--12) attend to periods and commas (Figure 2).
- [SEP] tokens attend to themselves and each other with more than 90% of attention weight (Figure 2, bottom).
- Gradient-based feature importance (gradient of masked language modeling loss with respect to attention weights; Sundararajan et al., 2017) shows that starting in layer 5, gradients for attention to [SEP] become very small, indicating that changing attention to [SEP] does not substantially change BERT's outputs (Figure 3).
- The authors hypothesize that attention to [SEP] serves as a **"no-op"**: when a head's specialized function is not applicable to a given token, the head defaults to attending to [SEP]. A similar pattern occurs for the uncased model, suggesting a systematic cause rather than a training artifact.

**Focused vs. broad attention (Section 3.3):**
- Attention entropy varies substantially across heads (Figure 4). Some lower-layer heads have very high entropy (near-uniform attention), producing bag-of-vectors representations.
- The [CLS] token in the last layer has high entropy (3.89 nats), consistent with its role in aggregating a whole-input representation for next sentence prediction.

#### Probing Individual Heads for Dependency Syntax (Section 4.2)

Attention maps are extracted on the Wall Street Journal portion of the Penn Treebank annotated with Stanford Dependencies. For each attention head and each word, whichever other word receives the highest attention weight is taken as the prediction (ignoring [SEP] and [CLS]). Both directions are evaluated: head word attending to dependent, and dependent attending to head word.

#### Probing Individual Heads for Coreference (Section 4.3)

Attention heads are evaluated on the CoNLL-2012 coreference dataset (documents truncated to 128 tokens). Antecedent selection accuracy is measured: what percent of the time does the head word of a coreferent mention most attend to the head of one of that mention's antecedents.

#### Attention-Based Probing Classifiers (Section 5)

Two probing classifiers are proposed for dependency parsing. BERT attention outputs are treated as fixed (no backpropagation into BERT).

**Attention-Only Probe:**

> p(i|j) proportional to exp( sum_k w_k alpha^k_ij + u_k alpha^k_ji )

where p(i|j) is the probability of word i being word j's syntactic head, alpha^k_ij is the attention weight from word i to word j in head k, and w, u are learned weight vectors. Both directions of attention are included.

**Attention-and-Words Probe:**

> p(i|j) proportional to exp( sum_k W_{k,:}(v_i + v_j) alpha^k_ij + U_{k,:}(v_i + v_j) alpha^k_ji )

where v denotes GloVe embeddings (held fixed), + denotes concatenation, and W, U are learned weight matrices. The dot product W_{k,:}(v_i + v_j) produces a word-sensitive weight for each attention head, allowing the classifier to, e.g., upweight the determiner head (8-11) when the input words are "the" and "cat."

#### Head Clustering (Section 6)

Distances between all pairs of attention heads are computed using Jensen-Shannon Divergence over their attention distributions across all tokens. Multidimensional scaling (Kruskal, 1964) embeds heads in two dimensions for visualization.

### Experimental Setup

**Model:** BERT-base (uncased), 12 layers, 12 heads, 110M parameters, pre-trained on 3.3 billion tokens of English text (BooksCorpus + Wikipedia) with masked language modeling and next sentence prediction.

**Evaluation data:**
- Surface-level patterns: 1000 random Wikipedia segments (at most 128 tokens each).
- Dependency syntax: Wall Street Journal portion of Penn Treebank with Stanford Dependencies.
- Coreference: CoNLL-2012 dataset (documents truncated to 128 tokens).
- Probing classifiers: Penn Treebank dev set with Stanford Dependencies.

**Baselines:**
- Dependency parsing: fixed-offset baselines (e.g., always predict word at offset -1 or +1), right-branching baseline (26.3 UAS).
- Coreference: nearest mention (27%), head-word match (52%), rule-based sieve system inspired by Lee et al. (2011) with 4 sieves -- full string match, head word match, number/gender/person match, all other mentions -- (69%), neural coreference system from Wiseman et al. (2015) (83%, on non-truncated documents with different mention detection).
- Probing classifiers: GloVe-only network with distance features (58 UAS), randomly initialized BERT attention + GloVe (30 UAS).

**Reproducibility:** Code is publicly available at https://github.com/clarkkev/attention-analysis. No random seeds are reported for the probing classifier training. Attention extraction is deterministic given the pre-trained model.

### Key Results

**Individual attention heads on dependency relations (Table 1):**

| Relation | Best Head | Accuracy | Fixed-Offset Baseline |
|---|---|---|---|
| All (overall) | 7-6 | 34.5 | 26.3 (offset +1) |
| prep | 7-4 | 66.7 | 61.8 (offset -1) |
| pobj | 9-6 | **76.3** | 34.6 (offset -2) |
| det | 8-11 | **94.3** | 51.7 (offset +1) |
| nn | 4-10 | 70.4 | 70.2 (offset +1) |
| nsubj | 8-2 | 58.5 | 45.5 (offset +1) |
| amod | 4-10 | 75.6 | 68.3 (offset +1) |
| dobj | 8-10 | **86.8** | 40.0 (offset -2) |
| advmod | 7-6 | 48.8 | 40.2 (offset +1) |
| aux | 4-10 | 81.1 | 71.5 (offset +1) |
| poss | 7-6 | **80.5** | 47.7 (offset +1) |
| auxpass | 4-10 | **82.5** | 40.5 (offset +1) |
| ccomp | 8-1 | **48.8** | 12.4 (offset -2) |
| mark | 8-2 | **50.7** | 14.5 (offset +2) |
| prt | 6-7 | **99.1** | 91.4 (offset -1) |

- The table shows the 10 most common relations plus 5 others where attention heads do particularly well (Table 1 caption).
- For all relations except pobj, the dependent attends to the head word (not the reverse), likely because each dependent has exactly one head while heads have multiple dependents (Section 4.2).
- No single head performs well at syntax overall (best: 34.5 UAS), but specific heads specialize to specific relations with remarkably high accuracy.
- Several heads substantially outperform the fixed-offset baseline, demonstrating they capture non-trivial syntactic patterns beyond simple positional heuristics.
- Heads can disagree with standard annotation conventions while still performing syntactic behavior: head 7-6 marks 's as the dependent for poss, while gold labels mark the complement of 's as the dependent (Section 4.2).

**Coreference resolution (Table 2):**

| Model | All | Pronoun | Proper | Nominal |
|---|---|---|---|---|
| Nearest mention | 27% | 29% | 29% | 19% |
| Head word match | 52% | 47% | 67% | 40% |
| Rule-based sieve | 69% | 70% | 77% | 60% |
| Neural coref* | 83% | -- | -- | -- |
| BERT Head 5-4 | **65%** | **64%** | **73%** | **58%** |

*\*Only roughly comparable: non-truncated documents, different mention detection.*

- Head 5-4 improves over the string-matching baseline by >10 points and approaches the rule-based system (Section 4.3).
- It is particularly effective on nominal mentions, suggesting capacity for fuzzy matching between synonyms (Section 4.3, Figure 5).

**Attention-based probing classifiers for dependency parsing (Table 3):**

| Model | UAS |
|---|---|
| Structural probe (Hewitt and Manning, 2019)* | 80 UUAS |
| Right-branching | 26 |
| Distances + GloVe | 58 |
| Random Init Attn + GloVe | 30 |
| Attn (attention-only) | 61 |
| Attn + GloVe | **77** |

*\*Not directly comparable: single layer, undirected trees, syntactic distance rather than direct tree prediction.*

- The Attn + GloVe probing classifier substantially outperforms all baselines (Table 3).
- The randomly initialized BERT baseline (30 UAS) confirms that the syntactic information comes from pre-trained attention weights, not merely from the word embeddings or positional encodings (Section 5).
- The similarity to the structural probe score (80 UUAS) suggests there is not much more syntactic information in BERT's vector representations compared to its attention maps, though the scores are not directly comparable (Section 5).

### Attention Head Clustering

- Jensen-Shannon Divergence-based clustering reveals clear behavioral groups: heads that attend broadly, attend to next/previous token, attend to [CLS], attend to [SEP], and attend to punctuation (Figure 6).
- Heads within the same layer tend to cluster together, indicating similar behavior within layers (Figure 6).
- The authors suggest this apparent redundancy may relate to attention dropout during training, which zeros out some attention weights and may encourage multiple heads to develop similar functions (Section 6).

---

## Limitations and Failure Modes

1. **Only BERT-base (uncased) analyzed.** The paper does not examine BERT-large or other Transformer architectures. It is unknown whether the same head specializations emerge in larger or differently-trained models.
2. **English-only evaluation.** All dependency and coreference evaluations use English data (Penn Treebank, CoNLL-2012). The authors explicitly note extending the analysis to other languages as future work (Section 4.2).
3. **No single head captures syntax overall.** The best individual head achieves only 34.5 UAS overall, barely above the right-branching baseline (26.3). Many dependency relations show only modest improvement over simple fixed-offset baselines (Table 1).
4. **Coreference documents truncated to 128 tokens.** This truncation limits the evaluation to short-range coreference links and prevents direct comparison with standard coreference systems that operate on full documents (Section 4.3, footnote 4).
5. **Attention as explanation vs. attention as information.** As noted by Jain and Wallace (2019, discussed in Section 7), attention weights do not always explain model predictions and can often be substantially changed without altering outputs. The authors acknowledge this concern but argue their goal is understanding what information attention learns, not explaining predictions.
6. **Interpretable behaviors found in only a subset of heads.** The paper identifies specific functions for a minority of BERT's 144 attention heads. The functional role of the remaining heads is unclear, though concurrent pruning work (Voita et al., 2019; Michel et al., 2019) suggests some may have minimal effect on performance.

---

## Conclusions

### Contributions

1. **Systematic attention pattern taxonomy.** Established that BERT's 144 attention heads exhibit organized surface-level patterns: positional offset attention (next/previous token in early layers), delimiter attention ([SEP] in middle layers, punctuation in late layers), and broad bag-of-vectors attention (Section 3, Figures 1--4).
2. **Head-level syntactic specialization.** Demonstrated that individual attention heads specialize to specific dependency relations without syntactic supervision, achieving remarkably high accuracy: 94.3% for determiners (head 8-11), 86.8% for direct objects (head 8-10), 82.5% for passive auxiliaries (head 4-10), 80.5% for possessives (head 7-6) (Table 1, Section 4.2).
3. **Coreference in attention.** Showed that head 5-4 achieves 65% antecedent selection accuracy on CoNLL-2012 coreference data, outperforming string-matching baselines by >10 points and approaching a rule-based system (69%) (Table 2, Section 4.3).
4. **Attention-based probing classifiers.** Introduced probing classifiers that take attention maps as input, achieving 77 UAS at dependency parsing, comparable to probing classifiers over BERT's hidden states (80 UUAS, not directly comparable) (Table 3, Section 5).
5. **[SEP]-as-no-op hypothesis.** Provided evidence from gradient analysis that attention to [SEP] in middle layers has near-zero effect on model outputs, supporting the interpretation that [SEP] serves as a no-op target for heads whose function is not applicable (Section 3.2, Figure 3).

### Implications

1. **Attention maps as a complementary analysis tool.** Probing attention maps provides insights distinct from probing hidden states or evaluating model outputs, and should be part of the standard toolkit for understanding what neural networks learn about language. [Inference: the extent to which attention-based probing is preferable to hidden-state probing remains an open methodological question.]
2. **Syntax-aware attention already exists in BERT.** Several works have proposed incorporating syntactic information to improve attention (Eriguchi et al., 2016; Chen et al., 2018; Strubell et al., 2018). This paper suggests that such syntax-aware attention already exists in BERT to an extent, which may partly explain its success (Section 1).
3. **Self-supervised training can produce linguistically-structured attention.** The emergence of syntactically-specialized heads from masked language modeling and next sentence prediction, without explicit syntactic supervision, suggests that rich self-supervised objectives on sufficient data can induce hierarchical linguistic structure (Section 8).

---

## Key Claims

1. **C1: Individual heads specialize to specific dependency relations.** Certain attention heads achieve high accuracy at specific dependency relations: det 94.3% (head 8-11), dobj 86.8% (head 8-10), auxpass 82.5% (head 4-10), poss 80.5% (head 7-6), pobj 76.3% (head 9-6) (Table 1, Section 4.2). Status: **supported**.

2. **C2: [SEP] attention functions as a learned no-op.** Over half of BERT's attention in layers 6--10 focuses on [SEP]. Gradient-based feature importance shows near-zero gradients for [SEP] attention starting in layer 5 (Figure 3). Heads with specific syntactic functions default to [SEP] for tokens where their function is not applicable (Section 3.2, Figure 5). Status: **supported**.

3. **C3: Attention-based probing achieves 77 UAS.** A probing classifier combining learned linear weights over all 144 attention heads plus GloVe embeddings achieves 77 UAS on Penn Treebank dependency parsing, substantially above the best baseline (58 UAS for Distances + GloVe) and comparable to hidden-state probing (80 UUAS, not directly comparable) (Table 3, Section 5). Status: **supported**.

4. **C4: A single head achieves 65% coreference accuracy.** Head 5-4 achieves 65% antecedent selection accuracy on CoNLL-2012 coreference (documents truncated to 128 tokens), improving by >10 points over string-matching and approaching a rule-based 4-sieve system (69%) (Table 2, Section 4.3). Status: **supported**.

5. **C5: Heads in the same layer exhibit similar behavior.** Jensen-Shannon Divergence-based clustering and multidimensional scaling visualization show that heads within the same layer tend to be close together in behavioral space. The authors suggest attention dropout during training as a possible cause (Section 6, Figure 6). Status: **supported**.

---

## Open Questions

1. **Do these head specializations transfer across languages?** The paper explicitly identifies extending the analysis to other languages as future work (Section 4.2). It is unknown whether the same syntactic-relation-specific heads emerge in multilingual models or models trained on non-English data. Not addressed.
2. **What role do heads without identified behaviors serve?** The paper found interpretable behaviors in only a subset of heads. Concurrent work by Michel et al. (2019) and Voita et al. (2019) suggests many heads can be pruned and that important surviving heads tend to have identified behaviors. Partially addressed by `2019-12-sixteen-heads-better-than-one` and `2019-07-specialized-attention-heads-pruning`.
3. **Why do same-layer heads develop similar attention distributions?** Despite multi-head attention being designed for representational diversity (Tu et al., 2018), heads within the same layer cluster together in behavioral space. The paper hypothesizes attention dropout as a cause but does not validate this (Section 6). Not addressed.
4. **Does BERT-large exhibit the same pattern of head specialization?** Only BERT-base was analyzed. Whether larger models exhibit more, fewer, or different specialized heads is not explored. Not addressed.

---

## Core References and Why They Are Referenced

### Foundational Model and Architecture

- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* The model being analyzed. BERT's bidirectional self-attention over 12 layers and 12 heads provides the 144 attention maps that are the subject of all experiments.
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational Transformer architecture. The paper uses the standard Transformer attention formulation (softmax-normalized dot-product attention) as the basis for all analysis.

### Prior Work on Probing Neural Network Representations

- **Adi et al. (2017)** -- *Fine-Grained Analysis of Sentence Embeddings Using Auxiliary Prediction Tasks.* Early work on probing classifiers for sentence embeddings. Referenced as part of the representation-probing paradigm that this paper complements with attention-based probing.
- **Belinkov et al. (2017)** -- *What Do Neural Machine Translation Models Learn About Morphology?* Probing classifiers applied to NMT internal representations. Referenced as a key example of the vector-representation analysis tradition.
- **Conneau et al. (2018)** -- *What You Can Cram into a Single Vector: Probing Sentence Embeddings for Linguistic Properties.* Showed that randomly initialized networks can be surprisingly strong baselines for probing tasks. Motivates the randomly initialized BERT baseline in Table 3.
- **Tenney et al. (2018, 2019)** -- *What Do You Learn from Context?* and *BERT Rediscovers the Classical NLP Pipeline.* Probing studies showing BERT's representations encode hierarchical linguistic structure. This paper shows similar findings in attention maps rather than hidden states.
- **Hewitt and Manning (2019)** -- *Finding Syntax with Structural Probes.* Probing classifier on BERT's vector representations for syntax, achieving 80 UUAS. Serves as the primary comparison point for the attention-based probing classifier (77 UAS in Table 3).

### Language Model Analysis via Outputs

- **Linzen et al. (2016)** -- *Assessing the Ability of LSTMs to Learn Syntax-Sensitive Dependencies.* Evaluates language models on subject-verb agreement. Referenced as a key example of the output-analysis paradigm.
- **Khandelwal et al. (2018)** -- *Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context.* Showed LSTM language models make increasingly coarse use of longer-term context. Related to the positional attention patterns found in BERT.
- **Goldberg (2019)** -- *Assessing BERT's Syntactic Abilities.* Concurrent work examining BERT's agreement abilities. Supports the conclusion that BERT learns syntax from self-supervised training.

### Attention Analysis Predecessors and Concurrent Work

- **Raganato and Tiedemann (2018)** -- *An Analysis of Encoder Representations in Transformer-Based Machine Translation.* Evaluated attention heads of machine translation models for dependency parsing but only reported overall UAS. This paper extends the approach by investigating relation-specific heads and proposing probing classifiers.
- **Marecek and Rosa (2018)** -- *Extracting Syntactic Trees from Transformer Encoder Self-Attentions.* Proposed heuristic conversion of attention to syntactic trees without quantitative evaluation. This paper provides the missing quantitative evaluation.
- **Voita et al. (2018)** -- *Context-Aware Neural Machine Translation Learns Anaphora Resolution.* Showed attention in NMT captures anaphora. This paper finds the analogous result for coreference in BERT.
- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned.* Concurrent work identifying syntactic, positional, and rare-word-sensitive heads in NMT and showing many heads can be pruned. The surviving heads tend to be those with identified behaviors, consistent with this paper's findings.
- **Michel et al. (2019)** -- *Are Sixteen Heads Really Better Than One?* Shows many of BERT's attention heads can be pruned. Suggests that heads without identified behaviors may have limited functional importance.
- **Jain and Wallace (2019)** -- *Attention Is Not Explanation.* Argues attention weights do not reliably explain predictions. Discussed in Section 7; the authors counter that their goal is understanding learned information, not explaining specific predictions.

### Evaluation Data

- **Marcus et al. (1993)** -- *Building a Large Annotated Corpus of English: The Penn Treebank.* Source of the WSJ dependency parsing evaluation data (annotated with Stanford Dependencies).
- **Pradhan et al. (2012)** -- *CoNLL-2012 Shared Task: Modeling Multilingual Unrestricted Coreference in OntoNotes.* Source of the coreference resolution evaluation data.

### Coreference Baselines

- **Lee et al. (2011)** -- *Stanford's Multi-Pass Sieve Coreference Resolution System.* Inspires the rule-based coreference baseline (4-sieve system achieving 69% accuracy).
- **Wiseman et al. (2015)** -- *Learning Anaphoricity and Antecedent Ranking Features for Coreference Resolution.* Neural coreference system used as an upper-bound comparison (83% accuracy, though not directly comparable).

### Other Tools

- **Pennington et al. (2014)** -- *GloVe: Global Vectors for Word Representation.* GloVe embeddings are used in the attention-and-words probing classifier to provide word identity information alongside attention weights.
- **Sundararajan et al. (2017)** -- *Axiomatic Attribution for Deep Networks.* Provides the gradient-based feature importance method used to analyze whether attention to [SEP] affects model outputs (Figure 3).
