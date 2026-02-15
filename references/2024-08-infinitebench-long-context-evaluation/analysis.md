---
title: "∞Bench: Extending Long Context Evaluation Beyond 100K Tokens"
authors: "Zhang, Chen, Hu, Xu, Chen, Moo, Han, Thai, Wang, Liu, Sun"
year: 2024
venue: "ACL 2024"
paper_type: conference-paper
categories: ["benchmarking", "long-context-evaluation"]
scope: ["100K+ token evaluation", "bilingual benchmark", "mixed synthetic and natural tasks"]
benchmarks_used: ["infinitebench"]
models_introduced: []
models_evaluated: ["gpt-4", "claude-2.1", "mistral-7b", "moonshot-v1-128k"]
key_claims:
  - id: C1
    claim: "∞Bench is the first LLM benchmark with average data length surpassing 100K tokens, spanning 5 domains in English and Chinese with 12 tasks and 3,946 examples"
    evidence: "Table 1, Table 2, Section 3"
    status: supported
    scope: "public benchmarks as of Feb 2024, English and Chinese"
    magnitude: "~200K average token length vs ~10K for LongBench and LRA"
  - id: C2
    claim: "All evaluated models show significant performance degradation at 100K+ contexts compared to shorter contexts"
    evidence: "Table 3, Figure 4, Section 4.3 and 5.1"
    status: supported
    scope: "4 models (GPT-4, Claude 2, Kimi-Chat, YaRN-Mistral), auto-generated tasks with controllable length"
    magnitude: "average scores 19.96--45.63%; GPT-4 Code.Run drops from ~75% at depth 2 to ~20% at depth 10"
  - id: C3
    claim: "No consistent lost-in-the-middle effect exists at 100K+ contexts; position-dependent performance is task- and model-specific"
    evidence: "Figure 5, Section 5.2"
    status: supported
    contested_by: 2024-02-lost-in-the-middle
    scope: "4 models, 3 position-dependent tasks (Retrieve.Number, Retrieve.KV, En.Dia), 100K+ context lengths"
    magnitude: "qualitative -- no universal U-shaped pattern; GPT-4 favors early answers on KV but later on En.Dia"
  - id: C4
    claim: "Context recalling prompting improves GPT-4 Code.Debug accuracy from 15.74% to 39.59%"
    evidence: "Section 5.3, Figure 6"
    status: supported
    scope: "GPT-4 only, Code.Debug task only, single prompt comparison"
    magnitude: "15.74% to 39.59% (2.5x improvement)"
  - id: C5
    claim: "Open-source YaRN-Mistral-7B-128K substantially underperforms proprietary models (19.96% vs 45.63% average)"
    evidence: "Table 3, Section 4.3"
    status: supported
    scope: "YaRN-Mistral-7B-128K vs GPT-4/Claude 2/Kimi-Chat, all 12 InfiniteBench tasks"
    magnitude: "19.96% average vs 45.63% (GPT-4), 37.06% (Claude 2), 34.73% (Kimi-Chat); 0% on Retrieve.KV"
cross_references:
  - target: 2023-12-landmark-attention-infinite-context
    type: extends
    detail: "Retrieve.PassKey task adapted from Mohtashami and Jaggi (2023) with 59 positions and 590 examples"
  - target: 2024-02-lost-in-the-middle
    type: contradicts
    detail: "Finds no consistent lost-in-the-middle effect at 100K+ contexts, unlike Liu et al. (2023) at 16K; also adapts Retrieve.KV task"
  - target: 2024-05-yarn-context-extension
    type: evaluates
    detail: "YaRN-Mistral-7B-128K is a baseline model, achieving 19.96% average"
  - target: 2024-08-longbench-bilingual-benchmark
    type: complementary
    detail: "LongBench (~10K avg tokens) is the closest prior benchmark; ∞Bench addresses its limited context length"
  - target: 2024-08-l-eval-standardized-evaluation
    type: complementary
    detail: "L-Eval reaches up to 60K tokens; ∞Bench surpasses its length ceiling by over 3x"
  - target: 2021-05-long-range-arena
    type: complementary
    detail: "LRA (~10K tokens) targets efficient transformers; ∞Bench targets LLMs at 100K+ with broader domain coverage"
  - target: 2024-10-ruler-context-size
    type: complementary
    detail: "RULER provides controllable synthetic evaluation; ∞Bench combines synthetic and realistic tasks at 100K+"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong extends to 10M tokens with reasoning focus; ∞Bench provides realistic multi-domain tasks at 100K+"
  - target: 2025-04-helmet-long-context-evaluation
    type: extended-by
    detail: "HELMET directly compares against InfiniteBench, showing that improved prompting and model-based evaluation yield more reliable rankings than InfiniteBench's ROUGE-based metrics"
  - target: 2025-07-nolima-long-context-evaluation
    type: complementary
    detail: "NoLiMa identifies InfiniteBench QA as having the highest literal overlap measured (ROUGE-1 = 0.966); NoLiMa provides a complementary low-overlap evaluation (ROUGE-1 = 0.069)"
  - target: 2025-07-longbench-v2
    type: complementary
    detail: "LongBench v2 contrasts with InfiniteBench as having more reliable evaluation (multiple-choice vs ROUGE/F1) and human-verified difficulty calibration"
  - target: 2026-01-longbench-pro
    type: complementary
    detail: "LongBench Pro references ∞Bench as a mixed synthetic/natural benchmark"
  - target: 2025-03-longiclbench-long-in-context-learning
    type: complementary
    detail: "LongICLBench provides a complementary evaluation paradigm at 2K-50K tokens requiring full label-space comprehension via extreme-label ICL rather than information retrieval"
  - target: 2024-07-llama-3-herd-of-models
    type: extended-by
    detail: "Llama 3 405B achieves 83.4% on En.MC, outperforming GPT-4 (72.0%)"
open_questions:
  - question: "Is the context recalling prompting technique generalizable beyond Code.Debug to other long-context tasks?"
    addressed_by: null
  - question: "How do lost-in-the-middle effects change as context lengths scale from 16K to 100K+ tokens?"
    addressed_by: 2024-08-found-in-the-middle
  - question: "Can evaluation be extended to million-token scales with realistic (non-synthetic) tasks?"
    addressed_by: 2024-12-babilong-long-context-reasoning
---
# ∞Bench: Extending Long Context Evaluation Beyond 100K Tokens

**Authors:** Xinrong Zhang, Yingfa Chen, Shengding Hu, Zihang Xu, Junhao Chen, Moo Khai Hao, Xu Han, Zhen Leng Thai, Shuo Wang, Zhiyuan Liu, Maosong Sun (Tsinghua University)
**Date:** August 2024, ACL 2024 Long Papers (arXiv:2402.13718)

---

## Core Research Problem

Despite rapid advances in LLM context windows -- with GPT-4 Turbo (128K), Claude 2 (200K), and Kimi-Chat (200K) claiming to process over 100K tokens -- existing long-context benchmarks lag far behind. LongBench (Bai et al., 2023) averages ~10K tokens across 21 tasks; L-Eval (An et al., 2023) reaches at most 60K; LRA (Tay et al., 2020) averages ~10K; and LooGLE (Li et al., 2023) averages ~20K. No public benchmark at the time had an average data length surpassing 100K tokens (Table 1, Section 2).

This length gap creates two problems. First, it is impossible to comparatively evaluate models that claim 100K+ context support when benchmarks test only at 10K. Second, existing benchmarks are dominated by retrieval-style tasks or tasks where parametric knowledge can compensate for failure to process the full context -- simply retrieving a limited number of passages is often sufficient to answer questions, making these benchmarks unable to isolate genuine long-context reasoning from short-context retrieval ability.

**The core challenge is how to construct a standardized, multi-domain, bilingual benchmark with average data length exceeding 100K tokens, featuring tasks that require genuine understanding of long-range dependencies rather than simple passage retrieval.**

---

## Problem Solutions

∞Bench is the first LLM benchmark with an average data length surpassing 100K tokens (~200K average across all tasks). It spans 5 domains (retrieval, code, math, novels, dialogue) in both English and Chinese, with 12 tasks totaling 3,946 examples.

1. **Multi-domain realistic and synthetic tasks.** The benchmark combines human-annotated tasks from realistic contexts (novels, code repositories, movie scripts) with auto-generated synthetic tasks (passkey retrieval, number retrieval, key-value lookup, code execution, arithmetic).
2. **Tasks requiring long-range dependencies.** Novel-based tasks use aggregation (compiling information scattered throughout the text) and filtering (identifying specific information from a large set), both requiring processing of the full context. Synthetic tasks test retrieval at elevated resolution, state preservation, and sequential processing.
3. **Data contamination countermeasures.** Novel-based tasks employ key entity replacement -- substituting prominent character names with unrelated ones to create "fake novels" -- preventing LLMs from relying on training data memorization.

---

## Approach Details

### Method

∞Bench constructs tasks in two broad categories: realistic context tasks using real-world data, and synthetic context tasks testing specific long-context capabilities.

**Realistic context tasks:**

- **Novel-based tasks (En.Sum, En.QA, En.MC, Zh.QA):** Entire novels are presented at inference time, with key entities replaced by unrelated names. Annotators create questions requiring two types of reasoning: (1) **aggregation** -- compiling various pieces of information scattered throughout the novel (e.g., "How much money in total did A spend on lunch?"); and (2) **filtering** -- identifying specific information from a larger set (e.g., "What color dress did A wear when A met B for the second time?"). En.Sum requires generating a concise summary; En.MC provides four answer choices annotated to be challenging (Section 3.1.1).
- **Dialogue (En.Dia):** Movie and drama scripts from IMSDB, with random character name instances replaced by `$$MASK$$`; the model must identify the masked character. Scripts shorter than 100K tokens are padded with additional scripts (Section 3.1.2).
- **Code debugging (Code.Debug):** Real Python packages from PyPI (64K--256K tokens) with a deliberate, obvious error injected into one function. Six bug injection methods are used: (1) deleting a necessary variable declaration; (2) incorrect number of function arguments; (3) infinite loops; (4) indentation errors; (5) undefined variable/function references; (6) blatant syntax errors. Presented in four-choice format because the open-ended version is too difficult for current LLMs (Section 3.1.3).

**Synthetic context tasks** test four essential capabilities for long-context processing:

- **Location and retrieval (Retrieve.PassKey, Retrieve.Number, Retrieve.KV):** PassKey retrieves a random 5-digit sequence from noisy text (adapted from Mohtashami and Jaggi, 2023, with 59 evenly-distributed positions and 590 examples). Number retrieves a 10-digit answer with successive repetitive digits (e.g., 9998877762), testing local attention resolution. KV retrieves a value from a large JSON object of UUID key-value pairs (adapted from Liu et al., 2023), where relevant and irrelevant information share the same format (Section 3.2.1).
- **State preservation (Code.Run, Math.Find):** Code.Run simulates multi-step Python function executions with addition/subtraction and nested calls at depths 2--10. Math.Find locates specific elements (3 largest, 3 smallest, median) in a large number array (Sections 3.2.2--3.2.3).
- **Sequential processing (Math.Calc):** Computes intermediate results of a long arithmetic expression. Models provide intermediate values after each operator rather than a final answer, since no model can produce the final result directly (Section 3.2.3).

### Key Technical Components

**Annotation pipelines.** Five distinct annotation pipelines are used for human-annotated tasks (Figure 3). Each annotation is quality-checked by at least two other annotators. Novel tasks share a pipeline covering entity replacement, question annotation, and answer/option annotation. The annotation work is performed by the paper's authors (Appendix C).

**Key entity replacement.** Prominent entities (main character names) are replaced with unrelated names to prevent LLMs from leveraging training data knowledge of well-known novels. Some novels are exempt from replacement because they are too obscure for LLMs to recognize (Appendix C).

**Evaluation metrics.** Exact match for most tasks; ROUGE-L-Sum for En.Sum. For multiple-choice tasks, failure to output a valid option receives a score of 0. For Math.Calc, performance is measured by the number of correct intermediate values before the first error.

**Input truncation.** For models with maximum input length limits, inputs are truncated by removing the center and joining both ends, based on the assumption that key information (instructions, book titles) is typically at the start or end of the prompt (Section 4.2).

### Experimental Setup

**Models evaluated (4 baselines):**

| Model | Context Length | Access Method |
|---|---|---|
| GPT-4 (gpt-4-0125-preview) | 128K | API (~$5,000 total cost) |
| Claude 2 | 200K | Manual web interface (3 authors, several weeks, ~$160) |
| Kimi-Chat (Moonshot AI) | 200K | Manual web interface (free) |
| YaRN-Mistral-7B-128K | 128K | 1x A100 80GB GPU, ~10 min/example |

An additional experiment with RWKV-4-World-7B is reported in Appendix A, but it produces unintelligible output at these lengths (0% on Retrieve.PassKey) due to being trained only on 4K sequences. The authors emphasize this does not reflect the RWKV architecture's inherent capability (Table 4).

**Data statistics (Table 2):**

| Task | Annotation | # Examples | Avg Length (input/output tokens) |
|---|---|---|---|
| Retrieve.PassKey | Auto | 590 | 122.4K / 2 |
| Retrieve.Number | Auto | 590 | 122.4K / 4 |
| Retrieve.KV | Auto | 500 | 121.1K / 22.7 |
| En.Sum | Human | 103 | 103.5K / 1.1K |
| En.QA | Human | 351 | 192.6K / 4.8 |
| En.MC | Human | 229 | 184.4K / 5.3 |
| Zh.QA | Human | 189 | 2,068.6K / 6.3 |
| En.Dia | Auto | 200 | 103.6K / 3.4 |
| Code.Debug | Human | 394 | 114.7K / 4.8 |
| Code.Run | Auto | 400 | 75.2K / 1.3 |
| Math.Calc | Auto | 50 | 43.9K / 43.9K |
| Math.Find | Auto | 350 | 87.9K / 1.3 |

Zh.QA is notably the longest task at ~2.07M tokens average input length, using Chinese novels that are substantially longer than the English ones.

**Prompt design.** Model-specific prompt templates are optimized on short dummy examples for each model-task combination. YaRN-Mistral prompts include answer prefixes (e.g., "The pass key is", "The correct option is:") to constrain generation. GPT-4 requires a special system prompt for Math.Calc to avoid refusal (Appendix B).

### Key Results

**Main results (Table 3):**

| Task | GPT-4 | YaRN-Mistral | Kimi-Chat | Claude 2 |
|---|---|---|---|---|
| Retrieve.PassKey | **100.00** | 92.71 | 98.14 | 97.80 |
| Retrieve.Number | **100.00** | 56.61 | 95.42 | 98.14 |
| Retrieve.KV | **89.00** | 0.00 | 53.60 | 65.40 |
| En.Sum | 14.73 | 9.09 | **17.93** | 14.45 |
| En.QA | **22.22** | 9.55 | 16.52 | 11.97 |
| En.MC | 67.25 | 27.95 | **72.49** | 62.88 |
| En.Dia | 8.50 | 7.50 | 11.50 | **46.50** |
| Zh.QA | **23.06** | 16.98 | 18.62 | 10.53 |
| Code.Debug | **39.59** | 0.76 | 18.02 | 2.28 |
| Code.Run | **23.25** | 1.25 | 2.00 | 2.50 |
| Math.Calc | **0.01** | 0.00 | 0.00 | 0.00 |
| Math.Find | **60.00** | 17.14 | 12.57 | 32.29 |
| **Average** | **45.63** | 19.96 | 34.73 | 37.06 |

- **GPT-4 leads overall** with 45.63% average, excelling in retrieval (100% on PassKey and Number), code, and math domains (Section 4.3).
- **No clear winner on novel-based tasks.** Kimi-Chat leads on En.Sum (17.93) and En.MC (72.49); GPT-4 leads on En.QA (22.22) and Zh.QA (23.06); Claude 2 dominates En.Dia (46.50 vs. GPT-4's 8.50).
- **YaRN-Mistral substantially underperforms** proprietary models (19.96% average), showing near-random performance on multiple tasks and 0.00% on Retrieve.KV.
- **Math.Calc is unsolvable** for all models (best: GPT-4 at 0.01%), indicating that sequential processing over very long arithmetic expressions remains far beyond current capabilities.
- **All models struggle on realistic tasks.** Even GPT-4 achieves only 22.22% on En.QA and 14.73 ROUGE-L-Sum on En.Sum.

### Length Ablation

Performance on auto-generated tasks is measured at shortened context lengths (Figure 4, Section 5.1):

- **Retrieve.KV:** GPT-4 maintains ~90% accuracy up to ~1,000 KV pairs, then drops. Kimi-Chat degrades more gradually. YaRN-Mistral scores 0% at all lengths.
- **Math.Find:** All models degrade with increasing array size. GPT-4 drops from ~60% to ~40%.
- **Code.Run:** GPT-4 drops from ~75% at depth 2 to ~20% at depth 10. Other models near 0% at all depths.
- **En.Dia:** GPT-4 drops from ~60% at short scripts to ~8% as script length increases.

**Performance generally declines with longer input lengths**, confirming that models' effectiveness diminishes even though they can technically accept extended inputs.

### Lost-in-the-Middle Analysis

Unlike Liu et al. (2023), who found performance drops when answers are in the middle of 16K contexts, ∞Bench finds **no consistent trend between performance and answer position** across models at 100K+ (Figure 5, Section 5.2):

- GPT-4 favors early answers on Retrieve.KV but later answers on En.Dia.
- Claude 2 is relatively unaffected by answer position across all three tested tasks (Retrieve.Number, Retrieve.KV, En.Dia).
- YaRN-Mistral and Kimi-Chat tend to perform better with end-positioned answers (except YaRN-Mistral's uniform 0% on Retrieve.KV).
- The steep drop for Kimi-Chat in the middle on Retrieve.KV is caused by center truncation removing the answer.

The authors hypothesize that the "lost in the middle" phenomenon is task- and model-specific, and that the 100K+ context setting (roughly 8x longer than Liu et al.'s 16K) may produce qualitatively different position-dependent behaviors.

### Context Recalling

A prompting technique termed **context recalling** is identified: explicitly instructing the model to first repeat/recall relevant information from the context before reasoning (Section 5.3, Figure 6). On Code.Debug with GPT-4:

- Step-by-step prompting ("Think step by step and at last give me your answer"): **15.74%**
- Context recalling ("Locate the functions in the options, repeat their content, inspect through code"): **39.59%**

This 2.5x improvement suggests that prompting models to relocate relevant information into their generation buffer before reasoning is more effective than direct reasoning over the full 100K+ context.

---

## Limitations and Failure Modes

1. **[Inferred] Small set of baselines.** Only 4 models are benchmarked, compared to 34+ in later benchmarks like BABILong (Kuratov et al., 2024). The limited model set restricts the generalizability of observed patterns.
2. **[Inferred] Manual evaluation for two models.** Claude 2 and Kimi-Chat are evaluated by manually entering examples through web interfaces, limiting scalability, reproducibility, and control over decoding parameters (Appendix D).
3. **Exact match scoring sensitivity.** Performance depends on prompt templates and answer parsing, requiring tailored prompt engineering for each model. The paper acknowledges this "may necessitate tailored redesigns for new model evaluations" (Limitations section).
4. **100K ceiling may be insufficient.** The authors note that "supporting contexts up to 100K tokens may fall short for applications requiring analysis of extensive datasets, such as multiple books or entire databases." Later benchmarks like BABILong extend to 10M+ tokens.
5. **[Inferred] No controllable length scaling for realistic tasks.** Unlike BABILong's predefined length splits, ∞Bench's realistic tasks have fixed lengths determined by the source material (novels, code repositories), preventing systematic analysis of performance degradation curves on these tasks.
6. **Limited diversity of benchmark.** The paper acknowledges that ∞Bench "may not be sufficiently diverse or extensive to provide a comprehensive assessment of model capabilities" (Limitations section).

#### Scope and Comparability

- **What was not tested:** Only 4 models were evaluated (3 proprietary, 1 open-source 7B). No models in the 13B--70B open-source range were tested. No evaluation of retrieval-augmented generation (RAG) approaches as baselines. No evaluation with different decoding strategies (temperature, top-p) -- GPT-4 used default API settings, Claude 2 and Kimi-Chat used web interfaces with no control over decoding parameters. RWKV-4-World-7B was tested (Appendix A, Table 4) but excluded from main results due to being trained on only 4K sequences.
- **Comparability notes:** Kimi-Chat and Claude 2 were evaluated via manual web interface entry (not API), making exact reproduction impossible and introducing potential variability. Input truncation (center removal) was applied for inputs exceeding model limits, which affects tasks differently depending on where the answer is located -- the Kimi-Chat Retrieve.KV middle-position drop is directly caused by this truncation. ∞Bench's ~200K average length is substantially longer than LongBench (~10K) and L-Eval (up to 60K), so direct cross-benchmark score comparison is not meaningful. The benchmark uses exact match for most tasks, while other benchmarks may use F1 or LLM-as-judge metrics, further limiting cross-benchmark comparability.

---

## Conclusions

### Contributions

1. **First 100K+ benchmark.** ∞Bench is the first LLM benchmark with average data length surpassing 100K tokens, spanning 5 domains (retrieval, code, math, novels, dialogue) in English and Chinese with 12 tasks and 3,946 examples (Table 1, Table 2).

2. **Demonstrated performance degradation at scale.** All evaluated models show substantial performance drops at 100K+ contexts compared to shorter contexts, establishing that claimed context window sizes do not translate to effective utilization (Table 3, Figure 4).

3. **Retrieval-reasoning gap quantified.** Models excel at retrieval tasks (GPT-4 achieves 100% on PassKey/Number) but struggle with tasks requiring genuine long-range reasoning (22.22% on En.QA, 0.01% on Math.Calc), demonstrating a clear hierarchy of difficulty across task types (Table 3).

4. **Position bias findings at 100K+ contexts.** Unlike prior findings at 16K contexts (Liu et al., 2023), answer position effects are model- and task-specific at ∞Bench's 100K+ lengths, with no universal lost-in-the-middle pattern (Figure 5).

5. **Context recalling technique identified.** Prompting models to explicitly recall relevant information before reasoning yields 2.5x improvement on Code.Debug (15.74% to 39.59% for GPT-4), establishing that generation-time information relocation can be more effective than direct attention over long contexts (Figure 6).

### Implications

1. **Context window claims require benchmark validation.** The gap between claimed context lengths and effective performance at those lengths suggests that benchmark-based evaluation at the claimed length is necessary for meaningful model comparison.

2. **Long-context evaluation needs domain diversity.** The finding that no single model dominates across all task types (GPT-4 leads retrieval/code/math; Kimi-Chat leads summarization/MC; Claude 2 leads dialogue) implies that single-task benchmarks may produce misleading rankings.

3. **Context recalling may indicate an attention bottleneck.** The effectiveness of context recalling suggests that even when information is within the context window, models may struggle to directly attend to and reason over distant tokens -- copying relevant information into the generation buffer may bypass this bottleneck (speculative).

---

## Key Claims

1. **C1: First 100K+ benchmark.** ∞Bench is the first LLM benchmark with average data length surpassing 100K tokens (~200K across tasks), covering 5 domains in 2 languages with 12 tasks and 3,946 examples. Evidence: Table 1 comparison with prior benchmarks; Table 2 data statistics showing average lengths from 43.9K to 2,068.6K tokens. Status: **supported**.

2. **C2: Performance degrades at 100K+.** All evaluated models show significant performance degradation as context length increases, even though they technically accept inputs at these lengths. Evidence: Table 3 main results (average scores 19.96--45.63%); Figure 4 length ablation showing monotonic degradation on auto-generated tasks. Status: **supported**.

3. **C3: No consistent lost-in-the-middle at 100K+.** Position-dependent performance is task- and model-specific at 100K+, with no universal U-shaped degradation pattern. This contrasts with Liu et al. (2023) who found consistent position effects at 16K. Evidence: Figure 5 showing divergent position-performance patterns across models and tasks (Section 5.2). Status: **supported** (though tested on only 4 models and 3 tasks, limiting generalizability).

4. **C4: Context recalling improves long-context performance.** Explicitly prompting GPT-4 to repeat relevant code before analysis improves Code.Debug accuracy from 15.74% (step-by-step) to 39.59% (context recalling). Evidence: Section 5.3, Figure 6 comparing two prompt variants. Status: **supported** (demonstrated on one task and one model).

5. **C5: Open-source models lag substantially.** YaRN-Mistral-7B-128K achieves 19.96% average versus GPT-4's 45.63%, with 0% on Retrieve.KV and near-random performance on several tasks. Evidence: Table 3. Status: **supported** (though comparing a 7B open-source model to proprietary models of unknown size is not size-controlled).

---

## Open Questions

1. **Is context recalling generalizable?** The 2.5x improvement on Code.Debug raises the question of whether prompting models to first recall/repeat relevant context before reasoning is a generally effective strategy for long-context tasks, or specific to code debugging with GPT-4. Not addressed in subsequent work in this collection.

2. **How do position bias effects change with context scale?** ∞Bench's finding of no consistent lost-in-the-middle at 100K+ diverges from Liu et al. (2023) at 16K. How and why these effects change across the 16K--200K range remains unclear. Partially addressed by Peysakhovich and Lerer (2024) in *Found in the Middle*.

3. **Can realistic (non-synthetic) evaluation scale to millions of tokens?** ∞Bench's realistic tasks are limited by source material length. BABILong (Kuratov et al., 2024) extends to 10M tokens but uses synthetic reasoning tasks embedded in book text, not fully realistic tasks.

---

## Core References and Why They Are Referenced

### Long-Context Evaluation Benchmarks

- **Bai et al. (2023)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* The closest prior benchmark, averaging ~10K tokens across 21 tasks in 4 categories. ∞Bench explicitly addresses LongBench's limited context length and inability to evaluate 100K+ models (Table 1).
- **An et al. (2023)** -- *L-Eval: Instituting Standardized Evaluation for Long Context Language Models.* Prior benchmark with 18 tasks reaching up to 60K tokens. ∞Bench surpasses L-Eval's length ceiling by over 3x and adds bilingual coverage (Table 1).
- **Tay et al. (2020)** -- *Long Range Arena: A Benchmark for Efficient Transformers.* Older benchmark (~10K tokens) spanning text, image, and math, designed for efficient transformers. ∞Bench differs by targeting LLMs rather than efficient architectures and using much longer contexts (Table 1).
- **Li et al. (2023)** -- *LooGLE: Can Long-Context Language Models Understand Long Contexts?* Averages ~20K tokens with summary and QA tasks focusing on short vs long dependency examples. ∞Bench provides 10x longer contexts and broader domain coverage (Table 1).

### Task Foundations

- **Mohtashami & Jaggi (2023)** -- *Landmark Attention: Random-Access Infinite Context Length for Transformers.* Source of the Retrieve.PassKey task, which ∞Bench adapts with 59 evenly-distributed positions and 590 examples at 100K+ context lengths (Section 3.2.1).
- **Liu et al. (2023)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Source of the Retrieve.KV task and the "lost in the middle" hypothesis. ∞Bench's analysis at 100K+ contexts finds no consistent position-dependent performance drop, contrasting with Liu et al.'s findings at 16K (Section 5.2).
- **Bubeck et al. (2023)** -- *Sparks of Artificial General Intelligence: Early Experiments with GPT-4.* Demonstrates GPT-4's state tracking capability, motivating the Code.Run task design in ∞Bench (Section 3.2.2).

### Models and Context Extension Methods

- **OpenAI (2023)** -- *GPT-4 Technical Report / GPT-4 Turbo.* The strongest baseline on ∞Bench (45.63% average), supporting 128K contexts. Achieves perfect scores on passkey and number retrieval but struggles on realistic tasks (Table 3).
- **Anthropic (2023)** -- *Claude 2.* Claims 200K context support. Achieves the best performance on En.Dia (46.50%) but lags behind GPT-4 on most other tasks (Table 3).
- **Moonshot AI (2023)** -- *Kimi-Chat.* Proprietary 200K-context model. Leads on En.Sum (17.93) and En.MC (72.49) but underperforms GPT-4 overall (34.73% average, Table 3).
- **Peng et al. (2023b)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Provides the YaRN-Mistral-7B-128K baseline, which substantially underperforms proprietary models (19.96% average), demonstrating that positional encoding modifications alone do not confer robust 100K+ context processing (Table 3).
- **Peng et al. (2023a)** -- *RWKV: Reinventing RNNs for the Transformer Era.* RWKV-4-World-7B is tested in Appendix A but produces unintelligible output at ∞Bench lengths (0% on Retrieve.PassKey) due to being trained on only 4K sequences (Table 4).

### Positional Encoding

- **Su et al. (2023)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE is the positional encoding modified by context extension methods like YaRN that are evaluated on ∞Bench.
- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* Positional interpolation is referenced as a key method for extending LLM context windows, forming the technical background for the models evaluated.

### Infrastructure

- **Dao et al. (2022)** -- *FlashAttention.* Referenced as enabling efficient long-context training, forming part of the infrastructure that makes 100K+ LLMs feasible.
- **Dao (2023)** -- *FlashAttention-2.* The improved version enabling faster attention computation for the long-context models evaluated on ∞Bench.
