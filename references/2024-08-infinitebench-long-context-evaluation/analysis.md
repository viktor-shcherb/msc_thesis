# ∞Bench: Extending Long Context Evaluation Beyond 100K Tokens

**Authors:** Xinrong Zhang, Yingfa Chen, Shengding Hu, Zihang Xu, Junhao Chen, Moo Khai Hao, Xu Han, Zhen Leng Thai, Shuo Wang, Zhiyuan Liu, Maosong Sun (Tsinghua University)
**Date:** August 2024, ACL 2024 Long Papers (arXiv:2402.13718)

---

## Core Research Problem

Despite rapid advances in LLM context windows -- with models like GPT-4 (128K), Claude 2 (200K), and Kimi-Chat (200K) claiming to process over 100K tokens -- existing long-context benchmarks lag far behind. LongBench (Bai et al., 2023) and LRA (Tay et al., 2020) average only ~10K tokens; L-Eval (An et al., 2023) reaches 60K at most. No public benchmark at the time of writing had an average data length surpassing 100K tokens.

This gap creates two problems. First, it is impossible to comparatively evaluate models that claim 100K+ context support when benchmarks test only at 10K. Second, existing benchmarks are dominated by retrieval-style tasks or tasks where parametric knowledge can compensate for failure to process the full context. Simply retrieving a limited number of passages is often sufficient to answer questions, making the benchmarks unable to isolate genuine long-context reasoning from short-context retrieval ability.

**The core challenge is how to construct a standardized, multi-domain, bilingual benchmark with average data length exceeding 100K tokens, featuring tasks that require genuine understanding of long-range dependencies rather than simple passage retrieval.**

---

## Problem Solutions

∞Bench is the first LLM benchmark with an average data length surpassing 100K tokens (~200K average). It spans 5 domains (retrieval, code, math, novels, dialogue) in both English and Chinese, with 12 tasks totaling 3,946 examples.

1. **Multi-domain realistic and synthetic tasks.** The benchmark combines human-annotated tasks from realistic contexts (novels, code repositories, movie scripts) with auto-generated synthetic tasks (passkey retrieval, number retrieval, key-value lookup, code execution, arithmetic).
2. **Tasks requiring long-range dependencies.** Novel-based tasks use aggregation (compiling information scattered throughout the text) and filtering (identifying specific information from a large set), both of which require processing the full context. Synthetic tasks test retrieval at elevated resolution, state preservation, and sequential processing.
3. **Data contamination countermeasures.** Novel-based tasks employ key entity replacement -- substituting prominent character names with unrelated ones to create "fake novels" -- preventing LLMs from relying on training data memorization.

---

## Approach Details

### Method

∞Bench constructs tasks in two broad categories:

**Realistic context tasks** use real-world data:
- **Novel-based tasks (En.Sum, En.QA, En.MC, Zh.QA):** Entire novels are presented at inference time, with key entities replaced. Annotators create questions requiring aggregation or filtering reasoning across the full novel.
- **Dialogue (En.Dia):** Movie/drama scripts with random character name instances replaced by `$$MASK$$`; the model must identify the masked character. Scripts shorter than 100K tokens are padded with additional scripts.
- **Code debugging (Code.Debug):** Real Python packages from PyPI (64K--256K tokens) with a deliberate bug injected into one function. Four-choice format due to extreme difficulty of the open-ended version.

**Synthetic context tasks** test specific capabilities:
- **Retrieve.PassKey:** Find a random 5-digit passkey hidden in noisy text (from Mohtashami and Jaggi, 2023). 590 examples with 59 positions.
- **Retrieve.Number:** Enhanced passkey with 10-digit answers containing successive repetitive digits (e.g., 9998877762), testing local attention resolution.
- **Retrieve.KV:** Identify and retrieve a value from a large JSON object of key-value pairs (from Liu et al., 2023). Relevant and irrelevant information share the same format.
- **Code.Run:** Simulate multi-step Python function executions (addition/subtraction with nested calls at depths 2--10), testing state tracking.
- **Math.Find:** Locate specific elements (3 largest, 3 smallest, median) in a large number array, testing state preservation.
- **Math.Calc:** Compute intermediate results of a long arithmetic expression, testing sequential processing.

### Key Technical Components

**Annotation pipelines.** Five distinct pipelines are used for human-annotated tasks (Figure 3 in paper). Each annotation is quality-checked by at least two other annotators. For novel tasks, a shared pipeline covers entity replacement, question annotation, and answer/option annotation.

**Key entity replacement.** Prominent entities (main character names) are replaced with unrelated names to prevent LLMs from leveraging training data knowledge of well-known novels.

**Evaluation metrics.** Exact match for most tasks; ROUGE-L-Sum for En.Sum. For multiple-choice tasks, failure to output a valid option receives a score of 0.

**Input truncation.** For models with maximum input limits, inputs are truncated by removing the center and joining both ends, based on the assumption that key information (instructions, book titles) is typically at the start or end.

### Experimental Setup

**Models evaluated (4 baselines):**
- **GPT-4** (gpt-4-0125-preview): 128K context, evaluated via API (~$5000 total cost)
- **Claude 2:** 200K context, evaluated manually via web interface
- **Kimi-Chat:** 200K context, evaluated manually via web interface
- **YaRN-Mistral-7B-128K:** Open-source, Mistral-7B adapted to 128K via modified position encoding (Peng et al., 2023b). Inference on 1x A100 80GB GPU, ~10 min/example

An additional experiment with **RWKV-4-World-7B** is reported in Appendix A, but it produces unintelligible output at these lengths (0% on Retrieve.PassKey) due to being trained only on 4K sequences.

**Prompt design.** Model-specific prompt templates optimized on short dummy examples. YaRN-Mistral prompts include answer prefixes to constrain generation.

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

- **GPT-4 leads overall** with 45.63% average, excelling in retrieval (100% on PassKey and Number), code, and math domains.
- **No clear winner on novel tasks.** Kimi-Chat leads on En.Sum and En.MC; GPT-4 leads on En.QA and Zh.QA; Claude 2 dominates En.Dia (46.50% vs. GPT-4's 8.50%).
- **YaRN-Mistral substantially underperforms** proprietary models (19.96% average), showing near-random performance on multiple tasks and 0% on Retrieve.KV.
- **Math.Calc is unsolvable** for all models (best: GPT-4 at 0.01%), indicating that sequential processing over very long arithmetic expressions remains far beyond current capabilities.
- **All models struggle on realistic tasks.** Even GPT-4 achieves only 22.22% on En.QA and 14.73 ROUGE-L-Sum on En.Sum.

### Length Ablation

Performance on auto-generated tasks is measured at shortened context lengths (Figure 4):

- **Retrieve.KV:** GPT-4 maintains ~90% up to ~1000 KV pairs, then drops. Kimi-Chat degrades more gradually. YaRN-Mistral scores 0 at all lengths.
- **Math.Find:** All models degrade with increasing array size. GPT-4 drops from ~60% to ~40%.
- **Code.Run:** GPT-4 drops from ~75% at depth 2 to ~20% at depth 10. Other models near 0 at all depths.
- **En.Dia:** Claude 2 (not shown but reported) maintains relatively stable performance; GPT-4 drops from ~60% to ~8% as script length increases.

**Performance generally declines with longer input lengths**, confirming that models' effectiveness diminishes even though they can technically accept extended inputs.

### Lost-in-the-Middle Analysis

Unlike Liu et al. (2023), ∞Bench finds **no consistent trend between performance and answer position** across models (Figure 5):

- GPT-4 favors early answers on Retrieve.KV but later answers on En.Dia.
- Claude 2 is relatively unaffected by answer position across all three tested tasks.
- YaRN-Mistral and Kimi-Chat tend to perform better with end-positioned answers.

The authors hypothesize that the "lost in the middle" phenomenon is task- and model-specific, and that their 100K+ context setting (8x longer than Liu et al.'s 16K) may produce different position-dependent behaviors.

### Context Recalling

A prompting technique termed **context recalling** is identified: explicitly instructing the model to first repeat/recall relevant information before reasoning improves performance. On Code.Debug with GPT-4:

- Step-by-step prompting: **15.74%**
- Context recalling (repeat relevant code first): **39.59%**

This 2.5x improvement suggests that for long-context tasks, prompting models to relocate relevant information into their generation buffer before reasoning is more effective than direct reasoning over the full context.

### Limitations

1. **Small set of baselines.** Only 4 models are benchmarked, compared to 34+ in later benchmarks like BABILong.
2. **Manual evaluation for two models.** Claude 2 and Kimi-Chat are evaluated by manually entering examples through web interfaces, limiting scalability and reproducibility.
3. **Exact match scoring sensitivity.** Performance depends on prompt templates and answer parsing, requiring tailored prompt engineering for each model.
4. **100K ceiling may be insufficient.** For applications requiring analysis of multiple books or entire databases, 100K--200K tokens may not be enough. Later benchmarks like BABILong (Kuratov et al., 2024) extend to 10M+ tokens.
5. **No controllable length scaling.** Unlike BABILong, ∞Bench does not offer predefined length splits for systematic analysis of performance degradation curves on realistic tasks.

---

## Conclusions

1. **First 100K+ benchmark.** ∞Bench is the first LLM benchmark with average data length surpassing 100K tokens, spanning 5 domains (retrieval, code, math, novels, dialogue) in English and Chinese with 12 tasks and 3,946 examples.

2. **Significant performance degradation at scale.** All evaluated models show substantial performance drops at 100K+ contexts compared to shorter contexts, demonstrating that claimed context window sizes do not translate to effective utilization.

3. **Retrieval is easier than reasoning.** Models excel at retrieval tasks (GPT-4 achieves 100% on PassKey/Number) but struggle with tasks requiring genuine long-range reasoning (22% on En.QA, 0.01% on Math.Calc).

4. **No consistent lost-in-the-middle effect at 100K+.** Unlike prior findings at 16K contexts (Liu et al., 2023), answer position effects are model- and task-specific at ∞Bench's much longer contexts.

5. **Context recalling improves long-context performance.** Prompting models to explicitly recall relevant information before reasoning yields 2.5x improvement on Code.Debug (15.74% to 39.59% for GPT-4), suggesting that generation-time information relocation is more effective than direct long-range attention.

6. **Open-source models lag substantially.** YaRN-Mistral-7B-128K achieves only 19.96% average versus GPT-4's 45.63%, indicating that context extension methods applied to smaller open-source models do not match proprietary long-context models on challenging tasks.

---

## Core References and Why They Are Referenced

### Long-Context Evaluation Benchmarks

- **Bai et al. (2023)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* The closest prior benchmark, averaging ~10K tokens across 21 tasks. ∞Bench explicitly addresses LongBench's limited context length and lack of 100K+ evaluation.
- **An et al. (2023)** -- *L-Eval: Instituting Standardized Evaluation for Long Context Language Models.* Another prior benchmark reaching up to 60K tokens. ∞Bench surpasses L-Eval's length ceiling by 3x and adds bilingual coverage.
- **Tay et al. (2020)** -- *Long Range Arena: A Benchmark for Efficient Transformers.* An older benchmark (~10K tokens) spanning text, image, and math. ∞Bench differs by targeting LLMs rather than efficient transformer architectures and using much longer contexts.
- **Li et al. (2023)** -- *LooGLE: Can Long-Context Language Models Understand Long Contexts?* Averages ~20K tokens with summary and QA tasks. ∞Bench provides 10x longer contexts and broader domain coverage.

### Models and Context Extension Methods

- **OpenAI (2023)** -- *GPT-4 Technical Report / GPT-4 Turbo.* The strongest baseline on ∞Bench (45.63% average), supporting 128K contexts. GPT-4 achieves perfect scores on passkey and number retrieval but struggles on realistic tasks.
- **Anthropic (2023)** -- *Claude 2.* Claims 200K context support. Achieves the best performance on En.Dia (46.50%) but lags behind GPT-4 on most other tasks.
- **AI (2023)** -- *Kimi-Chat.* Proprietary 200K-context model by Moonshot AI. Leads on En.Sum (17.93) and En.MC (72.49) but underperforms GPT-4 overall.
- **Peng et al. (2023b)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Provides the YaRN-Mistral-7B-128K baseline, which substantially underperforms proprietary models (19.96% average), demonstrating that positional encoding modifications alone do not confer robust 100K+ context processing.
- **Peng et al. (2023a)** -- *RWKV: Reinventing RNNs for the Transformer Era.* RWKV-4-World-7B is tested but produces unintelligible output at ∞Bench lengths due to being trained only on 4K sequences.

### Attention and Positional Encoding

- **Su et al. (2023)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE is the positional encoding modified by context extension methods like YaRN that are evaluated on ∞Bench.
- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* Positional interpolation is referenced as a key method for extending LLM context windows, forming the technical background against which ∞Bench evaluates models.

### Task Foundations

- **Mohtashami & Jaggi (2023)** -- *Landmark Attention: Random-Access Infinite Context Length for Transformers.* Source of the Retrieve.PassKey task adapted in ∞Bench with 59 positions and 590 examples.
- **Liu et al. (2023)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Source of the Retrieve.KV task and the "lost in the middle" hypothesis. ∞Bench's analysis at 100K+ contexts contradicts the consistent position-dependent performance drop observed at 16K.
- **Bubeck et al. (2023)** -- *Sparks of Artificial General Intelligence: Early Experiments with GPT-4.* Demonstrates GPT-4's state tracking capability, motivating the Code.Run task design in ∞Bench.

### Infrastructure

- **Dao et al. (2022)** -- *FlashAttention.* Referenced as enabling efficient long-context training and inference, forming part of the infrastructure that makes 100K+ LLMs feasible.
- **Dao (2023)** -- *FlashAttention-2.* The improved version enabling the training infrastructure for the long-context models evaluated on ∞Bench.

#### Cross-References in Available Papers

- **BABILong (2024-12-babilong-long-context-reasoning):** BABILong references ∞Bench (as "InfinityBench") alongside LongBench and ZeroSCROLLS as realistic benchmarks lacking controllable sequence length that confound long-context utilization with parametric knowledge. BABILong extends evaluation to 10M tokens and 50M tokens for fine-tuned models, far beyond ∞Bench's ~200K average.
- **LongBench v2 (2025-07-longbench-v2):** References ∞Bench as focusing on shallow understanding with extractive questions; contrasts it with LongBench v2's human-verified difficulty calibration and more reliable multiple-choice evaluation format versus ROUGE/F1.
- **Effective Context Length Falls Short (2025-04-effective-context-length-falls-short):** Evaluates models on ∞Bench at 128K and reports that STRING method improves Llama3.1 70B and Qwen2 72B by over 10 points, with Llama3.1 70B + STRING surpassing GPT-4-128K (56.88 vs. 55.69).
- **LongBench Pro (2026-01-longbench-pro):** References ∞Bench as a mixed synthetic/natural benchmark, contrasting it with LongBench Pro's fully natural text approach.
- **YaRN (2024-05-yarn-context-extension):** YaRN-Mistral-7B-128K is evaluated as the sole open-source baseline on ∞Bench and substantially underperforms proprietary models, consistent with RULER and BABILong findings that context extension via positional encoding modification does not guarantee effective long-context utilization.
- **Lost in the Middle (2024-02-lost-in-the-middle):** ∞Bench's Retrieve.KV task originates from Liu et al. (2023), and ∞Bench's analysis at 100K+ contradicts the consistent lost-in-the-middle effect observed at 16K, suggesting the phenomenon is task- and model-specific.
- **LongBench (2024-08-longbench-bilingual-benchmark):** ∞Bench directly positions itself as addressing LongBench's ~10K token limitation, extending evaluation to 100K+ tokens while adding math and novel domains not covered by LongBench.
