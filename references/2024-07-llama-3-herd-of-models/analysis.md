---
title: "The Llama 3 Herd of Models"
authors: "Dubey, Jauhri, Pandey, Kadian, Al-Dahle, Letman, Mathur, Schelten, Yang, Fan, et al."
year: 2024
venue: "arXiv preprint 2407.21783"
paper_type: preprint
categories: ["model-release", "architecture", "context-extension", "long-context-evaluation"]
scope: ["open foundation models", "dense transformer scaling", "128K context extension", "grouped-query attention", "RoPE scaling", "multimodal integration", "tool use"]
benchmarks_used: ["mmlu", "gsm8k", "humaneval", "mbpp", "arc", "hellaswag", "winogrande", "piqa", "natural-questions", "triviaqa", "squad", "bbh", "agi-eval", "race", "boolq", "niah", "zeroscrolls", "infinitebench"]
models_introduced: ["llama-3-8b", "llama-3-70b", "llama-3.1-8b", "llama-3.1-70b", "llama-3.1-405b"]
models_evaluated: ["llama-2-7b", "llama-2-70b", "mistral-7b", "gpt-4", "gpt-4o", "claude-3.5-sonnet", "gemini-1.5-pro"]
key_claims:
  - id: C1
    claim: "Llama 3.1 405B performs competitively with GPT-4 and Claude 3.5 Sonnet across benchmarks, scoring 88.6% on MMLU (0-shot CoT) vs GPT-4o's 88.7%"
    evidence: "Table 2, Section 5"
    status: supported
  - id: C2
    claim: "Pre-training on 15.6T tokens with 3.8x10^25 FLOPs yields a 405B dense model that outperforms earlier models with more parameters (e.g., PaLM 540B)"
    evidence: "Section 3, Table 3"
    status: supported
  - id: C3
    claim: "Context length extension from 8K to 128K tokens via incremental training on ~800B tokens achieves 100% needle-in-a-haystack retrieval at all depths and context lengths"
    evidence: "Section 3.4.2, Figure 7"
    status: supported
  - id: C4
    claim: "Llama 3 405B achieves 95.2% on ZeroSCROLLS/QuALITY, matching GPT-4 (0125) and outperforming GPT-4o (90.5%)"
    evidence: "Table 2, Table 21"
    status: supported
  - id: C5
    claim: "Training the 405B model on 16K H100 GPUs achieves >90% effective training time despite 466 job interruptions in a 54-day period"
    evidence: "Section 3.3.3, Table 5"
    status: supported
  - id: C6
    claim: "Scaling law extrapolation with (alpha, A) = (0.53, 0.29) correctly predicts training a 402B model on 16.55T tokens as compute-optimal for 3.8x10^25 FLOPs"
    evidence: "Section 3.2, Figure 2"
    status: supported
  - id: C7
    claim: "Mixing 0.1% synthetic long-context SFT data with short-context data optimizes both long- and short-context performance; DPO on short-context data alone does not degrade long-context capabilities"
    evidence: "Section 4.3.4"
    status: supported
cross_references:
  - target: 2023-07-llama-2-open-foundation-chat
    type: extends
    detail: "Direct successor to Llama 2 with 8x more training data (15.6T vs 2T tokens), 128K context (vs 4K), 405B flagship model, and improved tokenizer (128K vocabulary)"
  - target: 2023-02-llama-open-efficient-foundation
    type: extends
    detail: "Third generation of LLaMA family, retaining decoder-only dense Transformer with RoPE, RMSNorm, SwiGLU but scaling to 405B parameters and 15.6T tokens"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Uses standard dense Transformer architecture with minor modifications (GQA, RMSNorm, SwiGLU, RoPE)"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Uses RoPE with increased base frequency theta=500,000 (vs 10,000 in Llama 2) to support 128K context"
  - target: 2024-05-attention-sinks-streaming
    type: extended-by
    detail: "Attention sink analysis applicable to Llama 3 models"
  - target: 2025-07-position-bias-transformers
    type: extended-by
    detail: "Position bias analysis conducted on Llama 3 models"
  - target: 2025-04-effective-context-length-falls-short
    type: extended-by
    detail: "Evaluates effective context length of Llama 3 models"
  - target: 2024-02-lost-in-the-middle
    type: extended-by
    detail: "Positional bias analysis methodology applicable to Llama 3's 128K context"
  - target: 2023-11-needle-in-a-haystack
    type: uses-benchmark
    detail: "Uses needle-in-a-haystack and multi-needle variants to validate 128K context extension"
  - target: 2023-12-zeroscrolls-zero-shot-long-text
    type: uses-benchmark
    detail: "Uses ZeroSCROLLS QuALITY for long-context evaluation"
  - target: 2024-08-infinitebench-long-context-evaluation
    type: uses-benchmark
    detail: "Uses InfiniteBench En.QA and En.MC for 100K+ token evaluation"
open_questions:
  - question: "Would training beyond 15.6T tokens continue to improve the 405B model, or has a data quality ceiling been reached?"
    addressed_by: null
  - question: "Can the multimodal compositional approach (cross-attention adapters) match jointly pre-trained multimodal models at scale?"
    addressed_by: null
  - question: "Does the 128K context extension maintain quality on tasks requiring reasoning over the full context, beyond simple retrieval?"
    addressed_by: 2025-04-effective-context-length-falls-short
  - question: "How does the 8K-to-128K incremental context extension compare to methods like YaRN or PI in terms of quality per compute?"
    addressed_by: null
---

# The Llama 3 Herd of Models

**Authors:** Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, et al. (Llama Team, AI @ Meta)
**Date:** July 2024, arXiv:2407.21783

---

## Core Research Problem

Despite the proliferation of large language models, the open-weight ecosystem lacked a model competitive with proprietary frontier systems (GPT-4, Claude 3.5 Sonnet, Gemini 1.5 Pro) across the full range of capabilities: general knowledge, coding, mathematics, reasoning, multilingual understanding, long-context processing, and tool use. Llama 2's largest model (70B) significantly trailed GPT-4 on most benchmarks, and its 4096-token context window was a practical limitation. Furthermore, scaling to hundreds of billions of parameters with dense architectures posed infrastructure challenges, and integrating multimodal capabilities (vision, speech) into language models typically required complex joint pre-training. The core challenge was: **how to train and release an open-weight dense Transformer model family that matches proprietary frontier models in quality while supporting 128K context, multilingual capabilities, and tool use.**

---

## Problem Solutions

Llama 3 addresses this through three strategies:

1. **Massive data and compute scaling.** Train 8B, 70B, and 405B parameter dense Transformers on approximately 15.6T tokens (8x more than Llama 2) using 3.8 x 10^25 FLOPs. Use scaling laws to determine compute-optimal model size and training duration.

2. **Incremental context extension.** Extend context from 8K to 128K tokens during the final pre-training stage through progressive increases in sequence length over ~800B tokens, using RoPE with base frequency theta = 500,000.

3. **Simple post-training with iterative refinement.** Apply multiple rounds of supervised fine-tuning (SFT), rejection sampling, and Direct Preference Optimization (DPO) rather than complex RLHF pipelines. Use synthetic data generation extensively for coding, math, tool use, and long-context tasks.

---

## Approach Details

### Architecture

Llama 3 uses a **standard dense Transformer** (decoder-only, autoregressive) with the following modifications from the original Transformer:

- **Grouped-Query Attention (GQA):** 8 key-value heads across all model sizes (vs. full MHA or size-dependent GQA in Llama 2). This reduces KV cache by 4x (8B), 8x (70B), and 16x (405B) compared to standard MHA.
- **Positional encoding:** RoPE with base frequency theta = 500,000 (increased from 10,000 in Llama 2). Xiong et al. (2023) showed this value effective for context lengths up to 32,768.
- **Normalization:** RMSNorm (pre-normalization).
- **Activation:** SwiGLU.
- **Tokenizer:** 128,000-token vocabulary using tiktoken (100K base tokens + 28K additional tokens for non-English languages). Compression rate improved from 3.17 to 3.94 characters per token on English data vs. Llama 2's 32K SentencePiece tokenizer.
- **Attention mask:** Document-level mask preventing cross-document attention within packed sequences, found important for long-context pre-training.

| Hyperparameter | 8B | 70B | 405B |
|---|---|---|---|
| Layers | 32 | 80 | 126 |
| Model Dimension | 4,096 | 8,192 | 16,384 |
| FFN Dimension | 14,336 | 28,672 | 53,248 |
| Attention Heads | 32 | 64 | 128 |
| Key/Value Heads | 8 | 8 | 8 |
| Peak Learning Rate | 3 x 10^-4 | 1.5 x 10^-4 | 8 x 10^-5 |
| Vocabulary Size | 128,000 | 128,000 | 128,000 |
| Positional Embeddings | RoPE (theta=500,000) | RoPE (theta=500,000) | RoPE (theta=500,000) |

(Table 3)

### Key Technical Components

#### Pre-Training Data

- **Total:** ~15T multilingual tokens from publicly available sources (knowledge cutoff end of 2023).
- **Composition:** ~50% general knowledge, ~25% mathematical/reasoning, ~17% code, ~8% multilingual.
- **Curation pipeline:** PII/safety filtering, custom HTML parser for text extraction, three-level deduplication (URL-level, document-level MinHash, line-level), heuristic filtering (n-gram coverage, KL divergence), model-based quality filtering (fasttext + RoBERTa classifiers trained on Llama 2 predictions).
- No Meta user data used.

#### Scaling Laws

The paper fits a power-law relation for compute-optimal training tokens:

> N*(C) = A * C^alpha

with fitted parameters **(alpha, A) = (0.53, 0.29)**. Extrapolation to 3.8 x 10^25 FLOPs predicts training a **402B parameter model on 16.55T tokens** as compute-optimal. The smaller 8B and 70B models are trained well beyond compute-optimal to trade training compute for inference efficiency.

#### Training Infrastructure (405B)

- **Hardware:** Up to 16K H100 GPUs (80GB HBM3, 700W TDP) from a cluster of 24K GPUs on Meta's Grand Teton platform.
- **Network:** RoCE fabric with 400 Gbps interconnects, three-layer Clos topology (3,072 GPUs per pod with full bisection bandwidth, 1:7 oversubscription between pods).
- **Storage:** Tectonic distributed file system, 240 PB, 2 TB/s sustained throughput.
- **Parallelism (4D):** Tensor Parallelism (TP=8) within nodes, Context Parallelism (CP=up to 16), Pipeline Parallelism (PP=16), Data Parallelism (FSDP, DP=8-128).
- **Numerical precision:** BF16 with FP32 gradient accumulation and FP32 reduce-scatter.
- **MFU:** 38-43% BF16 model FLOPs utilization depending on configuration.
- **Reliability:** >90% effective training time. In a 54-day snapshot, 466 job interruptions occurred (47 planned, 419 unexpected). GPU issues accounted for 58.7% of unexpected interruptions (Table 5).

#### Training Schedule (405B)

- **Optimizer:** AdamW (beta_1=0.9, beta_2=0.95, eps=1e-5).
- **LR schedule:** Cosine decay from 8 x 10^-5 to 8 x 10^-7 over 1,200,000 steps, with 8,000-step linear warmup.
- **Batch size ramp:** 4M tokens (seq len 4,096) → 8M tokens (seq len 8,192) after 252M tokens → 16M tokens after 2.87T tokens.
- **Total tokens:** 15.6T text tokens for the flagship model.

#### Annealing

During the final 40M tokens, learning rate is linearly annealed to 0, context length set to 128K, and data mix adjusted to upsample high-quality sources. **Polyak averaging** of checkpoints during annealing produces the final pre-trained model. Annealing on GSM8K/MATH training sets improved the 8B model by 24.0%/6.4% respectively; improvements on 405B were negligible.

#### Context Length Extension

Context length is extended from 8K to 128K tokens during the final pre-training stage (Section 3.4.2):

1. Context length is increased **incrementally** in six stages (for 405B), starting from 8K and ending at 128K.
2. At each stage, two criteria must be met before proceeding: (a) short-context evaluation performance has **recovered completely**, (b) the model **perfectly solves needle-in-a-haystack** up to that length.
3. Approximately **800B training tokens** are used for the long-context stage.
4. **Context Parallelism (CP)** enables training on 128K sequences: the input is partitioned into 2 x CP chunks, with the i-th CP rank receiving the i-th and (2 x CP - 1 - i)-th chunks for load balancing. An all-gather based method collects K and V tensors for computing attention on local Q chunks.
5. **Document attention mask** prevents cross-document attention within packed sequences, found important for long-context training.

Final long-context configuration (Table 4): 16,384 GPUs, TP=8, CP=16, PP=16, DP=8, sequence length=131,072, 380 TFLOPs/GPU, 38% BF16 MFU.

### Post-Training

Post-training uses six rounds of SFT followed by DPO (not PPO as in Llama 2):

- **SFT:** Learning rate 10^-5 over 8.5K-9K steps.
- **DPO:** Learning rate 10^-5, beta=0.1. Two modifications: (1) masking formatting tokens from loss, (2) NLL regularization with coefficient 0.2 on chosen sequences.
- **Rejection sampling:** K=10-30 samples per prompt, selected by reward model. Data from the 405B model used to train smaller models (distillation).
- **Model averaging** applied at each RM, SFT, and DPO stage.
- **Synthetic data generation** used extensively for coding (~1M synthetic dialogs with execution feedback, ~1.2M backtranslation dialogs), math (step-wise reasoning traces, MCTS with stepwise reward models), tool use, and long-context tasks.

#### Long-Context Post-Training

- Synthetic SFT data generated for QA (documents split into 8K chunks), summarization (hierarchical), and long-context code reasoning.
- Synthetic samples categorized by length: 16K, 32K, 64K, 128K tokens.
- **0.1% synthetic long-context data** mixed with short-context data optimizes both.
- DPO on short-context data alone does **not** degrade long-context performance (Section 4.3.4).

### Experimental Setup

**Pre-training evaluation:** Standard benchmarks across categories: reading comprehension (SQuAD V2, QuAC, RACE), code (HumanEval, MBPP), commonsense (CSQA, PiQA, SiQA, OpenBookQA, WinoGrande), math/reasoning (GSM8K, MATH, ARC-C, DROP), adversarial, long context (QuALITY, many-shot GSM8K), aggregate (MMLU, MMLU-Pro, AGIEval, BBH).

**Post-training evaluation:** MMLU, MMLU-Pro, IFEval, GSM8K, MATH, GPQA, ARC-C, HumanEval, MBPP, MGSM, Nexus, BFCL, ZeroSCROLLS, NIAH, InfiniteBench.

**Human evaluation:** ~7,000 prompts spanning 6 single-turn and 3 multi-turn capabilities, ~10% easy / ~30% medium / ~60% hard.

### Key Results

**Post-trained models on key benchmarks (Table 2):**

| Benchmark | Llama 3 8B | Llama 3 70B | Llama 3 405B | GPT-4 (0125) | GPT-4o | Claude 3.5 Sonnet |
|---|---|---|---|---|---|---|
| MMLU (0-shot, CoT) | 73.0 | 86.0 | 88.6 | 85.4 | 88.7 | 88.3 |
| MMLU-Pro (5-shot, CoT) | 48.3 | 66.4 | 73.3 | 64.8 | 74.0 | 77.0 |
| IFEval | 80.4 | 87.5 | 88.6 | 84.3 | 85.6 | 88.0 |
| HumanEval (0-shot) | 72.6 | 80.5 | 89.0 | 86.6 | 90.2 | 92.0 |
| GSM8K (8-shot, CoT) | 84.5 | 95.1 | 96.8 | 94.2 | 96.1 | 96.4 |
| MATH (0-shot, CoT) | 51.9 | 68.0 | 73.8 | 64.5 | 76.6 | 71.1 |
| ARC-C (0-shot) | 83.4 | 94.8 | 96.9 | 96.4 | 96.7 | 96.7 |
| GPQA (0-shot, CoT) | 32.8 | 46.7 | 51.1 | 41.4 | 53.6 | 59.4 |
| MGSM (0-shot, CoT) | 68.9 | 86.9 | 91.6 | 85.9 | 90.5 | 91.6 |

**Long-context benchmarks (Table 21):**

| Benchmark | Llama 3 8B | Llama 3 70B | Llama 3 405B | GPT-4 (0125) | GPT-4o |
|---|---|---|---|---|---|
| ZeroSCROLLS/QuALITY (EM) | 81.0 | 90.5 | 95.2 | 95.2 | 90.5 |
| InfiniteBench En.MC (Acc) | 65.1 | 78.2 | 83.4 | 72.0 | 82.5 |
| Multi-needle (Recall) | 98.8 | 97.5 | 98.1 | 100.0 | 100.0 |
| InfiniteBench En.QA (F1) | 27.1 | 36.7 | 30.5 | 15.7 | 19.1 |

- Llama 3 405B matches GPT-4 on QuALITY (95.2%) and outperforms it on InfiniteBench En.MC (83.4% vs 72.0%) and En.QA (30.5% vs 15.7%).
- All Llama 3 models achieve near-perfect needle-in-a-haystack retrieval (>97.5%).

**Pre-trained models on aggregate benchmarks (Table 13):**

| Model | MMLU | MMLU-Pro | AGIEval | BBH |
|---|---|---|---|---|
| Llama 3 8B | 66.7 | 37.1 | 47.8 | 64.2 |
| Llama 3 70B | 79.3 | 53.8 | 64.6 | 81.6 |
| Llama 3 405B | 85.2 | 61.6 | 71.6 | 85.9 |
| GPT-4 | 86.4 | -- | -- | -- |
| Gemini Ultra | 83.7 | -- | -- | 83.6 |

**Human evaluation (Figure 17, 405B vs competitors, excluding ties):**

| Competitor | Category | Win | Loss |
|---|---|---|---|
| GPT-4 | English | 24.1% | 23.6% |
| GPT-4 | Coding | 28.0% | 24.2% |
| GPT-4o | English | 22.1% | 24.8% |
| GPT-4o | Coding | 22.0% | 28.0% |
| Claude 3.5 Sonnet | English | 28.0% | 20.5% |
| Claude 3.5 Sonnet | Coding | 22.4% | 28.5% |

Llama 3 405B is roughly at parity with GPT-4 on human evaluations but trails GPT-4o and Claude 3.5 Sonnet, particularly on reasoning and coding.

### Contamination Analysis

Novel contamination detection applied to pre-training data (Table 15). Key findings:

| Benchmark | Contamination % | Perf. gain 405B |
|---|---|---|
| AGIEval | 98% | 16.3 |
| BBH | 95% | 41.0 |
| HellaSwag | 85% | 14.3 |
| GSM8K | 41% | 1.3 |
| MATH | 1% | -0.2 |
| SQuAD | 0% | 0.0 |

High contamination in AGIEval and BBH warrants caution interpreting those results. GSM8K and MATH show minimal contamination impact despite GSM8K having 41% contaminated samples.

### FP8 Inference Quantization

Applied to feedforward network layers (~50% of inference compute). Self-attention layers are not quantized. Three mitigations: no quantization in first/last layers, dynamic scaling factors upper-bounded to 1200, row-wise quantization. FP8 achieves up to **50% throughput improvement** during pre-fill and fits the 405B model on a **single node** (vs. 2 nodes for BF16), providing a 2x throughput advantage.

---

## Limitations and Failure Modes

The paper acknowledges the following limitations:

1. **Trailing proprietary models on reasoning and coding.** Human evaluations show Llama 3 405B loses to GPT-4o on reasoning (16.8% win vs 30.1% loss) and coding (22.0% win vs 28.0% loss). GPQA scores trail Claude 3.5 Sonnet by 8.3 points (51.1% vs 59.4%).

2. **Multilingual gap.** Despite improved multilingual support, Llama 3 405B trails GPT-4o on multilingual MMLU (83.2% vs 85.5%) and loses on multilingual human evaluations against GPT-4o (17.4% win vs 34.7% loss).

3. **High contamination on some benchmarks.** AGIEval (98%), BBH (95%), and HellaSwag (85%) show high contamination rates with substantial performance gains on contaminated samples, complicating interpretation.

4. **Multimodal models not released.** Vision and speech capabilities are described as "still under active development and not yet ready for release." Image pre-training learning rate settings from small-scale experiments did not generalize to long training schedules. Numerical instabilities arose with BF16 gradient accumulation after adding the image encoder.

5. **Verbatim memorization scales with model size.** Average 50-gram verbatim memorization rates increase from 0.26% (8B) to 0.60% (70B) to 1.13% (405B) for English (Table 24).

6. **File upload capability gap.** Human evaluation of code execution shows Llama 3 405B loses significantly to GPT-4o on file upload tasks (22.9% win vs 64.2% loss; Figure 16).

7. **Dense architecture trade-off.** The paper notes that while Llama 3 outperforms MoE models like Mixtral, "there remain numerous trade offs in terms of training and inference efficiency" with dense architectures at this scale.

---

## Conclusions

### Contributions

1. **Largest open-weight dense Transformer.** The 405B model with 128K context is the largest publicly available dense Transformer, trained on 15.6T tokens using 3.8 x 10^25 FLOPs. It performs competitively with GPT-4 across standard benchmarks (MMLU 88.6% vs 85.4%, GSM8K 96.8% vs 94.2%; Table 2).

2. **Validated compute-optimal scaling for dense models.** Scaling law extrapolation with (alpha, A) = (0.53, 0.29) correctly predicts the 405B/16.55T configuration. Smaller models trained beyond compute-optimal effectively trade training compute for inference efficiency (Section 3.2).

3. **Incremental context extension to 128K tokens.** Six-stage progressive extension from 8K to 128K over ~800B tokens achieves near-perfect needle-in-a-haystack retrieval and 95.2% on ZeroSCROLLS/QuALITY, matching GPT-4 (Section 3.4.2, Table 21).

4. **Simple post-training outperforms complex pipelines.** SFT + rejection sampling + DPO (without PPO) across six rounds, combined with extensive synthetic data generation, produces competitive results with less complexity than Llama 2's RLHF pipeline (Section 4).

5. **Compositional multimodal integration.** Cross-attention adapters for vision (~100B additional parameters for 405B) and speech (~100M adapter parameters) enable modality integration without degrading text performance and without joint pre-training. Vision model outperforms GPT-4V on all benchmarks tested (Table 29).

6. **Comprehensive training infrastructure documentation.** Detailed reporting of 4D parallelism strategies, failure analysis (58.7% GPU-related), and reliability engineering (>90% effective training time) for 16K H100 GPU training (Section 3.3).

### Implications

1. **Dense architectures remain competitive at 405B scale.** Despite the trend toward MoE, Llama 3's dense architecture matches or exceeds MoE models (Mixtral 8x22B) on quality, though at higher inference cost. The paper suggests dense models are not the limiting factor.

2. **Data quality and quantity are the primary scaling lever.** The 8x increase in training data (15.6T vs 2T) and improved curation drove larger gains than architectural changes, consistent with the general trend of "straightforward methods at ever increasing scales."

3. **Open-weight models can match proprietary frontier models.** Llama 3 405B achieves approximate parity with GPT-4 and narrows the gap to GPT-4o and Claude 3.5 Sonnet, though deficits remain on reasoning and multilingual tasks. This is speculative as proprietary model comparisons depend on evaluation methodology.

4. **Context extension through continued pre-training is effective but costly.** The ~800B token investment for 8K→128K extension is substantial but achieves robust long-context performance without architectural changes to the attention mechanism.

---

## Key Claims

1. **Llama 3 405B matches GPT-4 on MMLU and outperforms it on several benchmarks.** MMLU 0-shot CoT: 88.6% vs 85.4%; GSM8K: 96.8% vs 94.2%; ARC-C: 96.9% vs 96.4%; IFEval: 88.6% vs 84.3%. Evidence: Table 2. Status: **supported**.

2. **Pre-training on 15.6T tokens with compute-optimal scaling produces a 405B model outperforming larger prior models.** Despite having fewer parameters than PaLM 540B, Llama 3 405B outperforms it due to better scaling laws. Evidence: Section 3, 9.1. Status: **supported**.

3. **Incremental context extension from 8K to 128K achieves 100% NIAH retrieval.** Six-stage progressive extension over ~800B tokens, with validation at each stage. Evidence: Section 3.4.2, Figure 7. Status: **supported**.

4. **Llama 3 405B achieves 95.2% on ZeroSCROLLS/QuALITY (128K context).** Matches GPT-4 (0125) and outperforms GPT-4o (90.5%) and Claude 3.5 Sonnet (90.5%). Evidence: Table 2, Table 21. Status: **supported**.

5. **>90% effective training time achieved at 16K GPU scale.** Despite 419 unexpected interruptions in 54 days (78% hardware-related, 58.7% GPU-specific). Evidence: Section 3.3.3, Table 5. Status: **supported**.

6. **0.1% synthetic long-context data suffices for post-training.** Mixing this proportion with short-context data optimizes both long- and short-context performance. DPO on short-context data alone does not degrade long-context capabilities. Evidence: Section 4.3.4. Status: **supported**.

7. **Llama 3 405B trails GPT-4o and Claude 3.5 Sonnet on human evaluations.** Loses on reasoning (16.8% vs 30.1% against GPT-4o), coding (22.0% vs 28.0%), and multilingual (17.4% vs 34.7%). Evidence: Figure 17. Status: **supported**.

---

## Open Questions

1. **Data scaling ceiling.** Would continued training beyond 15.6T tokens improve 405B performance, or has data quality become the bottleneck? The paper does not report training loss saturation behavior.

2. **Dense vs. MoE at 405B+ scale.** The paper argues dense architectures are competitive but acknowledges inference efficiency trade-offs. Whether MoE would achieve better quality per inference FLOP at this scale is unresolved.

3. **Effective context utilization at 128K.** While NIAH retrieval is near-perfect, whether the model can effectively reason over information distributed throughout a 128K context (not just retrieve it) remains unclear. Partially addressed by effective context length evaluations (2025-04-effective-context-length-falls-short).

4. **Context extension compute trade-off.** The ~800B token investment for 8K→128K extension is substantial. How this compares to post-hoc methods (YaRN, PI) in quality per compute is not analyzed.

5. **Multimodal integration scalability.** The compositional approach with cross-attention adapters adds ~100B parameters for vision at 405B scale. Whether this scales efficiently to higher resolutions and more modalities is unclear, and the models remain unreleased.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The base Transformer architecture that Llama 3 retains as a dense decoder-only model.
- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Provides RoPE, used with increased base frequency theta=500,000 for 128K context support.

### Direct Predecessors

- **Touvron et al. (2023a)** -- *LLaMA: Open and Efficient Foundation Language Models.* First-generation open-weight LLaMA establishing the architecture (RMSNorm, SwiGLU, RoPE).
- **Touvron et al. (2023b)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Direct predecessor with 2T tokens and 4K context. Llama 3 extends to 15.6T tokens, 128K context, and 405B parameters.

### Scaling Laws

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Foundational scaling law framework.
- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models (Chinchilla).* Compute-optimal training framework that Llama 3's scaling law extrapolation builds on.

### Context Extension

- **Xiong et al. (2023)** -- *Effective Long-Context Scaling of Foundation Models.* Showed RoPE theta=500,000 effective for context lengths up to 32,768, informing Llama 3's choice.

### Long-Context Evaluation

- **Kamradt (2023)** -- *Needle-in-a-Haystack test.* Used to validate context extension at each incremental stage.
- **Shaham et al. (2023)** -- *ZeroSCROLLS.* Long-text understanding benchmark used for evaluation.
- **Zhang et al. (2024)** -- *InfiniteBench.* 100K+ token evaluation benchmark.

### Post-Training

- **Rafailov et al. (2023)** -- *Direct Preference Optimization.* DPO replaces PPO from Llama 2's RLHF pipeline as the primary alignment method.

### Competing Models

- **OpenAI (2023)** -- *GPT-4 Technical Report.* Primary comparison target for flagship model.
- **Jiang et al. (2024)** -- *Mixtral of Experts.* MoE model compared against Llama 3's dense approach.
- **Chowdhery et al. (2023)** -- *PaLM: Scaling Language Modeling with Pathways.* Larger (540B) but less performant model, demonstrating Llama 3's scaling efficiency.
