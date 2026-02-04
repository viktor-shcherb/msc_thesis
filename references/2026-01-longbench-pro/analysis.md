---
title: "LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark"
authors: "Chen, Wu, Jia, Gao, Fu, Zhang, Hu"
year: 2026
venue: "arXiv:2601.02872"
paper_type: "preprint"
categories: ["benchmarking", "long-context-evaluation"]
scope: ["bilingual long-context evaluation", "1500 samples", "up to 256K tokens"]
benchmarks_used: ["longbench-pro"]
models_introduced: []
models_evaluated: ["llama-3.1-8b", "llama-3.1-70b"]
key_claims:
  - id: C1
    claim: "Long-context optimization outperforms parameter scaling: Qwen3-4B-Instruct-2507 (256K) scores 45.68, surpassing Qwen3-8B (44.34); Qwen3-30B-A3B-Instruct-2507 (256K) scores 54.52, outperforming Qwen3-32B (51.12)"
    evidence: "Table 3, Section 5.2 finding (1)"
    status: supported
  - id: C2
    claim: "Claimed context length does not equal effective context length: MiniMax-Text-01 (4M claimed) scores only 45.00, below most 128K models; GLM-4.6 (198K claimed) drops from 34.14 to 2.55 at 256K when truncation length is raised from 120K to 190K"
    evidence: "Table 3, Table 4, Section 5.2 finding (2)"
    status: supported
  - id: C3
    claim: "Cross-lingual performance is misaligned: GPT/Claude/Mistral/Llama series perform better in English; GLM/Kimi/MiniMax perform better in Chinese; stronger models narrow this gap"
    evidence: "Table 3, Section 5.2 finding (3)"
    status: supported
  - id: C4
    claim: "Extreme difficulty reveals true capability gaps: on Easy samples the gap between open-source and closed-source is minimal (GPT-5 85.23 vs DeepSeek-V3.2 85.02), but on Extreme it widens (Gemini-2.5-Pro 50.77 vs DeepSeek-V3.2 44.27)"
    evidence: "Table 3, Section 5.2 finding (4)"
    status: supported
  - id: C5
    claim: "Native thinking training is essential for long-context gains; instruct models show limited or negative gains from thinking prompts (Llama-3.1-405B +0.59, Gemma-3-12B-It -0.24, Llama-3.1-8B -1.03)"
    evidence: "Table 3, Section 5.2 finding (6)"
    status: supported
  - id: C6
    claim: "Mixed-thinking models achieve Pareto optimality between fast response and deep reasoning: Gemini-2.5-Flash approaches Gemini-2.5-Pro in thinking mode; DeepSeek-V3.2 significantly outperforms DeepSeek-R1 in thinking mode"
    evidence: "Table 3, Section 5.2 finding (7)"
    status: supported
  - id: C7
    claim: "Human-model collaborative construction achieves highest sample quality (0.9609 +/- 0.0415), outperforming human-only (0.9484 +/- 0.0450) and model-only (0.8964 +/- 0.0536) strategies"
    evidence: "Section 5.7, Figure 10"
    status: supported
cross_references:
  - target: 2024-08-longbench-bilingual-benchmark
    type: extends
    detail: "Direct successor to LongBench with broader task coverage (11 vs 6 primary tasks) and multi-dimensional categorization"
  - target: 2025-07-longbench-v2
    type: extends
    detail: "Extends LongBench v2 with bilingual coverage (EN+ZH vs EN only), diverse metrics (vs single metric), and fine-grained categorization"
  - target: 2024-10-ruler-context-size
    type: complementary
    detail: "Explicitly compares against RULER, noting its synthetic-only text and 4-task limitation; LongBench Pro covers all RULER capability dimensions"
  - target: 2022-12-scrolls-long-language-sequences
    type: complementary
    detail: "References SCROLLS as an early effort in long-context evaluation"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: complementary
    detail: "References ZeroSCROLLS as an early effort in long-context evaluation"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Cites Lost in the Middle as foundational work on the gap between advertised and effective context length"
  - target: 2025-04-effective-context-length-falls-short
    type: complementary
    detail: "Both address claimed vs effective context length from complementary perspectives"
  - target: 2022-12-chain-of-thought-prompting
    type: complementary
    detail: "LongBench Pro's thinking/non-thinking prompt design is inspired by chain-of-thought prompting"
  - target: 2024-08-infinitebench-long-context-evaluation
    type: complementary
    detail: "Compares against InfiniteBench in Table 1 as a mixed synthetic/natural benchmark; LongBench Pro uses fully natural text with broader task and language coverage"
  - target: 2024-08-l-eval-standardized-evaluation
    type: complementary
    detail: "References L-Eval as a standardized evaluation protocol in the broader long-context evaluation landscape"
  - target: 2024-06-ada-leval-length-adaptable-benchmark
    type: complementary
    detail: "References Ada-LEval as a length-adaptable extension of standardized evaluation"
open_questions:
  - question: "Will the context-optimization-first paradigm hold as models scale beyond current parameter counts?"
    addressed_by: null
  - question: "How can human-model collaborative construction scale beyond 256K while maintaining verification accuracy?"
    addressed_by: null
  - question: "Will mixed-thinking models remain Pareto-optimal as dedicated thinking models improve?"
    addressed_by: null
  - question: "Can recursive critique schemes (Critique-of-Critique) resolve the verification-efficiency tension at extreme lengths?"
    addressed_by: null
---
# LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark

**Authors:** Ziyang Chen, Xing Wu, Junlong Jia, Chaochen Gao, Qi Fu, Debing Zhang, Songlin Hu (Institute of Information Engineering, Chinese Academy of Sciences; University of Chinese Academy of Sciences; Beihang University; Xiaohongshu Inc.)
**Date:** January 2026, arXiv:2601.02872

**Type:** arXiv preprint (not yet peer-reviewed)

Note: Earlier versions of this benchmark series -- LongBench (Bai et al., 2023) at ACL 2024 and LongBench v2 (Bai et al., 2025) at ACL 2025 -- were peer-reviewed. LongBench Pro has not yet been accepted at a venue.

---

## Core Research Problem

The rapid expansion of context length in LLMs -- now reaching 1M tokens for models like Gemini-2.5-Pro (Comanici et al., 2025) -- has outpaced existing evaluation benchmarks. Current long-context benchmarks face a fundamental trade-off between scalability and realism:

- **Synthetic benchmarks** (RULER (Hsieh et al., 2024), HELMET (Yen et al., 2024)) enable controlled evaluation at arbitrary lengths but underrepresent the semantic complexity of real-world long-context scenarios. RULER, for example, covers only 4 task categories and uses fully synthetic text.
- **Manually annotated benchmarks** (LongBench v2 (Bai et al., 2025), CLongEval (Qiu et al., 2024)) ensure authenticity through realistic tasks but are prohibitively expensive and cognitively demanding to scale to extreme lengths (128K--256K tokens) and diverse task coverage.
- **Existing benchmarks lack multi-dimensional categorization.** Most benchmarks do not simultaneously categorize samples by context requirement (full vs. partial), length (fine-grained buckets), and difficulty (model-calibrated levels), limiting the granularity of analysis.
- **Language coverage is narrow.** RULER, HELMET, and LongBench v2 are English-only; CLongEval is Chinese-only. No existing benchmark provides fine-grained bilingual coverage with diverse metrics.

**The core challenge is how to construct a realistic, comprehensive, bilingual long-context benchmark that supports fine-grained multi-dimensional analysis while balancing annotation quality with scalability to extreme context lengths.**

---

## Problem Solutions

LongBench Pro addresses this challenge through a benchmark of 1,500 naturally occurring bilingual samples and a novel construction methodology:

1. **Comprehensive task taxonomy.** 11 primary tasks and 25 secondary tasks covering the full spectrum of long-context capabilities assessed by all existing benchmarks, with diverse task-specific evaluation metrics.
2. **Multi-dimensional categorization.** Each sample is tagged along three orthogonal dimensions: context requirement (Full vs. Partial), length (six levels from 8K to 256K), and difficulty (four model-calibrated levels from Easy to Extreme).
3. **Human-Model Collaborative Construction.** A pipeline where frontier LLMs draft candidate questions, reference answers, design rationales, and solution processes from authentic documents, while human experts rigorously verify correctness, filter flawed samples, and calibrate difficulty. This achieves higher quality than either purely human or purely model annotation at moderate cost.

---

## Approach Details

### Method

LongBench Pro is organized around a two-level task taxonomy. The 11 primary task categories are crossed with an orthogonal **context requirement** dimension:

- **Full:** solving the task requires integrating evidence dispersed across multiple, distant spans of the document (emphasizing integration and reasoning).
- **Partial:** solving the task primarily relies on localized spans (emphasizing localization and retrieval).

This crossing produces 25 secondary task categories. Each sample is further assigned to one of six **length buckets** (8K/16K/32K/64K/128K/256K tokens, measured by the Qwen tokenizer, with a tolerance of +/-20%) and one of four **difficulty levels** (Easy, Moderate, Hard, Extreme), calibrated by model performance.

The benchmark contains exactly 5 samples for each combination of 25 secondary tasks x 2 languages x 6 length buckets = 1,500 samples total.

### Key Technical Components

**Task taxonomy (Table 2).** The 11 primary tasks and their metrics:

| Primary Task | Description | Metrics |
|---|---|---|
| T1 Retrieval & Ranking | Retrieve content and rank most relevant first | NDCG@k |
| T2 Sequencing & Structure Reconstruction | Restore timeline or logical order | Pairwise Accuracy |
| T3 Evidence-Grounded QA | Answer fact/reasoning questions based on evidence | Accuracy |
| T4 Summarization & Synthesis | Generate abstract summary under constraints | SemSim, ROUGE-L |
| T5 Attribution & Citation Alignment | Bind correct sources to generated text | F1 |
| T6 Aggregation & Clustering | Cluster and output statistics/examples/sort | SubEM, F1, Pairwise Accuracy |
| T7 Consistency & Compliance Checking | Detect and locate contradictions/violations | F1 |
| T8 Structured & Numeric Reasoning | Numerical calculations in structured text | SubEM |
| T9 Version & Code Diff Analysis | Compare changes in different text/code versions | F1 |
| T10 Rule Induction & In-Context Learning | Summarize rules and make decisions on new samples | SubEM |
| T11 Dialogue Memory & Long-Horizon Tracking | Track and respond to dialogue history | Accuracy |

**Summarization scoring formula.** For T4, the final score combines semantic similarity and lexical overlap:

> Score_summary = 0.5 * max_i SemSim(S_gen, S_ref_i) + 0.5 * max_i ROUGE-L(S_gen, S_ref_i)

Each summarization sample includes three reference summaries; the maximum across references is taken for each metric.

**Human-Model Collaborative Construction pipeline.** The construction proceeds in five stages:

1. **Document Collection.** Naturally occurring long documents curated from the public internet across diverse domains (news, medicine, science, literature, law, education) and formats (reports, tables, code, dialogues, lists, JSON). Documents are balanced across single-document and multi-document settings, English and Chinese, and six length buckets. All documents undergo a compliance review to exclude privacy-sensitive, copyrighted, or non-compliant content.

2. **Human-Model Collaborative Sample Generation.** Five frontier LLMs (Gemini-2.5-Pro, GPT-5, Claude-4-Sonnet, DeepSeek-V3.2, Qwen3-235B-A22B-Thinking-2507) each draft three candidate samples per document aligned with a target task definition and context requirement, including: (i) questions, (ii) reference answers, (iii) design rationales, and (iv) solution processes. Human annotators then critically evaluate: task alignment (via design rationale), answer correctness (via solution process), difficulty (a sample is challenging if at least one model answers incorrectly), and select the best qualifying sample or move to the next document. Each accepted sample is reviewed by a long-context expert; failed cases are revised until they satisfy the criteria.

3. **Question Standardization.** Two standardized prompt templates are constructed for each question: a non-thinking prompt (direct answer) and a thinking prompt (explicit step-by-step reasoning before the answer). Both follow a uniform format with an "[Answer]" identifier for automated extraction and evaluation.

4. **Answer Review.** Five advanced models generate predictions for each sample. Two annotators independently verify each component of the original answer (ensuring precision) and check model predictions for missing components (ensuring recall). Samples without issues are included directly; disputed samples go to a long-context expert for final judgment.

5. **Difficulty Classification.** Models are ranked by overall performance and partitioned into three tiers (high/mid/low), with five representative models per tier selected for diverse architecture coverage:
   - **High-performing:** Gemini-2.5-Pro, GPT-5, Claude-4-Sonnet, DeepSeek-V3.2, Qwen3-235B-A22B-Thinking-2507
   - **Mid-performing:** GLM-4.6, DeepSeek-V3-0324, Kimi-K2-Instruct-0905, Qwen3-30B-A3B-Instruct-2507, MiniMax-M2
   - **Low-performing:** Ministral-3-8B-Instruct-2512, Qwen3-8B, Qwen2.5-72B-Instruct, Llama-3.1-405B-Instruct, Gemma-3-27B-It

   Difficulty levels are defined progressively:
   - **Extreme:** at most one high-performing model answers correctly (score > 0.65 for summarization)
   - **Hard:** after excluding Extreme, at most one mid-performing model answers correctly
   - **Moderate:** after excluding Hard, at most one low-performing model answers correctly
   - **Easy:** remaining samples

**Quality validation.** An audit of 300 uniformly sampled samples yields 99.3% attribute correctness (language, length, task, context requirement all correct) and 97.3% answer correctness, with problematic samples impacting overall score by only 0.96 points (Section 4).

**Construction strategy comparison.** The human-model collaborative strategy achieves the highest average quality score (0.9609 +/- 0.0415) across five dimensions, outperforming human-only (0.9484 +/- 0.0450) and model-only (0.8964 +/- 0.0536). Fleiss' Kappa among three expert evaluators is 0.76 (high agreement). Time cost increases slowly with sample length for the collaborative strategy, compared to exponential growth for human-only (Section 5.7, Figure 10).

### Experimental Setup

- **Models:** 46 long-context LLMs spanning closed-source (e.g., GPT-5, Gemini-2.5-Pro) and open-source (e.g., GPT-OSS-120B), thinking (e.g., DeepSeek-R1), mixed-thinking (e.g., DeepSeek-V3.2, Claude-4-Sonnet), and non-thinking (instruct) modes, sizes from 3B to 1T parameters, dense and MoE architectures, and context lengths from 128K to 4M.
- **Inference:** Each model's default inference parameters; temperature set to 1.0 when no default exists. Inference run three times per sample. Both general performance (average across runs) and upper-bound performance (Best-of-N, Pass@N) are reported.
- **Output length:** 32K for thinking scores on models supporting 256K context; 8K for other models' thinking scores. 1K for all non-thinking scores.
- **Truncation:** When sample length exceeds model context length, text is truncated from the middle to (context length minus output length). DeepSeek-V3.2, GLM-4.6, and MiniMax-M2 use a truncation length of 120K to reserve sufficient thinking space (Appendix E).
- **Default reporting:** Thinking scores are reported unless otherwise specified.

### Key Results

**General performance (Table 3, top models by overall thinking score):**

| Model | Type | Context Length | Overall | English | Chinese | Extreme | Hard | Moderate | Easy |
|---|---|---|---|---|---|---|---|---|---|
| Gemini-2.5-Pro | Thinking | 1M | 73.42 | 72.35 | 74.49 | 50.77 | 81.03 | 81.98 | 84.40 |
| GPT-5 | Thinking | 272K | 72.61 | 73.24 | 71.97 | 48.37 | 78.74 | 82.31 | 85.23 |
| Claude-4-Sonnet | Mixed | 1M | 69.87 | 71.09 | 68.65 | 47.05 | 74.72 | 76.58 | 83.78 |
| DeepSeek-V3.2 | Mixed | 160K | 67.82 | 67.89 | 67.75 | 44.27 | 67.73 | 75.08 | 85.02 |
| Qwen3-235B-A22B-Thinking-2507 | Thinking | 256K | 66.97 | 66.83 | 67.12 | 43.39 | 67.10 | 75.12 | 83.55 |
| GLM-4.6 | Mixed | 198K | 58.21 | 56.50 | 59.92 | 38.88 | 48.92 | 60.95 | 79.78 |
| Kimi-K2-Instruct-0905 | Instruct | 256K | 55.53 | 56.96 | 54.10 | 38.25 | 43.75 | 57.33 | 77.29 |
| Ministral-3-14B-Instruct-2512 | Instruct | 256K | 45.80 | 47.75 | 43.85 | 31.66 | 37.48 | 39.35 | 67.56 |
| Llama-3.1-405B-Instruct | Instruct | 128K | 40.66 | 44.46 | 36.86 | 29.81 | 34.09 | 29.22 | 61.36 |

Key findings from the evaluation:

- **(1) Long-context optimization outperforms parameter scaling.** Qwen3-4B-Instruct-2507 (256K) scores 45.68, surpassing Qwen3-8B (44.34). Qwen3-30B-A3B-Instruct-2507 (256K) attains 54.52, outperforming the larger Qwen3-32B (51.12). Extending effective context length yields greater gains than scaling parameters by several times (Table 3, Section 5.2).

- **(2) Claimed context length does not equal effective context length.** MiniMax-Text-01 claims 4M context but scores only 45.00, falling behind most 128K models. GLM-4.6 (claiming 198K) becomes unstable at its claimed limit: scores drop from 34.14 to 2.55 at 256K when truncation length is raised from 120K to 190K (Table 3, Table 4, Section 5.2).

- **(3) Cross-lingual performance is misaligned.** GPT, Claude, Mistral, and Llama series perform better in English; GLM, Kimi, and MiniMax perform better in Chinese. However, stronger models (DeepSeek-V3.2, Qwen3-235B-A22B-Thinking-2507) narrow this gap through stronger cross-lingual semantic representation (Table 3, Section 5.2).

- **(4) Extreme difficulty reveals true capability gaps.** On Easy samples, the gap between open-source and closed-source models is minimal (GPT-5: 85.23, DeepSeek-V3.2: 85.02). On Extreme samples, the gap widens (Gemini-2.5-Pro: 50.77, DeepSeek-V3.2: 44.27). Thinking gains exhibit diminishing returns at higher difficulty: Claude-4-Sonnet gains +15.36 on Easy but only +4.13 on Extreme (Table 3, Section 5.2).

- **(5) Thinking improves long-context performance substantially.** Gemini-2.5-Flash: 55.92 -> 67.41 with thinking. Qwen3-4B with thinking (40.82) surpasses Qwen3-32B without thinking (40.28) (Table 3, Section 5.2).

- **(6) Native thinking training is required.** Thinking/mixed-thinking models gain substantially: Claude-4-Sonnet +13.80 (56.07 -> 69.87), DeepSeek-V3.2 +16.15 (51.67 -> 67.82). Traditional instruct models show limited or negative gains: Llama-3.1-405B-Instruct +0.59 (40.07 -> 40.66), Gemma-3-12B-It -0.24 (32.16 -> 31.92), Llama-3.1-8B-Instruct -1.03 (21.09 -> 20.06) (Table 3, Section 5.2).

- **(7) Mixed-thinking models achieve Pareto optimality.** They maintain robust baseline capability without thinking and approach or surpass dedicated thinking models with thinking enabled. Gemini-2.5-Flash approaches Gemini-2.5-Pro in thinking mode; DeepSeek-V3.2 significantly outperforms DeepSeek-R1 in thinking mode (Table 3, Section 5.2).

### Length Dimension Analysis

Most models exhibit declining performance as sample length increases. Gemini-2.5-Pro is the exception, showing remarkable length insensitivity: 74.50 at 8K vs. 71.77 at 256K. This indicates that within the 256K range, the bottleneck for state-of-the-art models is not the ability to "read" 256K tokens but rather the capacity to handle long-range dependencies and complex logical relationships (Section 5.4, Figure 7).

**Performance across length (selected models):**

| Model | 8K | 16K | 32K | 64K | 128K | 256K |
|---|---|---|---|---|---|---|
| Gemini-2.5-Pro | 74.50 | 74.79 | 75.31 | 74.18 | 70.00 | 71.77 |
| GPT-5 | 75.37 | 76.27 | 74.34 | 76.46 | 69.36 | 63.82 |
| Claude-4-Sonnet | 72.73 | 71.48 | 72.82 | 70.52 | 66.43 | 65.26 |
| DeepSeek-V3.2 | 75.54 | 74.49 | 69.53 | 69.47 | 64.77 | 53.12 |
| Llama-3.1-405B-Instruct | 52.38 | 51.80 | 46.41 | 41.82 | 26.01 | 25.54 |

### Task Dimension Analysis

- **Gap between retrieval and aggregation.** Models score above 80 on retrieval (T1) and sequencing (T2) but drop sharply on aggregation (T6, average 57.72), indicating that "needle-in-a-haystack" localization capability does not transfer to semantic aggregation of dispersed information (Section 5.5, Figure 8).
- **Imbalance in forward vs. backward inference.** Models perform relatively well on evidence retrieval/citation alignment (T5, average 63.47) but lower on QA (T3) and summarization (T4, below 55), suggesting backward alignment (outcomes to evidence) is easier than forward generation (evidence to outcomes) (Section 5.5).
- **Logical reasoning and consistency maintenance are bottlenecks.** Models perform moderately on reasoning tasks (T8--T10, ~60) and poorly on consistency maintenance (T7, T11, average below 49) (Section 5.5).

### Context Requirement Dimension

All models perform substantially better on Partial tasks (localization and retrieval) than Full tasks (integration and reasoning), with a performance drop of 7.32 to 10.84 points when shifting from Partial to Full context requirements. This indicates that associating dispersed information across segments and performing holistic reasoning remains a notable limitation of current models (Section 5.6, Figure 9).

### Upper-Bound Performance

Under Best-of-3 evaluation, all models show monotonic improvement. Gemini-2.5-Pro and GPT-5 exhibit strong stability (marginal gains converge quickly), while Qwen3-235B-A22B-Thinking-2507 shows high potential (N significantly corrects initial reasoning bias). Under Pass@3, even Gemini-2.5-Pro achieves only 10.68% on Extreme samples, demonstrating substantial headroom (Section 5.3, Figures 5--6).

---

## Limitations and Failure Modes

1. **Maximum length capped at 256K tokens.** The benchmark does not evaluate beyond 256K, while several evaluated models claim context lengths of 1M or more. Whether the findings generalize to longer contexts is unknown (Section 2, Section 5.4).

2. **Bilingual only, not multilingual.** Coverage is limited to English and Chinese. Performance patterns for other languages (especially lower-resource languages) are not assessed (Table 1).

3. **Difficulty calibration is model-dependent.** Difficulty levels are defined by the performance of 15 specific models (5 per tier). As models improve, current "Extreme" samples may become routine, and the difficulty distribution will need recalibration. The authors acknowledge this as inherent to the design's co-evolution with model capabilities (Section 3.5).

4. **Construction pipeline involves the same models used for evaluation.** The five frontier LLMs used for sample generation (Gemini-2.5-Pro, GPT-5, Claude-4-Sonnet, DeepSeek-V3.2, Qwen3-235B-A22B-Thinking-2507) are also among the highest-ranked models in evaluation. This could introduce a bias where samples are implicitly tuned to the strengths or weaknesses of these specific models.

5. **Human-model collaborative construction faces scaling tension.** The authors note that "as task length and complexity continue to grow, even human-model collaborative construction can face a tension between verification accuracy and production efficiency" (Section 7).

6. **All models struggle with Full-context tasks.** Every evaluated model shows a 7.32 to 10.84 point drop when shifting from Partial to Full context requirements, indicating that holistic reasoning over dispersed evidence remains a fundamental limitation, not just a benchmark difficulty issue (Section 5.6).

7. **Consistency maintenance is universally weak.** Models score below 49 on average for T7 (Consistency & Compliance Checking) and T11 (Dialogue Memory & Long-Horizon Tracking), exposing inherent limitations in sustaining global states over long sequences (Section 5.5).

---

## Conclusions

### Contributions

1. **Comprehensive bilingual benchmark with multi-dimensional categorization.** LongBench Pro provides 1,500 naturally occurring samples across 11 primary tasks and 25 secondary tasks in English and Chinese, with fine-grained categorization along context requirement (Full/Partial), length (six levels), and difficulty (four model-calibrated levels), covering all capability dimensions of existing benchmarks (Section 2, Table 1, Table 2).

2. **Human-Model Collaborative Construction transcends the cost-quality trade-off.** The collaborative pipeline achieves the highest sample quality (0.9609 +/- 0.0415) at moderate cost, outperforming both purely human (0.9484 +/- 0.0450) and purely model (0.8964 +/- 0.0536) construction strategies. Model drafting reduces human cognitive burden at extreme lengths while human verification eliminates hallucinated answers (Section 5.7, Figure 10).

3. **Comprehensive evaluation of 46 long-context LLMs.** The evaluation reveals systematic patterns across model families, architectures, and thinking paradigms, providing an empirical foundation for understanding long-context capabilities (Table 3, Sections 5.2--5.7).

### Implications

1. **Context-optimization-first paradigm.** Extending effective context length may contribute more to long-context comprehension than scaling model parameters, suggesting a shift from "scale-first" to "context-optimization-first" for long-context performance. However, this finding is based on comparisons within the Qwen3 family and may not generalize across architectures (Section 5.2 finding (1)).

2. **Effective context length falls short of claimed length.** Models' actual long-context understanding capability often does not match their advertised context window, constraining practical utility. Cross-lingual performance misalignment further limits real-world deployment (Section 5.2 findings (2) and (3)).

3. **Native thinking training is a post-training paradigm shift.** Thinking improves performance substantially, but only for models trained with native reasoning capability. This implies that thinking is a fundamental capability that must be internalized during training, not merely elicited through prompt engineering (Section 5.2 finding (6)).

4. **Mixed-thinking models define a promising future paradigm.** Models that combine fast response and deep reasoning achieve Pareto-optimal performance, suggesting this may become the dominant architecture for long-context applications (Section 5.2 finding (7)).

5. **Deep comprehension is the frontier challenge.** For state-of-the-art models, the bottleneck has shifted from reading capacity to comprehending long-range dependencies and complex logical relationships. Even Gemini-2.5-Pro achieves only Pass@3 of 10.68% on Extreme samples (Section 5.3, Section 5.4).

---

## Key Claims

1. **C1: Long-context optimization outperforms parameter scaling.** Qwen3-4B-Instruct-2507 (256K) scores 45.68, surpassing Qwen3-8B (44.34); Qwen3-30B-A3B-Instruct-2507 (256K) scores 54.52, outperforming Qwen3-32B (51.12). Evidence: Table 3, Section 5.2. Status: **supported**.

2. **C2: Claimed context length does not equal effective context length.** MiniMax-Text-01 (4M claimed) scores only 45.00, below most 128K models. GLM-4.6 drops from 34.14 to 2.55 at 256K when truncation length is raised from 120K to 190K. Evidence: Table 3, Table 4. Status: **supported**.

3. **C3: Cross-lingual performance is misaligned.** GPT/Claude/Mistral/Llama series perform better in English; GLM/Kimi/MiniMax perform better in Chinese. Stronger models narrow this gap. Evidence: Table 3, Section 5.2. Status: **supported**.

4. **C4: Extreme difficulty reveals true capability gaps.** On Easy samples, GPT-5 (85.23) and DeepSeek-V3.2 (85.02) are nearly tied. On Extreme samples, Gemini-2.5-Pro (50.77) leads DeepSeek-V3.2 (44.27) by 6.5 points. Thinking gains diminish at higher difficulty. Evidence: Table 3, Section 5.2. Status: **supported**.

5. **C5: Native thinking training is essential for long-context gains.** Thinking/mixed-thinking models gain substantially (Claude-4-Sonnet +13.80, DeepSeek-V3.2 +16.15), while instruct models show limited or negative gains (Llama-3.1-405B +0.59, Gemma-3-12B-It -0.24, Llama-3.1-8B -1.03). Evidence: Table 3, Section 5.2. Status: **supported**.

6. **C6: Mixed-thinking models achieve Pareto optimality.** Gemini-2.5-Flash approaches Gemini-2.5-Pro in thinking mode; DeepSeek-V3.2 outperforms DeepSeek-R1 (67.82 vs 60.07) in thinking mode while maintaining robust non-thinking baseline. Evidence: Table 3, Section 5.2. Status: **supported**.

7. **C7: Human-model collaborative construction achieves highest quality.** Average quality score 0.9609 +/- 0.0415 vs human-only 0.9484 +/- 0.0450 and model-only 0.8964 +/- 0.0536. Fleiss' Kappa = 0.76. Evidence: Section 5.7, Figure 10. Status: **supported**.

---

## Open Questions

1. **Will the context-optimization-first paradigm hold as models scale beyond current parameter counts?** The finding is based primarily on Qwen3 family comparisons. Whether it generalizes across architectures and to much larger models is unresolved.

2. **How can human-model collaborative construction scale beyond 256K while maintaining verification accuracy?** The authors note the tension between verification accuracy and production efficiency at extreme lengths (Section 7). They are exploring a recursive "Critique-of-Critique" scheme but have not yet published results.

3. **Will mixed-thinking models remain Pareto-optimal as dedicated thinking models improve?** The current advantage of mixed-thinking over pure thinking models may be transient as thinking-specific training matures.

4. **Can the benchmark maintain discriminability as models improve?** With even Gemini-2.5-Pro achieving only Pass@3 of 10.68% on Extreme samples, LongBench Pro currently has headroom. However, the model-calibrated difficulty levels will need periodic recalibration.

---

## Core References and Why They Are Referenced

### Long-Context Evaluation Benchmarks

- **Bai et al. (2023)** -- *LongBench.* The predecessor benchmark in the same line of work. LongBench Pro extends it with broader task coverage (11 vs. 6 primary tasks), multi-dimensional categorization, and fully natural text at longer context lengths.
- **Bai et al. (2025)** -- *LongBench v2.* The immediate predecessor at ACL 2025. LongBench Pro extends it with bilingual coverage (EN + ZH vs. EN only), diverse metrics (vs. single metric), and fine-grained categorization across all three dimensions (context requirement, length, difficulty).
- **Hsieh et al. (2024)** -- *RULER.* A synthetic benchmark with controllable length and complexity. LongBench Pro contrasts with RULER by using fully natural text, bilingual coverage, and a broader task taxonomy (11 vs. 4 categories). LongBench Pro covers all capability dimensions tested by RULER.
- **Yen et al. (2024)** -- *HELMET.* A methodology-focused benchmark emphasizing systematic evaluation. LongBench Pro compares against it in Table 1 as having coarser difficulty granularity and English-only coverage.
- **Qiu et al. (2024)** -- *CLongEval.* A Chinese long-context benchmark. LongBench Pro subsumes its language coverage while adding English and achieving finer-grained multi-dimensional categorization.
- **Zhang et al. (2024)** -- *InfiniteBench.* A mixed synthetic/natural benchmark extending evaluation beyond 100K tokens. LongBench Pro uses fully natural text (vs. mixed) with broader task and language coverage.
- **Shaham et al. (2022; 2023)** -- *SCROLLS/ZeroSCROLLS.* Long-document NLP suites that LongBench Pro references as early efforts in long-context evaluation.
- **An et al. (2023); Wang et al. (2024)** -- *L-Eval and Ada-L-Eval.* Standardized evaluation protocols for long-context LLMs, referenced as part of the broader evaluation landscape.

### Models Used in Evaluation

- **Comanici et al. (2025)** -- *Gemini 2.5.* The top-performing model on LongBench Pro (73.42 overall), exhibiting remarkable length insensitivity (74.50 at 8K vs. 71.77 at 256K). Also used as one of the five frontier models for sample generation.
- **OpenAI (2025)** -- *GPT-5.* The second-ranked model (72.61 overall). Also used for sample generation.
- **Anthropic (2025)** -- *Claude-4-Sonnet.* Third-ranked model (69.87 overall) and primary example for the thinking gain analysis (+13.80). Also used for sample generation.
- **Liu et al. (2025)** -- *DeepSeek-V3.2.* Top open-source model (67.82 overall) and primary example for mixed-thinking Pareto optimality. Also used for sample generation.
- **Yang et al. (2025)** -- *Qwen3.* Multiple Qwen3 variants are used for context-optimization vs. parameter-scaling analysis and for difficulty calibration. Qwen3-235B-A22B-Thinking-2507 is the fifth sample generation model.
- **DeepSeek-AI et al. (2025)** -- *DeepSeek-R1.* A dedicated thinking model (60.07 overall) that DeepSeek-V3.2 outperforms in thinking mode, illustrating mixed-thinking Pareto optimality.
- **OpenAI et al. (2025)** -- *GPT-OSS-120B/20B.* Open-source thinking models evaluated to compare closed vs. open-source performance.
- **AI (2024)** -- *Llama 3.1.* Multiple Llama variants evaluated; Llama-3.1-405B-Instruct serves as an example of limited thinking gains for instruct models (+0.59).

### Foundational Techniques

- **Wei et al. (2022)** -- *Chain-of-Thought Prompting.* The thinking process paradigm that motivates LongBench Pro's dual prompt design (non-thinking vs. thinking) for evaluating model upper bounds.
- **Liu et al. (2023)** -- *Lost in the Middle.* Demonstrates positional effects and the gap between advertised and effective reasoning length in long contexts, a phenomenon that LongBench Pro's length-dimension analysis confirms and extends.
