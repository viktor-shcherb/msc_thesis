---
title: "Kimi k1.5: Scaling Reinforcement Learning with LLMs"
authors: "Kimi Team"
year: 2025
venue: "arXiv preprint"
paper_type: preprint
categories: ["reasoning-evaluation", "in-context-learning", "model-release"]
scope: ["reinforcement learning for LLMs", "long chain-of-thought", "test-time compute scaling", "multimodal reasoning"]
benchmarks_used: ["math-hendrycks", "mmlu", "ifeval", "c-eval", "humaneval", "livecodebench", "mathvista", "mmmu"]
models_introduced: ["kimi-k1.5"]
models_evaluated: ["gpt-4o", "claude-3.5-sonnet", "qwen2.5-72b", "llama-3.1-405b", "deepseek-v3", "qwq-32b"]
key_claims:
  - id: C1
    claim: "Long context scaling is a key dimension for continued RL improvement with LLMs; scaling the RL context window to 128k yields continued performance gains"
    evidence: "Section 1, Section 3.3, Figures 5-6"
    status: supported
    scope: "mathematical reasoning benchmarks"
    magnitude: "Strong positive correlation between response length and accuracy across 12 benchmarks"
  - id: C2
    claim: "Strong reasoning performance can be achieved without Monte Carlo tree search, value functions, or process reward models through long context scaling and improved policy optimization alone"
    evidence: "Section 1, Section 4"
    status: supported
    scope: "AIME, MATH-500, Codeforces benchmarks"
  - id: C3
    claim: "Kimi k1.5 long-CoT matches OpenAI o1 on key benchmarks: 77.5 vs 74.4 on AIME 2024, 96.2 vs 94.8 on MATH-500, 94 vs 94 percentile on Codeforces"
    evidence: "Table 2, Figure 1"
    status: supported
    scope: "Pass@1, greedy decoding"
  - id: C4
    claim: "Long2short methods can transfer thinking priors from long-CoT models to short-CoT models, achieving 60.8 on AIME 2024 with only 3,272 average tokens"
    evidence: "Section 2.4, Section 3.4, Figure 7"
    status: supported
    scope: "short-CoT inference budget"
  - id: C5
    claim: "Partial rollouts technique enables efficient long-context RL training by reusing previous trajectory segments across iterations"
    evidence: "Section 2.6.2, Figure 3b"
    status: supported
  - id: C6
    claim: "Negative gradients in policy optimization significantly improve sample efficiency compared to ReST which only fits best responses"
    evidence: "Section 3.5, Figure 10"
    status: supported
    scope: "12 math/reasoning benchmarks"
  - id: C7
    claim: "Chain-of-Thought reward model achieves 98.5% accuracy vs 84.4% for classic value-head reward model on math verification"
    evidence: "Section 2.3.5"
    status: supported
    scope: "math answer verification"
cross_references:
  - target: 2022-12-chain-of-thought-prompting
    type: extends
    detail: "Extends chain-of-thought prompting by training models to generate extended reasoning traces via reinforcement learning rather than prompting"
  - target: 2024-07-llama-3-herd-of-models
    type: evaluates
    detail: "Compares against Llama 3.1 405B-Instruct as a baseline for short-CoT performance"
  - target: 2023-07-llama-2-open-foundation-chat
    type: complementary
    detail: "Follows similar pretraining-SFT-RL pipeline but scales RL context to 128k and removes value functions"
  - target: 2025-04-kimi-vl-technical-report
    type: extended-by
    detail: "Kimi-VL-Thinking adopts the online policy mirror descent RL algorithm and long-CoT approach from Kimi k1.5 for multimodal reasoning"
open_questions:
  - question: "How does the overthinking phenomenon (response length growth during RL) affect generalization to out-of-distribution problems?"
    addressed_by: null
  - question: "Can partial rollouts scale beyond 128k context while maintaining training stability?"
    addressed_by: null
  - question: "How do the learned long-CoT reasoning patterns transfer across domains (e.g., math to code)?"
    addressed_by: null
  - question: "What is the optimal balance between model size scaling and context length scaling for a fixed compute budget?"
    addressed_by: null
---

# Kimi k1.5: Scaling Reinforcement Learning with LLMs

**Authors:** Kimi Team (Moonshot AI)
**Date:** January 2025, arXiv:2501.12599

---

## Core Research Problem

Language model pretraining with next-token prediction has been studied under scaling laws where proportionally scaling model parameters and data sizes leads to continued improvement. However, this approach is fundamentally limited by the amount of available high-quality training data. Prior work on reinforcement learning (RL) with LLMs had not produced competitive results compared to frontier models.

The core challenge is: **how to scale reinforcement learning as a new axis for continued LLM improvement, enabling models to learn to explore with rewards rather than being limited to static pre-existing datasets.**

Several obstacles had prevented effective RL scaling: (1) the computational cost of generating long reasoning trajectories, (2) the instability of policy optimization at scale, (3) the complexity of techniques like Monte Carlo tree search and process reward models, and (4) the difficulty of credit assignment in long chain-of-thought sequences.

---

## Problem Solutions

The paper presents the training recipe of Kimi k1.5, a multimodal LLM trained with reinforcement learning. The key insight is that **long context scaling** combined with **simplified policy optimization** can achieve strong reasoning performance without complex techniques. The main contributions are:

1. **Long context scaling for RL**: Scale the RL context window to 128k tokens with continued performance improvement as context length increases.
2. **Partial rollouts**: A technique to efficiently handle long reasoning trajectories by reusing previous trajectory segments across training iterations.
3. **Simplified RL framework**: Achieve state-of-the-art results without Monte Carlo tree search, value functions, or process reward models.
4. **Long2short methods**: Transfer thinking priors from long-CoT models to short-CoT models for improved token efficiency.

---

## Approach Details

### Method

The development of Kimi k1.5 consists of four stages: pretraining, vanilla supervised fine-tuning (SFT), long-CoT supervised fine-tuning, and reinforcement learning.

**Problem Formulation.** Given training dataset D = {(x_i, y*_i)} of problems x_i and ground truth answers y*_i, the goal is to train a policy model pi_theta to solve test problems. The chain-of-thought (CoT) method uses intermediate steps z = (z_1, z_2, ..., z_m) to bridge problem x and answer y. The RL objective is:

> max_theta E_{(x,y*) ~ D, (y,z) ~ pi_theta} [r(x, y, y*)]

where r is a reward model that assigns r(x, y, y*) in {0, 1} based on answer correctness.

**Policy Optimization.** The paper employs a variant of online policy mirror descent. At iteration i, using current model pi_{theta_i} as reference, the algorithm optimizes:

> max_theta E_{(x,y*) ~ D} [E_{(y,z) ~ pi_theta} [r(x, y, y*)] - tau * KL(pi_theta(x) || pi_{theta_i}(x))]

This has closed-form solution pi*(y, z|x) = pi_{theta_i}(y, z|x) * exp(r(x, y, y*)/tau) / Z. The gradient for each problem x with k sampled responses is:

> (1/k) * sum_{j=1}^{k} [grad log pi_theta(y_j, z_j|x) * (r(x, y_j, y*) - r_bar) - (tau/2) * grad (log(pi_theta / pi_{theta_i}))^2]

The key distinction from standard policy gradient is that responses are sampled from pi_{theta_i} (off-policy) and an L2 regularization is applied.

**No Value Network.** The paper explicitly excludes value networks, hypothesizing that conventional credit assignment may not be suitable for long-CoT. Exploring erroneous reasoning steps z'_{t+1} is valuable for training if the model learns to recover and reach the correct answer — standard value-based credit assignment would penalize such exploration.

### Key Technical Components

**Length Penalty.** The model exhibits an "overthinking" phenomenon where response length significantly increases during RL training. To address this, a length reward is introduced:

> len_reward(i) = lambda if r(x, y_i, y*) = 1; min(0, lambda) if r(x, y_i, y*) = 0

where lambda = 0.5 - (len(i) - min_len) / (max_len - min_len). This promotes shorter correct responses and penalizes long incorrect responses. The length penalty is gradually warmed up during training.

**Partial Rollouts.** To efficiently handle long-CoT training at 128k context, the system establishes a fixed output token budget per iteration. If a trajectory exceeds the limit, the unfinished portion is saved to a replay buffer and continued in the next iteration. Previous segments (from iterations n-m to n-1) are reused from the buffer, eliminating repeated rollouts. Only the current iteration requires on-policy computation.

**Sampling Strategies.**
- *Curriculum Sampling*: Start with easier tasks and gradually progress to harder ones, since the initial RL model has limited performance.
- *Prioritized Sampling*: Track success rates s_i for each problem and sample proportional to (1 - s_i), focusing on problems where the model underperforms.

**Reward Modeling for Math.** Two reward models are compared:
1. *Classic RM*: Value-head based, ~800k training examples, achieves 84.4% accuracy.
2. *Chain-of-Thought RM*: Generates step-by-step reasoning before correctness judgment in JSON format, ~800k CoT-labeled examples, achieves 98.5% accuracy.

The CoT RM is adopted for RL training due to significantly better accuracy.

**Long2short Methods.** Four approaches to transfer long-CoT capabilities to short-CoT models:
1. *Model Merging*: Average weights of long-CoT and short-CoT models.
2. *Shortest Rejection Sampling*: Sample n=8 responses, select shortest correct one for SFT.
3. *DPO*: Shortest correct solution as positive sample, longer responses (both wrong and 1.5x longer correct) as negatives.
4. *Long2short RL*: Apply length penalty with significantly reduced maximum rollout length.

### Experimental Setup

**Pretraining.** Three stages: (1) Vision-language pretraining establishing language foundation then gradual multimodal integration; (2) Cooldown with curated and synthetic data for reasoning and knowledge; (3) Long-context activation extending to 131,072 tokens with RoPE frequency 1,000,000.

**Vanilla SFT.** ~1M text examples (500k QA, 200k coding, 200k math/science, 5k writing, 20k long-context) + ~1M text-vision examples. Two epochs: first at 32k sequence length, second at 128k. Learning rate: 2e-5 -> 2e-6 (32k stage), re-warmup to 1e-5 -> 1e-6 (128k stage).

**RL Prompt Set Curation.** Three key properties: (1) Diverse coverage across STEM, coding, general reasoning; (2) Balanced difficulty using model-based pass-rate assessment; (3) Accurate evaluability — excludes multiple-choice, true/false, and proof-based questions to avoid reward hacking. Easy-to-hack prompts removed by checking if model guesses correctly within N=8 attempts without CoT.

**Infrastructure.** Iterative synchronous RL framework using Megatron for training and vLLM for inference. Hybrid deployment on same GPUs with <1 minute switching time. Code sandbox using crun (0.04s startup vs 0.12s Docker) and cgroup reusing (120 containers/sec vs 27 Docker).

### Key Results

**Long-CoT Performance (Table 2):**

| Benchmark | Kimi k1.5 | OpenAI o1 | QwQ-32B Preview |
|---|---|---|---|
| MATH-500 (EM) | **96.2** | 94.8 | 90.6 |
| AIME 2024 (Pass@1) | **77.5** | 74.4 | 50.0 |
| Codeforces (Percentile) | **94** | **94** | 62 |
| LiveCodeBench (Pass@1) | 62.5 | **67.2** | 40.6 |
| MathVista-Test (Pass@1) | **74.9** | 71.0 | - |
| MMMU-Val (Pass@1) | 70.0 | **77.3** | - |

**Short-CoT Performance (Table 3):**

| Benchmark | Kimi k1.5 | DeepSeek V3 | GPT-4o | Claude 3.5 |
|---|---|---|---|---|
| MATH-500 (EM) | **94.6** | 90.2 | 74.6 | 78.3 |
| AIME 2024 (Pass@1) | **60.8** | 39.2 | 9.3 | 16.0 |
| LiveCodeBench (Pass@1) | **47.3** | 40.5 | 33.4 | 36.3 |
| MMLU (EM) | 87.4 | 88.5 | 87.2 | **88.3** |
| C-Eval (EM) | **88.3** | 86.5 | 76.0 | 76.7 |

**Long Context Scaling (Section 3.3).** Strong positive correlation between response length and accuracy across 12 benchmarks (Figure 6). The trend slopes range from 1.36e-05 (MATH-500) to 4.24e-05 (GPQA) per token. Final k1.5 scales to 128k context with continued improvement.

**Long2short Token Efficiency (Figure 7).** k1.5-short w/ rl achieves 60.8 Pass@1 on AIME 2024 with only 3,272 average tokens. k1.5-shortest achieves 88.2 on MATH-500 with token count comparable to baseline short models.

**Ablation: Model Size vs Context Length (Figure 8).** Smaller models can match larger model performance by utilizing longer CoTs through RL. However, larger models show better token efficiency (steeper slopes). For best performance, scale context length of larger models. For fixed test-time budget, training smaller models with larger context is viable.

**Ablation: Negative Gradients vs ReST (Figure 10).** The proposed method with negative gradients shows superior sample complexity compared to ReST (which only fits best responses) across all 12 benchmarks.

**Ablation: Curriculum Sampling (Figure 9).** Curriculum learning (uniform problems first, then hard problems from iteration 24) significantly outperforms baseline uniform sampling, reaching ~0.65 accuracy vs ~0.50 baseline.

---

## Limitations and Failure Modes

1. **Model size not disclosed.** The paper does not specify the parameter count of Kimi k1.5, making comparisons difficult.

2. **Overthinking persists.** Despite length penalties, the overthinking phenomenon remains a challenge — response length grows significantly during RL training. The paper acknowledges this needs further study.

3. **LiveCodeBench underperforms o1.** On LiveCodeBench v5, k1.5 achieves 62.5 vs o1's 67.2, suggesting coding performance gaps remain.

4. **MMMU performance gap.** On multimodal understanding (MMMU-Val), k1.5 achieves 70.0 vs o1's 77.3, indicating room for improvement in general multimodal reasoning.

5. **Limited ablation on reward model.** Only math verification accuracy is reported for reward models; impact on final RL performance not directly ablated.

6. **Partial rollout staleness.** Previous trajectory segments from iterations n-m to n-1 are off-policy, but the paper does not study how staleness affects training.

7. **No process reward model comparison.** Claims simplicity over process reward models but does not directly compare with PRM-based approaches.

### Scope and Comparability

- **Codeforces evaluation**: Uses majority voting with self-generated test cases, different from standard evaluation.
- **LiveCodeBench versions differ**: Short-CoT uses v4 (2408-2411), long-CoT uses v5 (2412-2502).
- **Inference details sparse**: Temperature, sampling parameters, and maximum token limits not fully specified.

---

## Conclusions

### Contributions

1. **Long context scaling for RL.** Demonstrated that scaling the RL context window to 128k tokens yields continued performance improvement, identifying context length as a key dimension for RL scaling with LLMs (Sections 1, 3.3).

2. **Partial rollouts technique.** Introduced efficient handling of long reasoning trajectories by reusing previous trajectory segments across iterations, enabling practical training at 128k context (Section 2.6.2).

3. **Simplified RL framework.** Achieved state-of-the-art reasoning performance without Monte Carlo tree search, value functions, or process reward models — through long context scaling and improved policy optimization alone (Section 4).

4. **Long2short knowledge transfer.** Demonstrated multiple methods (model merging, shortest rejection sampling, DPO, long2short RL) to transfer long-CoT capabilities to short-CoT models with improved token efficiency (Section 2.4, 3.4).

5. **Chain-of-thought reward model.** Showed that CoT-augmented reward models (98.5% accuracy) significantly outperform classic value-head reward models (84.4%) for math verification (Section 2.3.5).

6. **Hybrid training-inference infrastructure.** Developed efficient RL infrastructure with <1 minute switching between Megatron training and vLLM inference on shared GPUs (Section 2.6.3).

### Implications

1. **New scaling axis for LLMs.** Reinforcement learning provides a viable path for continued LLM improvement beyond pretraining data limits, with context length as a key scaling dimension. [Speculative: this may define a new compute-optimal frontier trading off pretraining, SFT, and RL budgets.]

2. **Simplicity over complexity.** Complex techniques like MCTS, value functions, and process reward models may be unnecessary when long context scaling is properly exploited. This could significantly simplify deployment and reduce inference cost.

3. **Test-time compute scaling.** The strong correlation between response length and accuracy suggests test-time compute scaling (allowing more tokens) can substitute for model scaling in some regimes, with implications for inference cost optimization.

---

## Key Claims

1. **C1: Long context scaling is a key dimension for RL improvement.** Scaling the RL context window to 128k yields continued performance gains with strong positive correlation between response length and accuracy (slopes 1.36e-05 to 4.24e-05 per token across 12 benchmarks). Status: **supported** (Figures 5-6, Section 3.3).

2. **C2: Strong reasoning without complex techniques.** State-of-the-art performance achieved without MCTS, value functions, or process reward models through long context scaling and policy optimization alone. Status: **supported** (Section 1, 4; comparison limited to o1 without ablation against PRM-based methods).

3. **C3: Kimi k1.5 long-CoT matches OpenAI o1.** 77.5 vs 74.4 on AIME 2024, 96.2 vs 94.8 on MATH-500, 94 vs 94 percentile on Codeforces. Status: **supported** (Table 2). Scope: Pass@1, specific benchmark versions.

4. **C4: Long2short transfer improves token efficiency.** k1.5-short achieves 60.8 on AIME 2024 with only 3,272 average tokens vs ~5,000 for k1.5-long at similar performance. Status: **supported** (Figure 7, Section 3.4).

5. **C5: Partial rollouts enable efficient long-context RL.** Reusing previous trajectory segments eliminates redundant rollouts while maintaining training quality. Status: **supported** (Section 2.6.2; no direct ablation comparing with/without partial rollouts).

6. **C6: Negative gradients improve sample efficiency over ReST.** Consistent improvement across all 12 benchmarks compared to ReST which only fits best responses. Status: **supported** (Figure 10, Section 3.5).

7. **C7: CoT reward model achieves 98.5% vs 84.4% for classic RM.** Chain-of-thought reasoning before correctness judgment significantly improves math verification accuracy. Status: **supported** (Section 2.3.5; limited to spot-check accuracy, not downstream RL performance).

---

## Open Questions

1. **How does overthinking affect generalization?** The paper notes response length grows during RL but does not study whether this degrades out-of-distribution performance or leads to reward hacking. Not addressed.

2. **Can partial rollouts scale beyond 128k?** The technique is presented at 128k context but scaling to longer contexts (e.g., 1M tokens) may face additional challenges. Not addressed.

3. **How do long-CoT patterns transfer across domains?** The paper trains on math and code jointly but does not study whether reasoning patterns learned in one domain transfer to others. Not addressed.

4. **What is the optimal model size vs context length tradeoff?** Figure 8 shows larger models are more token-efficient, but the optimal allocation of compute budget between model scaling and context scaling is not characterized. Not addressed.

5. **How does the approach compare to process reward models?** The paper claims simplicity over PRMs but provides no direct comparison. Not addressed.

---

## Core References and Why They Are Referenced

### Scaling Laws and Pretraining

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Establishes the scaling law context that k1.5 aims to extend via RL as a new scaling axis.

- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models.* Chinchilla scaling laws motivate the search for new scaling dimensions beyond pretraining data.

### Chain-of-Thought and Reasoning

- **Wei et al. (2022)** -- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.* Foundational CoT work that k1.5 extends through RL training rather than prompting.

- **Yao et al. (2024)** -- *Tree of Thoughts.* Planning algorithm baseline that k1.5 aims to match without explicit search tree construction.

- **Snell et al. (2024)** -- *Scaling LLM Test-Time Compute.* Related work on test-time compute scaling that k1.5's context length scaling connects to.

### Reinforcement Learning for LLMs

- **Ouyang et al. (2022)** -- *Training Language Models to Follow Instructions with Human Feedback (InstructGPT).* RLHF foundation that k1.5 builds upon with value-head reward models.

- **OpenAI (2024)** -- *Learning to Reason with LLMs (o1 System Card).* Primary comparison target for k1.5's reasoning performance.

- **Ahmadian et al. (2024)** -- *Back to Basics: Revisiting REINFORCE Style Optimization.* Related work on policy gradient methods without value networks.

- **Gulcehre et al. (2023)** -- *Reinforced Self-Training (ReST).* Baseline for ablation study showing negative gradients improve over ReST.

### Policy Optimization

- **Abbasi-Yadkori et al. (2019)** -- *Politex: Regret Bounds for Policy Iteration Using Expert Prediction.* Theoretical foundation for online mirror descent variant used in k1.5.

- **Tomar et al. (2020)** -- *Mirror Descent Policy Optimization.* Direct predecessor for the policy optimization algorithm.

- **Rafailov et al. (2024)** -- *Direct Preference Optimization (DPO).* Used as one of the long2short methods for token efficiency.

### Infrastructure

- **Shoeybi et al. (2020)** -- *Megatron-LM.* Training framework used in k1.5's hybrid deployment.

- **Kwon et al. (2023)** -- *vLLM: Efficient Memory Management for Large Language Model Serving.* Inference framework for rollout generation.

### Evaluation Benchmarks

- **Hendrycks et al. (2020)** -- *MMLU.* General knowledge benchmark used for short-CoT evaluation.

- **Lightman et al. (2023)** -- *Let's Verify Step by Step.* MATH-500 benchmark used as primary math evaluation.

- **Jain et al. (2024)** -- *LiveCodeBench.* Contamination-free code benchmark used for both short and long-CoT evaluation.
