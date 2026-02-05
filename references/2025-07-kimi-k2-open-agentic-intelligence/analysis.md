---
title: "Kimi K2: Open Agentic Intelligence"
authors: "Kimi Team"
year: 2025
venue: "arXiv preprint 2507.20534"
paper_type: preprint
categories: ["model-release", "architecture", "in-context-learning", "attention-efficiency"]
scope: ["open foundation models", "mixture-of-experts", "agentic AI", "tool use", "reinforcement learning", "training optimization"]
benchmarks_used: ["mmlu", "mmlu-pro", "mmlu-redux", "gpqa", "humaneval", "mbpp", "gsm8k", "math-hendrycks", "bbh", "hellaswag", "winogrande", "truthfulqa", "arc", "ifeval", "livecodebench", "evalplus", "c-eval", "cmmlu", "longbench-v2"]
models_introduced: ["kimi-k2-base", "kimi-k2-instruct"]
models_evaluated: ["deepseek-v3", "qwen3-235b-a22b", "gpt-4o", "claude-3.5-sonnet", "llama-4-maverick", "gemini-2.5-pro"]
key_claims:
  - id: C1
    claim: "Kimi K2 achieves 65.8% on SWE-bench Verified (single attempt), outperforming most open- and closed-source baselines in non-thinking settings"
    evidence: "Table 3, Figure 1"
    status: supported
    scope: "non-thinking mode, agentic coding"
    magnitude: "65.8% vs 38.8% DeepSeek-V3-0324, 34.4% Qwen3-235B-A22B"
  - id: C2
    claim: "MuonClip enables stable pre-training on 15.5 trillion tokens with zero loss spikes"
    evidence: "Figure 3, Section 2.1"
    status: supported
    scope: "1T parameter MoE training"
  - id: C3
    claim: "Increasing MoE sparsity to 48 (384 total experts, 8 activated) reduces FLOPs by 1.69x compared to sparsity 8 for the same validation loss"
    evidence: "Figure 5, Section 2.3"
    status: supported
    scope: "compute-optimal sparsity scaling"
  - id: C4
    claim: "Kimi K2 ranks #1 among open-source models and #5 overall on LMSYS Arena leaderboard (July 17, 2025)"
    evidence: "Section 4.1.2"
    status: supported
    scope: "3000+ user votes"
  - id: C5
    claim: "Synthetic data rephrasing improves SimpleQA accuracy from 23.76% to 28.94% compared to raw multi-epoch training"
    evidence: "Table 1, Section 2.2"
    status: supported
    scope: "knowledge data augmentation"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Builds on Transformer architecture with MoE, Multi-head Latent Attention (MLA), and SwiGLU"
  - target: 2024-05-yarn-context-extension
    type: extends
    detail: "Uses YaRN to extend context window from 32K to 128K tokens"
  - target: 2025-05-qwen3-technical-report
    type: concurrent
    detail: "Concurrent open-source model release; K2 outperforms Qwen3-235B-A22B on most agentic benchmarks"
  - target: 2025-12-deepseek-v3.2-frontier-open-llm
    type: concurrent
    detail: "Concurrent open reasoning model; DeepSeek-V3.2 compared directly against Kimi-K2-Thinking on reasoning and agentic benchmarks"
open_questions:
  - question: "Can the MuonClip optimizer be applied effectively to dense models or other MoE architectures?"
    addressed_by: null
  - question: "How does the synthetic agentic data synthesis pipeline generalize to domains beyond tool use?"
    addressed_by: null
  - question: "What is the optimal balance between verifiable rewards and self-critique rubric rewards in general RL?"
    addressed_by: null
---

# Kimi K2: Open Agentic Intelligence

**Authors:** Kimi Team (Moonshot AI)
**Date:** July 2025, arXiv:2507.20534

---

## Core Research Problem

The development of Large Language Models is shifting toward **Agentic Intelligence**—the capability for models to autonomously perceive, plan, reason, and act within complex environments. This transition introduces challenges in both pre-training and post-training:

1. **Pre-training token efficiency:** High-quality human data is increasingly limited, making token efficiency (learning signal per token) a critical scaling coefficient.

2. **Training instability:** The token-efficient Muon optimizer suffers from attention logit explosion when scaled to large models, causing loss spikes and divergence.

3. **Agentic capability scarcity:** Multi-step reasoning, long-term planning, and tool use are rare in natural data and costly to scale through human annotation.

4. **Inference efficiency:** Efficient long-context processing is essential for agentic applications, but increasing attention heads (as in DeepSeek-V3) significantly increases inference FLOPs.

**The core challenge: how to build a token-efficient, stable pre-training regime for trillion-parameter MoE models while developing scalable post-training methods for agentic capabilities.**

---

## Problem Solutions

Kimi K2 addresses these challenges through three main contributions:

1. **MuonClip optimizer:** Integrates the token-efficient Muon algorithm with a novel QK-Clip mechanism that rescales query and key projection weights to bound attention logits, enabling stable 15.5T token training with zero loss spikes.

2. **Large-scale agentic data synthesis:** A pipeline that systematically generates tool-use demonstrations via simulated and real-world environments, constructing diverse tools, agents, tasks, and trajectories at scale.

3. **General reinforcement learning framework:** Combines verifiable rewards (RLVR) with a self-critique rubric reward mechanism, extending alignment from tasks with ground-truth rewards to open-ended domains.

---

## Approach Details

### Method

#### MuonClip Optimizer

The Muon optimizer provides superior token efficiency over AdamW but causes attention logit explosion at scale. QK-Clip addresses this by rescaling query and key projection weights post-update:

> Let the max logit for attention head h be:
> S^h_max = (1/√d) max_{X∈B} max_{i,j} Q^h_i K^h⊤_j

When S^h_max exceeds threshold τ, QK-Clip applies per-head scaling:

> γ_h = min(1, τ/S^h_max)

For Multi-head Latent Attention (MLA):
- **q^C and k^C** (head-specific components): scaled by √γ_h
- **q^R** (head-specific rotary): scaled by γ_h
- **k^R** (shared rotary): unchanged to avoid cross-head effects

The algorithm integrates Muon with weight decay (λ=0.1), consistent RMS matching (0.2 scaling factor), and QK-Clip into a single optimizer.

#### Model Architecture

Kimi K2 is a 1.04 trillion parameter MoE with 32 billion activated parameters:

| Component | Kimi K2 | DeepSeek-V3 | Change |
|---|---|---|---|
| Total Parameters | 1.04T | 671B | +54% |
| Activated Parameters | 32.6B | 37B | -13% |
| Total Experts | 384 | 256 | +50% |
| Experts per Token | 8 | 8 | = |
| Attention Heads | 64 | 128 | -50% |
| Layers | 61 | 61 | = |
| Hidden Dimension | 7168 | - | - |
| Expert Hidden Dim | 2048 | - | - |

Key architectural decisions:
- **Sparsity 48:** 384 total experts with 8 activated achieves 1.69× FLOPs reduction vs sparsity 8 at same validation loss.
- **64 attention heads:** Doubling heads (like DeepSeek-V3) yields only 0.5-1.2% loss improvement but 83% inference FLOP increase at 128K context.
- **Multi-head Latent Attention (MLA):** Following DeepSeek-V3 for efficient attention computation.

---

### Key Technical Components

#### Pre-training Data Rephrasing

To improve token utility without overfitting:

**Knowledge Data Rephrasing:**
- Style- and perspective-diverse prompting (inspired by WRAP)
- Chunk-wise autoregressive generation for long documents (256-token chunks, 4096-token outputs)
- Fidelity verification via semantic alignment checks

**Mathematics Data Rephrasing:**
- Rewriting to "learning-note" style (following SwallowMath)
- Translation of high-quality materials from other languages

**Pre-training corpus:** 15.5 trillion tokens spanning Web Text, Code, Mathematics, and Knowledge domains.

#### Training Recipe

- **Initial training:** 10T tokens at constant learning rate 2e-4 (4096 context, 67M batch)
- **Decay phase:** 5.5T tokens with cosine decay from 2e-4 to 2e-5
- **Annealing:** 400B tokens with decay from 2e-5 to 7e-6
- **Long context:** 60B tokens at 32K sequence length; YaRN extends to 128K inference

#### Large-Scale Agentic Data Synthesis

Three-stage pipeline:

1. **Tool spec generation:** 3000+ real MCP tools from GitHub + 20,000+ synthetic tools via hierarchical domain evolution

2. **Agent and task generation:** Diverse system prompts, tool combinations, and rubric-based tasks with explicit success criteria

3. **Trajectory generation:**
   - LLM-generated user personas for multi-turn dialogues
   - Tool simulator with persistent state and controlled stochasticity
   - LLM-based judge evaluates against task rubrics
   - Real execution sandboxes for coding/SWE tasks (ground-truth via test suite pass rates)

#### Reinforcement Learning Framework

**Verifiable Rewards Gym:**
- Math/STEM/Logical: Diverse coverage + moderate difficulty filtering via pass@k
- Instruction Following: Hybrid rule verification (code interpreters + LLM-as-judge) with hack-check layer
- Faithfulness: Sentence-level faithfulness judge model
- Coding/SWE: Competition problems + GitHub PRs with executable unit tests
- Safety: Adversarial prompt evolution (Attack Model → Target Model → Judge Model)

**Self-Critique Rubric Reward:**
- K2 critic evaluates own outputs via pairwise comparison
- Core rubrics: Clarity/Relevance, Conversational Fluency, Objective Interaction
- Prescriptive rubrics: No initial praise, no explicit self-justification
- Closed-loop refinement: Critic updated using verifiable signals from RLVR

**RL Algorithm Enhancements:**
- Budget Control: Per-sample token limits with truncation penalty
- PTX Loss: Auxiliary loss on curated high-quality samples to prevent forgetting
- Temperature Decay: High initial temperature for exploration, decaying for exploitation

---

### Experimental Setup

**Benchmarks:**
- Coding: LiveCodeBench v6, OJBench, MultiPL-E, SWE-bench Verified, SWE-bench Multilingual, SWE-Lancer, PaperBench, TerminalBench, Aider-Polyglot
- Tool Use: τ²-Bench (retail, airline, telecom), ACEBench
- Math/STEM: AIME 2024/2025, MATH-500, HMMT 2025, CNMO 2024, ZebraLogic, AutoLogi, GPQA-Diamond, SuperGPQA
- Long Context: MRCR, DROP, FRAMES, LongBench v2
- Factuality: FACTS Grounding, HHEM v2.1, FaithJudge
- General: MMLU, MMLU-Redux, MMLU-Pro, IFEval, Multi-Challenge, SimpleQA, LiveBench

**Baselines:**
- Open-source: DeepSeek-V3-0324, Qwen3-235B-A22B (non-thinking)
- Proprietary: Claude Sonnet 4, Claude Opus 4, GPT-4.1, Gemini 2.5 Flash Preview

**Evaluation configuration:** Non-thinking mode, 8192 max output tokens (16384 for SWE-bench Agentless), 128K context window.

---

### Key Results

#### Post-training: Agentic and Competitive Coding

| Benchmark | Kimi-K2-Instruct | DeepSeek-V3-0324 | Qwen3-235B-A22B | Claude Opus 4 |
|---|---|---|---|---|
| SWE-bench Verified (Agentic Single) | **65.8** | 38.8 | 34.4 | 72.5 |
| SWE-bench Multilingual | **47.3** | 25.8 | 20.9 | — |
| LiveCodeBench v6 | **53.7** | 46.9 | 37.0 | 47.4 |
| OJBench | **27.1** | 24.0 | 11.3 | 19.6 |
| τ²-Bench (micro-avg) | **66.1** | 48.8 | 37.3 | 67.6 |
| ACEBench (En) | **76.5** | 72.7 | 70.5 | 75.6 |

- K2 achieves SOTA among open-source models on all agentic benchmarks
- Closes gap with Claude 4 Opus/Sonnet on SWE-bench

#### Post-training: Math, STEM, and General

| Benchmark | Kimi-K2-Instruct | DeepSeek-V3-0324 | Qwen3-235B-A22B | GPT-4.1 |
|---|---|---|---|---|
| AIME 2025 (Avg@64) | **49.5** | 46.7 | 24.7 | 37.0 |
| GPQA-Diamond (Avg@8) | **75.1** | 68.4 | 62.9 | 66.3 |
| MMLU | **89.5** | 89.4 | 87.0 | 90.4 |
| IFEval (Prompt Strict) | **89.8** | 81.1 | 83.2 | 88.0 |
| SimpleQA | **31.0** | 27.7 | 13.2 | 42.3 |

#### Base Model Evaluation

| Benchmark | Kimi-K2-Base | DeepSeek-V3-Base | Llama4-Maverick-Base |
|---|---|---|---|
| MMLU | **87.79** | 87.10 | 84.87 |
| MMLU-Pro | **69.17** | 60.59 | 63.47 |
| MATH | **70.22** | 61.70 | 63.02 |
| EvalPlus | **80.33** | 65.61 | 65.48 |
| C-Eval | **92.50** | 90.04 | 80.91 |
| SimpleQA | **35.25** | 26.49 | 23.74 |

- K2-Base achieves SOTA on 10/12 English benchmarks, all Chinese benchmarks, and all coding benchmarks

#### Training Stability (MuonClip)

- QK-Clip activated in 12.7% of attention heads during first 70K steps
- After 70K steps, all heads reduced max logits below threshold τ=100
- Zero loss spikes throughout 15.5T token training (Figure 3)

---

## Limitations and Failure Modes

1. **Excessive token generation:** On hard reasoning tasks or unclear tool definitions, the model may generate excessive tokens, leading to truncated outputs or incomplete tool calls (Section 5).

2. **Unnecessary tool use degradation:** Performance may decline on certain tasks if tool use is enabled when not needed.

3. **One-shot project building:** Success rate for building complete software projects via one-shot prompting is lower than using K2 under an agentic coding framework.

4. **Long-context reasoning gap:** Kimi-K2-Instruct lags DeepSeek-V3-0324 by ~2% on FRAMES and LongBench v2 (Section 4.1.2).

5. **SimpleQA factuality:** Despite improvements, K2 (31.0%) still trails GPT-4.1 (42.3%) on short-form factuality.

6. **Self-critique limitations:** The evaluation framework may favor confident responses over appropriately cautious ones in ambiguous contexts, potentially overstating certainty (Appendix F.3).

### Scope and Comparability

- **Non-thinking mode only:** All comparisons use non-thinking configurations; thinking/reasoning modes not evaluated.
- **Agentic evaluation variance:** SWE-bench results use Avg@4 seeds; single-attempt results may vary.
- **LMSYS Arena ranking:** Based on 3000+ votes as of July 17, 2025; rankings may change over time.

---

## Conclusions

### Contributions

1. **MuonClip optimizer.** Novel integration of token-efficient Muon with QK-Clip weight clipping, enabling stable training of 1T parameter MoE models on 15.5T tokens with zero loss spikes.

2. **Sparsity scaling law for MoE.** Demonstrated that increasing sparsity to 48 (384 experts, 8 activated) reduces FLOPs by 1.69× compared to sparsity 8 for equivalent validation loss.

3. **Large-scale agentic data synthesis.** Scalable pipeline combining 23,000+ tools (real MCP + synthetic), rubric-based task generation, and hybrid simulated/real execution environments.

4. **General RL framework.** Extended alignment beyond verifiable rewards via self-critique rubric mechanism with closed-loop critic refinement from RLVR signals.

5. **SOTA open-source agentic model.** Kimi K2 achieves #1 open-source ranking on LMSYS Arena and outperforms all open-source baselines on SWE-bench, τ²-Bench, and ACEBench.

6. **Efficient architecture choices.** 64 attention heads (vs 128 in DeepSeek-V3) reduces inference FLOPs by 83% at 128K context with only 0.5-1.2% loss degradation.

### Implications

1. **Token efficiency as primary scaling axis.** With limited high-quality data, optimizer improvements (Muon over AdamW) and synthetic data augmentation (rephrasing) become critical for continued scaling.

2. **Self-critique enables general alignment.** Grounding subjective evaluation in verifiable data through closed-loop refinement may enable robust alignment with complex, non-verifiable human objectives.

3. **Hybrid simulation + real execution.** Combining scalable simulated environments with targeted real-world execution provides both diversity and authenticity for agentic training data.

4. **Architecture-inference trade-offs.** Reducing attention heads significantly improves long-context inference efficiency with minimal impact on model quality, important for agentic applications.

---

## Key Claims

1. **C1:** Kimi K2 achieves 65.8% on SWE-bench Verified (agentic single attempt), outperforming DeepSeek-V3-0324 (38.8%) and Qwen3-235B-A22B (34.4%), closing the gap with Claude 4 Opus (72.5%) (Table 3, Figure 1). Status: **supported**.

2. **C2:** MuonClip enables stable pre-training on 15.5 trillion tokens with zero loss spikes, with QK-Clip activating in only 12.7% of heads during early training and self-deactivating after 70K steps (Figure 3, Section 2.1). Status: **supported**.

3. **C3:** Under compute-optimal sparsity scaling, sparsity 48 reduces FLOPs by 1.69×, 1.39×, and 1.15× compared to sparsity 8, 16, and 32 respectively for the same validation loss of 1.5 (Figure 5, Section 2.3). Status: **supported**.

4. **C4:** Kimi K2 ranks #1 among open-source models and #5 overall on the LMSYS Arena leaderboard (July 17, 2025) based on over 3,000 user votes (Section 4.1.2). Status: **supported**.

5. **C5:** Data rephrasing improves SimpleQA accuracy: 10 rephrasings + 1 epoch (28.94%) outperforms raw text + 10 epochs (23.76%), a gain of 5.18 percentage points (Table 1, Section 2.2). Status: **supported**.

6. **C6:** Reducing attention heads from 128 to 64 yields only 0.5-1.2% validation loss increase but reduces inference FLOPs by 83% at 128K context (Figure 6, Section 2.3). Status: **supported**.

7. **C7:** Kimi-K2-Base achieves SOTA on 10/12 English benchmarks, all Chinese benchmarks, and all coding benchmarks compared to DeepSeek-V3-Base, Llama4-Maverick-Base, and Qwen2.5-72B-Base (Table 4, Section 4.2.2). Status: **supported**.

---

## Open Questions

1. **MuonClip generalization.** While MuonClip effectively stabilizes attention logits for MLA-based MoE models, its applicability to standard multi-head attention or dense architectures remains unexplored.

2. **Self-critique calibration.** The rubric reward framework may favor confident assertions over appropriately cautious responses. Future work may need fine-grained handling of calibrated uncertainty.

3. **Synthetic data quality control.** The paper notes challenges in generalizing rephrasing to diverse domains without compromising factual accuracy, minimizing hallucinations, and ensuring scalability.

4. **Agentic RL scaling.** The optimal balance between verifiable rewards and self-critique rewards across different task types and model scales is not systematically explored.

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundation Transformer architecture upon which Kimi K2 builds.
- **DeepSeek-AI (2024)** -- *DeepSeek-V3 Technical Report.* K2 follows DeepSeek-V3's MLA and MoE design; primary architectural and performance baseline.
- **Liu et al. (2024)** -- *DeepSeek-V2.* Introduces Multi-head Latent Attention (MLA) used in K2.

### Optimizer Development

- **Jordan et al. (2024)** -- *Muon: An Optimizer for Hidden Layers.* Token-efficient optimizer that K2 extends with QK-Clip.
- **Liu et al. (2025)** -- *Muon is Scalable for LLM Training (Moonlight).* Demonstrates Muon's scalability; K2 builds on this with stability improvements.
- **Kingma & Ba (2015)** -- *Adam: A Method for Stochastic Optimization.* Baseline optimizer that Muon outperforms in token efficiency.

### Training Stability

- **Dehghani et al. (2023)** -- *Scaling Vision Transformers to 22B Parameters.* Introduces QK-Norm, which is not applicable to MLA, motivating QK-Clip.
- **Gemma Team (2024)** -- *Gemma 2.* Logit soft-cap approach that K2 argues is insufficient for bounding pre-softmax growth.

### Context Extension

- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension.* K2 uses YaRN to extend context from 32K to 128K.

### Synthetic Data and RL

- **Maini et al. (2024)** -- *WRAP: Rephrasing the Web.* Inspires K2's style-diverse rephrasing for knowledge data.
- **Fujii et al. (2025)** -- *SwallowMath: Rewriting Pre-Training Data.* Methodology for mathematics data rephrasing.
- **Kimi Team (2025)** -- *Kimi K1.5: Scaling RL with LLMs.* Foundation RL algorithm and partial rollout technique adopted by K2.
- **Ouyang et al. (2022)** -- *Training Language Models to Follow Instructions with Human Feedback.* PTX loss for preventing forgetting during RL.

### Agentic Benchmarks

- **Yao et al. (2024)** -- *τ-bench: Tool-Agent-User Interaction.* Multi-turn tool-use benchmark extended to τ²-bench.
- **Chen et al. (2025)** -- *ACEBench: Who Wins the Match Point in Tool Learning?* Comprehensive tool-use benchmark.
- **Jimenez et al. (2024)** -- *SWE-bench: Can LMs Resolve Real-world GitHub Issues?* Primary software engineering benchmark.

### Competing Models

- **Qwen Team (2025)** -- *Qwen3 Technical Report.* Concurrent open-source baseline; K2 outperforms on most agentic benchmarks.
- **LlaMA Team (2025)** -- *Llama 4.* Llama-4-Maverick used as base model baseline.
