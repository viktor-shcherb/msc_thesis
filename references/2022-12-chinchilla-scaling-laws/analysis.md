---
title: "Training Compute-Optimal Large Language Models"
authors: "Hoffmann, Borgeaud, Mensch, Buchatskaya, Cai, Rutherford, et al."
year: 2022
venue: "NeurIPS 2022"
paper_type: conference-paper
categories: ["scaling-laws", "learning-theory"]
scope: ["compute-optimal training", "dense transformers", "autoregressive language models"]
benchmarks_used: ["mmlu", "perplexity-wikitext103", "hellaswag", "piqa", "winogrande", "boolq", "natural-questions", "triviaqa", "race", "truthfulqa"]
models_introduced: ["chinchilla-70b"]
models_evaluated: ["chinchilla-70b", "gopher-280b", "gpt-3-175b"]
key_claims:
  - id: C1
    claim: "For compute-optimal training, model size and number of training tokens should be scaled equally"
    evidence: "Table 2, Section 3.4; three independent approaches yield N_opt ∝ C^0.5 and D_opt ∝ C^0.5"
    status: supported
    scope: "dense autoregressive transformers, single-epoch training"
    magnitude: "a ≈ 0.50, b ≈ 0.50 vs Kaplan et al. a = 0.73, b = 0.27"
  - id: C2
    claim: "Current large language models are significantly undertrained"
    evidence: "Figure 1, Table 1; models like GPT-3 (175B), Gopher (280B), MT-NLG (530B) trained on ~300B tokens"
    status: supported
    scope: "models trained as of March 2022"
    magnitude: "GPT-3 should use 3.7T tokens, Gopher should use 5.9T tokens for optimal performance"
  - id: C3
    claim: "Chinchilla (70B, 1.4T tokens) outperforms Gopher (280B, 300B tokens) with same compute budget"
    evidence: "Table 6, Figure 5, Figure 6, Figure 7; Section 4.2"
    status: supported
    scope: "same compute budget (5.76 × 10^23 FLOPs)"
    magnitude: "67.6% vs 60.0% on MMLU (+7.6 percentage points)"
  - id: C4
    claim: "The parametric loss function L(N,D) = E + A/N^α + B/D^β accurately models training loss"
    evidence: "Section 3.3, Equation 2, Figure 4"
    status: supported
    scope: "dense transformers, MassiveText dataset"
    magnitude: "α = 0.34, β = 0.28, E = 1.69"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: evaluates
    detail: "Uses transformer architecture as the basis for all experiments"
  - target: 2019-02-gpt-2-language-models-unsupervised
    type: extends
    detail: "Formalizes the implicit scaling assumptions in GPT-2, showing that both GPT-2 and GPT-3 were undertrained relative to compute-optimal allocation"
  - target: 2023-02-llama-open-efficient-foundation
    type: extended-by
    detail: "LLaMA explicitly follows Chinchilla scaling recommendations"
  - target: 2020-12-gpt-3-few-shot-learners
    type: extends
    detail: "Revises GPT-3's implicit scaling assumptions, demonstrating that GPT-3 (175B, 300B tokens) was undertrained and should have used 3.7T tokens for optimal compute allocation"
  - target: 2024-08-scaling-llm-test-time-compute
    type: extended-by
    detail: "Extends compute-optimal scaling from pretraining to test-time, comparing FLOPs allocated to pretraining vs inference in a matched evaluation"
open_questions:
  - question: "Do scaling laws hold in the multi-epoch training regime?"
    addressed_by: null
  - question: "How do scaling laws differ for mixture-of-expert models?"
    addressed_by: null
  - question: "What is the optimal scaling relationship at compute budgets beyond 10^26 FLOPs?"
    addressed_by: null
---

# Training Compute-Optimal Large Language Models

**Authors:** Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, Laurent Sifre (DeepMind)
**Date:** December 2022, NeurIPS 2022; arXiv:2203.15556

---

## Core Research Problem

Prior work by Kaplan et al. (2020) established power-law relationships between model size and performance, leading to a paradigm of training increasingly large models on relatively fixed amounts of data (~300B tokens). This approach suggested that for a 10× increase in compute budget, model size should increase 5.5× while training tokens should only increase 1.8×.

However, this recommendation suffers from a critical methodological flaw: Kaplan et al. used a fixed learning rate schedule for all models regardless of training duration. This prevents them from modeling the impact of training length on final loss, leading to underestimating the benefits of training smaller models for longer.

The core question is: **Given a fixed compute budget, what is the optimal allocation between model size and training data?**

---

## Problem Solutions

The paper proposes that model size and training tokens should scale **equally** with compute:

1. **Revised scaling exponents:** For optimal training, N_opt ∝ C^a and D_opt ∝ C^b where a ≈ b ≈ 0.5, in contrast to Kaplan et al.'s a = 0.73, b = 0.27.
2. **Methodological improvement:** Match the learning rate cosine schedule length to the number of training tokens for each model configuration.
3. **Validation:** Train Chinchilla (70B parameters, 1.4T tokens) using the same compute as Gopher (280B parameters, 300B tokens) and demonstrate superior performance.

---

## Approach Details

### Method

The authors model the final pre-training loss L(N, D) as a function of model parameters N and training tokens D. Given compute budget C where FLOPs(N, D) = C, they seek:

> N_opt(C), D_opt(C) = argmin_{N,D s.t. FLOPs(N,D)=C} L(N, D)

Three independent approaches are used to estimate these optimal allocation functions.

### Key Technical Components

#### Approach 1: Fix Model Sizes, Vary Training Tokens

- Train models from 70M to 10B parameters
- Each model trained for 4 different training horizons (16× range)
- Learning rate decays 10× over a cosine schedule matched to training length
- Extract envelope of minimum loss per FLOP
- Fit power laws to optimal N and D: **a = 0.50, b = 0.50**

#### Approach 2: IsoFLOP Profiles

- Fix 9 different FLOP budgets (6×10^18 to 3×10^21 FLOPs)
- Vary model size (up to 16B parameters) for each budget
- Fit parabola to loss vs. parameters for each IsoFLOP curve
- Find minimum loss model size for each budget
- Result: **a = 0.49, b = 0.51**

#### Approach 3: Parametric Loss Function

Model loss with classical risk decomposition:

> L̂(N, D) ≜ E + A/N^α + B/D^β

Where:
- E: Bayes risk (entropy of natural text)
- A/N^α: functional approximation error (model capacity)
- B/D^β: optimization suboptimality (finite training data)

Fitted parameters: E = 1.69, A = 406.4, B = 410.7, α = 0.34, β = 0.28

The efficient frontier is derived analytically:

> N_opt(C) = G(C/6)^a, D_opt(C) = G^{-1}(C/6)^b

where G = (αA/βB)^{1/(α+β)}, a = β/(α+β), b = α/(α+β)

Result: **a = 0.46, b = 0.54**

### Experimental Setup

**Training Data:** MassiveText (same as Gopher), with slight distribution adjustments for Chinchilla:
- MassiveWeb: 45%
- Books: 30%
- C4: 10%
- News: 10%
- GitHub: 4%
- Wikipedia: 1%

**Scaling Experiments:**
- Over 400 models trained
- Parameter range: 70M to 16B
- Token range: 5B to 500B
- Hardware: TPUv3/TPUv4 with JAX and Haiku

**Chinchilla Configuration (70B):**
- 80 layers, 64 attention heads, 128 key/value size, d_model = 8192
- Learning rate: 1×10^{-4} with cosine decay
- Batch size: 1.5M → 3M tokens (doubled midway)
- Optimizer: AdamW (vs. Adam for Gopher)
- Training: 1.4T tokens

**Reproducibility:** Code not released; hyperparameters detailed in Table 4 and Appendix.

### Key Results

| Model | Parameters | Training Tokens | MMLU 5-shot | Compute (FLOPs) |
|-------|------------|-----------------|-------------|-----------------|
| Chinchilla | 70B | 1.4T | **67.6%** | 5.76×10^23 |
| Gopher | 280B | 300B | 60.0% | 5.76×10^23 |
| GPT-3 | 175B | 300B | 43.9% | ~3.6×10^23 |
| MT-NLG 530B | 530B | 270B | - | ~10^24 |

**Projected Optimal Configurations (Table 3):**

| Parameters | Optimal FLOPs | Optimal Tokens |
|------------|---------------|----------------|
| 1B | 1.21×10^20 | 20.2B |
| 10B | 1.23×10^22 | 205.1B |
| 67B | 5.76×10^23 | 1.5T |
| 175B | 3.85×10^24 | 3.7T |
| 280B | 9.90×10^24 | 5.9T |
| 1T | 1.27×10^26 | 21.2T |

**Key Takeaways:**
- Chinchilla outperforms Gopher on all 20 subsets of The Pile (Figure 5)
- Chinchilla improves on 51/57 MMLU tasks vs. Gopher (Figure 6)
- Chinchilla improves on 58/62 BIG-bench tasks vs. Gopher (Figure 7)
- 4× smaller model enables substantially reduced inference cost

### Comparison with Prior Scaling Laws

| Approach | N_opt ∝ C^a | D_opt ∝ C^b |
|----------|-------------|-------------|
| Approach 1 (envelope) | 0.50 | 0.50 |
| Approach 2 (IsoFLOP) | 0.49 | 0.51 |
| Approach 3 (parametric) | 0.46 | 0.54 |
| Kaplan et al. (2020) | 0.73 | 0.27 |

---

## Limitations and Failure Modes

### Author-Acknowledged Limitations

1. **Limited large-scale validation:** Only two comparable runs at large scale (Chinchilla and Gopher); no intermediate-scale validation points.

2. **Power-law assumption:** The analysis assumes power-law relationships, but Appendix E shows curvature in the FLOP-loss frontier at high compute, suggesting optimal models may be even smaller than predicted.

3. **Single-epoch training:** All training runs used less than one epoch; the multi-epoch regime may have different scaling properties.

4. **Dataset dependence:** Results may not generalize to all datasets, though Appendix C shows similar results on C4 and GitHub code.

### Scope and Comparability

**What was not tested:**
- Mixture-of-expert models (scaling may differ; Clark et al. 2022 suggests diminishing returns)
- Retrieval-augmented models
- Multi-epoch training regimes
- Non-English data
- Instruction-tuned or RLHF models

**Comparability notes:**
- Different tokenizers between Chinchilla and Gopher (94.15% overlap; Chinchilla removes NFKC normalization)
- Different optimizers (AdamW vs. Adam; Figure A6 shows AdamW improves performance)
- Slight differences in training data distribution

### Failure Cases

On MMLU, Chinchilla underperforms Gopher on 4/57 tasks:
- college_mathematics
- econometrics
- moral_scenarios
- formal_logic

On BIG-bench, Chinchilla underperforms on 4/62 tasks:
- crash_blossom
- dark_humor_detection
- mathematical_induction
- logical_args

---

## Conclusions

### Contributions

1. **Revised scaling laws:** Established that model size and training tokens should scale equally (a ≈ b ≈ 0.5) with compute, contradicting the prior consensus from Kaplan et al. (2020) that favored larger models (a = 0.73).

2. **Three independent estimation approaches:** Provided robust evidence through training curve envelopes, IsoFLOP profiles, and parametric loss fitting, all yielding consistent predictions.

3. **Chinchilla validation:** Trained a 70B parameter model on 1.4T tokens that outperforms the 280B Gopher model across nearly all benchmarks while using the same compute budget.

4. **Practical implications for inference:** A 4× smaller model with better performance substantially reduces memory footprint and inference cost, enabling broader deployment.

5. **Parametric loss function:** Proposed and fitted L(N,D) = E + A/N^α + B/D^β, providing a theoretical framework for predicting optimal allocation.

### Implications

1. **Training data is the bottleneck:** The results suggest that scaling to larger datasets is essential; a 175B model should be trained on 3.7T tokens, far exceeding datasets available at the time.

2. **Existing models are undertrained:** Most large models (GPT-3, Gopher, MT-NLG 530B) were trained on ~300B tokens but would benefit from 5-20× more training data.

3. **Inference efficiency gains:** Compute-optimal models are smaller than previously thought, which has significant practical benefits for deployment and environmental cost.

4. **Dataset quality matters:** Speculatively, the benefits of scaling data depend on data quality, highlighting the importance of responsible dataset curation.

---

## Key Claims

1. **C1: Equal scaling of parameters and data.** For compute-optimal training, N_opt ∝ C^0.5 and D_opt ∝ C^0.5, meaning both should scale equally. Evidence: Three independent approaches (Table 2) with bootstrapped confidence intervals. Scope: Dense autoregressive transformers trained for less than one epoch.

2. **C2: Current LLMs are undertrained.** Models like GPT-3 (175B), Gopher (280B), and MT-NLG (530B) are significantly larger than optimal for their compute budgets. Evidence: Figure 1, Table 3 projections. Magnitude: GPT-3 should be ~67B with 1.5T tokens; Gopher should be ~67B with 1.5T tokens.

3. **C3: Chinchilla outperforms larger models.** With the same compute budget, Chinchilla (70B, 1.4T tokens) outperforms Gopher (280B, 300B tokens). Evidence: Table 6 (+7.6% on MMLU), Figure 5 (all Pile subsets), Table 7 (reading comprehension). Scope: Same FLOPs budget of 5.76×10^23.

4. **C4: Parametric loss decomposition is accurate.** The loss function L(N,D) = E + A/N^α + B/D^β with E=1.69, α=0.34, β=0.28 accurately predicts training loss. Evidence: Figure 4, Section 3.3. Scope: MassiveText dataset, dense transformers.

---

## Open Questions

1. **Multi-epoch training:** How do scaling laws change when training for multiple epochs? All experiments used less than one epoch.

2. **Mixture-of-experts:** Do the same scaling relationships hold for sparse MoE models? Clark et al. (2022) suggests diminishing returns at scale.

3. **Curvature at high compute:** Appendix E shows negative curvature in the frontier at high compute, suggesting even smaller models may be optimal. What is the asymptotic behavior?

4. **Data quality vs. quantity:** At what point does adding more data provide diminishing returns, and how does data quality interact with scaling?

5. **Transfer to downstream tasks:** Do compute-optimal pretraining configurations remain optimal after fine-tuning or instruction-tuning?

---

## Core References and Why They Are Referenced

### Scaling Law Foundations

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* The primary work this paper contradicts. Established N_opt ∝ C^0.73, D_opt ∝ C^0.27 using fixed learning rate schedules, leading to the "scale model size" paradigm.

### Models Compared

- **Brown et al. (2020)** -- *Language Models are Few-Shot Learners.* GPT-3 (175B, 300B tokens) serves as a key comparison point, demonstrating the "train on ~300B tokens" convention.

- **Rae et al. (2021)** -- *Scaling Language Models: Methods, Analysis & Insights from Training Gopher.* Gopher (280B, 300B tokens) is the direct comparison model; Chinchilla uses the same dataset and compute budget.

- **Smith et al. (2022)** -- *Using Deepspeed and Megatron to Train Megatron-Turing NLG 530B.* MT-NLG (530B, 270B tokens) represents the largest dense model at the time, following the scale-model-size paradigm.

### Architecture and Training

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational transformer architecture used for all models.

- **Loshchilov and Hutter (2019)** -- *Decoupled Weight Decay Regularization.* AdamW optimizer used for Chinchilla, shown to outperform Adam (Figure A6).

### Evaluation Benchmarks

- **Hendrycks et al. (2020)** -- *Measuring Massive Multitask Language Understanding.* MMLU benchmark where Chinchilla achieves 67.6% vs. Gopher's 60.0%.

- **BIG-bench collaboration (2021)** -- *Beyond the Imitation Game.* BIG-bench tasks where Chinchilla improves average accuracy from 54.4% to 65.1%.

- **Gao et al. (2020)** -- *The Pile: An 800GB Dataset of Diverse Text for Language Modeling.* The Pile evaluation sets where Chinchilla outperforms on all 20 subsets.
