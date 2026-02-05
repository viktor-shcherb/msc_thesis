---
title: "DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models"
authors: "DeepSeek-AI"
year: 2025
venue: "arXiv preprint 2512.02556"
paper_type: preprint
categories: ["model-release", "architecture", "attention-efficiency", "context-extension"]
scope: ["open foundation models", "sparse attention", "reinforcement learning post-training", "agentic capabilities", "reasoning models", "128K context"]
benchmarks_used: ["mmlu-pro", "gpqa", "humaneval", "livecodebench", "gsm8k", "math-hendrycks", "swe-verified", "aime-2025", "hmmt-2025", "imo-2025", "terminal-bench", "browsecomp", "tau2-bench", "mcp-universe", "tool-decathlon"]
models_introduced: ["deepseek-v3.2", "deepseek-v3.2-speciale"]
models_evaluated: ["gpt-5", "gemini-3.0-pro", "claude-4.5-sonnet", "kimi-k2-thinking", "minimax-m2"]
key_claims:
  - id: C1
    claim: "DeepSeek Sparse Attention (DSA) reduces core attention complexity from O(L²) to O(Lk) while preserving performance on both short- and long-context tasks"
    evidence: "Section 2.1, Section 2.2, Figure 3"
    status: supported
    scope: "128K context, MLA-based architecture"
    magnitude: "~50% cost reduction at 128K tokens for prefilling"
  - id: C2
    claim: "DeepSeek-V3.2 achieves comparable performance to GPT-5-High on reasoning benchmarks with substantially fewer output tokens compared to Kimi-K2-Thinking"
    evidence: "Table 2, Table 3"
    status: supported
    scope: "AIME 2025, HMMT 2025, LiveCodeBench, GPQA Diamond"
    magnitude: "93.1% vs 94.6% on AIME 2025; 16k vs 24k tokens"
  - id: C3
    claim: "DeepSeek-V3.2-Speciale achieves gold-medal performance in IMO 2025, IOI 2025, ICPC World Finals 2025, and CMO 2025"
    evidence: "Table 4, Section 4.2"
    status: supported
    scope: "High-compute variant with relaxed length constraints"
    magnitude: "35/42 on IMO 2025, 492/600 on IOI 2025, 10/12 problems on ICPC WF 2025"
  - id: C4
    claim: "Post-training compute budget exceeding 10% of pre-training cost unlocks advanced reasoning capabilities"
    evidence: "Section 1, Section 3"
    status: supported
    scope: "GRPO-based RL training"
  - id: C5
    claim: "Large-scale synthetic agentic task synthesis (1,827 environments, 85,000 prompts) substantially improves generalization on out-of-domain agent benchmarks"
    evidence: "Section 3.2.3, Section 4.3, Figure 5, Table 5"
    status: supported
    scope: "General agent tasks, τ²-bench, MCP-Mark, MCP-Universe"
cross_references:
  - target: 2024-12-deepseek-v3-technical-report
    type: extends
    detail: "Direct successor to DeepSeek-V3, introducing DSA sparse attention and scaled RL post-training"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "DSA modifies standard attention with learnable sparse token selection"
  - target: 2025-07-kimi-k2-open-agentic-intelligence
    type: concurrent
    detail: "Concurrent open reasoning model; DeepSeek-V3.2 compared directly against Kimi-K2-Thinking"
open_questions:
  - question: "Can token efficiency of extended thinking be improved to match Gemini-3.0-Pro's output length while maintaining performance?"
    addressed_by: null
  - question: "Does DSA's learned sparse attention pattern generalize to domains not seen during continued pre-training?"
    addressed_by: null
  - question: "What is the optimal combination of serial (context management) and parallel scaling for test-time compute?"
    addressed_by: null
---

# DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models

**Authors:** DeepSeek-AI (263+ contributors)
**Date:** December 2025, arXiv:2512.02556

---

## Core Research Problem

Despite rapid progress in open-source LLMs, a performance gap has emerged between open and closed-source models on complex tasks. The paper identifies three critical deficiencies limiting open-source models:

1. **Architectural inefficiency:** Reliance on vanilla O(L²) attention constrains efficiency for long sequences, hindering both scalable deployment and effective post-training.

2. **Insufficient post-training compute:** Open-source models allocate insufficient computational resources during post-training, limiting performance on hard reasoning tasks.

3. **Weak agentic capabilities:** Open models lag in generalization and instruction-following for tool-use scenarios compared to proprietary models, hindering real-world deployment.

The core challenge is: **how to build an open LLM that matches frontier proprietary models (GPT-5, Gemini-3.0-Pro) on reasoning and agentic tasks while maintaining computational efficiency.**

---

## Problem Solutions

DeepSeek-V3.2 addresses these limitations through three innovations:

1. **DeepSeek Sparse Attention (DSA):** A learned sparse attention mechanism that reduces core attention complexity from O(L²) to O(Lk) where k << L, using a "lightning indexer" to select relevant tokens.

2. **Scalable RL framework:** A robust reinforcement learning protocol allocating >10% of pre-training compute to post-training, with technical innovations for stable GRPO scaling.

3. **Large-scale agentic task synthesis:** A pipeline generating 1,827 environments and 85,000 complex prompts for RL training, enabling generalization to unseen agent benchmarks.

---

## Approach Details

### Architecture

DeepSeek-V3.2 uses the same base architecture as DeepSeek-V3.1-Terminus with one modification: the introduction of **DeepSeek Sparse Attention (DSA)** through continued training.

#### DeepSeek Sparse Attention (DSA)

DSA consists of two components:

**1. Lightning Indexer:** Computes index scores between query and key tokens to determine which tokens to select:

> I_{t,s} = Σ_{j=1}^{H^I} w^I_{t,j} · ReLU(q^I_{t,j} · k^I_s)

where H^I is the number of indexer heads, q^I and w^I are derived from the query token, and k^I from preceding tokens. ReLU activation enables FP8 implementation for throughput.

**2. Fine-grained token selection:** Retrieves only the key-value entries corresponding to top-k index scores:

> u_t = Attn(h_t, {c_s | I_{t,s} ∈ Top-k(I_{t,:})})

**DSA under MLA:** For continued training from DeepSeek-V3.1-Terminus, DSA is instantiated based on Multi-head Latent Attention (MLA) in MQA mode, where each latent vector (key-value entry) is shared across all query heads.

### Key Technical Components

#### Continued Pre-Training for DSA

**Dense Warm-up Stage (2.1B tokens):**
- Freezes all parameters except lightning indexer
- Trains indexer with KL-divergence loss to match aggregated attention distribution:
> L^I = Σ_t D_KL(p_{t,:} || Softmax(I_{t,:}))
- Learning rate: 10^-3, 1000 steps, 16 sequences of 128K tokens per step

**Sparse Training Stage (943.7B tokens):**
- Introduces fine-grained token selection, optimizes all parameters
- Selects k=2048 key-value tokens per query token
- Learning rate: 7.3 × 10^-6, 15000 steps, 480 sequences of 128K tokens per step
- Indexer trained only on L^I; main model trained only on language modeling loss (detached gradients)

#### Inference Cost Reduction

DSA reduces costs significantly at long contexts (Figure 3):

| Token Position | V3.1-Terminus Prefill | V3.2 Prefill | V3.1-Terminus Decode | V3.2 Decode |
|---|---|---|---|---|
| 32K | ~$0.15/M | ~$0.10/M | ~$0.6/M | ~$0.4/M |
| 128K | ~$0.65/M | ~$0.30/M | ~$2.4/M | ~$1.0/M |

(Costs estimated from H800 GPU deployment at $2/GPU-hour)

### Post-Training

#### Specialist Distillation

For each domain (mathematics, programming, general reasoning, agentic tasks, agentic coding, agentic search), a specialized model is trained via large-scale RL from the DeepSeek-V3.2 base checkpoint. Both thinking and non-thinking modes are supported. Specialists generate domain-specific training data for the final model.

#### Mixed RL Training

Uses **Group Relative Policy Optimization (GRPO)** with several innovations for stable scaling:

**1. Unbiased KL Estimate:** Corrects the K3 estimator using importance sampling:

> D_KL(π_θ || π_ref) = (π_θ/π_old) · [(π_ref/π_θ) - log(π_ref/π_θ) - 1]

This eliminates unbounded gradient weights when sampled tokens have low probability under the current policy.

**2. Off-Policy Sequence Masking:** Masks negative-advantage sequences with high KL divergence from sampling policy:

> M_{i,t} = 0 if Â_{i,t} < 0 and (1/|o_i|) Σ log(π_old/π_θ) > δ; else 1

**3. Keep Routing:** Preserves expert routing paths from inference during training to ensure consistent MoE expert activation.

**4. Keep Sampling Mask:** Preserves top-p/top-k truncation masks from sampling to ensure identical action subspaces between π_old and π_θ.

#### DeepSeek-V3.2-Speciale

A high-compute variant trained exclusively on reasoning data with reduced length penalty, incorporating DeepSeekMath-V2 techniques for mathematical proofs.

### Thinking in Tool-Use

#### Context Management

Unlike DeepSeek-R1 (which discards reasoning on each new message), DeepSeek-V3.2 retains reasoning content when only tool-related messages are appended (Figure 4). Reasoning is discarded only on new user messages, while tool call history is always preserved.

#### Cold-Start

Integrates reasoning and tool-use capabilities via carefully designed prompting (Tables 6-8). System prompts explicitly instruct the model to incorporate tool calls within the <think></think> reasoning process.

#### Large-Scale Agentic Tasks

| Task Type | Count | Environment | Prompt Source |
|---|---|---|---|
| Code agent | 24,667 | Real (GitHub) | Extracted |
| Search agent | 50,275 | Real (Search API) | Synthesized |
| General agent | 4,417 | Synthesized | Synthesized |
| Code interpreter | 5,908 | Real (Jupyter) | Extracted |

**General Agent Synthesis Pipeline:**
1. Given task category and sandbox with bash/search tools, generate/retrieve data and store in database
2. Synthesize task-specific tools as functions
3. Create task, solution, and verification functions iteratively increasing difficulty
4. Retain only instances with non-zero pass@100 → 1,827 environments, 4,417 tasks

### Experimental Setup

**Evaluation benchmarks:**
- English: MMLU-Pro, GPQA Diamond, HLE (text-only)
- Code: LiveCodeBench (2024.08-2025.04), Codeforces, Aider-Polyglot
- Math: AIME 2025, HMMT Feb/Nov 2025, IMOAnswerBench
- Code Agent: Terminal Bench 2.0, SWE-Verified, SWE Multilingual
- Search Agent: BrowseComp, BrowseCompZh, HLE with search
- Tool Use: τ²-bench, MCP-Universe, MCP-Mark, Tool-Decathlon

**Evaluation settings:** Temperature 1.0, context window 128K, standard function call format with thinking mode for tool-use benchmarks.

### Key Results

**Main Results (Table 2):**

| Benchmark | Claude-4.5-Sonnet | GPT-5-High | Gemini-3.0-Pro | DeepSeek-V3.2 |
|---|---|---|---|---|
| MMLU-Pro (EM) | 88.2 | 87.5 | **90.1** | 85.0 |
| GPQA Diamond | 83.4 | 85.7 | **91.9** | 82.4 |
| HLE (Pass@1) | 13.7 | 26.3 | **37.7** | 25.1 |
| LiveCodeBench | 64.0 | 84.5 | **90.7** | 83.3 |
| Codeforces (Rating) | 1480 | 2537 | **2708** | 2386 |
| AIME 2025 | 87.0 | 94.6 | **95.0** | 93.1 |
| HMMT Feb 2025 | 79.2 | 88.3 | **97.5** | 92.5 |
| SWE Verified | **77.2** | 74.9 | 76.2 | 73.1 |
| Terminal Bench 2.0 | 42.8 | 35.2 | **54.2** | 46.4 |
| τ²-bench | 84.7 | 80.2 | **85.4** | 80.3 |
| Tool-Decathlon | **38.6** | 29.0 | 36.4 | 35.2 |

DeepSeek-V3.2 achieves comparable performance to GPT-5-High on reasoning tasks but trails Gemini-3.0-Pro.

**DeepSeek-V3.2-Speciale Results (Table 3):**

| Benchmark | GPT-5-High | Gemini-3.0-Pro | DeepSeek-V3.2-Speciale |
|---|---|---|---|
| AIME 2025 | 94.6 (13k) | 95.0 (15k) | **96.0** (23k) |
| HMMT Feb 2025 | 88.3 (16k) | 97.5 (16k) | **99.2** (27k) |
| LiveCodeBench | 84.5 (13k) | **90.7** (13k) | 88.7 (27k) |
| IMOAnswerBench | 76.0 (31k) | 83.3 (18k) | **84.5** (45k) |

Numbers in parentheses indicate output token count (in thousands).

**Competition Performance (Table 4):**

| Competition | P1 | P2 | P3 | P4 | P5 | P6 | Overall | Medal |
|---|---|---|---|---|---|---|---|---|
| IMO 2025 | 7 | 7 | 7 | 7 | 7 | 0 | 35/42 | Gold |
| CMO 2025 | 18 | 18 | 9 | 21 | 18 | 18 | 102/126 | Gold |
| IOI 2025 | 100 | 82 | 72 | 100 | 55 | 83 | 492/600 | Gold |
| ICPC WF 2025 | 3 | - | 1 | 1 | 2 | 2 | - | 1 | 1 | 1 | 1 | 1 | 10/12 | Gold |

DeepSeek-V3.2-Speciale ranked 2nd in ICPC WF 2025 and 10th in IOI 2025.

**Synthetic Agentic Task Generalization (Figure 5):**

RL on synthetic general agent data yields substantial improvements on τ²-bench, MCP-Mark, and MCP-Universe, while RL restricted to code and search scenarios does not improve these benchmarks. This demonstrates generalization from synthetic to out-of-domain environments.

---

## Limitations and Failure Modes

The paper acknowledges the following limitations:

1. **Knowledge breadth gap:** Due to fewer total training FLOPs, world knowledge in DeepSeek-V3.2 lags behind frontier proprietary models.

2. **Token efficiency:** DeepSeek-V3.2 requires longer generation trajectories (more tokens) to match output quality of Gemini-3.0-Pro. For example, on AIME 2025: DeepSeek-V3.2 uses 16k tokens vs Gemini-3.0-Pro's 15k for similar accuracy.

3. **Complex task performance:** Solving complex tasks remains inferior to Gemini-3.0-Pro across most benchmarks (e.g., GPQA Diamond: 82.4% vs 91.9%).

4. **Context management incompatibility:** The thinking mode context management strategy is incompatible with some agent frameworks (Roo Code, Terminus) that simulate tool interactions via user messages. Non-thinking mode is recommended for such architectures.

5. **Context length overflow in MCP tasks:** DeepSeek-V3.2 frequently engages in redundant self-verification, causing context to exceed 128K limit on MCP-Mark GitHub and Playwright tasks, hindering performance.

### Scope and Comparability

- **128K context window:** While DSA reduces attention cost, the model is still limited to 128K context, causing ~20%+ of BrowseComp test cases to exceed limits.
- **Evaluation environment differences:** MCP-Universe and MCP-Mark evaluated with internal environment; search and playwright environments may differ from official settings.
- **Framework dependency:** Terminal Bench 2.0 score of 46.4 achieved with Claude Code framework; Terminus framework yields 39.3 in non-thinking mode.

---

## Conclusions

### Contributions

1. **DeepSeek Sparse Attention (DSA).** A learned sparse attention mechanism reducing core attention complexity from O(L²) to O(Lk) through a lightning indexer and fine-grained token selection. Achieved through ~946B tokens of continued pre-training without performance degradation on short- or long-context tasks (Section 2).

2. **Scalable GRPO framework.** Technical innovations enabling stable RL scaling with >10% of pre-training compute: unbiased KL estimation, off-policy sequence masking, keep routing for MoE, and keep sampling mask for top-p/top-k consistency (Section 3.1).

3. **Integrated reasoning and tool-use.** Context management strategy retaining thinking content across tool calls, cold-start prompting for thinking-in-tool-use, enabling effective agentic reasoning (Section 3.2).

4. **Large-scale agentic task synthesis.** Pipeline generating 1,827 environments and 85,000+ prompts enabling generalization to out-of-domain agent benchmarks (τ²-bench, MCP-Mark, MCP-Universe) not seen during training (Section 3.2.3, Section 4.3).

5. **Frontier reasoning performance.** DeepSeek-V3.2-Speciale achieves gold-medal performance at IMO 2025, IOI 2025, ICPC WF 2025, and CMO 2025, demonstrating open models can match proprietary frontier on top-tier reasoning competitions (Section 4.2).

### Implications

1. **Sparse attention is viable for reasoning models.** DSA demonstrates that learned sparse attention can reduce long-context compute costs substantially (~50% at 128K) without degrading reasoning or long-context task performance, challenging the assumption that full attention is necessary.

2. **Post-training compute scaling unlocks capabilities.** Allocating >10% of pre-training compute to RL post-training yields consistent performance improvements, suggesting this ratio may be underinvested in current open-source models.

3. **Synthetic environments enable agentic generalization.** RL on synthetically generated task environments transfers to real-world agent benchmarks, providing a scalable path to improve tool-use capabilities without relying on proprietary interaction data.

4. **Token efficiency remains a challenge.** Despite matching proprietary models on accuracy, open reasoning models require significantly more output tokens, indicating inefficiency in reasoning chains that warrants future investigation.

---

## Key Claims

1. **DSA reduces attention complexity without performance loss.** Core attention complexity reduced from O(L²) to O(Lk) with k=2048 selected tokens per query. Parity evaluation shows similar performance to DeepSeek-V3.1-Terminus on standard benchmarks, ChatbotArena Elo, and long-context evaluations (AA-LCR, Fiction.liveBench). Evidence: Section 2.2. Status: **supported**.

2. **DeepSeek-V3.2 matches GPT-5-High on reasoning with fewer tokens than Kimi-K2.** On AIME 2025: 93.1% (16k tokens) vs GPT-5 94.6% (13k) and Kimi-K2 94.5% (24k). Evidence: Table 2, Table 3. Status: **supported**.

3. **DeepSeek-V3.2-Speciale achieves gold medals at 2025 competitions.** IMO: 35/42, IOI: 492/600 (10th place), ICPC WF: 10/12 (2nd place), CMO: 102/126. Evidence: Table 4. Status: **supported**.

4. **>10% pre-training compute for post-training unlocks advanced capabilities.** The paper allocates post-training budget exceeding 10% of pre-training cost and observes "consistent performance improvements correlating with extended RL training budget." Evidence: Section 1, Section 4.1. Status: **supported** (qualitative, no quantitative ablation).

5. **Synthetic agentic tasks generalize to real benchmarks.** RL on general synthesized agent data improves τ²-bench, MCP-Mark, and MCP-Universe, while restricting RL to code/search environments does not. Evidence: Figure 5, Section 4.3. Status: **supported** (ablation study provided).

6. **Context management extends test-time compute for search agents.** Discard-all strategy achieves 67.6% on BrowseComp vs 51.4% without context management, comparable to parallel scaling with fewer steps. Evidence: Figure 6, Section 4.4. Status: **supported**.

---

## Open Questions

1. **Token efficiency optimization.** Can the intelligence density of reasoning chains be improved to match Gemini-3.0-Pro's output quality with comparable token counts? Current gap is ~1.5-2x.

2. **DSA generalization.** How does DSA's learned indexer perform on domains substantially different from the continued pre-training distribution? No out-of-domain ablation is provided.

3. **Optimal test-time compute allocation.** What is the optimal combination of serial (context management) and parallel (multi-trajectory) scaling for different task types?

4. **Post-training compute scaling laws.** What is the relationship between post-training compute budget and downstream performance? Is 10% optimal, or would higher allocation yield further gains?

5. **Synthetic task coverage.** Are 1,827 synthesized environments sufficient for broad agentic generalization, or does performance plateau on more diverse real-world tasks?

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Standard attention mechanism that DSA modifies with learned sparse selection.
- **DeepSeek-AI (2024)** -- *DeepSeek-V2.* Introduces Multi-head Latent Attention (MLA) that DSA builds upon in MQA mode.
- **Shazeer (2019)** -- *Fast Transformer Decoding.* Multi-Query Attention concept used for DSA implementation.

### Direct Predecessors

- **DeepSeek-AI (2024)** -- *DeepSeek-V3 Technical Report.* Direct predecessor providing base architecture and cold-start methodology for tool-use integration.
- **DeepSeek-AI (2025)** -- *DeepSeek-R1.* Reasoning model demonstrating thinking process benefits; DeepSeek-V3.2 extends with tool-use integration and context management.

### Reinforcement Learning

- **Shao et al. (2024)** -- *DeepSeekMath.* Introduces GRPO algorithm used for post-training.
- **Schulman (2020)** -- *Approximating KL Divergence.* K3 estimator that DeepSeek-V3.2 corrects for unbiased gradient estimation.

### Competing Models

- **OpenAI (2025)** -- *GPT-5.* Primary closed-source comparison target.
- **DeepMind (2025)** -- *Gemini 3.0 Pro.* State-of-the-art comparison target; DeepSeek-V3.2-Speciale aims for parity.
- **MoonShot (2025)** -- *Kimi K2 Thinking.* Open-source reasoning model baseline.

### Evaluation Benchmarks

- **Wang et al. (2024)** -- *MMLU-Pro.* Robust multi-task evaluation.
- **Rein et al. (2023)** -- *GPQA Diamond.* Graduate-level science QA.
- **Phan et al. (2025)** -- *Humanity's Last Exam (HLE).* Challenging reasoning benchmark.
- **Wei et al. (2025)** -- *BrowseComp.* Web browsing agent benchmark.
- **Barres et al. (2025)** -- *τ²-bench.* Conversational agent evaluation.
- **Luo et al. (2025)** -- *MCP-Universe.* Model Context Protocol benchmark with real-world servers.
