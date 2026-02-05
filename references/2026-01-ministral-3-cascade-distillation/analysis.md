---
title: "Ministral 3"
authors: "Liu, Khandelwal, Subramanian, Jouault, et al."
year: 2026
venue: "arXiv preprint 2601.08584"
paper_type: preprint
categories: ["model-release", "architecture", "pruning-and-sparsity"]
scope: ["knowledge distillation", "model compression", "cascade pruning", "efficient pretraining", "reasoning models"]
benchmarks_used: ["mmlu", "triviaqa", "math-hendrycks", "agi-eval", "arc", "gpqa", "mbpp", "mmmu", "arena-hard", "livecodebench"]
models_introduced: ["ministral-3-3b", "ministral-3-8b", "ministral-3-14b"]
models_evaluated: ["qwen2-7b", "qwen2-72b", "gemma-7b"]
key_claims:
  - id: C1
    claim: "Cascade Distillation produces competitive models trained on 1-3T tokens by leveraging a 24B parent model, compared to Qwen3 (36T) and Llama3 (15T) trained from scratch"
    evidence: "Section 1, Table 2"
    status: supported
  - id: C2
    claim: "Ministral 3 14B Base closely matches Mistral Small 3.1 Base while being >40% smaller and trained on a much shorter horizon"
    evidence: "Section 1, Table 3"
    status: supported
  - id: C3
    claim: "For pretraining distillation, a smaller teacher (Mistral Small 3.1) outperforms a larger teacher (Mistral Medium 3), but post-training benefits from stronger teachers"
    evidence: "Section 5.1, Figure 3"
    status: supported
  - id: C4
    claim: "Distilling from a post-trained (instruct) teacher during pretraining yields stronger models than distilling from a base teacher, especially for math and code"
    evidence: "Section 5.1, Figure 4"
    status: supported
  - id: C5
    claim: "Ministral 3 14B Reasoning achieves 89.8% on AIME 2024 (pass@16), outperforming Qwen 3 14B (83.7%)"
    evidence: "Table 5"
    status: supported
  - id: C6
    claim: "Layer importance for pruning can be approximated by the ratio of output to input activation norms, providing a simpler proxy than counterfactual perplexity"
    evidence: "Section 3.1, Algorithm 2"
    status: supported
  - id: C7
    claim: "Online DPO significantly improves alignment over SFT and offline DPO variants, and mitigates infinite generation artifacts"
    evidence: "Section 3.2.2"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Ministral 3 uses decoder-only Transformer architecture with GQA, RoPE, SwiGLU, and RMSNorm"
  - target: 2023-10-mistral-7b
    type: extends
    detail: "Builds on Mistral architecture; uses GQA with 32 query heads and 8 KV heads"
  - target: 2024-05-yarn-context-extension
    type: extends
    detail: "Uses YaRN for context extension from 16K to 256K tokens"
  - target: 2024-07-llama-3-herd-of-models
    type: evaluates
    detail: "Compares against Llama 3 training efficiency; achieves competitive results with 1-3T tokens vs 15T"
open_questions:
  - question: "How does Cascade Distillation scale beyond 3 pruning stages? Could it derive even smaller models (1B, 0.5B) effectively?"
    addressed_by: null
  - question: "What is the optimal teacher-student capacity ratio for distillation at different training stages?"
    addressed_by: null
  - question: "Does the 'capacity gap' where stronger teachers hurt pretraining distillation generalize across architectures?"
    addressed_by: null
---

# Ministral 3

**Authors:** Alexander H. Liu, Kartik Khandelwal, Sandeep Subramanian, Victor Jouault, et al. (Mistral AI)
**Date:** January 2026, arXiv:2601.08584

---

## Core Research Problem

Training competitive language models from scratch requires enormous compute budgets: Qwen3 uses 36 trillion tokens and Llama3 uses 15 trillion tokens. This creates significant barriers for organizations seeking to produce efficient, smaller models for resource-constrained deployment. Prior work on knowledge distillation and model pruning (Minitron, Wanda) demonstrated that pretrained models could be compressed, but a systematic approach to iteratively derive multiple model sizes from a single parent while maintaining competitive performance was lacking. The core challenge was: **how to efficiently produce a family of competitive dense models at multiple scales (3B, 8B, 14B) from a single larger parent model using significantly fewer training tokens than from-scratch pretraining.**

---

## Problem Solutions

Ministral 3 addresses this through Cascade Distillation, an iterative pruning and distillation approach:

1. **Iterative prune-distill-repeat.** Starting from Mistral Small 3.1 (24B), progressively prune to 14B, then 8B, then 3B, with distillation training at each stage. This produces competitive models with 1-3T tokens instead of 15-36T.

2. **Multi-stage post-training.** Apply SFT + Online DPO for instruction-following variants, and SFT + GRPO + ODPO for reasoning variants, each distilling from appropriate teacher models.

3. **Unified multimodal architecture.** All models share a frozen 410M parameter ViT vision encoder from Mistral Small 3.1, with trainable projection layers per model size.

---

## Approach Details

### Architecture

All Ministral 3 models are decoder-only Transformers with common architectural choices (Table 1):

| Model | Layers | Latent dim | Q/KV heads | FFN dim | Tied Emb | Context |
|---|---|---|---|---|---|---|
| Ministral 3 14B | 40 | 5120 | 32/8 | 16384 | No | 256K |
| Ministral 3 8B | 34 | 4096 | 32/8 | 14336 | No | 256K |
| Ministral 3 3B | 26 | 3072 | 32/8 | 9216 | Yes | 256K |

Key architectural components:
- **Grouped-Query Attention (GQA):** 32 query heads, 8 key-value heads (Ainslie et al., 2023)
- **RoPE positional embeddings** (Su et al., 2021)
- **SwiGLU activation** (Shazeer, 2020)
- **RMSNorm** (Zhang & Sennrich, 2019)
- **YaRN** for long-context extension (Peng et al., 2023)
- **Position-based softmax temperature scaling** (Nakanishi, 2025; MetaAI, 2025)
- **Vocabulary size:** 131K tokens
- **Tied embeddings:** Only for 3B model to avoid embedding parameters dominating

**Vision encoder:** All models use a frozen 410M parameter ViT copied from Mistral Small 3.1 Base with the Pixtral architecture (Agrawal et al., 2024). The projection layer from ViT to LM space is retrained for each model size.

### Cascade Distillation

The pretraining recipe (Algorithm 1) follows an iterative approach:

```
1. Start with Mistral Small 3.1 (MS3.1) as parent
2. For each target size in [14B, 8B, 3B]:
   a. Prune parent model to target size
   b. Short context distillation (16K context) with MS3.1 as teacher
   c. Long context distillation (256K context) with MS3.1 as teacher
   d. Output of (b) becomes input for pruning the next smaller model
```

This approach avoids data repetition: the entire process goes through the data mix once with pruning en route (Figure 2).

### Pruning Strategy

Three pruning techniques are applied (Algorithm 2):

**1. Layer Pruning:** Rank layers by the ratio of output to input activation norms:
> importance_score = mean(output_norm / input_norm)

This provides a simpler proxy than counterfactual perplexity from Minitron.

**2. Hidden Dimension Pruning:** Apply PCA to concatenated activations from attention normalization and feed-forward normalization layers across all layers. The resulting rotation matrix projects to a lower-dimensional space while maximizing explained variance.

**3. Feedforward Dimension Pruning:** For SwiGLU MLPs expressed as W2(SiLU(W1x) * W3x), compute importance as:
> importance = mean(abs(silu(W1.output) * W3.output))

Keep the top-k dimensions based on this score.

### Distillation

Each child model is trained with logit distillation from the teacher. Key finding: **forward KL distillation objective alone outperforms weighted combinations** of distillation and next-token prediction losses.

**Two-stage pretraining:**
1. **Short context stage:** 16,384 token context window
2. **Long context stage:** Extend to 262,144 tokens using YaRN and position-based temperature scaling

### Post-Training: Instruction-Following

**Supervised Fine-Tuning (SFT):**
- Uses fp8 quantization
- Logit distillation from Mistral Medium 3 (not Mistral Small 3.1)
- Vision encoder remains frozen; adapter is trainable

**Online Direct Preference Optimization (ODPO):**
- For each example, sample two responses from current policy at T=0.7
- Pairwise Reward Model (PWRM) ranks responses
- Modified DPO loss using binomial probabilistic output instead of hard labels
- PWRM temperature calibration and β-rescaling for stability
- Heuristic: responses with infinite loops automatically treated as "loser"
- Tool execution enabled during generation

### Post-Training: Reasoning

Three-stage pipeline starting from pretrained (not ODPO) checkpoint:

**1. Reasoning SFT:** Fine-tune on mixture of short and long chain-of-thought samples across math, coding, dialogue, instruction following, multilingual, tool use, and visual reasoning.

**2. GRPO (Group Relative Policy Optimization):**
- **STEM RL stage:** Train on math, code, visual reasoning with rigorous data filtering
- **General RL stage:** Extend beyond STEM using atomic grading rubrics evaluated by LLM judge
- Maximum generation length: 80K tokens (increased from 32K to reduce truncation)

**3. ODPO:** Post-RL alignment with thinking chunks stripped before reward model scoring.

**3B model special handling:** Vanilla SFT led to brittle, verbose outputs with repetition. Logit distillation from Magistral Small 1.2 was used to reduce verbosity and stabilize RL training.

### Key Results

**Pretraining (Table 2) - Base models:**

| Model | MMLU-Redux | TriviaQA | MATH | AGIEval | Multilingual MMLU |
|---|---|---|---|---|---|
| Qwen 3 14B | 83.7 | 70.3 | 62.0 | 66.1 | 75.4 |
| **Ministral 3 14B** | 82.0 | **74.9** | **67.6** | 64.8 | 74.2 |
| Gemma 3 12B | 76.6 | 78.8 | 48.7 | 58.7 | 69.0 |
| Qwen 3 8B | 79.4 | 63.9 | 57.6 | 59.6 | 70.0 |
| **Ministral 3 8B** | 79.3 | **68.1** | **62.6** | 59.1 | **70.6** |
| Gemma 3 4B | 62.6 | 64.0 | 29.4 | 43.0 | 51.6 |
| Qwen 3 4B | 75.9 | 53.0 | 40.5 | 57.0 | 67.7 |
| **Ministral 3 3B** | 73.5 | **59.2** | **60.1** | 51.1 | 65.2 |

Key observations:
- Ministral 3 14B outperforms Qwen 3 14B on TriviaQA (+4.6) and MATH (+5.6)
- Ministral 3 8B outperforms larger Gemma 12B on most benchmarks
- Ministral 3 3B shows strong MATH performance (60.1% vs Qwen 3 4B's 40.5%)

**Post-training - Instruct models (Table 4):**

| Model | Arena Hard | WildBench | MATH (maj@1) | MM MTBench |
|---|---|---|---|---|
| Qwen3 14B (Non-Thinking) | 42.7 | 65.1 | 87.0 | N/A |
| **Ministral 3 14B** | **55.1** | **68.5** | **90.4** | 84.9 |
| Gemma3-12B-Instruct | 43.6 | 63.2 | 85.4 | 67.0 |
| Qwen3-VL-8B-Instruct | **52.8** | 66.3 | **94.6** | 80.0 |
| **Ministral 3 8B** | 50.9 | **66.8** | 87.6 | **80.8** |

**Reasoning models (Table 5) - pass@16:**

| Benchmark | Qwen 3 14B | Ministral 3 14B | Qwen3-VL 8B | Ministral 3 8B | Qwen3-VL 4B | Ministral 3 3B |
|---|---|---|---|---|---|---|
| AIME 2024 | 83.7 | **89.8** | 86.0 | 86.0 | 72.9 | **77.5** |
| AIME 2025 | 73.7 | **85.0** | **79.8** | 78.7 | 69.7 | **72.1** |
| HMMT 2025 | 55.8 | **67.5** | 57.5 | 55.8 | 50.8 | **51.7** |
| GPQA Diamond | 66.3 | **71.2** | 67.1 | 66.8 | **60.1** | 53.4 |
| LiveCodeBench v6 | 59.3 | **64.6** | 58.0 | **61.6** | 51.3 | **54.8** |

### Teacher Selection Findings

**Capacity gap (Figure 3):** For pretraining distillation, Mistral Small 3.1 outperforms the stronger Mistral Medium 3 as teacher, even in non-FLOP-matched settings. However, post-training benefits from stronger teachers.

**Base vs. instruct teacher (Figure 4):** Distilling from a post-trained (instruct) teacher during pretraining yields stronger models, especially for MATH and code, with smaller impact on knowledge benchmarks (MMLU, TriviaQA).

**Preference-tuned teachers:** Distilling from a preference-tuned checkpoint during SFT is substantially better than from an SFT-only checkpoint, and gains persist after the student's own preference tuning.

---

## Limitations and Failure Modes

The paper acknowledges the following limitations:

1. **3B model sensitivity.** The 3B base model is more sensitive to hyperparameter choice in fine-tuning than 14B and 8B variants (footnote 4).

2. **Verbosity issues.** Vanilla SFT on 3B led to brittle, overly verbose outputs with repetition and infinite generations, requiring special handling with logit distillation.

3. **Reasoning-chat tradeoff.** Reasoning models lag in general conversational quality compared to instruct variants, requiring ODPO post-RL to address.

4. **Long CoT tradeoffs.** Increasing long chain-of-thought data in SFT improves STEM benchmarks but leads to excessive reflection, internal monologues, and backtracking behavior undesirable for general chat.

5. **3B ODPO limited gains.** The 3B model did not show significant public benchmark improvements from ODPO, though internal human evaluations improved.

---

## Conclusions

### Contributions

1. **Cascade Distillation methodology.** Introduced an iterative prune-distill-repeat approach that derives competitive models at 3B, 8B, and 14B scales from a 24B parent using 1-3T tokens instead of 15-36T from-scratch pretraining.

2. **Pruning heuristics.** Demonstrated that layer importance can be approximated by output/input activation norm ratios, providing a simpler alternative to counterfactual perplexity.

3. **Teacher selection insights.** Confirmed that (a) stronger teachers don't always yield better students in pretraining, (b) post-trained teachers are better than base teachers for pretraining distillation, (c) preference-tuned teachers are better than SFT-only teachers.

4. **Open-weight release.** Released 9 models (3 sizes x 3 variants) under Apache 2.0 with 256K context and vision capabilities.

### Implications

1. **Compute efficiency.** Cascade Distillation offers a path to producing model families at multiple scales without full pretraining runs for each size, potentially democratizing access to competitive smaller models.

2. **Distillation research.** The finding that stronger teachers can hurt pretraining distillation while helping post-training suggests different mechanisms at play, warranting further investigation into the "capacity gap" phenomenon.

3. **Reasoning model development.** The multi-stage pipeline (SFT + GRPO + ODPO) with separate STEM and General RL stages provides a template for training reasoning models that maintain conversational quality.

---

## Key Claims

1. **Cascade Distillation produces competitive models efficiently.** Models trained on 1-3T tokens compete with Qwen3 (36T) and Llama3 (15T). Evidence: Tables 2-5. Status: **supported**.

2. **Ministral 3 14B matches 40% larger Mistral Small 3.1.** Comparable performance despite significant parameter reduction. Evidence: Table 3. Status: **supported**.

3. **Smaller teachers can outperform larger teachers for pretraining distillation.** Mistral Small 3.1 beats Mistral Medium 3 as pretraining teacher. Evidence: Figure 3, Section 5.1. Status: **supported**.

4. **Post-trained teachers yield stronger students.** Instruct teacher outperforms base teacher during pretraining, especially for STEM. Evidence: Figure 4. Status: **supported**.

5. **Ministral 3 14B Reasoning achieves 89.8% on AIME 2024.** Outperforms Qwen 3 14B (83.7%) on math competition benchmarks. Evidence: Table 5. Status: **supported**.

6. **Output/input norm ratio is effective for layer pruning.** Simpler than counterfactual perplexity while being effective. Evidence: Algorithm 2, Section 3.1. Status: **supported**.

7. **Online DPO improves over SFT and offline DPO.** Particularly important for mitigating infinite generation artifacts. Evidence: Section 3.2.2. Status: **supported**.

---

## Open Questions

1. **Cascade depth limits.** How many pruning stages can Cascade Distillation support before quality degrades significantly? Could it derive 1B or 0.5B models effectively?

2. **Optimal teacher-student ratio.** What is the ideal capacity ratio between teacher and student at different training stages? The capacity gap phenomenon suggests this is non-trivial.

3. **Generalization of capacity gap.** Does the finding that stronger teachers hurt pretraining distillation generalize across different architectures and training setups?

4. **Long-context quality.** How does Ministral 3's 256K context perform on tasks requiring reasoning over the full context, beyond simple retrieval?

5. **Verbosity-quality tradeoff.** Can the verbosity issues observed in 3B be systematically addressed without hurting reasoning capabilities?

---

## Core References and Why They Are Referenced

### Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The decoder-only Transformer architecture that Ministral 3 builds upon.

- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models.* Grouped-Query Attention with 32 query and 8 KV heads used across all Ministral 3 sizes.

- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE positional encoding used in all models.

- **Shazeer (2020)** -- *GLU Variants Improve Transformer.* SwiGLU activation used in all models.

### Pruning and Distillation

- **Sun et al. (2023)** -- *Wanda: A Simple and Effective Pruning Approach for Large Language Models.* Pruning methodology that Ministral 3's approach builds on.

- **Muralidharan et al. (2024)** -- *Compact Language Models via Pruning and Knowledge Distillation (Minitron).* Direct predecessor for the Cascade Distillation approach; Ministral 3 uses similar pruning strategies but with simpler layer importance scoring.

- **Busbridge et al. (2025)** -- *Distillation Scaling Laws.* Confirms the capacity gap observation where stronger teachers don't always yield better students.

- **Goyal et al. (2025)** -- *Distilled Pretraining.* Confirms that post-trained teachers outperform base teachers for pretraining distillation.

### Context Extension

- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Used for extending context from 16K to 256K tokens.

- **Nakanishi (2025)** -- *Scalable-Softmax is Superior for Attention.* Position-based temperature scaling used for long-context extension.

### Post-Training

- **Ouyang et al. (2022)** -- *Training Language Models to Follow Instructions with Human Feedback.* Foundation for instruction-following fine-tuning approach.

- **Rafailov et al. (2023)** -- *Direct Preference Optimization.* DPO framework that ODPO extends with online sampling.

- **Guo et al. (2024)** -- *Direct Language Model Alignment from Online AI Feedback.* Online DPO methodology adopted for Ministral 3.

- **Shao et al. (2024)** -- *DeepSeekMath.* GRPO algorithm used for reasoning model training.

- **DeepSeek-AI et al. (2025)** -- *DeepSeek-R1.* GRPO training recipe followed for reasoning models.

### Evaluation

- **Hendrycks et al. (2020, 2021)** -- *MMLU* and *MATH.* Primary benchmarks for general knowledge and mathematical reasoning.

- **Rein et al. (2024)** -- *GPQA.* Graduate-level science QA benchmark for evaluating reasoning.

- **Li et al. (2024)** -- *Arena-Hard.* Post-training benchmark for instruction-following quality.

- **Jain et al. (2024)** -- *LiveCodeBench.* Contamination-free code evaluation benchmark.
