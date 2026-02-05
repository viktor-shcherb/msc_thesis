---
title: "How Long-Context Benchmarks Construct Length, and What Their Choices Reveal"
research_question: "How do long-context benchmarks construct their length dimension, and what do their methodological choices reveal about what is actually being measured?"
date_produced: 2026-02-05
corpus:
  - 2021-05-long-range-arena
  - 2021-11-long-range-models-use-context
  - 2022-12-scrolls-long-language-sequences
  - 2023-11-needle-in-a-haystack
  - 2023-12-zeroscrolls-zero-shot-long-text
  - 2024-02-lost-in-the-middle
  - 2024-06-ada-leval-length-adaptable-benchmark
  - 2024-08-flenqa-input-length-reasoning
  - 2024-08-infinitebench-long-context-evaluation
  - 2024-08-l-eval-standardized-evaluation
  - 2024-08-longbench-bilingual-benchmark
  - 2024-10-ruler-context-size
  - 2024-11-genuinely-difficult-long-context
  - 2024-12-babilong-long-context-reasoning
  - 2025-03-longiclbench-long-in-context-learning
  - 2025-04-effective-context-length-falls-short
  - 2025-07-longbench-v2
  - 2025-07-nolima-long-context-evaluation
  - 2025-11-context-length-hurts-performance
  - 2026-01-longbench-pro
corpus_search_strategy: |
  category benchmarking
  category long-context-evaluation
  text "length"
  text "benchmark"
  text "haystack"
  text "synthetic"
categories: ["benchmarking", "long-context-evaluation"]
themes:
  - id: length-construction-taxonomy
    label: "A taxonomy of length construction strategies"
  - id: confounds-in-length-scaling
    label: "Confounds introduced by each construction strategy"
  - id: literal-overlap-shortcut
    label: "Literal overlap as a pervasive shortcut"
  - id: length-vs-difficulty
    label: "Disentangling length from task difficulty"
  - id: what-benchmarks-actually-measure
    label: "What benchmarks actually measure vs. what they claim"
consensus_claims:
  - claim: "Every length construction strategy introduces confounds that covary with the length dimension, and no single benchmark isolates pure context-length effects across realistic tasks"
    sources: ["2024-08-flenqa-input-length-reasoning", "2025-11-context-length-hurts-performance", "2024-11-genuinely-difficult-long-context", "2024-10-ruler-context-size"]
    strength: strong
  - claim: "Benchmarks that pad with irrelevant text (NIAH, BABILong, RULER) conflate length with signal-to-noise ratio, while benchmarks that use naturally long documents (SCROLLS, LongBench v2) conflate length with task complexity"
    sources: ["2024-08-flenqa-input-length-reasoning", "2024-11-genuinely-difficult-long-context", "2024-10-ruler-context-size", "2024-12-babilong-long-context-reasoning", "2022-12-scrolls-long-language-sequences", "2025-07-longbench-v2"]
    strength: strong
  - claim: "High literal overlap between queries and relevant context (ROUGE-1 up to 0.966) enables surface-level token matching that inflates benchmark scores, masking failures in genuine long-context reasoning"
    sources: ["2025-07-nolima-long-context-evaluation", "2024-10-ruler-context-size", "2024-08-infinitebench-long-context-evaluation"]
    strength: strong
  - claim: "Benchmarks using naturally long documents without truncation controls cannot establish that their tasks actually require full-context comprehension, as demonstrated by cases where truncation improves or negligibly affects performance"
    sources: ["2022-12-scrolls-long-language-sequences", "2024-06-ada-leval-length-adaptable-benchmark", "2024-08-l-eval-standardized-evaluation"]
    strength: strong
  - claim: "Perplexity is a misleading proxy for long-context capability, showing negative correlation with downstream task performance and failing to detect reasoning degradation"
    sources: ["2024-08-flenqa-input-length-reasoning", "2024-12-babilong-long-context-reasoning", "2021-11-long-range-models-use-context"]
    strength: strong
  - claim: "Synthetic benchmarks with controllable length (RULER, BABILong, Ada-LEval) offer superior experimental control but have unvalidated proxy relationships with realistic long-context tasks"
    sources: ["2024-10-ruler-context-size", "2024-12-babilong-long-context-reasoning", "2024-06-ada-leval-length-adaptable-benchmark", "2025-07-longbench-v2"]
    strength: moderate
contested_claims:
  - claim: "Whether padding-based length construction measures context-length ability or merely information retrieval under increasing noise"
    for: ["2024-10-ruler-context-size", "2024-12-babilong-long-context-reasoning"]
    against: ["2025-07-nolima-long-context-evaluation", "2024-08-flenqa-input-length-reasoning", "2024-11-genuinely-difficult-long-context"]
    resolution: "Both aspects are present. FLenQA's duplicate-padding experiment isolates length from noise, showing degradation even without distractors. Du et al.'s attention-masking experiment (`2025-11-context-length-hurts-performance`) provides the strongest causal evidence: even when all padding tokens are invisible to the attention mechanism, performance degrades 7.9%--50% at 30K tokens. However, most padding-based benchmarks (RULER, BABILong) simultaneously increase noise, making their measured degradation a composite of both factors."
    resolved: true
  - claim: "Whether naturally long documents or synthetic constructions provide more valid measures of long-context capability"
    for: ["2025-07-longbench-v2", "2026-01-longbench-pro", "2022-12-scrolls-long-language-sequences"]
    against: ["2024-10-ruler-context-size", "2024-06-ada-leval-length-adaptable-benchmark"]
    resolution: "Unresolved. Natural documents have ecological validity but uncontrollable length and unverified full-context necessity. Synthetic constructions have experimental control but unvalidated proxy relationships with real tasks. The field lacks a benchmark that combines both. LongBench Pro (`2026-01-longbench-pro`) represents the most comprehensive natural-document effort but explicitly does not experimentally manipulate length."
    resolved: false
gaps:
  - description: "No benchmark simultaneously controls for length, task difficulty, literal overlap, signal-to-noise ratio, and information position while using realistic text"
    severity: high
  - description: "The proxy relationship between synthetic benchmark tasks (variable tracking, frequency counting) and realistic NLP tasks (coreference resolution, summarization) has never been empirically validated"
    severity: high
  - description: "No study has systematically compared how the same model performs on the same underlying task when length is constructed via different strategies (padding vs. distractor addition vs. naturally long documents)"
    severity: high
  - description: "Generation tasks (open-ended writing, long-form summarization) are poorly represented across all benchmarks; most tasks are extractive or classificatory"
    severity: medium
  - description: "The interaction between length construction method and position bias has not been studied; the lost-in-the-middle effect may differ depending on how length was achieved"
    severity: medium
  - description: "Multilingual evaluation of length construction effects is absent; nearly all controlled-length benchmarks are English-only"
    severity: medium
overall_confidence:
  - conclusion: "Context length alone, independent of retrieval difficulty or distraction, degrades LLM reasoning performance"
    level: high
    basis: "3 papers with complementary controls -- FLenQA (duplicate padding), Du et al. (attention masking), NoLiMa (position-aligned analysis) -- all showing degradation attributable to length itself"
    caveats: ["All controlled studies test relatively simple tasks (True/False, short-answer)", "Maximum controlled length is 30K tokens, far below claimed context windows", "Mechanistic explanation is only partially understood (positional distribution bias)"]
  - conclusion: "Literal lexical overlap between questions and needles is a major confound in existing benchmarks"
    level: high
    basis: "NoLiMa provides quantitative measurements (ROUGE-1 0.069 vs 0.905 for NIAH) and ablations showing 16x reduction in effective length when overlap is removed"
    caveats: ["NoLiMa tests only 58 question-needle pairs", "Applies primarily to retrieval-style tasks; aggregation tasks may be less affected"]
  - conclusion: "No existing benchmark provides a valid measure of 'long-context capability' as a unitary construct"
    level: moderate
    basis: "Goldman et al.'s taxonomy shows benchmarks target different capability dimensions; no benchmark scores correlate across dimensions"
    caveats: ["The dispersion/scope taxonomy is informal and not empirically validated", "Correlation studies between benchmark types have not been conducted"]
---

# How Long-Context Benchmarks Construct Length, and What Their Choices Reveal

**Research question:** How do long-context benchmarks construct their length dimension, and what do their methodological choices reveal about what is actually being measured?
**Corpus:** 20 papers, 2021--2026.
**Categories:** benchmarking, long-context-evaluation.

---

## Executive Summary

- **Six distinct strategies for constructing benchmark length exist across the corpus**, each introducing different confounds: byte inflation, naturally long documents, haystack padding, distractor injection, demonstration concatenation, and controlled padding with fixed tasks (`2021-05-long-range-arena`, `2022-12-scrolls-long-language-sequences`, `2023-11-needle-in-a-haystack`, `2024-02-lost-in-the-middle`, `2025-03-longiclbench-long-in-context-learning`, `2024-08-flenqa-input-length-reasoning`).

- **Context length alone degrades reasoning, independent of retrieval or distraction.** Du et al. (`2025-11-context-length-hurts-performance`) provide the strongest causal evidence: even when all padding tokens are masked from attention computation, performance drops 7.9%--50% at 30K tokens. The only difference from short-context is positional displacement. FLenQA (`2024-08-flenqa-input-length-reasoning`) shows earlier evidence: duplicate-padding (no distractors) degrades accuracy from 0.92 to 0.68 at just 3,000 tokens.

- **High literal overlap between queries and relevant context is a pervasive confound.** NoLiMa (`2025-07-nolima-long-context-evaluation`) measured ROUGE-1 precision between questions and context across benchmarks, finding values from 0.553 (BABILong) to 0.966 (InfiniteBench QA). When overlap is removed, Llama 3.1 70B's effective length drops from 32K (RULER) to 2K (NoLiMa) -- a 16x reduction.

- **Benchmarks using naturally long documents cannot verify that their tasks require reading the full input.** Ada-LEval (`2024-06-ada-leval-length-adaptable-benchmark`) showed that GovReport summarization performance actually *improves* when truncated from full length to 8K tokens, while NarrativeQA drops only 8.4 points -- compared to 33 points for a task designed to require full-text comprehension.

- **Goldman et al. (`2024-11-genuinely-difficult-long-context`) provide the conceptual vocabulary** for distinguishing orthogonal dimensions of difficulty beyond length: dispersion (how hard it is to find information) and scope (how much information is needed). Most benchmarks measure one axis while claiming to measure "long-context ability" generally. The high-scope, high-dispersion quadrant is severely under-explored.

- **The evolution of benchmark design shows progressive recognition of these confounds**, from LRA's byte inflation (2021) through SCROLLS's insistence on natural length (2022), NIAH's systematic length sweeping (2023), and finally the controlled designs of FLenQA, RULER, and NoLiMa (2024--2025), which each isolate specific variables at the cost of ecological validity.

- **Perplexity is unreliable as a proxy for long-context capability.** Sun et al. (`2021-11-long-range-models-use-context`) showed perplexity plateaus at 2K tokens for models with 8K context. Levy et al. (`2024-08-flenqa-input-length-reasoning`) found a -0.95 Pearson correlation between next-word prediction accuracy and reasoning accuracy. Kuratov et al. (`2024-12-babilong-long-context-reasoning`) showed that YaRN-extended models maintain stable perplexity while failing on BABILong reasoning tasks.

- **A fundamental tension exists between controllability and ecological validity** that no benchmark has resolved. Synthetic benchmarks (RULER, BABILong) offer precise length control but have unvalidated proxy relationships with real tasks. Natural-document benchmarks (LongBench v2, LongBench Pro) test realistic scenarios but cannot attribute performance changes to context length specifically.

---

## Temporal Evolution

| Year-Month | Paper | Key Contribution | Shift in Understanding |
|---|---|---|---|
| 2021-05 | `2021-05-long-range-arena` | LRA: byte tokenization and pixel flattening to reach 1K--16K | Established first benchmark suite for efficient Transformers; exposed that byte inflation conflates character composition with long-range dependency |
| 2021-11 | `2021-11-long-range-models-use-context` | Prefix-length manipulation on PG-19 | Showed perplexity plateaus at 2K; long-range context primarily enables token copying, not discourse understanding |
| 2022-12 | `2022-12-scrolls-long-language-sequences` | SCROLLS: naturally long documents, no inflation | Rejected LRA's byte inflation; insisted on organic length; introduced information spread metric |
| 2023-11 | `2023-11-needle-in-a-haystack` | NIAH: systematic (depth × length) sweeping | Introduced the haystack padding paradigm; first systematic position × length evaluation |
| 2023-12 | `2023-12-zeroscrolls-zero-shot-long-text` | ZeroSCROLLS: zero-shot natural documents + aggregation tasks | Extended SCROLLS to zero-shot; introduced aggregation tasks requiring full-input synthesis |
| 2024-02 | `2024-02-lost-in-the-middle` | Position-controlled multi-document QA | Showed U-shaped performance curve; but confounded length with distractor count |
| 2024-06 | `2024-06-ada-leval-length-adaptable-benchmark` | Ada-LEval: first length-adaptable design (1K--128K) | Introduced principled length controllability; validated full-text requirement via truncation |
| 2024-08 | `2024-08-flenqa-input-length-reasoning` | FLenQA: duplicate-padding isolates length from noise | First benchmark to truly isolate input length from task difficulty; showed degradation at just 3K tokens |
| 2024-08 | `2024-08-longbench-bilingual-benchmark` | LongBench: multi-strategy length + LongBench-E bins | Introduced per-length-range analysis via binning; revealed Wikipedia memorization confound |
| 2024-08 | `2024-08-infinitebench-long-context-evaluation` | InfiniteBench: first 100K+ benchmark | Extended evaluation ceiling to 100K+; later revealed to have highest literal overlap (R-1=0.966) |
| 2024-08 | `2024-08-l-eval-standardized-evaluation` | L-Eval: evaluation methodology (LIE technique) | Shifted focus from length construction to evaluation protocol; showed metrics fail without length-matched generation |
| 2024-10 | `2024-10-ruler-context-size` | RULER: 4-category synthetic benchmark, fully controllable | Established that vanilla NIAH is insufficient; showed that near-perfect NIAH does not predict broader performance |
| 2024-11 | `2024-11-genuinely-difficult-long-context` | Dispersion × scope taxonomy | Provided conceptual vocabulary for distinguishing orthogonal dimensions of difficulty beyond length |
| 2024-12 | `2024-12-babilong-long-context-reasoning` | BABILong: reasoning-in-a-haystack, up to 50M tokens | Extended NIAH to multi-fact reasoning; showed perplexity unreliable and RAG fails on multi-fact tasks |
| 2025-03 | `2025-03-longiclbench-long-in-context-learning` | LongICLBench: length via demonstration count | Novel construction via ICL demonstrations; but confounds length with label-space complexity |
| 2025-04 | `2025-04-effective-context-length-falls-short` | Mechanistic explanation via position frequency | Provided causal mechanism (left-skewed position frequency) for why extended context fails |
| 2025-07 | `2025-07-longbench-v2` | LongBench v2: human-annotated, naturally long, multiple-choice | Raised the difficulty floor via human verification pipeline; but task distribution varies with length |
| 2025-07 | `2025-07-nolima-long-context-evaluation` | NoLiMa: quantified literal overlap confound | Demonstrated that removing lexical overlap reduces effective length by 16x; identified attention mechanism overload as the bottleneck |
| 2025-11 | `2025-11-context-length-hurts-performance` | Attention-masking experiment | Strongest causal evidence: positional displacement alone degrades reasoning, even when padding tokens are invisible |
| 2026-01 | `2026-01-longbench-pro` | LongBench Pro: 1500 samples, bilingual, 256K, difficulty-calibrated | Most comprehensive natural-document benchmark; but length is intrinsic to documents, not experimentally controlled |

### Phase 1: Establishing Long-Context Evaluation (2021--2022)

The field began with two opposing philosophies. LRA (`2021-05-long-range-arena`) used byte tokenization and pixel flattening to inflate sequence length, explicitly trading tokenization realism for controlled evaluation of efficient attention mechanisms. SCROLLS (`2022-12-scrolls-long-language-sequences`) rejected this approach, insisting on "organically long" documents. In parallel, Sun et al. (`2021-11-long-range-models-use-context`) established through prefix-length experiments that perplexity plateaus at 2K tokens, suggesting models used long-range context only for superficial token copying. This early work set the stage for the central tension: controllability (synthetic construction) vs. ecological validity (natural documents).

### Phase 2: The Haystack Paradigm and Position Analysis (2023--early 2024)

Kamradt's NIAH test (`2023-11-needle-in-a-haystack`) introduced the dominant paradigm for the next two years: insert a target into padding material and sweep over both position and length. This paradigm was immediately adopted for its simplicity and interpretability. Liu et al. (`2024-02-lost-in-the-middle`) extended position analysis using multi-document QA, discovering the U-shaped performance curve. ZeroSCROLLS (`2023-12-zeroscrolls-zero-shot-long-text`) added aggregation tasks that structurally require full-input processing. However, during this phase, the confounds introduced by each construction strategy were not yet recognized.

### Phase 3: Recognizing and Isolating Confounds (2024)

The critical year. Four papers independently exposed different confounds. FLenQA (`2024-08-flenqa-input-length-reasoning`) introduced duplicate padding to show that length alone degrades reasoning -- the first design to isolate length from noise. Ada-LEval (`2024-06-ada-leval-length-adaptable-benchmark`) validated full-text comprehension requirements via truncation experiments, revealing that traditional QA/summarization tasks do not actually require reading the full input. RULER (`2024-10-ruler-context-size`) demonstrated that vanilla NIAH scores are uninformative by showing near-perfect NIAH alongside massive degradation on harder tasks. Goldman et al. (`2024-11-genuinely-difficult-long-context`) provided the conceptual framework, arguing that "context length" conflates dispersion (how hard it is to find information) with scope (how much information is needed).

### Phase 4: Mechanistic Understanding and Confound Elimination (2025--2026)

NoLiMa (`2025-07-nolima-long-context-evaluation`) quantified the literal overlap confound, measuring ROUGE-1 precision across benchmarks and showing that effective length collapses 16x when surface cues are removed. Du et al. (`2025-11-context-length-hurts-performance`) provided the strongest causal evidence through attention masking: even invisible padding tokens degrade performance, isolating positional displacement as a causal factor. An et al. (`2025-04-effective-context-length-falls-short`) identified the mechanistic root cause -- left-skewed position frequency distributions in pretraining. Meanwhile, LongBench v2 (`2025-07-longbench-v2`) and LongBench Pro (`2026-01-longbench-pro`) pushed natural-document benchmarks toward greater difficulty and scale, but without resolving the fundamental controllability limitation.

---

## Thematic Synthesis

### A Taxonomy of Length Construction Strategies

**Statement:** Across the corpus, six distinct strategies for constructing the length dimension can be identified, each with characteristic strengths and confounds.

**Heterogeneity check:** Papers use different tokenizers and length measurement conventions. LRA (`2021-05-long-range-arena`) measures in bytes/characters. SCROLLS (`2022-12-scrolls-long-language-sequences`) measures in words. Most recent benchmarks use model-specific tokenizers (GPT-4, Qwen). LongBench Pro (`2026-01-longbench-pro`) notes a ±20% tolerance. These measurement differences complicate direct comparison of length thresholds across papers but do not affect the qualitative classification of construction strategies.

| Strategy | Examples | Mechanism | Length Range | Controllable? |
|---|---|---|---|---|
| **Byte/character inflation** | `2021-05-long-range-arena` | Byte-level tokenization of text; pixel flattening of images | 1K--16K | Fixed per task |
| **Naturally long documents** | `2022-12-scrolls-long-language-sequences`, `2023-12-zeroscrolls-zero-shot-long-text`, `2024-08-l-eval-standardized-evaluation`, `2024-08-infinitebench-long-context-evaluation`, `2025-07-longbench-v2`, `2026-01-longbench-pro` | Curate documents at their native length | 1.7K--2M words | No |
| **Haystack padding** | `2023-11-needle-in-a-haystack`, `2024-10-ruler-context-size`, `2024-12-babilong-long-context-reasoning`, `2025-07-nolima-long-context-evaluation` | Insert target facts into irrelevant filler text | 1K--50M tokens | Yes (continuous) |
| **Distractor injection** | `2024-02-lost-in-the-middle`, `2024-08-longbench-bilingual-benchmark` (multi-doc QA) | Add more retrieved or random distractor documents/answers | ~2K--16K | Yes (discrete, via count) |
| **Demonstration concatenation** | `2025-03-longiclbench-long-in-context-learning`, `2024-08-longbench-bilingual-benchmark` (few-shot) | Increase the number of in-context learning examples | 1K--50K | Yes (via rounds × classes) |
| **Controlled padding with fixed task** | `2024-08-flenqa-input-length-reasoning`, `2025-11-context-length-hurts-performance` | Pad around a fixed-difficulty task with duplicate, topical, or null tokens | 250--30K | Yes (continuous) |

#### Cross-paper analysis

The most significant division is between **controllable** and **uncontrollable** strategies. Seven of 15 benchmark papers use naturally long documents, inheriting whatever length the source material provides. This prevents attributing performance changes to context length specifically: a model might score lower on a 100K-token novel than on a 10K-token paper because the novel requires different reasoning, not because it is longer.

Among controllable strategies, the critical variable is **what covaries with length**. In haystack padding (`2023-11-needle-in-a-haystack`, `2024-10-ruler-context-size`, `2024-12-babilong-long-context-reasoning`), signal-to-noise ratio decreases as length increases -- the number of relevant tokens stays constant while irrelevant tokens grow. In distractor injection (`2024-02-lost-in-the-middle`, `2024-08-longbench-bilingual-benchmark`), the number of plausible-but-incorrect items increases with length, raising retrieval difficulty. In demonstration concatenation (`2025-03-longiclbench-long-in-context-learning`), label-space size and context length increase simultaneously. Only FLenQA's duplicate-padding design (`2024-08-flenqa-input-length-reasoning`) and Du et al.'s whitespace/masking conditions (`2025-11-context-length-hurts-performance`) isolate length from these covariates.

The evolution from LRA's byte inflation (2021) to FLenQA's controlled padding (2024) and Du et al.'s attention masking (2025) represents a five-year trajectory toward recognizing that "making the input longer" is not a single operation but a family of operations with different causal implications.

### Confounds Introduced by Each Construction Strategy

**Statement:** Every length construction strategy introduces at least one confound that covaries with the length dimension, making it impossible to attribute observed performance changes solely to context length.

**Heterogeneity check:** Papers vary in how they measure and report degradation. FLenQA reports accuracy on True/False tasks. Du et al. report percentage drops from baseline on GSM8K, MMLU, and HumanEval. RULER uses a recall-based composite score. These metric differences mean effect magnitudes are not directly comparable across papers, but the qualitative finding (degradation occurs) is consistent.

| Strategy | Primary Confound | Evidence |
|---|---|---|
| Byte inflation | Conflates character composition with long-range dependency | `2021-05-long-range-arena` acknowledges this; `2022-12-scrolls-long-language-sequences` criticizes it explicitly |
| Natural documents | Task difficulty, domain, and length are entangled | `2024-06-ada-leval-length-adaptable-benchmark` shows GovReport improves when truncated; `2025-07-longbench-v2` acknowledges that task distributions differ across length bins |
| Haystack padding | Signal-to-noise ratio decreases with length | `2024-08-flenqa-input-length-reasoning` (C2) shows degradation even with duplicate padding (no noise), isolating length; the difference between duplicate and different-padding conditions quantifies the noise confound |
| Distractor injection | Retrieval difficulty increases with length | `2024-02-lost-in-the-middle` uses Contriever distractors in relevance order, confounding position and relevance; `2024-08-longbench-bilingual-benchmark` adds distractors up to a maximum, conflating length with distractor count |
| Demonstration concatenation | Label-space complexity increases with length | `2025-03-longiclbench-long-in-context-learning` analysis notes this explicitly: "impossible to isolate which factor drives performance degradation" |
| Controlled padding | Limited ecological validity; very short length range | `2024-08-flenqa-input-length-reasoning` tests only to 3K tokens; `2025-11-context-length-hurts-performance` tests to 30K but only on simple single-evidence tasks |

#### Cross-paper analysis

The confound picture sharpens when comparing results across strategies. FLenQA's duplicate-padding experiment (`2024-08-flenqa-input-length-reasoning`, C2) shows that average accuracy drops from 0.92 to 0.68 at 3,000 tokens when the padding consists of duplicates of the key paragraphs -- zero irrelevant content, zero change in task difficulty. Du et al. (`2025-11-context-length-hurts-performance`, C3) extend this further: even when all padding tokens are masked from attention, performance drops 7.9%--50% at 30K tokens, isolating positional displacement as the causal factor. These two papers together provide the strongest evidence that "context length alone" is a genuine independent variable, not merely a proxy for noise, distraction, or retrieval difficulty.

However, this clean isolation comes at the cost of ecological validity. FLenQA tasks are simple True/False reasoning chains; Du et al. use short-answer math and code problems. Whether length-alone degradation occurs for complex multi-document reasoning, long-form summarization, or code repository understanding remains untested. The controlled-padding strategy has proven that length effects are real but has not yet demonstrated their magnitude in the settings that natural-document benchmarks target.

The natural-document benchmarks, conversely, test ecologically valid tasks but cannot determine what fraction of the observed degradation comes from length per se. The gap between these two approaches constitutes the most significant unresolved methodological problem in the field.

### Literal Overlap as a Pervasive Shortcut

**Statement:** High lexical overlap between benchmark queries and relevant context enables models to exploit surface-level pattern matching, inflating scores and masking genuine reasoning failures.

**Heterogeneity check:** NoLiMa (`2025-07-nolima-long-context-evaluation`) provides the only systematic cross-benchmark measurement of literal overlap (Table 1). All values below are from this single source, using ROUGE-1 precision between question tokens and context. The metric is well-defined, making these values directly comparable.

| Benchmark | ROUGE-1 Precision (Q→Context) | Source |
|---|---|---|
| InfiniteBench QA | 0.966 | `2025-07-nolima-long-context-evaluation`, Table 1 |
| InfiniteBench MC | 0.946 | `2025-07-nolima-long-context-evaluation`, Table 1 |
| Vanilla NIAH | 0.905 | `2025-07-nolima-long-context-evaluation`, Table 1 |
| RULER QA | 0.809 | `2025-07-nolima-long-context-evaluation`, Table 1 |
| HELMET RAG | 0.689 | `2025-07-nolima-long-context-evaluation`, Table 1 |
| RULER S-NIAH | 0.571 | `2025-07-nolima-long-context-evaluation`, Table 1 |
| BABILong 0K | 0.553 | `2025-07-nolima-long-context-evaluation`, Table 1 |
| **NoLiMa** | **0.069** | `2025-07-nolima-long-context-evaluation`, Table 1 |

#### Cross-paper analysis

The literal overlap confound was not recognized until NoLiMa (`2025-07-nolima-long-context-evaluation`) systematically measured it in 2025. Prior benchmark authors were aware that their tasks might be "too easy" (RULER acknowledges NIAH is insufficient; BABILong extends NIAH with reasoning), but the specific mechanism -- lexical token matching via induction heads rather than genuine comprehension -- was not identified.

The impact is dramatic. Llama 3.1 70B achieves 32K effective length on RULER, 16K on BABILong (QA1), but only **2K on NoLiMa** (`2025-07-nolima-long-context-evaluation`, Section 4.4). This 16x reduction occurs despite the underlying task being simpler on NoLiMa (single-fact retrieval vs. RULER's multi-task suite). The explanation is mechanistic: Olsson et al. (2022) showed that attention excels at recalling repetitive patterns through induction heads. When question tokens literally appear in the context, the attention mechanism can locate the relevant passage via pattern matching. When this cue is absent (NoLiMa), the model must perform latent associative reasoning, which degrades rapidly with context length.

NoLiMa's ablation experiments (`2025-07-nolima-long-context-evaluation`, Table 6) provide direct causal evidence: adding multiple-choice options containing literal matches raises two-hop accuracy from 25.9% to 87.2% at 32K tokens -- a 3.4x improvement from surface cues alone, with no change in the underlying reasoning requirement. Conversely, adding literal-match distractors (sentences containing the query keyword but irrelevant to the answer) reduces GPT-4o's effective length from 8K to 1K.

This finding retroactively calls into question results across the corpus. NIAH's original finding (`2023-11-needle-in-a-haystack`) that Claude 2.1 achieves only 27% retrieval may partly reflect a refusal behavior rather than retrieval failure (accuracy jumps to 98% with a single prompt directive), but the needle itself ("The best thing to do in San Francisco is eat a sandwich...") shares most tokens with the query ("What is the best thing to do in San Francisco?"). RULER's extension of NIAH (`2024-10-ruler-context-size`) adds harder tasks, but its retrieval subtasks still use direct lexical matching ("the special magic number for XXX is: YYY"). InfiniteBench QA (`2024-08-infinitebench-long-context-evaluation`) has the highest measured overlap (R-1=0.966), suggesting that models can locate answers through simple token scanning.

The benchmarks that fare best under this analysis are those that structurally prevent lexical shortcuts: FLenQA (`2024-08-flenqa-input-length-reasoning`) requires reasoning over relationships between entities, not retrieval of specific facts. LongICLBench (`2025-03-longiclbench-long-in-context-learning`) requires label matching against a set of demonstrations. RULER's aggregation tasks (CWE, FWE) require counting occurrences across the full context. But even these benchmarks have not been systematically evaluated for the degree to which surface-level patterns enable shortcuts.

### Disentangling Length from Task Difficulty

**Statement:** Most benchmarks fail to disentangle context length from task difficulty, making it impossible to determine whether observed degradation stems from length per se or from harder tasks at longer lengths.

**Heterogeneity check:** Papers use fundamentally different experimental designs. Some (FLenQA, Du et al.) hold the task constant and vary only length. Others (LongBench-E, LongBench v2) bin samples by length but use different samples in each bin. Still others (Ada-LEval's BestAnswer) add distractors to increase length. These designs answer different questions and cannot be pooled. The table below organizes findings by design type.

| Paper | Disentanglement Approach | Limitation |
|---|---|---|
| `2024-08-flenqa-input-length-reasoning` | Identical task at all lengths; duplicate padding eliminates noise | Maximum 3K tokens; simple True/False only |
| `2025-11-context-length-hurts-performance` | Identical task at all lengths; whitespace/attention-masking conditions | Maximum 30K; single-evidence tasks only |
| `2024-06-ada-leval-length-adaptable-benchmark` | Same questions reused across lengths (BestAnswer); validate via truncation | BestAnswer adds distractors to increase length, changing retrieval difficulty |
| `2024-08-longbench-bilingual-benchmark` | LongBench-E bins samples by word count (0--4K, 4K--8K, 8K+) | Different samples in each bin; difficulty may correlate with length |
| `2024-10-ruler-context-size` | Same task configurations scaled to different lengths | Signal-to-noise ratio decreases with length for aggregation tasks; distractor count increases for QA |
| `2024-12-babilong-long-context-reasoning` | Same bAbI reasoning tasks embedded in growing haystacks | Signal-to-noise ratio changes; fact-to-filler ratio changes |
| `2025-07-longbench-v2` | Length bins (Short/Medium/Long) with natural documents | Task distributions differ by bin (code in Long, dialogue in Short) |
| `2026-01-longbench-pro` | 6 length buckets × 25 task types × 2 languages | Documents at different lengths; no per-task length manipulation |

#### Cross-paper analysis

Only 2 of 15 benchmark papers achieve clean disentanglement of length and difficulty (`2024-08-flenqa-input-length-reasoning`, `2025-11-context-length-hurts-performance`), and both pay a steep price in ecological validity. The remaining benchmarks exhibit various degrees of confounding.

The starkest illustration comes from Ada-LEval's truncation experiment (`2024-06-ada-leval-length-adaptable-benchmark`, Table 10). When GPT-4-Turbo-1106 is tested on three benchmarks with progressive truncation:

| Benchmark | 2K | 4K | 8K | Full | Drop (Full→2K) |
|---|---|---|---|---|---|
| BestAnswer | 11.0 | 20.0 | 31.5 | 44.0 | 33 points |
| NarrativeQA | 24.7 | 25.6 | 29.7 | 33.1 | 8.4 points |
| GovReport | 30.7 | 32.4 | 33.6 | 30.9 | **−2.7 (improves)** |

GovReport -- a summarization benchmark from SCROLLS -- actually performs *better* when truncated to 8K tokens than when given the full document (~30K tokens). NarrativeQA loses only 8.4 points, suggesting that ~75% of its performance is achievable from a small fraction of the input. Only BestAnswer, which was specifically designed to require full-text reading, shows the expected pattern.

This finding implies that most natural-document benchmarks from the early period (`2022-12-scrolls-long-language-sequences`, `2023-12-zeroscrolls-zero-shot-long-text`, `2024-08-l-eval-standardized-evaluation`) may not actually be measuring long-context capability in any meaningful sense -- the tasks can often be solved from truncated input, and longer contexts may introduce noise that degrades metric scores.

Goldman et al. (`2024-11-genuinely-difficult-long-context`) provide the conceptual framework for understanding this. Their dispersion × scope taxonomy identifies two independent axes of difficulty that are conflated when benchmarks use only "context length" as their primary variable. A task can be long because the document is long (high scope, low dispersion -- summarize an entire book) or because a single fact is buried in noise (low scope, high dispersion -- needle in a haystack). Most benchmarks measure one axis while claiming to measure "long-context ability" generally. The hardest quadrant (high scope + high dispersion) is "severely under-explored" across the entire corpus.

### What Benchmarks Actually Measure vs. What They Claim

**Statement:** Each benchmark's length construction method implicitly defines what aspect of long-context capability it measures, and these aspects differ fundamentally from the generic "long-context understanding" most benchmarks claim to evaluate.

**Heterogeneity check:** The table below synthesizes claims from each paper's abstract/introduction against what the experimental design actually measures. This analysis reflects interpretation of methodology, not pooled quantitative results.

| Paper | Claims to Measure | Actually Measures |
|---|---|---|
| `2021-05-long-range-arena` | Long-range dependency modeling | Character composition + spatial reasoning on 1D sequences |
| `2022-12-scrolls-long-language-sequences` | Long-text understanding via information synthesis | Fine-tuned seq2seq generation with n-gram overlap metrics; BART (1K tokens) nearly matches LED (16K) |
| `2023-11-needle-in-a-haystack` | Full context window retrieval capability | Lexical token matching of a high-overlap fact (ROUGE-1=0.905) |
| `2023-12-zeroscrolls-zero-shot-long-text` | Zero-shot long-text understanding | Task performance × format compliance interaction; all models capped at 8K tokens despite source documents up to 49K words |
| `2024-02-lost-in-the-middle` | How models use long contexts | Position-dependent retrieval from distractor sets of varying size |
| `2024-06-ada-leval-length-adaptable-benchmark` | Full-text comprehension at adaptive lengths | At ultra-long settings: instruction following (TSort) or answer selection from growing distractor pools (BestAnswer) |
| `2024-08-flenqa-input-length-reasoning` | Input length effect on reasoning | Pure length-induced reasoning degradation (cleanest measure in corpus) |
| `2024-08-infinitebench-long-context-evaluation` | 100K+ context understanding | Lexical retrieval (ROUGE-1=0.966 for QA) + entity-replaced novel comprehension |
| `2024-08-l-eval-standardized-evaluation` | Standardized long-context evaluation | Evaluation methodology (metric-human correlation) rather than length effects per se |
| `2024-08-longbench-bilingual-benchmark` | Bilingual long-context understanding | Broad task coverage with partially memorizable content (Wikipedia-based multi-doc QA) |
| `2024-10-ruler-context-size` | Real context size beyond NIAH | Synthetic behavioral checks with lexical overlap cues; proxy relationship to real tasks unvalidated |
| `2024-11-genuinely-difficult-long-context` | Genuine long-context difficulty | Conceptual taxonomy (no empirical benchmark) |
| `2024-12-babilong-long-context-reasoning` | Reasoning in long contexts | Signal-in-noise filtering + simple bAbI reasoning; some tasks confound inherent difficulty with length |
| `2025-03-longiclbench-long-in-context-learning` | Full-input comprehension via extreme-label ICL | Label-space complexity × context length × label granularity (entangled) |
| `2025-07-longbench-v2` | Deep understanding and reasoning on realistic tasks | Human-calibrated difficulty on natural documents; but task distributions vary with length bins |
| `2025-07-nolima-long-context-evaluation` | Long-context evaluation without literal matching | Latent associative reasoning degradation with context length (narrowly scoped: 58 question-needle pairs) |
| `2025-11-context-length-hurts-performance` | Context length effects independent of retrieval | Positional displacement effects on single-evidence reasoning (cleanest causal design for this factor) |
| `2026-01-longbench-pro` | Comprehensive long-context capability | Natural-document task performance at various lengths, with difficulty calibration; but length is not experimentally manipulated |

#### Cross-paper analysis

The gap between claimed and actual measurement is largest for early benchmarks and narrows over time as the field develops awareness of confounds. LRA (`2021-05-long-range-arena`) explicitly acknowledges that byte tokenization "conflates the compositional challenge of learning to compose bytes into words with the long-range dependency challenge." SCROLLS (`2022-12-scrolls-long-language-sequences`) avoids this confound but introduces another: the near-equivalence of BART-1024 and LED-16384 (29.01 vs. 29.16) suggests that long-context capability is not being discriminated.

By 2024--2025, benchmarks become more honest about their scope. RULER (`2024-10-ruler-context-size`) authors explicitly state it should be used as "convenient behavioral checks" rather than preferred over realistic settings. NoLiMa (`2025-07-nolima-long-context-evaluation`) is precisely scoped to one specific confound (literal overlap) and does not claim to measure long-context understanding generally. FLenQA (`2024-08-flenqa-input-length-reasoning`) acknowledges its 3K-token ceiling.

**Synthesis inference:** The trajectory suggests a Kuhnian progression from "long-context benchmarks measure long-context ability" (2021--2023) to "each benchmark measures a specific interaction between its construction method and model capabilities" (2024--2026). The implication is that no single benchmark score can serve as a proxy for "long-context capability" -- the concept itself decomposes into retrieval robustness, noise tolerance, reasoning stability under positional displacement, literal-match independence, and information aggregation capacity, each requiring distinct evaluation. The papers contributing to this inference are: `2024-08-flenqa-input-length-reasoning`, `2024-11-genuinely-difficult-long-context`, `2025-07-nolima-long-context-evaluation`, `2025-11-context-length-hurts-performance`.

---

## Consensus and Disagreements

### Consensus

**Claim:** Every length construction strategy introduces confounds that covary with the length dimension.
**Supporting papers:** `2024-08-flenqa-input-length-reasoning`, `2025-11-context-length-hurts-performance`, `2024-11-genuinely-difficult-long-context`, `2024-10-ruler-context-size`
**Evidence strength:** strong
**Qualification:** FLenQA and Du et al. demonstrate that length has an independent effect beyond these confounds, but no benchmark simultaneously controls for all of them in a realistic setting.

**Claim:** High literal overlap enables surface-level shortcuts that inflate long-context benchmark scores.
**Supporting papers:** `2025-07-nolima-long-context-evaluation`, `2024-10-ruler-context-size`, `2024-08-infinitebench-long-context-evaluation`
**Evidence strength:** strong
**Qualification:** NoLiMa provides the quantitative measurements and ablation experiments. The claim applies specifically to retrieval-style tasks; aggregation and generation tasks are less affected.

**Claim:** Benchmarks using naturally long documents cannot verify that their tasks require full-context comprehension without explicit truncation controls.
**Supporting papers:** `2024-06-ada-leval-length-adaptable-benchmark`, `2022-12-scrolls-long-language-sequences`, `2024-08-l-eval-standardized-evaluation`
**Evidence strength:** strong
**Qualification:** Ada-LEval's truncation comparison is the definitive evidence (Table 10). Only 1 of 3 tested benchmarks showed the expected pattern of full-text necessity.

**Claim:** Perplexity is unreliable as a proxy for long-context capability.
**Supporting papers:** `2024-08-flenqa-input-length-reasoning`, `2024-12-babilong-long-context-reasoning`, `2021-11-long-range-models-use-context`
**Evidence strength:** strong
**Qualification:** Three independent lines of evidence: perplexity plateaus at 2K while models process 8K (Sun et al.); perplexity correlates negatively with reasoning accuracy (Levy et al., rho = -0.95); stable perplexity coexists with reasoning failure (Kuratov et al.).

**Claim:** Synthetic benchmarks with controllable length offer superior experimental control but have unvalidated proxy relationships with realistic tasks.
**Supporting papers:** `2024-10-ruler-context-size`, `2024-12-babilong-long-context-reasoning`, `2024-06-ada-leval-length-adaptable-benchmark`, `2025-07-longbench-v2`
**Evidence strength:** moderate
**Qualification:** RULER explicitly acknowledges this limitation (Section 8). LongBench v2 and LongBench Pro motivate their existence partly by this gap. No paper has validated the proxy relationships.

### Active Disagreements

**Claim:** Whether padding-based length construction measures context-length ability or noise tolerance.
**Position A** (`2024-10-ruler-context-size`, `2024-12-babilong-long-context-reasoning`): Haystack padding tests whether models can identify relevant information in growing contexts, which is a core component of long-context capability.
**Position B** (`2025-07-nolima-long-context-evaluation`, `2024-08-flenqa-input-length-reasoning`, `2024-11-genuinely-difficult-long-context`): Haystack padding primarily tests signal-to-noise filtering, which can be achieved via lexical matching. True long-context capability requires latent reasoning without surface cues.
**Methodological differences:** Position A papers use synthetic benchmarks with lexical overlap (RULER R-1=0.571--0.809). Position B papers use controlled designs (FLenQA duplicate padding, NoLiMa R-1=0.069) that isolate length from lexical cues.
**Assessment:** Both are partially correct. FLenQA's duplicate-padding experiment and Du et al.'s attention-masking experiment prove that length alone degrades performance. However, most padding benchmarks (RULER, BABILong) do not use these controls, leaving their results as a composite of length and noise effects.
**Resolution path:** A study comparing the same task under duplicate-padding, noise-padding, and attention-masking conditions across multiple models would resolve this.
**Status:** Partially resolved. FLenQA and Du et al. show length effects exist; the remaining question is their magnitude relative to noise effects in existing benchmarks.

**Claim:** Whether natural-document or synthetic benchmarks provide more valid evaluation.
**Position A** (`2025-07-longbench-v2`, `2026-01-longbench-pro`, `2022-12-scrolls-long-language-sequences`): Natural documents reflect real usage and test holistic capability; synthetic tasks are too simple and artificial.
**Position B** (`2024-10-ruler-context-size`, `2024-06-ada-leval-length-adaptable-benchmark`): Natural documents introduce uncontrollable confounds; only synthetic constructions allow attributing effects to specific variables.
**Methodological differences:** Position A papers use curated documents without length manipulation. Position B papers generate synthetic inputs with controllable parameters. Neither approach can do what the other does -- natural documents cannot be length-controlled, and synthetic inputs may not generalize to realistic tasks.
**Assessment:** Unresolved. Both positions are well-supported within their scope. Ada-LEval's truncation experiments (showing GovReport improves when truncated) validate Position B's concern. LongBench Pro's comprehensive task coverage and difficulty calibration validate Position A's goals. The fundamental limitation is that no benchmark yet combines natural text with experimental control over length.
**Resolution path:** A benchmark embedding identical reasoning tasks within real documents at controlled lengths, using the document itself as padding material.
**Status:** Unresolved.

---

## Methodological Patterns

### Common Experimental Setups

**Length ranges by benchmark type:**
- Synthetic benchmarks: typically 4K--128K, sometimes extending to 1M+ (`2024-12-babilong-long-context-reasoning` reaches 50M)
- Natural-document benchmarks: determined by source material, typically 3K--256K+
- Controlled-padding benchmarks: much shorter (250--30K) due to experimental constraints

**Models most frequently evaluated:** GPT-4/4o (14 of 20 papers), Llama series (12 papers), Gemini 1.5/2.0 (10 papers), Mistral/Mixtral (7 papers), Claude (6 papers), Qwen series (6 papers).

### Benchmark Coverage Matrix

| Paper | NIAH-style | Multi-hop | Aggregation | Summarization | QA | Code | ICL | Classification |
|---|---|---|---|---|---|---|---|---|
| `2021-05-long-range-arena` | | | | | | | | x |
| `2022-12-scrolls-long-language-sequences` | | | | x | x | | | x |
| `2023-11-needle-in-a-haystack` | x | | | | | | | |
| `2023-12-zeroscrolls-zero-shot-long-text` | | | x | x | x | | | |
| `2024-02-lost-in-the-middle` | | | | | x | | | |
| `2024-06-ada-leval-length-adaptable-benchmark` | | | | | | | | x |
| `2024-08-flenqa-input-length-reasoning` | | | | | | | | x |
| `2024-08-infinitebench-long-context-evaluation` | x | | | x | x | x | | |
| `2024-08-l-eval-standardized-evaluation` | | | | x | x | x | | x |
| `2024-08-longbench-bilingual-benchmark` | x | x | | x | x | x | x | |
| `2024-10-ruler-context-size` | x | x | x | | x | | | |
| `2024-12-babilong-long-context-reasoning` | x | x | | | | | | |
| `2025-03-longiclbench-long-in-context-learning` | | | | | | | x | x |
| `2025-07-longbench-v2` | | | | | x | x | x | |
| `2025-07-nolima-long-context-evaluation` | x | x | | | | | | |
| `2026-01-longbench-pro` | | | x | x | x | x | x | |

### Methodological Strengths

The strongest methodological contributions in the corpus:

1. **Du et al.'s attention-masking experiment** (`2025-11-context-length-hurts-performance`): The strongest causal test in the corpus -- invisible tokens still degrade performance (7.9%--50% at 30K), isolating positional displacement as the mechanism. Three conditions (essay tokens, whitespace, attention masking) systematically eliminate alternative explanations.

2. **FLenQA's duplicate-padding design** (`2024-08-flenqa-input-length-reasoning`): The first benchmark to fully disentangle length from noise, distraction, and task difficulty. Degradation from 0.92 to 0.68 accuracy with zero irrelevant content.

3. **NoLiMa's ROUGE-1 quantification** (`2025-07-nolima-long-context-evaluation`): Transformed an intuitive concern (benchmarks may be too easy) into a measurable quantity across benchmarks. The 16x reduction in effective length when overlap is removed provides a concrete measure of the confound's magnitude.

4. **Ada-LEval's truncation validation** (`2024-06-ada-leval-length-adaptable-benchmark`): Simple but decisive method for verifying whether tasks require full-text reading. The finding that GovReport improves when truncated challenges assumptions underlying all naturally-long-document benchmarks.

5. **Goldman et al.'s dispersion × scope taxonomy** (`2024-11-genuinely-difficult-long-context`): Provided conceptual vocabulary for distinguishing dimensions of difficulty that length alone conflates. Enables systematic classification of what benchmarks actually measure.

### Methodological Weaknesses

Recurring limitations across the corpus:

1. **No variance estimates.** 10 of 15 benchmark papers report single-run results without confidence intervals or significance testing. Results are point estimates at best, and the small evaluation subset sizes in some benchmarks (Ada-LEval uses only 50 samples for ultra-long evaluation) mean individual examples shift accuracy meaningfully.

2. **Instruction-following confound.** Multiple benchmarks conflate task capability with instruction compliance. Ada-LEval (`2024-06-ada-leval-length-adaptable-benchmark`) cannot distinguish among open-source models because they all fail at instruction following. L-Eval (`2024-08-l-eval-standardized-evaluation`) shows that metric-human correlation collapses without generation length control. ZeroSCROLLS (`2023-12-zeroscrolls-zero-shot-long-text`) shows GPT-4 appears weaker than Claude on NarrativeQA by F1 but stronger by human judgment due to format non-compliance.

3. **Narrow model coverage.** Many benchmark papers evaluate primarily 7B-parameter models plus one or two proprietary APIs, leaving the intermediate scale (13B--70B) underrepresented. LongBench Pro (`2026-01-longbench-pro`) is the exception, covering 46 models.

4. **English dominance.** Of the 15 benchmark papers, only 4 include non-English evaluation (`2024-08-longbench-bilingual-benchmark`, `2024-08-infinitebench-long-context-evaluation`, `2026-01-longbench-pro`, `2025-03-longiclbench-long-in-context-learning` for some tasks). The literal overlap confound, position bias patterns, and length-difficulty interactions may differ across languages.

5. **Generation tasks underrepresented.** 12 of 15 benchmarks are dominated by extractive or classificatory tasks. Long-form generation, open-ended writing, and creative composition -- where the model must maintain coherence over many output tokens -- are evaluated only in summarization subtasks and are scored via n-gram metrics that the corpus itself shows to be unreliable.

---

## Gaps and Open Questions

1. **No benchmark combines experimental control with ecological validity.**
   - **Description:** Controlled-padding designs (FLenQA, Du et al.) isolate length effects but test only simple tasks at short lengths (3K--30K tokens). Natural-document benchmarks test realistic tasks but cannot attribute effects to length. No benchmark uses realistic text with experimental manipulation of length.
   - **Severity:** high
   - **Potential approach:** A benchmark could embed identical reasoning tasks within real documents at controlled lengths, using the document itself as the padding material. Ada-LEval's approach of reusing questions across length settings is a step in this direction but introduces distractor-count confounds.
   - **Related open questions:** `2024-10-ruler-context-size` open question on proxy task validity; `2024-08-flenqa-input-length-reasoning` open question on scaling beyond 3K.

2. **Synthetic-to-realistic proxy relationships are unvalidated.**
   - **Description:** RULER claims variable tracking proxies coreference resolution and CWE/FWE proxy summarization. BABILong claims bAbI tasks measure "reasoning in long contexts." These relationships are assumed, not tested.
   - **Severity:** high
   - **Potential approach:** Correlate synthetic benchmark scores with performance on matched realistic tasks (e.g., RULER VT vs. CoNLL coreference) across many models.
   - **Related open questions:** `2024-10-ruler-context-size` open question 1; `2024-12-babilong-long-context-reasoning` open question 4.

3. **No study compares the same task under different length construction strategies.**
   - **Description:** If the same underlying task were evaluated with haystack padding, distractor injection, and controlled padding, would models show the same degradation curves? This comparison would reveal whether "context length" is a single dimension or a family of dimensions.
   - **Severity:** high
   - **Potential approach:** Take a single task (e.g., multi-hop QA) and construct length via (a) irrelevant padding, (b) additional distractor documents, (c) duplicate-question padding, and (d) whitespace insertion.
   - **Related open questions:** `2025-11-context-length-hurts-performance` open question 1; `2024-11-genuinely-difficult-long-context` open question 1.

4. **Generation tasks are poorly represented.**
   - **Description:** Long-form generation (summarization, writing, planning) is evaluated in only 6 of 15 benchmark papers, always via ROUGE or model-based metrics that the corpus shows are unreliable (`2024-08-l-eval-standardized-evaluation`, `2025-07-longbench-v2`). LongBench Pro (`2026-01-longbench-pro`) uses SemSim + ROUGE-L for summarization but acknowledges limitations.
   - **Severity:** medium
   - **Potential approach:** Design generation tasks with objective correctness criteria (e.g., generate a story that must reference N specific events from the input in the correct order).
   - **Related open questions:** `2022-12-scrolls-long-language-sequences` open question on model-based evaluation.

5. **Interaction between length construction and position bias is unexplored.**
   - **Description:** The lost-in-the-middle effect (`2024-02-lost-in-the-middle`) has been studied under distractor-injection and haystack-padding settings. Whether the same U-shaped curve appears under controlled-padding (FLenQA) or natural-document (LongBench v2) settings is unknown. NoLiMa (`2025-07-nolima-long-context-evaluation`) shows that two-hop tasks produce a flat depth profile where context length dominates, suggesting the interaction depends on task type.
   - **Severity:** medium
   - **Potential approach:** Apply NoLiMa's aligned-depth analysis to other benchmarks with controllable needle positions.
   - **Related open questions:** `2024-10-ruler-context-size` open question 3; `2025-07-nolima-long-context-evaluation` open question 2.

6. **Multilingual evaluation of length effects is absent.**
   - **Description:** Of controlled-length benchmarks (where length effects can be measured), none include non-English evaluation. LongBench (`2024-08-longbench-bilingual-benchmark`) and LongBench Pro (`2026-01-longbench-pro`) are bilingual but do not experimentally control length. Whether the literal-overlap confound, position bias, and length-alone degradation operate identically across languages is unknown.
   - **Severity:** medium
   - **Potential approach:** Replicate NoLiMa's design with non-English needles and haystacks; replicate FLenQA's design with non-English reasoning tasks.
