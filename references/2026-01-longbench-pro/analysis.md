---
title: "LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark"
authors: "Chen, Wu, Jia, Gao, Fu, Zhang, Hu"
year: 2026
venue: "arXiv:2601.02872"
paper_type: preprint
categories: ["benchmarking", "long-context-evaluation", "reasoning-evaluation"]
scope:
  - "English and Chinese long-context evaluation with 8K-256K input lengths"
  - "46 representative long-context LLMs under standardized thinking/non-thinking prompts"
benchmarks_used: ["longbench-pro", "longbench", "longbench-v2", "ruler", "infinitebench", "scrolls", "zeroscrolls", "l-eval", "ada-leval", "helmet"]
models_introduced: []
models_evaluated: ["gemini-2.5-pro", "gemini-2.5-flash", "gpt-5", "gpt-4o", "deepseek-v3.2", "deepseek-r1", "qwen3-235b-a22b", "qwen3-30b-a3b", "qwen3-32b", "qwen3-8b", "qwen3-4b", "qwen2.5-72b", "kimi-k2-instruct", "minimax-m2", "ministral-3-14b", "ministral-3-8b", "ministral-3-3b", "llama-3.1-405b", "llama-3.1-70b", "llama-3.1-8b", "gemma-3-27b", "gemma-3-12b", "gemma-3-4b"]
key_claims:
  - id: C1
    claim: "Long-context optimization can outperform parameter scaling for long-context benchmarks"
    evidence: "Table 3, Section 5.2"
    status: supported
    scope: "Qwen3 family comparisons on LongBench Pro under standardized evaluation settings"
    magnitude: "Qwen3-4B-Instruct-2507 (45.68) > Qwen3-8B (44.34); Qwen3-30B-A3B-Instruct-2507 (54.52) > Qwen3-32B (51.12)"
  - id: C2
    claim: "Claimed context length is often larger than effective context capability"
    evidence: "Section 5.2 and Table 4"
    status: supported
    scope: "Cross-model comparison on LongBench Pro, including truncation stress test for GLM-4.6"
    magnitude: "MiniMax-Text-01 (4M claimed) scores 45.00 overall; GLM-4.6 drops from 34.14 to 2.55 on 256K samples when truncation moves from 120K to 190K"
  - id: C3
    claim: "Long-context performance remains cross-lingually misaligned between English and Chinese"
    evidence: "Table 3, Section 5.2"
    status: supported
    scope: "EN/ZH score splits across 46 models and multiple model families"
    magnitude: "Systematic EN-vs-ZH asymmetry by family (e.g., GPT/Claude/Llama stronger in EN, GLM/Kimi/MiniMax stronger in ZH)"
  - id: C4
    claim: "Extreme-difficulty samples reveal larger open-vs-closed capability gaps than easy samples"
    evidence: "Table 3, Section 5.2"
    status: supported
    scope: "Difficulty-tier analysis on LongBench Pro"
    magnitude: "Easy gap is near-zero for top models (GPT-5 85.23 vs DeepSeek-V3.2 85.02), while Extreme gap is much larger (Gemini-2.5-Pro 50.77 vs DeepSeek-V3.2 44.27)"
  - id: C5
    claim: "Thinking gains are substantial mainly for models with native reasoning training"
    evidence: "Table 3, Section 5.2"
    status: supported
    scope: "Thinking vs non-thinking comparisons across mixed, thinking, and instruct model groups"
    magnitude: "Claude-4-Sonnet +13.80 and DeepSeek-V3.2 +16.15, while Gemma-3-12B-It -0.24 and Llama-3.1-8B-Instruct -1.03 under prompted thinking"
  - id: C6
    claim: "Mixed-thinking models provide a practical Pareto trade-off between fast response and deep reasoning"
    evidence: "Section 5.2"
    status: supported
    scope: "Models supporting both non-thinking and thinking modes on the same benchmark"
    magnitude: "DeepSeek-V3.2 reaches 67.82 (thinking) while retaining 51.67 non-thinking baseline; Gemini-2.5-Flash rises from 55.92 to 67.41"
  - id: C7
    claim: "Human-model collaborative sample construction improves quality over human-only or model-only strategies"
    evidence: "Section 5.7, Figure 10"
    status: supported
    scope: "50-document controlled comparison of three construction strategies with 3-expert scoring"
    magnitude: "Quality 0.9609 +/- 0.0415 vs 0.9484 +/- 0.0450 (human-only) and 0.8964 +/- 0.0536 (model-only); Fleiss' Kappa = 0.76"
cross_references:
  - target: 2024-08-longbench-bilingual-benchmark
    type: extends
    detail: "LongBench Pro extends LongBench with larger task taxonomy, longer context range, and explicit context/length/difficulty dimensions"
  - target: 2025-07-longbench-v2
    type: extends
    detail: "Extends LongBench v2 by adding bilingual EN/ZH coverage and broader metric/task diversity"
  - target: 2024-10-ruler-context-size
    type: complementary
    detail: "Contrasts synthetic controllability in RULER with fully natural-document realism in LongBench Pro"
  - target: 2022-12-scrolls-long-language-sequences
    type: complementary
    detail: "Builds on SCROLLS-style long-document evaluation but adds modern long-context LLM difficulty calibration"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: complementary
    detail: "Shares zero/few-shot long-document focus while expanding language and task taxonomy"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Empirically echoes the gap between advertised and effective long-context behavior"
  - target: 2025-04-effective-context-length-falls-short
    type: complementary
    detail: "Provides benchmark-level empirical confirmation of effective-vs-claimed context mismatch"
  - target: 2022-12-chain-of-thought-prompting
    type: complementary
    detail: "Uses non-thinking versus thinking prompt templates directly inspired by chain-of-thought framing"
  - target: 2024-08-infinitebench-long-context-evaluation
    type: complementary
    detail: "Complements InfinityBench by focusing on fully natural bilingual tasks with calibrated difficulty"
  - target: 2024-08-l-eval-standardized-evaluation
    type: complementary
    detail: "Shares protocol-standardization goals and references L-Eval as prior evaluation methodology"
  - target: 2024-06-ada-leval-length-adaptable-benchmark
    type: complementary
    detail: "Related to length-adaptable evaluation methodology; LongBench Pro adds broader realistic task coverage"
open_questions:
  - question: "Will context-optimization-first continue to dominate as model scale and architecture families change?"
    addressed_by: null
  - question: "How can collaborative construction be scaled beyond 256K while preserving expert-level verification quality?"
    addressed_by: null
  - question: "Can mixed-thinking remain Pareto-optimal if native-thinking training improves substantially?"
    addressed_by: null
  - question: "Can recursive Critique-of-Critique reliably reduce verification cost without lowering annotation fidelity?"
    addressed_by: null
---

# LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark

**Authors:** Ziyang Chen, Xing Wu, Junlong Jia, Chaochen Gao, Qi Fu, Debing Zhang, Songlin Hu  
**Date:** January 2026, arXiv:2601.02872  
**Type:** arXiv preprint (not yet peer-reviewed)

---

## Core Research Problem

Existing long-context benchmarks are split between **controllable but synthetic** evaluation (for example, RULER, HELMET) and **realistic but expensive** human-heavy construction (for example, LongBench v2, CLongEval). The paper argues this creates a practical gap: benchmark design has not kept pace with rapidly growing context windows and model reasoning complexity.

The technical challenge is to build a benchmark that is simultaneously:
- realistic (natural documents),
- broad (many task types and capability dimensions),
- scalable (cost-feasible construction), and
- diagnostically fine-grained (length, context dependency, difficulty).

**Core challenge:** how to evaluate genuine long-context understanding at scale without collapsing either realism or annotation quality.

---

## Problem Solutions

The proposed solution is **LongBench Pro**, defined by three coupled design choices:

1. **Broader benchmark taxonomy:** 11 primary tasks and 25 secondary tasks, bilingual EN/ZH coverage, and contexts from 8K to 256K.
2. **Multi-dimensional labeling:** each sample is tagged by context requirement (Full/Partial), length bucket (6 levels), and model-calibrated difficulty (Easy/Moderate/Hard/Extreme).
3. **Human-model collaborative construction:** frontier models draft candidate samples, while human annotators and experts verify, repair, and calibrate difficulty.

This design targets higher ecological validity than purely synthetic setups, while retaining operational throughput beyond purely manual pipelines.

---

## Approach Details

### Method

LongBench Pro composes a fixed grid over:
- 25 secondary tasks,
- 2 languages,
- 6 lengths,
- 5 samples per cell,

yielding 1,500 samples.

For summarization tasks, score uses the paper's exact formula:

> \(\text{Score}_{summary} = 0.5 \cdot \max_i \text{SemSim}(S_{gen}, S_{ref_i}) + 0.5 \cdot \max_i \text{ROUGE-L}(S_{gen}, S_{ref_i})\)

where each sample has 3 references and the max over references is used for each component metric.

### Key Technical Components

- **Context requirement axis:** distinguishes local retrieval-oriented tasks (Partial) from dispersed-evidence integration (Full).
- **Model-centric difficulty calibration:** three model tiers (high/mid/low) produce progressive boundaries for Extreme/Hard/Moderate/Easy.
- **Prompt dualization:** every item has non-thinking and thinking templates with rigid output schema (`[Answer]` marker + line-by-line elements).
- **Verification workflow:** two annotator review plus expert adjudication for disputed or low-confidence samples.

### Experimental Setup

- **Model pool:** 46 long-context models across closed/open ecosystems, from small instruct models to frontier mixed/thinking systems.
- **Evaluation protocol:** multiple runs per sample, with average performance plus Best-of-N and Pass@N upper bounds.
- **Length handling:** middle truncation when required; thinking output budgets adjusted by model context capacity.
- **Reproducibility:** per-model inference parameters, truncation lengths, and temperatures are documented in Appendix D (Table 5).

Evidence breadth note: this is one of the broadest model-coverage evaluations in the repository, but statistical uncertainty intervals are not reported for most leaderboard comparisons (moderate evidence breadth for comparative ranking, limited for variance-sensitive claims).

### Key Results

| Setting | Proposed / Highlighted Result | Best/Relevant Baseline Comparison |
|---|---|---|
| Context optimization vs scale | Qwen3-4B-256K = 45.68 | Qwen3-8B = 44.34 |
| Context optimization vs scale | Qwen3-30B-A3B-256K = 54.52 | Qwen3-32B = 51.12 |
| Claimed vs effective context | MiniMax-Text-01 (4M claimed) = 45.00 | Below many 128K models |
| Truncation stability test | GLM-4.6 at 256K: 34.14 (120K trunc.) vs 2.55 (190K trunc.) | Indicates instability near claimed window |
| Top overall score | Gemini-2.5-Pro = 73.42 | GPT-5 = 72.61, Claude-4-Sonnet = 69.87 |
| Construction quality | Collaborative = 0.9609 +/- 0.0415 | Human-only 0.9484 +/- 0.0450; model-only 0.8964 +/- 0.0536 |

Additional takeaways:
- Full-context tasks are consistently harder than Partial tasks (7.32-10.84 point drop).
- Extreme difficulty remains unsaturated (Gemini-2.5-Pro Pass@3 on Extreme = 10.68).
- Thinking gains are architecture/training dependent rather than universally prompt-induced.

---

## Limitations and Failure Modes

Author-acknowledged limitations:
- Context length coverage ends at 256K despite some evaluated models advertising 1M+.
- Difficulty calibration is model-dependent and can drift as model quality improves.
- Collaborative construction can still face verification cost/accuracy tension at higher complexity.

Observed failure modes from reported results:
- Full-context integration remains weaker than localized retrieval for all model families tested.
- Consistency-oriented tasks (for example, contradiction/compliance and long-horizon dialogue tracking) remain comparatively weak.
- Several instruct models receive negligible or negative benefit from thinking prompts.

**[Inferred]** Potential benchmark-construction coupling bias: top frontier models are used both in sample generation and later evaluation, which may introduce subtle alignment effects even with expert review.

### Scope and Comparability

- **What was not tested:** contexts beyond 256K for the core benchmark; multilingual coverage beyond EN/ZH; controlled causal manipulations of isolated length effects within the same natural document.
- **Comparability notes:** unlike synthetic length-controlled benchmarks (for example, RULER), LongBench Pro uses naturally occurring texts and multi-dimensional tagging; this improves realism but weakens direct causal attribution of length-only effects across papers.

---

## Conclusions

### Contributions

1. **Comprehensive bilingual benchmark design.** LongBench Pro contributes a 1,500-sample EN/ZH benchmark spanning 11 primary tasks, 25 secondary tasks, and three explicit analysis dimensions (context requirement, length, difficulty).
2. **Scalable quality-oriented construction process.** The human-model collaborative pipeline achieves the best measured quality among compared strategies while controlling annotation cost growth.
3. **Large-scale empirical characterization.** Evaluation over 46 models identifies consistent modern long-context patterns: effective-vs-claimed gaps, cross-lingual asymmetry, and mode-dependent reasoning gains.

### Implications

1. **Context optimization can dominate raw scaling** in practical long-context performance regimes tested here.
2. **Advertised context windows are insufficient evidence** of usable long-context reasoning capability.
3. **Reasoning mode is a training property, not only a prompt property,** as shown by weak/negative prompted-thinking gains in many instruct models.
4. **Mixed-thinking architecture is currently a strong deployment compromise,** but this remains contingent on future training paradigms.

---

## Key Claims

1. **C1 (supported): Context optimization can outperform parameter scaling.** Evidence: Qwen3-4B-256K (45.68) > Qwen3-8B (44.34), and Qwen3-30B-A3B-256K (54.52) > Qwen3-32B (51.12) (Table 3, Section 5.2). Scope: Qwen3-family comparisons on this benchmark. Magnitude: +1.34 and +3.40 in the cited pairs.

2. **C2 (supported): Claimed context length diverges from effective capability.** Evidence: MiniMax-Text-01 (4M claimed) scores 45.00 overall; GLM-4.6 drops to 2.55 at 256K under 190K truncation but 34.14 under 120K truncation (Section 5.2, Table 4). Scope: benchmark-level and truncation-stress settings. Magnitude: 31.59-point collapse in GLM-4.6 256K case.

3. **C3 (supported): Cross-lingual long-context behavior is asymmetric.** Evidence: family-level EN/ZH skew patterns in Table 3 (Section 5.2). Scope: 46-model EN/ZH split reporting. Magnitude: directionally consistent family skew, with stronger frontier models showing narrower gaps.

4. **C4 (supported): Extreme difficulty better separates model tiers than Easy difficulty.** Evidence: near parity on Easy between top open/closed models (85.23 vs 85.02) but larger spread on Extreme (50.77 vs 44.27) (Table 3). Scope: LongBench Pro difficulty stratification. Magnitude: 6.50-point lead at Extreme in cited example.

5. **C5 (supported): Native reasoning training matters for thinking gains.** Evidence: Claude-4-Sonnet +13.80 and DeepSeek-V3.2 +16.15 versus Gemma-3-12B-It -0.24 and Llama-3.1-8B-Instruct -1.03 (Table 3, Section 5.2). Scope: mixed/thinking/instruct comparisons under benchmark prompts. Magnitude: positive double-digit gains for some models versus negative deltas for others.

6. **C6 (supported): Mixed-thinking models provide Pareto-like behavior.** Evidence: Gemini-2.5-Flash and DeepSeek-V3.2 maintain non-thinking baselines while improving significantly in thinking mode (Section 5.2). Scope: dual-mode models with both scores reported. Magnitude: Gemini-2.5-Flash +11.49; DeepSeek-V3.2 +16.15.

7. **C7 (supported): Collaborative construction improves quality.** Evidence: quality 0.9609 +/- 0.0415 versus 0.9484 +/- 0.0450 (human-only) and 0.8964 +/- 0.0536 (model-only), with Fleiss' Kappa 0.76 (Section 5.7, Figure 10). Scope: 50-document comparative construction experiment. Magnitude: +0.0125 vs human-only and +0.0645 vs model-only.

---

## Open Questions

1. Will context-optimization-first trends hold beyond the model families and training recipes tested in this paper?
2. Can collaborative construction remain quality-stable beyond 256K when verification complexity grows further?
3. Will mixed-thinking remain Pareto-optimal if native-thinking training continues to improve rapidly?
4. Can recursive Critique-of-Critique pipelines reduce verification cost without introducing systematic annotation drift?

---

## Core References and Why They Are Referenced

### Benchmark Lineage

- **Bai et al. (2023)** -- *LongBench.* Direct benchmark predecessor; defines early bilingual long-context multi-task framing.
- **Bai et al. (2025)** -- *LongBench v2.* Immediate predecessor emphasizing more difficult realistic long-context reasoning.

### Long-Context Evaluation Methodology

- **Hsieh et al. (2024)** -- *RULER.* Synthetic controllable long-context stress-testing baseline used for contrast.
- **Yen et al. (2024)** -- *HELMET.* Methodology-focused benchmark framing comprehensive evaluation criteria.
- **Zhang et al. (2024)** -- *InfinityBench.* Mixed synthetic/natural long-context benchmark for >100K evaluation.
- **An et al. (2023)** -- *L-Eval.* Standardized long-context protocol foundation.
- **Wang et al. (2024)** -- *Ada-L-Eval.* Length-adaptable extension of standardized long-context evaluation.
- **Shaham et al. (2022; 2023)** -- *SCROLLS / ZeroSCROLLS.* Long-document benchmark suites used as prior realistic baselines.

### Model and Reasoning Context

- **Comanici et al. (2025)** -- *Gemini 2.5.* Top-tier long-context model used in both drafting and evaluation.
- **OpenAI (2025)** -- *GPT-5.* Frontier reasoning model benchmarked as near-top performer.
- **Liu et al. (2025)** -- *DeepSeek-V3.2.* Strong open-model mixed-thinking reference point.
- **Yang et al. (2025)** -- *Qwen3 Technical Report.* Family used for scale-vs-context optimization comparisons.
- **Wei et al. (2022)** -- *Chain-of-Thought Prompting.* Conceptual basis for non-thinking versus thinking prompt protocol.
- **Liu et al. (2023)** -- *Lost in the Middle.* Prior evidence for effective-length limitations discussed in relation to LongBench Pro findings.
