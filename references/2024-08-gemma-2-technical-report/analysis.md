---
title: "Gemma 2: Improving Open Language Models at a Practical Size"
authors: "Gemma Team"
year: 2024
venue: "arXiv preprint 2408.00118"
paper_type: preprint
categories: ["model-release", "architecture", "attention-efficiency"]
scope: ["open foundation models", "knowledge distillation", "efficient attention", "grouped-query attention", "sliding window attention"]
benchmarks_used: ["mmlu", "gsm8k", "arc", "hellaswag", "winogrande", "humaneval", "mbpp", "bbh", "math-hendrycks", "triviaqa", "natural-questions", "agi-eval", "drop", "piqa", "siqa", "boolq", "truthfulqa"]
models_introduced: ["gemma-2-2b", "gemma-2-9b", "gemma-2-27b"]
models_evaluated: ["llama-3-8b", "llama-3-70b", "mistral-7b", "gemma-7b", "gemma-2b", "qwen1.5-32b"]
key_claims:
  - id: C1
    claim: "Knowledge distillation improves small model performance: a 2B model trained with distillation achieves 67.7 average (vs 60.3 from scratch) on 3 benchmarks"
    evidence: "Table 6, Section 5"
    status: supported
    scope: "2B model, 500B tokens, 7B teacher"
    magnitude: "+7.4 points average improvement"
  - id: C2
    claim: "Gemma 2 27B outperforms Qwen1.5 32B on all reported HuggingFace evaluation suite benchmarks"
    evidence: "Table 12, Section 6.1"
    status: supported
    scope: "HuggingFace evaluation suite: MMLU, GSM8K, ARC-c, HellaSwag, Winogrande"
    magnitude: "MMLU 75.2 vs 74.3, GSM8K 74.0 vs 61.1, ARC-c 71.4 vs 63.6, HellaSwag 86.4 vs 85.0, Winogrande 83.7 vs 81.5"
  - id: C3
    claim: "Gemma 2 27B is competitive with LLaMA-3 70B despite being 2.5x smaller and trained on 2/3 less data"
    evidence: "Table 12, Section 6.1"
    status: supported
    scope: "MMLU, GSM8K, ARC-c, HellaSwag, Winogrande"
    magnitude: "Within 4-5% on most benchmarks: MMLU 75.2 vs 79.2, GSM8K 74.0 vs 76.9"
  - id: C4
    claim: "Gemma 2 9B IT achieves Elo 1187 on LMSYS Chatbot Arena, nearly identical to GPT-4-0314 (Elo 1186)"
    evidence: "Table 14, Section 6.2"
    status: supported
    scope: "LMSYS Chatbot Arena blind human evaluations, snapshot in time"
    magnitude: "Elo 1187 vs 1186, within 1 point"
  - id: C5
    claim: "GQA with num_groups=2 maintains downstream performance while increasing inference speed compared to MHA"
    evidence: "Table 8, Section 5"
    status: supported
    scope: "9B model, 4 benchmarks"
    magnitude: "50.8 average (GQA) vs 50.3 (MHA), +0.5 points with fewer parameters"
  - id: C6
    claim: "Deeper networks are slightly better than wider networks for the same parameter count"
    evidence: "Table 9, Section 5"
    status: supported
    scope: "9B model comparison, 4 benchmarks"
    magnitude: "+1.2 points average (52.0 deep vs 50.8 wide)"
  - id: C7
    claim: "Gemma 2 memorizes significantly less than prior models, with verbatim memorization rates below 0.1%"
    evidence: "Figure 1, Section 7"
    status: supported
    scope: "50-token continuation, exact match criterion"
    magnitude: "Below 0.1% memorization rate, substantially lower than Gemma 1"
  - id: C8
    claim: "Distillation benefit persists as model size increases: 200M, 400M, and 1B models all show ~2-point perplexity reduction"
    evidence: "Table 7, Section 5"
    status: supported
    scope: "200M-1B models, 7B teacher, validation perplexity"
    magnitude: "2-point perplexity reduction at each model size (23->21, 19->17, 17->15)"
  - id: C9
    claim: "Gemma 2 27B IT achieves Elo 1218 on LMSYS Chatbot Arena, ranked higher than LLaMA-3 70B Instruct (Elo 1206)"
    evidence: "Table 14, Section 6.2"
    status: supported
    scope: "LMSYS Chatbot Arena blind human evaluations, snapshot in time"
    magnitude: "Elo 1218 vs 1206, +12 points despite 2.5x smaller model size"
  - id: C10
    claim: "Sliding window size can be reduced at inference time with minimal perplexity impact"
    evidence: "Table 10, Section 5"
    status: supported
    scope: "9B model, validation set perplexity"
    magnitude: "Perplexity 1.63 at 4096, 1.63 at 2048, 1.64 at 1024 window"
  - id: C11
    claim: "Gemma 2 models produce safer responses than GPT-4o on held-out safety prompts, regardless of model size"
    evidence: "Table 15, Section 6.2"
    status: supported
    scope: "Held-out safety prompt set, side-by-side with GPT-4o"
    magnitude: "Win rates 53-57.5% vs GPT-4o on safety"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Builds on decoder-only Transformer with GQA, GeGLU, RoPE, logit soft-capping, and interleaved local-global attention"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Uses RoPE positional embeddings for all model sizes"
  - target: 2020-04-longformer-long-document-transformer
    type: extends
    detail: "Adopts interleaved local sliding window and global attention pattern from Longformer"
  - target: 2023-07-llama-2-open-foundation-chat
    type: evaluates
    detail: "Compares Gemma 2 models against LLaMA-3 8B and 70B on multiple benchmarks"
  - target: 2023-10-mistral-7b
    type: evaluates
    detail: "Compares Gemma 2 2B and 9B against Mistral 7B; notes Mistral is significantly less format-robust (std 6.9 vs 0.9)"
  - target: 2024-07-qwen2-technical-report
    type: concurrent
    detail: "Both released mid-2024 as competitive open-weight model families with GQA; Gemma 2 focuses on distillation while Qwen2 focuses on data scaling"
open_questions:
  - question: "How does distillation scale beyond 9B parameters? Would distilling the 27B model from an even larger teacher yield further gains?"
    addressed_by: null
  - question: "What is the optimal teacher-student size ratio for knowledge distillation in language models?"
    addressed_by: null
  - question: "Can the interleaved local-global attention pattern be extended to longer context lengths beyond 8K?"
    addressed_by: null
  - question: "How does the distillation benefit vary with training token count? The paper trains at 50x compute-optimal but does not ablate intermediate points."
    addressed_by: null
---

# Gemma 2: Improving Open Language Models at a Practical Size

**Authors:** Gemma Team (Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy Hardin, et al., Google DeepMind)
**Date:** August 2024, arXiv:2408.00118

---

## Core Research Problem

Small-scale language models have shown rapid performance increases, largely derived from increasing training length (Gemma Team, 2024; Jiang et al., 2023; Touvron et al., 2023). However, this approach only scales **logarithmically** with dataset size (Hoffmann et al., 2022 -- *Training Compute-Optimal Large Language Models*), and the latest small models require up to **15T tokens** to improve state of the art by less than 1-2% (AI@Meta, 2024) (Section 1). The continued improvements provide evidence that small models remain under-trained, but simply scaling training tokens yields diminishing returns.

Prior open-weight models like LLaMA 3 (AI@Meta, 2024) and Mistral 7B (Jiang et al., 2023) have advanced the state of the art, but achieving strong performance at practical sizes (2B-27B parameters) without massive data scaling remains challenging. The key limitation is that the standard next-token prediction objective provides only a one-hot target, offering sparse gradients to the model at each training step (Section 1).

**The core challenge: how to improve the quality of information received by the network at each training step, so that small language models can be improved without solely relying on increasing training length.**

---

## Problem Solutions

Gemma 2 addresses these challenges through two main strategies:

1. **Knowledge distillation** replaces the one-hot next-token prediction target with the full probability distribution from a larger teacher model, providing richer gradients and enabling training beyond available token counts. The 2B and 9B models are distilled from larger teachers on a quantity of tokens more than **50x** the compute-optimal quantity predicted by Chinchilla scaling laws (Hoffmann et al., 2022).

2. **Architectural modifications** including interleaved local sliding window and global attention (from Beltagy et al., 2020a -- *Longformer*), Grouped-Query Attention (GQA) with num_groups=2 (Ainslie et al., 2023), logit soft-capping, and both pre-norm and post-norm with RMSNorm for training stability.

---

## Approach Details

### Method

#### Model Architecture

Gemma 2 models are decoder-only Transformers (Vaswani et al., 2017) with the following specifications (Table 1, Section 2):

| Parameter | 2B | 9B | 27B |
|---|---|---|---|
| d_model | 2304 | 3584 | 4608 |
| Layers | 26 | 42 | 46 |
| Num heads | 8 | 16 | 32 |
| Num KV heads | 4 | 8 | 16 |
| Head size | 256 | 256 | 128 |
| Feedforward dim | 18432 | 28672 | 73728 |
| Vocab size | 256128 | 256128 | 256128 |
| Non-embedding params | 2.02B | 8.32B | 26.05B |

The larger embedding parameter counts (590M for 2B, 918M for 9B, 1.18B for 27B) are inherited from the large Gemini vocabulary (256K entries), designed for multilingual support (Table 2, Section 2).

#### Interleaved Local-Global Attention

The models alternate between local sliding window attention and global attention in every other layer (Section 2):

- **Local attention layers:** Sliding window size of **4096** tokens
- **Global attention layers:** Span of **8192** tokens (full context)

This design, adapted from Longformer (Beltagy et al., 2020a), reduces computational cost while maintaining long-range dependencies through interleaved global layers.

#### Logit Soft-Capping

Logits are capped in each attention layer and the final layer to stabilize training (Bello et al., 2016) (Section 2):

> logits <- soft_cap * tanh(logits / soft_cap)

The soft_cap parameter is set to **50.0** for self-attention layers and **30.0** for the final layer.

#### Grouped-Query Attention

All models use GQA (Ainslie et al., 2023) with **num_groups = 2** (i.e., 2 query heads per KV head). Ablations show increased inference speed while maintaining downstream performance (Table 8, Section 5).

#### Normalization

Both **pre-norm and post-norm** are applied using RMSNorm (Zhang and Sennrich, 2019) to normalize input and output of each transformer sub-layer (attention and feedforward) (Section 2).

#### Shared Elements with Gemma 1

Context length of 8192 tokens, Rotary Position Embeddings (RoPE) (Su et al., 2021), and the approximated GeGLU non-linearity (Shazeer, 2020) are retained from Gemma 1 (Section 2).

---

### Key Technical Components

#### Knowledge Distillation

For the 2B and 9B models, training uses knowledge distillation from a larger teacher model rather than standard next-token prediction. Given teacher probability P_T(x | x_c), the student minimizes (Section 3.2):

> min_{P_S} sum_x -P_T(x | x_c) log P_S(x | x_c)

where P_S is the parameterized probability of the student.

Key aspects:
- The **2B and 9B** models are trained with distillation; the **27B** model is trained from scratch
- Training uses more than **50x** the compute-optimal token quantity predicted by Chinchilla scaling laws (Hoffmann et al., 2022)
- Distillation was also used in Gemini 1.5 (Gemini Team, 2024)

#### Training Data

| Model | Training Tokens | Data Sources |
|---|---|---|
| 27B | 13T | Web documents, code, science articles |
| 9B | 8T | Web documents, code, science articles |
| 2B | 2T | Web documents, code, science articles |

- Primarily English data
- Not multimodal, not trained for multilingual capabilities
- Same tokenizer as Gemma 1 and Gemini: SentencePiece (Kudo and Richardson, 2018) with split digits, preserved whitespace, byte-level encodings, and 256K vocabulary
- Data filtering applied to reduce unwanted/unsafe utterances, filter personal information, decontaminate evaluation sets, and reduce recitation risk (Section 3.1)

#### Post-Training

The post-training pipeline consists of three stages (Section 4):

1. **Supervised Fine-Tuning (SFT):** Text-only, English-only synthetic and human-generated prompt-response pairs. Behavioral cloning on synthetic and real prompts with responses predominantly synthetically generated by the teacher. Distillation from teacher on student's distribution is also applied (Agarwal et al., 2024; Gu et al., 2024).
2. **RLHF:** Reward model trained on English-only preference data; reward model is an **order of magnitude larger** than the policy. The reward model is oriented more towards conversational capabilities, specifically multi-turn (Section 4).
3. **Model merging:** Averaging models from different hyperparameter runs (Rame et al., 2024 -- *WARP*).

Post-training data was extended from Gemma 1.1 with a mixture of internal and external public data. Specifically, the prompts (not answers) from LMSYS-Chat-1M (Zheng et al., 2023) are used. Data filtering removes examples with personal information, unsafe/toxic outputs, mistaken self-identification, and duplicates (Section 4).

#### Compute Infrastructure

| Model | TPU Type | #Chips | Data Shards | Model Shards |
|---|---|---|---|---|
| 2B | TPUv5e | 512 | 512 | 1 |
| 9B | TPUv4 | 4096 | 1024 | 4 |
| 27B | TPUv5p | 6144 | 768 | 8 |

Optimizer state is further sharded using techniques similar to ZeRO-3 (Ren et al., 2021). The GSPMD partitioner (Xu et al., 2021) and MegaScale XLA compiler are used. Carbon emissions are estimated at **1247.61 tCO2eq** (Table 3, Section 3.3-3.4).

---

### Experimental Setup

**Pre-training evaluation:** HuggingFace evaluation suite including MMLU (5-shot), GSM8K (5-shot), ARC-C (25-shot), HellaSwag (10-shot), Winogrande (5-shot). Extended benchmarks in Table 13 include AGIEval (3-5-shot), DROP (3-shot F1), BBH (3-shot CoT), MATH (4-shot), ARC-e (0-shot), PIQA (0-shot), SIQA (0-shot), BoolQ (0-shot), TriviaQA (5-shot), NQ (5-shot), HumanEval (pass@1), MBPP (3-shot) (Section 6.1).

**Instruction-tuned evaluation:**
- LMSYS Chatbot Arena (Chiang et al., 2024) blind side-by-side evaluations by human raters with Elo scoring
- Human preference studies for safety and instruction following using GPT-4o as base model
- Multi-turn conversation scenarios (500 held-out scenarios, avg 8.4 turns) (Section 6.2)

**Baselines:** LLaMA-3 8B/70B, Mistral 7B, Qwen1.5 32B, Gemma 1 2B/7B, GPT-4o, GPT-3.5-Turbo, GPT-4-0314.

**Compute:** TPUv4/v5e/v5p clusters; 512-6144 chips depending on model size; ZeRO-3 style optimizer state sharding; GSPMD partitioner (Table 3, Section 3.3).

**Reproducibility:** Specific learning rates, optimizer configurations, and total compute costs are **not disclosed**. Code and models are released publicly. Training data composition is described only at a high level (web, code, science). No random seeds are reported.

---

### Key Results

#### Pre-trained Model: Gemma 2 27B vs Baselines (Table 12)

| Benchmark | LLaMA-3 70B | Qwen1.5 32B | Gemma-2 27B |
|---|---|---|---|
| MMLU | 79.2 | 74.3 | **75.2** |
| GSM8K | 76.9 | 61.1 | **74.0** |
| ARC-c | 68.8 | 63.6 | **71.4** |
| HellaSwag | 88.0 | 85.0 | **86.4** |
| Winogrande | 85.3 | 81.5 | **83.7** |

- Gemma 2 27B outperforms Qwen1.5 32B on **all 5 benchmarks** (Table 12, Section 6.1)
- Only a few percent below LLaMA-3 70B despite being **2.5x smaller** and trained on **2/3 less data** (Section 6.1)
- Performance improves only logarithmically with model size for models trained similarly, suggesting Gemma 2 27B is on the same Pareto curve as LLaMA-3 (limited evidence: 3 models compared on 5 benchmarks, single evaluation per configuration)

#### Pre-trained Models: Full Comparison (Table 13)

| Benchmark | metric | Gemma-1 2B | Gemma-2 2B | Mistral 7B | LLaMA-3 8B | Gemma-1 7B | Gemma-2 9B | Gemma-2 27B |
|---|---|---|---|---|---|---|---|---|
| MMLU | 5-shot | 42.3 | **52.2** | 62.5 | 66.6 | 64.4 | **71.3** | 75.2 |
| ARC-C | 25-shot | 48.5 | **55.7** | 60.5 | 59.2 | 61.1 | **68.4** | 71.4 |
| GSM8K | 5-shot | 15.1 | **24.3** | 39.6 | 45.7 | 51.8 | **68.6** | 74.0 |
| AGIEval | 3-5-shot | 24.2 | **31.5** | 44.0 | 45.9 | 44.9 | **52.8** | 55.1 |
| DROP | 3-shot, F1 | 48.5 | **51.2** | 63.8 | 58.4 | 56.3 | **69.4** | 74.2 |
| BBH | 3-shot, CoT | 35.2 | **41.9** | 56.0 | 61.1 | 59.0 | **68.2** | 74.9 |
| Winogrande | 5-shot | 66.8 | **71.3** | 78.5 | 76.1 | 79.0 | **80.6** | 83.7 |
| HellaSwag | 10-shot | 71.7 | **72.9** | **83.0** | 82.0 | 82.3 | 81.9 | 86.4 |
| MATH | 4-shot | 11.8 | **16.0** | 12.7 | - | 24.3 | **36.6** | 42.3 |
| ARC-e | 0-shot | 73.2 | **80.6** | 80.5 | - | 81.5 | **88.0** | 88.6 |
| PIQA | 0-shot | 77.3 | **78.4** | **82.2** | - | 81.2 | 81.7 | 83.2 |
| SIQA | 0-shot | 49.7 | **51.9** | 47.0 | - | 51.8 | **53.4** | 53.7 |
| BoolQ | 0-shot | 69.4 | **72.7** | 83.2 | - | 83.2 | **84.2** | 84.8 |
| TriviaQA | 5-shot | 53.2 | **60.4** | 62.5 | - | 63.4 | **76.6** | 83.7 |
| NQ | 5-shot | 12.5 | **17.1** | 23.2 | - | 23.0 | **29.2** | 34.5 |
| HumanEval | pass@1 | **22.0** | 20.1 | 26.2 | - | 32.3 | **40.2** | 51.8 |
| MBPP | 3-shot | 29.2 | **30.2** | 40.2 | - | 44.4 | **52.4** | 62.6 |
| Average (8) | | 44.0 | **50.0** | 61.0 | 61.9 | 62.4 | **70.2** | 74.4 |
| Average (all) | | 44.2 | **48.7** | 55.6 | - | 57.9 | **64.9** | 69.4 |

- Gemma 2 9B achieves average **70.2** on 8 core benchmarks, surpassing LLaMA-3 8B (61.9) by +8.3 points (strong evidence: 8 diverse benchmarks)
- Massive improvement from Gemma 1: Gemma 2 9B vs Gemma 1 7B shows +7.8 points on 8-benchmark average (62.4 to 70.2), up to +16.8 points on GSM8K (51.8 to 68.6) (Section 6.1)
- Gemma 2 2B improves over Gemma 1 2B by +6.0 points on 8-benchmark average (44.0 to 50.0), confirming distillation benefit at small scale
- Note: some baseline numbers for AGIEval and BBH use different evaluation procedures (marked with daggers/circles in paper), leading to +3-4% compared to the authors' own evaluation (Section 6.1)

#### LMSYS Chatbot Arena (Table 14)

| Model | Elo | 95% CI | Open |
|---|---|---|---|
| gemma-2-27b-it | **1218** | +4/-3 | + |
| llama-3-70b-instruct | 1206 | +2/-2 | + |
| gemma-2-9b-it | **1187** | +3/-5 | + |
| gpt-4-0314 | 1186 | +2/-3 | - |
| gemma-2-2b-it | **1126** | +10/-10 | + |
| gpt-3.5-turbo-0613 | 1116 | +3/-4 | - |

- Gemma 2 27B IT (Elo 1218) ranked **higher than LLaMA-3 70B Instruct** (Elo 1206) despite being 2.5x smaller (Table 14, Section 6.2)
- Gemma 2 9B IT (Elo 1187) similar to **GPT-4-0314** (Elo 1186) (Table 14, Section 6.2)
- Gemma 2 2B IT (Elo 1126) ranked higher than **GPT-3.5-Turbo** (Elo 1116) (Table 14, Section 6.2)
- These are blind side-by-side human evaluations -- a snapshot in time (limited evidence: single evaluation period, no repeated measurements)

#### Human Preference Evaluations (Tables 15, 16)

| Model | Instruction Following | Safety (win rate vs GPT-4o) |
|---|---|---|
| Gemma 1.1 IT 7B | 24.3% +/- 1.9% | 42.8% (W/T/L: 37.4/10.8/51.8%) |
| Gemma 2 IT 2B | 26.5% +/- 1.8% | **57.5%** (W/T/L: 53/9/38%) |
| Gemma 2 IT 9B | 34.1% +/- 3.0% | **57.8%** (W/T/L: 48.2/19.2/28.3%) |
| Gemma 2 IT 27B | 37.7% +/- 2.3% | **55%** (W/T/L: 49.6/10.8/39.6%) |

- All Gemma 2 models produce **safer responses than GPT-4o** on the held-out safety prompt set (Table 15, Section 6.2)
- Instruction following scores increase monotonically with model size

| Model | User Satisfaction (1-5) | Conversation Goal Achievement (1-5) |
|---|---|---|
| Gemma 1.1 IT 7B | 3.32 | 3.36 |
| Gemma 2 IT 2B | 3.64 | 3.88 |
| Gemma 2 IT 9B | 4.04 | 4.08 |
| Gemma 2 IT 27B | 4.20 | 4.24 |

- Multi-turn evaluation on 500 held-out scenarios (avg 8.4 turns) shows Gemma 2 models are rated significantly better than Gemma 1.1 in both user satisfaction and goal achievement (Table 16, Section 6.2)

#### Pre-trained vs Instruction-Tuned (Table 17)

| Benchmark | 2B PT | 2B IT | 9B PT | 9B IT | 27B PT | 27B IT |
|---|---|---|---|---|---|---|
| MMLU | 52.2 | **56.1** | 71.3 | **72.3** | 75.2 | **76.2** |
| MBPP | 30.2 | **36.6** | 52.4 | **59.2** | 62.6 | **67.4** |

- Instruction fine-tuning improves few-shot benchmark performance across all model sizes, consistent with observations from LLaMA-3 (AI@Meta, 2024). The authors conjecture IT models are better at understanding formatted questions (Table 17, Section 6.2).

#### Distillation Ablations (Tables 6, 7)

| Training Method | Average (3 benchmarks) |
|---|---|
| From scratch | 60.3 |
| Distilled (7B teacher) | **67.7** |

- Distillation provides **+7.4 points** improvement on a 2B model trained for 500B tokens (10x compute-optimal) with a 7B teacher (Table 6, Section 5)

| Model Size | From Scratch (perplexity) | Distilled (perplexity) |
|---|---|---|
| 200M | 23 | 21 |
| 400M | 19 | 17 |
| 1B | 17 | 15 |

- Distillation benefit persists as model size increases: consistent ~2-point perplexity reduction at all scales with a 7B teacher (Table 7, Section 5)

#### Architecture Ablations (Tables 8, 9, 10)

| Configuration | GQA vs MHA (9B, avg 4 bench.) |
|---|---|
| MHA | 50.3 |
| GQA | **50.8** |

- GQA with num_groups=2 maintains performance while enabling faster inference and using fewer parameters (Table 8, Section 5; limited evidence: single model size, 4 benchmarks)

| Configuration | Wide vs Deep (9B, avg 4 bench.) |
|---|---|
| Wide | 50.8 |
| Deep | **52.0** |

- Deeper 9B architecture outperforms wider 9B by **+1.2 points** on 4 benchmarks (Table 9, Section 5; limited evidence: single model size, 4 benchmarks, consistent across benchmarks)

| Sliding Window | 4096 | 2048 | 1024 |
|---|---|---|---|
| Perplexity (val. set) | 1.63 | 1.63 | 1.64 |

- Sliding window size can be reduced at inference time with **minimal perplexity impact**: reducing from 4096 to 1024 increases perplexity by only 0.01 (Table 10, Section 5). This provides a lever for inference speed optimization.

#### Format Sensitivity (Table 11)

| Model | MMLU Std. Dev. (12 format combinations) |
|---|---|
| Gemma 1 2B | 1.5 |
| Gemma 2 2B | 2.1 |
| Mistral 7B | **6.9** |
| Gemma 1 7B | 0.7 |
| Gemma 2 9B | 0.9 |
| Gemma 2 27B | 1.0 |

- Gemma 2 2B is slightly less format-robust than larger models (std 2.1 vs 0.9-1.0), but **Mistral 7B is significantly less robust** (std 6.9) (Table 11, Section 5)

---

### Safety and Responsibility Evaluations

#### Safety Benchmark Results (Table 18)

| Benchmark | metric | Gemma 1.1 IT 2.5B | Gemma 1.1 IT 7B | Gemma 2 IT 2.6B | Gemma 2 IT 9B | Gemma 2 IT 27B |
|---|---|---|---|---|---|---|
| RealToxicity | avg tox | **7.03** | 8.04 | 8.16 | 8.25 | 8.84 |
| CrowS-Pairs | top-1 | 45.89 | **49.67** | 37.67 | 37.47 | 36.67 |
| BBQ Ambig | 4-shot | 58.97 | 86.06 | 83.20 | **88.58** | 85.99 |
| BBQ Disambig | 4-shot | 53.9 | 85.08 | 69.31 | 82.67 | **86.94** |
| Winogender | top-1 | 50.14 | 57.64 | 52.91 | **79.17** | 77.22 |
| TruthfulQA | MC2Acc | 44.24 | 45.34 | 43.72 | 50.27 | **51.60** |
| Winobias 1_2 | top-1 | 55.93 | 59.22 | 59.28 | 78.09 | **81.94** |
| Winobias 2_2 | top-1 | 89.46 | 89.2 | 88.57 | 95.32 | **97.22** |
| Toxigen | avg tox | **29.64** | 38.75 | 48.32 | 39.30 | 38.42 |

- Gemma 2 improves over Gemma 1 on bias-related benchmarks (Winogender, Winobias, BBQ) but shows **higher toxicity scores** (RealToxicity, Toxigen) than the smaller Gemma 1 models (Table 18, Section 8.3)
- For CrowS-Pairs, **lower is better** (less stereotypical): Gemma 2 models show improvement (36.67-37.67 vs 45.89-49.67)

#### Assurance Evaluations (Tables 19-25)

**Offensive Cyber-Security (Table 19):**

| Model | InterCode-CTF | Internal CTF | Hack the Box |
|---|---|---|---|
| Gemini 1.0 Ultra | 28/76 (37%) | 3/13 (23%) | 0/13 |
| Gemini 1.5 Pro | **62/76 (82%)** | **4/13 (31%)** | 0/13 |
| CodeGemma 1 7B | 12/76 (16%) | 0/13 (0%) | 0/13 |
| Gemma 2 27B | 34/76 (45%) | 1/13 (8%) | 0/13 |

- Gemma 2 27B shows increased capabilities over CodeGemma 1 7B but is much less capable than Gemini 1.5 Pro (Section 8.4). Note: InterCode-CTF results exclude challenges requiring internet access.

**Self-Proliferation (Table 21):**

| Model | End-to-end | All milestones | Total milestones | Expert bits |
|---|---|---|---|---|
| Gemini 1.0 Ultra | 0/10 | 1/10 | 16/45 (36%) | 13,026 |
| Gemini 1.5 Pro | 0/10 | **2/10** | **25/45 (56%)** | **11,046** |
| Gemma 2 27B | 0/10 | 1/10 | 22/45 (49%) | 12,462 |

- No model passes the easiest end-to-end challenge (installing a Bitcoin wallet). Gemma 2 completes more milestones than Gemini 1.0 Ultra but still has low capabilities on end-to-end self-proliferation tasks (Section 8.4).

**Persuasion:** Gemma 2 27B is strong at building rapport (80% personal connection, 75% would speak again) comparable to Gemini 1.5 Pro. However, on deception tasks (Hidden Agenda), Gemma 2 does not show significant differences from Gemini models. On belief shifting (Web of Lies), Gemma 2 is significantly weaker than a human baseline at persuading participants of incorrect answers (Tables 22-25, Section 8.4).

---

## Limitations and Failure Modes

1. **English-only focus:** Models are not trained for multilingual capabilities and are not multimodal (Section 3.1).

2. **No distillation for 27B:** The largest model is trained from scratch without distillation, leaving open whether distillation would help at this scale (Section 3.2).

3. **Format sensitivity at small scale:** Gemma 2 2B models show higher variance across formatting variations (std 2.1) compared to larger models (std 0.9-1.0), though still much better than Mistral 7B (std 6.9) (Table 11, Section 5).

4. **Safety limitations:** While Gemma 2 shows lower violation rates overall, the paper acknowledges models cannot cover all applications and scenarios. Users should conduct rigorous safety testing specific to their use case (Section 8).

5. **Higher toxicity scores than Gemma 1:** On RealToxicity and Toxigen benchmarks, Gemma 2 models show **higher average toxicity** than Gemma 1 models (Table 18, Section 8.3). This is a negative result -- improved capability does not uniformly reduce toxicity.

6. **Future research needed:** The authors explicitly state that future research is required to investigate and improve factuality, robustness to adversarial attacks, reasoning, and alignment (Section 9).

7. **[Inferred]** Limited context length: 8192 token context window, shorter than competitors like LLaMA-3 (128K with RoPE scaling) and Qwen2 (128K). The paper does not discuss this as a limitation.

8. **[Inferred]** Limited training detail disclosure: Specific learning rates, optimizer configurations, and total compute costs are not disclosed, impeding independent reproducibility analysis.

9. **[Inferred]** HumanEval regression for 2B: Gemma 2 2B scores 20.1 on HumanEval vs Gemma 1 2B's 22.0, one of the few cases where the new model underperforms the predecessor (Table 13, Section 6.1).

### Scope and Comparability

- **What was not tested:** Long-context evaluation beyond 8K tokens; multilingual benchmarks; multimodal tasks; distillation at 27B+ scale; intermediate training token counts between compute-optimal and 50x.
- **Comparability notes:** Comparison with LLaMA-3 70B is not apples-to-apples due to 2.5x size difference and different training token counts. The paper uses **total parameters** (not active) for comparison since "total memory usage is often what limits the use of open models on standard devices" (Section 6). Some baseline numbers for AGIEval and BBH use different evaluation procedures (marked with daggers/circles), leading to +3-4% inflation compared to the authors' own evaluation (Table 13 footnotes).

---

## Conclusions

### Contributions

1. **Knowledge distillation as scaling alternative.** Demonstrates that distilling from a larger teacher provides richer gradients than next-token prediction, enabling training beyond available token counts and achieving +7.4 points improvement over training from scratch at 2B scale (Table 6, Section 5). Benefit persists across 200M-1B model sizes (Table 7).

2. **State-of-the-art open models at practical sizes.** Releases 2B, 9B, and 27B models that outperform competitors at similar or larger sizes: Gemma 2 27B beats Qwen1.5 32B on all benchmarks and approaches LLaMA-3 70B despite being 2.5x smaller (Table 12, Section 6.1). On LMSYS Chatbot Arena, Gemma 2 27B IT (Elo 1218) outranks LLaMA-3 70B Instruct (Elo 1206) (Table 14, Section 6.2).

3. **Architectural innovations for stability and efficiency.** Combines interleaved local-global attention, logit soft-capping, GQA with num_groups=2, and dual pre-norm/post-norm with RMSNorm. Ablations validate each choice (Tables 8-10, Section 5).

4. **Comprehensive safety evaluation.** Extensive assurance evaluations including offensive cyber-security, CBRN knowledge, self-proliferation, and persuasion capabilities, finding Gemma 2 has low capabilities in high-risk domains while performing well on safety benchmarks (Tables 18-25, Section 8).

5. **Significantly reduced memorization.** Verbatim memorization rates below 0.1%, significantly lower than Gemma 1 across all data sources. Very low rate (0.00026%) of memorized data containing personal information (Figure 1, Section 7).

### Implications

1. **Distillation may extend effective training.** The success of training 50x beyond compute-optimal tokens with distillation suggests this approach may circumvent diminishing returns from data scaling alone. The distillation objective effectively simulates training beyond the number of available tokens (Section 1; speculative: could enable "synthetic" data augmentation effects).

2. **Depth over width at matched parameters.** The finding that deeper 9B networks outperform wider ones (+1.2 points, Table 9) may inform future architecture design for practical-sized models, though evidence is from a single model size.

3. **GQA as standard for open models.** Following Qwen2 and LLaMA 3, adoption of GQA across all sizes suggests this is becoming the de facto standard for efficient inference. The ablation shows no performance loss with GQA (Table 8).

4. **Safety-capability tension.** Higher toxicity scores despite improved capabilities (Table 18) suggests that capability improvements do not automatically translate to safety improvements, reinforcing the need for dedicated safety training.

---

## Key Claims

1. **C1:** A 2B model trained with knowledge distillation achieves 67.7 average on 3 benchmarks vs 60.3 from scratch training (+7.4 points) (Table 6, Section 5). Status: **supported**. Scope: 500B tokens, 7B teacher, 2B student. Magnitude: +7.4 points. Evidence breadth: single model size, single teacher, 3 benchmarks (moderate evidence); corroborated by Table 7 showing consistent gains at 200M, 400M, and 1B scales.

2. **C2:** Gemma 2 27B outperforms Qwen1.5 32B on all HuggingFace evaluation benchmarks: MMLU 75.2 vs 74.3, GSM8K 74.0 vs 61.1, ARC-c 71.4 vs 63.6, HellaSwag 86.4 vs 85.0, Winogrande 83.7 vs 81.5 (Table 12, Section 6.1). Status: **supported**. Scope: 5 HuggingFace leaderboard benchmarks, single evaluation per configuration. Magnitude: +0.9 to +12.9 points across benchmarks. Evidence breadth: 5 benchmarks, single run per configuration, no variance reported (moderate evidence).

3. **C3:** Gemma 2 27B is competitive with LLaMA-3 70B despite being 2.5x smaller and trained on 2/3 less data: MMLU 75.2 vs 79.2, GSM8K 74.0 vs 76.9, HellaSwag 86.4 vs 88.0 (Table 12, Section 6.1). Status: **supported**. Scope: 5 benchmarks, pre-trained models. Magnitude: within 2-5% on most benchmarks. Evidence breadth: same 5 benchmarks as C2, single run (moderate evidence).

4. **C4:** Gemma 2 9B IT achieves Elo 1187 on LMSYS Chatbot Arena, nearly identical to GPT-4-0314 (Elo 1186) (Table 14, Section 6.2). Status: **supported**. Scope: blind human evaluations, snapshot in time. Magnitude: within 1 Elo point. Evidence breadth: single evaluation period, crowd-sourced human judgments (moderate evidence; Elo confidence intervals overlap).

5. **C5:** GQA with num_groups=2 maintains downstream performance (50.8 vs 50.3 for MHA) while enabling faster inference (Table 8, Section 5). Status: **supported**. Scope: 9B model, 4 benchmarks. Magnitude: +0.5 points average. Evidence breadth: single model size, 4 benchmarks (limited evidence).

6. **C6:** Deeper 9B architecture outperforms wider 9B by +1.2 points average on 4 benchmarks (52.0 vs 50.8) (Table 9, Section 5). Status: **supported**. Scope: 9B model, matched parameter count. Magnitude: +1.2 points. Evidence breadth: single model size, 4 benchmarks, gap is small but consistent (limited evidence).

7. **C7:** Gemma 2 memorizes significantly less than prior models, with verbatim memorization rates below 0.1% (Figure 1, Section 7). Status: **supported**. Scope: 50-token continuation, exact match criterion, uniform sample of training data. Magnitude: below 0.1%, substantially lower than Gemma 1 (note log y-axis). Evidence breadth: all model sizes tested, both exact and approximate memorization, multiple data sources (strong evidence).

8. **C8:** Distillation benefit persists as model size increases: 200M, 400M, and 1B models all show ~2-point perplexity reduction with a 7B teacher (Table 7, Section 5). Status: **supported**. Scope: 200M-1B models, 7B teacher, validation perplexity. Magnitude: 2-point perplexity reduction at each scale. Evidence breadth: 3 model sizes, single teacher, single metric (moderate evidence).

9. **C9:** Gemma 2 27B IT achieves Elo 1218 on LMSYS Chatbot Arena, ranked higher than LLaMA-3 70B Instruct (Elo 1206) despite being 2.5x smaller (Table 14, Section 6.2). Status: **supported**. Scope: LMSYS Chatbot Arena, snapshot in time. Magnitude: +12 Elo points. Evidence breadth: single evaluation period, human judgments (moderate evidence).

10. **C10:** Sliding window size can be reduced at inference time with minimal perplexity impact: 4096->1024 increases perplexity by only 0.01 (Table 10, Section 5). Status: **supported**. Scope: 9B model, validation set perplexity. Magnitude: 0.01 perplexity increase (1.63 to 1.64). Evidence breadth: single model, single metric (limited evidence).

11. **C11:** Gemma 2 models produce safer responses than GPT-4o on held-out safety prompts, regardless of model size (Table 15, Section 6.2). Status: **supported**. Scope: held-out safety prompt set, side-by-side with GPT-4o. Magnitude: 53-57.5% safety win rate vs GPT-4o. Evidence breadth: 3 model sizes, human-rated, single safety prompt set (moderate evidence).

---

## Open Questions

1. **Distillation scaling.** Would distilling the 27B model from an even larger teacher yield gains? The paper only applies distillation to 2B and 9B. Not addressed by subsequent work in this repository.

2. **Optimal teacher-student ratio.** The paper uses roughly 3-4x teacher-to-student size ratio (7B->2B, 27B->9B). Is this optimal? Not addressed.

3. **Context extension.** The 8K context is shorter than competitors. Can the interleaved local-global attention pattern be extended while maintaining efficiency? Not addressed.

4. **Distillation data efficiency.** How does the distillation benefit vary with training token count? The paper shows 50x compute-optimal but doesn't ablate intermediate points. Not addressed.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundation decoder-only Transformer architecture that Gemma 2 builds upon.
- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models.* Gemma 2 uses GQA with num_groups=2 across all model sizes.
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE positional embeddings used in all Gemma 2 models.
- **Shazeer (2020)** -- *GLU Variants Improve Transformer.* GeGLU activation function used in all Gemma 2 models.

### Efficient Attention

- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Gemma 2 adopts interleaved local sliding window and global attention pattern from Longformer.
- **Zhang and Sennrich (2019)** -- *Root Mean Square Layer Normalization.* RMSNorm used for both pre-norm and post-norm in all sub-layers.

### Knowledge Distillation

- **Hinton et al. (2015)** -- *Distilling the Knowledge in a Neural Network.* Foundational knowledge distillation work that Gemma 2's training approach extends.
- **Agarwal et al. (2024)** -- *On-Policy Distillation of Language Models.* Recent on-policy distillation techniques applied in Gemma 2's SFT phase.
- **Gu et al. (2024)** -- *MiniLLM: Knowledge Distillation of Large Language Models.* Distillation from teacher on student's distribution during SFT.

### Post-Training and Model Merging

- **Rame et al. (2024)** -- *WARP: On the Benefits of Weight Averaged Rewarded Policies.* Model merging technique used to combine checkpoints from different hyperparameter runs.
- **Zheng et al. (2023)** -- *LMSYS-Chat-1M.* Prompts (not answers) used for post-training data.

### Training Infrastructure

- **Barham et al. (2022)** -- *Pathways: Asynchronous Distributed Dataflow for ML.* Pathways approach used for data-replica reduction and single controller programming.
- **Ren et al. (2021)** -- *ZeRO-Offload.* ZeRO-3 style optimizer state sharding used in training.
- **Xu et al. (2021)** -- *GSPMD.* GSPMD partitioner used for training step computation.

### Scaling Laws

- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models.* Chinchilla scaling laws that Gemma 2's distillation approach exceeds by 50x, establishing the baseline for compute-optimal training.

### Competing Models

- **AI@Meta (2024)** -- *LLaMA 3 Model Card.* Primary comparison baseline; Gemma 2 27B approaches LLaMA-3 70B despite 2.5x smaller size.
- **Jiang et al. (2023)** -- *Mistral 7B.* 7B-class baseline; Gemma 2 shows much better format robustness (std 0.9 vs 6.9).
- **Gemma Team (2024)** -- *Gemma: Open Models Based on Gemini Research.* Direct predecessor; Gemma 2 demonstrates major improvements across all sizes.

### Evaluation

- **Chiang et al. (2024)** -- *Chatbot Arena: An Open Platform for Evaluating LLMs.* Primary human evaluation benchmark where Gemma 2 sets new open-model records.
- **Hendrycks et al. (2020)** -- *Measuring Massive Multitask Language Understanding.* MMLU benchmark for knowledge evaluation.

### Safety and Responsibility

- **Phuong et al. (2024)** -- *Evaluating Frontier Models for Dangerous Capabilities.* Methodology for assurance evaluations including cyber-security, CBRN, self-proliferation, and persuasion.
- **Shevlane et al. (2023)** -- *Model Evaluation for Extreme Risks.* Framework for capabilities relevant to extreme risks referenced in assurance evaluations.
