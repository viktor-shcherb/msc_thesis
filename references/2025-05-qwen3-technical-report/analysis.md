---
title: "Qwen3 Technical Report"
authors: "Qwen Team"
year: 2025
venue: "arXiv preprint 2505.09388"
paper_type: preprint
categories: ["model-release", "architecture", "context-extension", "in-context-learning", "reasoning-evaluation"]
scope: ["open foundation models", "multilingual LLMs", "mixture-of-experts", "thinking modes", "reasoning models", "strong-to-weak distillation", "reinforcement learning"]
benchmarks_used: ["mmlu", "mmlu-pro", "gpqa", "humaneval", "mbpp", "gsm8k", "math-hendrycks", "bbh", "hellaswag", "winogrande", "truthfulqa", "arc", "ifeval", "mgsm", "ruler", "mt-bench", "arena-hard", "livecodebench", "evalplus", "multipl-e", "c-eval", "cmmlu"]
models_introduced: ["qwen3-0.6b", "qwen3-1.7b", "qwen3-4b", "qwen3-8b", "qwen3-14b", "qwen3-32b", "qwen3-30b-a3b", "qwen3-235b-a22b"]
models_evaluated: ["deepseek-r1", "deepseek-v3", "llama-4-maverick", "llama-4-scout", "gpt-4o", "gemini-2.5-pro", "qwen2.5-72b", "qwq-32b", "gemma-3-27b"]
key_claims:
  - id: C1
    claim: "Qwen3-235B-A22B outperforms DeepSeek-V3 Base on 14/15 benchmarks with only 1/3 total parameters and 2/3 activated parameters"
    evidence: "Table 3, Section 3.3"
    status: supported
  - id: C2
    claim: "Qwen3 MoE models achieve similar performance to Qwen3 dense models with only 1/5 activated parameters"
    evidence: "Section 3.3"
    status: supported
  - id: C3
    claim: "Qwen3 dense models match Qwen2.5 performance at higher parameter scales (e.g., Qwen3-8B matches Qwen2.5-14B)"
    evidence: "Tables 4-8, Section 3.3"
    status: supported
  - id: C4
    claim: "Qwen3-235B-A22B achieves 85.7 on AIME'24 and 81.5 on AIME'25 in thinking mode, competitive with o1 and Gemini2.5-Pro"
    evidence: "Table 11, Section 4.6"
    status: supported
  - id: C5
    claim: "Strong-to-weak distillation requires only 1/10 GPU hours compared to four-stage training while achieving better performance"
    evidence: "Table 21, Section 4.7"
    status: supported
  - id: C6
    claim: "Increasing thinking budget leads to consistent performance improvements across various tasks"
    evidence: "Figure 2, Section 4.7"
    status: supported
  - id: C7
    claim: "On-policy distillation achieves +7.4 AIME'24 and +10.0 AIME'25 over off-policy distillation with 1/10 GPU hours vs RL"
    evidence: "Table 21, Section 4.7"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Builds on decoder-only Transformer with GQA, SwiGLU, RoPE, QK-Norm, RMSNorm, and pre-normalization"
  - target: 2024-07-qwen2-technical-report
    type: extends
    detail: "Direct successor to Qwen2, scaling pre-training from 7T to 36T tokens and adding thinking/non-thinking mode fusion"
  - target: 2024-05-yarn-context-extension
    type: extends
    detail: "Uses YARN with DCA to achieve 4x context length extrapolation during inference (32K to 128K)"
  - target: 2023-11-needle-in-a-haystack
    type: uses-benchmark
    detail: "Evaluates long-context retrieval via RULER benchmark up to 128K tokens"
  - target: 2025-07-kimi-k2-open-agentic-intelligence
    type: concurrent
    detail: "Concurrent open-source MoE release; Kimi K2 outperforms Qwen3 on agentic benchmarks (SWE-bench, τ²-bench) in non-thinking mode"
open_questions:
  - question: "Can thinking mode performance degradation in long-context tasks be addressed while maintaining reasoning benefits?"
    addressed_by: null
  - question: "Does the thinking/non-thinking mode fusion trade-off (slight degradation on AIME/LiveCodeBench) scale with model size?"
    addressed_by: null
  - question: "Can strong-to-weak distillation be applied across different model families or is it specific to Qwen?"
    addressed_by: null
  - question: "What is the optimal thinking budget allocation strategy across different task types?"
    addressed_by: null
---

# Qwen3 Technical Report

**Authors:** Qwen Team (An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, et al., Alibaba Group)
**Date:** May 2025, arXiv:2505.09388

---

## Core Research Problem

Large language models have made significant progress toward artificial general intelligence, with both proprietary models (GPT-4o, Claude 3.7, Gemini 2.5) and open-weight models (DeepSeek-V3, Llama-4, Qwen2.5) demonstrating strong capabilities. However, several challenges remain:

1. **Model deployment flexibility:** Users need both fast, chat-optimized models for simple queries and dedicated reasoning models for complex tasks, requiring deployment of separate model variants (e.g., Qwen2.5 for chat, QwQ-32B for reasoning).

2. **Inference-time compute control:** Recent reasoning models (o3, DeepSeek-R1) show that extended thinking improves performance, but users lack fine-grained control over computational resources allocated to reasoning.

3. **Training efficiency for smaller models:** Building competitive lightweight models requires extensive four-stage post-training pipelines, consuming significant computational resources.

4. **Multilingual coverage:** Previous Qwen2.5 supported 29 languages; broader language support is needed for global deployment.

**The core challenge: how to build a unified model family that integrates thinking and non-thinking modes with controllable inference-time compute, while efficiently training models across scales from 0.6B to 235B parameters with expanded multilingual capabilities.**

---

## Problem Solutions

Qwen3 addresses these challenges through several key innovations:

1. **Unified thinking/non-thinking modes:** A single model supports both extended reasoning (thinking mode with `<think>` blocks) and rapid responses (non-thinking mode), controllable via chat template flags (`/think` and `/no_think`).

2. **Thinking budget mechanism:** Users can allocate computational resources adaptively by setting a token budget for the thinking process, enabling fine-grained latency-performance trade-offs.

3. **Strong-to-weak distillation:** Large flagship models (Qwen3-32B, Qwen3-235B-A22B) distill knowledge to smaller models, reducing post-training compute by 10x while improving performance.

4. **Expanded pre-training:** 36 trillion tokens covering 119 languages and dialects, with synthetic data generation using Qwen2.5-VL, Qwen2.5-Math, and Qwen2.5-Coder.

5. **Four-stage post-training:** Long-CoT cold start, Reasoning RL, Thinking Mode Fusion, and General RL progressively build reasoning and general capabilities.

---

## Approach Details

### Method

#### Dense Model Architecture

Qwen3 dense models are decoder-only Transformers with causal attention. Key architectural choices:

- **Grouped Query Attention (GQA):** All sizes use GQA (Ainslie et al., 2023). KV head count is 8 for all models.
- **QK-Norm:** Introduced to ensure stable training, replacing the QKV-bias used in Qwen2.
- **Other components:** SwiGLU activation, RoPE positional embeddings, RMSNorm with pre-normalization.

| Model | Layers | Heads (Q/KV) | Tie Embedding | Context Length |
|---|---|---|---|---|
| Qwen3-0.6B | 28 | 16/8 | Yes | 32K |
| Qwen3-1.7B | 28 | 16/8 | Yes | 32K |
| Qwen3-4B | 36 | 32/8 | Yes | 128K |
| Qwen3-8B | 36 | 32/8 | No | 128K |
| Qwen3-14B | 40 | 40/8 | No | 128K |
| Qwen3-32B | 64 | 64/8 | No | 128K |

#### MoE Architecture

Qwen3 MoE models use fine-grained expert segmentation with 128 total experts and 8 activated per token:

| Model | Layers | Heads (Q/KV) | Experts (Total/Activated) | Context Length |
|---|---|---|---|---|
| Qwen3-30B-A3B | 48 | 32/4 | 128/8 | 128K |
| Qwen3-235B-A22B | 94 | 64/4 | 128/8 | 128K |

Key MoE design differences from Qwen2.5-MoE:
- **No shared experts:** Unlike Qwen2.5-MoE, shared experts are removed.
- **Global-batch load balancing loss:** Encourages expert specialization (Qiu et al., 2025).

#### Tokenizer

Byte-level byte-pair encoding (BBPE) tokenizer with vocabulary size of 151,669.

---

### Key Technical Components

#### Pre-training Data

The pre-training corpus consists of **36 trillion tokens** covering **119 languages and dialects**:

- **Data expansion pipeline:** Qwen2.5-VL performs OCR on PDF documents; Qwen2.5 refines the extracted text. Qwen2.5-Math and Qwen2.5-Coder synthesize domain-specific data.
- **Multilingual data annotation system:** Annotates >30T tokens across educational value, fields, domains, and safety dimensions.
- **Instance-level data mixing:** Unlike prior work optimizing at source/domain level, Qwen3 optimizes data mixture at instance level using fine-grained labels.

#### Three-Stage Pre-training

1. **General Stage (S1):** >30T tokens at sequence length 4,096. Covers 119 languages and dialects.
2. **Reasoning Stage (S2):** ~5T higher-quality tokens emphasizing STEM, coding, reasoning, and synthetic data. Accelerated learning rate decay.
3. **Long Context Stage:** Hundreds of billions of tokens at sequence length 32,768. RoPE base frequency increased from 10,000 to 1,000,000 using ABF (Xiong et al., 2023). YARN + DCA enable 4x extrapolation to 128K during inference.

#### Four-Stage Post-training

**Stage 1: Long-CoT Cold Start**
- Comprehensive dataset spanning math, code, logical reasoning, and STEM with verified answers.
- Two-phase filtering: query filtering (remove unverifiable, too-easy queries) and response filtering (remove incorrect, repetitive, guessing responses).
- QwQ-32B generates N candidate responses; human annotators assess hard cases.
- Minimal training samples/steps to avoid limiting RL potential.

**Stage 2: Reasoning RL**
- 3,995 query-verifier pairs satisfying: (1) not used in cold-start, (2) learnable, (3) challenging, (4) broad domain coverage.
- GRPO (Shao et al., 2024) with large batch size and high rollouts per query.
- Off-policy training for sample efficiency.
- Entropy control for exploration-exploitation balance.
- Result: AIME'24 score increases from 70.1 to 85.1 over 170 RL steps.

**Stage 3: Thinking Mode Fusion**
- Continual SFT on Reasoning RL model with both thinking and non-thinking data.
- Chat template with `/think` and `/no_think` flags; non-thinking mode uses empty `<think></think>` block.
- **Thinking Budget:** When thinking length reaches threshold, insert stop instruction: "Considering the limited time by the user, I have to give the solution based on the thinking directly now.\n</think>.\n\n"

**Stage 4: General RL**
- Reward system covering >20 tasks: instruction following, format following, preference alignment, agent ability, specialized scenarios (RAG).
- Three reward types: (1) Rule-based, (2) Model-based with reference answer, (3) Model-based without reference answer (reward model).

#### Strong-to-Weak Distillation

For lightweight models (0.6B, 1.7B, 4B, 8B, 14B dense; 30B-A3B MoE):

1. **Off-policy Distillation:** Response distillation from teacher outputs in both `/think` and `/no_think` modes.
2. **On-policy Distillation:** Student generates on-policy sequences; fine-tune by minimizing KL divergence with teacher (Qwen3-32B or Qwen3-235B-A22B) logits.

---

### Experimental Setup

**Base model evaluation (15 benchmarks):**
- General: MMLU (5-shot), MMLU-Pro (5-shot CoT), MMLU-Redux (5-shot), BBH (3-shot CoT), SuperGPQA (5-shot CoT)
- Math & STEM: GPQA (5-shot CoT), GSM8K (4-shot CoT), MATH (4-shot CoT)
- Coding: EvalPlus (0-shot), MultiPL-E (0-shot), MBPP-3shot, CRUX-O (1-shot)
- Multilingual: MGSM (8-shot CoT), MMMLU (5-shot), INCLUDE (5-shot)

**Post-trained model evaluation:**
- General: MMLU-Redux, GPQA-Diamond (10 samples), C-Eval, LiveBench (2024-11-25)
- Alignment: IFEval (strict-prompt), Arena-Hard, AlignBench v1.1, Creative Writing V3, WritingBench
- Math & Reasoning: MATH-500, AIME'24, AIME'25 (64 samples per question), ZebraLogic, AutoLogi
- Agent & Coding: BFCL v3, LiveCodeBench v5 (2024.10-2025.02), CodeForces (CodeElo)
- Multilingual: Multi-IF (8 languages), INCLUDE (44 languages), MMMLU (14 languages), MT-AIME2024 (55 languages), PolyMath (18 languages), MLogiQA (10 languages)

**Baselines:**
- Thinking mode: OpenAI-o1, DeepSeek-R1, Grok-3-Beta (Think), Gemini2.5-Pro, QwQ-32B
- Non-thinking mode: GPT-4o-2024-11-20, DeepSeek-V3, Qwen2.5-72B-Instruct, Llama-4-Maverick

**Sampling hyperparameters:**
- Thinking mode: temperature=0.6, top-p=0.95, top-k=20
- Non-thinking mode: temperature=0.7, top-p=0.8, top-k=20, presence_penalty=1.5
- Max output: 32,768 tokens (38,912 for AIME)

---

### Key Results

#### Base Model: Qwen3-235B-A22B-Base vs 70B+ Baselines

| Benchmark | Qwen2.5-72B | DeepSeek-V3 | Llama-4-Maverick | **Qwen3-235B-A22B** |
|---|---|---|---|---|
| Architecture | Dense | MoE | MoE | MoE |
| Total/Activated Params | 72B/72B | 671B/37B | 402B/17B | **235B/22B** |
| MMLU | 86.06 | 87.19 | 85.16 | **87.81** |
| MMLU-Pro | 58.07 | 59.84 | 63.91 | **68.18** |
| GPQA | 45.88 | 41.92 | 43.94 | **47.47** |
| GSM8K | 91.50 | 87.57 | 87.72 | **94.39** |
| MATH | 62.12 | 62.62 | 63.32 | **71.84** |
| EvalPlus | 65.93 | 63.75 | 68.38 | **77.60** |
| MultiPL-E | 58.70 | 62.26 | 57.28 | **65.94** |

- Outperforms DeepSeek-V3-Base on 14/15 benchmarks with 1/3 total parameters and 2/3 activated parameters (Table 3, Section 3.3).
- Largest gains in coding (+13.85 EvalPlus vs DeepSeek-V3) and math (+9.22 MATH vs DeepSeek-V3).

#### Parameter Efficiency: Dense vs MoE

| Comparison | Result |
|---|---|
| Qwen3 MoE vs Qwen3 Dense | Similar performance with 1/5 activated parameters |
| Qwen3-30B-A3B (3B activated) vs Qwen2.5-14B (14B) | Outperforms on all tasks |
| Qwen3-235B-A22B (22B activated) vs Qwen2.5-72B (72B) | Surpasses on all benchmarks with <1/3 activated params |

#### Post-trained: Qwen3-235B-A22B Thinking Mode vs Reasoning Baselines

| Benchmark | OpenAI-o1 | DeepSeek-R1 | Gemini2.5-Pro | **Qwen3-235B-A22B** |
|---|---|---|---|---|
| AIME'24 | 74.3 | 79.8 | 92.0 | **85.7** |
| AIME'25 | 79.2 | 70.0 | 86.7 | **81.5** |
| LiveCodeBench v5 | 63.9 | 64.3 | 70.4 | **70.7** |
| CodeForces | 1891/96.7% | 2029/98.1% | 2001/97.9% | **2056/98.2%** |
| BFCL v3 | 67.8 | 56.9 | 62.9 | **70.8** |
| MT-AIME2024 | 67.4 | 73.5 | 76.9 | **80.8** |

- Outperforms DeepSeek-R1 on 17/23 benchmarks with 60% activated and 35% total parameters (Table 11).

#### Post-trained: Qwen3-235B-A22B Non-thinking Mode vs Non-reasoning Baselines

| Benchmark | GPT-4o | DeepSeek-V3 | Llama-4-Maverick | **Qwen3-235B-A22B** |
|---|---|---|---|---|
| MATH-500 | 77.2 | 90.2 | 90.6 | **91.2** |
| AIME'24 | 11.1 | 39.2 | 38.5 | **40.1** |
| Arena-Hard | 85.3 | 85.5 | 82.7 | **96.1** |
| CodeForces | 864/35.4% | 1134/54.1% | 712/24.3% | **1387/75.7%** |

- Surpasses GPT-4o on 18/23 benchmarks (Table 12).

#### Thinking Budget Scaling (Figure 2)

Performance improves consistently with increased thinking budget across AIME'24, AIME'25, LiveCodeBench v5, and GPQA-Diamond. Scaling curves suggest further gains possible beyond 32K tokens.

#### Strong-to-Weak Distillation Efficiency (Table 21)

| Method | AIME'24 | AIME'25 | GPU Hours |
|---|---|---|---|
| Off-policy Distillation | 55.0 (90.0 pass@64) | 42.8 (83.3) | - |
| + Reinforcement Learning | 67.6 (90.0) | 55.5 (83.3) | 17,920 |
| + On-policy Distillation | **74.4 (93.3)** | **65.5 (86.7)** | **1,800** |

- On-policy distillation achieves +6.8 AIME'24 and +10.0 AIME'25 over RL with 10x fewer GPU hours.
- Distillation improves pass@64 (exploration capability); RL does not.

#### Long-Context Evaluation (RULER, Table 23)

| Model | 4K | 8K | 16K | 32K | 64K | 128K | Avg |
|---|---|---|---|---|---|---|---|
| Qwen2.5-72B-Instruct | 97.7 | 97.2 | 97.7 | 96.5 | 93.0 | 88.4 | 95.1 |
| Qwen3-235B-A22B (Non-thinking) | 97.7 | 97.2 | 96.4 | 95.1 | 93.3 | 90.6 | **95.0** |
| Qwen3-235B-A22B (Thinking) | 95.1 | 94.8 | 93.0 | 92.3 | 92.0 | 86.0 | 92.2 |

- Non-thinking mode outperforms Qwen2.5 at similar sizes.
- Thinking mode slightly degrades performance on retrieval tasks (thinking content may interfere).

---

## Limitations and Failure Modes

1. **Thinking mode degrades long-context retrieval:** On RULER benchmark, thinking mode underperforms non-thinking mode by 2-4 points across context lengths (Table 23). The authors hypothesize thinking content interferes with retrieval tasks that don't require reasoning.

2. **Thinking Mode Fusion reduces math/coding performance:** After Stages 3-4, AIME'24 drops from 83.8 to 81.4 and LiveCodeBench from 68.4 to 65.7 in thinking mode (Table 22). The authors attribute this to training on broader general tasks compromising specialized capabilities.

3. **IFEval performance gap:** Qwen3-235B-A22B achieves 83.4 on IFEval strict-prompt vs 92.6 for OpenAI-o1 and 89.5 for Gemini2.5-Pro (Table 11).

4. **Limited training detail disclosure:** Specific learning rates, optimizer configurations, batch sizes, and total compute costs are not disclosed.

5. **MoE inference overhead:** While activated parameters are fewer, MoE models require all 235B parameters to be loaded, limiting deployment to high-memory systems.

6. **Multilingual gaps at small scales:** Qwen3-0.6B and Qwen3-1.7B show substantial drops on multilingual benchmarks compared to larger models (Tables 19-20).

---

## Conclusions

### Contributions

1. **Unified thinking/non-thinking framework.** Integration of reasoning and chat modes into a single model family with `/think` and `/no_think` control, eliminating the need for separate model deployments.

2. **Thinking budget mechanism.** Users can control inference-time compute allocation, with demonstrated smooth performance scaling as budget increases (Figure 2).

3. **Strong-to-weak distillation.** Teacher logit distillation achieves 10x training efficiency over RL while improving both immediate (Pass@1) and exploration (Pass@64) performance.

4. **State-of-the-art open-weight models.** Qwen3-235B-A22B outperforms DeepSeek-R1 on 17/23 benchmarks in thinking mode and DeepSeek-V3 on 14/15 base model benchmarks.

5. **Parameter-efficient MoE design.** Qwen3 MoE matches dense model performance with 1/5 activated parameters; Qwen3-235B-A22B surpasses Qwen2.5-72B with <1/3 activated parameters.

6. **Expanded multilingual support.** Coverage increased from 29 to 119 languages and dialects, with competitive performance on MT-AIME2024 (55 languages) and PolyMath (18 languages).

7. **Data scaling to 36T tokens.** Pre-training corpus doubled from Qwen2.5 with synthetic data generation via Qwen2.5-VL, Qwen2.5-Math, and Qwen2.5-Coder.

### Implications

1. **Unified deployment reduces infrastructure complexity.** Organizations can deploy a single model for both chat and reasoning use cases, with mode switching controlled at inference time (speculative: this may become the standard approach for production LLM deployment).

2. **Distillation may outperform RL for smaller models.** The finding that on-policy distillation achieves better Pass@64 than RL suggests knowledge transfer from stronger teachers is more effective for building exploration capabilities than self-improvement.

3. **Thinking mode has task-specific trade-offs.** Extended reasoning helps math/coding but harms retrieval tasks, suggesting production systems may need automatic mode selection based on query type.

4. **MoE efficiency enables reasoning at scale.** The 22B activated parameters of Qwen3-235B-A22B match or exceed 72B dense models, making extended reasoning economically viable.

---

## Key Claims

1. **C1:** Qwen3-235B-A22B-Base outperforms DeepSeek-V3-Base on 14/15 evaluation benchmarks with only 1/3 total parameters (235B vs 671B) and 2/3 activated parameters (22B vs 37B) (Table 3, Section 3.3). Status: **supported**.

2. **C2:** Qwen3 MoE base models achieve similar performance to Qwen3 dense base models with only 1/5 activated parameters. This is demonstrated by Qwen3-30B-A3B (3B activated) matching Qwen3-14B (14B activated) performance (Table 5, Section 3.3). Status: **supported**.

3. **C3:** Qwen3 dense base models match Qwen2.5 performance at higher parameter scales: Qwen3-1.7B/4B/8B/14B/32B achieve comparable performance to Qwen2.5-3B/7B/14B/32B/72B respectively, especially on STEM, coding, and reasoning benchmarks (Tables 4-8, Section 3.3). Status: **supported**.

4. **C4:** Qwen3-235B-A22B (Thinking) achieves 85.7 on AIME'24 and 81.5 on AIME'25, competitive with OpenAI-o1 (74.3, 79.2) and DeepSeek-R1 (79.8, 70.0), though below Gemini2.5-Pro (92.0, 86.7) (Table 11, Section 4.6). Status: **supported**.

5. **C5:** Strong-to-weak distillation requires approximately 1/10 GPU hours compared to four-stage training (1,800 vs 17,920 GPU hours for Qwen3-8B) while achieving better performance (+6.8 AIME'24, +10.0 AIME'25) (Table 21, Section 4.7). Status: **supported**.

6. **C6:** Increasing thinking budget leads to consistent performance improvements across AIME'24, AIME'25, LiveCodeBench v5, and GPQA-Diamond, with smooth scaling curves up to 32K tokens (Figure 2, Section 4.7). Status: **supported**.

7. **C7:** On-policy distillation from teacher logits improves Pass@64 scores (exploration capability) from 90.0 to 93.3 on AIME'24, while reinforcement learning does not improve Pass@64 (Table 21, Section 4.7). Status: **supported**.

---

## Open Questions

1. **Long-context thinking performance.** Thinking mode slightly degrades RULER performance compared to non-thinking mode (Table 23). The authors commit to enhancing long-context capability in thinking mode in future versions, but the fundamental tension between reasoning overhead and retrieval efficiency remains unresolved.

2. **Thinking Mode Fusion trade-offs.** Stages 3-4 reduce specialized reasoning performance (AIME'24: 83.8 → 81.4) to improve general capabilities. Whether this trade-off can be mitigated while maintaining unified mode support is unclear.

3. **Cross-family distillation.** Strong-to-weak distillation is demonstrated within the Qwen family. Whether teacher-student knowledge transfer is equally effective across different model architectures (e.g., using Qwen3 to train Llama-style students) is not explored.

4. **Automatic thinking budget allocation.** The thinking budget mechanism requires user specification. Developing automatic strategies that allocate thinking tokens based on query complexity remains an open direction.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundation architecture. Qwen3 builds on the decoder-only Transformer with causal attention.
- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models.* Qwen3 adopts GQA across all model sizes with 8 KV heads.
- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Qwen3 uses RoPE with base frequency scaled from 10,000 to 1,000,000 for long-context training.
- **Dauphin et al. (2017)** -- *Language Modeling with Gated Convolutional Networks.* SwiGLU activation used in Qwen3.
- **Dehghani et al. (2023)** -- *Scaling Vision Transformers to 22 Billion Parameters.* QK-Norm introduced to ensure stable training in Qwen3.

### Context Extension

- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension.* Qwen3 employs YARN to achieve 4x context length extrapolation during inference.
- **An et al. (2024)** -- *Training-Free Long-Context Scaling.* Dual Chunk Attention (DCA) combined with YARN enables 128K inference context.
- **Xiong et al. (2023)** -- *Effective Long-Context Scaling of Foundation Models.* ABF technique for RoPE base frequency scaling adopted by Qwen3.

### Mixture-of-Experts

- **Dai et al. (2024)** -- *DeepSeekMoE: Towards Ultimate Expert Specialization.* Qwen3 MoE adopts fine-grained expert segmentation with 128 experts and 8 activated per token.
- **Qiu et al. (2025)** -- *Demons in the Detail: Load Balancing Loss.* Global-batch load balancing loss used to encourage expert specialization in Qwen3.

### Post-Training and Reasoning

- **Shao et al. (2024)** -- *DeepSeekMath: Pushing the Limits of Mathematical Reasoning.* GRPO algorithm used for Reasoning RL stage.
- **Guo et al. (2025)** -- *DeepSeek-R1: Incentivizing Reasoning via Reinforcement Learning.* Primary open-source reasoning baseline; demonstrates RL for inference-time scaling.
- **Qwen Team (2024, 2025)** -- *QwQ-32B.* Predecessor reasoning model; used for cold-start data generation in Qwen3 post-training.

### Competing Models

- **Liu et al. (2024)** -- *DeepSeek-V3 Technical Report.* Primary open-source MoE baseline; Qwen3-235B-A22B outperforms with 1/3 parameters.
- **Meta-AI (2025)** -- *Llama 4.* Llama-4-Maverick and Llama-4-Scout used as baselines for base and instruct evaluations.
- **Yang et al. (2024)** -- *Qwen2.5 Technical Report.* Direct predecessor; Qwen3 scales from 7T to 36T tokens and adds thinking mode.

### Evaluation Benchmarks

- **Hendrycks et al. (2021)** -- *Measuring Massive Multitask Language Understanding.* MMLU is the primary knowledge benchmark.
- **Rein et al. (2023)** -- *GPQA: Graduate-Level Q&A Benchmark.* Graduate-level STEM evaluation.
- **Jain et al. (2024)** -- *LiveCodeBench.* Contamination-free code evaluation.
- **AIME (2025)** -- *American Invitational Mathematics Examination.* Primary mathematical reasoning benchmark for thinking mode.
- **Hsieh et al. (2024)** -- *RULER.* Long-context evaluation up to 128K tokens.
