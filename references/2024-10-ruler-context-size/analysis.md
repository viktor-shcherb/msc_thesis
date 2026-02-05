---
title: "RULER: What's the Real Context Size of Your Long-Context Language Models?"
authors: "Hsieh, Sun, Kriman, Acharya, Rekesh, Jia, Zhang, Ginsburg"
year: 2024
venue: "COLM 2024"
paper_type: conference-paper
categories: ["benchmarking", "long-context-evaluation"]
scope: ["synthetic long-context benchmark", "multi-task evaluation beyond retrieval"]
benchmarks_used: ["ruler", "niah", "squad", "hotpotqa"]
models_introduced: []
models_evaluated: ["gemini-1.5-pro", "gpt-4", "llama-3-8b", "llama-3-70b", "yi-34b", "mistral-7b", "qwen-series"]
key_claims:
  - id: C1
    claim: "Despite near-perfect vanilla NIAH scores, almost all models exhibit large performance drops on the full RULER suite as context length increases"
    evidence: "Table 3 vs Appendix E (Tables 10-11), Section 4"
    status: supported
  - id: C2
    claim: "While all models claim context sizes of 32K+ tokens, only half can maintain satisfactory performance at 32K on RULER"
    evidence: "Table 3, effective vs claimed context lengths"
    status: supported
  - id: C3
    claim: "Larger model sizes positively correlate with better long-context capabilities on RULER"
    evidence: "Section 6, Figure 4 middle-right; Yi-34B vs Yi-9B vs Yi-6B comparison"
    status: supported
  - id: C4
    claim: "Training on longer sequences does not always lead to better RULER performance"
    evidence: "Section 6, Figure 4 left and middle-left; LWM-1M worse than LWM-512K at 256K"
    status: supported
  - id: C5
    claim: "Non-Transformer architectures (RWKV, Mamba) lag behind the Transformer baseline by large margins on RULER"
    evidence: "Section 6, Figure 4 right"
    status: supported
cross_references:
  - target: 2023-11-needle-in-a-haystack
    type: extends
    detail: "RULER directly extends NIAH along three axes: diverse needle types, hard distractors, multi-needle retrieval"
  - target: 2023-12-landmark-attention-infinite-context
    type: extends
    detail: "RULER extends the passkey retrieval task and reuses the noise sentence format from Landmark Attention"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: complementary
    detail: "RULER contrasts with ZeroSCROLLS as controllable synthetic evaluation vs realistic evaluation relying on parametric knowledge"
  - target: 2024-08-longbench-bilingual-benchmark
    type: complementary
    detail: "RULER compares against LongBench in Table 1 for benchmark design properties (diverse tasks, controllability)"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "RULER acknowledges lacking position-within-context controlling as a limitation, referencing Lost in the Middle"
  - target: 2024-05-yarn-context-extension
    type: evaluates
    detail: "YaRN-Llama-2-7b-128k is included in RULER's base model evaluation (Table 4)"
  - target: 2023-06-pi-positional-interpolation
    type: evaluates
    detail: "Models using positional interpolation-based context extension are included in the evaluation"
  - target: 2026-01-longbench-pro
    type: complementary
    detail: "LongBench Pro compares against RULER, noting its synthetic-only text and limited task coverage"
  - target: 2025-07-longbench-v2
    type: complementary
    detail: "LongBench v2 cites RULER as representative of synthetic benchmarks that fail to test deep understanding; provides complementary natural-document evaluation with human-verified difficulty"
  - target: 2025-07-nolima-long-context-evaluation
    type: complementary
    detail: "NoLiMa removes literal overlap between questions and needles; Llama 3.1 70B achieves 32K effective length on RULER but only 2K on NoLiMa, highlighting the literal matching confound"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong extends NIAH with reasoning-in-a-haystack tasks requiring multi-hop inference; RULER extends NIAH with diverse retrieval and aggregation tasks -- both address NIAH's single-fact retrieval limitation from complementary angles"
  - target: 2024-03-gemini-1.5-long-context
    type: evaluates
    detail: "Gemini 1.5 Pro achieves the highest RULER score (95.8% avg) with effective length exceeding 128K tokens"
  - target: 2023-10-mistral-7b
    type: evaluates
    detail: "Mistral 7B evaluated on RULER to measure real context utilization vs claimed context size"
  - target: 2024-03-yi-open-foundation-models
    type: evaluates
    detail: "Yi-34B evaluated on RULER synthetic long-context tasks including multi-needle retrieval"
  - target: 2025-10-kimi-linear-attention
    type: extended-by
    detail: "Kimi Linear uses RULER as primary long-context benchmark, achieving 84.3 at 128k (vs 81.3 MLA) and 94.8 at 1M tokens, demonstrating hybrid linear attention viability for extreme context lengths"
open_questions:
  - question: "Do RULER's synthetic proxy tasks (variable tracking, frequent words extraction) correlate with performance on realistic long-context NLP tasks?"
    addressed_by: null
  - question: "How sensitive are RULER results to prompt format and fixed task hyperparameters (variable name length, vocabulary size)?"
    addressed_by: null
  - question: "Does adding position controlling (depth-level evaluation) to RULER reveal lost-in-the-middle patterns across task categories?"
    addressed_by: null
---

# RULER: What's the Real Context Size of Your Long-Context Language Models?

**Authors:** Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang, Boris Ginsburg (NVIDIA)
**Date:** October 2024, COLM 2024 (arXiv:2404.06654)

---

## Core Research Problem

The needle-in-a-haystack (NIAH) test (Kamradt, 2023) has become the standard synthetic evaluation for long-context language models, but it measures only a superficial form of long-context understanding: retrieving a single piece of information from distractor text. Models achieving near-perfect NIAH scores may still fail at tasks requiring multi-hop tracing, aggregation, or robust retrieval under harder conditions (e.g., many distractors, multiple needles, non-standard needle types).

Existing realistic benchmarks (ZeroSCROLLS, L-Eval, LongBench, InfiniteBench) offer task diversity but lack control over sequence length and task complexity. Their reliance on parametric knowledge confounds measurement of genuine long-context utilization (Shaham et al., 2023; Bai et al., 2023). Purely synthetic benchmarks like passkey retrieval or key-value retrieval offer controllability but cover only retrieval. **The core challenge is how to build a synthetic benchmark that is both controllable (arbitrary sequence length and complexity) and comprehensive (testing behaviors beyond simple retrieval).**

---

## Problem Solutions

RULER is a new synthetic benchmark with flexible configurations for sequence length and task complexity, organized around four task categories that go beyond vanilla retrieval:

1. **Retrieval (extended NIAH):** Extends the vanilla NIAH test along three axes -- diverse needle/haystack types, hard distractors (multi-keys), and high-recall retrieval (multi-values, multi-queries).
2. **Multi-hop tracing:** A variable tracking task that emulates coreference chain resolution, requiring models to trace entity bindings across multiple hops in the context.
3. **Aggregation:** Common words extraction (CWE) and frequent words extraction (FWE), proxy tasks for summarization that require models to aggregate information spanning the full context.
4. **Question answering:** Existing short-context QA datasets (SQuAD, HotpotQA) extended with distracting paragraphs to simulate long-context scenarios.

---

## Approach Details

### Method

RULER generates evaluation examples automatically from input configurations (Table 2) that define the length and complexity of each input. Task complexity is a function of two factors: the number of target output tokens and the signal-to-noise ratio in the context. All tasks use synthetic input to minimize reliance on parametric knowledge. The benchmark is inspired by CheckList (Ribeiro et al., 2020), evaluating models via diverse behavioral task categories rather than single aggregate metrics (Section 3).

### Key Technical Components

**Retrieval tasks (NIAH variants).** Each task inserts key-value pair "needles" into a "haystack" of distractor text. The query appears at the end of the sequence and cues matching keys to retrieve associated values. Four sub-tasks test distinct retrieval capabilities:

- **Single NIAH (S-NIAH):** Vanilla retrieval of one needle. The needle format is "the special magic number for XXX is: YYY". Query/key/value can be words, 7-digit numbers, or 32-digit UUIDs. The haystack can be repeated noise sentences (Mohtashami & Jaggi, 2023) or Paul Graham essays (Kamradt, 2023) (Section 3.1).
- **Multi-keys NIAH (MK-NIAH):** Multiple needles inserted, only one must be retrieved. The additional needles are hard distractors. The most challenging variant fills the entire haystack with distractor needles (Section 3.1).
- **Multi-values NIAH (MV-NIAH):** Multiple needles share the same key. All associated values must be retrieved (Section 3.1).
- **Multi-queries NIAH (MQ-NIAH):** Multiple needles with distinct keys, all must be retrieved. This is the same multi-query associative recall task setup used by Arora et al. (2024) (Section 3.1).

**Variable Tracking (VT).** A variable X1 is initialized with a value V, followed by a chain of name-binding statements (X2 = X1, X3 = X2, ...) inserted at various positions in the input. The model must return all variable names pointing to V. Complexity scales with the number of hops (binding depth) and the number of chains (parallel bindings acting as distractors). One in-context demonstration is included at the beginning of the sequence (Section 3.2, Appendix D).

**Common Words Extraction (CWE).** Words are sampled from discrete uniform distributions: a fixed number of common words (each appearing `freq_cw` times) and a growing number of uncommon words (each appearing `freq_ucw` times, with `freq_ucw < freq_cw`). The number of uncommon words increases with sequence length. The model must return the top-K most frequent words (K = number of common words). One in-context demonstration is included (Section 3.3, Appendix D).

**Frequent Words Extraction (FWE).** Words are sampled from a Zeta distribution inspired by Zipf's Law. The frequency of the k-th ranked word is:

> freq(k) = k^{-α} · N / ζ(α)

where N is the total number of words (determined by context size) and ζ(α) is the Zeta function. The top-ranked word is set to noise. The model must return the top-3 most frequent words. Lower values of α make the task harder by reducing frequency differences between words (Section 3.3, footnote 4, Figure 1).

**Question Answering (QA).** Golden paragraphs from SQuAD (Rajpurkar et al., 2018) or HotpotQA (Yang et al., 2018) are embedded among randomly sampled distractor paragraphs from the same dataset. The number of distractor paragraphs scales with context length. This is a real-world adaptation (Ivgi et al., 2023) of NIAH, where the question serves as the query and the golden paragraphs are the needles (Section 3.4).

### Experimental Setup

- **Models:** 17 long-context LLMs in the main evaluation (15 open-source, 2 closed-source: Gemini-1.5-Pro and GPT-4), covering 7B to 8x22B (MoE) parameters and claimed context lengths from 32K to 1M. An additional 7 base models, model series for ablation (Yi-6B/9B/34B, LWM-128K/256K/512K/1M), and 2 non-Transformer models (RWKV-v5-7B, Mamba-2.8B-slimpj) bring the total to 37 models (Table 4, Appendix A).
- **Inference:** All models evaluated using vLLM (Kwon et al., 2023), BFloat16, 8 NVIDIA A100 GPUs, greedy decoding.
- **Task configurations:** 13 representative tasks selected via a correlational study on 8 open-source models across 18 configurations, using agglomerative clustering with correlation coefficient distance. The four categories form cohesive non-redundant clusters; 5 redundant tasks were eliminated (Appendix C, Figure 5). Final 13 tasks (Table 5): S-NIAH (3 subtasks: passkey retrieval, vanilla NIAH, word-UUID), MK-NIAH (3 subtasks: 4 keys, line retrieval, KV retrieval), MV-NIAH (4 values), MQ-NIAH (4 queries), VT (1 chain, 4 hops), CWE (freq_cw=30, freq_ucw=3, num_cw=10), FWE (α=2.0), QA (SQuAD, HotpotQA).
- **Evaluation:** 500 examples per task per length from the series (4K, 8K, 16K, 32K, 64K, 128K). Each model's chat template is applied. An answer prefix is appended to prevent refusals. Recall-based accuracy checks the presence of target output tokens (Section 4).
- **Effective context size:** The maximum length at which a model exceeds the Llama2-7B baseline performance at 4K (85.6% averaged across 13 tasks).
- **Ranking:** Two weighted average scores -- wAvg.(inc) and wAvg.(dec) -- with weights linearly increasing or decreasing with sequence length, simulating usage distributions dominated by longer or shorter sequences respectively (Section 4).

### Key Results

| Model | Claimed | Effective | 4K | 8K | 16K | 32K | 64K | 128K | Avg. |
|---|---|---|---|---|---|---|---|---|---|
| Llama2-7B (baseline) | 4K | - | 85.6 | - | - | - | - | - | - |
| Gemini-1.5-Pro | 1M | >128K | 96.7 | 95.8 | 96.0 | 95.9 | 95.9 | 94.4 | 95.8 |
| GPT-4 | 128K | 64K | 96.6 | 96.3 | 95.2 | 93.2 | 87.0 | 81.2 | 91.6 |
| Llama3.1 (70B) | 128K | 64K | 96.5 | 95.8 | 95.4 | 94.8 | 88.4 | 66.6 | 89.6 |
| Qwen2 (72B) | 128K | 32K | 96.9 | 96.1 | 94.9 | 94.1 | 79.8 | 53.7 | 85.9 |
| Command-R-plus (104B) | 128K | 32K | 95.6 | 95.2 | 94.2 | 92.0 | 84.3 | 63.1 | 87.4 |
| GLM4 (9B) | 1M | 64K | 94.7 | 92.8 | 92.1 | 89.9 | 86.7 | 83.1 | 89.9 |
| Llama3.1 (8B) | 128K | 32K | 95.5 | 93.8 | 91.6 | 87.4 | 84.7 | 77.0 | 88.3 |
| Mixtral-8x22B (39B/141B) | 64K | 32K | 95.6 | 94.9 | 93.4 | 90.9 | 84.7 | 31.7 | 81.9 |
| Yi (34B) | 200K | 32K | 93.3 | 92.2 | 91.3 | 87.5 | 83.2 | 77.3 | 87.5 |
| Phi3-medium (14B) | 128K | 32K | 93.3 | 93.2 | 91.1 | 86.8 | 78.6 | 46.1 | 81.5 |
| Mistral-v0.2 (7B) | 32K | 16K | 93.6 | 91.2 | 87.2 | 75.4 | 49.0 | 13.8 | 68.4 |
| LWM (7B) | 1M | <4K | 82.3 | 78.4 | 73.7 | 69.1 | 68.1 | 65.0 | 72.8 |
| DBRX (36B/132B) | 32K | 8K | 95.1 | 93.8 | 83.6 | 63.1 | 2.4 | 0.0 | 56.3 |

(Table 3, Section 4. Performance (%) averaged across 13 RULER tasks. Scores exceeding the 85.6% Llama2-7B threshold are underlined in the paper.)

- **Gemini-1.5-Pro** dominates all other models by a large margin, with effective length exceeding 128K (Section 4).
- **All models claim 32K+ context, but only half maintain satisfactory performance at 32K** on the full RULER suite (Table 3).
- **Near-perfect vanilla NIAH performance does not predict RULER performance.** Almost all models achieve near-perfect passkey retrieval and vanilla NIAH scores (Appendix E, Tables 10-11) but degrade substantially on harder tasks (Table 3).
- **Top open-source models (Llama3.1, Qwen2, Command-R-plus) share traits:** larger model sizes and larger RoPE base frequencies (Xiong et al., 2023). Large training context window is not always necessary -- Qwen2 (trained on 32K) matches or beats models trained on 1M context (Section 4).
- The two ranking schemes (wAvg.inc and wAvg.dec) produce consistent top-tier rankings (Gemini-1.5 and GPT-4 remain top 2) but diverge for mid-tier models, revealing a **trade-off between absolute short-context performance and relative degradation at long context** (Section 4).

### Task Error Analysis (Yi-34B Case Study)

Yi-34B-200K was evaluated up to 256K tokens with increased task complexity (Section 5). Key failure modes:

- **Non-robustness to needle types:** Near-perfect on word-number pairs, but degrades when needles are UUIDs -- Yi sometimes fails to return complete 32-digit strings at >128K (Figure 2, left).
- **Failure to ignore distractors:** Increasing distractor needles in MK-NIAH steadily lowers performance, with Yi dropping by ~40 points at 256K in the extreme full-haystack version (#K=FULL). Yi retrieves values from the vicinity of the target rather than the exact match, suggesting coarse positional matching (Figure 2, middle-left).
- **Incomplete retrieval:** Increasing queries from 1 to 8 drops performance by ~15 points. With multi-values, Yi outputs duplicated answers instead of the complete set, implying uneven associations between the key and each of its values (Figure 2, middle-right and right).
- **Tendency to copy from context:** At 128K, over 80% of Yi's CWE output is a verbatim copy of the one-shot example, whereas copying is nonexistent for short sequences. This behavior is also present in LWM and LongAlpaca but less prevalent in Mixtral. When the one-shot example is removed, the model copies the beginning of the input instead, likely due to attention sinks (Xiao et al., 2024b) (Section 5, footnote 7).
- **Unreliable tracking:** Both more chains and more hops degrade VT performance. Yi returns empty strings or variables from other chains. Degradation in the more-chains setting is most significant at lengths >128K (Figure 3, left and middle-left).
- **Failure to aggregate:** Some models ignore context and use parametric knowledge instead -- Mistral-v0.2 returns "the", "an", "a" rather than counting words in context. Yi fails to distinguish top-frequent words as the Zeta α parameter decreases (Figure 3, middle-right).
- **Hallucination in QA:** At large context sizes, Yi's performance approaches its no-context baseline. Predictions sometimes are irrelevant to the question and coincide with no-context answers (Figure 3, right).

### Model Analysis

**Effect of training context length (Section 6, Figure 4 left and middle-left).** Evaluation of the LargeWorldModel (LWM) series (7B, trained up to 128K-1M) shows that larger context sizes generally lead to better performance, but rankings can be inconsistent for long sequences. LWM-1M is worse than LWM-512K at 256K, likely due to insufficient training for adjusting to the new RoPE base frequency. Abrupt performance drops occur when models extrapolate beyond their training length (e.g., LWM-128K at 256K), with almost linear degradation on log scale within the maximum training context size.

**Effect of model size (Section 6, Figure 4 middle-right).** Comparing Yi-34B-200K, Yi-9B-200K, and Yi-6B-200K (all trained on 200K context with the same data blend), the 34B model is significantly better than the 6B model on RULER for both absolute performance at 4K and relative degradation with context scaling.

**Effect of architecture (Section 6, Figure 4 right).** Non-Transformer architectures (RWKV-v5-7B and Mamba-2.8B-slimpj) demonstrate significant degradation when extending context size to 8K and underperform the Transformer baseline Llama2-7B by large margins up to 4K, beyond which Llama2 shows poor length extrapolation.

---

## Limitations and Failure Modes

The paper explicitly acknowledges four limitations (Section 8):

1. **Lack of position controlling.** RULER reports a single metric per length without depth-level (position-within-context) performance. The depth-level evaluation used by the NIAH test (Kamradt, 2023) and LV-Eval (Yuan et al., 2024) can reveal position-dependent degradation such as the lost-in-the-middle phenomenon (Liu et al., 2024d) that RULER does not capture.
2. **Lack of correlation with realistic long-context tasks.** Variable tracking and frequent words extraction are proposed as proxies for real long-context tasks (coreference resolution, summarization), but this proxy relationship is not validated. The authors emphasize RULER should be used as "convenient behavioral checks" rather than preferred over realistic settings such as NoCHA (Karpinska et al., 2024).
3. **Lack of evaluation on short context.** Tasks are selected to be easy at 4K; increasing task complexity degrades performance at shorter lengths too, but these results are excluded. FlenQA (Levy et al., 2024) has shown degrading performance at just a few thousand tokens.
4. **Lack of verification of prompt robustness.** Sensitivity to prompt format and fixed hyperparameters (variable name length in VT, synthetic vocabulary size in CWE/FWE) is not studied.

---

## Conclusions

### Contributions

1. **Comprehensive synthetic benchmark beyond retrieval.** RULER introduces four task categories (retrieval, multi-hop tracing, aggregation, QA) with flexible sequence length and complexity configurations, going beyond the vanilla NIAH test that dominates existing synthetic evaluation (Section 3).
2. **Quantitative evidence that claimed context lengths are unreliable.** Despite near-perfect vanilla NIAH scores, almost all models degrade substantially on the full RULER suite. Only half of models claiming 32K+ context maintain satisfactory performance at 32K (Table 3, Section 4).
3. **Systematic taxonomy of long-context failure modes.** Models exhibit distinct failure patterns at large context sizes: non-robustness to needle types, failure to ignore distractors, incomplete retrieval, verbatim copying from context, reliance on parametric knowledge instead of context, and hallucination in QA (Section 5).
4. **Practical evaluation methodology for comparing long-context models.** The effective context size metric (threshold-based on Llama2-7B at 4K) and weighted average ranking schemes (wAvg.inc/dec) provide tools for comparing models under different usage assumptions (Section 4).
5. **Task category validation via correlation analysis.** A preliminary correlation study confirms that the four task categories form cohesive, non-redundant clusters, validating the multi-category design (Appendix C, Figure 5).

### Implications

1. **Model size may matter more than training context length for long-context capabilities.** Larger model sizes consistently correlate with better RULER performance (Yi comparison), while training on longer sequences does not always help and can be counterproductive (LWM comparison). This suggests scaling model capacity may be a more reliable path to long-context competence than simply scaling training context (Section 6). [Inference: the paper presents these as separate observations; the relative importance comparison is implied but not directly tested.]
2. **Current non-Transformer architectures are not yet competitive for long-context tasks.** RWKV and Mamba lag substantially behind Transformer baselines on RULER, indicating that efficient alternatives have not yet matched attention-based models -- though this finding is limited to the specific models and tasks tested (Section 6).
3. **The community should adopt more comprehensive synthetic evaluations.** The gap between near-perfect NIAH scores and poor RULER performance suggests that passkey retrieval and vanilla NIAH alone provide a misleading picture of model capabilities. [Inference: this is the authors' recommendation rather than a demonstrated finding.]

---

## Key Claims

1. **C1: Near-perfect vanilla NIAH does not predict RULER performance.** Almost all models achieve near-perfect passkey retrieval and vanilla NIAH scores (100% or near-100% for most models at their claimed lengths; Appendix E, Tables 10-11) but exhibit large degradation on the full 13-task RULER suite as context length increases (Table 3, Section 4). **Status: supported.**

2. **C2: Only half of 32K+ models maintain satisfactory performance at 32K.** Despite all 17 evaluated models claiming context sizes of 32K or greater, only about half exceed the 85.6% Llama2-7B threshold at 32K tokens (Table 3). **Status: supported.**

3. **C3: Larger model sizes correlate with better long-context capabilities.** Yi-34B-200K significantly outperforms Yi-9B-200K and Yi-6B-200K on RULER, both in absolute 4K performance and relative degradation with context scaling, with all three trained on the same 200K context and data blend (Section 6, Figure 4 middle-right). **Status: supported.**

4. **C4: Training on longer sequences does not always improve RULER performance.** In the LWM-7B series, LWM-1M is worse than LWM-512K at 256K, likely due to insufficient training for the new RoPE base frequency. Abrupt drops occur at extrapolation boundaries (Section 6, Figure 4 left and middle-left). **Status: supported.**

5. **C5: Non-Transformer architectures lag behind Transformers on RULER.** RWKV-v5-7B and Mamba-2.8B-slimpj underperform the Transformer baseline Llama2-7B by large margins at lengths up to 4K and show significant degradation extending to 8K (Section 6, Figure 4 right). **Status: supported.**

---

## Open Questions

1. **Do RULER's synthetic proxy tasks correlate with realistic long-context performance?** Variable tracking and FWE are proposed as proxies for coreference resolution and summarization, but this proxy relationship is not validated (Section 8). No subsequent paper in this directory has addressed this question.

2. **How sensitive are RULER results to prompt format and task hyperparameters?** The paper did not conduct a comprehensive prompt robustness study beyond preliminary testing (Section 8). Sensitivity to variable name length, vocabulary size, and prompt wording remains unknown.

3. **Does adding position controlling to RULER reveal lost-in-the-middle patterns across task categories?** The paper acknowledges this gap and plans to support position controlling in the codebase (Section 8). This would connect RULER to findings from Liu et al. (2024d).

---

## Core References and Why They Are Referenced

### Long-Context Evaluation Foundations

- **Kamradt (2023)** -- *Needle In A Haystack.* The vanilla NIAH test that RULER directly extends. RULER addresses its limitation of testing only single-needle retrieval with word-number pairs.
- **Mohtashami & Jaggi (2023)** -- *Landmark Attention.* Introduced the passkey retrieval task (one of the S-NIAH subtasks in RULER) and the repeated noise sentence format ("The grass is green...") used as one haystack option.
- **Shaham et al. (2023)** -- *ZeroSCROLLS.* A realistic zero-shot long-context benchmark. RULER contrasts with it in Table 1 as lacking controllable context and relying on parametric knowledge.
- **Bai et al. (2023)** -- *LongBench.* A bilingual hybrid benchmark. RULER compares against it in Table 1 for benchmark design properties (diverse tasks, minimal parametric knowledge, controllable context).
- **Liu et al. (2024d)** -- *Lost in the Middle.* Demonstrates position-dependent performance degradation in long contexts. RULER acknowledges lacking position controlling as a limitation and references this work.
- **Ribeiro et al. (2020)** -- *CheckList.* Inspires RULER's behavioral testing approach of evaluating models via diverse task categories rather than single aggregate metrics.
- **Arora et al. (2024)** -- *Zoology.* Provides the multi-query associative recall setup that MQ-NIAH directly replicates.

### Positional Encoding and Context Extension

- **Su et al. (2023)** -- *RoFormer (RoPE).* The rotary position embedding used by most models evaluated in RULER. Top-performing open-source models use larger RoPE base frequencies.
- **Chen et al. (2023)** -- *Positional Interpolation.* A context extension method; models using PI variants are among those evaluated.
- **Peng et al. (2024)** -- *YaRN.* Context extension method; YaRN-Llama-2-7b-128k is included in the base model evaluation (Table 4).
- **Xiong et al. (2023)** -- *Effective Long-Context Scaling.* Describes the large base frequency approach to RoPE scaling used by top-performing open-source models.

### Models Evaluated

- **Reid et al. (2024)** -- *Gemini 1.5.* The top-performing model on RULER with effective length >128K and average score of 95.8%.
- **OpenAI: Josh Achiam et al. (2023)** -- *GPT-4.* The second-ranked model on RULER with effective length of 64K.
- **Young et al. (2024)** -- *Yi.* Yi-34B-200K serves as the primary case study for task error analysis (Section 5) and the Yi-6B/9B/34B series for model size ablation (Section 6).
- **Liu et al. (2024a)** -- *LargeWorldModel (LWM).* The LWM-7B series (128K-1M) is used to analyze the effect of training context length (Section 6).

### Alternative Architectures

- **Gu & Dao (2023)** -- *Mamba.* Non-Transformer architecture evaluated on RULER, found to lag behind the Transformer baseline by large margins (Section 6, Figure 4 right).
- **Peng et al. (2023)** -- *RWKV.* Non-Transformer architecture evaluated, also underperforming the Transformer baseline (Section 6).

### Behavioral Phenomena

- **Xiao et al. (2024b)** -- *Attention Sinks.* Referenced to explain the copying behavior observed when the one-shot example is removed in CWE: models copy the beginning of the input instead, likely due to attention sinks (Section 5, footnote 7).

### Evaluation Infrastructure

- **Kwon et al. (2023)** -- *vLLM.* The inference engine used for all model evaluations with efficient KV cache memory management.
