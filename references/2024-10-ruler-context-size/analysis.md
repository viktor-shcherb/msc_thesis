# RULER: What's the Real Context Size of Your Long-Context Language Models?

**Authors:** Cheng-Ping Hsieh, Simeng Sun, Samuel Kriman, Shantanu Acharya, Dima Rekesh, Fei Jia, Yang Zhang, Boris Ginsburg (NVIDIA)
**Date:** October 2024, COLM 2024 (arXiv:2404.06654)

---

## Core Research Problem

The needle-in-a-haystack (NIAH) test has become the dominant synthetic evaluation for long-context language models, but it only measures a superficial form of long-context understanding: retrieving a single piece of information from distractor text. Models that achieve near-perfect NIAH scores may still fail at tasks requiring multi-hop tracing, aggregation, or robust retrieval under harder conditions (e.g., many distractors, multiple needles, non-standard needle types).

Existing realistic benchmarks (ZeroSCROLLS, L-Eval, LongBench, InfiniteBench) offer task diversity but lack control over sequence length and task complexity, and their reliance on parametric knowledge confounds the measurement of genuine long-context utilization (Shaham et al., 2023; Bai et al., 2023). Purely synthetic benchmarks like passkey retrieval or key-value retrieval offer controllability but cover only retrieval. **The core challenge is how to build a synthetic benchmark that is both controllable (arbitrary sequence length and complexity) and comprehensive (testing behaviors beyond simple retrieval).**

---

## Problem Solutions

RULER is a new synthetic benchmark with flexible configurations for sequence length and task complexity, organized around four task categories that go beyond vanilla retrieval:

1. **Retrieval (extended NIAH):** Extends the vanilla NIAH test along three axes -- diverse needle/haystack types, hard distractors (multi-keys), and high-recall retrieval (multi-values, multi-queries).
2. **Multi-hop tracing:** A variable tracking task that emulates coreference chain resolution, requiring models to trace entity bindings across multiple hops in the context.
3. **Aggregation:** Common words extraction (CWE) and frequent words extraction (FWE) tasks that serve as proxies for summarization, requiring models to aggregate information spanning the full context.
4. **Question answering:** Existing short-context QA datasets (SQuAD, HotpotQA) extended with distracting paragraphs to simulate long-context scenarios.

---

## Approach Details

### Method

RULER generates evaluation examples automatically from input configurations (Table 2 of the paper) that define the length and complexity of each input. Task complexity is a function of two factors: the number of target output tokens and the signal-to-noise ratio in the context. All tasks use synthetic input to minimize reliance on parametric knowledge.

### Key Technical Components

**Retrieval tasks (NIAH variants).** Each task inserts key-value pair "needles" into a "haystack" of distractor text. The query appears at the end of the sequence and cues matching keys to retrieve associated values. Four sub-tasks test distinct retrieval capabilities:

- **Single NIAH (S-NIAH):** Vanilla retrieval of one needle. The needle format is "the special magic number for XXX is: YYY". Query/key/value can be words, 7-digit numbers, or 32-digit UUIDs. The haystack can be repeated noise sentences or Paul Graham essays.
- **Multi-keys NIAH (MK-NIAH):** Multiple needles inserted, only one must be retrieved. Additional needles are hard distractors. The most challenging variant fills the entire haystack with distractor needles.
- **Multi-values NIAH (MV-NIAH):** Multiple needles share the same key. All associated values must be retrieved.
- **Multi-queries NIAH (MQ-NIAH):** Multiple needles with distinct keys, all must be retrieved. This is the multi-query associative recall setup of Arora et al. (2024).

**Variable Tracking (VT).** A variable X1 is initialized with a value V, followed by a chain of name-binding statements (X2 = X1, X3 = X2, ...) inserted at various positions. The model must return all variable names pointing to V. Complexity scales with the number of hops (binding depth) and the number of chains (parallel bindings acting as distractors).

**Common Words Extraction (CWE).** Words are sampled from discrete uniform distributions: a fixed number of common words (each appearing `freq_cw` times) and a growing number of uncommon words (each appearing `freq_ucw` times, with `freq_ucw < freq_cw`). The number of uncommon words increases with sequence length. The model must return the top-K most frequent words (K = number of common words, set to 10 in the main evaluation).

**Frequent Words Extraction (FWE).** Words are sampled from a Zeta distribution inspired by Zipf's Law. The frequency of the k-th ranked word is `k^{-alpha} * N / zeta(alpha)`, where N is the total number of words (determined by context size) and `zeta(alpha)` is the Zeta function. The top-ranked word is set to noise. The model must return the top-3 most frequent words. Lower values of alpha make the task harder by reducing frequency differences between words.

**Question Answering (QA).** Golden paragraphs from SQuAD (Rajpurkar et al., 2018) or HotpotQA (Yang et al., 2018) are embedded among randomly sampled distractor paragraphs from the same dataset. The number of distractor paragraphs scales with context length.

### Experimental Setup

- **Models:** 17 long-context LLMs (15 open-source, 2 closed-source: Gemini-1.5-Pro and GPT-4), covering 7B to 8x22B (MoE) parameters and claimed context lengths from 32K to 1M.
- **Inference:** All models evaluated using vLLM (Kwon et al., 2023), BFloat16, 8 NVIDIA A100 GPUs, greedy decoding.
- **Task configurations:** 13 representative tasks selected via a correlational study (Appendix C) across the four categories.
- **Evaluation:** 500 examples per task per length from the series (4K, 8K, 16K, 32K, 64K, 128K). Recall-based accuracy with an answer prefix appended to prevent refusals.
- **Effective context size:** Defined as the maximum length at which a model exceeds the Llama2-7B baseline performance at 4K (85.6%).
- **Ranking:** Two weighted average scores -- wAvg.(inc) and wAvg.(dec) -- with weights linearly increasing or decreasing with sequence length, simulating usage distributions dominated by longer or shorter sequences respectively.

### Key Results

| Model | Claimed Length | Effective Length | 4K | 8K | 16K | 32K | 64K | 128K | Avg. |
|---|---|---|---|---|---|---|---|---|---|
| Gemini-1.5-Pro | 1M | >128K | 96.7 | 95.8 | 96.0 | 95.9 | 95.9 | 94.4 | 95.8 |
| GPT-4 | 128K | 64K | 96.6 | 96.3 | 95.2 | 93.2 | 87.0 | 81.2 | 91.6 |
| Llama3.1 (70B) | 128K | 64K | 96.5 | 95.8 | 95.4 | 94.8 | 88.4 | 66.6 | 89.6 |
| Qwen2 (72B) | 128K | 32K | 96.9 | 96.1 | 94.9 | 94.1 | 79.8 | 53.7 | 85.9 |
| Yi (34B) | 200K | 32K | 93.3 | 92.2 | 91.3 | 87.5 | 83.2 | 77.3 | 87.5 |
| GLM4 (9B) | 1M | 64K | 94.7 | 92.8 | 92.1 | 89.9 | 86.7 | 83.1 | 89.9 |
| Llama3.1 (8B) | 128K | 32K | 95.5 | 93.8 | 91.6 | 87.4 | 84.7 | 77.0 | 88.3 |
| Mixtral-8x22B | 64K | 32K | 95.6 | 94.9 | 93.4 | 90.9 | 84.7 | 31.7 | 81.9 |
| LWM (7B) | 1M | <4K | 82.3 | 78.4 | 73.7 | 69.1 | 68.1 | 65.0 | 72.8 |
| DBRX | 32K | 8K | 95.1 | 93.8 | 83.6 | 63.1 | 2.4 | 0.0 | 56.3 |

- **Gemini-1.5-Pro** dominates all other models by a large margin, with effective length exceeding 128K.
- **All models claim context sizes of 32K+, but only half maintain satisfactory performance at 32K** on the full RULER suite.
- **Near-perfect vanilla NIAH performance does not predict RULER performance.** Almost all models achieve near-perfect passkey retrieval and vanilla NIAH scores but degrade substantially on harder tasks.
- **Top open-source models (Llama3.1, Qwen2, Command-R-plus) share traits:** larger model sizes and larger RoPE base frequencies. Large training context window is not always necessary -- Qwen2 (trained on 32K) matches or beats models trained on 1M context.
- The two weighted average ranking schemes (wAvg. inc and wAvg. dec) produce largely consistent top-tier rankings (Gemini-1.5 and GPT-4 remain top-2) but diverge for mid-tier models, revealing a trade-off between absolute short-context performance and relative degradation at long context.

### Task Error Analysis (Yi-34B Case Study)

Yi-34B-200K was evaluated up to 256K tokens with increased task complexity. Key failure modes:

- **Non-robustness to needle types:** Near-perfect on word-number pairs, but degrades when needles are UUIDs (fails to return complete 32-digit strings at >128K).
- **Failure to ignore distractors:** Increasing distractor needles in MK-NIAH steadily lowers performance (~40 point drop at 256K in the extreme full-haystack version). Yi retrieves values from the vicinity of the target rather than the exact match.
- **Incomplete retrieval:** Increasing queries from 1 to 8 drops performance by ~15 points. With multi-values, Yi outputs duplicated answers instead of the complete set.
- **Tendency to copy from context:** At 128K, over 80% of Yi's CWE output is a verbatim copy of the one-shot example. This behavior also appears in LWM and LongAlpaca but is less prevalent in Mixtral.
- **Unreliable tracking:** Both more chains and more hops degrade VT performance. Yi returns empty strings or variables from other chains.
- **Failure to aggregate:** Some models ignore context and use parametric knowledge instead (e.g., Mistral-v0.2 returns "the", "an", "a" rather than counting words in context). Yi fails to distinguish top-frequent words as the Zeta alpha parameter decreases.
- **Hallucination in QA:** At large context sizes, Yi's performance approaches its no-context baseline, with predictions sometimes irrelevant to the question.

### Model Analysis

**Training context length:** Evaluation of the LargeWorldModel (LWM) series (7B, trained up to 128K-1M) shows that larger training context sizes generally help, but rankings can be inconsistent (LWM-1M is worse than LWM-512K at 256K, likely due to insufficient training for the new RoPE base frequency). Abrupt drops occur when models extrapolate beyond their training length.

**Model size:** Comparing Yi-34B, Yi-9B, and Yi-6B (all trained on 200K) shows that 34B is significantly better than 6B in both absolute 4K performance and relative degradation, confirming the benefit of scaling model size for long-context capabilities.

**Architecture:** Non-Transformer architectures (RWKV-v5-7B and Mamba-2.8B-slimpj) lag behind the Transformer baseline Llama2-7B by large margins up to 4K, with significant degradation when extending to 8K.

### Limitations

1. **No position controlling:** RULER reports a single metric per length without depth-level (position-within-context) performance, unlike the lost-in-the-middle analysis (Liu et al., 2024d).
2. **No correlation with realistic tasks:** Variable tracking and FWE are proposed as proxies for real tasks but this proxy relationship is not validated.
3. **No evaluation on short context:** Tasks are selected to be easy at 4K; increasing task complexity degrades performance at short lengths too, but these results are excluded.
4. **No prompt robustness verification:** Sensitivity to prompt format and fixed hyperparameters (e.g., variable name length, synthetic vocabulary size) is not studied.

---

## Conclusions

1. **Comprehensive synthetic benchmark beyond retrieval.** RULER introduces four task categories (retrieval, multi-hop tracing, aggregation, QA) with flexible sequence length and complexity configurations, going well beyond the vanilla NIAH test.

2. **Claimed context lengths are unreliable.** Despite near-perfect vanilla NIAH scores, almost all models degrade substantially on the full RULER suite as context length increases. Only half of models claiming 32K+ context can maintain satisfactory performance at 32K.

3. **Common failure modes at scale.** Models exhibit distinct failure patterns at large context sizes: failure to ignore distractors, incomplete retrieval, verbatim copying from context, reliance on parametric knowledge instead of context, and hallucination in QA.

4. **Model size matters more than training length.** Larger model sizes consistently correlate with better long-context capabilities, while training on longer sequences does not always help and can be counterproductive without sufficient training for the new positional encoding parameters.

5. **Non-Transformer architectures lag behind.** RWKV and Mamba underperform the Transformer baseline by large margins on RULER, indicating that efficient alternatives have not yet matched attention-based models for long-context tasks.

6. **Evaluation methodology contributions.** The effective context size metric (threshold-based on Llama2-7B at 4K) and weighted average ranking schemes (wAvg. inc/dec) provide practical tools for comparing long-context models under different usage assumptions.

---

## Core References and Why They Are Referenced

### Long-Context Evaluation Foundations

- **Kamradt (2023)** -- *Needle In A Haystack.* The vanilla NIAH test that RULER directly extends. RULER addresses its limitation of testing only single-needle retrieval.
- **Mohtashami & Jaggi (2023)** -- *Landmark Attention.* Introduced passkey retrieval, one of the S-NIAH subtasks in RULER. Also provides the repeated noise sentence format used as one haystack option.
- **Shaham et al. (2023)** -- *ZeroSCROLLS.* A realistic long-context benchmark that RULER contrasts with as lacking controllable context and relying on parametric knowledge.
- **Bai et al. (2023)** -- *LongBench.* A bilingual hybrid benchmark that RULER compares against in Table 1 for benchmark design properties.
- **Liu et al. (2024d)** -- *Lost in the Middle.* Demonstrates position-dependent performance degradation in long contexts. RULER acknowledges lacking position controlling as a limitation and references this work.
- **Arora et al. (2024)** -- *Zoology.* Provides the multi-query associative recall setup that MQ-NIAH directly replicates.
- **Ribeiro et al. (2020)** -- *CheckList.* Inspires RULER's behavioral testing approach, evaluating models via diverse task categories rather than single aggregate metrics.

### Positional Encoding and Context Extension

- **Su et al. (2023)** -- *RoFormer (RoPE).* The rotary position embedding used by most models evaluated in RULER. Top-performing models use larger RoPE base frequencies.
- **Chen et al. (2023)** -- *Positional Interpolation.* A context extension method; models using PI variants are among those evaluated.
- **Peng et al. (2024)** -- *YaRN.* Context extension method; YaRN-base is included in the evaluation (Table 4).
- **Xiong et al. (2023)** -- *Effective Long-Context Scaling.* Describes the large base frequency approach to RoPE scaling used by top-performing open-source models.

### Models Evaluated

- **Reid et al. (2024)** -- *Gemini 1.5.* The top-performing model on RULER with effective length >128K.
- **OpenAI: Josh Achiam et al. (2023)** -- *GPT-4.* The second-ranked model on RULER.
- **Young et al. (2024)** -- *Yi.* Yi-34B-200K serves as the primary case study for task error analysis (Section 5).
- **Liu et al. (2024a)** -- *LargeWorldModel (LWM).* The LWM series is used to analyze the effect of training context length (Section 6).

### Alternative Architectures

- **Gu & Dao (2023)** -- *Mamba.* Non-Transformer architecture evaluated on RULER, found to lag behind Transformer baselines.
- **Peng et al. (2023)** -- *RWKV.* Non-Transformer architecture evaluated, also underperforming the Transformer baseline.

### Evaluation Infrastructure

- **Kwon et al. (2023)** -- *vLLM.* The inference engine used for all model evaluations, with efficient KV cache memory management.

#### Cross-References in Available Papers

- **PI (2023-06-pi-positional-interpolation):** RULER evaluates models that use PI-based context extension (e.g., the extended Llama2 variants). PI is referenced as one of the context extension methods enabling the long-context models benchmarked.
- **YaRN (2024-05-yarn-context-extension):** YaRN-Llama-2-7b-128k is included as a base model in RULER's evaluation (Table 4, Appendix A).
- **Lost in the Middle (2024-02-lost-in-the-middle):** RULER explicitly acknowledges its lack of position-controlling as a limitation, referencing the lost-in-the-middle phenomenon. The QA task category is a real-world adaptation of NIAH inspired by this line of work.
- **DroPE (2025-12-drope-dropping-positional-embeddings):** DroPE uses RULER's multi-query/key/value NIAH tasks as its primary evaluation benchmark for zero-shot long-context extension.
