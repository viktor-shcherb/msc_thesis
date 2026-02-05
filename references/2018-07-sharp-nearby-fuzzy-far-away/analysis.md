---
title: "Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context"
authors: "Khandelwal, He, Qi, Jurafsky"
year: 2018
venue: "ACL 2018"
paper_type: conference-paper
categories: ["probing-and-analysis"]
scope: ["context utilization in LSTM language models", "nearby vs. long-range context representation", "copy mechanisms"]
benchmarks_used: ["penn-treebank", "perplexity-wikitext2"]
models_introduced: []
models_evaluated: ["awd-lstm"]
key_claims:
  - id: C1
    claim: "LSTM language models have an effective context size of about 200 tokens on average, with only 1% increase in perplexity beyond 150 tokens on PTB and 250 tokens on Wiki"
    evidence: "Section 4, Figure 1a"
    status: supported
  - id: C2
    claim: "Changing hyperparameters (BPTT length, dropout rate, model size) does not change the effective context size, only the absolute perplexity"
    evidence: "Section 4, Figure 1b"
    status: supported
  - id: C3
    claim: "Infrequent words need more context (>200 tokens) than frequent words (<50 tokens)"
    evidence: "Section 4.1, Figure 1c"
    status: supported
  - id: C4
    claim: "Content words (nouns, verbs, adjectives) need more context than function words (determiners, prepositions); determiners rely only on the last 10 tokens"
    evidence: "Section 4.1, Figure 1d"
    status: supported
  - id: C5
    claim: "Local word order only matters within the most recent 20 tokens (approximately one sentence); permuting 20-token windows beyond this point has negligible effect on loss"
    evidence: "Section 5.1, Figure 2a"
    status: supported
  - id: C6
    claim: "Global word order only matters within the most recent 50 tokens; shuffling or reversing all context beyond 50 tokens has no effect on model performance"
    evidence: "Section 5.1, Figure 2b"
    status: supported
  - id: C7
    claim: "Beyond 50 tokens, word identity still matters even though word order does not, indicating the model maintains a rough semantic/topic representation of distant context"
    evidence: "Section 5.1, Figure 2b (gap between permutation and random replacement curves)"
    status: supported
  - id: C8
    claim: "Content words matter more than function words beyond the first sentence; dropping content words 5 tokens away increases perplexity by ~65% vs ~17% for random drop of same proportion"
    evidence: "Section 5.2, Figure 3"
    status: supported
  - id: C9
    claim: "LSTMs can regenerate words from nearby context without caches (dropping target from nearby context increases perplexity by ~9%) but rely on rough semantic representation for long-range context (dropping target from far context increases perplexity by only ~2%)"
    evidence: "Section 6.1, Figure 4a"
    status: supported
  - id: C10
    claim: "Neural caches help words that can only be copied from long-range context the most: C_far words see 28% (PTB) and 53% (Wiki) perplexity increase without cache vs 22% (PTB) and 32% (Wiki) for C_near"
    evidence: "Section 6.2, Figure 7"
    status: supported
  - id: C11
    claim: "The cache hurts about 36% of words in PTB and 20% in Wiki that cannot be copied from context, due to a flat, confused cache distribution"
    evidence: "Section 6.2, Figures 5-7"
    status: supported
cross_references:
  - target: 2024-02-lost-in-the-middle
    type: extended-by
    detail: "Liu et al. (2024) extend context utilization analysis from LSTMs to Transformer LLMs, finding that larger models additionally exhibit primacy bias not seen in the smaller LSTM models studied here"
  - target: 2019-08-bert-attention-analysis
    type: extended-by
    detail: "Clark, Khandelwal et al. (2019) extend context analysis to BERT attention heads, finding positional biases that echo the nearby-vs-far context utilization patterns"
  - target: 2022-12-scrolls-long-language-sequences
    type: complementary
    detail: "SCROLLS cites this paper's finding that perplexity mostly captures local short-range patterns to motivate task-based rather than perplexity-based evaluation of long-context models"
  - target: 2018-06-prediction-short-memory
    type: complementary
    detail: "Sharan et al. provide theoretical grounding via bounded mutual information for the empirical finding that LSTM LMs effectively use only ~200 tokens of context"
  - target: 2021-08-context-features-transformer-lm
    type: extended-by
    detail: "O'Connor & Andreas extend the evaluation-time ablation paradigm to transformers and introduce V-information to distinguish usable information loss from distributional shift, finding that content words carry most long-range usable information"
open_questions:
  - question: "Do these findings about nearby vs. long-range context generalize to Transformer-based language models with self-attention?"
    addressed_by: 2024-02-lost-in-the-middle
  - question: "Would findings hold for different languages beyond English?"
    addressed_by: null
  - question: "Can adaptive word dropout strategies that leverage word-type importance (content vs. function) improve training?"
    addressed_by: null
  - question: "How do sentence-level interactions affect context utilization beyond the token-level analysis presented?"
    addressed_by: null
  - question: "Can memory models benefit from representations that specifically capture information orthogonal to what the LSTM already models from long-range context?"
    addressed_by: null
---

# Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context

**Authors:** Urvashi Khandelwal, He He, Peng Qi, Dan Jurafsky (Stanford University)
**Date:** July 2018, ACL 2018 (arXiv:1805.04623)

---

## Core Research Problem

Neural language models (NLMs) consistently outperform classical n-gram models, an improvement often attributed to their ability to model long-range dependencies. Yet **how these NLMs actually use context is largely unexplained**. Prior work studied LSTMs at the sentence level only: they can remember sentence lengths, word identity, and word order (Adi et al., 2017), capture subject-verb agreement (Linzen et al., 2016), and model negation and intensification (Li et al., 2016). However, none of this work examines long-range context beyond a single sentence.

The core challenge is: **how much context do LSTM language models actually use, and how do nearby and long-range contexts differ in their representation and utility?**

---

## Problem Solutions

The paper investigates context utilization through **test-time ablation studies** on a pretrained LSTM language model, measuring perplexity changes when prior context is systematically perturbed.

1. **Context truncation** to determine how many tokens the model effectively uses.
2. **Permutation experiments** (shuffle, reverse) to determine where word order matters.
3. **Word dropping and replacement** to distinguish the importance of content vs. function words at different distances.
4. **Target word perturbation** to test whether LSTMs directly copy words from context or rely on rough semantic representations.
5. **Neural cache analysis** to explain how external copy mechanisms complement the LSTM's internal representations.

---

## Approach Details

### Method

All experiments use **test-time perturbations** applied to a pretrained LSTM language model. The model is never retrained with the perturbations; the resulting losses are therefore upper bounds that would likely be lower if the model were also trained to handle such perturbations. Performance is measured as the change in NLL (negative log likelihood) on the dev set relative to an unperturbed baseline, which is equivalent to relative changes in perplexity:

> PP = exp(NLL)

Three families of perturbation functions are used:

1. **Truncation.** Feed only the most recent n tokens:

> `δ_truncate(w_{t-1}, ..., w_1) = (w_{t-1}, ..., w_{t-n})`

2. **Permutation.** Shuffle or reverse tokens within a span `(s_1, s_2]`:

> `δ_permute(w_{t-1}, ..., w_{t-n}) = (w_{t-1}, .., ρ(w_{t-s_1-1}, .., w_{t-s_2}), .., w_{t-n})`

where `ρ ∈ {shuffle, reverse}`. Local word order uses 20-token spans; global word order permutes all tokens before a given point.

3. **Dropping/Replacement.** Drop all words of a given POS tag, or drop/replace specific target word occurrences:

> `δ_drop(w_{t-1}, ..., w_{t-n}) = (w_{t-1}, .., w_{t-s_1}, f_pos(y, (w_{t-s_1-1}, .., w_{t-n})))`

where `f_pos(y, span)` drops all words with POS tag y in the given span.

### Key Technical Components

**Model.** AWD-LSTM (Merity et al., 2018) with the following default hyperparameters:

| Hyperparameter | PTB | Wiki |
|---|---|---|
| Word Emb. Size | 400 | 400 |
| Hidden State Dim | 1150 | 1150 |
| Layers | 3 | 3 |
| Sequence Length (BPTT) | 70 | 70 |
| LSTM Layer Dropout | 0.25 | 0.2 |
| Recurrent Dropout | 0.5 | 0.5 |
| Optimizer | ASGD | ASGD |

**Neural cache** (Grave et al., 2017b). Records hidden state `h_t` at each timestep and computes a cache distribution:

> `P_cache(w_t | w_{t-1}, ..., w_1; h_t, ..., h_1) ∝ Σ_{i=1}^{t-1} 1[w_i = w_t] exp(θ h_i^T h_t)`

where `θ` controls the flatness of the distribution. Cache size is set to 500 for PTB and 3,875 for Wiki (matching average document lengths).

**Three word categories for copy analysis:**
- **C_near:** words that can be copied from nearby context (within 50 most recent tokens)
- **C_far:** words that can only be copied from long-range context (beyond 50 tokens)
- **C_none:** words that cannot be copied from context at all (control set)

### Experimental Setup

**Datasets:**

| | PTB Dev | PTB Test | Wiki Dev | Wiki Test |
|---|---|---|---|---|
| # Tokens | 73,760 | 82,430 | 217,646 | 245,569 |
| Perplexity (no cache) | 59.07 | 56.89 | 67.29 | 64.51 |
| Avg. Sent. Len. | 20.9 | 20.9 | 23.7 | 22.6 |

- **Penn Treebank (PTB):** Wall Street Journal news articles, 0.9M training tokens, 10K vocabulary.
- **WikiText-2 (Wiki):** Wikipedia articles, 2.1M training tokens, 33K vocabulary.

All results are averaged from **three models trained with different random seeds**, with error bars representing standard deviation (or 95% confidence intervals for bar charts). Results are reported on dev sets only; test set consistency is confirmed.

POS tags obtained using Stanford CoreNLP (Manning et al., 2014). Content words defined as nouns, verbs, and adjectives; function words as prepositions and determiners.

### Key Results

**Effective context size (~200 tokens, Section 4):**
- Loss difference between truncated and infinite context gradually diminishes from 5 to 1000 tokens.
- Only 1% perplexity increase beyond 150 tokens on PTB and 250 tokens on Wiki.
- Hyperparameter variations (BPTT 10 vs 100, hidden size 575 vs 1150, 2 vs 3 layers, various dropout settings) change absolute perplexity but not the context usage trend.

**Word-type context dependence (Section 4.1):**
- Frequent words (≥800 training occurrences): insensitive to context beyond 50 tokens.
- Infrequent words: require >200 tokens.
- Determiners: rely only on last ~10 tokens; nouns and verbs: sensitive to distant context.

**Word order sensitivity (Section 5.1):**

| Perturbation | Range of Sensitivity |
|---|---|
| Local shuffle/reverse (20-token windows) | Most recent 20 tokens |
| Global shuffle/reverse (all tokens before point) | Most recent 50 tokens |
| Random replacement (same length) | Full 200+ token range |

- The gap between permutation and replacement curves beyond 50 tokens shows that **word identity matters** in the distant context even though **word order does not**.

**Content vs. function words in context (Section 5.2):**
- Dropping content words 5 tokens from target: ~65% perplexity increase (vs ~17% for random drop of same proportion).
- Dropping function words: not significantly different from random drop of same proportion.
- Beyond 20 tokens: only content words are relevant.

**Copy behavior (Section 6.1):**
- For C_near: dropping only the target word increases perplexity by ~9%; dropping all long-range context increases it by only ~3.5%.
- For C_far: dropping all distant context increases perplexity by ~12%; dropping only the target increases it by only ~2%.
- Replacing the target with `<unk>` or a similar word hurts C_near by up to 14% but has no effect on C_far.

**Cache effectiveness (Section 6.2):**
- Without cache: C_near sees 22% (PTB) / 32% (Wiki) perplexity increase; C_far sees 28% (PTB) / 53% (Wiki) increase.
- Cache disproportionately helps C_far words.
- Cache hurts ~36% of PTB words and ~20% of Wiki words (C_none) due to flat, confused cache distributions when the target is not in the history.

---

## Limitations and Failure Modes

1. **Train-test mismatch.** Perturbations are applied only at test time; the model was never trained to handle them. All measured losses are therefore upper bounds (Section 3).
2. **Confounding factors.** Separating model behavior from language characteristics is challenging. Vocabulary size, dataset size, and other factors confound the analysis (Section 7).
3. **Token-level analysis only.** The study reports observations at the token level; deeper understanding of sentence-level interactions is left to future work (Section 8).
4. **Only two datasets.** Results are limited to PTB (news) and WikiText-2 (encyclopedia). Generalization to other domains and languages is untested.
5. **LSTM-only.** The analysis is specific to LSTM language models. Whether the findings generalize to other architectures (e.g., Transformers) is not investigated.
6. **Cache failure mode.** The cache hurts a substantial fraction of words (36% on PTB, 20% on Wiki) that cannot be copied from context, because the cache distribution becomes flat and confused (Section 6.2, Figure 6).

---

## Conclusions

### Contributions

1. **Effective context size quantification.** Empirically demonstrated that LSTM LMs use about 200 tokens of context on average, independent of hyperparameter settings such as model size and BPTT length.
2. **Nearby vs. long-range context distinction.** Showed that word order matters only within the most recent ~50 tokens (one sentence for local order, 2-3 sentences for global order), while distant context is represented only as a rough semantic field.
3. **Word-type context dependence.** Established that infrequent words and content words require substantially more context than frequent words and function words, with determiners relying on as few as 10 tokens.
4. **Copy mechanism analysis.** Demonstrated that LSTMs can regenerate words from nearby context internally but rely on external caches for long-range copying, and that caches disproportionately benefit words available only in distant context.
5. **Cache failure characterization.** Identified that neural caches hurt performance on words not present in context due to flat, uncertain cache distributions, suggesting the model would benefit from the option to ignore the cache.

### Implications

1. The finding that distant context is modeled only as a rough semantic field implies that **bag-of-words-like topic representations may be sufficient for modeling long-range dependencies in LSTMs** (speculative inference from the order-insensitivity result).
2. The word-type-dependent context usage suggests that **adaptive word dropout strategies** could improve training by differentiating between content and function words.
3. The complementarity between LSTM and cache suggests that **memory-augmented models should explicitly target information not already captured by the base model**, particularly position-specific word identity in distant context.

---

## Key Claims

1. **C1:** LSTM LMs have an effective context size of ~200 tokens (1% perplexity increase beyond 150 tokens on PTB and 250 on Wiki), regardless of hyperparameters (Figure 1a-b, Section 4).
2. **C2:** Local word order matters only within the most recent 20 tokens (~1 sentence); global word order matters only within the most recent 50 tokens (Figure 2a-b, Section 5.1).
3. **C3:** Beyond 50 tokens, word identity still contributes to the model but word order does not, indicating a rough semantic/topic representation (Figure 2b, Section 5.1).
4. **C4:** Content words are far more important than function words beyond the first sentence; within the first sentence, both matter (Figure 3, Section 5.2).
5. **C5:** LSTMs directly copy words from nearby context but rely on rough semantic representation for long-range context; neural caches especially help copy words from the distant context where the LSTM falls short (Figures 4, 7, Sections 6.1-6.2).
6. **C6:** Neural caches hurt ~36% (PTB) / ~20% (Wiki) of words not copyable from context, due to flat cache distributions (Figure 7, Section 6.2).

---

## Open Questions

1. **Do these findings generalize to Transformer-based language models?** The LSTM's sequential processing is fundamentally different from Transformer self-attention, which can attend to any position directly. (Addressed by Liu et al. (2024) -- *Lost in the Middle*, which extends context utilization analysis to Transformer LLMs.)
2. **Would the findings hold for languages other than English?** The two datasets are both English-only (Section 7).
3. **Can adaptive word dropout strategies leveraging content/function word distinctions improve training?** Suggested in Section 7 but not tested.
4. **How do sentence-level interactions (beyond token-level) affect context utilization?** Explicitly left to future work (Section 8).
5. **Can memory-augmented models be designed to capture information orthogonal to the LSTM's representations?** Suggested in Section 7.

---

## Core References and Why They Are Referenced

### Language Model Architecture and Training

- **Merity et al. (2018)** -- *Regularizing and Optimizing LSTM Language Models.* Provides the AWD-LSTM architecture and training procedure used throughout the paper.
- **Hochreiter & Schmidhuber (1997)** -- *Long Short-Term Memory.* The foundational LSTM architecture that the paper analyzes.

### Copy Mechanisms

- **Grave et al. (2017b)** -- *Improving Neural Language Models with a Continuous Cache.* The neural cache model analyzed in Section 6, which interpolates a cache distribution over past hidden states with the model output.
- **Grave et al. (2017a)** -- *Unbounded Cache Model for Online Language Modeling with Open Vocabulary.* Alternative caching approach referenced alongside the continuous cache.

### Prior Analysis of LSTMs

- **Adi et al. (2017)** -- *Fine-grained Analysis of Sentence Embeddings Using Auxiliary Prediction Tasks.* Showed LSTMs can remember word order within a sentence; this paper extends the analysis beyond sentence level.
- **Linzen et al. (2016)** -- *Assessing the Ability of LSTMs to Learn Syntax-Sensitive Dependencies.* Demonstrated LSTMs capture subject-verb agreement; motivates the question of whether syntactic sensitivity extends to long-range context.
- **Li et al. (2016)** -- *Visualizing and Understanding Neural Models in NLP.* Showed LSTMs model semantic compositionality such as negation; referenced as prior work on LSTM interpretability.

### Datasets

- **Marcus et al. (1993)** -- *Building a Large Annotated Corpus of English: The Penn Treebank.* Source of the PTB dataset.
- **Merity et al. (2017)** -- *Pointer Sentinel Mixture Models.* Source of the WikiText-2 dataset and pointer-based copy mechanism.

### Context-Length Analysis

- **Boyd-Graber & Blei (2009)** -- *Syntactic Topic Models.* Previously found that function words rely on less context than content words; corroborated by this paper.
- **Hill et al. (2016)** -- *The Goldilocks Principle: Reading Children's Books with Explicit Memory Representations.* Prior work on context length effects in language modeling.
- **Wang & Cho (2016)** -- *Larger-Context Language Modelling with Recurrent Neural Network.* Prior finding on effective context sizes, consistent with results here.
- **Chelba et al. (2017)** -- *N-gram Language Modeling Using Recurrent Neural Network Estimation.* Found only 8% perplexity increase with 13 tokens of context on PTB (vs. 25% in this paper's setup), attributed to training with restricted context.
