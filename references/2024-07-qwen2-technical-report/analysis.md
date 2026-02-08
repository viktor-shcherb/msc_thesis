---
title: "Qwen2 Technical Report"
authors: "Yang, Yang, Hui, Zheng, Yu, Zhou, Li, Li, Liu, Huang, et al."
year: 2024
venue: "arXiv preprint 2407.10671"
paper_type: preprint
categories: ["model-release", "architecture", "context-extension"]
scope: ["open foundation models", "multilingual LLMs", "mixture-of-experts", "grouped-query attention", "long-context training", "data scaling"]
benchmarks_used: ["mmlu", "mmlu-pro", "gpqa", "humaneval", "mbpp", "gsm8k", "math-hendrycks", "bbh", "hellaswag", "winogrande", "truthfulqa", "arc", "ifeval", "mgsm", "niah", "mt-bench", "arena-hard", "livecodebench", "evalplus", "multipl-e", "c-eval", "cmmlu", "needlebench", "lv-eval", "theorem-qa", "mixeval", "alignbench"]
models_introduced: ["qwen2-0.5b", "qwen2-1.5b", "qwen2-7b", "qwen2-57b-a14b", "qwen2-72b"]
models_evaluated: ["llama-3-8b", "llama-3-70b", "mistral-7b", "gemma-7b", "mixtral-8x7b", "gpt-4", "gpt-4o"]
key_claims:
  - id: C1
    claim: "Qwen2-72B outperforms Llama-3-70B on MMLU by +4.7 (84.2 vs 79.5) and MMLU-Pro by +2.8 (55.6 vs 52.8)"
    evidence: "Table 2, Section 5.1.1"
    status: supported
    scope: "72B scale, 5-shot evaluation, English benchmarks"
    magnitude: "84.2 MMLU (vs 79.5 Llama-3-70B), 55.6 MMLU-Pro (vs 52.8 Llama-3-70B)"
  - id: C2
    claim: "Enriched code and math data yields +18.3 on HumanEval (64.6 vs 46.3) and +10.0 on GSM8K (89.5 vs 79.5) over Qwen1.5-72B"
    evidence: "Table 2, Section 5.1.1"
    status: supported
    scope: "72B scale, 0-shot HumanEval, 5-shot GSM8K, comparing Qwen2-72B vs Qwen1.5-72B"
    magnitude: "+18.3 HumanEval (64.6 vs 46.3), +10.0 GSM8K (89.5 vs 79.5), +17.0 MATH (51.1 vs 34.1)"
  - id: C3
    claim: "Qwen2-57B-A14B (MoE, 14B active) matches 30B dense model performance while activating only 14B parameters per forward pass"
    evidence: "Table 3, Section 5.1.1"
    status: supported
    scope: "57B total / 14B activated MoE, compared against Yi-1.5-34B (dense 32B) and Qwen1.5-32B (dense 34B)"
    magnitude: "Comparable NLU (MMLU 76.5 vs Yi-1.5-34B 77.1), superior coding (HumanEval 53.0 vs 46.3) and math (MATH 43.0 vs 41.7)"
  - id: C4
    claim: "YARN + DCA enables 128K context with near-perfect NIAH accuracy for Qwen2-72B-Instruct and Qwen2-7B-Instruct"
    evidence: "Figure 1, Table 12, Section 5.2.3"
    status: supported
    scope: "72B and 7B instruct models, NIAH retrieval test, 8K-128K context lengths"
    magnitude: "NeedleBench 128K: 73.05 to 90.27 (+17.22) for 72B; NeedleBench 256K: 17.13 to 85.21 (+68.08) for 72B"
  - id: C5
    claim: "Qwen2-72B-Instruct achieves multilingual human evaluation scores competitive with GPT-4-Turbo (3.93 vs 3.98 average) across 10 languages"
    evidence: "Table 13, Section 5.2.4"
    status: supported
    scope: "72B instruct model, human evaluation on 10 languages (Arabic, French, Indonesian, Japanese, Korean, Portuguese, Russian, Spanish, Thai, Vietnamese), 1-5 scoring scale"
    magnitude: "3.93 average (vs GPT-4-Turbo 3.98, GPT-4o 4.09, Claude-3-Opus 4.15)"
  - id: C6
    claim: "Expanding pre-training data from 3T to 7T tokens improves performance, but further relaxation to 12T tokens with lower quality does not yield significant gains"
    evidence: "Section 3.1"
    status: supported
    scope: "Dense models, data quality threshold comparison between 7T and 12T token datasets"
    magnitude: "qualitative (no specific numerical comparison reported between 7T and 12T models)"
  - id: C7
    claim: "Data scaling remains effective for sub-billion parameter models: Qwen2-0.5B and Qwen2-1.5B significantly outperform Qwen1.5 counterparts"
    evidence: "Table 5, Table 9, Section 5.1.1"
    status: supported
    scope: "0.5B (0.3B non-embedding) and 1.5B (1.2B non-embedding) parameter models, Qwen2-0.5B trained on 12T tokens"
    magnitude: "Qwen2-1.5B: MMLU 56.5 (vs Qwen1.5-1.8B 46.8), GSM8K 58.5 (vs 38.4), HumanEval 31.1 (vs 20.1)"
  - id: C8
    claim: "Contamination analysis shows no significant performance degradation between original and non-contaminated test sets despite high nominal contamination rates on some benchmarks"
    evidence: "Table 15, Section 5.2.6"
    status: supported
    scope: "Qwen2-72B-Instruct and Qwen2-7B-Instruct, strict 13-gram overlap criterion, 9 benchmarks"
    magnitude: "Qwen2-72B-Instruct deltas: MMLU +0.9, GSM8K -0.4, IFEval -0.2; despite HumanEval 75.0% nominal contamination rate"
cross_references:
  - target: 2023-09-qwen-technical-report
    type: extends
    detail: "Direct successor to Qwen 1, scaling from 3T to 7T tokens, adding GQA, extending context from 8K to 32K (128K with YARN), and introducing MoE variant"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Builds on decoder-only Transformer with GQA, SwiGLU, RoPE, QKV bias, RMSNorm, and pre-normalization"
  - target: 2023-11-needle-in-a-haystack
    type: uses-benchmark
    detail: "Uses NIAH to evaluate long-context retrieval up to 128K tokens across all model sizes"
  - target: 2023-07-llama-2-open-foundation-chat
    type: evaluates
    detail: "Compares Qwen2 against Llama-3-8B and Llama-3-70B across core capability and instruction-tuned benchmarks"
  - target: 2023-10-mistral-7b
    type: evaluates
    detail: "Compares Qwen2-7B against Mistral-7B on 7B-class base model benchmarks"
  - target: 2024-05-yarn-context-extension
    type: extends
    detail: "Uses YARN to rescale attention weights for length extrapolation beyond 32K tokens, enabling up to 131K context"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Uses RoPE positional embeddings with base frequency scaled from 10,000 to 1,000,000 for long-context training"
  - target: 2025-05-qwen3-technical-report
    type: extended-by
    detail: "Qwen3 extends Qwen2 with 36T tokens (vs 7T), 119 languages (vs 29), thinking/non-thinking mode fusion, and improved MoE architecture"
  - target: 2024-08-gemma-2-technical-report
    type: concurrent
    detail: "Both released mid-2024 as competitive open-weight model families with GQA; Qwen2 focuses on data scaling to 7T tokens while Gemma 2 focuses on knowledge distillation for smaller models"
open_questions:
  - question: "Does the lack of improvement from 7T to 12T tokens indicate a data quality ceiling, or would better filtering at scale yield further gains?"
    addressed_by: null
  - question: "Can the MoE architecture with fine-grained experts scale beyond 57B total parameters while maintaining efficient routing?"
    addressed_by: 2025-05-qwen3-technical-report
  - question: "Why does Qwen2-7B-Instruct significantly underperform Llama-3-8B-Instruct on instruction following (IFEval 54.7 vs 72.1) despite competitive overall performance?"
    addressed_by: null
  - question: "What is the optimal trade-off between data quality threshold and data volume for pre-training at different model scales?"
    addressed_by: null
---

# Qwen2 Technical Report

**Authors:** An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, et al. (62 authors, Qwen Team, Alibaba Group)
**Date:** July 2024, arXiv:2407.10671

---

## Core Research Problem

Open-weight large language models have rapidly narrowed the gap with proprietary models, but significant challenges remain in building competitive model families that span a wide range of sizes (from sub-billion to 70B+ parameters), support strong multilingual capabilities across dozens of languages, and handle long contexts reliably. Prior open-weight models such as Llama 2 (Touvron et al., 2023), Llama 3 (AI@Meta, 2024), and Mistral 7B (Jiang et al., 2023a) have advanced the state of the art, but gaps persist in coding, mathematics, and multilingual performance relative to proprietary models like GPT-4o and Claude-3 Opus (Section 1).

The predecessor Qwen1.5 (Qwen Team, 2024a) was trained on 3 trillion tokens and demonstrated competitive performance but had limited multilingual coverage, a 4,096-token context window, and used conventional multi-head attention with associated KV cache overhead (Sections 1, 3.1).

**The core challenge: how to build a comprehensive open-weight model family that achieves competitive performance with proprietary models across language understanding, coding, mathematics, reasoning, and multilingual tasks, while supporting efficient inference and long-context processing up to 128K tokens.**

---

## Problem Solutions

The Qwen2 series addresses these challenges through a combination of architectural improvements, data scaling, and improved post-training (Section 1):

1. **Grouped Query Attention (GQA)** replaces multi-head attention across all model sizes, reducing KV cache memory and improving inference throughput (Section 2.2.1).
2. **Dual Chunk Attention (DCA) with YARN** enables context extension from 32K to 131,072 tokens without significant performance degradation (Sections 2.2.1, 3.2).
3. **Pre-training data scaling** from 3T to 7T tokens with enhanced quality filtering and expanded coverage of code, mathematics, and ~30 languages (Section 3.1).
4. **Mixture-of-Experts (MoE) variant** using fine-grained experts and shared/routing-specific expert design achieves dense-model performance with fewer activated parameters (Section 2.2.2).
5. **Scalable post-training** with collaborative annotation, automated data synthesis (rejection sampling, execution feedback, data repurposing, constitutional feedback), and a two-stage RLHF pipeline (offline DPO + online DPO with reward models) (Section 4).

---

## Approach Details

### Method

#### Dense Model Architecture

Qwen2 dense models are decoder-only Transformers with causal attention (Section 2.2.1). Key architectural choices:

- **Grouped Query Attention (GQA):** All sizes use GQA (Ainslie et al., 2023) instead of conventional MHA. KV head counts range from 2 (0.5B, 1.5B) to 8 (72B), significantly reducing KV cache memory.
- **Dual Chunk Attention (DCA):** Segments long sequences into manageable chunks (An et al., 2024). For inputs within a single chunk, DCA produces identical results to standard attention. For longer inputs, it captures relative positional information within and across chunks.
- **YARN:** Rescales attention weights for length extrapolation (Peng et al., 2023).
- **Other components:** SwiGLU activation (Dauphin et al., 2017), RoPE positional embeddings (Su et al., 2024), QKV bias (Su, 2023), RMSNorm (Jiang et al., 2023b), pre-normalization.

**Table 1** (p. 5): Architecture of Qwen2 dense and MoE models.

| Configuration | 0.5B | 1.5B | 7B | 72B | 57B-A14B |
|---|---|---|---|---|---|
| Hidden Size | 896 | 1,536 | 3,584 | 8,192 | 3,584 |
| # Layers | 24 | 28 | 28 | 80 | 28 |
| # Query Heads | 14 | 12 | 28 | 64 | 28 |
| # KV Heads | 2 | 2 | 4 | 8 | 4 |
| Head Size | 64 | 128 | 128 | 128 | 128 |
| Intermediate Size | 4,864 | 8,960 | 18,944 | 29,568 | 2,560 |
| # Routed Experts | - | - | - | - | 64 |
| # Activated Experts | - | - | - | - | 8 |
| # Shared Experts | - | - | - | - | 8 |
| Embedding Tying | True | True | False | False | False |
| Vocabulary Size | 151,646 | 151,646 | 151,646 | 151,646 | 151,646 |
| # Trained Tokens | 12T | 7T | 7T | 7T | 4.5T |

#### MoE Architecture

Qwen2-57B-A14B uses a Mixture-of-Experts architecture with fine-grained experts (Section 2.2.2). The MoE FFN replaces the dense FFN:

> **p** = softmax(G(**x**))

> **y** = Sum_{i in top_k(**p**)} **p**_i E_i(**x**)

Equation (1) computes the routing probabilities over all experts via softmax of the gating network output. Equation (2) computes the final output as a weighted sum of the top-k selected experts' outputs.

Key MoE design choices:

- **Fine-grained experts:** Rather than using full-sized FFN experts (as in Mixtral's transition from Mistral-7B to 8x7B), Qwen2 MoE uses smaller experts with more activated simultaneously, providing a richer set of expert combinations. Configuration: 64 routed experts, 8 activated per token, 8 shared experts, each with intermediate size 2,560 (Section 2.2.2).
- **Shared and routing-specific experts:** Shared experts handle common patterns across tasks; routing-specific experts specialize (Section 2.2.2).
- **Expert initialization via upcycling:** Initializes from the dense Qwen2-7B model (Komatsuzaki et al., 2023). The FFN is replicated ceil(n x h_E / h_FFN) times, parameters are shuffled along the intermediate dimension for diversity, fine-grained experts are extracted, and **50% of each expert's parameters are randomly reinitialized** to enhance exploration during training (Section 2.2.2).

---

### Key Technical Components

#### Tokenizer

Byte-level byte-pair encoding tokenizer identical to Qwen (Bai et al., 2023a). Vocabulary of **151,643 regular tokens + 3 control tokens**, shared across all model sizes. High compression rate facilitates multilingual capabilities (Section 2.1).

#### Pre-training Data

The pre-training corpus expanded from 3T tokens (Qwen1.5) to **7T tokens** for all dense models except Qwen2-0.5B (12T tokens) (Section 3.1):

- **Quality enhancement:** Refined filtering with heuristic and model-based methods, including using Qwen models to filter low-quality data and synthesize high-quality pre-training data.
- **Data expansion:** Significantly more code, mathematics, and multilingual data covering **approximately 30 languages** (English, Chinese, Spanish, French, German, Arabic, Russian, Korean, Japanese, Thai, Vietnamese, etc.).
- **Distribution improvement:** Scaled-down model experiments to optimize data mixing across sources and domains.
- **12T experiment:** Relaxing quality thresholds to create a 12T token dataset did not significantly improve over 7T, as the authors "suspect that increasing the volume of data does not necessarily benefit model pre-training" (Section 3.1).
- **Multi-task instruction data:** Integrated into pre-training to enhance in-context learning and instruction-following.
- **MoE pre-training:** Qwen2-57B-A14B received an additional **4.5 trillion tokens**, consistent with the upcycling approach (Section 3.1).

#### Long-Context Training

Context length extended from 4,096 to **32,768 tokens** during the final pre-training phase (Section 3.2):

- RoPE base frequency changed from **10,000 to 1,000,000** (following Xiong et al., 2023).
- Complemented by increased volume of high-quality long-form data.
- YARN + DCA enable processing up to **131,072 tokens** with minimal perplexity degradation in preliminary experiments.

#### Post-Training Pipeline

**Supervised Fine-Tuning (SFT)** (Section 4.2):
- **500,000+ instruction examples** covering instruction following, coding, mathematics, logical reasoning, role-playing, multilingualism, and safety.
- 2 epochs, sequence length 32,768, learning rate 7x10^-6 to 7x10^-7, weight decay 0.1, gradient clipping at 1.0.

**RLHF (two stages)** (Section 4.3):
1. **Offline DPO:** Pre-compiled preference dataset P, maximizing likelihood difference between preferred and dispreferred responses using DPO (Rafailov et al., 2023).
2. **Online DPO:** Current policy model generates multiple responses; reward model selects best and worst to form preference pairs for iterative DPO.
- **Online Merging Optimizer** (Lu et al., 2024a) mitigates the alignment tax.

**Post-training data construction** (Section 4.1):
- **Collaborative annotation:** InsTag ontology extraction (Lu et al., 2024c) -> instruction selection (Dong et al., 2023) -> instruction evolution (Zhao et al., 2024) -> human ranking.
- **Automated synthesis:** Rejection sampling for math (Yuan et al., 2023), execution feedback for code (Dong et al., 2024), data repurposing for literary writing (Lu et al., 2024b), constitutional feedback for safety (Bai et al., 2022).

---

### Experimental Setup

**Base model evaluation** (Section 5.1): Few-shot prompting on standard benchmarks. MMLU (5-shot), MMLU-Pro (5-shot), GPQA (5-shot), TheoremQA (5-shot), BBH (3-shot), HellaSwag (10-shot), Winogrande (5-shot), TruthfulQA (0-shot), ARC-C (25-shot), HumanEval (0-shot), MBPP (0-shot), EvalPlus (0-shot), MultiPL-E (0-shot on Python, C++, Java, PHP, TypeScript, C#, Bash, JavaScript), GSM8K (5-shot), MATH (4-shot), C-Eval (5-shot), CMMLU (5-shot).

**Multilingual base evaluation** (Section 5.1): Grouped into four categories: (a) Exam: M3Exam (5-shot), IndoMMLU (3-shot), ruMMLU (5-shot), translated MMLU (5-shot); (b) Understanding: BELEBELE (5-shot), XCOPA (5-shot), XWinograd (5-shot), XStoryCloze (0-shot), PAWS-X (5-shot); (c) Mathematics: MGSM (8-shot CoT); (d) Translation: Flores-101 (5-shot).

**Instruction-tuned evaluation** (Section 5.2): MMLU, MMLU-Pro, GPQA, TheoremQA, HumanEval, MBPP, MultiPL-E, LiveCodeBench v1, GSM8K, MATH, MT-Bench, Arena-Hard, AlignBench, MixEval, IFEval (strict-prompt).

**Long context** (Section 5.2.3): Needle in a Haystack (8K-128K), NeedleBench (8K-256K), LV-Eval (16K-256K). YARN applied for contexts >32K tokens.

**Baselines:** Llama-3-70B, Llama-3-8B, Mixtral-8x22B, Mixtral-8x7B, Mistral-7B, Gemma-7B, Gemma-2B, Yi-1.5-34B, Yi-1.5-9B, Phi-2, Jamba, GLM-4-9B, Qwen1.5 series, GPT-4, GPT-4o, GPT-3.5-Turbo, Claude-3-Opus.

**Reproducibility:** Model weights are openly available on Hugging Face and ModelScope. Code, quantization, fine-tuning, and deployment resources on GitHub. However, specific training infrastructure, pre-training learning rate schedules, optimizer configurations, and total compute costs are not disclosed.

---

### Key Results

#### Base Model: Qwen2-72B vs 70B+ Baselines (Table 2)

| Benchmark | Mixtral-8x22B | Llama-3-70B | Qwen1.5-72B | Qwen1.5-110B | **Qwen2-72B** |
|---|---|---|---|---|---|
| MMLU | 77.8 | 79.5 | 77.5 | 80.4 | **84.2** |
| MMLU-Pro | 49.5 | 52.8 | 45.8 | 49.4 | **55.6** |
| GPQA | 34.3 | 36.3 | 36.3 | 35.9 | **37.9** |
| TheoremQA | 35.9 | 32.3 | 29.3 | 34.9 | **43.1** |
| BBH | 78.9 | 81.0 | 65.5 | 74.8 | **82.4** |
| HellaSwag | **88.7** | 88.0 | 86.0 | 87.5 | 87.6 |
| Winogrande | 85.0 | **85.3** | 83.0 | 83.5 | 85.1 |
| ARC-C | **70.7** | 68.8 | 65.9 | 69.6 | 68.9 |
| TruthfulQA | 51.0 | 45.6 | **59.6** | 49.6 | 54.8 |
| HumanEval | 46.3 | 48.2 | 46.3 | 54.3 | **64.6** |
| MBPP | 71.7 | 70.4 | 66.9 | 70.9 | **76.9** |
| EvalPlus | 54.1 | 54.8 | 52.9 | 57.7 | **65.4** |
| MultiPL-E | 46.7 | 46.3 | 41.8 | 52.7 | **59.6** |
| GSM8K | 83.7 | 83.0 | 79.5 | 85.4 | **89.5** |
| MATH | 41.7 | 42.5 | 34.1 | 49.6 | **51.1** |
| C-Eval | 54.6 | 65.2 | 84.1 | 89.1 | **91.0** |
| CMMLU | 53.4 | 67.2 | 83.5 | 88.3 | **90.1** |
| Multilingual Exam | 63.5 | 70.0 | 66.4 | 75.6 | **76.6** |
| Multilingual Understanding | 77.7 | 79.9 | 78.2 | 78.2 | **80.7** |
| Multilingual Mathematics | 62.9 | 67.1 | 61.7 | 64.4 | **76.0** |
| Multilingual Translation | 23.3 | **38.0** | 35.6 | 36.2 | 37.8 |

- Qwen2-72B leads on all benchmarks except HellaSwag (Mixtral-8x22B: 88.7 vs 87.6), Winogrande (Llama-3-70B: 85.3 vs 85.1), ARC-C (Mixtral-8x22B: 70.7 vs 68.9), TruthfulQA (Qwen1.5-72B: 59.6 vs 54.8), and Translation (Llama-3-70B: 38.0 vs 37.8) (Table 2, Section 5.1.1). Tested across 21 benchmarks covering NLU, coding, math, Chinese, and multilingual tasks (strong evidence).
- The largest gains over Qwen1.5-72B are in coding (+18.3 HumanEval, +10.0 MBPP) and mathematics (+10.0 GSM8K, +17.0 MATH), attributed to enriched code and math pre-training data (Section 5.1.1).

#### Base Model: Qwen2-57B-A14B vs 30B+ Dense and 40B+ MoE Baselines (Table 3)

| Benchmark | Jamba | Mixtral-8x7B | Yi-1.5-34B | Qwen1.5-32B | **Qwen2-57B-A14B** |
|---|---|---|---|---|---|
| Architecture | MoE | MoE | Dense | Dense | MoE |
| # Act Params | 12B | 12B | 32B | 34B | 14B |
| # Params | 52B | 47B | 32B | 34B | 57B |
| MMLU | 67.4 | 71.8 | **77.1** | 74.3 | 76.5 |
| MMLU-Pro | - | 41.0 | **48.3** | 44.0 | 43.0 |
| GPQA | - | 29.2 | - | 30.8 | **34.3** |
| TheoremQA | - | 23.2 | - | 28.8 | **33.5** |
| BBH | 45.4 | 50.3 | **76.4** | 66.8 | 67.0 |
| HellaSwag | **87.1** | 86.5 | 85.9 | 85.0 | 85.2 |
| Winogrande | 82.5 | 81.9 | **84.9** | 81.5 | 79.5 |
| ARC-C | 64.4 | **66.0** | 65.6 | 63.6 | 64.1 |
| TruthfulQA | 46.4 | 51.1 | 53.9 | 57.4 | **57.7** |
| HumanEval | 29.3 | 37.2 | 46.3 | 43.3 | **53.0** |
| MBPP | - | 63.9 | 65.5 | 64.2 | **71.9** |
| EvalPlus | - | 46.4 | 51.9 | 50.4 | **57.2** |
| MultiPL-E | - | 39.0 | 39.5 | 38.5 | **49.8** |
| GSM8K | 59.9 | 62.5 | **82.7** | 76.8 | 80.7 |
| MATH | - | 30.8 | 41.7 | 36.1 | **43.0** |
| C-Eval | - | - | - | 83.5 | **87.7** |
| CMMLU | - | - | 84.8 | 82.3 | **88.5** |
| Multilingual Exam | - | 56.1 | 58.3 | 61.6 | **65.5** |
| Multilingual Understanding | - | 70.7 | 73.9 | 76.5 | **77.0** |
| Multilingual Mathematics | - | 45.0 | 49.3 | 56.1 | **62.3** |
| Multilingual Translation | - | 29.8 | 30.0 | 33.5 | **34.5** |

- Qwen2-57B-A14B performs comparably to Yi-1.5-34B in NLU (MMLU 76.5 vs 77.1) while activating only 14B parameters. It outperforms all baselines in coding (HumanEval 53.0) and math (MATH 43.0), and demonstrates strong Chinese and multilingual capabilities (Table 3, Section 5.1.1). Tested against 2 MoE and 2 dense baselines across 21 benchmarks (moderate evidence; only one MoE size tested).

#### Base Model: Qwen2-7B vs 7B+ Baselines (Table 4)

| Benchmark | Mistral-7B | Gemma-7B | Llama-3-8B | Qwen1.5-7B | **Qwen2-7B** |
|---|---|---|---|---|---|
| MMLU | 64.2 | 64.6 | 66.6 | 61.0 | **70.3** |
| MMLU-Pro | 30.9 | 33.7 | 35.4 | 29.9 | **40.0** |
| GPQA | 24.7 | 25.7 | 25.8 | 26.7 | **31.8** |
| TheoremQA | 19.2 | 21.5 | 22.1 | 14.2 | **31.1** |
| BBH | 56.1 | 55.1 | 57.7 | 40.2 | **62.6** |
| HellaSwag | **83.2** | 82.2 | 82.1 | 78.5 | 80.7 |
| Winogrande | 78.4 | **79.0** | 77.4 | 71.3 | 77.0 |
| ARC-C | 60.0 | **61.1** | 59.3 | 54.2 | 60.6 |
| TruthfulQA | 42.2 | 44.8 | 44.0 | 51.1 | **54.2** |
| HumanEval | 29.3 | 37.2 | 33.5 | 36.0 | **51.2** |
| MBPP | 51.1 | 50.6 | 53.9 | 51.6 | **65.9** |
| EvalPlus | 36.4 | 39.6 | 40.3 | 40.0 | **54.2** |
| MultiPL-E | 29.4 | 29.7 | 22.6 | 28.1 | **46.3** |
| GSM8K | 52.2 | 46.4 | 56.0 | 62.5 | **79.9** |
| MATH | 13.1 | 24.3 | 20.5 | 20.3 | **44.2** |
| C-Eval | 47.4 | 43.6 | 49.5 | 74.1 | **83.2** |
| CMMLU | - | - | 50.8 | 73.1 | **83.9** |
| Multilingual Exam | 47.1 | 42.7 | 52.3 | 47.7 | **59.2** |
| Multilingual Understanding | 63.3 | 58.3 | 68.6 | 67.6 | **72.0** |
| Multilingual Mathematics | 26.3 | 39.1 | 36.3 | 37.3 | **57.5** |
| Multilingual Translation | 23.3 | 31.2 | **31.9** | 28.4 | 31.5 |

- Qwen2-7B outperforms all 7B baselines on most benchmarks, with especially large margins in coding (HumanEval 51.2 vs next-best 37.2) and math (MATH 44.2 vs next-best 24.3). It trails on HellaSwag (Mistral-7B: 83.2), Winogrande (Gemma-7B: 79.0), ARC-C (Gemma-7B: 61.1), and Translation (Llama-3-8B: 31.9) (Table 4, Section 5.1.1). Tested across 21 benchmarks against 4 baselines (strong evidence).

#### Base Model: Qwen2-0.5B and Qwen2-1.5B vs Small Baselines (Table 5)

| Benchmark | Phi-2 | Gemma-2B | Qwen1.5-1.8B | Qwen2-0.5B | **Qwen2-1.5B** |
|---|---|---|---|---|---|
| # Non-Emb Params | 2.5B | 2.0B | 1.2B | 0.3B | 1.2B |
| MMLU | 52.7 | 42.3 | 46.8 | 45.4 | **56.5** |
| MMLU-Pro | - | 15.9 | - | 14.7 | 21.8 |
| TheoremQA | - | - | - | 8.9 | **15.0** |
| BBH | **43.4** | 35.2 | 24.2 | 28.4 | 37.2 |
| HellaSwag | **73.1** | 71.4 | 61.4 | 49.3 | 66.6 |
| Winogrande | **74.4** | 66.8 | 60.3 | 56.8 | 66.2 |
| ARC-C | **61.1** | 48.5 | 37.9 | 31.5 | 43.9 |
| TruthfulQA | 44.5 | 33.1 | 39.4 | 39.7 | **45.9** |
| HumanEval | **47.6** | 22.0 | 20.1 | 22.0 | 31.1 |
| MBPP | **55.0** | 29.2 | 18.0 | 22.0 | 37.4 |
| GSM8K | 57.2 | 17.7 | 38.4 | 36.5 | **58.5** |
| MATH | 3.5 | 11.8 | 10.1 | 10.7 | **21.7** |
| C-Eval | 23.4 | 28.0 | 59.7 | 58.2 | **70.6** |
| CMMLU | 24.2 | - | 57.8 | 55.1 | **70.3** |

- Qwen2-0.5B (0.3B non-embedding parameters, trained on 12T tokens) achieves competitive performance with larger Gemma-2B and Qwen1.5-1.8B in coding (HumanEval 22.0 matching Gemma-2B), while excelling in Chinese (C-Eval 58.2 vs Gemma-2B 28.0) (Table 5, Section 5.1.1). Phi-2 outperforms on general reasoning (BBH, HellaSwag, Winogrande, ARC-C), reflecting the significance of textbook-like training data for reasoning.
- Qwen2-1.5B (1.2B non-embedding) outperforms Phi-2 (2.5B non-embedding) in MMLU (56.5 vs 52.7), GSM8K (58.5 vs 57.2), and MATH (21.7 vs 3.5), demonstrating data scaling effectiveness at sub-billion parameter scale (Table 5, Section 5.1.1).

#### Instruction-Tuned: Qwen2-72B-Instruct (Table 6)

| Benchmark | Mixtral-8x22B | Llama-3-70B | Qwen1.5-72B | Qwen1.5-110B | **Qwen2-72B** |
|---|---|---|---|---|---|
| MMLU | 74.0 | 82.0 | 75.6 | 76.5 | **82.3** |
| MMLU-Pro | 56.1 | 56.2 | 51.7 | 50.5 | **64.4** |
| GPQA | **49.7** | 41.9 | 39.4 | 32.8 | 42.4 |
| TheoremQA | 40.8 | 42.5 | 28.8 | 18.8 | **44.4** |
| HumanEval | 73.8 | 81.7 | 71.3 | 74.4 | **86.0** |
| MBPP | 75.9 | **82.3** | 71.9 | 76.4 | 80.2 |
| MultiPL-E | 61.1 | 63.4 | 48.1 | 55.4 | **69.2** |
| LiveCodeBench v1 | 21.8 | 29.3 | 17.9 | 25.3 | **35.7** |
| GSM8K | 89.1 | 93.0 | 82.7 | 84.5 | **93.2** |
| MATH | 47.4 | 50.4 | 42.5 | 42.0 | **69.0** |
| MT-Bench | 8.66 | 8.95 | 8.61 | 8.88 | **9.12** |
| MixEval | 82.3 | 84.0 | 84.1 | 85.7 | **86.7** |
| Arena-Hard | 36.4 | 41.1 | 36.1 | 39.8 | **48.1** |
| IFEval strict-prompt | 67.1 | 77.3 | 55.8 | 57.5 | **77.6** |
| AlignBench | - | 7.42 | 7.28 | 7.87 | **8.27** |

- Qwen2-72B-Instruct leads on all metrics except GPQA (Mixtral-8x22B: 49.7 vs 42.4) and MBPP (Llama-3-70B: 82.3 vs 80.2) (Table 6, Section 5.2.1). Tested across 15 benchmarks covering knowledge, coding, math, and alignment against 4 baselines (strong evidence).
- MATH shows the most dramatic improvement: 69.0 vs Llama-3-70B 50.4 (+18.6) and Qwen1.5-72B 42.5 (+26.5).

#### Instruction-Tuned: Qwen2-57B-A14B-Instruct (Table 7)

| Benchmark | Mixtral-8x7B | Yi-1.5-34B | Qwen1.5-32B | **Qwen2-57B-A14B** |
|---|---|---|---|---|
| Architecture | MoE | Dense | Dense | MoE |
| # Act Params | 12B | 32B | 34B | 14B |
| # Params | 47B | 32B | 32B | 57B |
| MMLU | 71.4 | **76.8** | 74.8 | 75.4 |
| MMLU-Pro | 43.3 | 52.3 | 46.4 | **52.8** |
| GPQA | - | - | 30.8 | **34.3** |
| TheoremQA | - | - | 30.9 | **33.1** |
| HumanEval | 45.1 | 75.2 | 68.3 | **79.9** |
| MBPP | 59.5 | **74.6** | 67.9 | 70.9 |
| MultiPL-E | - | - | 50.7 | **66.4** |
| LiveCodeBench v1 | 12.3 | - | 15.2 | **25.5** |
| GSM8K | 65.7 | **90.2** | 83.6 | 85.3 |
| MATH | 30.7 | **50.1** | 42.4 | 49.1 |
| MT-Bench | 8.30 | 8.50 | 8.30 | **8.55** |
| MixEval | 70.0 | 81.7 | 81.0 | **82.3** |
| IFEval strict-prompt | - | - | 50.3 | **59.9** |
| AlignBench | 5.70 | 7.20 | 7.19 | **7.36** |

- Qwen2-57B-A14B-Instruct outperforms Qwen1.5-32B-Chat on nearly all benchmarks and is competitive with Yi-1.5-34B-Chat, except in GSM8K (85.3 vs 90.2) and MATH (49.1 vs 50.1). The alignment advantages are notably evident (MT-Bench 8.55, MixEval 82.3) (Table 7, Section 5.2.1).

#### Instruction-Tuned: Qwen2-7B-Instruct (Table 8)

| Benchmark | Llama-3-8B | Yi-1.5-9B | GLM-4-9B | Qwen1.5-7B | **Qwen2-7B** |
|---|---|---|---|---|---|
| MMLU | 68.4 | 69.5 | **72.4** | 59.5 | 70.5 |
| MMLU-Pro | 41.0 | - | - | 29.1 | **44.1** |
| GPQA | 34.2 | - | - | 27.8 | **34.3** |
| TheoremQA | 23.0 | - | - | 14.1 | **25.3** |
| HumanEval | 62.2 | 66.5 | 71.8 | 46.3 | **79.9** |
| MBPP | **67.9** | - | - | 48.9 | 67.2 |
| MultiPL-E | 48.5 | - | - | 27.2 | **59.1** |
| LiveCodeBench v1 | 17.3 | - | - | 6.0 | **26.6** |
| GSM8K | 79.6 | 84.8 | 79.6 | 60.3 | **85.7** |
| MATH | 30.0 | 47.7 | 50.6 | 23.2 | **52.9** |
| MT-Bench | 8.05 | 8.20 | 8.35 | 7.60 | **8.41** |
| MixEval | 75.0 | 74.2 | - | 71.4 | **76.5** |
| IFEval strict-prompt | **72.1** | - | 69.0 | 38.3 | 54.7 |
| AlignBench | 6.20 | 6.90 | 7.01 | 6.20 | **7.21** |

- Qwen2-7B-Instruct demonstrates competitive performance against Llama-3-8B-Instruct, with superior coding (HumanEval 79.9 vs 62.2) and math (MATH 52.9 vs 30.0). However, it **greatly falls behind on instruction following**: IFEval 54.7 vs Llama-3-8B-Instruct 72.1, a -17.4 gap (Table 8, Section 5.2.1). The authors plan to address this through post-training data quality improvements.

#### Instruction-Tuned: Small Models (Table 9)

| Benchmark | Qwen1.5-0.5B | Qwen2-0.5B | Qwen1.5-1.8B | **Qwen2-1.5B** |
|---|---|---|---|---|
| MMLU | 35.0 | **37.9** | 43.7 | **52.4** |
| HumanEval | 10.4 | **29.9** | 27.4 | **47.0** |
| MBPP | 14.5 | **37.8** | 28.6 | **51.9** |
| GSM8K | 11.3 | **40.1** | 35.3 | **61.6** |
| IFEval strict-prompt | 14.6 | **20.0** | 16.8 | **29.0** |

- Both Qwen2 small models significantly outperform their Qwen1.5 predecessors across all benchmarks. Qwen2-1.5B-Instruct achieves HumanEval 47.0 (+19.6 over Qwen1.5-1.8B) and GSM8K 61.6 (+26.3), attributed to pre-training data scaling (Table 9, Section 5.2.1).

#### In-House Evaluation: English (Table 11)

- In English in-house evaluation, Qwen2-72B-Instruct falls behind Llama-3-70B-Instruct in comprehension (73.58 vs 76.31) and coding (53.03 vs 57.18), though it leads in math (82.15 vs 79.70). The authors attribute this gap to the amount of English pre-training tokens and post-training data diversity (Table 11, Section 5.2.2).

#### In-House Evaluation: Chinese (Table 10)

- Qwen2-72B-Instruct outperforms Qwen1.5-110B-Chat despite fewer parameters (69.58 vs 65.86 average). Qwen2-57B-A14B-Instruct underperforms Qwen1.5-32B-Chat specifically in knowledge understanding (64.15 vs 68.63), attributed to insufficient MoE pre-training tokens (Table 10, Section 5.2.2).

#### Long Context Evaluation

- **NIAH (Figure 1, Section 5.2.3):** Qwen2-72B-Instruct achieves near-perfect accuracy across the full 128K context at all document depths. Qwen2-7B-Instruct also handles 128K tokens at high accuracy (single small degradation patch around 32K-40K context at mid-depth). Qwen2-57B-A14B-Instruct supports up to 64K, smaller models up to 32K. All models above 32K integrate YARN.
- **NeedleBench + LV-Eval with YARN+DCA (Table 12, Section 5.2.3):**

| Model | NeedleBench 8K | NeedleBench 32K | NeedleBench 128K | NeedleBench 256K | LV-Eval 16K | LV-Eval 32K | LV-Eval 64K | LV-Eval 128K | LV-Eval 256K |
|---|---|---|---|---|---|---|---|---|---|
| ChatGLM4-9B-1M | 56.61 | 49.15 | 44.30 | 45.29 | 46.40 | 43.23 | 42.92 | 40.41 | 36.95 |
| Qwen2-7B-Instruct | 87.07 | 73.64 | 38.77 / **66.32** | 2.92 / **60.71** | 49.77 | 46.93 | 28.03 / **42.14** | 11.01 / **36.64** | 0.55 / **34.72** |
| Qwen2-72B-Instruct | **91.90** | **92.01** | 73.05 / **90.27** | 17.13 / **85.21** | **58.82** | **56.70** | 42.92 / **53.03** | 31.79 / **48.83** | 2.88 / **42.35** |

*Values shown as x / y: x = without YARN+DCA, y = with YARN+DCA. YARN+DCA does not change behavior within 32K tokens.*

- YARN + DCA dramatically improves ultra-long context performance. For Qwen2-72B-Instruct: NeedleBench 128K improves from 73.05 to 90.27 (+17.22); NeedleBench 256K improves from 17.13 to 85.21 (+68.08); LV-Eval 256K improves from 2.88 to 42.35 (+39.47) (Table 12, Section 5.2.3). Qwen2-7B-Instruct surpasses ChatGLM4-9B-1M (which claims 1M context length) on NeedleBench with YARN+DCA (moderate evidence; only two Qwen2 model sizes tested with YARN+DCA).

#### Multilingual Human Evaluation (Table 13)

| Language | GPT-3.5-Turbo | GPT-4-Turbo | GPT-4o | Claude-3-Opus | **Qwen2-72B-Instruct** |
|---|---|---|---|---|---|
| Arabic | 2.52 | 3.44 | 3.55 | 4.15 | 3.86 |
| French | 3.47 | 4.19 | 4.16 | 4.23 | 4.01 |
| Indonesian | 3.56 | 4.09 | 4.39 | 4.40 | 3.83 |
| Japanese | 2.75 | 3.68 | 3.72 | 3.85 | 3.63 |
| Korean | 2.37 | 4.24 | 4.40 | 4.23 | 4.14 |
| Portuguese | 3.37 | 3.86 | 3.89 | 4.09 | 3.97 |
| Russian | 3.24 | 4.27 | 4.32 | 4.25 | 4.15 |
| Spanish | 4.07 | 4.08 | 4.26 | 4.31 | 4.10 |
| Thai | 3.38 | 4.11 | 4.09 | 4.01 | 3.75 |
| Vietnamese | 3.90 | 3.84 | 4.14 | 3.98 | 3.91 |
| **Average** | 3.16 | 3.98 | 4.09 | 4.15 | **3.93** |

- Qwen2-72B-Instruct significantly outperforms GPT-3.5-Turbo (3.93 vs 3.16) and is competitive with GPT-4-Turbo (3.98), but falls behind GPT-4o (4.09) and Claude-3-Opus (4.15) (Table 13, Section 5.2.4). One professional annotator per language, 1-5 scoring scale (limited evidence for individual languages due to single annotator per language).

#### Safety Evaluation (Table 14)

| Risk Category | GPT-4 | Mixtral-8x22B | **Qwen2-72B-Instruct** |
|---|---|---|---|
| Illegal | 0.00 | 6.87 | **0.00** |
| Fraud | 3.40 | 8.49 | **2.41** |
| Pornography | **23.63** | 33.82 | 22.91 |
| Privacy | 3.37 | 15.03 | **2.47** |

*Lower is better (proportion of harmful responses).* Qwen2-72B-Instruct outperforms GPT-4 overall and significantly outperforms Mixtral-8x22B-Instruct. Pornography remains the most difficult category (22.91% harmful rate), described as "conventionally difficult to differentiate even for humans" (Table 14, Section 5.2.5).

#### Contamination Analysis (Table 15)

| Test set | Contamination % | Qwen2-72B-Instruct Original | Qwen2-72B-Instruct Non-Contam. | Delta | Qwen2-7B-Instruct Original | Qwen2-7B-Instruct Non-Contam. | Delta |
|---|---|---|---|---|---|---|---|
| MMLU | 11.2% | 82.3 | 83.2 | +0.9 | 70.5 | 71.3 | +0.8 |
| MMLU-Pro | 11.6% | 64.4 | 65.6 | +1.2 | 44.1 | 46.5 | +2.4 |
| GPQA | 1.0% | 42.4 | 41.8 | -0.6 | 34.3 | 34.1 | -0.2 |
| HumanEval | 75.0% | 86.0 | 87.0 | +1.0 | 79.9 | 87.8 | +7.9 |
| MBPP | 29.6% | 80.2 | 79.7 | -0.5 | 67.2 | 69.0 | +1.8 |
| MultiPL-E | 37.7% | 69.2 | 69.2 | 0.0 | 59.1 | 58.9 | -0.2 |
| GSM8K | 0.7% | 93.2 | 92.8 | -0.4 | 85.7 | 85.6 | -0.1 |
| MATH | 31.7% | 69.0 | 74.6 | +5.6 | 52.9 | 57.6 | +4.7 |
| IFEval | 0.9% | 77.6 | 77.4 | -0.2 | 54.7 | 53.7 | -1.0 |

- Despite high nominal contamination rates (e.g., HumanEval 75.0%, MultiPL-E 37.7%, MATH 31.7%), performance on non-contaminated subsets remains consistent or even improves. The authors note most "contaminated" samples are false positives from common code snippets and mathematical expressions (Table 15, Section 5.2.6). Decontamination uses 13-gram overlap combined with LCS constraint (|LCS| >= 13 and |LCS| >= 0.6 x min(|s_t|, |s_e|)) (Section 5.2.6).

---

## Limitations and Failure Modes

1. **Instruction following at 7B scale:** Qwen2-7B-Instruct scores 54.7 on IFEval strict-prompt, substantially behind Llama-3-8B-Instruct (72.1), a gap of -17.4 points. The authors acknowledge this gap and plan to address it through improved post-training data quality (Table 8, Section 5.2.1).

2. **English performance gap vs Llama-3-70B:** In in-house English evaluation, Qwen2-72B-Instruct falls behind Llama-3-70B-Instruct in comprehension (73.58 vs 76.31) and coding (53.03 vs 57.18). The authors attribute this to the amount of English pre-training tokens and post-training data diversity (Table 11, Section 5.2.2).

3. **MoE knowledge understanding:** Qwen2-57B-A14B-Instruct underperforms Qwen1.5-32B-Chat on knowledge understanding in Chinese in-house evaluation (64.15 vs 68.63), attributed to insufficient pre-training tokens for the MoE model (Table 10, Section 5.2.2).

4. **Data quality vs quantity trade-off:** Expanding from 7T to 12T tokens with relaxed quality thresholds did not improve performance, suggesting diminishing returns from data volume alone. The authors "suspect that increasing the volume of data does not necessarily benefit model pre-training" (Section 3.1).

5. **Safety gaps in pornography detection:** While Qwen2-72B-Instruct outperforms GPT-4 and Mixtral-8x22B on overall safety, the pornography category shows a 22.91% harmful response rate, described as "conventionally difficult to differentiate even for humans" (Table 14, Section 5.2.5).

6. **[Inferred]** Limited training detail disclosure: Specific training infrastructure, pre-training learning rate schedules, optimizer configurations, and total compute costs are not disclosed, limiting reproducibility assessment.

7. **[Inferred]** MoE scalability unvalidated: Only one MoE size (57B-A14B) is presented; the scalability of fine-grained expert design to larger models is not demonstrated.

8. **[Inferred]** NIAH as a limited evaluation: While NIAH results are impressive, the benchmark tests simple factual retrieval rather than multi-hop reasoning or complex long-context understanding. NeedleBench and LV-Eval provide more challenging assessments but are only tested on 72B and 7B models with YARN+DCA.

#### Scope and Comparability

- **What was not tested:** No evaluation on non-English multilingual instruction-tuned benchmarks beyond human evaluation. No evaluation on retrieval-augmented or tool-use tasks. No evaluation of safety in languages other than a combined multilingual assessment. Long-context evaluation with YARN+DCA limited to Qwen2-72B-Instruct and Qwen2-7B-Instruct (Table 12); the 57B MoE and smaller models were not tested with YARN+DCA at extended contexts.
- **Comparability notes:** Few-shot counts vary across benchmarks (e.g., MMLU 5-shot, BBH 3-shot, HellaSwag 10-shot), which is standard but affects cross-paper comparison when other papers use different shot counts. The in-house evaluation benchmarks (Tables 10-11) are proprietary and not reproducible by other groups. Multilingual human evaluation uses a 1-5 scoring scale with a single annotator per language, which may have limited inter-annotator reliability. Contamination analysis uses a strict 13-gram overlap criterion that the authors themselves note produces many false positives in code and math domains, making the "contamination percentage" figure hard to compare with other papers using different contamination definitions.

---

## Conclusions

### Contributions

1. **Comprehensive open-weight model family.** Release of five model sizes (0.5B to 72B) plus a MoE variant, covering deployment from mobile devices to multi-GPU clusters, with permissive licensing (Apache 2.0 for most sizes, Qianwen License for 72B) (Section 1).

2. **Architecture improvements for inference efficiency.** Adoption of GQA across all sizes reduces KV cache memory; the MoE design with fine-grained experts (64 routed, 8 activated, 8 shared) achieves 30B-dense-equivalent performance with 14B activated parameters (Sections 2.2, 5.1.1).

3. **Long-context extension to 128K tokens.** Combination of RoPE base frequency scaling (10K to 1M), YARN, and Dual Chunk Attention enables reliable 128K context for the 72B and 7B models, with 256K processing possible using YARN+DCA. NeedleBench 256K improves from 17.13 to 85.21 for 72B (Sections 3.2, 5.2.3).

4. **Data scaling to 7T tokens with quality focus.** Demonstrated that quality-filtered 7T tokens outperforms quality-relaxed 12T tokens, establishing that data quality dominates volume at this scale (Section 3.1).

5. **Competitive multilingual capabilities.** Proficiency across approximately 30 languages, with human evaluation scores competitive with GPT-4-Turbo across 10 languages (3.93 vs 3.98 average) (Sections 5.1.1, 5.2.4).

6. **Scalable post-training methodology.** Combination of collaborative human annotation and automated data synthesis (rejection sampling, execution feedback, data repurposing, constitutional feedback) with a two-stage offline+online DPO pipeline enables high-quality alignment with minimal human annotation (Section 4).

### Implications

1. **Data quality over quantity at scale.** The finding that 12T tokens with relaxed filtering does not outperform 7T tokens with strict filtering suggests that current data scaling approaches may be hitting quality bottlenecks (speculative: this may motivate synthetic data approaches for future scaling).

2. **Fine-grained MoE as a scaling paradigm.** The success of smaller, more numerous experts with more activated simultaneously (64 routed, 8 active vs Mixtral's 8 routed, 2 active) suggests this design may offer better parameter efficiency than coarse-grained MoE approaches. However, this is demonstrated at only one scale, so the generality is uncertain.

3. **GQA as a universal architectural choice.** The adoption of GQA across all model sizes, including 0.5B, suggests that GQA's KV cache savings outweigh any potential quality trade-off even at small scales (speculative: requires controlled ablation to confirm).

4. **Data scaling effectiveness for sub-billion models.** Training Qwen2-0.5B on 12T tokens (far exceeding Chinchilla-optimal) yields competitive performance with models 4-5x larger, suggesting over-training small models may be an effective strategy for deployment-constrained settings.

---

## Key Claims

1. **C1:** Qwen2-72B achieves 84.2 on MMLU, outperforming Llama-3-70B (79.5) by +4.7 points and Qwen1.5-110B (80.4) by +3.8 points (Table 2, Section 5.1.1). Tested across 21 benchmarks against 4 baselines at 70B+ scale (strong evidence). Status: **supported**. Scope: 72B scale, 5-shot evaluation, English benchmarks. Magnitude: 84.2 MMLU (vs 79.5 Llama-3-70B).

2. **C2:** Enriched code and math pre-training data yields Qwen2-72B gains of +18.3 on HumanEval (64.6 vs 46.3) and +10.0 on GSM8K (89.5 vs 79.5) over Qwen1.5-72B (Table 2, Section 5.1.1). Attribution is inferred from data composition changes, not controlled ablation (moderate evidence). Status: **supported**. Scope: 72B scale, 0-shot HumanEval, 5-shot GSM8K. Magnitude: +18.3 HumanEval, +10.0 GSM8K, +17.0 MATH.

3. **C3:** Qwen2-57B-A14B, with 14B activated parameters, matches 30B dense models on most benchmarks. It is competitive with Yi-1.5-34B in NLU (MMLU 76.5 vs 77.1) and outperforms baselines in coding (HumanEval 53.0) and math (MATH 43.0) (Table 3, Section 5.1.1). Only one MoE size tested, limiting generalizability claims (limited evidence for MoE scaling). Status: **supported**. Scope: 57B total / 14B activated MoE, compared against 30B+ dense baselines. Magnitude: MMLU 76.5 vs Yi-1.5-34B 77.1, HumanEval 53.0 vs 46.3, MATH 43.0 vs 41.7.

4. **C4:** YARN + DCA enable Qwen2-72B-Instruct and Qwen2-7B-Instruct to handle 128K tokens on NIAH with near-perfect accuracy. YARN+DCA improve NeedleBench at 256K from 17.13 to 85.21 for the 72B model (Figure 1, Table 12, Section 5.2.3). Tested on 2 model sizes with YARN+DCA (moderate evidence). Status: **supported**. Scope: 72B and 7B instruct models, NIAH retrieval, 8K-128K context. Magnitude: NeedleBench 256K: 17.13 to 85.21 (+68.08) for 72B.

5. **C5:** Qwen2-72B-Instruct scores 3.93 average on multilingual human evaluation across 10 languages, competitive with GPT-4-Turbo (3.98) and behind Claude-3-Opus (4.15) (Table 13, Section 5.2.4). Single annotator per language, 1-5 scale (limited evidence for individual language assessments). Status: **supported**. Scope: 72B instruct model, 10 languages, 1-5 human scoring. Magnitude: 3.93 average (vs GPT-4-Turbo 3.98, GPT-4o 4.09, Claude-3-Opus 4.15).

6. **C6:** Expanding pre-training data from 3T to 7T tokens with quality filtering improves performance, but relaxing quality to 12T tokens does not yield significant gains. The authors "suspect that increasing the volume of data does not necessarily benefit model pre-training" (Section 3.1). No specific numerical comparison between 7T and 12T models is provided (limited evidence; qualitative claim without reported metrics). Status: **supported**. Scope: Dense models, data quality threshold comparison between 7T and 12T token datasets. Magnitude: qualitative (no specific numbers reported).

7. **C7:** Data scaling is effective for sub-billion parameter models. Qwen2-0.5B (0.3B non-embedding parameters, 12T tokens) and Qwen2-1.5B achieve competitive performance with larger models (Table 5, Table 9, Section 5.1.1). Tested against Phi-2, Gemma-2B, and Qwen1.5 baselines across 14 benchmarks (moderate evidence). Status: **supported**. Scope: 0.5B and 1.5B parameter models, 12T tokens for 0.5B. Magnitude: Qwen2-1.5B MMLU 56.5 (vs Qwen1.5-1.8B 46.8), GSM8K 58.5 (vs 38.4).

8. **C8:** Contamination analysis using strict 13-gram overlap criterion shows that performance on non-contaminated test sets is consistent with original sets (e.g., Qwen2-72B-Instruct MMLU: 82.3 to 83.2, GSM8K: 93.2 to 92.8), indicating no significant contamination benefit (Table 15, Section 5.2.6). Tested on 2 model sizes across 9 benchmarks (moderate evidence). Status: **supported**. Scope: Qwen2-72B-Instruct and Qwen2-7B-Instruct, strict 13-gram overlap criterion. Magnitude: Deltas range from -1.0 to +5.6, with most <1 point; despite up to 75% nominal contamination rate on HumanEval.

---

## Open Questions

1. **Data quality ceiling.** The 7T vs 12T finding raises the question of whether better data curation methods (e.g., model-based quality scoring, deduplication at scale) could unlock gains from larger corpora, or whether 7T tokens represents a fundamental saturation point for current data sources. Not addressed by subsequent work in this repository.

2. **MoE scaling.** Only a single MoE size is demonstrated. Whether the fine-grained expert approach maintains its advantages at 100B+ total parameters, and how expert routing evolves with scale, remains unexplored. Addressed by Qwen3 (2025-05-qwen3-technical-report), which scales MoE to 235B-A22B.

3. **IFEval gap at 7B.** Qwen2-7B-Instruct's weak instruction following (IFEval 54.7 vs Llama-3-8B-Instruct at 72.1) is a significant gap that the authors plan to address through post-training data improvements. Not addressed by subsequent work in this repository.

4. **Optimal data mix.** The paper mentions experiments on scaled-down models to optimize data mixing (Section 3.1), but provides no details on the methodology or resulting distribution. How the optimal mix varies across model scales is an open question. Not addressed by subsequent work in this repository.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundation architecture. Qwen2 builds on the decoder-only Transformer with causal attention.
- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models.* Qwen2 adopts GQA across all model sizes to reduce KV cache memory during inference.
- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Qwen2 uses RoPE for positional encoding with base frequency scaled from 10,000 to 1,000,000 for long-context training.
- **Dauphin et al. (2017)** -- *Language Modeling with Gated Convolutional Networks.* SwiGLU activation used in Qwen2.

### Context Extension

- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Qwen2 employs YARN to rescale attention weights for length extrapolation beyond 32K tokens.
- **An et al. (2024)** -- *Training-Free Long-Context Scaling of Large Language Models.* Dual Chunk Attention segments long sequences into chunks, enabling 131K-token processing.
- **Xiong et al. (2023)** -- *Effective Long-Context Scaling of Foundation Models.* RoPE base frequency scaling strategy adopted by Qwen2.

### Mixture-of-Experts

- **Dai et al. (2024)** -- *DeepSeekMoE: Towards Ultimate Expert Specialization.* Qwen2 MoE adopts fine-grained expert design and shared/routing-specific expert architecture.
- **Komatsuzaki et al. (2023)** -- *Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints.* Qwen2 MoE initialization based on upcycling from the dense Qwen2-7B model.
- **Jiang et al. (2024)** -- *Mixtral of Experts.* Coarse-grained MoE baseline; Qwen2 MoE differs by using smaller, more numerous experts (64 routed, 8 active vs 8 routed, 2 active).

### Post-Training

- **Rafailov et al. (2023)** -- *Direct Preference Optimization.* DPO used for both offline and online RLHF stages.
- **Lu et al. (2024a)** -- *Online Merging Optimizers for Boosting Rewards and Mitigating Tax.* Used to mitigate alignment tax during online RLHF.
- **Bai et al. (2022)** -- *Constitutional AI.* Constitutional feedback approach for safety data synthesis.

### Competing Models

- **Touvron et al. (2023)** -- *LLaMA: Open and Efficient Foundation Language Models.* Predecessor open-weight models that catalyzed the open LLM ecosystem.
- **AI@Meta (2024)** -- *Llama 3 Model Card.* Primary open-weight baseline; Llama-3-70B and Llama-3-8B are the main comparison models.
- **Jiang et al. (2023a)** -- *Mistral 7B.* 7B-class baseline model.
- **Mesnard et al. (2024)** -- *Gemma: Open Models Based on Gemini Research.* Small-model baseline (Gemma-2B, Gemma-7B).

### Predecessor

- **Bai et al. (2023a)** -- *Qwen Technical Report.* Direct predecessor. Qwen2 extends with 7T tokens (vs 3T), GQA, extended context, and MoE variant.

### Evaluation Benchmarks

- **Kamradt (2023)** -- *Needle in a Haystack.* Primary long-context retrieval evaluation up to 128K tokens.
- **Hendrycks et al. (2021a)** -- *Measuring Massive Multitask Language Understanding.* MMLU is the primary knowledge understanding benchmark.
- **Chen et al. (2021)** -- *Evaluating Large Language Models Trained on Code.* HumanEval coding benchmark.
- **Cobbe et al. (2021)** -- *Training Verifiers to Solve Math Word Problems.* GSM8K math benchmark.
- **Zheng et al. (2023)** -- *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* MT-Bench for instruction-tuned model evaluation.
- **OpenCompass Contributors (2023)** -- *OpenCompass.* NeedleBench multi-needle retrieval and reasoning evaluation.
- **Yuan et al. (2024)** -- *LV-Eval.* Long-context QA benchmark with balanced length levels up to 256K.
