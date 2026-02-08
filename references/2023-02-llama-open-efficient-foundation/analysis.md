---
title: "LLaMA: Open and Efficient Foundation Language Models"
authors: "Touvron, Lavril, Izacard, Martinet, Lachaux, Lacroix, Roziere, Goyal, Hambro, Azhar, Rodriguez, Joulin, Grave, Lample"
year: 2023
venue: "arXiv 2023"
paper_type: preprint
categories: ["model-release", "architecture"]
scope: ["open foundation models", "efficient training", "scaling beyond Chinchilla-optimal", "publicly available training data"]
benchmarks_used: ["arc", "hellaswag", "mmlu", "triviaqa", "natural-questions", "humaneval", "gsm8k", "boolq", "race", "piqa", "siqa", "winogrande", "openbookqa", "mbpp", "math-hendrycks", "truthfulqa"]
models_introduced: ["llama-7b", "llama-13b", "llama-33b", "llama-65b"]
models_evaluated: ["gpt-3-175b", "palm-540b", "chinchilla-70b", "gopher-280b", "lamda-137b"]
key_claims:
  - id: C1
    claim: "LLaMA-13B outperforms GPT-3 (175B) on most benchmarks despite being >10x smaller"
    evidence: "Tables 3-9, Section 3"
    status: supported
    scope: "zero-shot and few-shot settings, 8 common sense + 2 QA + 2 reading comprehension + 2 code + 1 multitask benchmarks, English only"
    magnitude: "e.g., HellaSwag 79.2 vs 78.9, ARC-c 52.7 vs 51.4, MMLU 46.9 vs 43.9"
  - id: C2
    claim: "Training exclusively on publicly available data produces competitive foundation models"
    evidence: "Section 2.1, Tables 3-9"
    status: supported
    scope: "English-dominant data (67% CommonCrawl, 15% C4, 4.5% GitHub, 4.5% Wikipedia in 20 languages, 4.5% books, 2.5% ArXiv, 2% StackExchange)"
    magnitude: "LLaMA-13B matches or exceeds GPT-3 175B across 20 benchmarks; LLaMA-65B competitive with Chinchilla-70B"
  - id: C3
    claim: "LLaMA-65B is competitive with Chinchilla-70B and PaLM-540B on most benchmarks"
    evidence: "Tables 3-9, Section 3"
    status: supported
    scope: "zero-shot and few-shot settings across common sense reasoning, QA, reading comprehension, code, math benchmarks; English only"
    magnitude: "outperforms Chinchilla on most common sense tasks (e.g., HellaSwag 84.2 vs 80.8); trails on MMLU (63.4 vs 67.5 Chinchilla, 69.3 PaLM)"
  - id: C4
    claim: "Model performance continues to improve beyond Chinchilla-optimal token counts without saturating"
    evidence: "Figure 1, Section 1"
    status: supported
    scope: "7B-65B parameter models, 1.0T-1.4T tokens, training loss and downstream benchmarks"
    magnitude: "training loss still decreasing at 1.0T-1.4T tokens for all model sizes; Chinchilla-optimal for 7B would be ~200B tokens"
  - id: C5
    claim: "LLaMA-65B lags behind Chinchilla-70B and PaLM-540B on MMLU, possibly due to limited book and academic data in training"
    evidence: "Table 9, Section 3.6"
    status: supported
    scope: "MMLU 5-shot evaluation across humanities, STEM, social sciences, other"
    magnitude: "63.4 vs 67.5 (Chinchilla) and 69.3 (PaLM); LLaMA book/academic data totals 177GB vs up to 2TB in competing models"
  - id: C6
    claim: "Instruction finetuning on LLaMA-65B (LLaMA-I) achieves 68.9% on MMLU, outperforming comparable instruction-tuned models of moderate size"
    evidence: "Table 10, Section 4"
    status: supported
    scope: "MMLU 5-shot, comparison with OPT-IML-Max 30B, Flan-PaLM 62B, Flan-PaLM-cont 62B"
    magnitude: "68.9% vs OPT-IML-Max 43.2%, Flan-PaLM 59.6%, Flan-PaLM-cont 66.1%; still below GPT code-davinci-002 at 77.4%"
cross_references:
  - target: 2020-12-gpt-3-few-shot-learners
    type: extends
    detail: "LLaMA-13B outperforms GPT-3 175B on most benchmarks by training smaller models on substantially more tokens (1T vs 300B), demonstrating that inference-efficient scaling with architectural improvements can surpass much larger models"
  - target: 2019-02-gpt-2-language-models-unsupervised
    type: extends
    detail: "LLaMA continues GPT-2's scaling approach with architectural improvements (RoPE, SwiGLU, RMSNorm) and substantially more training tokens"
  - target: 2022-12-chinchilla-scaling-laws
    type: extends
    detail: "LLaMA explicitly follows Chinchilla scaling laws, training smaller models on more tokens for inference efficiency"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "LLaMA modifies the original Transformer architecture with pre-normalization, SwiGLU, and RoPE"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "LLaMA adopts RoPE for positional encoding, establishing it as the default for open models"
  - target: 2023-06-pi-positional-interpolation
    type: extended-by
    detail: "PI extends LLaMA's context window by interpolating RoPE positions"
  - target: 2023-07-llama-2-open-foundation-chat
    type: extended-by
    detail: "Llama 2 builds directly on LLaMA with longer context (4096 tokens) and RLHF"
  - target: 2023-06-rope-ntk
    type: extended-by
    detail: "NTK-aware scaling provides an alternative method to extend LLaMA's RoPE context window"
  - target: 2024-05-yarn-context-extension
    type: extended-by
    detail: "YaRN extends context of LLaMA-family models with improved RoPE scaling"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: extended-by
    detail: "DroPE modifies RoPE positional encoding in LLaMA-family models"
  - target: 2023-12-landmark-attention-infinite-context
    type: extended-by
    detail: "Landmark attention fine-tunes LLaMA 7B with learned block retrieval, extending its context to 32K tokens"
  - target: 2023-10-mistral-7b
    type: extended-by
    detail: "Mistral 7B outperforms LLaMA 1 34B on reasoning, math, and code generation at 7B parameters"
  - target: 2024-07-llama-3-herd-of-models
    type: extended-by
    detail: "Third generation of LLaMA family, scaling to 405B parameters and 15.6T tokens with 128K context"
  - target: 2024-03-yi-open-foundation-models
    type: extended-by
    detail: "Yi builds on LLaMA architecture and codebase with GQA for all model sizes, 3.1T bilingual tokens, and 200K context extension"
  - target: 2023-09-qwen-technical-report
    type: extended-by
    detail: "Qwen builds on LLaMA architecture with SwiGLU, RoPE, RMSNorm, adds QKV bias, and introduces training-free context extension via NTK-aware interpolation"
  - target: 2024-05-ring-attention-near-infinite-context
    type: extended-by
    detail: "Ring Attention uses LLaMA architecture (3B, 7B, 13B, 30B) to demonstrate context scaling up to 16M+ tokens through distributed blockwise attention"
  - target: 2025-04-differential-transformer
    type: extended-by
    detail: "DIFF Transformer adopts the LLaMA architecture template (RMSNorm, SwiGLU, RoPE) and replaces standard multi-head attention with differential attention that subtracts two softmax maps to cancel noise"
open_questions:
  - question: "How far beyond Chinchilla-optimal token counts can training be pushed before diminishing returns?"
    addressed_by: null
  - question: "Can the architecture support longer context windows beyond 2048 tokens without modification to RoPE?"
    addressed_by: 2023-06-pi-positional-interpolation
  - question: "Would training on more book and academic data close the MMLU gap with Chinchilla and PaLM?"
    addressed_by: null
  - question: "Can instruction finetuning close the remaining gap with proprietary models on knowledge-intensive tasks?"
    addressed_by: 2023-07-llama-2-open-foundation-chat
---

# LLaMA: Open and Efficient Foundation Language Models

**Authors:** Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothee Lacroix, Baptiste Roziere, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, Guillaume Lample (Meta AI)
**Date:** February 2023, arXiv:2302.13971

---

## Core Research Problem

At the time of writing, the most capable large language models (GPT-3, Chinchilla, PaLM) were not publicly released, restricting reproducibility and downstream research. Meanwhile, Hoffmann et al. (2022) -- *Training Compute-Optimal Large Language Models (Chinchilla)* -- demonstrated that for a given compute budget, the best performance is not achieved by the largest model but by smaller models trained on more data, revising the earlier scaling laws of Kaplan et al. (2020) which suggested scaling model size faster than data. However, Chinchilla's scaling laws optimize for *training* compute, disregarding the *inference* budget, which becomes critical when serving a language model at scale. As the paper states: "the preferred model is not the fastest to train but the fastest at inference" (Section 1).

Existing open models were either too small to be competitive (GPT-2, GPT-J 6B) or trained on insufficient data relative to their size (OPT-175B and GPT-3 each trained on only ~300B tokens). Open models like OPT (Zhang et al., 2022), GPT-NeoX (Black et al., 2022), BLOOM (Scao et al., 2022), and GLM (Zeng et al., 2022) were not competitive with PaLM-62B or Chinchilla (Section 1). The core challenge was: **how to train a family of open-weight language models that match or exceed the performance of the best closed models by training smaller architectures on significantly more tokens, using only publicly available data.**

---

## Problem Solutions

LLaMA addresses the problem by training four models (7B, 13B, 33B, 65B parameters) on 1.0T--1.4T tokens of publicly available data, substantially exceeding the Chinchilla-optimal token count for each model size:

1. **More tokens than Chinchilla-optimal.** Rather than stopping at the compute-optimal point, LLaMA trains beyond it, trading additional training compute for better inference-time performance at each model size. Hoffmann et al. (2022) recommends training a 10B model on 200B tokens, but LLaMA demonstrates that "the performance of a 7B model continues to improve even after 1T tokens" (Section 1).

2. **Publicly available training data only.** All training data comes from publicly accessible sources (CommonCrawl, C4, GitHub, Wikipedia, Gutenberg, Books3, ArXiv, StackExchange), enabling full reproducibility and open-sourcing (Section 2.1).

3. **Efficient Transformer architecture.** LLaMA adopts several architectural improvements over the original Transformer that had been validated independently in prior work: pre-normalization with RMSNorm (from GPT-3), SwiGLU activations (from PaLM), and Rotary Positional Embeddings (from GPT-NeoX) (Section 2.2).

---

## Approach Details

### Method

LLaMA uses a Transformer decoder (autoregressive, causal attention) with three modifications to the original architecture of Vaswani et al. (2017), as described in Section 2.2:

1. **Pre-normalization with RMSNorm.** Normalization is applied *before* each transformer sub-layer (attention and feed-forward) rather than after, following GPT-3. The RMSNorm normalizing function (Zhang & Sennrich, 2019) is used instead of LayerNorm. This improves training stability (Section 2.2).

2. **SwiGLU activation function.** The feed-forward network uses the SwiGLU activation (Shazeer, 2020) instead of ReLU. SwiGLU introduces a gating mechanism with a third weight matrix, so the FFN hidden dimension is set to 2/3 * 4d (instead of the standard 4d) to maintain roughly the same parameter count as a standard ReLU FFN (Section 2.2). The paper follows PaLM's use of this activation.

3. **Rotary Positional Embeddings (RoPE).** Absolute positional embeddings are removed and replaced with RoPE (Su et al., 2021), applied at each layer of the network, following GPT-NeoX. RoPE encodes position information by rotating query and key vectors in the attention mechanism, enabling relative position awareness through the dot product of rotated queries and keys (Section 2.2).

### Key Technical Components

#### Model Configurations

Table 2 (Section 2.2) specifies the hyperparameters for each model size:

| Model | Parameters | d_model | n_heads | n_layers | Learning Rate | Batch Size | Training Tokens |
|---|---|---|---|---|---|---|---|
| LLaMA-7B | 6.7B | 4096 | 32 | 32 | 3.0e-4 | 4M tokens | 1.0T |
| LLaMA-13B | 13.0B | 5120 | 40 | 40 | 3.0e-4 | 4M tokens | 1.0T |
| LLaMA-33B | 32.5B | 6656 | 52 | 60 | 1.5e-4 | 4M tokens | 1.4T |
| LLaMA-65B | 65.2B | 8192 | 64 | 80 | 1.5e-4 | 4M tokens | 1.4T |

Head dimension is d_model / n_heads = 128 for all models. The FFN hidden dimension for each model is 2/3 * 4 * d_model, rounded to the nearest multiple of 256 (derivable from the SwiGLU description and released code: 11008, 13824, 17920, 22016 respectively).

#### Training Data

All data is publicly available. After deduplication and filtering, the training mixture is (Table 1, Section 2.1):

| Dataset | Sampling Proportion | Epochs | Disk Size |
|---|---|---|---|
| English CommonCrawl (CCNet) | 67.0% | 1.10 | 3.3 TB |
| C4 | 15.0% | 1.06 | 783 GB |
| GitHub | 4.5% | 0.64 | 328 GB |
| Wikipedia (20 languages) | 4.5% | 2.45 | 83 GB |
| Books (Gutenberg + Books3) | 4.5% | 2.23 | 85 GB |
| ArXiv | 2.5% | 1.06 | 92 GB |
| StackExchange | 2.0% | 1.03 | 78 GB |

The entire training dataset contains roughly 1.4T tokens after tokenization. For most of the training data, each token is used only once during training, with the exception of Wikipedia and Books domains, over which approximately two epochs are performed (Section 2.1).

**CommonCrawl** is processed with a CCNet pipeline (Wenzek et al., 2020): deduplication at the line level, language identification with a fastText classifier to remove non-English pages, and quality filtering using a linear classifier trained to distinguish Wikipedia references from random CommonCrawl pages (Section 2.1).

**Tokenizer.** BPE using SentencePiece (Kudo & Richardson, 2018). All numbers are split into individual digits. Unknown UTF-8 characters are decomposed into bytes (Section 2.1).

#### Optimizer and Training

- **Optimizer:** AdamW (Loshchilov & Hutter, 2017) with beta_1 = 0.9, beta_2 = 0.95 (Section 2.3)
- **Learning rate schedule:** Cosine decay to 10% of peak, with 2,000 warmup steps
- **Weight decay:** 0.1
- **Gradient clipping:** 1.0
- Learning rate and batch size vary with model size (Table 2)

#### Efficient Implementation

Three optimizations are described in Section 2.4:

1. **Efficient causal multi-head attention** using the xformers library (Lefaudeux et al., 2022), inspired by Rabe & Staats (2021) and using the backward pass from Dao et al. (2022). This avoids storing attention weights and does not compute masked key/query scores.

2. **Selective activation checkpointing.** Rather than recomputing all activations during the backward pass, LLaMA saves expensive-to-compute activations (outputs of linear layers) while allowing cheap-to-recompute activations to be recomputed. This is achieved by manually implementing the backward function for transformer layers instead of relying on PyTorch autograd.

3. **Overlapping computation and communication.** Model and sequence parallelism (Korthikanti et al., 2022) combined with overlapping activation computation and GPU communication (all_reduce operations) during distributed training.

**Training throughput for the 65B model:** approximately 380 tokens/sec/GPU on 2048 A100-80GB GPUs, approximately 21 days for 1.4T tokens (Section 2.4).

### Experimental Setup

Models are evaluated on 20 benchmarks spanning six categories, in zero-shot and few-shot settings (Section 3):

- **Common sense reasoning (0-shot):** BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC-easy, ARC-challenge, OpenBookQA
- **Closed-book question answering:** Natural Questions (0/1/5/64-shot), TriviaQA (0/1/5/64-shot)
- **Reading comprehension (0-shot):** RACE-middle, RACE-high
- **Mathematical reasoning:** MATH, GSM8k (with and without maj1@k majority voting)
- **Code generation:** HumanEval (pass@1, 0-shot), MBPP (pass@1, 3-shot)
- **Multitask language understanding:** MMLU (5-shot)

**Baselines:** GPT-3 175B (Brown et al., 2020), Gopher 280B (Rae et al., 2021), Chinchilla 70B (Hoffmann et al., 2022), PaLM 8B/62B/540B (Chowdhery et al., 2022), OPT 175B (Zhang et al., 2022), GPT-J 6B (Wang & Komatsuzaki, 2021), GPT-NeoX 20B (Black et al., 2022). LLaMA also compares with LaMDA 137B on code generation. All baseline numbers are taken from the corresponding papers (Section 3).

For multiple choice tasks, the completion with the highest likelihood (normalized by number of characters) is selected, following Gao et al. (2021). For BoolQ and OpenBookQA, likelihood is normalized by the likelihood given "Answer:" as context, following Brown et al. (2020):

> P(completion|context) / P(completion|"Answer:")

**Reproducibility:** Code available at https://github.com/facebookresearch/llama. All training data is publicly available. No seeds are reported. Single training run per model configuration, no variance estimates reported (limited evidence for any individual benchmark result).

### Key Results

**Common sense reasoning (0-shot):**

| Model | Params | BoolQ | PIQA | SIQA | HellaSwag | WinoGrande | ARC-e | ARC-c | OBQA |
|---|---|---|---|---|---|---|---|---|---|
| GPT-3 | 175B | 60.5 | 81.0 | - | 78.9 | 70.2 | 68.8 | 51.4 | 57.6 |
| Gopher | 280B | 79.3 | 81.8 | 50.6 | 79.2 | 70.1 | - | - | - |
| Chinchilla | 70B | 83.7 | 81.8 | 51.3 | 80.8 | 74.9 | - | - | - |
| PaLM | 62B | 84.8 | 80.5 | - | 79.7 | 77.0 | 75.2 | 52.5 | 50.4 |
| PaLM-cont | 62B | 83.9 | 81.4 | - | 80.6 | 77.0 | - | - | - |
| PaLM | 540B | 88.0 | 82.3 | - | 83.4 | 81.1 | 76.6 | 53.0 | 53.4 |
| LLaMA | 7B | 76.5 | 79.8 | 48.9 | 76.1 | 70.1 | 72.8 | 47.6 | 57.2 |
| LLaMA | 13B | 78.1 | 80.1 | 50.4 | 79.2 | 73.0 | 74.8 | 52.7 | 56.4 |
| LLaMA | 33B | 83.1 | 82.3 | 50.4 | 82.8 | 76.0 | 80.0 | 57.8 | 58.6 |
| LLaMA | 65B | 85.3 | 82.8 | 52.3 | 84.2 | 77.0 | 78.9 | 56.0 | 60.2 |

LLaMA-65B outperforms Chinchilla-70B on all reported benchmarks but BoolQ (per the paper's text, Section 3.1, though the numerical values show LLaMA-65B at 85.3 vs Chinchilla at 83.7 on BoolQ). LLaMA-65B surpasses PaLM-540B on all benchmarks except BoolQ and WinoGrande. LLaMA-13B outperforms GPT-3 175B on most benchmarks despite being >10x smaller (Table 3, Section 3.1; tested across 8 benchmarks, single run per model, strong cross-benchmark evidence).

**Closed-book question answering (exact match):**

| Model | Params | NQ 0-shot | NQ 1-shot | NQ 5-shot | NQ 64-shot |
|---|---|---|---|---|---|
| GPT-3 | 175B | 14.6 | 23.0 | - | 29.9 |
| Gopher | 280B | 10.1 | - | 24.5 | 28.2 |
| Chinchilla | 70B | 16.6 | - | 31.5 | 35.5 |
| PaLM | 8B | 8.4 | 10.6 | - | 14.6 |
| PaLM | 62B | 18.1 | 26.5 | - | 27.6 |
| PaLM | 540B | 21.2 | 29.3 | - | 39.6 |
| LLaMA | 7B | 16.8 | 18.7 | 22.0 | 26.1 |
| LLaMA | 13B | 20.1 | 23.4 | 28.1 | 31.9 |
| LLaMA | 33B | 24.9 | 28.3 | 32.9 | 36.0 |
| LLaMA | 65B | 23.8 | 31.0 | 35.0 | 39.9 |

| Model | Params | TriviaQA 0-shot | TriviaQA 1-shot | TriviaQA 5-shot | TriviaQA 64-shot |
|---|---|---|---|---|---|
| Gopher | 280B | 43.5 | - | 57.0 | 57.2 |
| Chinchilla | 70B | 55.4 | - | 64.1 | 64.6 |
| LLaMA | 7B | 50.0 | 53.4 | 56.3 | 57.6 |
| LLaMA | 13B | 56.6 | 60.5 | 63.1 | 64.0 |
| LLaMA | 33B | 65.1 | 67.9 | 69.9 | 70.4 |
| LLaMA | 65B | 68.2 | 71.6 | 72.6 | 73.0 |

LLaMA-65B achieves state-of-the-art performance in the zero-shot and few-shot settings on both benchmarks. LLaMA-13B is competitive with GPT-3 and Chinchilla despite being 5--10x smaller, and "runs on a single V100 GPU during inference" (Tables 4--5, Section 3.2). Note: TriviaQA evaluation uses the filtered dev set, which differs from GPT-3 and PaLM's use of the unfiltered test set (Appendix A), affecting direct comparability.

**Reading comprehension (0-shot):**

| Model | Params | RACE-middle | RACE-high |
|---|---|---|---|
| GPT-3 | 175B | 58.4 | 45.5 |
| PaLM | 8B | 57.9 | 42.3 |
| PaLM | 62B | 64.3 | 47.5 |
| PaLM | 540B | 68.1 | 49.1 |
| LLaMA | 7B | 61.1 | 46.9 |
| LLaMA | 13B | 61.6 | 47.2 |
| LLaMA | 33B | 64.1 | 48.3 |
| LLaMA | 65B | 67.9 | 51.6 |

LLaMA-65B is competitive with PaLM-540B and LLaMA-13B outperforms GPT-3 by a few percentage points (Table 6, Section 3.3).

**Mathematical reasoning:**

| Model | Params | MATH | MATH+maj1@k | GSM8k | GSM8k+maj1@k |
|---|---|---|---|---|---|
| PaLM | 8B | 1.5 | - | 4.1 | - |
| PaLM | 62B | 4.4 | - | 33.0 | - |
| PaLM | 540B | 8.8 | - | 56.5 | - |
| Minerva | 8B | 14.1 | 25.4 | 16.2 | 28.4 |
| Minerva | 62B | 27.6 | 43.4 | 52.4 | 68.5 |
| Minerva | 540B | 33.6 | 50.3 | 68.5 | 78.5 |
| LLaMA | 7B | 2.9 | 6.9 | 11.0 | 18.1 |
| LLaMA | 13B | 3.9 | 8.8 | 17.8 | 29.3 |
| LLaMA | 33B | 7.1 | 15.2 | 35.6 | 53.1 |
| LLaMA | 65B | 10.6 | 20.5 | 50.9 | 69.7 |

On GSM8k without majority voting, LLaMA-65B (50.9) trails Minerva-62B (52.4), but with maj1@k majority voting, LLaMA-65B (69.7) outperforms Minerva-62B (68.5). The paper states "LLaMA-65B outperforms Minerva-62B" on GSM8k (Section 3.4), likely referring to the majority-voting setting. This is notable because LLaMA has not been finetuned on mathematical data, while Minerva is finetuned on 38.5B tokens from ArXiv and math web pages. Majority voting uses k = 256 for MATH and k = 100 for GSM8k (Table 7, Section 3.4; comparison is between two models at ~60B scale, moderate evidence).

**Code generation (pass@k):**

| Model | Params | HumanEval @1 | HumanEval @100 | MBPP @1 | MBPP @80 |
|---|---|---|---|---|---|
| LaMDA | 137B | 14.0 | 47.3 | 14.8 | 62.4 |
| PaLM | 8B | 3.6* | 18.7* | 5.0* | 35.7* |
| PaLM | 62B | 15.9 | 46.3* | 21.4 | 63.2* |
| PaLM-cont | 62B | 23.7 | - | 31.2 | - |
| PaLM | 540B | 26.2 | 76.2 | 36.8 | 75.0 |
| LLaMA | 7B | 10.5 | 36.5 | 17.7 | 56.2 |
| LLaMA | 13B | 15.8 | 52.5 | 22.0 | 64.0 |
| LLaMA | 33B | 21.7 | 70.7 | 30.2 | 73.4 |
| LLaMA | 65B | 23.7 | 79.3 | 37.7 | 76.8 |

Values marked with * are read from figures in Chowdhery et al. (2022). LLaMA-13B outperforms LaMDA 137B on both HumanEval and MBPP. LLaMA-65B outperforms PaLM-62B even when PaLM is trained longer (PaLM-cont 62B: 23.7 on HumanEval). Pass@1 results use temperature 0.1; pass@100/80 use temperature 0.8. Finetuning on code-specific tokens is beyond the scope of this paper (Table 8, Section 3.5).

**Multitask language understanding (MMLU, 5-shot):**

| Model | Params | Humanities | STEM | Social Sciences | Other | Average |
|---|---|---|---|---|---|---|
| GPT-NeoX | 20B | 29.8 | 34.9 | 33.7 | 37.7 | 33.6 |
| GPT-3 | 175B | 40.8 | 36.7 | 50.4 | 48.8 | 43.9 |
| Gopher | 280B | 56.2 | 47.4 | 71.9 | 66.1 | 60.0 |
| Chinchilla | 70B | 63.6 | 54.9 | 79.3 | 73.9 | 67.5 |
| PaLM | 8B | 25.6 | 23.8 | 24.1 | 27.8 | 25.4 |
| PaLM | 62B | 59.5 | 41.9 | 62.7 | 55.8 | 53.7 |
| PaLM | 540B | 77.0 | 55.6 | 81.0 | 69.6 | 69.3 |
| LLaMA | 7B | 34.0 | 30.5 | 38.3 | 38.1 | 35.1 |
| LLaMA | 13B | 45.0 | 35.8 | 53.8 | 53.3 | 46.9 |
| LLaMA | 33B | 55.8 | 46.0 | 66.7 | 63.4 | 57.8 |
| LLaMA | 65B | 61.8 | 51.7 | 72.9 | 67.4 | 63.4 |

LLaMA-65B (63.4) lags behind Chinchilla-70B (67.5) and PaLM-540B (69.3) on MMLU. The paper attributes this to limited book and academic data in LLaMA's training set: ArXiv, Gutenberg, and Books3 total only 177GB, while these models were trained on up to 2TB of books. This large quantity of books used by Gopher, Chinchilla and PaLM may also explain why Gopher outperforms GPT-3 on this benchmark, while comparable on other benchmarks (Table 9, Section 3.6; 5-shot evaluation across 57 tasks with per-domain breakdown, strong evidence for the MMLU gap).

### Instruction Finetuning

A brief experiment with instruction finetuning (Section 4) following the protocol of Chung et al. (2022) produces LLaMA-I, which achieves 68.9% on MMLU (5-shot):

| Model | Params | MMLU (5-shot) |
|---|---|---|
| OPT | 30B | 26.1 |
| GLM | 120B | 44.8 |
| PaLM | 62B | 55.1 |
| PaLM-cont | 62B | 62.8 |
| Chinchilla | 70B | 67.5 |
| LLaMA | 65B | 63.4 |
| OPT-IML-Max | 30B | 43.2 |
| Flan-PaLM | 62B | 59.6 |
| Flan-PaLM-cont | 62B | 66.1 |
| **LLaMA-I** | **65B** | **68.9** |

LLaMA-I outperforms all instruction-finetuned models of moderate size in Table 10 but remains below the state-of-the-art of 77.4 for GPT code-davinci-002 (numbers from Iyer et al. (2022)). The paper states this is "not the focus of this paper" and only a single experiment was conducted (Table 10, Section 4; limited evidence -- single experiment, single benchmark).

### Scaling Behavior

Training loss as a function of training tokens (Figure 1) shows that all four models continue to improve throughout training. The 33B and 65B models have not converged at 1.4T tokens. The 7B model has not saturated at 1.0T tokens. Performance on downstream benchmarks correlates with training perplexity during training (Figure 2), with exceptions on SIQA (high variance, "may indicate that this benchmark is not reliable") and WinoGrande (LLaMA-33B and LLaMA-65B show similar performance during training) (Section 3.7).

### Bias, Toxicity, and Misinformation

The paper evaluates potential harms across four benchmarks (Section 5):

**RealToxicityPrompts** (Table 11, Section 5.1): Toxicity scores from greedy generation on ~100k prompts, scored via PerspectiveAPI:

| Model | Params | Basic | Respectful |
|---|---|---|---|
| LLaMA | 7B | 0.106 | 0.081 |
| LLaMA | 13B | 0.104 | 0.095 |
| LLaMA | 33B | 0.107 | 0.087 |
| LLaMA | 65B | 0.128 | 0.141 |

Toxicity increases with model size, especially for "Respectful" prompts at the 65B scale. The authors note this pattern was also observed by Zhang et al. (2022) but not by Hoffmann et al. (2022), suggesting "the relation between toxicity and model size may only apply within a model family" (Section 5.1).

**CrowS-Pairs** (Table 12, Section 5.2): Bias measurement across 9 categories (higher = more biased):

| Category | LLaMA-65B | GPT-3 175B | OPT-175B |
|---|---|---|---|
| Gender | 70.6 | 62.6 | 65.7 |
| Religion | 79.0 | 73.3 | 68.6 |
| Race/Color | 57.0 | 64.7 | 68.6 |
| Sexual orientation | 81.0 | 76.2 | 78.6 |
| Age | 70.1 | 64.4 | 67.8 |
| Nationality | 64.2 | 61.6 | 62.9 |
| Disability | 66.7 | 76.7 | 76.7 |
| Physical appearance | 77.8 | 74.6 | 76.2 |
| Socioeconomic status | 71.5 | 73.8 | 76.2 |
| Average | 66.6 | 67.2 | 69.5 |

LLaMA compares slightly favorably on average (66.6 vs 67.2 and 69.5) but shows elevated bias in the religion category (79.0 vs 68.6 for OPT), followed by age (70.1) and gender (70.6). The authors note these biases "are expected to come from CommonCrawl despite multiple filtering steps" (Section 5.2).

**WinoGender** (Table 13, Section 5.3): Coreference resolution accuracy by pronoun type:

| Pronoun type | 7B | 13B | 33B | 65B |
|---|---|---|---|---|
| All | 66.0 | 64.7 | 69.0 | 77.5 |
| her/her/she | 65.0 | 66.7 | 66.7 | 78.8 |
| his/him/he | 60.8 | 62.5 | 62.1 | 72.1 |
| their/them/someone | 72.1 | 65.0 | 78.3 | 81.7 |
| her/her/she (gotcha) | 64.2 | 65.8 | 61.7 | 75.0 |
| his/him/he (gotcha) | 55.0 | 55.8 | 55.8 | 63.3 |

The model performs better on "their/them/someone" pronouns (81.7% for 65B) than on gendered pronouns, and drops further on "gotcha" cases where the pronoun does not match the majority gender of the occupation. This demonstrates "captured societal biases related to gender and occupation" (Section 5.3).

**TruthfulQA** (Table 14, Section 5.4):

| Model | Params | Truthful | Truthful*Informative |
|---|---|---|---|
| GPT-3 | 1.3B | 0.31 | 0.19 |
| GPT-3 | 6B | 0.22 | 0.19 |
| GPT-3 | 175B | 0.28 | 0.25 |
| LLaMA | 7B | 0.33 | 0.29 |
| LLaMA | 13B | 0.47 | 0.41 |
| LLaMA | 33B | 0.52 | 0.48 |
| LLaMA | 65B | 0.57 | 0.53 |

LLaMA-65B scores higher than GPT-3 175B (0.57 vs 0.28 truthful; 0.53 vs 0.25 truthful*informative) but "the rate of correct answers is still low, showing that our model is likely to hallucinate incorrect answers" (Section 5.4).

### Carbon Footprint

Table 15 (Section 6) provides carbon footprint estimates using the formula from Wu et al. (2022):

> Wh = GPU-h x (GPU power consumption) x PUE

with PUE = 1.1 and the US national average carbon intensity factor of 0.385 kg CO2eq/KWh:

> tCO2eq = MWh x 0.385

| Model | GPU Type | GPU Power | GPU-hours | Total Power | Carbon (tCO2eq) |
|---|---|---|---|---|---|
| OPT-175B | A100-80GB | 400W | 809,472 | 356 MWh | 137 |
| BLOOM-175B | A100-80GB | 400W | 1,082,880 | 475 MWh | 183 |
| LLaMA-7B | A100-80GB | 400W | 82,432 | 36 MWh | 14 |
| LLaMA-13B | A100-80GB | 400W | 135,168 | 59 MWh | 23 |
| LLaMA-33B | A100-80GB | 400W | 530,432 | 233 MWh | 90 |
| LLaMA-65B | A100-80GB | 400W | 1,022,362 | 449 MWh | 173 |

Total training of all LLaMA models: approximately 2,638 MWh and 1,015 tCO2eq. The same formula is applied to OPT and BLOOM for fair comparison, using the US national average rather than the data center's actual carbon intensity (Section 6).

---

## Limitations and Failure Modes

- **MMLU gap with knowledge-intensive baselines.** LLaMA-65B (63.4) trails Chinchilla-70B (67.5) and PaLM-540B (69.3) on MMLU. The paper attributes this to limited book and academic paper data: ArXiv, Gutenberg, and Books3 total 177GB vs. up to 2TB of books in competing models. This suggests knowledge-intensive tasks still benefit from more diverse or larger training data (Table 9, Section 3.6).

- **Toxicity increases with model size.** On RealToxicityPrompts, average toxicity scores increase from 0.106/0.081 (7B, basic/respectful) to 0.128/0.141 (65B), with a particularly sharp increase for "respectful" prompts at the 65B scale. The paper notes this pattern "could be explained by the fact that the larger model, Gopher, has worse performance than Chinchilla, suggesting that the relation between toxicity and model size may only apply within a model family" (Table 11, Section 5.1).

- **Gender bias in coreference resolution.** On WinoGender, the model performs significantly better on "their/them/someone" pronouns (81.7% for 65B) than on gendered pronouns ("her/her/she": 78.8%, "his/him/he": 72.1%). Performance drops further on "gotcha" cases where the pronoun does not match the majority gender of the occupation (75.0% and 63.3% for 65B), demonstrating captured societal biases related to gender and occupation (Table 13, Section 5.3).

- **Social biases.** On CrowS-Pairs, LLaMA-65B scores comparably to GPT-3 and OPT-175B on average (66.6 vs. 67.2 and 69.5) but shows elevated bias in the religion category (79.0 vs. 68.6 for OPT), followed by age (70.1) and gender (70.6). The authors note these biases "are expected to come from CommonCrawl despite multiple filtering steps" (Table 12, Section 5.2).

- **Hallucination.** On TruthfulQA, LLaMA-65B achieves 0.57 truthful and 0.53 truthful*informative scores, better than GPT-3 175B (0.28/0.25) but "still low, showing that our model is likely to hallucinate incorrect answers" (Table 14, Section 5.4).

- **[Inferred]** **Short context window.** The models are trained with a context length of 2048 tokens, limiting their applicability to tasks requiring longer inputs. This limitation is not discussed as a shortcoming in the paper but motivated the subsequent context extension research (Position Interpolation, NTK-aware scaling, YaRN).

- **[Inferred]** **No instruction tuning by default.** The released models are base models without instruction finetuning. Section 4 shows only a brief experiment with instruction tuning, noting it is "not the focus of this paper." The lack of instruction tuning limits out-of-the-box usability for downstream applications.

#### Scope and Comparability

- **What was not tested:** No evaluation on non-English tasks beyond Wikipedia training data in 20 languages (all benchmarks are English-only). No evaluation at scales below 7B or above 65B. No evaluation of long-context capabilities beyond the 2048-token training context. No ablation of individual architectural choices (RMSNorm vs LayerNorm, SwiGLU vs ReLU, RoPE vs absolute embeddings).
- **Comparability notes:** TriviaQA evaluation uses the filtered dev set, while GPT-3 and PaLM use the unfiltered test set (Appendix A), making direct comparison imprecise. RealToxicityPrompts scores are obtained with different sampling strategies, numbers of prompts, and API versions than prior work, making cross-paper toxicity comparison difficult (Section 5.1). The CrowS-Pairs benchmark methodology (perplexity-based comparison) differs across implementations. All baseline numbers are taken from their respective papers rather than re-evaluated under identical conditions, introducing potential methodological inconsistencies.

---

## Conclusions

### Contributions

1. **Inference-optimized scaling strategy.** LLaMA demonstrates that training smaller models on significantly more tokens than Chinchilla-optimal yields better performance at each inference budget, reframing the scaling problem from training compute to inference efficiency (Section 1, Figure 1).

2. **Competitive open models from public data.** All training data comes from publicly available sources, establishing that proprietary or undocumented datasets are not necessary for competitive foundation model performance. LLaMA-13B outperforms GPT-3 175B on most benchmarks, and LLaMA-65B is competitive with Chinchilla-70B and PaLM-540B (Tables 3--9).

3. **Architectural configuration for the open model ecosystem.** The combination of pre-normalization (RMSNorm), SwiGLU activations, and RoPE became the de facto architecture for subsequent open-weight models. These choices, each validated independently in prior work, combine to produce models that train stably across a wide range of scales (Section 2.2).

4. **RoPE as positional encoding standard.** LLaMA's adoption of RoPE with a 2048-token context window established the positional encoding configuration that the entire subsequent context extension research direction targets (Position Interpolation, NTK-aware scaling, YaRN, DroPE) (Section 2.2).

5. **Training efficiency at scale.** The 65B model requires 1,022,362 GPU-hours on A100-80GB with throughput of ~380 tokens/sec/GPU. The efficient implementation (xformers attention, selective activation checkpointing, overlapped computation/communication) enables training on 2048 GPUs in approximately 21 days (Table 15, Section 2.4).

6. **Carbon footprint transparency.** The paper provides detailed carbon emission accounting: total training of all LLaMA models consumed 2,638 MWh and emitted an estimated 1,015 tCO2eq, using the US national average carbon intensity factor of 0.385 kg CO2eq/KWh (Table 15, Section 6).

### Implications

1. **Smaller models can replace much larger ones.** The finding that LLaMA-13B outperforms GPT-3 175B suggests that many practical LLM applications can be served with models 10x smaller than previously assumed, with dramatic implications for deployment cost and accessibility. [Inference: this was subsequently validated by the widespread adoption of LLaMA-derived models.]

2. **Training token scaling may be more important than parameter scaling.** The consistent improvement of all models beyond their Chinchilla-optimal token counts suggests the Chinchilla scaling laws underestimate the benefit of additional training data, particularly when optimizing for inference-time performance rather than training compute (Section 1, Figure 1).

3. **Data composition matters for knowledge-intensive tasks.** The MMLU gap despite competitive performance elsewhere suggests that benchmark-specific performance depends heavily on training data composition (e.g., book and academic data for MMLU), not just total data volume (Section 3.6). [Speculative implication.]

---

## Key Claims

1. **C1: LLaMA-13B outperforms GPT-3 175B on most benchmarks.** Demonstrated across common sense reasoning (Table 3: higher on 6 of 7 comparable benchmarks), closed-book QA (Tables 4--5: competitive or better), reading comprehension (Table 6: higher on both RACE-middle and RACE-high), and code generation (Table 8: higher on both HumanEval and MBPP). LLaMA-13B also exceeds GPT-3 on MMLU (46.9 vs 43.9) (Section 3). Scope: zero-shot and few-shot settings, English-only, across 8 common sense + 2 QA + 2 reading comprehension + 2 code + 1 multitask benchmarks. Magnitude: e.g., HellaSwag 79.2 vs 78.9, ARC-c 52.7 vs 51.4, MMLU 46.9 vs 43.9. Tested across 15+ benchmarks spanning 6 task categories (strong cross-benchmark evidence, but single run per configuration). Status: **supported**.

2. **C2: Public data suffices for competitive models.** All training data comes from publicly available sources (Table 1, Section 2.1). The resulting models match or exceed closed models trained on proprietary data across 20 benchmarks (Section 3). Scope: English-dominant data mixture (67% CommonCrawl, 15% C4, etc.), 1.0T-1.4T tokens. Magnitude: LLaMA-13B matches or exceeds GPT-3 175B; LLaMA-65B competitive with Chinchilla-70B. Single set of training runs -- no comparison against identical models trained on proprietary data (limited causal evidence). Status: **supported**.

3. **C3: LLaMA-65B is competitive with Chinchilla-70B and PaLM-540B.** LLaMA-65B outperforms Chinchilla-70B on all common sense reasoning benchmarks but BoolQ per the paper's text (Table 3), surpasses PaLM-540B on all except BoolQ and WinoGrande (Table 3), and achieves state-of-the-art on Natural Questions and TriviaQA (Tables 4--5). The main deficit is on MMLU (63.4 vs. 67.5 for Chinchilla, 69.3 for PaLM) (Table 9). Scope: zero-shot and few-shot settings across common sense, QA, reading comprehension, code, math, and multitask benchmarks; English only. Magnitude: HellaSwag 84.2 vs 80.8 (Chinchilla) and 83.4 (PaLM); MMLU 63.4 vs 67.5/69.3. Tested across all 20 benchmarks (strong evidence breadth). Status: **supported**.

4. **C4: Performance continues to improve beyond Chinchilla-optimal token counts.** Training loss curves (Figure 1) show no saturation for any model size at 1.0T or 1.4T tokens. Downstream benchmark performance improves steadily during training and correlates with training perplexity (Figure 2, Section 3.7). Scope: 7B--65B parameter models, 1.0T--1.4T tokens, training loss and downstream benchmarks. Magnitude: training loss still decreasing at 1.0T--1.4T tokens; Chinchilla-optimal for 7B would be ~200B tokens, so LLaMA trains 5x beyond that. Evidence based on 4 model sizes with continuous monitoring (moderate evidence, but no controlled experiment isolating the effect of additional tokens). Status: **supported**.

5. **C5: MMLU gap attributed to limited book/academic data.** LLaMA's book and academic data (ArXiv + Gutenberg + Books3) totals only 177GB, while competing models used up to 2TB of books. The paper explicitly cites this as "a potential explanation" (Section 3.6). Scope: MMLU 5-shot evaluation across humanities, STEM, social sciences, other. Magnitude: 63.4 vs 67.5 (Chinchilla) and 69.3 (PaLM). The causal link is hypothesized, not experimentally isolated -- no ablation varying book/academic data proportion (limited evidence for the causal claim). Status: **supported** as a plausible explanation.

6. **C6: Instruction-finetuned LLaMA-I reaches 68.9% on MMLU.** This outperforms OPT-IML-Max 30B (43.2), Flan-PaLM 62B (59.6), and Flan-PaLM-cont 62B (66.1), but remains below GPT code-davinci-002 (77.4) (Table 10, Section 4). Scope: MMLU 5-shot, comparison with OPT-IML-Max 30B, Flan-PaLM 62B, Flan-PaLM-cont 62B. Magnitude: 68.9% vs Flan-PaLM-cont 66.1% (+2.8 pp). Single experiment on a single benchmark (limited evidence). Status: **supported**.

---

## Open Questions

1. **How far beyond Chinchilla-optimal can training be pushed?** The paper shows that training loss has not saturated at 1.0T--1.4T tokens for any model size (Figure 1), but does not investigate diminishing returns at higher token counts. The optimal training token count for each model size when optimizing for inference remains an open question. Not directly addressed by subsequent work in this directory.

2. **Can the 2048-token context window be extended without modification?** The fixed 2048-token context length limits applicability to long-document tasks. Addressed by Position Interpolation (Chen et al., 2023), NTK-aware scaling (bloc97, 2023), and YaRN (Peng et al., 2024), which extend LLaMA's RoPE-based context window.

3. **Would more book and academic data close the MMLU gap?** The paper hypothesizes that the MMLU deficit is due to limited training data from books and academic papers (Section 3.6). Whether increasing this data proportion would close the gap with Chinchilla and PaLM is not experimentally tested. Not directly addressed.

4. **Can instruction finetuning close the gap with proprietary models?** LLaMA-I achieves 68.9% on MMLU but remains below 77.4% for GPT code-davinci-002. Whether more sophisticated instruction tuning or RLHF can close this gap is explored in Llama 2 (Touvron et al., 2023b). Partially addressed by 2023-07-llama-2-open-foundation-chat.

---

## Core References and Why They Are Referenced

### Scaling Laws and Training Strategy

- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models (Chinchilla).* Central motivation: Chinchilla demonstrates that scaling tokens is as important as scaling parameters. LLaMA's training strategy extends this insight by deliberately training beyond the Chinchilla-optimal token budget to maximize inference-time performance rather than training compute. Chinchilla-70B serves as a primary comparison target.

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Earlier scaling laws that Chinchilla revised. Kaplan et al. suggested scaling model size faster than data; LLaMA's results further support Chinchilla's revision by demonstrating the benefit of additional training tokens.

### Architecture Components

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that LLaMA modifies with pre-normalization, SwiGLU, and RoPE.

- **Zhang & Sennrich (2019)** -- *Root Mean Square Layer Normalization.* Introduces RMSNorm, used for pre-normalization in LLaMA. Simpler and more efficient than LayerNorm.

- **Shazeer (2020)** -- *GLU Variants Improve Transformer.* Introduces SwiGLU and other gated linear unit variants for Transformer FFN layers. LLaMA uses SwiGLU with a 2/3 scaling factor on the hidden dimension.

- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the positional encoding used by LLaMA. Applied at each layer, encoding positions through rotations of query and key vectors.

### Baseline Models

- **Brown et al. (2020)** -- *GPT-3: Language Models Are Few-Shot Learners.* Primary comparison target. LLaMA-13B surpasses GPT-3 175B on most benchmarks. GPT-3 also inspired LLaMA's use of pre-normalization.

- **Chowdhery et al. (2022)** -- *PaLM: Scaling Language Modeling with Pathways.* PaLM 540B serves as the upper-bound comparison. LLaMA-65B approaches PaLM's performance at 8x fewer parameters. PaLM also inspired LLaMA's use of SwiGLU activations.

- **Rae et al. (2021)** -- *Scaling Language Models: Methods, Analysis & Insights from Training Gopher.* Gopher 280B serves as a comparison target, particularly on MMLU where its strong performance is attributed to extensive book data.

- **Zhang et al. (2022)** -- *OPT: Open Pre-trained Transformer Language Models.* Open-weight baseline. OPT-175B underperforms LLaMA despite matching GPT-3's architecture and scale, likely due to insufficient training tokens.

### Training Data and Tokenization

- **Wenzek et al. (2020)** -- *CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data.* The pipeline used to process and filter CommonCrawl, which constitutes 67% of LLaMA's training data.

- **Raffel et al. (2020)** -- *T5: Exploring the Limits of Transfer Learning.* Source of the C4 dataset (15% of training data).

- **Kudo & Richardson (2018)** -- *SentencePiece: A Simple and Language Independent Subword Tokenizer.* BPE tokenizer implementation used for LLaMA's vocabulary.

### Efficient Training

- **Lefaudeux et al. (2022)** -- *xformers: A Modular and Hackable Transformer Modelling Library.* Provides the efficient causal multi-head attention implementation used in LLaMA training.

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* The backward pass from FlashAttention is used in the xformers attention implementation adopted by LLaMA.

- **Rabe & Staats (2021)** -- *Self-Attention Does Not Need O(n^2) Memory.* The memory-efficient attention approach that inspired the xformers implementation used in LLaMA.

- **Korthikanti et al. (2022)** -- *Reducing Activation Recomputation in Large Transformer Models.* Model and sequence parallelism techniques used to reduce memory usage in LLaMA's distributed training.

### Instruction Finetuning

- **Chung et al. (2022)** -- *Scaling Instruction-Finetuned Language Models.* The instruction finetuning protocol and dataset used to train LLaMA-I. LLaMA-I outperforms Flan-PaLM-cont 62B (68.9 vs. 66.1 on MMLU).

### Safety and Bias Evaluation

- **Gehman et al. (2020)** -- *RealToxicityPrompts: Evaluating Neural Toxic Degeneration in Language Models.* The benchmark used to measure toxicity of LLaMA generations.

- **Nangia et al. (2020)** -- *CrowS-Pairs: A Challenge Dataset for Measuring Social Biases in Masked Language Models.* The benchmark used to measure social biases across 9 categories.

- **Rudinger et al. (2018)** -- *Gender Bias in Coreference Resolution.* The WinoGender benchmark used to measure gender bias in coreference resolution.

- **Lin et al. (2021)** -- *TruthfulQA: Measuring How Models Mimic Human Falsehoods.* The benchmark used to evaluate truthfulness and hallucination tendencies.
