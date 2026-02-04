---
title: "Is It Really Long Context if All You Need Is Retrieval? Towards Genuinely Difficult Long Context NLP"
authors: "Goldman, Jacovi, Slobodkin, Maimon, Dagan, Tsarfaty"
year: 2024
venue: "EMNLP 2024"
paper_type: conference-paper
categories: ["long-context-evaluation", "benchmarking"]
scope: ["long-context taxonomy", "benchmark difficulty characterization", "dispersion and scope axes"]
benchmarks_used: []
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "Conflating qualitatively different long-context tasks by input length alone is unproductive; the field requires a more precise vocabulary to describe what makes long-context tasks difficult"
    evidence: "Section 1, Section 2, Section 3"
    status: supported
  - id: C2
    claim: "Long-context task difficulty is captured by two orthogonal axes: Dispersion (how hard it is to find and extract required information) and Scope (how much information is needed to solve the task)"
    evidence: "Section 3, Figure 1"
    status: unvalidated
  - id: C3
    claim: "The majority of existing long-context benchmarks target either scope or dispersion, but not both simultaneously"
    evidence: "Section 4, Figure 2, Table 1 (Appendix A)"
    status: supported
  - id: C4
    claim: "The most challenging and interesting long-context setting -- high scope and high dispersion -- is severely under-explored in current benchmarks"
    evidence: "Section 4, Figure 2"
    status: supported
  - id: C5
    claim: "Tasks with low scope and low dispersion (e.g., NIAH, simple factual QA) are the least indicative of genuine long-context capabilities because they can be solved by implicit retrieval"
    evidence: "Section 3, Section 4, Figure 1"
    status: supported
cross_references:
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Goldman et al. classify Liu et al.'s multi-document QA as low-scope low-dispersion and key-value retrieval as low-scope low-dispersion in their taxonomy; both papers argue that simple retrieval tasks are insufficient for evaluating long-context capabilities"
  - target: 2024-10-ruler-context-size
    type: complementary
    detail: "RULER tasks are classified across multiple quadrants of the taxonomy: single-hop QA and S-NIAH as low-scope low-dispersion, MV-NIAH and MQ-NIAH as high-dispersion low-scope, and aggregation tasks as high-dispersion"
  - target: 2024-08-flenqa-input-length-reasoning
    type: complementary
    detail: "Levy et al.'s FLenQA tasks appear across both dispersion levels in the taxonomy; cited as evidence that adding distractors between needles increases dispersion independently of needle count or input length"
  - target: 2023-11-needle-in-a-haystack
    type: complementary
    detail: "NIAH is the primary example of low-scope low-dispersion tasks that can be solved by implicit retrieval and thus are least indicative of genuine long-context capabilities"
  - target: 2022-12-scrolls-long-language-sequences
    type: complementary
    detail: "SCROLLS is cited as an example of benchmarks that group tasks primarily by input length"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: complementary
    detail: "ZeroSCROLLS tasks (SpaceDigest, BookSumSort) are classified as high-scope low-dispersion (aggregation tasks) in the taxonomy"
  - target: 2021-05-long-range-arena
    type: complementary
    detail: "LRA tasks are classified across the taxonomy: classification tasks as high-dispersion low-scope, Long ListOps as high-scope high-dispersion (reasoning)"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong tasks span all four quadrants of the taxonomy, from low-dispersion retrieval tasks (1, 4-6, 9-10) to high-dispersion reasoning (14-20) and coreference resolution (11, 13)"
  - target: 2024-08-longbench-bilingual-benchmark
    type: complementary
    detail: "LongBench tasks (MultiFieldQA, PassageCount, PassageRetrieval) are classified across multiple quadrants in the taxonomy"
  - target: 2025-11-context-length-hurts-performance
    type: complementary
    detail: "Both papers challenge the assumption that retrieval is the sole bottleneck in long-context tasks; Du et al. show context length itself hurts even with perfect retrieval, while Goldman et al. argue the community should focus on tasks where retrieval alone is insufficient"
  - target: 2025-07-nolima-long-context-evaluation
    type: extended-by
    detail: "NOLIMA explicitly designs tasks targeting high dispersion by requiring multi-hop reasoning without literal lexical cues, directly addressing the under-explored quadrant identified by Goldman et al."
  - target: 2025-04-helmet-long-context-evaluation
    type: complementary
    detail: "HELMET evaluates across multiple task types spanning different scope-dispersion quadrants, contributing to the more nuanced evaluation vocabulary Goldman et al. call for"
  - target: 2024-03-gemini-1.5-long-context
    type: complementary
    detail: "Cited for models technically capable of processing up to 1M tokens, motivating the question of whether long context is genuinely utilized beyond retrieval"
  - target: 2017-12-attention-is-all-you-need
    type: complementary
    detail: "Cited as the foundational architecture whose extrapolation capabilities drive the push towards longer contexts"
open_questions:
  - question: "Can the dispersion and scope axes be formalized with concrete, quantitative metrics rather than remaining intuitive descriptors?"
    addressed_by: null
  - question: "What benchmark designs can effectively target the high-scope high-dispersion quadrant at scale (100K+ tokens)?"
    addressed_by: null
  - question: "Do models that perform well on high-dispersion high-scope tasks require fundamentally different architectures or training strategies than those optimized for retrieval-like tasks?"
    addressed_by: null
  - question: "How should evaluation metrics be adapted for tasks in the high-scope high-dispersion quadrant, where standard accuracy or F1 may be insufficient?"
    addressed_by: null
---

# Is It Really Long Context if All You Need Is Retrieval? Towards Genuinely Difficult Long Context NLP

**Authors:** Omer Goldman\*, Alon Jacovi\*, Aviv Slobodkin\*, Aviya Maimon\*, Ido Dagan, Reut Tsarfaty (Bar-Ilan University)
**Date:** November 2024, EMNLP 2024, pages 16576--16586 (arXiv:2407.00402)

---

## Core Research Problem

The ability to process long contexts has become a defining capability of large language models, with context windows growing from hundreds of tokens (Devlin et al., 2019; Raffel et al., 2020) to 128K and even 1M tokens (Gemini Team Google, 2024; OpenAI, 2024). This has spurred a line of research on designing long-context tasks and benchmarks (Shaham et al., 2022; Bai et al., 2023; Zhang et al., 2024). However, the field generally uses a single descriptor to characterize these measurements: **context length in tokens**. This means qualitatively different tasks -- Needle-in-a-Haystack, book summarization, information aggregation -- are grouped together and conclusions about capabilities are extended from one class to others.

Prior evaluation approaches fall into two categories. Naturally-constructed tasks extend short-context tasks to longer inputs (QA, summarization, NLI) or leverage domains with inherently long texts (legal, literature). Synthetically-constructed tasks use distractors to artificially increase length (NIAH, PassKey retrieval). Both approaches are typically differentiated only by length and construction method (natural vs. synthetic), which the authors argue is insufficient.

**The core challenge is: identifying the properties, beyond mere token count, that make long-context tasks qualitatively different from each other and from short-context tasks, in order to inform more productive benchmark design and model evaluation.**

---

## Problem Solutions

As a position paper, this work proposes a conceptual framework rather than an empirical method:

1. **Two-axis taxonomy.** Long-context task difficulty is characterized by two orthogonal axes: *Dispersion* (how hard it is to find and extract required information) and *Scope* (how much information is needed to solve the task).
2. **Literature survey and classification.** Existing long-context benchmarks are surveyed and positioned within the taxonomy, revealing that most benchmarks target either scope or dispersion but rarely both.
3. **Identification of under-explored quadrant.** The high-scope high-dispersion quadrant -- the most challenging and most indicative of genuine long-context capabilities -- is identified as severely under-explored.
4. **Call for targeted benchmark design.** The paper calls for tasks that explicitly target both axes, suggesting domain-expert tasks and structured-data aggregation as promising directions.

---

## Approach Details

### Taxonomy Definition

The taxonomy is defined by two orthogonal questions about a given task:

**(I) Dispersion.** How difficult is it to find and extract the required information? Information is harder to find when it is: (1) more obscured (linguistically, semantically, contextually); (2) more sparse, interspersed with non-required information; (3) less redundant, with fewer locations in the document where the same information is available (Section 3).

**(II) Scope.** How much information is needed to solve the task? This refers to the minimal quantity of required information -- measured in tokens, sentences, relations, table cells, or any metric that reliably captures difficulty for an established solver (Section 3).

The taxonomy produces four quadrants (Figure 1):

| | Low Scope | High Scope |
|---|---|---|
| **Low Dispersion** | Easiest (e.g., NIAH, simple QA) | Moderate (e.g., aggregation, QBS) |
| **High Dispersion** | Moderate (e.g., multi-hop QA, code understanding) | Hardest (e.g., book summarization, high-dispersion reasoning) |

### Illustrative Example

Using the Wikipedia entry for New York City (Section 3):
- "What is the estimated population?" -- **low scope, low dispersion** (small snippet, easily accessible)
- "How many syllables are in this document?" -- **high scope, low dispersion** (requires entire document, but counting is straightforward)
- "Was the city's mayor elected before or after Hurricane Sandy?" -- **low scope, higher dispersion** (requires finding two separate facts)
- "What makes the city a prominent place on the world stage?" -- **high scope, high dispersion** (requires synthesizing dispersed information across the document)

### Survey of Long-Context Tasks

**With respect to dispersion (Section 4):**
- **Low dispersion:** NIAH (Kamradt, 2023; Mohtashami and Jaggi, 2023), factual single-hop QA (NarrativeQA, NQ, Qasper, etc.)
- **Moderate dispersion:** Multi-needle NIAH (Arora et al., 2023; Hsieh et al., 2024), multi-hop QA (MuSiQue, HotpotQA), tasks with less straightforward detection (QuALITY)
- **High dispersion:** Summarization (GovReport, BookSum, SQuALITY), coreference resolution, code understanding

**With respect to scope (Section 4):**
- **Low scope:** NIAH and variants, most QA datasets
- **Moderate scope:** Query-based summarization (QMSum, SQuALITY), QA with obfuscated answers requiring surrounding context
- **High scope:** Book summarization (limited to ~20K tokens in practice), common words extraction (artificial, low dispersion)

### Classification of Benchmarks

Appendix A (Table 1) provides a detailed four-quadrant classification of 90+ benchmark tasks, organized by both scope and dispersion. The classification reveals that the high-scope high-dispersion quadrant contains primarily summarization tasks and a small number of reasoning tasks (Long ListOps, LRA task 3), confirming the under-exploration claim.

---

## Limitations and Failure Modes

- **Informal taxonomy.** The dispersion and scope axes are deliberately defined informally, without concrete quantitative metrics. The authors acknowledge this as intentional (for flexibility) but it limits the taxonomy's precision: the Figure 2 scatter plot involves "a good deal of subjective judgements" (Section 4).
- **No empirical validation.** The paper does not experimentally validate that the proposed axes predict task difficulty for models. The claim that high-scope high-dispersion tasks are harder is justified by intuition and informal argument, not by controlled experiments measuring model performance across the quadrants.
- **Scope is underspecified.** "Quantity of information" is left vague -- it could mean tokens, relations, or cells. Different metrics might produce different classifications for the same task.
- **Static classification.** Individual benchmarks are assigned single positions in the taxonomy, but many contain tasks spanning multiple quadrants (e.g., RULER has tasks in three of the four quadrants). The paper acknowledges this for QA but the table in Appendix A assigns each benchmark a single cell.
- **Only input-as-task.** The taxonomy only covers long inputs that serve as inputs to a task. Other uses of long context (many in-context examples, multi-modal inputs, agentic tool-use contexts) are excluded (Limitations section).
- **Retrieval is still useful.** The title's framing may undervalue retrieval-focused tasks: the authors acknowledge that low-scope low-dispersion tasks are "certainly relevant and useful" for common use-cases (Limitations section).

---

## Conclusions

### Contributions

1. **Two-axis taxonomy for long-context task difficulty.** Proposed dispersion and scope as two orthogonal axes that capture the properties making long-context tasks more difficult beyond mere input length, providing a shared vocabulary for the community (Section 3, Figure 1).

2. **Comprehensive survey and classification of benchmarks.** Classified 90+ long-context benchmark tasks into four quadrants of the taxonomy, providing a map of the current evaluation landscape (Section 4, Figure 2, Table 1).

3. **Identification of under-explored difficulty regime.** Demonstrated that the high-scope high-dispersion quadrant -- where required information is extensive and difficult to extract -- is severely under-represented in current benchmarks (Section 4, Figure 2).

4. **Actionable directions for benchmark design.** Identified domain-expert tasks (legal, financial, biomedical) and structured-data aggregation as promising avenues for creating benchmarks that target both axes (Section 5).

### Implications

1. **Benchmark scores conflate different capabilities.** Aggregate "long-context" scores that combine tasks from different quadrants may be misleading, as high performance on retrieval-like tasks (low scope, low dispersion) does not imply capability on synthesis tasks (high scope, high dispersion). [Inference: this follows logically from the taxonomy but is not empirically demonstrated.]

2. **NIAH-style evaluations are necessary but insufficient.** NIAH and similar retrieval tasks test only the low-scope low-dispersion quadrant. Claims about "long-context capabilities" based solely on such evaluations are overclaimed. [Inference: this is the paper's central argument.]

3. **Model development may be biased towards retrieval.** If benchmarks disproportionately measure retrieval-like capabilities, model development may optimize for the wrong objective, neglecting the synthesis and reasoning capabilities needed for genuinely difficult long-context tasks. [Speculative: not directly argued in the paper.]

---

## Key Claims

1. **C1: Context length alone is an insufficient descriptor for long-context task difficulty.** Grouping tasks by input length conflates qualitatively different challenges, making conclusions about long-context capabilities unreliable when extended across task types. Evidence: the paper surveys numerous tasks at similar context lengths but with fundamentally different difficulty profiles (Section 1, Section 2, Section 3). Status: **supported**.

2. **C2: Two orthogonal axes -- dispersion and scope -- capture the key difficulty dimensions.** The taxonomy provides a more informative characterization than length alone. Evidence: illustrative examples (Section 3), classification of 90+ benchmarks (Table 1), and the observation that the classification surfaces a meaningful gap (Section 4). Status: **unvalidated** (the axes are proposed informally without quantitative validation that they predict model performance).

3. **C3: Most benchmarks target either scope or dispersion, not both.** The literature survey shows tasks cluster along one axis at a time. Evidence: Figure 2 and Table 1 (Section 4). Status: **supported**.

4. **C4: The high-scope high-dispersion quadrant is under-explored.** The most challenging setting for long-context evaluation has very few representative benchmarks. Evidence: Figure 2 shows the upper-right quadrant is sparsely populated (Section 4). Status: **supported**.

5. **C5: Low-scope low-dispersion tasks are least indicative of genuine long-context capabilities.** These tasks can be solved by implicit retrieval and do not require the model to synthesize information across the full context. Evidence: the observation that NIAH-style tasks do not distinguish models on their ability to handle genuinely long context (Section 3, Section 4). Status: **supported**.

---

## Open Questions

1. **Quantitative formalization.** Can dispersion and scope be operationalized with concrete, reproducible metrics (e.g., information-theoretic measures, compression ratios, attention entropy)? The informal definition is the paper's acknowledged limitation. Not yet addressed.

2. **Benchmark design for the hardest quadrant.** What practical benchmark designs can target high-scope high-dispersion at scale (100K+ tokens)? The paper suggests domain-expert tasks and structured-data aggregation but does not implement them. Partially addressed by NOLIMA (2025-07-nolima-long-context-evaluation), which targets high-dispersion evaluation.

3. **Architectural implications.** Do models that excel at high-dispersion high-scope tasks require fundamentally different architectures (e.g., hierarchical attention, retrieval-augmented generation, memory mechanisms) or training regimes? Not yet addressed.

4. **Metric design.** How should evaluation metrics be adapted for high-scope high-dispersion tasks, where standard accuracy or F1 on extractive answers may be insufficient to capture the quality of synthesis? Not yet addressed.

---

## Core References and Why They Are Referenced

### Benchmark Design Foundations

- **Shaham et al. (2022)** -- *SCROLLS: Standardized CompaRison over Long Language Sequences.* Example of a benchmark that groups tasks primarily by input length, motivating the need for a more nuanced taxonomy.

- **Bai et al. (2023)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* Another benchmark grouping tasks by length; individual tasks (MultiFieldQA, PassageCount, PassageRetrieval) are classified across the taxonomy quadrants.

- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* RULER tasks span multiple quadrants: single-hop QA (low/low), MV-NIAH and MQ-NIAH (high-dispersion/low-scope), aggregation tasks (high-dispersion), demonstrating that even within one benchmark, tasks differ fundamentally.

- **Shaham et al. (2023)** -- *ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding.* ZeroSCROLLS tasks (SpaceDigest, BookSumSort) classified as high-scope low-dispersion aggregation tasks.

### Retrieval-Focused Long-Context Tasks

- **Kamradt (2023)** -- *Needle in a Haystack -- Pressure Testing LLMs.* The canonical example of a low-scope low-dispersion task that tests retrieval rather than genuine long-context understanding.

- **Mohtashami and Jaggi (2023)** -- *Landmark Attention: Random-Access Infinite Context Length for Transformers.* PassKey retrieval task, another exemplar of the low-scope low-dispersion quadrant.

- **Liu et al. (2024)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Multi-document QA and key-value retrieval classified as low-scope tasks; position bias findings complement the argument that retrieval-focused tasks measure a narrow capability.

### Tasks Increasing Dispersion

- **Levy et al. (2024)** -- *Same Task, More Tokens: The Impact of Input Length on the Reasoning Performance of Large Language Models.* Cited as evidence that adding distractors between needles increases dispersion independently of needle count or context length.

- **Arora et al. (2023)** -- *Zoology: Measuring and Improving Recall in Efficient Language Models.* Multi-needle retrieval increases dispersion by requiring location of multiple snippets.

- **Trivedi et al. (2022)** -- *MuSiQue: Multi-Hop Questions via Single-Hop Question Composition.* Multi-hop QA increases dispersion through multi-step information finding.

### Tasks with High Scope

- **Wang et al. (2022)** -- *SQuALITY: Building a Long-Document Summarization Dataset the Hard Way.* Example of high-scope tasks (query-based summarization) that also have moderate-to-high dispersion.

- **Kuratov et al. (2024)** -- *BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack.* BABILong tasks span all four quadrants, from simple retrieval to high-dispersion reasoning and coreference resolution.

### Architecture and Context Extension

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational architecture whose extrapolation capabilities drive the push towards longer contexts.

- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Cited as an extrapolation architecture enabling longer context windows.

- **Gemini Team Google (2024)** -- *Gemini 1.5: Unlocking Multimodal Understanding across Millions of Tokens of Context.* Cited for models technically capable of processing up to 1M tokens, motivating the question of whether this capacity is genuinely utilized.
