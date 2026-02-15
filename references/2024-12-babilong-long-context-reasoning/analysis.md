---
title: "BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack"
authors: "Kuratov, Bulatov, Anokhin, Rodkin, Sorokin, Sorokin, Burtsev"
year: 2024
venue: "NeurIPS 2024 Datasets and Benchmarks Track"
paper_type: conference-paper
categories: ["benchmarking", "long-context-evaluation", "reasoning-evaluation"]
scope: ["reasoning in long contexts", "up to 50M tokens", "multi-fact reasoning"]
benchmarks_used: ["babilong", "niah", "mmlu", "ruler"]
models_introduced: []
models_evaluated: ["gpt-4", "gpt-2", "gpt-3.5-turbo", "llama-3-8b", "llama-3.1-8b", "llama-3.1-70b", "gemini-1.5-pro", "mistral-7b", "mixtral-8x7b", "qwen2.5-7b", "qwen2.5-72b", "phi-3-mini", "phi-3-medium", "phi-3.5-moe", "mamba-2.8b", "mamba-130m", "rwkv-7b", "yi-9b", "yi-34b", "gpt-4o-mini"]
# NOTE: Additional model IDs needed in metadata.yaml: mixtral-8x22b, jamba
key_claims:
  - id: C1
    claim: "Popular LLMs effectively utilize only 10-20% of their claimed context window on QA1"
    evidence: "Figure 2, Section 3.1: most models maintain >85% accuracy only up to 4K tokens; GPT-4 and LLama-3.1-70B extend to 16K; Qwen-2.5-72B and Gemini 1.5 Pro extend to 64K"
    status: supported
    scope: "QA1 single-fact retrieval task, 34 models, few-shot prompting, PG19 background text"
    magnitude: "Effective range 5-50% of claimed context, majority capped at 4K out of 128K"
  - id: C2
    claim: "BABILong provides 20 controllable reasoning tasks scalable to arbitrary length with predefined splits up to 10M tokens"
    evidence: "Table 1, Section 2: benchmark design with 20 tasks from bAbI embedded in PG19 background text"
    status: supported
    scope: "English only, bAbI reasoning tasks, PG19 background text"
    magnitude: "20 tasks, predefined splits from 0K to 10M tokens, evaluations demonstrated up to 50M"
  - id: C3
    claim: "RAG fails on multi-fact reasoning tasks, with sentence-level retrieval achieving scalable but weak performance on QA1 and collapsing on QA2/QA3"
    evidence: "Figure 3a, Section 3.2: RAG-S top-5 achieves moderate QA1 accuracy but drops below random guessing on QA2 and QA3"
    status: supported
    scope: "GPT-4 + FAISS with text-embedding-ada-002, Llama3-ChatQA-1.5-8B + nvidia/dragon encoder, unoptimized retrieval"
    magnitude: "QA2 and QA3 accuracy below random guessing at 128K; RAG-C inferior to RAG-S"
  - id: C4
    claim: "Fine-tuned recurrent memory transformers (ARMT, 137M parameters) process up to 50 million tokens, outperforming LLMs 1000x their size"
    evidence: "Figure 1b, Figure 3b, Section 3.3: ARMT with GPT-2 backbone achieves 77% on QA1 at 50M tokens"
    status: supported
    scope: "QA1 single-fact task, GPT-2 backbone, curriculum training up to 32 segments (16K tokens)"
    magnitude: "ARMT 77% at 50M tokens on QA1; RMT scales to 11.1M tokens (600x training length)"
  - id: C5
    claim: "Context extension methods (YaRN, Activation Beacon) fail to extend effective context despite stable perplexity"
    evidence: "Section 3.1, Table 2: YaRN fails to extend; LongChat, LongAlpaca fail at trained 32K length; Activation Beacon <40% at 32K"
    status: supported
    scope: "YaRN-Mistral, Activation Beacon on LLama-2 and Mistral, 32K-128K context range"
    magnitude: "YaRN shows no improvement; Activation Beacon <40% at 32K; LongChat/LongAlpaca fail at trained 32K"
  - id: C6
    claim: "BABILong captures differences in model behavior starting from 2K tokens, while RULER requires 128K+ tokens for differentiation from MMLU"
    evidence: "Figure 4, Section 3.4: BABILong correlation with MMLU drops as length increases; RULER maintains near-constant correlation"
    status: supported
    scope: "Correlation analysis across multiple models, BABILong QA1-5 vs MMLU vs RULER, up to 128K tokens"
    magnitude: "BABILong-MMLU R^2 = 0.888 at 0K (QA2), dropping with length; RULER-MMLU R^2 = 0.928 at <=128K; at most-correlated lengths 0.928 vs 0.435 and 0.910 vs 0.455"
  - id: C7
    claim: "BABILong is immune to data contamination because facts are procedurally generated"
    evidence: "Section 2: generated benchmarks like bAbI and BABILong are immune to data leakage to training sets"
    status: supported
    scope: "general"
    magnitude: "qualitative"
cross_references:
  - target: 2023-11-needle-in-a-haystack
    type: extends
    detail: "BABILong extends the vanilla NIAH test from single-fact retrieval to multi-fact reasoning across 20 diverse tasks"
  - target: 2024-10-ruler-context-size
    type: complementary
    detail: "Both provide synthetic controllable evaluation; BABILong focuses on reasoning while RULER focuses on retrieval/aggregation; Section 3.4 compares their MMLU correlations"
  - target: 2024-08-longbench-bilingual-benchmark
    type: complementary
    detail: "Cites LongBench as limited to 40K tokens and confounding long-context with parametric knowledge"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: complementary
    detail: "References ZeroSCROLLS as a realistic benchmark lacking controllable sequence length"
  - target: 2024-08-infinitebench-long-context-evaluation
    type: complementary
    detail: "Both scale beyond 100K tokens; BABILong goes further with splits up to 10M and evaluations to 50M"
  - target: 2024-05-yarn-context-extension
    type: evaluates
    detail: "Evaluates YaRN on BABILong; finds it fails to extend effective context despite stable long-context perplexity"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Appendix K analyzes fact position effects for GPT-4, finding middle-of-context is hardest, consistent with lost-in-the-middle findings"
  - target: 2025-07-longbench-v2
    type: complementary
    detail: "LongBench v2 cites BABILong as part of the synthetic benchmark landscape; provides complementary evaluation using fully natural documents"
  - target: 2025-07-nolima-long-context-evaluation
    type: complementary
    detail: "NoLiMa notes BABILong counting achieves only 28% at 0K, confounding task difficulty with context-length difficulty; NoLiMa isolates context-length effects by ensuring high base scores"
  - target: 2025-04-effective-context-length-falls-short
    type: complementary
    detail: "Both find that models use only a fraction of their claimed context; complementary evidence from different evaluation methodologies"
  - target: 2020-04-compressive-transformer-pg19
    type: uses-benchmark
    detail: "Uses PG-19 books (introduced by Rae et al., 2020) as the background 'haystack' text for embedding reasoning facts"
  - target: 2024-03-gemini-1.5-long-context
    type: evaluates
    detail: "BABILong evaluates Gemini 1.5 Pro on reasoning-in-a-haystack tasks; achieves ~64K effective context on QA1"
  - target: 2024-08-flenqa-input-length-reasoning
    type: complementary
    detail: "FlenQA demonstrates reasoning degradation at short lengths (250-3000 tokens) with controlled padding, complementing BABILong's evaluation at much longer contexts (up to 10M tokens)"
  - target: 2024-11-genuinely-difficult-long-context
    type: complementary
    detail: "Goldman et al. classify BABILong tasks across all four quadrants of their scope-dispersion taxonomy, from low-dispersion retrieval tasks (1, 4-6, 9-10) to high-dispersion reasoning (14-20) and coreference resolution (11, 13)"
open_questions:
  - question: "Can optimized RAG pipelines recover reasoning performance on multi-fact tasks?"
    addressed_by: null
  - question: "How do different background text sources (beyond PG19 and Wikipedia) affect task difficulty?"
    addressed_by: null
  - question: "Can recurrent memory models generalize to more complex reasoning tasks beyond QA1-QA5?"
    addressed_by: null
  - question: "Can the BABILong framework be extended with more complex reasoning sources (e.g., Ruletaker, ProofWriter, FOLIO) for harder evaluation?"
    addressed_by: null
  - question: "Does fine-tuning on BABILong tasks transfer across tasks, or does it lead to task-specific overfitting?"
    addressed_by: null
---
# BABILong: Testing the Limits of LLMs with Long Context Reasoning-in-a-Haystack

**Authors:** Yuri Kuratov, Aydar Bulatov, Petr Anokhin, Ivan Rodkin, Dmitry Sorokin, Artyom Sorokin, Mikhail Burtsev (AIRI, Moscow; Neural Networks and Deep Learning Lab, MIPT, Dolgoprudny; London Institute for Mathematical Sciences, London)
**Date:** December 2024, NeurIPS 2024 Datasets and Benchmarks Track, Spotlight (arXiv:2406.10149)

---

## Core Research Problem

Existing long-context benchmarks fail to keep pace with the rapidly growing context windows of LLMs. Benchmarks such as LongBench (Bai et al., 2023) and L-Eval (An et al., 2023) scale only to 40K tokens, while models claim to support hundreds of thousands to millions of tokens (Section 1). The dominant synthetic evaluation -- the vanilla needle-in-a-haystack (NIAH) test (Kamradt, 2023) -- is overly simplistic: most modern models achieve near-perfect performance on it, producing "fully green numbers" that do not differentiate between models (Reid et al., 2024; Cohere, 2024; Liu et al., 2024a; Wang et al., 2024c) (Section 1).

More critically, the vanilla NIAH test evaluates only single-fact retrieval. It does not test whether models can reason over multiple facts scattered across a long context. Meanwhile, realistic benchmarks (ZeroSCROLLS, LongBench, InfinityBench) lack controllable sequence length and confound long-context utilization with parametric knowledge. An additional problem is that most NLP benchmarks are vulnerable to data leakage into LLM training sets (Sainz et al., 2023) (Section 2).

**The core challenge is how to build a scalable, controllable, contamination-proof benchmark that tests genuine reasoning -- not just retrieval -- across arbitrarily long contexts.**

---

## Problem Solutions

BABILong extends the bAbI benchmark (Weston et al., 2016) -- 20 reasoning tasks designed as prerequisites for conversational AI -- by embedding task facts within long natural text from the PG19 corpus (Rae et al., 2020).

1. **Reasoning-in-a-haystack design.** Task-relevant facts (e.g., "Mary moved to the office") are interspersed between sentences drawn from PG19 books, creating a signal-in-noise problem that scales to arbitrary length (Figure 1a, Section 2).
2. **20 diverse reasoning tasks.** The tasks cover single-fact retrieval (QA1), multi-fact chaining (QA2, QA3), spatial reasoning (QA4), three-argument relations (QA5), yes/no questions (QA6), counting (QA7), lists/sets (QA8), negation (QA9), indefinite knowledge (QA10), and ten additional tasks testing induction, deduction, coreference, and path finding (QA11-QA20) (Table 1, Section 2).
3. **Scalable generation.** Because both the facts and the background text are generated or drawn from large corpora, BABILong can produce evaluation samples at any desired length, with predefined splits from 0K to 10M tokens (Section 2).
4. **Contamination immunity.** Because bAbI facts are procedurally generated, BABILong is immune to data leakage from LLM pretraining corpora (Section 2).

---

## Approach Details

### Method

BABILong constructs evaluation samples by interleaving sentences from a bAbI task instance with sentences from PG19 books in their natural order. Background sentences are added until the sample reaches the target token length. The question appears at the end of the input. The model must (1) distinguish task-relevant facts from background text, (2) identify the subset of facts relevant to the question (supporting facts), and (3) perform the required reasoning to produce the answer (Section 2).

The 20 tasks are labeled QA1--QA20. They differ in the number of total facts (2--320), the number of relevant facts per question (1--10), and the type of reasoning required:

| Task | Name | Facts per Task | Relevant Facts | Reasoning Type |
|---|---|---|---|---|
| QA1 | Single supporting fact | 2--10 | 1 | Retrieval |
| QA2 | Two supporting facts | 2--68 | 2 | Two-hop chaining |
| QA3 | Three supporting facts | 4--320 | 3 | Three-hop chaining |
| QA4 | Two arg relations | 2--6 | 1 | Spatial reasoning |
| QA5 | Three arg relations | 2--126 | 1 | Argument tracking |
| QA6 | Yes/no questions | 2--26 | 1 | Boolean reasoning |
| QA7 | Counting | 2--52 | 1--10 | Aggregation |
| QA8 | Lists/sets | 2--50 | 1--8 | Set operations |
| QA9 | Simple negation | 2--10 | 1 | Negation |
| QA10 | Indefinite knowledge | 2--10 | 1 | Uncertainty |

(Table 1, Section 2)

### Key Technical Components

**Background text selection.** PG19 was chosen because its narrative style (people, locations, actions) is distributionally similar to bAbI facts, making the filtering task non-trivial. The similarity between task facts and background text is a deliberate design choice: it prevents models from relying on superficial distributional cues (Section 2). Wikipedia was also tested as an alternative background source (Appendix G).

**Evaluation metric.** Accuracy is measured by exact match of the generated answer. Performance is considered satisfactory at >85% and a complete failure at <30% (Section 3.1).

**Few-shot prompting.** Each evaluation prompt begins with a task description and 2--3 in-context examples inside `<example>` tags, followed by the long context inside `<context>` tags, and a duplicated question after the context (Appendix J).

**Data contamination resistance.** Because bAbI facts are procedurally generated, BABILong is immune to data leakage from LLM pretraining corpora (Section 2).

**Length measurement.** Token lengths are measured using the GPT-2 tokenizer, which is close in fertility to the GPT-4 tokenizer. Actual token counts vary by model tokenizer (e.g., 128K GPT-2 tokens = ~123K GPT-4 tokens = ~137K Llama-2 tokens) (Table 5, Appendix F).

**RMT memory mechanism.** Analysis of RMT memory states (Appendix H, Figure 8) reveals that the model learns to distinguish facts from distractor text: memory states remain similar to initialization in the absence of task facts but change visibly when a fact is encountered. Attention maps show concentrated patterns when writing facts to and reading facts from memory, confirming the model stores task-relevant information in its recurrent memory tokens.

### Experimental Setup

**Models evaluated (34+):**
- **8K--32K context:** LLaMA-2-7B-32K, LongChat-7b-v1.5-32k, LongAlpaca-13B, LLama-3-8B
- **32K--64K:** Mistral-7B-Instruct-v0.1/v0.2/v0.3, Mixtral-8x7B, Mixtral-8x22B
- **128K:** ChatGLM3-6b, LLama-3.1-8B/70B, Phi-3-mini/medium, Phi-3.5-mini/MoE, Command-R/R-Plus, Qwen-2.5-7B/72B, Jamba-v1, GPT-4o-mini
- **200K:** Yi-9B/34B-200K
- **Closed-source:** GPT-4 (gpt-4-0125-preview), Gemini 1.5 Pro 002
- **Long-context adaptations:** YaRN-Mistral, Activation Beacon (LLama-2, Mistral)
- **Alternative architectures:** Mamba-2.8B, RWKV-v5-7b, RWKV-v6, RecurrentGemma-9B
- **Fine-tuned small models:** RMT (137M), ARMT (137M), Mamba (130M)
- **RAG pipelines:** GPT-4 + RAG-C/RAG-S (FAISS + text-embedding-ada-002), Llama3-ChatQA-1.5-8B + RAG-S (nvidia/dragon encoder)

(Table 2, Section 3; Appendix D, Table 4)

**Evaluation:** 1000 samples per task per length for lengths up to 32K; 100 samples per task per length for longer sequences. Predefined splits at 0K, 1K, 2K, 4K, 8K, 16K, 32K, 64K, 128K, 512K, 1M, and 10M tokens (Section 3, Appendix F).

**Fine-tuning:** RMT uses GPT-2 (137M) backbone with 512-token segments and 16 memory tokens. ARMT uses GPT-2 with 10 memory tokens, memory dimension 64, and DPFP-3 non-linearity. Curriculum training from 1 to 32 segments (up to 16K tokens). Mamba-130M uses the same curriculum approach with batch size 128. AdamW optimizer; learning rate 5e-5 to 3e-5 for RMT, 1e-4 for ARMT, 4e-4 for Mamba; batch size 64 (RMT/ARMT) or 128 (Mamba). Each curriculum stage has up to 10,000 steps with early stopping. Training on 1--4 Nvidia A100/H100 GPUs, 40 minutes to 20 hours per stage. Three runs per experiment with different seeds (Appendix C).

**Reproducibility:** Code at https://github.com/booydar/babilong, dataset at https://huggingface.co/datasets/RMT-team/babilong. Predictions of all models released. Code under Apache 2.0 license; PG19 under Apache 2.0; bAbI under BSD (Appendix A).

### Key Results

**Effective context utilization (QA1):**

On QA1 (single supporting fact), the majority of models maintain >85% accuracy only up to 4K tokens. Exceptions: LLama-3.1-8B and LLama-3.1-70B extend to 16K; Qwen-2.5-72B and Gemini 1.5 Pro extend to 64K. The range of full context utilization on QA1 varies from 5% to a maximum of 50% (Figure 2, Section 3.1). Only 23 out of 34 tested LLMs achieved 85%+ accuracy on any QA1--QA3 task even without background text (strong evidence: 34 models, 1000 samples per configuration up to 32K).

**Table 2 results (average accuracy over QA1--QA5, selected models):**

| Model | 0K | 4K | 16K | 32K | 64K | 128K |
|---|---|---|---|---|---|---|
| GPT-4 | 76% | 52% | [not in notes] | [not in notes] | [not in notes] | [not in notes] |
| Gemini 1.5 Pro 002 | [not in notes] | [not in notes] | [not in notes] | [not in notes] | [not in notes] | [not in notes] |
| Qwen-2.5-72B | [not in notes] | [not in notes] | [not in notes] | [not in notes] | [not in notes] | [not in notes] |
| LLama-3.1-70B | [not in notes] | [not in notes] | [not in notes] | [not in notes] | [not in notes] | [not in notes] |

Note: Table 2 in the paper contains full results for all models; the section notes capture only selected values from this dense table. The notes confirm GPT-4 at 76% (0K) and 52% (4K) as averages over QA1-QA5 (Section 3).

**Per-task results from Table 4 (Appendix D, selected models):**

| Model | QA1 0K | QA1 4K | QA1 128K | QA2 0K | QA3 0K |
|---|---|---|---|---|---|
| GPT-4 | 93% | 58% | [not in notes] | 58% | 44% |
| RWKV-v5-7b | 95% | 100% | 98% | 43% | 28% |
| Mamba-2.8b | 93% | 100% | 100% | 88% | 56% |
| LLama-3-8b-instruct | 85% | 52% | [not in notes] | 44% | [not in notes] |
| Mistral-7b-instruct | 67% | 50% | [not in notes] | [not in notes] | [not in notes] |

(Table 4, Appendix D; values copied directly from section notes)

- **Multi-fact reasoning degrades sharply.** On QA2, only a few models solve the task without background text. On QA3, no LLM exceeds 80% even at 0K (Figure 2, Section 3.1).
- **Mamba-2.8B (pretrained) excels on QA1:** achieves 100% accuracy on QA1 even at 128K tokens. Also shows strong QA2 performance (88% at 0K). RWKV-v5-7b similarly shows strong QA1 results (95% at 0K, 100% at 1K--8K, 98% at 128K) (Table 4, Appendix D).
- **Context extension methods largely fail.** YaRN does not extend to longer contexts despite stable perplexity (Peng et al., 2023b). LongChat, LLama-2-7B-32K, and LongAlpaca fail even at their trained length of 32K. Activation Beacon improves over YaRN but still achieves <40% at 32K (Section 3.1).
- **Multistage pre-training helps.** LLama-3.1 uses six-stage pre-training from 8K to 128K with supervised fine-tuning on long context data, showing significant improvement. LLama-3.1-70B outperforms GPT-4 on longer contexts. Qwen-2.5 models outperform LLama-3.1 of similar size and achieve the best results of all evaluated open LLMs (Section 3.1).

**RAG results (QA1 task, Figure 3a, Section 3.2):**

| Method | Description |
|---|---|
| GPT-4 + RAG-C top-5 | Chunk retrieval (512 tokens) fails to improve GPT-4 performance on long-context tasks |
| GPT-4 + RAG-S top-5 | Sentence-level retrieval outperforms chunk retrieval, with improvement visible after 16K context |
| GPT-4 + RAG-S top-20 | Increasing retrieved sentences from top-5 to top-20 does not help |
| Llama3-ChatQA-1.5-8B + RAG-S | Strong advantage of being able to perform on any context length up to 10M tokens |

- **RAG fails on multi-fact tasks.** Sentence-level retrieval (RAG-S) outperforms chunk retrieval (RAG-C), but accuracy on QA2 and QA3 drops below random guessing. The retrieval system cannot recover all supporting facts because not all relevant facts are semantically similar to the question. The retrieval algorithm lacks temporal consideration (Section 3.2, Figure 3a).

**Fine-tuned models (Figure 3b, Section 3.3):**

- **Fine-tuned small models outperform LLMs.** RMT and ARMT with GPT-2 backbone (137M parameters) significantly outperform GPT-4 despite being ~1000x smaller (Section 3.3).
- **ARMT processes up to 50 million tokens** -- a record for single-model sequence processing (Rodkin et al., 2024). Achieves 77% on QA1 at 50M tokens (Figure 1b).
- **RMT scales to 11.1M tokens**, over 600x its training length of 16K tokens, with consistent performance up to 128K and only marginal quality degradation beyond (Section 3.3).
- **Mamba-130M (fine-tuned) excels at medium lengths.** Achieves the best overall results across QA1--QA5 and greatly outperforms RAG, but inference beyond 128K is extremely slow due to technical limitations, making it nearly impossible to process longer sequences (Section 3.3).
- **Mamba has an edge on complex tasks:** outperforms RMT/ARMT on tasks like QA3 that require remembering a large number of facts (Table 4, Section 3.3).
- **RMT performance varies between training seeds.** Three runs with different memory initializations and dataset shuffles show variation on context lengths exceeding training length (Figure 5, Appendix C).

**GPT-3.5 and Mistral-7B fine-tuning (Appendix I, Figure 9):**

- Fine-tuning dramatically improves QA1 performance, making scores uniform across all input sizes (both achieve 90%+ accuracy).
- GPT-3.5 fine-tuned for QA1 shows improved performance on QA2--QA5 tasks as well.
- Full fine-tuning of Mistral-7B on QA1 results in **degraded scores for other tasks** (QA2--QA5), suggesting task-specific overfitting (Appendix I).
- Both remain behind fine-tuned Mamba, RMT, and ARMT (Appendix I).

### Comparison with RULER and MMLU

BABILong's correlation with MMLU is high at short contexts (R^2 = 0.888 at 0K on QA2) and decreases as length grows. RULER maintains near-constant correlation with MMLU regardless of length (R^2 = 0.928 at <=128K). Comparing at RULER's most correlated lengths (<=128K and 64K), BABILong shows much lower correlation: 0.928 vs. 0.435 and 0.910 vs. 0.455, respectively (Figure 4, Section 3.4). This indicates that **BABILong captures differences in long-context behavior starting from 2K tokens**, while RULER requires 128K+ tokens to differentiate models from MMLU (moderate evidence: correlation analysis across available models on both benchmarks).

### Fact Position Effects

GPT-4-Turbo performance varies significantly by fact position within the context (Appendix K, Figure 10). On QA1:

| Depth | 4K | 8K | 16K | 32K | 64K |
|---|---|---|---|---|---|
| 75 (near end) | 96% | 88% | 68% | 40% | 32% |
| 50 (middle) | 100% | 92% | 44% | 24% | 36% |
| 25 (near start) | 100% | 92% | 72% | 44% | 32% |
| 0 (beginning) | 92% | 100% | 80% | 64% | 20% |

The most difficult location is the **middle of context** (depth = 50), consistent with lost-in-the-middle findings. All positions show degradation as context length increases (Appendix K).

### Gemini Content Safety Filtering

Gemini 1.5 Pro 002 refused to respond up to **14% of the time** at longer context sizes due to built-in content safety filtering, even with BLOCK_NONE set. Results are reported both with and without rejected requests (Appendix E, Figure 6).

---

## Limitations and Failure Modes

1. **Limited background text sources.** Only PG19 and Wikipedia were tested as background text; other sources may affect difficulty differently. Interference between similar facts in the background text can increase difficulty (Limitations section).
2. **Unoptimized RAG.** The retrieval component was not optimized; better RAG pipelines might improve performance. The selected prompts could be suboptimal (Limitations section).
3. **Limited vocabulary in facts.** bAbI uses small vocabularies for names and objects, making the task easier for fine-tuned models that can learn to detect fact-specific tokens. Distractor facts partially mitigate this (Limitations section).
4. **Alternative fact sources not explored.** The paper suggests incorporating tasks from Ruletaker, ProofWriter, FOLIO, PrOntoQA, LogicNLI, and DELTA for more complex scenarios, but these were not tested (Limitations section).
5. **Recurrent models limited by sequential processing.** RMT and ARMT are hindered by their sequential nature, reducing parallelizability, and have finite memory storage capacity (Limitations section).
6. **[Inferred]** No systematic position control analysis in the main evaluation. The main results do not condition on fact position within the context, though Appendix K provides a GPT-4-specific depth analysis.
7. **[Inferred]** Gemini content safety filtering causes up to 14% request denials at longer contexts, potentially biasing results (Appendix E).
8. **[Inferred]** Mistral-7B fine-tuning shows task-specific overfitting (QA2--QA5 degrade after QA1 fine-tuning), raising questions about generalization of fine-tuning approaches (Appendix I).

#### Scope and Comparability

- **What was not tested:** Tasks QA6--QA20 were not evaluated for most LLMs (Table 4 covers only QA1--QA5 for the full model set). Non-English languages were not tested, though the paper notes adding new languages is straightforward. Models were not tested with chain-of-thought prompting or other advanced prompting strategies.
- **Comparability notes:** BABILong uses exact-match accuracy on short generated answers, which differs from benchmarks like RULER that may use different scoring (e.g., substring matching). The GPT-2 tokenizer is used for length measurement, so actual token counts differ across model tokenizers (Table 5). The "0K" baseline includes bAbI facts with no background text, which tests base reasoning ability rather than long-context ability, making cross-benchmark comparison at this length ambiguous. BABILong's QA1 is comparable to multi-needle NIAH but QA2--QA20 have no direct counterpart in RULER or other NIAH-style benchmarks.

---

## Conclusions

### Contributions

1. **Scalable reasoning-in-a-haystack benchmark.** BABILong provides 20 diverse reasoning tasks that can be generated at any length (predefined splits up to 10M tokens), going far beyond the single-fact retrieval of vanilla NIAH (Section 2, Table 1).
2. **Comprehensive model evaluation.** Evaluated 34+ models spanning open-source LLMs, commercial APIs, context extension methods, alternative architectures (Mamba, RWKV), RAG pipelines, and fine-tuned small models on a consistent benchmark (Table 2, Table 4).
3. **Quantified effective context utilization.** Demonstrated that LLMs use only 10--20% of their claimed context window on QA1, with the effective range varying from 5% to a maximum of 50% (Figure 2, Section 3.1).
4. **Exposed RAG failure on multi-hop tasks.** Showed that standard retrieval pipelines achieve modest performance on single-fact QA but collapse on two- and three-fact tasks because retrieval cannot recover all supporting facts (Figure 3a, Section 3.2).
5. **Record sequence processing.** Demonstrated that ARMT with a 137M-parameter backbone processes up to 50 million tokens, with RMT generalizing over 600x beyond its training length to 11.1M tokens (Figure 1b, Section 3.3).
6. **Contamination-proof design.** Because facts are procedurally generated, BABILong is immune to data leakage from LLM pretraining corpora (Section 2).

### Implications

1. **Short-context evaluation is insufficient.** BABILong's divergence from MMLU starting at 2K tokens suggests that short-context benchmarks cannot predict long-context behavior, and dedicated long-context evaluation is necessary (Section 3.4).
2. **Recurrent memory may be key for ultra-long contexts.** The strong performance of RMT and ARMT at 10--50M tokens suggests that recurrent memory mechanisms may be more effective than attention-based approaches for extreme sequence lengths (speculative -- tested only on BABILong tasks with small models).
3. **RAG requires fundamental improvements for multi-hop reasoning.** The failure of standard RAG on QA2 and QA3 suggests that retrieval systems need temporal awareness and multi-hop retrieval capabilities (Section 3.2).
4. **Perplexity does not predict task performance.** YaRN shows stable long-context perplexity but fails on BABILong, indicating that perplexity alone is insufficient for evaluating context extension methods (Section 3.1).

---

## Key Claims

1. **C1: LLMs effectively utilize only 10--20% of their claimed context window.** On QA1 (single supporting fact), the majority of models maintain >85% accuracy only up to 4K tokens; GPT-4 and LLama-3.1-70B extend to 16K; Qwen-2.5-72B and Gemini 1.5 Pro to 64K. The range of full context utilization varies from 5% to a maximum of 50% (Figure 2, Section 3.1). **Scope:** QA1 single-fact retrieval, 34 models, few-shot prompting. **Magnitude:** majority capped at 4K out of 128K claimed. **Evidence breadth:** tested across 34 models with 1000 samples per configuration (strong evidence). **Status: supported.**

2. **C2: BABILong provides 20 controllable reasoning tasks scalable to arbitrary length.** The benchmark includes predefined splits from 0K to 10M tokens, with evaluation demonstrated up to 50M tokens. Tasks cover retrieval, multi-hop chaining, spatial reasoning, counting, negation, and more (Table 1, Section 2). **Scope:** English only, bAbI reasoning tasks, PG19 background text. **Magnitude:** 20 tasks, splits to 10M, evaluations to 50M. **Status: supported.**

3. **C3: RAG fails on multi-fact reasoning tasks.** RAG-S (sentence-level retrieval) shows scalable but weak performance on QA1 but drops below random guessing on QA2 and QA3 at 128K. The retrieval system cannot recover all supporting facts because not all facts are semantically similar to the question (Figure 3a, Section 3.2). **Scope:** GPT-4 + FAISS, Llama3-ChatQA, unoptimized retrieval. **Magnitude:** QA2/QA3 accuracy below random guessing. **Evidence breadth:** tested with two LLMs, two retrieval granularities, multiple top-k settings (moderate evidence). **Status: supported.**

4. **C4: Fine-tuned recurrent memory transformers process up to 50M tokens.** ARMT with GPT-2 backbone (137M parameters) achieves 77% on QA1 at 50M tokens and 89% at 10M, outperforming LLMs that are 1000x larger. RMT generalizes to 11.1M tokens, over 600x its training length (Figure 1b, Figure 3b, Section 3.3). **Scope:** QA1 single-fact task, GPT-2 backbone, curriculum training. **Magnitude:** ARMT 77% at 50M, RMT 600x generalization. **Evidence breadth:** three runs per configuration with different seeds (moderate evidence). **Status: supported.**

5. **C5: Context extension methods fail to extend effective context.** YaRN fails despite stable long-context perplexity. LongChat, LongAlpaca, and LLama-2-7B-32K fail at their trained 32K length. Activation Beacon achieves <40% at 32K (Section 3.1, Table 2). **Scope:** YaRN-Mistral, Activation Beacon on LLama-2/Mistral, 32K--128K range. **Magnitude:** YaRN no improvement; Activation Beacon <40% at 32K. **Status: supported.**

6. **C6: BABILong differentiates models at shorter lengths than RULER.** BABILong's correlation with MMLU drops from R^2 = 0.888 (QA2, 0K) as length increases, while RULER maintains R^2 = 0.928 at <=128K. Comparing most-correlated lengths: RULER R^2 = 0.928 vs BABILong R^2 = 0.435, and RULER R^2 = 0.910 vs BABILong R^2 = 0.455 (Figure 4, Section 3.4). **Scope:** correlation analysis across available models on MMLU, RULER, and BABILong. **Magnitude:** BABILong diverges from 2K tokens; RULER requires 128K+. **Status: supported.**

7. **C7: BABILong is immune to data contamination.** Because bAbI facts are procedurally generated, the benchmark is immune to data leakage from LLM training corpora (Section 2). **Scope:** general. **Magnitude:** qualitative. **Status: supported.**

---

## Open Questions

1. **Can optimized RAG pipelines recover reasoning performance on multi-fact tasks?** The paper acknowledges that the retrieval component was not optimized. Better RAG pipelines with temporal awareness and multi-hop retrieval might improve performance on QA2 and QA3 (Limitations section). Not yet addressed.

2. **How do different background text sources affect task difficulty?** Only PG19 and Wikipedia were tested. Other text sources with different distributional properties may make fact filtering easier or harder (Limitations section). Not yet addressed.

3. **Can recurrent memory models generalize to more complex reasoning tasks beyond QA1--QA5?** While ARMT achieves record performance on QA1 at 50M tokens, Mamba outperforms it on more complex tasks like QA3 (Table 4, Section 3.3). The generalization of recurrent memory to harder reasoning remains open. Not yet addressed.

4. **Can the BABILong framework be extended with more complex reasoning sources?** The paper suggests incorporating tasks from Ruletaker, ProofWriter, FOLIO, PrOntoQA, LogicNLI, and DELTA for harder evaluation (Limitations section). Not yet addressed.

5. **Does fine-tuning on BABILong tasks transfer across tasks, or does it lead to task-specific overfitting?** GPT-3.5 fine-tuned on QA1 generalizes to QA2--QA5, while Mistral-7B shows degraded QA2--QA5 performance after QA1 fine-tuning (Appendix I, Figure 9). The conditions governing transfer vs. overfitting remain unexplored. Not yet addressed.

---

## Core References and Why They Are Referenced

### Benchmark Foundations

- **Weston et al. (2016)** -- *Towards AI-Complete Question Answering: A Set of Prerequisite Toy Tasks (bAbI).* The source of the 20 reasoning tasks that BABILong extends to long contexts. BABILong inherits bAbI's task design, fact structure, and vocabulary.
- **Rae et al. (2020)** -- *Compressive Transformers for Long-Range Sequence Modelling (PG19).* Provides the background text corpus (books published before 1919) used as the "haystack" in BABILong.
- **Kamradt (2023)** -- *Needle In A Haystack (LLMTest).* The vanilla NIAH test that BABILong addresses as overly simplistic. BABILong replaces single-fact retrieval with multi-fact reasoning.

### Long-Context Evaluation Benchmarks

- **Hsieh et al. (2024)** -- *RULER: What's the Real Context Size of Your Long-Context Language Models?* The closest comparable benchmark. BABILong and RULER share the NIAH extension concept, but RULER uses more synthetic haystacks (repeated noise sentences) and does not test multi-hop reasoning as deeply. Section 3.4 compares their MMLU correlations.
- **Bai et al. (2023)** -- *LongBench.* A bilingual long-context benchmark limited to 40K tokens. BABILong contrasts with LongBench's lack of controllable length and reliance on parametric knowledge.
- **Shaham et al. (2023)** -- *ZeroSCROLLS.* A zero-shot long-context benchmark that BABILong compares against as lacking controllable context length.
- **Zhang et al. (2024b)** -- *InfinityBench.* Extends long-context evaluation beyond 100K tokens. BABILong goes further with splits up to 10M tokens and evaluations to 50M.
- **Song et al. (2024b)** -- *Counting-Stars.* Another scalable NIAH-style benchmark that introduces aggregation tasks. BABILong provides more diverse reasoning categories (20 tasks vs. Counting-Stars' single task type).

### Models and Architectures

- **Reid et al. (2024)** -- *Gemini 1.5.* The top-performing commercial model on BABILong, maintaining strong performance up to 64K tokens on QA1.
- **Dubey et al. (2024)** -- *The Llama 3 Herd of Models.* LLama-3.1-70B outperforms GPT-4 on longer contexts. Uses multistage pre-training from 8K to 128K with progressive length increases.
- **Gu & Dao (2023)** -- *Mamba: Linear-Time Sequence Modeling with Selective State Spaces.* Both pretrained Mamba-2.8B and fine-tuned Mamba-130M achieve strong results on BABILong, but Mamba is impractical beyond 128K due to slow inference.
- **Bulatov et al. (2022, 2024)** -- *Recurrent Memory Transformer / Beyond Attention.* RMT provides the backbone for the fine-tuned models that achieve record sequence processing (11.1M tokens for RMT, 50M for ARMT).
- **Rodkin et al. (2024)** -- *Associative Recurrent Memory Transformer (ARMT).* Achieves the record of 50M-token processing on BABILong QA1 by combining recurrent memory with trainable retrieval.
- **Peng et al. (2023a)** -- *RWKV: Reinventing RNNs for the Transformer Era.* RWKV-v5-7b achieves near-perfect QA1 accuracy across context lengths up to 128K in Table 4 without fine-tuning.

### Context Extension Methods

- **Peng et al. (2023b)** -- *YaRN: Efficient Context Window Extension.* Evaluated on BABILong; fails to extend effective context despite stable long-context perplexity.
- **Zhang et al. (2024a)** -- *Activation Beacon.* Evaluated as a context extension method; performs better than YaRN but still achieves <40% at 32K.

### Evaluation Infrastructure

- **Hendrycks et al. (2020)** -- *MMLU.* Used to compute cross-benchmark correlations showing that BABILong diverges from MMLU at shorter contexts than RULER does.
- **Sainz et al. (2023)** -- *NLP Evaluation in Trouble.* Cited to motivate the need for contamination-resistant benchmarks, as most NLP benchmarks are vulnerable to data leakage.
