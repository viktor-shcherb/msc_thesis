---
title: "Gemma 3 Technical Report"
authors: "Gemma Team"
year: 2025
venue: "arXiv preprint 2503.19786"
paper_type: preprint
categories: ["model-release", "architecture", "context-extension", "long-context-evaluation", "attention-efficiency"]
scope: ["open multimodal models", "128K context", "local-global attention interleaving", "knowledge distillation", "KV cache efficiency", "vision-language"]
benchmarks_used: ["mmlu", "mmlu-pro", "gsm8k", "math-hendrycks", "humaneval", "mbpp", "gpqa", "hellaswag", "piqa", "winogrande", "arc", "bbh", "triviaqa", "natural-questions", "ruler", "mmmu"]
models_introduced: ["gemma-3-1b", "gemma-3-4b", "gemma-3-12b", "gemma-3-27b"]
models_evaluated: ["gemma-7b", "llama-3.1-405b", "qwen2.5-72b", "deepseek-v3", "gemini-1.5-pro", "gemini-2.0-flash"]
key_claims:
  - id: C1
    claim: "5:1 local-to-global attention layer interleaving reduces KV cache memory overhead from 60% to less than 15% at 32K context with minimal perplexity impact"
    evidence: "Figure 3, Figure 5, Section 5.2"
    status: supported
    scope: "text-only 2B model ablations"
    magnitude: "~45 percentage point reduction in KV cache overhead"
  - id: C2
    claim: "Gemma 3 27B IT achieves Elo 1338 on Chatbot Arena, ranking 9th overall and above DeepSeek-V3 (1318), LLaMA 3 405B (1269), and Qwen2.5-72B (1257)"
    evidence: "Table 5, Section 4.1"
    status: supported
    scope: "preliminary results as of March 8, 2025"
  - id: C3
    claim: "Gemma 3 models memorize long-form text at significantly lower rates than prior Gemma and Gemini models"
    evidence: "Figure 9, Section 6"
    status: supported
    scope: "exact and approximate memorization with 50-token prefix/suffix"
  - id: C4
    claim: "Gemma 3 4B IT is competitive with Gemma 2 27B IT, and Gemma 3 27B IT is comparable to Gemini 1.5 Pro across benchmarks"
    evidence: "Table 6, Abstract"
    status: supported
    scope: "zero-shot IT benchmarks"
  - id: C5
    claim: "Sliding window size can be reduced to 1024 tokens without significant perplexity impact when using 5:1 local-to-global interleaving"
    evidence: "Figure 4, Section 5.2"
    status: supported
    scope: "2B text-only model ablations"
  - id: C6
    claim: "Pan & Scan improves DocVQA by +4.8 to +8.2 points and InfoVQA by +12.9 to +17.0 points by enabling native aspect ratio and resolution handling"
    evidence: "Table 8, Section 5.5"
    status: supported
    scope: "4B and 27B models on validation sets"
  - id: C7
    claim: "RoPE rescaling with factor 8 enables 128K context after 32K pre-training, with perplexity generalizing to 128K but degrading beyond"
    evidence: "Figure 7, Section 5.3"
    status: supported
    scope: "4B, 12B, 27B models"
cross_references:
  - target: 2024-03-gemma-open-models
    type: extends
    detail: "Third generation of Gemma family, adding multimodality, 128K context, and 5:1 local-global attention interleaving"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Decoder-only Transformer with GQA, RoPE, RMSNorm, and novel local-global attention interleaving"
  - target: 2024-10-ruler-context-size
    type: uses-benchmark
    detail: "Uses RULER for long-context evaluation at 32K and 128K lengths"
  - target: 2024-05-yarn-context-extension
    type: complementary
    detail: "Different approach to context extension; Gemma 3 uses RoPE rescaling with increased base frequency (10K to 1M for global layers)"
  - target: 2025-04-kimi-vl-technical-report
    type: concurrent
    detail: "Both are 2025 multimodal models with 128K context; Kimi-VL uses MoE with 2.8B activated parameters while Gemma 3 uses dense local-global interleaving"
open_questions:
  - question: "How does the 5:1 local-global interleaving affect tasks requiring multi-hop reasoning across the full 128K context?"
    addressed_by: null
  - question: "Would the local-global attention pattern transfer to MoE architectures?"
    addressed_by: null
  - question: "Can the significantly reduced memorization rates be attributed to specific architectural or training choices?"
    addressed_by: null
---

# Gemma 3 Technical Report

**Authors:** Gemma Team (Google DeepMind)
**Date:** March 2025, arXiv:2503.19786

---

## Core Research Problem

Open language models face a fundamental tension between capability and efficiency at deployment scale. Previous Gemma models supported only 8K context and lacked vision capabilities, limiting their applicability. Extending context to 128K tokens with standard global attention causes the KV cache to grow linearly with sequence length, creating memory bottlenecks that prevent deployment on consumer hardware. Additionally, multimodal capability requires integrating vision encoders without degrading text performance. The core challenge was: **how to add multimodality and 128K context to lightweight open models while maintaining efficiency for consumer hardware deployment.**

---

## Problem Solutions

Gemma 3 addresses these challenges through three architectural and training innovations:

1. **5:1 local-to-global attention interleaving.** Alternate 5 local sliding window attention layers (1024-token span) with 1 global attention layer to reduce KV cache memory from ~60% overhead to <15% at 32K context.

2. **RoPE frequency scaling for long context.** Increase global attention RoPE base frequency from 10K to 1M while keeping local layers at 10K, enabling 128K context through positional interpolation after 32K pre-training.

3. **Frozen vision encoder with Pan & Scan.** Use a shared 400M SigLIP encoder (frozen during training) with adaptive windowing at inference to handle varying aspect ratios and resolutions.

---

## Approach Details

### Architecture

Gemma 3 uses a **decoder-only Transformer** with the following modifications:

- **Grouped-Query Attention (GQA):** Same as Gemma 2.
- **Normalization:** RMSNorm with post-norm and pre-norm.
- **QK-norm:** Replaces soft-capping from Gemma 2 (inspired by Dehghani et al., 2023; Wortsman et al., 2023; Chameleon Team, 2024).
- **5:1 local-global interleaving:** 5 local sliding window layers (1024-token span) followed by 1 global attention layer, starting with a local layer.
- **RoPE base frequency:** 1M for global layers (up from 10K), 10K for local layers.

| Model | Vision Encoder | Embedding Params | Non-embedding Params |
|-------|----------------|------------------|----------------------|
| 1B | 0 | 302M | 698M |
| 4B | 417M | 675M | 3,209M |
| 12B | 417M | 1,012M | 10,759M |
| 27B | 417M | 1,416M | 25,600M |

(Table 1)

#### Vision Modality

- **Vision encoder:** 400M SigLIP variant (Zhai et al., 2023), frozen during training, shared across 4B, 12B, 27B models.
- **Input resolution:** 896 x 896 pixels.
- **Output compression:** 256 image tokens per image via average pooling.
- **Pan & Scan (P&S):** Inference-time adaptive windowing that segments images into non-overlapping crops, resizes each to 896x896, and passes to encoder. Handles varying aspect ratios and high-resolution images. Can be disabled for faster inference.

### Key Technical Components

#### Local-Global Attention Interleaving

The 5:1 local-to-global ratio significantly reduces KV cache memory:

| Configuration | KV Cache Overhead at 32K |
|---------------|-------------------------|
| Global only | ~60% |
| 1:1, sw=4096 (Gemma 2) | ~35% |
| 1:3, sw=1024 | <15% |

(Figure 5)

Ablations show minimal perplexity impact when changing local-to-global ratio from 1:1 to 7:1 (Figure 3), and sliding window can be reduced from 4096 to 512 with minimal perplexity degradation (Figure 4).

#### Long Context Extension

Instead of training with 128K sequences from scratch:

1. Pre-train with 32K sequences.
2. Apply RoPE rescaling with factor 8 at end of pre-training.
3. Increase global attention RoPE base frequency from 10K to 1M.

Models generalize to 128K context but degrade rapidly beyond (Figure 7).

### Pre-Training

- **Training tokens:** 14T (27B), 12T (12B), 4T (4B), 2T (1B).
- **Tokenizer:** Gemini 2.0 SentencePiece tokenizer (262K vocabulary), more balanced for non-English languages.
- **Distillation:** Sample 256 logits per token weighted by teacher probabilities; student learns teacher distribution via cross-entropy loss.
- **Data filtering:** Quality reweighting inspired by Sachdeva et al. (2024), evaluation set decontamination, PII filtering.

#### Training Infrastructure

| Model | TPU Type | #Chips | Data Shards | Seq Shards | Replicas |
|-------|----------|--------|-------------|------------|----------|
| 1B | TPUv5e | 512 | 16 | 16 | 2 |
| 4B | TPUv5e | 2048 | 16 | 16 | 8 |
| 12B | TPUv4 | 6144 | 16 | 16 | 24 |
| 27B | TPUv5p | 6144 | 24 | 8 | 32 |

(Table 2)

### Post-Training

Post-training uses:

1. **Knowledge distillation** from large IT teacher (Agarwal et al., 2024; Hinton et al., 2015).
2. **RL finetuning** based on improved BOND (Sessa et al., 2024), WARM (Rame et al., 2024b), and WARP (Rame et al., 2024a).

**Reward functions:** Weight-averaged reward models trained on human feedback, code execution feedback (Gehring et al., 2024), ground-truth rewards for math problems (DeepSeek-AI, 2025; Lambert et al., 2024).

### Quantization Aware Training

Quantized checkpoints provided in three formats:

| Model | bf16 | Int4 | Int4 (blocks=32) | SFP8 |
|-------|------|------|------------------|------|
| 1B | 2.0 GB | 0.5 GB | 0.7 GB | 1.0 GB |
| 4B | 8.0 GB | 2.6 GB | 2.9 GB | 4.4 GB |
| 12B | 24.0 GB | 6.6 GB | 7.1 GB | 12.4 GB |
| 27B | 54.0 GB | 14.1 GB | 15.3 GB | 27.4 GB |

(Table 3, weights only)

### Key Results

#### Chatbot Arena (Table 5)

Gemma 3 27B IT achieves **Elo 1338** (rank 9), above:
- DeepSeek-V3 (1318, 671B/37B MoE)
- LLaMA 3 405B (1269)
- Qwen2.5-72B (1257)
- Gemma 2 27B (1220)

#### IT Model Benchmarks (Table 6)

| Benchmark | Gemma 2 27B | Gemma 3 27B | Gemini 1.5 Pro | Gemini 2.0 Pro |
|-----------|-------------|-------------|----------------|----------------|
| MMLU-Pro | 56.9 | 67.5 | 75.8 | 79.1 |
| MATH | 55.6 | 89.0 | 86.5 | 91.8 |
| HiddenMath | 14.8 | 60.3 | 52.0 | 65.2 |
| GSM8K (implied) | - | 95.9 | - | - |
| Global MMLU-Lite | 68.6 | 75.1 | 80.8 | 86.5 |
| MMMU (val) | - | 64.9 | 65.9 | 72.7 |

#### Long Context (Table 15)

| Benchmark | Context | 4B IT | 12B IT | 27B IT |
|-----------|---------|-------|--------|--------|
| RULER | 32K | 61.4 | 80.3 | 91.1 |
| RULER | 128K | 46.8 | 57.1 | 66.0 |
| MRCR | 32K | 49.8 | 53.7 | 63.2 |
| MRCR | 128K | 44.6 | 49.8 | 59.3 |

#### Vision (Table 8, with P&S)

| Benchmark | 4B | 27B |
|-----------|-----|-----|
| DocVQA | 81.0 | 90.4 |
| InfoVQA | 57.0 | 76.4 |
| TextVQA | 60.8 | 70.2 |

---

## Limitations and Failure Modes

1. **Long context degradation beyond 128K.** Models generalize to 128K but rapidly degrade at longer contexts (Figure 7). No evaluation beyond 128K.

2. **1B model lacks vision.** The smallest model has no vision encoder and only 32K context.

3. **RULER/MRCR drop at 128K.** RULER 128K performance drops significantly from 32K (e.g., 27B IT: 91.1% at 32K vs 66.0% at 128K; Table 15).

4. **Contamination risk acknowledged.** Despite decontamination techniques, "there is always a risk of contamination of these probes, making more definitive conclusions harder to assess" (Section 5.1).

5. **Chatbot Arena numbers preliminary.** Elo scores are "preliminary results received on March 8, 2025" (Table 5 caption).

### Scope and Comparability

- **What was not tested:** Models larger than 27B; dense models with full global attention as baseline at 128K; MoE architectures.
- **Comparability notes:** Direct comparison with external models not provided due to different evaluation settings; paper encourages following third-party leaderboards.

---

## Conclusions

### Contributions

1. **KV cache efficient long context via local-global interleaving.** The 5:1 local-to-global ratio with 1024-token sliding window reduces KV cache overhead from ~60% to <15% at 32K context with minimal perplexity impact (Figure 5, Section 5.2).

2. **128K context open models.** Gemma 3 4B, 12B, 27B support 128K context through RoPE rescaling (factor 8) and increased base frequency (1M for global layers), achieving 91.1% on RULER 32K and 66.0% on RULER 128K for the 27B IT model.

3. **Multimodal capability with efficient integration.** Shared frozen 400M SigLIP encoder with 256-token compression per image and Pan & Scan for aspect ratio handling, with P&S providing +4.8 to +17.0 point improvements on document understanding tasks (Table 8).

4. **Significantly reduced memorization.** Gemma 3 models memorize long-form text at much lower rates than prior Gemma and Gemini models (Figure 9), with no personal information detected in memorized outputs.

5. **Strong performance at smaller scale.** Gemma 3 27B IT achieves Elo 1338 on Chatbot Arena, outperforming much larger models including DeepSeek-V3 (671B/37B), LLaMA 3 405B, and Qwen2.5-72B (Table 5).

### Implications

1. **Local-global interleaving may enable practical long-context deployment.** The dramatic KV cache reduction suggests dense models can support long context on consumer hardware without sparse attention approximations. However, this is demonstrated only at 32K context in ablations.

2. **Distillation from larger teachers effective for longer training.** Ablations show smaller teachers are better for short training but larger teachers become better for longer training (Figure 8), contrary to some prior findings.

3. **Vision integration without degrading text performance is feasible.** Freezing the vision encoder during training preserves text capabilities while adding multimodal understanding, though this approach may limit vision-language integration depth.

---

## Key Claims

1. **5:1 local-global interleaving reduces KV cache overhead with minimal quality loss.** From ~60% to <15% at 32K context (Figure 5). Perplexity impact is "minimal" even with 7:1 ratio (Figure 3). Evidence: Figures 3-5. Status: **supported**. Scope: 2B text-only ablations.

2. **Gemma 3 27B IT ranks 9th on Chatbot Arena with Elo 1338.** Above DeepSeek-V3 (1318), LLaMA 3 405B (1269), Qwen2.5-72B (1257), and 118 Elo points above Gemma 2 27B (1220). Evidence: Table 5. Status: **supported**. Scope: Preliminary results as of March 8, 2025.

3. **Gemma 3 models memorize at significantly lower rates than prior models.** Log-scale improvement visible in Figure 9; no personal information detected in memorized outputs. Evidence: Figure 9, Section 6. Status: **supported**. Scope: Exact and approximate memorization with 50-token prefix/suffix.

4. **Pan & Scan improves document understanding tasks substantially.** +4.8 to +8.2 on DocVQA, +12.9 to +17.0 on InfoVQA. Evidence: Table 8. Status: **supported**. Scope: 4B and 27B models on validation sets.

5. **RoPE rescaling enables 128K context after 32K pre-training.** Models generalize to 128K but degrade beyond. Evidence: Figure 7, Section 5.3. Status: **supported**. Scope: 4B, 12B, 27B models.

6. **Gemma 3 27B IT achieves 89.0% on MATH, outperforming Gemini 1.5 Pro (86.5%).** Evidence: Table 6. Status: **supported**. Scope: Zero-shot IT evaluation.

---

## Open Questions

1. **Multi-hop reasoning at 128K.** How well can models reason over information distributed throughout the full 128K context, not just retrieve it? The RULER and MRCR drops from 32K to 128K (Table 15) suggest degradation but the nature of failure modes is not analyzed.

2. **Local-global pattern for MoE.** Would the 5:1 interleaving pattern transfer to MoE architectures, which already have sparse computation?

3. **Root cause of reduced memorization.** Is the significantly lower memorization rate attributable to architectural changes, training data curation, or distillation? The paper does not isolate the factor.

4. **Vision encoder fine-tuning.** Would unfreezing the vision encoder during training improve vision-language integration, and at what cost to text performance?

5. **Beyond 128K context.** What modifications would be needed to extend beyond 128K without the rapid degradation observed in Figure 7?

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Base Transformer architecture.
- **Ainslie et al. (2023)** -- *GQA.* Grouped-Query Attention used in all Gemma 3 models.
- **Zhang and Sennrich (2019)** -- *RMSNorm.* Normalization used for training stability.
- **Beltagy et al. (2020)** -- *Longformer.* Sliding window self-attention pattern adapted for local layers.

### Direct Predecessors

- **Gemma Team (2024a)** -- *Gemma.* First-generation Gemma establishing architecture foundations.
- **Gemma Team (2024b)** -- *Gemma 2.* Direct predecessor with 1:1 local-global ratio and soft-capping.

### Context Extension

- **Chen et al. (2023)** -- *Positional Interpolation.* RoPE rescaling approach adapted for extending global attention span.

### Vision Integration

- **Zhai et al. (2023)** -- *SigLIP.* Vision encoder architecture (400M variant) used for multimodal capability.
- **Liu et al. (2024)** -- *LLaVA.* Pan & Scan approach inspired by LLaVA's handling of varying resolutions.

### Post-Training

- **Hinton et al. (2015)** -- *Knowledge Distillation.* Foundation for pre-training and post-training distillation approach.
- **Sessa et al. (2024)** -- *BOND.* RL finetuning method used in post-training.
- **Rame et al. (2024a,b)** -- *WARP and WARM.* Weight averaging methods for reward models and policies.

### Long-Context Evaluation

- **Hsieh et al. (2024)** -- *RULER.* Multi-task synthetic long-context benchmark used for 32K and 128K evaluation.
- **Vodrahalli et al. (2024)** -- *MRCR (Michelangelo).* Long-context evaluation beyond needle-in-haystack.
