---
title: "LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding"
authors: "Bai, Lv, Zhang, Lyu, Tang, Huang, Du, Liu, Zeng, Hou, Dong, Tang, Li"
year: 2024
venue: "ACL 2024"
paper_type: conference-paper
categories: ["benchmarking", "long-context-evaluation"]
scope: ["bilingual long-context evaluation", "21 datasets across 6 task categories in EN and ZH"]
benchmarks_used: ["longbench"]
models_introduced: []
models_evaluated: ["gpt-3.5-turbo", "llama-2-7b", "chatglm2-6b", "chatglm2-6b-32k", "longchat-v1.5-7b-32k", "xgen-7b-8k", "internlm-7b-8k", "vicuna-7b-v1.5-16k"]
key_claims:
  - id: C1
    claim: "LongBench is the first bilingual, multi-task benchmark for long context understanding, comprising 21 datasets across 6 categories in both English and Chinese"
    evidence: "Table 1, Section 1, Section 3"
    status: supported
  - id: C2
    claim: "GPT-3.5-Turbo-16k outperforms open-source models overall (44.7%) but degrades 17% from 0-4K to 8K+ on LongBench-E"
    evidence: "Tables 2-3, Figure 3, Section 4.1"
    status: supported
  - id: C3
    claim: "Position interpolation and longer fine-tuning yield up to 62% relative improvement (ChatGLM2-6B-32k over ChatGLM2-6B) and 19% (LongChat-v1.5-7B-32k over Llama2-7B-chat-4k)"
    evidence: "Tables 2-3, Section 4.1"
    status: supported
  - id: C4
    claim: "Retrieval-based compression helps only models with weak long-context ability (+21% for Llama2-7B-chat-4k) but slightly degrades strong models (-2% GPT-3.5-Turbo-16k, -5% ChatGLM2-6B-32k)"
    evidence: "Table 4, Section 4.2"
    status: supported
  - id: C5
    claim: "Models trained on longer contexts (ChatGLM2-6B-32k, LongChat-v1.5-7B-32k) are most robust to length increases on LongBench-E, with relative drops of only 4% and 7% from 0-4K to 8K+"
    evidence: "Figure 3, Table 9, Section 4.1"
    status: supported
  - id: C6
    claim: "Wikipedia-based multi-doc QA tasks show high memorization scores without context, indicating models partly rely on parametric knowledge rather than context understanding"
    evidence: "Table 6, Section 4.3"
    status: supported
  - id: C7
    claim: "Synthetic tasks exhibit near-binary discriminability, making simple averaging across all tasks potentially misleading for ranking models"
    evidence: "Tables 2-3, Appendix D"
    status: supported
cross_references:
  - target: 2022-12-scrolls-long-language-sequences
    type: extends
    detail: "LongBench argues SCROLLS covers a restricted range of task types and extends it with broader coverage, bilingual support, and controlled-length subsets"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: concurrent
    detail: "ZeroSCROLLS is a concurrent zero-shot benchmark; LongBench provides broader task diversity and bilingual support"
  - target: 2021-05-long-range-arena
    type: complementary
    detail: "LongBench uses natural-text tasks contrasting with LRA's synthetic-only evaluation"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "LongBench's MultiFieldQA ensures random evidence placement to avoid the positional biases documented in Lost in the Middle"
  - target: 2024-08-l-eval-standardized-evaluation
    type: concurrent
    detail: "L-Eval is a concurrent ACL 2024 long-context benchmark focused on manual sample curation and evaluation metric standardization"
  - target: 2024-10-ruler-context-size
    type: complementary
    detail: "RULER proposes synthetic controllable tasks complementing LongBench's natural-text approach"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong addresses reasoning in long contexts, citing LongBench's limitation to ~40K tokens and confounding with parametric knowledge"
  - target: 2025-07-longbench-v2
    type: extended-by
    detail: "LongBench v2 replaces extractive questions with harder human-annotated multiple-choice questions requiring deep reasoning, extends length coverage to 2M words"
  - target: 2026-01-longbench-pro
    type: extended-by
    detail: "LongBench Pro is the direct successor with broader task coverage, longer contexts, and multi-dimensional categorization"
  - target: 2025-03-longiclbench-long-in-context-learning
    type: complementary
    detail: "LongICLBench complements LongBench by requiring full-input comprehension via extreme-label ICL (28-174 classes, 2K-50K tokens) rather than retrieval-based tasks"
open_questions:
  - question: "Do LongBench results predict performance on tasks with contexts beyond 40K tokens?"
    addressed_by: 2026-01-longbench-pro
  - question: "Would LLM-as-examiner evaluation provide more reliable scores than automatic metrics like ROUGE-L and F1 for long-context tasks?"
    addressed_by: null
  - question: "How much does instruction-following capability confound long-context evaluation results?"
    addressed_by: null
---

# LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding

**Authors:** Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu, Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao Liu, Aohan Zeng, Lei Hou, Yuxiao Dong, Jie Tang, Juanzi Li (Tsinghua University, Zhipu.AI, Chinese Academy of Sciences)
**Date:** August 2024, ACL 2024 (arXiv:2308.14508)

---

## Core Research Problem

Although LLMs have demonstrated strong performance on many language tasks, most models at the time could only process texts a few thousand tokens long, limiting their application to longer inputs such as books, reports, and codebases. Recent methods -- context window extension (Press et al., 2022; Chen et al., 2023), recurrent memory (Dai et al., 2019; Bulatov et al., 2023), sparse attention (Ding et al., 2023; Mohtashami and Jaggi, 2023), and external memory augmentation (Liang et al., 2023; Zhou et al., 2023) -- have sought to improve long-context capabilities, but no comprehensive benchmark existed to evaluate them.

Prior evaluation relied primarily on **perplexity**, which does not necessarily reflect performance on downstream sequence-level tasks (Sun et al., 2021), or on **synthetic retrieval tasks** (Tay et al., 2021; Chen et al., 2023; Li et al., 2023) that fail to mirror real-world scenarios. Concurrent benchmarks -- ZeroSCROLLS (Shaham et al., 2022, 2023) and L-Eval (An et al., 2023) -- encompassed a restricted range of task types, limiting the diversity of long-dependency patterns tested. No benchmark offered bilingual coverage (English and Chinese), multitask breadth across realistic application scenarios, or controlled-length subsets for disentangling long-context ability from task ability.

**The core challenge is how to build a bilingual, multitask benchmark that comprehensively evaluates LLMs' long context understanding across diverse real-world tasks, lengths, and languages.**

---

## Problem Solutions

LongBench addresses this gap by introducing the first bilingual, multitask benchmark for long context understanding, comprising 21 datasets across 6 task categories in both English and Chinese.

1. **Broad task coverage.** Six major categories -- single-document QA, multi-document QA, summarization, few-shot learning, synthetic tasks, and code completion -- each testing different long-dependency patterns (local retrieval, global comprehension, multi-hop reasoning, in-context learning, code cross-reference).
2. **Bilingual design.** Both English and Chinese datasets in each applicable category, enabling evaluation of cross-lingual long-context capabilities.
3. **Controlled-length variant (LongBench-E).** A uniformly sampled subset of 13 English datasets with balanced length distributions across 0--4K, 4K--8K, and 8K+ word bins, disentangling context-length effects from task difficulty.
4. **Fully automated evaluation.** Standardized format with automatic metrics (F1, ROUGE-L, Edit Similarity, Accuracy) to avoid costly manual or API-based evaluation.

---

## Approach Details

### Method

LongBench formalizes long context understanding as: given input `I` and context `C`, the model produces answer `A`. In most tasks, `I` (question/query) and `A` (answer) are short, while `C` (document, code, or few-shot examples) extends to thousands or tens of thousands of tokens. The benchmark contains 4,750 test instances with an average length of 6,711 words (English) and 13,386 characters (Chinese).

### Key Technical Components

**Task taxonomy.** The 21 datasets are organized into 6 categories:

| Category | Dataset | Source | Avg Len | Metric | Language | #Data |
|---|---|---|---|---|---|---|
| Single-Doc QA | NarrativeQA | Literature, Film | 18,409 | F1 | EN | 200 |
| | Qasper | Science | 3,619 | F1 | EN | 200 |
| | MultiFieldQA-en | Multi-field | 4,559 | F1 | EN | 150 |
| | MultiFieldQA-zh | Multi-field | 6,701 | F1 | ZH | 200 |
| Multi-Doc QA | HotpotQA | Wikipedia | 9,151 | F1 | EN | 200 |
| | 2WikiMultihopQA | Wikipedia | 4,887 | F1 | EN | 200 |
| | MuSiQue | Wikipedia | 11,214 | F1 | EN | 200 |
| | DuReader | Baidu Search | 15,768 | ROUGE-L | ZH | 200 |
| Summarization | GovReport | Government | 8,734 | ROUGE-L | EN | 200 |
| | QMSum | Meeting | 10,614 | ROUGE-L | EN | 200 |
| | MultiNews | News | 2,113 | ROUGE-L | EN | 200 |
| | VCSUM | Meeting | 15,380 | ROUGE-L | ZH | 200 |
| Few-shot Learning | TREC | Web question | 5,177 | Accuracy (CLS) | EN | 200 |
| | TriviaQA | Wikipedia, Web | 8,209 | F1 | EN | 200 |
| | SAMSum | Dialogue | 6,258 | ROUGE-L | EN | 200 |
| | LSHT | News | 22,337 | Accuracy (CLS) | ZH | 200 |
| Synthetic | PassageCount | Wikipedia | 11,141 | Accuracy (EM) | EN | 200 |
| | PassageRetrieval-en | Wikipedia | 9,289 | Accuracy (EM) | EN | 200 |
| | PassageRetrieval-zh | C4 | 6,745 | Accuracy (EM) | ZH | 200 |
| Code | LCC | GitHub | 1,235 | Edit Sim | Py/C#/Java | 500 |
| | RepoBench-P | GitHub repo | 4,206 | Edit Sim | Py/Java | 500 |

Average length is measured in words for English/code datasets and characters for Chinese datasets (Table 1).

**Dataset construction.** Of the 21 datasets, 6 are extracted directly from existing test sets, 10 are adapted from existing datasets with modifications for long-context evaluation, and 5 are newly created and annotated (MultiFieldQA-en, MultiFieldQA-zh, PassageCount, PassageRetrieval-en, PassageRetrieval-zh) (Section 3.2).

- **Multi-doc QA adaptation:** Supporting Wikipedia passages are included first, then distracting passages are added until a maximum length is reached, and all passages are randomly ordered (Section 3.2.1).
- **Few-shot learning:** For each test instance, a random number of examples from the training set are concatenated as context `C`. Ranges: TREC [100, 600], LSHT [10, 40], SAMSum [10, 100], TriviaQA [2, 24] (Section 3.2.1).
- **MultiFieldQA annotation:** Documents collected from multiple sources (legal, government, encyclopedias, academic papers). Three PhD students annotated questions and answers, ensuring random placement of evidence paragraphs to avoid positional biases (Section 3.2.1).
- **PassageRetrieval:** 30 random passages are sampled; one is summarized by GPT-3.5-Turbo. The model must identify which passage the summary corresponds to (Section 3.2.1).
- **PassageCount:** N unique passages from Wikipedia are sampled, each repeated a random number of times, then shuffled. The model must count the number of unique passages. N is drawn from [2, M] where M is in [17, 50]. M total passages are produced by sampling with replacement from the N unique ones (Section 3.2.1).

**LongBench-E.** A subset of 13 English datasets uniformly sampled by word count into three bins (0--4K, 4K--8K, 8K+), with ~100 samples per bin per dataset (Table 8), enabling per-length-range analysis that disentangles context length from task difficulty.

**Truncation strategy.** When input length `L` exceeds maximum context length `M`, the input is truncated from the middle to preserve both instruction/question (at the front) and potential tail information:

> S_{1:L} → [S_{1:⌊M/2⌋}; S_{L-⌊M/2⌋-1:L}]

**Evaluation protocol.** Zero-shot setting for all tasks except few-shot learning (where examples form the long context). Greedy decoding for reproducibility. Chat-specific prompts are omitted for few-shot and code tasks to elicit completion-style responses (Section 4.1).

### Experimental Setup

**Models (8):**
- GPT-3.5-Turbo-16k (commercial, 16K context)
- Llama2-7B-chat-4k (4K context)
- LongChat-v1.5-7B-32k (fine-tuned from Llama2-7B, linear RoPE scaling, 32K)
- XGen-7B-8k (8K context)
- InternLM-7B-8k (8K context)
- ChatGLM2-6B (base, ~4K effective)
- ChatGLM2-6B-32k (position interpolation + 32K alignment training, based on ChatGLM2-6B)
- Vicuna-v1.5-7B-16k (fine-tuned from Llama2-7B, linear RoPE scaling, 16K)

**Context compression experiments:** Three retrievers (text-embedding-ada-002, Contriever, BM25) with two chunk sizes (200 and 500 words), top-7 and top-3 chunks respectively. Also summarization-based compression via model-generated chunk summaries (Section 4.2).

### Key Results

**Overall performance (macro-average across 6 categories, Tables 2-3):**

| Model | EN | ZH | All |
|---|---|---|---|
| GPT-3.5-Turbo-16k | 44.0 | 44.5 | 44.7 |
| ChatGLM2-6B-32k | 40.9 | 41.7 | 41.4 |
| LongChat-v1.5-7B-32k | 34.3 | 23.9 | 31.6 |
| Vicuna-v1.5-7B-16k | 31.9 | 26.4 | 30.5 |
| Llama2-7B-chat-4k | 31.0 | 14.3 | 26.8 |
| ChatGLM2-6B | 26.6 | 22.9 | 25.7 |
| XGen-7B-8k | 28.3 | 15.1 | 25.0 |
| InternLM-7B-8k | 24.2 | 18.3 | 22.6 |

Overall is computed as the macro-average (mean of per-category averages) over 6 major task categories. Code tasks are included in both EN and ZH scores (Table 3).

- **GPT-3.5-Turbo-16k leads overall** but still struggles on longer contexts (−17% from 0--4K to 8K+ on LongBench-E, Figure 3).
- **Scaled positional embedding and longer fine-tuning help substantially.** ChatGLM2-6B-32k (position interpolation + 32K alignment) improves 62% over ChatGLM2-6B; LongChat-v1.5-7B-32k (linear RoPE scaling) improves 19% over Llama2-7B-chat-4k (Section 4.1).
- **ChatGLM2-6B-32k and LongChat-v1.5-7B-32k are most robust to length increases** on LongBench-E, with relative drops of only 4% and 7% from 0--4K to 8K+ (Figure 3, Section 4.1).
- **Synthetic tasks are highly discriminating:** models either achieve high scores (e.g., ChatGLM2-6B-32k: 77.0% on PassageRetrieval-en) or near-zero (e.g., Llama2-7B-chat-4k: 9.8%), suggesting that simple averaging may let these tasks dominate rankings (Tables 2-3, Appendix D).
- **Higher inter-task correlations within same category and language** (Spearman analysis, Appendix D). Chinese tasks (1-4, 2-4, 3-4, 4-4, 5-3) correlate highly with each other. PassageCount (5-1) has low correlation with all other tasks since most models score near zero.

**Truncation experiment (LongBench, macro-average, Figure 2):**

| Model | Max Length | 8K Trunc. | 4K Trunc. |
|---|---|---|---|
| GPT-3.5-Turbo-16k | 44.7 | 44.2 | 39.1 |
| ChatGLM2-6B-32k | 41.5 | 39.3 | 35.4 |
| Vicuna-v1.5-7B-16k | 30.5 | 30.5 | 30.2 |

GPT-3.5-Turbo-16k and ChatGLM2-6B-32k benefit from longer context, confirming that LongBench tasks genuinely require long-context modeling. Vicuna-v1.5-7B-16k shows no improvement, indicating it does not effectively use context beyond 4K (Section 4.1).

**Retrieval-based compression (best retriever per model, QA tasks avg, Table 4):**

| Model | w/o Retrieval | Best Retrieval | Delta |
|---|---|---|---|
| GPT-3.5-Turbo-16k | 40.7 | 39.9 | −2% |
| Llama2-7B-chat-4k | 19.9 | 24.0 | +21% |
| ChatGLM2-6B-32k | 36.1 | 34.4 | −5% |

- **text-embedding-ada-002 is the best retriever**, followed by Contriever, then BM25 (Table 4).
- **Retrieval helps only weak long-context models.** Llama2-7B-chat-4k gains +21%, but even with retrieval its performance lags behind stronger models without retrieval. Models with strong long-context ability (GPT-3.5-Turbo-16k, ChatGLM2-6B-32k) are slightly harmed by retrieval (Section 4.2).
- **Smaller chunks with more retrieved segments** (200 words × 7 chunks) outperform larger chunks (500 × 3) (Table 4).

**Summarization-based compression (Table 5):**

| Model | w/o Summ | w/ Summ |
|---|---|---|
| GPT-3.5-Turbo-16k | 23.9 | 18.0 |
| Llama2-7B-chat-4k | 18.5 | 8.6 |
| ChatGLM2-6B-32k | 24.8 | 16.4 |

Summarization-based compression degrades performance on 3 of 4 summarization tasks. Only VCSUM (the longest dataset at avg 15,380 characters) sees slight improvement for GPT-3.5-Turbo-16k and ChatGLM2-6B-32k (Section 4.2).

**Context understanding vs. memorization (Table 6):** When context is withheld and only the question is presented, performance on Wikipedia-based tasks (HotpotQA, 2WikiMultihopQA, MuSiQue) remains relatively high, indicating models rely partly on parametric knowledge from pretraining. The delta (score with context minus score without) serves as a purer measure of context understanding ability. For GPT-3.5-Turbo-16k, the largest deltas are on MultiFieldQA-zh (+50.3) and MultiFieldQA-en (+36.6), while multi-doc QA deltas are smaller (+8.8 to +19.9), reflecting Wikipedia memorization (Section 4.3).

---

## Limitations and Failure Modes

1. **Automatic metrics (ROUGE-L, F1) may underestimate models that generate longer responses.** Using LLM-as-examiner could reduce this problem but introduces its own biases and costs (Section 6).
2. **Performance is coupled with instruction-following capability.** The benchmark aims to test long-context modeling, but real-world tasks inevitably require instruction comprehension. Performance on LongBench is confounded with models' instruction-following ability (Section 6).
3. **Maximum length reaches ~40K tokens.** LongBench does not test contexts beyond tens of thousands of tokens, limiting evaluation of models claiming 100K+ context windows.
4. **Synthetic tasks have near-binary discriminability.** Models either achieve high scores or near-zero on PassageCount and PassageRetrieval, reducing the granularity of differentiation on these tasks (Appendix D).
5. **Summarization and code completion are insufficiently discerning.** Similarity-based metrics (ROUGE-L, Edit Sim) on these tasks do not well distinguish between strong and weak models (Appendix C).

---

## Conclusions

### Contributions

1. **First bilingual, multitask long-context benchmark.** LongBench provides 21 datasets across 6 task categories in English and Chinese, with 4,750 test instances averaging 6,711 words (EN) and 13,386 characters (ZH), filling the gap of comprehensive long-context evaluation (Table 1).
2. **Controlled-length evaluation variant.** LongBench-E provides uniformly sampled data across three length bins (0--4K, 4K--8K, 8K+) for 13 English tasks, enabling analysis that disentangles context length effects from task difficulty (Table 8, Figure 3).
3. **Systematic context compression analysis.** Retrieval-based compression with three retrievers and two chunk sizes, plus summarization-based compression, showing retrieval helps only weak models and is not a shortcut to solving long-context understanding (Tables 4-5).
4. **Memorization vs. understanding decomposition.** Context-withheld experiments quantifying the contribution of parametric knowledge vs. genuine context understanding, revealing that Wikipedia-based tasks are substantially solvable through memorization (Table 6).

### Implications

1. **Position extension is effective but insufficient.** While position interpolation and longer fine-tuning yield large gains (62% for ChatGLM2-6B-32k), even the best models still degrade on longer contexts, suggesting further improvements in long-context modeling are needed.
2. **Retrieval is not a shortcut.** Retrieval-based compression cannot replace strong native long-context ability; even the best retriever (ada-002) slightly harms models that already handle long contexts well.
3. **Per-category evaluation is more meaningful than overall averaging.** Synthetic tasks exhibit near-binary discriminability, so averaging across all tasks may let these dominate rankings. LongBench's category-level reporting provides more nuanced benchmarking.
4. **Bilingual evaluation reveals important differences.** Some models (Llama2-7B-chat-4k, XGen-7B-8k) show large EN-ZH gaps (31.0 vs. 14.3 and 28.3 vs. 15.1), suggesting long-context capability does not transfer equally across languages (Tables 2-3).

---

## Key Claims

1. **C1: First bilingual, multi-task long-context benchmark.** LongBench provides 21 datasets across 6 categories in English and Chinese. No prior benchmark combined bilingual coverage, multitask breadth, and controlled-length subsets (Table 1, Section 1). **Status: supported.**

2. **C2: GPT-3.5-Turbo-16k leads but degrades on longer contexts.** GPT-3.5-Turbo-16k achieves the highest overall macro-average (44.7%) but drops 17% from 0--4K to 8K+ on LongBench-E (Tables 2-3, Figure 3). **Status: supported.**

3. **C3: Position interpolation and longer fine-tuning yield large gains.** ChatGLM2-6B-32k improves 62% over ChatGLM2-6B; LongChat-v1.5-7B-32k improves 19% over Llama2-7B-chat-4k (Tables 2-3, Section 4.1). **Status: supported.**

4. **C4: Retrieval-based compression helps only weak models.** Llama2-7B-chat-4k gains +21% with best retrieval, but GPT-3.5-Turbo-16k loses 2% and ChatGLM2-6B-32k loses 5% (Table 4, Section 4.2). **Status: supported.**

5. **C5: Models trained on longer contexts are most robust to length increases.** ChatGLM2-6B-32k and LongChat-v1.5-7B-32k show relative drops of only 4% and 7% from 0--4K to 8K+ on LongBench-E, while GPT-3.5-Turbo-16k drops 17% (Figure 3, Section 4.1). **Status: supported.**

6. **C6: Wikipedia-based tasks are partially solvable through memorization.** Without context, GPT-3.5-Turbo-16k scores 31.7 on HotpotQA and 28.9 on 2WikiMultihopQA, compared to 4.7 on NarrativeQA. The delta metric provides a purer measure of context understanding (Table 6, Section 4.3). **Status: supported.**

7. **C7: Synthetic tasks have near-binary discriminability.** On PassageRetrieval-en, scores range from 3.0% (ChatGLM2-6B) to 77.0% (ChatGLM2-6B-32k); on PassageCount, all models score below 6.5% except none. Simple averaging across all tasks would let these extremes dominate rankings (Tables 2-3, Appendix D). **Status: supported.**

---

## Open Questions

1. **Do LongBench results predict performance on tasks with contexts beyond 40K tokens?** LongBench's maximum context length is ~40K tokens; models claiming 100K+ windows cannot be fully evaluated. *Addressed by:* Bai et al. (2025) -- *LongBench v2* and Bai et al. (2026) -- *LongBench Pro* extend to longer contexts.

2. **Would LLM-as-examiner evaluation provide more reliable scores than automatic metrics like ROUGE-L and F1?** The authors acknowledge that automatic metrics may underestimate models generating longer responses (Section 6), but LLM-based evaluation introduces its own biases and cost. *Unresolved.*

3. **How much does instruction-following capability confound long-context evaluation results?** The benchmark couples long-context modeling with instruction comprehension, making it difficult to isolate long-context ability (Section 6). *Unresolved.*

---

## Core References and Why They Are Referenced

### Prior Long-Context Evaluation Benchmarks

- **Shaham et al. (2022)** -- *SCROLLS.* Prior long-context benchmark based on fine-tuning. LongBench argues SCROLLS covers a restricted range of task types, limiting the diversity of long-dependency patterns tested.
- **Shaham et al. (2023)** -- *ZeroSCROLLS.* Concurrent zero-shot long-context benchmark. LongBench contrasts itself as providing broader task coverage, bilingual support, and controlled-length subsets.
- **An et al. (2023)** -- *L-Eval.* Concurrent evaluation benchmark for long text modeling. LongBench contrasts with broader task diversity, while L-Eval focuses on manual sample curation and metric standardization.
- **Tay et al. (2021)** -- *Long Range Arena.* Benchmark for efficient transformers using synthetic tasks. LongBench argues synthetic-only evaluation does not mirror real-world scenarios.

### Context Extension and Long-Context Methods

- **Chen et al. (2023)** -- *Positional Interpolation.* The context extension method used in ChatGLM2-6B-32k. LongBench's results show that position interpolation combined with longer fine-tuning produces a 62% improvement.
- **Press et al. (2022)** -- *ALiBi.* Length extrapolation via linear biases. Referenced as part of the context extension landscape that LongBench evaluates.
- **Li et al. (2023)** -- *LongChat.* Fine-tuned Llama2-7B with linear RoPE scaling and 32K context. One of the eight models evaluated in LongBench.

### Source Datasets

- **Yang et al. (2018)** -- *HotpotQA.* Source of 2-hop multi-document QA data.
- **Ho et al. (2020)** -- *2WikiMultihopQA.* Source of up-to-5-hop multi-document QA data.
- **Trivedi et al. (2022)** -- *MuSiQue.* Source of up-to-4-hop multi-document QA with shortcut-resistant questions.
- **Kociskỳ et al. (2018)** -- *NarrativeQA.* Source of single-document QA over long stories.
- **Dasigi et al. (2021)** -- *Qasper.* Source of QA over NLP papers.
- **Huang et al. (2021)** -- *GovReport.* Source of government report summarization data.
- **Zhong et al. (2021)** -- *QMSum.* Source of query-based meeting summarization data.
- **Fabbri et al. (2019)** -- *MultiNews.* Source of multi-document news summarization data.
- **Liu et al. (2023b)** -- *RepoBench.* Source of repository-level code completion data.
- **Guo et al. (2023)** -- *LongCoder/LCC.* Source of long code completion data.
- **He et al. (2018)** -- *DuReader.* Source of Chinese reading comprehension data from Baidu Search.

### Models Evaluated

- **OpenAI (2022)** -- *GPT-3.5-Turbo-16k.* The top-performing commercial model on LongBench (44.7% overall).
- **Touvron et al. (2023)** -- *Llama 2.* Base model for LongChat and Vicuna fine-tuned variants; evaluated directly as Llama2-7B-chat-4k.
- **Du et al. (2022); Zeng et al. (2023)** -- *GLM/ChatGLM2.* Base model and its 32K-extended variant demonstrating the largest gains from position interpolation (+62%).

### Evaluation and Analysis

- **Liu et al. (2023a)** -- *Lost in the Middle.* Referenced for positional bias in evidence placement. LongBench's MultiFieldQA annotation ensures random evidence placement.
- **Sun et al. (2021)** -- *Do Long-Range Language Models Actually Use Long-Range Context?* Referenced for showing that perplexity may not reflect performance on sequence-level tasks.
- **Yu et al. (2024)** -- *KoLA.* Referenced for the delta-score approach to disentangling memorization from context understanding (Section 4.3).
