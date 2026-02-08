---
title: "SCROLLS: Standardized CompaRison Over Long Language Sequences"
authors: "Shaham, Segal, Ivgi, Efrat, Yoran, Haviv, Gupta, Xiong, Geva, Berant, Levy"
year: 2022
venue: "EMNLP 2022"
paper_type: conference-paper
categories: ["benchmarking", "long-context-evaluation"]
scope: ["long-document NLP tasks", "fine-tuning evaluation", "benchmark design"]
benchmarks_used: ["scrolls"]
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "SCROLLS tasks require synthesizing information spread across hundreds to thousands of words, unlike short-text benchmarks where answer bigrams cluster within 5 words"
    evidence: "Section 4, Figure 4"
    status: supported
    scope: "7 English-language datasets, bigram-based spread metric, comparison against SQuAD/Natural Questions/CNN-DM/arXiv"
    magnitude: "output bigram spread of hundreds to thousands of words (std dev) vs under 5 words for SQuAD/NQ; 1.5x-2x greater spread than arXiv for summarization"
  - id: C2
    claim: "More context improves performance: BART gains +2.66 avg points (256->1024 tokens) and LED gains +2.1 avg points (1024->16384 tokens)"
    evidence: "Table 2, Section 5.2"
    status: supported
    scope: "BART-base and LED-base, 7 SCROLLS tasks, fine-tuning evaluation, greedy decoding"
    magnitude: "BART: +2.66 avg points (26.35->29.01); LED: +2.1 avg points (27.06->29.16)"
  - id: C3
    claim: "BART (1024 tokens) nearly matches LED (16384 tokens) despite 16x shorter input, scoring 29.01 vs 29.16 average"
    evidence: "Table 2, Section 5.2"
    status: supported
    scope: "BART-base vs LED-base, 7 SCROLLS tasks, fine-tuning evaluation, greedy decoding"
    magnitude: "0.15 avg point difference (29.01 vs 29.16)"
  - id: C4
    claim: "LED is under-optimized without long-text pretraining; at matched input length (1024 tokens), BART outperforms LED by almost 2 points"
    evidence: "Table 2, Section 5.2: BART 1024 avg 29.01 vs LED 1024 avg 27.06"
    status: supported
    scope: "BART-base vs LED-base at 1024 tokens, 7 SCROLLS tasks, LED initialized from BART without long-text pretraining"
    magnitude: "~2 avg point gap (29.01 vs 27.06); LED significantly outperforms BART only on 2 largest datasets (GovReport, NarrativeQA)"
  - id: C5
    claim: "Large gap between baseline performance (~29 avg) and estimated human performance: Qasper inter-annotator 60.9% F1 vs best 26.6%, QuALITY human agreement 93.5% EM vs best 26.8%, NarrativeQA inter-annotator 58.7% F1 vs best 18.5%"
    evidence: "Section 5.2"
    status: supported
    scope: "3 QA datasets with available human performance estimates (Qasper, QuALITY, NarrativeQA); no human ceiling for summarization tasks"
    magnitude: "Qasper: 60.9% vs 26.6% F1; QuALITY: 93.5% vs 26.8% EM; NarrativeQA: ~58.7% vs 18.5% F1"
  - id: C6
    claim: "Language modeling perplexity is an inadequate metric for evaluating long-range modeling ability because next-token prediction mostly captures local short-range patterns"
    evidence: "Section 2, citing Khandelwal et al. (2018) and Sun et al. (2021)"
    status: supported
    scope: "general argument based on prior empirical findings, not directly tested in this paper"
    magnitude: "qualitative"
cross_references:
  - target: 2021-05-long-range-arena
    type: complementary
    detail: "SCROLLS critiques LRA for having only 2 NL tasks, using byte tokenization to inflate sequence length, and truncating at ~1000 words"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: extended-by
    detail: "ZeroSCROLLS extends SCROLLS to zero-shot evaluation, adapting 6 of 7 tasks and adding 4 new ones"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "LED (Longformer Encoder-Decoder) is one of the two baseline models evaluated on SCROLLS"
  - target: 2024-08-longbench-bilingual-benchmark
    type: complementary
    detail: "LongBench argues SCROLLS covers a restricted range of task types"
  - target: 2026-01-longbench-pro
    type: complementary
    detail: "LongBench Pro references SCROLLS as an early effort in long-context evaluation"
  - target: 2024-08-l-eval-standardized-evaluation
    type: extended-by
    detail: "L-Eval addresses SCROLLS limitations with manual sample filtering, metric-human correlation analysis, and more closed-ended tasks"
  - target: 2018-07-sharp-nearby-fuzzy-far-away
    type: complementary
    detail: "Khandelwal et al.'s finding that LM perplexity mostly captures local short-range patterns is cited to motivate SCROLLS's argument that task-based evaluation is needed for long-context abilities"
  - target: 2024-06-ada-leval-length-adaptable-benchmark
    type: complementary
    detail: "Ada-LEval addresses SCROLLS's fixed-length limitation and lack of ultra-long settings with length-adaptable tasks"
open_questions:
  - question: "Can model-based evaluation replace or complement ROUGE for long-text summarization?"
    addressed_by: null
  - question: "Can SCROLLS be extended to multilingual settings?"
    addressed_by: null
  - question: "Does LED's underperformance relative to BART at matched input length stem from lack of long-text pretraining or fundamental architectural limitations?"
    addressed_by: null
  - question: "Do zero-shot and few-shot models perform better on SCROLLS tasks than fine-tuned baselines?"
    addressed_by: 2023-12-zeroscrolls-zero-shot-long-text
---
# SCROLLS: Standardized CompaRison Over Long Language Sequences

**Authors:** Uri Shaham, Elad Segal, Maor Ivgi, Avia Efrat, Ori Yoran, Adi Haviv, Ankit Gupta, Wenhan Xiong, Mor Geva, Jonathan Berant, Omer Levy (Tel Aviv University, Allen Institute for AI, IBM Research, Meta AI)
**Date:** December 2022, EMNLP 2022; arXiv:2201.03533

---

## Core Research Problem

Standard NLP benchmarks such as GLUE (Wang et al., 2018, 2019), SQuAD (Rajpurkar et al., 2016, 2018), and WMT (Barrault et al., 2019, 2020) focus on short texts -- sentences and paragraphs -- even though long texts (books, articles, meeting transcripts) comprise a large portion of natural language (Section 1). The emergence of efficient transformer architectures designed for long sequences (Tay et al., 2020b; Fournier et al., 2021) has not been accompanied by a standard evaluation scheme for long natural language problems.

Existing evaluation approaches are inadequate in three ways:

1. **Language modeling perplexity** mostly captures local, short-range patterns (Khandelwal et al., 2018; Sun et al., 2021), and masking or down-weighting distant tokens can actually *improve* perplexity (Press et al., 2021a,b) (Section 2).
2. **Long Range Arena (LRA)** (Tay et al., 2021) contains only two natural language tasks (sentiment analysis and document relatedness), uses byte tokenization to artificially inflate sequence length, and truncates at 4,000 bytes (~1,000 words), exempting models from coping with naturally long texts (Section 2).
3. **Summarization-only evaluation** biases toward academic domains (arXiv, PubMed) and covers only one task type (Section 2).

**The core challenge is how to establish a standardized, multi-task benchmark for evaluating long-text understanding across diverse domains and task types, where inputs are naturally long and tasks require synthesizing information spread across the document.**

---

## Problem Solutions

SCROLLS provides a curated suite of 7 datasets requiring reasoning over naturally long texts, covering multiple task types and domains.

1. **Naturally long texts.** All datasets contain inputs that are organically long (thousands of words), not artificially elongated via byte tokenization (Section 3).
2. **Information synthesis across distance.** Datasets are selected to prioritize tasks where critical information is spread across multiple parts of the input, not concentrated in one location (Section 3, Figure 2, Figure 3).
3. **Unified text-to-text format.** All datasets are converted to a single sequence-to-sequence format, enabling evaluation of a single model across all tasks (Section 3.2).
4. **Single aggregate score and live leaderboard.** A single SCROLLS score (average across datasets) and website with private test sets enable systematic comparison (Section 3.3).

---

## Approach Details

### Method

SCROLLS curates 7 existing long-text datasets, cleans them, and reformats them into a unified text-to-text input-output format. The benchmark covers three task types: summarization, question answering, and natural language inference, across domains including government reports, TV shows, meeting transcripts, scientific articles, literature, and legal contracts (Section 3).

### Key Technical Components

**Datasets (Table 1):**

| Dataset | Task | Domain | Metric | Avg #Words (In) | Avg #Words (Out) | #Examples |
|---|---|---|---|---|---|---|
| GovReport (Huang et al., 2021) | Summarization | Government | ROUGE | 7,886 | 492.5 | 19,402 |
| SummScreenFD (Chen et al., 2021) | Summarization | TV | ROUGE | 5,598 | 99.6 | 4,348 |
| QMSum (Zhong et al., 2021) | Query-Based Summ | Meetings | ROUGE | 9,497 | 69.7 | 1,810 |
| Qasper (Dasigi et al., 2021) | QA | Science | F1 | 3,629 | 11.4 | 5,692 |
| NarrativeQA (Kocisky et al., 2018) | QA | Literature, Film | F1 | 51,653 | 4.6 | 71,187 |
| QuALITY (Pang et al., 2021) | Multiple-Choice QA | Literature, Misc | EM | 4,193 | 10.3 | 6,737 |
| ContractNLI (Koreeda and Manning, 2021) | NLI | Legal | EM | 1,706 | 1.4 | 10,319 |

Notable dataset characteristics:
- **NarrativeQA** has the longest inputs (avg 51,653 words) from books and movie scripts, with ~30 questions per each of 1,567 books/scripts (Section 3.1).
- **QuALITY** has 50% of questions labeled as *hard* via a speed validation process where annotators given limited time chose the wrong answer (Section 3.1).
- **ContractNLI** uses 607 contracts combined with 17 unique hypotheses to produce 10,319 examples, predicting entailment, not entailed (neutral), or contradiction (Section 3.1).
- **Qasper** contains abstractive, extractive, yes/no, and unanswerable questions over NLP papers (Section 3.1).

**Dataset curation criteria (Section 3).** Datasets were selected based on: (1) texts being naturally long, not artificially inflated; (2) tasks requiring synthesis of information from multiple distant parts of the input; (3) diversity of task types and domains.

**Data cleansing (Section 3.2).** GovReport: removed 64 examples where report length was <2x or >1000x the summary length, or where the summary appeared verbatim. Qasper: removed 176 questions over 63 papers with <8,192 characters. NarrativeQA: stripped excess metadata (licenses, HTML headers).

**Unified format (Section 3.2).** All datasets reformulated as sequence-to-sequence tasks. Queries prepended to text with two newlines as separator. Multiple-choice options provided as part of the query. Multiple target outputs split into separate training instances; at test time, maximum score over all valid answers.

**Evaluation metrics (Section 3.3).** ROUGE (geometric mean of ROUGE-1/2/L) for summarization, F1 (unigram overlap with stopword removal) for QA, exact match (EM) for classification/multiple-choice. The aggregate SCROLLS score is the average across all 7 datasets' individual scores. For QuALITY, only EM over the full test set (EM-T) is used for the SCROLLS score, though EM over the hard subset (EM-H) is also reported.

**Spread analysis (Section 4).** The authors quantify how far apart relevant information is by computing the standard deviation of output bigram positions in the input. For each input-output pair, they represent the output as a set of bigrams, locate each bigram's first occurrence in the input, and compute the standard deviation of these positions. SCROLLS datasets show spread of hundreds to thousands of words, compared to under 5 words for SQuAD and Natural Questions (Figure 4). SCROLLS summarization datasets show 1.5x to 2x greater spread than arXiv on average (Section 4).

### Experimental Setup

**Baselines (Section 5.1):**
- **BART-base** (Lewis et al., 2020): Standard transformer encoder-decoder, pretrained on sequences up to 1,024 tokens. Inputs truncated to prefix of 256, 512, or 1,024 tokens.
- **LED-base** (Beltagy et al., 2020): Longformer Encoder-Decoder with sliding-window attention (window 1,024 tokens), global attention only for the first token (summarization setting throughout all tasks). Initialized from BART parameters without long-text pretraining. Maximum input lengths of 1,024, 4,096, or 16,384 tokens.
- **Naive heuristics:** Fixed-length prefix proportional to average output/input length ratio for most tasks. Majority class for QuALITY (just above 25%). Per-hypothesis majority class for ContractNLI (same 17 hypotheses shared across all documents).

**Training (Appendix D):** AdamW with beta=(0.9, 0.98), epsilon=1e-6, fp16, gradient checkpointing. Effective batch size 131,072 (2^17) tokens, processing 16,384 tokens per GPU across 8 NVIDIA V100 32GB GPUs. Summarization: 10 epochs; Qasper, QuALITY, ContractNLI: 20 epochs; NarrativeQA: 2 epochs. Learning rate tuned from {1e-5, 2e-5, 5e-5, 1e-4, 2e-4, 5e-4}. Linear warmup (10%) then linear decay to zero. Dropout of 0.1 throughout. Greedy decoding at inference.

### Key Results

**Baseline results (Table 2):**

| Model (Input) | GovReport R-1/2/L | SummScreen R-1/2/L | QMSum R-1/2/L | Qasper F1 | NarQA F1 | QuALITY EM-T/H | CNLI EM | Avg |
|---|---|---|---|---|---|---|---|---|
| Naive | 45.3 / 17.9 / 20.8 | 19.6 / 1.8 / 11.0 | 14.2 / 2.0 / 9.3 | 3.4 | 1.5 | 25.2 / 26.1 | 66.0 | 19.35 |
| BART (256) | 41.9 / 14.2 / 20.3 | 24.5 / 3.8 / 15.3 | 29.9 / 8.3 / 20.4 | 23.3 | 14.0 | 26.0 / 25.8 | 69.8 | 26.35 |
| BART (512) | 45.6 / 16.9 / 21.8 | 26.3 / 5.1 / 16.2 | 29.5 / 8.2 / 20.1 | 24.7 | 14.5 | 26.8 / 27.4 | 71.6 | 27.58 |
| BART (1024) | 47.9 / 18.6 / 22.7 | 27.2 / 4.9 / 16.7 | 30.2 / 8.7 / 20.7 | 26.3 | 15.4 | 26.0 / 25.9 | 77.4 | 29.01 |
| LED (1024) | 40.9 / 16.1 / 23.1 | 22.7 / 3.6 / 15.1 | 24.6 / 6.5 / 19.0 | 24.4 | 15.2 | 26.6 / 27.2 | 73.4 | 27.06 |
| LED (4096) | 52.5 / 23.3 / 26.8 | 23.0 / 4.1 / 15.1 | 26.6 / 6.9 / 19.9 | 25.0 | 16.3 | 26.6 / 27.3 | 71.5 | 28.30 |
| LED (16384) | 56.2 / 26.6 / 28.8 | 24.2 / 4.5 / 15.4 | 25.1 / 6.7 / 18.8 | 26.6 | 18.5 | 25.8 / 25.4 | 71.5 | 29.16 |

- **More context improves performance.** BART improves by +2.66 avg points from 256 to 1024 tokens (26.35 -> 29.01). LED improves by +2.1 avg points from 1024 to 16384 tokens (27.06 -> 29.16). This trend is relatively consistent across datasets for BART, but less so for LED (e.g., QMSum and ContractNLI) (Section 5.2).
- **BART nearly matches LED despite 16x shorter input.** BART (1024 tokens) scores 29.01 vs LED (16384 tokens) at 29.16 -- only 0.15 points difference. When controlling for input length (1024 tokens), BART outperforms LED by almost 2 points (29.01 vs 27.06), suggesting LED is under-optimized without long-text pretraining (Section 5.2).
- **LED benefits most on the largest datasets.** LED (16384) significantly outperforms BART (1024) only on GovReport (ROUGE-1: 56.2 vs 47.9) and NarrativeQA (F1: 18.5 vs 15.4), which are the two largest datasets in SCROLLS by number of examples. The authors suggest that since LED is initialized from BART without long-text pretraining, it requires substantial data and fine-tuning to adapt its parameters to sliding-window attention (Section 5.2).
- **Large gap to human performance.** Qasper inter-annotator agreement: 60.9% F1 vs best baseline 26.6% F1. QuALITY human agreement: 93.5% EM vs best baseline 26.8% EM. NarrativeQA inter-annotator agreement: ~58.7% F1 vs best baseline 18.5% F1 (Section 5.2).
- **Naive GovReport baseline is surprisingly strong.** The prefix heuristic achieves ROUGE-1 of 45.3 on GovReport, outperforming BART (256) at 41.9, because government report summaries tend to draw heavily from the document's introduction (Table 2).

---

## Limitations and Failure Modes

The paper includes a dedicated limitations section (Section 7):

1. **ROUGE limitations for summarization evaluation.** ROUGE only accounts for n-gram overlaps and may downvalue valid paraphrases of the reference summary. The authors acknowledge that "establishing unbiased, automated metrics for long generations that correlate well with human judgments is an emerging field of research" and that they may "replace or complement ROUGE with model-based evaluation in the future" (Section 7).

2. **English only.** SCROLLS is monolingual, limiting applicability to languages other than English (Section 7).

3. **Fine-tuning required.** SCROLLS requires task-specific fine-tuning, which limits evaluation of zero-shot and few-shot capabilities. This limitation was directly addressed by the follow-up ZeroSCROLLS benchmark (Shaham et al., 2023).

4. **LED baseline lacks long-text pretraining.** LED is initialized from BART parameters without further pretraining on long texts, which the results suggest is a key limitation. The near-parity between BART (1024) and LED (16384) may reflect LED's under-optimization rather than the intrinsic difficulty of the tasks (Section 5.2).

5. **No established human performance ceiling.** While inter-annotator agreement provides estimates for some datasets (Qasper, QuALITY, NarrativeQA), "it is difficult to establish an accurate human performance ceiling on SCROLLS, especially when considering the summarization datasets" (Section 5.2).

6. **Spread analysis limitations.** The bigram-based spread metric (Section 4) measures positional dispersion of output n-grams in the input, but cannot capture semantic dependencies that do not manifest as shared surface forms, particularly for abstractive outputs.

#### Scope and Comparability

- **What was not tested:** No decoder-only models (e.g., GPT-style) were evaluated. No retrieval-augmented baselines were tested. No models with long-text pretraining (e.g., LongT5, BigBird with pretraining) were included. Only base-sized models were evaluated; no large-sized variants. No zero-shot or few-shot evaluation was conducted. No non-English languages were included.
- **Comparability notes:** LED-base is initialized from BART parameters without long-text pretraining, making it a weaker baseline than LED variants that underwent continued pretraining on long documents. The SCROLLS preprocessing (data cleansing, format unification) means results are **not directly comparable** to results reported on the original datasets (Appendix C, Table 4 explicitly notes this). The aggregate SCROLLS score averages across datasets of very different sizes, domains, and difficulty levels, which may mask per-task variation. Greedy decoding is used throughout, which may understate model capabilities relative to beam search or sampling.

---

## Conclusions

### Contributions

1. **First standardized multi-task long-text NLP benchmark.** SCROLLS fills the gap between short-text benchmarks (GLUE, SQuAD) and the growing capabilities of efficient transformer architectures by providing 7 diverse tasks with naturally long inputs ranging from 1,706 to 51,653 average words (Table 1, Section 1).

2. **Quantitative evidence of information spread.** The bigram spread analysis demonstrates that SCROLLS tasks require fusing information separated by hundreds to thousands of words, unlike short-text benchmarks where answer bigrams cluster within 5 words (Section 4, Figure 4).

3. **Revealed the importance of long-text pretraining.** LED achieves only marginal gains over BART despite 16x longer input (29.16 vs 29.01), demonstrating that architectural efficiency alone is insufficient -- models also need long-text pretraining or substantially more fine-tuning data (Table 2, Section 5.2).

4. **Unified evaluation platform.** By providing a single aggregate score, live leaderboard, standardized text-to-text format, and private test sets, SCROLLS enables systematic comparison of diverse approaches: new architectures, pretraining schemes, and retrieval-based methods (Section 1, Section 3.3).

### Implications

1. **Efficient architectures need more than efficiency.** The finding that BART nearly matches LED despite processing only ~6% of the input suggests that measuring whether an architecture can *effectively* model long-range semantics is as important as measuring whether it can *efficiently* process long sequences -- a distinction SCROLLS is designed to test (Section 5.2).

2. **Benchmark design influences research direction.** The paper argues that prior evaluation practices (perplexity, LRA, summarization-only) biased research toward local pattern modeling. By providing naturally long texts with verified information spread, SCROLLS redirects attention toward genuine long-range reasoning (Section 2, Section 4).

3. **Large headroom for improvement.** The gap between baseline models (~29 avg) and estimated human performance (60--93% on individual tasks) suggests that long-text understanding remained a major open challenge at the time of publication (Section 5.2).

---

## Key Claims

1. **C1: SCROLLS tasks require synthesizing information spread across hundreds to thousands of words.** The spread analysis shows output bigrams in SCROLLS are dispersed across standard deviations of hundreds to thousands of words, compared to under 5 words for SQuAD and Natural Questions. SCROLLS summarization tasks show 1.5x--2x greater spread than arXiv. Evidence: Section 4, Figure 4. Status: **supported**.

2. **C2: More context improves performance.** BART improves by +2.66 avg points from 256 to 1024 tokens; LED improves by +2.1 avg points from 1024 to 16384 tokens. The trend is consistent across datasets for BART but less so for LED. Evidence: Table 2, Section 5.2. Status: **supported**.

3. **C3: BART (1024 tokens) nearly matches LED (16384 tokens) despite 16x shorter input.** BART scores 29.01 vs LED at 29.16 -- only 0.15 points difference. Evidence: Table 2, Section 5.2. Status: **supported**.

4. **C4: LED is under-optimized without long-text pretraining.** At matched input length (1024 tokens), BART outperforms LED by almost 2 points (29.01 vs 27.06). LED significantly outperforms BART only on the two largest datasets (GovReport and NarrativeQA), suggesting it needs substantial fine-tuning data to adapt to sliding-window attention. Evidence: Table 2, Section 5.2. Status: **supported**.

5. **C5: Large gap between baselines and estimated human performance.** Qasper inter-annotator 60.9% F1 vs best baseline 26.6%; QuALITY human agreement 93.5% EM vs best 26.8%; NarrativeQA inter-annotator ~58.7% F1 vs best 18.5%. Evidence: Section 5.2. Status: **supported**.

6. **C6: Language modeling perplexity is inadequate for evaluating long-range modeling.** Perplexity mostly captures sensitivity to local, short-range patterns, and masking distant tokens can actually improve perplexity. Evidence: Section 2, citing Khandelwal et al. (2018), Sun et al. (2021), Press et al. (2021a,b). Status: **supported**.

---

## Open Questions

1. **Can model-based evaluation replace or complement ROUGE for long-text summarization?** The authors acknowledge ROUGE's limitations for evaluating long generations and suggest they may adopt model-based evaluation in the future (Section 7). **Unresolved** within the references directory.

2. **Can SCROLLS be extended to multilingual settings?** The paper notes SCROLLS is limited to English and identifies multilingual benchmarks as a natural future direction (Section 7). **Unresolved**.

3. **Does LED's underperformance stem from lack of long-text pretraining or fundamental architectural limitations?** The near-parity between BART (1024) and LED (16384) raises the question of whether long-text pretraining (not just long-context architecture) is the critical ingredient. The authors suggest pretraining is key but do not test this directly (Section 5.2). **Unresolved**.

4. **Do zero-shot and few-shot models perform better on SCROLLS tasks than fine-tuned baselines?** SCROLLS only evaluates fine-tuned models. **Addressed by** Shaham et al. (2023) -- *ZeroSCROLLS*, which adapts SCROLLS to zero-shot evaluation.

---

## Core References and Why They Are Referenced

### Short-Text Benchmarks (Motivation)

- **Wang et al. (2018; 2019)** -- *GLUE / SuperGLUE.* The canonical short-text NLP benchmarks that SCROLLS extends to long sequences. SCROLLS mirrors their design philosophy (multi-task, unified format, aggregate score, live leaderboard).
- **Rajpurkar et al. (2016; 2018)** -- *SQuAD / SQuAD 2.0.* Standard short-text QA benchmarks used as comparison points for SCROLLS's spread analysis, where SQuAD bigrams cluster within 5 words vs. hundreds in SCROLLS.

### Long-Text Evaluation (Prior Work)

- **Tay et al. (2021)** -- *Long Range Arena (LRA).* The most prominent prior long-sequence benchmark. SCROLLS critiques LRA for having only two natural language tasks, using byte tokenization, and truncating at ~1,000 words (Section 2).
- **Cohan et al. (2018)** -- *arXiv/PubMed Summarization.* Popular long-document summarization datasets that bias evaluation toward academic domains. SCROLLS's spread analysis shows its tasks require fusing information 1.5--2x more dispersed than arXiv (Section 4).
- **Khandelwal et al. (2018)** -- *Sharp Nearby, Fuzzy Far Away.* Shows that neural language models use primarily local context for next-token prediction, motivating SCROLLS's argument that perplexity is inadequate for evaluating long-range abilities (Section 2).

### Component Datasets

- **Huang et al. (2021)** -- *GovReport.* Government report summarization with the longest documents in SCROLLS after NarrativeQA (avg 7,886 words, avg summary 492.5 words). The bigram spread methodology for SCROLLS is inspired by Huang et al.'s analysis.
- **Chen et al. (2021)** -- *SummScreenFD.* TV episode transcript summarization requiring synthesis across scattered dialogue snippets from 88 different TV shows.
- **Zhong et al. (2021)** -- *QMSum.* Query-based meeting transcript summarization where annotators ensured relevant text spans at least 200 words or 10 turns.
- **Dasigi et al. (2021)** -- *Qasper.* Scientific paper QA where inter-annotator F1 is 60.9%, more than double the best baseline (26.6%).
- **Kocisky et al. (2018)** -- *NarrativeQA.* Book/script QA with the longest inputs in SCROLLS (avg 51,653 words), with ~30 questions per each of 1,567 books/scripts.
- **Pang et al. (2021)** -- *QuALITY.* Multiple-choice QA with a speed validation process; 50% of questions are labeled as hard. Human agreement is 93.5% EM.
- **Koreeda and Manning (2021)** -- *ContractNLI.* Legal NLI over 607 non-disclosure agreements with 17 unique hypotheses.

### Baseline Models

- **Lewis et al. (2020)** -- *BART.* Standard transformer encoder-decoder used as the short-context baseline (max 1024 tokens). Surprisingly competitive with LED despite 16x shorter input.
- **Beltagy et al. (2020)** -- *Longformer / LED.* Efficient transformer with sliding-window attention. LED is initialized from BART without long-text pretraining, which SCROLLS demonstrates as a key limitation.
