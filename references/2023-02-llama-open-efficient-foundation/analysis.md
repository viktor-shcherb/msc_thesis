# LLaMA: Open and Efficient Foundation Language Models

**Authors:** Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, Guillaume Lample (Meta AI)
**Date:** February 2023, arXiv:2302.13971

---

## Core Research Problem

At the time of writing, the most capable large language models (GPT-3, Chinchilla, PaLM) were not publicly released, restricting reproducibility and downstream research. Meanwhile, Hoffmann et al. (2022) -- *Chinchilla* -- demonstrated that smaller models trained on more data can match the performance of larger models trained on fewer tokens, contradicting the prevailing paradigm of scaling model parameters with a fixed token budget. However, this insight had not been fully exploited in practice: most existing open models were either too small to be competitive (GPT-2, OPT-1.3B) or trained on insufficient data relative to their size (OPT-175B used 300B tokens; GPT-3 used 300B tokens). The core challenge was: **how to train a family of open-weight language models that match or exceed the performance of the best closed models by training smaller architectures on significantly more tokens, using only publicly available data.**

---

## Problem Solutions

LLaMA addresses the problem by training four models (7B, 13B, 33B, 65B parameters) on 1.0T--1.4T tokens of publicly available data, substantially exceeding the Chinchilla-optimal token count for each model size:

1. **More tokens than Chinchilla-optimal:** Rather than stopping at the compute-optimal point, LLaMA trains beyond it, trading additional training compute for better inference-time performance at each model size. The 7B model trains on 1.0T tokens -- roughly 7x the Chinchilla-optimal budget for its size.

2. **Publicly available training data only:** All training data comes from publicly accessible sources (CommonCrawl, C4, GitHub, Wikipedia, Gutenberg, ArXiv, StackExchange), enabling full reproducibility.

3. **Efficient Transformer architecture:** LLaMA adopts several architectural improvements over the original Transformer that had been validated independently: pre-normalization with RMSNorm, SwiGLU activations, and Rotary Positional Embeddings (RoPE).

---

## Approach Details

### Architecture

LLaMA uses a Transformer decoder (autoregressive, causal attention) with three modifications to the original architecture of Vaswani et al. (2017):

1. **Pre-normalization with RMSNorm.** Normalization is applied *before* each sub-layer (attention and feed-forward) rather than after, following Zhang & Sennrich (2019). RMSNorm (Zhang & Sennrich, 2019) is used instead of LayerNorm:

> RMSNorm(x) = x / sqrt(mean(x^2) + epsilon) * gamma

This improves training stability and was adopted by GPT-3 and subsequent models.

2. **SwiGLU activation function.** The feed-forward network uses the SwiGLU activation (Shazeer, 2020) instead of ReLU:

> FFN(x, W1, W2, W3) = (SiLU(xW1) ⊙ xW3) W2

where SiLU(x) = x * sigmoid(x) and ⊙ denotes element-wise multiplication. This introduces a third weight matrix W3 (gating), so the hidden dimension is set to (2/3) * 4d (rounded to the nearest multiple of 256) to maintain roughly the same parameter count as a standard 4d FFN with ReLU.

3. **Rotary Positional Embeddings (RoPE).** Absolute positional embeddings are replaced with RoPE (Su et al., 2021), which encodes position information by rotating query and key vectors in the attention mechanism:

> f(x_m, m) = R(m, theta) * x_m

where R(m, theta) is a block-diagonal rotation matrix with angles m * theta_d = m * b^(-2d/|D|) for dimension pair d and base frequency b = 10000. RoPE enables relative position awareness through the dot product of rotated queries and keys: the attention score between positions m and n depends only on the relative distance m - n.

Additional details:
- **No bias terms** in any linear layer.
- **Context length:** 2048 tokens.
- **Vocabulary:** 32,000 tokens using byte-pair encoding via SentencePiece (Kudo & Richardson, 2018). All numbers are split into individual digits. Unknown UTF-8 characters are decomposed into bytes.

### Model Configurations

| Model | Parameters | d_model | n_heads | n_layers | d_ff | Learning Rate | Batch Size | Training Tokens |
|---|---|---|---|---|---|---|---|---|
| LLaMA-7B | 6.7B | 4096 | 32 | 32 | 11008 | 3.0e-4 | 4M tokens | 1.0T |
| LLaMA-13B | 13.0B | 5120 | 40 | 40 | 13824 | 3.0e-4 | 4M tokens | 1.0T |
| LLaMA-33B | 32.5B | 6656 | 52 | 60 | 17920 | 1.5e-4 | 4M tokens | 1.4T |
| LLaMA-65B | 65.2B | 8192 | 64 | 80 | 22016 | 1.5e-4 | 4M tokens | 1.4T |

Head dimension is d_model / n_heads = 128 for all models.

### Training Data

All data is publicly available. After deduplication and filtering:

| Dataset | Sampling Proportion | Epochs | Disk Size |
|---|---|---|---|
| English CommonCrawl (CCNet) | 67.0% | 1.10 | 3.3 TB |
| C4 | 15.0% | 1.06 | 783 GB |
| GitHub | 4.5% | 0.64 | 328 GB |
| Wikipedia (20 languages) | 4.5% | 2.45 | 83 GB |
| Books (Gutenberg + Books3) | 4.5% | 2.23 | 85 GB |
| ArXiv | 2.5% | 1.06 | 92 GB |
| StackExchange | 2.0% | 1.03 | 78 GB |

CommonCrawl is processed with a CCNet pipeline: deduplication at line level, language classification with fastText, and quality filtering using a linear classifier trained to distinguish Wikipedia references from random CommonCrawl pages.

### Training Procedure

- **Optimizer:** AdamW (beta_1 = 0.9, beta_2 = 0.95)
- **Learning rate schedule:** Cosine decay to 10% of peak, with 2000 warmup steps.
- **Weight decay:** 0.1
- **Gradient clipping:** 1.0
- **Precision:** Mixed precision (bfloat16 for forward pass, float32 for accumulation)

### Efficient Implementation

- **Causal multi-head attention** using an efficient implementation from xformers (Lefaudeux et al., 2022) that avoids storing attention weights and does not compute masked entries.
- **Activation checkpointing** to reduce GPU memory by recomputing activations during the backward pass. Specifically, linear layer outputs (which are expensive in memory) are checkpointed, while attention computation outputs (which are cheap to recompute) are not.
- **Overlapping computation and communication** during FSDP-based distributed training.

Training cost for the 65B model: 1,022K GPU-hours on A100-80GB, approximately 21 days on 2048 GPUs. Each GPU processes ~380 tokens/sec. Total training carbon footprint estimated at 2638 tCO2eq.

### Experimental Setup

Models are evaluated on standard NLP benchmarks spanning commonsense reasoning, closed-book question answering, reading comprehension, mathematical reasoning, code generation, and multitask language understanding. Key benchmarks include BoolQ, PIQA, SIQA, HellaSwag, WinoGrande, ARC (Easy/Challenge), OpenBookQA, TriviaQA, Natural Questions, MMLU, HumanEval, MBPP, GSM8K, and MATH.

Baselines: GPT-3 175B (Brown et al., 2020), Chinchilla 70B (Hoffmann et al., 2022), PaLM 540B (Chowdhery et al., 2022), OPT 175B (Zhang et al., 2022), GPT-J 6B (Wang & Komatsuzaki, 2021).

### Key Results

**Commonsense reasoning (0-shot, except 25-shot for ARC):**

| Model | BoolQ | PIQA | HellaSwag | WinoGrande | ARC-e | ARC-c | OBQA |
|---|---|---|---|---|---|---|---|
| LLaMA-7B | 76.5 | 79.8 | 76.1 | 70.1 | 72.8 | 47.6 | 57.2 |
| LLaMA-13B | 78.1 | 80.1 | 79.2 | 73.0 | 74.8 | 52.5 | 56.4 |
| LLaMA-33B | 83.1 | 82.3 | 82.8 | 76.0 | 80.0 | 57.8 | 58.6 |
| LLaMA-65B | 85.3 | 82.8 | 84.2 | 77.0 | 81.4 | 56.0 | 60.2 |
| GPT-3 175B | 60.5 | 81.0 | 78.9 | 70.2 | 68.8 | 51.4 | -- |
| Chinchilla 70B | 83.7 | 81.8 | 80.8 | 74.9 | -- | 54.6 | -- |
| PaLM 540B | 88.0 | 82.3 | 83.4 | 77.0 | -- | 53.0 | -- |

**Multitask language understanding (MMLU, 5-shot):**

| Model | Humanities | STEM | Social Sciences | Other | Average |
|---|---|---|---|---|---|
| LLaMA-7B | 34.0 | 30.5 | 38.3 | 38.1 | 35.1 |
| LLaMA-13B | 45.0 | 35.8 | 53.8 | 53.3 | 46.9 |
| LLaMA-33B | 55.8 | 46.0 | 66.7 | 63.4 | 57.8 |
| LLaMA-65B | 61.8 | 51.7 | 72.9 | 67.4 | 63.4 |
| GPT-3 175B | 40.8 | 36.7 | 50.4 | 48.8 | 43.9 |
| Chinchilla 70B | 63.6 | 54.9 | 73.9 | 73.1 | 67.6 |
| PaLM 540B | 77.0 | 55.6 | 81.0 | 69.6 | 69.3 |

**Code generation (pass@1, 0-shot for HumanEval, 3-shot for MBPP):**

| Model | HumanEval | MBPP |
|---|---|---|
| LLaMA-7B | 10.5 | 17.7 |
| LLaMA-13B | 15.8 | 22.0 |
| LLaMA-33B | 21.7 | 30.2 |
| LLaMA-65B | 23.7 | 37.7 |
| PaLM 540B | 26.2 | 36.8 |

- **LLaMA-13B outperforms GPT-3 175B** on most benchmarks despite being >10x smaller (6.7B vs 175B effective parameters at inference).
- **LLaMA-65B is competitive with Chinchilla-70B and PaLM-540B** across most tasks, despite PaLM having 8x more parameters.
- On MMLU, LLaMA-65B (63.4) lags behind Chinchilla-70B (67.6) and PaLM-540B (69.3), suggesting knowledge-intensive tasks still benefit from larger models or more diverse training data.
- Training has not saturated: loss curves for the 7B model at 1.0T tokens show continued improvement, indicating further scaling of training tokens would yield gains.

### Scaling Behavior

The paper reports training loss as a function of compute budget (GPU-hours) across model sizes. The 33B and 65B models continue to improve throughout training and have not converged at their respective token budgets (1.4T). The 7B model also does not saturate at 1.0T tokens. This validates the paper's central premise: performance at a given inference budget is better served by training smaller models on more data than by training larger models on fewer tokens.

---

## Conclusions

1. **Smaller models trained on more data match larger models.** LLaMA-13B outperforms GPT-3 175B on most benchmarks, and LLaMA-65B is competitive with Chinchilla-70B and PaLM-540B, demonstrating that inference-time efficiency can be dramatically improved by investing more in training compute.

2. **Public data is sufficient for competitive performance.** All training data comes from publicly available sources, without any proprietary or filtered datasets. This enables full reproducibility and removes the data access barrier for the research community.

3. **Architectural choices matter at scale.** The combination of pre-normalization (RMSNorm), SwiGLU activations, and Rotary Positional Embeddings yields a robust architecture. These choices, each validated independently in prior work, combine to produce models that train stably and efficiently across a wide range of scales (7B--65B).

4. **RoPE as positional encoding standard.** LLaMA's adoption of RoPE (with base frequency b = 10000 and context length 2048) established the positional encoding configuration that subsequent context extension work (Position Interpolation, NTK-aware scaling, YaRN, DroPE) targets. The 2048-token context window became the baseline that motivated the entire RoPE context extension research direction.

5. **Training efficiency at scale.** The 65B model requires 1,022K GPU-hours on A100-80GB, with throughput of ~380 tokens/sec/GPU. The efficient implementation (xformers attention, activation checkpointing, overlapped computation/communication) enables training on 2048 GPUs.

6. **Foundation for open-weight ecosystem.** LLaMA established the architecture and weight format adopted by the majority of subsequent open-weight models (Alpaca, Vicuna, LongChat, CodeLlama, and the Llama 2/3 family), making it the de facto standard for open LLM research.

---

## Core References and Why They Are Referenced

### Scaling Laws and Training Strategy
- **Hoffmann et al. (2022)** -- *Chinchilla: Training Compute-Optimal Large Language Models.* Central motivation: Chinchilla shows that scaling tokens is as important as scaling parameters. LLaMA's entire training strategy follows from this insight, training models beyond the Chinchilla-optimal token budget to maximize inference-time performance.
- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Earlier scaling laws that Chinchilla revised. Kaplan et al. suggested scaling model size faster than data, which LLaMA contradicts by demonstrating the benefit of scaling tokens.

### Architecture Components
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that LLaMA modifies with pre-normalization, SwiGLU, and RoPE.
- **Zhang & Sennrich (2019)** -- *Root Mean Square Layer Normalization.* Introduces RMSNorm, used for pre-normalization in LLaMA. Simpler and more efficient than LayerNorm.
- **Shazeer (2020)** -- *GLU Variants Improve Transformer.* Introduces SwiGLU and other gated linear unit variants for Transformer FFN layers. LLaMA uses SwiGLU with a 2/3 scaling factor on the hidden dimension.
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the positional encoding used by LLaMA. Encodes positions through rotations of query and key vectors, enabling relative position awareness through the attention dot product.

### Baseline Models
- **Brown et al. (2020)** -- *GPT-3: Language Models Are Few-Shot Learners.* Primary comparison target. LLaMA-13B surpasses GPT-3 175B on most benchmarks.
- **Chowdhery et al. (2022)** -- *PaLM: Scaling Language Modeling with Pathways.* PaLM 540B serves as the upper-bound comparison. LLaMA-65B approaches PaLM's performance at 8x fewer parameters.
- **Zhang et al. (2022)** -- *OPT: Open Pre-trained Transformer Language Models.* Open-weight baseline. OPT-175B underperforms LLaMA despite matching GPT-3's architecture and scale.

### Training Data
- **Wenzek et al. (2020)** -- *CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data.* The pipeline used to process and filter CommonCrawl, which constitutes 67% of LLaMA's training data.
- **Raffel et al. (2020)** -- *T5: Exploring the Limits of Transfer Learning.* Source of the C4 dataset (15% of training data).
- **Kudo & Richardson (2018)** -- *SentencePiece: A Simple and Language Independent Subword Tokenizer.* BPE tokenizer used for LLaMA's 32K vocabulary.

### Efficient Training
- **Lefaudeux et al. (2022)** -- *xformers: A Modular and Hackable Transformer Modelling Library.* Provides the efficient causal multi-head attention implementation used in LLaMA.
- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* Related efficient attention approach; xformers implementation achieves similar benefits.

#### Cross-References in Available Papers

**How LLaMA is referenced in papers in this directory:**

- **PI (2023-06-pi-positional-interpolation):** LLaMA 7B through 65B are the experimental subjects. PI extends LLaMA's 2048-token context window to 8192--32768 tokens by linearly downscaling RoPE position indices. LLaMA 7B achieves 6.95 perplexity at 8192 tokens on PG-19 with PI, down from divergence with direct extrapolation.
- **NTK-aware (2023-06-rope-ntk):** Targets LLaMA models specifically. The title references LLaMA: "NTK-Aware Scaled RoPE allows LLaMA models to have extended (8k+) context size." Proposes changing the RoPE base frequency as an alternative to PI's position interpolation.
- **Landmark Attention (2023-12-landmark-attention-infinite-context):** Fine-tunes LLaMA 7B with landmark tokens to extend effective context from 2048 to 32K tokens. Base LLaMA 7B fails beyond ~3K tokens on passkey retrieval, while the fine-tuned version achieves 98% accuracy at 32K.
- **YaRN (2024-05-yarn-context-extension):** References LLaMA as [38], the original architecture providing the model family that YaRN targets. LLaMA's RoPE configuration (b = 10000, |D| = 128) and the alpha/beta frequency boundaries are used directly.
- **StreamingLLM (2024-05-attention-sinks-streaming):** Uses Llama-2 (LLaMA's successor) as a primary evaluation model. StreamingLLM's attention sink finding is first demonstrated on LLaMA-family architectures.
- **Lost in the Middle (2024-02-lost-in-the-middle):** References LLaMA as the base model for LongChat-13B (16K context).
- **L-Eval (2024-08-l-eval-standardized-evaluation):** Evaluates LLaMA and its derivatives (Vicuna, Longchat, NTK variants) as open-source baselines. References "Touvron et al. (2023a)" as the base model for many evaluated LCLMs.
- **LongBench (2024-08-longbench-bilingual-benchmark):** Evaluates LongChat and Vicuna variants fine-tuned from LLaMA.
- **DroPE (2025-12-drope-dropping-positional-embeddings):** Uses LLaMA-family architecture for recalibration experiments.
- **Effective Context Length (2025-04-effective-context-length-falls-short):** References "Touvron et al. (2023a)" as the architecture basis for TinyLlama pretraining experiments.
