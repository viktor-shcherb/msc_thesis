---
title: "LV-Eval: A Balanced Long-Context Benchmark with 5 Length Levels Up to 256K"
authors: "Yuan, Ning, Zhou, Yang, Li, Zhuang, Tan, Yao, Lin, Li, Dai, Yan, Wang"
year: 2025
venue: "COLM 2025"
paper_type: conference-paper
categories: ["benchmarking", "long-context-evaluation"]
scope: ["long-context QA evaluation", "bilingual (English and Chinese)", "16k-256k word contexts", "knowledge leakage mitigation"]
benchmarks_used: ["lv-eval", "hotpotqa", "2wikimultihopqa", "niah"]
models_introduced: []
models_evaluated: ["llama-2-7b", "qwen-7b", "llama-3-8b", "vicuna-7b-v1.5-16k", "chatglm3-6b-32k", "bluelm-7b-32k", "longchat-v1.5-7b-32k", "qwen2.5-72b", "llama-3.1-70b", "yi-6b", "llama3-8b-1m", "gpt-4", "gpt-3.5-turbo", "moonshot-v1-128k"]
key_claims:
  - id: C1
    claim: "Moonshot-v1 and recent large-scale open-source models (Qwen-2.5-72B, Llama-3.1-70B) achieve the highest performance on LV-Eval, particularly at lengths below 64k"
    evidence: "Figure 4(a), Section 4.1"
    status: supported
    scope: "15 LLMs evaluated, average across 11 datasets"
    magnitude: "Both Qwen2.5-72B and Moonshot-v1 obtain average scores exceeding 40 at 16k and 32k lengths"
  - id: C2
    claim: "Models exhibit distinct score trends across length levels, with some smaller-context models showing gentler degradation than models with larger claimed context windows"
    evidence: "Figure 4(a), Section 4.1"
    status: supported
    scope: "15 LLMs, 5 length levels"
    magnitude: "Llama3-8B-1M shows one of the slowest declines from 16k to 128k despite lower absolute scores at 16k"
  - id: C3
    claim: "Confusing facts insertion (CFI) leads to notable performance degradation, especially on multifieldqa-en-mixup and multifieldqa-zh-mixup datasets"
    evidence: "Tables A8, A9, A10, Section 4.2"
    status: supported
    scope: "5 models ablated across 3 datasets"
    magnitude: "ChatGLM3-6B-32k degrades from 41.46 to 31.97 (9.49 points) on multifieldqa-en-mixup at 16k"
  - id: C4
    claim: "Knowledge leakage exists in open-source benchmark corpora and can be mitigated by keyword and phrase replacement (KPR)"
    evidence: "Table 4, Section 4.2"
    status: supported
    scope: "3 models tested on hotpotwikiqa-mixup"
    magnitude: "Yi-6B-200k score without context drops from 16.11 to 6.06 after KPR; ChatGLM3-6B-32k drops from 12.24 to 4.96"
  - id: C5
    claim: "The keyword-recall-based metric produces more calibrated scores than standard F1, reducing score inflation from non-informative word matching"
    evidence: "Table 5, Section 4.2"
    status: supported
    scope: "ChatGLM3-6B-32k on cmrc-mixup"
    magnitude: "At 256k, original F1 gives 26.43% vs. reference L_m/L_d = 12.5%; keyword-recall metric gives 8.38%"
cross_references:
  - target: 2024-08-longbench-bilingual-benchmark
    type: concurrent
    detail: "LV-Eval and LongBench are both bilingual (EN+ZH) long-context benchmarks; LV-Eval uses MultiFieldQA datasets from LongBench and extends evaluation to 256k words with controlled length levels"
  - target: 2024-08-l-eval-standardized-evaluation
    type: concurrent
    detail: "Both propose improved evaluation metrics for long-context; L-Eval uses length-instruction-enhanced metrics with LLM assistance, while LV-Eval uses keyword-recall-based two-stage F1"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: concurrent
    detail: "LV-Eval addresses ZeroSCROLLS' limitation of insufficient average context length (~14k words) by providing five controlled length levels up to 256k"
  - target: 2023-11-needle-in-a-haystack
    type: extends
    detail: "LV-Eval's factrecall-en and factrecall-zh datasets extend NIAH with confusing facts insertion and keyword replacement, making the retrieval task substantially harder"
  - target: 2024-10-ruler-context-size
    type: concurrent
    detail: "Both extend NIAH-style evaluation; RULER uses synthetic multi-task evaluation while LV-Eval uses natural-language QA with knowledge-leakage mitigation"
  - target: 2024-06-effective-long-context-scaling
    type: complementary
    detail: "Effective long-context scaling proposes training methods evaluated on long-context benchmarks including LV-Eval; LV-Eval provides the evaluation framework these methods are tested against"
open_questions:
  - question: "Can stronger LLMs (e.g., GPT-4-128k, GPT-4o) be used to automate confusing fact generation and revision, reducing human annotation effort?"
    addressed_by: null
  - question: "Why does the anti-interference ability of models vary significantly across languages, with Llama-3-8B-Instruct showing 100% susceptibility to confusing facts in Chinese but only 32% in English?"
    addressed_by: null
  - question: "How do recently released long-context models (Llama 3.1, Qwen 2.5, etc.) perform on LV-Eval compared to the originally evaluated set?"
    addressed_by: null
  - question: "Can LV-Eval's techniques (CFI, KPR) be extended to task types beyond QA, such as summarization or code understanding?"
    addressed_by: null
---

# LV-Eval: A Balanced Long-Context Benchmark with 5 Length Levels Up to 256K

**Authors:** Tao Yuan, Xuefei Ning, Dong Zhou, Zhijie Yang, Shiyao Li, Minghui Zhuang, Zheyue Tan, Zhuyu Yao, Dahua Lin, Boxun Li, Guohao Dai, Shengen Yan, Yu Wang (Tsinghua University, Infinigence-AI, Shanghai AI Lab, CUHK, SJTU)
**Date:** February 2024, arXiv:2402.05136; COLM 2025

---

## Core Research Problem

State-of-the-art LLMs claim supported context lengths of 256k tokens or more, but existing long-context benchmarks have three critical shortcomings: (1) **insufficient context lengths** — mainstream benchmarks average only 5k–21k words (Table 1), far below the claimed capacities of modern LLMs; (2) **knowledge leakage** — benchmarks built from unaltered public documents may overlap with LLM training data, enabling models to answer from memorization rather than context understanding (Zhou et al., 2023a); and (3) **inaccurate metrics** — standard N-gram metrics like F1 are sensitive to answer format variations and inflated by matching non-informative words. Prior benchmarks such as ZeroSCROLLS (Shaham et al., 2023), LooGLE (Li et al., 2023b), and L-Eval (An et al., 2023) are monolingual with no explicit length-level partitioning, while BAMBOO (Dong et al., 2023) and LongBench (Bai et al., 2023b) offer length levels but at scales (~5k and ~9.5k average words) too short for evaluating models claiming 128k–256k context.

**The core challenge: how to construct a long-context benchmark that provides controlled evaluation across sufficiently long lengths while mitigating knowledge leakage and metric bias.**

---

## Problem Solutions

LV-Eval is a bilingual (English + Chinese) long-context benchmark with the following design:

1. **Five controlled length levels** (16k, 32k, 64k, 128k, 256k words) where the same QA pairs appear at every length, differing only in the amount of surrounding context — enabling controlled comparison across lengths.
2. **Confusing facts insertion (CFI)** — GPT-4-generated, human-revised confusing facts inserted into the context to test anti-interference ability.
3. **Keyword and phrase replacement (KPR)** — human-annotated replacements of key entities throughout contexts and QA pairs to eliminate knowledge leakage from memorization.
4. **Keyword-recall-based two-stage metric** — answer keywords are manually annotated and used in a recall gate before computing F1, reducing score inflation from non-informative word matching.

---

## Approach Details

### Method

LV-Eval comprises **11 bilingual datasets** organized into two task types:

- **Single-hop QA** (7 datasets): lic-mixup (zh), loogle-SD-mixup (en), cmrc-mixup (zh), multifieldqa-en-mixup (en), multifieldqa-zh-mixup (zh), factrecall-en (en), factrecall-zh (zh)
- **Multi-hop QA** (4 datasets): dureader-mixup (zh), loogle-CR-mixup (en), loogle-MR-mixup (en), hotpotwikiqa-mixup (en)

Each test instance consists of three parts: a context (*C*), a question (*Q*), and a ground-truth answer (*A*), where *C* is a synthetic document containing the information required to answer *Q*. The total benchmark comprises **1,729 QA pairs × 5 length levels = 8,645 synthetic contexts**.

The construction pipeline for each QA pair proceeds in three stages:

1. **Context mixing up**: Supporting documents for the QA pair are shuffled with distracting documents sampled until the target length level is reached. Documents are prepended with "Passage i\n" headers and concatenated.
2. **Confusing facts insertion**: For applicable datasets, GPT-4 generates two descriptions close to the original fact, human annotators resolve conflicts, and the confusing facts are inserted at random positions.
3. **Keyword and phrase replacement**: Human annotators select keywords/phrases for replacement, write substitutes, and replace throughout the entire context and QA pair. Annotators verify the modified context for consistency.

### Key Technical Components

**Confusing Facts Insertion (CFI).** Applied to 6 of 11 datasets (hotpotwikiqa-mixup, lic-mixup, multifieldqa-en-mixup, multifieldqa-zh-mixup, factrecall-en, factrecall-zh). GPT-4 is prompted to generate two confusing facts per QA pair that are similar but factually different and non-contradictory to the original. Human annotators resolve any conflicts (e.g., changing "Albert Einstein was an Italian astronomer" to "Albert Beverley was an Italian astronomer" to avoid direct contradiction). The number of confusing facts per dataset ranges from 3 (factrecall datasets) to 786 (cmrc-mixup) (Table 2).

**Keyword and Phrase Replacement (KPR).** Applied to 6 of 11 datasets (hotpotwikiqa-mixup, cmrc-mixup, multifieldqa-en-mixup, multifieldqa-zh-mixup, factrecall-en, factrecall-zh). Annotators follow guidelines: (a) replaced words must be distinct from originals and not synonyms; (b) maximize differences between revised and original sentences; (c) prioritize replacement of words without synonyms; (d) resulting statements may be inconsistent with common knowledge, as long as the answer is derivable from context. The number of KPR rules ranges from 3 (factrecall datasets) to 786 (cmrc-mixup) (Table 2).

**Keyword-Recall-Based Two-Stage Metric.** For evaluating a generated answer *A'*:
1. **Stage 1 (recall gate)**: Compute the recall of manually annotated "answer keywords" in *A'*. If recall < threshold (0.2 for Chinese, 0.4 for English datasets), the score is 0.
2. **Stage 2 (filtered F1)**: If recall passes the threshold, compute F1 between *A'* and ground-truth *A*, excluding words from a blacklist of common non-informative words (e.g., "the", "a", "of").

The word blacklist is constructed by: (1) summarizing word counts in generations of Llama2-7B-Chat-hf and ChatGLM3-6B-32K across all datasets; (2) selecting the top 100 words matching the GT answer most frequently; (3) manually annotating non-informative words from these 100. Answer keywords are manually annotated for 8 of 11 datasets. For cmrc-mixup (already concise answers) and dureader-mixup (long GT answers), the metric is simplified to F1 with blacklist and ROUGE-L with blacklist, respectively.

**Factrecall Datasets.** These are synthetic NIAH-style tasks. One English and one Chinese fact-question-answer pair are written. For each length level, 200 documents are generated by inserting the fact at 200 evenly spaced positions within the context. Distracting documents are sourced from PG-19 (English) and *Journey to the West* (Chinese). Both CFI and KPR are applied, making this a substantially harder version of the standard NIAH test.

### Experimental Setup

**Models.** 15 LLMs are evaluated: 12 open-source and 3 commercial (Table 3):

| Model | Context Length | Type |
|---|---|---|
| Llama2-7B-Chat-hf | 4k | Open-source, SFT |
| Qwen-7B-8k-Chat | 8k | Open-source, SFT |
| Llama3-8B-Instruct | 8k | Open-source, SFT |
| Vicuna-7B-16k-v1.5 | 16k | Open-source, SFT |
| ChatGLM3-6B-32k | 32k | Open-source, SFT |
| BlueLM-7B-32k-Chat | 32k | Open-source, SFT |
| LongChat-7B-32k-v1.5 | 32k | Open-source, SFT |
| Qwen2.5-72B-Instruct-128k | 128k | Open-source, SFT |
| Meta-Llama-3.1-70B-Instruct | 128k | Open-source, SFT |
| Yi-6B-200k | 200k | Open-source |
| Llama3-8B-1M | 1048k | Open-source, SFT |
| GPT-4-8k | 8k | Commercial |
| GPT-3.5-16k | 16k | Commercial, SFT |
| Moonshot-V1-128k | 128k | Commercial, SFT |

**Inference.** Greedy sampling for all models. For models with context windows smaller than the input, the middle of the data context is truncated, and head and tail are concatenated to ensure QA instructions are present.

**Metrics.** Keyword-recall-based F1 for most datasets; F1 with word blacklist for cmrc-mixup; ROUGE-L with word blacklist for dureader-mixup.

**Reproducibility.** All datasets and evaluation code are publicly released at https://github.com/infinigence/LVEval. Human annotation involved 5 annotators (3 master's students in LLM research, 2 in linguistics). CFI required ~3 days for 557 instances; KPR required 3–5 days for 1,924 pairs; answer keyword annotation took 1 day for 955 instances.

### Key Results

**Overall performance across length levels (Figure 4(a), Section 4.1):**

| Model | 16k | 32k | 64k | 128k | 256k |
|---|---|---|---|---|---|
| Qwen2.5-72B-Instruct-128k | ~42 | ~40 | ~30 | ~18 | ~12 |
| Meta-Llama-3.1-70B-Instruct | ~38 | ~35 | ~28 | ~18 | ~12 |
| GLM-4-9B-Instruct-128k | ~32 | ~30 | ~25 | ~18 | ~12 |
| Moonshot-V1-128k | ~42 | ~40 | — | — | — |
| Llama3-8B-1M | ~20 | ~18 | ~17 | ~16 | ~14 |
| ChatGLM3-6B-32k | ~28 | ~25 | ~15 | ~8 | ~5 |

*(Approximate values read from Figure 4(a); exact per-dataset scores in Tables A6, A7.)*

Key takeaways:

- **Top performers** are Moonshot-v1, Qwen2.5-72B, and Llama-3.1-70B, particularly at lengths below 64k. Both Qwen2.5-72B and Moonshot-v1 exceed average scores of 40 at 16k and 32k.
- **Among 6–9B open-source models**, GLM-4-9B achieves the best performance, even outperforming Llama-3.1-70B on longer lengths (128k, 256k).
- **Distinct score trends**: Llama3-8B-1M (1048k context) shows one of the slowest declines from 16k to 128k but has lower absolute scores at 16k than ChatGLM3-6B-32k and BlueLM-7B-32k-Chat.
- **Sharp performance drops** occur at or near the supported context length. Qwen2.5-72B-128k, GLM-4-9B-128k, and ChatGLM3-6B-32k drop sharply after 128k, 128k, and 32k respectively. Llama-3.1-70B drops sharply after 64k despite claiming 128k support.
- **Multi-hop QA is harder** than single-hop QA, and CFI adds further complexity, particularly evident in single-hop and multi-hop confusion QA (Figure 4(b)).

**Ablation: Confusing Facts Insertion (Section 4.2, Tables A8–A10):**

| Model | Dataset | w. both (16k) | w.o. both (16k) | Degradation |
|---|---|---|---|---|
| ChatGLM3-6B-32k | multifieldqa-en-mixup | 25.40 | 41.46 | -16.06 |
| ChatGLM3-6B-32k | multifieldqa-zh-mixup | 32.38 | 44.80 | -12.42 |
| ChatGLM3-6B-32k | hotpotwikiqa-mixup | 16.98 | 28.48 | -11.50 |
| Yi-6B-200k | multifieldqa-en-mixup | 10.01 | 16.78 | -6.77 |

- CFI causes notable degradation on multifieldqa datasets; less severe on hotpotwikiqa-mixup.
- ChatGLM3-6B-32k is most susceptible to CFI among tested models.
- As context length increases, CFI degradation magnitude decreases because confusing facts get truncated and baseline performance drops.

**Ablation: Keyword and Phrase Replacement (Section 4.2, Table 4):**

| Model | Direct (w. KPR) | Direct (w.o. KPR) | w. context (w. KPR, 16k) |
|---|---|---|---|
| Yi-6B-200k | 6.06 | 16.11 | 23.55 |
| ChatGLM3-6B-32k | 4.96 | 12.24 | 16.98 |
| Llama2-7B-Chat-hf | 2.43 | 3.52 | 3.99 |

- Without KPR, models achieve considerable scores even **without context** (e.g., Yi-6B-200k: 16.11), demonstrating knowledge leakage via memorization.
- KPR reduces context-free scores substantially (Yi-6B-200k: 16.11 → 6.06), confirming that KPR mitigates memorization-based answering.
- Degradation from KPR is relatively consistent across length levels.

**Ablation: Factrecall NIAH task (Section 4.2, Figure 5, Table A11):**

- ChatGLM3-6B-32k achieves near-perfect accuracy on factrecall-en without CFI or KPR within its context window (32k).
- Adding CFI alone, KPR alone, or both progressively degrades retrieval accuracy.
- The degradation is most severe on factrecall-zh, where combined CFI+KPR causes **performance collapse** (e.g., ChatGLM3-6B-32k: 91.50 → 0 at 16k on factrecall-zh with both techniques).
- This demonstrates that standard NIAH is too simple; CFI and KPR expose genuine limitations in retrieval under interference.

**Ablation: Keyword-recall-based metric (Section 4.2, Table 5):**

| Metric | 16k | 32k | 64k | 128k | 256k |
|---|---|---|---|---|---|
| Reference L_m/L_d | 100 | 100 | 50.00 | 25.00 | 12.50 |
| Original F1 | 66.49 | 59.99 | 38.71 | 31.76 | 26.43 |
| w. answer keywords | 57.67 | 52.18 | 28.92 | 21.07 | 15.45 |
| w. answer keywords + word blacklist | 51.21 | 46.34 | 20.71 | 14.16 | 8.38 |

*(ChatGLM3-6B-32k on cmrc-mixup.)*

- At 256k, original F1 gives 26.43% — far above the theoretical reference of L_m/L_d = 12.50%, indicating substantial score inflation.
- The full keyword-recall metric with blacklist yields 8.38% at 256k, more aligned with theoretical expectations.

### Language-Specific Observations

- Several models show unbalanced performance between Chinese and English on multifieldqa datasets (Tables A6, A7).
- On factrecall tasks, the performance gap between factrecall-en and factrecall-zh is especially large for some models. Llama-3-8B-Instruct is 100% misled by confusing facts in factrecall-zh-16k but only 32% misled in factrecall-en-16k (Section F).

---

## Limitations and Failure Modes

**Limitations acknowledged by the authors (Section 5):**

1. **Task type coverage**: LV-Eval covers only QA tasks. Other task types such as summarization, code understanding, and dialogue are not included.
2. **Model coverage**: Due to cost constraints, recent commercial models (GPT-4-128k, GPT-4o) were not evaluated.
3. **Benchmark overfitting risk**: All test data is publicly released, making it possible to intentionally overfit by training on the test data. Training on KPR-modified data may introduce factual errors.
4. **KPR side effect**: In some cases, models identify factual errors introduced by KPR and insist on providing common-sense responses rather than following the instruction to answer based solely on context. The authors attribute this to instruction-following limitations.
5. **CFI annotation cost**: Manual revision of GPT-4-generated confusing facts is labor-intensive and may not scale to larger benchmarks.

#### Scope and Comparability

- **Models evaluated are predominantly 6–9B scale** (10 of 12 open-source models), with only Qwen2.5-72B and Llama-3.1-70B representing larger scales. No 30B-class or 400B+ models are evaluated.
- **Word count vs. token count**: LV-Eval defines length levels in words (for English) and characters (for Chinese), not tokens. This means the effective token count varies across models depending on their tokenizer.
- **Context truncation strategy**: For models with context windows smaller than the input, middle-truncation is applied. This means models with smaller windows may still perform reasonably if the answer is near the beginning or end of the context, potentially underestimating the difficulty for those models.
- **Greedy decoding only**: All models use greedy sampling, which may not reflect performance under other decoding strategies.
- **No variance estimates** reported across runs or QA pairs. Scores are point estimates.

---

## Conclusions

### Contributions

1. **Controlled multi-length evaluation framework.** LV-Eval introduces five explicit length levels (16k–256k words) where identical QA pairs appear in every length, enabling controlled comparison of model performance across context lengths — a design not present in prior benchmarks like ZeroSCROLLS or LooGLE.

2. **Knowledge leakage mitigation via KPR.** Keyword and phrase replacement, manually annotated by humans, forces models to rely on context understanding rather than memorization. Ablations demonstrate that KPR substantially reduces context-free scores (e.g., Yi-6B-200k: 16.11 → 6.06 on hotpotwikiqa-mixup).

3. **Anti-interference evaluation via CFI.** Confusing facts insertion, generated by GPT-4 and human-revised, tests models' ability to distinguish relevant from misleading information — revealing that current models are substantially degraded by confusing facts.

4. **More calibrated evaluation metric.** The keyword-recall-based two-stage metric with word blacklist produces scores more aligned with theoretical expectations (L_m/L_d) than standard F1, reducing inflation from non-informative word matching.

5. **Enhanced NIAH evaluation.** The factrecall datasets extend the standard needle-in-a-haystack paradigm with CFI and KPR, showing that standard NIAH is too simple and that current models struggle significantly when interference is introduced.

### Implications

1. **Claimed context length ≠ effective context length.** Models like Llama-3.1-70B (128k claimed) show sharp performance drops at 64k on LV-Eval, suggesting that claimed context windows substantially overstate effective utilization — consistent with findings from RULER (Hsieh et al., 2024).

2. **Knowledge leakage is a real concern for long-context benchmarks.** The KPR ablations suggest that benchmarks built from public data without mitigation may systematically overestimate long-context ability, as models can score non-trivially even without any context.

3. **Standard NIAH is insufficient for evaluating retrieval ability.** The factrecall results show that adding interference (CFI) and preventing memorization (KPR) can collapse performance from near-perfect to near-zero, indicating that current NIAH-based evaluations may paint an overly optimistic picture.

---

## Key Claims

1. **C1 (Top model performance).** Moonshot-v1 and recent large-scale open-source models (Qwen-2.5-72B, Llama-3.1-70B) achieve the highest performance on LV-Eval, with average scores exceeding 40 at 16k and 32k (Figure 4(a), Section 4.1). Status: **supported**. Evidence breadth: 15 models, 11 datasets, 5 length levels.

2. **C2 (Distinct score trends).** Models exhibit different degradation patterns: Llama3-8B-1M shows gentle degradation despite lower absolute scores, while ChatGLM3-6B-32k and others show sharp drops near their context limit (Figure 4(a), Section 4.1). Status: **supported**. Evidence breadth: 15 models across 5 length levels.

3. **C3 (CFI degrades performance).** LLMs significantly degrade with confusing information, especially on multifieldqa datasets where ChatGLM3-6B-32k drops by 16.06 points at 16k (Tables A8–A10, Section 4.2). Status: **supported**. Evidence breadth: 5 models ablated on 3 datasets. Note: CFI degradation on hotpotwikiqa-mixup is less severe, suggesting task-dependent sensitivity.

4. **C4 (Knowledge leakage mitigation).** KPR reduces context-free scores substantially (Yi-6B-200k: 16.11 → 6.06; ChatGLM3-6B-32k: 12.24 → 4.96 on direct querying without context), confirming knowledge leakage in Wikipedia-sourced benchmarks (Table 4, Section 4.2). Status: **supported**. Evidence breadth: 3 models on 1 dataset (hotpotwikiqa-mixup); limited to Wikipedia-based data.

5. **C5 (Metric calibration).** The keyword-recall-based metric reduces score inflation: at 256k on cmrc-mixup, original F1 gives 26.43% while the full metric gives 8.38%, closer to the theoretical reference of 12.5% (Table 5, Section 4.2). Status: **supported**. Evidence breadth: single model (ChatGLM3-6B-32k), single dataset.

---

## Open Questions

1. **Can CFI generation be automated with stronger LLMs?** The authors note manual revision is labor-intensive and suggest leveraging stronger models to reduce human effort. As of writing, this remains unexplored.

2. **Why does anti-interference ability vary significantly across languages?** Llama-3-8B-Instruct is 100% misled by confusing facts in factrecall-zh but only 32% in factrecall-en. The mechanism behind this asymmetry is not investigated.

3. **How do models beyond the evaluated set perform?** The evaluation predates many recent models (GPT-4o, Claude 3.5, Gemini 1.5 Pro) that claim long-context capabilities. Updated evaluations would be informative.

4. **Can LV-Eval's techniques extend to non-QA tasks?** CFI and KPR are designed for QA; their applicability to summarization, code understanding, or dialogue tasks remains unexplored.

5. **What is the relationship between KPR-induced difficulty and context length?** The paper shows KPR degradation is relatively consistent across lengths, but the interaction between KPR and context-length scaling deserves deeper analysis.

---

## Core References and Why They Are Referenced

### Long-Context Benchmarks (Direct Comparisons)

- **Shaham et al. (2023)** — *ZeroSCROLLS.* Zero-shot long-text benchmark with ~14k average word count; LV-Eval addresses its insufficient context length.
- **Li et al. (2023b)** — *LooGLE.* Long-context benchmark with ~21k average word count; provides source data for loogle-SD-mixup, loogle-CR-mixup, and loogle-MR-mixup datasets.
- **An et al. (2023)** — *L-Eval.* Standardized long-context evaluation with optimized metrics; concurrent effort with different metric approach (LLM-assisted vs. keyword-recall).
- **Bai et al. (2023b)** — *LongBench.* Bilingual multitask benchmark with ~9.5k average word count; provides source data for multifieldqa datasets.
- **Dong et al. (2023)** — *BAMBOO.* Long-text modeling benchmark with ~5k average words and length levels at 4k and 16k.

### Needle-in-a-Haystack Evaluation

- **Kamradt (2023)** — *Needle in a Haystack.* Original NIAH retrieval test; LV-Eval extends this with factrecall datasets incorporating CFI and KPR.
- **Hsieh et al. (2024)** — *RULER.* Multi-task synthetic long-context benchmark extending NIAH; concurrent effort with different approach (synthetic diversity vs. knowledge-leakage mitigation).

### Knowledge Leakage

- **Zhou et al. (2023a)** — *Don't Make Your LLM an Evaluation Benchmark Cheater.* Identifies knowledge leakage as a concern in LLM evaluation; motivates LV-Eval's KPR technique.

### Data Sources

- **Yang et al. (2018)** — *HotpotQA.* Multi-hop QA dataset; source for hotpotwikiqa-mixup.
- **Ho et al. (2020)** — *2WikiMultiHopQA.* Multi-hop QA with template-designed questions; source for hotpotwikiqa-mixup.
- **Rae et al. (2019)** — *PG-19.* Book corpus; source for factrecall distracting documents.
- **Cui et al. (2018)** — *CMRC 2018.* Chinese reading comprehension; source for cmrc-mixup.
- **Tang et al. (2020)** — *DuReader Robust.* Chinese reading comprehension; source for dureader-mixup.

### Models Evaluated

- **Touvron et al. (2023)** — *Llama 2.* Base model for Llama2-7B-Chat-hf (4k context).
- **AI@Meta (2024)** — *Llama 3.* Base model for Llama3-8B-Instruct (8k context).
- **Meta (2024)** — *Llama 3.1.* 70B-Instruct with 128k context.
- **Yang et al. (2024)** — *Qwen2 Technical Report.* Qwen2.5-72B-Instruct-128k.
- **Yi (2023)** — *Yi series.* Yi-6B-200k with 200k context.
- **Achiam et al. (2023)** — *GPT-4 Technical Report.* GPT-4-8k. Also used for CFI generation.
