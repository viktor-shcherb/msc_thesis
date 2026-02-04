---
title: "ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding"
authors: "Shaham, Ivgi, Efrat, Berant, Levy"
year: 2023
venue: "Findings of EMNLP 2023"
paper_type: conference-paper
categories: ["benchmarking", "long-context-evaluation"]
scope: ["zero-shot long-text evaluation", "benchmark design", "information aggregation"]
benchmarks_used: ["zeroscrolls", "scrolls"]
models_introduced: []
models_evaluated: ["gpt-4"]
key_claims:
  - id: C1
    claim: "GPT-4 achieves the highest average ZeroSCROLLS score (41.7), followed by Claude (39.1), both significantly outperforming open-source models"
    evidence: "Table 3, Section 4.2"
    status: supported
  - id: C2
    claim: "Zero-shot LLMs bridge the gap with fine-tuned models on QA tasks but not summarization: GPT-4 scores 89.2 on QuALITY (vs CoLT5 47.0) but only 26.3 on GovReport (vs CoLT5 41.0)"
    evidence: "Table 3, Section 4.2"
    status: supported
  - id: C3
    claim: "Information aggregation tasks (SpaceDigest, BookSumSort) are exceptionally difficult: only GPT-4 surpasses naive baselines on both tasks"
    evidence: "Table 3, Section 4.2"
    status: supported
  - id: C4
    claim: "Format discrepancy significantly impacts automatic evaluation: GPT-4 is correct more often than Claude on NarrativeQA (53% vs 39% human-judged accuracy) despite scoring 5 F1 points lower"
    evidence: "Section 5, Figure 4"
    status: supported
  - id: C5
    claim: "Performance scales with both model size and input length: Flan-T5 improves from avg 11.0 (60M params) to 29.9 (11B params), and from avg 17.1 (512 tokens) to 29.9 (8192 tokens)"
    evidence: "Table 4, Section 4.3"
    status: supported
cross_references:
  - target: 2022-12-scrolls-long-language-sequences
    type: extends
    detail: "Direct zero-shot successor to SCROLLS, adapting 6 of 7 tasks and adding 4 new datasets"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong references ZeroSCROLLS as lacking controllable sequence length"
  - target: 2024-10-ruler-context-size
    type: complementary
    detail: "RULER contrasts with ZeroSCROLLS as a realistic but uncontrollable benchmark"
  - target: 2025-07-longbench-v2
    type: complementary
    detail: "LongBench v2 references ZeroSCROLLS as an earlier long-context evaluation effort"
  - target: 2026-01-longbench-pro
    type: complementary
    detail: "LongBench Pro references ZeroSCROLLS as an early effort in long-context evaluation"
  - target: 2024-08-l-eval-standardized-evaluation
    type: concurrent
    detail: "L-Eval is a concurrent long-context benchmark that addresses dataset quality and evaluation metric standardization"
  - target: 2024-07-llama-3-herd-of-models
    type: extended-by
    detail: "Llama 3 achieves 95.2% on QuALITY, matching GPT-4"
open_questions:
  - question: "How should automatic metrics be adapted for zero-shot evaluation where output format varies across models?"
    addressed_by: null
  - question: "Can chain-of-thought prompting or model-specific prompts significantly improve performance on aggregation tasks?"
    addressed_by: null
  - question: "How do models with context windows beyond 8,192 tokens perform on ZeroSCROLLS tasks?"
    addressed_by: null
  - question: "Why does GPT-4 refuse to answer questions about trimmed context far more often than Claude (30/200 vs 5/200)?"
    addressed_by: null
---

# ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding

**Authors:** Uri Shaham, Maor Ivgi, Avia Efrat, Jonathan Berant, Omer Levy (Tel Aviv University, Meta AI)
**Date:** December 2023, Findings of EMNLP 2023 (arXiv:2305.14196)

---

## Core Research Problem

SCROLLS (Shaham et al., 2022) established a multi-task benchmark for long-text understanding, but it requires task-specific fine-tuning. In the era of general-purpose zero-shot LLMs (Wei et al., 2022a; Ouyang et al., 2022; OpenAI, 2023), a new evaluation setup is needed that removes this dependence on training data (Section 1, Section 2). Existing zero-shot LLM benchmarks evaluate primarily on short sequences: HELM (Liang et al., 2022) and BigBench (Srivastava et al., 2022) focus on short inputs, with BigBench averaging only 77 words per input (Section 1).

Furthermore, SCROLLS lacks tasks that explicitly test **information aggregation** across long sequences -- tasks requiring a model to contextualize and combine information from many distinct parts of the input, such as computing sentiment statistics over dozens of reviews or establishing temporal ordering across chapter summaries (Section 3.1.3).

**The core challenge is how to evaluate zero-shot LLM capabilities on long-text understanding tasks that require no training data, while introducing new task types that test information aggregation across long contexts.**

---

## Problem Solutions

ZeroSCROLLS extends SCROLLS to the zero-shot setting by removing training data, adding new task types, and conducting the first systematic zero-shot evaluation of LLMs on long-text tasks.

1. **Zero-shot design.** Only test and small validation sets are provided, with no training data. Simple natural-language prompts define each task without in-context demonstrations (Section 3.2).
2. **10 diverse tasks.** Six tasks adapted from SCROLLS (GovReport, SummScreenFD, QMSum, Qasper, NarrativeQA, QuALITY) plus four new tasks (SQuALITY, MuSiQue, SpaceDigest, BookSumSort) (Section 3.1, Table 1).
3. **Two novel aggregation tasks.** SpaceDigest (sentiment aggregation over 50 hotel reviews) and BookSumSort (reordering shuffled chapter summaries) explicitly require fusing information across the entire input (Section 3.1.3).
4. **Affordability.** Each task is capped at a maximum of 500 test examples to limit evaluation cost (Section 3).

---

## Approach Details

### Method

ZeroSCROLLS provides each instance with a zero-shot prompt composed of four components (Section 3.2, Figure 3): (1) an **instruction** describing the task and desired output format, (2) a **context** header and the long document, (3) a **query** (for tasks with questions), and (4) a **response** header (e.g., "Answer:" or "Summary:"). When input exceeds the model's context window, the context is trimmed and an explicit note informs the model that the rest of the context has been removed.

**Chat model accommodations.** For chat LLMs (ChatGPT, Claude, GPT-4), response headers are omitted and an additional instruction "Do not provide any explanation." is appended for QA and aggregation tasks. For Claude specifically, prompts are wrapped with "Human:" and "Assistant:" dialogue indicators, with instructions to highlight the final answer using XML tags (Section 3.2).

### Key Technical Components

**Datasets (Table 1):**

| Dataset | Task | Domain | Metric | Avg #Words | #Examples |
|---|---|---|---|---|---|
| GovReport | Summarization | Government | ROUGE | 7,273 | 500 |
| SummScreenFD | Summarization | TV | ROUGE | 5,663 | 337 |
| QMSum | QB-Summarization | Meetings | ROUGE | 10,839 | 281 |
| SQuALITY (new) | QB-Summarization | Literature | ROUGE | 4,971 | 260 |
| Qasper | QA | Science | F1 | 3,531 | 500 |
| NarrativeQA | QA | Literature, Film | F1 | 49,384 | 500 |
| QuALITY | MC-QA | Literature, Misc | Accuracy | 4,248 | 500 |
| MuSiQue (new) | Multi-hop QA | Wikipedia | F1 | 1,749 | 500 |
| SpaceDigest (new) | Aggregation | Reviews | ES | 5,481 | 500 |
| BookSumSort (new) | Aggregation | Literature | C_idx | 6,840 | 500 |

**New task construction:**

- **SpaceDigest** (Section 3.1.3): 50 hotel reviews per example from the Space dataset (Angelidis et al., 2021), drawn from the 500 most-rated hotels. Only strictly positive (rating 4--5) or negative (rating 1--2) reviews are kept; ambivalent 3-star reviews are discarded. The task is to determine the percentage of positive reviews. Human annotators achieved ~98.4% accuracy at classifying individual reviews (8 errors out of 500 reviews across 5 annotators), with perfect aggregation.
- **BookSumSort** (Section 3.1.3): 125 manually selected books from BookSum (Kryscinski et al., 2022). Summaries are manually edited to remove positional indicators (e.g., "Chapter 8 begins with..." replaced by "This Chapter begins with..."). Each list contains 3--86 chapter summaries (median 15, mean 18.8). Four random permutations per book yield 500 instances.
- **MuSiQue** (Section 3.1.2): Multi-hop QA over 20 Wikipedia paragraphs. 400 answerable and 100 unanswerable questions randomly sampled from the original dataset (Trivedi et al., 2022).
- **SQuALITY** (Section 3.1.1): Question-focused summarization over Project Gutenberg stories (Wang et al., 2022), where experienced writers designed questions requiring reading significant parts of the story.

**Evaluation metrics (Section 3.3):**

- **ROUGE** (GovReport, SummScreenFD, QMSum, SQuALITY): Geometric mean of ROUGE-1, ROUGE-2, and ROUGE-L. For SQuALITY (multiple references), the max of each ROUGE type is taken before computing the geometric mean.
- **F1** (Qasper, NarrativeQA, MuSiQue): Unigram overlap after lowercasing, stopword/punctuation removal, and Unicode-to-ASCII transliteration. Max F1 across multiple references per instance.
- **Accuracy** (QuALITY): First valid option letter (A, B, C, D) surrounded by word boundaries.
- **Exponential Similarity** (SpaceDigest):

> `ES(p, p_hat) = d^(-c * |p - p_hat|)` with `d = 2, c = 10`

The score halves for every 10 percentage point deviation. Outputs that are not a valid percentage score 0%.

- **Concordance Index** (BookSumSort): Fraction of chapter summary pairs in the correct relative order, out of all `n choose 2` pairs. Random permutations average 50%. Outputs that are not a valid permutation score 0%.

**Naive baselines (Section 4.1):** Random spans of task-specific lengths for summarization and NarrativeQA (500, 200, 50, 120, and 4 words respectively). Random fixed choices for Qasper ("Yes"/"No"/"Unanswerable" or 15-word span). "Unanswerable" for all MuSiQue instances. Random A/B/C/D for QuALITY. Always 50% for SpaceDigest. Trivial permutation "1, 2, 3, ..., n" for BookSumSort.

### Experimental Setup

**Models evaluated (Table 2):**

| Model | Parameters | Max Tokens | Open/Closed |
|---|---|---|---|
| T0pp | 11B | 8,192 | Open |
| Flan-T5-xxl | 11B | 8,192 | Open |
| Flan-UL2 | 20B | 8,192 | Open |
| DaVinci003 | -- | 4,096 | Closed |
| ChatGPT (v0301) | -- | 4,096 | Closed |
| Claude (v1.3) | -- | 8,192 | Closed |
| GPT-4 (v0314) | -- | 8,192 | Closed |

Greedy decoding is applied to all models (Section 4.1). For Flan-T5, additional scaling experiments use sizes from Small (60M) to XXL (11B), and input lengths from 512 to 8,192 tokens (Table 4). Claude is also evaluated at 4,096 tokens.

**Fine-tuned comparison:** CoLT5-xl (Ainslie et al., 2023), a conditionally-computing transformer with 16,384 max tokens, the state of the art on SCROLLS at the time (Section 4.1).

**Human performance (Table 3):** SQuALITY 23.6 ROUGE (inter-reference comparison, Wang et al., 2022), Qasper 67.7 F1 (inter-annotator), NarrativeQA 58.2 F1 (inter-annotator), QuALITY 93.5 accuracy (Pang et al., 2022), MuSiQue 74.8 F1 (combined from Trivedi et al., 2022), SpaceDigest 93.3 ES (own human annotations, Section 3.1.3).

### Key Results

**Main leaderboard (Table 3):**

| Model | GovReport | SummScreenFD | QMSum | SQuALITY | Qasper | NarrativeQA | QuALITY | MuSiQue | SpaceDigest | BookSumSort | Avg |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 22.6 | 6.7 | 6.7 | 10.5 | 6.1 | 2.1 | 26.6 | 20.0 | 45.0 | 50.0 | 19.6 |
| T0pp (8k) | 7.1 | 9.6 | 7.2 | 3.9 | 25.0 | 18.7 | 21.4 | 35.3 | 15.2 | 0.0 | 14.3 |
| Flan-T5-xxl (8k) | 17.6 | 7.8 | 11.0 | 8.0 | 48.3 | 19.3 | 75.2 | 46.8 | 48.7 | 16.4 | 29.9 |
| Flan-UL2 (8k) | 16.1 | 11.5 | 13.6 | 5.7 | 56.9 | 25.5 | 75.6 | 51.3 | 36.0 | 14.0 | 30.6 |
| DaVinci003 (4k) | 21.7 | 16.1 | 16.9 | 22.0 | 52.7 | 24.6 | 69.0 | 33.5 | 31.3 | 49.5 | 33.7 |
| ChatGPT (4k) | 21.3 | 16.1 | 15.6 | 20.4 | 49.3 | 25.1 | 66.6 | 27.1 | 49.1 | 49.8 | 34.0 |
| Claude (8k) | 24.2 | 16.1 | 14.6 | 21.0 | 52.3 | 32.6 | 84.8 | 36.1 | 61.6 | 47.4 | 39.1 |
| GPT-4 (8k) | 26.3 | 17.3 | 18.5 | 22.6 | 50.7 | 27.6 | 89.2 | 41.1 | 62.8 | 60.5 | 41.7 |
| CoLT5 (16k, fine-tuned) | 41.0 | 20.0 | 22.5 | -- | 53.1 | 31.0 | 47.0 | -- | -- | -- | -- |

- **GPT-4 achieves the highest average score (41.7)**, followed by Claude (39.1). Both significantly outperform open-source models and the remaining closed models (Section 4.2).
- **Summarization: zero-shot LLMs lag behind fine-tuning.** CoLT5 scores 41.0 on GovReport vs. GPT-4's 26.3 -- a 14.7-point gap. Gaps are smaller on SummScreenFD (20.0 vs 17.3) and QMSum (22.5 vs 18.5). On SQuALITY, GPT-4 (22.6) approaches the lower bound of human performance (23.6) (Section 4.2).
- **QA: zero-shot LLMs bridge the gap with fine-tuned models.** GPT-4 scores 89.2% on QuALITY, close to human performance (93.5%) and far above CoLT5 (47.0%). On Qasper, Flan-UL2 (56.9) exceeds CoLT5 (53.1). Claude leads on NarrativeQA (32.6 vs GPT-4's 27.6), and Flan-UL2 leads on MuSiQue (51.3 vs GPT-4's 41.1) (Section 4.2).
- **Aggregation tasks are exceptionally difficult.** On SpaceDigest, only Claude (61.6) and GPT-4 (62.8) surpass the naive 45.0 baseline (which always predicts 50%). On BookSumSort, only GPT-4 (60.5) exceeds the trivial permutation baseline (50.0) (Section 4.2).

### Impact of Model Size and Input Length

**Model size (Table 4, upper section):** Flan-T5 performance increases consistently from Small (60M parameters, avg 11.0) through Base (avg 13.2), Large (avg 22.7), XL (avg 25.5) to XXL (11B parameters, avg 29.9). SpaceDigest shows a non-monotonic pattern: 0.0 for Small and Base, 48.0 for Large, 32.8 for XL, then 48.7 for XXL (Table 4).

**Input length -- Flan-T5-xxl (Table 4, middle section):** Average improves from 17.1 (512 tokens) to 20.8 (1024), 24.9 (2048), 29.1 (4096), and 29.9 (8192). Flan-T5 achieves higher scores on longer inputs despite being trained on much shorter sequences (Section 4.3).

**Input length -- Claude (Table 4, lower section):** Average improves from 36.3 (4,096 tokens) to 39.1 (8,000 tokens) -- a gain of ~2.8 points. The largest gains come from QuALITY (76.8 to 84.8) and BookSumSort (37.6 to 47.4) (Table 4).

### Format Discrepancy Analysis

Human evaluation on 100 sampled instances per dataset reveals that automatic metrics understate GPT-4's true performance (Section 5, Figure 4):

| Task | Compared Model | Compared Model Human Accuracy | GPT-4 Human Accuracy |
|---|---|---|---|
| NarrativeQA | Claude | 39% | 53% |
| Qasper | Flan-UL2 | 69% | 80% |
| MuSiQue | Flan-UL2 | 51% | 47% |

- On NarrativeQA, Claude scores 5 F1 points higher than GPT-4 on automatic metrics, but human evaluation shows GPT-4 is correct more often (53% vs 39%). Analysis of 200 random instances shows Claude answers in the requested format ("using a single phrase if possible") 191/200 times vs. GPT-4's 71/200 (Section 5).
- GPT-4 refuses to answer 30/200 NarrativeQA questions because the trimmed context does not contain the answer, compared to Claude's 5/200 refusals, despite both having similar context lengths (~8k) (Section 5, footnote 9).
- Output length distributions (Figure 5) confirm format discrepancy is not unique to GPT-4 or NarrativeQA: Claude generates overly long answers for QMSum, Flan-UL2 generates overly long summaries for SummScreenFD, and all models generate overly short summaries for GovReport (Section 5).

---

## Limitations and Failure Modes

The paper discusses limitations in Section 7:

1. **Automatic metrics penalize valid outputs.** In the zero-shot setting, where models must infer output format from the prompt, ROUGE and F1 assign low scores to semantically equivalent generations with different word choices or answer lengths. This is confirmed by the format discrepancy analysis in Section 5, where GPT-4's human-judged accuracy exceeds its automatic F1 scores.

2. **Common prompts across models.** For fair evaluation, the same prompt templates are used across all models. Model-specific prompts or chain-of-thought prompting (Wei et al., 2022b) could improve performance but were not explored (Section 7).

3. **Context length caps.** All models were evaluated with at most 8,192 input tokens. Models with longer context windows may perform differently, especially on tasks like NarrativeQA (avg 49,384 words) where substantial truncation occurs (Section 7).

4. **Moving target.** New models, alignment methods, decoding algorithms, and prompting techniques continuously emerge. The paper's results reflect a snapshot in time; the live leaderboard addresses this (Section 7).

5. **Aggregation task difficulty may conflate multiple skills.** SpaceDigest combines sentiment classification, counting, and division -- individually "easy" tasks whose combination proves challenging. It is unclear whether failures stem from difficulty in aggregating across long contexts or from the compositional nature of the task (inference from Section 4.2).

---

## Conclusions

### Contributions

1. **First systematic zero-shot long-text evaluation benchmark.** ZeroSCROLLS fills the gap between short-text zero-shot benchmarks (HELM, BigBench) and fine-tuning-dependent long-text benchmarks (SCROLLS), enabling comparison of general-purpose LLMs on 10 tasks with naturally long texts (Section 1, Section 3).

2. **Revealed that zero-shot LLMs match fine-tuned models on QA but not summarization.** GPT-4 achieves 89.2% on QuALITY (vs. CoLT5's 47.0% and human 93.5%), but scores only 26.3 on GovReport (vs. CoLT5's 41.0) (Table 3, Section 4.2).

3. **Established information aggregation as an open challenge.** SpaceDigest and BookSumSort demonstrate that even strong LLMs struggle to systematically aggregate information across long contexts -- combining individually easy subtasks into a difficult composite task. Only GPT-4 beats naive baselines on both tasks (Table 3, Section 4.2).

4. **Quantified format discrepancy as a significant evaluation issue.** Human evaluation demonstrates that GPT-4 is correct more often than its F1 scores suggest (e.g., 53% vs 39% accuracy on NarrativeQA vs Claude), with format non-compliance (71/200 vs 191/200) explaining the automatic metric gap (Section 5).

5. **Confirmed that both model size and input length matter.** Performance scales with model size (Flan-T5: avg 11.0 at 60M to 29.9 at 11B) and context length (Flan-T5-xxl: avg 17.1 at 512 tokens to 29.9 at 8192 tokens; Claude: avg 36.3 at 4k to 39.1 at 8k), confirming ZeroSCROLLS captures genuine long-text understanding (Table 4, Section 4.3).

### Implications

1. **Zero-shot evaluation requires new metrics.** The demonstrated gap between automatic metrics and human judgments -- particularly for models that generate correct but differently formatted answers -- suggests that standard n-gram metrics (ROUGE, F1) are insufficient for zero-shot long-text evaluation. This echoes SCROLLS's own acknowledgment of ROUGE limitations.

2. **Aggregation tasks probe a distinct capability.** The finding that sentiment classification, counting, and division are individually easy but their composition over long contexts is hard suggests that **information aggregation** across sequences represents a capability distinct from retrieval or synthesis, warranting dedicated evaluation (inference from Section 4.2).

3. **Instruction following is entangled with task performance.** The format discrepancy results suggest that benchmarks measuring both instruction adherence and task competence conflate two distinct skills, potentially misranking models that are stronger at one but weaker at the other (inference from Section 5).

---

## Key Claims

1. **C1: GPT-4 achieves the highest average ZeroSCROLLS score (41.7).** Claude follows at 39.1, both significantly above open-source models (Flan-UL2 30.6, Flan-T5 29.9) and other closed models (ChatGPT 34.0, DaVinci003 33.7). Evidence: Table 3, Section 4.2. Status: **supported**.

2. **C2: Zero-shot LLMs bridge the gap with fine-tuned models on QA but not summarization.** GPT-4 scores 89.2 on QuALITY vs. CoLT5's 47.0, and Flan-UL2 scores 56.9 on Qasper vs. CoLT5's 53.1. But on GovReport summarization, CoLT5 scores 41.0 vs. GPT-4's 26.3 -- a 14.7-point gap. Evidence: Table 3, Section 4.2. Status: **supported**.

3. **C3: Information aggregation tasks are exceptionally difficult for all models.** On SpaceDigest, only Claude (61.6) and GPT-4 (62.8) surpass the naive baseline (45.0). On BookSumSort, only GPT-4 (60.5) exceeds the trivial permutation baseline (50.0). T0pp scores 0.0 on BookSumSort and 15.2 on SpaceDigest. Evidence: Table 3, Section 4.2. Status: **supported**.

4. **C4: Format discrepancy significantly impacts automatic evaluation scores.** On NarrativeQA, Claude outperforms GPT-4 by 5 F1 points (32.6 vs 27.6), but human evaluation shows GPT-4 is correct more often (53% vs 39% accuracy). GPT-4 conforms to the requested format in only 71/200 cases vs. Claude's 191/200. Evidence: Section 5, Figure 4. Status: **supported**.

5. **C5: Performance scales with both model size and input length.** Flan-T5 averages increase from 11.0 (60M) to 29.9 (11B). Flan-T5-xxl averages increase from 17.1 (512 tokens) to 29.9 (8192 tokens). Claude gains ~2.8 points from 4k to 8k tokens (36.3 to 39.1). Evidence: Table 4, Section 4.3. Status: **supported**.

---

## Open Questions

1. **How should automatic metrics be adapted for zero-shot evaluation where output format varies across models?** The paper demonstrates that ROUGE and F1 penalize correct but differently formatted answers, particularly GPT-4's tendency to generate complete sentences when asked for phrases (Section 5, Section 7). **Unresolved** within the references directory.

2. **Can chain-of-thought prompting or model-specific prompts significantly improve performance on aggregation tasks?** The paper uses common prompts across all models for fairness and explicitly notes that chain-of-thought prompting was not explored (Section 3.2, Section 7). **Unresolved**.

3. **How do models with context windows beyond 8,192 tokens perform on ZeroSCROLLS tasks?** All evaluated models have at most 8,192 tokens of context. Tasks like NarrativeQA (avg 49,384 words) require substantial truncation, and Claude's improvement from 4k to 8k tokens suggests further gains may be possible (Table 4, Section 4.3, Section 7). **Unresolved**.

4. **Why does GPT-4 refuse to answer questions about trimmed context far more often than Claude?** GPT-4 responds "unable to answer" for 30/200 NarrativeQA instances vs. Claude's 5/200, despite similar context lengths (Section 5, footnote 9). **Unresolved**.

---

## Core References and Why They Are Referenced

### Predecessor Benchmark

- **Shaham et al. (2022)** -- *SCROLLS: Standardized CompaRison Over Long Language Sequences.* The direct predecessor that ZeroSCROLLS extends. Six of ZeroSCROLLS's ten tasks are adapted from SCROLLS. The key difference is removing training data and evaluating zero-shot capabilities.

### Short-Text Zero-Shot Benchmarks

- **Liang et al. (2022)** -- *HELM: Holistic Evaluation of Language Models.* A large-scale LLM evaluation covering many tasks but focusing on short sequences. ZeroSCROLLS fills the long-text gap in HELM's coverage.
- **Srivastava et al. (2022)** -- *Beyond the Imitation Game (BigBench).* A large benchmark with an average of 77 words per input, motivating ZeroSCROLLS's focus on naturally long inputs.

### Models Evaluated

- **OpenAI (2023)** -- *GPT-4.* The top-performing model on ZeroSCROLLS (avg 41.7), approaching human performance on QuALITY (89.2 vs. 93.5) but struggling on aggregation tasks.
- **Wei et al. (2022a)** -- *Finetuned Language Models Are Zero-Shot Learners (Flan-T5).* Open-source instruction-tuned model family used for model size and input length scaling experiments (Table 4). Flan-UL2 achieves the highest open-source scores on Qasper (56.9) and MuSiQue (51.3).
- **Sanh et al. (2022)** -- *T0pp.* An LM-adapted T5 model finetuned on various NLP tasks for zero-shot generalization. Achieves the lowest average score among evaluated models (14.3), scoring 0.0 on BookSumSort.
- **Ainslie et al. (2023)** -- *CoLT5.* Conditionally-computing transformer, state of the art on SCROLLS at the time. Used as the fine-tuned comparison point: outperforms GPT-4 on summarization (GovReport 41.0 vs 26.3) but underperforms on QuALITY (47.0 vs 89.2).

### New Task Sources

- **Wang et al. (2022)** -- *SQuALITY.* Question-focused summarization dataset over Project Gutenberg stories. GPT-4 (22.6) approaches the lower bound of human performance (23.6).
- **Trivedi et al. (2022)** -- *MuSiQue.* Multi-hop QA over Wikipedia paragraphs. ZeroSCROLLS samples 400 answerable and 100 unanswerable questions.
- **Angelidis et al. (2021)** -- *Space.* Hotel review dataset providing the raw reviews for SpaceDigest. Reviews are filtered to keep only strictly positive (4--5) or negative (1--2) ratings.
- **Kryscinski et al. (2022)** -- *BookSum.* Novel chapter summaries providing the data for BookSumSort. Summaries are manually edited to remove positional indicators.

### Instruction Following and Zero-Shot Generalization

- **Ouyang et al. (2022)** -- *InstructGPT / RLHF.* Training language models to follow instructions, enabling the zero-shot evaluation paradigm that ZeroSCROLLS targets.
- **Wei et al. (2022b)** -- *Chain-of-Thought Prompting.* Noted as a promising but unexplored prompting technique that could improve ZeroSCROLLS performance (Section 3.2, Section 7).
