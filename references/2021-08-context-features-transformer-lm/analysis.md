---
title: "What Context Features Can Transformer Language Models Use?"
authors: "O'Connor, Andreas"
year: 2021
venue: "ACL 2021"
paper_type: conference-paper
categories: ["probing-and-analysis", "attention-analysis"]
scope: ["context utilization in transformer language models", "V-information framework", "usable information in long-range context", "content words vs function words", "word order effects"]
benchmarks_used: ["perplexity-wikitext103"]
models_introduced: []
models_evaluated: ["gpt-2"]
key_claims:
  - id: C1
    claim: "Content words are the primary carriers of usable information in long-range context; retaining only content words in the long-range condition improves predictions over full context (negative ablated information of -31%)"
    evidence: "Section 3.2, Figure 3b"
    status: supported
    scope: "GPT-2 trained from scratch on WikiText-103, 512-token ablated context, English Wikipedia"
    magnitude: "-31% ablated information long-range (content words improve over full context); 9% ablated information mid-range"
  - id: C2
    claim: "Local co-occurrence statistics carry a significant fraction of usable information; shuffling within trigrams removes only 14% of usable information in the mid-range condition and 41% in the long-range condition"
    evidence: "Section 3.1, Figure 2"
    status: supported
    scope: "GPT-2 on WikiText-103, 512-token ablated context, V-information paradigm"
    magnitude: "14% ablated information mid-range, 41% long-range (shuf. within trigrams)"
  - id: C3
    claim: "Long-range context is not simply a source of topic information: replacing context with topically similar earlier text from the same document removes 55% (mid-range) and 69% (long-range) of usable information"
    evidence: "Section 3.1, Figure 2, replace w/ old ablation"
    status: supported
    scope: "GPT-2 on WikiText-103, 512-token ablated context, replacement from same source document"
    magnitude: "55% ablated information mid-range, 69% long-range"
  - id: C4
    claim: "Training-time ablation (V-information) and evaluation-time ablation give qualitatively different results, especially for lexical ablations: deleting content words has a large effect at evaluation time but preserves most usable information when models are retrained"
    evidence: "Section 3.3, Figures 4 and 5"
    status: supported
    scope: "GPT-2 on WikiText-103, comparison of two paradigms on same ablation set"
    magnitude: "Retaining only nouns: ~55% normalized accuracy eval-only vs ~80% train+eval (Figure 5a, mid-range)"
  - id: C5
    claim: "Function words carry very little usable information: retaining only function words removes 69% (mid-range) and 89% (long-range) of usable information, while deleting function words (retaining content words) removes only 9% mid-range and improves predictions in the long-range condition"
    evidence: "Section 3.2, Figure 3"
    status: supported
    scope: "GPT-2 on WikiText-103, 512-token ablated context, English"
    magnitude: "Function-words-only: 69% mid-range, 89% long-range ablated information; content-words-only: 9% mid-range, -31% long-range"
cross_references:
  - target: 2018-07-sharp-nearby-fuzzy-far-away
    type: extends
    detail: "Directly extends Khandelwal et al.'s evaluation-time context ablation study on LSTMs by introducing V-information to distinguish usable information loss from distributional shift effects, and applies the framework to transformers"
  - target: 2022-03-in-context-learning-induction-heads
    type: complementary
    detail: "Olsson et al. cite this paper's word-order findings as consistent with the induction head hypothesis (preserving word order matters), though the finding that retaining only nouns can improve loss is noted as partially in tension"
  - target: 2021-11-long-range-models-use-context
    type: concurrent
    detail: "Both papers study what information long-range transformer LMs extract from distant context using perturbation experiments; Sun et al. study the Routing Transformer on PG-19 while O'Connor & Andreas use GPT-2 on WikiText-103 with V-information"
  - target: 2020-07-theoretical-limitations-self-attention
    type: complementary
    detail: "Hahn provides theoretical bounds on what self-attention can compute from context; O'Connor & Andreas provide complementary empirical evidence about what information transformers actually extract in practice"
  - target: 2017-12-attention-is-all-you-need
    type: evaluates
    detail: "Studies the context utilization properties of the transformer architecture introduced by Vaswani et al."
open_questions:
  - question: "Does the finding that retaining only content words improves long-range predictions reflect a limitation of current transformer architectures or a fundamental property of natural language?"
    addressed_by: null
  - question: "Do the results generalize to larger transformer models (billions of parameters) and to non-English languages?"
    addressed_by: null
  - question: "Does the usable information added by long contexts improve predictability of syntax, semantics, or simply document-level word frequency statistics?"
    addressed_by: null
  - question: "Can more efficient, compressed context representations that preserve only usable information (content words, local co-occurrence) improve transformer LM efficiency without sacrificing accuracy?"
    addressed_by: null
  - question: "Do context ablations affect the quality of text generated by models, beyond what perplexity captures?"
    addressed_by: null
---

# What Context Features Can Transformer Language Models Use?

**Authors:** Joe O'Connor, Jacob Andreas (Massachusetts Institute of Technology)
**Date:** August 2021, ACL 2021 (arXiv:2106.08367)

---

## Core Research Problem

Transformer-based language models benefit from conditioning on contexts of hundreds to thousands of previous tokens, with predictive accuracy improving when conditioning on up to a thousand tokens (Beltagy et al., 2020). However, **what aspects of these long contexts actually contribute to accurate prediction** is not understood. Prior work by Khandelwal et al. (2018) -- *Sharp Nearby, Fuzzy Far Away* -- measured changes in a pre-trained LSTM LM when context words were permuted and deleted at evaluation time, finding effective context of ~200 tokens. But neural language models are highly sensitive to distributional shifts: a model might be unable to use information from long-range context but still be adversely affected when the structure of that context changes at evaluation time. Evaluation-time ablation conflates two distinct effects: loss of usable information and out-of-distribution degradation.

The core challenge is: **distinguishing what information in long-range context is actually usable by transformer language models from what merely causes distributional shift artifacts when removed.**

---

## Problem Solutions

The paper applies the **V-information framework** (Xu et al., 2020) to measure usable predictive information in transformer LM contexts through training-time context ablations. The key idea is to train separate models on ablated contexts and compare their accuracy, rather than applying ablations only at evaluation time.

The solution is built on three components:

1. **V-information as a measurement tool.** Training a model with access to ablated context and comparing its accuracy to a model with full context measures how much *usable* information (rather than sensitivity to distributional shift) the ablation removes.
2. **Systematic context ablations.** A comprehensive set of structural (word-order shuffling, sentence shuffling) and lexical (POS-based deletion, frequency-based deletion) ablations applied to long-range context.
3. **Comparison with evaluation-time ablation.** Repeating the ablation experiments at evaluation time only (the paradigm of Khandelwal et al., 2018) to demonstrate where the two paradigms diverge.

---

## Approach Details

### Method

The paper uses the **predictive V-information** framework (Xu et al., 2020):

> I_V(X -> Y) = [inf_{p1 in V} -E log p1(Y)] - [inf_{p2 in V} -E log p2(Y | X)]

This measures how much extra information about Y (target token) can be extracted from X (context) by any predictor in V (a class of LMs). In practice, this amounts to training a model without the extra context and a model with it, then comparing their losses (Eq. 2, Section 2).

The **ablated context** is defined as (Eq. 6):

> f_k(X) = [f(X_{0:n-k}), X_{n-k:n}]

where f is an ablation function and k is an integer offset.

The **ablated information** due to ablation f at offset k is defined as (Eq. 8-9):

> A(f, k) = [inf_theta L(theta, f, k) - inf_theta' L(theta', n)] / [inf_theta'' L(theta'', n-k) - inf_theta' L(theta', n)]

where L(theta, f, k) is the ablated negative log-likelihood (Eq. 7). This ratio measures what fraction of the usable information added by the extra k tokens is removed by the ablation f. Values near 0 mean the ablation removes almost no information; values near 1 mean almost all is removed; negative values mean the ablation *improves* predictions.

In practice, models are trained and evaluated using a batched likelihood computation on subsequences (Eq. 10):

> L(theta, f, l : m ~ n) = -1/(|X|(n-m)) sum_x sum_{i=l+m}^{l+n} log p_theta(X_i | [f(X_{0:l}), X_{l:i}])

This is read as "l tokens of f-ablated context, followed by m to n tokens of unablated context."

### Key Technical Components

#### Experimental Conditions

Results are stratified into two evaluation conditions (Section 3, p. 4):

- **Mid-range condition:** likelihoods of the form L(., f, 512 : 0 ~ 256) -- the first 256 tokens after the ablated context.
- **Long-range condition:** likelihoods of the form L(., f, 512 : 256 ~ 512) -- tokens 256--512 after the ablated context.

The mid-range label is used rather than "short-range" because most tokens are still predicted with significant unablated context; the experiments do not characterize sentence-internal modeling of syntactic well-formedness (Section 3, p. 4).

Three baseline models are trained: a **no information model** (L(theta, 0 ~ 512), no extra context), a **full information model** (L(theta, 512 ~ 1024), full unablated extra context), and one model per ablation.

#### Context Ablation Types

**Structural ablations (word order):**
- **shuffle all** -- uniform random permutation of all words
- **shuf. trigrams globally** -- permute non-overlapping trigram blocks globally
- **shuf. within sent.** -- uniform permutation of words within each sentence
- **shuf. within trigrams** -- permute words within each trigram
- **shuf. trigrams within sent.** -- permute trigram blocks within each sentence
- **sent. shuf.** -- shuffle sentence order, preserving internal word order
- **replace w/ old** -- replace context with the 512 tokens immediately preceding it in the source document (topically similar text)

**Lexical ablations (word identity):**
- **N** -- retain only nouns
- **N & VB** -- retain nouns and verbs
- **N & VB & ADJ** -- retain nouns, verbs, and adjectives
- **cont. words** -- retain content words (nouns, verbs, adjectives, adverbs)
- **func. words** -- retain only function words
- **named entities** -- retain only named entities and quantities
- **common** -- retain only frequent words (~2% of types, 80% of tokens)
- **rare** -- retain only rare words (~98% of types, 20% of tokens)

All ablations are defined at the word level (not BPE token level). For lexical ablations that reduce token count, padding tokens are inserted at the beginning of the context window to preserve sequence length. POS tagging uses the spaCy model (Honnibal et al., 2020).

### Experimental Setup

- **Model architecture:** GPT-2 (Radford et al., 2019) with default hyperparameters, implemented via HuggingFace Transformers (Wolf et al., 2020).
- **Training data:** WikiText-103 (Merity et al., 2016), 103,221,021 words (training), 217,646 words (evaluation).
- **Training:** All models trained from scratch. A special separator token is inserted between ablated and unablated context. All reported results are averaged over two random initializations.
- **Context size:** 512-token ablated contexts in the main experiments; 1024-token ablated contexts in Appendix B to verify robustness.
- **Compute:** Roughly 100 training runs across all conditions (initial exploration, evaluation conditions, and training runs), performed at the Massachusetts Green HPC center, a carbon-neutral supercomputing facility (Impact Statement).
- **Reproducibility:** Code for all experiments is publicly available at https://github.com/lingo-mit/context-ablations (Footnote 1, p. 1). Results are averaged over two random initializations, though specific random seeds are not reported.

### Key Results

#### Word Order Ablations (Section 3.1, Figure 2)

**Mid-range condition (first 256 tokens after ablation):**

| Ablation | Ablated Likelihood (bits) | Ablated Information |
|---|---|---|
| full information | 4.19 | 0% |
| shuf. within trigrams | ~4.23 | 14% |
| shuf. trigrams within sent. | ~4.23 | 16% |
| sent. shuf. | ~4.23 | 17% |
| shuf. within sent. | ~4.25 | 26% |
| shuf. trigrams globally | ~4.27 | 31% |
| shuffle all | ~4.29 | 41% |
| replace w/ old | ~4.33 | 55% |
| no information | 4.45 | 100% |

**Long-range condition (tokens 256--512 after ablation):**

| Ablation | Ablated Likelihood (bits) | Ablated Information |
|---|---|---|
| full information | 4.17 | 0% |
| sent. shuf. | ~4.18 | 14% |
| shuf. trigrams within sent. | ~4.19 | 35% |
| shuf. within trigrams | ~4.19 | 41% |
| shuf. trigrams globally | ~4.20 | 50% |
| shuf. within sent. | ~4.20 | 55% |
| replace w/ old | ~4.20 | 69% |
| shuffle all | ~4.21 | 84% |
| no information | 4.22 | 100% |

Key takeaways:
- **Local co-occurrence statistics carry significant usable information.** Ablations preserving trigram-level statistics (shuf. within trigrams, shuf. trigrams within sent.) remove relatively little information in both conditions (single model architecture, two random initializations per condition -- moderate evidence).
- **Sentence order matters little.** Shuffling sentence order removes only 17% (mid-range) and 14% (long-range) (Section 3.1, Figure 2).
- **Complete shuffling is destructive in the long range** (84%) but less so in the mid range (41%) (Figure 2).
- **Topically similar text is not a substitute** for the actual context: replacing with earlier text from the same document removes 55--69% of information (Section 3.1, Figure 2).

#### Lexical Ablations (Section 3.2, Figure 3)

**Mid-range condition:**

| Ablation | Ablated Likelihood (bits) | Ablated Information |
|---|---|---|
| full information | 4.19 | 0% |
| cont. words | ~4.20 | 9% |
| N & VB & ADJ | ~4.21 | 11% |
| N & VB | ~4.21 | 13% |
| N | ~4.24 | 20% |
| common | ~4.29 | 38% |
| named entities | ~4.29 | 39% |
| rare | ~4.34 | 58% |
| func. words | ~4.37 | 69% |
| no information | 4.45 | 100% |

**Long-range condition:**

| Ablation | Ablated Likelihood (bits) | Ablated Information |
|---|---|---|
| cont. words | ~4.17 | **-31%** |
| N & VB & ADJ | ~4.17 | **-25%** |
| N & VB | ~4.17 | **-22%** |
| N | ~4.17 | **-9%** |
| full information | 4.17 | 0% |
| named entities | ~4.18 | 31% |
| common | ~4.18 | 33% |
| rare | ~4.19 | 73% |
| func. words | ~4.20 | 89% |
| no information | 4.22 | 100% |

Key takeaways:
- **Content words carry most usable information.** Deleting all words except nouns removes only 20% of usable information mid-range and actually *improves* predictions in the long range (-9%) (Section 3.2, Figure 3; single model architecture on single dataset -- limited evidence breadth, but robust across two random initializations).
- **In the long-range condition, content-word-only contexts outperform full contexts.** All four content-word ablations (N, N&VB, N&VB&ADJ, cont. words) have negative ablated information, meaning they improve model accuracy. The effect is robust across multiple random initializations (Section 3.2, Figure 3).
- **Function words carry minimal information.** Retaining only function words removes 69% (mid) and 89% (long) of usable information (Figure 3).
- **The content-word improvement is likely due to reduced overfitting.** The authors note an ~11% gap between training and validation perplexity, suggesting the ablation preserves semantic content while reducing the model's ability to overfit (Section 3.2, p. 6).

#### Evaluation-Time Ablation Comparison (Section 3.3, Figures 4--5)

Training a single model with optional context padding and evaluating with ablations at test time (the paradigm of Khandelwal et al., 2018) gives qualitatively different results. In the mid-range condition, lexical ablations have a large negative impact under evaluation-time ablation but preserve most usable information under training-time ablation. For example, retaining only nouns falls at ~55% normalized accuracy under evaluation-time ablation but ~80% under training-time ablation (Figure 5a, Appendix A). Locality-preserving ablations (trigram shuffling, sentence shuffling) are the most robust across both paradigms (Section 3.3, Figures 4--5; single model comparison -- limited evidence).

#### Longer Context Windows (Appendix B, Figures 6--7)

Repeating experiments with 1024-token ablated contexts produces consistent results:
- Shuffling within sentences removes 29% (mid) and 65% (long) of usable information (Figure 6).
- Retaining only N&VB&ADJ improves predictions in both conditions (ablated information of -4% in both mid-range and long-range) (Figure 7).
- Function words again carry minimal usable information (76% mid, 114% long -- exceeding 100% in the long-range indicates performance worse than the no information baseline) (Figure 7).

#### Context Extension Experiment (Section 3.4)

Replacing padding tokens in the nouns+verbs ablation with nouns and verbs from even further back in the document -- effectively providing a longer-range view of informative features -- slightly increased usable information mid-range (+0.2%) but decreased it long-range (-0.6%). **Longer contexts, even of a kind previously found to be informative, did not provide additional usable information** (Section 3.4, p. 8), consistent with the hypothesis that content-word ablation improves predictions by reducing overfitting rather than by being inherently more informative.

---

## Limitations and Failure Modes

- **Single model architecture and scale.** All experiments use GPT-2-sized models (~124M parameters, standard configuration) trained from scratch on WikiText-103. Results may not generalize to larger models, different architectures, or different training corpora.
- **English Wikipedia only.** WikiText-103 consists of English Wikipedia articles. The relative importance of word order, function words, and content words may differ across languages and domains.
- **Perplexity-only evaluation.** Results characterize LMs as predictive models only. The authors explicitly note that the same analysis applied to downstream NLP tasks (question answering, summarization) might give different conclusions (Section 3, p. 4).
- **Overfitting confound.** The ~11% training-validation perplexity gap means some results (especially the negative ablated information for content words) may reflect overfitting reduction rather than purely information-theoretic properties. The authors acknowledge this (Section 3.2, p. 6).
- **[Inferred]** BPE tokenization mismatch. Ablations are defined at the word level but the model operates on BPE tokens, creating a mismatch between the unit of ablation and the unit of prediction. The paper does not discuss the implications of this mismatch.
- **Text generation quality not systematically measured.** Appendix C provides qualitative generation examples but no systematic evaluation of whether ablations affect generation quality. The authors acknowledge this as an open question (Section 5, p. 9).

#### Scope and Comparability

- **What was not tested:** Models larger than GPT-2 (~124M parameters), non-English languages, non-Wikipedia domains, downstream NLP tasks, alternative tokenization schemes (character-level, word-level), alternative positional encoding schemes, and the effect of pre-training data distribution on context utilization.
- **Comparability notes:** Khandelwal et al. (2018) studied LSTMs on WikiText-103 using evaluation-time ablation only, making direct numerical comparison of ablated information percentages inappropriate because the two paradigms measure different things (as demonstrated in Section 3.3). Sun et al. (2021) study context utilization in the Routing Transformer on PG-19 using a different set of perturbation experiments, differing in both model, dataset, and methodology. The "mid-range" and "long-range" conditions used here (0--256 and 256--512 tokens after 512 tokens of ablated context) are specific to this paper and do not directly map to context distance definitions in other work.

---

## Conclusions

### Contributions

1. **V-information framework applied to context analysis.** Introduced the use of V-information (Xu et al., 2020) to distinguish usable information from distributional shift artifacts in context ablation experiments, providing a principled methodology that avoids the confounds of evaluation-time-only ablation (Section 2, Eq. 8--9).

2. **Content words identified as primary information carriers.** Demonstrated that content words (nouns, verbs, adjectives, adverbs) carry the vast majority of usable information in long-range context: retaining only nouns removes just 20% of usable information mid-range and actually improves predictions in the long-range condition (Section 3.2, Figure 3).

3. **Local co-occurrence more informative than global order.** Showed that local co-occurrence statistics (preserved by trigram-level ablations) carry significantly more usable information than global word order or sentence order: shuffling within trigrams removes only 14% (mid-range) and sentence shuffling removes only 14% (long-range) (Section 3.1, Figure 2).

4. **Long-range context is not topic information.** Replacing context with topically similar earlier text removes 55--69% of usable information, refuting the hypothesis that long-range context serves primarily as a topic signal (Section 3.1, Figure 2).

5. **Two paradigms give qualitatively different results.** Demonstrated that training-time ablation (V-information) and evaluation-time ablation produce different conclusions, especially for lexical ablations, underscoring the importance of methodology choice in context analysis (Section 3.3, Figure 5).

### Implications

1. **Current models underutilize structural information in context.** The finding that fine-grained word order and syntactic structure contribute little usable information suggests that current transformers may not be effectively leveraging the full propositional content of their contexts. This could reflect architectural limitations or fundamental properties of natural language. [Inference, acknowledged by authors as an open question, Section 5]

2. **Compressed context representations may be viable.** The results motivate more efficient context representations that preserve content words and local co-occurrence while discarding syntactic detail, potentially enabling longer effective contexts with less compute. [Noted by authors, Section 5]

3. **Overfitting may mask context utilization.** The improvement from content-word-only contexts suggests that current models may overfit to surface patterns in long-range context that do not generalize, and that regularization through context compression could improve held-out performance. [Speculative inference from Section 3.2 and 3.4]

---

## Key Claims

1. **Content words carry most usable information in long-range context.** Retaining only content words removes 9% of usable information mid-range and improves predictions by 31% of the full-vs-no-information gap in the long range. Retaining only nouns removes 20% mid-range and improves predictions by 9% long-range (Figure 3, Section 3.2). Scope: GPT-2 trained from scratch on WikiText-103, 512-token ablated context, English. Effect: -31% ablated information long-range for content words. Evidence: two random initializations, single model architecture and dataset (limited breadth but robust across seeds). Status: **supported**.

2. **Local co-occurrence statistics are a primary carrier of usable information.** Shuffling within non-overlapping trigrams removes only 14% of usable information mid-range (Figure 2a). Shuffling trigram blocks within sentences removes only 16% mid-range and 35% long-range (Figure 2). Scope: GPT-2 on WikiText-103, V-information paradigm. Effect: 14% mid-range, 41% long-range (shuf. within trigrams). Evidence: two random initializations, single model architecture (limited breadth). Status: **supported**.

3. **Long-range context is not simply a source of topic information.** Replacing the ablated context with the 512 tokens immediately preceding it in the source document (topically similar text) removes 55% (mid-range) and 69% (long-range) of usable information, nearly as uninformative as no context at all in the long range (Figure 2, Section 3.1). Scope: GPT-2 on WikiText-103, same-document replacement. Effect: 55% mid, 69% long. Evidence: two random initializations, single model (limited breadth). Status: **supported**.

4. **V-information and evaluation-time ablation give qualitatively different results for lexical ablations.** Under evaluation-time ablation, lexical ablations (e.g., retaining only nouns) cause large perplexity increases; under V-information (retraining), they preserve most usable information. The two paradigms agree for locality-preserving structural ablations but diverge for lexical ones (Figure 5, Section 3.3). Scope: GPT-2 on WikiText-103, comparison of train+eval vs eval-only paradigms. Effect: retaining only nouns ~55% normalized accuracy eval-only vs ~80% train+eval (Figure 5a, mid-range). Evidence: single model comparison (limited breadth). Status: **supported**.

5. **Function words contribute minimal usable information.** Retaining only function words removes 69% (mid-range) and 89% (long-range) of usable information, while deleting them (retaining content words) removes only 9% mid-range and improves predictions in the long range (Figure 3, Section 3.2). Scope: GPT-2 on WikiText-103, English, 512-token ablated context. Effect: function-words-only: 69% mid, 89% long; content-words-only: 9% mid, -31% long. Evidence: two random initializations, single model architecture and dataset (limited breadth). Status: **supported**.

---

## Open Questions

1. **Model-specific or language-universal?** Do the results reflect limitations of GPT-2-scale transformers, or are they fundamental properties of English? Deleting function words cannot add information theoretically, but improves held-out accuracy, suggesting at least some effects are model-specific (overfitting). Whether larger or differently trained models would extract more usable information from word order and function words remains open (Section 5). Not yet addressed in this reference set.

2. **Generalization to larger models and non-English languages.** All experiments use a single GPT-2-sized model on English Wikipedia. Do the patterns hold for billion-parameter models, for different languages with different morphological properties, and for different domains? Not yet addressed.

3. **What linguistic level does long-range context inform?** Does the usable information added by long contexts improve predictability of syntax, semantics, or simply document-level word frequency statistics? The authors raise this question explicitly (Section 5). Not yet addressed.

4. **Compressed context representations.** The results motivate more efficient context representations preserving only usable information (content words, local co-occurrence). Can such representations improve transformer LM efficiency without sacrificing accuracy? The authors note this direction (Section 5). Not yet addressed.

5. **Generation quality under ablation.** Do context ablations affect the quality of text generated by models, beyond what perplexity captures? Appendix C provides qualitative examples but no systematic evaluation. The authors explicitly list this as an open question (Section 5). Not yet addressed.

---

## Core References and Why They Are Referenced

### Direct Predecessors

- **Khandelwal et al. (2018)** -- *Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context.* The most direct predecessor. Measured context utilization in LSTM LMs through evaluation-time ablations (word permutation and deletion), finding effective context of ~200 tokens. O'Connor & Andreas extend this work in two ways: they apply V-information to distinguish usable information from distributional shift, and they study transformers rather than LSTMs.

### Theoretical Framework

- **Xu et al. (2020)** -- *A Theory of Usable Information Under Computational Constraints.* Introduced V-information, the formal framework that underlies all experiments. V-information generalizes Shannon mutual information to computationally bounded predictors, enabling the distinction between information that is theoretically present and information that is practically usable.

### Transformer Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduced the transformer architecture whose context utilization properties are the subject of this study.

- **Radford et al. (2019)** -- *Language Models Are Unsupervised Multitask Learners.* The GPT-2 architecture used for all experiments.

### Long-Range Transformers

- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Demonstrated that transformer LM accuracy improves when conditioning on up to a thousand tokens, motivating the question of what information in those tokens is used.

- **Rae et al. (2019)** -- *Compressive Transformers for Long-Range Sequence Modelling.* Found that long-range contexts could be informatively summarized in fixed-size vectors, consistent with the finding that fine-grained ordering contributes little usable information.

### Context Analysis

- **Hahn (2020)** -- *Theoretical Limitations of Self-Attention in Neural Sequence Models.* Provided theoretical limits on what self-attention can compute from input sequences, complementing this paper's empirical analysis of what information is actually used.

### Evaluation and Probing

- **Voita & Titov (2020)** -- *Information-Theoretic Probing with Minimum Description Length.* Used related information-theoretic tools for probing linguistic structure in LM representations. Shares the motivation of principled information-theoretic measurement but focuses on representations rather than predictions.

- **Pimentel et al. (2020)** -- *Information-Theoretic Probing for Linguistic Structure.* Another information-theoretic approach to probing, focused on interpreting linguistic structure rather than characterizing context effects.

### Shuffling and Ablation Studies

- **Pham et al. (2020)** -- *Out of Order: How Important Is the Sequential Order of Words in a Sentence in Natural Language Understanding Tasks?* Found that shuffling experiments have limited effect on NLI models. The within-sentence and within-trigram shuffling ablations used in this paper are inspired by this work.
