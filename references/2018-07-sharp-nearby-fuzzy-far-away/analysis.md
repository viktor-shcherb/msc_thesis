---
title: "Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context"
authors: "Khandelwal, He, Qi, Jurafsky"
year: 2018
venue: "ACL 2018"
paper_type: conference-paper
categories: ["probing-and-analysis", "attention-analysis"]
scope: ["LSTM language models", "context utilization analysis", "copy mechanism analysis", "English-only evaluation"]
benchmarks_used: ["penn-treebank", "perplexity-wikitext2"]
models_introduced: []
models_evaluated: ["awd-lstm"]
key_claims:
  - id: C1
    claim: "LSTM language models have an effective context size of about 200 tokens on average, with only 1% increase in perplexity beyond 150 tokens on PTB and 250 tokens on Wiki"
    evidence: "Section 4, Figure 1a"
    status: supported
    scope: "AWD-LSTM on PTB and WikiText-2, English only"
    magnitude: "1% perplexity increase beyond 150 tokens (PTB) / 250 tokens (Wiki)"
  - id: C2
    claim: "Changing hyperparameters (BPTT length, dropout rate, model size) does not change the effective context size, only the absolute perplexity"
    evidence: "Section 4, Figure 1b"
    status: supported
    scope: "AWD-LSTM on PTB and Wiki; BPTT 10-100, hidden 575-1150, 2-3 layers, various dropout"
  - id: C3
    claim: "Infrequent words need more context (>200 tokens) than frequent words (<50 tokens)"
    evidence: "Section 4.1, Figure 1c"
    status: supported
    scope: "AWD-LSTM on PTB and Wiki; frequency threshold >=800 training occurrences"
  - id: C4
    claim: "Content words (nouns, verbs, adjectives) need more context than function words (determiners, prepositions); determiners rely only on the last 10 tokens"
    evidence: "Section 4.1, Figure 1d"
    status: supported
    scope: "AWD-LSTM on PTB and Wiki; POS tags from Stanford CoreNLP"
  - id: C5
    claim: "Local word order only matters within the most recent 20 tokens (approximately one sentence); permuting 20-token windows beyond this point has negligible effect on loss"
    evidence: "Section 5.1, Figure 2a"
    status: supported
    scope: "AWD-LSTM on PTB and Wiki; 20-token permutable spans within 300-token context"
  - id: C6
    claim: "Global word order only matters within the most recent 50 tokens; shuffling or reversing all context beyond 50 tokens has no effect on model performance"
    evidence: "Section 5.1, Figure 2b"
    status: supported
    scope: "AWD-LSTM on PTB and Wiki; permuting all tokens before a given point within 300-token context"
  - id: C7
    claim: "Beyond 50 tokens, word identity still matters even though word order does not, indicating the model maintains a rough semantic/topic representation of distant context"
    evidence: "Section 5.1, Figure 2b (gap between permutation and random replacement curves)"
    status: supported
    scope: "AWD-LSTM on Wiki (main) and PTB (Appendix Figure 8)"
  - id: C8
    claim: "Content words matter more than function words beyond the first sentence; dropping content words 5 tokens away increases perplexity by ~65% vs ~17% for random drop of same proportion"
    evidence: "Section 5.2, Figure 3"
    status: supported
    scope: "AWD-LSTM on PTB (main) and Wiki (Appendix Figure 9)"
    magnitude: "~65% perplexity increase (content words at 5 tokens) vs ~17% (random drop)"
  - id: C9
    claim: "LSTMs can regenerate words from nearby context without caches (dropping target from nearby context increases perplexity by ~9%) but rely on rough semantic representation for long-range context (dropping target from far context increases perplexity by only ~2%)"
    evidence: "Section 6.1, Figure 4a"
    status: supported
    scope: "AWD-LSTM on PTB (main) and Wiki (Appendix Figure 11); context of 300 tokens"
    magnitude: "~9% perplexity increase for C_near target drop vs ~2% for C_far target drop"
  - id: C10
    claim: "Neural caches help words that can only be copied from long-range context the most: C_far words see 28% (PTB) and 53% (Wiki) perplexity increase without cache vs 22% (PTB) and 32% (Wiki) for C_near"
    evidence: "Section 6.2, Figure 7"
    status: supported
    scope: "AWD-LSTM with Grave et al. (2017b) neural cache; cache size 500 (PTB), 3875 (Wiki)"
    magnitude: "C_far: 28% (PTB) / 53% (Wiki) vs C_near: 22% (PTB) / 32% (Wiki)"
  - id: C11
    claim: "The cache hurts about 36% of words in PTB and 20% in Wiki that cannot be copied from context, due to a flat, confused cache distribution"
    evidence: "Section 6.2, Figures 5-7"
    status: supported
    scope: "AWD-LSTM on PTB and Wiki with neural cache"
    magnitude: "36% of PTB words / 20% of Wiki words hurt by cache"
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
    detail: "O'Connor & Andreas extend the evaluation-time ablation paradigm to Transformers and introduce V-information to distinguish usable information loss from distributional shift, finding that content words carry most long-range usable information"
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

Neural language models (NLMs) consistently outperform classical n-gram models, an improvement often attributed to their ability to model long-range dependencies. Yet **how these NLMs actually use context is largely unexplained** (Section 1). Prior work studied LSTMs at the sentence level only: they can remember sentence lengths, word identity, and word order (Adi et al., 2017), capture subject-verb agreement (Linzen et al., 2016), and model negation and intensification (Li et al., 2016). However, none of this work examines long-range context beyond a single sentence (Section 1).

The gap is threefold: (1) how many tokens of context the model effectively uses, (2) whether nearby and long-range contexts are represented differently, and (3) how copy mechanisms help in different context regions.

The core challenge is: **how much context do LSTM language models actually use, and how do nearby and long-range contexts differ in their representation and utility?**

---

## Problem Solutions

The paper investigates context utilization through **test-time ablation studies** on a pretrained AWD-LSTM language model, measuring perplexity changes when prior context is systematically perturbed (Section 3). The key idea is that perturbations applied only at test time reveal what contextual information the model has learned to rely on.

1. **Context truncation** to determine how many tokens the model effectively uses (Section 4).
2. **Permutation experiments** (shuffle, reverse) to determine where word order matters (Section 5.1).
3. **Word dropping and replacement** to distinguish the importance of content vs. function words at different distances (Section 5.2).
4. **Target word perturbation** to test whether LSTMs directly copy words from context or rely on rough semantic representations (Section 6.1).
5. **Neural cache analysis** to explain how external copy mechanisms complement the LSTM's internal representations (Section 6.2).

---

## Approach Details

### Method

All experiments use **test-time perturbations** applied to a pretrained LSTM language model. The model is never retrained with the perturbations; the resulting losses are therefore upper bounds that would likely be lower if the model were also trained to handle such perturbations (Section 3). Performance is measured as the change in NLL (negative log likelihood) on the dev set relative to an unperturbed baseline, which is equivalent to relative changes in perplexity:

> PP = exp(NLL)

Three families of perturbation functions are used:

1. **Truncation.** Feed only the most recent n tokens (Equation 1, Section 4):

> `delta_truncate(w_{t-1}, ..., w_1) = (w_{t-1}, ..., w_{t-n})`

where n > 0 and all tokens farther away from the target w_t are dropped. Words at the beginning of the test sequence with fewer than n tokens in the context are ignored for loss computation.

2. **Permutation.** Shuffle or reverse tokens within a span (s_1, s_2] (Equation 2, Section 5.1):

> `delta_permute(w_{t-1}, ..., w_{t-n}) = (w_{t-1}, .., rho(w_{t-s_1-1}, .., w_{t-s_2}), .., w_{t-n})`

where `rho in {shuffle, reverse}`. Local word order uses 20-token spans; global word order permutes all tokens before a given point. Permutable spans are selected within a context of n = 300 tokens, greater than the effective context size.

3. **Dropping/Replacement.** Drop all words of a given POS tag, or drop/replace specific target word occurrences (Equation 3, Section 5.2):

> `delta_drop(w_{t-1}, ..., w_{t-n}) = (w_{t-1}, .., w_{t-s_1}, f_pos(y, (w_{t-s_1-1}, .., w_{t-n})))`

where `f_pos(y, span)` drops all words with POS tag y in the given span. For target word perturbation (Equation 4, Section 6.1), `f_word(w, span)` drops or replaces all occurrences of word w in the span.

### Key Technical Components

**Model.** AWD-LSTM (Merity et al., 2018) with the following default hyperparameters (Table 2, Appendix A):

| Hyperparameter | PTB | Wiki |
|---|---|---|
| Word Emb. Size | 400 | 400 |
| Hidden State Dim | 1150 | 1150 |
| Layers | 3 | 3 |
| Sequence Length (BPTT) | 70 | 70 |
| LSTM Layer Dropout | 0.25 | 0.2 |
| Recurrent Dropout | 0.5 | 0.5 |
| Word Emb. Dropout | 0.4 | 0.65 |
| Word Dropout | 0.1 | 0.1 |
| FF Layers Dropout | 0.4 | 0.4 |
| Optimizer | ASGD | ASGD |
| Learning Rate | 30 | 30 |
| Gradient Clip | 0.25 | 0.25 |
| Weight Decay | 1.2e-6 | 1.2e-6 |
| Epochs (train) | 500 | 750 |
| Batch Size | 20 | 80 |

The model uses weight tying between the word embedding and softmax layers (Inan et al., 2017; Press & Wolf, 2017) and dropout on recurrent connections, embedding weights, and all input/output connections (Wan et al., 2013; Gal & Ghahramani, 2016).

**Neural cache** (Grave et al., 2017b), used only in Section 6.2. Records hidden state h_t at each timestep and computes a cache distribution (Equation 5):

> `P_cache(w_t | w_{t-1}, ..., w_1; h_t, ..., h_1) proportional_to sum_{i=1}^{t-1} 1[w_i = w_t] exp(theta * h_i^T * h_t)`

where `theta` controls the flatness of the distribution. This cache distribution is interpolated with the model's output distribution over the vocabulary. Cache size is set to 500 for PTB and 3,875 for Wiki, matching average document lengths in the respective datasets (Section 6.2).

**Three word categories for copy analysis (Section 6):**
- **C_near:** words that can be copied from nearby context (within 50 most recent tokens)
- **C_far:** words that can only be copied from long-range context (beyond 50 tokens)
- **C_none:** words that cannot be copied from context at all (control set)

### Experimental Setup

**Datasets (Table 1, Section 3):**

| | PTB Dev | PTB Test | Wiki Dev | Wiki Test |
|---|---|---|---|---|
| # Tokens | 73,760 | 82,430 | 217,646 | 245,569 |
| Perplexity (no cache) | 59.07 | 56.89 | 67.29 | 64.51 |
| Avg. Sent. Len. | 20.9 | 20.9 | 23.7 | 22.6 |

- **Penn Treebank (PTB):** Wall Street Journal news articles, 0.9M training tokens, 10K vocabulary (Marcus et al., 1993; Mikolov et al., 2010).
- **WikiText-2 (Wiki):** Wikipedia articles, 2.1M training tokens, 33K vocabulary (Merity et al., 2017).

All results are averaged from **three models trained with different random seeds**, with error bars representing standard deviation (or 95% confidence intervals for bar charts). Results are reported on dev sets only; test set consistency is confirmed (Section 3).

POS tags obtained using Stanford CoreNLP (Manning et al., 2014). Content words defined as nouns, verbs, and adjectives; function words as prepositions and determiners (Section 4.1).

**Reproducibility:** Code is publicly available at https://github.com/urvashik/lm-context-analysis (Section 3). Three random seeds are used with error bars reported. All hyperparameters are specified in Appendix A. The AWD-LSTM codebase is also public at https://github.com/salesforce/awd-lstm-lm.

### Key Results

**Effective context size (~200 tokens, Section 4, Figures 1a-b):**
- Loss difference between truncated and infinite context gradually diminishes from 5 to 1000 tokens.
- Only **1% perplexity increase** beyond 150 tokens on PTB and 250 tokens on Wiki (Figure 1a).
- Hyperparameter variations (BPTT 10 vs 70 vs 100, hidden size 575 vs 1150, 2 vs 3 layers, various dropout settings) change absolute perplexity but not the context usage trend (Figure 1b). Complementary Wiki results in Appendix Figure 10a confirm the same pattern.

**Word-type context dependence (Section 4.1, Figures 1c-d):**
- Frequent words (>=800 training occurrences): insensitive to context beyond 50 tokens (Figure 1c).
- Infrequent words: require >200 tokens (Figure 1c).
- Determiners: rely only on last ~10 tokens; nouns and verbs: sensitive to distant context (Figure 1d, Wiki; Appendix Figure 10b, PTB).

**Word order sensitivity (Section 5.1, Figures 2a-b):**

| Perturbation | Range of Sensitivity | Evidence |
|---|---|---|
| Local shuffle/reverse (20-token windows) | Most recent 20 tokens | Figure 2a (PTB and Wiki) |
| Global shuffle/reverse (all tokens before point) | Most recent 50 tokens | Figure 2b (Wiki); Figure 8 (PTB) |
| Random replacement (same length) | Full 200+ token range | Figure 2b (Wiki); Figure 8 (PTB) |

The gap between permutation and replacement curves beyond 50 tokens shows that **word identity matters** in the distant context even though **word order does not** (Section 5.1).

**Content vs. function words in context (Section 5.2, Figure 3 for PTB, Appendix Figure 9 for Wiki):**
- Dropping content words 5 tokens from target: **~65% perplexity increase** (vs ~17% for random drop of same proportion, on PTB).
- Dropping function words: not significantly different from random drop of same proportion.
- Beyond 20 tokens: only content words are relevant.
- On Wiki (Appendix Figure 9): the same pattern holds; content words at 5 tokens cause ~55% increase.

**Copy behavior (Section 6.1, Figure 4a-b for PTB, Appendix Figure 11a-b for Wiki):**
- For C_near: dropping only the target word increases perplexity by **~9%**; dropping all long-range context increases it by only ~3.5% (Figure 4a).
- For C_far: dropping all distant context increases perplexity by **~12%**; dropping only the target increases it by only ~2% (Figure 4a).
- Replacing the target with `<unk>` or a similar word hurts C_near by up to **14%** but has no effect on C_far (Figure 4b).

**Cache effectiveness (Section 6.2, Figure 7):**

| Category | PTB (without cache) | Wiki (without cache) |
|---|---|---|
| C_near | 22% perplexity increase | 32% perplexity increase |
| C_far | 28% perplexity increase | 53% perplexity increase |
| C_none | Cache hurts (~36% of words) | Cache hurts (~20% of words) |

- Cache disproportionately helps C_far words, which is complementary to the LSTM's strength at copying nearby words (Figure 7).
- The cache hurts C_none words due to flat, confused cache distributions when the target is not in the history (Figures 5-6).

---

## Limitations and Failure Modes

**Author-acknowledged limitations:**

1. **Train-test mismatch.** Perturbations are applied only at test time; the model was never trained to handle them. All measured losses are therefore upper bounds (Section 3).
2. **Confounding factors.** Separating model behavior from language characteristics is challenging. Vocabulary size, dataset size, and other factors confound the analysis (Section 7).
3. **Token-level analysis only.** The study reports observations at the token level; deeper understanding of sentence-level interactions is left to future work (Section 8).
4. **Cache failure mode.** The cache hurts a substantial fraction of words (36% on PTB, 20% on Wiki) that cannot be copied from context, because the cache distribution becomes flat and confused (Section 6.2, Figure 6). The authors suggest the model would benefit from having the option to ignore the cache (Section 6.2).

**Inferred limitations (not explicitly stated by authors):**

5. **Only two datasets.** Results are limited to PTB (news, 0.9M tokens) and WikiText-2 (encyclopedia, 2.1M tokens). Generalization to other domains, genres, and dataset scales is untested.
6. **LSTM-only.** The analysis is specific to LSTM language models. Whether the findings generalize to Transformer architectures with self-attention, which can attend to any position directly, is not investigated.
7. **Single model architecture.** Only the AWD-LSTM is tested. Different LSTM variants (e.g., with attention mechanisms, different gating designs) might exhibit different context utilization patterns.

#### Scope and Comparability

- **What was not tested:** No Transformer models, no attention-based architectures, no languages other than English, no datasets beyond PTB and WikiText-2, no model scales beyond the single AWD-LSTM configuration (3 layers, 1150 hidden, 400 embedding). Hyperparameter variation experiments (Section 4) vary one parameter at a time but do not explore interactions.
- **Comparability notes:** The train-test mismatch design means measured losses are upper bounds on the true sensitivity; methods that also train with perturbations (as in later work such as O'Connor & Andreas, 2021) would measure different quantities. The 50-token nearby/long-range boundary is defined empirically from this paper's word order experiments and may not transfer directly to other architectures or datasets. Chelba et al. (2017) reported only 8% perplexity increase at 13 tokens of context on PTB (vs. 25% in this paper) due to training with restricted context (Section 7), illustrating how training regime affects the measured effective context size.

---

## Conclusions

### Contributions

1. **Effective context size quantification.** Empirically demonstrated that LSTM LMs use about 200 tokens of context on average, independent of hyperparameter settings such as model size and BPTT length (Section 4, Figure 1a-b). This is the first systematic measurement spanning up to 1000 tokens across multiple hyperparameter configurations.

2. **Nearby vs. long-range context distinction.** Showed that word order matters only within the most recent ~50 tokens (one sentence for local order, 2-3 sentences for global order), while distant context is represented only as a rough semantic field where word identity matters but order does not (Section 5.1, Figures 2a-b).

3. **Word-type context dependence.** Established that infrequent words and content words require substantially more context than frequent words and function words, with determiners relying on as few as 10 tokens (Section 4.1, Figures 1c-d; Section 5.2, Figure 3).

4. **Copy mechanism analysis.** Demonstrated that LSTMs can regenerate words from nearby context internally but rely on external caches for long-range copying, and that caches disproportionately benefit words available only in distant context (Sections 6.1-6.2, Figures 4, 7).

5. **Cache failure characterization.** Identified that neural caches hurt performance on words not present in context due to flat, uncertain cache distributions, suggesting the model would benefit from the option to ignore the cache (Section 6.2, Figures 5-7).

### Implications

1. The finding that distant context is modeled only as a rough semantic field implies that **bag-of-words-like topic representations may be sufficient for modeling long-range dependencies in LSTMs** (speculative inference from the order-insensitivity result in Section 5.1).

2. The word-type-dependent context usage suggests that **adaptive word dropout strategies** could improve training by differentiating between content and function words (Section 7, speculative).

3. The complementarity between LSTM and cache suggests that **memory-augmented models should explicitly target information not already captured by the base model**, particularly position-specific word identity in distant context (Section 7).

---

## Key Claims

1. **C1: Effective context size is ~200 tokens.** LSTM LMs achieve within 1% perplexity of the infinite-context setting beyond 150 tokens on PTB and 250 on Wiki (Figure 1a, Section 4). Evidence breadth: tested on two datasets (PTB and Wiki), three random seeds per configuration, with consistent results. Single architecture (AWD-LSTM).

2. **C2: Hyperparameters do not change effective context size.** Varying BPTT (10 vs 70 vs 100), hidden size (575 vs 1150), layers (2 vs 3), dropout, and embedding size changes absolute perplexity but not the context usage trend (Figure 1b, Section 4). Evidence breadth: eight hyperparameter variants tested on PTB (Figure 1b), complementary results on Wiki in Appendix Figure 10a.

3. **C3: Infrequent words need more context than frequent words.** Words with >=800 training occurrences are insensitive to context beyond 50 tokens; infrequent words require >200 tokens (Figure 1c, Section 4.1). Evidence breadth: both datasets show the same pattern.

4. **C4: Content words need more context than function words.** Nouns and verbs are sensitive to distant context; determiners rely only on the last ~10 tokens (Figure 1d Wiki, Appendix Figure 10b PTB, Section 4.1). Evidence breadth: both datasets, five POS categories tested.

5. **C5: Local word order matters only within 20 tokens.** Permuting 20-token windows beyond the most recent 20 tokens has negligible effect on loss (Figure 2a, Section 5.1). Evidence breadth: both shuffle and reverse permutations on both datasets.

6. **C6: Global word order matters only within 50 tokens.** Shuffling or reversing all context beyond 50 tokens has no effect on performance (Figure 2b Wiki, Appendix Figure 8 PTB, Section 5.1). Evidence breadth: two permutation types on both datasets.

7. **C7: Word identity matters beyond 50 tokens despite order insensitivity.** The gap between the permutation curve and the random replacement curve beyond 50 tokens shows that word identity contributes even where order does not, indicating a rough semantic/topic representation (Figure 2b, Section 5.1). Evidence breadth: shown on Wiki (Figure 2b) and PTB (Appendix Figure 8).

8. **C8: Content words dominate beyond the first sentence.** Dropping content words 5 tokens from the target increases perplexity by ~65% on PTB (vs ~17% for random drop); beyond 20 tokens, only content words are relevant (Figure 3, Section 5.2). Evidence breadth: PTB (Figure 3) and Wiki (Appendix Figure 9) show consistent patterns, with 95% confidence intervals.

9. **C9: LSTMs copy nearby words directly but use rough semantics for far words.** Dropping only the target word from nearby context increases perplexity by ~9%, while dropping all distant context increases it by ~12% for C_far but only ~3.5% for C_near. Replacing the target hurts C_near by up to 14% but does not affect C_far (Figures 4a-b, Section 6.1). Evidence breadth: PTB (Figure 4) and Wiki (Appendix Figure 11), three perturbation types.

10. **C10: Neural caches disproportionately help long-range copying.** C_far words see 28% (PTB) and 53% (Wiki) perplexity increase without cache, vs 22% (PTB) and 32% (Wiki) for C_near (Figure 7, Section 6.2). Evidence breadth: both datasets, consistent pattern.

11. **C11: Neural caches hurt non-copyable words.** ~36% of PTB words and ~20% of Wiki words (C_none) are hurt by the cache due to flat, confused cache distributions (Figures 5-7, Section 6.2). Evidence breadth: both datasets, illustrated with qualitative examples (Figures 5-6, 12-13).

---

## Open Questions

1. **Do these findings generalize to Transformer-based language models?** The LSTM's sequential processing is fundamentally different from Transformer self-attention, which can attend to any position directly. (Addressed by Liu et al. (2024) -- *Lost in the Middle*, which extends context utilization analysis to Transformer LLMs, and O'Connor & Andreas (2021) -- *What Context Features Can Transformer Language Models Use?*, which adapts the ablation paradigm to Transformers.)

2. **Would the findings hold for languages other than English?** The two datasets are both English-only (Section 7). No subsequent work in the references directory addresses this for LSTM LMs specifically.

3. **Can adaptive word dropout strategies leveraging content/function word distinctions improve training?** Suggested in Section 7 but not tested. Not addressed by subsequent work in the references directory.

4. **How do sentence-level interactions (beyond token-level) affect context utilization?** Explicitly left to future work (Section 8). Not addressed by subsequent work in the references directory.

5. **Can memory-augmented models be designed to capture information orthogonal to the LSTM's representations?** Suggested in Section 7, motivated by the finding that the cache is complementary to the LSTM. Not directly addressed by subsequent work in the references directory.

---

## Core References and Why They Are Referenced

### Language Model Architecture and Training

- **Merity et al. (2018)** -- *Regularizing and Optimizing LSTM Language Models.* Provides the AWD-LSTM architecture and training procedure (ASGD optimizer, regularization techniques) used throughout the paper. All default hyperparameters follow this work.
- **Hochreiter & Schmidhuber (1997)** -- *Long Short-Term Memory.* The foundational LSTM architecture that the paper analyzes; cited in the motivation that LSTMs are designed to capture long-range dependencies.

### Copy Mechanisms

- **Grave et al. (2017b)** -- *Improving Neural Language Models with a Continuous Cache.* The neural cache model analyzed in Section 6, which interpolates a cache distribution over past hidden states with the model output. Cache size and setup replicate this work's original configuration.
- **Grave et al. (2017a)** -- *Unbounded Cache Model for Online Language Modeling with Open Vocabulary.* Alternative caching approach referenced alongside the continuous cache as a successful copy mechanism.
- **Merity et al. (2017)** -- *Pointer Sentinel Mixture Models.* Source of the WikiText-2 dataset and a pointer-based copy mechanism referenced in Section 6.

### Prior Analysis of LSTMs

- **Adi et al. (2017)** -- *Fine-grained Analysis of Sentence Embeddings Using Auxiliary Prediction Tasks.* Showed LSTMs can remember word order within a sentence; this paper extends the analysis beyond sentence level. Also cited in Section 6 for awareness degradation with sequence length.
- **Linzen et al. (2016)** -- *Assessing the Ability of LSTMs to Learn Syntax-Sensitive Dependencies.* Demonstrated LSTMs capture subject-verb agreement; motivates the question of whether syntactic sensitivity extends to long-range context.
- **Li et al. (2016)** -- *Visualizing and Understanding Neural Models in NLP.* Showed LSTMs model semantic compositionality such as negation; referenced as prior work on LSTM interpretability.

### Datasets and Tools

- **Marcus et al. (1993)** -- *Building a Large Annotated Corpus of English: The Penn Treebank.* Source of the PTB dataset.
- **Manning et al. (2014)** -- *The Stanford CoreNLP Natural Language Processing Toolkit.* Used for POS tagging to categorize content and function words.

### Context-Length Analysis

- **Boyd-Graber & Blei (2009)** -- *Syntactic Topic Models.* Previously found that function words rely on less context than content words; corroborated by this paper's Section 4.1 findings.
- **Hill et al. (2016)** -- *The Goldilocks Principle: Reading Children's Books with Explicit Memory Representations.* Prior work on context length effects in language modeling, consistent with findings here.
- **Wang & Cho (2016)** -- *Larger-Context Language Modelling with Recurrent Neural Network.* Prior finding on effective context sizes, consistent with results here.
- **Chelba et al. (2017)** -- *N-gram Language Modeling Using Recurrent Neural Network Estimation.* Found only 8% perplexity increase with 13 tokens of context on PTB (vs. 25% in this paper's setup), attributed to training with restricted context (Section 7).

### Memory-Augmented Models (Discussion)

- **Ghosh et al. (2016)** -- *Contextual LSTM (CLSTM) Models for Large Scale NLP Tasks.* Memory model feeding explicit context representations to the LSTM; cited in Section 7 as a potential beneficiary of orthogonal representations.
- **Lau et al. (2017)** -- *Topically Driven Neural Language Model.* Another memory model cited in Section 7 for the same point.
