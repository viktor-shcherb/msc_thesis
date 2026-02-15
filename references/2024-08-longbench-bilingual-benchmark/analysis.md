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
    scope: "English and Chinese, 6 task categories, up to ~40K tokens"
    magnitude: "21 datasets, 4,750 test instances, avg 6,711 words (EN) / 13,386 chars (ZH)"
  - id: C2
    claim: "GPT-3.5-Turbo-16k outperforms open-source models overall (44.7%) but degrades 17% from 0-4K to 8K+ on LongBench-E"
    evidence: "Tables 2-3, Figure 3, Section 4.1"
    status: supported
    scope: "8 models at 6B-7B open-source scale plus one commercial model, greedy decoding, zero-shot except few-shot tasks"
    magnitude: "44.7% overall macro-average; -17% relative drop from 0-4K to 8K+ (51.5 to 42.4)"
  - id: C3
    claim: "Position interpolation and longer fine-tuning yield up to 62% relative improvement (ChatGLM2-6B-32k over ChatGLM2-6B) and 19% (LongChat-v1.5-7B-32k over Llama2-7B-chat-4k)"
    evidence: "Tables 2-3, Section 4.1"
    status: supported
    scope: "6B-7B parameter models, position interpolation with 32K alignment training"
    magnitude: "62% relative improvement (25.7 to 41.4) and 19% relative improvement (26.8 to 31.6)"
  - id: C4
    claim: "Retrieval-based compression helps only models with weak long-context ability (+21% for Llama2-7B-chat-4k) but slightly degrades strong models (-2% GPT-3.5-Turbo-16k, -5% ChatGLM2-6B-32k)"
    evidence: "Table 4, Section 4.2"
    status: supported
    scope: "QA tasks only (single-doc and multi-doc), 3 retrievers, 2 chunk sizes, 3 models tested"
    magnitude: "+21% (19.9 to 24.0), -2% (40.7 to 39.9), -5% (36.1 to 34.4)"
  - id: C5
    claim: "Models trained on longer contexts (ChatGLM2-6B-32k, LongChat-v1.5-7B-32k) are most robust to length increases on LongBench-E, with relative drops of only 4% and 7% from 0-4K to 8K+"
    evidence: "Figure 3, Table 9, Section 4.1"
    status: supported
    scope: "13 English datasets in LongBench-E, 3 length bins, macro-average"
    magnitude: "4% relative drop (44.2 to 43.1) and 7% relative drop (36.9 to 34.5) vs 17% for GPT-3.5-Turbo-16k"
  - id: C6
    claim: "Wikipedia-based multi-doc QA tasks show high memorization scores without context, indicating models partly rely on parametric knowledge rather than context understanding"
    evidence: "Table 6, Section 4.3"
    status: supported
    scope: "GPT-3.5-Turbo-16k, Llama2-7B-chat-4k, ChatGLM2-6B-32k on single-doc and multi-doc QA"
    magnitude: "GPT-3.5-Turbo-16k scores 31.7 (HotpotQA) and 28.9 (2WikiMQA) without context vs 4.7 (NarrativeQA)"
  - id: C7
    claim: "Synthetic tasks exhibit near-binary discriminability, making simple averaging across all tasks potentially misleading for ranking models"
    evidence: "Tables 2-3, Appendix C-D"
    status: supported
    scope: "PassageCount and PassageRetrieval tasks across 8 models"
    magnitude: "PassageRetrieval-en scores range from 3.0% (ChatGLM2-6B) to 77.0% (ChatGLM2-6B-32k); PassageCount all models below 6.5%"
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
  - target: 2025-04-helmet-long-context-evaluation
    type: extended-by
    detail: "HELMET extends beyond LongBench's limited context lengths and adds controllable length evaluation with more diverse task categories"
  - target: 2026-01-longbench-pro
    type: extended-by
    detail: "LongBench Pro is the direct successor with broader task coverage, longer contexts, and multi-dimensional categorization"
  - target: 2025-03-longiclbench-long-in-context-learning
    type: complementary
    detail: "LongICLBench complements LongBench by requiring full-input comprehension via extreme-label ICL (28-174 classes, 2K-50K tokens) rather than retrieval-based tasks"
  - target: 2025-05-100-longbench-long-context-benchmarks
    type: extended-by
    detail: "100-LongBench restructures LongBench datasets with controllable-length context and proposes the LongScore metric to disentangle base ability from long-context capability"
  - target: 2025-07-lv-eval-long-context-benchmark
    type: concurrent
    detail: "LV-Eval uses MultiFieldQA datasets from LongBench, extends evaluation to 256k words with five controlled length levels, and adds knowledge-leakage mitigation via keyword replacement"
  - target: 2024-11-genuinely-difficult-long-context
    type: complementary
    detail: "Goldman et al. classify LongBench tasks (MultiFieldQA, PassageCount, PassageRetrieval) across multiple quadrants of their scope-dispersion taxonomy"
  - target: 2025-04-longgenbench-long-form-generation
    type: complementary
    detail: "LongGenBench evaluates long-output generation (16K-32K tokens), complementing LongBench's focus on long-input understanding; both address different aspects of long-context capability"
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

LongBench formalizes long context understanding as: given input `I` and context `C`, the model produces answer `A`. In most tasks, `I` (question/query) and `A` (answer) are short, while `C` (document, code, or few-shot examples) extends to thousands or tens of thousands of tokens. The benchmark contains 4,750 test instances with an average length of 6,711 words (English) and 13,386 characters (Chinese) (Table 1).

### Key Technical Components

**Task taxonomy.** The 21 datasets are organized into 6 categories (Table 1):

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
| Summarization | GovReport | Government report | 8,734 | ROUGE-L | EN | 200 |
| | QMSum | Meeting | 10,614 | ROUGE-L | EN | 200 |
| | MultiNews | News | 2,113 | ROUGE-L | EN | 200 |
| | VCSUM | Meeting | 15,380 | ROUGE-L | ZH | 200 |
| Few-shot Learning | TREC | Web question | 5,177 | Accuracy (CLS) | EN | 200 |
| | TriviaQA | Wikipedia, Web | 8,209 | F1 | EN | 200 |
| | SAMSum | Dialogue | 6,258 | ROUGE-L | EN | 200 |
| | LSHT | News | 22,337 | Accuracy (CLS) | ZH | 200 |
| Synthetic | PassageCount | Wikipedia | 11,141 | Accuracy (EM) | EN | 200 |
| | PassageRetrieval-en | Wikipedia | 9,289 | Accuracy (EM) | EN | 200 |
| | PassageRetrieval-zh | C4 Dataset | 6,745 | Accuracy (EM) | ZH | 200 |
| Code | LCC | GitHub | 1,235 | Edit Sim | Py/C#/Java | 500 |
| | RepoBench-P | GitHub repository | 4,206 | Edit Sim | Py/Java | 500 |

Average length is measured in words for English/code datasets and characters for Chinese datasets (Table 1).

**Dataset construction.** Of the 21 datasets, 6 are extracted directly from existing test sets, 10 are adapted from existing datasets with modifications for long-context evaluation, and 5 are newly created and annotated (MultiFieldQA-en, MultiFieldQA-zh, PassageCount, PassageRetrieval-en, PassageRetrieval-zh) (Section 3.2).

- **Multi-doc QA adaptation:** Supporting Wikipedia passages are included first, then distracting passages are added until a maximum length is reached, and all passages are randomly ordered (Section 3.2.1).
- **Few-shot learning:** For each test instance, a random number of examples from the training set are concatenated as context `C`. Ranges: TREC [100, 600], LSHT [10, 40], SAMSum [10, 100], TriviaQA [2, 24] (Section 3.2.1).
- **MultiFieldQA annotation:** Documents collected from multiple sources (legal, government, encyclopedias, academic papers). Three PhD students annotated questions and answers, with 100% cross-validation accuracy. Evidence paragraphs are randomly placed to avoid positional biases (Section 3.2.1, Appendix A).
- **PassageRetrieval:** 30 random passages are sampled; one is summarized by GPT-3.5-Turbo. The model must identify which passage the summary corresponds to (Section 3.2.1).
- **PassageCount:** M passages are produced by sampling with replacement from N unique Wikipedia passages (N drawn from [2, M], M drawn from [17, 50]), then shuffled. The model must count the number of unique passages (Section 3.2.1).

**LongBench-E.** A subset of 13 English datasets uniformly sampled by word count into three bins (0--4K, 4K--8K, 8K+), with ~100 samples per bin per dataset (Table 8), enabling per-length-range analysis that disentangles context length from task difficulty.

**Truncation strategy.** When input length `L` exceeds maximum context length `M`, the input is truncated from the middle to preserve both instruction/question (at the front) and potential tail information (Section 4.1):

> S_{1:L} -> [S_{1:floor(M/2)}; S_{L-floor(M/2)-1:L}]

**Evaluation protocol.** Zero-shot setting for all tasks except few-shot learning (where examples form the long context). Greedy decoding for reproducibility. Chat-specific prompts are omitted for few-shot and code tasks to elicit completion-style responses (Section 4.1). For few-shot learning, the first line of the response is extracted; for code completion, the first non-comment line is extracted (Section 4.1).

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

All open-source models are in the 6B-7B parameter range. Single commercial model (GPT-3.5-Turbo-16k). No variance estimates reported; single run per configuration (limited evidence for individual scores).

**Context compression experiments:** Three retrievers (text-embedding-ada-002, Contriever, BM25) with two chunk sizes (200 and 500 words), top-7 and top-3 chunks respectively. Also summarization-based compression via model-generated chunk summaries (Section 4.2).

**Reproducibility:** Code and datasets publicly available at https://github.com/THUDM/LongBench and https://huggingface.co/datasets/THUDM/LongBench. Greedy decoding ensures deterministic outputs. No random seeds reported (deterministic via greedy decoding). Evaluation prompts are fully specified in Appendix B.

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

Overall is computed as the macro-average (mean of per-category averages) over 6 major task categories. Code tasks are included in both EN and ZH scores (Table 3). Results are from 8 models at 6B-7B open-source scale plus one commercial model, with single runs per configuration and no variance estimates.

- **GPT-3.5-Turbo-16k leads overall** but still struggles on longer contexts: -17% relative from 0--4K (51.5) to 8K+ (42.4) on LongBench-E (Figure 3, Table 9).
- **Scaled positional embedding and longer fine-tuning help substantially.** ChatGLM2-6B-32k (position interpolation + 32K alignment) improves 62% over ChatGLM2-6B (41.4 vs 25.7); LongChat-v1.5-7B-32k (linear RoPE scaling) improves 19% over Llama2-7B-chat-4k (31.6 vs 26.8) (Tables 2-3, Section 4.1; 8 models, single configuration each -- moderate evidence).
- **ChatGLM2-6B-32k and LongChat-v1.5-7B-32k are most robust to length increases** on LongBench-E, with relative drops of only 4% and 7% from 0--4K to 8K+ (Figure 3, Table 9).
- **Synthetic tasks are highly discriminating:** models either achieve high scores (e.g., ChatGLM2-6B-32k: 77.0% on PassageRetrieval-en) or near-zero (e.g., Llama2-7B-chat-4k: 9.8%), suggesting that simple averaging may let these tasks dominate rankings (Tables 2-3, Appendix C-D).
- **Higher inter-task correlations within same category and language** (Spearman analysis, Appendix D). Chinese tasks (1-4, 2-4, 3-4, 4-4, 5-3) correlate highly with each other. PassageCount (5-1) has low correlation with all other tasks since most models score near zero. Qasper (1-2) and RepoBench-P (6-2) also show lower correlations with other tasks, implying different attention patterns.

**Truncation experiment (LongBench, macro-average, Figure 2):**

| Model | Max Length | 8K Trunc. | 4K Trunc. |
|---|---|---|---|
| GPT-3.5-Turbo-16k | 44.7 | 41.5 | 39.1 |
| ChatGLM2-6B-32k | 41.4 | 39.3 | 35.4 |
| Vicuna-v1.5-7B-16k | 30.2 | 30.3 | 30.5 |

GPT-3.5-Turbo-16k and ChatGLM2-6B-32k benefit from longer context, confirming that LongBench tasks genuinely require long-context modeling. Vicuna-v1.5-7B-16k shows no improvement with increasing context length (essentially flat from 30.5 at 4K to 30.2 at max), indicating it does not effectively use context beyond 4K (Section 4.1; 3 models tested, limited evidence for generalization).

**Retrieval-based compression (best retriever per model, QA tasks avg, Table 4):**

| Model | w/o Retrieval | Best Retrieval | Delta |
|---|---|---|---|
| GPT-3.5-Turbo-16k | 40.7 | 39.9 | -2% |
| Llama2-7B-chat-4k | 19.9 | 24.0 | +21% |
| ChatGLM2-6B-32k | 36.1 | 34.4 | -5% |

- **text-embedding-ada-002 is the best retriever**, followed by Contriever, then BM25 (Table 4).
- **Retrieval helps only weak long-context models.** Llama2-7B-chat-4k gains +21%, but even with retrieval its performance (24.0) lags behind ChatGLM2-6B-32k without retrieval (36.1). Models with strong long-context ability (GPT-3.5-Turbo-16k, ChatGLM2-6B-32k) are slightly harmed by retrieval (Section 4.2; 3 models, QA tasks only -- moderate evidence for the specific finding, limited generalizability to other task types).
- **Smaller chunks with more retrieved segments** (200 words x 7 chunks) outperform larger chunks (500 x 3) (Table 4).

**Summarization-based compression (Table 5):**

| Model | 3-1 (GovReport) | 3-2 (QMSum) | 3-3 (MultiNews) | 3-4 (VCSUM) | Avg |
|---|---|---|---|---|---|
| GPT-3.5-Turbo-16k | 29.5 | 23.4 | 26.7 | 16.0 | 23.9 |
| GPT-3.5-Turbo-16k+Summ | 17.9 | 16.6 | 17.9 | 19.7 | 18.0 |
| Llama2-7B-chat-4k | 27.3 | 20.8 | 25.8 | 0.2 | 18.5 |
| Llama2-7B-chat-4k+Summ | 12.8 | 16.6 | 4.6 | 0.6 | 8.6 |
| ChatGLM2-6B-32k | 32.4 | 24.0 | 26.5 | 16.2 | 24.8 |
| ChatGLM2-6B-32k+Summ | 17.6 | 15.9 | 14.9 | 17.2 | 16.4 |

Summarization-based compression degrades performance on 3 of 4 summarization tasks for all models. Only VCSUM (3-4, the longest dataset at avg 15,380 characters) sees slight improvement for GPT-3.5-Turbo-16k (16.0 to 19.7) and ChatGLM2-6B-32k (16.2 to 17.2) (Section 4.2, Table 5).

**Context understanding vs. memorization (Table 6):** When context is withheld and only the question is presented, performance on Wikipedia-based tasks (HotpotQA, 2WikiMultihopQA, MuSiQue) remains relatively high, indicating models rely partly on parametric knowledge from pretraining. The delta (score with context minus score without) serves as a purer measure of context understanding ability (Yu et al., 2024). Selected results for GPT-3.5-Turbo-16k (Table 6):

| Dataset | w/o Context | w/ Context | Delta |
|---|---|---|---|
| NarrativeQA | 4.7 | 23.6 | +18.9 |
| Qasper | 12.4 | 43.3 | +30.9 |
| MultiFieldQA-en | 15.7 | 52.3 | +36.6 |
| MultiFieldQA-zh | 10.9 | 61.2 | +50.3 |
| HotpotQA | 31.7 | 51.6 | +19.9 |
| 2WikiMultihopQA | 28.9 | 37.7 | +8.8 |
| MuSiQue | 15.0 | 26.9 | +11.9 |
| DuReader | 17.1 | 28.7 | +11.6 |

The largest deltas are on MultiFieldQA-zh (+50.3) and MultiFieldQA-en (+36.6), while multi-doc QA deltas are smaller (+8.8 to +19.9), reflecting Wikipedia memorization. Similar patterns hold for Llama2-7B-chat-4k and ChatGLM2-6B-32k (Table 6; 3 models tested -- moderate evidence, but only QA tasks examined).

---

## Limitations and Failure Modes

1. **Automatic metrics (ROUGE-L, F1) may underestimate models that generate longer responses.** Using LLM-as-examiner could reduce this problem but introduces its own biases and costs (Section 6, Limitation 1).
2. **Performance is coupled with instruction-following capability.** The benchmark aims to test long-context modeling, but real-world tasks inevitably require instruction comprehension. Performance on LongBench is confounded with models' instruction-following ability (Section 6, Limitation 2).
3. **[Inferred] Maximum length reaches only ~40K tokens.** LongBench does not test contexts beyond tens of thousands of tokens, limiting evaluation of models claiming 100K+ context windows. The length distribution (Figure 1) is heavily right-skewed with most instances under 10,000 words.
4. **[Inferred] Synthetic tasks have near-binary discriminability.** Models either achieve high scores or near-zero on PassageCount and PassageRetrieval, reducing the granularity of differentiation on these tasks (Appendix C-D).
5. **[Inferred] Summarization and code completion are insufficiently discerning.** Similarity-based metrics (ROUGE-L, Edit Sim) on these tasks do not well distinguish between strong and weak models, as noted in the radar plot analysis (Appendix C).
6. **[Inferred] No variance estimates or repeated runs.** All results are from single runs with greedy decoding. While greedy decoding is deterministic, different prompt phrasings or evaluation orderings could affect results.

#### Scope and Comparability

- **What was not tested:** No models larger than 16K context (commercial) or 32K (open-source) are evaluated at the time of publication; no models above 7B parameters (open-source). Evaluation is zero-shot only (except few-shot learning tasks). No chain-of-thought or multi-turn evaluation. No evaluation of retrieval-augmented generation on non-QA tasks.
- **Comparability notes:** LongBench's "overall" macro-average weights all 6 task categories equally regardless of number of tasks per category, which differs from simple averaging across all 21 tasks. The controlled-length variant (LongBench-E) uses word count for binning, which may not correspond to tokenizer-specific token counts. Context compression experiments (Table 4) are restricted to QA tasks, making direct comparison with full-benchmark results difficult. The truncation strategy (middle truncation) differs from the left truncation used by some other benchmarks, potentially affecting comparability of truncation-sensitivity results.

---

## Conclusions

### Contributions

1. **First bilingual, multitask long-context benchmark.** LongBench provides 21 datasets across 6 task categories in English and Chinese, with 4,750 test instances averaging 6,711 words (EN) and 13,386 characters (ZH), filling the gap of comprehensive long-context evaluation (Table 1).
2. **Controlled-length evaluation variant.** LongBench-E provides uniformly sampled data across three length bins (0--4K, 4K--8K, 8K+) for 13 English tasks, enabling analysis that disentangles context length effects from task difficulty (Table 8, Figure 3).
3. **Systematic context compression analysis.** Retrieval-based compression with three retrievers and two chunk sizes, plus summarization-based compression, showing retrieval helps only weak models and is not a shortcut to solving long-context understanding (Tables 4-5).
4. **Memorization vs. understanding decomposition.** Context-withheld experiments quantifying the contribution of parametric knowledge vs. genuine context understanding, revealing that Wikipedia-based tasks are substantially solvable through memorization (Table 6).

### Implications

1. **Position extension is effective but insufficient.** While position interpolation and longer fine-tuning yield large gains (62% for ChatGLM2-6B-32k), even the best models still degrade on longer contexts, suggesting further improvements in long-context modeling are needed.
2. **Retrieval is not a shortcut.** Retrieval-based compression cannot replace strong native long-context ability; even the best retriever (ada-002) slightly harms models that already handle long contexts well (Table 4).
3. **Per-category evaluation is more meaningful than overall averaging.** Synthetic tasks exhibit near-binary discriminability, so averaging across all tasks may let these dominate rankings. LongBench's category-level reporting provides more nuanced benchmarking (Appendix C).
4. **Bilingual evaluation reveals important differences.** Some models (Llama2-7B-chat-4k, XGen-7B-8k) show large EN-ZH gaps (31.0 vs. 14.3 and 28.3 vs. 15.1), suggesting long-context capability does not transfer equally across languages (Tables 2-3).

---

## Key Claims

1. **C1: First bilingual, multi-task long-context benchmark.** LongBench provides 21 datasets across 6 categories in English and Chinese. No prior benchmark combined bilingual coverage, multitask breadth, and controlled-length subsets (Table 1, Section 1). **Scope:** English and Chinese, 6 task categories, up to ~40K tokens. **Magnitude:** 21 datasets, 4,750 test instances. **Status: supported** (benchmark novelty verifiable by comparison with prior work; limited to EN/ZH bilingual scope).

2. **C2: GPT-3.5-Turbo-16k leads but degrades on longer contexts.** GPT-3.5-Turbo-16k achieves the highest overall macro-average (44.7%) but drops 17% from 0--4K (51.5) to 8K+ (42.4) on LongBench-E (Tables 2-3, Figure 3, Table 9). **Scope:** 8 models at 6B-7B scale + 1 commercial, greedy decoding, zero-shot. **Magnitude:** 44.7% overall; 17% relative degradation. **Status: supported** (8 models evaluated, single run per configuration -- moderate evidence).

3. **C3: Position interpolation and longer fine-tuning yield large gains.** ChatGLM2-6B-32k improves 62% over ChatGLM2-6B (41.4 vs 25.7); LongChat-v1.5-7B-32k improves 19% over Llama2-7B-chat-4k (31.6 vs 26.8) (Tables 2-3, Section 4.1). **Scope:** 6B-7B models, position interpolation + alignment training. **Magnitude:** 62% and 19% relative improvement. **Status: supported** (2 model pairs compared, no ablation isolating position interpolation from fine-tuning -- limited evidence for isolating the mechanism).

4. **C4: Retrieval-based compression helps only weak models.** Llama2-7B-chat-4k gains +21% with best retrieval (19.9 to 24.0), but GPT-3.5-Turbo-16k loses 2% (40.7 to 39.9) and ChatGLM2-6B-32k loses 5% (36.1 to 34.4) (Table 4, Section 4.2). **Scope:** QA tasks only, 3 retrievers, 2 chunk sizes, 3 models. **Magnitude:** +21%, -2%, -5%. **Status: supported** (3 models, QA tasks only, 6 retrieval configurations each -- moderate evidence within QA scope).

5. **C5: Models trained on longer contexts are most robust to length increases.** ChatGLM2-6B-32k and LongChat-v1.5-7B-32k show relative drops of only 4% and 7% from 0--4K to 8K+ on LongBench-E, while GPT-3.5-Turbo-16k drops 17% (Figure 3, Table 9, Section 4.1). **Scope:** 13 English datasets in LongBench-E, 3 length bins. **Magnitude:** 4% and 7% drops vs 17% for GPT-3.5. **Status: supported** (8 models across 13 tasks and 3 length bins -- strong evidence for this specific set of models).

6. **C6: Wikipedia-based tasks are partially solvable through memorization.** Without context, GPT-3.5-Turbo-16k scores 31.7 on HotpotQA and 28.9 on 2WikiMultihopQA, compared to 4.7 on NarrativeQA. The delta metric provides a purer measure of context understanding (Table 6, Section 4.3). **Scope:** GPT-3.5-Turbo-16k, Llama2-7B-chat-4k, ChatGLM2-6B-32k on single-doc and multi-doc QA. **Magnitude:** w/o context scores of 28.9-31.7 on Wikipedia QA vs 4.7 on non-Wikipedia QA. **Status: supported** (3 models, 8 QA datasets -- moderate evidence).

7. **C7: Synthetic tasks have near-binary discriminability.** On PassageRetrieval-en, scores range from 3.0% (ChatGLM2-6B) to 77.0% (ChatGLM2-6B-32k); on PassageCount, all models score below 6.5%. Simple averaging across all tasks would let these extremes dominate rankings (Tables 2-3, Appendix C-D). **Scope:** PassageCount and PassageRetrieval tasks, 8 models. **Magnitude:** 3.0% to 77.0% range on PassageRetrieval-en; all <6.5% on PassageCount. **Status: supported** (8 models, 3 synthetic tasks -- strong evidence for this specific observation).

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
- **Kocisky et al. (2018)** -- *NarrativeQA.* Source of single-document QA over long stories.
- **Dasigi et al. (2021)** -- *Qasper.* Source of QA over NLP papers.
- **Huang et al. (2021)** -- *GovReport.* Source of government report summarization data.
- **Zhong et al. (2021)** -- *QMSum.* Source of query-based meeting summarization data.
- **Fabbri et al. (2019)** -- *MultiNews.* Source of multi-document news summarization data.
- **Liu et al. (2023b)** -- *RepoBench.* Source of repository-level code completion data.
- **Guo et al. (2023)** -- *LongCoder/LCC.* Source of long code completion data.
- **He et al. (2018)** -- *DuReader.* Source of Chinese reading comprehension data from Baidu Search.
- **Wu et al. (2023)** -- *VCSUM.* Source of Chinese meeting summarization data.
- **Li and Roth (2002)** -- *TREC.* Source of question classification data.
- **Joshi et al. (2017)** -- *TriviaQA.* Source of reading comprehension QA data.
- **Gliwa et al. (2019)** -- *SAMSum.* Source of dialogue summarization data.

### Models Evaluated

- **OpenAI (2022)** -- *GPT-3.5-Turbo-16k.* The top-performing commercial model on LongBench (44.7% overall).
- **Touvron et al. (2023)** -- *Llama 2.* Base model for LongChat and Vicuna fine-tuned variants; evaluated directly as Llama2-7B-chat-4k.
- **Du et al. (2022); Zeng et al. (2023)** -- *GLM/ChatGLM2.* Base model and its 32K-extended variant demonstrating the largest gains from position interpolation (+62%).

### Evaluation and Analysis

- **Liu et al. (2023a)** -- *Lost in the Middle.* Referenced for positional bias in evidence placement. LongBench's MultiFieldQA annotation ensures random evidence placement.
- **Sun et al. (2021)** -- *Do Long-Range Language Models Actually Use Long-Range Context?* Referenced for showing that perplexity may not reflect performance on sequence-level tasks.
- **Yu et al. (2024)** -- *KoLA.* Referenced for the delta-score approach to disentangling memorization from context understanding (Section 4.3).
