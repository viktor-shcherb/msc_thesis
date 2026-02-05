---
title: "Do Long-Range Language Models Actually Use Long-Range Context?"
authors: "Sun, Krishna, Mattarella-Micke, Iyyer"
year: 2021
venue: "EMNLP 2021"
paper_type: conference-paper
categories: ["attention-analysis", "long-context-evaluation", "probing-and-analysis", "attention-efficiency"]
scope: ["long-range context utilization", "token-level vs sequence-level analysis", "perturbation analysis of distant context"]
benchmarks_used: ["perplexity-pg19"]
models_introduced: []
models_evaluated: ["routing-transformer"]
key_claims:
  - id: C1
    claim: "Providing long-range context beyond 2K tokens has negligible impact on aggregate perplexity for both Routing Transformer and Local Transformer"
    evidence: "Section 3, Figure 1"
    status: supported
  - id: C2
    claim: "Infrequent tokens and tokens inside subword clusters benefit from long-range context up to 5K tokens, but the benefit reverses with further context extension"
    evidence: "Section 3, Figures 2 and 3"
    status: supported
  - id: C3
    claim: "Routing Transformer can copy tokens from long-range context: perplexity of tokens whose last occurrence is more than 2K tokens away steadily decreases until 8K prefix length"
    evidence: "Section 3, Figure 4 (left plot)"
    status: supported
  - id: C4
    claim: "Long-range context benefits fictional and continuous books more than non-fictional and discontinuous books"
    evidence: "Section 3, Figures 5 and 6"
    status: supported
  - id: C5
    claim: "Perturbing the long-range context (shuffling or random replacement) beyond 2K tokens from the target has minimal impact on overall perplexity"
    evidence: "Section 4, Figure 7"
    status: supported
  - id: C6
    claim: "Routing Transformer encodes token identity but not word order or discourse structure in the long-range context"
    evidence: "Section 4, Figures 11 and 12"
    status: supported
  - id: C7
    claim: "Both models lose the ability to exploit copied sequences when the duplicate occurs more than 2K tokens away, and long-range context does not improve suffix identification accuracy"
    evidence: "Section 5, Figure 13"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: evaluates
    detail: "Analyzes Transformer-based language models and the limitations of self-attention for encoding long-range context"
  - target: 2020-04-compressive-transformer-pg19
    type: complementary
    detail: "Both study long-range language models on PG-19; Rae et al. show Compressive Transformer improves infrequent token prediction, consistent with Sun et al.'s finding that infrequent tokens benefit from longer context"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer is mentioned as a related long-range LM architecture; not directly evaluated due to lack of PG-19 checkpoints"
  - target: 2025-04-effective-context-length-falls-short
    type: extended-by
    detail: "An et al. provide a mechanistic explanation (left-skewed position frequency distribution) for the effective context length gap that Sun et al. observe empirically at the 2K-token boundary"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Both find positional biases in how models use context; Liu et al. show a U-shaped performance curve, while Sun et al. show that benefits of long-range context are limited to superficial token copying"
  - target: 2025-11-context-length-hurts-performance
    type: complementary
    detail: "Both find that additional context does not help as expected; Du et al. extend this to show context length alone degrades performance even with perfect retrieval"
  - target: 2018-06-prediction-short-memory
    type: complementary
    detail: "Sharan et al. provide theoretical grounding for the empirical finding that long-range context has limited benefit under perplexity: bounded mutual information between past and future implies a Markov model predicts well on average"
  - target: 2021-08-context-features-transformer-lm
    type: concurrent
    detail: "Both study what information long-range transformer LMs extract from distant context using perturbation experiments; O'Connor & Andreas use V-information on GPT-2/WikiText-103 while Sun et al. study Routing Transformer on PG-19, reaching consistent conclusions about the primacy of token identity over word order"
open_questions:
  - question: "Would modern decoder-only LLMs at much larger scale (e.g., 7B-70B parameters) show the same pattern of superficial long-range context use observed in the 490M-parameter Routing Transformer?"
    addressed_by: 2025-04-effective-context-length-falls-short
  - question: "Can architectural modifications beyond sparse attention enable genuine discourse-level understanding from long-range context, rather than just token-level copying?"
    addressed_by: null
  - question: "Does the finding that long-range context primarily helps through token copying generalize to models trained on more diverse corpora beyond PG-19?"
    addressed_by: null
---

# Do Long-Range Language Models Actually Use Long-Range Context?

**Authors:** Simeng Sun, Kalpesh Krishna, Andrew Mattarella-Micke, Mohit Iyyer (University of Massachusetts Amherst, Intuit AI)
**Date:** November 2021, EMNLP 2021, arXiv:2109.09115

---

## Core Research Problem

Transformer language models are constrained by the quadratic complexity of self-attention, which limits the input sequence length. Recent efficient attention methods have extended this from GPT-2's 1024 tokens (Radford et al., 2019) to 4096 tokens (Zaheer et al., 2020) and 8192 tokens (Roy et al., 2021, Routing Transformer). These "long-range" Transformer LMs achieve lower perplexities on the PG-19 benchmark (Rae et al., 2020), but **how they take advantage of the long-range context remains unclear**. Prior analysis of LSTM LMs by Khandelwal et al. (2018) showed perplexity plateaus after only 200 words, and Press et al. (2020) found perplexity flattens after 1K tokens for a smaller standard Transformer. The core question is: **do long-range Transformer LMs actually encode discourse-level information from the distant context, or do they rely on superficial cues?**

---

## Problem Solutions

The paper conducts a fine-grained empirical analysis of two long-range Transformer LMs -- the Routing Transformer (RT) and a Local Transformer (LT) -- using prefix length manipulation, perturbation experiments, and sequence-level prediction tasks on PG-19. The analysis reveals:

1. **Long-range context has negligible aggregate impact.** Overall perplexity plateaus after 2K prefix tokens for both models (Figure 1), despite RT's theoretical ability to attend to 8K tokens.
2. **Only a small subset of tokens benefit.** Infrequent tokens, tokens inside subword clusters, and tokens that can be copied from distant context show decreasing perplexity with longer prefixes (up to ~5K tokens).
3. **The models encode token identity, not discourse structure.** Perturbation experiments (shuffling, random replacement) reveal that RT is insensitive to word order in the long-range context but does memorize token presence.
4. **Long-range context does not help sequence-level tasks.** Both sequence copying and suffix identification tasks show no improvement from context beyond 2K tokens.

---

## Approach Details

### Method

#### Models

Two long-range Transformer LMs are analyzed, both using publicly available PG-19 checkpoints:

**Routing Transformer (RT):** 490M parameters, 22 layers, 8 attention heads per layer, ~98K subword vocabulary, processes sequences up to 8192 tokens. The top two layers use content-based clustering attention that routes queries to the nearest learned centroid, reducing complexity from O(N^2) to O(N^1.5). Achieves 33.2 perplexity on PG-19 test set. The clustering attention computes:

> X_i = sum over {j : K_j in mu(Q_i), j < i} of A_ij * V_j

where mu(Q_i) is the cluster whose centroid is closest to query Q_i.

**Local Transformer (LT):** Derived from the same RT checkpoint by replacing all clustering heads with local attention heads (attending to the previous 256 tokens). This yields an effective receptive field of ~5K tokens (256 * 22 layers, minus overlap). Achieves 38.3 perplexity on PG-19 test (slightly better than the 39.3 reported by Roy et al., 2021, for an LT trained from scratch).

#### Evaluation Setup

All analyses use the PG-19 validation set (50 books, ~3M tokens). For computational feasibility, 220K validation tokens are sampled proportionally from each book. Target tokens per context: k = 10, positioned near the end of each N-token input sequence (specifically tokens at positions [-50:-40] to avoid an RT end-sequence artifact). Losses are scaled by 1.248 to match word-level perplexity following Roy et al. (2021).

### Key Technical Components

#### Prefix Length Analysis (Section 3)

The core experiment varies the prefix length from 512 to 8192 tokens and measures perplexity of the k = 10 target tokens. Results across multiple token categories:

**All tokens (Figure 1):** RT perplexity plateaus after 2K tokens. LT plateaus even earlier at ~1K. The perplexity gap between RT and LT is relatively consistent regardless of prefix length, indicating RT's gains come primarily from better local context modeling, not long-range context.

**By token frequency (Figure 2):** Frequent tokens (top 10% by vocabulary frequency) show no benefit from long-range context. Infrequent tokens (remaining 90%, ~20K of 220K target tokens) show RT perplexity decreasing from ~1200 at 2K prefix to ~1180 at 5K prefix, but then increasing back to ~1200 at 8K.

**By subword position (Figure 3):** First subword tokens in multi-word clusters (~4.1K tokens) show the same pattern as infrequent tokens. Remaining subwords within clusters (~5.1K tokens) show positive impact from long-range context until 5K prefix for RT.

**By copy distance (Figure 4):** Tokens whose last occurrence is more than 2K tokens away (~22K tokens) show steadily decreasing RT perplexity from ~200 at 2K to ~170 at 8K. Tokens never appearing in the prefix (~36K tokens) show a decrease until ~5K, then plateau.

**By book type (Figures 5, 6):** 49 books annotated as fiction (19) vs non-fiction (30) and continuous (18) vs discontinuous (31). RT perplexity for fictional and continuous books continues to decrease until ~5K prefix, while non-fictional and discontinuous books plateau at 2K.

#### Perturbation Analysis (Section 4)

Three perturbation operations applied to the first m tokens of an 8K-token prefix:

1. **Sequence shuffling:** Tokens shuffled across the entire perturbed window.
2. **Random sequence replacement:** Perturbed window replaced with tokens from another validation book.
3. **Specific token drop:** Target tokens within the perturbed window replaced with padding.

**Key Results:**

| Perturbation | All tokens (6K pert.) | Infrequent tokens (6K pert.) | Distant copied tokens (6K pert.) |
|---|---|---|---|
| Unperturbed (8K) | 35.2 | ~1200 | ~170 |
| Shuffle | ~35.3 | ~1210 | ~172 |
| Random replacement | ~35.5 | ~1225 | ~174 |

- Perturbing up to 6K tokens has minimal impact on overall perplexity (Figure 7), though perturbations closer to the target have increasing impact.
- Shuffling achieves slightly *lower* perplexity than the unperturbed baseline for overall tokens, suggesting the model does not encode word order in the long-range context.
- Random replacement is more harmful than shuffling for distant copied tokens (174 vs 172 perplexity), but shuffling is more harmful for subword cluster tokens (3.8 vs 3.7 perplexity) (Figures 10, 11).
- Targeted token drop experiments (Figure 12) confirm RT memorizes token identity: dropping long-range occurrences of target tokens increases their perplexity, while dropping random tokens does not.

#### Sequence-Level Analysis (Section 5)

**Sequence copying:** A duplicate of the target sequence is pasted at various positions in the prefix. Both models achieve very low perplexity when the duplicate is within 512 tokens, but lose the ability to exploit it when the duplicate is more than 2K tokens away (Figure 13, left).

**Suffix identification:** A prefix is paired with the ground-truth next 128 tokens and 5 randomly sampled 128-token negatives from the same book. Accuracy is measured by whether the gold suffix has lower perplexity. Results (Figure 13, right): both RT and LT achieve ~30-45% accuracy, with no improvement from context beyond 2K tokens. RT and LT have nearly identical (and poor) performance, indicating RT's perplexity advantage does not translate to better sequence-level prediction.

### Experimental Setup

- **Dataset:** PG-19 validation set, 49 books (~3M tokens), 220K sampled target tokens
- **Models:** Routing Transformer (490M params, 8192-token context), Local Transformer (derived from same checkpoint, ~5K effective context)
- **Hardware:** RTX8000 GPU; ~104 hours to evaluate entire PG-19 validation set with 8K sequence length
- **Evaluation metric:** Perplexity (word-level, scaled by 1.248 for RT/LT)
- **Perturbation experiments:** 5 runs averaged per perturbation type

### Key Results

| Analysis | Finding | Evidence |
|---|---|---|
| Overall perplexity vs prefix length | Plateaus after 2K tokens for RT | Figure 1 |
| Infrequent token perplexity | Decreases from ~1200 to ~1180 (2K to 5K prefix), then reverses | Figure 2 |
| Distant copied tokens | RT perplexity decreases from ~200 to ~170 (2K to 8K prefix) | Figure 4 |
| Shuffling 6K distant tokens | No notable impact on overall perplexity | Figure 7 |
| Token identity drop | Dropping distant occurrences of target tokens increases their perplexity by ~4 points | Figure 12 |
| Sequence copying beyond 2K | Both models lose ability to exploit duplicate sequences | Figure 13 (left) |
| Suffix identification | ~30-45% accuracy, no improvement from long-range context | Figure 13 (right) |

---

## Limitations and Failure Modes

1. **Only two models analyzed.** The analysis is limited to the Routing Transformer and a Local Transformer derived from the same checkpoint. Other architectures (Compressive Transformer, Longformer) could not be evaluated due to lack of PG-19 checkpoints, and they differ in model size, making controlled comparison infeasible (Section 2.2).

2. **Single dataset (PG-19).** All experiments use the PG-19 benchmark, which consists entirely of pre-1919 books. The findings may not generalize to modern text domains (e.g., code, technical documents, conversational data).

3. **Small model scale by modern standards.** The 490M-parameter models analyzed here are much smaller than modern LLMs. Whether the same patterns hold at larger scales (billions of parameters) is unknown.

4. **End-sequence artifact in RT.** The clustering heads in RT cause the last ~20 tokens of a sequence to have anomalously high perplexity (Figure 14, Appendix A). The authors work around this by evaluating tokens at positions [-50:-40], but this artifact limits the analysis to a specific position range.

5. **Limited perturbation types.** Only three perturbation operations are tested. More nuanced perturbations (e.g., entity replacement, discourse structure manipulation) could reveal different patterns of context use.

6. **PG-19 data quality issues.** The authors discovered an annotated edition of *The Canterbury Tales and Other Poems* that causes a ~10 perplexity gap between test and validation sets due to interleaved line-by-line annotations. This book was removed, but similar quality issues may affect other books in the dataset (Section 2.2, footnote 3).

---

## Conclusions

### Contributions

1. **Established that long-range context beyond 2K tokens has negligible aggregate impact on perplexity.** Despite RT's ability to attend to 8K tokens via content-based routing, overall perplexity plateaus at 2K prefix length, and the RT-LT gap is consistent across prefix lengths (Section 3, Figure 1).

2. **Identified a small subset of tokens that benefit from long-range context.** Infrequent tokens, tokens within subword clusters, and tokens copyable from distant context show perplexity improvements with longer prefixes, with the benefits concentrated in fictional and continuous books (Section 3, Figures 2-6).

3. **Demonstrated through perturbation analysis that RT encodes token identity but not word order in long-range context.** Shuffling up to 6K distant tokens has minimal impact on perplexity, but dropping specific token occurrences in the distant context increases target token perplexity (Section 4, Figures 7, 12).

4. **Showed that long-range context does not help sequence-level prediction.** Both sequence copying and suffix identification tasks reveal no benefit from context beyond 2K tokens, indicating models do not encode discourse structure from distant context (Section 5, Figure 13).

### Implications

1. **Perplexity improvements from longer context are misleading.** The gains from extending context windows come primarily from better local modeling, not from encoding discourse structure. This suggests that perplexity alone is insufficient to evaluate long-range context utilization (inference from Figures 1 and 7).

2. **Future long-range LMs need discourse-aware evaluation.** Standard perplexity evaluation under teacher forcing masks the inability of models to use long-range context for prediction. Sequence-level tasks that require integrating distant information are more informative diagnostics (speculative, based on Section 5 findings).

3. **Document type significantly affects long-range context utility.** The finding that fictional and continuous books benefit more than non-fiction and discontinuous collections suggests that evaluation on diverse document types is necessary to assess long-range modeling capabilities (Section 3, Figures 5-6).

---

## Key Claims

1. **C1: Perplexity plateaus after 2K prefix tokens.** RT perplexity on all target tokens plateaus after 2K prefix tokens (Figure 1). LT perplexity starts flattening even earlier at ~1K. Status: **supported**.

2. **C2: Infrequent tokens benefit from long-range context up to 5K tokens.** RT perplexity of infrequent tokens decreases from ~1200 at 2K prefix to ~1180 at 5K, but increases back to ~1200 at 8K. Tokens within subword clusters show similar patterns (Section 3, Figures 2, 3). Status: **supported**.

3. **C3: RT copies tokens from long-range context.** Perplexity of tokens whose last occurrence is more than 2K tokens away steadily decreases from ~200 to ~170 as prefix extends from 2K to 8K. RT also detects simple patterns like chapter number incrementing across 2300-token distances (Section 3, Figure 4). Status: **supported**.

4. **C4: Book type affects long-range context benefits.** Fictional and continuous books show perplexity improvements until ~5K prefix; non-fictional and discontinuous books plateau at 2K (Section 3, Figures 5, 6). Status: **supported**.

5. **C5: Distant context perturbations have minimal impact on overall perplexity.** Shuffling or randomly replacing up to 6K prefix tokens (leaving 2K unperturbed near the target) does not notably affect aggregate perplexity (Section 4, Figure 7). Status: **supported**.

6. **C6: RT memorizes token identity but not word order in long-range context.** Dropping distant occurrences of target tokens increases their perplexity (Figure 12, right), but shuffling distant context achieves slightly *lower* perplexity than unperturbed prefixes (Figure 7 inset). Status: **supported**.

7. **C7: Long-range context does not help sequence-level tasks.** Both models lose the ability to exploit copied sequences beyond 2K tokens (Figure 13, left). Suffix identification accuracy (~30-45%) does not improve with prefix length beyond 2K, and RT and LT perform nearly identically (Figure 13, right). Status: **supported**.

---

## Open Questions

1. **Would modern decoder-only LLMs at much larger scale show the same superficial use of long-range context?** The 490M-parameter models analyzed here predate the era of multi-billion-parameter LLMs. An et al. (2025) partially address this by showing that effective context length falls short even for Llama 3.1 70B, though for different mechanistic reasons (position frequency distribution). Addressed by: 2025-04-effective-context-length-falls-short.

2. **Can architectural modifications beyond sparse attention enable genuine discourse-level understanding from long-range context?** The paper shows that content-based routing (RT) does not meaningfully improve discourse-level predictions over local attention (LT). Whether other approaches (e.g., memory mechanisms, retrieval augmentation) can achieve genuine long-range discourse modeling remains open. Addressed by: null.

3. **Does the finding that long-range context primarily helps through token copying generalize beyond PG-19?** PG-19 consists entirely of pre-1919 books. Modern text (code, technical documents, dialogue) may exhibit different patterns of long-range dependency. Addressed by: null.

---

## Core References and Why They Are Referenced

### Long-Range Language Models Analyzed
- **Roy et al. (2021)** -- *Efficient Content-Based Sparse Attention with Routing Transformers.* Introduces the Routing Transformer, the primary model analyzed. RT uses content-based clustering attention to extend context to 8192 tokens and achieves SOTA perplexity on PG-19.
- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Introduces sparse attention for long-range modeling; the Local Transformer uses a similar position-based local attention strategy.
- **Rae et al. (2020)** -- *Compressive Transformers for Long-Range Sequence Modelling.* Introduces PG-19 benchmark and Compressive Transformer. The paper notes Compressive Transformer improves infrequent token prediction, consistent with Sun et al.'s findings.

### Foundational Architecture
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational Transformer architecture. The quadratic complexity of self-attention motivates the efficient variants analyzed.

### Prior Context Analysis Work
- **Khandelwal et al. (2018)** -- *Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context.* Direct predecessor analyzing LSTM LMs' context usage, finding perplexity plateaus after 200 words. Several experiments in this paper are inspired by Khandelwal et al.'s methodology.
- **Press et al. (2020)** -- *Shortformer: Better Language Modeling Using Shorter Inputs.* Also observe negligible benefits of long-term context for a smaller Transformer; Sun et al. extend this with larger models and more fine-grained analysis.
- **Sharan et al. (2018)** -- *Prediction with a Short Memory.* Prove that long-term context is not needed for HMM LMs under teacher forcing due to bounded mutual information, providing theoretical grounding for the empirical findings.

### Evaluation Benchmark
- **Rae et al. (2020)** -- *Compressive Transformers for Long-Range Sequence Modelling.* Also introduces PG-19, the long-document benchmark (average document length ~69K tokens) used for all experiments.
- **Zellers et al. (2018)** -- *SWAG: A Large-Scale Adversarial Dataset for Grounded Commonsense Inference.* Inspires the suffix identification task design, adapted from SWAG's multiple-choice format.
