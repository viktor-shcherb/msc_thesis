# LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding

**Authors:** Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu, Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao Liu, Aohan Zeng, Lei Hou, Yuxiao Dong, Jie Tang, Juanzi Li (Tsinghua University, Zhipu.AI, Chinese Academy of Sciences)
**Date:** August 2024, ACL 2024 (arXiv:2308.14508)

---

## Core Research Problem

Although LLMs have demonstrated strong performance on many language tasks, most models at the time could only process texts a few thousand tokens long, limiting their application to longer inputs such as books, reports, and codebases. Recent methods -- context window extension (Press et al., 2022; Chen et al., 2023), recurrent memory (Dai et al., 2019; Bulatov et al., 2023), sparse attention (Ding et al., 2023), and external memory augmentation (Liang et al., 2023) -- have sought to improve long-context capabilities, but no comprehensive benchmark existed to evaluate them.

Prior evaluation relied primarily on **perplexity**, which does not necessarily reflect performance on downstream sequence-level tasks (Sun et al., 2021), or on **synthetic retrieval tasks** (Tay et al., 2021; Chen et al., 2023) that fail to mirror real-world scenarios. Concurrent benchmarks -- ZeroSCROLLS (Shaham et al., 2022, 2023) and L-Eval (An et al., 2023) -- covered only a restricted range of task types, limiting the diversity of long-dependency patterns tested. No benchmark offered bilingual coverage (English and Chinese), multitask breadth across realistic application scenarios, or controlled-length subsets for disentangling long-context ability from task ability.

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

**Dataset construction.** Of the 21 datasets, 6 are extracted directly from existing test sets, 10 are adapted from existing datasets with modifications for long-context evaluation, and 5 are newly created and annotated (MultiFieldQA-en, MultiFieldQA-zh, PassageCount, PassageRetrieval-en, PassageRetrieval-zh).

- **Multi-doc QA adaptation:** Supporting Wikipedia passages are included first, then distracting passages are added until a maximum length is reached, and all passages are randomly ordered.
- **Few-shot learning:** For each test instance, a random number of examples from the training set are concatenated as context `C`. Ranges: TREC [100, 600], LSHT [10, 40], SAMSum [10, 100], TriviaQA [2, 24].
- **PassageRetrieval:** 30 random passages are sampled; one is summarized by GPT-3.5-Turbo. The model must identify which passage the summary corresponds to.
- **PassageCount:** N unique passages from Wikipedia are sampled, each repeated a random number of times, then shuffled. The model must count the number of unique passages. N is drawn from [2, M] where M is in [17, 50].

**LongBench-E.** A subset of 13 English datasets uniformly sampled by length into three bins (0--4K, 4K--8K, 8K+ words), with ~100 samples per bin per dataset, enabling per-length-range analysis.

**Truncation strategy.** When input length `L` exceeds maximum context length `M`, the input is truncated from the middle to preserve both instruction/question (at the front) and potential tail information:

> S_{1:L} → [S_{1:⌊M/2⌋}; S_{L-⌊M/2⌋-1:L}]

**Evaluation.** Zero-shot setting for all tasks except few-shot learning (where examples form the long context). Greedy decoding for reproducibility. Chat-specific prompts are omitted for few-shot and code tasks to elicit completion-style responses.

### Experimental Setup

**Models (8):**
- GPT-3.5-Turbo-16k (commercial, 16K context)
- Llama2-7B-chat-4k (4K context)
- LongChat-v1.5-7B-32k (fine-tuned from Llama2-7B, linear RoPE scaling, 32K)
- XGen-7B-8k (8K context)
- InternLM-7B-8k (8K context)
- ChatGLM2-6B (base, ~4K effective)
- ChatGLM2-6B-32k (position interpolation + 32K alignment training)
- Vicuna-v1.5-7B-16k (fine-tuned from Llama2-7B, linear RoPE scaling, 16K)

**Context compression experiments:** Three retrievers (text-embedding-ada-002, Contriever, BM25) with two chunk sizes (200 and 500 words), top-7 and top-3 chunks respectively. Also summarization-based compression via model-generated chunk summaries.

### Key Results

**Overall performance (macro-average across 6 categories):**

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

- **GPT-3.5-Turbo-16k leads overall** but still struggles on longer contexts (−17% from 0--4K to 8K+ on LongBench-E).
- **Scaled positional embedding and longer fine-tuning help substantially.** ChatGLM2-6B-32k improves 62% over ChatGLM2-6B; LongChat-v1.5-7B-32k improves 19% over Llama2-7B-chat-4k.
- **ChatGLM2-6B-32k and LongChat-v1.5-7B-32k are most robust to length increases** on LongBench-E, with relative drops of only 4% and 7% from 0--4K to 8K+.
- **Synthetic tasks are highly discriminating:** models either achieve high scores or near-zero, suggesting that simple averaging across all tasks may not reflect true long-context capability.

**Truncation experiment (LongBench, macro-average):**

| Model | Max Length | 8K Trunc. | 4K Trunc. |
|---|---|---|---|
| GPT-3.5-Turbo-16k | 44.7 | 44.2 | 39.1 |
| ChatGLM2-6B-32k | 41.5 | 39.3 | 35.4 |
| Vicuna-v1.5-7B-16k | 30.5 | 30.5 | 30.2 |

GPT-3.5-Turbo-16k and ChatGLM2-6B-32k benefit from longer context, confirming that LongBench tasks genuinely require long-context modeling. Vicuna-v1.5-7B-16k shows no improvement, indicating it does not effectively use context beyond 4K.

**Retrieval-based compression (best retriever per model, QA tasks avg):**

| Model | w/o Retrieval | Best Retrieval | Delta |
|---|---|---|---|
| GPT-3.5-Turbo-16k | 40.7 | 39.9 | −2% |
| Llama2-7B-chat-4k | 19.9 | 24.0 | +21% |
| ChatGLM2-6B-32k | 36.1 | 34.4 | −5% |

- **text-embedding-ada-002 is the best retriever**, followed by Contriever, then BM25.
- **Retrieval helps only weak long-context models.** Llama2-7B-chat-4k gains +21%, but even with retrieval its performance lags behind stronger models without retrieval. Models with strong long-context ability (GPT-3.5-Turbo-16k, ChatGLM2-6B-32k) are slightly harmed by retrieval.
- **Smaller chunks with more retrieved segments** (200 words × 7 chunks) outperform larger chunks (500 × 3).

**Context understanding vs. memorization (Table 6):** When context is withheld and only the question is presented, performance on Wikipedia-based tasks (HotpotQA, 2WikiMultihopQA, MuSiQue) remains relatively high, indicating models rely partly on parametric knowledge from pretraining. The delta (score with context minus score without) serves as a purer measure of context understanding ability. For GPT-3.5-Turbo-16k, the largest deltas are on MultiFieldQA-zh (+50.3) and MultiFieldQA-en (+36.6), while multi-doc QA deltas are smaller (+8.8 to +19.9), reflecting Wikipedia memorization.

### Limitations

1. **Automatic metrics (ROUGE-L, F1) may underestimate models that generate longer responses.** Using LLM-as-examiner could reduce this problem but introduces its own biases and costs.
2. **Performance is coupled with instruction-following capability.** The benchmark aims to test long-context modeling, but real-world tasks inevitably require instruction comprehension.
3. **Maximum length reaches ~40K tokens.** LongBench does not test contexts beyond tens of thousands of tokens, limiting evaluation of models claiming 100K+ context windows.
4. **Synthetic tasks have near-binary discriminability.** Models either achieve high scores or near-zero on PassageCount and PassageRetrieval, reducing the granularity of differentiation on these tasks.

---

## Conclusions

1. **First bilingual, multitask long-context benchmark.** LongBench provides 21 datasets across 6 task categories in English and Chinese, with 4,750 test instances averaging 6,711 words (EN) and 13,386 characters (ZH), filling the gap of comprehensive long-context evaluation.

2. **Commercial models lead but still degrade on longer contexts.** GPT-3.5-Turbo-16k achieves the highest overall score (44.7%) but drops 17% from short to long contexts on LongBench-E, showing that even the strongest models have room for improvement.

3. **Position extension and longer fine-tuning yield large gains.** ChatGLM2-6B-32k (with position interpolation and 32K alignment) improves 62% over ChatGLM2-6B, and is the most robust model across length ranges (only 4% drop from 0--4K to 8K+).

4. **Retrieval-based compression helps only weak models.** Context compression via retrieval improves Llama2-7B-chat-4k by 21% on QA tasks but slightly degrades models with strong native long-context capability, indicating retrieval is not a shortcut to solving long-context understanding.

5. **LongBench-E disentangles length from task difficulty.** The uniformly sampled variant reveals that models trained on longer contexts (ChatGLM2-6B-32k, LongChat-v1.5-7B-32k) maintain more stable performance across length ranges, while others show steep degradation.

6. **Per-category evaluation is more meaningful than overall averaging.** Synthetic tasks exhibit near-binary discriminability, so averaging across all tasks may let these dominate rankings. LongBench's category-level reporting avoids this distortion.

---

## Core References and Why They Are Referenced

### Prior Long-Context Evaluation Benchmarks

- **Shaham et al. (2022; 2023)** -- *SCROLLS/ZeroSCROLLS.* The closest prior work on long-context evaluation. LongBench argues that SCROLLS and ZeroSCROLLS cover a restricted range of task types, limiting the diversity of long-dependency patterns tested.
- **An et al. (2023)** -- *L-Eval.* Concurrent evaluation benchmark for long text modeling. LongBench contrasts itself as providing broader task coverage, bilingual support, and controlled-length subsets.
- **Tay et al. (2021)** -- *Long Range Arena.* A benchmark for efficient transformers that uses synthetic tasks. LongBench argues synthetic-only evaluation does not mirror real-world scenarios.

### Context Extension and Long-Context Methods

- **Chen et al. (2023)** -- *Positional Interpolation.* The context extension method used in ChatGLM2-6B-32k. LongBench's results show that position interpolation combined with longer fine-tuning produces a 62% improvement.
- **Press et al. (2022)** -- *ALiBi.* A length extrapolation method via linear biases. Referenced as part of the context extension landscape that LongBench evaluates.
- **Bulatov et al. (2022; 2023)** -- *Recurrent Memory Transformer / Scaling RMT.* Referenced as recurrent memory approaches to long-context modeling.
- **Dai et al. (2019)** -- *Transformer-XL.* Foundational work on recurrent memory for transformers, referenced in the context extension discussion.

### Source Datasets

- **Yang et al. (2018)** -- *HotpotQA.* Source of 2-hop multi-document QA data in LongBench.
- **Ho et al. (2020)** -- *2WikiMultihopQA.* Source of up-to-5-hop multi-document QA data.
- **Trivedi et al. (2022)** -- *MuSiQue.* Source of up-to-4-hop multi-document QA data with shortcut-resistant questions.
- **Kociskỳ et al. (2018)** -- *NarrativeQA.* Source of single-document QA over long stories.
- **Dasigi et al. (2021)** -- *Qasper.* Source of QA over NLP papers.
- **Huang et al. (2021)** -- *GovReport.* Source of government report summarization data.
- **Zhong et al. (2021)** -- *QMSum.* Source of query-based meeting summarization data.
- **Fabbri et al. (2019)** -- *MultiNews.* Source of multi-document news summarization data.
- **Liu et al. (2023b)** -- *RepoBench.* Source of repository-level code completion data.
- **Guo et al. (2023)** -- *LongCoder/LCC.* Source of long code completion data.

### Models Evaluated

- **OpenAI (2022)** -- *GPT-3.5-Turbo.* The top-performing commercial model on LongBench (44.7% overall).
- **Touvron et al. (2023)** -- *Llama 2.* Base model for LongChat and Vicuna fine-tuned variants; evaluated directly as Llama2-7B-chat-4k.
- **Du et al. (2022); Zeng et al. (2023)** -- *GLM/ChatGLM2.* Base model and its 32K-extended variant that demonstrates the largest gains from position interpolation.
- **Li et al. (2023)** -- *LongChat.* Fine-tuned Llama2-7B with linear RoPE scaling and 32K context.

### Evaluation and Analysis

- **Liu et al. (2023a)** -- *Lost in the Middle.* Referenced for the observation that answer-related evidence placement can bias evaluation. LongBench's MultiFieldQA annotation ensures random evidence placement.
- **Sun et al. (2021)** -- *Do Long-Range Language Models Actually Use Long-Range Context?* Referenced for showing that perplexity may not reflect performance on sequence-level tasks.

#### Cross-References in Available Papers

- **BABILong (2024-12-babilong-long-context-reasoning):** Cites LongBench as "a bilingual long-context benchmark limited to 40K tokens" and contrasts BABILong's controllable length (up to 10M tokens) and resistance to parametric knowledge confounds. BABILong specifically notes that LongBench and similar realistic benchmarks "lack controllable sequence length and confound long-context utilization with parametric knowledge."
- **RULER (2024-10-ruler-context-size):** Lists LongBench in Table 1 as a comparison point for benchmark design properties. RULER contrasts itself as offering controllable synthetic tasks with configurable complexity, while LongBench uses natural-text tasks.
- **DroPE (2025-12-drope-dropping-positional-embeddings):** Uses four LongBench tasks (MultiFieldQA, MuSiQue, GovReport, LCC) for downstream evaluation of context extension methods. DroPE reports results on LongBench in Table 2 (SmolLM LongBench Avg. 30.52 vs. 19.94 for YaRN; Llama2-7B LongBench Avg. 26.08 vs. 21.88 for RoPE-NTK).
- **LongBench Pro (2026-01-longbench-pro):** The direct successor benchmark in the same line of work. LongBench Pro extends LongBench with broader task coverage (11 vs. 6 primary tasks), multi-dimensional categorization (context requirement, length, difficulty), and fully natural text at longer context lengths (up to 256K tokens).
- **Lost in the Middle (2024-02-lost-in-the-middle):** LongBench references Liu et al. (2023a) regarding evidence placement bias. The MultiFieldQA annotation guidelines explicitly ensure random placement of answer-related statements to avoid the position biases identified in this paper.
- **YaRN (2024-05-yarn-context-extension):** LongBench tasks are used by DroPE to evaluate YaRN's downstream performance, showing that YaRN's zero-shot context extension does not translate to improved LongBench scores.
