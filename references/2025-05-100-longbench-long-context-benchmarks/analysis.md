---
title: "100-LongBench: Are de facto Long-Context Benchmarks Literally Evaluating Long-Context Ability?"
authors: "Yang, Jin, Zhong, Jiang, Wang, Chaudhary, Han"
year: 2025
venue: "arXiv 2025"
paper_type: preprint
categories: ["benchmarking", "long-context-evaluation"]
scope: ["long-context benchmark design", "evaluation metric design", "disentangling base ability from long-context capability"]
benchmarks_used: ["longbench", "ruler", "l-eval", "helmet", "niah", "100-longbench"]
models_introduced: []
models_evaluated: ["llama-3.1-8b", "llama-3.1-70b", "llama-3.2-1b", "llama-3.2-3b", "phi-3-mini", "phi-3-medium", "qwen2.5-7b", "qwen2.5-14b", "yi-34b", "gemini-1.5-pro", "gemini-1.5-flash"]
key_claims:
  - id: C1
    claim: "Existing long-context benchmarks conflate a model's baseline ability with its long-context capability: rankings based on traditional average scores are almost identical to rankings based on Base Ability (short-context performance)"
    evidence: "Table 4, Section 4.3"
    status: supported
    scope: "LongBench and similar fixed-length benchmarks"
  - id: C2
    claim: "LongScore metric produces significantly different rankings from traditional metrics, revealing that models with high average scores (e.g., Qwen 2.5-14B-Instruct) can have poor long-context capability (worst LongScore despite ranking first by Base Ability)"
    evidence: "Table 4, Figure 6, Section 4.3"
    status: supported
    scope: "open-source models with up to 256K context"
    magnitude: "Qwen2.5-14B ranks 1st by Base Ability (59.1) but last by Avg LongScore (-31.1)"
  - id: C3
    claim: "LongScore provides greater discriminative power than traditional average scores, amplifying meaningful gaps between methods that align with community understanding (NTK > PI, RoPE ratio=64 > ratio=1, Gemini-1.5-Pro > Gemini-1.5-Flash)"
    evidence: "Table 6, Section 4.2"
    status: supported
    magnitude: "NTK vs PI: LongScore gap -18.40 vs -27.68; traditional avg gap 15.83 vs 13.87"
  - id: C4
    claim: "Within the same model family, larger models generally outperform smaller ones across all tasks and context lengths on 100-LongBench, confirming the benchmark's reliability"
    evidence: "Figure 5, Figure 13, Section 4.1"
    status: supported
    scope: "Llama 3.1, Llama 3.2, Phi-3 model families"
  - id: C5
    claim: "Models can answer QA questions from prior knowledge without reading the provided context, inflating long-context performance metrics; a QA filtering mechanism is necessary to remove such samples"
    evidence: "Figure 4, Section 3.1"
    status: supported
  - id: C6
    claim: "Performance of long-context enhancement methods varies significantly across different text lengths within the same LongBench dataset, with average performance dominated by the most common length range"
    evidence: "Figure 1, Section 2"
    status: supported
    scope: "LM-Infinite evaluated on Multi-News, Qasper, Gov Report from LongBench"
cross_references:
  - target: 2024-08-longbench-bilingual-benchmark
    type: extends
    detail: "100-LongBench restructures LongBench datasets with controllable-length context and proposes LongScore to disentangle base ability from long-context capability"
  - target: 2024-10-ruler-context-size
    type: complementary
    detail: "Both provide controllable-length evaluation; RULER uses purely synthetic tasks while 100-LongBench combines real-world and reflective-synthetic tasks with a QA filtering mechanism"
  - target: 2024-08-l-eval-standardized-evaluation
    type: complementary
    detail: "L-Eval is cited as an early benchmark that, like LongBench, has fixed non-controllable context lengths and no long-context capability distinction"
  - target: 2023-06-pi-positional-interpolation
    type: evaluates
    detail: "PI is compared against NTK on 100-LongBench to validate LongScore's discriminative power (Table 6)"
  - target: 2024-05-yarn-context-extension
    type: evaluates
    detail: "YaRN is used by Qwen 2.5 models to extend context to 128K; these extended models are evaluated on 100-LongBench"
  - target: 2021-05-long-range-arena
    type: complementary
    detail: "LRA evaluates efficient Transformers with synthetic tasks; 100-LongBench evaluates LLMs with controllable-length real-world and reflective-synthetic tasks"
  - target: 2025-03-survey-transformer-context-extension
    type: complementary
    detail: "Survey provides a complementary taxonomy of long-context evaluation approaches, contextualizing the base-ability-vs-long-context-capability distinction within the broader landscape of context extension methods"
open_questions:
  - question: "Does LongScore remain effective when the model's base ability is very weak, given that the metric normalizes by Base Ability?"
    addressed_by: null
  - question: "How does 100-LongBench generalize to closed-source models where base ability estimation may differ due to different pretraining context lengths?"
    addressed_by: null
  - question: "Can the QA filtering mechanism be extended to non-QA tasks such as summarization to further isolate long-context capability?"
    addressed_by: null
---

# 100-LongBench: Are *de facto* Long-Context Benchmarks Literally Evaluating Long-Context Ability?

**Authors:** Wang Yang, Hongye Jin, Shaochen Zhong, Song Jiang, Qifan Wang, Vipin Chaudhary, Xiaotian Han
**Date:** May 2025
**Affiliations:** Case Western Reserve University, Texas A&M University, Rice University, Meta

---

## Core Research Problem

Existing long-context evaluation benchmarks suffer from three shortcomings that undermine their ability to assess models' true long-context capabilities:

1. **Non-reflective synthetic content:** Benchmarks like NIAH and Passkey Retrieval use purely synthetic content (random digits, unrelated blog posts) with no semantic or task relevance to the padding context, failing to reflect real-world long-context usage scenarios.

2. **Fixed input lengths:** Each data sample has a fixed sequence length, making benchmarks suitable only for models with compatible context windows. With context windows growing from 4K to 128K+, many "long-context" datasets have become outdated. Moreover, constant-budget methods (StreamingLLM, InfLLM) report "compressed performance" that mixes compressed and uncompressed evaluation.

3. **Conflation of base ability and long-context capability:** Benchmarks evaluate long-context capabilities solely based on task scores without isolating the influence of a model's baseline abilities. A model scoring high on long-context tasks may simply be a better general model, not necessarily better at handling long contexts specifically.

---

## Problem Solutions

The paper proposes two complementary solutions:

1. **100-LongBench:** A length-controllable long-context benchmark with 8 tasks across 4 categories, where context length can be specified (e.g., up to ~128K tokens). Tasks use "real-life reflective" synthetic construction — content is semantically aligned and task-compatible, mimicking real usage patterns like RAG pipelines.

2. **LongScore:** A new evaluation metric that disentangles a model's Base Ability from its long-context capability by normalizing performance degradation relative to short-context performance.

---

## Approach Details

### Benchmark Construction

**Task taxonomy** — four types, each with two difficulty levels, yielding eight tasks:

| Type | Tasks | Evaluation Metric |
|------|-------|-------------------|
| **Key Retrieval** | KV Retrieval, Counting Stars | Accuracy |
| **Information Retrieval** | Passage Retrieval, Passage Count | Accuracy |
| **Information Comprehension** | Single-doc QA, Multi-doc QA | LLM-based (Fluency × Correctness) |
| **Information Summarization** | Single-doc Sum, Multi-doc Sum | LLM-based (Fluency × Precision) |

**Length-controllable context generation:** For each task, the context length is controllable up to ~128K tokens. The process:
1. Randomly select one article from **Real Context Sources** as the ground truth
2. Sample distractor articles from **Noisy Context Sources** (same domain, task-compatible)
3. Combine ground truth and distractors, shuffle ordering, to reach target length

Real and Noisy Context Sources are drawn from 20 existing datasets spanning diverse domains: qasper, multifieldqa, narrativeqa, multidoc_qa, legal_contract_qa, financial_qa, natural_question, scientific_qa, cnn_dailymail, gov_report, qmsum, patent_summ, tv_show_summ, review_summ, meeting_summ, hotpotqa, 2wikimqa, musique, rag-mini-bioasq, multi_news_e (Table 2).

**QA filtering mechanism:** For QA tasks, models are tested in a no-context scenario. If the model's response score exceeds a threshold, it indicates reliance on prior knowledge rather than context comprehension, and that sample is excluded from evaluation.

### LongScore Metric

**Base Ability** is estimated from short-context performance:

> Base Ability = (S_{2k} + S_{4k} + S_{6k}) / 3

where S_{*k} is the model's score at context length *k. These lengths are chosen because most models have a pre-extension context window of 4K or 8K.

**LongScore** (LC_l) for a given length l:

> LC_l = (S_l - Base Ability) / Base Ability

LongScore captures the *relative* improvement or decline at longer lengths, normalized by the model's short-context performance. This enables fair cross-model comparison by removing the influence of Base Ability.

### Comparison with Other Benchmarks

Table 3 compares 100-LongBench against six existing benchmarks across six properties:

| Property | LongBench | L-Eval | ∞-Bench | NIAH | RULER | Helmet | 100-LongBench |
|----------|-----------|--------|---------|------|-------|--------|---------------|
| L > 128K | No | No | Yes | Yes | Yes | Yes | Yes |
| Controllable | No | No | No | Yes | Yes | Yes | Yes |
| Diverse Tasks | Yes | Yes | Yes | No | Yes | Yes | Yes |
| LLM-based Metric | No | Yes | No | — | — | Yes | Yes |
| LC Distinction | No | No | No | No | No | No | **Yes** |
| QA Filter | No | No | No | — | — | No | **Yes** |

100-LongBench is the only benchmark providing both **LC distinction** (separating base ability from long-context capability) and **QA filtering** (removing prior-knowledge contamination).

### Experimental Setup

- **Benchmark validation (Section 4.1):** Three model families (Llama 3.2, Llama 3.1, Phi-3), two sizes each, tested on all 8 tasks at context lengths 8K–256K.
- **Metric validation (Section 4.2):** Three pairwise comparisons: NTK vs. PI on 100-LongBench, LLaMA3-8B with RoPE ratio=1 vs. ratio=64, and Gemini-1.5-Flash vs. Gemini-1.5-Pro on HELMET.
- **Frontier open-source evaluation (Section 4.3):** Four models (Qwen2.5-14B, Qwen2.5-7B, Llama3.1-8B, Llama3.2-1B) at 100 samples per task at each context length (8K, 16K, 32K, 64K, 128K). Base Ability from 2K, 4K, 6K.
- **Extended evaluation (Appendix A.5):** Eight models from four families at five context lengths.
- **RULER validation (Section 4.4):** LongScore applied to RULER data (Hsieh et al., 2024) using 4K as Base Ability.

### Key Results

**Benchmark reliability (Section 4.1):** Across all three model families, larger models consistently outperform smaller ones at every context length and on every task (Figure 5, Figure 13). Performance decreases as context length increases for all models, confirming expected trends.

**Metric effectiveness (Section 4.2):** LongScore amplifies discriminative differences between methods that are known to differ in long-context quality:
- NTK vs. PI: Average score gap is 15.83 vs. 13.87 (barely distinguishable); LongScore gap is −18.40 vs. −27.68 (clearly different)
- RoPE ratio=64 vs. ratio=1: Average score 18.83 vs. 7.13; LongScore −42.12 vs. −79.84
- Gemini-1.5-Pro vs. Flash: Average score 57.77 vs. 56.00; LongScore −2.90 vs. −6.04

**Frontier model evaluation (Section 4.3):** Traditional metric rankings mirror Base Ability rankings almost exactly. LongScore reveals a fundamentally different picture:
- Qwen2.5-14B-Instruct: **1st** by Base Ability (59.1), **last** by Avg LongScore (−31.1)
- Llama3.2-1B-Instruct: **last** by Base Ability (28.7), **2nd** by Avg LongScore (−28.8)

**RULER validation (Section 4.4):** Applying LongScore to RULER data (Table 5) reveals that the traditional metric rankings are "heavily influenced by the model's inherent abilities, which might not really reflect long-context ability." For example, Yi (34B) has a slightly lower overall score than Llama3.1 (70B) before 128K but performs significantly better at 128K; LongScore captures this.

---

## Limitations and Failure Modes

1. **Base Ability assumption:** LongScore requires models to have "relatively strong base ability on the task." If base ability is insufficient, long-context evaluations may exhibit significant fluctuations (Section: Limitations).

2. **Article length constraints:** When constructing contexts for shorter target lengths (e.g., 2K), the selected articles must also be short (< 1K tokens) to ensure at least two documents can form the context. This requires collecting texts of diverse lengths, particularly shorter ones.

3. **Negative LongScore values:** All models evaluated achieve negative LongScore values across all lengths (Tables 4, 5, 7), meaning performance consistently degrades with length. The metric cannot distinguish between models that degrade gracefully and those with different degradation profiles at very long contexts if both are severely negative.

4. **LLM-based evaluation:** Four of eight tasks use GPT-4o-mini as evaluator, introducing potential evaluator bias and non-reproducibility as the evaluation model changes.

---

## Conclusions

### Contributions

1. **Diagnostic critique:** Identifies and empirically demonstrates that existing long-context benchmarks conflate base ability with long-context capability, producing misleading rankings.

2. **100-LongBench benchmark:** Introduces a length-controllable benchmark with 8 diverse tasks covering retrieval, comprehension, and summarization, using real-life reflective synthetic construction and a QA filtering mechanism.

3. **LongScore metric:** Proposes a simple normalization-based metric that disentangles base ability from long-context capability, enabling fairer cross-model comparison.

4. **Comprehensive evaluation:** Provides fresh rankings of 8 open-source models across 4 model families using LongScore, revealing that traditional metrics can be severely misleading.

### Implications

- Existing benchmark rankings (LongBench, RULER, etc.) may not accurately reflect which models are truly better at long-context processing, since they do not separate baseline NLU ability from long-context degradation.
- Future long-context benchmarks should incorporate metrics that normalize for base ability.
- QA filtering for prior knowledge contamination is an important but often overlooked component of long-context evaluation.

---

## Key Claims

1. **[C1]** Existing long-context benchmarks conflate base ability with long-context capability, producing rankings almost identical to Base Ability rankings (Table 4, Section 4.3).

2. **[C2]** LongScore produces significantly different rankings: Qwen2.5-14B ranks 1st by Base Ability but last by LongScore (Table 4).

3. **[C3]** LongScore amplifies meaningful gaps between methods that align with community understanding (NTK > PI, RoPE ratio=64 > ratio=1, Gemini-1.5-Pro > Flash) (Table 6).

4. **[C4]** Larger models outperform smaller ones within the same family on 100-LongBench, confirming benchmark reliability (Figure 5).

5. **[C5]** Models can answer QA questions from prior knowledge without context, necessitating a QA filtering mechanism (Figure 4).

6. **[C6]** Performance varies significantly across text lengths within the same LongBench dataset, with averages dominated by the most common length range (Figure 1).

---

## Open Questions

1. Does LongScore remain effective when the model's base ability is very weak, given that the metric normalizes by Base Ability?
2. How does 100-LongBench generalize to closed-source models where base ability estimation may differ due to different pretraining context lengths?
3. Can the QA filtering mechanism be extended to non-QA tasks such as summarization to further isolate long-context capability?

---

## Core References and Why They Are Referenced

- **LongBench (Bai et al., 2023):** Primary benchmark being critiqued; source of datasets restructured for 100-LongBench.
- **RULER (Hsieh et al., 2024):** Controllable synthetic benchmark used for LongScore validation in Section 4.4; compared in Table 3.
- **L-Eval (An et al., 2023):** Early long-context benchmark cited as having same fixed-length and conflation limitations.
- **HELMET (Yen et al., 2024):** Recent controllable benchmark with LLM-based metrics; data used for Gemini comparison in Table 6.
- **Counting Stars (Song et al., 2024):** Task design adopted for the Counting Stars task in 100-LongBench.
- **LM-Infinite (Han et al., 2024):** Long-context enhancement method whose performance variation across lengths motivates the paper (Figure 1).
- **Position Interpolation (Chen et al., 2023a):** Context extension method compared against NTK to validate LongScore's discriminative power (Table 6).
- **NTK-aware RoPE (Peng and Quesnelle, 2023):** Context extension method compared against PI to validate LongScore (Table 6).
- **YaRN (Peng et al., 2023):** Used by Qwen 2.5 models for context extension to 128K.
- **StreamingLLM (Xiao et al., 2023):** Constant-budget method cited as producing misleading "compressed performance" under fixed-length benchmarks.
- **Llama 3.1 (Dubey et al., 2024):** Model family evaluated; representative of 128K context models that make older benchmarks outdated.
