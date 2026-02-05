---
title: "Gemma 2: Improving Open Language Models at a Practical Size"
authors: "Gemma Team"
year: 2024
venue: "arXiv preprint 2408.00118"
paper_type: preprint
categories: ["model-release", "architecture", "attention-efficiency"]
scope: ["open foundation models", "knowledge distillation", "efficient attention", "grouped-query attention", "sliding window attention"]
benchmarks_used: ["mmlu", "gsm8k", "arc", "hellaswag", "winogrande", "humaneval", "mbpp", "bbh", "math-hendrycks", "triviaqa", "natural-questions", "mt-bench", "truthfulqa"]
models_introduced: ["gemma-2-2b", "gemma-2-9b", "gemma-2-27b"]
models_evaluated: ["llama-3-8b", "llama-3-70b", "mistral-7b", "gemma-7b", "qwen1.5-32b"]
key_claims:
  - id: C1
    claim: "Knowledge distillation improves small model performance: a 2B model trained with distillation achieves 67.7 average (vs 60.3 from scratch) on 3 benchmarks"
    evidence: "Table 6, Section 5"
    status: supported
    scope: "2B model, 500B tokens, 7B teacher"
    magnitude: "+7.4 points average improvement"
  - id: C2
    claim: "Gemma 2 27B outperforms Qwen1.5 32B on all reported benchmarks while being smaller"
    evidence: "Table 12, Section 6.1"
    status: supported
    scope: "HuggingFace evaluation suite benchmarks"
  - id: C3
    claim: "Gemma 2 27B is competitive with LLaMA-3 70B despite being 2.5x smaller and trained on 2/3 less data"
    evidence: "Table 12, Section 6.1"
    status: supported
    scope: "MMLU, GSM8K, ARC-c, HellaSwag, Winogrande"
    magnitude: "Within 4-5% on most benchmarks"
  - id: C4
    claim: "Gemma 2 9B achieves Elo 1187 on LMSYS Chatbot Arena, similar to GPT-4-0314 (Elo 1186)"
    evidence: "Table 14, Section 6.2"
    status: supported
    scope: "LMSYS Chatbot Arena blind human evaluations"
  - id: C5
    claim: "GQA with num_groups=2 maintains downstream performance while increasing inference speed"
    evidence: "Table 8, Section 5"
    status: supported
    scope: "9B model, 4 benchmarks"
  - id: C6
    claim: "Deeper networks are slightly better than wider networks for the same parameter count"
    evidence: "Table 9, Section 5"
    status: supported
    scope: "9B model comparison"
    magnitude: "+1.2 points average on 4 benchmarks"
  - id: C7
    claim: "Gemma 2 memorizes significantly less than prior models, with memorization rates below 0.1%"
    evidence: "Figure 1, Section 7"
    status: supported
    scope: "50-token continuation, exact match criterion"
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
---

# Gemma 2: Improving Open Language Models at a Practical Size

**Authors:** Gemma Team (Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy Hardin, et al., Google DeepMind)
**Date:** August 2024, arXiv:2408.00118

---

## Core Research Problem

Small-scale language models have shown rapid performance improvements, but these gains are largely derived from increasing training length. This approach scales only logarithmically with dataset size (Hoffmann et al., 2022), and recent small models require up to 15T tokens to improve state of the art by less than 1-2% (AI@Meta, 2024). The continued improvements provide evidence that small models remain under-trained, but simply scaling training tokens yields diminishing returns.

Prior open-weight models like LLaMA 3 (AI@Meta, 2024) and Mistral 7B (Jiang et al., 2023) have advanced the state of the art, but achieving strong performance at practical sizes (2B-27B parameters) without massive data scaling remains challenging.

**The core challenge: how to improve small language model performance without solely relying on increasing training length, while maintaining practical model sizes suitable for deployment on standard hardware.**

---

## Problem Solutions

Gemma 2 addresses these challenges through two main strategies:

1. **Knowledge distillation** replaces the one-hot next-token prediction target with the full probability distribution from a larger teacher model, providing richer gradients and enabling training beyond available token counts.

2. **Architectural modifications** including interleaved local-global attention (from Longformer), Grouped-Query Attention (GQA), logit soft-capping, and both pre-norm and post-norm with RMSNorm.

---

## Approach Details

### Method

#### Model Architecture

Gemma 2 models are decoder-only Transformers with the following specifications:

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

#### Interleaved Local-Global Attention

The models alternate between local sliding window attention and global attention in every other layer:

- **Local attention layers:** Sliding window size of 4096 tokens
- **Global attention layers:** Span of 8192 tokens (full context)

This design, adapted from Longformer (Beltagy et al., 2020), reduces computational cost while maintaining long-range dependencies through interleaved global layers.

#### Logit Soft-Capping

Logits are capped in each attention layer and the final layer to stabilize training:

> logits <- soft_cap * tanh(logits / soft_cap)

The soft_cap parameter is set to **50.0** for self-attention layers and **30.0** for the final layer.

#### Grouped-Query Attention

All models use GQA with **num_groups = 2** (i.e., 2 query heads per KV head). Ablations show increased inference speed while maintaining downstream performance (Table 8).

#### Normalization

Both **pre-norm and post-norm** are applied using RMSNorm to normalize input and output of each transformer sub-layer (attention and feedforward).

---

### Key Technical Components

#### Knowledge Distillation

For the 2B and 9B models, training uses knowledge distillation from a larger teacher model rather than standard next-token prediction. Given teacher probability P_T(x | x_c), the student minimizes:

> min_{P_S} sum_x -P_T(x | x_c) log P_S(x | x_c)

Key aspects:
- The 2B and 9B models are trained with distillation; the 27B model is trained from scratch
- Training uses more than **50x** the compute-optimal token quantity predicted by Chinchilla scaling laws
- Distillation was also used in Gemini 1.5 (Gemini Team, 2024)

#### Training Data

| Model | Training Tokens | Data Sources |
|---|---|---|
| 27B | 13T | Web documents, code, science articles |
| 9B | 8T | Web documents, code, science articles |
| 2B | 2T | Web documents, code, science articles |

- Primarily English data
- Not multimodal, not trained for multilingual capabilities
- Same tokenizer as Gemma 1 and Gemini: SentencePiece with 256K vocabulary

#### Post-Training

1. **Supervised Fine-Tuning (SFT):** Text-only, English-only synthetic and human-generated prompt-response pairs
2. **RLHF:** Reward model trained on English-only preference data; reward model is an order of magnitude larger than the policy
3. **Model merging:** Averaging models from different hyperparameter runs (Ramé et al., 2024)

---

### Experimental Setup

**Pre-training evaluation:** HuggingFace evaluation suite including MMLU (5-shot), GSM8K (5-shot), ARC-C (25-shot), HellaSwag (10-shot), Winogrande (5-shot).

**Instruction-tuned evaluation:**
- LMSYS Chatbot Arena blind side-by-side evaluations
- Human preference studies for safety and instruction following
- Multi-turn conversation scenarios (500 held-out scenarios, avg 8.4 turns)

**Baselines:** LLaMA-3 8B/70B, Mistral 7B, Qwen1.5 32B, Gemma 1 2B/7B, GPT-4o, GPT-3.5-Turbo.

**Compute:** TPUv4/v5e/v5p clusters; 512-6144 chips depending on model size; ZeRO-3 style optimizer state sharding; GSPMD partitioner.

---

### Key Results

#### Pre-trained Model: Gemma 2 27B vs Baselines

| Benchmark | LLaMA-3 70B | Qwen1.5 32B | Gemma-2 27B |
|---|---|---|---|
| MMLU | 79.2 | 74.3 | **75.2** |
| GSM8K | 76.9 | 61.1 | **74.0** |
| ARC-c | 68.8 | 63.6 | **71.4** |
| HellaSwag | 88.0 | 85.0 | **86.4** |
| Winogrande | 85.3 | 81.5 | **83.7** |

- Gemma 2 27B outperforms Qwen1.5 32B on all benchmarks
- Only a few percent below LLaMA-3 70B despite being 2.5x smaller and trained on 2/3 less data

#### Pre-trained Models: 2B-9B Range

| Benchmark | Gemma-1 2B | Gemma-2 2B | Mistral 7B | LLaMA-3 8B | Gemma-1 7B | Gemma-2 9B | Gemma-2 27B |
|---|---|---|---|---|---|---|---|
| MMLU (5-shot) | 42.3 | **52.2** | 62.5 | 66.6 | 64.4 | **71.3** | 75.2 |
| GSM8K (5-shot) | 15.1 | **24.3** | 39.6 | 45.7 | 51.8 | **68.6** | 74.0 |
| BBH (3-shot) | 35.2 | **41.9** | 56.0 | 61.1 | 59.0 | **68.2** | 74.9 |
| HumanEval | 22.0 | 20.1 | 26.2 | - | 32.3 | **40.2** | 51.8 |
| MATH (4-shot) | 11.8 | **16.0** | 12.7 | - | 24.3 | **36.6** | 42.3 |
| Average (8) | 44.0 | **50.0** | 61.0 | 61.9 | 62.4 | **70.2** | 74.4 |

- Gemma 2 9B achieves average 70.2 on 8 core benchmarks, surpassing LLaMA-3 8B (61.9)
- Massive improvement from Gemma 1: +10 points for 9B vs 7B on several benchmarks

#### LMSYS Chatbot Arena (Instruction-Tuned)

| Model | Elo | 95% CI | Open |
|---|---|---|---|
| gemma-2-27b-it | **1218** | +4/-3 | + |
| llama-3-70b-instruct | 1206 | +2/-2 | + |
| gemma-2-9b-it | **1187** | +3/-5 | + |
| gpt-4-0314 | 1186 | +2/-3 | - |
| gemma-2-2b-it | **1126** | +10/-10 | + |
| gpt-3.5-turbo-0613 | 1116 | +3/-4 | - |

- Gemma 2 27B (Elo 1218) ranked higher than LLaMA-3 70B (Elo 1206)
- Gemma 2 9B (Elo 1187) similar to GPT-4-0314 (Elo 1186)
- Gemma 2 2B (Elo 1126) ranked higher than GPT-3.5-Turbo (Elo 1116)

#### Distillation Ablations

| Training Method | Average (3 benchmarks) |
|---|---|
| From scratch | 60.3 |
| Distilled (7B teacher) | **67.7** |

- Distillation provides +7.4 points improvement on a 2B model trained for 500B tokens
- Benefit persists as model size increases (Table 7): 200M, 400M, 1B models all show 2-point perplexity reduction

---

## Limitations and Failure Modes

1. **English-only focus:** Models are not trained for multilingual capabilities and are not multimodal.

2. **Limited context length:** 8192 token context window, shorter than competitors like LLaMA-3 (128K with RoPE scaling) and Qwen2 (128K).

3. **No distillation for 27B:** The largest model is trained from scratch without distillation, leaving open whether distillation would help at this scale.

4. **Format sensitivity at small scale:** Gemma 2 2B models show higher variance across formatting variations (std 2.1) compared to larger models (std 0.9-1.0), though still much better than Mistral 7B (std 6.9) (Table 11).

5. **Safety limitations:** While Gemma 2 shows lower violation rates overall, the paper acknowledges models cannot cover all applications and scenarios. Users should conduct rigorous safety testing specific to their use case.

6. **Limited training detail disclosure:** Specific learning rates, optimizer configurations, and total compute costs are not disclosed.

### Scope and Comparability

- **What was not tested:** Long-context evaluation beyond 8K tokens; multilingual benchmarks; multimodal tasks.
- **Comparability notes:** Comparison with LLaMA-3 70B is not apples-to-apples due to 2.5x size difference. The paper uses total parameters (not active) for comparison since "total memory usage is often what limits the use of open models on standard devices."

---

## Conclusions

### Contributions

1. **Knowledge distillation as scaling alternative.** Demonstrates that distilling from a larger teacher provides richer gradients than next-token prediction, enabling training beyond available token counts and achieving +7.4 points improvement over training from scratch.

2. **State-of-the-art open models at practical sizes.** Releases 2B, 9B, and 27B models that outperform competitors at similar or larger sizes: Gemma 2 27B beats Qwen1.5 32B and approaches LLaMA-3 70B despite being 2.5x smaller.

3. **Architectural innovations for stability and efficiency.** Combines interleaved local-global attention, logit soft-capping, GQA, and dual normalization to achieve training stability and inference efficiency.

4. **Comprehensive safety evaluation.** Extensive assurance evaluations including offensive cyber-security, CBRN knowledge, self-proliferation, and persuasion capabilities, finding Gemma 2 has low capabilities in high-risk domains.

5. **Significantly reduced memorization.** Memorization rates below 0.1%, significantly lower than prior models including Gemma 1.

### Implications

1. **Distillation may extend effective training.** The success of training 50x beyond compute-optimal tokens with distillation suggests this approach may circumvent diminishing returns from data scaling alone (speculative: could enable "synthetic" data augmentation effects).

2. **Depth over width at matched parameters.** The finding that deeper 9B networks outperform wider ones (+1.2 points) may inform future architecture design for practical-sized models.

3. **GQA as standard for open models.** Following Qwen2 and Llama 3, adoption of GQA across all sizes suggests this is becoming the de facto standard for efficient inference.

---

## Key Claims

1. **C1:** A 2B model trained with knowledge distillation achieves 67.7 average on 3 benchmarks vs 60.3 from scratch training (+7.4 points) (Table 6, Section 5). Status: **supported**. Scope: 500B tokens, 7B teacher.

2. **C2:** Gemma 2 27B outperforms Qwen1.5 32B on all HuggingFace evaluation benchmarks (MMLU 75.2 vs 74.3, GSM8K 74.0 vs 61.1, ARC-c 71.4 vs 63.6) (Table 12, Section 6.1). Status: **supported**.

3. **C3:** Gemma 2 27B is competitive with LLaMA-3 70B despite being 2.5x smaller: MMLU 75.2 vs 79.2, GSM8K 74.0 vs 76.9, HellaSwag 86.4 vs 88.0 (Table 12, Section 6.1). Status: **supported**.

4. **C4:** Gemma 2 9B IT achieves Elo 1187 on LMSYS Chatbot Arena, nearly identical to GPT-4-0314 (Elo 1186) (Table 14, Section 6.2). Status: **supported**. Scope: Blind human evaluations, snapshot in time.

5. **C5:** GQA with num_groups=2 maintains downstream performance (50.8 vs 50.3 for MHA) while enabling faster inference (Table 8, Section 5). Status: **supported**. Scope: 9B model, 4 benchmarks.

6. **C6:** Deeper 9B architecture outperforms wider 9B by +1.2 points average on 4 benchmarks (52.0 vs 50.8) (Table 9, Section 5). Status: **supported**.

7. **C7:** Gemma 2 memorizes significantly less than prior models, with verbatim memorization rates below 0.1% (Figure 1, Section 7). Status: **supported**. Scope: 50-token continuation, exact match.

---

## Open Questions

1. **Distillation scaling.** Would distilling the 27B model from an even larger teacher yield gains? The paper only applies distillation to 2B and 9B. Not addressed by subsequent work in this repository.

2. **Optimal teacher-student ratio.** The paper uses roughly 3-4x teacher-to-student size ratio (7B→2B, 27B→9B). Is this optimal? Not addressed.

3. **Context extension.** The 8K context is shorter than competitors. Can the interleaved local-global attention pattern be extended while maintaining efficiency? Not addressed.

4. **Distillation data efficiency.** How does the distillation benefit vary with training token count? The paper shows 50x compute-optimal but doesn't ablate intermediate points. Not addressed.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundation decoder-only Transformer architecture that Gemma 2 builds upon.
- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models.* Gemma 2 uses GQA with num_groups=2 across all model sizes.
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE positional embeddings used in Gemma 2.
- **Shazeer (2020)** -- *GLU Variants Improve Transformer.* GeGLU activation function used in all Gemma 2 models.

### Efficient Attention

- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Gemma 2 adopts interleaved local sliding window and global attention pattern.
- **Zhang and Sennrich (2019)** -- *Root Mean Square Layer Normalization.* RMSNorm used for both pre-norm and post-norm.

### Knowledge Distillation

- **Hinton et al. (2015)** -- *Distilling the Knowledge in a Neural Network.* Foundational knowledge distillation work that Gemma 2's training approach extends.
- **Agarwal et al. (2024)** -- *On-Policy Distillation of Language Models.* Recent distillation techniques applied in Gemma 2's SFT phase.

### Post-Training

- **Ramé et al. (2024)** -- *WARP: On the Benefits of Weight Averaged Rewarded Policies.* Model merging technique used to combine checkpoints from different hyperparameters.
- **Zheng et al. (2023)** -- *LMSYS-Chat-1M.* Prompts (not answers) used for post-training data.

### Competing Models

- **AI@Meta (2024)** -- *LLaMA 3 Model Card.* Primary comparison baseline; Gemma 2 27B approaches LLaMA-3 70B despite 2.5x smaller size.
- **Jiang et al. (2023)** -- *Mistral 7B.* 7B-class baseline; Gemma 2 shows much better format robustness.
- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models.* Chinchilla scaling laws that Gemma 2's distillation approach exceeds by 50x.

### Evaluation

- **Chiang et al. (2024)** -- *Chatbot Arena: An Open Platform for Evaluating LLMs.* Primary human evaluation benchmark where Gemma 2 sets new open-model records.
- **Hendrycks et al. (2020)** -- *Measuring Massive Multitask Language Understanding.* MMLU benchmark for knowledge evaluation.
