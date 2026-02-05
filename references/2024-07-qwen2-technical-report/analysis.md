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
  - id: C2
    claim: "Enriched code and math data yields +18.3 on HumanEval (64.6 vs 46.3) and +10.0 on GSM8K (89.5 vs 79.5) over Qwen1.5-72B"
    evidence: "Table 2, Section 5.1.1"
    status: supported
  - id: C3
    claim: "Qwen2-57B-A14B (MoE, 14B active) matches 30B dense model performance while activating only 14B parameters per forward pass"
    evidence: "Table 3, Section 5.1.1"
    status: supported
  - id: C4
    claim: "YARN + DCA enables 128K context with near-perfect NIAH accuracy for Qwen2-72B-Instruct and Qwen2-7B-Instruct"
    evidence: "Figure 1, Table 12, Section 5.2.3"
    status: supported
  - id: C5
    claim: "Qwen2-72B-Instruct achieves multilingual human evaluation scores competitive with GPT-4-Turbo (3.93 vs 3.98 average) across 10 languages"
    evidence: "Table 13, Section 5.2.4"
    status: supported
  - id: C6
    claim: "Expanding pre-training data from 3T to 7T tokens improves performance, but further relaxation to 12T tokens with lower quality does not yield significant gains"
    evidence: "Section 3.1"
    status: supported
  - id: C7
    claim: "Data scaling remains effective for sub-billion parameter models: Qwen2-0.5B and Qwen2-1.5B significantly outperform Qwen1.5 counterparts"
    evidence: "Table 5, Table 9, Section 5.1.1"
    status: supported
  - id: C8
    claim: "Contamination analysis shows no significant performance degradation between original and non-contaminated test sets despite high nominal contamination rates on some benchmarks"
    evidence: "Table 15, Section 5.2.6"
    status: supported
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

Open-weight large language models have rapidly narrowed the gap with proprietary models, but significant challenges remain in building competitive model families that span a wide range of sizes (from sub-billion to 70B+ parameters), support strong multilingual capabilities across dozens of languages, and handle long contexts reliably. Prior open-weight models such as Llama 2 (Touvron et al., 2023), Llama 3 (AI@Meta, 2024), and Mistral 7B (Jiang et al., 2023a) have advanced the state of the art, but gaps persist in coding, mathematics, and multilingual performance relative to proprietary models like GPT-4o and Claude-3 Opus.

The predecessor Qwen1.5 (Qwen Team, 2024a) was trained on 3 trillion tokens and demonstrated competitive performance but had limited multilingual coverage, a 4,096-token context window, and used conventional multi-head attention with associated KV cache overhead.

**The core challenge: how to build a comprehensive open-weight model family that achieves competitive performance with proprietary models across language understanding, coding, mathematics, reasoning, and multilingual tasks, while supporting efficient inference and long-context processing up to 128K tokens.**

---

## Problem Solutions

The Qwen2 series addresses these challenges through a combination of architectural improvements, data scaling, and improved post-training:

1. **Grouped Query Attention (GQA)** replaces multi-head attention across all model sizes, reducing KV cache memory and improving inference throughput.
2. **Dual Chunk Attention (DCA) with YARN** enables context extension from 32K to 131,072 tokens without significant performance degradation.
3. **Pre-training data scaling** from 3T to 7T tokens with enhanced quality filtering and expanded coverage of code, mathematics, and ~30 languages.
4. **Mixture-of-Experts (MoE) variant** using fine-grained experts and shared/routing-specific expert design achieves dense-model performance with fewer activated parameters.
5. **Scalable post-training** with collaborative annotation, automated data synthesis (rejection sampling, execution feedback, data repurposing, constitutional feedback), and a two-stage RLHF pipeline (offline DPO + online DPO with reward models).

---

## Approach Details

### Method

#### Dense Model Architecture

Qwen2 dense models are decoder-only Transformers with causal attention. Key architectural choices:

- **Grouped Query Attention (GQA):** All sizes use GQA (Ainslie et al., 2023) instead of conventional MHA. KV head counts range from 2 (0.5B, 1.5B) to 8 (72B), significantly reducing KV cache memory.
- **Dual Chunk Attention (DCA):** Segments long sequences into manageable chunks (An et al., 2024). For inputs within a single chunk, DCA produces identical results to standard attention. For longer inputs, it captures relative positional information within and across chunks.
- **YARN:** Rescales attention weights for length extrapolation (Peng et al., 2023).
- **Other components:** SwiGLU activation (Dauphin et al., 2017), RoPE positional embeddings (Su et al., 2024), QKV bias (Su, 2023), RMSNorm (Jiang et al., 2023b), pre-normalization.

| Configuration | 0.5B | 1.5B | 7B | 72B | 57B-A14B |
|---|---|---|---|---|---|
| Hidden Size | 896 | 1,536 | 3,584 | 8,192 | 3,584 |
| # Layers | 24 | 28 | 28 | 80 | 28 |
| # Query Heads | 14 | 12 | 28 | 64 | 28 |
| # KV Heads | 2 | 2 | 4 | 8 | 4 |
| Head Size | 64 | 128 | 128 | 128 | 128 |
| Intermediate Size | 4,864 | 8,960 | 18,944 | 29,568 | 2,560 |
| # Trained Tokens | 12T | 7T | 7T | 7T | 4.5T |
| Embedding Tying | True | True | False | False | False |
| Vocabulary Size | 151,646 | 151,646 | 151,646 | 151,646 | 151,646 |

#### MoE Architecture

Qwen2-57B-A14B uses a Mixture-of-Experts architecture with fine-grained experts. The MoE FFN replaces the dense FFN:

> **p** = softmax(G(**x**)),
> **y** = Σ_{i ∈ topk(**p**)} **p**_i E_i(**x**).

Key MoE design choices:

- **Fine-grained experts:** Rather than using full-sized FFN experts (as in Mixtral's transition from Mistral-7B to 8x7B), Qwen2 MoE uses smaller experts with more activated simultaneously. This provides a richer set of expert combinations. Configuration: 64 routed experts, 8 activated per token, 8 shared experts, each with intermediate size 2,560.
- **Shared and routing-specific experts:** Shared experts handle common patterns across tasks; routing-specific experts specialize.
- **Expert initialization via upcycling:** Initializes from a dense model (Qwen2-7B). The FFN is replicated ⌈n×h_E/h_FFN⌉ times, parameters are shuffled along the intermediate dimension for diversity, fine-grained experts are extracted, and 50% of each expert's parameters are randomly reinitialized.

---

### Key Technical Components

#### Tokenizer

Byte-level byte-pair encoding tokenizer identical to Qwen (Bai et al., 2023a). Vocabulary of 151,643 regular tokens + 3 control tokens, shared across all model sizes. High compression rate facilitates multilingual capabilities.

#### Pre-training Data

The pre-training corpus expanded from 3T tokens (Qwen1.5) to **7T tokens** for all dense models except Qwen2-0.5B (12T tokens):

- **Quality enhancement:** Refined filtering with heuristic and model-based methods, including using Qwen models to filter low-quality data and synthesize high-quality pre-training data.
- **Data expansion:** Significantly more code, mathematics, and multilingual data covering ~30 languages (English, Chinese, Spanish, French, German, Arabic, Russian, Korean, Japanese, Thai, Vietnamese, etc.).
- **Distribution improvement:** Scaled-down model experiments to optimize data mixing across sources and domains.
- **12T experiment:** Relaxing quality thresholds to create a 12T token dataset did not significantly improve over 7T, suggesting data quality matters more than volume at this scale.
- **Multi-task instruction data:** Integrated into pre-training to enhance in-context learning and instruction-following.

#### Long-Context Training

Context length extended from 4,096 to **32,768 tokens** during the final pre-training phase:

- RoPE base frequency changed from 10,000 to **1,000,000** (following Xiong et al., 2023).
- Complemented by increased volume of high-quality long-form data.
- YARN + DCA enable processing up to **131,072 tokens** with minimal perplexity degradation.

#### Post-Training Pipeline

**Supervised Fine-Tuning (SFT):**
- 500,000+ instruction examples covering instruction following, coding, mathematics, logical reasoning, role-playing, multilingualism, and safety.
- 2 epochs, sequence length 32,768, learning rate 7×10⁻⁶ → 7×10⁻⁷, weight decay 0.1, gradient clipping at 1.0.

**RLHF (two stages):**
1. **Offline DPO:** Pre-compiled preference dataset P, maximizing likelihood difference between preferred and dispreferred responses.
2. **Online DPO:** Current policy model generates multiple responses; reward model selects best and worst to form preference pairs for iterative DPO.
- **Online Merging Optimizer** (Lu et al., 2024a) mitigates the alignment tax.

**Post-training data construction:**
- **Collaborative annotation:** InsTag ontology extraction → instruction selection → instruction evolution → human ranking.
- **Automated synthesis:** Rejection sampling (math), execution feedback (code), data repurposing (literary writing), constitutional feedback (safety).

---

### Experimental Setup

**Base model evaluation:** Few-shot prompting on standard benchmarks. MMLU (5-shot), MMLU-Pro (5-shot), GPQA (5-shot), TheoremQA (5-shot), BBH (3-shot), HellaSwag (10-shot), Winogrande (5-shot), TruthfulQA (0-shot), ARC-C (25-shot), HumanEval (0-shot), MBPP (0-shot), EvalPlus (0-shot), MultiPL-E (0-shot), GSM8K (5-shot), MATH (4-shot), C-Eval (5-shot), CMMLU (5-shot).

**Multilingual evaluation:** M3Exam (5-shot), IndoMMLU (3-shot), ruMMLU (5-shot), translated MMLU (5-shot), BELEBELE (5-shot), XCOPA (5-shot), XWinograd (5-shot), XStoryCloze (0-shot), PAWS-X (5-shot), MGSM (8-shot CoT), Flores-101 (5-shot).

**Instruction-tuned evaluation:** MMLU, MMLU-Pro, GPQA, TheoremQA, HumanEval, MBPP, MultiPL-E, LiveCodeBench v1, GSM8K, MATH, MT-Bench, Arena-Hard, AlignBench, MixEval, IFEval (strict-prompt).

**Long context:** Needle in a Haystack (8K–128K), NeedleBench (8K–256K), LV-Eval (16K–256K). YARN applied for contexts >32K tokens.

**Baselines:** Llama-3-70B, Llama-3-8B, Mixtral-8x22B, Mixtral-8x7B, Mistral-7B, Gemma-7B, Yi-1.5-34B, Phi-2, Gemma-2B, Qwen1.5 series, GPT-4, GPT-4o, GPT-3.5-Turbo, Claude-3-Opus.

---

### Key Results

#### Base Model: Qwen2-72B vs 70B+ Baselines

| Benchmark | Mixtral-8x22B | Llama-3-70B | Qwen1.5-72B | Qwen1.5-110B | **Qwen2-72B** |
|---|---|---|---|---|---|
| MMLU | 77.8 | 79.5 | 77.5 | 80.4 | **84.2** |
| MMLU-Pro | 49.5 | 52.8 | 45.8 | 49.4 | **55.6** |
| GPQA | 34.3 | 36.3 | 36.3 | 35.9 | **37.9** |
| TheoremQA | 35.9 | 32.3 | 29.3 | 34.9 | **43.1** |
| BBH | 78.9 | 81.0 | 65.5 | 74.8 | **82.4** |
| HumanEval | 46.3 | 48.2 | 46.3 | 54.3 | **64.6** |
| MBPP | 71.7 | 70.4 | 66.9 | 70.9 | **76.9** |
| GSM8K | 83.7 | 83.0 | 79.5 | 85.4 | **89.5** |
| MATH | 41.7 | 42.5 | 34.1 | 49.6 | **51.1** |
| C-Eval | 54.6 | 65.2 | 84.1 | 89.1 | **91.0** |
| CMMLU | 53.4 | 67.2 | 83.5 | 88.3 | **90.1** |

- Qwen2-72B leads on all benchmarks except HellaSwag (Mixtral-8x22B: 88.7 vs 87.6), Winogrande (Llama-3-70B: 85.3 vs 85.1), ARC-C (Mixtral-8x22B: 70.7 vs 68.9), and TruthfulQA (Qwen1.5-72B: 59.6 vs 54.8) (Table 2, Section 5.1.1).
- The largest gains over Qwen1.5-72B are in coding (+18.3 HumanEval, +10.0 MBPP) and mathematics (+10.0 GSM8K, +17.0 MATH).

#### Base Model: Qwen2-7B vs 7B+ Baselines

| Benchmark | Mistral-7B | Gemma-7B | Llama-3-8B | Qwen1.5-7B | **Qwen2-7B** |
|---|---|---|---|---|---|
| MMLU | 64.2 | 64.6 | 66.6 | 61.0 | **70.3** |
| MMLU-Pro | 30.9 | 33.7 | 35.4 | 29.9 | **40.0** |
| HumanEval | 29.3 | 37.2 | 33.5 | 36.0 | **51.2** |
| GSM8K | 52.2 | 46.4 | 56.0 | 62.5 | **79.9** |
| MATH | 13.1 | 24.3 | 20.5 | 20.3 | **44.2** |

- Qwen2-7B outperforms all 7B baselines on most benchmarks, with especially large margins in coding and math (Table 4, Section 5.1.1).

#### Instruction-Tuned: Qwen2-72B-Instruct

| Benchmark | Mixtral-8x22B | Llama-3-70B | Qwen1.5-72B | Qwen1.5-110B | **Qwen2-72B** |
|---|---|---|---|---|---|
| MMLU | 74.0 | 82.0 | 75.6 | 76.5 | **82.3** |
| MMLU-Pro | 56.1 | 56.2 | 51.7 | 50.5 | **64.4** |
| HumanEval | 73.8 | 81.7 | 71.3 | 74.4 | **86.0** |
| GSM8K | 89.1 | 93.0 | 82.7 | 84.5 | **93.2** |
| MATH | 47.4 | 50.4 | 42.5 | 42.0 | **69.0** |
| MT-Bench | 8.66 | 8.95 | 8.61 | 8.88 | **9.12** |
| Arena-Hard | 36.4 | 41.1 | 36.1 | 39.8 | **48.1** |
| LiveCodeBench | 21.8 | 29.3 | 17.9 | 25.3 | **35.7** |
| IFEval | 67.1 | 77.3 | 55.8 | 57.5 | **77.6** |
| AlignBench | - | 7.42 | 7.28 | 7.87 | **8.27** |

- Qwen2-72B-Instruct leads on all metrics except GPQA (Mixtral-8x22B: 49.7 vs 42.4) and MBPP (Llama-3-70B: 82.3 vs 80.2) (Table 6, Section 5.2.1).

#### Long Context Evaluation

- **NIAH (Figure 1):** Qwen2-72B-Instruct achieves near-perfect accuracy across the full 128K context. Qwen2-7B-Instruct also handles 128K tokens at high accuracy. Qwen2-57B-A14B-Instruct supports up to 64K, smaller models up to 32K.
- **NeedleBench + LV-Eval with YARN+DCA (Table 12):**

| Model | NeedleBench 128K | NeedleBench 256K | LV-Eval 128K | LV-Eval 256K |
|---|---|---|---|---|
| Qwen2-7B-Instruct | 38.77 | 2.92 | 11.01 | 0.55 |
| + YARN + DCA | 66.32 | 60.71 | 36.64 | 34.72 |
| Qwen2-72B-Instruct | 73.05 | 17.13 | 31.79 | 2.88 |
| + YARN + DCA | 90.27 | 85.21 | 48.83 | 42.35 |

- YARN + DCA integration dramatically improves ultra-long context performance, with Qwen2-72B-Instruct achieving 90.27 on NeedleBench at 128K (vs 73.05 without) and 85.21 at 256K (vs 17.13 without).

#### Multilingual Human Evaluation (Table 13)

| Model | Average (10 languages) |
|---|---|
| GPT-3.5-Turbo | 3.16 |
| GPT-4-Turbo | 3.98 |
| GPT-4o | 4.09 |
| Claude-3-Opus | 4.15 |
| **Qwen2-72B-Instruct** | **3.93** |

- Competitive with GPT-4-Turbo, slightly behind Claude-3-Opus.

---

## Limitations and Failure Modes

1. **Instruction following at 7B scale:** Qwen2-7B-Instruct scores 54.7 on IFEval strict-prompt, substantially behind Llama-3-8B-Instruct (72.1). The authors acknowledge this gap and plan to address it through improved post-training data quality (Section 5.2.1).

2. **English performance gap vs Llama-3-70B:** In in-house English evaluation, Qwen2-72B-Instruct falls slightly behind Llama-3-70B-Instruct in comprehension (73.58 vs 76.31) and coding (53.03 vs 57.18). The authors attribute this to the amount of English pre-training tokens and post-training data diversity (Section 5.2.2).

3. **MoE knowledge understanding:** Qwen2-57B-A14B-Instruct underperforms Qwen1.5-32B-Chat on knowledge understanding in Chinese in-house evaluation, attributed to insufficient pre-training tokens for the MoE model (Section 5.2.2).

4. **Data quality vs quantity trade-off:** Expanding from 7T to 12T tokens with relaxed quality thresholds did not improve performance, suggesting diminishing returns from data volume alone (Section 3.1).

5. **Safety gaps in pornography detection:** While Qwen2-72B-Instruct outperforms GPT-4 and Mixtral-8x22B on overall safety, the pornography category remains difficult (22.91% harmful response rate), described as "conventionally difficult to differentiate even for humans" (Table 14, Section 5.2.5).

6. **Limited training detail disclosure:** Specific training infrastructure, learning rates for pre-training, optimizer configurations, and total compute costs are not disclosed.

7. **MoE scalability unvalidated:** Only one MoE size (57B-A14B) is presented; the scalability of fine-grained expert design to larger models is not demonstrated.

---

## Conclusions

### Contributions

1. **Comprehensive open-weight model family.** Release of five model sizes (0.5B to 72B) plus a MoE variant, covering deployment from mobile devices to multi-GPU clusters, with permissive licensing.

2. **Architecture improvements for inference efficiency.** Adoption of GQA across all sizes reduces KV cache memory; the MoE design with fine-grained experts achieves 30B-dense-equivalent performance with 14B activated parameters.

3. **Long-context extension to 128K tokens.** Combination of RoPE base frequency scaling (10K → 1M), YARN, and Dual Chunk Attention enables reliable 128K context for the 72B and 7B models, with 256K processing possible using YARN+DCA.

4. **Data scaling to 7T tokens with quality focus.** Demonstrated that quality-filtered 7T tokens outperforms quality-relaxed 12T tokens, establishing that data quality dominates volume at this scale.

5. **Competitive multilingual capabilities.** Proficiency across ~30 languages, with human evaluation scores competitive with GPT-4-Turbo across 10 languages.

6. **Scalable post-training methodology.** Combination of collaborative human annotation and automated data synthesis (rejection sampling, execution feedback, data repurposing, constitutional feedback) enables high-quality alignment with minimal human annotation.

### Implications

1. **Data quality over quantity at scale.** The finding that 12T tokens with relaxed filtering does not outperform 7T tokens with strict filtering suggests that current data scaling approaches may be hitting quality bottlenecks (speculative: this may motivate synthetic data approaches for future scaling).

2. **Fine-grained MoE as a scaling paradigm.** The success of smaller, more numerous experts with more activated simultaneously suggests this design may offer better parameter efficiency than coarse-grained MoE approaches like Mixtral's 8x7B design.

3. **GQA as a universal architectural choice.** The adoption of GQA across all model sizes, including 0.5B, suggests that GQA's KV cache savings outweigh any potential quality trade-off even at small scales.

---

## Key Claims

1. **C1:** Qwen2-72B achieves 84.2 on MMLU, outperforming Llama-3-70B (79.5) by +4.7 points and Qwen1.5-110B (80.4) by +3.8 points (Table 2, Section 5.1.1). Status: **supported**.

2. **C2:** Enriched code and math pre-training data yields Qwen2-72B gains of +18.3 on HumanEval (64.6 vs 46.3) and +10.0 on GSM8K (89.5 vs 79.5) over Qwen1.5-72B (Table 2, Section 5.1.1). Status: **supported**.

3. **C3:** Qwen2-57B-A14B, with 14B activated parameters, matches 30B dense models on most benchmarks. It is competitive with Yi-1.5-34B in NLU and outperforms baselines in coding and math (Table 3, Section 5.1.1). Status: **supported**.

4. **C4:** YARN + DCA enable Qwen2-72B-Instruct and Qwen2-7B-Instruct to handle 128K tokens on NIAH with near-perfect accuracy. YARN+DCA improve NeedleBench at 256K from 17.13 to 85.21 for the 72B model (Figure 1, Table 12, Section 5.2.3). Status: **supported**.

5. **C5:** Qwen2-72B-Instruct scores 3.93 average on multilingual human evaluation across 10 languages, competitive with GPT-4-Turbo (3.98) and behind Claude-3-Opus (4.15) (Table 13, Section 5.2.4). Status: **supported**.

6. **C6:** Expanding pre-training data from 3T to 7T tokens with quality filtering improves performance, but relaxing quality to 12T tokens does not yield significant gains. The authors "suspect that increasing the volume of data does not necessarily benefit model pre-training" (Section 3.1). Status: **supported** (by authors' own observation, though limited detail on the 12T experiment).

7. **C7:** Data scaling is effective for sub-billion parameter models. Qwen2-0.5B (0.3B non-embedding parameters, 12T tokens) and Qwen2-1.5B achieve competitive performance with larger models like Gemma-2B and Phi-2 (Table 5, Table 9, Section 5.1.1). Status: **supported**.

8. **C8:** Contamination analysis using strict 13-gram overlap criterion shows that performance on non-contaminated test sets is consistent with original sets (e.g., Qwen2-72B-Instruct MMLU: 82.3 → 83.2, GSM8K: 93.2 → 92.8), indicating no significant contamination benefit (Table 15, Section 5.2.6). Status: **supported**.

---

## Open Questions

1. **Data quality ceiling.** The 7T vs 12T finding raises the question of whether better data curation methods (e.g., model-based quality scoring, deduplication at scale) could unlock gains from larger corpora, or whether 7T tokens represents a fundamental saturation point for current data sources. Not addressed by subsequent work in this repository.

2. **MoE scaling.** Only a single MoE size is demonstrated. Whether the fine-grained expert approach maintains its advantages at 100B+ total parameters, and how expert routing evolves with scale, remains unexplored. Not addressed.

3. **IFEval gap at 7B.** Qwen2-7B-Instruct's weak instruction following (IFEval 54.7 vs Llama-3-8B at 72.1) is a significant gap that the authors plan to address through post-training data improvements. Not addressed.

4. **Optimal data mix.** The paper mentions experiments on scaled-down models to optimize data mixing, but provides no details on the methodology or resulting distribution. How the optimal mix varies across model scales is an open question. Not addressed.

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
- **Jiang et al. (2024)** -- *Mixtral of Experts.* Coarse-grained MoE baseline; Qwen2 MoE differs by using smaller, more numerous experts.

### Post-Training

- **Rafailov et al. (2023)** -- *Direct Preference Optimization.* DPO used for both offline and online RLHF stages.
- **Lu et al. (2024a)** -- *Online Merging Optimizers for Boosting Rewards and Mitigating Tax.* Used to mitigate alignment tax during online RLHF.
- **Bai et al. (2022)** -- *Constitutional AI.* Constitutional feedback approach for safety data synthesis.

### Competing Models

- **Touvron et al. (2023)** -- *LLaMA: Open and Efficient Foundation Language Models.* Predecessor open-weight models that catalyzed the open LLM ecosystem.
- **AI@Meta (2024)** -- *Llama 3 Model Card.* Primary open-weight baseline; Llama-3-70B and Llama-3-8B are the main comparison models.
- **Jiang et al. (2023a)** -- *Mistral 7B.* 7B-class baseline model.
- **Mesnard et al. (2024)** -- *Gemma: Open Models Based on Gemini Research.* Small-model baseline.

### Evaluation Benchmarks

- **Kamradt (2023)** -- *Needle in a Haystack.* Primary long-context retrieval evaluation up to 128K tokens.
- **Hendrycks et al. (2021a)** -- *Measuring Massive Multitask Language Understanding.* MMLU is the primary knowledge understanding benchmark.
- **Chen et al. (2021)** -- *Evaluating Large Language Models Trained on Code.* HumanEval coding benchmark.
- **Cobbe et al. (2021)** -- *Training Verifiers to Solve Math Word Problems.* GSM8K math benchmark.
- **Zheng et al. (2023)** -- *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.* MT-Bench for instruction-tuned model evaluation.
