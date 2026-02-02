# LongBench v2: Towards Deeper Understanding and Reasoning on Realistic Long-context Multitasks

**Authors:** Yushi Bai, Shangqing Tu, Jiajie Zhang, Hao Peng, Xiaozhi Wang, Xin Lv, Shulin Cao, Jiazheng Xu, Lei Hou, Yuxiao Dong, Jie Tang, Juanzi Li (Tsinghua University, Zhipu.AI)
**Date:** July 2025, ACL 2025 (arXiv:2412.15204)

---

## Core Research Problem

Long-context LLMs have rapidly expanded their context windows from 8K to 128K and even 1M tokens (OpenAI, 2024; Anthropic, 2024; Reid et al., 2024; GLM et al., 2024), yet existing evaluation benchmarks fail to test whether models truly comprehend and reason over these long inputs.

- **Existing benchmarks focus on shallow understanding.** Benchmarks such as LongBench (Bai et al., 2024b), InfinityBench (Zhang et al., 2024d), and RULER (Hsieh et al., 2024) primarily test extractive questions where the answer is directly found in the material -- a task easily handled by modern long-context models and RAG systems, as evidenced by near-perfect Needle-in-a-Haystack scores.
- **Synthetic tasks limit real-world applicability.** Many benchmarks rely on synthetic data construction, which does not reflect the complexity of real-world long-context reasoning scenarios.
- **Evaluation metrics are unreliable.** Widely adopted metrics such as ROUGE and F1 are known to correlate poorly with human judgment (Novikova et al., 2017). LLM-as-a-judge evaluation is costly and may introduce biases (Bai et al., 2024c; Ye et al., 2024).

**The core challenge is how to build a long-context benchmark that tests deep understanding and reasoning -- not just retrieval -- across diverse realistic tasks, with reliable evaluation and sufficient difficulty to differentiate current state-of-the-art models.**

---

## Problem Solutions

LongBench v2 addresses this challenge through a 503-question multiple-choice benchmark with four design pillars:

1. **Length coverage.** Contexts range from 8K to 2M words, with the majority under 128K, covering the full operational range of modern long-context LLMs.
2. **Difficulty calibration.** Each question is verified to be challenging enough that human experts using document search tools cannot answer correctly in under 3 minutes, and at least one of three screening LLMs answers incorrectly.
3. **Task diversity.** Six major task categories and 20 subtasks cover realistic long-context scenarios: single-document QA, multi-document QA, long in-context learning, long-dialogue history understanding, code repository understanding, and long structured data understanding.
4. **Reliable evaluation.** A uniform multiple-choice format with four options eliminates metric ambiguity, with a random-guessing baseline of 25%.

---

## Approach Details

### Method

LongBench v2 organizes 503 multiple-choice questions across six major task categories subdivided into 20 subtasks. All data is in English. Each sample consists of a long text, a question, four choices, a groundtruth answer, and supporting evidence.

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

The 20 subtasks include: academic, literary, legal, financial, governmental, detective, and event-ordering QA (single-doc); academic, legal, financial, governmental, multi-news QA (multi-doc); user guide QA, new language translation, many-shot learning (ICL); agent history QA, dialogue history QA (dialogue); code repo QA (code); table QA, knowledge graph reasoning (structured data).

**Data collection pipeline (Figure 2).** Five steps:

1. **Document Collection.** Annotators upload documents they have personally read or used. Documents are automatically checked for minimum length (8,192 words) and overlap with existing annotations.

2. **Data Annotation.** Annotators propose a multiple-choice question with four choices, a groundtruth answer, and evidence. Specific question types are prohibited: counting questions (>10 items), simple retrieval questions, overly professional questions, deliberately difficult questions, and questions depending on visual understanding.

3. **Automated Review.** Three LLMs (GPT-4o-mini, GLM-4-Air, GLM-4-Flash) answer each question. If all three answer correctly, the question is considered too easy and returned for revision.

4. **Manual Review.** A human expert reviewer downloads the raw files, answers the question using document search tools, and checks a quality checklist. Questions answered correctly within 3 minutes are deemed too easy. Time spent is tracked. Experts may respond "I don't know the answer" after 15 minutes.

5. **Data Revision.** Questions failing automated or manual review are returned to annotators with categorized feedback: illegal question, insufficient difficulty, or wrong answer. Up to five revision cycles are permitted.

**Difficulty and length categorization.** Data is classified into two difficulty levels: "Easy" (192 samples) and "Hard" (311 samples). A sample is classified as Hard if at most one of three screening LLMs answers correctly and the human reviewer cannot solve it within 10 minutes. Length is divided into three groups: "Short" (<32K words, 180 samples), "Medium" (32K--128K, 215 samples), and "Long" (>128K, 108 samples).

**Annotation workforce.** 97 annotators from top universities with diverse academic backgrounds (CS 29%, Law 24%, Economics 22%, others), ranging from bachelor's to PhD level. 24 professional human experts selected for manual review. Total data collection cost: approximately 100,000 CNY.

**Incentive mechanism.** Base reward of 100 CNY per accepted question. Length bonuses: +20 CNY (32K--64K), +40 CNY (64K--128K), +50 CNY (>128K). Difficulty bonus: +50 CNY for Hard samples. Reviewers receive 25 CNY per review.

**Data verification.** Author verification of 70 sampled data points: 68/70 (97.1%) correct answers, 67/70 (95.7%) Google-proofed. Answer distribution across options: A 19%, B 25%, C 30%, D 26%.

### Experimental Setup

- **Models:** 10 open-source LLMs (all with 128K context windows): GLM-4-9B-Chat, Llama-3.1-8B/70B-Instruct, Llama-3.3-70B-Instruct, Llama-3.1-Nemotron-70B-Instruct, Qwen2.5-7B/72B-Instruct, Mistral-Large-Instruct-2407/2411, c4ai-command-r-plus-08-2024. 7 proprietary LLMs: GLM-4-Plus, GPT-4o-mini, GPT-4o (two versions), o1-mini, o1-preview, Claude-3.5-Sonnet.
- **Evaluation settings:** Zero-shot and zero-shot + CoT. In the CoT setting, the model first generates a chain of thought (max 1,024 tokens), then produces a final answer (max 128 tokens). Temperature = 0.1 for all settings.
- **Truncation:** Middle truncation for sequences exceeding the model's context window (following Bai et al., 2024b).
- **Qwen2.5 with YaRN:** Evaluated separately with scaling factor 4.0 (Table 4).

### Key Results

**Main evaluation (Table 2, selected models, zero-shot and CoT):**

| Model | Overall | Overall (CoT) | Easy (CoT) | Hard (CoT) | Short (CoT) | Medium (CoT) | Long (CoT) |
|---|---|---|---|---|---|---|---|
| o1-preview | 57.7 | 56.2 | 58.9 | 54.6 | 64.6 | 50.2 | 54.3 |
| GPT-4o (08-06) | 50.1 | 51.2 | 57.9 | 47.1 | 53.9 | 50.7 | 47.7 |
| Claude-3.5-Sonnet | 41.0 | 46.7 | 55.2 | 41.5 | 53.9 | 41.9 | 44.4 |
| GLM-4-Plus | 44.3 | 46.1 | 52.1 | 42.4 | 53.3 | 44.7 | 37.0 |
| Qwen2.5-72B-Instruct | 39.4 | 38.8 | 42.2 | 36.7 | 50.0 | 28.8 | 39.8 |
| Llama-3.1-70B-Instruct | 31.6 | 36.2 | 35.9 | 36.3 | 45.0 | 34.0 | 25.9 |
| Human (15 min) | 53.7 | -- | 100 | 25.1 | 47.2 | 59.1 | 53.7 |

Key findings:

- **(1) o1-preview surpasses human experts.** The best model (o1-preview, 57.7%) exceeds human expert performance (53.7%) under a 15-minute time constraint by 4%. This is achieved through extended inference-time reasoning, not through direct answer generation.

- **(2) Scaling test-time compute is highly effective.** o1-preview vs. GPT-4o: +7.6%. o1-mini vs. GPT-4o-mini: +8.5%. CoT prompting alone yields an average +3.4% improvement for open-source models.

- **(3) Model scaling law holds.** Smaller models (GLM-4-9B-Chat, Qwen2.5-7B-Instruct, GPT-4o-mini) score around 30%, while their larger counterparts (GLM-4-Plus, Qwen2.5-72B-Instruct, GPT-4o) achieve around or above 40%.

- **(4) Models outperform humans on short contexts but underperform on medium contexts.** On Short (<32K), the best model surpasses human performance by 15.4%. On Medium (32K--128K), even the top model trails human accuracy by 5.6%.

- **(5) RAG provides limited benefit.** Qwen2.5 and GLM-4-Plus show no improvement beyond 32K retrieval context length. Both perform better with 32K RAG context than with the full 128K context window without RAG (Qwen2.5: +4.1%). Only GPT-4o effectively leverages longer retrieval contexts, but still lags behind its non-RAG score by 0.6%. This confirms that LongBench v2 questions cannot be solved solely through retrieval.

- **(6) Memorization is minimal.** Without context, most models achieve 25--30% accuracy (random-guessing level). The memorization effect is slightly higher for single-document QA and code repository tasks, likely because models may have encountered some of these documents during training.

- **(7) Structured data understanding is the weakest area.** The performance gap between LLMs and humans is largest on long structured data understanding tasks. On single-doc and multi-doc QA, models perform at or surpass human levels.

**YaRN results (Table 4):**

| Model | Overall | Overall (+YaRN) | Medium | Medium (+YaRN) | Long | Long (+YaRN) |
|---|---|---|---|---|---|---|
| Qwen2.5-7B-Instruct (CoT) | 29.8 | **35.6** | 26.5 | **32.6** | 26.9 | **27.8** |
| Qwen2.5-72B-Instruct (CoT) | 38.8 | **43.5** | 28.8 | **40.9** | 39.8 | 39.8 |

YaRN significantly enhances long-context processing on LongBench v2, particularly on Medium and Long samples. The impact is larger under the CoT setting.

### Limitations

1. **Benchmark size.** 503 samples may lead to less stable results vulnerable to randomness. Expansion was limited by cost (100,000 CNY, over two months).
2. **Language.** English only, preventing cross-lingual evaluation.
3. **Length distribution inconsistencies.** Task distributions differ across length ranges, making single-model comparisons across length intervals unreliable. The authors recommend between-model comparisons within each length interval.

---

## Conclusions

1. **Challenging benchmark at the frontier of human-AI parity.** Human experts achieve only 53.7% under a 15-minute time constraint (vs. 25% random guessing), while the best model (o1-preview) reaches 57.7%, providing a reliable evaluation standard for both current and future superhuman AI systems.

2. **Deep reasoning matters more than retrieval.** Questions are deliberately designed to resist retrieval-based solving. RAG experiments confirm that retrieval alone does not solve LongBench v2, and models must actively reason over the long context to answer correctly.

3. **Scaling inference-time compute is the most effective strategy.** o1-preview's extended reasoning yields +7.6% over GPT-4o, a larger gain than model scaling or CoT prompting alone. This highlights inference-time thinking as a crucial direction for long-context reasoning.

4. **Model capability degrades with length, but not uniformly.** Models outperform humans on Short (<32K) data by 15.4% but underperform on Medium (32K--128K) by 5.6%, indicating that maintaining reasoning capability under longer contexts remains an open challenge.

5. **Quality-controlled human annotation at scale is feasible but expensive.** The five-step pipeline with automated and manual review achieves a ~3% error rate and ~96% Google-proof rate, demonstrating that high-quality long-context evaluation data can be collected at the cost of ~200 CNY per accepted sample.

6. **Structured data understanding is a blind spot.** The largest model-human gap is on long structured data tasks (tables and knowledge graphs), suggesting that long-context training corpora underrepresent structured formats.

---

## Core References and Why They Are Referenced

### Long-Context Evaluation Benchmarks

- **Bai et al. (2024b)** -- *LongBench.* The predecessor benchmark by the same group, published at ACL 2024. LongBench v2 extends it with harder questions requiring deep reasoning rather than shallow retrieval, a uniform multiple-choice format, and lengths up to 2M words.
- **Zhang et al. (2024d)** -- *InfinityBench.* A benchmark extending evaluation beyond 100K tokens. LongBench v2 contrasts with it as having more reliable evaluation (multiple-choice vs. ROUGE/F1) and human-verified difficulty calibration.
- **Hsieh et al. (2024)** -- *RULER.* A synthetic benchmark with controllable length. LongBench v2 cites RULER as representative of benchmarks that fail to reflect deep understanding capabilities, since synthetic tasks do not capture real-world complexity.
- **Yen et al. (2024)** -- *HELMET.* A methodology-focused evaluation framework. Referenced alongside RULER and LongBench as part of the existing benchmark landscape that LongBench v2 addresses.
- **Shaham et al. (2023)** -- *ZeroSCROLLS.* A zero-shot long-context benchmark referenced as an earlier comprehensive evaluation effort.
- **Kuratov et al. (2024)** -- *BABILong.* Cited as part of the retrieval and attribution benchmark category. BABILong extends NIAH with reasoning tasks but uses synthetic data, while LongBench v2 uses fully natural documents.

### Models and Architectures

- **OpenAI (2024b)** -- *o1-preview.* The top-performing model on LongBench v2 (57.7%), surpassing human experts by 4%. Its extended inference-time reasoning provides the strongest evidence for the scaling-test-time-compute thesis.
- **OpenAI (2024c)** -- *GPT-4o.* The strongest non-reasoning model (50.1%), used as the primary baseline for RAG and memorization experiments.
- **Anthropic (2024)** -- *Claude-3.5-Sonnet.* Evaluated as a proprietary baseline (41.0% zero-shot, 46.7% CoT) with a 200K context window, the largest among evaluated models.
- **GLM et al. (2024)** -- *GLM-4.* Both GLM-4-9B-Chat and GLM-4-Plus are evaluated, and three GLM-4 models (GPT-4o-mini, GLM-4-Air, GLM-4-Flash) serve as the automated review screening panel.
- **Dubey et al. (2024)** -- *Llama 3.* Multiple Llama-3.1 and Llama-3.3 variants are evaluated. Performance differences between Llama-3.1-8B and 70B illustrate the parameter scaling law on LongBench v2.

### Context Extension Methods

- **Peng et al. (2024)** -- *YaRN.* Evaluated with Qwen2.5 models (Table 4). YaRN with scaling factor 4.0 yields significant improvements, especially on Medium and Long samples, demonstrating that context extension remains beneficial even on deep reasoning tasks.

### Foundational Techniques

- **Wei et al. (2022)** -- *Chain-of-Thought Prompting.* Motivates the CoT evaluation setting. CoT yields an average +3.4% improvement for open-source models, and the extended reasoning in o1-preview yields +7.6% over GPT-4o.
- **Lewis et al. (2020)** -- *Retrieval-Augmented Generation.* The RAG evaluation (Section 4.2) uses the standard RAG pipeline to demonstrate that LongBench v2 questions cannot be solved by retrieval alone, as performance plateaus or degrades at longer retrieval contexts.
- **Rein et al. (2023)** -- *GPQA.* Provides the Google-proof verification methodology adapted by LongBench v2 to ensure questions cannot be answered from internet search. Also provides the CoT evaluation protocol (model generates reasoning first, then selects the answer).

#### Cross-References in Available Papers

- **RULER (2024-10-ruler-context-size):** LongBench v2 explicitly lists RULER (Hsieh et al., 2024) as one of the existing benchmarks that fails to reflect deep understanding capabilities (Section 1, Section 2). Both benchmarks share the observation that existing evaluations over-rely on retrieval, but LongBench v2 addresses this with human-verified reasoning questions rather than synthetic tasks.
- **BABILong (2024-12-babilong-long-context-reasoning):** LongBench v2 cites Kuratov et al. (2024) among retrieval and attribution benchmarks (Section 2). Both benchmarks aim to move beyond simple NIAH evaluation, but BABILong uses synthetic bAbI tasks embedded in PG19 text while LongBench v2 uses naturally occurring documents with human-annotated questions.
- **YaRN (2024-05-yarn-context-extension):** LongBench v2 evaluates Qwen2.5 models with YaRN context extension (Table 4, Appendix E), finding significant improvements especially on longer samples. This complements BABILong's finding that YaRN fails on synthetic reasoning tasks -- suggesting YaRN's benefits depend on task type (deep reasoning on natural text vs. synthetic multi-hop).
- **LongBench Pro (2026-01-longbench-pro):** LongBench Pro is the direct successor of LongBench v2, extending it with bilingual coverage (EN + ZH vs. EN only), diverse task-specific metrics (vs. single multiple-choice accuracy), fine-grained categorization across three dimensions (context requirement, length with six levels, difficulty with four model-calibrated levels), and a larger dataset (1,500 vs. 503 samples). LongBench Pro also introduces a human-model collaborative construction pipeline that scales beyond LongBench v2's purely human annotation approach.
