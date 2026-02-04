---
title: "Ada-LEval: Evaluating Long-Context LLMs with Length-Adaptable Benchmarks"
authors: "Wang, Duan, Zhang, Lin, Chen"
year: 2024
venue: "NAACL 2024"
paper_type: conference-paper
categories: ["benchmarking", "long-context-evaluation", "position-bias"]
scope: ["length-controllable evaluation", "full-text comprehension tasks", "ultra-long context evaluation"]
benchmarks_used: ["ada-leval"]
models_introduced: []
models_evaluated: ["gpt-4"]
key_claims:
  - id: C1
    claim: "Only GPT-4-Turbo significantly exceeds random guess on TSort at 2k--8k tokens; at 16k all models deteriorate to random-guess level"
    evidence: "Table 2, Section 4.2"
    status: supported
  - id: C2
    claim: "All models achieve 0% accuracy on BestAnswer at 64k and 128k tokens despite claiming context windows of 100k--200k tokens"
    evidence: "Table 6, Section 4.4"
    status: supported
  - id: C3
    claim: "Open-source models can distinguish correct text orderings via perplexity evaluation (up to 89.2% accuracy) but fail to produce them generatively (maximum 5.4%), revealing a gap between comprehension and instruction following"
    evidence: "Table 7, Section 4.5.1"
    status: supported
  - id: C4
    claim: "All models exhibit significant position bias on BestAnswer, with most models achieving higher accuracy when the ground-truth answer is at the beginning; this bias intensifies as input length increases"
    evidence: "Table 8, Section 4.5.2"
    status: supported
  - id: C5
    claim: "Ada-LEval requires more full-text comprehension than traditional QA and summarization tasks, as BestAnswer performance drops 33 points when truncated vs. 8.4 for NarrativeQA"
    evidence: "Table 10, Section 4.5.4"
    status: supported
  - id: C6
    claim: "Scalable position embeddings (NTK-aware Scaled RoPE, ReRoPE, Leaky ReRoPE) improve long-context capability and achieve performance comparable to models trained on longer contexts"
    evidence: "Table 9, Section 4.5.3"
    status: supported
cross_references:
  - target: 2022-12-scrolls-long-language-sequences
    type: complementary
    detail: "SCROLLS is cited as a predecessor multi-task long-context benchmark; Ada-LEval addresses its fixed-length limitation and lack of ultra-long settings"
  - target: 2024-08-l-eval-standardized-evaluation
    type: complementary
    detail: "Both provide long-context evaluation; Ada-LEval critiques L-Eval for inflexible text lengths (up to ~32k) and reliance on traditional QA/summarization"
  - target: 2024-08-longbench-bilingual-benchmark
    type: complementary
    detail: "Ada-LEval critiques LongBench for fixed-length test cases, open-ended metrics (F1/ROUGE), and lack of ultra-long settings; uses LongBench subsets (NarrativeQA, GovReport) for truncation comparison"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Ada-LEval's position bias results (Section 4.5.2) are consistent with the lost-in-the-middle finding that models struggle with information in the middle of long contexts"
  - target: 2025-04-effective-context-length-falls-short
    type: complementary
    detail: "Both find that effective context length falls far short of claimed context window size"
  - target: 2024-01-roformer-rope
    type: evaluates
    detail: "Scalable RoPE variants (NTK-aware, ReRoPE) are evaluated in the position embedding ablation study (Section 4.5.3)"
  - target: 2023-06-rope-ntk
    type: evaluates
    detail: "NTK-aware Scaled RoPE is evaluated on BestAnswer and shown to improve long-context capability beyond the original context window"
  - target: 2023-06-pi-positional-interpolation
    type: complementary
    detail: "Position Interpolation is referenced as the technique used by ChatGLM2-32k for context extension"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "ALiBi is referenced as a contrasting position encoding approach that applies linearly decreasing attention penalties"
  - target: 2023-07-llama-2-open-foundation-chat
    type: evaluates
    detail: "Vicuna-v1.5 models (Llama 2 fine-tuned) serve as both baselines and testbeds for scalable position embedding experiments"
  - target: 2026-01-longbench-pro
    type: complementary
    detail: "LongBench Pro references Ada-LEval as a length-adaptable extension of standardized evaluation"
open_questions:
  - question: "Can instruction-following capabilities over long texts be improved to close the gap between perplexity-based comprehension and generative output quality?"
    addressed_by: null
  - question: "How can ultra-long benchmarks be designed to differentiate model capabilities at 64k+ tokens, where current models uniformly score 0%?"
    addressed_by: null
  - question: "Does position bias in answer selection reflect a fundamental attention mechanism limitation or a training data artifact?"
    addressed_by: 2024-08-found-in-the-middle
---

# Ada-LEval: Evaluating Long-Context LLMs with Length-Adaptable Benchmarks

**Authors:** Chonghua Wang, Haodong Duan, Songyang Zhang, Dahua Lin, Kai Chen (Shanghai AI Laboratory, Shanghai Jiao Tong University)
**Date:** June 2024, NAACL 2024 (arXiv:2404.06480)

---

## Core Research Problem

Existing long-context benchmarks such as L-Eval (An et al., 2023) and LongBench (Bai et al., 2023) suffer from three limitations. First, they integrate test samples of varying lengths (from 2k to 32k+ tokens) into a single evaluation, making it difficult to assess model capabilities at specific length ranges. Second, they do not cover the **ultra-long setting** (32k+ tokens) that the latest LLMs claim to support -- GPT-4-Turbo (128k tokens), Claude-2.1 (200k tokens), and Kimi Chat (200k Chinese characters). Third, their reliance on traditional QA and summarization tasks does not require comprehensive content understanding; many questions can be answered from a small portion of the input (Section 1).

Prior benchmarks like SCROLLS (Shaham et al., 2022) established multi-task long-text evaluation but are limited to moderate lengths and do not provide mechanisms for controlling test case length. L-Eval and LongBench offer broader task coverage but use fixed-length documents and open-ended metrics (F1, ROUGE) that "may not align well with human judgments" (Section 2.3).

**The core challenge is how to build a length-adaptable benchmark that requires full-text comprehension, scales to ultra-long contexts (128k tokens), and provides precise accuracy-based evaluation.**

---

## Problem Solutions

Ada-LEval introduces two tasks -- **TSort** (text segment ordering) and **BestAnswer** (best answer selection) -- designed for length-adaptable evaluation of long-context LLMs. The solution rests on three properties:

1. **Controllable test cases.** Test case length can be finely tuned by adjusting the number and length of text segments (TSort) or the number of distractor answers (BestAnswer), producing samples from 1k to 128k tokens.
2. **Necessity for full-text comprehension.** Both tasks mandate reading the entire input: TSort requires understanding all segments to determine their order; BestAnswer requires comparing all candidate answers to identify the best one.
3. **Precise accuracy measurement.** TSort has a single correct ordering; BestAnswer uses the answer explicitly accepted by the original questioner as ground truth. No subjective metrics like ROUGE or F1 are needed.

---

## Approach Details

### Method

**TSort.** The model receives N shuffled text segments extracted from contiguous chapters of a long book. Adjacent paragraphs before and after the chapters are provided as contextual hints. The task is to sort the segments into their original order. A response is correct only if it exactly matches the original sequence. Under long-context settings (2k--16k), N is fixed at 4, giving a random guess accuracy of 1/4! = 1/24 ~ 4.2% (Section 3.1).

**BestAnswer.** The model receives a programming question from Stack Overflow and a set of candidate answers. The ground truth is the answer explicitly accepted by the original asker. Distractor answers include both **intra-question answers** (other answers to the same question, posted before the accepted answer) and **inter-question answers** (answers from questions with similar tags). Random guess accuracy is 1/N, where N varies per question based on the number of candidates at each length setting (Section 3.1).

### Key Technical Components

**Source data.** TSort uses BookSum (Kryscinski et al., 2021), derived from Project Gutenberg. Genres with non-sequential structure (epistolary literature, poetry) are excluded. Chapter numbers and annotations are removed to prevent superficial cue exploitation. BestAnswer uses threads from 23 Stack Overflow tags (JavaScript, Python, C++, etc.), with the top 2,500 questions per tag selected by popularity. Questions where the accepted answer is not text-only are excluded. Only answers posted prior to the accepted answer are used as intra-question distractors (Sections 3.2, 3.3).

**Length control.** For TSort, the segment count (N=4) and per-segment length upper limit are fixed at each target length; a stride parameter between beginning paragraphs generates diverse test cases. Per Table 11 (Appendix A), segment length upper limits range from 350 tokens (2k setting) to 31,700 tokens (128k setting), with stride 64 (long-context) or 128 (ultra-long). For BestAnswer, the same questions are reused across all long-context length settings, with the number of inter-question distractor answers adjusted to reach the target length. Under ultra-long settings, tag similarity constraints are relaxed: questions need only share at least 1 tag in common (vs. 40% tags in common under long-context settings) (Sections 3.3, Appendix A).

**Data statistics (GPT-4 CL100K tokenizer):**

| Task | Setting | Total Cases Built | Max Tokens | Avg Tokens |
|---|---|---|---|---|
| TSort | 2k | 5,123 | 2,000 | 1,816 |
| TSort | 4k | 5,451 | 4,000 | 3,724 |
| TSort | 8k | 5,324 | 8,000 | 7,663 |
| TSort | 16k | 4,957 | 16,000 | 15,662 |
| TSort | 32k | 2,206 | 32,000 | 31,226 |
| TSort | 64k | 1,658 | 64,000 | 62,407 |
| TSort | 128k | 782 | 127,800 | 121,488 |
| BestAnswer | 1k | 7,526 | 1,128 | 955 |
| BestAnswer | 16k | 7,526 | 15,964 | 15,646 |
| BestAnswer | 32k | 200 | 32,974 | 32,329 |
| BestAnswer | 64k | 200 | 64,216 | 63,274 |
| BestAnswer | 128k | 200 | 127,059 | 126,098 |

(Table 1, Section 3)

**Evaluation protocol.** Zero-shot evaluation for all models. Open-source models use 1,000-testcase subsets; proprietary models use 200-testcase subsets (long-context) and 50-testcase subsets (ultra-long). Instruction following rate and copy instruction rate are measured alongside accuracy. Evaluation conducted via OpenCompass (Contributors, 2023). For proprietary models (GPT-4-Turbo, GPT-3.5-Turbo), temperature is set to 0; open-source models use their default hyperparameters. Open-source experiments run on NVIDIA A100 80GB GPUs, consuming approximately 800 GPU-hours total (Section 4.1, Appendix B).

### Experimental Setup

**Models evaluated:**

| Model | Type | Context Window |
|---|---|---|
| GPT-4-Turbo-0125 | Proprietary | 128k |
| GPT-4-Turbo-1106 | Proprietary | 128k |
| GPT-3.5-Turbo-1106 | Proprietary | 16k |
| Claude-2 | Proprietary | 100k |
| LongChat-7b-v1.5-32k | Open-source | 32k |
| ChatGLM2-6B-32k | Open-source | 32k |
| ChatGLM3-6B-32k | Open-source | 32k |
| Vicuna-7b-v1.5-16k | Open-source | 16k |
| Vicuna-13b-v1.5-16k | Open-source | 16k |
| InternLM2-7b | Open-source | -- |

Ultra-long evaluation (32k--128k) is limited to GPT-4-Turbo, Claude-2, Claude-2.1, and InternLM2-7b (BestAnswer only) due to inferior open-source model performance (Section 4.1).

### Key Results

**TSort (long-context, N=4, random guess ~ 4.2%):**

| Model | 2k | 4k | 8k | 16k |
|---|---|---|---|---|
| GPT-4-Turbo-0125 | 15.5 | 16.5 | 8.5 | 5.5 |
| GPT-4-Turbo-1106 | 18.5 | 15.5 | 7.5 | 3.5 |
| GPT-3.5-Turbo-1106 | 4.0 | 4.5 | 4.5 | 5.5 |
| Claude-2 | 5.0 | 5.0 | 4.5 | 3.0 |
| LongChat-7b-v1.5-32k | 5.3 | 5.0 | 3.1 | 2.5 |
| ChatGLM2-6B-32k | 0.9 | 0.7 | 0.2 | 0.9 |
| ChatGLM3-6B-32k | 2.3 | 2.4 | 2.0 | 0.7 |
| Vicuna-7b-v1.5-16k | 5.3 | 2.2 | 2.3 | 1.7 |
| Vicuna-13b-v1.5-16k | 5.4 | 5.0 | 2.4 | 3.1 |
| InternLM2-7b | 5.1 | 3.9 | 5.1 | 4.3 |
| Random Guess | 4.2 | 4.2 | 4.2 | 4.2 |

(Table 2)

- **Only GPT-4-Turbo significantly exceeds random at 2k--8k.** At 16k, GPT-4-Turbo deteriorates to near random-guess level. All other models perform at or near random across all settings, "even under the relative short 2k setting" (Section 4.2).

**BestAnswer (long-context):**

| Model | 1k | 2k | 4k | 6k | 8k | 12k | 16k |
|---|---|---|---|---|---|---|---|
| GPT-4-Turbo-0125 | 73.5 | 73.5 | 65.5 | 63.0 | 56.5 | 52.0 | 44.5 |
| GPT-4-Turbo-1106 | 74.0 | 73.5 | 67.5 | 59.5 | 53.5 | 49.5 | 44.0 |
| GPT-3.5-Turbo-1106 | 61.5 | 48.5 | 41.5 | 29.5 | 17.0 | 2.5 | 2.5 |
| Claude-2 | 65.0 | 43.5 | 23.5 | 15.0 | 17.0 | 12.0 | 11.0 |
| LongChat-7b-v1.5-32k | 32.4 | 10.7 | 5.7 | 3.1 | 1.9 | 1.6 | 0.8 |
| ChatGLM2-6B-32k | 31.2 | 10.9 | 4.5 | 1.6 | 1.6 | 0.0 | 0.3 |
| ChatGLM3-6B-32k | 39.8 | 18.8 | 9.0 | 5.0 | 3.4 | 0.9 | 0.5 |
| Vicuna-7b-v1.5-16k | 37.0 | 11.1 | 5.8 | 3.2 | 1.8 | 1.9 | 1.0 |
| Vicuna-13b-v1.5-16k | 53.4 | 29.2 | 13.1 | 4.3 | 2.2 | 1.4 | 0.9 |
| InternLM2-7b | 58.6 | 49.5 | 33.9 | 12.3 | 13.4 | 2.0 | 0.8 |
| Random Guess | 26.7 | 10.1 | 4.5 | 3.0 | 2.3 | 1.4 | 1.1 |

(Table 3)

- **GPT-4-Turbo achieves state-of-the-art on BestAnswer**, maintaining 44.5% at 16k with ~100 distractors per question. Claude-2 is second at 11% under the 16k setting. Open-source models decline to near random by 8k--16k (Section 4.2).

**Ultra-long-context results (32k--128k):**

| Task | Model | 32k | 64k | 128k |
|---|---|---|---|---|
| TSort | GPT-4-Turbo-0125 | 2.0 | 4.0 | 2.0 |
| TSort | GPT-4-Turbo-1106 | 6.0 | 6.0 | 6.0 |
| TSort | Claude-2 | 0.0 | 0.0 | / |
| TSort | Claude-2.1 | 0.0 | 0.0 | 0.0 |
| TSort | Random Guess | 4.2 | 4.2 | 4.2 |
| BestAnswer | GPT-4-Turbo-0125 | 30.0 | 0.0 | 0.0 |
| BestAnswer | GPT-4-Turbo-1106 | 16.0 | 0.0 | 0.0 |
| BestAnswer | Claude-2 | 4.0 | 0.0 | / |
| BestAnswer | Claude-2.1 | 4.0 | 0.0 | 0.0 |
| BestAnswer | InternLM2-7b | 0.5 | 0.5 | 0.0 |
| BestAnswer | Random Guess | 0.6 | 0.3 | 0.1 |

(Table 6)

- **All models collapse at 64k+ tokens on BestAnswer.** No model produces any correct answers at 64k or 128k. On TSort, GPT-4-Turbo achieves only random-level accuracy across all ultra-long settings; Claude produces zero correct answers. These models "suffer from a dramatic decline on their performance under ultra-long-context settings" despite claiming 100k+ token context windows (Section 4.4).

### Error Analysis

Most errors fall into two categories: (1) **failure to follow instructions** (not outputting a valid answer format) and (2) **copying the example answer** provided in the in-context example prompt (Section 4.3).

GPT-4-Turbo maintains near-perfect instruction following and low copy rates on both tasks. Claude-2 and LongChat exhibit elevated copy instruction rates: Claude-2 reaches 95--99.5% copy rate on TSort (Table 4), while its copy rate on BestAnswer increases from 21.5% at 1k to 55.0% at 16k (Table 5). ChatGLM models suffer primarily from low instruction following rates (Figure 2). All models except GPT-4-Turbo find it harder to follow instructions as text length increases (Section 4.3).

### Perplexity Evaluation on TSort

When open-source models evaluate TSort via perplexity (selecting the lowest-perplexity permutation among all 24 orderings), accuracy dramatically exceeds generative performance (Section 4.5.1):

| Model (PPL Eval) | 2k | 4k | 8k |
|---|---|---|---|
| LongChat-7b-v1.5-32k | 60.9 | 68.3 | 77.4 |
| ChatGLM2-6B-32k | 40.5 | 53.5 | 57.5 |
| ChatGLM3-6B-32k | 50.1 | 57.0 | 59.3 |
| Vicuna-7b-v1.5-16k | 70.1 | 78.3 | 77.7 |
| Vicuna-13b-v1.5-16k | 79.3 | 86.7 | 89.2 |
| Random Guess | 4.2 | 4.2 | 4.2 |

(Table 7)

Vicuna-13b-v1.5-16k achieves 79.3--89.2% via PPL evaluation vs. 2.4--5.4% generative (Table 2). This shows models can distinguish correct ordering internally but fail to produce it when asked. The authors note: "when the sorting task is presented as QAs where LLMs are asked to directly output the correct order, the performance significantly deteriorates, indicating the limited instruction following capabilities of existing LLMs" (Section 4.5.1). One potential cause is that the book chapters have been used for pretraining (footnote 5).

### Position Bias in BestAnswer

All models demonstrate **significant position bias** in choosing the best answer (Section 4.5.2). The ground-truth answer position is varied (beginning, middle, rear) while keeping questions and candidates identical:

| Model | Pos | 1k | 2k | 4k | 8k | 16k |
|---|---|---|---|---|---|---|
| GPT-4-Turbo-1106 | front | 76.5 | 82.5 | 86.5 | 90.0 | 82.0 |
| GPT-4-Turbo-1106 | mid | 74.5 | 68.0 | 60.0 | 38.0 | 38.5 |
| GPT-4-Turbo-1106 | rear | 57.5 | 46.6 | 44.0 | 40.5 | 26.5 |
| Claude-2 | front | 34.0 | 19.0 | 14.5 | 50.0 | 6.0 |
| Claude-2 | mid | 49.0 | 35.5 | 21.5 | 13.0 | 5.0 |
| Claude-2 | rear | 59.0 | 36.5 | 26.0 | 11.0 | 9.5 |
| Vicuna-7b-v1.5-16k | front | 29.3 | 8.9 | 14.0 | 37.6 | 25.4 |
| Vicuna-7b-v1.5-16k | mid | 32.8 | 13.6 | 0.0 | 0.0 | 0.2 |
| Vicuna-7b-v1.5-16k | rear | 34.2 | 2.1 | 0.0 | 0.0 | 0.7 |

(Table 8, selected rows)

Most models achieve higher accuracy when the ground-truth answer is at the beginning. Claude-2 uniquely performs best when the ground truth is at the rear across 4 of 5 settings. Position bias intensifies as input length increases: Vicuna-7b-v1.5-16k shows relatively uniform accuracy at 1k but at 16k performance remains stable only for front-positioned answers (Section 4.5.2).

### Scalable Position Embeddings

NTK-aware Scaled RoPE, ReRoPE, and Leaky ReRoPE are evaluated on Vicuna-v1.5 models (Llama 2 fine-tuned with 4k context window) on the BestAnswer benchmark (Section 4.5.3). Results reported as accuracy / accuracy-excluding-instruction-failures:

| Vicuna-7b-v1.5 | 1k | 2k | 4k | 8k |
|---|---|---|---|---|
| ReRoPE | 39.6/39.6 | 11.6/11.6 | 4.7/5.4 | 2.3/3.2 |
| Leaky ReRoPE | 39.9/39.9 | 11.2/11.2 | 5.1/5.7 | 1.3/2.0 |
| NTK | 32.5/32.5 | 10.7/10.7 | 5.8/5.8 | 3.9/3.9 |
| Original (4k) | 39.5/39.5 | 9.8/11.0 | 4.2/5.5 | 0.0/0.0 |
| Original (16k) | 37.0/39.5 | 11.1/11.1 | 5.8/5.8 | 2.5/2.7 |

| Vicuna-13b-v1.5 | 1k | 2k | 4k | 8k |
|---|---|---|---|---|
| ReRoPE | 49.2/49.2 | 22.5/22.5 | 9.2/10.0 | 1.5/2.8 |
| Leaky ReRoPE | 49.3/49.3 | 23.8/23.8 | 8.7/9.8 | 1.3/2.6 |
| NTK | 43.8/43.8 | 23.0/23.0 | 11.1/11.1 | 2.3/2.3 |
| Original (4k) | 49.1/49.1 | 17.7/17.7 | 5.9/5.9 | 0.1/1.0 |
| Original (16k) | 53.4/53.4 | 29.2/29.2 | 13.1/13.5 | 2.6/2.7 |

(Table 9)

All methods enhance accuracy beyond the original 4k window (e.g., at 8k, NTK achieves 3.9% vs. 0.0% for Original-4k on Vicuna-7b). NTK-aware Scaled RoPE diminishes 1k performance but outperforms other methods at longer contexts. Performance is comparable to models further trained on 16k contexts with Flash Attention. Advantages are more pronounced on Vicuna-13b-v1.5 (Section 4.5.3).

### Comparison with Other Long-Context Benchmarks

GPT-4-Turbo-1106 evaluated on BestAnswer (16k), NarrativeQA (LongBench subset, QA task, F1 metric), and GovReport (LongBench subset, summarization task, ROUGE-L metric) with progressive text truncation (Section 4.5.4):

| Benchmark | 2k | 4k | 8k | Full | Avg Tokens |
|---|---|---|---|---|---|
| BestAnswer | 11.0 | 20.0 | 31.5 | 44.0 | 15,646 |
| NarrativeQA | 24.7 | 25.6 | 29.7 | 33.1 | 10,276 |
| GovReport | 30.7 | 32.4 | 33.6 | 30.9 | 29,872 |

(Table 10)

BestAnswer shows the steepest performance drop when truncated: from 44.0% (full) to 11.0% (2k), a 33-point drop. NarrativeQA drops only 8.4 points (33.1 to 24.7). GovReport performance actually increases when truncated (30.9 full to 33.6 at 8k). This confirms that Ada-LEval requires more comprehensive text understanding than traditional QA and summarization tasks (Section 4.5.4).

---

## Limitations and Failure Modes

1. **Cannot distinguish open-source models.** Due to poor instruction following and high copy instruction rates, Ada-LEval accuracy scores for open-source models cluster near random guess, limiting discriminative power among them (Section 6).

2. **Difficulty ceiling at ultra-long settings.** "Even state-of-the-art proprietary models are not able to achieve an ideal performance" at ultra-long settings, with all models scoring 0% on BestAnswer at 64k+, which "further constrains its applicability to current LLMs" (Section 6).

3. **Evaluation subset size.** Proprietary models are evaluated on only 200 test cases (long-context) or 50 test cases (ultra-long) due to API cost constraints. Though Appendix B validates that 200-testcase results are consistent with 1,000-testcase results for open-source models (Tables 12, 13), the ultra-long 50-testcase subset is small enough that individual correct/incorrect answers meaningfully shift accuracy.

4. **Domain specificity of BestAnswer.** BestAnswer draws exclusively from Stack Overflow programming questions, limiting the benchmark to the programming domain. The ground truth (asker-accepted answer) may not always be the objectively best answer, as the authors acknowledge (footnote 2).

5. **Potential pretraining contamination on TSort.** The PPL evaluation results may be inflated because "one potential cause is that the chapters have been used for pretraining" (footnote 5), which would allow models to recognize correct text ordering through memorization rather than comprehension.

---

## Conclusions

### Contributions

1. **First length-adaptable long-context benchmark.** Ada-LEval introduces two tasks (TSort and BestAnswer) that can generate test cases at any target length from 1k to 128k tokens, addressing the inflexibility of fixed-length benchmarks like LongBench and L-Eval (Section 1).

2. **Full-text comprehension requirement validated by truncation.** Truncation experiments demonstrate that BestAnswer performance degrades 33 points when truncated to 2k vs. only 8.4 points for NarrativeQA and a slight improvement for GovReport, confirming Ada-LEval tasks require reading the entire input (Table 10, Section 4.5.4).

3. **Systematic quantification of ultra-long context failure.** Ada-LEval is the first benchmark to evaluate models at 32k--128k tokens, revealing that no model achieves meaningful accuracy on BestAnswer at 64k+ despite claimed context windows of 100k--200k tokens (Table 6, Section 4.4).

4. **Generative-perceptual gap quantified.** PPL-based evaluation on TSort shows open-source models can distinguish correct orderings (up to 89.2%) but fail to produce them generatively (maximum 5.4%), revealing a fundamental gap between internal comprehension and instruction-following output (Table 7, Section 4.5.1).

5. **Position bias characterized across models and lengths.** Systematic position manipulation on BestAnswer reveals that all models exhibit significant position bias, most preferring answers at the beginning, with bias intensifying as context grows (Table 8, Section 4.5.2).

6. **Scalable position embeddings validated as viable.** NTK-aware Scaled RoPE, ReRoPE, and Leaky ReRoPE extend effective context beyond the training window and achieve performance comparable to models explicitly trained on longer contexts (Table 9, Section 4.5.3).

### Implications

1. **Claimed context windows are unreliable.** The gap between claimed context window size (128k--200k tokens) and effective comprehension capability (collapsing at 16k--32k) suggests that context window size alone is a misleading measure of long-context capability. [Inference: this calls into question marketing claims about context window size.]

2. **Instruction following is a bottleneck distinct from comprehension.** The perplexity-vs-generative gap suggests that model improvements should target instruction following in long-context settings, not only context comprehension itself (Section 4.5.1).

3. **Benchmark design matters for evaluating long-context capability.** Traditional QA and summarization tasks can be answered from truncated input, masking long-context limitations that Ada-LEval exposes. Future benchmarks should validate that tasks genuinely require full-text comprehension (Section 4.5.4).

---

## Key Claims

1. **C1: Only GPT-4-Turbo exceeds random on TSort; all models reach random-guess level at 16k.** Under 2k--8k settings, only GPT-4-Turbo outputs correct orderings "with a significant higher probability compared to the random baseline." At 16k, "the quality of GPT-4-Turbo's predictions also deteriorates to the random guess level" (Table 2, Section 4.2). Status: **supported**.

2. **C2: All models achieve 0% on BestAnswer at 64k and 128k tokens.** No model produces any correct answers at 64k or 128k. On BestAnswer, "the performance of all three models fall sharply from 16k to 32k text length. Meanwhile, they can not give any correct answer when the text length is greater than 32k" (Table 6, Section 4.4). Status: **supported**.

3. **C3: Open-source models distinguish correct orderings via PPL (up to 89.2%) but fail generatively (max 5.4%).** "When text segments are arranged in the correct order, a significantly lower perplexity score can usually be observed, resulting in the high TSort accuracy. However, when the sorting task is presented as QAs ... the performance significantly deteriorates" (Table 7, Section 4.5.1). Status: **supported**.

4. **C4: All models show significant position bias, intensifying with length.** "All models demonstrate significant position bias in choosing the most helpful answer. Most models achieve much better accuracy when the most helpful answer presents at the beginning." GPT-4-Turbo-1106 at 8k: 90.0% (front) vs. 38.0% (mid) vs. 40.5% (rear). Bias intensifies as input grows (Table 8, Section 4.5.2). Status: **supported**.

5. **C5: Ada-LEval requires more full-text comprehension than traditional benchmarks.** BestAnswer drops 33 points when truncated to 2k (44.0 to 11.0), while NarrativeQA drops 8.4 points and GovReport actually improves. "Our benchmarks require more full-text comprehension than traditional QA and summarization tasks" (Table 10, Section 4.5.4). Status: **supported**.

6. **C6: Scalable position embeddings achieve performance comparable to models trained on longer contexts.** All three methods (NTK, ReRoPE, Leaky ReRoPE) enhance accuracy at 8k (beyond the 4k training window), with performance "comparable to their counterparts trained on longer contexts" (Table 9, Section 4.5.3). Status: **supported**.

---

## Open Questions

1. **Can instruction following over long texts be improved to close the generative-perceptual gap?** The paper demonstrates that models can internally comprehend text ordering (89.2% PPL accuracy) but fail to output it (5.4% generative accuracy). Whether this gap is addressable through instruction tuning on long texts or represents a deeper architectural limitation is unresolved. Not yet addressed.

2. **How can ultra-long benchmarks differentiate model capabilities at 64k+ tokens?** At 64k--128k, all models score 0% on BestAnswer, creating a ceiling effect that prevents measuring relative progress. Future benchmarks need graduated difficulty at ultra-long lengths. Not yet addressed.

3. **Does position bias in answer selection reflect an attention mechanism limitation or a training data artifact?** The paper observes position bias but does not determine its root cause. Addressed in part by Wang et al. (2025) in 2024-08-found-in-the-middle.

---

## Core References and Why They Are Referenced

### Prior Long-Context Benchmarks

- **Shaham et al. (2022)** -- *SCROLLS.* An earlier multi-task long-context benchmark. Ada-LEval addresses SCROLLS's limitations of fixed-length evaluation and lack of ultra-long settings (Section 2.3).

- **An et al. (2023)** -- *L-Eval.* A long-context evaluation benchmark with close-ended and open-ended tasks. Ada-LEval critiques L-Eval for inflexible text lengths (up to ~32k) and reliance on traditional QA/summarization (Section 2.3).

- **Bai et al. (2023)** -- *LongBench.* A bilingual long-context benchmark covering six task categories. Ada-LEval critiques LongBench for fixed-length test cases, open-ended metrics (F1/ROUGE), and lack of ultra-long settings. LongBench subsets (NarrativeQA, GovReport) are used in the truncation comparison (Section 2.3, Section 4.5.4).

### Task Source Data

- **Kryscinski et al. (2021)** -- *BookSum.* Provides the Project Gutenberg book data used to construct TSort. Text segments are extracted from contiguous chapters with identifiers removed (Section 3.2).

- **Kocisky et al. (2018)** -- *NarrativeQA.* Used as a comparison benchmark (LongBench subset) in the truncation experiment; NarrativeQA drops only 8.4 points when truncated (Table 10, Section 4.5.4).

- **Huang et al. (2021)** -- *GovReport.* Used as a comparison benchmark (LongBench subset) in the truncation experiment; GovReport performance actually improves when truncated (Table 10, Section 4.5.4).

### Long-Context Techniques

- **Su et al. (2021)** -- *RoPE (RoFormer).* The base positional encoding used by most evaluated models. Scalable RoPE variants (NTK-aware, ReRoPE) are evaluated in the ablation study (Section 2.1, Section 4.5.3).

- **Chen et al. (2023b)** -- *Position Interpolation.* Linearly scales down position indices to extend context windows. Referenced as the context extension technique used by ChatGLM2-32k (Section 2.1, Section 2.2).

- **Su (2023)** -- *ReRoPE / Leaky ReRoPE.* Rectified Rotary Position Embeddings that control scaling via a window size parameter. Evaluated on Vicuna-v1.5 in the scalable position embedding ablation (Section 2.1, Section 4.5.3).

- **Press et al. (2021)** -- *ALiBi.* An alternative position encoding applying linearly decreasing penalties to attention scores based on key-query distances. Referenced as a contrasting approach to RoPE-based methods (Section 2.1).

### Position Bias

- **Liu et al. (2023a)** -- *Lost in the Middle.* Identified that LLMs struggle to use information in the middle of long contexts. Ada-LEval's position bias results (Section 4.5.2) are consistent with this finding (Section 2.1).

### Models and Evaluation Infrastructure

- **OpenAI (2023)** -- *GPT-4.* GPT-4-Turbo is the top-performing model across both tasks but still collapses at ultra-long settings (0% on BestAnswer at 64k+) (Section 4).

- **Zheng et al. (2023)** -- *Vicuna / MT-Bench.* Vicuna models are used both as open-source baselines and as the testbed for scalable position embedding ablations (Section 4, Section 4.5.3).

- **Touvron et al. (2023)** -- *Llama 2.* The base model for Vicuna-v1.5, which integrates RoPE with a 4k context window. The scalable position embedding ablation extends Vicuna-v1.5 beyond this 4k window (Section 2.2).

- **Contributors (2023)** -- *OpenCompass.* The open-source evaluation platform used to conduct all experiments (Section 4.1).

### Efficient Attention and Long-Context Modeling

- **Dao et al. (2022a)** -- *FlashAttention.* An efficient attention implementation referenced as enabling longer context windows in Vicuna-v1.5-16k models (Section 2.1, Section 4.5.3).

- **Ding et al. (2023)** -- *LongNet / Dilated Attention.* Reduces attention complexity to near-linear and scales to 1 billion tokens. Referenced alongside Liu et al. (2023a)'s finding that such mechanisms struggle with middle portions of long texts (Section 2.1).
