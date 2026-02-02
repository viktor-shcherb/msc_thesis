# ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding

**Authors:** Uri Shaham, Maor Ivgi, Avia Efrat, Jonathan Berant, Omer Levy (Tel Aviv University, Meta AI)
**Date:** December 2023, Findings of EMNLP 2023 (arXiv:2305.14196)

---

## Core Research Problem

SCROLLS (Shaham et al., 2022) established a standard benchmark for long-text understanding, but it relies on task-specific fine-tuning. In the era of general-purpose zero-shot LLMs (Wei et al., 2022a; Ouyang et al., 2022; OpenAI, 2023), a new evaluation setup is needed that removes the dependence on training data. Existing zero-shot LLM benchmarks such as HELM (Liang et al., 2022) and BigBench (Srivastava et al., 2022) mostly focus on short sequences -- BigBench has an average of 77 words per input.

Furthermore, SCROLLS lacks tasks that explicitly test information aggregation across long sequences. Its tasks evaluate retrieval and synthesis but not systematic aggregation (e.g., computing statistics over many documents) or temporal ordering.

**The core challenge is how to evaluate zero-shot LLM capabilities on long-text understanding tasks that require no training data, while introducing new task types that test information aggregation across long contexts.**

---

## Problem Solutions

ZeroSCROLLS extends SCROLLS to the zero-shot setting by removing training data, adding new task types, and conducting the first systematic zero-shot evaluation of LLMs on long-text tasks.

1. **Zero-shot design.** Only test and small validation sets, no training data. Simple natural-language prompts define each task.
2. **10 diverse tasks.** Six tasks adapted from SCROLLS (GovReport, SummScreenFD, QMSum, Qasper, NarrativeQA, QuALITY) plus four new tasks (SQuALITY, MuSiQue, SpaceDigest, BookSumSort).
3. **Two novel aggregation tasks.** SpaceDigest (sentiment aggregation over 50 hotel reviews) and BookSumSort (reordering shuffled chapter summaries) test information fusion across the entire input.

---

## Approach Details

### Method

ZeroSCROLLS provides each instance with a zero-shot prompt composed of four components: (1) an instruction describing the task and desired output format, (2) a context header and the long document, (3) a query (for tasks with questions), and (4) a response header. When input exceeds the model's context window, the context is trimmed with an explicit note informing the model. Chat models receive adapted prompts without response headers and with additional format enforcement instructions.

### Datasets

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

### Key Technical Components

**New evaluation metrics:**

- **Exponential Similarity (ES)** for SpaceDigest: `ES(p, p_hat) = 2^(-10 * |p - p_hat|)`. The score halves for every 10 percentage point deviation from the correct answer.
- **Concordance Index (C_idx)** for BookSumSort: fraction of chapter summary pairs in the correct relative order, out of all `n choose 2` pairs. Random permutation scores 50%.

**Prompt design.** Simple, natural-language zero-shot prompts without in-context demonstrations. Task description includes desired output format (e.g., "Answer the question as concisely as you can, using a single phrase if possible"). Chat models receive additional instructions ("Do not provide any explanation") and omitted response headers.

**Affordability.** Each task capped at 500 test examples to limit evaluation cost.

**SpaceDigest construction.** 50 hotel reviews per example from the Space dataset (Angelidis et al., 2021), keeping only clearly positive (4--5) or negative (1--2) ratings, discarding ambivalent 3-star reviews. Human annotators achieved ~98.4% accuracy (8 errors out of 500 reviews).

**BookSumSort construction.** 125 books from BookSum (Kryscinski et al., 2022), manually edited to remove positional indicators (e.g., "Chapter 8 begins with..." replaced by "This Chapter begins with..."). 3--86 chapter summaries per book (median 15). 4 random permutations per book yield 500 instances.

### Experimental Setup

**Models evaluated:**

| Model | Parameters | Max Tokens | Open/Closed |
|---|---|---|---|
| T0pp | 11B | 8,192 | Open |
| Flan-T5-xxl | 11B | 8,192 | Open |
| Flan-UL2 | 20B | 8,192 | Open |
| DaVinci003 | -- | 4,096 | Closed |
| ChatGPT (v0301) | -- | 4,096 | Closed |
| Claude (v1.3) | -- | 8,192 | Closed |
| GPT-4 (v0314) | -- | 8,192 | Closed |

**Fine-tuned comparison:** CoLT5-xl (Ainslie et al., 2023) with 16,384 tokens, state of the art on SCROLLS.

**Decoding:** Greedy decoding for all models.

### Key Results

| Model | GovReport | SummScreenFD | QMSum | SQuALITY | Qasper | NarrativeQA | QuALITY | MuSiQue | SpaceDigest | BookSumSort | Avg |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Naive | 22.6 | 6.7 | 6.7 | 10.5 | 6.1 | 2.1 | 26.6 | 20.0 | 45.0 | 50.0 | 19.6 |
| Flan-UL2 (8k) | 16.1 | 11.5 | 13.6 | 5.7 | 56.9 | 25.5 | 75.6 | 51.3 | 36.0 | 14.0 | 30.6 |
| Claude (8k) | 24.2 | 16.1 | 14.6 | 21.0 | 52.3 | 32.6 | 84.8 | 36.1 | 61.6 | 47.4 | 39.1 |
| GPT-4 (8k) | 26.3 | 17.3 | 18.5 | 22.6 | 50.7 | 27.6 | 89.2 | 41.1 | 62.8 | 60.5 | 41.7 |
| CoLT5 (16k, fine-tuned) | 41.0 | 20.0 | 22.5 | -- | 53.1 | 31.0 | 47.0 | -- | -- | -- | -- |

- **GPT-4 achieves the highest average score (41.7)**, followed by Claude (39.1). Both significantly outperform open-source models.
- **Zero-shot LLMs bridge the gap with fine-tuned models on QA.** GPT-4 scores 89.2% on QuALITY, approaching human performance (93.5%). On Qasper, Flan-UL2 (56.9) and GPT-4 (50.7) are close to CoLT5 (53.1).
- **Zero-shot summarization lags behind fine-tuning.** CoLT5 scores 41.0 on GovReport vs. GPT-4's 26.3 -- a 14.7-point gap. The gap is smaller on SummScreenFD and QMSum.
- **Aggregation tasks are exceptionally difficult.** On SpaceDigest, only Claude and GPT-4 surpass the naive 50% baseline. On BookSumSort, only GPT-4 exceeds the trivial permutation baseline (60.5 vs. 50.0).
- **Format discrepancy penalizes GPT-4.** On NarrativeQA, Claude scores 5 F1 points higher than GPT-4 on automatic metrics, but human evaluation shows GPT-4 is correct more often (53% vs. 39% accuracy). GPT-4 conforms to the requested format in only 71/200 cases vs. Claude's 191/200.

### Impact of Model Size and Input Length

**Model size (Flan-T5):** Performance increases consistently from 60M (Flan-T5-s, avg 11.0) to 11B (Flan-T5-xxl, avg 29.9) parameters.

**Input length:** Increasing from 512 to 8,192 tokens improves Flan-T5-xxl from 17.1 to 29.9 average. Claude gains ~3 points going from 4,096 to 8,000 tokens (36.3 -> 39.1).

### Limitations

1. **Automatic metrics penalize valid outputs.** ROUGE and F1 assign low scores to semantically equivalent but differently worded generations, especially in the zero-shot setting where models may not match expected formats.
2. **Common prompts across models.** Model-specific prompts or chain-of-thought prompting could improve performance but were not explored for fairness.
3. **Context length caps.** All models evaluated at <= 8,192 tokens; longer-context models may perform differently.
4. **Moving target.** New models and techniques continuously emerge; the leaderboard addresses this but the paper's results reflect a snapshot in time.

---

## Conclusions

1. **First systematic zero-shot long-text evaluation.** ZeroSCROLLS enables comparison of general-purpose LLMs on 10 tasks requiring reasoning over naturally long texts without any task-specific training, filling the gap between short-text zero-shot benchmarks (HELM, BigBench) and fine-tuning-dependent long-text benchmarks (SCROLLS).

2. **GPT-4 and Claude lead, but significant gaps remain.** GPT-4 achieves the best average score (41.7), approaching human performance on QuALITY (89.2 vs. 93.5), but all models struggle with summarization compared to fine-tuned models, and aggregation tasks prove exceptionally challenging.

3. **Information aggregation is an open challenge.** SpaceDigest and BookSumSort reveal that even strong LLMs struggle to systematically aggregate information across long contexts -- combining individually easy subtasks (sentiment classification, counting, ordering) into a difficult composite task.

4. **Format discrepancy is a significant evaluation issue.** GPT-4 frequently generates correct but differently formatted answers, inflating the gap between automatic metrics and true performance. Human evaluation on QA tasks shows GPT-4 outperforming its F1 scores.

5. **Both model size and input length matter.** Performance scales with both parameters and context length across all tasks, confirming that ZeroSCROLLS captures genuine long-text understanding rather than short-text reasoning.

---

## Core References and Why They Are Referenced

### Predecessor Benchmark

- **Shaham et al. (2022)** -- *SCROLLS.* The direct predecessor that ZeroSCROLLS extends. Six of ZeroSCROLLS's ten tasks are adapted from SCROLLS. The key difference is removing training data and evaluating zero-shot capabilities.

### Short-Text Zero-Shot Benchmarks

- **Liang et al. (2022)** -- *HELM.* A holistic evaluation of language models that covers many tasks but focuses on short sequences. ZeroSCROLLS fills the long-text gap in HELM's coverage.
- **Srivastava et al. (2022)** -- *BigBench.* A large-scale LLM benchmark with an average of 77 words per input, motivating ZeroSCROLLS's focus on long inputs.

### Models Evaluated

- **OpenAI (2023)** -- *GPT-4.* The top-performing model on ZeroSCROLLS (avg 41.7), approaching human performance on QuALITY (89.2 vs. 93.5) but struggling on aggregation tasks.
- **Wei et al. (2022a)** -- *Flan-T5 / Finetuned Language Models.* Open-source instruction-tuned models that achieve competitive scores on QA tasks, especially Flan-UL2 on Qasper (56.9) and MuSiQue (51.3).
- **Ainslie et al. (2023)** -- *CoLT5.* State-of-the-art fine-tuned model on SCROLLS, used as the comparison point between zero-shot and fine-tuned performance. CoLT5 outperforms GPT-4 on summarization but underperforms on QuALITY.

### New Task Sources

- **Wang et al. (2022)** -- *SQuALITY.* Question-focused summarization added to ZeroSCROLLS. GPT-4 approaches the lower bound of human performance (22.6 vs. 23.6 ROUGE).
- **Trivedi et al. (2022)** -- *MuSiQue.* Multi-hop QA over Wikipedia paragraphs. ZeroSCROLLS samples 400 answerable and 100 unanswerable questions.
- **Angelidis et al. (2021)** -- *Space.* Hotel review dataset providing the raw reviews for SpaceDigest, ZeroSCROLLS's sentiment aggregation task.
- **Kryscinski et al. (2022)** -- *BookSum.* Novel chapter summaries providing the data for BookSumSort, ZeroSCROLLS's ordering task.

### Instruction Following and Zero-Shot Generalization

- **Ouyang et al. (2022)** -- *InstructGPT / RLHF.* Training language models to follow instructions, enabling the zero-shot evaluation paradigm that ZeroSCROLLS targets.
- **Sanh et al. (2022)** -- *T0pp.* An LM-adapted T5 model finetuned on various NLP tasks for zero-shot generalization. Achieves the lowest average score (14.3) among evaluated models.

#### Cross-References in Available Papers

- **BABILong (2024-12-babilong-long-context-reasoning):** References ZeroSCROLLS as a realistic benchmark lacking controllable sequence length. BABILong's reasoning-in-a-haystack approach addresses ZeroSCROLLS's inability to generate evaluation samples at arbitrary lengths.
- **RULER (2024-10-ruler-context-size):** Contrasts with ZeroSCROLLS as a realistic but uncontrollable benchmark that relies on parametric knowledge, motivating RULER's fully synthetic, length-controllable design.
- **LongBench v2 (2025-07-longbench-v2):** References ZeroSCROLLS as an earlier comprehensive evaluation effort in the long-context benchmarking lineage.
- **LongBench Pro (2026-01-longbench-pro):** References SCROLLS/ZeroSCROLLS as early efforts in long-context evaluation that later benchmarks build upon.
- **SCROLLS (2022-12-scrolls-long-language-sequences):** ZeroSCROLLS is the direct zero-shot successor, adapting 6 of SCROLLS's 7 tasks (dropping ContractNLI) and adding 4 new datasets.
