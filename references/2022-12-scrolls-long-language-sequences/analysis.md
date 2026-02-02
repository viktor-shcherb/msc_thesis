# SCROLLS: Standardized CompaRison Over Long Language Sequences

**Authors:** Uri Shaham, Elad Segal, Maor Ivgi, Avia Efrat, Ori Yoran, Adi Haviv, Ankit Gupta, Wenhan Xiong, Mor Geva, Jonathan Berant, Omer Levy (Tel Aviv University, Allen Institute for AI, IBM Research, Meta AI)
**Date:** December 2022, EMNLP 2022 (arXiv:2201.03533)

---

## Core Research Problem

Standard NLP benchmarks such as GLUE (Wang et al., 2018, 2019), SQuAD (Rajpurkar et al., 2016, 2018), and WMT (Barrault et al., 2019, 2020) focus on short texts -- sentences and paragraphs -- even though long texts (books, articles, meeting transcripts) comprise a large portion of natural language. The emergence of efficient transformer architectures designed for long sequences (Tay et al., 2020b; Fournier et al., 2021) has not been accompanied by a standard evaluation scheme for long natural language problems.

Existing evaluation approaches are inadequate:
1. **Language modeling perplexity** mostly captures local, short-range patterns (Khandelwal et al., 2018; Sun et al., 2021), and masking distant tokens can actually improve perplexity (Press et al., 2021a,b).
2. **Long Range Arena (LRA)** (Tay et al., 2021) contains only two natural language tasks (sentiment analysis and document relatedness), uses byte tokenization to artificially inflate sequence length, and truncates at 4,000 bytes (~1,000 words).
3. **Summarization-only evaluation** biases toward academic domains (arXiv, PubMed).

**The core challenge is how to establish a standardized, multi-task benchmark for evaluating long-text understanding across diverse domains and task types.**

---

## Problem Solutions

SCROLLS provides a curated suite of 7 datasets requiring reasoning over naturally long texts, covering multiple task types and domains.

1. **Naturally long texts.** All datasets contain inputs that are organically long (thousands of words), not artificially elongated via byte tokenization.
2. **Information synthesis across distance.** Datasets are selected to prioritize tasks where critical information is spread across multiple parts of the input, not concentrated in one location.
3. **Unified text-to-text format.** All datasets are converted to a single sequence-to-sequence format, enabling evaluation of a single model across all tasks.

---

## Approach Details

### Method

SCROLLS curates 7 existing long-text datasets, cleans them, and reformats them into a unified text-to-text input-output format. The benchmark covers three task types: summarization, question answering, and natural language inference, across domains including government reports, TV shows, meeting transcripts, scientific articles, literature, and legal contracts.

### Datasets

| Dataset | Task | Domain | Metric | Avg #Words (Input) | #Examples |
|---|---|---|---|---|---|
| GovReport (Huang et al., 2021) | Summarization | Government | ROUGE | 7,886 | 19,402 |
| SummScreenFD (Chen et al., 2021) | Summarization | TV | ROUGE | 5,598 | 4,348 |
| QMSum (Zhong et al., 2021) | Query-Based Summarization | Meetings | ROUGE | 9,497 | 1,810 |
| Qasper (Dasigi et al., 2021) | QA | Science | F1 | 3,629 | 5,692 |
| NarrativeQA (Kocisky et al., 2018) | QA | Literature, Film | F1 | 51,653 | 71,187 |
| QuALITY (Pang et al., 2021) | Multiple-Choice QA | Literature, Misc | EM | 4,193 | 6,737 |
| ContractNLI (Koreeda and Manning, 2021) | NLI | Legal | EM | 1,706 | 10,319 |

### Key Technical Components

**Dataset curation criteria.** Datasets were selected based on: (1) texts being naturally long, not artificially inflated; (2) tasks requiring synthesis of information from multiple distant parts of the input; (3) diversity of task types and domains.

**Data cleansing.** GovReport: removed 64 examples where report length was <2x or >1000x the summary length, or where the summary appeared verbatim. Qasper: removed 176 questions over 63 papers with <8,192 characters. NarrativeQA: stripped excess metadata (licenses, HTML headers).

**Unified format.** All datasets reformulated as sequence-to-sequence tasks. Queries prepended to text with two newlines as separator. Multiple-choice options provided as part of the query. Multiple target outputs split into separate training instances; at test time, maximum score over all valid answers.

**Evaluation metrics.** ROUGE (geometric mean of ROUGE-1/2/L) for summarization, F1 (unigram overlap with stopword removal) for QA, exact match (EM) for classification/multiple-choice. A single aggregate SCROLLS score is the average across all datasets.

**Spread analysis.** The authors quantify how far apart relevant information is in the input by computing the standard deviation of output bigram positions in the input. SCROLLS datasets show spread hundreds to thousands of words apart, compared to under 5 words for SQuAD and Natural Questions.

### Experimental Setup

**Baselines:**
- **BART-base** (Lewis et al., 2020): Standard transformer encoder-decoder, max input 1,024 tokens, also tested at 256 and 512 tokens.
- **LED-base** (Beltagy et al., 2020): Longformer Encoder-Decoder with sliding-window attention (window 1,024), max input 16,384 tokens, also tested at 1,024 and 4,096. Initialized from BART parameters without long-text pretraining.
- **Naive heuristics:** Fixed-length prefix (proportional to average output/input ratio), majority class for classification tasks.

**Training:** AdamW with beta=(0.9, 0.98), epsilon=1e-6, fp16, gradient checkpointing. Effective batch size 131,072 tokens across 8 NVIDIA V100 32GB GPUs. Summarization trained 10 epochs, QA/NLI 20 epochs, NarrativeQA 2 epochs. Learning rate tuned from {1e-5, 2e-5, 5e-5, 1e-4, 2e-4, 5e-4}. Linear warmup (10%) then linear decay.

### Key Results

| Model (Input) | GovReport | SummScreenFD | QMSum | Qasper | NarrativeQA | QuALITY (EM-T/H) | ContractNLI | Avg |
|---|---|---|---|---|---|---|---|---|
| Naive | 26.5 | 9.8 | 7.7 | 3.4 | 1.5 | 25.2 / 26.1 | 66.0 | 19.35 |
| BART (1024) | 28.5 | 15.3 | 19.1 | 26.3 | 15.4 | 26.0 / 25.9 | 77.4 | 29.01 |
| LED (16384) | 36.0 | 13.8 | 16.3 | 26.6 | 18.5 | 25.8 / 25.4 | 71.5 | 29.16 |

- **More context improves performance.** Both BART (256 -> 1024 tokens: +2.66 points) and LED (1024 -> 16384: +2.1 points) improve with longer inputs, confirming that the tasks benefit from processing more of the document.
- **BART nearly matches LED despite 16x shorter input.** BART (1024 tokens) scores 29.01 vs LED (16384) at 29.16 -- only 0.15 points difference. When controlling for input length, BART outperforms LED by ~2 points, suggesting LED is under-optimized without long-text pretraining.
- **LED benefits most on the largest datasets.** LED (16k) significantly outperforms BART (1k) only on GovReport and NarrativeQA, the two largest datasets, suggesting that adapting sliding-window attention requires substantial fine-tuning data.
- **Large gap to human performance.** Human agreement on Qasper is 60.9% F1 (vs. 26.6% best baseline), QuALITY 93.5% EM (vs. 26.8%), NarrativeQA 58.7% F1 (vs. 18.5%).

### Limitations

1. **ROUGE limitations for summarization.** ROUGE only measures ngram overlap and penalizes valid paraphrases. Model-based evaluation may be needed.
2. **English only.** SCROLLS is monolingual, limiting applicability to other languages.
3. **No zero-shot evaluation.** SCROLLS requires task-specific fine-tuning, which was addressed by the follow-up ZeroSCROLLS benchmark.

---

## Conclusions

1. **First standardized long-text NLP benchmark.** SCROLLS fills the gap between short-text benchmarks (GLUE, SQuAD) and the growing capabilities of efficient transformer architectures by providing 7 diverse tasks with naturally long inputs (thousands to tens of thousands of words).

2. **Information is spread across long distances.** Quantitative spread analysis confirms that SCROLLS tasks require fusing information separated by hundreds to thousands of words, unlike short-text benchmarks where answer bigrams cluster within 5 words.

3. **Efficient architectures need long-text pretraining.** LED achieves only marginal gains over BART despite 16x longer input, suggesting that architectural efficiency alone is insufficient -- models also need long-text pretraining or substantially more fine-tuning data.

4. **Substantial room for improvement.** The gap between baseline models (avg ~29) and estimated human performance (60--93% on individual tasks) is large, challenging the community to develop better approaches for long-text understanding.

5. **Unified evaluation platform.** By providing a single aggregate score, live leaderboard, and standardized format, SCROLLS enables systematic comparison of diverse approaches: new architectures, pretraining schemes, and retrieval-based methods.

---

## Core References and Why They Are Referenced

### Short-Text Benchmarks (Motivation)

- **Wang et al. (2018; 2019)** -- *GLUE / SuperGLUE.* The canonical short-text NLP benchmarks that SCROLLS extends to long sequences. SCROLLS mirrors their design philosophy (multi-task, unified format, aggregate score, live leaderboard).
- **Rajpurkar et al. (2016; 2018)** -- *SQuAD / SQuAD 2.0.* Standard short-text QA benchmarks used as comparison points for SCROLLS's spread analysis, where SQuAD bigrams cluster within 5 words vs. hundreds in SCROLLS.

### Long-Text Evaluation (Prior Work)

- **Tay et al. (2021)** -- *Long Range Arena (LRA).* The most prominent prior long-sequence benchmark. SCROLLS critiques LRA for having only two natural language tasks, using byte tokenization, and truncating at ~1,000 words.
- **Cohan et al. (2018)** -- *arXiv/PubMed Summarization.* Popular long-document summarization datasets that bias evaluation toward academic domains. SCROLLS's spread analysis shows its tasks require fusing more distant information than arXiv.

### Component Datasets

- **Huang et al. (2021)** -- *GovReport.* Government report summarization with the longest documents in SCROLLS (avg 7,886 words). The spread analysis methodology for SCROLLS is inspired by Huang et al.'s bigram statistics.
- **Chen et al. (2021)** -- *SummScreenFD.* TV episode transcript summarization requiring synthesis across scattered dialogue snippets.
- **Zhong et al. (2021)** -- *QMSum.* Query-based meeting transcript summarization with answers spanning 200+ words or 10+ turns.
- **Dasigi et al. (2021)** -- *Qasper.* Scientific paper QA where inter-annotator F1 is 60.9%, more than double the best baseline.
- **Kocisky et al. (2018)** -- *NarrativeQA.* Book/script QA with the longest inputs in SCROLLS (avg 51,653 words).
- **Pang et al. (2021)** -- *QuALITY.* Multiple-choice QA over stories with 50% hard questions; human agreement 93.5% EM.
- **Koreeda and Manning (2021)** -- *ContractNLI.* Legal NLI over non-disclosure agreements.

### Baseline Models

- **Lewis et al. (2020)** -- *BART.* Standard transformer encoder-decoder used as the short-context baseline. Surprisingly competitive with LED despite 16x shorter input.
- **Beltagy et al. (2020)** -- *Longformer / LED.* Efficient transformer with sliding-window attention. LED is initialized from BART without long-text pretraining, which SCROLLS shows is a key limitation.

#### Cross-References in Available Papers

- **BABILong (2024-12-babilong-long-context-reasoning):** Contrasts with SCROLLS's lack of controllable sequence length and reliance on parametric knowledge. BABILong addresses SCROLLS's limitation of being capped at ~50K tokens by providing tasks scalable to 10M tokens.
- **RULER (2024-10-ruler-context-size):** References ZeroSCROLLS (the zero-shot successor to SCROLLS) as a realistic but uncontrollable long-context benchmark.
- **PI (2023-06-pi-positional-interpolation):** Uses SCROLLS leaderboard results for GovReport summarization comparison.
- **LongBench v2 (2025-07-longbench-v2):** References ZeroSCROLLS as an earlier comprehensive evaluation effort.
- **LongBench Pro (2026-01-longbench-pro):** References SCROLLS/ZeroSCROLLS as early efforts in long-context evaluation.
