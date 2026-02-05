---
title: "Qwen Technical Report"
authors: "Bai, Bai, Chu, Cui, Dang, Deng, Fan, Ge, Han, Huang, et al."
year: 2023
venue: "arXiv preprint"
paper_type: preprint
categories: ["model-release", "architecture", "position-encoding", "context-extension"]
scope: ["bilingual LLM (English/Chinese)", "open-source foundation models"]
benchmarks_used: ["mmlu", "c-eval", "gsm8k", "math-hendrycks", "humaneval", "mbpp", "bbh", "hellaswag", "piqa", "arc", "cmmlu", "agi-eval", "gaokao-bench"]
models_introduced: ["qwen-1.8b", "qwen-7b", "qwen-14b", "code-qwen-7b", "code-qwen-14b"]
models_evaluated: ["llama-7b", "llama-13b", "llama-2-7b", "llama-2-13b", "llama-2-70b", "gpt-3.5-turbo", "gpt-4"]
key_claims:
  - id: C1
    claim: "Qwen-14B outperforms previous 13B-class open-source models across all evaluated benchmarks"
    evidence: "Table 2, Section 2.6"
    status: supported
  - id: C2
    claim: "Training-free context extension techniques (dynamic NTK + LogN + window attention) maintain low perplexity at 16K context"
    evidence: "Table 3, Section 2.5"
    status: supported
  - id: C3
    claim: "RLHF significantly outperforms SFT in human evaluation, approaching but not matching GPT-4"
    evidence: "Figure 4, Section 3.3"
    status: supported
  - id: C4
    claim: "Qwen-Chat achieves 98% tool selection accuracy on ReAct prompting benchmark, surpassing GPT-4 (95%)"
    evidence: "Table 6, Section 3.4"
    status: supported
  - id: C5
    claim: "Adding bias to QKV attention layers enhances length extrapolation ability"
    evidence: "Section 2.3, citing Su (2023b)"
    status: unvalidated
cross_references:
  - target: 2023-02-llama-open-efficient-foundation
    type: extends
    detail: "Qwen architecture builds on LLaMA with modifications including untied embeddings, QKV bias, and SwiGLU activation"
  - target: 2023-07-llama-2-open-foundation-chat
    type: concurrent
    detail: "Released concurrently; Qwen compares against Llama 2 throughout"
  - target: 2024-07-qwen2-technical-report
    type: extended-by
    detail: "Qwen2 succeeds Qwen with expanded model sizes and improved performance"
open_questions:
  - question: "What is the optimal balance between pretrain gradient and RLHF for mitigating alignment tax?"
    addressed_by: null
  - question: "How do layer-wise window sizes affect context modeling at different depths?"
    addressed_by: null
---

# Qwen Technical Report

**Authors:** Jinze Bai, Shuai Bai, Yunfei Chu, et al. (Qwen Team, Alibaba Group)
**Date:** September 2023, arXiv:2309.16609

---

## Core Research Problem

Despite remarkable progress in large language models, the community faces challenges with **reproducibility, steerability, and accessibility**. While proprietary models like GPT-4 demonstrate impressive capabilities, open-source alternatives remain limited, particularly for bilingual (English/Chinese) applications and specialized domains like coding and mathematics.

Prior open-source efforts (LLaMA, Llama 2) established strong foundations but:
1. Lacked native multilingual optimization, particularly for Chinese
2. Provided limited context extension capabilities without fine-tuning
3. Offered no specialized variants for coding or mathematical reasoning

The core challenge: **how to build a comprehensive, competitive open-source LLM family with strong bilingual capabilities, effective context extension, and specialized domain variants**.

---

## Problem Solutions

The paper introduces **Qwen**, a family of large language models with the following key innovations:

1. **Modified Transformer architecture** building on LLaMA with targeted improvements (untied embeddings, QKV bias, SwiGLU activation)
2. **Bilingual tokenizer** with 152K vocabulary optimized for Chinese, English, and code
3. **Training-free context extension** combining NTK-aware interpolation, LogN-Scaling, and layer-wise window attention
4. **Comprehensive alignment pipeline** using SFT with ChatML format and RLHF with PPO
5. **Specialized domain models** for coding (Code-Qwen) and mathematics (Math-Qwen)

---

## Approach Details

### Architecture

Qwen adopts a modified Transformer architecture based on LLaMA with the following changes:

| Component | Design Choice | Rationale |
|-----------|--------------|-----------|
| Embedding | Untied input/output | Better performance at cost of memory |
| Position encoding | RoPE (FP32 inverse frequency) | Higher accuracy than BF16/FP16 |
| Bias | QKV attention only | Enhances extrapolation ability |
| Normalization | Pre-Norm with RMSNorm | Training stability + efficiency |
| Activation | SwiGLU | Outperforms GeLU in experiments |
| FFN dimension | 8/3 × hidden size | Standard practice with GLU variants |

**Model configurations:**

| Parameters | Hidden | Heads | Layers | Training Tokens |
|------------|--------|-------|--------|-----------------|
| 1.8B | 2048 | 16 | 24 | 2.2T |
| 7B | 4096 | 32 | 32 | 2.4T |
| 14B | 5120 | 40 | 40 | 3.0T |

### Tokenization

Qwen uses BPE tokenization based on OpenAI's tiktoken `cl100k_base` vocabulary, augmented with:
- Commonly used Chinese characters and words
- Tokens for other languages
- Numbers split into single digits (following LLaMA)

Final vocabulary size: **~152K tokens**.

The tokenizer achieves higher compression efficiency than LLaMA, Baichuan, ChatGLM2, and InternLM across most languages (Figure 3), implying lower serving costs.

### Pretraining

**Data:** Up to 3 trillion tokens from diverse sources:
- Public web documents (deduplicated via MinHash/LSH)
- Encyclopedia, books, code
- Multilingual with English and Chinese emphasis
- High-quality instruction data mixed into pretraining

**Data quality pipeline:**
1. HTML text extraction with language identification
2. Exact-match and fuzzy deduplication
3. Rule-based and ML-based quality filtering
4. Selective up-sampling of high-quality sources
5. 13-gram overlap filtering against benchmark test sets

**Training configuration:**
- Context length: 2048 tokens
- Optimizer: AdamW (β₁=0.9, β₂=0.95, ε=10⁻⁸)
- Learning rate: 3.0×10⁻⁴ (cosine decay to 10%)
- Batch size: 4M tokens
- Precision: BFloat16 mixed precision
- Attention: Flash Attention

### Context Length Extension

Qwen implements **training-free** techniques for inference-time context extension:

1. **NTK-aware interpolation** (bloc97, 2023): Adjusts RoPE base to preserve high-frequency information without fine-tuning

2. **Dynamic NTK-aware interpolation**: Changes scale dynamically by chunks to avoid performance degradation

3. **LogN-Scaling** (Chiang & Cholak, 2022; Su, 2023a): Rescales query-value dot product by factor dependent on context-to-training length ratio, stabilizing attention entropy

4. **Layer-wise window attention**: Lower layers use shorter windows; higher layers use longer windows (based on observation that lower layers are more sensitive to context extension)

**Perplexity results on arXiv (Table 3):**

| Model | 1024 | 2048 | 4096 | 8192 | 16384 |
|-------|------|------|------|------|-------|
| Qwen-7B (base) | 4.23 | 3.78 | 39.35 | 469.81 | 2645.09 |
| + all techniques | 4.23 | 3.78 | 3.58 | 3.49 | 4.32 |
| Qwen-14B + all | - | 3.46 | 3.29 | 3.18 | 3.42 |

### Alignment

#### Supervised Fine-Tuning (SFT)

**Data format:** ChatML style with special tokens `<|im_start|>` and `<|im_end|>` to disambiguate roles.

**Training configuration:**
- Loss masks on system and user inputs
- Sequence length: 2048
- Batch size: 128
- Steps: 4000
- Peak learning rate: 2×10⁻⁶ (warmup over 1430 steps)
- Weight decay: 0.1, dropout: 0.1, gradient clipping: 1.0

#### Reinforcement Learning from Human Feedback (RLHF)

**Reward model:**
- Preference Model Pretraining (PMP) on large comparison dataset
- Fine-tuning on diverse prompts (~6600 tags for sampling)
- Same-sized pretrained model as base with pooling layer
- Learning rate: 3×10⁻⁶, batch size: 64, 1 epoch

**PPO training:**
- 50-step value model warmup before policy updates
- 2 responses sampled per query
- KL divergence coefficient: 0.04
- Policy learning rate: 1×10⁻⁶, value learning rate: 5×10⁻⁶
- Value loss clipping: 0.15
- Policy top-p: 0.9
- Pretrained gradient to mitigate alignment tax

### Specialized Models

#### Code-Qwen

**Training:**
- Continued pretraining on ~90B code tokens
- Context length: 8192 (extended from 2048)
- Learning rate: 6.0×10⁻⁵ (14B) / 3.0×10⁻⁵ (7B)
- Multi-stage SFT for chat models

#### Math-Qwen-Chat

**Training:**
- Math SFT on augmented instruction dataset
- Sequence length: 1024 (shorter average length)
- Loss masks on system/user inputs
- Peak learning rate: 2×10⁻⁵, 50K steps

### Key Results

**Base model evaluation (Table 2):**

| Model | MMLU | C-Eval | GSM8K | MATH | HumanEval | MBPP | BBH |
|-------|------|--------|-------|------|-----------|------|-----|
| Llama 2-70B | 69.8 | 50.1 | 63.3 | 13.5 | 29.9 | 45.0 | 64.9 |
| **Qwen-14B** | **66.3** | **72.1** | **61.3** | **24.8** | **32.3** | **40.8** | **53.4** |
| Qwen-7B | 58.2 | 63.5 | 51.7 | 11.6 | 29.9 | 31.6 | 45.0 |

Qwen-14B outperforms Llama 2-70B on 3 of 7 benchmarks (C-Eval, MATH, HumanEval) despite being 5× smaller.

**Chat model evaluation (Table 5):**

| Model | MMLU (0/5) | C-Eval (0/5) | GSM8K (0/8) | HumanEval | BBH (0/3) |
|-------|------------|--------------|-------------|-----------|-----------|
| GPT-4 | -/83.0 | -/69.9 | -/91.4 | 86.6 | -/86.7 |
| Qwen-14B-Chat | 64.6/66.5 | 69.8/71.7 | 60.1/59.3 | 43.9 | 46.9/58.7 |
| Llama 2-Chat-70B | -/63.8 | -/44.3 | -/59.3 | 32.3 | -/60.8 |

**Tool use (Table 6):**

| Model | Tool Selection | Tool Input (Rouge-L) | False Positive |
|-------|----------------|---------------------|----------------|
| GPT-4 | 95% | 90 | 15.0% |
| Qwen-14B-Chat | **98%** | **93** | **2.4%** |
| GPT-3.5 | 85% | 88 | 75.0% |

**Code generation (Table 10):**

| Model | HumanEval | MBPP |
|-------|-----------|------|
| GPT-4 | 86.6 | - |
| Code-Qwen-14B-Chat | **66.4** | 52.4 |
| WizardCoder-34B | 73.2 | 61.2 |

**Math reasoning (Table 12):**

| Model | GSM8K | MATH |
|-------|-------|------|
| GPT-4 | 92.0 | 42.5 |
| Math-Qwen-14B-Chat | 69.8 | 24.2 |
| WizardMath-70B | 81.6 | 22.7 |

---

## Limitations and Failure Modes

1. **Gap with proprietary models:** Despite competitive performance, Qwen-Chat "still falls behind GPT-4" on human evaluation benchmarks (Section 3.3, Figure 4).

2. **Limited context training:** Base models trained with 2048 context length; longer contexts require inference-time techniques with some quality degradation at 16K+.

3. **Evaluation limitations:** Authors acknowledge "traditional benchmark evaluation" may not "accurately measure the performance and potential of chat models" (Section 3.3).

4. **Code Interpreter hallucination:** While Qwen-Chat outperforms Code LLaMA on code interpreter tasks, it can still fail on visualization tasks requiring multi-step planning (Tables 7-8, Figure 5).

5. **No explicit safety evaluation:** While safety data was included in SFT, comprehensive safety benchmarks are not reported.

---

## Conclusions

### Contributions

1. **Open-source multilingual LLM family:** Released Qwen models (1.8B, 7B, 14B) with strong bilingual (English/Chinese) capabilities, outperforming prior open-source models of similar size.

2. **Efficient tokenization:** Developed 152K vocabulary tokenizer achieving higher compression across multiple languages than competitors.

3. **Training-free context extension:** Demonstrated that combining NTK-aware interpolation, LogN-Scaling, and layer-wise window attention enables effective 8K-16K context handling without fine-tuning.

4. **Comprehensive alignment pipeline:** Documented SFT and RLHF procedures showing RLHF significantly improves human preference alignment.

5. **Specialized domain models:** Introduced Code-Qwen and Math-Qwen variants demonstrating continued pretraining and specialized SFT effectiveness.

6. **Tool use capabilities:** Demonstrated strong ReAct-based tool use, achieving higher accuracy than GPT-4 on Chinese tool selection benchmarks.

### Implications

1. **Architecture design:** QKV bias for length extrapolation and layer-wise attention windows suggest Transformer architectural choices remain consequential for long-context capability.

2. **Training efficiency:** Qwen-14B competitive with Llama 2-70B on several tasks suggests smaller models with more tokens and better data quality can match larger models.

3. **Alignment scaling:** RLHF improvements over SFT consistent across model sizes suggests preference learning remains valuable even for smaller models.

---

## Key Claims

1. **C1:** Qwen-14B achieves 66.3% on MMLU (5-shot), 72.1% on C-Eval (5-shot), outperforming all prior 13B-class open-source models (Table 2). *Status: supported.*

2. **C2:** Training-free context extension maintains perplexity below 4.32 at 16K context for Qwen-7B (Table 3). *Status: supported.*

3. **C3:** RLHF model significantly outperforms SFT models in human evaluation across knowledge, language understanding, creative writing, math, and coding (Figure 4). *Status: supported.*

4. **C4:** Qwen-Chat achieves 98% tool selection accuracy, surpassing GPT-4 (95%) and GPT-3.5 (85%) on Chinese ReAct benchmark (Table 6). *Status: supported.*

5. **C5:** Adding bias to QKV attention layers enhances extrapolation ability (Section 2.3). *Status: unvalidated* — referenced to Su (2023b) without experimental ablation in this paper.

---

## Open Questions

1. **Optimal alignment tax mitigation:** The paper notes using "significantly larger volume of pretrained data in comparison to PPO data" but does not provide optimal ratios.

2. **Layer-wise window assignment:** The observation that "lower layers are more sensitive to context length extension" is noted but not systematically studied.

3. **Scaling laws for specialized models:** How do continued pretraining data requirements scale with base model size for coding/math specialization?

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Touvron et al. (2023a)** — *LLaMA: Open and Efficient Foundation Language Models.* Primary architectural foundation that Qwen extends with modifications.

- **Su et al. (2021)** — *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Source of RoPE positional encoding used throughout Qwen.

- **Shazeer (2020)** — *GLU Variants Improve Transformer.* Basis for SwiGLU activation function selection.

### Context Extension

- **bloc97 (2023)** — *NTK-aware scaled RoPE.* Reddit post introducing NTK-aware interpolation for training-free context extension.

- **Chiang & Cholak (2022)** — *Overcoming a Theoretical Limitation of Self-Attention.* Source of LogN-Scaling technique.

- **Beltagy et al. (2020)** — *Longformer: The Long-Document Transformer.* Source of window attention mechanism.

### Alignment

- **Ouyang et al. (2022)** — *Training Language Models to Follow Instructions with Human Feedback.* InstructGPT paper establishing SFT + RLHF paradigm.

- **Bai et al. (2022b)** — *Training a Helpful and Harmless Assistant with RLHF.* Source of preference model pretraining (PMP) concept.

- **Schulman et al. (2017)** — *Proximal Policy Optimization Algorithms.* PPO algorithm used for policy training.

### Evaluation Benchmarks

- **Hendrycks et al. (2020)** — *Measuring Massive Multitask Language Understanding.* MMLU benchmark.

- **Huang et al. (2023)** — *C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite.* Primary Chinese evaluation benchmark.

- **Chen et al. (2021)** — *Evaluating Large Language Models Trained on Code.* HumanEval code generation benchmark.
