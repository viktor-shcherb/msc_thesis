---
title: "Effective Long-Context Scaling of Foundation Models"
authors: "Xiong, Liu, Molybog, Zhang, Bhargava, Hou, Martin, Rungta, Sankararaman, Oguz, Khabsa, Fang, Mehdad, Narang, Malik, Fan, Bhosale, Edunov, Lewis, Wang, Ma"
year: 2024
venue: "NAACL 2024"
paper_type: conference-paper
categories: ["context-extension", "position-encoding", "model-release"]
scope: ["RoPE-based LLMs", "continual pretraining", "long-context scaling", "Llama 2 family"]
benchmarks_used: ["humaneval", "mbpp", "gsm8k", "math-hendrycks", "mmlu", "natural-questions", "triviaqa", "hellaswag", "winogrande", "arc", "piqa", "siqa", "csqa", "openbookqa", "qasper", "zeroscrolls", "l-eval", "truthfulqa", "toxigen", "bold"]
models_introduced: ["llama-2-long-7b", "llama-2-long-13b", "llama-2-long-34b", "llama-2-long-70b"]
models_evaluated: ["llama-2-7b", "llama-2-13b", "llama-2-70b", "gpt-3.5-turbo", "gpt-4", "mpt-7b", "claude-2.1"]
key_claims:
  - id: C1
    claim: "RoPE base frequency adjustment (ABF) outperforms Position Interpolation (PI) for long-context extension"
    evidence: "Table 5, Table 6, Figure 5, Section 4.1"
    status: supported
    scope: "Llama 2 7B, 80B continual pretraining tokens, 32k context"
    magnitude: "Perplexity 6.323 vs 6.341 (Books); HumanEval 17.07 vs 15.24; MMLU 46.24 vs 45.84; FIRST-SENTENCE-RETRIEVAL maintained to 32k (PI degrades at 24k+)"
  - id: C2
    claim: "Validation loss follows power-law scaling with context length: L(c) = (alpha/c)^beta + gamma"
    evidence: "Figure 1, Section 3.1"
    status: supported
    scope: "Llama 2 Long 7B-70B, up to 32k context, validation data"
    magnitude: "beta ranges from 0.45 (7B) to 0.51 (70B); for 70B, doubling context reduces loss by factor 2^{-0.51} ~ 0.70"
  - id: C3
    claim: "Long-context continual pretraining saves ~40% FLOPs compared to pretraining from scratch with no performance loss"
    evidence: "Table 10, Table 11, Section 4.4"
    status: supported
    scope: "7B model, 32k context, 4k->32k curriculum switch at 80%"
    magnitude: "2.270 x 10^22 FLOPs (4k->32k @ 80%) vs 3.783 x 10^22 (32k from scratch) = 40% reduction; perplexity equivalent (6.49 vs 6.52 Books); QA tasks comparable"
  - id: C4
    claim: "Data quality matters more than length distribution for long-context continual pretraining"
    evidence: "Table 7, Table 8, Section 4.2"
    status: supported
    scope: "7B model ablations, 4 data mix configurations"
    magnitude: "Removing long texts still achieves most gains (NarrativeQA 19.48% vs 23.70% with new data); upsampling long texts (22.15%) no consistent advantage over removing long texts (19.48%)"
  - id: C5
    claim: "Llama 2 Long 70B Chat outperforms gpt-3.5-turbo-16k on 7/10 ZeroSCROLLS tasks without human-annotated long data"
    evidence: "Table 4, Section 3.2"
    status: supported
    scope: "70B instruction-tuned model, ZeroSCROLLS benchmark, synthetic self-instruct data only"
    magnitude: "Average 37.7 vs 36.7; wins on GR (26.0 vs 24.3), QM (20.0 vs 17.4), Qspr (52.0 vs 50.0), Nrtv (31.7 vs 29.5), QALT (82.6 vs 72.0), SpDg (55.5 vs 54.1)"
  - id: C6
    claim: "Llama 2 Long improves over Llama 2 on short-context benchmarks, especially coding, math, and MMLU"
    evidence: "Table 1, Table 2, Section 3.1"
    status: supported
    scope: "All model sizes (7B-70B), standard short-context benchmarks"
    magnitude: "70B: Coding +2.5 (39.9 vs 37.4), Math +6.1 (41.3 vs 35.2), MMLU +2.8 (71.7 vs 68.9); outperforms GPT-3.5 on MMLU (71.7 vs 70.0) and GSM8K (65.4 vs 57.1)"
  - id: C7
    claim: "Calculating LM loss on long input prompts during instruction tuning gives consistent improvements on downstream tasks"
    evidence: "Table 9, Section 4.3"
    status: supported
    scope: "7B model, self-instruct QA data, 5 long-context tasks"
    magnitude: "With LM loss vs without: Qasper 38.9 vs 35.7, NarrativeQA 23.3 vs 22.3, QuALITY 77.3 vs 59.3, QMSum 18.5 vs 13.4"
cross_references:
  - target: 2023-07-llama-2-open-foundation-chat
    type: extends
    detail: "Llama 2 Long is built through continual pretraining from Llama 2 checkpoints with 400B additional tokens"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Modifies RoPE's base frequency from 10,000 to 500,000 to reduce attention decay for distant tokens"
  - target: 2023-06-pi-positional-interpolation
    type: contradicts
    detail: "Shows that RoPE ABF outperforms Position Interpolation on perplexity, retrieval, and downstream tasks (Table 5, Table 6)"
  - target: 2024-05-yarn-context-extension
    type: complementary
    detail: "YaRN evaluated as baseline; Llama 2 Long 7B outperforms Yarn-7B-128k and Yarn-13B-128k on long-context tasks (Table 3)"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: uses-benchmark
    detail: "Uses ZeroSCROLLS for instruction-tuned model evaluation, outperforming gpt-3.5-turbo-16k on 7/10 tasks"
  - target: 2024-08-l-eval-standardized-evaluation
    type: uses-benchmark
    detail: "Evaluates on L-Eval tasks including Coursera, TPO, TopicRetrieval, FinQA, ContractQA, NaturalQuestions (Table 17)"
  - target: 2022-12-flashattention
    type: complementary
    detail: "Uses FlashAttention for efficient training with negligible GPU memory overhead when increasing sequence length"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "Compares to ALiBi's approach; both address long-context via positional encoding modifications but RoPE ABF operates on RoPE-based models"
  - target: 2023-12-landmark-attention-infinite-context
    type: complementary
    detail: "Landmark attention cited as concurrent long-context work; their passkey task is noted as 'overly simple for context probing' (footnote 4)"
  - target: 2024-07-llama-3-herd-of-models
    type: extended-by
    detail: "Llama 3 adopts similar RoPE base frequency scaling approach for long-context extension"
  - target: 2025-07-lv-eval-long-context-benchmark
    type: complementary
    detail: "LV-Eval provides a controlled long-context evaluation framework with knowledge-leakage mitigation, complementing the training methods proposed in this paper"
open_questions:
  - question: "Why does the power-law exponent beta increase with model size (0.45 for 7B to 0.51 for 70B)?"
    addressed_by: null
  - question: "Can the training curriculum findings (40% FLOP savings) scale to longer contexts (64k+) and larger models?"
    addressed_by: null
  - question: "What is the optimal base frequency for different target context lengths beyond 32k?"
    addressed_by: 2024-07-longrope-context-extension
  - question: "Does the LM loss on input prompts generalize beyond QA tasks to other instruction tuning formats?"
    addressed_by: null
---
# Effective Long-Context Scaling of Foundation Models

**Authors:** Wenhan Xiong, Jingyu Liu, Igor Molybog, Hejia Zhang, Prajjwal Bhargava, Rui Hou, Louis Martin, Rashi Rungta, Karthik Abinav Sankararaman, Barlas Oguz, Madian Khabsa, Han Fang, Yashar Mehdad, Sharan Narang, Kshitiz Malik, Angela Fan, Shruti Bhosale, Sergey Edunov, Mike Lewis, Sinong Wang, Hao Ma (GenAI, Meta)
**Date:** June 2024, NAACL 2024; arXiv:2309.16039

---

## Core Research Problem

Large language models with robust long-context capabilities are primarily available through proprietary APIs (Anthropic, OpenAI). Existing open-source long-context models fall short in three ways: (1) they primarily measure long-context capabilities via language modeling loss and synthetic tasks, which do not demonstrate real-world effectiveness (Section 1); (2) they often overlook maintaining strong performance on standard short-context tasks, either bypassing evaluations or reporting degraded performance (Chen et al., 2023; Peng et al., 2023); and (3) there is no open recipe for building long-context models that match proprietary model performance.

A key technical limitation is that Llama 2's RoPE positional encoding imposes a heavy decay on attention scores for distant tokens -- the quantity E_{q,k}[RoPE(q, m)^T RoPE(k, n)] decays heavily as |m - n| increases (footnote 3, Section 4.1). Early experiments showed the model was unable to effectively attend beyond 4,000-6,000 tokens even after extensive long-context continual pretraining with the original architecture untouched (Section 4.1). The core challenge is: **how to extend Llama 2's context window to 32k tokens while improving (not degrading) performance on both long-context and short-context tasks.**

---

## Problem Solutions

The paper presents Llama 2 Long, a series of long-context LLMs supporting effective context windows of 32,768 tokens, built through:

1. **RoPE base frequency adjustment (ABF):** Increase the RoPE base frequency from b = 10,000 to b = 500,000, reducing the rotation angle per dimension and attenuating the attention score decay for distant tokens (Section 2.1, Section 4.1).

2. **Continual pretraining:** Train from Llama 2 checkpoints with 400B additional tokens formed as long sequences (32k for 7B/13B, 16k for 34B/70B), rather than pretraining from scratch (Section 2.1).

3. **Quality-focused data mix:** Up-sample long texts but prioritize data quality over length distribution; the quality of the data plays a more critical role than the length of texts (Section 4.2).

4. **Cost-effective instruction tuning:** Use Llama 2 Chat's RLHF data augmented with synthetic self-instruct long QA data generated by Llama 2 Chat itself, without any human-annotated long instruction data (Section 2.2).

---

## Approach Details

### Method

**RoPE Base Frequency Adjustment (ABF):**

RoPE maps position m to rotation angles via:

> f^{RoPE}(x, m)_j = (x_{2j} + ix_{2j+1}) e^{i b^{-2j/d} m}

where b = 10,000 is the base frequency and d is the model dimension. The attention score decays as relative position |m - n| increases (Figure 4). Increasing b to 500,000 reduces the rotation angles, which reduces the decaying effect for distant tokens. The idea is also concurrently suggested in the Reddit r/LocalLLaMA community and Roziere et al. (2023).

**Continual Pretraining:**

- 400B tokens over 100,000 steps for all models
- 7B/13B: 32,768-token sequences; 34B/70B: 16,384-token sequences
- Same number of tokens per batch as Llama 2 (4M tokens per gradient update)
- Learning rate: 2e-5 for 7B/13B, 1e-5 for 34B/70B (smaller LR critical for larger models to get monotonically decreasing validation losses)
- Cosine schedule with 2000 warm-up steps
- FlashAttention (Dao et al., 2022) for memory efficiency; ~17% speed loss when increasing from 4k to 16k for 70B
- No sparse attention applied: given Llama 2 70B's model dimension (h = 8192), attention only becomes a computation bottleneck beyond 49,152 tokens (6h) (Narayanan et al., 2021)

**Power-Law Scaling:**

Validation loss follows a power-law relationship with context length (Figure 1):

> L(c) = (alpha/c)^beta + gamma

Fitted parameters for each model size:

| Model | alpha | beta | gamma |
|---|---|---|---|
| Llama 2 Long 7B | 25.4 | 0.45 | 1.56 |
| Llama 2 Long 13B | 19.5 | 0.48 | 1.45 |
| Llama 2 Long 34B | 17.7 | 0.50 | 1.41 |
| Llama 2 Long 70B | 17.9 | 0.51 | 1.35 |

Larger models have larger beta, indicating they leverage contexts more effectively. For the 70B model, doubling context length reduces loss by a factor of 2^{-0.51} ~ 0.70 (tested across 4 model sizes; strong evidence for the power-law relationship within the 32k range).

### Key Technical Components

**Position Interpolation (PI) Comparison:**

PI (Chen et al., 2023) linearly scales input positions by alpha = L/L' so that positions in long sequences map to the original position range. Both PI and ABF reduce attention decay, but ABF provides higher granularity between consecutive position embeddings (Theorem 1, Appendix B).

Positional encoding variant comparison (all 7B models, 80B continual pretraining tokens, 32k sequences; single configuration per variant, no variance reported):

| PE Variant | Books PPL | CC PPL | Wikipedia PPL | HumanEval | Math | MMLU | HellaSwag | TQA |
|---|---|---|---|---|---|---|---|---|
| RoPE (baseline) | 6.548 | 6.816 | 3.802 | 14.63 | **3.62** | 45.69 | 76.31 | 65.23 |
| RoPE PI | 6.341 | 6.786 | 3.775 | 15.24 | 3.08 | 45.84 | 76.65 | **65.96** |
| RoPE ABF | **6.323** | **6.780** | **3.771** | **17.07** | 3.52 | **46.24** | **76.73** | 66.04 |
| xPOS ABF | 6.331 | **6.780** | **3.771** | 16.46 | 3.54 | 45.72 | 76.68 | **66.14** |

(Table 5 perplexity, Table 6 downstream tasks)

On the FIRST-SENTENCE-RETRIEVAL context probing task (Figure 5b): RoPE fails beyond 4k-8k tokens, PI degrades at 24k+, **RoPE ABF and xPOS ABF maintain near-100 ROUGE-L to 32k**. All variants except RoPE achieve perfect accuracy on the PASSKEY task, which the authors consider "overly simple for context probing" (footnote 4).

**xPos Comparison:**

xPos (Sun et al., 2022) smooths high-frequency oscillation in RoPE that could be undesirable for language modeling. However, with base frequency modification, xPos ABF does not outperform RoPE ABF on perplexity, downstream tasks, or extrapolation (Table 5, Table 6, Appendix C). The oscillation artifacts are not detrimental to language modeling (Section 4.1).

**Instruction Tuning Without Human Annotation:**

1. Take Llama 2 Chat's RLHF dataset ("RLHF V5")
2. Generate synthetic long QA data via self-instruct:
   - Select random chunk from long document
   - Prompt Llama 2 Chat to write QA pairs (two prompt types: normal and short answers)
   - Apply self-critique step for verification
   - Use original long document (truncated to model's max context) as context
3. Concatenate short instruction data as 16k sequences
4. For long data: add padding, process individually without truncation
5. **Key finding:** Calculating LM loss on long input prompts (not just output tokens) gives consistent improvements (Table 9, Section 4.3)

### Theoretical Analysis

Appendix B provides a formal comparison of ABF and PI through positional embedding granularity. The authors introduce a metric measuring the distance between consecutive embedding images using Euclidean sine similarity.

**Theorem 1** (Appendix B): For x in R^d and n in N, the Euclidean sine similarity between two consecutive images of a positional embedding is bounded by:

> (min_k x_k^2 / ||x||^2) C_d <= sin angle(f(x, n+1), f(x, n)) <= (max_k x_k^2 / ||x||^2) C_d

where in the limit d -> infinity:

> C_d ~ (log b + log beta)^{-1} for ABF
> C_d ~ alpha (log b)^{-1} for PI

With b = 10,000, alpha = 1/4 (PI for 4x extension), and beta = 50 (ABF, since 500,000/10,000 = 50), the granularity values are:
- **ABF:** C_d ~ (log 10,000 + log 50)^{-1} ~ 0.076
- **PI:** C_d ~ 0.25 * (log 10,000)^{-1} ~ 0.027

ABF provides **2.8x higher positional granularity** than PI, making it easier for the model to distinguish between positions. The relative distance between embedded vectors has a **logarithmic** dependence on the key parameter of ABF (beta) vs a **linear** dependence on the key parameter of PI (alpha), which explains why the base frequency is not very sensitive and can be easily adjusted (Section 4.1).

### Experimental Setup

**Models:** Llama 2 Long 7B, 13B, 34B, 70B; all continually pretrained from Llama 2 checkpoints.

**Short-context benchmarks:**
- Coding: HumanEval (0-shot), MBPP (3-shot)
- Math: GSM8K (8-shot), MATH (4-shot)
- Knowledge: MMLU (5-shot), NaturalQuestions (5-shot), TriviaQA (5-shot)
- Commonsense: PIQA, SIQA, HellaSwag, WinoGrande, ARC easy and challenge, OpenBookQA, CommonsenseQA

**Long-context benchmarks:**
- NarrativeQA (0-shot), QuALITY (2-shot), Qasper (2-shot), QMSum (1-shot)
- ZeroSCROLLS (10 tasks)
- L-Eval (6 tasks: Coursera, TPO, TopicRetrieval, FinQA, ContractQA, NaturalQuestions)

**Baselines:** Focused Transformer 3B, YaRN 7B/13B-128k, Together-7B-32k, Xgen-7B-8k, MPT-7B-8k/30B-8k, GPT-3.5-turbo, GPT-3.5-turbo-16k, GPT-4, Claude (8k), Llama 2 (7B-70B)

**Safety evaluation:** TruthfulQA, ToxiGen, BOLD -- compared against GPT-3.5-turbo, GPT-4, Claude-2, Falcon-instruct 40B, MPT-instruct 30B, Llama 2 Chat 70B (Table 12)

**Human evaluation:** 2,352 examples across multi-turn conversation and multi-document search query answering, each evaluated by 3 annotators (Figure 3)

**Reproducibility:** No code release mentioned. Training details fully specified (Section 2.1): learning rates, batch sizes, schedules, 400B tokens, 100k steps. Evaluation prompts described (footnote 2, Appendix D). Simple prompt format: "{CONTEXT} Q: {QUESTION}, A:". Maximum allowed prompt length 16,384 tokens for long-task comparisons. Single run per configuration, no variance reported (limited evidence for individual benchmark numbers).

### Key Results

**Short-context benchmarks (Table 1, Table 2):**

| Model | Size | Coding | Math | MMLU | Commonsense | OpenQA |
|---|---|---|---|---|---|---|
| Llama 2 | 7B | 16.8 | 8.55 | 45.3 | 63.9 | 48.9 |
| Llama 2 Long | 7B | 20.6 | 10.5 | 47.8 | 64.9 | 51.0 |
| Llama 2 | 13B | 24.5 | 16.3 | 54.8 | 66.9 | 55.4 |
| Llama 2 Long | 13B | 25.7 | 21.5 | 60.1 | 67.8 | 56.8 |
| Llama 2 | 34B | 27.8 | 24.2 | 62.6 | 69.9 | 58.7 |
| Llama 2 Long | 34B | 29.9 | 29.0 | 65.0 | 70.9 | 60.3 |
| Llama 2 | 70B | 37.4 | 35.2 | 68.9 | 71.9 | 63.6 |
| Llama 2 Long | 70B | **39.9** | **41.3** | **71.7** | **72.7** | **64.0** |

- Llama 2 Long **improves** over Llama 2 on all aggregated metrics across all model sizes (tested across 4 scales; strong evidence)
- 70B improvements: Coding +2.5, Math +6.1, MMLU +2.8, Commonsense +0.8, OpenQA +0.4
- Outperforms GPT-3.5 on MMLU (71.7 vs 70.0) and GSM8K (65.4 vs 57.1) (Table 2)
- Attributed to additional computation FLOPs and knowledge from newly introduced data (Section 3.1)

**Long-context benchmarks (Table 3):**

| Model | NarrativeQA F1 | Qasper F1 | QuALITY EM | QMSum ROUGE-geo |
|---|---|---|---|---|
| Focused Transformer (3B) | 16.3 | 15.4 | 20.5 | 10.6 |
| Yarn-7B-128k | 20.9 | 26.2 | 32.3 | 11.4 |
| Together-7B-32k | 23.3 | 27.3 | 41.2 | 12.6 |
| Xgen-7B-8k | 17.4 | 20.5 | 21.0 | 6.79 |
| MPT-7B-8k | 18.8 | 24.7 | 23.7 | 8.78 |
| Yarn-13B-128k | 23.4 | 27.1 | 46.4 | 11.9 |
| MPT-30B-8k | 22.9 | 29.0 | 41.5 | 10.3 |
| Llama 2 70B | 25.7 | 27.5 | 53.0 | 11.9 |
| Llama 2 Long 7B | 21.9 | 27.8 | 43.2 | 14.9 |
| Llama 2 Long 13B | 25.6 | 31.2 | 57.6 | 15.7 |
| Llama 2 Long 34B | 29.4 | 33.7 | 65.7 | 15.9 |
| Llama 2 Long 70B | **30.9** | **35.7** | **79.7** | **16.5** |

- Maximum prompt length set to 16,384 tokens for all models
- Together-7B-32k is finetuned with supervised data (not purely self-supervised), making comparison imperfect
- Performance improves monotonically as max context length increases for 70B (Figure 2): NarrativeQA 27.5->30.9, Qasper 28.9->35.7, QuALITY 63.9->79.7, QMSum 10.9->16.5 across 4k-16k prompt lengths

**ZeroSCROLLS instruction-tuned results (Table 4):**

| Model | GR | SS | QM | SQAL | Qspr | Nrtv | QALT | MuSQ | SpDg | BkSS | Avg |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GPT-3.5-turbo (4k) | 21.3 | 16.1 | 15.6 | 20.4 | 49.3 | 25.1 | 66.6 | 27.1 | 49.1 | 49.8 | 34.0 |
| GPT-3.5-turbo-16k | 24.3 | 16.2 | 17.4 | 21.4 | 50.0 | 29.5 | 72.0 | 27.0 | 54.1 | 54.6 | 36.7 |
| Claude (8k) | 24.2 | 16.1 | 14.6 | 21.0 | 52.3 | 32.6 | 84.8 | 36.1 | 61.6 | 47.4 | 39.1 |
| GPT-4 (8k) | 26.3 | 17.3 | 18.5 | 22.6 | 50.7 | 27.6 | 89.2 | 41.1 | 62.8 | 60.5 | 41.7 |
| Llama 2 Long Chat 70B | **26.0** | 15.0 | **20.0** | 20.9 | **52.0** | **31.7** | **82.6** | 27.3 | **55.5** | 46.2 | **37.7** |

- Outperforms GPT-3.5-turbo-16k on **7/10 tasks**: GR, QM, Qspr, Nrtv, QALT, SpDg, and Avg (single evaluation per configuration; limited evidence for individual task margins)
- Achieved without any human-annotated long-context data
- Still below Claude (8k) and GPT-4 (8k) overall (39.1 and 41.7 respectively)

**L-Eval results (Table 17, Appendix A):**

| Model | Coursera | TPO | TopicRetrieval | FinQA | ContractQA | NaturalQuestions |
|---|---|---|---|---|---|---|
| Claude 1.3 100k | **60.2** | 83.6 | 70.6 | - | - | - |
| gpt-3.5-turbo-16k | 59.7 | 69.9 | 69.3 | 45.4 | 24.9 | 45.9 |
| longchat-13b-16k | 36.8 | 55.4 | 33.3 | 37.9 | 21.1 | 22.8 |
| chatglm2-6b-8k | 47.2 | 54.6 | 10.0 | 34.8 | 16.4 | 17.6 |
| Llama 2 Long Chat | 52.9 | **81.8** | **76.0** | **47.3** | **25.5** | **66.7** |

- Best on 5/6 tasks among models compared; Coursera below Claude 1.3 100k and gpt-3.5-turbo-16k
- Particularly strong on QA tasks (NaturalQuestions 66.7 vs gpt-3.5-turbo-16k 45.9), consistent with the QA-focused self-instruct data

**Training curriculum ablation (Table 10, Table 11):**

| Curriculum | FLOPs | NarrativeQA F1 | Qasper F1 | Quality EM | QMSum ROUGE-geo |
|---|---|---|---|---|---|
| 32k from scratch | 3.783 x 10^22 | 18.5 | 28.6 | 37.9 | 11.46 |
| 4k->32k @ 20% | 3.405 x 10^22 | 20.0 | 28.1 | 38.8 | 12.09 |
| 4k->32k @ 40% | 3.026 x 10^22 | 20.1 | 27.0 | 37.4 | 12.44 |
| 4k->32k @ 80% | 2.270 x 10^22 | 18.5 | 25.0 | 38.3 | 11.00 |

| Curriculum | CC PPL | Books PPL | Wikipedia PPL |
|---|---|---|---|
| 32k from scratch | 7.67 | 6.52 | 4.31 |
| 4k->32k @ 20% | 7.59 | 6.46 | 4.26 |
| 4k->32k @ 40% | 7.59 | 6.46 | 4.25 |
| 4k->32k @ 80% | 7.59 | 6.49 | 4.25 |

- All curriculum models achieve **equivalent or better perplexity** than 32k-from-scratch (Table 11)
- Switching at 80% saves ~40% FLOPs (2.270 vs 3.783) with comparable long-context task performance, though Qasper drops (25.0 vs 28.6)
- Models quickly adapt to increased sequence length within a few thousand steps after switching (Figure 6)
- 7B scale only (single scale; limited evidence for generalization)

**Data mix ablation (Table 7, Table 8):**

| Data Mix | NarrativeQA Delta | Qasper Delta | Quality Delta | QMSum Delta | MMLU |
|---|---|---|---|---|---|
| Llama 2 Long data mix | **23.70%** | **43.64%** | **75.5%** | **45.70%** | **48.62** |
| Llama 2 data mix | 18.23% | 38.12% | 60.3% | 44.87% | 46.30 |
| - remove long text data | 19.48% | 39.14% | 67.1% | 36.60% | 46.25 |
| - upsample existing long | 22.15% | 36.82% | 65.0% | 42.83% | 46.25 |

(Delta values are relative improvement over Llama 2 7B with 4k context; MMLU from Table 8)

- Removing long texts still achieves most gains; upsampling existing long texts provides no consistent advantage
- New data mix MMLU improvement (48.62 vs 46.30) suggests **data quality matters more than length distribution** (7B ablation only; limited scale evidence)

**Instruction tuning ablation (Table 9):**

| Settings | Qasper | NarrativeQA | QuALITY | SummScreenFD | QMSum |
|---|---|---|---|---|---|
| Llama 2 Chat baseline | 12.2 | 9.13 | 56.7 | 10.5 | 14.4 |
| RLHF V5 only | 22.3 | 13.2 | 71.4 | 14.8 | 16.9 |
| RLHF V5 + pretrain data | 23.7 | 16.6 | 76.2 | **15.7** | 17.8 |
| RLHF V5 + self-inst w/o LM loss | 35.7 | 22.3 | 59.3 | 12.2 | 13.4 |
| RLHF V5 + self-inst with LM loss | **38.9** | **23.3** | **77.3** | 14.5 | **18.5** |

- Self-instruct without LM loss on inputs dramatically improves Qasper/NarrativeQA but degrades QuALITY/SummScreenFD/QMSum
- Adding LM loss on input prompts resolves the degradation and gives the best overall results (7B model only)

### Human Evaluation

Human evaluations on 2,352 examples across multi-turn conversation and multi-document search query answering tasks, each evaluated by 3 annotators (Figure 3). Win/Tie/Loss rates with 95% confidence intervals:

| Comparison | Win | Tie | Loss |
|---|---|---|---|
| vs MPT-30B-chat | 53.3 (+/-2.3) | 28.7 (+/-2.0) | 18.1 (+/-1.8) |
| vs GPT-3.5-turbo-16k | 35.8 (+/-1.6) | 31.5 (+/-2.2) | 32.8 (+/-2.1) |
| vs Claude-2-100k | 38.9 (+/-1.9) | 29.4 (+/-2.0) | 31.7 (+/-1.8) |
| vs GPT-4 | 25.0 (+/-1.9) | 30.0 (+/-1.7) | 45.0 (+/-2.3) |

- Competitive with GPT-3.5-turbo-16k and Claude-2 (win rate exceeds loss rate for both)
- Clear win over MPT-30B-chat; clear loss to GPT-4

### AI Safety Evaluation

Safety performance evaluated on 70B instruction-tuned model (Table 12):

| Model | TruthfulQA (higher better) | ToxiGen (lower better) | BOLD (closer to 0 better) |
|---|---|---|---|
| GPT-3.5-turbo | 78.46 | 0.01 | 0.50 |
| GPT-3.5-turbo-16k | 75.15 | 0.07 | 0.49 |
| Claude-2 | 62.66 | 0.05 | 0.46 |
| GPT-4 | **80.66** | 0.03 | 0.43 |
| Falcon-instruct 40B | 57.41 | 3.3 | 0.39 |
| MPT-instruct 30B | 42.71 | 16.85 | **0.34** |
| Llama 2 Chat 70B | 64.14 | 0.01 | 0.41 |
| Llama 2 Long Chat 70B | 60.95 | **0.00** | 0.40 |

- Maintains similar safety performance to Llama 2 Chat; TruthfulQA slightly lower (60.95 vs 64.14)
- Lowest ToxiGen score (0.00) among all models tested
- Internal red teaming found no significant safety risks compared to Llama 2 Chat (Section 5.2)

### Extrapolation Results

Appendix C evaluates 70B model extrapolation beyond 16k training sequence length:
- **Validation loss** (Figure 9a): RoPE ABF and xPOS ABF maintain stable cross-entropy in the extrapolation region (16k-32k), while Llama 2 loss explodes beyond 4k
- **FIRST-SENTENCE-RETRIEVAL** (Figure 9b): Both PE variants show degradation during extrapolation (ROUGE-L drops to ~60-70 at 30k from ~100 in the interpolation region)
- xPOS ABF does not outperform RoPE ABF on extrapolation despite being claimed to have better extrapolation properties (Sun et al., 2022)

---

## Limitations and Failure Modes

1. **Limited functionality for long-form outputs.** The model has not been finetuned for applications requiring long-form generation such as creative writing (Section 6).

2. **Tokenizer efficiency.** The Llama tokenizer (32k vocabulary) produces ~10% more tokens than GPT-3.5's tokenizer and cannot efficiently handle whitespace, making it inefficient for long code data (Section 6).

3. **Hallucination.** Like other LLMs, hallucination is observed, potentially more pronounced for long-context models due to dense information consumption and insufficient alignment (Section 6).

4. **34B/70B trained on shorter sequences.** The larger models were trained with 16k sequences rather than 32k due to computational constraints, though they still support 32k inference.

5. **Evaluation limitations.** Automatic metrics for summarization (single ground-truth, n-gram matching) do not align with human preference. Input truncation may remove necessary information. Proprietary models may have data leakage concerns (Section 3.2).

6. **No passkey retrieval evaluation.** The paper uses FIRST-SENTENCE-RETRIEVAL but notes "passkey task is overly simple for context probing" (footnote 4), not providing systematic needle-in-haystack evaluation.

7. **Self-instruct data limited to QA format.** The instruction tuning data generation focuses on QA tasks only (Appendix D), potentially limiting the model's ability to generalize to other long-context task types.

8. **[Inferred]** TruthfulQA drops from 64.14 (Llama 2 Chat) to 60.95 (Llama 2 Long Chat), suggesting continual pretraining with new data may slightly degrade factuality despite maintaining overall safety profile (Table 12).

9. **[Inferred]** All positional encoding ablations conducted at 7B scale only (80B tokens, Section 4.1). Whether the relative ranking of PE methods holds at 70B scale is untested.

### Scope and Comparability

- **What was not tested:** Context lengths beyond 32k; models beyond the Llama 2 family; non-English languages; complex reasoning tasks over long contexts; other PE methods beyond PI, ABF, and xPOS ABF.
- **Comparability notes:** Together-7B-32k is not purely pretrained (finetuned with supervised data), making comparison imperfect (Table 3 footnote). Maximum prompt length set to 16,384 tokens for long-task comparison, which is below the maximum supported context of some baseline models (YaRN-128k). ZeroSCROLLS results evaluated as of 8/7/2023 (Table 4 footnote), so leaderboard positions may have changed. The 70B model was trained with 16k sequences rather than 32k, so its 32k performance relies on extrapolation.

---

## Conclusions

### Contributions

1. **RoPE base frequency adjustment (ABF) for long-context.** Introduced a minimal modification to RoPE (b: 10,000 -> 500,000) that outperforms Position Interpolation on perplexity, synthetic retrieval tasks, and downstream benchmarks. Provided theoretical analysis (Theorem 1) showing ABF provides ~2.8x higher positional granularity (Section 4.1, Appendix B).

2. **Power-law context scaling.** Demonstrated that validation loss follows L(c) = (alpha/c)^beta + gamma, establishing context length as another important axis of LLM scaling. Larger models have larger beta exponents (0.45 to 0.51), indicating more effective context utilization (Figure 1).

3. **Efficient continual pretraining recipe.** Showed that switching from 4k to 32k sequences partway through training can save up to ~40% FLOPs with equivalent perplexity, validating continual pretraining from short-context models (Section 4.4).

4. **Data quality over length distribution.** Ablations show that long-context capabilities can be trained with limited long data; improvements come from data quality, not length distribution (Section 4.2).

5. **Cost-effective long-context instruction tuning.** Achieved GPT-3.5-turbo-16k-competitive performance on ZeroSCROLLS using only synthetic self-instruct data without human annotation. Key insight: calculating LM loss on long input prompts improves performance (Section 2.2, Section 4.3).

6. **Short-context improvements.** Unlike prior work reporting degradation, Llama 2 Long improves over Llama 2 on short-context benchmarks across all 4 model sizes, attributed to additional compute and knowledge from new data (Section 3.1).

### Implications

1. **Continual pretraining is sufficient for long-context.** The training curriculum ablation suggests that long-context capabilities can be efficiently added post-hoc without architectural changes beyond positional encoding modifications.

2. **Sparse attention may not be necessary at 32k.** For Llama 2 70B (h = 8192), attention only becomes a bottleneck beyond 49,152 tokens (6h), suggesting full attention remains viable for moderate context extensions (Section 2.1).

3. **Human annotation may be unnecessary for long-context alignment.** The success of self-instruct long data suggests scalable approaches to long-context instruction tuning without expensive human annotation (speculative beyond QA tasks).

4. **Context length as a scaling axis.** The power-law relationship suggests that context length scaling follows similar principles to model size and data scaling, potentially enabling principled decisions about compute allocation between these axes (speculative; the paper does not derive a unified scaling law).

---

## Key Claims

**C1. RoPE ABF outperforms Position Interpolation for long-context extension.** ABF achieves lower perplexity (6.323 vs 6.341 on 32k Books, 6.780 vs 6.786 on CC, 3.771 vs 3.775 on Wikipedia), maintains FIRST-SENTENCE-RETRIEVAL to 32k (PI degrades at 24k+), and improves downstream tasks (HumanEval: 17.07 vs 15.24, MMLU: 46.24 vs 45.84) (Table 5, Table 6, Figure 5). Theoretical analysis shows ABF provides ~2.8x higher positional granularity (Appendix B, Theorem 1). **Scope:** Llama 2 7B, 80B continual pretraining tokens, 32k context. Single configuration per PE variant, no variance reported (limited evidence). Status: **supported**.

**C2. Validation loss follows power-law scaling with context length.** L(c) = (alpha/c)^beta + gamma fits all model sizes. The 70B model's beta = 0.51 indicates ~30% loss reduction when doubling context (2^{-0.51} ~ 0.70). Larger models have larger beta (7B: 0.45, 13B: 0.48, 34B: 0.50, 70B: 0.51) (Figure 1). **Scope:** Llama 2 Long 7B-70B, up to 32k context, tested across 4 model sizes (strong evidence for the trend). Status: **supported**.

**C3. Continual pretraining can save up to ~40% FLOPs compared to pretraining from scratch.** The 4k->32k @ 80% curriculum uses 2.270 x 10^22 FLOPs vs 3.783 x 10^22 for 32k from scratch (~40% reduction). Perplexity is equivalent (Books: 6.49 vs 6.52, Table 11). Long-context task performance is comparable though Qasper drops (25.0 vs 28.6, Table 10). The 4k->32k @ 40% curriculum achieves 20% FLOP savings with more balanced task performance. **Scope:** 7B model only, 32k context, single scale (limited evidence for generalization). Status: **supported**.

**C4. Data quality matters more than length distribution for long-context training.** Removing long texts from Llama 2 data still achieves most performance gains (NarrativeQA: 19.48% vs 23.70% with new data). Upsampling existing long texts (22.15%) does not consistently outperform removing long texts (19.48%). The new data mix's MMLU advantage (48.62 vs 46.30) suggests quality differences, not length (Table 7, Table 8). **Scope:** 7B model ablations, 4 configurations (moderate evidence). Status: **supported**.

**C5. Llama 2 Long 70B Chat outperforms gpt-3.5-turbo-16k on 7/10 ZeroSCROLLS tasks.** Specifically: GR (26.0 vs 24.3), QM (20.0 vs 17.4), Qspr (52.0 vs 50.0), Nrtv (31.7 vs 29.5), QALT (82.6 vs 72.0), SpDg (55.5 vs 54.1), and overall average (37.7 vs 36.7) (Table 4). **Scope:** 70B instruction-tuned model, ZeroSCROLLS benchmark, evaluated as of 8/7/2023, synthetic self-instruct data only. Single evaluation (limited evidence for individual narrow margins). Status: **supported**.

**C6. Llama 2 Long improves over Llama 2 on short-context benchmarks.** 70B improvements: Coding +2.5 (39.9 vs 37.4), Math +6.1 (41.3 vs 35.2), MMLU +2.8 (71.7 vs 68.9), Commonsense +0.8 (72.7 vs 71.9), OpenQA +0.4 (64.0 vs 63.6) (Table 1). Pattern holds across all 4 model sizes. Attributed to additional FLOPs and knowledge from new data. **Scope:** All model sizes 7B-70B, standard benchmarks. Tested at 4 scales (strong evidence for the trend). Status: **supported**.

**C7. Calculating LM loss on long input prompts during instruction tuning gives consistent improvements.** With LM loss vs without: Qasper 38.9 vs 35.7, NarrativeQA 23.3 vs 22.3, QuALITY 77.3 vs 59.3, QMSum 18.5 vs 13.4 (Table 9). The improvement is particularly dramatic on QuALITY (+18.0) and QMSum (+5.1). Motivated by the observation that output lengths are much shorter than input lengths for long-context tasks (footnote 5). **Scope:** 7B model, self-instruct QA data, 5 tasks. Single run (limited evidence). SummScreenFD is a counterexample (14.5 vs 12.2 without LM loss, but 15.7 with pretrain mix). Status: **supported**.

---

## Open Questions

1. **Why does the power-law exponent beta increase with model size?** The paper observes beta increasing from 0.45 (7B) to 0.51 (70B) but does not explain the mechanism. Is this related to attention head count, hidden dimension, or emergent capabilities? Unresolved.

2. **Can the training curriculum findings scale to longer contexts and larger models?** The 40% FLOP savings are demonstrated at 7B scale with 32k context. Whether this generalizes to 64k+, 128k, or million-token contexts remains untested. Partially addressed by: `2024-07-longrope-context-extension` (LongRoPE uses progressive extension to 2048k).

3. **What is the optimal base frequency for different target context lengths?** The paper uses b = 500,000 for 32k context. The relationship between optimal b and target context length is not characterized. Addressed by: `2024-07-longrope-context-extension` (LongRoPE uses search-based methods to find optimal rescale factors).

4. **Does the LM loss on input prompts generalize beyond QA tasks?** The instruction tuning finding that LM loss on inputs helps is specific to long QA tasks with unbalanced input/output lengths (footnote 5). Generalization to other task types (summarization, creative writing, dialogue) is unknown. Unresolved.

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations

- **Su et al. (2022)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the positional encoding modified in this work. The base frequency b = 10,000 is the parameter adjusted to b = 500,000.
- **Sun et al. (2022)** -- *A Length-Extrapolatable Transformer (xPos).* Alternative rotary encoding that smooths high-frequency oscillation. Evaluated as xPOS ABF but found not to outperform RoPE ABF on perplexity, downstream tasks, or extrapolation.

### Direct Predecessors (Context Extension Methods)

- **Chen et al. (2023)** -- *Extending Context Window via Positional Interpolation.* Concurrent approach that linearly scales positions. ABF is shown to outperform PI on perplexity, downstream tasks, and retrieval (Table 5, Table 6, Figure 5).
- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension.* Evaluated as baseline. Llama 2 Long outperforms YaRN-7B-128k and YaRN-13B-128k on all long-context tasks (Table 3).
- **Mohtashami & Jaggi (2023)** -- *Landmark Attention.* Concurrent long-context work; their passkey task is noted as "overly simple for context probing" (footnote 4).

### Base Models

- **Touvron et al. (2023)** -- *Llama 2: Open Foundation and Fine-tuned Chat Models.* The base model that Llama 2 Long extends through continual pretraining. RLHF dataset ("RLHF V5") used for instruction tuning.

### Concurrent Long-Context Models (Baselines)

- **Tworkowski et al. (2023)** -- *Focused Transformer.* Baseline model using contrastive training for context scaling (Table 3).
- **MosaicML (2023)** -- *MPT-7B/30B.* Baseline long-context models evaluated in Table 3; MPT-instruct 30B in safety evaluation (Table 12).
- **Nijkamp et al. (2023)** -- *Xgen-7B.* Baseline with 8k context (Table 3).
- **Together (2023)** -- *Llama-2-7B-32K.* PI-based 32k model; noted as finetuned with supervised data, not purely pretrained.
- **Roziere et al. (2023)** -- *Code Llama.* Concurrently suggests the base frequency modification idea.

### Scaling Laws

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Foundational scaling laws work; power-law context scaling (Figure 1) extends this paradigm to context length.
- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models (Chinchilla).* Scaling laws reference for the power-law formulation.

### Evaluation Benchmarks

- **Shaham et al. (2023)** -- *ZeroSCROLLS.* Primary long-context evaluation benchmark for instruction-tuned model (Table 4, 10 tasks).
- **An et al. (2023)** -- *L-Eval.* Additional long-context evaluation benchmark (Table 17, 6 tasks).
- **Kocisky et al. (2018)** -- *NarrativeQA.* Long-context QA benchmark (Table 3).
- **Pang et al. (2022)** -- *QuALITY.* Long-context multiple-choice QA benchmark (Table 3).
- **Dasigi et al. (2021)** -- *Qasper.* Scientific paper QA benchmark (Table 3).
- **Zhong et al. (2021)** -- *QMSum.* Query-based meeting summarization benchmark (Table 3).

### Training Infrastructure

- **Dao et al. (2022)** -- *FlashAttention.* Enables efficient long-sequence training with negligible GPU memory overhead; ~17% speed loss when increasing from 4k to 16k for 70B.

### Safety Evaluation

- **Lin et al. (2021)** -- *TruthfulQA.* Factuality benchmark for safety evaluation (Table 12).
- **Hartvigsen et al. (2022)** -- *ToxiGen.* Toxicity benchmark (Table 12).
- **Dhamala et al. (2021)** -- *BOLD.* Bias in open-ended language generation benchmark (Table 12).

### Self-Instruct and Alignment

- **Wang et al. (2022)** -- *Self-Instruct.* Method used to generate synthetic long QA data for instruction tuning without human annotation (Section 2.2, Appendix D).
- **Ouyang et al. (2022)** -- *Training Language Models to Follow Instructions with Human Feedback.* Referenced for the cost and difficulty of human demonstration and preference labeling.
