---
title: "The Gap Between Claimed and Effective Context Length in Large Language Models"
research_question: "How large is the gap between claimed and effective context lengths, and what factors predict degradation?"
date_produced: 2026-02-05
corpus:
  - 2018-07-sharp-nearby-fuzzy-far-away
  - 2021-08-context-features-transformer-lm
  - 2021-11-long-range-models-use-context
  - 2023-11-needle-in-a-haystack
  - 2024-02-lost-in-the-middle
  - 2024-06-ada-leval-length-adaptable-benchmark
  - 2024-07-qwen2-technical-report
  - 2024-08-flenqa-input-length-reasoning
  - 2024-08-infinitebench-long-context-evaluation
  - 2024-08-longbench-bilingual-benchmark
  - 2024-10-ruler-context-size
  - 2024-11-genuinely-difficult-long-context
  - 2024-12-babilong-long-context-reasoning
  - 2024-12-transformers-need-glasses-over-squashing
  - 2025-03-longiclbench-long-in-context-learning
  - 2025-04-effective-context-length-falls-short
  - 2025-07-longbench-v2
  - 2025-07-nolima-long-context-evaluation
  - 2025-11-context-length-hurts-performance
  - 2026-01-longbench-pro
corpus_search_strategy: |
  category long-context-evaluation
  category benchmarking
  category context-extension
  category position-bias
  category attention-analysis
  text "effective context"
  text "degradation"
  text "claimed"
  text "over-squashing"
categories: ["long-context-evaluation", "benchmarking", "position-bias", "attention-analysis"]
themes:
  - id: magnitude-of-gap
    label: "Magnitude of the effective-vs-claimed gap"
  - id: task-sensitivity
    label: "Task type as a moderator of effective length"
  - id: causal-mechanisms
    label: "Causal mechanisms underlying the gap"
  - id: model-scale-effects
    label: "Model scale and architecture effects"
  - id: mitigation-strategies
    label: "Inference-time and training-time mitigations"
consensus_claims:
  - claim: "Most LLMs effectively utilize substantially less than their claimed context window, with effective lengths typically 25-50% of claimed lengths on synthetic benchmarks and often far less on realistic tasks"
    sources: ["2024-10-ruler-context-size", "2024-12-babilong-long-context-reasoning", "2025-04-effective-context-length-falls-short", "2024-07-qwen2-technical-report", "2026-01-longbench-pro"]
    strength: strong
  - claim: "Performance degradation with context length occurs even when retrieval is perfect, demonstrating that length itself is an independent degradation factor beyond retrieval difficulty"
    sources: ["2024-08-flenqa-input-length-reasoning", "2025-11-context-length-hurts-performance"]
    strength: strong
  - claim: "Perplexity and next-word prediction accuracy are negatively correlated with downstream task performance at longer contexts, making perplexity an unreliable proxy for long-context capability"
    sources: ["2024-08-flenqa-input-length-reasoning", "2024-12-babilong-long-context-reasoning"]
    strength: moderate
  - claim: "Larger model sizes correlate with better effective context utilization, but no model achieves 100% utilization of its claimed window"
    sources: ["2024-10-ruler-context-size", "2025-11-context-length-hurts-performance", "2024-07-qwen2-technical-report", "2025-07-longbench-v2", "2026-01-longbench-pro"]
    strength: strong
  - claim: "The left-skewed position frequency distribution in pretraining corpora is a root cause of the effective context gap, with position frequency -- not training window size -- determining effective length"
    sources: ["2025-04-effective-context-length-falls-short"]
    strength: moderate
  - claim: "Removing literal lexical overlap between queries and relevant information dramatically reduces effective context length, from 32K (RULER) to as low as 2K (NoLiMa) for the same model"
    sources: ["2025-07-nolima-long-context-evaluation", "2024-10-ruler-context-size"]
    strength: strong
  - claim: "Position bias (U-shaped performance with respect to information location) is a consistent contributor to degradation, with information in the middle of the context being hardest to use"
    sources: ["2024-02-lost-in-the-middle", "2024-06-ada-leval-length-adaptable-benchmark", "2025-03-longiclbench-long-in-context-learning"]
    strength: strong
contested_claims:
  - claim: "Whether position bias or context length per se is the primary bottleneck for long-context performance"
    for: ["2024-02-lost-in-the-middle", "2024-06-ada-leval-length-adaptable-benchmark"]
    against: ["2025-11-context-length-hurts-performance", "2025-07-nolima-long-context-evaluation"]
    resolution: "Both factors contribute independently. Position bias dominates for retrieval-like tasks, while context length alone degrades reasoning even when position effects are controlled for."
    resolved: true
  - claim: "Whether lost-in-the-middle effects persist at 100K+ contexts"
    for: ["2024-02-lost-in-the-middle"]
    against: ["2024-08-infinitebench-long-context-evaluation"]
    resolution: "InfiniteBench finds no consistent lost-in-the-middle effect at 100K+, but the task and model differences make direct comparison difficult. NoLiMa later showed that position effects persist for one-hop tasks but context length dominates for two-hop tasks."
    resolved: true
gaps:
  - description: "No study systematically measures effective context length across both synthetic and realistic tasks on the same models with the same methodology"
    severity: high
  - description: "The relationship between position frequency distributions in post-training stages (SFT, RLHF) and effective context length is unexplored"
    severity: high
  - description: "No benchmark tests effective context utilization for generation tasks (summarization, translation) as rigorously as for retrieval and QA"
    severity: medium
  - description: "The interaction between chain-of-thought reasoning and context length degradation is poorly characterized beyond FlenQA's finding that CoT provides constant rather than compensatory benefit"
    severity: medium
  - description: "Whether training-time interventions (position-balanced data, curriculum learning) can close the effective-to-claimed gap remains speculative"
    severity: high
overall_confidence:
  - conclusion: "The gap between claimed and effective context length is substantial, task-dependent, and persistent across model generations"
    level: high
    basis: "20 papers with diverse methodologies, covering 100+ models, consistent findings across synthetic and realistic evaluations"
    caveats: ["Magnitude of gap varies by benchmark design and threshold definition", "Frontier closed-source models show smaller gaps but are not immune"]
---

# The Gap Between Claimed and Effective Context Length in Large Language Models

**Research question:** How large is the gap between claimed and effective context lengths, and what factors predict degradation?
**Corpus:** 20 papers, 2018--2026.
**Categories:** long-context-evaluation, benchmarking, position-bias, attention-analysis.

---

## Executive Summary

- The gap between claimed and effective context length is large and persistent. On RULER, only half of models claiming 32K+ context maintain satisfactory performance at 32K; effective lengths range from <4K to 64K against claims of 32K to 1M (`2024-10-ruler-context-size`). On BABILong, most LLMs effectively utilize only 10--20% of their claimed context (`2024-12-babilong-long-context-reasoning`). On NoLiMa (which removes literal cues), 11 of 13 models claiming 128K+ context drop below 50% of their base score at just 32K tokens (`2025-07-nolima-long-context-evaluation`).
- The gap widens dramatically with task complexity. Vanilla NIAH (single-fact retrieval with high lexical overlap) yields near-perfect scores, but the same models fail on harder tasks: RULER aggregation, NoLiMa latent reasoning, BABILong multi-hop, and Ada-LEval full-text comprehension all expose effective lengths far below what NIAH suggests (`2024-10-ruler-context-size`, `2025-07-nolima-long-context-evaluation`, `2024-06-ada-leval-length-adaptable-benchmark`). Qwen2 provides an especially clear within-paper demonstration: Qwen2-72B achieves near-perfect NIAH at 128K, but drops to 17.13 on NeedleBench and 2.88 on LV-Eval at 256K without context-extension methods (`2024-07-qwen2-technical-report`).
- Context length alone degrades reasoning performance, independent of retrieval quality and distraction content. FlenQA shows degradation from 0.92 to 0.68 accuracy at just 3K tokens (`2024-08-flenqa-input-length-reasoning`); Du et al. show 13.9--85% drops at 30K even with perfect retrieval and attention-masked distractors (`2025-11-context-length-hurts-performance`).
- Multiple causal mechanisms contribute to the gap: undertrained position indices from left-skewed pretraining distributions (`2025-04-effective-context-length-falls-short`), over-squashing from the causal attention topology (`2024-12-transformers-need-glasses-over-squashing`), and position-dependent attention bias (`2024-02-lost-in-the-middle`).
- Larger model scale helps but does not eliminate the gap. Closed-source models (GPT-4o, Gemini) show less degradation than 7--8B open-source models, but no model achieves full utilization (`2025-11-context-length-hurts-performance`, `2024-10-ruler-context-size`). On LongBench Pro, even Gemini-2.5-Pro drops from 74.5 at 8K to 71.8 at 256K (`2026-01-longbench-pro`).
- Literal lexical overlap between queries and relevant information is a confounding factor. Benchmarks with high overlap (ROUGE-1 up to 0.966 for InfiniteBench QA) dramatically overestimate effective context: Llama 3.1 70B achieves 32K effective length on RULER but only 2K on NoLiMa (`2025-07-nolima-long-context-evaluation`).
- Inference-time mitigations (STRING, retrieve-then-reason) partially close the gap. STRING improves Llama 3.1 70B by 15.1 points on RULER at 128K (`2025-04-effective-context-length-falls-short`); retrieve-then-reason improves Mistral by up to 31.2% on GSM8K (`2025-11-context-length-hurts-performance`). However, no current mitigation fully eliminates length-induced degradation.

---

## Temporal Evolution

The understanding of the effective-vs-claimed context gap evolved through three distinct phases.

| Date | Paper | Key Contribution | Shift |
|------|-------|-------------------|-------|
| 2018-07 | Sharp Nearby, Fuzzy Far Away | LSTM effective context ~200 tokens; word order irrelevant beyond 50 tokens | Established that language models use context far more shallowly than assumed |
| 2021-08 | What Context Features Can Transformer LMs Use? | Content words carry most usable information; word order and function words contribute little | Distinguished usable information from distributional shift via V-information framework |
| 2021-11 | Do Long-Range Models Use Context? | Transformer LMs gain negligible aggregate perplexity beyond 2K tokens | Extended the finding to efficient Transformers; long-range benefit limited to token copying |
| 2023-11 | Needle in a Haystack | GPT-4 degrades above 73K; position-dependent retrieval failures | Created the first systematic depth-vs-length diagnostic; made the gap visible via heatmaps |
| 2024-02 | Lost in the Middle | U-shaped performance curve; mid-context accuracy below closed-book | Established position bias as a first-class problem; motivated positional analysis in all subsequent work |
| 2024-06 | Ada-LEval | 0% accuracy on BestAnswer at 64K--128K despite 128K--200K claims | Showed full-text comprehension collapses at lengths far below claimed windows |
| 2024-07 | Qwen2 Technical Report | Near-perfect NIAH at 128K but NeedleBench drops to 17.13 at 256K; YARN+DCA recovers to 85.21 | Model developer's own data confirms NIAH overestimates effective context; context-extension methods partially close gap |
| 2024-08 | FlenQA | Reasoning degrades at 3K tokens; perplexity anti-correlates with downstream task | Demonstrated that length degrades reasoning even without distraction; invalidated perplexity as proxy |
| 2024-10 | RULER | Only half of 32K+ models pass at 32K; defined effective context length metric | Formalized the effective-vs-claimed comparison; showed NIAH alone is misleading |
| 2024-11 | Genuinely Difficult Long Context | Dispersion-scope taxonomy; NIAH is low-scope low-dispersion | Reframed the problem: benchmark difficulty, not just length, determines what the gap means |
| 2024-12 | BABILong | LLMs use 10--20% of claimed context; reasoning degrades more than retrieval | Extended NIAH to reasoning tasks; showed retrieval-to-reasoning gap grows with length |
| 2024-12 | Transformers Need Glasses | Over-squashing in decoder-only Transformers; representational collapse | Provided theoretical explanation for U-shaped curve via causal mask topology |
| 2025-03 | LongICLBench | ICL peaks at 7K--14K then declines; 174-class task yields near-zero | Showed the gap extends to in-context learning, not just QA/retrieval |
| 2025-04 | Effective Context Falls Short | Left-skewed position frequency is root cause; STRING improves by 15+ points | Provided the first causal explanation for why effective length falls short |
| 2025-07 | NoLiMa | Without literal cues, effective length drops to 2K--8K | Revealed that high NIAH scores partly reflect surface matching, not comprehension |
| 2025-07 | LongBench v2 | Human experts score 53.7%; models outperform on short but not medium contexts | Showed the gap is real even on human-calibrated realistic tasks |
| 2025-11 | Context Length Hurts Performance | Length alone causes 13.9--85% drops even with perfect retrieval + attention masking | Isolated length as an independent degradation factor, beyond retrieval and distraction |
| 2026-01 | LongBench Pro | MiniMax 4M-claimed scores below 128K models; GLM-4.6 crashes at claimed limit | Confirmed the gap persists with latest models; claimed length is unreliable even for 2026 models |

### Phase 1: Establishing the phenomenon (2018--2023)

The earliest evidence that language models use context more shallowly than assumed came from LSTM analysis. Khandelwal et al. (`2018-07-sharp-nearby-fuzzy-far-away`) showed that LSTM LMs have an effective context of only ~200 tokens, with word order mattering only within the nearest 50 tokens. O'Connor & Andreas (`2021-08-context-features-transformer-lm`) extended this line of inquiry to transformers using the V-information framework, which crucially distinguished *usable information* from distributional shift artifacts by retraining models on ablated contexts rather than ablating only at evaluation time. Their finding that content words carry almost all usable information in long-range context -- and that retaining only content words actually *improves* long-range predictions -- provided the first rigorous evidence that transformers extract only shallow lexical features from distant context. Concurrently, Sun et al. (`2021-11-long-range-models-use-context`) reached consistent conclusions via a different approach: the Routing Transformer gains negligible aggregate perplexity beyond 2K tokens despite attending to 8K, and long-range context helps only through superficial token copying, not discourse understanding. Together, these three papers established that models use context far more shallowly than their architectural capacity suggests, but the community's focus on scaling context windows meant these findings were not widely acted upon.

Kamradt (`2023-11-needle-in-a-haystack`) created the first widely adopted diagnostic by systematically sweeping depth and length on GPT-4-128K and Claude 2.1-200K. The heatmap visualizations made context utilization failures immediately visible: GPT-4 degraded above 73K tokens, and Claude 2.1 achieved only 27% baseline accuracy. The NIAH format became the standard evaluation, but its limitations -- single-needle, high lexical overlap -- would later be exposed.

### Phase 2: Systematic measurement and the benchmark explosion (2024)

2024 saw an explosion of benchmarks designed to measure different facets of the gap. Liu et al. (`2024-02-lost-in-the-middle`) established the U-shaped performance curve, showing that mid-context accuracy could drop below closed-book performance. RULER (`2024-10-ruler-context-size`) formalized the effective context length metric and showed that near-perfect NIAH scores masked large degradation on harder tasks. Ada-LEval (`2024-06-ada-leval-length-adaptable-benchmark`) pushed evaluation to 128K and found complete collapse. FlenQA (`2024-08-flenqa-input-length-reasoning`) demonstrated that reasoning degrades at just 3K tokens and that perplexity anti-correlates with downstream performance. BABILong (`2024-12-babilong-long-context-reasoning`) quantified that LLMs use only 10--20% of their claimed context.

A key conceptual advance was Goldman et al.'s taxonomy (`2024-11-genuinely-difficult-long-context`), which argued that conflating tasks by length alone was unproductive. Their dispersion-scope framework showed that most benchmarks target low-scope low-dispersion tasks (retrieval), leaving the high-scope high-dispersion quadrant (genuine long-context reasoning) under-explored.

Barbero et al. (`2024-12-transformers-need-glasses-over-squashing`) provided the first theoretical framework connecting long-context degradation to the causal attention topology. By adapting the over-squashing concept from graph neural networks, they proved that earlier tokens in decoder-only Transformers have exponentially more information pathways to the final token than later tokens, providing a topological explanation for the U-shaped retrieval curve observed empirically.

### Phase 3: Causal explanation and mitigation (2025--2026)

The transition from 2024 to 2025 shifted focus from measurement to mechanism. An et al. (`2025-04-effective-context-length-falls-short`) identified the left-skewed position frequency distribution as the root cause: the last L/3 of position indices are severely undertrained during pretraining, and effective context length is determined by position frequency, not training window size. Their STRING method demonstrated that the gap could be partially closed at inference time without training.

Du et al. (`2025-11-context-length-hurts-performance`) further isolated the problem by showing that context length *alone* degrades reasoning, even with perfect retrieval, whitespace distractors, and attention-masked irrelevant tokens. NoLiMa (`2025-07-nolima-long-context-evaluation`) revealed that removing literal lexical overlap reduced effective lengths to 2K--8K, exposing a confound in all prior NIAH-style evaluations. LongBench v2 (`2025-07-longbench-v2`) and LongBench Pro (`2026-01-longbench-pro`) confirmed the gap persists on realistic, human-calibrated tasks and even with the latest frontier models.

---

## Thematic Synthesis

### Magnitude of the effective-vs-claimed gap

**Statement:** Across all evaluation methodologies, models' effective context lengths fall substantially short of their claimed context windows, with the magnitude of the gap depending on task complexity and evaluation methodology.

**Heterogeneity check:** Papers differ substantially in how they define "effective length." RULER uses a fixed 85.6% threshold based on Llama-2 at 4K (`2024-10-ruler-context-size`). NoLiMa uses 85% of each model's own base score (`2025-07-nolima-long-context-evaluation`). BABILong uses an 85% accuracy threshold without normalization (`2024-12-babilong-long-context-reasoning`). LongBench Pro uses task-specific metrics without a single effective-length definition (`2026-01-longbench-pro`). These methodological differences mean absolute effective-length numbers are not directly comparable across papers; we focus on within-paper comparisons and consistent patterns.

**Evidence table:**

| Paper | Benchmark | Model | Claimed | Effective | Ratio |
|-------|-----------|-------|---------|-----------|-------|
| `2024-10-ruler-context-size` | RULER (13 tasks) | GPT-4 | 128K | 64K | 50% |
| `2024-10-ruler-context-size` | RULER | Llama 3.1 70B | 128K | 64K | 50% |
| `2024-10-ruler-context-size` | RULER | Qwen2 72B | 128K | 32K | 25% |
| `2024-07-qwen2-technical-report` | NIAH | Qwen2 72B | 128K | 128K | 100% |
| `2024-07-qwen2-technical-report` | NeedleBench (no YARN+DCA) | Qwen2 72B | 128K | <128K | -- |
| `2024-07-qwen2-technical-report` | NeedleBench + YARN+DCA | Qwen2 72B | 128K | ~128K | ~100% |
| `2024-10-ruler-context-size` | RULER | LWM 7B | 1M | <4K | <0.4% |
| `2024-10-ruler-context-size` | RULER | Gemini 1.5 Pro | 1M | >128K | >12.8% |
| `2024-12-babilong-long-context-reasoning` | BABILong QA1 | Llama 3.1 8B | 128K | ~8K | ~6% |
| `2024-12-babilong-long-context-reasoning` | BABILong QA1 | GPT-4 | 128K | ~16K | ~12.5% |
| `2024-12-babilong-long-context-reasoning` | BABILong QA1 | Gemini 1.5 Pro | 1M | ~64K | ~6.4% |
| `2025-07-nolima-long-context-evaluation` | NoLiMa | GPT-4o | 128K | 8K | 6.3% |
| `2025-07-nolima-long-context-evaluation` | NoLiMa | Llama 3.1 70B | 128K | 2K | 1.6% |
| `2025-07-nolima-long-context-evaluation` | NoLiMa | Gemini 1.5 Pro | 2M | 2K | 0.1% |
| `2025-04-effective-context-length-falls-short` | RULER | Llama 3.1 70B | 128K | 64K | 50% |
| `2025-04-effective-context-length-falls-short` | RULER + STRING | Llama 3.1 70B | 128K | 100K | 78% |
| `2026-01-longbench-pro` | LongBench Pro | MiniMax-Text-01 | 4M | <128K | <3.2% |
| `2024-06-ada-leval-length-adaptable-benchmark` | Ada-LEval BestAnswer | GPT-4-Turbo | 128K | <32K | <25% |

**Cross-paper analysis.** The ratio of effective to claimed context ranges from 0.1% (Gemini 1.5 Pro on NoLiMa) to 78% (Llama 3.1 70B with STRING on RULER). Three factors explain the enormous variance:

First, **benchmark difficulty determines the measured gap**. Vanilla NIAH produces near-perfect scores for most models at their claimed lengths (C1 from `2024-10-ruler-context-size`), while harder benchmarks expose dramatically shorter effective lengths. Llama 3.1 70B provides a particularly instructive comparison across benchmarks: 32K effective on RULER, but only 2K on NoLiMa (`2025-07-nolima-long-context-evaluation`). This 16x discrepancy for the *same model* demonstrates that effective context length is not a fixed property of the model but a function of task demands. Qwen2 (`2024-07-qwen2-technical-report`) provides uniquely compelling within-paper evidence for the same point: Qwen2-72B achieves near-perfect NIAH at 128K, but on NeedleBench (multi-needle retrieval + reasoning) without YARN+DCA, performance drops to 73.05 at 128K and 17.13 at 256K, while LV-Eval (comprehension) drops to 31.79 at 128K and 2.88 at 256K. This within-paper comparison across three benchmarks of increasing difficulty, using the model developer's own evaluation, eliminates potential confounds from differences in evaluation methodology across papers.

Second, **model scale consistently improves the ratio but never eliminates the gap**. On RULER, GPT-4 and Llama 3.1 70B achieve 50% utilization while smaller models achieve 25% or less (`2024-10-ruler-context-size`). On LongBench Pro, Gemini 2.5 Pro shows remarkable length insensitivity (74.5 at 8K vs. 71.8 at 256K), but even this frontier model achieves only 10.68% Pass@3 on Extreme samples (`2026-01-longbench-pro`). No model in the corpus achieves full utilization of its claimed window on any task harder than vanilla NIAH.

Third, **the gap has been persistent across model generations**. From GPT-4's degradation above 73K in late 2023 (`2023-11-needle-in-a-haystack`) to MiniMax-Text-01's 4M-claimed window scoring below 128K models in early 2026 (`2026-01-longbench-pro`), the pattern of overclaimed context windows has been consistent despite substantial model improvements. The gap has *narrowed* for frontier models -- Gemini 2.5 Pro shows near-flat performance up to 256K on LongBench Pro -- but has not closed.

**Current state.** As of January 2026, the best available evidence indicates that on synthetic benchmarks with literal cues (RULER), frontier models achieve 50--80% effective utilization. On benchmarks requiring latent reasoning without surface cues (NoLiMa), effective lengths collapse to 2--8K even for models claiming 128K--2M. On realistic, human-calibrated tasks (LongBench v2, LongBench Pro), models approach human performance on short contexts (<32K) but trail on medium contexts (32K--128K), with the gap widening at extreme difficulty levels.

---

### Task type as a moderator of effective length

**Statement:** The type of task -- retrieval vs. reasoning, literal-match vs. latent-association, single-fact vs. multi-fact -- is the strongest predictor of effective context length, more so than model identity or claimed window size.

**Heterogeneity check:** Papers evaluate diverse task types, but the underlying construct they measure -- "effective context length" -- is operationalized differently. RULER focuses on retrieval and aggregation with synthetic text (`2024-10-ruler-context-size`). BABILong focuses on reasoning with embedded facts in natural text (`2024-12-babilong-long-context-reasoning`). NoLiMa isolates latent association retrieval (`2025-07-nolima-long-context-evaluation`). FlenQA controls for reasoning with padding (`2024-08-flenqa-input-length-reasoning`). LongICLBench tests in-context learning (`2025-03-longiclbench-long-in-context-learning`). Despite these differences, all papers consistently find that harder tasks produce shorter effective lengths, supporting cross-paper comparison of the *direction* of effects.

**Evidence table:**

| Paper | Task Type | Effective Length Range | Key Finding |
|-------|-----------|----------------------|-------------|
| `2023-11-needle-in-a-haystack` | Single-fact retrieval (high overlap) | 73K--200K | Near-perfect for most models |
| `2024-07-qwen2-technical-report` | NIAH vs NeedleBench vs LV-Eval | 128K (NIAH) to <128K (NeedleBench/LV-Eval) | Same model: near-perfect on NIAH, 17.13 on NeedleBench, 2.88 on LV-Eval at 256K |
| `2024-10-ruler-context-size` | Multi-task synthetic (NIAH + aggregation + VT) | 4K--128K | Near-perfect NIAH does not predict RULER; aggregation is hardest |
| `2025-07-nolima-long-context-evaluation` | Single-fact retrieval (no overlap) | 2K--8K | 16x reduction from RULER for same model |
| `2024-12-babilong-long-context-reasoning` | Multi-hop reasoning | 4K--64K | Reasoning degrades faster than retrieval |
| `2024-06-ada-leval-length-adaptable-benchmark` | Full-text comprehension (ordering, selection) | <16K | All models at random-guess by 16K on TSort |
| `2024-08-flenqa-input-length-reasoning` | Controlled reasoning (logical inference) | <3K | Degradation begins at 500 tokens |
| `2025-03-longiclbench-long-in-context-learning` | Extreme-label ICL (28--174 classes) | 7K--14K plateau | Near-zero on 174-class task for all models |

**Cross-paper analysis.** Goldman et al.'s dispersion-scope taxonomy (`2024-11-genuinely-difficult-long-context`) provides a useful organizing framework: tasks with low scope and low dispersion (vanilla NIAH, simple QA) produce the highest effective lengths, while tasks with high scope or high dispersion produce much shorter ones. This is empirically confirmed across multiple benchmark papers in the corpus.

The most striking evidence comes from the NoLiMa-RULER comparison. Modarressi et al. (`2025-07-nolima-long-context-evaluation`) showed that existing NIAH-style benchmarks contain ROUGE-1 overlap of 0.553--0.966 between questions and relevant context, while NoLiMa achieves only 0.069. When literal overlap is removed, the effective length of Llama 3.1 70B drops from 32K (RULER) to 2K (NoLiMa). This finding is consistent with Olsson et al.'s mechanistic account of induction heads (`2022-03-in-context-learning-induction-heads`), referenced by NoLiMa: attention excels at recalling repetitive patterns, which literal overlap provides for free.

Qwen2 (`2024-07-qwen2-technical-report`) offers a particularly clean demonstration of the task-type effect because the NIAH, NeedleBench, and LV-Eval results are reported within the same paper using the same models and evaluation pipeline. Qwen2-72B-Instruct scores near-perfect on NIAH at 128K (single-fact retrieval with high overlap), but without YARN+DCA, NeedleBench (which adds multi-needle retrieval and reasoning) drops to 73.05 at 128K and 17.13 at 256K, while LV-Eval (comprehension) drops to 31.79 at 128K and 2.88 at 256K. The progression from NIAH to NeedleBench to LV-Eval -- within the same model, same paper, same evaluation conditions -- mirrors the NIAH-to-RULER-to-NoLiMa progression observed across different papers, and confirms that task complexity is the dominant moderator of measured effective length. The smaller Qwen2-7B-Instruct shows an even steeper gradient: near-perfect NIAH at 128K, but NeedleBench at 38.77 (128K) and 2.92 (256K) without YARN+DCA, demonstrating the interaction between model scale and task sensitivity.

BABILong (`2024-12-babilong-long-context-reasoning`) provides complementary evidence from the reasoning dimension. On QA1 (single-fact retrieval), models maintain >85% accuracy up to 4K--64K depending on scale. On QA2 (two-fact chaining), effective lengths shrink dramatically: only GPT-4 and Gemini 1.5 Pro solve QA2 at 0K, and QA3 (three-fact chaining) pushes all models below 80% even without background text. This retrieval-to-reasoning gap confirms Goldman et al.'s prediction that adding scope or dispersion to evaluation reveals fundamentally shorter effective lengths.

FlenQA (`2024-08-flenqa-input-length-reasoning`) demonstrates the most extreme case: reasoning performance degrades from 0.92 to 0.68 at just 3K tokens -- three orders of magnitude below the claimed windows of the evaluated models. Even with duplicate padding (no irrelevant content), degradation occurs, isolating input length as the causal variable.

**Current state.** Task complexity is the dominant factor determining measured effective context length. A model's effective length on vanilla NIAH should not be cited as its effective context length; it is an upper bound that is dramatically loose for any task requiring reasoning, aggregation, or retrieval without surface cues.

---

### Causal mechanisms underlying the gap

**Statement:** The gap between claimed and effective context length arises from at least four independent mechanisms: undertrained position indices, over-squashing from causal attention topology, attention mechanism limitations with token count, and position-dependent performance bias.

**Heterogeneity check:** Papers propose different mechanistic explanations using different methodologies. An et al. (`2025-04-effective-context-length-falls-short`) use controlled pretraining and probing. Barbero et al. (`2024-12-transformers-need-glasses-over-squashing`) use theoretical analysis with gradient bounds. Du et al. (`2025-11-context-length-hurts-performance`) use controlled evaluation with attention masking. Liu et al. (`2024-02-lost-in-the-middle`) use empirical position manipulation. These methodological differences mean each paper isolates a different aspect of the mechanism; the findings are complementary rather than conflicting.

**Evidence table:**

| Paper | Proposed Mechanism | Evidence Type | Scope |
|-------|-------------------|---------------|-------|
| `2025-04-effective-context-length-falls-short` | Left-skewed position frequency distribution | Controlled pretraining + probing | Retrieval (NIAH, RULER) |
| `2024-12-transformers-need-glasses-over-squashing` | Over-squashing from causal mask topology | Theoretical (gradient bounds) | Information propagation, counting, copying |
| `2025-11-context-length-hurts-performance` | Positional distance degrades reasoning (length alone) | Whitespace padding + attention masking | Reasoning (GSM8K, MMLU, HumanEval) |
| `2024-02-lost-in-the-middle` | Position-dependent attention bias (U-shaped) | Multi-position QA experiments | Retrieval (multi-doc QA) |
| `2025-07-nolima-long-context-evaluation` | Attention overload without surface cues | Aligned-depth analysis | Latent-association retrieval |
| `2024-08-flenqa-input-length-reasoning` | Length-induced failure modes (refusals, label bias, premature answering, reduced coverage) | Behavioral analysis with statistical tests | Reasoning (logical inference) |
| `2021-08-context-features-transformer-lm` | Content words carry most usable information; word order and syntax contribute little to long-range context | V-information (training-time ablation) | Perplexity (WikiText-103) |

**Cross-paper analysis.** An et al. (`2025-04-effective-context-length-falls-short`) provide the most mechanistically grounded explanation for position-related degradation. Their key insight is that in pretraining corpora, position frequency decreases dramatically with distance: for a 2048-token window, positions i <= 1024 account for more than 80% of occurrences, while positions i >= 1536 constitute less than 5%. Controlled experiments with two TinyLlama models (2K and 4K training lengths) show that effective context length aligns with position frequency, not training window size (C2 from `2025-04-effective-context-length-falls-short`). This explains why models trained on 128K windows still have effective lengths of 32K--64K: the last 33--50% of positions are undertrained.

Barbero et al. (`2024-12-transformers-need-glasses-over-squashing`) provide a complementary theoretical explanation through the over-squashing framework adapted from graph neural networks. Their key result (Theorem 5.1) shows that the gradient of the final-token output with respect to earlier input tokens is bounded by a sum counting directed paths through the causal computation graph. Earlier tokens have combinatorially more such paths than later tokens, creating an inherent asymmetry in information flow. This explains the U-shaped retrieval curve: early tokens have an advantage from pathway abundance (exponentially more paths), while end tokens benefit from recency bias. The middle suffers from both moderate path count and lack of recency bias. Additionally, they prove that representational collapse -- where distinct input sequences produce arbitrarily close final-token representations -- occurs as sequence length increases (Theorem 4.2), exacerbated by low-precision arithmetic (bf16 causes collapse near machine precision at ~50--100 tokens for repeated sequences).

Du et al. (`2025-11-context-length-hurts-performance`) demonstrate a complementary mechanism: context length *alone* degrades problem-solving performance, independent of retrieval, distraction, and evidence-question distance. Their attention-masking experiment is particularly important -- when all distraction tokens are masked, the only difference from a short-context setting is positional distance, yet performance still drops 7.9--50% at 30K tokens (C3 from `2025-11-context-length-hurts-performance`). This finding cannot be explained solely by undertrained positions; it points to an additional mechanism whereby increased positional indices degrade reasoning capacity.

The position bias documented by Liu et al. (`2024-02-lost-in-the-middle`) represents a fourth mechanism. The U-shaped performance curve -- models attend best to information at the beginning and end of context -- has been replicated across multi-document QA, in-context learning (`2025-03-longiclbench-long-in-context-learning`), and best-answer selection (`2024-06-ada-leval-length-adaptable-benchmark`). However, NoLiMa's aligned-depth analysis (`2025-07-nolima-long-context-evaluation`) reveals an important moderation: for two-hop latent reasoning tasks, performance depends more on total context length than needle position (C5 from `2025-07-nolima-long-context-evaluation`), indicating that position bias is primarily a retrieval-related mechanism while context-length degradation affects reasoning more broadly.

FlenQA (`2024-08-flenqa-input-length-reasoning`) adds a behavioral dimension by identifying four failure modes that worsen with length: instruction non-compliance (refusals grow), label bias (toward "False"), premature answering in CoT (odds-ratio 3.643), and reduced fact coverage (odds-ratio 3.138). These failure modes suggest that length-induced degradation manifests through multiple downstream behavioral channels, consistent with multiple underlying mechanisms.

**Synthesis inference.** [Derived from `2025-04-effective-context-length-falls-short`, `2024-12-transformers-need-glasses-over-squashing`, `2025-11-context-length-hurts-performance`, `2024-02-lost-in-the-middle`, and `2025-07-nolima-long-context-evaluation`.] The evidence supports at least four independent mechanisms: (1) position frequency undertraining, which limits the model's ability to gather information from distant positions; (2) over-squashing from causal attention topology, which creates asymmetric information pathways favoring early tokens; (3) positional distance degradation of reasoning, which impairs problem-solving even when retrieval is perfect; and (4) position-dependent attention bias, which causes selective neglect of mid-context information. These mechanisms have different domains of impact -- (1) and (2) primarily affect retrieval, (3) primarily affects reasoning, and (4) affects both -- which explains why no single mitigation strategy fully closes the gap.

---

### Model scale and architecture effects

**Statement:** Larger models achieve better effective-to-claimed ratios, but the relationship is logarithmic rather than linear, and architectural choices matter as much as scale.

**Heterogeneity check:** Papers compare different model families with different architectures and training procedures. RULER evaluates within the Yi family (same training data, different sizes) (`2024-10-ruler-context-size`). Qwen2 reports results across its own model family (`2024-07-qwen2-technical-report`). NoLiMa evaluates across model families (`2025-07-nolima-long-context-evaluation`). LongBench Pro evaluates 46 models (`2026-01-longbench-pro`). The Yi comparison provides the cleanest within-family evidence; cross-family comparisons may confound scale with architecture and training differences.

**Evidence table:**

| Paper | Model Comparison | Key Finding |
|-------|-----------------|-------------|
| `2024-10-ruler-context-size` | Yi-34B vs Yi-9B vs Yi-6B (all 200K) | 34B significantly better in both absolute 4K performance and relative degradation |
| `2024-07-qwen2-technical-report` | Qwen2 family (0.5B--72B) | 0.5B/1.5B: 32K effective; 7B: 128K with YARN+DCA; 57B-A14B (MoE): 64K; 72B: 128K with YARN+DCA |
| `2024-10-ruler-context-size` | RWKV-v5, Mamba vs Transformers | Non-Transformer architectures lag by large margins |
| `2025-11-context-length-hurts-performance` | Llama 3.1 8B / Mistral 7B vs GPT-4o / Claude 3.5 / Gemini 2.0 | Closed-source models more robust but not immune; VarSum: 0% drop for GPT-4o vs -48% for Llama |
| `2025-07-nolima-long-context-evaluation` | Llama 3.1 8B/70B/405B | 8B-to-70B gap larger than 70B-to-405B gap; diminishing returns at scale |
| `2026-01-longbench-pro` | Qwen3-4B (256K) vs Qwen3-8B (128K) | Context optimization outperforms parameter scaling: 4B-256K scores 45.68 vs 8B 44.34 |
| `2025-03-longiclbench-long-in-context-learning` | Transformer vs RWKV / Mamba | Non-Transformers achieve near-zero on most ICL tasks |
| `2024-12-babilong-long-context-reasoning` | ARMT (137M) vs GPT-4 | Fine-tuned recurrent memory model processes 50M tokens, outperforming 1000x larger models |

**Cross-paper analysis.** The evidence consistently shows that larger Transformer models achieve better effective context utilization. The RULER comparison within the Yi family (C3 from `2024-10-ruler-context-size`) -- where model size is the only variable, with identical training data and context length -- provides the cleanest evidence. Du et al. (`2025-11-context-length-hurts-performance`) extend this: GPT-4o maintains perfect VarSum scores at 30K whitespace tokens where Llama 3.1 8B drops 48%.

The Qwen2 model family (`2024-07-qwen2-technical-report`) provides complementary evidence across five model sizes within a single architecture and training pipeline. The smallest models (0.5B, 1.5B) support only 32K effective context on NIAH; the 57B-A14B MoE variant supports 64K; and the 7B and 72B dense models reach 128K with YARN+DCA. However, the scale advantage is dramatically moderated by task difficulty: on NeedleBench without YARN+DCA, the 72B model scores 73.05 at 128K while the 7B model scores only 38.77 -- a 1.9x advantage for a 10x scale increase. On LV-Eval, the same comparison yields 31.79 vs 11.01 -- a 2.9x advantage but still far from the near-perfect NIAH scores both models achieve.

However, two caveats emerge from cross-paper comparison. First, the scaling benefit exhibits diminishing returns. NoLiMa (`2025-07-nolima-long-context-evaluation`) found that the 8B-to-70B improvement is larger than the 70B-to-405B improvement for the Llama 3.1 family, and even the 405B model achieves only 2K effective length on latent-association tasks. Second, LongBench Pro's finding that context-optimized smaller models can outperform larger models with shorter effective context (`2026-01-longbench-pro`, C1: Qwen3-4B-256K > Qwen3-8B) suggests that training methodology for long-context capability may matter more than raw scale.

Non-Transformer architectures (RWKV, Mamba) consistently underperform Transformer baselines on long-context tasks, despite their theoretical advantage of linear-complexity unlimited context. RULER (`2024-10-ruler-context-size`, C5), BABILong (`2024-12-babilong-long-context-reasoning`), and LongICLBench (`2025-03-longiclbench-long-in-context-learning`, C4) all report near-zero or far-below-Transformer performance. The exception is fine-tuned recurrent memory models: ARMT (`2024-12-babilong-long-context-reasoning`, C4) processes 50M tokens using only 137M parameters, outperforming GPT-4. This suggests that the architecture-scale interaction depends critically on training methodology -- off-the-shelf non-Transformer models fail, but purpose-built recurrent memory models can succeed.

**Current state.** Model scale improves effective context length, but the improvement is sublinear. Architectural innovations (recurrent memory, context-optimized training) may offer a more efficient path to closing the gap than scale alone, but this finding rests on limited evidence (one model family for context optimization, one model family for recurrent memory).

---

### Inference-time and training-time mitigations

**Statement:** Several inference-time methods partially close the effective-to-claimed gap, but no single approach eliminates it. Training-time solutions remain largely unexplored.

**Heterogeneity check:** Papers evaluate different mitigation strategies with different baselines and metrics. STRING targets position encoding (`2025-04-effective-context-length-falls-short`). YARN+DCA targets position embedding scaling (`2024-07-qwen2-technical-report`). Retrieve-then-reason targets task decomposition (`2025-11-context-length-hurts-performance`). CoT prompting targets reasoning elicitation (`2024-08-flenqa-input-length-reasoning`). ARMT targets architectural design (`2024-12-babilong-long-context-reasoning`). These approaches address different mechanisms and are measured on different benchmarks, so direct comparison of effect sizes is limited.

**Evidence table:**

| Paper | Method | Type | Best Improvement | Limitation |
|-------|--------|------|-----------------|------------|
| `2025-04-effective-context-length-falls-short` | STRING | Inference-time (position manipulation) | +15.1 points on RULER (Llama 3.1 70B at 128K); effective 64K -> 100K | RoPE-specific; does not improve reasoning tasks as much as retrieval |
| `2025-11-context-length-hurts-performance` | Retrieve-then-reason | Inference-time (pipeline) | +31.2% on GSM8K (Mistral at 26K) | Requires accurate retrieval; doubles inference cost |
| `2024-08-flenqa-input-length-reasoning` | Chain-of-thought | Inference-time (prompting) | Constant benefit; only GPT-4 shows increasing CoT benefit with length | Does not mitigate degradation trend for most models |
| `2024-07-qwen2-technical-report` | YARN + DCA | Inference-time (PE scaling + chunked attention) | NeedleBench 256K: 17.13 -> 85.21 (72B); LV-Eval 256K: 2.88 -> 42.35 (72B) | Does not fully close gap on comprehension; 7B gains smaller than 72B |
| `2025-07-longbench-v2` | YaRN (scaling factor 4.0) | Inference-time (PE scaling) | +4.7 overall (Qwen2.5-72B on LongBench v2) | Diminishes short-context performance in some settings |
| `2024-06-ada-leval-length-adaptable-benchmark` | NTK-Aware RoPE / ReRoPE | Inference-time (PE scaling) | Comparable to further-trained models on BestAnswer | All methods still collapse at ultra-long settings |
| `2024-12-babilong-long-context-reasoning` | Recurrent memory (ARMT) | Training-time (architecture) | 77% on QA1 at 50M tokens | Requires task-specific fine-tuning; sequential processing |

**Cross-paper analysis.** STRING (`2025-04-effective-context-length-falls-short`) provides the strongest evidence for an inference-time fix to the position frequency problem. By replacing undertrained tail positions with well-trained ones during inference, STRING improves Llama 3.1 70B from 66.6 to 81.7 on RULER at 128K and from 45.25 to 56.88 on InfiniteBench, surpassing GPT-4-128K on both benchmarks (C6 from `2025-04-effective-context-length-falls-short`). However, STRING's gains are concentrated on retrieval-like tasks; its improvement on RULER Aggregation (39.8 to 50.0) is smaller than on NIAH (78.9 to 92.7), consistent with the position that different degradation mechanisms affect retrieval and reasoning differently.

The retrieve-then-reason approach (`2025-11-context-length-hurts-performance`) addresses the reasoning dimension by converting long-context tasks into short-context ones. It improves Mistral's GSM8K performance from 35.5% to 66.7% at 26K tokens (C6), but requires that the model first accurately retrieve all relevant evidence -- a prerequisite that fails on harder tasks. The strategy is complementary to STRING: STRING fixes position encoding for retrieval, while retrieve-then-reason bypasses the length-reasoning degradation.

Chain-of-thought prompting (`2024-08-flenqa-input-length-reasoning`) provides roughly constant benefit across lengths rather than compensating for length-induced degradation (C6). The sole exception is GPT-4, where CoT benefit increases with length, but this model is also the least degraded overall. This finding challenges the intuition that step-by-step reasoning would help models process longer contexts, and suggests that CoT operates on a different dimension than the length-induced failure modes.

Position embedding modifications (NTK-Aware RoPE, ReRoPE, YaRN) are evaluated by multiple papers with mixed results. Ada-LEval (`2024-06-ada-leval-length-adaptable-benchmark`, C6) shows they can extend effective context beyond the training window, achieving performance comparable to models trained on longer contexts. LongBench v2 (`2025-07-longbench-v2`) confirms YaRN gains on realistic tasks. The Qwen2 Technical Report (`2024-07-qwen2-technical-report`) provides the most detailed YARN evaluation from a model developer, showing that YARN+DCA dramatically improves NeedleBench scores (72B: 17.13 to 85.21 at 256K; 7B: 2.92 to 60.71 at 256K) and LV-Eval scores (72B: 2.88 to 42.35 at 256K). Notably, the improvement is much larger for the 72B model than the 7B model on both benchmarks, suggesting that PE scaling methods interact positively with model scale. However, even with YARN+DCA, the 72B model's LV-Eval score of 42.35 at 256K remains far below its NIAH performance, confirming that PE modifications do not fully resolve the comprehension gap. BABILong (`2024-12-babilong-long-context-reasoning`, C5) reports that YaRN "fails to extend effective context despite stable perplexity" on reasoning tasks, and RULER (`2024-10-ruler-context-size`) reports that training on longer sequences does not always improve performance (C4: LWM-1M is worse than LWM-512K at 256K). The reconciliation is that position embedding modifications help retrieval and multi-needle tasks substantially (as Qwen2's NeedleBench results show) but provide diminishing returns on comprehension tasks (as Qwen2's LV-Eval results and BABILong's reasoning results confirm).

**Current state.** No single mitigation fully closes the effective-to-claimed gap. STRING partially addresses the position frequency mechanism. Retrieve-then-reason partially addresses reasoning degradation but depends on retrieval accuracy. PE modifications partially address extrapolation but fail on reasoning tasks. Training-time solutions (balanced position distributions, position-aware curriculum learning) remain speculative -- An et al. (`2025-04-effective-context-length-falls-short`) explicitly note that adjusting position frequency during training may require data similar to the original pretraining corpus to preserve reasoning ability.

---

## Consensus and Disagreements

### Consensus

**Claim:** Most LLMs effectively utilize substantially less than their claimed context window.
**Supporting papers:** `2024-10-ruler-context-size`, `2024-12-babilong-long-context-reasoning`, `2025-04-effective-context-length-falls-short`, `2025-07-nolima-long-context-evaluation`, `2024-07-qwen2-technical-report`, `2026-01-longbench-pro`, `2024-06-ada-leval-length-adaptable-benchmark`.
**Evidence strength:** strong (7 papers with diverse methodologies, covering 50+ models, consistent findings; Qwen2's model-developer-reported NIAH-vs-NeedleBench-vs-LV-Eval comparison provides particularly credible within-paper evidence).
**Qualification:** The magnitude of the gap is benchmark-dependent. On easy benchmarks (vanilla NIAH), most models approach full utilization. The consensus applies to any evaluation harder than single-fact retrieval with high lexical overlap.

**Claim:** Context length alone degrades reasoning, independent of retrieval and distraction.
**Supporting papers:** `2024-08-flenqa-input-length-reasoning`, `2025-11-context-length-hurts-performance`.
**Evidence strength:** strong (two independent papers with systematic controls; FlenQA shows degradation with duplicate padding; Du et al. show degradation with attention-masked distractors).
**Qualification:** The magnitude of the degradation varies by model scale. Closed-source models are more robust but not immune (C5 from `2025-11-context-length-hurts-performance`).

**Claim:** Perplexity is an unreliable proxy for long-context capability.
**Supporting papers:** `2024-08-flenqa-input-length-reasoning`, `2024-12-babilong-long-context-reasoning`.
**Evidence strength:** moderate (two papers with consistent findings; FlenQA shows rho = -0.95 anti-correlation; BABILong shows YaRN has stable perplexity but fails on reasoning tasks).
**Qualification:** FlenQA's correlation is based on four models; broader validation is needed.

**Claim:** Literal lexical overlap inflates effective context length measurements.
**Supporting papers:** `2025-07-nolima-long-context-evaluation`, `2024-10-ruler-context-size`, `2024-11-genuinely-difficult-long-context`.
**Evidence strength:** strong (NoLiMa's ROUGE analysis quantifies overlap in 8 benchmarks; the 16x gap between RULER and NoLiMa effective lengths for the same model is large and consistent).
**Qualification:** NoLiMa tests only one type of non-literal association (geographic/semantic links); generalizability to other association types is unvalidated.

**Claim:** Multiple independent mechanisms contribute to context-length degradation.
**Supporting papers:** `2025-04-effective-context-length-falls-short`, `2024-12-transformers-need-glasses-over-squashing`, `2024-02-lost-in-the-middle`, `2025-11-context-length-hurts-performance`.
**Evidence strength:** moderate (four papers with complementary theoretical and empirical approaches; mechanisms are distinct but their relative contributions are not quantified).
**Qualification:** The interaction between mechanisms is not well understood; different mechanisms may dominate for different task types.

### Active Disagreements

**Claim:** Whether position bias or context length per se is the primary bottleneck.
**Position A (`2024-02-lost-in-the-middle`, `2024-06-ada-leval-length-adaptable-benchmark`):** Position bias is the dominant factor. The U-shaped curve shows that even at moderate lengths, mid-context information is inaccessible. Mitigating position bias (via recalibration or position manipulation) should recover most lost performance.
**Position B (`2025-11-context-length-hurts-performance`, `2025-07-nolima-long-context-evaluation`):** Context length itself independently degrades performance. Du et al. show degradation persists even with evidence at optimal positions (beginning) and with attention-masked distractors. NoLiMa shows that in two-hop tasks, context length dominates over position.
**Methodological differences:** Position A papers use empirical position manipulation without controlling for length. Position B papers use controlled experiments isolating length from position (attention masking, aligned-depth analysis).
**Assessment:** Both factors contribute independently, but their relative importance depends on the task. For retrieval tasks with literal cues, position bias is the larger factor. For reasoning tasks or tasks without literal cues, context length is the larger factor. Position B is better supported by more controlled experimental evidence (attention masking, aligned-depth analysis).
**Resolution path:** A unified evaluation that systematically varies both position and length on the same tasks with matched methodology would quantify relative contributions.

---

## Methodological Patterns

### Common experimental setups

Models are most frequently evaluated at 7--8B parameter scale (Llama 3.1 8B, Mistral 7B appear in 10+ of 20 papers) and at 70B+ scale (Llama 3.1 70B, GPT-4/4o appear in 12+ papers). Context lengths of 4K--128K dominate evaluation; only BABILong (`2024-12-babilong-long-context-reasoning`) and LongBench Pro (`2026-01-longbench-pro`) evaluate beyond 128K on realistic tasks. The most common evaluation framework is vLLM with greedy decoding on A100 GPUs.

### Methodological strengths

The best papers in the corpus employ systematic controls to isolate variables. Du et al. (`2025-11-context-length-hurts-performance`) use three distraction conditions (essay, whitespace, attention masking) and position manipulation to isolate length effects. FlenQA (`2024-08-flenqa-input-length-reasoning`) uses duplicate padding to separate length from distraction. NoLiMa (`2025-07-nolima-long-context-evaluation`) uses ROUGE analysis to quantify the literal-overlap confound. Barbero et al. (`2024-12-transformers-need-glasses-over-squashing`) provide rigorous theoretical bounds connecting architecture to information flow limitations. These papers set the methodological standard for the field.

### Methodological weaknesses

1. **No variance estimates.** Du et al. (`2025-11-context-length-hurts-performance`) run all experiments once with no variance estimates. Several other papers report only mean accuracy without confidence intervals.
2. **Narrow model coverage.** Most papers evaluate 2--5 open-source models at 7B scale and 1--3 closed-source APIs. The interaction between model scale, architecture, and task type is poorly explored.
3. **Inconsistent effective-length definitions.** RULER uses a fixed 85.6% threshold (Llama 2 at 4K), while NoLiMa uses 85% of each model's base score. These definitions are not comparable and produce different rankings.
4. **Limited realistic evaluation.** Most papers use synthetic or semi-synthetic tasks. LongBench v2 and LongBench Pro are the only corpus papers with fully human-annotated realistic evaluation, but they are limited to 503 and 1500 questions respectively.
5. **Theoretical analysis limited to simplified models.** Barbero et al. (`2024-12-transformers-need-glasses-over-squashing`) prove results for pre-LN Transformers with simplifying assumptions about layer normalization and attention weights; generalization to real models is not formally established.

### Benchmark coverage matrix

| Paper | NIAH | RULER | BABILong | NoLiMa | LongBench | InfiniteBench | FlenQA | Ada-LEval | Realistic QA |
|-------|------|-------|----------|--------|-----------|---------------|--------|-----------|-------------|
| `2024-10-ruler-context-size` | x | x | | | | | | | x |
| `2024-12-babilong-long-context-reasoning` | x | x | x | | | | | | |
| `2025-04-effective-context-length-falls-short` | x | x | | | | x | | | |
| `2025-07-nolima-long-context-evaluation` | x | x | x | x | | x | | | |
| `2025-11-context-length-hurts-performance` | | x | | | | | | | x |
| `2024-08-flenqa-input-length-reasoning` | | | | | | | x | | |
| `2024-06-ada-leval-length-adaptable-benchmark` | | | | | x | | | x | |
| `2025-07-longbench-v2` | | | | | | | | | x |
| `2026-01-longbench-pro` | | | | | | | | | x |
| `2024-02-lost-in-the-middle` | | | | | | | | | x |
| `2025-03-longiclbench-long-in-context-learning` | | | | | | | | | x |
| `2024-12-transformers-need-glasses-over-squashing` | | | | | | | | | |

---

## Gaps and Open Questions

1. **No unified effective-length measurement methodology.**
   **Description:** Each paper defines effective length differently (fixed threshold, relative threshold, percent of claimed length), making cross-benchmark comparisons unreliable.
   **Severity:** high.
   **Potential approach:** A standardized evaluation suite that reports effective lengths under multiple definitions (retrieval, reasoning, latent reasoning) on the same models.
   **Related open questions:** RULER's open question on position controlling; NoLiMa's open question on downstream task translation.

2. **Training-time fixes for position frequency are unexplored.**
   **Description:** An et al. (`2025-04-effective-context-length-falls-short`) explicitly note that adjusting position frequency during training is left as future work, with the caveat that it may require data similar to the original pretraining corpus. No paper in the corpus tests whether position-balanced training closes the gap.
   **Severity:** high.
   **Potential approach:** Controlled pretraining experiments with uniform or balanced position frequency distributions, measuring the trade-off between effective length and reasoning quality.
   **Related open questions:** An et al.'s Q1 and Q2; Du et al.'s Q2.

3. **Post-training position frequency effects are unknown.**
   **Description:** SFT and RLHF stages use predominantly short-context data, which may further skew position frequencies. The interaction between pretraining and post-training distributions is unexplored.
   **Severity:** high.
   **Potential approach:** Analysis of position frequency distributions in common SFT/RLHF datasets; controlled experiments varying post-training data length distributions.
   **Related open questions:** An et al.'s Q2.

4. **Generation tasks are poorly evaluated.**
   **Description:** The corpus focuses on retrieval, QA, and classification. Summarization, translation, and long-form generation tasks are absent from controlled evaluations of effective context length.
   **Severity:** medium.
   **Potential approach:** Extending FlenQA or NoLiMa methodology to generation tasks with controlled length variation.
   **Related open questions:** Goldman et al.'s Q2 on high-scope high-dispersion benchmark design.

5. **Chain-of-thought interaction with length degradation is poorly characterized.**
   **Description:** FlenQA finds CoT provides constant rather than compensatory benefit, and only GPT-4 shows increasing CoT benefit. LongBench Pro finds thinking prompts hurt instruct models. The interaction between reasoning strategies and context length is not well understood.
   **Severity:** medium.
   **Potential approach:** Systematic evaluation of multiple reasoning strategies (CoT, step-by-step, self-consistency) across length conditions on controlled benchmarks.
   **Related open questions:** LongBench v2's Q1 on inference-time compute vs. context length.

6. **Non-RoPE architectures are under-evaluated.**
   **Description:** STRING is designed for RoPE; its applicability to ALiBi, T5-bias, or absolute positional encodings is unknown. Most non-Transformer architectures (RWKV, Mamba) fail on standard evaluations, but purpose-built recurrent memory models succeed.
   **Severity:** medium.
   **Potential approach:** Extending position frequency analysis to non-RoPE encodings; evaluating purpose-built long-context architectures on the same benchmarks.
   **Related open questions:** An et al.'s Q3; NoLiMa's Q1.

7. **Interaction between over-squashing and other mechanisms is unexplored.**
   **Description:** Barbero et al. (`2024-12-transformers-need-glasses-over-squashing`) provide theoretical bounds on information flow, but the connection to position frequency undertraining and attention masking experiments is not established.
   **Severity:** medium.
   **Potential approach:** Experiments measuring gradient sensitivity at different positions and comparing to empirical performance degradation; testing whether STRING or other mitigations affect the theoretical pathway counts.
   **Related open questions:** Barbero et al.'s Q1 on architectural modifications.
