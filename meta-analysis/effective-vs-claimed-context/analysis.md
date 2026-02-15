---
title: "The Gap Between Claimed and Effective Context Length in Large Language Models"
research_question: "How large is the gap between claimed and effective context lengths, and what factors predict degradation?"
thesis_objective: "Produce thesis-ready synthesis for related work and analysis sections on effective context evaluation and mechanistic explanations of long-context failure."
date_produced: 2026-02-13
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
  - 2025-04-helmet-long-context-evaluation
  - 2025-07-longbench-v2
  - 2025-07-nolima-long-context-evaluation
  - 2025-11-context-length-hurts-performance
  - 2026-01-longbench-pro
corpus_search_strategy: |
  category long-context-evaluation
  category benchmarking
  category position-bias
  category attention-analysis
  category mechanistic-interpretability
  text "effective context"
  text "claimed context"
  text "length degradation"
  text "position frequency"
  text "literal overlap"
inclusion_criteria:
  - "Papers reporting explicit effective-vs-claimed context evidence (benchmark or model-level)."
  - "Papers with controlled experiments isolating length-related degradation mechanisms."
  - "Papers providing mechanistic or theoretical explanations relevant to effective context limits."
exclusion_criteria:
  - "Architecture-only papers with no direct evidence on effective-vs-claimed context behavior."
  - "Model reports without concrete long-context evaluation details."
categories: ["long-context-evaluation", "benchmarking", "position-bias", "attention-analysis"]
themes:
  - id: magnitude-and-persistence
    label: "Magnitude and persistence of the effective-vs-claimed gap"
  - id: task-and-benchmark-dependence
    label: "Task and benchmark dependence of effective length"
  - id: causal-mechanisms
    label: "Causal mechanisms behind degradation"
  - id: scale-and-architecture
    label: "Model scale and architecture effects"
  - id: mitigation-methods
    label: "Mitigation methods and their limits"
consensus_claims:
  - claim: "Effective context is typically much smaller than claimed context, and this gap persists across model generations."
    sources: ["2024-10-ruler-context-size", "2024-12-babilong-long-context-reasoning", "2025-07-nolima-long-context-evaluation", "2026-01-longbench-pro"]
    strength: strong
  - claim: "Length alone can degrade reasoning even when retrieval and distractor access are controlled."
    sources: ["2024-08-flenqa-input-length-reasoning", "2025-11-context-length-hurts-performance"]
    strength: strong
  - claim: "Measured effective length is strongly task- and benchmark-dependent, not a single model constant."
    sources: ["2024-07-qwen2-technical-report", "2024-10-ruler-context-size", "2025-07-nolima-long-context-evaluation", "2025-03-longiclbench-long-in-context-learning"]
    strength: strong
  - claim: "Literal overlap inflates NIAH-style scores and can mask latent reasoning failures."
    sources: ["2025-07-nolima-long-context-evaluation", "2024-08-infinitebench-long-context-evaluation", "2025-04-helmet-long-context-evaluation"]
    strength: strong
  - claim: "Perplexity and next-token metrics are insufficient proxies for effective long-context reasoning."
    sources: ["2021-11-long-range-models-use-context", "2024-08-flenqa-input-length-reasoning", "2024-12-babilong-long-context-reasoning"]
    strength: strong
  - claim: "Multiple mechanisms jointly contribute to the gap (position-frequency undertraining, over-squashing/topology effects, and position/length interaction)."
    sources: ["2025-04-effective-context-length-falls-short", "2024-12-transformers-need-glasses-over-squashing", "2024-02-lost-in-the-middle", "2025-11-context-length-hurts-performance"]
    strength: moderate
contested_claims:
  - claim: "Whether position bias or pure context length is the dominant bottleneck."
    for: ["2024-02-lost-in-the-middle", "2024-06-ada-leval-length-adaptable-benchmark"]
    against: ["2025-11-context-length-hurts-performance", "2025-07-nolima-long-context-evaluation"]
    resolution: "Both are active contributors; evidence indicates position effects dominate some retrieval settings, while length-alone degradation appears in controlled reasoning settings."
    resolved: true
  - claim: "Whether lost-in-the-middle behavior remains universal at 100K+ lengths."
    for: ["2024-02-lost-in-the-middle"]
    against: ["2024-08-infinitebench-long-context-evaluation", "2025-07-nolima-long-context-evaluation"]
    resolution: "At larger lengths, position effects become more task- and model-specific; no universal pattern is confirmed."
    resolved: true
evaluation_validity_summary:
  construct_validity: "moderate: effective-length definitions vary (fixed thresholds, relative thresholds, category scores)."
  causal_validity: "moderate: a few high-quality controlled studies exist, but much evidence is still observational."
  external_validity: "moderate: realistic benchmarks confirm persistence, but with weaker causal attribution."
mechanistic_evidence_summary:
  interventional_papers: ["2024-08-flenqa-input-length-reasoning", "2025-11-context-length-hurts-performance", "2025-07-nolima-long-context-evaluation", "2025-04-effective-context-length-falls-short"]
  observational_papers: ["2023-11-needle-in-a-haystack", "2024-02-lost-in-the-middle", "2024-08-infinitebench-long-context-evaluation", "2024-10-ruler-context-size", "2026-01-longbench-pro"]
  theoretical_papers: ["2024-12-transformers-need-glasses-over-squashing", "2024-11-genuinely-difficult-long-context"]
thesis_mapping:
  literature_review:
    - claim: "Reported context windows substantially overstate practical long-context capability on harder tasks."
      sources: ["2024-10-ruler-context-size", "2024-12-babilong-long-context-reasoning", "2025-07-nolima-long-context-evaluation", "2026-01-longbench-pro"]
    - claim: "The field moved from measuring the gap to isolating causes through confound-aware designs."
      sources: ["2023-11-needle-in-a-haystack", "2024-08-flenqa-input-length-reasoning", "2025-11-context-length-hurts-performance", "2025-04-effective-context-length-falls-short"]
  analysis_section:
    - claim: "Method evaluation should report a portfolio of task types and confound controls rather than a single effective-length number."
      sources: ["2024-10-ruler-context-size", "2025-04-helmet-long-context-evaluation", "2025-07-nolima-long-context-evaluation"]
      uncertainty: "No standardized cross-benchmark aggregation method currently exists."
    - claim: "Mitigation gains are meaningful but mechanism-specific; no single method closes the gap across retrieval, reasoning, and generation."
      sources: ["2025-04-effective-context-length-falls-short", "2025-11-context-length-hurts-performance", "2024-07-qwen2-technical-report", "2024-12-babilong-long-context-reasoning"]
      uncertainty: "Cross-method comparisons are limited by heterogeneous benchmarks."
gaps:
  - description: "No unified and broadly accepted definition of effective context length across benchmark families."
    severity: high
  - description: "Training-time mitigation of position-frequency imbalance remains under-tested."
    severity: high
  - description: "Post-training stages (SFT/RLHF) and their effect on effective context are weakly characterized."
    severity: high
  - description: "Controlled evaluations for long-context generation remain sparse compared to retrieval/QA."
    severity: medium
  - description: "Interactions between over-squashing theory and empirical mitigation methods are not yet quantified."
    severity: medium
overall_confidence:
  - conclusion: "The effective-vs-claimed context gap is substantial, persistent, and benchmark-sensitive."
    level: high
    basis: "Consistent evidence across synthetic, controlled, and realistic benchmarks."
    caveats: ["Absolute magnitudes depend on benchmark design and threshold definitions."]
  - conclusion: "Length-induced degradation has at least one component independent of retrieval failure."
    level: high
    basis: "Independent controlled findings from duplicate-padding and attention-masking setups."
    caveats: ["Controlled evidence currently concentrates on limited task families."]
  - conclusion: "Mechanistic explanations are converging but not fully integrated into one quantitative model."
    level: moderate
    basis: "Complementary empirical and theoretical work points to multiple interacting causes."
    caveats: ["Relative contribution of mechanisms remains unresolved."]
---

# The Gap Between Claimed and Effective Context Length in Large Language Models

**Research question:** How large is the gap between claimed and effective context lengths, and what factors predict degradation?
**Thesis objective:** Produce thesis-ready synthesis for related work and analysis sections on effective context evaluation and mechanistic explanations of long-context failure.
**Corpus:** 21 papers, 2018-2026.
**Categories:** long-context-evaluation, benchmarking, position-bias, attention-analysis.

---

## Executive Summary

- Effective context is substantially lower than claimed context across benchmark families (`2024-10-ruler-context-size`, `2024-12-babilong-long-context-reasoning`, `2025-07-nolima-long-context-evaluation`, `2026-01-longbench-pro`).
- RULER shows that although all 17 tested models claimed 32K+ windows, only about half met the 32K threshold criterion; effective lengths ranged from under 4K to over 128K (`2024-10-ruler-context-size`).
- BABILong reports that popular models often use only about 10-20% of claimed context on QA1 (`2024-12-babilong-long-context-reasoning`).
- NoLiMa shows that at 32K, 11 of 13 models fall below 50% of base score; Llama 3.1 70B shifts from 32K effective length on RULER to 2K on NoLiMa (`2025-07-nolima-long-context-evaluation`, `2024-10-ruler-context-size`).
- Controlled evidence indicates a length-only effect: FLenQA drops from 0.92 to 0.68 by 3K tokens, and attention-masked settings still show at least 7.9% degradation at 30K (`2024-08-flenqa-input-length-reasoning`, `2025-11-context-length-hurts-performance`).
- Qwen2 within-paper comparisons show extreme benchmark sensitivity: at 256K, Qwen2-72B-Instruct reports NeedleBench 17.13 and LV-Eval 2.88 without YARN+DCA, improving to 85.21 and 42.35 with YARN+DCA (`2024-07-qwen2-technical-report`).
- LongBench Pro confirms ongoing claimed-vs-effective divergence in newer models (for example, MiniMax-Text-01 with 4M claim scores 45.00; GLM-4.6 drops from 34.14 to 2.55 in truncation stress at 256K) (`2026-01-longbench-pro`).
- Mitigations improve parts of the problem but do not remove the gap: STRING improves Llama 3.1 70B by 15.1 points on RULER-128K, while retrieve-then-reason yields up to 31.2% on GSM8K (`2025-04-effective-context-length-falls-short`, `2025-11-context-length-hurts-performance`).

---

## Thesis-Ready Outputs

### For Literature Review (Related Work)

The literature converges on a robust empirical pattern: claimed context windows overstate usable context on tasks requiring more than shallow retrieval. This pattern appears in synthetic suites (`2024-10-ruler-context-size`), reasoning-in-haystack benchmarks (`2024-12-babilong-long-context-reasoning`), overlap-controlled evaluations (`2025-07-nolima-long-context-evaluation`), and realistic long-document evaluation (`2026-01-longbench-pro`).

A second trend is methodological: work shifts from descriptive gap measurement (NIAH-era diagnostics) to confound-isolating designs and mechanism-oriented explanations (`2024-08-flenqa-input-length-reasoning`, `2025-11-context-length-hurts-performance`, `2025-04-effective-context-length-falls-short`, `2024-12-transformers-need-glasses-over-squashing`).

### For Analysis/Discussion

For thesis analysis, effective context should be reported as task-conditional and benchmark-conditional, not as a single model trait. At minimum, model claims should be triangulated across high-overlap retrieval tests, low-overlap latent reasoning tests, and realistic downstream suites (`2024-10-ruler-context-size`, `2025-07-nolima-long-context-evaluation`, `2026-01-longbench-pro`).

Mechanistic interpretation should also be plural: current evidence supports interacting causes (position-frequency imbalance, position bias, topological compression limits, and length-induced reasoning degradation), which explains why single-mitigation methods only partially recover performance (`2025-04-effective-context-length-falls-short`, `2024-12-transformers-need-glasses-over-squashing`, `2025-11-context-length-hurts-performance`).

---

## Temporal Evolution

| Year-Month | Paper | Key Contribution | Shift |
|---|---|---|---|
| 2018-07 | `2018-07-sharp-nearby-fuzzy-far-away` | Early effective-context framing in LMs | Established gap between nominal context and usable context |
| 2021-11 | `2021-11-long-range-models-use-context` | Perplexity gains plateau despite longer context access | Questioned perplexity as long-context proxy |
| 2023-11 | `2023-11-needle-in-a-haystack` | Popularized depth x length retrieval diagnostics | Standardized claimed-vs-observed window testing |
| 2024-02 | `2024-02-lost-in-the-middle` | U-shaped position effect in multi-doc QA | Position bias became central to interpretation |
| 2024-10 | `2024-10-ruler-context-size` | Multi-task synthetic effective-length benchmark | Showed NIAH saturation is insufficient evidence |
| 2024-12 | `2024-12-babilong-long-context-reasoning` | Reasoning-in-haystack at scale | Quantified retrieval-reasoning gap growth with length |
| 2025-04 | `2025-04-effective-context-length-falls-short` | Position-frequency mechanism + STRING | Shift from measurement to mechanistic mitigation |
| 2025-07 | `2025-07-nolima-long-context-evaluation` | Literal-overlap confound quantified | Exposed lexical shortcut inflation directly |
| 2025-11 | `2025-11-context-length-hurts-performance` | Attention-masking controls | Isolated length-only degradation component |
| 2026-01 | `2026-01-longbench-pro` | Large realistic bilingual benchmark | Confirmed gap persists in newer model cohorts |

**Synthesis inference:** The field trajectory is from capacity claims to capability diagnostics, then toward causal decomposition of failure sources.

---

## Thematic Synthesis

### Theme 1: Magnitude and Persistence of the Gap

**Statement:** Effective context remains substantially below claimed context for many model-task combinations.

**Heterogeneity check:** Effective length thresholds vary across papers, so absolute values are not fully comparable (`2024-10-ruler-context-size`, `2025-07-nolima-long-context-evaluation`, `2026-01-longbench-pro`).

| Evidence | Verified observation |
|---|---|
| `2024-10-ruler-context-size` | All 17 models claim 32K+, only about half pass at 32K; effective lengths span under 4K to over 128K |
| `2024-12-babilong-long-context-reasoning` | Popular models effectively use about 10-20% of claimed context on QA1 |
| `2025-07-nolima-long-context-evaluation` | At 32K, 11/13 models are below 50% of base score |
| `2026-01-longbench-pro` | MiniMax-Text-01 (4M claim) scores 45.00; GLM-4.6 truncation stress: 34.14 to 2.55 at 256K |

**Current state:** The gap remains material in 2026 and is not explained by older-model artifacts.

### Theme 2: Task and Benchmark Dependence

**Statement:** Effective length is highly task-dependent; retrieval-friendly settings can overstate broader capability.

**Heterogeneity check:** Benchmarks differ in overlap, task composition, and metric definitions.

| Model/context evidence | Contrast |
|---|---|
| `2024-07-qwen2-technical-report` | Qwen2-72B: near-perfect NIAH at 128K, but NeedleBench/LV-Eval degrade strongly at 256K without YARN+DCA |
| `2025-07-nolima-long-context-evaluation` + `2024-10-ruler-context-size` | Llama 3.1 70B: 32K effective on RULER vs 2K on NoLiMa |
| `2025-03-longiclbench-long-in-context-learning` | Open models often plateau around 7K-14K and near-zero on Discovery (174 classes), except Gemini 1.5 Pro at 14% |

**Current state:** Any single benchmark estimate should be treated as a conditional upper or lower bound, not a universal effective-context number.

### Theme 3: Causal Mechanisms Behind Degradation

**Statement:** The gap reflects multiple mechanisms rather than a single failure mode.

**Heterogeneity check:** Mechanistic papers use different evidence classes: controlled interventions, formal theory, and observational diagnostics.

| Mechanism | Papers | Evidence |
|---|---|---|
| Position-frequency undertraining | `2025-04-effective-context-length-falls-short` | controlled analysis + intervention (STRING) |
| Position-dependent retrieval bias | `2024-02-lost-in-the-middle`, `2024-06-ada-leval-length-adaptable-benchmark` | controlled positional manipulations |
| Topological over-squashing / representational collapse | `2024-12-transformers-need-glasses-over-squashing` | formal theoretical results + empirical checks |
| Length-alone reasoning degradation | `2024-08-flenqa-input-length-reasoning`, `2025-11-context-length-hurts-performance` | duplicate padding and attention masking controls |

**Synthesis inference:** No single mechanism explains all observed failure patterns across retrieval, reasoning, and ICL tasks.

### Theme 4: Model Scale and Architecture Effects

**Statement:** Scale helps but does not remove the gap; architecture/training choices can dominate parameter count.

**Heterogeneity check:** Cross-family comparisons conflate scale and training recipe.

| Evidence | Observation |
|---|---|
| `2024-10-ruler-context-size` | Within Yi family, larger models show better long-context robustness |
| `2025-11-context-length-hurts-performance` | Closed-source models are more robust on average but still degrade |
| `2026-01-longbench-pro` | Context optimization can beat size scaling within Qwen3 comparisons |
| `2025-03-longiclbench-long-in-context-learning` | Non-Transformer baselines (RWKV/Mamba) underperform strongly on extreme-label ICL |

**Current state:** Scale provides partial gains; effective-context behavior remains bottlenecked by training/evaluation regime and mechanism-specific weaknesses.

### Theme 5: Mitigation Methods and Their Limits

**Statement:** Mitigations produce meaningful but partial recovery.

**Heterogeneity check:** Methods target different failure sources and are evaluated on different tasks.

| Method | Evidence | Limit |
|---|---|---|
| STRING (`2025-04-effective-context-length-falls-short`) | +15.1 on RULER-128K for Llama 3.1 70B; +30.9 for Qwen2 72B | primarily addresses position-index issue; task-transfer limits remain |
| Retrieve-then-reason (`2025-11-context-length-hurts-performance`) | up to +31.2% on GSM8K | depends on retrieval stage quality and pipeline overhead |
| YARN + DCA (`2024-07-qwen2-technical-report`) | large 256K gains (NeedleBench 17.13 to 85.21; LV-Eval 2.88 to 42.35) | large residual gap remains on difficult comprehension tasks |
| Prompting-only adjustments (`2024-08-flenqa-input-length-reasoning`) | CoT helps but does not remove degradation trend for most models | does not address core length bottleneck |

**Current state:** Combined interventions are promising, but no method yet yields stable near-claimed performance across all long-context task types.

---

## Consensus and Active Disagreements

### Consensus

**Claim:** Claimed context and effective context diverge substantially.
**Supporting papers:** `2024-10-ruler-context-size`, `2024-12-babilong-long-context-reasoning`, `2025-07-nolima-long-context-evaluation`, `2026-01-longbench-pro`
**Evidence strength:** strong
**Qualification:** Magnitude depends on benchmark and threshold definition.

**Claim:** Length can degrade reasoning independently of distractor quality.
**Supporting papers:** `2024-08-flenqa-input-length-reasoning`, `2025-11-context-length-hurts-performance`
**Evidence strength:** strong
**Qualification:** Strongest evidence comes from controlled tasks; broader task transfer still needs study.

**Claim:** Benchmark shortcut effects (especially overlap) materially bias effective-length estimates.
**Supporting papers:** `2025-07-nolima-long-context-evaluation`, `2024-08-infinitebench-long-context-evaluation`, `2025-04-helmet-long-context-evaluation`
**Evidence strength:** strong
**Qualification:** Most directly validated for retrieval-like tasks.

### Active Disagreements

**Claim:** Dominant bottleneck: position bias or pure length?
**Position A:** Position bias dominates many failures (`2024-02-lost-in-the-middle`, `2024-06-ada-leval-length-adaptable-benchmark`).
**Position B:** Length-alone degradation remains after controls (`2025-11-context-length-hurts-performance`, `2025-07-nolima-long-context-evaluation`).
**Methodological differences:** positional manipulations versus explicit distractor/access controls.
**Assessment:** best-supported view is interaction: both mechanisms are real, and dominance is task-dependent.
**Resolution path:** unified experiments varying depth and length with overlap/noise controls in one protocol.

---

## Effective Context Evaluation Validity Audit

### Construct Validity

| Paper | Effective-context construct |
|---|---|
| `2024-10-ruler-context-size` | thresholded multi-task synthetic performance (85.6 baseline reference) |
| `2024-12-babilong-long-context-reasoning` | thresholded reasoning-in-haystack performance |
| `2025-07-nolima-long-context-evaluation` | threshold relative to per-model base score |
| `2026-01-longbench-pro` | realistic multi-task performance across length/difficulty/context labels |

Construct definitions are useful but not harmonized.

### Confound Audit

| Confound | Evidence |
|---|---|
| literal overlap | quantified directly in NoLiMa across prior benchmarks |
| task-difficulty/length entanglement | highlighted in LongBench v2/Pro and taxonomy work |
| metric mismatch (capability vs proxy) | shown in FLenQA, BABILong, and L-Eval-like analyses |

### Causal Evidence Ladder

| Level | Description | Papers |
|---|---|---|
| A | direct isolation experiments | `2024-08-flenqa-input-length-reasoning`, `2025-11-context-length-hurts-performance`, `2025-07-nolima-long-context-evaluation` |
| B | controlled but mixed-factor benchmark studies | `2024-10-ruler-context-size`, `2024-12-babilong-long-context-reasoning`, `2024-06-ada-leval-length-adaptable-benchmark` |
| C | observational cross-benchmark/model reporting | `2023-11-needle-in-a-haystack`, `2024-08-infinitebench-long-context-evaluation`, `2026-01-longbench-pro` |

### External Validity Judgment

- Realistic benchmark evidence (`2025-07-longbench-v2`, `2026-01-longbench-pro`) confirms persistence of the gap.
- Controlled causal studies provide strongest attribution but limited domain breadth.
- Best-practice interpretation requires combining both.

---

## Mechanistic Interpretability Evidence Synthesis

| Mechanism | Papers | Evidence type | Causal strength | Explains | Open limits |
|---|---|---|---|---|---|
| Position-frequency undertraining | `2025-04-effective-context-length-falls-short` | controlled probing + intervention | high | why tail positions are weakly utilized | training-time correction evidence is sparse |
| Over-squashing / representational collapse | `2024-12-transformers-need-glasses-over-squashing` | formal theory + empirical support | moderate-high | topology-linked information bottlenecks | quantitative linkage to benchmark-level gains |
| Position bias (U-shaped) | `2024-02-lost-in-the-middle`, `2024-06-ada-leval-length-adaptable-benchmark` | controlled position tests | moderate | depth-sensitive retrieval failures | universality at 100K+ is disputed |
| Length-alone degradation | `2024-08-flenqa-input-length-reasoning`, `2025-11-context-length-hurts-performance` | interventional controls | high | failure beyond retrieval/access confounds | internal circuit-level mechanism unspecified |
| Overlap shortcut reliance | `2025-07-nolima-long-context-evaluation` | direct overlap ablations | high | inflated NIAH-like success under lexical cues | generalization to all task families |

**Synthesis inference:** Mechanistic evidence supports multi-cause degradation, making single-cause mitigation unlikely to generalize.

---

## Methodological Patterns

### Common Experimental Setups

- Frequent model coverage: 7B-70B open-source plus selected API models.
- Frequent length ranges: 4K-128K, with fewer strong evaluations beyond 128K.
- Common protocol choices: greedy decoding and benchmark-specific thresholds.

### Recurring Strengths

- Confound-isolating designs in FLenQA and Du et al. provide high causal value.
- Cross-benchmark overlap analysis in NoLiMa improves interpretability.
- Mechanistic-plus-intervention coupling in STRING strengthens causal claims.

### Recurring Weaknesses

- Inconsistent effective-length definitions prevent clean meta-comparison.
- Limited uncertainty reporting and limited cross-paper normalization.
- Controlled generation-focused effective-context evaluation remains weaker than retrieval/QA coverage.

### Benchmark Coverage Snapshot

| Paper | NIAH | RULER | BABILong | NoLiMa | LongBench family | Controlled causal tests |
|---|---|---|---|---|---|---|
| `2024-10-ruler-context-size` | x | x | | | | |
| `2024-12-babilong-long-context-reasoning` | x | x | x | | | |
| `2025-07-nolima-long-context-evaluation` | x | x | x | x | | x |
| `2024-08-flenqa-input-length-reasoning` | | | | | | x |
| `2025-11-context-length-hurts-performance` | | x | | | | x |
| `2026-01-longbench-pro` | | | | | x | |

---

## Gaps and Open Questions

1. **Unified effective-length definition (high):** no standardized cross-benchmark definition is widely adopted.
   **Minimal next evidence:** report all major evaluations under a shared multi-definition protocol.

2. **Training-time mechanism mitigation (high):** position-frequency balancing is proposed but under-tested.
   **Minimal next evidence:** controlled pretraining/post-training interventions with matched downstream evaluation.

3. **Post-training effects (high):** SFT/RLHF positional distributions and their impact on effective context are under-characterized.
   **Minimal next evidence:** dataset-position audits plus ablation runs on post-training length distributions.

4. **Generation-focused effective context (medium):** output-length studies exist but do not yet close evaluation coverage.
   **Minimal next evidence:** controlled long-generation benchmarks with robust reasoning and factuality scoring.

5. **Mechanism integration (medium):** no quantitative decomposition allocates variance to each mechanism.
   **Minimal next evidence:** joint studies combining controlled manipulations with mechanistic probes and theory-linked predictions.
