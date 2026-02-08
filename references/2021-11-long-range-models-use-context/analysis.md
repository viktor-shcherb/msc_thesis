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
    scope: "PG-19 validation set, 490M-parameter RT and derived LT, 8192-token max context, teacher-forced evaluation"
    magnitude: "RT perplexity plateaus at ~35.2 after 2K prefix tokens; RT-LT gap consistent regardless of prefix length"
  - id: C2
    claim: "Infrequent tokens and tokens inside subword clusters benefit from long-range context up to 5K tokens, but the benefit reverses with further context extension"
    evidence: "Section 3, Figures 2 and 3"
    status: supported
    scope: "RT on PG-19, infrequent tokens (~20K of 220K target tokens, bottom 90% by vocabulary frequency)"
    magnitude: "Infrequent token perplexity decreases from ~1200 at 2K prefix to ~1180 at 5K prefix, then increases back to ~1200 at 8K"
  - id: C3
    claim: "Routing Transformer can copy tokens from long-range context: perplexity of tokens whose last occurrence is more than 2K tokens away steadily decreases until 8K prefix length"
    evidence: "Section 3, Figure 4 (left plot)"
    status: supported
    scope: "RT on PG-19, ~22K target tokens whose last occurrence is >2K tokens away"
    magnitude: "RT perplexity decreases from ~200 at 2K prefix to ~170 at 8K prefix for distant copied tokens"
  - id: C4
    claim: "Long-range context benefits fictional and continuous books more than non-fictional and discontinuous books"
    evidence: "Section 3, Figures 5 and 6"
    status: supported
    scope: "RT on PG-19 validation set, 49 books (19 fiction, 30 non-fiction; 18 continuous, 31 discontinuous)"
    magnitude: "Fiction/continuous book perplexity continues decreasing until ~5K prefix; non-fiction/discontinuous plateau at 2K"
  - id: C5
    claim: "Perturbing the long-range context (shuffling or random replacement) beyond 2K tokens from the target has minimal impact on overall perplexity"
    evidence: "Section 4, Figure 7"
    status: supported
    scope: "RT on PG-19, perturbation of first m tokens of 8K prefix, 5 runs averaged per perturbation"
    magnitude: "Perturbing up to 6K tokens keeps overall perplexity within ~35.2-35.5 range (vs ~35.2 unperturbed)"
  - id: C6
    claim: "Routing Transformer encodes token identity but not word order or discourse structure in the long-range context"
    evidence: "Section 4, Figures 7, 11, and 12"
    status: supported
    scope: "RT on PG-19, shuffling and targeted token drop perturbations, 5 runs averaged"
    magnitude: "Shuffling 6K distant tokens achieves slightly lower perplexity than unperturbed; dropping distant target token occurrences increases their perplexity by ~4 points"
  - id: C7
    claim: "Both models lose the ability to exploit copied sequences when the duplicate occurs more than 2K tokens away, and long-range context does not improve suffix identification accuracy"
    evidence: "Section 5, Figure 13"
    status: supported
    scope: "RT and LT on PG-19, sequence copying with pasted duplicates, suffix identification with 128-token suffixes and 5 negatives from same book"
    magnitude: "Sequence copying: very low perplexity within 512 tokens, rises to ~35-40 beyond 2K; suffix identification: ~30-45% accuracy with no improvement beyond 2K prefix"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: evaluates
    detail: "Analyzes Transformer-based language models and the limitations of self-attention for encoding long-range context"
  - target: 2018-07-sharp-nearby-fuzzy-far-away
    type: extends
    detail: "Direct methodological predecessor: Sun et al. adapt Khandelwal et al.'s context analysis framework from LSTM LMs to long-range Transformer LMs, extending the analysis with perturbation experiments and sequence-level tasks"
  - target: 2020-04-compressive-transformer-pg19
    type: complementary
    detail: "Both study long-range language models on PG-19; Rae et al. show Compressive Transformer improves infrequent token prediction, consistent with Sun et al.'s finding that infrequent tokens benefit from longer context"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer is mentioned as a related long-range LM architecture; not directly evaluated due to lack of PG-19 checkpoints"
  - target: 2018-06-prediction-short-memory
    type: complementary
    detail: "Sharan et al. provide theoretical grounding for the empirical finding that long-range context has limited benefit under perplexity: bounded mutual information between past and future implies a Markov model predicts well on average"
  - target: 2021-08-context-features-transformer-lm
    type: concurrent
    detail: "Both study what information long-range transformer LMs extract from distant context using perturbation experiments; O'Connor & Andreas use V-information on GPT-2/WikiText-103 while Sun et al. study Routing Transformer on PG-19, reaching consistent conclusions about the primacy of token identity over word order"
  - target: 2025-04-effective-context-length-falls-short
    type: extended-by
    detail: "An et al. provide a mechanistic explanation (left-skewed position frequency distribution) for the effective context length gap that Sun et al. observe empirically at the 2K-token boundary"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Both find positional biases in how models use context; Liu et al. show a U-shaped performance curve, while Sun et al. show that benefits of long-range context are limited to superficial token copying"
  - target: 2025-11-context-length-hurts-performance
    type: complementary
    detail: "Both find that additional context does not help as expected; Du et al. extend this to show context length alone degrades performance even with perfect retrieval"
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

Transformer language models are constrained by the quadratic complexity of self-attention, which limits the input sequence length. Recent efficient attention methods have extended context from GPT-2's 1024 tokens (Radford et al., 2019) to 4096 tokens (Zaheer et al., 2020) and 8192 tokens (Roy et al., 2021, Routing Transformer). These "long-range" Transformer LMs achieve lower perplexities on the PG-19 benchmark (Rae et al., 2020), but **how they take advantage of the long-range context remains unclear**. Prior analysis of LSTM LMs by Khandelwal et al. (2018) showed perplexity plateaus after only 200 words, and Press et al. (2020) found perplexity flattens after 1K tokens for a smaller standard Transformer. The core question is: **do long-range Transformer LMs actually encode discourse-level information from the distant context, or do they rely on superficial cues?**

---

## Problem Solutions

The paper conducts a fine-grained empirical analysis of two long-range Transformer LMs -- the Routing Transformer (RT) and a Local Transformer (LT) -- using prefix length manipulation, perturbation experiments, and sequence-level prediction tasks on PG-19. The analysis reveals:

1. **Long-range context has negligible aggregate impact.** Overall perplexity plateaus after 2K prefix tokens for both models (Figure 1), despite RT's theoretical ability to attend to 8K tokens.
2. **Only a small subset of tokens benefit.** Infrequent tokens, tokens inside subword clusters, and tokens that can be copied from distant context show decreasing perplexity with longer prefixes (up to ~5K tokens).
3. **The models encode token identity, not discourse structure.** Perturbation experiments (shuffling, random replacement, targeted token drop) reveal that RT is insensitive to word order in the long-range context but does memorize token presence.
4. **Long-range context does not help sequence-level tasks.** Both sequence copying and suffix identification tasks show no improvement from context beyond 2K tokens.

---

## Approach Details

### Method

#### Models

Two long-range Transformer LMs are analyzed, both using publicly available PG-19 checkpoints:

**Routing Transformer (RT):** 490M parameters, 22 layers, 8 attention heads per layer, ~98K subword vocabulary, processes sequences up to 8192 tokens. The top two layers use content-based clustering attention that routes queries to the nearest learned centroid, reducing complexity from O(N^2) to O(N^1.5). Achieves 33.2 perplexity on PG-19 test set (Section 2.2). The clustering attention computes:

> X_i = sum over {j : K_j in mu(Q_i), j < i} of A_ij * V_j

where mu(Q_i) is the cluster whose centroid is closest to query Q_i (Section 2.1).

**Local Transformer (LT):** Derived from the same RT checkpoint by replacing all clustering heads with local attention heads (attending to the previous 256 tokens). This yields an effective receptive field of ~5K tokens (256 tokens * 22 layers, minus overlap). Achieves 38.3 perplexity on PG-19 test, slightly better than the 39.3 reported by Roy et al. (2021) for an LT trained from scratch -- possibly because the local attention heads learn better weight matrices from the information in the clustering heads (Section 2.2). A newly released LT checkpoint (24 layers, trained from scratch) was also evaluated in Appendix F, showing the same trends.

#### Evaluation Framework

Language models are evaluated using perplexity, defined as the exponentiated negative log likelihood of a held-out corpus:

> ppl = exp( -1/N * sum_{i=1}^{N} log p(w_i | w_{<i}) )

where p(w_i | w_{<i}) is the model's probability for each token given its prefix (Section 2.1). Losses are scaled by 1.248 to match word-level perplexity following Roy et al. (2021).

All analyses use the PG-19 validation set (50 books, ~3M tokens). For computational feasibility, 220K validation tokens are sampled proportionally from each book. Target tokens per context: k = 10, positioned near the end of each N-token input sequence (specifically tokens at positions [-50:-40] to avoid an RT end-sequence artifact where the last ~20 tokens have anomalously high perplexity due to clustering heads, see Appendix A). On one RTX8000 GPU, it takes ~104 hours to evaluate the entire PG-19 validation set with 8K sequence length (Section 2.2, single dataset and two models -- limited evidence breadth).

### Key Technical Components

#### Prefix Length Analysis (Section 3)

The core experiment varies the prefix length from 512 to 8192 tokens and measures perplexity of the k = 10 target tokens. Results across multiple token categories:

**All tokens (Figure 1):** RT perplexity plateaus after 2K tokens. LT plateaus even earlier at ~1K. The perplexity gap between RT and LT is relatively consistent regardless of prefix length, indicating that **much of RT's gains come from better local context modeling, not long-range context** (Section 3, two models compared -- limited evidence breadth).

**By token frequency (Figure 2):** Frequent tokens (top 10% by vocabulary frequency) show no benefit from long-range context. Infrequent tokens (remaining 90%, ~20K of 220K target tokens) show RT perplexity decreasing from ~1200 at 2K prefix to ~1180 at 5K prefix, but then increasing back to ~1200 at 8K (Section 3). The LT is significantly worse on infrequent token prediction, and its perplexity increases with prefix length -- likely an artifact of eliminating routing attention heads from the RT checkpoint, since the LT trained from scratch does not exhibit this behavior (Appendix F).

**By subword position (Figure 3):** Words split into multiple subword tokens are analyzed by position within the cluster. First subword tokens (~4.1K tokens) exhibit the same curve shape as infrequent tokens. Remaining subwords within clusters (~5.1K tokens) show positive impact from long-range context until 5K prefix for RT (Section 3).

**By copy distance (Figure 4):** Tokens whose last occurrence is more than 2K tokens away (~22K tokens) show steadily decreasing RT perplexity from ~200 at 2K to ~170 at 8K. Tokens never appearing in the prefix (~36K tokens) show a decrease until ~5K, then plateau. There is some overlap between token categories, but the authors verify in Appendix C (Table 2) that the overlap is not significant enough to confound results -- the maximum overlap ratio is 0.36 (between in-subword and infrequent tokens), with most ratios below 0.1.

**Pattern following:** Beyond simple token copying, the RT model picks up on some simple patterns. For example, it learns to increment chapter numbers even when the previous chapter title appears more than 2K tokens away: modifying "Chapter IV" (2300 tokens away) to "Chapter V" increases the loss of the predicted token "V" by over 10 (Section 3, qualitative observation -- single example, limited evidence).

**By book type (Figures 5, 6):** 49 validation books annotated as fiction (19) vs non-fiction (30) and continuous (18) vs discontinuous (31), with 25 books both non-fiction and discontinuous. RT perplexity for fictional and continuous books continues to decrease until ~5K prefix, while non-fictional and discontinuous books plateau at 2K. The improvement on tokens inside subword clusters also comes primarily from fictional and continuous books (Section 3, Figures 5-6; Appendix B provides further breakdowns by genre, continuity, and authorship).

#### Perturbation Analysis (Section 4)

Three perturbation operations are applied to the first m tokens of an 8K-token prefix. Formally, given a prefix P = (w_0, w_1, ..., w_n), a perturbation rho is applied to the first m tokens to obtain:

> tilde-P = (rho(w_0, ..., w_m), w_{m+1}, ..., w_n)

The three perturbation operations (results averaged over 5 runs each):

1. **Sequence shuffling:** Tokens within the perturbed window w_{0:m} shuffled across the entire window (sentence boundaries not respected).
2. **Random sequence replacement:** Perturbed window replaced with m tokens from another validation book.
3. **Specific token drop:** Specific tokens within the perturbed window (e.g., those that occur in the target) dropped and replaced with the padding token.

Only RT results are presented in the main text because the LT never uses context beyond 3K tokens (Appendix D, Figure 20).

**Key Results (Figures 7, 9, 10, 11):**

- **All tokens (Figure 7):** Perturbing up to 6K tokens has minimal impact on overall perplexity -- both shuffling and random replacement keep perplexity within the ~35.2-35.5 range. Beyond 6K perturbation (encroaching on the 2K local window), perplexity rises sharply to ~40-42 at full 8K perturbation (5 runs averaged -- moderate evidence).
- **By token frequency (Figure 9):** Frequent tokens are largely unaffected by perturbation up to 6K. Infrequent tokens show increasing perplexity as perturbation approaches the target, with sharp increases beyond 5K perturbation length.
- **By subword position (Figure 10):** Both shuffling and random replacement increase perplexity of tokens inside subword clusters, with shuffling having more negative impact than random replacement (e.g., for rest-of-subword tokens at 6K perturbation: shuffling ~3.8 vs random ~3.7 perplexity, Section 4).
- **By copy distance (Figure 11):** Both perturbation operations increase the perplexity of tokens whose last occurrence is >2K tokens away. Random replacement is more harmful than shuffling for distant copied tokens (e.g., at 6K perturbation: random ~174 vs shuffling ~172 perplexity, Section 4).
- **Crucially, shuffling distant context achieves slightly *lower* perplexity than the unperturbed baseline for overall tokens**, suggesting the model does not encode word order in the long-range context (Figure 7 inset, Section 4).

**Token identity encoding (Figure 12):** Targeted token drop experiments confirm RT memorizes token identity. Dropping long-range occurrences of target tokens (those whose last occurrence is >2K tokens away) increases their perplexity (from ~168 to ~172 as perturbation length increases from 2K to 8K), while dropping the same number of random tokens has no effect (~168-169, flat). For tokens whose last occurrence is within the previous 2K tokens, dropping their distant occurrences has no effect (~14.1-14.3 for both conditions), confirming the model relies only on the most recent occurrences for prediction (Section 4, Figure 12).

#### Sequence-Level Analysis (Section 5)

**Sequence copying (Figure 13, left):** A duplicate of the target sequence is pasted at various positions in the prefix. Both models achieve very low perplexity (~10-15) when the duplicate is within 512 tokens, but **both models lose the ability to exploit the copied sequence when the duplicate is more than 2K tokens away** (perplexity rises to ~35-40 and remains flat). This confirms that sequence order is not encoded in the long-range context (Section 5).

**Suffix identification (Figure 13, right):** A prefix is paired with the ground-truth next 128 tokens and 5 randomly sampled 128-token negatives from the same book, constrained to start at sentence boundaries. The model predicts correctly when the gold suffix has lower perplexity than all negatives. Out of 7K examples, both RT and LT achieve ~30-45% accuracy, **with no improvement from context beyond 2K tokens**. RT and LT have nearly identical (and poor) performance, indicating RT's perplexity advantage does not translate to better sequence-level prediction (Section 5, Figure 13). The model often assigns lower perplexity to obviously wrong suffixes -- for example, in the *Beyond the City* example (Appendix E, Tables 3-4), the gold suffix receives perplexity 74.4 while two wrong suffixes receive perplexity 34.6 and 33.54 (two models tested, single dataset -- limited evidence breadth).

**Suffix length variation (Appendix E, Figure 21):** Accuracy peaks at suffix length 10-20 (~55-58%), then decreases as suffix length increases to 128 (~38-40%). This is likely because longer suffixes become more probable as they incorporate more local context. Regardless of suffix length, no improvement is observed from context beyond 2K tokens.

### Experimental Setup

- **Dataset:** PG-19 validation set, 49 books (~3M tokens), 220K sampled target tokens proportional to book length. One book (*The Canterbury Tales and Other Poems*, an annotated edition) causes a ~10 perplexity gap between test and validation sets due to interleaved annotations; it was removed from experiments (Section 2.2, footnote 3).
- **Models:** Routing Transformer (490M params, 8192-token context, trained on 128 TPUv3 cores for several weeks), Local Transformer (derived from same checkpoint, ~5K effective context). A newly released LT checkpoint (24 layers) was also evaluated in Appendix F with consistent trends.
- **Hardware:** RTX8000 GPU; ~104 hours to evaluate entire PG-19 validation set with 8K sequence length and k=10 target tokens. Each 8K-token forward pass takes ~1.3-1.4 seconds (Section 2.2, Ethical Concerns).
- **Evaluation metric:** Perplexity (word-level, scaled by 1.248 for RT/LT)
- **Perturbation experiments:** 5 runs averaged per perturbation type (Section 4)
- **Suffix identification:** 7K examples constructed, 128-token suffixes with 5 negatives from same book (Section 5)
- **Reproducibility:** Code and checkpoints available at https://github.com/google-research/google-research/tree/master/routing_transformer. No variance estimates reported for non-perturbation experiments. Seeds not reported.

### Key Results

| Analysis | Finding | Evidence |
|---|---|---|
| Overall perplexity vs prefix length | Plateaus after 2K tokens for RT, ~1K for LT | Figure 1 |
| Infrequent token perplexity (RT) | Decreases from ~1200 to ~1180 (2K to 5K prefix), then reverses to ~1200 at 8K | Figure 2 |
| Distant copied tokens (RT) | Perplexity decreases from ~200 to ~170 (2K to 8K prefix) | Figure 4 (left) |
| Tokens not in prefix (RT) | Perplexity decreases until ~5K, then plateaus | Figure 4 (right) |
| Fiction vs non-fiction (RT) | Fiction perplexity continues decreasing until ~5K; non-fiction plateaus at 2K | Figure 5 |
| Shuffling 6K distant tokens | Overall perplexity within ~35.2-35.5 range (5 runs averaged) | Figure 7 |
| Token identity drop | Dropping distant target token occurrences increases their perplexity from ~168 to ~172 | Figure 12 (right) |
| Sequence copying beyond 2K | Both models lose ability to exploit duplicates (perplexity rises to ~35-40) | Figure 13 (left) |
| Suffix identification | ~30-45% accuracy, no improvement from long-range context; RT and LT nearly identical | Figure 13 (right) |
| Suffix length variation | Accuracy peaks at suffix length 10-20 (~55-58%), decreases for longer suffixes | Figure 21 (Appendix E) |

---

## Limitations and Failure Modes

1. **Only two models analyzed.** The analysis is limited to the Routing Transformer and a Local Transformer derived from the same checkpoint. Other architectures (Compressive Transformer, Longformer) could not be evaluated due to lack of PG-19 checkpoints, and they differ in model size, making controlled comparison infeasible (Section 2.2).

2. **Single dataset (PG-19).** All experiments use the PG-19 benchmark, which consists entirely of pre-1919 books. The authors note PG-19 contains diverse document types but the dataset predates modern text domains (Section 2.2).

3. **End-sequence artifact in RT.** The clustering heads in RT cause the last ~20 tokens of a sequence to have anomalously high perplexity (Figure 14, Appendix A). The authors work around this by evaluating tokens at positions [-50:-40], but this artifact limits the analysis to a specific position range (Section 2.2, Appendix A).

4. **PG-19 data quality issues.** The authors discovered an annotated edition of *The Canterbury Tales and Other Poems* that causes a ~10 perplexity gap between test and validation sets. This book was removed, but similar quality issues may affect other books (Section 2.2, footnote 3).

5. **[Inferred]** Small model scale by modern standards. The 490M-parameter models analyzed here are much smaller than modern LLMs (7B-70B+ parameters). Whether the same patterns hold at larger scales is unknown.

6. **[Inferred]** Limited perturbation types. Only three perturbation operations are tested (shuffling, random replacement, targeted token drop). More nuanced perturbations (e.g., entity replacement, discourse structure manipulation, paraphrase) could reveal different patterns of context use.

7. **[Inferred]** No variance estimates for most experiments. Perturbation experiments report 5-run averages, but the prefix length experiments and sequence-level analyses do not report variance or confidence intervals, limiting assessment of statistical significance.

8. **[Inferred]** Generalizability to modern text domains. PG-19 consists entirely of pre-1919 books. Code, technical documents, dialogue, and other modern text types may exhibit different long-range dependency patterns.

#### Scope and Comparability

- **What was not tested:** Models larger than 490M parameters; architectures with memory mechanisms (Compressive Transformer), learned attention spans (Longformer), or recurrence (Transformer-XL); datasets other than PG-19; languages other than English; generation tasks (all evaluation is perplexity-based under teacher forcing, except the suffix identification task).
- **Comparability notes:** The Local Transformer is derived from the RT checkpoint (not trained from scratch), which may give it better representations than a true local-attention baseline, though the newly released LT from scratch (Appendix F) shows the same trends. The RT evaluation setup (k=10 target tokens at positions [-50:-40], 220K sampled tokens, loss scaling by 1.248) differs from standard evaluation protocols, making direct perplexity comparisons with other papers' reported numbers require care. The 2K-token boundary identified here should be compared cautiously with findings from other papers using different effective-length thresholds.

---

## Conclusions

### Contributions

1. **Established that long-range context beyond 2K tokens has negligible aggregate impact on perplexity.** Despite RT's ability to attend to 8K tokens via content-based routing, overall perplexity plateaus at 2K prefix length, and the RT-LT gap is consistent across prefix lengths, indicating RT's advantage comes from better local modeling (Section 3, Figure 1; single dataset, two models).

2. **Identified a small subset of tokens that benefit from long-range context.** Infrequent tokens, tokens within subword clusters, and tokens copyable from distant context show perplexity improvements with longer prefixes, with the benefits concentrated in fictional and continuous books (Section 3, Figures 2-6; Appendix B provides further breakdowns).

3. **Demonstrated through perturbation analysis that RT encodes token identity but not word order in long-range context.** Shuffling up to 6K distant tokens has minimal impact on perplexity (in fact achieves slightly lower perplexity than unperturbed), but dropping specific token occurrences in the distant context increases target token perplexity (Section 4, Figures 7, 12; 5-run averages).

4. **Showed that long-range context does not help sequence-level prediction.** Both sequence copying and suffix identification tasks reveal no benefit from context beyond 2K tokens, with RT and LT performing nearly identically on suffix identification despite RT's substantial token-level perplexity advantage (Section 5, Figure 13).

5. **Revealed that PG-19 document diversity significantly affects long-range context utility.** Fictional and continuous books benefit more from extended context than non-fiction and discontinuous collections, with the improvement concentrated in subword cluster tokens (Section 3, Figures 5-6).

### Implications

1. **Perplexity improvements from longer context windows may be misleading.** The gains from extending context come primarily from better local modeling, not from encoding discourse structure. This suggests perplexity alone is insufficient to evaluate long-range context utilization (inference from Figures 1 and 7).

2. **Future long-range LMs need discourse-aware evaluation.** Standard perplexity evaluation under teacher forcing masks the inability of models to use long-range context for prediction. Sequence-level tasks that require integrating distant information are more informative diagnostics (speculative, based on Section 5 findings).

3. **Document type significantly affects long-range context utility.** The finding that fictional and continuous books benefit more than non-fiction and discontinuous collections suggests that evaluation on diverse document types is necessary to assess long-range modeling capabilities (Section 3, Figures 5-6).

---

## Key Claims

1. **C1: Perplexity plateaus after 2K prefix tokens.** RT perplexity on all target tokens plateaus after 2K prefix tokens, with LT flattening even earlier at ~1K (Figure 1). The RT-LT gap remains consistent regardless of prefix length, suggesting RT's advantage comes from local context modeling. Scope: PG-19 validation set, 490M-parameter RT, teacher-forced evaluation. Magnitude: RT plateaus at ~35.2 perplexity. Status: **supported** (single dataset, two models -- limited evidence breadth).

2. **C2: Infrequent tokens benefit from long-range context up to 5K tokens.** RT perplexity of infrequent tokens decreases from ~1200 at 2K prefix to ~1180 at 5K, but increases back to ~1200 at 8K. Tokens within subword clusters show similar patterns (Section 3, Figures 2, 3). Scope: ~20K infrequent target tokens out of 220K, bottom 90% by vocabulary frequency. Magnitude: ~20-point perplexity decrease (1200 to 1180) then reversal. Status: **supported** (single dataset, no variance reported).

3. **C3: RT copies tokens from long-range context.** Perplexity of tokens whose last occurrence is more than 2K tokens away steadily decreases from ~200 to ~170 as prefix extends from 2K to 8K. RT also detects simple patterns like chapter number incrementing across 2300-token distances (Section 3, Figure 4). Scope: ~22K target tokens with last occurrence >2K away. Magnitude: ~30-point perplexity decrease (200 to 170). Status: **supported** (pattern-following observation based on single qualitative example).

4. **C4: Book type affects long-range context benefits.** Fictional and continuous books show perplexity improvements until ~5K prefix; non-fictional and discontinuous books plateau at 2K (Section 3, Figures 5, 6). The improvement on tokens inside subword clusters also comes primarily from fictional and continuous books (Appendix B, Figures 15-17). Scope: 49 books annotated (19 fiction, 30 non-fiction; 18 continuous, 31 discontinuous; 25 both non-fiction and discontinuous). Magnitude: fiction/continuous perplexity continues decreasing to ~5K while non-fiction/discontinuous plateau at 2K. Status: **supported** (manual annotation of book types -- moderate evidence).

5. **C5: Distant context perturbations have minimal impact on overall perplexity.** Shuffling or randomly replacing up to 6K prefix tokens (leaving 2K unperturbed near the target) keeps aggregate perplexity within ~35.2-35.5 (Section 4, Figure 7). Beyond 6K perturbation, perplexity rises sharply. Scope: RT on PG-19, 5 runs averaged per perturbation. Magnitude: <0.3 perplexity difference for up to 6K perturbation. Status: **supported** (5-run averages -- moderate evidence).

6. **C6: RT memorizes token identity but not word order in long-range context.** Shuffling distant context achieves slightly *lower* perplexity than unperturbed prefixes (Figure 7 inset), showing insensitivity to word order. Dropping distant occurrences of target tokens increases their perplexity from ~168 to ~172 (Figure 12, right), while dropping random tokens has no effect. Scope: RT on PG-19, 5 runs averaged for perturbation; targeted token drop for ~22K distant copied tokens. Magnitude: ~4-point perplexity increase from targeted token drop. Status: **supported** (5-run averages -- moderate evidence).

7. **C7: Long-range context does not help sequence-level tasks.** Both models lose the ability to exploit copied sequences beyond 2K tokens -- very low perplexity within 512 tokens rising to ~35-40 beyond 2K (Figure 13, left). Suffix identification accuracy (~30-45%) does not improve with prefix length beyond 2K, and RT and LT perform nearly identically (Figure 13, right). The model assigns lower perplexity to wrong suffixes (e.g., gold ppl=74.4 vs negative ppl=33.54, Tables 3-4). Scope: RT and LT on PG-19, 7K suffix identification examples with 128-token suffixes, duplicates pasted at varying distances. Magnitude: ~30-45% accuracy (vs 16.7% random chance for 6 choices). Status: **supported** (two models, single dataset, single suffix length in main text -- limited evidence breadth; Appendix E confirms across multiple suffix lengths).

---

## Open Questions

1. **Would modern decoder-only LLMs at much larger scale show the same superficial use of long-range context?** The 490M-parameter models analyzed here predate the era of multi-billion-parameter LLMs. An et al. (2025) partially address this by showing that effective context length falls short even for Llama 3.1 70B, though for different mechanistic reasons (position frequency distribution). Addressed by: 2025-04-effective-context-length-falls-short.

2. **Can architectural modifications beyond sparse attention enable genuine discourse-level understanding from long-range context?** The paper shows that content-based routing (RT) does not meaningfully improve discourse-level predictions over local attention (LT). Whether memory mechanisms, retrieval augmentation, or other approaches can achieve genuine long-range discourse modeling remains open. Addressed by: null.

3. **Does the finding that long-range context primarily helps through token copying generalize beyond PG-19?** PG-19 consists entirely of pre-1919 books. Modern text (code, technical documents, dialogue) may exhibit different patterns of long-range dependency. Addressed by: null.

---

## Core References and Why They Are Referenced

### Long-Range Language Models Analyzed

- **Roy et al. (2021)** -- *Efficient Content-Based Sparse Attention with Routing Transformers.* Introduces the Routing Transformer, the primary model analyzed. RT uses content-based clustering attention to extend context to 8192 tokens and achieves state-of-the-art perplexity on PG-19. Published in TACL.

- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Introduces sparse attention for long-range modeling; the Local Transformer uses a similar position-based local attention strategy.

- **Rae et al. (2020)** -- *Compressive Transformers for Long-Range Sequence Modelling.* Introduces PG-19 benchmark and Compressive Transformer. Mentioned as a model that could not be evaluated due to lack of PG-19 checkpoints. The paper notes Compressive Transformer improves infrequent token prediction, consistent with Sun et al.'s findings.

### Foundational Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational Transformer architecture. The quadratic complexity of self-attention motivates the efficient variants analyzed.

### Prior Context Analysis Work

- **Khandelwal et al. (2018)** -- *Sharp Nearby, Fuzzy Far Away: How Neural Language Models Use Context.* Direct methodological predecessor analyzing LSTM LMs' context usage, finding perplexity plateaus after 200 words. Sun et al.'s experimental design is directly inspired by this work's methodology, extending it with perturbation experiments and sequence-level tasks.

- **Sharan et al. (2018)** -- *Prediction with a Short Memory.* Prove that long-term context is not needed for HMM LMs under teacher forcing due to bounded mutual information, providing theoretical grounding for the empirical findings.

- **Press et al. (2020)** -- *Shortformer: Better Language Modeling Using Shorter Inputs.* Also observe negligible benefits of long-term context for a smaller Transformer; Sun et al. extend this with larger models and more fine-grained analysis.

- **Rae and Razavi (2020)** -- *Do Transformers Need Deep Long-Range Memory?* Conduct analysis exclusively for the Transformer-XL model; Sun et al. analyze more advanced architectures.

### Efficient Transformer Variants (Related Work)

- **Zaheer et al. (2020)** -- *Big Bird: Transformers for Longer Sequences.* Extends context to 4096 tokens with sparse attention; contextualizes the progression of context lengths.

- **Kitaev et al. (2020)** -- *Reformer: The Efficient Transformer.* Hash-based efficient attention variant mentioned as related work.

- **Katharopoulos et al. (2020)** -- *Transformers Are RNNs: Fast Autoregressive Transformers with Linear Attention.* Linear attention variant mentioned as related work.

### Evaluation Benchmark and Task Design

- **Rae et al. (2020)** -- *Compressive Transformers for Long-Range Sequence Modelling.* Also introduces PG-19, the long-document benchmark (average document length ~69K tokens) used for all experiments.

- **Zellers et al. (2018)** -- *SWAG: A Large-Scale Adversarial Dataset for Grounded Commonsense Inference.* Inspires the suffix identification task design, adapted from SWAG's multiple-choice format to a perplexity-based selection among 6 suffixes.
