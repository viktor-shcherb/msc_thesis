---
title: "LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks"
authors: "Bai, Tu, Zhang, Peng, Wang, Lv, Cao, Xu, Hou, Dong, Tang, Li"
year: 2025
venue: "ACL 2025"
paper_type: conference-paper
categories: ["benchmarking", "long-context-evaluation"]
scope: ["human-annotated long-context benchmark", "deep reasoning evaluation", "inference-time compute scaling"]
benchmarks_used: ["longbench-v2"]
models_introduced: []
models_evaluated: ["gpt-4", "qwen-series", "llama-3-8b", "llama-3-70b"]
key_claims:
  - id: C1
    claim: "LongBench v2 is sufficiently challenging that human experts achieve only 53.7% accuracy under a 15-minute time constraint, compared to 25% random guessing"
    evidence: "Table 1, Table 2, Section 3.2"
    status: supported
  - id: C2
    claim: "o1-preview achieves 57.7% accuracy, surpassing human expert performance (53.7%) by 4 percentage points through extended inference-time reasoning"
    evidence: "Table 2, Section 4.1"
    status: supported
  - id: C3
    claim: "Scaling test-time compute is highly effective: o1-preview vs GPT-4o yields +7.6%, o1-mini vs GPT-4o-mini yields +8.5%, and CoT prompting yields an average +3.4% for open-source models"
    evidence: "Table 2, Section 4.1"
    status: supported
  - id: C4
    claim: "Model parameter scaling improves performance: smaller models (~7-9B) score around 30%, while larger counterparts (~70B+) achieve around or above 40%"
    evidence: "Table 2, Section 4.1"
    status: supported
  - id: C5
    claim: "Models outperform humans on short contexts (<32K) by up to 15.4% but trail human accuracy on medium contexts (32K-128K) by 5.6%"
    evidence: "Table 2, Section 4.1"
    status: supported
  - id: C6
    claim: "RAG provides limited benefit: Qwen2.5 and GLM-4-Plus show no improvement beyond 32K retrieval context, and GPT-4o's best RAG performance still lags behind its non-RAG score by 0.6%"
    evidence: "Figure 4, Section 4.2"
    status: supported
  - id: C7
    claim: "Memorization is minimal: without context, most models achieve 25-30% accuracy (random-guessing level), confirming questions require active comprehension"
    evidence: "Table 3, Section 4.3"
    status: supported
  - id: C8
    claim: "The model-human performance gap is largest on long structured data understanding tasks (tables and knowledge graphs)"
    evidence: "Figure 3, Table 3, Section 4.1"
    status: supported
cross_references:
  - target: 2024-08-longbench-bilingual-benchmark
    type: extends
    detail: "Direct successor to LongBench; replaces extractive questions with harder human-annotated multiple-choice questions requiring deep reasoning, extends length coverage to 2M words"
  - target: 2026-01-longbench-pro
    type: extended-by
    detail: "LongBench Pro extends LongBench v2 with bilingual coverage and multi-dimensional categorization"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: complementary
    detail: "ZeroSCROLLS cited as an earlier comprehensive zero-shot long-context evaluation effort; LongBench v2 addresses its reliance on unreliable metrics (ROUGE, F1) through multiple-choice format"
  - target: 2024-10-ruler-context-size
    type: complementary
    detail: "RULER cited as representative of synthetic benchmarks that fail to test deep understanding; LongBench v2 uses fully natural documents and human-verified difficulty calibration"
  - target: 2024-08-infinitebench-long-context-evaluation
    type: complementary
    detail: "InfiniteBench extends evaluation beyond 100K tokens; LongBench v2 contrasts with more reliable evaluation (multiple-choice vs ROUGE/F1) and human-verified difficulty"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong extends NIAH with reasoning tasks but uses synthetic data; LongBench v2 uses fully natural documents with human-annotated questions"
  - target: 2024-05-yarn-context-extension
    type: evaluates
    detail: "YaRN evaluated with Qwen2.5 models using scaling factor 4.0; yields significant improvements especially on Medium and Long samples (Table 4)"
  - target: 2022-12-chain-of-thought-prompting
    type: evaluates
    detail: "CoT prompting evaluated as one of the inference settings; yields average +3.4% improvement for open-source models"
  - target: 2023-11-needle-in-a-haystack
    type: complementary
    detail: "NIAH cited as evidence that modern models achieve perfect retrieval, motivating the need for benchmarks testing deeper understanding beyond simple retrieval"
  - target: 2024-08-l-eval-standardized-evaluation
    type: complementary
    detail: "L-Eval cited as one of the comprehensive long-context benchmarks that LongBench v2 improves upon with harder questions and more reliable evaluation"
open_questions:
  - question: "How does scaling inference-time compute (e.g., o1-style reasoning) interact with context length for deep long-context understanding?"
    addressed_by: null
  - question: "Why does YaRN have a larger impact on model performance under the CoT setting than zero-shot?"
    addressed_by: null
  - question: "Can long-context models be improved on structured data understanding tasks through targeted training data composition?"
    addressed_by: null
  - question: "How would LongBench v2 results change if extended to multilingual evaluation?"
    addressed_by: null
---
# LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks

**Authors:** Yushi Bai, Shangqing Tu, Jiajie Zhang, Hao Peng, Xiaozhi Wang, Xin Lv, Shulin Cao, Jiazheng Xu, Lei Hou, Yuxiao Dong, Jie Tang, Juanzi Li (Tsinghua University, Zhipu.AI)
**Date:** July 2025, ACL 2025 (arXiv:2412.15204)

---

## Core Research Problem

Long-context LLMs have rapidly expanded their context windows from 8K to 128K and even 1M tokens (OpenAI, 2024; Anthropic, 2024; Reid et al., 2024; GLM et al., 2024), yet existing evaluation benchmarks fail to test whether models truly comprehend and reason over these long inputs.

- **Existing benchmarks focus on shallow understanding.** Benchmarks such as LongBench (Bai et al., 2024b), InfiniteBench (Zhang et al., 2024d), and RULER (Hsieh et al., 2024) primarily test extractive questions where the answer is directly found in the material -- a task easily handled by modern long-context models and RAG systems, as evidenced by near-perfect Needle-in-a-Haystack scores (Kamradt, 2023).
- **Synthetic tasks limit real-world applicability.** Many benchmarks rely on synthetic data construction (e.g., RULER, BABILong), which does not capture the complexity of real-world long-context reasoning.
- **Evaluation metrics are unreliable.** Widely adopted metrics such as ROUGE and F1 are known to correlate poorly with human judgment (Novikova et al., 2017). LLM-as-a-judge evaluation is costly and may introduce biases (Bai et al., 2024c; Ye et al., 2024).

**The core challenge is how to build a long-context benchmark that tests deep understanding and reasoning -- not just retrieval -- across diverse realistic tasks, with reliable evaluation and sufficient difficulty to differentiate current state-of-the-art models.**

---

## Problem Solutions

LongBench v2 addresses this challenge through a 503-question multiple-choice benchmark built on four design pillars:

1. **Length coverage.** Contexts range from 8K to 2M words (median 54K, average 104K), with relatively even distribution up to 128K, covering the full operational range of modern long-context LLMs.
2. **Difficulty calibration.** Each question is verified through a five-step pipeline: human experts using document search tools cannot answer correctly within 3 minutes, and at least one of three screening LLMs answers incorrectly.
3. **Task diversity.** Six major task categories and 20 subtasks cover realistic long-context scenarios: single-document QA, multi-document QA, long in-context learning, long-dialogue history understanding, code repository understanding, and long structured data understanding.
4. **Reliable evaluation.** A uniform multiple-choice format with four options eliminates metric ambiguity, with a random-guessing baseline of 25%.

---

## Approach Details

### Method

LongBench v2 consists of 503 multiple-choice questions across six major task categories subdivided into 20 subtasks. All data is in English. Each sample consists of a long text, a question, four choices, a groundtruth answer, and supporting evidence.

### Key Technical Components

**Task taxonomy (Table 1).** The six major categories and their statistics:

| Category | #Data | Median Length | Expert Acc | Expert Time |
|---|---|---|---|---|
| I. Single-Document QA | 175 | 51K | 55% | 8.9 min |
| II. Multi-Document QA | 125 | 34K | 36% | 6.1 min |
| III. Long In-context Learning | 81 | 71K | 63% | 8.3 min |
| IV. Long-dialogue History Understanding | 39 | 25K | 79% | 8.2 min |
| V. Code Repository Understanding | 50 | 167K | 44% | 6.4 min |
| VI. Long Structured Data Understanding | 33 | 49K | 73% | 6.4 min |

The 20 subtasks include: academic, literary, legal, financial, governmental, detective, and event-ordering QA (single-doc); academic, legal, financial, governmental, and multi-news QA (multi-doc); user guide QA, new language translation, and many-shot learning (ICL); agent history QA and dialogue history QA (dialogue); code repo QA (code); table QA and knowledge graph reasoning (structured data).

**Data collection pipeline (Figure 2).** Five steps:

1. **Document Collection.** Annotators upload documents they have personally read or used. Documents are automatically checked for minimum length (8,192 words) and overlap with existing annotations.
2. **Data Annotation.** Annotators propose a multiple-choice question with four choices, a groundtruth answer, and evidence. Prohibited question types: counting questions (>10 items), simple retrieval questions, overly professional questions, deliberately difficult questions, and questions depending on visual understanding.
3. **Automated Review.** Three LLMs (GPT-4o-mini, GLM-4-Air, GLM-4-Flash) answer each question. If all three answer correctly, the question is considered too easy and returned for revision. Inputs exceeding 128K context are truncated from the middle.
4. **Manual Review.** A human expert reviewer downloads the raw files, answers the question using document search tools, and checks a quality checklist. Questions answered correctly within 3 minutes are deemed too easy. Experts may respond "I don't know the answer" after 15 minutes. Time spent is tracked.
5. **Data Revision.** Questions failing automated or manual review are returned to annotators with categorized feedback: illegal question, insufficient difficulty, or wrong answer. Up to five revision cycles are permitted.

**Difficulty and length categorization.** Data is classified into two difficulty levels: "Easy" (192 samples) and "Hard" (311 samples). A sample is classified as Hard if at most one of three screening LLMs answers correctly and the human reviewer cannot solve it within 10 minutes. By construction, human expert accuracy on Easy samples is 100% and on Hard samples is 25.1% (near random guessing). Length is divided into three groups: "Short" (<32K words, 180 samples), "Medium" (32K--128K, 215 samples), and "Long" (>128K, 108 samples).

**Annotation workforce.** 97 annotators from top universities with diverse academic backgrounds (CS 29%, Law 24%, Economics 22%, others), ranging from bachelor's to PhD level. 24 professional human experts selected for manual review. Each annotator could submit at most 20 questions to ensure diversity. Total data collection cost: approximately 100,000 CNY over two months.

**Incentive mechanism.** Base reward of 100 CNY per accepted question. Length bonuses: +20 CNY (32K--64K), +40 CNY (64K--128K), +50 CNY (>128K). Difficulty bonus: +50 CNY for Hard samples. Reviewers receive 25 CNY per review, with random quality checks and reward revocation for poor reviewing.

**Data verification (Section 3.3).** Author verification of 70 sampled data points: 68/70 (97.1%) correct answers, 67/70 (95.7%) Google-proofed (Rein et al., 2023). Answer distribution across options: A 19%, B 25%, C 30%, D 26%. Rejection rates during manual review: 4% illegal question, 7% insufficient difficulty, 4% wrong answer.

### Experimental Setup

- **Open-source models (10 models, all 128K context windows):** GLM-4-9B-Chat, Llama-3.1-8B-Instruct, Llama-3.1-70B-Instruct, Llama-3.3-70B-Instruct, Llama-3.1-Nemotron-70B-Instruct, Qwen2.5-7B-Instruct, Qwen2.5-72B-Instruct, Mistral-Large-Instruct-2407, Mistral-Large-Instruct-2411, c4ai-command-r-plus-08-2024.
- **Proprietary models (7 models):** GLM-4-Plus, GPT-4o-mini-2024-07-18, GPT-4o-2024-08-06, GPT-4o-2024-11-20, o1-mini-2024-09-12, o1-preview-2024-09-12, Claude-3.5-Sonnet-20241022 (200K context window; all others 128K).
- **Evaluation settings:** Zero-shot and zero-shot + CoT. Following Rein et al. (2023), in the CoT setting, the model first generates a chain of thought (max 1,024 tokens), then produces a final answer (max 128 tokens). Temperature = 0.1 for all settings. o1-preview performs latent CoT under zero-shot prompting.
- **Truncation:** Middle truncation for sequences exceeding the model's context window (following Bai et al., 2024b).
- **Qwen2.5 with YaRN:** Evaluated separately with scaling factor 4.0 (Table 4).

### Key Results

**Main evaluation (Table 2, selected models):**

| Model | Overall | Overall (CoT) | Easy (CoT) | Hard (CoT) | Short (CoT) | Medium (CoT) | Long (CoT) |
|---|---|---|---|---|---|---|---|
| o1-preview | 57.7 | 56.2 | 58.9 | 54.6 | 64.6 | 50.2 | 54.3 |
| GPT-4o (08-06) | 50.1 | 51.2 | 57.9 | 47.1 | 53.9 | 50.7 | 47.7 |
| GPT-4o (11-20) | 46.0 | 51.4 | 54.2 | 49.7 | 59.6 | 48.6 | 43.5 |
| Claude-3.5-Sonnet | 41.0 | 46.7 | 55.2 | 41.5 | 53.9 | 41.9 | 44.4 |
| GLM-4-Plus | 44.3 | 46.1 | 52.1 | 42.4 | 53.3 | 44.7 | 37.0 |
| Qwen2.5-72B-Instruct | 39.4 | 38.8 | 42.2 | 36.7 | 50.0 | 28.8 | 39.8 |
| Llama-3.1-70B-Instruct | 31.6 | 36.2 | 35.9 | 36.3 | 45.0 | 34.0 | 25.9 |
| Qwen2.5-7B-Instruct | 27.0 | 29.8 | 30.7 | 29.3 | 35.6 | 26.5 | 26.9 |
| Human (15 min) | 53.7 | -- | 100 | 25.1 | 47.2 | 59.1 | 53.7 |

- **(1) o1-preview surpasses human experts.** The best model (o1-preview, 57.7%) exceeds human expert performance (53.7%) under a 15-minute time constraint by 4%. o1-preview performs latent chain-of-thought under zero-shot prompting, achieving this through extended inference-time reasoning (Table 2, Section 4.1).
- **(2) Scaling test-time compute is highly effective.** o1-preview vs. GPT-4o: +7.6%. o1-mini vs. GPT-4o-mini: +8.5%. CoT prompting alone yields an average +3.4% improvement for open-source models (Table 2, Section 4.1).
- **(3) Model parameter scaling holds.** Smaller models (GLM-4-9B-Chat, Qwen2.5-7B-Instruct, GPT-4o-mini) score around 30%, while their larger counterparts (GLM-4-Plus, Qwen2.5-72B-Instruct, GPT-4o) achieve around or above 40% (Table 2, Section 4.1).
- **(4) Models outperform humans on short contexts but underperform on medium contexts.** On Short (<32K), the best model surpasses human performance by 15.4% (o1-preview CoT 64.6% vs. human 47.2%, accounting for the task distribution caveat). On Medium (32K--128K), even the top model (o1-preview 50.2%) trails human accuracy (59.1%) by 8.9% (Table 2, Section 4.1). Note: the paper cautions that task distributions differ across length ranges, so within-model comparisons across ranges are unreliable; between-model comparisons within each range are recommended.
- **(5) o1-preview shows disproportionate strengths on specific tasks.** Compared to GPT-4o, o1-preview shows superior performance on multi-doc QA, long in-context learning, and code repository understanding, with a substantial lead over other models (Figure 3, Section 4.1).

**RAG evaluation (Figure 4, Section 4.2):**

Long contexts are split into 512-token chunks using GLM-4-9B tokenizer, encoded with Zhipu Embedding-3, and top-N chunks retrieved by embedding similarity. Results at N = 4, 8, 16, 32, 64, 128, 256:

- Qwen2.5-72B and GLM-4-Plus show no significant improvement as retrieval context length increases beyond 32K tokens. Both perform better with 32K RAG context than with the full 128K context window without RAG (Qwen2.5: +4.1%).
- Only GPT-4o effectively leverages longer retrieval contexts, achieving its best RAG performance at 128K, while still lagging behind its non-RAG score by 0.6%.
- These findings confirm that LongBench v2 questions cannot be solved solely through retrieval.

**Memorization evaluation (Table 3, Section 4.3):**

| Model | With Context | Without Context |
|---|---|---|
| GLM-4-9B-Chat | 30.2 | 26.2 |
| Llama-3.1-8B-Instruct | 30.0 | 25.8 |
| Qwen2.5-72B-Instruct | 39.4 | 30.0 |
| GLM-4-Plus | 44.3 | 27.6 |
| GPT-4o | 50.1 | 33.1 |

Without context, most models achieve 25--30% overall accuracy (random-guessing level). Memorization is slightly higher for single-document QA (Task I) and code repository tasks (Task V), likely because models encountered some of these documents during training. Memorization is minimal for multi-doc QA (Task II), long ICL (Task III), and structured data (Task VI).

**YaRN results (Table 4, Appendix E):**

| Model | Overall | Overall (+YaRN) | Medium | Medium (+YaRN) | Long | Long (+YaRN) |
|---|---|---|---|---|---|---|
| Qwen2.5-7B-Instruct (CoT) | 29.8 | **35.6** | 26.5 | **32.6** | 26.9 | **27.8** |
| Qwen2.5-72B-Instruct (CoT) | 38.8 | **43.5** | 28.8 | **40.9** | 39.8 | 39.8 |

YaRN with scaling factor 4.0 significantly enhances long-context processing on LongBench v2, especially on Medium and Long samples. The impact is larger under the CoT setting than zero-shot, though the underlying reasons for this remain unclear.

---

## Limitations and Failure Modes

The paper explicitly discusses three limitations (Section 6):

1. **Benchmark size.** 503 samples may lead to less stable results vulnerable to randomness. The current dataset cost 100,000 CNY and took over two months to collect, preventing expansion due to resource constraints.
2. **Language.** English only, preventing cross-lingual evaluation of long-context capabilities.
3. **Length distribution inconsistencies.** Task distributions differ significantly across length ranges (e.g., code repo questions are concentrated in the Long range), making within-model comparisons across length intervals unreliable. The authors recommend between-model comparisons within each length interval.

Additional limitations not explicitly discussed:

4. **Difficulty definition is circular for human baseline.** Easy samples are defined partly by the human reviewer solving them correctly, so human accuracy on the Easy subset is 100% by construction. This makes the aggregate 53.7% human accuracy a function of the Easy/Hard classification criteria rather than an independent measure. [Inference: not stated explicitly.]
5. **Compensated results for invalid outputs.** Claude-3.5-Sonnet has a 13.9% (zero-shot) and 14.9% (CoT) invalid output rate due to refusal or format errors, higher than other models. Compensated results (Table 5, Appendix E) assign 25% accuracy to invalid outputs, which may slightly inflate scores for models with high refusal rates. [Inference: from Table 5.]

---

## Conclusions

### Contributions

1. **Challenging benchmark at the frontier of human-AI parity.** Human experts achieve only 53.7% under a 15-minute time constraint (vs. 25% random guessing), while the best model (o1-preview) reaches 57.7%, providing a reliable evaluation standard for both current and future long-context AI systems (Table 2, Section 4.1).

2. **Five-step quality-controlled annotation pipeline.** The combination of automated review (three-LLM screening) and manual review (expert verification with time tracking) achieves a ~3% error rate and ~96% Google-proof rate across 503 samples (Section 3.3).

3. **Deep reasoning matters more than retrieval.** Questions are deliberately designed to resist retrieval-based solving. RAG experiments confirm that retrieval alone does not solve LongBench v2: Qwen2.5 and GLM-4-Plus plateau at 32K retrieval context, and GPT-4o's best RAG score still trails its non-RAG performance (Figure 4, Section 4.2).

4. **Scaling inference-time compute is the most effective strategy.** o1-preview's extended reasoning yields +7.6% over GPT-4o, a larger gain than model parameter scaling or CoT prompting alone. This highlights inference-time thinking as a crucial direction for long-context reasoning (Table 2, Section 4.1).

5. **Task-specific performance gaps identified.** The model-human gap is largest on long structured data understanding tasks (tables and knowledge graphs), suggesting training corpora underrepresent structured formats. o1-preview shows disproportionate strengths on multi-doc QA, long ICL, and code repository tasks (Figure 3, Section 4.1).

### Implications

1. **Inference-time reasoning may be necessary for long-context understanding.** The o1-preview result suggests that simply increasing context windows is insufficient; models need extended reasoning capabilities to deeply understand long texts. This parallels findings in math and coding reasoning (Wei et al., 2022; Sprague et al., 2024). [Speculative: tested only on one reasoning model.]

2. **Context window utilization degrades non-uniformly with length.** Models excel on short contexts but degrade on medium-length contexts (32K--128K) even more than on very long ones (>128K), possibly because task distributions confound the comparison. Developing methods to maintain reasoning capabilities under longer contexts remains an open challenge. [Speculative: confounded by task distribution.]

3. **Benchmark design methodology is transferable.** The five-step pipeline with LLM screening, human review, and Google-proof verification could be applied to create challenging benchmarks in other domains where human-AI parity is approaching. [Speculative: not validated outside this benchmark.]

---

## Key Claims

1. **C1: LongBench v2 is sufficiently challenging.** Human experts achieve only 53.7% accuracy under a 15-minute time constraint, compared to 25% random guessing. The five-step pipeline with automated and manual review ensures difficulty calibration (Table 1, Table 2, Section 3.2). Status: **supported**.

2. **C2: o1-preview surpasses human experts.** o1-preview achieves 57.7% accuracy, exceeding the human baseline by 4 percentage points. This is achieved through extended inference-time reasoning, not direct answer generation (Table 2, Section 4.1). Status: **supported**.

3. **C3: Scaling test-time compute is highly effective.** o1-preview vs. GPT-4o: +7.6%. o1-mini vs. GPT-4o-mini: +8.5%. CoT prompting yields an average +3.4% improvement for open-source models (Table 2, Section 4.1). Status: **supported**.

4. **C4: Model parameter scaling improves performance.** Smaller models (~7-9B) score around 30%, while larger counterparts (~70B+) achieve around or above 40% (Table 2, Section 4.1). Status: **supported**.

5. **C5: Models outperform humans on short contexts but underperform on medium contexts.** On Short (<32K), the best model surpasses human performance by 15.4%. On Medium (32K--128K), even the top model trails human accuracy by 5.6--8.9% (Table 2, Section 4.1). Note: task distribution differences across length ranges confound single-model length comparisons. Status: **supported** (with caveat).

6. **C6: RAG provides limited benefit on LongBench v2.** Qwen2.5 and GLM-4-Plus show no improvement beyond 32K retrieval context. GPT-4o's best RAG performance still lags behind its non-RAG score by 0.6%. This confirms questions cannot be solved solely through retrieval (Figure 4, Section 4.2). Status: **supported**.

7. **C7: Memorization is minimal.** Without context, most models achieve 25--30% accuracy (random-guessing level). Slightly higher memorization on single-doc QA and code repo tasks, likely from training data overlap (Table 3, Section 4.3). Status: **supported**.

8. **C8: Structured data understanding is the weakest area for LLMs.** The performance gap between LLMs and humans is largest on long structured data understanding tasks. The authors hypothesize that models have seen less structured data during long-context training (Figure 3, Table 3, Section 4.1). Status: **supported**.

---

## Open Questions

1. **How does scaling inference-time compute interact with context length?** o1-preview's extended reasoning is the most effective strategy overall, but its advantage varies across length ranges and tasks. Whether inference-time scaling can compensate for degraded context utilization at longer lengths is not fully explored. Not yet addressed.

2. **Why does YaRN have a larger impact under the CoT setting?** YaRN with scaling factor 4.0 shows greater improvements with CoT prompting than zero-shot, but the underlying reasons remain unclear (Table 4, Appendix E). Not yet addressed.

3. **Can structured data understanding be improved through targeted training?** The largest model-human gap is on structured data tasks, suggesting training corpora underrepresent structured formats. Whether targeted data composition can close this gap is unexplored. Not yet addressed.

4. **How would LongBench v2 results change with multilingual evaluation?** The benchmark is English-only. Cross-lingual long-context capabilities remain untested (Section 6). Partially addressed by LongBench Pro (2026-01-longbench-pro), which includes bilingual coverage.

---

## Core References and Why They Are Referenced

### Long-Context Evaluation Benchmarks

- **Bai et al. (2024b)** -- *LongBench.* The predecessor benchmark by the same group, published at ACL 2024. LongBench v2 extends it with harder questions requiring deep reasoning rather than shallow retrieval, a uniform multiple-choice format, and lengths up to 2M words.
- **Zhang et al. (2024d)** -- *InfiniteBench.* A benchmark extending evaluation beyond 100K tokens. LongBench v2 contrasts with it as having more reliable evaluation (multiple-choice vs. ROUGE/F1) and human-verified difficulty calibration.
- **Hsieh et al. (2024)** -- *RULER.* A synthetic benchmark with controllable length. LongBench v2 cites RULER as representative of benchmarks that fail to reflect deep understanding capabilities, since synthetic tasks do not capture real-world complexity.
- **Yen et al. (2024)** -- *HELMET.* A methodology-focused evaluation framework. Referenced alongside RULER and LongBench as part of the existing benchmark landscape that LongBench v2 addresses.
- **Shaham et al. (2023)** -- *ZeroSCROLLS.* A zero-shot long-context benchmark referenced as an earlier comprehensive evaluation effort, part of the timeline of multitask long-context benchmarks.
- **An et al. (2024)** -- *L-Eval.* Standardized long-context evaluation benchmark. Referenced as part of the benchmark landscape; LongBench v2 integrates and expands subtask categories from L-Eval and LongBench.
- **Kuratov et al. (2024)** -- *BABILong.* Cited as part of the retrieval and reasoning benchmark category. BABILong extends NIAH with reasoning tasks but uses synthetic data, while LongBench v2 uses fully natural documents.
- **Kamradt (2023)** -- *Needle-in-a-Haystack.* Cited as evidence that modern models achieve near-perfect retrieval, motivating the need for benchmarks that test deeper understanding beyond simple information extraction.

### Models and Architectures

- **OpenAI (2024b)** -- *o1-preview.* The top-performing model on LongBench v2 (57.7%), surpassing human experts by 4%. Its extended inference-time reasoning provides the primary evidence for the scaling-test-time-compute thesis.
- **OpenAI (2024c)** -- *GPT-4o.* The strongest non-reasoning model (50.1% zero-shot, 51.2% CoT), used as the primary baseline for RAG and memorization experiments.
- **Anthropic (2024)** -- *Claude-3.5-Sonnet.* Evaluated as a proprietary baseline (41.0% zero-shot, 46.7% CoT) with a 200K context window, the largest among evaluated models.
- **GLM et al. (2024)** -- *GLM-4.* Both GLM-4-9B-Chat and GLM-4-Plus are evaluated. Three GLM-4 variants (GPT-4o-mini, GLM-4-Air, GLM-4-Flash) serve as the automated review screening panel.
- **Dubey et al. (2024)** -- *Llama 3.* Multiple Llama-3.1 and Llama-3.3 variants evaluated. Performance differences between 8B and 70B variants illustrate the parameter scaling effect on LongBench v2.
- **Qwen Team (2024)** -- *Qwen2.5.* 7B and 72B variants evaluated, also used as the primary models for YaRN and RAG experiments.

### Context Extension Methods

- **Peng et al. (2024)** -- *YaRN.* Evaluated with Qwen2.5 models using scaling factor 4.0 (Table 4). YaRN yields significant improvements, especially on Medium and Long samples, demonstrating that context extension remains beneficial even on deep reasoning tasks.

### Foundational Techniques

- **Wei et al. (2022)** -- *Chain-of-Thought Prompting.* Motivates the CoT evaluation setting. CoT yields an average +3.4% improvement for open-source models, and the extended reasoning in o1-preview yields +7.6% over GPT-4o.
- **Lewis et al. (2020)** -- *Retrieval-Augmented Generation.* The RAG evaluation (Section 4.2) uses a standard RAG pipeline to demonstrate that LongBench v2 questions cannot be solved by retrieval alone, as performance plateaus or degrades at longer retrieval contexts.
- **Rein et al. (2023)** -- *GPQA.* Provides both the Google-proof verification methodology adapted by LongBench v2 and the CoT evaluation protocol (generate reasoning first, then select the answer).
