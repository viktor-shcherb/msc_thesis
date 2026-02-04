---
title: "Context Length Alone Hurts LLM Performance Despite Perfect Retrieval"
authors: "Du, Tian, Ronanki, Rongali, Bodapati, Galstyan, Wells, Schwartz, Huerta, Peng"
year: 2025
venue: "Findings of EMNLP 2025"
paper_type: conference-paper
categories: ["long-context-evaluation", "position-bias"]
scope: ["context length degradation independent of retrieval", "retrieval-reasoning decomposition"]
benchmarks_used: ["gsm8k", "mmlu", "humaneval", "ruler"]
models_introduced: []
models_evaluated: ["llama-3.1-8b", "mistral-7b", "gpt-4o", "claude-3.5-sonnet", "gemini-2.0"]
key_claims:
  - id: C1
    claim: "Even when models perfectly retrieve all evidence with 100% exact match, performance degrades 13.9%--85% as input length increases to 30K tokens"
    evidence: "Section 3.2, Figure 3, Table 6"
    status: supported
  - id: C2
    claim: "Performance degradation persists when irrelevant tokens are replaced with minimally distracting whitespace"
    evidence: "Section 4.1, Figure 4a, Tables 2, 7"
    status: supported
  - id: C3
    claim: "Performance degrades even when all distraction tokens are masked via attention, with drops of at least 7.9% at 30K tokens"
    evidence: "Section 4.2, Table 3"
    status: supported
  - id: C4
    claim: "Performance degrades when evidence is placed immediately before the question, ruling out evidence-question distance as the sole cause"
    evidence: "Section 4.1, Figure 4b, Table 8"
    status: supported
  - id: C5
    claim: "Closed-source models are more robust but not immune to context-length degradation"
    evidence: "Section 4.1, Table 2"
    status: supported
  - id: C6
    claim: "A simple retrieve-then-reason strategy improves performance by up to 31.2% on GSM8K and up to 4% on RULER QA2"
    evidence: "Section 5, Tables 4, 5"
    status: supported
cross_references:
  - target: 2024-02-lost-in-the-middle
    type: extends
    detail: "Builds on Lost in the Middle's positional bias findings; places evidence at the beginning (easiest position per Lost-in-the-Middle) and shows degradation still occurs from input length itself"
  - target: 2025-04-effective-context-length-falls-short
    type: complementary
    detail: "An et al. attribute performance drops to positional distribution bias during training; this paper shows that positional bias also causes degradation from context length alone, independent of retrieval"
  - target: 2025-07-position-bias-transformers
    type: complementary
    detail: "Both find longer context hurts performance; position bias paper provides theoretical framework while this paper provides controlled empirical measurement"
  - target: 2023-07-gsm-ic-irrelevant-context
    type: complementary
    detail: "GSM-IC shows irrelevant tokens distract models in reasoning; this paper shows even without irrelevant content (via masking), context length alone degrades performance"
  - target: 2024-10-ruler-context-size
    type: uses-benchmark
    detail: "Uses RULER QA1 and QA2 tasks to evaluate the retrieve-then-reason mitigation strategy with GPT-4o"
  - target: 2023-11-needle-in-a-haystack
    type: complementary
    detail: "Uses Paul Graham Essays from the NIAH work as distraction tokens; challenges the sufficiency of retrieval-focused evaluations like NIAH"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong reports a gap between retrieval and reasoning in long contexts; this paper disentangles causes by controlling for perfect retrieval"
  - target: 2024-03-gemini-1.5-long-context
    type: complementary
    detail: "Evaluates Gemini 2.0 (successor to 1.5) and finds it shows better robustness than open-source models but still exhibits context-length-induced degradation"
  - target: 2021-11-long-range-models-use-context
    type: complementary
    detail: "Sun et al. are an early empirical demonstration that long-range context does not help overall predictions; this paper extends the finding by showing context length alone degrades performance even with perfect retrieval"
  - target: 2024-11-genuinely-difficult-long-context
    type: complementary
    detail: "Goldman et al. argue that retrieval-like tasks (low scope, low dispersion) are insufficient for evaluating long-context capabilities; this paper empirically demonstrates that even when retrieval is perfect, context length itself degrades problem-solving performance"
  - target: 2024-08-flenqa-input-length-reasoning
    type: extends
    detail: "Extends FlenQA's finding that input length degrades reasoning; adds whitespace padding and attention masking controls to further isolate the length effect from content and distraction effects"
open_questions:
  - question: "What is the precise mechanism by which increased positional indices degrade reasoning capacity in transformers?"
    addressed_by: null
  - question: "Can training-time interventions eliminate the length-alone degradation, beyond the inference-time retrieve-then-reason strategy?"
    addressed_by: null
  - question: "Is there a model size threshold above which the length-alone degradation disappears, given that closed-source models (likely larger) showed less degradation?"
    addressed_by: null
---

# Context Length Alone Hurts LLM Performance Despite Perfect Retrieval

**Authors:** Yufeng Du*, Minyang Tian*, Srikanth Ronanki, Subendhu Rongali, Sravan Bodapati, Aram Galstyan, Azton Wells, Roy Schwartz, Eliu A. Huerta, Hao Peng (University of Illinois at Urbana-Champaign, Amazon, USC Information Sciences Institute, Argonne National Laboratory, Hebrew University of Jerusalem, University of Chicago)
**Date:** October 2025, Findings of EMNLP 2025, arXiv:2510.05381

---

## Core Research Problem

Large language models now claim context windows of 100K+ tokens (Llama-3, Claude 3) and even several million tokens (Gemini), yet expanded windows have not consistently translated into improved task performance over long inputs (Hengle et al., 2025; Lee et al., 2024; Kuratov et al., 2024). Recent work decomposes long-context task solving into two interleaved processes: (1) **retrieval** -- identifying relevant information in the input, and (2) **problem solving** -- using that information to answer the question (Wu et al., 2024c; Kuratov et al., 2024; Li et al., 2024a; Zhang et al., 2025b). This decomposition invites a natural assumption: if retrieval is perfect, the model should perform just as well on a long input as on a short one.

Failures on long-context tasks are therefore commonly attributed to suboptimal retrieval. Retrieval performance drops when more distractors are present (Ivgi et al., 2022; Goldman et al., 2024), when aggregation of multiple evidence pieces is required (Wang, 2025; Karpinska et al., 2024), when evidence has low lexical overlap (Modarressi et al., 2025b), or when evidence is in the middle of the context (Liu et al., 2024b). However, prior work entangles retrieval accuracy with task performance. Studies that compare retrieval and reasoning on different tasks cannot conclude that perfect retrieval on the actual problem-solving task eliminates the long-context penalty. Others that combine retrieval, aggregation, and reasoning over multiple needles leave multiple failure modes as potential explanations. **The core challenge is: does the sheer length of the input context itself hurt LLM problem-solving performance, independent of retrieval quality and distraction from irrelevant tokens?**

---

## Problem Solutions

The paper provides systematic empirical evidence that context length alone degrades LLM performance, and proposes a simple mitigation strategy:

1. **Performance degradation despite perfect retrieval.** Across 5 open- and closed-source models on math, QA, and coding tasks, performance degrades by 13.9%--85% as input length increases, even when models can recite all evidence with 100% exact match.
2. **Degradation persists without distraction.** The performance drop occurs even when irrelevant tokens are replaced with whitespace (minimal distraction), and even when all irrelevant tokens are masked via attention masking (zero distraction).
3. **Degradation is independent of evidence position.** A similar drop is observed when all evidence is placed immediately before the question, ruling out evidence-question distance as the sole cause.
4. **Retrieve-then-reason mitigation.** A simple, model-agnostic strategy that prompts the model to recite retrieved evidence, then solves the problem using only the recited evidence in a new short prompt.

---

## Approach Details

### Method

The paper constructs a controlled synthetic benchmark by converting short-context problems into long-context ones. Each problem has two components: **evidence** (all information needed to solve the task) and **question** (the query and format requirements). Distraction tokens are inserted between them to reach desired context lengths, creating inputs of the form: `[Evidence] [Distraction Tokens] [Question]`.

Two major design choices isolate the effect of context length from retrieval difficulty: (1) evidence is kept in a single consecutive chunk (no aggregation required), and (2) evidence is placed at the beginning of the input -- the easiest location to retrieve per the Lost-in-the-Middle effect (Liu et al., 2024b) -- with the question at the end.

Retrieval is measured separately from problem solving: the model is prompted to recite both the evidence and the question exactly as they appear in the input, scored by **exact match** (score of zero for any difference). This strictest possible retrieval measurement ensures that when a model achieves perfect retrieval, it has demonstrably accessed every token of the evidence. The retrieval evaluation is separate from the problem-solving evaluation; models are not asked to recite before solving.

### Key Technical Components

**Three distraction conditions**, ordered by decreasing strength:

1. **Essay tokens (Section 3):** Paul Graham Essays (following Kamradt, 2023) inserted between evidence and question. These carry rich semantic content and represent natural distractors.
2. **Whitespace tokens (Section 4.1):** All natural language distraction tokens replaced with whitespace, carrying minimal information and creating least distraction (Zhang et al., 2025c).
3. **Attention masking (Section 4.2):** All distraction tokens masked in the attention computation. The model attends *only* to evidence and question tokens -- identical to the short-context setting except for the increased positional distance.

**Evidence position control (Section 4.1):** A separate experiment moves evidence to the end of the input, immediately before the question (`[Whitespace] [Evidence] [Question]`), so that the evidence-question distance does not change with input size. This controls for the relative distance factor noted by Li et al. (2024a) and An et al. (2024).

**Retrieve-then-reason mitigation (Section 5):** Given a long-context input, the model first retrieves and recites all relevant evidence. The recited evidence is then concatenated with the original question to form a new, shorter prompt. The model solves the problem based solely on this short prompt (analogous to starting a new chat session), effectively converting the long-context task into a short-context one.

### Experimental Setup

**Models:**

| Model | Type | Claimed Context Length |
|---|---|---|
| Llama-3.1-8B-Instruct | Open-source, decoder-only | 128K |
| Mistral-v0.3-7B-Instruct | Open-source, decoder-only | 32K |
| GPT-4o | Closed-source | Not specified |
| Claude-3.5-Sonnet | Closed-source | Not specified |
| Gemini-2.0 | Closed-source | Not specified |

**Tasks:**

| Task | Type | Evidence | Question |
|---|---|---|---|
| Variable Summation (VarSum) | Variable tracking | Values of 50 integer variables | Sum of 3 random variables |
| GSM8K (Cobbe et al., 2021) | Math | Problem description with chain-of-thought steps | Specific question |
| MMLU (Hendrycks et al., 2021a) | Multiple choice QA | Problem description | Question and four options |
| HumanEval (Chen et al., 2021) | Coding | Function definition with docstring | Instruction |

**Context lengths tested:** 0 (baseline), 3750, 7500, 11250, 15000, 18750, 22500, 26250, 30000 tokens (varying by experiment). Closed-source models tested at 0, 7500, 15000, 30000 whitespace tokens.

**Mitigation evaluation:** (1) Synthetic benchmark with essay tokens on GSM8K using Mistral-v0.3-7B-Instruct. (2) QA1 and QA2 tasks of RULER (Hsieh et al., 2024) using GPT-4o, at context lengths from 4K to 128K tokens.

**Hardware:** GH200 GPUs, approximately 20,000 GPU hours total. All experiments run once (no variance estimates reported).

### Key Results

**Essay distraction (Section 3.2, Table 6) -- Llama-3.1-8B and Mistral-v0.3-7B:**

| Model | Task | Baseline (0 tokens) | Drop at 7500 | Drop at 15000 | Drop at 30000 |
|---|---|---|---|---|---|
| Llama3 | VarSum | 96.0% | -59.0 | -60.0 | -85.0 |
| Llama3 | GSM8K | 87.8% | -5.4 | -9.0 | -12.3 |
| Llama3 | MMLU | 63.2% | -21.4 | -20.0 | -24.2 |
| Llama3 | HumanEval | 57.3% | -20.1 | -40.9 | -47.6 |
| Mistral | VarSum | 68.0% | -44.0 | -47.0 | -66.0 |
| Mistral | GSM8K | 70.6% | -27.2 | -28.9 | -34.2 |
| Mistral | MMLU | 54.1% | -13.9 | -16.9 | -20.3 |
| Mistral | HumanEval | 34.8% | -17.7 | -23.8 | -34.8 |

- Retrieval scores remain high: for inputs shorter than 15K tokens, both models retrieve evidence with exact match for all but at most 8.2% of problems (Section 3.2).
- **Llama-3.1-8B retrieves all evidence for 970 of 1000 MMLU problems at 30K tokens, yet accuracy drops by 24.2%** (Section 3.2).
- A large portion of the problem-solving drop occurs within 7K tokens, well below the limits where retrieval degrades. On VarSum, Llama drops 59 percentage points at 7K while retrieval only drops 8 points; Mistral drops 44 points while retrieval drops only 2 points (Table 6).

**Whitespace distraction (Section 4.1, Table 7) -- open-source models:**

| Model | Task | Baseline | Drop at 7500 | Drop at 15000 | Drop at 30000 |
|---|---|---|---|---|---|
| Llama3 | VarSum | 96.0% | -8.0 | -12.0 | -48.0 |
| Llama3 | GSM8K | 87.5% | -4.7 | -3.2 | -7.0 |
| Llama3 | MMLU | 63.2% | -15.9 | -15.3 | -20.2 |
| Llama3 | HumanEval | 57.3% | -12.2 | -12.8 | -31.7 |
| Mistral | VarSum | 68.0% | -4.0 | -17.0 | -28.0 |
| Mistral | GSM8K | 70.0% | -12.0 | -24.0 | -30.0 |
| Mistral | MMLU | 54.1% | -9.2 | -12.7 | -14.0 |
| Mistral | HumanEval | 34.8% | -4.9 | -6.7 | -11.0 |

- Performance generally improves compared to essay distraction but substantial drops remain: at least 7% at 30K for all tasks, and up to 48% (Llama VarSum) and 30% (Mistral GSM8K).

**Whitespace distraction (Section 4.1, Table 2) -- closed-source models:**

| Model | Task | Baseline | Drop at 7500 | Drop at 15000 | Drop at 30000 |
|---|---|---|---|---|---|
| GPT-4o | VarSum | 100.0% | 0.0 | 0.0 | 0.0 |
| GPT-4o | GSM8K | 87.8% | -7.0 | -8.5 | -7.0 |
| GPT-4o | MMLU | 82.4% | -2.1 | -0.3 | -1.0 |
| GPT-4o | HumanEval | 68.3% | 0.0 | 0.0 | -3.1 |
| Claude-3.5 | VarSum | 90.2% | -0.6 | -5.4 | -4.8 |
| Claude-3.5 | GSM8K | 95.3% | -3.8 | -5.2 | -6.0 |
| Claude-3.5 | MMLU | 82.2% | -41.7 | -38.8 | -67.6 |
| Claude-3.5 | HumanEval | 90.2% | -0.6 | -5.4 | -4.8 |
| Gemini-2.0 | VarSum | 100.0% | 0.0 | 0.0 | 0.0 |
| Gemini-2.0 | GSM8K | 83.2% | +7.7 | +8.6 | +6.2 |
| Gemini-2.0 | MMLU | 81.9% | -3.0 | -3.5 | -3.9 |
| Gemini-2.0 | HumanEval | 86.0% | -11.0 | -2.5 | -1.8 |

- Closed-source models are more robust but still show substantial degradation in most model-task combinations. Notable exception: Gemini-2.0 *improves* on GSM8K at 30K whitespace (+6.2%).
- Claude-3.5-Sonnet shows a large MMLU drop (-67.6% at 30K) despite strong baselines on other tasks. The VarSum and HumanEval rows for Claude-3.5 report identical numbers in the paper (Table 2).

**Evidence before question (Section 4.1, Table 8) -- whitespace inserted before evidence:**

| Model | Task | Baseline | Drop at 7500 | Drop at 15000 | Drop at 30000 |
|---|---|---|---|---|---|
| Llama3 | VarSum | 97.0% | -8.0 | -6.0 | -20.0 |
| Llama3 | GSM8K | 85.5% | -6.6 | -8.1 | -7.1 |
| Llama3 | MMLU | 62.9% | -12.9 | -15.6 | -19.4 |
| Llama3 | HumanEval | 57.3% | -7.9 | -12.2 | -18.3 |
| Mistral | VarSum | 66.0% | -4.0 | -7.0 | -17.0 |
| Mistral | GSM8K | 64.2% | -7.9 | -9.3 | -7.9 |
| Mistral | MMLU | 54.0% | -7.2 | -7.2 | -10.1 |
| Mistral | HumanEval | 34.8% | -6.7 | -6.7 | -9.8 |

- Substantial drops persist despite constant evidence-question distance: up to 20% for Llama (VarSum) and 17% for Mistral (VarSum) at 30K whitespace tokens (Section 4.1).
- **Input length itself is a decisive factor**, independent of the relative position between evidence and question.

**Attention masking (Section 4.2, Table 3):**

| Model | Task | Baseline | Drop at 3750 | Drop at 7500 | Drop at 15000 | Drop at 30000 |
|---|---|---|---|---|---|---|
| Llama3 | VarSum | 97.0% | -11.0 | -35.0 | -24.0 | -50.0 |
| Llama3 | GSM8K | 86.1% | -1.7 | -3.3 | -4.3 | -19.6 |
| Llama3 | MMLU | 62.8% | -11.3 | -15.9 | -15.5 | -21.1 |
| Llama3 | HumanEval | 57.3% | -5.5 | -22.0 | -16.5 | -50.0 |
| Mistral | VarSum | 66.0% | -5.0 | -11.0 | -19.0 | -34.0 |
| Mistral | GSM8K | 64.5% | -2.1 | -4.8 | -8.2 | -15.1 |
| Mistral | MMLU | 53.8% | -4.7 | -7.5 | -11.0 | -11.8 |
| Mistral | HumanEval | 34.8% | -7.3 | -8.5 | -10.4 | -7.9 |

- Performance drops persist even when the model cannot attend to any distraction tokens. Some drops are *larger* than with whitespace (Llama3 HumanEval: -50.0% with masking vs. -31.7% with whitespace at 30K).
- The only difference from the short-context setting is the increased positional distance between evidence and question tokens.

**Retrieve-then-reason mitigation (Section 5, Table 4) -- Mistral on GSM8K with essay distractions:**

| Length (tokens) | 0 | 3750 | 7500 | 15000 | 26250 |
|---|---|---|---|---|---|
| Baseline | 70.6% | 49.3% | 43.4% | 41.6% | 35.5% |
| Retrieve-then-reason | 76.2% | 71.4% | 66.7% | 69.1% | 66.7% |

- Up to 31.2 percentage point improvement at 26250 tokens (66.7% vs. 35.5%).

**Retrieve-then-reason mitigation (Section 5, Table 5) -- GPT-4o on RULER:**

| Method | Task | 128K | 64K | 32K | 16K | 8K | 4K |
|---|---|---|---|---|---|---|---|
| Baseline | QA1 | 88.2 | 87.8 | 87.8 | 88.8 | 87.2 | 90.4 |
| Retrieve-then-reason | QA1 | 88.2 | 88.4 | 88.6 | 89.8 | 89.8 | 92.2 |
| Baseline | QA2 | 63.2 | 67.0 | 68.4 | 69.4 | 71.4 | 71.2 |
| Retrieve-then-reason | QA2 | 65.4 | 70.6 | 72.4 | 72.8 | 74.0 | 73.2 |

- Consistent improvement for GPT-4o across all context lengths: up to 4.0 percentage points on QA2 at 32K, and up to 1.8 points on QA1 at 4K.

### Relation to Positional Distribution Bias

The paper connects its findings to Li et al. (2024a) and An et al. (2024), which attribute long-context performance drops to a distribution bias with position introduced during training. While An et al. (2024) targets retrieval drops and Li et al. (2024a) addresses overall long-context performance, this paper shows that the positional distribution bias also causes degradation from context length itself, independent of retrieval or distraction strength (Section 6). The relatively steady performance of closed-source models is consistent with this explanation, as larger models and more extensive training may partially mitigate the bias.

---

## Limitations and Failure Modes

- **Limited model coverage.** Conclusions are based on two open-source models (7B--8B scale) and three closed-source models. The finding may not generalize to all architectures or scales.
- **Limited task coverage.** Only 4 tasks are used (VarSum, GSM8K, MMLU, HumanEval), all single-evidence tasks. Multi-evidence or long-form generation tasks are not evaluated.
- **No retrieval evaluation for closed-source models.** Closed-source models occasionally refused to recite evidence under long inputs, so retrieval scores are not reported for them (Limitations section).
- **All experiments run once.** No variance estimates are provided, making it difficult to assess the reliability of individual data points (Section A.4).
- **Retrieve-then-reason requires accurate retrieval.** The mitigation strategy assumes the model can accurately retrieve evidence, which is often not the case in real-world settings with harder retrieval scenarios (Limitations section).
- **Open-source models not tested on RULER.** Retrieval failures on RULER would directly cause performance drops unrelated to the paper's hypothesis, so these results are omitted.
- **Anomalous closed-source results.** Gemini-2.0 *improves* on GSM8K with longer context (+6.2% at 30K), and Claude-3.5 shows identical VarSum and HumanEval numbers in Table 2, suggesting possible data issues or task-specific effects not fully explored.
- **Mechanism not identified.** The paper establishes the phenomenon empirically but does not identify the internal mechanism causing degradation from positional distance alone.

---

## Conclusions

### Contributions

1. **Demonstrated that context length alone degrades problem-solving performance.** Even when models perfectly retrieve all evidence (100% exact match), accuracy drops by 13.9%--85% as context length increases to 30K tokens -- well within claimed context windows (Section 3.2, Table 6).

2. **Isolated context length from distraction and position effects.** Through a systematic series of controls -- essay tokens, whitespace, attention masking, and evidence position manipulation -- the paper establishes that input length is an independent factor in performance degradation, beyond retrieval quality, distraction, or evidence-question distance (Sections 3--4).

3. **Showed closed-source models are more robust but not immune.** GPT-4o, Claude-3.5-Sonnet, and Gemini-2.0 show smaller drops than open-source models on most tasks, but consistent degradation is still observed across model-task combinations (Table 2).

4. **Proposed a simple retrieve-then-reason mitigation.** A model-agnostic inference-time strategy that converts long-context tasks into short-context ones by prompting the model to recite evidence before solving, yielding up to 31.2% improvement on GSM8K and up to 4% on RULER QA2 (Tables 4, 5).

### Implications

1. **The retrieval-reasoning decomposition is incomplete.** The prevailing two-part decomposition of long-context problem solving into retrieval and problem solving is challenged: improving retrieval alone does not fully bridge the long-context performance gap. A third factor -- the effect of input length itself on reasoning capacity -- must be accounted for (Section 6).

2. **Retrieval-focused evaluations may overestimate progress.** Benchmarks that isolate retrieval as a standalone capability (e.g., needle-in-a-haystack, passkey retrieval) might overestimate long-context capabilities, as improvements in retrieval do not necessarily translate to better task performance (Section 6).

3. **Practical consequences for RAG and chain-of-thought.** The findings explain recurring observations that RAG performance saturates or degrades as more documents are added (Cuconasu et al., 2024; Jin et al., 2024; Yu et al., 2024) and that excessively long chain-of-thought reasoning can hurt performance (Zeng et al., 2025; Dai et al., 2025) -- in both cases, longer effective context may itself be a contributing cause (Section 6).

---

## Key Claims

1. **C1: Performance degrades 13.9%--85% despite perfect retrieval.** Across all tasks and both open-source models, accuracy drops substantially as input length increases from 0 to 30K tokens with essay distractions, even though retrieval exact match remains above 91.8% for inputs under 15K tokens. Evidence: Section 3.2, Figure 3, Table 6. Status: **supported**.

2. **C2: Whitespace distraction still causes substantial degradation.** Replacing essay tokens with whitespace reduces but does not eliminate the performance drop: at least 7% at 30K tokens for Llama on GSM8K, and up to 48% for Llama on VarSum. Evidence: Section 4.1, Figure 4a, Table 7. Status: **supported**.

3. **C3: Attention masking does not prevent degradation.** Even when all distraction tokens are masked and the model attends only to evidence and question tokens, performance drops persist, reaching at least 7.9% (Mistral HumanEval) and up to 50% (Llama3 VarSum and HumanEval) at 30K masked tokens. Evidence: Section 4.2, Table 3. Status: **supported**.

4. **C4: Evidence-question distance is not the sole cause.** When evidence is placed immediately before the question (constant distance), substantial drops persist: up to 20% for Llama and 17% for Mistral at 30K whitespace tokens. Evidence: Section 4.1, Figure 4b, Table 8. Status: **supported**.

5. **C5: Closed-source models show less degradation but are not immune.** GPT-4o and Gemini-2.0 maintain perfect VarSum scores but still drop on GSM8K (GPT-4o: -7.0% at 30K) and MMLU. Claude-3.5 shows large MMLU drops (-67.6% at 30K). Exception: Gemini-2.0 improves on GSM8K (+6.2% at 30K). Evidence: Section 4.1, Table 2. Status: **supported**.

6. **C6: Retrieve-then-reason improves long-context performance.** Prompting the model to recite evidence and then solving in a new short prompt improves Mistral on GSM8K by up to 31.2 percentage points, and GPT-4o on RULER QA2 by up to 4.0 points. Evidence: Section 5, Tables 4, 5. Status: **supported**.

---

## Open Questions

1. **What is the precise mechanism by which increased positional indices degrade reasoning capacity?** The paper establishes the phenomenon through the attention masking experiment (where the only difference from short-context is positional distance) and connects it to positional distribution bias during training, but does not identify the internal mechanism. Partially addressed by An et al. (2024) and the theoretical framework of Li et al. (2025-07-position-bias-transformers).

2. **Can training-time interventions eliminate the length-alone degradation?** The paper only proposes an inference-time mitigation (retrieve-then-reason). Whether training on diverse positional distributions, using position-independent encodings, or other training strategies can address the root cause remains open.

3. **Is there a model size or training data threshold above which the degradation disappears?** The gap between open-source 7B--8B models and closed-source models (likely much larger) suggests scale may help, but whether sufficient scale fully eliminates the effect is unknown.

---

## Core References and Why They Are Referenced

### Long-Context Retrieval and Reasoning Decomposition

- **Wu et al. (2024c)** -- *Retrieval Head Mechanistically Explains Long-Context Factuality.* Provides the mechanistic basis for the retrieval-reasoning decomposition of long-context tasks that this paper challenges.
- **Kuratov et al. (2024)** -- *BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack.* Reports a gap between retrieval and reasoning performance in long contexts, which this paper disentangles by controlling for perfect retrieval.
- **Li et al. (2024a)** -- *ALR²: A Retrieve-Then-Reason Framework for Long-Context Question Answering.* Proposes training models to align retrieval and reasoning objectives. This paper's mitigation is related but inference-only and does not address retrieval itself.
- **Qiu et al. (2025)** -- *Eliciting In-Context Retrieval and Reasoning for Long-Context LLMs.* Follows the two-part decomposition that this paper shows is incomplete.

### Positional Bias and Context Length Effects

- **Liu et al. (2024b)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Demonstrates the U-shaped positional performance curve. This paper builds on this by placing evidence at the beginning (the easiest position per Lost-in-the-Middle) and showing degradation still occurs due to input length itself.
- **An et al. (2024)** -- *Why Does the Effective Context Length of LLMs Fall Short?* Attributes performance drops to distribution bias with position introduced during training. This paper extends the analysis to show that positional bias also drives degradation from length alone, independent of retrieval.
- **Shi et al. (2023)** -- *Large Language Models Can Be Easily Distracted by Irrelevant Context.* Shows that irrelevant tokens distract models in reasoning tasks. This paper demonstrates that even *without* irrelevant content (via masking), length alone hurts performance.

### Evaluation Benchmarks

- **Kamradt (2023)** -- *Needle in a Haystack -- Pressure Testing LLMs.* The original NIAH test; this paper uses Paul Graham Essays from this work as essay distraction tokens.
- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* Provides the QA1 and QA2 tasks used to evaluate the retrieve-then-reason strategy with GPT-4o.
- **Hendrycks et al. (2021a)** -- *Measuring Massive Multitask Language Understanding (MMLU).* QA benchmark used in the evaluation.
- **Cobbe et al. (2021)** -- *Training Verifiers to Solve Math Word Problems (GSM8K).* Math benchmark used in the evaluation.
- **Chen et al. (2021)** -- *Evaluating Large Language Models Trained on Code (HumanEval).* Coding benchmark used in the evaluation.

### Models Evaluated

- **Meta (2024)** -- *The Llama 3 Herd of Models.* Provides Llama-3.1-8B-Instruct (128K claimed context), one of the primary open-source models evaluated.
- **Jiang et al. (2023)** -- *Mistral 7B.* Provides Mistral-v0.3-7B-Instruct (32K claimed context), the other primary open-source model evaluated.

### RAG and Practical Implications

- **Cuconasu et al. (2024)** -- *The Power of Noise: Redefining Retrieval for RAG Systems.* Reports that RAG performance can degrade with more retrieved documents, consistent with this paper's finding that longer context hurts.
- **Jin et al. (2024)** -- *Long-Context LLMs Meet RAG: Overcoming Challenges for Long Inputs in RAG.* Reports similar saturation/degradation patterns in RAG with increasing context.
- **Yu et al. (2024)** -- *In Defense of RAG in the Era of Long-Context Language Models.* Finds diminishing returns from context length in RAG settings, supporting this paper's conclusions.
- **Zeng et al. (2025)** -- *Revisiting the Test-Time Scaling of O1-Like Models.* Shows that long chain-of-thought can hurt reasoning models, which this paper explains via the length-alone degradation effect.
