---
title: "LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs"
authors: "Wu, Hee, Hu, Lee"
year: 2025
venue: "ICLR 2025"
paper_type: conference-paper
categories: ["benchmarking", "long-context-evaluation"]
scope: ["long-form text generation", "instruction following over extended outputs", "16K and 32K token generation", "synthetic benchmark"]
benchmarks_used: ["ruler", "niah", "longbench", "longgenbench"]
models_introduced: []
models_evaluated: ["gpt-4o-mini", "gpt-4o", "llama-3.1-8b", "llama-3.1-70b", "qwen2-7b", "qwen2-72b", "mistral-7b", "mixtral-8x7b", "film-7b", "longwriter-llama3.1-8b", "mamba-2.8b", "phi-3-mini-3.8b", "phi-3.5-moe"]
key_claims:
  - id: C1
    claim: "All tested LLMs show significant performance degradation on long-form generation compared to retrieval-focused benchmarks like RULER"
    evidence: "Table 3, Figure 3b, Section 3.2"
    status: supported
    scope: "10 open-source and 2 closed-source models, 16K and 32K output lengths"
    magnitude: "Best wAvg is 32.4% (GPT-4o-mini at 16K); most models below 20%"
  - id: C2
    claim: "Model performance degrades progressively as output length increases, with a pronounced drop after 4,000 tokens"
    evidence: "Figure 2, Section 3.3"
    status: supported
    scope: "8 open-source models evaluated, 16K and 32K settings, greedy decoding"
    magnitude: "Instruction adherence diminishes significantly beyond 4K tokens, with further deterioration approaching 16K tokens"
  - id: C3
    claim: "Instruction adherence follows a difficulty hierarchy: single > range > periodic instructions"
    evidence: "Figure 3a, Section 3.4"
    status: supported
    scope: "8 open-source models at 16K output length"
  - id: C4
    claim: "Long-input retrieval ability and long-output generation ability are correlated but distinct capabilities"
    evidence: "Figure 3b, Section 3.5"
    status: supported
    scope: "5 open-source models compared on RULER vs LongGenBench at matched lengths"
    magnitude: "Pearson r = 0.51 at 16K, r = 0.66 at 32K"
  - id: C5
    claim: "GPT-4o-mini achieves the best overall performance at 16K with a weighted average score of 32.4%"
    evidence: "Table 3, Section 3.2"
    status: supported
    scope: "16K output length only; GPT-4o and GPT-4o-mini not tested at 32K due to output limitations"
  - id: C6
    claim: "Approximately 45% of long outputs exhibit significant content repetition despite varied time or location prompts"
    evidence: "Section 4 (Analysis and Limitations)"
    status: unvalidated
    scope: "Qualitative observation; no formal repetition metric defined"
cross_references:
  - target: 2023-10-mistral-7b
    type: evaluates
    detail: "Evaluates Mistral 7B v0.2 on long-form generation, finding strong CR (81.8% at 16K) but low STIC-2 (20.4%)"
  - target: 2021-05-long-range-arena
    type: complementary
    detail: "Both are benchmarking papers for long-sequence capabilities; LRA evaluates architectural efficiency on synthetic tasks, while LongGenBench evaluates generation quality"
open_questions:
  - question: "Can architectural modifications (e.g., improved attention mechanisms) or training data improvements better address long-form generation degradation?"
    addressed_by: null
  - question: "How should creativity and logical reasoning be evaluated in long-form generation beyond instruction following?"
    addressed_by: null
  - question: "Would instruction-tuning on longer output examples substantially improve long-form generation quality?"
    addressed_by: null
---

# LongGenBench: Benchmarking Long-Form Generation in Long Context LLMs

**Authors:** Yuhao Wu, Ming Shan Hee, Zhiqing Hu, Roy Ka-Wei Lee (Singapore University of Technology and Design)
**Date:** April 2025, ICLR 2025; arXiv:2409.02076

---

## Core Research Problem

Existing long-context benchmarks — including Needle-in-a-Haystack (NIAH), RULER, NeedleBench, and LongBench — focus exclusively on a model's ability to **retrieve and comprehend** information from long input sequences. They do not evaluate a complementary and practically important capability: generating coherent, instruction-following long-form text **outputs**.

Real-world applications such as design proposals, technical documentation, and creative writing require models to produce detailed, structured text spanning tens of thousands of tokens. Prior generation benchmarks like ELI5 (Fan et al., 2019b) and LongWrite (Bai et al., 2024) are limited to shorter outputs (~0.2K and ~2.7K tokens respectively) and lack robust evaluation of whether the generated text adheres to specific constraints throughout its full length. Manual evaluation is costly and unscalable, while LLM-as-a-judge methods (Zheng et al., 2024) suffer from biases (e.g., presentation order sensitivity, verbosity preference) and poor interpretability.

**The core challenge is: how to systematically evaluate whether LLMs can generate long-form text (16K–32K tokens) that faithfully follows complex, distributed instructions throughout the entire output.**

---

## Problem Solutions

LongGenBench introduces a synthetic benchmark that decomposes long-form generation evaluation into verifiable **instruction-following** subtasks. The key idea is to embed specific, checkable constraints at designated positions throughout a long generation task, then programmatically verify whether the model's output satisfies each constraint.

The solution is built on three components:

1. **Strictly Sequential Tasks** — tasks where a model must generate content for each unit in a sequence (e.g., each week of the year, each floor of a building), ensuring the output can be split into identifiable subtasks.
2. **Three instruction types** — Single Instruction (SI), Range Instruction (RI), and Periodic Instruction (PI) — that inject constraints at specific points, ranges, or periodic intervals in the generated text.
3. **Automated binary verification** — each constraint is verified by checking whether the corresponding subtask output contains the required content, using a Llama 3.3-70B evaluator framed as a binary classification task.

---

## Approach Details

### Method

LongGenBench defines a main task `T = {T_1, T_2, ..., T_n}` as a **Strictly Sequential Task**, where each `T_i` is a subtask responsible for generating a specific unit of text (e.g., one floor of a skyscraper, one week of a diary). Specific Task Instructions (STIs) are then injected into the prompt via three instruction types:

> **Single Instruction (SI):** `T_S = {T_{s_1}, T_{s_2}, ...}` — injects specific information at a unique point in the generated text. Example: "Floor 34 must host an aerial gym."

> **Range Instruction (RI):** `T_R = {T_{R_i}, T_{R_{i+1}}, ..., T_{R_{i+j}}}` — requires information within a contiguous range. Example: "Floors 1–9 house a comprehensive shopping mall."

> **Periodic Instruction (PI):** `T_P = {T_{P_n}, T_{P_{2n}}, ..., T_{P_{m \cdot n}}}` — distributes requirements at predefined intervals. Example: "Starting from Floor 20, every 10th floor has a small aerial garden."

The combined check set is `Check_set = {T_S, T_R, T_P}`. Each main task instruction splices 5 single instructions, 1 range instruction, and 1 periodic instruction, drawn from libraries of over 20 templates per instruction type.

### Key Technical Components

**Four Scenario Setups.** Tasks are organized into two categories with four scenarios:

| Category | Scenario | Short Task | Long Task |
|---|---|---|---|
| Temporal | Diary | Weekly Diary (52 weeks) | Daily Diary (365 days) |
| Temporal | Menu | Weekly Menu (52 weeks) | Daily Menu (365 days) |
| Spatial | Skyscraper Design | 100-floor Design | 300-floor Design |
| Spatial | Urban Planning | 10×10 block Design | 19×19 block Design |

Each scenario generates 800 examples per model at both 16K and 32K token target lengths.

**Three Evaluation Metrics.**

1. **Completion Rate (CR):** Fraction of designated subtasks successfully completed.

> `CR = (Number of Completed Subtasks / Total Number of Subtasks) × 100%`

2. **Specific Task Instruction Completion-1 (STIC-1):** Measures instruction adherence across the subtasks that were actually produced (denominator = outputs to STIs).

> `STIC-1 = (SI + RI + PI completions) / (Total Number of Outputs to STIs)`

3. **Specific Task Instruction Completion-2 (STIC-2):** Measures instruction adherence across all expected STIs (denominator = total STIs including those for missing subtasks).

> `STIC-2 = (SI + RI + PI completions) / (Total Number of STIs)`

STIC-1 captures correctness of what was generated; STIC-2 captures completeness overall. The **weighted average (wAvg) = CR × STIC-2** serves as the final composite score.

**Evaluation Pipeline.** Generated outputs are split into subtask answers `A = {A_1, A_2, ..., A_m}`. Each subtask is matched against the corresponding check set entry and evaluated via Llama 3.3-70B as a binary classification ("Does this content include X?"). Manual validation on 300 data points confirmed 100% agreement with the model evaluator.

### Experimental Setup

**Models.** Ten long-context LLMs were evaluated in the primary experiments (eight open-source, two closed-source), ranging from 7B to 72B parameters:

| Model | Size | Context Length | Type |
|---|---|---|---|
| GPT-4o-mini | — | 128K | Closed |
| GPT-4o | — | 128K | Closed |
| Llama 3.1-8B-Instruct | 8B | 128K | Open |
| Llama 3.1-70B-Instruct | 70B | 128K | Open |
| Qwen2-7B-Instruct | 7B | 128K | Open |
| Qwen2-72B-Instruct | 72B | 128K | Open |
| Mistral-7B-Instruct-v0.2 | 7B | 32K | Open |
| Mixtral-8x7B-Instruct | 8×7B | 32K | Open (MoE) |
| FILM-7B | 7B | 128K | Open |
| LongWriter-llama3.1-8B | 8B | 128K | Open |

Extended experiments also include Mamba-2.8B (2K context), Phi-3-mini-3.8B (128K), and Phi-3.5-MoE-8x7B (128K).

**Inference.** vLLM (Kwon et al., 2023) with BFloat16 precision on 8× NVIDIA A800 GPUs, greedy decoding.

**Reproducibility.** Code and data are open-sourced at https://github.com/mozhu621/LongGenBench. Greedy decoding ensures deterministic outputs. All task templates and evaluation prompts are provided.

### Key Results

**Main results at 16K and 32K output lengths (Table 3):**

| Model | Context | CR (16K) | STIC-2 (16K) | wAvg (16K) | CR (32K) | STIC-2 (32K) | wAvg (32K) |
|---|---|---|---|---|---|---|---|
| GPT-4o-mini | 128K | **97.0%** | **33.4%** | **32.4%** | — | — | — |
| Qwen2-72B | 128K | 94.3% | 27.1% | 25.5% | 66.2% | 21.7% | 14.4% |
| LLaMA3.1-70B | 128K | 79.3% | 29.2% | 23.1% | 63.1% | **26.3%** | **16.6%** |
| Mixtral-8x7B | 32K | 83.0% | 27.2% | 22.6% | 60.5% | 20.3% | 12.3% |
| LLaMA3.1-8B | 128K | 93.5% | 22.0% | 20.6% | **77.6%** | 20.6% | 16.0% |
| Mistral-v0.2-7B | 32K | 81.8% | 20.4% | 16.7% | 48.2% | 15.7% | 7.6% |
| GPT-4o | 128K | 67.2% | 24.4% | 15.3% | — | — | — |
| Qwen2-7B | 128K | 60.0% | 13.5% | 8.1% | 40.0% | 12.6% | 5.0% |
| LongWriter-llama3.1-8B | 128K | 46.0% | 14.2% | 6.5% | 34.5% | 10.8% | 3.7% |
| FILM-7B | 32K | 36.0% | 9.0% | 3.2% | 37.4% | 10.9% | 4.1% |

Note: GPT-4o and GPT-4o-mini were not tested at 32K due to output length limitations.

Key takeaways:

- **Even the best model (GPT-4o-mini) achieves only 32.4% wAvg at 16K**, indicating that long-form generation with instruction adherence remains very challenging.
- **Performance drops substantially from 16K to 32K** across all models. For example, Qwen2-72B drops from 25.5% to 14.4% wAvg.
- **LLaMA3.1-8B achieves the highest CR at 32K (77.6%)**, demonstrating strong task completion but only moderate instruction following (STIC-2 = 20.6%).
- **High CR does not guarantee high STIC scores.** Qwen2-72B has 94.3% CR at 16K but only 27.1% STIC-2, showing that models can complete subtasks without following specific instructions.

### Accuracy Trend with Sequence Length

Performance degrades progressively with output length (Figure 2). Instruction adherence drops notably after 4,000 tokens, with further deterioration as outputs approach 16,000 tokens. At 32K, all models show even steeper decline. This aligns with trends observed in NIAH for retrieval and highlights the challenge of maintaining coherence over long generations.

### Three Instruction Types

Performance follows a consistent hierarchy across models (Figure 3a): **single > range > periodic**. Periodic instructions are the hardest, requiring temporal/spatial awareness and consistency over long sequences (e.g., "every four weeks starting from week 10"). The increased difficulty of periodic tasks suggests models struggle with maintaining recurring patterns over extended text.

### Comparison with Long-Input Retrieval (RULER)

Comparing RULER scores (long-input retrieval) with LongGenBench scores (long-output generation) at the same sequence lengths reveals a **significant performance gap** (Figure 3b). Models that excel at retrieving information from long inputs may still struggle with long-form generation. The Pearson correlation is moderate: r = 0.51 at 16K and r = 0.66 at 32K, suggesting related but distinct capabilities.

---

## Limitations and Failure Modes

**Explicitly acknowledged by the authors:**

- **Content repetition.** Approximately 45% of long outputs exhibited significant repetition even when varied time/location prompts should have introduced diversity. Adjusting `repetition_penalty` during inference had limited effect (Section 4).
- **Content rationality.** The benchmark evaluates instruction following but not logical consistency. For example, diary entries for San Francisco showed warm temperatures even in January, and activities did not align with stated professions (Section 4).
- **Instruction data limitations.** Most instruction-tuning datasets contain outputs under 200 tokens, lacking the extended instructional content needed for long-form generation training (Section 4).
- **Generalizability.** The benchmark focuses on instruction-driven tasks and does not evaluate creativity, abstract reasoning, or unconstrained storytelling (Section 4).

**Observed failure modes:**

- **Premature termination.** Some models (especially GPT-4o) halt after completing only a few subtasks, recognizing the task requires long output but refusing to generate it.
- **Instruction forgetting.** Models correctly followed instructions for initial subtasks but progressively deviated. In Skyscraper Design, correct floor descriptions appeared early but instructions for later floors (range and periodic) were ignored (Appendix F).
- **Partial completion.** Some models responded only to specific subtasks, skipping intermediate ones entirely.

### Scope and Comparability

- **Output length only.** The benchmark tests generation at 16K and 32K tokens. Models with output limitations (GPT-4o, GPT-4o-mini) could not be evaluated at 32K, limiting cross-model comparison at longer lengths.
- **Greedy decoding only.** All experiments use greedy decoding. Sampling-based decoding strategies might produce different results.
- **Four scenario types only.** Diary Writing, Menu Design, Skyscraper Design, and Urban Planning cover temporal and spatial domains but may not represent all long-form generation use cases (e.g., technical writing, legal documents).
- **Evaluator model.** Binary verification uses Llama 3.3-70B. While manual validation confirmed 100% agreement on 300 samples, this coverage is limited relative to the full dataset.

---

## Conclusions

### Contributions

1. **First systematic benchmark for long-form generation evaluation.** LongGenBench is the first benchmark that evaluates long-context LLMs on their ability to generate instruction-compliant text at 16K and 32K token lengths, complementing existing retrieval-focused benchmarks.
2. **Three-metric evaluation framework.** The CR, STIC-1, and STIC-2 metrics decompose generation quality into task completion and instruction adherence components, enabling fine-grained diagnosis of model limitations.
3. **Evidence that generation and retrieval are distinct capabilities.** Moderate correlation between RULER and LongGenBench scores (r = 0.51–0.66) demonstrates that strong long-input performance does not guarantee strong long-output performance.
4. **Systematic evaluation of 10+ models.** Comprehensive experiments across open-source and closed-source models of varying sizes reveal universal struggles with long-form generation.

### Implications

1. **Training data gap.** The finding that most instruction-tuning data contains outputs under 200 tokens (Section 4) suggests that curating longer instructional examples may be necessary to improve long-form generation — though this remains to be empirically validated.
2. **Architectural limitations.** The progressive performance degradation beyond 4K tokens (speculative) may relate to limitations in self-attention for maintaining context over very long generations, though the paper does not test this directly.
3. **Benchmark complementarity.** Long-context model evaluation should include both input-retrieval and output-generation benchmarks to capture the full spectrum of capabilities.

---

## Key Claims

1. **All tested LLMs struggle with long-form generation.** Despite strong performance on retrieval benchmarks like RULER, all models achieved low wAvg scores on LongGenBench, with the best (GPT-4o-mini) reaching only 32.4% at 16K (Table 3, Section 3.2). Status: **supported** — evidence from 13 models across 4 scenarios at 2 lengths.

2. **Performance degrades progressively beyond 4,000 output tokens.** Instruction adherence drops after the 4K-token mark and continues to deteriorate toward 16K tokens, with steeper decline at 32K (Figure 2, Section 3.3). Status: **supported** — observed across all 8 open-source models with smoothed accuracy curves.

3. **Instruction difficulty hierarchy: single > range > periodic.** Models follow single instructions most reliably, with periodic instructions being the hardest to sustain over long sequences (Figure 3a, Section 3.4). Status: **supported** — consistent pattern across all evaluated models.

4. **Long-input retrieval and long-output generation are correlated but distinct skills.** Pearson correlation between RULER and LongGenBench is r = 0.51 at 16K and r = 0.66 at 32K (Figure 3b, Section 3.5). Status: **supported** — however, based on only 5 models, limiting statistical power.

5. **GPT-4o-mini achieves the best overall wAvg at 16K (32.4%), followed by Qwen2-72B (25.5%) and LLaMA3.1-70B (23.1%).** At 32K, LLaMA3.1-70B leads with 16.6% wAvg (Table 3, Section 3.2). Status: **supported** — GPT-4o and GPT-4o-mini not evaluated at 32K.

6. **~45% of long outputs show significant content repetition** even when prompted with varied contexts (Section 4). Status: **unvalidated** — reported as an observation without a formal repetition metric or systematic measurement methodology.

---

## Open Questions

1. **Can instruction-tuning on longer output examples substantially improve long-form generation?** The paper attributes poor performance partly to instruction-tuning data being typically under 200 tokens. Whether curating or synthesizing longer examples would help remains untested. Not addressed by subsequent work in this directory.

2. **Are architectural changes necessary, or can training alone close the gap?** The progressive degradation beyond 4K tokens may reflect fundamental attention limitations or merely a training data distribution mismatch. Not addressed by subsequent work in this directory.

3. **How should long-form generation quality be evaluated beyond instruction following?** The paper acknowledges that creativity, logical reasoning, and narrative coherence are not captured by the current metrics. Not addressed by subsequent work in this directory.

4. **Does the RULER–LongGenBench correlation hold at larger model scales?** The moderate correlation (r = 0.51–0.66) was measured on only 5 models. Whether this relationship is robust at larger scales (>100B) is unknown. Not addressed by subsequent work in this directory.

---

## Core References and Why They Are Referenced

### Direct Predecessors and Comparisons

- **Kamradt (2023)** — *Needle In A Haystack.* Introduces the NIAH retrieval test for long-context LLMs; LongGenBench draws an analogy with "reversed NIAH" for generation.
- **Hsieh et al. (2024)** — *RULER: What's the Real Context Size of Your Long-Context Language Models?* Synthetic multi-task long-context retrieval benchmark; LongGenBench directly compares model performance on RULER vs. long-form generation.
- **Bai et al. (2023)** — *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* Hybrid retrieval benchmark that LongGenBench positions itself against as complementary.
- **Bai et al. (2024)** — *LongWriter: Unleashing 10,000+ Word Generation from Long Context LLMs.* Synthetic generation benchmark with ~2.7K average output length; LongGenBench substantially extends the target output length to 16K–32K tokens.
- **Fan et al. (2019b)** — *ELI5: Long Form Question Answering.* Earlier long-form QA benchmark limited to ~0.2K token outputs.

### Models Evaluated

- **OpenAI (2024a,b)** — *GPT-4o-mini and GPT-4o.* Closed-source baselines; GPT-4o-mini achieves the best wAvg at 16K.
- **Dubey et al. (2024)** — *The Llama 3 Herd of Models.* Llama 3.1-8B and 70B are evaluated; LLaMA3.1-8B shows the best CR at 32K (77.6%).
- **Yang et al. (2024)** — *Qwen2 Technical Report.* Qwen2-7B and 72B are evaluated; Qwen2-72B ranks second at 16K.
- **Jiang et al. (2023)** — *Mistral 7B.* Mistral-v0.2-7B achieves 81.8% CR at 16K but only 20.4% STIC-2.
- **Jiang et al. (2024)** — *Mixtral of Experts.* Mixtral-8x7B evaluated as MoE representative.

### Evaluation Methodology

- **Zheng et al. (2023, 2024)** — *MT-Bench and Chatbot Arena / LLM-as-a-Judge.* LLM evaluation methods that LongGenBench critiques for bias and interpretability issues in long-form contexts.
- **Kwon et al. (2023)** — *vLLM: Efficient Memory Management for Large Language Model Serving.* Inference framework used for all experiments.

### Long-Form Text Generation

- **Fan et al. (2018, 2019c)** — *Hierarchical Neural Story Generation / Strategies for Structuring Story Generation.* Prior work on story generation, limited to shorter outputs.
- **Hu et al. (2022)** — *PLANET: Dynamic Content Planning in Autoregressive Transformers.* Content planning for long-form generation.
- **Hua & Wang (2020)** — *PAIR: Planning and Iterative Refinement for Long Text Generation.* Planning-based generation approach.
