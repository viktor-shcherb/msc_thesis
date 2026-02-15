---
title: "Kimi-VL Technical Report"
authors: "Kimi Team"
year: 2025
venue: "arXiv preprint 2504.07491"
paper_type: preprint
categories: ["model-release", "architecture", "context-extension", "long-context-evaluation", "attention-efficiency"]
scope: ["open MoE VLM", "128K context", "native-resolution vision encoder", "long-CoT reasoning", "vision-language", "agent tasks"]
benchmarks_used: ["mmmu", "egoschema", "niah"]
models_introduced: ["kimi-vl-a3b"]
models_evaluated: ["gpt-4o", "gpt-4o-mini", "qwen2.5-vl-7b", "gemma-3-12b", "gemma-3-27b", "deepseek-vl2"]
key_claims:
  - id: C1
    claim: "Kimi-VL-A3B with 2.8B activated LLM parameters matches GPT-4o on MMBench-EN-v1.1 (both 83.1%) and outperforms Qwen2.5-VL-7B on 19/24 benchmarks with 2.59x fewer activated parameters"
    evidence: "Table 3, Section 4.1"
    status: supported
    scope: "zero-shot evaluation across 24 benchmarks; compared to dense VLMs up to 12B and MoE VLMs up to 28B total"
    magnitude: "83.1% on MMBench (ties GPT-4o), 68.7% on MathVista (vs GPT-4o 63.8%), 83.2% on InfoVQA (vs GPT-4o 80.7%)"
  - id: C2
    claim: "Kimi-VL achieves 8.22% on OSWorld, outperforming GPT-4o (5.03%) on multi-turn agent tasks"
    evidence: "Table 3, Section 4.1.5"
    status: supported
    scope: "GPT-4o baseline uses Omniparser without UIA; Kimi-VL also achieves 10.4% on WindowsAgentArena vs GPT-4o 9.4%"
    magnitude: "8.22% vs 5.03% (3.19pp improvement over GPT-4o on OSWorld)"
  - id: C3
    claim: "128K context is achieved by extending RoPE base frequency from 50,000 to 800,000 during joint long-context training"
    evidence: "Section 2.3, Table 2"
    status: supported
    scope: "8K to 128K extension in two 4x sub-stages; tested on text and video NIAH"
    magnitude: "100% NIAH recall up to 64K; 87.0% text / 91.7% video at 64K-128K"
  - id: C4
    claim: "Kimi-VL-Thinking-2506 achieves 56.9% on MathVision with only 2.8B activated parameters, exceeding QVQ-72B-Preview (35.9%) with ~25x fewer activated parameters"
    evidence: "Table 4, Figure 1"
    status: supported
    scope: "with long-CoT SFT and RL training; MoonViT extended to 3.2M pixels; compared to both thinking and non-thinking models"
    magnitude: "56.9% on MathVision (+20.1pp over Kimi-VL-Thinking), 80.1% on MathVista, 64.0% on MMMU, 65.2% on VideoMMMU"
  - id: C5
    claim: "Training throughput is ~60% higher than a 7B dense VLM due to MoE architecture and 4D parallelism"
    evidence: "Section 2.5"
    status: unvalidated
    scope: "internal comparison against VLMs based on Qwen2.5-7B; no detailed methodology or hardware specification provided"
    magnitude: "~60% throughput improvement (qualitative claim, no precise measurement shared)"
  - id: C6
    claim: "Test-time scaling is effective for multimodal reasoning: increasing max thinking tokens from 1K to 16K improves MathVision from 18.7% to 36.8%"
    evidence: "Figure 13, Section 4.2"
    status: supported
    scope: "Kimi-VL-Thinking variant only; MathVista saturates at ~4K tokens; three benchmarks tested"
    magnitude: "MathVision: 18.7% -> 36.8% (+18.1pp); MMMU: 49.2% -> 61.7% (+12.5pp); MathVista: 66.7% -> 71.3% (+4.6pp, saturates at 4K)"
  - id: C7
    claim: "Kimi-VL-Thinking-2506 integrates reasoning with general perception abilities, achieving 84.4% on MMBench and 42.1% on MMLongBench-Doc while reducing output token length by ~20%"
    evidence: "Table 5, Section 4.3"
    status: supported
    scope: "compared against Kimi-VL-A3B-Instruct and Kimi-VL-Thinking on non-reasoning benchmarks"
    magnitude: "84.4% MMBench (+8.4pp over Thinking), 42.1% MMLongBench-Doc (+7pp over Instruct), 52.8% ScreenSpot-Pro (+17.4pp over Instruct); token reduction: 2.9K->2.4K on MMMU, 5.8K->4.4K on MathVision"
cross_references:
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Uses 2D RoPE for vision encoder spatial encoding and extends RoPE base frequency for 128K context"
  - target: 2025-03-gemma-3-technical-report
    type: concurrent
    detail: "Both are 2025 multimodal models with 128K context; Gemma 3 uses local-global interleaving while Kimi-VL uses MoE"
  - target: 2024-07-qwen2-technical-report
    type: evaluates
    detail: "Compares against Qwen2.5-VL-7B across multiple benchmarks as primary dense VLM baseline"
  - target: 2024-05-yarn-context-extension
    type: complementary
    detail: "Different approach to context extension; Kimi-VL uses direct RoPE base frequency scaling rather than NTK-aware interpolation"
  - target: 2024-12-deepseek-v3-technical-report
    type: extends
    detail: "Kimi-VL's language model (Moonlight) has architecture similar to DeepSeek-V3; initialized from intermediate Moonlight checkpoint"
  - target: 2025-01-kimi-k1.5-scaling-rl
    type: extends
    detail: "RL algorithm and long-CoT approach for Kimi-VL-Thinking derived from Kimi k1.5"
open_questions:
  - question: "How does the MoE routing behave differently for vision tokens versus text tokens?"
    addressed_by: null
  - question: "What is the performance degradation beyond 128K context, given NIAH already shows drops at 64K-128K?"
    addressed_by: null
  - question: "Would the training recipe (joint stages, progressive multimodal ratio) transfer to larger MoE configurations (e.g., 70B+ total parameters)?"
    addressed_by: null
  - question: "What is the impact of jointly training MoonViT vs freezing the vision encoder (as in Gemma 3) on vision-language integration depth?"
    addressed_by: null
  - question: "Would denser reward signals (beyond binary correctness) improve multimodal RL reasoning training?"
    addressed_by: null
---

# Kimi-VL Technical Report

**Authors:** Kimi Team (Moonshot AI; select authors from The University of Hong Kong)
**Date:** April 2025, arXiv:2504.07491 (v3: June 23, 2025)

---

## Core Research Problem

Open-source vision-language models have lagged behind language-only counterparts in scalability, computational efficiency, and advanced reasoning capabilities. While language models such as DeepSeek-R1 leverage MoE architectures and long chain-of-thought reasoning, most open-source VLMs (e.g., Qwen2.5-VL, Gemma 3) rely on dense architectures and do not support long-CoT reasoning (Section 1). Early MoE-based VLMs have limitations in other dimensions: DeepSeek-VL2 supports only 4K context and Aria falls short in fine-grained visual tasks; neither supports long video understanding. Architecturally, both still use traditional vision encoders that hinder adaptability to diverse visual inputs. The core challenge is: **how to build an efficient open-source VLM that combines MoE scalability, native-resolution vision encoding, 128K multimodal context, and long-CoT reasoning in a single model.**

---

## Problem Solutions

Kimi-VL addresses these challenges through four integrated innovations:

1. **MoE language decoder with 2.8B activated parameters.** Uses Moonlight architecture (similar to DeepSeek-V3) with 16B total parameters but only 2.8B activated per token, enabling ~60% higher training throughput than 7B dense models (Section 2.5).

2. **Native-resolution vision encoder (MoonViT).** Processes images at their original resolutions without sub-image splitting, using NaViT-style packing and 2D RoPE for spatial encoding (Section 2.1).

3. **128K multimodal context through RoPE frequency scaling.** Extends context from 8K to 128K by increasing RoPE base frequency from 50,000 to 800,000 in a two-stage process (Section 2.3).

4. **Long-CoT reasoning via SFT and RL (Kimi-VL-Thinking).** Long chain-of-thought supervised fine-tuning followed by reinforcement learning enables test-time scaling for multimodal reasoning (Section 2.4).

---

## Approach Details

### Method

Kimi-VL consists of three components (Figure 3):

**MoonViT (Native-resolution Vision Encoder):**
- Initialized from SigLIP-SO-400M (Zhai et al., 2023)
- Uses NaViT packing (Dehghani et al., 2023): images divided into patches, flattened, and concatenated into 1D sequences
- Dual positional encoding: interpolated absolute positional embeddings from SigLIP + 2D RoPE across height and width dimensions (Su et al., 2023)
- Supports variable-length sequence attention via FlashAttention (Dao et al., 2022)
- In Kimi-VL-Thinking-2506: extended to 3.2 million pixels per image (4x the original limit)

**MLP Projector:**
- Two-layer MLP with pixel shuffle operation (2x2 spatial downsampling)
- Compresses spatial dimension while expanding channel dimension
- Projects features into the LLM embedding dimension

**MoE Language Model:**
- Based on Moonlight (Liu et al., 2025a), architecture similar to DeepSeek-V3 (DeepSeek-AI, 2025)
- 2.8B activated parameters, 16B total parameters
- Initialized from intermediate Moonlight checkpoint (5.2T text tokens, 8K context)

| Component | Parameters |
|-----------|------------|
| MoonViT | 400M |
| MLP Projector | [not in notes] |
| LLM (activated) | 2.8B |
| LLM (total) | 16B |
| Full model activated (LLM+VT) | 2.8B + 0.4B = 3.2B |

### Key Technical Components

#### Native-Resolution Vision Processing

MoonViT eliminates the sub-image splitting and splicing operations used in LLaVA-OneVision (Li et al., 2024). Key design choices:

1. **NaViT packing:** Images of varying resolutions processed in the same batch by flattening patches into 1D sequences
2. **2D RoPE:** Rotary positional embeddings applied across height and width dimensions, improving fine-grained positional information for high-resolution images
3. **Dual position encoding:** Original interpolated absolute embeddings from SigLIP + 2D RoPE work together to encode spatial information
4. **Variable-length attention:** FlashAttention enables efficient attention over variable-length sequences within a batch

#### Context Extension

RoPE base frequency scaling for 128K context:

> RoPE base: 50,000 --> 800,000

Extension performed in two 4x sub-stages during the Joint Long-context activation stage:
- Sub-stage 1: 8K --> 32K
- Sub-stage 2: 32K --> 128K

Data composition for long-context activation: **25% long data** (long text, long video, long document) + **75% shorter data replay** to preserve existing capabilities (Section 2.3).

#### Muon Optimizer

Enhanced Muon optimizer (Liu et al., 2025b, building on Jordan et al., 2024) used throughout the entire training process for all model parameters (vision encoder, projector, and language model):
- Added weight decay (absent in original Muon)
- Adjusted per-parameter update scale
- Distributed implementation following ZeRO-1 (Rajbhandari et al., 2020) strategy for optimal memory efficiency and reduced communication overhead

### Pre-Training

Four stages consuming 4.4T tokens total after text pre-training (Figure 4, Table 1):

| Stage | Data | Tokens | Sequence Length | Components Trained |
|-------|------|--------|-----------------|-------------------|
| ViT Training | Alt text, captions, grounding, OCR | 2T + 0.1T | 8192 | ViT only (+ 0.1T aligning MLP projector) |
| Joint Pre-training | Text, knowledge, interleaving, video, agent | 1.4T | 8192 | ViT & LLM |
| Joint Cooldown | High-quality text & multimodal, academic sources | 0.6T | 8192 | ViT & LLM |
| Joint Long-context | Long text, long video, long document | 0.3T | 32768 --> 131072 | ViT & LLM |

**ViT Training:** Uses CoCa-style loss (Yu et al., 2022):

> L = L_siglip + 2 * L_caption

Contrastive loss (SigLIP variant) + caption generation with next-token prediction (lambda=2). Progressive resolution sampling strategy used. An emergence in caption loss was observed while scaling up OCR data, indicating the text decoder developed OCR capabilities. After 2T tokens, 0.1T additional tokens align MoonViT to the MoE language model (only MLP projector updated), significantly reducing initial perplexity.

**Joint Pre-training (1.4T tokens):** Continues from loaded LLM checkpoint with same learning rate scheduler. Initial steps use solely language data, after which multimodal data proportion gradually increases (progressive multimodal ratio, up to 40%). This joint approach preserves language capabilities while integrating visual comprehension (Section 2.3).

**Joint Cooldown (0.6T tokens):** High-quality data including synthetic QA pairs for math, knowledge, and code domains. Uses rejection sampling for quality control (Yue, Qu et al., 2023; Su et al., 2024). Multimodal data includes filtered and rewritten academic visual/vision-language data sources. Learning rate re-warms. QA pair ratio kept low to avoid overfitting.

**Joint Long-context (0.3T tokens):** Extends context with RoPE base frequency scaling from 50K to 800K. Uses 25% long data + 75% shorter data replay.

#### Data Construction

The pre-training corpus spans seven categories (Section 3.1):

1. **Caption data:** Open-source and in-house Chinese/English caption datasets; synthetic caption proportion strictly limited to mitigate hallucination risk
2. **Image-text interleaving data:** Boosts multi-image comprehension and long multimodal context learning; includes open-source datasets (Zhu et al., 2024; Laurencon et al., 2024) and in-house data from textbooks, webpages, tutorials
3. **OCR data:** Diverse sources including clean/augmented images, single-page and multi-page inputs, handwritten text; follows OCR 2.0 principles (Wei et al., 2024) for figures, charts, geometry, music sheets, mind maps
4. **Knowledge data:** Standardized taxonomy balancing content across categories; includes geometry data for visual reasoning; additional pipeline captures textual information from infographics
5. **Agent data:** Screenshots and action data from virtual machine environments; covers Desktop, Mobile, and Web action spaces; includes icon data and multi-step agent trajectories with synthesized CoT annotations
6. **Video data:** Open-source and in-house web-scale video data of varying durations; covers video description and video grounding; pipeline for dense long-video captions with synthetic proportion limited
7. **Text data:** Reuses Moonlight's (Liu et al., 2025a) text corpus covering English, Chinese, Code, Mathematics & Reasoning, and Knowledge domains

### Post-Training

**Joint SFT (Section 2.4):** Two-epoch training using ChatML format with supervision only on responses (system/user prompts masked):
- **Epoch 1 (32K context):** LR decays from 2x10^-5 to 2x10^-6
- **Epoch 2 (128K context):** LR re-warms to 1x10^-5, then decays to 1x10^-6
- Multiple training examples packed into each sequence for efficiency

**Long-CoT SFT (for Thinking variant, Section 2.4):** Warmup dataset with key cognitive patterns:
- **Planning:** systematic outlining of steps before execution
- **Evaluation:** critical assessment of intermediate steps
- **Reflection:** refining approach during execution
- **Exploration:** considering alternative solutions

Generated via prompt engineering with Kimi k1.5 (Team et al., 2025) and rejection sampling.

**Reinforcement Learning (Section 2.4):** Online policy mirror descent (similar to Kimi k1.5):

> max_theta E_{(x,y*) ~ D} [ E_{y ~ pi_theta} [r(x, y, y*)] - tau * KL(pi_theta(x) || pi_{theta_i}(x)) ]

where r is a binary correctness reward r(x, y, y*) in {0, 1} and tau > 0 controls regularization strength.

Key RL enhancements:
- **Length-based reward:** Penalizes excessively long responses to mitigate oververbalization
- **Curriculum sampling:** Leverages difficulty labels to focus training on pedagogically valuable examples
- **Prioritized sampling:** Uses per-instance success rates to optimize the learning trajectory

### Infrastructure

**4D Parallelism (Section 2.5):**
- **Data Parallelism (DP):** Model replicated across devices, each processing different micro-batches
- **Expert Parallelism (EP):** MoE layer distributed across devices; combined with DP, experts handle tokens from different DP groups
- **Pipeline Parallelism (PP):** Vision Tower (VT) and additional decoder layers in first stage; output layer and additional layers in last stage; remaining layers distributed evenly by time overhead
- **Context Parallelism (CP):** Sequences split across CP ranks with FlashAttention for long sequences

Additional optimizations: ZeRO-1 (Rajbhandari et al., 2020) for distributed optimizer states; Selective Checkpointing Activation (Chen et al., 2016; Korthikanti et al., 2022) recomputing low-time-overhead, high-memory layers; expanded recomputation for extremely long sequences.

### Experimental Setup

**Models compared (Table 3):** GPT-4o, GPT-4o-mini, Qwen2.5-VL-7B (dense, 7.6B+0.7B activated), Llama-3.2-11B-Inst (dense, 8B+2.6B), Gemma-3-12B-IT (dense, 12B+0.4B), DeepSeek-VL2 (MoE, 4.1B+0.4B activated, 28B total). Kimi-VL-A3B uses MoE with 2.8B+0.4B activated, 16B total.

**Thinking model comparisons (Table 4):** Additional models include Qwen2.5-VL-72B, Gemma-3-27B, o1-1217, QVQ-72B-Preview, Kimi-k1.5.

**Benchmarks:** 24 benchmarks across 9 categories -- college-level (MMMU, VideoMMMU, MMVU), general (MMBench-EN-v1.1, MMStar, MMVet, RealWorldQA, AI2D), multi-image (BLINK), math (MathVista, MathVision), OCR (InfoVQA, OCRBench), OS agent (ScreenSpot-V2, ScreenSpot-Pro, OSWorld, WindowsAgentArena), long document (MMLongBench-Doc), long video (Video-MME, MLVU, LongVideoBench), video perception (EgoSchema, VSI-Bench, TOMATO).

**Reproducibility:** Code and models publicly available at https://github.com/MoonshotAI/Kimi-VL and HuggingFace (https://huggingface.co/moonshotai). Training hyperparameters (learning rates, token counts) specified. However, data mixtures are described qualitatively rather than with exact proportions. No random seeds reported. Hardware details (GPU type, cluster size) not specified.

### Key Results

#### Main Comparison (Table 3)

| Benchmark | GPT-4o | GPT-4o-mini | Qwen2.5-VL-7B | Llama3.2-11B | Gemma3-12B-IT | DeepSeek-VL2 | Kimi-VL-A3B |
|-----------|--------|-------------|---------------|--------------|---------------|--------------|-------------|
| **College-level** | | | | | | | |
| MMMU (val) | 69.1 | 60.0 | 58.6 | 48.0 | 59.6 | 51.1 | 57.0 |
| VideoMMMU | 61.2 | - | 47.4 | 41.8 | 57.2 | 44.4 | 52.6 |
| MMVU (val) | 67.4 | 61.6 | 50.1 | 44.4 | 57.0 | 52.1 | 52.2 |
| **General** | | | | | | | |
| MMBench-EN-v1.1 | 83.1 | 77.1 | 82.6 | 65.8 | 74.6 | 79.6 | **83.1** |
| MMStar | 64.7 | 54.8 | 63.9 | 49.8 | 56.1 | 55.5 | 61.3 |
| MMVet | 69.1 | 66.9 | 67.1 | 57.6 | 64.9 | 60.0 | 66.7 |
| RealWorldQA | 75.4 | 67.1 | 68.5 | 63.3 | 59.1 | 68.4 | 68.1 |
| AI2D | 84.6 | 77.8 | 83.9 | 77.3 | 78.1 | 81.4 | **84.9** |
| **Multi-image** | | | | | | | |
| BLINK | 68.0 | 53.6 | 56.4 | 39.8 | 50.3 | - | 57.3 |
| **Math** | | | | | | | |
| MathVista | 63.8 | 52.5 | 68.2 | 47.7 | 56.1 | 62.8 | **68.7** |
| MathVision | 30.4 | - | 25.1 | 13.6 | 32.1 | 17.3 | 21.4 |
| **OCR** | | | | | | | |
| InfoVQA | 80.7 | 57.9 | 82.6 | 34.6 | 43.8 | 78.1 | **83.2** |
| OCRBench | 815 | 785 | 864 | 753 | 702 | 811 | **867** |
| **OS Agent** | | | | | | | |
| ScreenSpot-V2 | 18.1 | - | 86.8 | - | - | - | **92.8** |
| ScreenSpot-Pro | 0.8 | - | 29.0 | - | - | - | **34.5** |
| OSWorld | 5.03 | - | 2.8 | - | - | - | **8.22** |
| WindowsAgentArena | 9.4 | 2.7 | 3.4 | - | - | - | **10.4** |
| **Long Document** | | | | | | | |
| MMLongBench-Doc | 42.8 | 29.0 | 29.6 | 13.8 | 21.3 | - | 35.1 |
| **Long Video** | | | | | | | |
| Video-MME (w/o / w/ sub) | 71.9/77.2 | 64.8/68.9 | 65.1/71.6 | 46.0/49.5 | 58.2/62.1 | - | 67.8/72.6 |
| MLVU (MCQ) | 64.6 | 48.1 | 70.2 | 44.4 | 52.3 | - | **74.2** |
| LongVideoBench | 66.7 | 58.2 | 56.0 | 45.5 | 51.5 | - | 64.5 |
| **Video Perception** | | | | | | | |
| EgoSchema (full) | 72.2 | - | 65.0 | 54.3 | 56.9 | 38.5 | **78.5** |
| VSI-Bench | 34.0 | - | 34.2 | 20.6 | 32.4 | 21.7 | **37.4** |
| TOMATO | 37.7 | 28.8 | 27.6 | 21.5 | 28.6 | 27.2 | 31.7 |

Key takeaways from Table 3 (tested across 24 benchmarks against 6 baselines -- strong evidence breadth):
- **Kimi-VL-A3B outperforms Qwen2.5-VL-7B on 19/24 benchmarks** with 2.59x fewer activated parameters (Section 4.1)
- **Ties GPT-4o on MMBench-EN-v1.1** (83.1% each) and **surpasses GPT-4o on MathVista** (68.7% vs 63.8%), AI2D (84.9% vs 84.6%), InfoVQA (83.2% vs 80.7%), EgoSchema (78.5% vs 72.2%)
- **Agent tasks:** OSWorld 8.22% vs GPT-4o 5.03%; WindowsAgentArena 10.4% vs GPT-4o 9.4%
- **Long video:** MLVU 74.2% surpasses all including GPT-4o (64.6%); LongVideoBench 64.5% approaches GPT-4o (66.7%)
- **Weakness on MathVision:** 21.4% falls behind Gemma-3-12B-IT (32.1%) and Qwen2.5-VL-7B (25.1%), though this is addressed by the Thinking variants

#### Needle-in-a-Haystack (Table 2)

| Haystack Length | [0, 2K] | (2K, 4K] | (4K, 8K] | (8K, 16K] | (16K, 32K] | (32K, 64K] | (64K, 128K] |
|-----------------|---------|----------|----------|-----------|------------|------------|-------------|
| Text haystack | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 87.0 |
| Video haystack | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 91.7 |

Perfect recall up to 64K tokens; degradation at the 64K-128K range (87.0% text, 91.7% video).

#### Kimi-VL-Thinking Results (Table 4)

| Benchmark | GPT-4o | Qwen2.5-VL-72B | Gemma-3-27B | o1-1217 | QVQ-72B-Preview | Kimi-k1.5 | Kimi-VL-Thinking | Kimi-VL-Thinking-2506 |
|-----------|--------|----------------|-------------|---------|-----------------|-----------|------------------|----------------------|
| MathVision (full) | 30.4 | 38.1 | 35.5 | - | 35.9 | 38.6 | 36.8 | **56.9** |
| MathVista (mini) | 63.8 | 74.8 | 62.3 | 71.0 | 71.4 | 74.9 | 71.3 | **80.1** |
| MMMU (val) | 69.1 | 74.8 | 64.8 | **77.3** | 70.3 | 70.0 | 61.7 | 64.0 |
| MMMU-Pro (avg) | **51.7** | 51.1 | - | - | - | - | 43.0 | 46.3 |
| VideoMMMU | 61.1 | 60.2 | 61.8 | - | - | - | 55.5 | **65.2** |

Key takeaways from Table 4:
- **Kimi-VL-Thinking significantly improves over base model:** +15.4pp on MathVision (21.4% -> 36.8%), +4.7pp on MMMU (57.0% -> 61.7%), +2.6pp on MathVista (68.7% -> 71.3%) (Section 4.2)
- **Thinking-2506 provides massive further gains:** +20.1pp over Thinking on MathVision (36.8% -> 56.9%), +8.8pp on MathVista (71.3% -> 80.1%) (Section 4.3)
- **Thinking-2506 reduces token consumption by ~20%:** 2.9K -> 2.4K average tokens on MMMU-val, 5.8K -> 4.4K on MathVision (Section 4.3)
- **MMMU remains below frontier:** 64.0% vs o1-1217's 77.3% and Qwen2.5-VL-72B's 74.8%

#### Kimi-VL-Thinking-2506 Non-Reasoning Benchmarks (Table 5)

| Benchmark | GPT-4o | Qwen2.5-VL-7B | Gemma3-12B-IT | Kimi-VL-Instruct | Kimi-VL-Thinking | Kimi-VL-Thinking-2506 |
|-----------|--------|---------------|---------------|------------------|------------------|----------------------|
| MMBench-EN-v1.1 | 83.1 | 83.2 | 74.6 | 82.9 | 76.0 | **84.4** |
| RealWorldQA | 75.4 | 68.5 | 59.1 | 68.1 | 64.0 | **70.0** |
| OCRBench | 815 | 864 | 702 | 864 | 864 | **869** |
| MMStar | 64.0 | 63.0 | 56.1 | 61.7 | 64.2 | **70.4** |
| MMVet | 69.1 | 67.1 | 64.9 | 66.7 | 69.5 | **78.1** |
| MMVU (val) | 67.4 | 50.1 | 57.0 | 52.7 | 53.0 | **57.5** |
| Video-MME (w/ sub) | **77.2** | 71.6 | 62.1 | 72.7 | 66.0 | 71.9 |
| ScreenSpot-Pro | 0.8 | 29.0 | - | 35.4 | - | **52.8** |
| ScreenSpot-V2 | 18.1 | 84.2 | - | **92.8** | - | 91.4 |
| OSWorld-G | - | 31.5 | - | 41.6 | - | **52.5** |
| MMLongBench-Doc | 42.8 | 29.6 | 21.3 | 35.1 | 32.5 | **42.1** |

Key takeaways from Table 5:
- **Thinking-2506 recovers general abilities lost in Thinking:** MMBench 84.4% vs 76.0% (Thinking) and 82.9% (Instruct); MMVet 78.1% vs 69.5% and 66.7% (Section 4.3)
- **High-resolution MoonViT (3.2M pixels) drives OS grounding gains:** ScreenSpot-Pro 52.8% (+17.4pp over Instruct's 35.4%), OSWorld-G 52.5% (+10.9pp over Instruct's 41.6%)
- **MMLongBench-Doc:** 42.1% is the first open-source model matching GPT-4o (42.8%), a 7pp improvement over Instruct
- **Token efficiency on MMBench:** Only 180 tokens per answer average, 1/3 of previous thinking model, while improving 8.4pp accuracy

#### Test-Time Scaling (Figure 13)

Increasing max thinking length from 1K to 16K tokens (Kimi-VL-Thinking):

| Max Tokens | MathVision | MathVista | MMMU |
|------------|-----------|-----------|------|
| 1K | 18.7% | 66.7% | 49.2% |
| 2K | 22.6% | 69.0% | 52.4% |
| 4K | 29.0% | 70.9% | 56.2% |
| 8K | 34.0% | 70.6% | 60.1% |
| 16K | 36.8% | 71.3% | 61.7% |

- **MathVision:** Steady increase across all token lengths (+18.1pp from 1K to 16K)
- **MMMU:** Consistent improvement (+12.5pp from 1K to 16K)
- **MathVista:** Saturates at ~4K tokens (70.9%), with no significant gains from 4K to 16K (limited evidence -- single model, no variance reported)

---

## Limitations and Failure Modes

The authors explicitly acknowledge several limitations (Section 5):

1. **Model scale limitations.** The 2.8B activated parameter scale is insufficient for highly specialized or domain-specific problems that require strong language abilities.

2. **Reasoning ceiling not reached.** While reasoning capability is strong for typical use cases, it has not reached its theoretical upper bound for intricate tasks requiring multi-step inference or deeper contextual understanding.

3. **Long-context limitations despite 128K window.** Due to limited parameters in attention layers (comparable to a 3B model), long-context abilities are insufficient for certain advanced applications involving extremely long sequences.

4. **NIAH degradation at 64K-128K.** Text haystack recall drops to 87.0% and video to 91.7% at the 64K-128K range (Table 2), indicating incomplete utilization of the full 128K window.

5. **MathVista test-time scaling saturation.** Performance saturates at ~4K thinking tokens on MathVista (Figure 13), suggesting the reasoning depth needed is already captured within a short context for this benchmark.

6. **MathVision weakness in base model.** Kimi-VL-A3B scores only 21.4% on MathVision, below Gemma-3-12B-IT (32.1%) and Qwen2.5-VL-7B (25.1%) (Table 3), though this is substantially improved by the Thinking variants.

7. **[Inferred] No ablation isolating MoE vs dense architecture contribution.** The ~60% throughput claim (Section 2.5) is stated without detailed methodology; there is no controlled comparison isolating the MoE architecture's contribution to accuracy vs. efficiency.

8. **[Inferred] Limited language evaluation.** No standalone language benchmarks (e.g., MMLU, HumanEval) are reported, despite the claim of preserving text abilities through joint training.

### Scope and Comparability

- **What was not tested:** Models larger than 16B total parameters in the base model comparison (Table 3); dense VLM baselines with equivalent FLOPs; detailed ablations on MoE routing for vision vs. text tokens; standalone language-only benchmarks; evaluation beyond 128K context; non-English multimodal benchmarks.
- **Comparability notes:** OSWorld results for GPT-4o use Omniparser without UIA (Bonatti et al., 2024). Some competing models lack results on certain benchmarks due to context length or capability limitations (marked as "-" in tables). DeepSeek-VL2 comparison is limited because it supports only 4K context, excluding long-context benchmarks. Table 3 notes that GPT-4o results are listed "for reference" (proprietary, non-reproducible). The paper compares Kimi-VL-Thinking-2506 against non-thinking baselines in Table 5, which conflates reasoning enhancements with perception improvements.

---

## Conclusions

### Contributions

1. **Efficient MoE vision-language model.** Kimi-VL-A3B achieves competitive performance across 24 benchmarks with only 2.8B+0.4B activated parameters (16B total), outperforming Qwen2.5-VL-7B (8.3B activated) on 19/24 benchmarks and matching GPT-4o on MMBench (Table 3, Section 4.1).

2. **Native-resolution vision encoding.** MoonViT processes images at original resolutions using NaViT packing and 2D RoPE, eliminating sub-image splitting. Achieves 83.2% on InfoVQA, 867 on OCRBench, and 34.5% on ScreenSpot-Pro (Table 3).

3. **128K multimodal context.** RoPE frequency scaling (50K to 800K) in two 4x sub-stages enables 128K context with high NIAH recall (87-100% across lengths), supporting hour-long video understanding: 74.2% on MLVU, 64.5% on LongVideoBench (Table 2, Table 3).

4. **Long-CoT reasoning via SFT and RL.** Kimi-VL-Thinking-2506 achieves 56.9% on MathVision and 80.1% on MathVista with test-time scaling, while maintaining general perception (84.4% MMBench) and reducing token consumption by ~20% (Table 4, Table 5, Section 4.3).

5. **Strong agent capabilities.** 8.22% on OSWorld and 10.4% on WindowsAgentArena surpass GPT-4o, demonstrating multi-turn GUI agent interaction abilities with 92.8% grounding accuracy on ScreenSpot-V2 (Table 3).

6. **Integrated thinking model (Thinking-2506).** Demonstrates that reasoning abilities and general perception can coexist: 42.1% on MMLongBench-Doc (matching GPT-4o), 52.8% on ScreenSpot-Pro, and 65.2% on VideoMMMU, all from a 2.8B-activated model (Table 5, Section 4.3).

### Implications

1. **MoE enables efficient multimodal scaling.** The ~60% throughput gain over 7B dense VLMs suggests MoE may be preferable for VLMs, though this is a single internal comparison without detailed methodology (limited evidence).

2. **Joint training preserves text capabilities.** The progressive multimodal ratio and joint training stages maintain language model capabilities while adding vision (Section 2.3), though no ablation isolates this effect (no direct evidence).

3. **Test-time scaling transfers to multimodal.** The Thinking variant demonstrates that language-model test-time scaling techniques (long-CoT, RL) apply to vision-language tasks, with up to 18.1pp absolute improvement on MathVision (Figure 13). However, benefit varies by benchmark (MathVista saturates early).

4. **Native resolution outperforms sub-image splitting for diverse inputs.** MoonViT's NaViT-based approach handles everything from small images to high-resolution screenshots to long videos within a single architecture, achieving top results on OCR and agent grounding benchmarks (Table 3).

---

## Key Claims

1. **Kimi-VL-A3B matches or exceeds larger dense VLMs across diverse benchmarks.** Achieves 83.1% on MMBench (matches GPT-4o), 68.7% on MathVista (exceeds GPT-4o's 63.8%), 83.2% on InfoVQA (exceeds GPT-4o's 80.7%), and 84.9% on AI2D (exceeds GPT-4o's 84.6%), with only 2.8B+0.4B activated parameters. Outperforms Qwen2.5-VL-7B on 19/24 benchmarks. Evidence: Table 3, Section 4.1. Status: **supported** (tested across 24 benchmarks against 6 baselines -- strong evidence breadth). Scope: zero-shot evaluation on standard benchmarks. Magnitude: 83.1% MMBench, 68.7% MathVista, 83.2% InfoVQA.

2. **OSWorld performance exceeds GPT-4o.** 8.22% vs 5.03% on multi-turn agent interaction; also 10.4% vs 9.4% on WindowsAgentArena. Evidence: Table 3, Section 4.1.5. Status: **supported** (two agent benchmarks, consistent direction -- moderate evidence). Scope: GPT-4o uses Omniparser without UIA; limited open-source baselines report results. Magnitude: +3.19pp on OSWorld, +1.0pp on WindowsAgentArena.

3. **128K context achieved via RoPE frequency scaling.** Base frequency increased from 50K to 800K in two 4x sub-stages with 25% long data + 75% replay. NIAH recall: 100% up to 64K, 87.0%/91.7% at 64K-128K for text/video. Evidence: Table 2, Section 2.3. Status: **supported** (tested on both text and video haystacks -- moderate evidence, but no comparison to other context extension methods). Scope: text and video haystacks tested; no downstream long-context benchmark comparison against alternatives. Magnitude: 87.0% text / 91.7% video recall at 64K-128K.

4. **Kimi-VL-Thinking-2506 competitive with 72B models on reasoning.** 56.9% on MathVision exceeds QVQ-72B-Preview (35.9%) and Kimi-k1.5 (38.6%) with ~25x fewer activated parameters. Evidence: Table 4, Figure 1. Status: **supported** (5 reasoning benchmarks compared against 10 baselines -- strong evidence). Scope: with long-CoT and RL training, MoonViT extended to 3.2M pixels. Magnitude: 56.9% MathVision, 80.1% MathVista, 64.0% MMMU, 65.2% VideoMMMU.

5. **Training throughput ~60% higher than 7B dense VLM.** Evidence: Section 2.5. Status: **unvalidated** (single qualitative claim, no detailed methodology, hardware specs, or controlled comparison provided -- limited evidence). Scope: internal comparison against VLMs based on Qwen2.5-7B. Magnitude: ~60% (approximate, unverified).

6. **Test-time scaling effective for multimodal reasoning.** MathVision accuracy improves from 18.7% to 36.8% (+18.1pp) when scaling thinking tokens from 1K to 16K. MMMU improves from 49.2% to 61.7% (+12.5pp). MathVista saturates at ~4K tokens. Evidence: Figure 13, Section 4.2. Status: **supported** (3 benchmarks, consistent for MathVision and MMMU -- moderate evidence; single model, no variance reported). Scope: Kimi-VL-Thinking variant only; benefit varies by benchmark. Magnitude: +18.1pp MathVision, +12.5pp MMMU, +4.6pp MathVista (saturating).

7. **Thinking-2506 integrates reasoning with general perception.** Achieves 84.4% on MMBench (+8.4pp over Thinking), 42.1% on MMLongBench-Doc (first open-source model matching GPT-4o at 42.8%), 52.8% on ScreenSpot-Pro (+17.4pp over Instruct), while reducing average output tokens by ~20%. Evidence: Table 5, Section 4.3. Status: **supported** (11 benchmarks comparing 3 model variants -- moderate evidence). Scope: compared to Kimi-VL-Instruct and Kimi-VL-Thinking. Magnitude: 84.4% MMBench, 42.1% MMLongBench-Doc, 52.8% ScreenSpot-Pro; token reduction 2.9K->2.4K MMMU, 5.8K->4.4K MathVision.

---

## Open Questions

1. **MoE routing for vision tokens.** How does the expert routing behave differently for vision tokens versus text tokens? The paper does not analyze routing patterns, leaving open whether MoE experts specialize by modality.

2. **Performance beyond 128K.** What happens at longer contexts? NIAH already shows degradation at 64K-128K (87-91.7% vs 100% at shorter lengths), and the authors acknowledge attention layer parameters limit long-context ability (Section 5).

3. **Scaling to larger MoE configurations.** Would the training recipe (joint stages, progressive multimodal ratio, RoPE frequency scaling) transfer to 70B+ total parameter models?

4. **Vision encoder training vs. freezing.** Unlike Gemma 3's frozen encoder, Kimi-VL trains MoonViT jointly throughout. What is the impact on vision-language integration depth, and what is the risk of catastrophic forgetting of pre-trained visual features?

5. **RL reward design for multimodal.** The paper uses binary correctness rewards (r in {0, 1}). Would denser or more nuanced reward signals improve multimodal reasoning training beyond the current approach?

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Su et al. (2023)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Rotary positional embeddings used in both the vision encoder (2D RoPE) and language model, and extended via base frequency scaling for 128K context.
- **Zhai et al. (2023)** -- *SigLIP: Sigmoid Loss for Language Image Pre-Training.* MoonViT initialized from SigLIP-SO-400M; SigLIP loss used in ViT training stage.
- **Dehghani et al. (2023)** -- *NaViT: Patch n' Pack.* Packing method for native-resolution vision processing enabling variable-resolution batch handling.
- **DeepSeek-AI (2025)** -- *DeepSeek-V3 Technical Report.* MoE architecture that Moonlight (Kimi-VL's LLM backbone) is based on.
- **Liu et al. (2025a)** -- *Moonlight / Muon is Scalable for LLM Training.* Base MoE language model providing the 2.8B-activated/16B-total backbone and Muon optimizer.

### Vision-Language Models

- **Wu et al. (2024)** -- *DeepSeek-VL2.* Prior MoE VLM comparison; limited to 4K context.
- **Li et al. (2024)** -- *LLaVA-OneVision.* Sub-image splitting approach that MoonViT explicitly avoids.
- **Bai et al. (2025)** -- *Qwen2.5-VL Technical Report.* Primary dense VLM comparison baseline across 24 benchmarks.
- **Gemma Team (2025)** -- *Gemma 3 Technical Report.* Concurrent multimodal model with 128K context using local-global attention interleaving and frozen vision encoder.
- **Li et al. (2024)** -- *Aria.* Early MoE VLM that falls short in fine-grained visual tasks.

### Training Methods

- **Yu et al. (2022)** -- *CoCa: Contrastive Captioners are Image-Text Foundation Models.* CoCa-style loss formulation (contrastive + captioning) used for ViT training stage.
- **Dao et al. (2022)** -- *FlashAttention.* Enables efficient variable-length sequence attention in both MoonViT and context parallelism.
- **Jordan et al. (2024)** -- *Muon optimizer.* Base optimizer enhanced with weight decay and distributed implementation for Kimi-VL training.
- **Rajbhandari et al. (2020)** -- *ZeRO: Memory Optimizations.* Memory optimization strategy for distributed training (ZeRO-1) and distributed Muon implementation.
- **Kimi Team (2025)** -- *Kimi k1.5: Scaling Reinforcement Learning with LLMs.* RL algorithm (online policy mirror descent) and long-CoT approach adopted for Thinking variant.

### Parallelism and Infrastructure

- **Fedus et al. (2022)** -- *Switch Transformers.* Expert parallelism strategy for distributing MoE layers.
- **Narayanan et al. (2021)** -- *Megatron-LM.* Pipeline parallelism for efficient large-scale training.
- **Jacobs et al. (2023)** -- *DeepSpeed Ulysses.* Context parallelism for long-sequence training.
- **Chen et al. (2016)** -- *Training Deep Nets with Sublinear Memory Cost.* Selective checkpointing activation.
- **Korthikanti et al. (2022)** -- *Reducing Activation Recomputation.* Selective checkpointing strategy.

### Evaluation Benchmarks

- **Yue et al. (2024)** -- *MMMU.* College-level multimodal understanding benchmark.
- **Xie et al. (2024)** -- *OSWorld.* Multi-turn agent interaction benchmark in real computer environments.
- **Wu et al. (2024)** -- *LongVideoBench.* Long video understanding benchmark.
- **Mangalam et al. (2023)** -- *EgoSchema.* Long-form egocentric video QA benchmark.
- **Wang et al. (2024)** -- *MathVision.* Mathematical reasoning benchmark where Thinking-2506 achieves 56.9%.
- **Lu et al. (2023)** -- *MathVista.* Mathematical reasoning in visual contexts.
- **Bonatti et al. (2024)** -- *WindowsAgentArena.* Multi-modal OS agent evaluation benchmark.
