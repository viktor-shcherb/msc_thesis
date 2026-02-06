---
title: "L-Eval: Instituting Standardized Evaluation for Long Context Language Models"
authors: "An, Gong, Zhong, Zhao, Li, Zhang, Kong, Qiu"
year: 2024
venue: "ACL 2024"
paper_type: conference-paper
categories: ["benchmarking", "long-context-evaluation"]
scope: ["standardized long-context evaluation", "evaluation metrics for LCLMs", "open-source vs commercial LCLM comparison"]
benchmarks_used: ["l-eval"]
models_introduced: []
models_evaluated: ["gpt-4", "llama-7b", "llama-2-7b", "llama-2-13b", "mpt-7b"]
key_claims:
  - id: C1
    claim: "N-gram matching metrics (ROUGE-L, F-1) fail to correlate well with human judgment for LCLMs in zero-shot settings"
    evidence: "Figure 2, Section 4.1: without LIE, ROUGE-L achieves only ~0.5 Kendall-Tau with human scores"
    status: supported
  - id: C2
    claim: "Length-Instruction-Enhanced (LIE) evaluation substantially improves metric-human correlation: ROUGE-L Kendall-Tau from ~0.5 to ~0.8, GPT-4 judge from ~0.8 to 1.0"
    evidence: "Figure 2, Section 4.1"
    status: supported
  - id: C3
    claim: "GPT-4-32k achieves SOTA on L-Eval closed-ended tasks with 73.11% average, a ~20-point gap over the best open-source 16k model (Vicuna1.5-13b-16k at 43.46%)"
    evidence: "Table 3, Section 5.2"
    status: supported
  - id: C4
    claim: "Claude-100k surpasses GPT-4-32k on open-ended tasks (60.94% vs 54.16% GPT-4 judge win-rate) due to its longer context window"
    evidence: "Table 4, Section 5.2"
    status: supported
  - id: C5
    claim: "Scaled positional embeddings improve closed-ended task performance but degrade open-ended task performance, with extended-context models producing many invalid outputs on long inputs"
    evidence: "Table 3 vs Table 4, Figure 4, Section 5.2"
    status: supported
  - id: C6
    claim: "Full-context models outperform retrieval-based systems on closed-ended tasks (Turbo-16k 60.73% avg vs AdaEmb 49.73% and BM25 49.65%)"
    evidence: "Table 3, Section 5.2"
    status: supported
  - id: C7
    claim: "Increasing the NTK base from 20,000 to 160,000 continuously improves topic retrieval but degrades math reasoning (GSM-16-shot), revealing a retrieval-reasoning trade-off"
    evidence: "Figure 5, Section 5.2"
    status: supported
cross_references:
  - target: 2022-12-scrolls-long-language-sequences
    type: extends
    detail: "L-Eval addresses SCROLLS limitations: automatic filtering, reliance on n-gram metrics, and lack of closed-ended tasks"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: concurrent
    detail: "Concurrent zero-shot long-context benchmark; L-Eval differs by manually filtering samples and investigating metric-human correlation"
  - target: 2024-08-longbench-bilingual-benchmark
    type: concurrent
    detail: "Concurrent long-context benchmark at ACL 2024; L-Eval differentiates through manual sample curation and metric standardization"
  - target: 2024-06-ada-leval-length-adaptable-benchmark
    type: complementary
    detail: "Both provide length-aware evaluation; Ada-LEval controls input length while L-Eval standardizes evaluation metrics"
  - target: 2021-05-long-range-arena
    type: complementary
    detail: "LRA benchmarks efficient Transformers on synthetic classification; L-Eval targets generative LLMs on practical long-document tasks"
  - target: 2023-06-pi-positional-interpolation
    type: evaluates
    detail: "L-Eval evaluates PI-based models (Longchat, Vicuna1.5) and shows PI helps closed-ended but not open-ended tasks"
  - target: 2023-06-rope-ntk
    type: evaluates
    detail: "L-Eval evaluates NTK-aware scaling and reveals the retrieval-reasoning trade-off from increasing the NTK base"
  - target: 2022-04-alibi-train-short-test-long
    type: evaluates
    detail: "L-Eval evaluates MPT-7B-StoryWriter-65k which uses ALiBi; it achieves only 19.22% average on closed-ended tasks"
  - target: 2023-02-llama-open-efficient-foundation
    type: evaluates
    detail: "LLaMA serves as the base model for Vicuna, Longchat, and other evaluated LCLMs"
  - target: 2023-07-llama-2-open-foundation-chat
    type: evaluates
    detail: "Llama 2 serves as the base for Vicuna1.5, Longchat1.5, and NTK-scaled variants evaluated in L-Eval"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "L-Eval cites the lost-in-the-middle finding and designs enhanced topic retrieval to probe positional effects"
  - target: 2025-03-longiclbench-long-in-context-learning
    type: complementary
    detail: "LongICLBench complements L-Eval by testing full-input comprehension via extreme-label ICL rather than QA and summarization"
  - target: 2026-01-longbench-pro
    type: complementary
    detail: "LongBench Pro references L-Eval as a standardized evaluation protocol in the broader long-context evaluation landscape"
  - target: 2025-07-lv-eval-long-context-benchmark
    type: concurrent
    detail: "Both propose improved evaluation metrics for long-context; L-Eval uses LLM-assisted length-instruction-enhanced metrics, while LV-Eval uses keyword-recall-based two-stage F1 with human-annotated answer keywords"
open_questions:
  - question: "How can LLM judges be adapted to process the full long document rather than relying solely on reference answers and questions?"
    addressed_by: null
  - question: "How can open-source LCLMs improve instruction-following ability on open-ended tasks as context length increases?"
    addressed_by: null
  - question: "Can positional embedding scaling methods be modified to jointly optimize retrieval and reasoning capabilities?"
    addressed_by: null
---

# L-Eval: Instituting Standardized Evaluation for Long Context Language Models

**Authors:** Chenxin An, Shansan Gong, Ming Zhong, Xingjian Zhao, Mukai Li, Jun Zhang, Lingpeng Kong, Xipeng Qiu (Fudan University, The University of Hong Kong, UIUC, Shanghai AI Lab)
**Date:** ACL 2024 (arXiv:2307.11088, July 2023)

---

## Core Research Problem

Extending the context length of large language models has become a major research direction, with methods including efficient attention (Ding et al., 2023; Dao et al., 2022), chunked input processing (Bulatov et al., 2023; Mohtashami & Jaggi, 2023), and scaled positional embeddings (Chen et al., 2023; LocalLLaMA, 2023b). However, these methods have been primarily validated using perplexity, and no high-quality, standardized benchmark exists for evaluating long context language models (LCLMs) on practical tasks.

Existing long-sequence benchmarks have three specific problems. First, benchmarks such as SCROLLS (Shaham et al., 2022) and ZeroSCROLLS (Shaham et al., 2023) rely on automatic preprocessing scripts that fail to catch annotation errors, unanswerable questions, and low-quality samples. Second, nearly all previous benchmarks rely on n-gram matching metrics like ROUGE-L and F-1, and whether these metrics correlate well with human judgment for LCLMs in zero-shot settings has not been systematically studied. Third, the open-source community has released many models with 16k or 32k context lengths, but no comprehensive comparative study of these models against commercial models like GPT-4 and Claude exists.

**The core challenge is how to build a diverse, high-quality evaluation suite for LCLMs with both appropriate datasets and reliable evaluation metrics that correlate with human judgment.**

---

## Problem Solutions

L-Eval addresses the evaluation gap through three complementary contributions:

1. **Diverse, manually curated evaluation suite.** 20 sub-tasks, 508 long documents, and over 2,000 human-labeled query-response pairs spanning diverse question styles, domains, and input lengths (3k--200k tokens). Tasks are split into closed-ended (7 tasks with exact-match evaluation) and open-ended (13 tasks requiring generation). All samples are manually filtered and corrected after data collection (Section 3).
2. **Length-Instruction-Enhanced (LIE) evaluation.** A technique that injects the expected answer length into the prompt, substantially improving the correlation of all automatic metrics with human judgment. With LIE, the Kendall-Tau correlation of ROUGE-L rises from ~0.5 to ~0.8, and GPT-4 judge reaches 1.0 (Figure 2).
3. **Comprehensive model comparison.** 4 commercial LLMs and 12 open-source LCLMs evaluated under standardized conditions, revealing systematic gaps between open-source and commercial models that n-gram metrics fail to capture (Section 5).

---

## Approach Details

### Method

L-Eval constructs its evaluation suite from three data sources:

1. **4 datasets annotated from scratch** (Section 3.1): Coursera (lecture subtitles, multiple-choice with multiple correct answers), SFcition (science fiction True/False testing contextual vs. parametric knowledge), CodeU (Python code understanding from NumPy with obfuscated function names), and LongFQA (financial earnings call QA).
2. **4 datasets re-annotated from public sources** (Section 3.2): GSM(16-shot) (100 math problems from GSM8k with 16 Chain-of-Thought examples), QuALITY (enhanced with global context synthesis questions such as "What can we infer from the longest sentence?"), Openreview (paper writing and reviewing), and SPACE (aspect-based review summarization with diverse instructions).
3. **12 datasets manually filtered from prior benchmarks** (Section 3.3): TOEFL, TopicRet, MultiDoc2Dial, Qasper, NQ, CUAD, NarrativeQA, Multi-News, GovReport, BigPatent, SummScreen, QMSum. Claude-100k is used as an annotation assistant to identify mistaken QA pairs and unanswerable questions, which are then re-annotated or removed.

The suite is divided into two groups:

- **Closed-ended tasks** (7 tasks): Multiple choice (TOEFL, QuALITY, Coursera), True/False (SFcition), math (GSM-16-shot), code understanding (CodeU), topic retrieval (TopicRet). Evaluated by exact match accuracy (Section 4).
- **Open-ended tasks** (13 tasks): Abstractive QA, summarization, and generation tasks across law, finance, NLP papers, meetings, news, patents, TV transcripts, hotel reviews, and novels. Evaluated by human scoring, LLM judges, and n-gram metrics (Section 4).

### Key Technical Components

**Length-Instruction-Enhanced (LIE) evaluation.** LCLMs tend to generate excessively long responses, causing severe length bias in reference-based metrics. The generation length mismatch (delta-L) can be extreme: Claude-100k produces outputs 135 words longer than the reference on NQ, achieving only 9.84 F-1. LIE injects the word count of the reference answer into the instruction (e.g., "[Origin Instruction]: *Please summarize the opinions of the professor.* [Length Instruction]: *We need a 50-word summary*"). This reduces delta-L and substantially improves metric correlation with human judgment (Section 4.1):

| Metric | Kendall-Tau (tau) without LIE | Kendall-Tau (tau) with LIE |
|---|---|---|
| ROUGE-L | ~0.5 | ~0.8 |
| F-1 | ~0.7 | ~0.8 |
| GPT-3.5 judge | ~0.7 | ~0.8 |
| GPT-4 judge | ~0.8 | 1.0 |

Claude-100k's F-1 on NQ jumps from 9.84 to 57.76 with LIE -- a near 50-point improvement from controlling generation length alone (Table 2).

**LLM judges in long-context settings.** In short-context evaluation, the LLM judge can read the full input and infer ground truth independently. This assumption breaks in long-context settings because GPT-4 cannot process the lengthy input document. L-Eval uses a pair-wise battle format: the judge compares model output against Turbo-16k-0613 output using only the reference answer and question (without the long input). To counteract the judge's bias toward lengthy answers, the judgment prompt includes: *"Additional details or information that are not mentioned in the reference answer cannot be considered as advantages and do not let them sway your judgment."* Results are reported as win-rate vs. Turbo-16k-0613 %. Positional bias is reduced by swapping paired predictions (96x2 rounds for GPT-4, 181x2 for GPT-3.5) (Section 4).

**SFcition -- contextual vs. parametric knowledge.** This novel sub-task presents True/False questions about science fiction where answers contradict real-world facts. The model must follow the fictional world's rules (contextual knowledge) rather than its pretraining knowledge (parametric knowledge). Two questions are asked per fact: one based on the document and one based on real-world knowledge. The final accuracy averages both loyalty and factuality scores. Turbo-16k struggles on this task, tending to rely on parametric knowledge (Section 3.1, Table 3).

**Enhanced topic retrieval.** The original first-topic retrieval task from Li et al. (2023a) is too easy -- nearly all models score near 100%. L-Eval enhances it by requiring retrieval of the second and third topics from the conversation history. This proves dramatically harder: nearly all open-source models struggle while commercial models maintain high accuracy (Figure 1, Section 3.2).

**Coursera -- multiple correct answers.** Unlike standard multiple-choice benchmarks with a single correct option, L-Eval's Coursera task allows multiple correct answers. Failure to select all correct options yields only 25% of the question's score, increasing difficulty substantially (Section 3.1).

### Experimental Setup

**Models evaluated (16 total, Section 5.1):**
- **Commercial:** Claude-100k (Anthropic), GPT-4-32k (OpenAI), Turbo-16k-0613 (GPT-3.5, 16k), Turbo-4k-0613 (GPT-3.5, 4k)
- **Open-source (short context):** Llama1-7b (2k), Vicuna1.3-7b (2k), Llama2-7b (4k), Llama2-7b-chat (4k), Llama2-13b-chat (4k), ChatGLM2-6b-8k (2k/8k), XGen-7b-8k (2k/8k)
- **Open-source (extended context):** ChatGLM2-6b-32k (32k), Longchat-7b-16k (16k, PI), Longchat1.5-7b-32k (32k, PI), Vicuna1.5-7b-16k (16k, PI), Vicuna1.5-13b-16k (16k, PI), Longchat-13b-16k (16k), Llama2-7b-NTK (16k, NTK-aware), Llama2-13b-NTK (16k, NTK-aware), Llama2-13b-NTK-Dyn (16k, dynamic NTK), MPT-7B-StoryWriter-65k (8k, ALiBi)
- **Retrieval baselines:** AdaEmbedding + Turbo-4k, BM25 + Turbo-4k (4 chunks of 1k tokens)

**Hardware:** Single NVIDIA A800 GPU with FlashAttention (Dao et al., 2022). Documents truncated from the right. Greedy search decoding (Section 5, Appendix A.2).

**Human evaluation:** 3 annotators (Ph.D. students researching LCLMs) scoring 7 models on a 1--5 scale on an 85-question subset. Kendall-Tau correlation computed between automatic metrics and average human scores (Section 4.1, Appendix A.2).

**LLM evaluation:** GPT-4 judge on a 96-question subset (17 documents); GPT-3.5 judge on 181 questions (85+96). Positional bias reduced by swapping paired predictions (Section 4).

### Key Results

**Closed-ended tasks (exam evaluation, Table 3):**

| Model | Tokens | Coursera | GSM | QuALITY | TOEFL | CodeU | SFiction | Avg. |
|---|---|---|---|---|---|---|---|---|
| GPT-4-32k | 32k | 75.58 | 96.00 | 82.17 | 84.38 | 25.55 | 74.99 | 73.11 |
| Claude-100k | 100k | 60.03 | 88.00 | 73.76 | 83.64 | 17.77 | 72.65 | 65.97 |
| Turbo-16k | 16k | 63.51 | 84.00 | 61.38 | 78.43 | 12.22 | 64.84 | 60.73 |
| AdaEmb+Turbo-4k | 4k | 61.77 | 23.00 | 58.91 | 76.95 | 6.66 | 71.09 | 49.73 |
| BM25+Turbo-4k | 4k | 63.80 | 23.00 | 59.40 | 75.09 | 5.55 | 71.09 | 49.65 |
| Vicuna1.5-13b-16k | 16k | 40.69 | 36.00 | 53.96 | 68.40 | 0.00 | 61.71 | 43.46 |
| ChatGLM2-32k | 32k | 47.81 | 27.00 | 45.04 | 55.01 | 2.22 | 57.02 | 39.01 |

- GPT-4-32k achieves SOTA with a **~30-point gap** over the best open-source model and a **~20-point gap** over Turbo-16k.
- CodeU is the hardest task: even GPT-4-32k achieves only 25.55% (Section 5.2).
- Retrieval completely fails on CodeU (6.66/5.55%) and GSM-16-shot (23.00%), where global context understanding is required.

**Open-ended tasks (GPT-4 judge win-rate vs. Turbo-16k, Table 4):**

| Model | Tokens | GPT-4 win-rate % | GPT-3.5 win-rate % |
|---|---|---|---|
| Claude-100k | 100k | 60.94 | 58.68 |
| GPT-4-32k | 32k | 54.16 | 56.32 |
| Turbo-16k | 16k | 50.00 (baseline) | 50.00 |
| Llama2-13b-chat | 4k | 42.44 | 47.85 |
| Vicuna1.5-13b-16k | 16k | 34.11 | 40.92 |
| Llama2-7b-NTK | 16k | 22.13 | 23.59 |

- Claude-100k surpasses GPT-4-32k on open-ended tasks because open-ended tasks generally involve longer input documents that benefit from its 100k context window (Section 5.2).
- N-gram metrics (ROUGE-L column in Table 4) fail to reveal the gap between open-source and commercial models that both LLM judges and human evaluation clearly show.

**Human evaluation (85-question subset, 1--5 scale, Table 5):**

| Model | Human-Avg (with LIE) | Human-Avg (without LIE) |
|---|---|---|
| Claude-100k | 4.04 | 3.08 |
| Turbo-16k | 3.58 | 3.00 |
| Turbo-4k | 3.30 | 2.89 |
| Llama2-13b-chat | 3.15 | 2.31 |
| Llama2-7b-chat | 2.96 | 1.86 |
| Longchat-7b-16k | 2.28 | 1.72 |
| Vicuna1.5-7b-16k | 2.21 | 1.84 |

- With LIE, the human evaluation rankings closely match the GPT-4 judge rankings. Without LIE, rankings are distorted and open-source LCLMs produce many Level-1 (worst) outputs (Table 5, Section A.2).

### Extended Context Helps Closed-Ended but Not Open-Ended Tasks

For open-source models using scaled positional embeddings, Longchat-16k and Vicuna1.5-16k outperform their short-context counterparts on closed-ended tasks (Table 3: Vicuna1.5-13b-16k at 43.46% vs. Llama2-13b-chat at 39.01%). However, on open-ended tasks, the best extended-context model (Vicuna1.5-13b-16k) only achieves 34.11% win-rate against Turbo-16k -- **8 points lower** than its short-context counterpart Llama2-13b-chat at 42.44% (Table 4). Human evaluation reveals that extended-context models produce many "invalid outputs" (failing to follow instructions) when input exceeds 4k tokens. On the 85-question subset split by input length, Llama2/Vicuna1.5-16k produces 27% invalid outputs on inputs longer than 4k tokens (PART-B), while Turbo-16k maintains only ~4% invalid outputs at all lengths (Figure 4, Section 5.2).

### Retrieval-Based vs. Full-Context Models

End-to-end full-context models (Turbo-16k) outperform retrieval-based systems on closed-ended tasks: 60.73% average vs. 49.73% (AdaEmbedding) and 49.65% (BM25) (Table 3). Retrieval fails entirely on CodeU and GSM-16-shot (which require understanding the full codebase or all 16 examples), and struggles with topic retrieval and financial QA that demand long-range reasoning. On open-ended tasks, retrieval achieves similar performance for conventional summarization but produces "I don't know" answers when relevant passages cannot be retrieved. In closed-ended tasks, BM25 matches the dense retriever AdaEmbedding, but in open-ended tasks the dense retriever outperforms BM25 by more than two points due to semantic matching ability (Section 5.2, Appendix A.3).

### NTK Base Scaling: Retrieval vs. Reasoning Trade-off

Increasing the NTK base from 20,000 to 160,000 continuously improves topic retrieval accuracy but degrades math reasoning (GSM-16-shot) in an opposite trend (Figure 5). Topic retrieval performance plateaus after the base reaches ~60,000, while reasoning continues to decline. This indicates that NTK scaling enhances the model's ability to attend over longer distances (retrieval) while harming its reasoning ability, and these two capabilities cannot be jointly optimized through base scaling alone (Section 5.2).

### Dynamic NTK Scaling Rules Do Not Hold in Practice

The dynamic NTK scaling rule (setting the RoPE base to `10,000 * (L/l)^(d/(d-2))` where L is input length, l is pretraining length, and d is head dimension) does not hold in practical tasks when input length changes. Simple modifications such as NTK-bias (`10,000 * (L/l + 1)^(d/(d-2))`) and NTK-weighted (`10,000 * (L/l * 2)^(d/(d-2))`) yield different optima depending on the input length: NTK-bias works best for 4k--8k inputs while NTK-weighted is more robust at 16k inputs (Figure 6, Appendix A.3).

---

## Limitations and Failure Modes

1. **Benchmark temporal scope.** L-Eval was constructed in mid-2023 and evaluates models from that era. The benchmark does not cover models with 128k+ context windows that emerged later (Section 6).
2. **Preprint status of evaluated models.** Several open-source models evaluated were early releases and may have been subsequently improved.
3. **LIE requires known answer length.** The LIE technique assumes access to the reference answer's word count at inference time, which is unavailable in real-world deployment. It is designed as an evaluation protocol improvement, not a deployment strategy (Section 4.1).
4. **LLM judge cannot access the long document.** The GPT-4/GPT-3.5 judge evaluates outputs based only on the reference answer and question, without the long input document. This may miss valid answers not covered by the reference and introduces dependence on reference quality (Section 4).
5. **Closed-ended tasks limited to 6 tasks in main table.** TopicRet is reported separately, and the closed-ended average in Table 3 is computed over 6 of the 7 closed-ended tasks.
6. **Single GPU constraint.** All experiments use a single A800 GPU, requiring right-truncation of documents that exceed the model's context window. This means some models never see the full input for longer documents.

---

## Conclusions

### Contributions

1. **First standardized long-context evaluation with metric analysis.** L-Eval provides 20 sub-tasks across diverse domains and question styles (3k--200k tokens) with all samples manually filtered and corrected. It is the first benchmark to systematically study the correlation between automatic metrics and human judgment for LCLMs (Section 4.1).

2. **Length-Instruction-Enhanced evaluation protocol.** LIE improves the Kendall-Tau correlation of ROUGE-L with human judgment from ~0.5 to ~0.8, and GPT-4 judge from ~0.8 to 1.0, by controlling generation length through simple prompt injection (Figure 2).

3. **Quantified gap between open-source and commercial LCLMs.** On closed-ended tasks, GPT-4-32k leads by ~30 points over the best open-source model (Table 3). On open-ended tasks, both LLM judges and human evaluators confirm a significant gap that n-gram metrics fail to reveal (Tables 4, 5).

4. **Novel task designs testing underexplored capabilities.** SFcition tests contextual vs. parametric knowledge loyalty, CodeU tests long code understanding (hardest task at 25.55% for GPT-4), and enhanced TopicRet tests second/third topic retrieval where open-source models largely fail (Sections 3.1, 3.2).

5. **Full-context models outperform retrieval-based systems.** End-to-end LCLMs outperform RAG pipelines on L-Eval's closed-ended tasks by ~11 points, with retrieval failing entirely on tasks requiring global context understanding (Table 3).

### Implications

1. **Extended context helps structured tasks but may hurt open-ended generation.** Scaled positional embeddings improve closed-ended task performance but degrade instruction-following ability on open-ended tasks, with extended-context models producing up to 27% invalid outputs on longer inputs. This suggests that SFT on longer dialogues alone is insufficient for robust long-context generation (inference from Tables 3, 4, and Figure 4).

2. **NTK scaling reveals a fundamental retrieval-reasoning trade-off.** Retrieval and reasoning capabilities cannot be jointly optimized through positional embedding scaling alone, suggesting that more sophisticated approaches may be needed for truly general long-context LLMs (inference from Figure 5).

3. **N-gram metrics should not be used as the primary evaluation for LCLMs.** The poor correlation of ROUGE-L and F-1 with human judgment, especially without length control, means that benchmark leaderboards based solely on n-gram metrics may be misleading (inference from Figure 2 and Table 2).

---

## Key Claims

1. **N-gram metrics fail for LCLM evaluation.** ROUGE-L and F-1 achieve only ~0.5 and ~0.7 Kendall-Tau correlation with human judgment without LIE, respectively. All automatic metrics except GPT-4 fail to correlate with human judgment in the default setting (Figure 2, Section 4.1). **Status: supported.**

2. **LIE evaluation improves all automatic metrics.** After adding length instructions, Kendall-Tau improves for ROUGE-L (~0.5 to ~0.8), F-1 (~0.7 to ~0.8), GPT-3.5 judge (~0.7 to ~0.8), and GPT-4 judge (~0.8 to 1.0). Claude-100k's F-1 on NQ jumps from 9.84 to 57.76, a near 50-point improvement from length control alone (Figure 2, Table 2, Section 4.1). **Status: supported.**

3. **Large gap between commercial and open-source LCLMs.** GPT-4-32k achieves 73.11% average on closed-ended tasks vs. 43.46% for the best open-source model. On open-ended tasks, the best extended-context open-source model (Vicuna1.5-13b-16k) only achieves 34.11% GPT-4 win-rate vs. Turbo-16k (Tables 3, 4, Section 5.2). **Status: supported.**

4. **Extended context helps closed-ended but not open-ended tasks.** Vicuna1.5-13b-16k outperforms Llama2-13b-chat on closed-ended tasks (43.46% vs. 39.01%) but underperforms on open-ended tasks (34.11% vs. 42.44% win-rate). Human evaluation shows that extended-context models produce dramatically more invalid outputs on inputs longer than 4k tokens (Tables 3, 4, Figure 4). **Status: supported.**

5. **Full-context models outperform retrieval.** Turbo-16k outperforms AdaEmbedding+Turbo-4k and BM25+Turbo-4k on closed-ended tasks (60.73% vs. 49.73%/49.65%). Retrieval fails on CodeU, GSM-16-shot, and topic retrieval (Table 3, Section 5.2). **Status: supported.**

6. **NTK base scaling creates a retrieval-reasoning trade-off.** Increasing the NTK base from 20,000 to 160,000 monotonically improves topic retrieval but monotonically degrades GSM-16-shot reasoning (Figure 5). **Status: supported.**

7. **Dynamic NTK scaling rules do not hold in practical tasks.** The theoretical NTK scaling rule fails when input length varies; NTK-bias and NTK-weighted variants perform differently at different input lengths (Figure 6, Appendix A.3). **Status: supported.**

---

## Open Questions

1. **How can LLM judges evaluate long-context outputs without seeing the full document?** L-Eval's LLM judge relies solely on the reference answer and question, which may miss valid answers. No approach currently allows the judge to process the full long input alongside model outputs. Not addressed by subsequent work in this directory.

2. **How can open-source LCLMs improve instruction-following on long-context open-ended tasks?** L-Eval shows that extended-context models produce up to 27% invalid outputs on long inputs, but the root cause (SFT data distribution, positional embedding limitations, or both) remains unclear. Not addressed by subsequent work in this directory.

3. **Can positional embedding scaling jointly optimize retrieval and reasoning?** The NTK base trade-off (Figure 5) suggests these capabilities may be fundamentally in tension under current PE scaling approaches. Not addressed by subsequent work in this directory.

4. **What evaluation metrics beyond n-gram matching and LLM judges can reliably assess LCLM performance at scale?** LLM judges are expensive and still biased; n-gram metrics are unreliable. More advanced automatic metrics are needed. Not addressed by subsequent work in this directory.

---

## Core References and Why They Are Referenced

### Evaluation Benchmarks

- **Shaham et al. (2022)** -- *SCROLLS: Standardized CompaRison Over Long Language Sequences.* The most prominent prior long-context benchmark. L-Eval addresses three SCROLLS limitations: automatic sample filtering, sole reliance on n-gram metrics, and too few closed-ended tasks.
- **Shaham et al. (2023)** -- *ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding.* Concurrent zero-shot long-context benchmark. L-Eval differs in manual sample filtering and metric standardization.
- **Bai et al. (2023)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* Concurrent long-context benchmark. L-Eval differentiates through manual sample filtering, metric-human correlation study, and more closed-ended tasks.
- **Tay et al. (2020)** -- *Long Range Arena.* Benchmark for efficient Transformers with 5 classification tasks. L-Eval focuses on generative LLMs and practical long-document tasks rather than synthetic classification.
- **Zhang et al. (2023)** -- *CAB: Comprehensive Attention Benchmarking on Long Sequence Modeling.* Benchmark for efficient attention designs. L-Eval inherits 12 sub-tasks from datasets also used by CAB but adds manual correction and annotation.

### Positional Embedding and Context Extension

- **Su et al. (2022)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* The RoPE method underlying PI and NTK-aware scaling techniques evaluated in L-Eval.
- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* The PI method used by Longchat and Vicuna1.5. L-Eval shows PI helps closed-ended but not open-ended tasks.
- **LocalLLaMA (2023b)** -- *NTK-Aware Scaled RoPE.* Training-free context extension via NTK-aware scaling. L-Eval demonstrates the retrieval-reasoning trade-off from increasing the NTK base and shows that the theoretical scaling rule does not hold in practical tasks.
- **LocalLLaMA (2023a)** -- *Dynamically Scaled RoPE.* Dynamic NTK variant where the scale factor depends on input length. L-Eval shows this does not hold in practical tasks when input length varies.
- **Press et al. (2022)** -- *ALiBi: Train Short, Test Long.* Linear bias attention used by MPT-7B-StoryWriter-65k, which achieves only 19.22% average on L-Eval closed-ended tasks.

### Models Evaluated

- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* Base model for Vicuna, Longchat, and other open-source LCLMs evaluated in L-Eval.
- **Touvron et al. (2023b)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Base model for Vicuna1.5, Longchat1.5, and NTK-scaled variants. Llama2-13b-chat is the strongest open-source baseline on open-ended tasks.
- **Du et al. (2022)** -- *GLM: General Language Model Pretraining.* Base model for ChatGLM2-8k and ChatGLM2-32k evaluated in L-Eval.
- **Chiang et al. (2023)** -- *Vicuna.* Instruction-tuned LLaMA variant serving as the short-context baseline.
- **Li et al. (2023a)** -- *LongChat.* Long-context Vicuna variant using PI. Also provides the TopicRet task that L-Eval enhances with second/third topic retrieval.

### Evaluation Methodology

- **Lin (2004)** -- *ROUGE: A Package for Automatic Evaluation of Summaries.* The n-gram matching metric that L-Eval demonstrates has poor correlation with human judgment for LCLMs (~0.5 Kendall-Tau without LIE).
- **Zheng et al. (2023)** -- *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* Foundation for LLM-based evaluation. L-Eval adapts the pairwise battle format to long-context settings where the judge cannot read the full input.
- **Li et al. (2023c)** -- *AlpacaEval.* LLM-based evaluation framework. L-Eval's pairwise battle format draws on this approach.
- **Liu et al. (2023)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Cited for the finding that models attend best to the beginning and end of context. L-Eval's enhanced TopicRet (second/third topic retrieval) probes this phenomenon.

### Source Datasets

- **Pang et al. (2022)** -- *QuALITY.* Multiple-choice QA from Gutenberg that L-Eval re-annotates with global context synthesis questions.
- **Cobbe et al. (2021)** -- *GSM8k.* Grade school math dataset from which L-Eval constructs 16-shot in-context examples with lengthy Chain-of-Thought.
- **Kwiatkowski et al. (2019)** -- *Natural Questions.* Wikipedia-based QA dataset filtered for L-Eval.
- **Kocisk\'{y} et al. (2017)** -- *NarrativeQA.* The longest-document dataset in L-Eval (up to ~210k tokens).
- **Hendrycks et al. (2021b)** -- *CUAD.* Legal contract review dataset filtered for L-Eval.
- **Dao et al. (2022)** -- *FlashAttention.* Used to run all experiments efficiently on a single A800 GPU.
