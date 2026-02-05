---
title: "Kimi-VL Technical Report"
authors: "Kimi Team"
year: 2025
venue: "arXiv preprint 2504.07491"
paper_type: preprint
categories: ["model-release", "architecture", "context-extension", "long-context-evaluation", "attention-efficiency"]
scope: ["open MoE VLM", "128K context", "native-resolution vision encoder", "long-CoT reasoning", "vision-language", "agent tasks"]
benchmarks_used: ["mmmu", "mmlu", "mathvista", "math-hendrycks", "longbench", "niah", "infinitebench"]
models_introduced: ["kimi-vl-a3b"]
models_evaluated: ["gpt-4o", "qwen2.5-vl-7b", "gemma-3-12b", "deepseek-vl2"]
key_claims:
  - id: C1
    claim: "Kimi-VL-A3B with 2.8B activated LLM parameters achieves 83.1% on MMBench-EN-v1.1, matching GPT-4o"
    evidence: "Table 3, Section 4.1.2"
    status: supported
    scope: "zero-shot evaluation"
  - id: C2
    claim: "Kimi-VL achieves 8.22% on OSWorld, outperforming GPT-4o (5.03%) on multi-turn agent tasks"
    evidence: "Table 3, Section 4.1.5"
    status: supported
    scope: "with Omniparser for baselines"
  - id: C3
    claim: "128K context is achieved by extending RoPE base frequency from 50,000 to 800,000 during joint long-context training"
    evidence: "Section 2.3, Table 2"
    status: supported
    scope: "8K to 128K extension in two sub-stages"
  - id: C4
    claim: "Kimi-VL-Thinking-2506 achieves 56.9% on MathVision with only 2.8B activated parameters, competitive with 72B models"
    evidence: "Table 4, Figure 1"
    status: supported
    scope: "with long-CoT and RL training"
  - id: C5
    claim: "Training throughput is ~60% higher than a 7B dense VLM due to MoE architecture"
    evidence: "Section 2.5"
    status: unvalidated
    scope: "internal comparison, no detailed metrics provided"
cross_references:
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Uses 2D RoPE for vision encoder spatial encoding and extends RoPE base frequency for 128K context"
  - target: 2025-03-gemma-3-technical-report
    type: concurrent
    detail: "Both are 2025 multimodal models with 128K context; Gemma 3 uses local-global interleaving while Kimi-VL uses MoE"
  - target: 2024-07-qwen2-technical-report
    type: evaluates
    detail: "Compares against Qwen2.5-VL-7B across multiple benchmarks"
  - target: 2024-05-yarn-context-extension
    type: complementary
    detail: "Different approach to context extension; Kimi-VL uses direct RoPE base frequency scaling"
open_questions:
  - question: "How does the MoE routing behave differently for vision tokens versus text tokens?"
    addressed_by: null
  - question: "What is the performance degradation beyond 128K context?"
    addressed_by: null
  - question: "Would the training recipe transfer to larger MoE configurations (e.g., 70B+ total parameters)?"
    addressed_by: null
---

# Kimi-VL Technical Report

**Authors:** Kimi Team (Moonshot AI)
**Date:** April 2025, arXiv:2504.07491

---

## Core Research Problem

Open-source vision-language models have lagged behind language-only counterparts in scalability, computational efficiency, and advanced reasoning capabilities. While language models like DeepSeek-R1 leverage MoE architectures and long chain-of-thought reasoning, most VLMs (e.g., Qwen2.5-VL, Gemma-3) rely on dense architectures and do not support long-CoT reasoning. Existing MoE-based VLMs such as DeepSeek-VL2 and Aria have limitations: DeepSeek-VL2 supports only 4K context, while both use fixed-size vision encoders that hinder adaptability to diverse visual inputs. Additionally, neither supports long-thinking abilities. The core challenge was: **how to build an efficient open-source VLM that combines MoE scalability, native-resolution vision encoding, 128K context, and long-CoT reasoning.**

---

## Problem Solutions

Kimi-VL addresses these challenges through four innovations:

1. **MoE language decoder with 2.8B activated parameters.** Uses Moonlight architecture (similar to DeepSeek-V3) with 16B total parameters but only 2.8B activated per token, enabling ~60% higher training throughput than 7B dense models.

2. **Native-resolution vision encoder (MoonViT).** Processes images at their original resolutions without sub-image splitting, using NaViT-style packing and 2D RoPE for spatial encoding.

3. **128K context through RoPE frequency scaling.** Extends context from 8K to 128K by increasing RoPE base frequency from 50,000 to 800,000 in a joint long-context training stage.

4. **Long-CoT reasoning via SFT and RL.** Kimi-VL-Thinking variant uses long chain-of-thought supervised fine-tuning followed by reinforcement learning to enable test-time scaling.

---

## Approach Details

### Architecture

Kimi-VL consists of three components (Figure 3):

**MoonViT (Native-resolution Vision Encoder):**
- Initialized from SigLIP-SO-400M (Zhai et al., 2023)
- Uses NaViT packing (Dehghani et al., 2023): images divided into patches, flattened, concatenated into 1D sequences
- Dual positional encoding: interpolated absolute positional embeddings from SigLIP + 2D RoPE across height and width
- Supports variable-length sequence attention via FlashAttention
- In Kimi-VL-Thinking-2506: extended to 3.2 million pixels per image (4x original)

**MLP Projector:**
- Two-layer MLP with pixel shuffle (2x2 spatial downsampling)
- Compresses spatial dimension while expanding channel dimension

**MoE Language Model:**
- Based on Moonlight (Liu et al., 2025a), similar to DeepSeek-V3
- 2.8B activated parameters, 16B total parameters
- Initialized from intermediate Moonlight checkpoint (5.2T text tokens, 8K context)

| Component | Parameters |
|-----------|------------|
| MoonViT | 400M |
| LLM (activated) | 2.8B |
| LLM (total) | 16B |

### Key Technical Components

#### Native-Resolution Vision Processing

MoonViT eliminates sub-image splitting operations used in LLaVA-OneVision. Key design choices:

1. **NaViT packing:** Images of varying resolutions processed in same batch
2. **2D RoPE:** Improves fine-grained positional information for high-resolution images
3. **Dual position encoding:** Original interpolated absolute embeddings + 2D RoPE work together

#### Context Extension

RoPE base frequency scaling for 128K context:

> RoPE base: 50,000 → 800,000

Extension performed in two sub-stages (each 4x):
- Stage 1: 8K → 32K
- Stage 2: 32K → 128K

Data composition for long-context activation: 25% long data (text, video, document), 75% shorter data replay.

#### Muon Optimizer

Enhanced Muon optimizer (Liu et al., 2025b) used throughout training:
- Added weight decay
- Adjusted per-parameter update scale
- Distributed implementation following ZeRO-1 strategy

### Pre-Training

Four stages consuming 4.4T tokens total after text pre-training (Figure 4, Table 1):

| Stage | Data | Tokens | Sequence Length | Components Trained |
|-------|------|--------|-----------------|-------------------|
| ViT Training | Alt text, captions, grounding, OCR | 2T + 0.1T | 8192 | ViT only |
| Joint Pre-training | Text, knowledge, interleaving, video, agent | 1.4T | 8192 | ViT & LLM |
| Joint Cooldown | High-quality text & multimodal, academic sources | 0.6T | 8192 | ViT & LLM |
| Joint Long-context | Long text, long video, long document | 0.3T | 32768→131072 | ViT & LLM |

**ViT Training:** Uses CoCa-style (Yu et al., 2022) loss:

> L = L_siglip + 2 * L_caption

Contrastive loss + caption generation with next-token prediction.

**Joint Pre-training:** Progressive multimodal ratio (up to 40%), maintains language capabilities through joint training.

**Joint Cooldown:** High-quality data including synthetic QA pairs for math, knowledge, and code. Re-warms learning rate.

**Joint Long-context:** Extends context with RoPE base scaling, uses 25% long data + 75% replay.

### Post-Training

**Joint SFT:** Two-epoch training:
- Epoch 1: 32K context, LR 2×10⁻⁵ → 2×10⁻⁶
- Epoch 2: 128K context, LR re-warm to 1×10⁻⁵ → 1×10⁻⁶

Uses ChatML format with supervision only on answers and special tokens.

**Long-CoT SFT (for Thinking variant):** Warmup dataset with planning, evaluation, reflection, and exploration patterns. Generated via prompt engineering with Kimi k1.5 and rejection sampling.

**Reinforcement Learning:** Online policy mirror descent (similar to Kimi k1.5):

> max_θ E[(x,y*)~D] [E[(y,z)~π_θ][r(x, y, y*)] - τKL(π_θ(x)||π_θi(x))]

Key RL enhancements:
- Length-based reward to penalize overthinking
- Curriculum sampling using difficulty labels
- Prioritized sampling based on per-instance success rates

### Infrastructure

**4D Parallelism:**
- Data Parallelism (DP)
- Expert Parallelism (EP)
- Pipeline Parallelism (PP) with ViT in first stage
- Context Parallelism (CP) with FlashAttention for long sequences

Additional optimizations: ZeRO-1, Selective Checkpointing Activation.

### Key Results

#### Main Comparison (Table 3)

| Benchmark | GPT-4o | Qwen2.5-VL-7B | Gemma-3-12B-IT | DeepSeek-VL2 | Kimi-VL-A3B |
|-----------|--------|---------------|----------------|--------------|-------------|
| MMMU (val) | 69.1 | 58.6 | 59.6 | 51.1 | **57.0** |
| MMBench-EN-v1.1 | 83.1 | 82.6 | 74.6 | 79.6 | **83.1** |
| MathVista | 63.8 | 68.2 | 56.1 | 62.8 | **68.7** |
| InfoVQA | 80.7 | 82.6 | 43.8 | 78.1 | **83.2** |
| OSWorld | 5.03 | 2.5 | - | - | **8.22** |
| LongVideoBench | 66.7 | 56.0 | 51.5 | - | **64.5** |
| MMLongBench-Doc | 42.8 | 29.6 | 21.3 | - | **35.1** |

Kimi-VL-A3B outperforms Qwen2.5-VL-7B on 19/24 benchmarks with 2.59× fewer activated parameters.

#### Needle-in-a-Haystack (Table 2)

| Haystack Length | (0, 2K] | (2K, 4K] | (4K, 8K] | (8K, 16K] | (16K, 32K] | (32K, 64K] | (64K, 128K] |
|-----------------|---------|----------|----------|-----------|------------|------------|-------------|
| Text haystack | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 87.0 |
| Video haystack | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 91.7 |

#### Kimi-VL-Thinking (Table 4)

| Benchmark | Kimi-VL-A3B | Kimi-VL-Thinking | Kimi-VL-Thinking-2506 | QVQ-72B-Preview |
|-----------|-------------|------------------|----------------------|-----------------|
| MathVision | 21.4 | 36.8 | **56.9** | 35.9 |
| MathVista | 68.7 | 71.3 | **80.1** | 71.4 |
| MMMU | 57.0 | 61.7 | **64.0** | 70.3 |
| VideoMMMU | 52.6 | 55.5 | **65.2** | - |

Thinking-2506 achieves 56.9% on MathVision with 2.8B activated parameters, competitive with 72B models.

#### Test-Time Scaling (Figure 13)

Increasing max thinking length from 1K to 16K tokens:
- MathVision: 18.7% → 36.8%
- MMMU: 49.2% → 61.7%
- MathVista: 66.7% → 71.3% (saturates at 4K)

---

## Limitations and Failure Modes

The authors acknowledge several limitations (Section 5):

1. **Model scale limitations.** The 2.8B activated parameter scale is insufficient for highly specialized or domain-specific problems that require strong language abilities.

2. **Reasoning ceiling not reached.** While strong for typical use cases, reasoning has not reached theoretical upper bound for multi-step inference.

3. **Long-context limitations.** Despite 128K context, attention layer parameters (comparable to 3B model) limit performance on extremely long sequences.

4. **NIAH degradation at 128K.** Text haystack recall drops to 87.0% and video to 91.7% at 64K-128K range (Table 2).

5. **MathVista saturation.** Test-time scaling shows diminishing returns beyond 4K thinking tokens on MathVista (Figure 13).

### Scope and Comparability

- **What was not tested:** Models larger than 16B total parameters; dense VLM baselines with equivalent FLOPs; detailed ablations on MoE routing for vision vs. text tokens.
- **Comparability notes:** OSWorld results for GPT-4o and GPT-4o-mini use Omniparser without UIA (Bonatti et al., 2024). Some competing models lack results due to context length or capability limitations.

---

## Conclusions

### Contributions

1. **Efficient MoE vision-language model.** Kimi-VL achieves competitive performance with 2.8B activated parameters (16B total), providing ~60% higher training throughput than 7B dense VLMs (Section 2.5).

2. **Native-resolution vision encoding.** MoonViT processes images at original resolutions using NaViT packing and 2D RoPE, eliminating sub-image splitting while achieving 83.2% on InfoVQA and 34.5% on ScreenSpot-Pro (Table 3).

3. **128K multimodal context.** RoPE frequency scaling (50K→800K) enables 128K context with high NIAH recall (87-100% across lengths), supporting hour-long video understanding (Table 2).

4. **Long-CoT reasoning via RL.** Kimi-VL-Thinking-2506 achieves 56.9% on MathVision with test-time scaling, demonstrating effective long-horizon multimodal reasoning (Table 4, Figure 13).

5. **Strong agent capabilities.** 8.22% on OSWorld surpasses GPT-4o (5.03%), demonstrating multi-turn GUI agent interaction abilities (Table 3).

### Implications

1. **MoE enables efficient multimodal scaling.** The efficiency gains suggest MoE may be preferable to dense architectures for VLMs at the 7B-activated-parameter scale.

2. **Joint training preserves text capabilities.** The progressive multimodal ratio and joint training stages maintain language model capabilities while adding vision (Section 2.3), though no ablation isolates this effect.

3. **Test-time scaling transfers to multimodal.** The Thinking variant demonstrates that language-model test-time scaling techniques (long-CoT, RL) apply to vision-language tasks, with 20%+ absolute improvements on reasoning benchmarks.

---

## Key Claims

1. **Kimi-VL-A3B matches or exceeds larger dense VLMs.** Achieves 83.1% on MMBench (matches GPT-4o), 68.7% on MathVista (exceeds GPT-4o's 63.8%), with only 2.8B activated parameters. Evidence: Table 3. Status: **supported**. Scope: Zero-shot evaluation on standard benchmarks.

2. **OSWorld performance exceeds GPT-4o.** 8.22% vs 5.03% on multi-turn agent interaction. Evidence: Table 3. Status: **supported**. Scope: GPT-4o uses Omniparser without UIA.

3. **128K context achieved via RoPE frequency scaling.** Base frequency increased from 50K to 800K in two 4x sub-stages. NIAH recall maintains 87%+ across context lengths. Evidence: Table 2, Section 2.3. Status: **supported**. Scope: Text and video haystacks tested.

4. **Kimi-VL-Thinking-2506 competitive with 72B models on reasoning.** 56.9% on MathVision exceeds QVQ-72B-Preview (35.9%) with 25x fewer activated parameters. Evidence: Table 4, Figure 1. Status: **supported**. Scope: With long-CoT and RL training.

5. **Training throughput ~60% higher than 7B dense VLM.** Evidence: Section 2.5. Status: **unvalidated**. Scope: No detailed methodology or comparison provided.

6. **Test-time scaling effective for multimodal reasoning.** MathVision accuracy improves from 18.7% to 36.8% when scaling thinking tokens from 1K to 16K. Evidence: Figure 13. Status: **supported**. Scope: Thinking variant only; MathVista saturates early.

---

## Open Questions

1. **MoE routing for vision tokens.** How does the expert routing behave differently for vision tokens versus text tokens? The paper does not analyze routing patterns.

2. **Performance beyond 128K.** What happens at longer contexts? NIAH already shows degradation at 64K-128K (87-91.7% vs 100% at shorter lengths).

3. **Scaling to larger MoE configurations.** Would the training recipe (joint stages, progressive multimodal ratio) transfer to 70B+ total parameter models?

4. **Vision encoder fine-tuning vs. freezing.** Unlike Gemma 3's frozen encoder, Kimi-VL trains MoonViT jointly. What is the impact on vision-language integration depth?

5. **RL reward design for multimodal.** The paper uses binary correctness rewards. Would denser reward signals improve multimodal reasoning training?

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Base Transformer architecture.
- **Su et al. (2023)** -- *RoFormer/RoPE.* Rotary positional embeddings used in both vision encoder (2D) and language model.
- **Zhai et al. (2023)** -- *SigLIP.* MoonViT initialized from SigLIP-SO-400M.
- **Dehghani et al. (2023)** -- *NaViT.* Packing method for native-resolution vision processing.
- **DeepSeek-AI (2025)** -- *DeepSeek-V3.* MoE architecture that Moonlight (Kimi-VL's LLM) is based on.

### Vision-Language Models

- **Wu et al. (2024)** -- *DeepSeek-VL2.* Prior MoE VLM comparison; limited to 4K context.
- **Li et al. (2024)** -- *LLaVA-OneVision.* Sub-image splitting approach that MoonViT avoids.
- **Bai et al. (2025)** -- *Qwen2.5-VL.* Primary dense VLM comparison baseline.
- **Gemma Team (2025)** -- *Gemma 3.* Concurrent multimodal model with different architecture choices.

### Training Methods

- **Yu et al. (2022)** -- *CoCa.* Contrastive captioner loss formulation used for ViT training.
- **Dao et al. (2022)** -- *FlashAttention.* Enables efficient variable-length sequence attention.
- **Rajbhandari et al. (2020)** -- *ZeRO.* Memory optimization strategy for distributed training.
- **Kimi Team (2025)** -- *Kimi k1.5.* RL algorithm and long-CoT approach for Thinking variant.

### Long-Context and Reasoning

- **Jordan et al. (2024)** -- *Muon optimizer.* Base optimizer enhanced for Kimi-VL training.
- **Liu et al. (2025a)** -- *Moonlight.* Base MoE language model that Kimi-VL extends.

### Evaluation Benchmarks

- **Yue et al. (2024)** -- *MMMU.* College-level multimodal understanding benchmark.
- **Xie et al. (2024)** -- *OSWorld.* Multi-turn agent interaction benchmark.
- **Wu et al. (2024)** -- *LongVideoBench.* Long video understanding benchmark.
