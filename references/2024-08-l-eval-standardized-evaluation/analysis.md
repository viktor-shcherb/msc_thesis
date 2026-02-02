# L-Eval: Instituting Standardized Evaluation for Long Context Language Models

**Authors:** Chenxin An, Shansan Gong, Ming Zhong, Xingjian Zhao, Mukai Li, Jun Zhang, Lingpeng Kong, Xipeng Qiu (Fudan University, The University of Hong Kong, UIUC, Shanghai AI Lab)
**Date:** August 2024, ACL 2024 (arXiv:2307.11088)

---

## Core Research Problem

While there has been significant progress in extending the context length of large language models -- through efficient attention mechanisms (Ding et al., 2023; Dao et al., 2022), chunked input approaches (Bulatov et al., 2023; Mohtashami & Jaggi, 2023), and scaled positional embeddings (Chen et al., 2023; LocalLLaMA, 2023) -- there is no high-quality, standardized benchmark for evaluating these long context language models (LCLMs) on practical tasks.

Existing long-sequence benchmarks have three problems. First, prior benchmarks such as SCROLLS (Shaham et al., 2022) and ZeroScrolls (Shaham et al., 2023) rely primarily on automatic preprocessing scripts that do not catch annotation errors, unanswerable questions, or low-quality samples. Second, nearly all previous benchmarks rely on n-gram matching metrics like ROUGE-L and F-1, which have poor correlation with human judgment when applied to LCLMs in zero-shot settings. Third, there is no comprehensive comparative study of the rapidly growing set of open-source LCLMs (16k, 32k context) against commercial models like GPT-4 and Claude.

**The core challenge is how to build a diverse, high-quality evaluation suite for LCLMs with both appropriate datasets and reliable evaluation metrics that correlate with human judgment.**

---

## Problem Solutions

L-Eval addresses the evaluation gap through two complementary contributions: a new evaluation suite and a study of evaluation metrics.

1. **Diverse, manually curated evaluation suite.** 20 sub-tasks, 508 long documents, and over 2,000 human-labeled query-response pairs spanning diverse question styles, domains, and input lengths (3k--200k tokens). Tasks are split into closed-ended (7 tasks with exam-style evaluation) and open-ended (13 tasks requiring generation).
2. **Length-Instruction-Enhanced (LIE) evaluation.** A simple technique that injects the expected answer length into the prompt, substantially improving the correlation of all automatic metrics (n-gram and LLM judges) with human judgment.
3. **Comprehensive model comparison.** 4 commercial LLMs and 12 open-source LCLMs evaluated under standardized conditions, revealing systematic gaps between open-source and commercial models.

---

## Approach Details

### Method

L-Eval constructs its evaluation suite from three sources:

1. **4 datasets annotated from scratch** (Coursera, SFcition, CodeU, LongFQA): novel annotations on Coursera lecture subtitles, science fiction novels, Python codebases (from NumPy), and financial earnings call transcripts.
2. **4 datasets re-annotated from public sources** (GSM-16-shot, QuALITY, Openreview, SPACE): existing datasets enhanced with new instructions, additional question types (e.g., global context synthesis questions for QuALITY), and extended in-context examples (16-shot Chain-of-Thought for GSM).
3. **12 datasets manually filtered from prior benchmarks** (TOEFL, TopicRet, MultiDoc2Dial, Qasper, NQ, CUAD, NarrativeQA, Multi-News, GovReport, BigPatent, SummScreen, QMSum): samples manually reviewed and corrected with Claude-100k as an annotation assistant.

The suite is divided into two groups:

- **Closed-ended tasks** (7 tasks): Multiple choice (TOEFL, QuALITY, Coursera), True/False (SFcition), math (GSM-16-shot), code understanding (CodeU), topic retrieval (TopicRet). Evaluated by exact match accuracy.
- **Open-ended tasks** (13 tasks): Abstractive QA, summarization, and generation tasks. Evaluated by human scoring, LLM judges (GPT-4, GPT-3.5), and n-gram metrics (ROUGE-L, F-1).

### Key Technical Components

**Length-Instruction-Enhanced (LIE) evaluation.** LCLMs tend to generate very long responses, causing severe length bias in reference-based metrics. LIE injects the word count of the reference answer into the instruction (e.g., "We need a 50-word summary"). This reduces the generation length mismatch (delta-L) and substantially improves metric correlation with human judgment:

| Metric | Kendall-Tau (tau) without LIE | Kendall-Tau (tau) with LIE |
|---|---|---|
| ROUGE-L | ~0.5 | ~0.8 |
| F-1 | ~0.7 | ~0.8 |
| GPT-3.5 | ~0.7 | ~0.8 |
| GPT-4 | ~0.8 | 1.0 |

For example, Claude-100k achieves only 9.84 F-1 on NQ without LIE (due to excessively long outputs, delta-L = 135), but 57.76 F-1 with LIE (delta-L = 1) -- a near 50-point improvement from controlling generation length alone.

**LLM judges in long-context settings.** Unlike short-context evaluation where the judge can read the full input, GPT-4 cannot process the long document itself. L-Eval uses a pair-wise battle format: the judge compares model output against Turbo-16k-0613 output based on the reference answer and question only (without the long input). To counteract the judges' bias toward lengthy answers, the judgment prompt includes: *"Additional details or information that are not mentioned in the reference answer cannot be considered as advantages and do not let them sway your judgment."*

**SFcition -- testing contextual vs. parametric knowledge.** This novel sub-task presents True/False questions about science fiction where answers contradict real-world facts. The model must follow the fictional world's rules (contextual knowledge) rather than its pretraining knowledge (parametric knowledge). Two questions are asked per fact: one based on the document and one based on real-world knowledge, and the final accuracy averages both.

**Enhanced topic retrieval.** The original first-topic retrieval task (TopicRet from Li et al., 2023a) is too easy -- nearly all models score near 100%. L-Eval enhances it by requiring retrieval of the second and third topics from the conversation history, which proves dramatically harder for open-source models.

**Coursera -- multiple correct answers.** Unlike standard multiple-choice benchmarks with a single correct option, L-Eval's Coursera task allows multiple correct answers, increasing difficulty. Failure to select all correct options yields only 25% of the question's score.

### Experimental Setup

**Models evaluated (16 total):**
- **Commercial:** Claude-100k, GPT-4-32k, Turbo-16k-0613, Turbo-4k-0613
- **Open-source (truncated to pretraining length):** Llama1-7b, Vicuna1.3-7b, Llama2-7b, Llama2-7b-chat, Llama2-13b-chat, ChatGLM2-6b-8k, XGen-7b-8k
- **Open-source (extended context):** ChatGLM2-6b-32k, Longchat-7b-16k, Longchat1.5-7b-32k, Vicuna1.5-7b-16k, Vicuna1.5-13b-16k, Llama2-7b-NTK, Llama2-13b-NTK, Llama2-13b-NTK(Dyn), MPT-7B-StoryWriter-65k
- **Retrieval baselines:** AdaEmbedding + Turbo-4k, BM25 + Turbo-4k

**Hardware:** Single NVIDIA A800 GPU with FlashAttention (Dao et al., 2022). Documents truncated from the right.

**Human evaluation:** 3 annotators (Ph.D. students researching LCLMs) scoring on a 1--5 scale on an 85-question subset. Kendall-Tau correlation computed between automatic metrics and average human scores.

**LLM evaluation:** GPT-4 judge on a 96-question subset; GPT-3.5 judge on 181 questions (85+96). Positional bias reduced by swapping paired predictions (96x2 rounds for GPT-4, 181x2 for GPT-3.5).

### Key Results

**Closed-ended tasks (exam evaluation):**

| Model | Tokens | Coursera | GSM | QuALITY | TOEFL | CodeU | SFiction | Avg. |
|---|---|---|---|---|---|---|---|---|
| GPT-4-32k | 32k | 75.58 | 96.00 | 82.17 | 84.38 | 25.55 | 74.99 | 73.11 |
| Claude-100k | 100k | 60.03 | 88.00 | 73.76 | 83.64 | 17.77 | 72.65 | 65.97 |
| Turbo-16k | 16k | 63.51 | 84.00 | 61.38 | 78.43 | 12.22 | 64.84 | 60.73 |
| Vicuna1.5-13b-16k | 16k | 40.69 | 36.00 | 53.96 | 68.40 | 0.00 | 61.71 | 43.46 |
| ChatGLM2-32k | 32k | 47.81 | 27.00 | 45.04 | 55.01 | 2.22 | 57.02 | 39.01 |

- GPT-4-32k achieves SOTA on closed-ended tasks with a near **20-point gap** over the best open-source 16k models.
- CodeU is the hardest task: even GPT-4-32k achieves only 25.55%.

**Open-ended tasks (GPT-4 judge, win-rate vs. Turbo-16k):**

| Model | Tokens | GPT-4 Win-Rate % | GPT-3.5 Win-Rate % |
|---|---|---|---|
| Claude-100k | 100k | 60.94 | 58.68 |
| GPT-4-32k | 32k | 54.16 | 56.32 |
| Turbo-16k | 16k | 50.00 | 50.00 |
| Llama2-13b-chat | 4k | 42.44 | 47.85 |
| Vicuna1.5-13b-16k | 16k | 34.11 | 40.92 |

- Claude-100k surpasses GPT-4-32k on open-ended tasks due to its longer context window (100k vs. 32k), since open-ended tasks generally involve longer input documents.
- N-gram metrics fail to reveal the gap between open-source and commercial models that both LLM judges and human evaluation clearly show.

**Human evaluation (85-question subset, 1--5 scale):**

| Model | Human-Avg (with LIE) | Human-Avg (without LIE) |
|---|---|---|
| Claude-100k | 4.04 | 3.08 |
| Turbo-16k | 3.58 | 3.00 |
| Turbo-4k | 3.30 | 2.89 |
| Vicuna1.5-7b-16k | 2.21 | 1.84 |
| Longchat-7b-16k | 2.28 | 1.72 |

- With LIE, the human evaluation rankings closely match the GPT-4 judge rankings. Without LIE, the rankings are distorted.

### Fine-Tuning Longer Helps Closed-Ended but Not Open-Ended Tasks

Scaled positional embedding (PI, NTK-aware) improves closed-ended task performance: Longchat-16k and Vicuna1.5-16k outperform their short-context counterparts. However, on open-ended tasks, the best extended-context model (Vicuna1.5-13b-16k) only wins 34% against Turbo-16k -- 8 points lower than Llama2-13b-chat at 4k context. Human evaluation reveals that extended-context models produce many "invalid outputs" (failing to follow instructions) when input exceeds 4k tokens, while Turbo-16k maintains low invalid-output rates at all lengths.

### Retrieval-Based vs. Full-Context Models

End-to-end full-context models (Turbo-16k) outperform retrieval-based systems (AdaEmbedding + Turbo-4k, BM25 + Turbo-4k) on closed-ended tasks (60.73 vs. 49.73/49.65 average). Retrieval fails entirely on CodeU and GSM-16-shot, and struggles with topic retrieval and financial QA. On open-ended tasks, retrieval achieves similar performance for simple summarization but produces "I don't know" answers when relevant passages cannot be retrieved.

### NTK Base Scaling: Retrieval vs. Reasoning Trade-off

Increasing the NTK base from 20,000 to 160,000 continuously improves topic retrieval accuracy but degrades math reasoning (GSM-16-shot) in an opposite trend. This indicates that NTK scaling enhances the model's ability to attend over longer distances (retrieval) while harming its reasoning ability, and the two capabilities cannot be jointly optimized through base scaling alone.

### Limitations

1. **Benchmark scope.** L-Eval was constructed in mid-2023 and evaluates models from that era. The benchmark does not cover models with 128k+ context windows that emerged later.
2. **Preprint status of evaluated models.** Several open-source models evaluated were early releases and may have been subsequently improved.
3. **LIE evaluation requires known answer length.** The LIE technique assumes access to the reference answer's length at inference time, which is unavailable in real-world deployment. It is designed as an evaluation protocol improvement, not a deployment strategy.
4. **LLM judge limitations.** The judge cannot access the long input document, so evaluation depends entirely on the reference answer and question. This may miss valid answers not covered by the reference.

---

## Conclusions

1. **First standardized long-context evaluation with metric analysis.** L-Eval is the first benchmark to systematically study the correlation between automatic metrics and human judgment for LCLMs, demonstrating that n-gram metrics fail in this setting and advocating for LLM judges with LIE evaluation.

2. **Length-Instruction-Enhanced evaluation.** LIE improves the Kendall-Tau correlation of ROUGE-L with human judgment from 0.5 to 0.8, and GPT-4 judge from 0.8 to 1.0. This simple technique addresses the generation length bias that distorts all reference-based metrics.

3. **Large gap between open-source and commercial LCLMs.** On closed-ended tasks, GPT-4-32k leads by ~20 points over the best open-source 16k model. On open-ended tasks, both LLM judges and human evaluators confirm a significant gap that n-gram metrics fail to reveal.

4. **Extended context helps closed-ended but not open-ended tasks.** Scaled positional embeddings improve performance on structured tasks (multiple choice, retrieval) but degrade instruction-following ability on open-ended generation as input length increases, producing many invalid outputs.

5. **Full-context models outperform retrieval-based systems.** End-to-end LCLMs outperform RAG pipelines on L-Eval's closed-ended tasks, with retrieval failing entirely on tasks requiring global context understanding (code, many-shot reasoning, topic retrieval).

6. **NTK scaling reveals a retrieval-reasoning trade-off.** Increasing the NTK base improves long-range retrieval but degrades reasoning ability, indicating these capabilities cannot be jointly optimized through positional embedding scaling alone.

---

## Core References and Why They Are Referenced

### Evaluation Benchmarks

- **Shaham et al. (2022)** -- *SCROLLS: Standardized CompaRison Over Long Language Sequences.* The most prominent prior long-context benchmark. L-Eval differs by manually curating samples, investigating metric reliability, and including more closed-ended tasks.
- **Shaham et al. (2023)** -- *ZeroSCROLLS: A Zero-Shot Benchmark for Long Text Understanding.* Concurrent zero-shot long-context benchmark. L-Eval contrasts with ZeroSCROLLS by not relying on automatic sample filtering.
- **Bai et al. (2023)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* Concurrent long-context benchmark. L-Eval differentiates itself through manual sample filtering, standardized metrics investigation, and more closed-ended tasks.
- **Zhang et al. (2023)** -- *CAB: Comprehensive Attention Benchmarking on Long Sequence Modeling.* A benchmark for efficient attention designs. L-Eval inherits 12 sub-tasks from datasets also used by CAB but adds manual correction.
- **Tay et al. (2020)** -- *Long Range Arena.* Earlier benchmark for efficient Transformers with 5 classification tasks. L-Eval focuses on generative LLMs rather than encoder-only architectures.

### Positional Embedding and Context Extension

- **Su et al. (2022)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* The RoPE method that is the basis for PI and NTK-aware scaling techniques evaluated in L-Eval.
- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* The PI method used by Longchat and Vicuna1.5 models. L-Eval shows PI helps closed-ended but not open-ended tasks.
- **LocalLLaMA (2023b)** -- *NTK-Aware Scaled RoPE.* Training-free context extension via NTK-aware scaling. L-Eval demonstrates that increasing the NTK base improves retrieval but degrades reasoning.
- **Press et al. (2022)** -- *ALiBi: Train Short, Test Long.* Linear bias attention used by MPT-7B-StoryWriter-65k, evaluated in L-Eval.

### Models Evaluated

- **Touvron et al. (2023a,b)** -- *LLaMA / LLaMA 2.* Base models for many open-source LCLMs in L-Eval (Vicuna, Longchat, NTK variants).
- **Du et al. (2022)** -- *GLM.* Base model for ChatGLM2-8k and ChatGLM2-32k evaluated in L-Eval.
- **Chiang et al. (2023)** -- *Vicuna.* Instruction-tuned model built on LLaMA, serving as the short-context baseline.
- **Li et al. (2023a)** -- *LongChat.* Long-context Vicuna variant using PI. Also provides the TopicRet task that L-Eval enhances.

### Evaluation Methodology

- **Lin (2004)** -- *ROUGE.* The n-gram matching metric that L-Eval demonstrates has poor correlation with human judgment for LCLMs.
- **Zheng et al. (2023)** -- *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* Foundation for using LLM judges. L-Eval adapts this to long-context settings where the judge cannot read the full input.
- **Li et al. (2023c)** -- *AlpacaEval.* LLM-based evaluation framework. L-Eval's pair-wise battle format is informed by this approach.

### Source Datasets

- **Pang et al. (2022)** -- *QuALITY.* Multiple-choice QA dataset from Gutenberg that L-Eval re-annotates with global context synthesis questions.
- **Cobbe et al. (2021)** -- *GSM8k.* Grade school math dataset from which L-Eval constructs 16-shot in-context examples.
- **Kwiatkowski et al. (2019)** -- *Natural Questions.* Wikipedia-based QA dataset filtered for L-Eval.
- **Kocisk\'{y} et al. (2017)** -- *NarrativeQA.* The longest-document dataset in L-Eval (up to 210k tokens).
- **Hendrycks et al. (2021b)** -- *CUAD.* Legal contract review dataset filtered for L-Eval.
- **Dao et al. (2022)** -- *FlashAttention.* Used to run all experiments efficiently on a single A800 GPU.

#### Cross-References in Available Papers

- **BABILong (2024-12-babilong-long-context-reasoning):** Kuratov et al. (2024) cite L-Eval as one of the existing benchmarks that scale only to 40K tokens. BABILong differentiates itself by offering controllable sequence length up to 10M tokens and testing multi-fact reasoning.
- **SCROLLS (2022-12-scrolls-long-language-sequences):** L-Eval inherits and manually corrects several sub-tasks from datasets also used in SCROLLS, and directly contrasts its manual curation approach against SCROLLS's automatic filtering.
- **ZeroSCROLLS (2023-12-zeroscrolls-zero-shot-long-text):** Concurrent benchmark. L-Eval explicitly differentiates from ZeroSCROLLS on three axes: manual sample selection, metric standardization, and more closed-ended tasks.
- **LongBench (2024-08-longbench-bilingual-benchmark):** Concurrent benchmark. L-Eval identifies LongBench as a concurrent effort and differentiates through manual filtering and metric investigation. Both benchmarks are frequently cited together as the early generation of long-context evaluation suites.
