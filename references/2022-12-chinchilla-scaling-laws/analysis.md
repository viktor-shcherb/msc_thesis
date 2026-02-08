---
title: "Training Compute-Optimal Large Language Models"
authors: "Hoffmann, Borgeaud, Mensch, Buchatskaya, Cai, Rutherford, et al."
year: 2022
venue: "NeurIPS 2022"
paper_type: conference-paper
categories: ["scaling-laws", "learning-theory"]
scope: ["compute-optimal training", "dense transformers", "autoregressive language models"]
benchmarks_used: ["mmlu", "perplexity-wikitext103", "perplexity-pile", "hellaswag", "piqa", "winogrande", "siqa", "boolq", "natural-questions", "triviaqa", "race", "truthfulqa", "lambada"]
models_introduced: ["chinchilla-70b"]
models_evaluated: ["chinchilla-70b", "gopher-280b", "gpt-3-175b"]
key_claims:
  - id: C1
    claim: "For compute-optimal training, model size and number of training tokens should be scaled equally: N_opt proportional to C^a and D_opt proportional to C^b where a ≈ b ≈ 0.5"
    evidence: "Table 2, Section 3.4; three independent approaches with bootstrapped confidence intervals"
    status: supported
    scope: "dense autoregressive transformers, single-epoch training, 70M-16B parameter range, MassiveText dataset"
    magnitude: "a ≈ 0.50, b ≈ 0.50 vs Kaplan et al. a = 0.73, b = 0.27"
  - id: C2
    claim: "Current large language models are significantly undertrained relative to their compute budgets"
    evidence: "Figure 1, Table 1, Table 3; GPT-3 (175B, 300B tokens), Gopher (280B, 300B tokens), MT-NLG (530B, 270B tokens) all trained on ~300B tokens"
    status: supported
    scope: "models trained as of March 2022 on approximately 300B tokens"
    magnitude: "GPT-3 should use 3.7T tokens, Gopher should use 5.9T tokens for compute-optimal allocation (Table 3)"
  - id: C3
    claim: "Chinchilla (70B, 1.4T tokens) outperforms Gopher (280B, 300B tokens) using the same compute budget"
    evidence: "Table 6, Table 7, Table 8, Table 9, Figure 5, Figure 6, Figure 7; Section 4.2"
    status: supported
    scope: "same compute budget of 5.76 x 10^23 FLOPs, same training dataset (MassiveText)"
    magnitude: "67.6% vs 60.0% on MMLU 5-shot (+7.6 pp); 65.1% vs 54.4% on BIG-bench average (+10.7 pp); outperforms on all 20 Pile subsets"
  - id: C4
    claim: "The parametric loss function L(N,D) = E + A/N^alpha + B/D^beta accurately models training loss across model sizes and token counts"
    evidence: "Section 3.3, Equation 2, Figure 4"
    status: supported
    scope: "dense transformers, MassiveText dataset, model sizes 70M-16B, token counts 5B-500B"
    magnitude: "yields a = 0.46, b = 0.54 for the efficient frontier, consistent with the other two approaches"
  - id: C5
    claim: "Chinchilla shows improved gender bias resolution over Gopher, with uneven improvement rates across pronoun groups"
    evidence: "Table 10, Section 4.2.7"
    status: supported
    scope: "Winogender zero-shot evaluation"
    magnitude: "overall 78.3% vs 71.4% (+6.9 pp); female gotcha examples improve by 10 pp (76.7% vs 66.7%)"
  - id: C6
    claim: "Compute-optimal training does not meaningfully increase unconditional toxicity generation"
    evidence: "Section 4.2.7, PerspectiveAPI analysis of 25,000 unprompted samples"
    status: supported
    scope: "unprompted generation, PerspectiveAPI classifier"
    magnitude: "mean toxicity 0.087 vs 0.081 (Gopher), 95th percentile 0.238 vs 0.230 -- negligible difference"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: evaluates
    detail: "Uses transformer architecture as the basis for all experiments"
  - target: 2019-02-gpt-2-language-models-unsupervised
    type: extends
    detail: "Formalizes the implicit scaling assumptions in GPT-2, showing that both GPT-2 and GPT-3 were undertrained relative to compute-optimal allocation"
  - target: 2023-02-llama-open-efficient-foundation
    type: extended-by
    detail: "LLaMA explicitly follows Chinchilla scaling recommendations, training smaller models on more tokens"
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
  - question: "What is the optimal scaling relationship at compute budgets beyond 10^26 FLOPs, given the observed negative curvature in Appendix E?"
    addressed_by: null
  - question: "At what point does adding more training data provide diminishing returns, and how does data quality interact with scaling?"
    addressed_by: null
  - question: "Do compute-optimal pretraining configurations remain optimal after fine-tuning or instruction-tuning?"
    addressed_by: null
---

# Training Compute-Optimal Large Language Models

**Authors:** Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, Tom Hennigan, Eric Noland, Katie Millican, George van den Driessche, Bogdan Damoc, Aurelia Guy, Simon Osindero, Karen Simonyan, Erich Elsen, Jack W. Rae, Oriol Vinyals, Laurent Sifre (DeepMind)
**Date:** December 2022, NeurIPS 2022; arXiv:2203.15556

---

## Core Research Problem

Prior work by Kaplan et al. (2020) -- *Scaling Laws for Neural Language Models* -- established power-law relationships between model size and performance, concluding that for a 10x increase in compute budget, model size should increase 5.5x while training tokens should only increase 1.8x (N_opt proportional to C^0.73, D_opt proportional to C^0.27). This led to a paradigm of training increasingly large models on a relatively fixed amount of data: GPT-3 (175B), Gopher (280B), Jurassic-1 (178B), and MT-NLG (530B) were all trained on approximately 300B tokens (Table 1, Section 2).

However, this conclusion rests on a **critical methodological flaw**: Kaplan et al. used a fixed learning rate cosine schedule for all models regardless of training duration. This means that intermediate loss estimates for shorter training runs are overestimates, because the learning rate schedule does not match the actual number of training tokens. The result is an underestimation of the benefit of training smaller models for longer (Section 2; Figure A1).

The core question is: **given a fixed compute budget, what is the optimal allocation between model size and number of training tokens?**

---

## Problem Solutions

The paper proposes that model size and training tokens should be scaled **equally** with compute, fundamentally revising the Kaplan et al. (2020) recommendation:

1. **Revised scaling exponents:** For optimal training, N_opt proportional to C^a and D_opt proportional to C^b where a ≈ b ≈ 0.5, established through three independent estimation approaches (Table 2, Section 3.4).
2. **Methodological correction:** Match the learning rate cosine schedule length to the number of training tokens for each model configuration, removing the bias in Kaplan et al.'s analysis.
3. **Empirical validation:** Train Chinchilla (70B parameters, 1.4T tokens) using the same compute as Gopher (280B parameters, 300B tokens) and demonstrate uniformly superior performance across a large range of benchmarks (Section 4.2).

---

## Approach Details

### Method

The authors model the final pre-training loss L(N, D) as a function of model parameters N and training tokens D. Given compute budget C where FLOPs(N, D) = C, they seek:

> N_opt(C), D_opt(C) = argmin_{N,D s.t. FLOPs(N,D)=C} L(N, D)

Three independent approaches are used to estimate these optimal allocation functions, all yielding consistent predictions (Section 3, Equation 1).

### Key Technical Components

#### Approach 1: Fix Model Sizes, Vary Training Tokens (Section 3.1)

- Models ranging from 70M to over 10B parameters, each trained for 4 different training horizons (16x range in number of training tokens)
- Learning rate decays 10x over a cosine schedule **matched to training length** (contrast with Kaplan et al.'s fixed schedule)
- Training loss curves are smoothed and interpolated; at 1500 logarithmically spaced FLOP values, the model size achieving the lowest loss is identified
- Power laws fitted to extract the envelope of minimum loss per FLOP
- Result: **a = 0.50 (90% CI: 0.488-0.502), b = 0.50 (90% CI: 0.501-0.512)** (Table 2)

#### Approach 2: IsoFLOP Profiles (Section 3.2)

- 9 different FLOP budgets fixed (6 x 10^18 to 3 x 10^21 FLOPs)
- Model size varied (up to 16B parameters) for each budget, with cosine schedule length matched to the target token count
- A parabola is fitted to loss vs. parameters for each IsoFLOP curve, yielding a clear valley at the optimal model size (Figure 3, left)
- Power laws fitted to the minima to project optimal N and D
- Result: **a = 0.49 (90% CI: 0.462-0.534), b = 0.51 (90% CI: 0.483-0.529)** (Table 2)

#### Approach 3: Parametric Loss Function (Section 3.3)

Model loss with classical risk decomposition:

> L_hat(N, D) = E + A / N^alpha + B / D^beta

Where:
- E: Bayes risk (entropy of natural text) -- the irreducible loss of an ideal generative process
- A / N^alpha: functional approximation error (limited model capacity)
- B / D^beta: optimization suboptimality (finite training data)

Parameters estimated by minimizing Huber loss (delta = 10^-3) between predicted and observed log loss using L-BFGS with a grid of initialisations (Equation 3, Section 3.3).

The efficient frontier is derived analytically:

> N_opt(C) = G * (C/6)^a,    D_opt(C) = G^{-1} * (C/6)^b

where G = (alpha * A / (beta * B))^{1/(alpha + beta)}, a = beta / (alpha + beta), b = alpha / (alpha + beta) (Equation 4).

Result: **a = 0.46 (90% CI: 0.454-0.455), b = 0.54 (90% CI: 0.542-0.543)** (Table 2)

This approach predicts even smaller optimal models than Approaches 1 and 2 at high compute budgets, due to the Huber loss placing more weight on higher-FLOP data points (which show negative curvature in the frontier -- see Appendix E) (Section 3.4).

### Experimental Setup

**Training Data:** MassiveText (same dataset as Gopher), with a slightly different subset distribution for Chinchilla to account for more training tokens (Table A1):
- MassiveWeb: 45%
- Books: 30%
- C4: 10%
- News: 10%
- GitHub: 4%
- Wikipedia: 1%

**Scaling Experiments:**
- Over 400 models trained
- Parameter range: 70M to 16B (Approach 2 uses up to 16B; Approach 1 uses up to 10B)
- Token range: 5B to over 400B (500B stated in abstract)
- Hardware: TPUv3/TPUv4 with JAX (Bradbury et al., 2018) and Haiku (Hennigan et al., 2020)
- All training runs used less than one epoch of data

**Chinchilla Configuration (70B) (Table 4):**

| | Chinchilla 70B | Gopher 280B |
|---|---|---|
| Layers | 80 | 80 |
| Number Heads | 64 | 128 |
| Key/Value Size | 128 | 128 |
| d_model | 8,192 | 16,384 |
| Max LR | 1 x 10^{-4} | 4 x 10^{-5} |
| Batch Size | 1.5M -> 3M | 3M -> 6M |

Key differences from Gopher (Section 4.1):
- **Optimizer:** AdamW (Loshchilov and Hutter, 2019) instead of Adam (Kingma and Ba, 2014); shown to improve language modelling loss (Figure A6). AdamW only surpasses Adam around 80% of the way through the cosine cycle but achieves notably better final performance (Footnote 8, Figure A7).
- **Tokenizer:** Slightly modified SentencePiece without NFKC normalization; 94.15% token overlap with Gopher's vocabulary. Improves representation of mathematics and chemistry.
- **Precision:** Forward and backward pass in bfloat16 with float32 copy of weights in the distributed optimiser state.

**Evaluation:** Large subset of tasks from Rae et al. (2021) covering 6 categories: language modelling (20 tasks), reading comprehension (3), question answering (3), common sense (5), MMLU (57), and BIG-bench (62) -- totalling approximately 150 evaluation tasks (Table 5, Section 4.2).

**Reproducibility:** Code not released. Hyperparameters detailed in Table 4 and Appendix D. Training conducted on proprietary TPU infrastructure. No seeds reported.

### Key Results

#### Scaling Exponent Comparison (Table 2)

| Approach | N_opt proportional to C^a | D_opt proportional to C^b |
|----------|---------------------------|---------------------------|
| Approach 1 (training curve envelope) | 0.50 (0.488, 0.502) | 0.50 (0.501, 0.512) |
| Approach 2 (IsoFLOP profiles) | 0.49 (0.462, 0.534) | 0.51 (0.483, 0.529) |
| Approach 3 (parametric loss) | 0.46 (0.454, 0.455) | 0.54 (0.542, 0.543) |
| Kaplan et al. (2020) | 0.73 | 0.27 |

All three approaches consistently predict near-equal scaling of model size and data with compute, in clear contrast to Kaplan et al.'s recommendation (tested across over 400 models with bootstrapped confidence intervals -- strong evidence).

#### Projected Optimal Configurations (Table 3, Approach 1)

| Parameters | Optimal FLOPs | FLOPs (in Gopher unit) | Optimal Tokens |
|------------|---------------|------------------------|----------------|
| 400M | 1.92 x 10^19 | 1/29,968 | 8.0B |
| 1B | 1.21 x 10^20 | 1/4,761 | 20.2B |
| 10B | 1.23 x 10^22 | 1/46 | 205.1B |
| 67B | 5.76 x 10^23 | 1 | 1.5T |
| 175B | 3.85 x 10^24 | 6.7 | 3.7T |
| 280B | 9.90 x 10^24 | 17.2 | 5.9T |
| 520B | 3.43 x 10^25 | 59.5 | 11.0T |
| 1T | 1.27 x 10^26 | 221.3 | 21.2T |
| 10T | 1.30 x 10^28 | 22,515.9 | 216.2T |

#### MMLU 5-shot Results (Table 6)

| Model / Baseline | Accuracy |
|------------------|----------|
| Random | 25.0% |
| Average human rater | 34.5% |
| GPT-3 5-shot | 43.9% |
| Gopher 5-shot | 60.0% |
| **Chinchilla 5-shot** | **67.6%** |
| Average human expert | 89.8% |
| June 2022 Forecast | 57.1% |
| June 2023 Forecast | 63.4% |

Chinchilla exceeds the expert forecast for June 2023 (63.4%) by over 4 percentage points. Chinchilla achieves >90% accuracy on 4 tasks: high_school_gov_and_politics, international_law, sociology, and us_foreign_policy. Chinchilla improves on **51/57** individual tasks, ties on 2, and underperforms on 4 vs. Gopher (Figure 6, Section 4.2.2). Evaluated across 57 tasks spanning diverse academic subjects (strong evidence).

#### Reading Comprehension (Table 7)

| | Chinchilla | Gopher | GPT-3 | MT-NLG 530B |
|---|---|---|---|---|
| LAMBADA Zero-Shot | **77.4** | 74.5 | 76.2 | 76.6 |
| RACE-m Few-Shot | **86.8** | 75.1 | 58.1 | - |
| RACE-h Few-Shot | **82.3** | 71.6 | 46.8 | 47.9 |

Chinchilla improves over Gopher by more than 10 percentage points on both RACE-h and RACE-m (Section 4.2.3). Note that GPT-3 and MT-NLG 530B use a different prompt format on RACE-h/m, so results are not directly comparable to Gopher and Chinchilla.

#### Common Sense Zero-Shot (Table 8)

| | Chinchilla | Gopher | GPT-3 | MT-NLG 530B | Supervised SOTA |
|---|---|---|---|---|---|
| HellaSwag | **80.8%** | 79.2% | 78.9% | 80.2% | 93.9% |
| PIQA | 81.8% | 81.8% | 81.0% | **82.0%** | 90.1% |
| Winogrande | **74.9%** | 70.1% | 70.2% | 73.0% | 91.3% |
| SIQA | **51.3%** | 50.6% | - | - | 83.2% |
| BoolQ | **83.7%** | 79.3% | 60.5% | 78.2% | 91.4% |

Chinchilla outperforms both Gopher and GPT-3 on all tasks and outperforms MT-NLG 530B on all but PIQA (Section 4.2.5). Evidence breadth: 5 benchmarks, 4 model comparisons, zero-shot setting only (moderate evidence).

**TruthfulQA** (Section 4.2.5): Chinchilla achieves 43.6% (0-shot), 58.5% (5-shot), and 66.7% (10-shot), compared to Gopher's 29.5% (0-shot) and 43.7% (10-shot). The 14.1 percentage point improvement in 0-shot accuracy contradicts Lin et al.'s (2021) finding that larger models tend to be less truthful, suggesting that better modelling of pre-training data can improve truthfulness.

#### Closed-Book Question Answering (Table 9)

| | Method | Chinchilla | Gopher | GPT-3 | SOTA (open book) |
|---|---|---|---|---|---|
| Natural Questions (dev) | 0-shot | 16.6% | 10.1% | 14.6% | |
| | 5-shot | 31.5% | 24.5% | - | 54.4% |
| | 64-shot | 35.5% | 28.2% | 29.9% | |
| TriviaQA (unfiltered, test) | 0-shot | 67.0% | 52.8% | 64.3% | |
| | 5-shot | 73.2% | 63.6% | - | - |
| | 64-shot | 72.3% | 61.3% | 71.2% | |
| TriviaQA (filtered, dev) | 0-shot | 55.4% | 43.5% | - | |
| | 5-shot | 64.1% | 57.0% | - | 72.5% |
| | 64-shot | 64.6% | 57.2% | - | |

Chinchilla achieves new closed-book SOTA on Natural Questions (31.5% 5-shot, 35.5% 64-shot). On TriviaQA (filtered), Chinchilla lags behind the open-book SOTA (Izacard and Grave, 2020) by only 7.9% (Section 4.2.6).

#### Language Modelling (Figure 5, Section 4.2.1)

Chinchilla outperforms Gopher on **all 20 subsets of The Pile** (Gao et al., 2020), with bpb improvements ranging from approximately 0.02 to 0.10. On WikiText-103, Chinchilla achieves perplexity 7.16 vs. 7.75 for Gopher. The authors note caution about potential train/test leakage since Chinchilla is trained on 4x more data (Section 4.2.1).

#### BIG-bench (Figure 7, Section 4.2.4)

Chinchilla improves average BIG-bench performance by 10.7 percentage points (65.1% vs. 54.4% for Gopher). Chinchilla outperforms Gopher on **58/62** tasks and underperforms on only 4 tasks (crash_blossom, dark_humor_detection, mathematical_induction, logical_args). Evaluated across 62 diverse tasks (strong evidence).

### Gender Bias and Toxicity (Section 4.2.7)

#### Winogender Gender Bias (Table 10)

| | Chinchilla | Gopher |
|---|---|---|
| All | 78.3% | 71.4% |
| Male | 71.2% | 68.0% |
| Female | 79.6% | 71.3% |
| Neutral | 84.2% | 75.0% |

| | Chinchilla | Gopher |
|---|---|---|
| Male gotcha | 62.5% | 59.2% |
| Male not gotcha | 80.0% | 76.7% |
| Female gotcha | 76.7% | 66.7% |
| Female not gotcha | 82.5% | 75.8% |

Chinchilla resolves pronouns more accurately than Gopher across all groups. The improvement is **uneven**: male pronouns improve by 3.2 pp while female pronouns improve by 8.3 pp and neutral pronouns by 9.2 pp. The largest improvement is on female gotcha examples (+10 pp), suggesting compute-optimal training can reduce gender bias but does so unevenly across pronoun groups (Section 4.2.7).

#### Toxicity (Section 4.2.7)

Analysis of 25,000 unprompted samples using PerspectiveAPI: mean toxicity 0.087 (Chinchilla) vs. 0.081 (Gopher); median 0.066 vs. 0.064; 95th percentile 0.238 vs. 0.230. The difference is negligible, consistent with Rae et al.'s (2021) finding that toxicity levels in unconditional generation are largely independent of model quality. Evaluated on a single toxicity classifier (limited evidence for generalization to other toxicity measures).

---

## Limitations and Failure Modes

### Author-Acknowledged Limitations

1. **Limited large-scale validation:** Only two comparable training runs at large scale (Chinchilla and Gopher); no intermediate-scale validation points (Section 5). Single comparison at the target compute budget (limited evidence for the specific 70B configuration).

2. **Power-law assumption:** The analysis assumes power-law relationships between compute, model size, and tokens. Appendix E shows negative curvature in the FLOP-loss frontier at high compute, suggesting optimal models may be even smaller than predicted (Section 3.4, Section 5).

3. **Single-epoch training:** All training runs used less than one epoch of data; the multi-epoch regime may have different scaling properties (Section 5).

4. **Dataset dependence:** Results derived primarily on MassiveText. Appendix C reproduces IsoFLOP analysis on C4 (Raffel et al., 2020a) and GitHub code (Rae et al., 2021), finding similar conclusions, but these are only two additional datasets (moderate evidence for generalization).

### Failure Cases

On MMLU, Chinchilla underperforms Gopher on **4/57** tasks (Figure 6, Section 4.2.2):
- college_mathematics
- econometrics
- moral_scenarios
- formal_logic

On BIG-bench, Chinchilla underperforms on **4/62** tasks (Figure 7, Section 4.2.4):
- crash_blossom
- dark_humor_detection
- mathematical_induction
- logical_args

On common sense, Chinchilla ties Gopher on PIQA (81.8%) and is outperformed by MT-NLG 530B on PIQA (82.0%) (Table 8).

### Scope and Comparability

**What was not tested:**
- Mixture-of-expert models (Clark et al., 2022 suggests diminishing returns at scale for MoE but used a fixed token budget, potentially underestimating MoE benefits)
- Retrieval-augmented models
- Multi-epoch training regimes
- Non-English data (all evaluation is English-only)
- Instruction-tuned or RLHF models
- Models below 70M or above 16B parameters in the scaling analysis (extrapolation beyond this range carries uncertainty)

**Comparability notes:**
- **Different tokenizers:** Chinchilla and Gopher use different tokenizers (94.15% overlap); Chinchilla removes NFKC normalization. This affects token-level metrics and complicates direct perplexity comparison.
- **Different optimizers:** Chinchilla uses AdamW while Gopher uses Adam; Figure A6 shows AdamW improves performance, so some of Chinchilla's advantage may come from the optimizer rather than scaling alone.
- **Different training data distribution:** Slight differences in MassiveText subset weighting (Table A1).
- **Different prompt formats:** GPT-3 and MT-NLG 530B use different prompt formats on RACE-h/m, making those comparisons non-parallel (Table 7).
- **Train/test leakage risk:** Chinchilla is trained on 4x more data, increasing potential overlap with evaluation sets; the authors note this concern for language modelling benchmarks (Section 4.2.1).

---

## Conclusions

### Contributions

1. **Revised scaling laws for compute-optimal training.** Established that model size and training tokens should scale equally (a ≈ b ≈ 0.5) with compute, contradicting the prior consensus from Kaplan et al. (2020) that favored larger models (a = 0.73, b = 0.27). Three independent approaches with bootstrapped confidence intervals provide robust evidence (Table 2).

2. **Methodological correction to Kaplan et al.** Demonstrated that matching cosine learning rate schedule length to training duration is critical; Kaplan et al.'s fixed schedule biased their results toward larger models by overestimating loss for shorter training runs (Section 2, Section 3).

3. **Chinchilla validation.** Trained a 70B parameter model on 1.4T tokens that outperforms the 280B Gopher on nearly all benchmarks (51/57 MMLU tasks, 58/62 BIG-bench tasks, all 20 Pile subsets) while using the same compute budget of 5.76 x 10^23 FLOPs (Section 4.2).

4. **Practical inference efficiency.** A 4x smaller model with better performance substantially reduces memory footprint and inference cost, enabling broader deployment (Section 1, Section 5).

5. **Parametric loss framework.** Proposed L(N,D) = E + A/N^alpha + B/D^beta with closed-form optimal allocation, providing a theoretical framework for predicting compute-optimal configurations (Section 3.3, Equation 2, Equation 4).

6. **Quantitative projections for future models.** Provided a full table of predicted compute-optimal configurations from 400M to 10T parameters (Table 3), establishing that training data at the scale of trillions of tokens would be needed.

### Implications

1. **Training data is the bottleneck.** A 175B model should be trained on 3.7T tokens, far exceeding datasets available as of 2022, underscoring the need for large-scale data collection (Table 3, Section 3.4).

2. **Existing models are undertrained.** GPT-3, Gopher, Jurassic-1, and MT-NLG 530B were all trained on ~300B tokens but would benefit from 5-20x more training data for compute-optimal performance (Table 1, Table 3).

3. **Dataset quality becomes critical.** Speculatively, scaling to larger datasets is expected to be beneficial only when data quality is maintained, highlighting the need for responsible dataset curation (Section 5).

4. **Ethical implications of data scale.** Training on trillions of tokens increases the quantity of toxic language, biases, and private information, making dataset introspection more important (Section 5).

---

## Key Claims

1. **C1: Equal scaling of parameters and data.** For compute-optimal training, N_opt proportional to C^a and D_opt proportional to C^b where a ≈ b ≈ 0.5. Evidence: Three independent approaches (Table 2) with bootstrapped 10th-90th percentile confidence intervals, based on over 400 training runs. Scope: Dense autoregressive transformers trained for less than one epoch on MassiveText, parameter range 70M-16B. Magnitude: a ≈ 0.50, b ≈ 0.50 vs. Kaplan et al.'s a = 0.73, b = 0.27 (three independent methods with bootstrapped CIs -- strong evidence).

2. **C2: Current LLMs are undertrained.** Models like GPT-3 (175B), Gopher (280B), Jurassic-1 (178B), and MT-NLG (530B) are significantly larger than optimal for their compute budgets. Evidence: Figure 1, Table 1, Table 3 projections. Scope: Models trained as of March 2022 on ~300B tokens. Magnitude: GPT-3 should be ~67B with 1.5T tokens; Gopher should be ~67B with 1.5T tokens; 280B model requires ~10^25 FLOPs and 5.9T tokens (Table 3). Evidence is based on projections from fitted power laws (moderate evidence; projections validated only at the 70B/1.4T point).

3. **C3: Chinchilla outperforms larger models at same compute.** With the same compute budget (5.76 x 10^23 FLOPs), Chinchilla (70B, 1.4T tokens) outperforms Gopher (280B, 300B tokens). Evidence: +7.6 pp on MMLU 5-shot (Table 6), +10.7 pp on BIG-bench average (Section 4.2.4), all 20 Pile subsets improved (Figure 5), +10 pp on RACE-h/m (Table 7), new closed-book SOTA on Natural Questions (Table 9). Scope: Same dataset, same compute budget. Evaluated across approximately 150 tasks spanning 6 categories (strong evidence).

4. **C4: Parametric loss decomposition is accurate.** The loss function L(N,D) = E + A/N^alpha + B/D^beta with classical risk decomposition captures training loss across model sizes and token counts. Evidence: Figure 4 iso-loss contours, Section 3.3. Yields a = 0.46, b = 0.54 for the efficient frontier, consistent with the other approaches. Scope: MassiveText dataset, dense transformers, fitted with Huber loss (delta = 10^-3). The Huber loss downweights low-FLOP outliers, contributing to predicting smaller optimal models at high compute (Section 3.4). Moderate evidence: fit quality not quantified with held-out R^2 or similar metric.

5. **C5: Improved gender bias resolution with uneven gains.** Chinchilla resolves Winogender pronouns more accurately than Gopher across all groups. Evidence: Table 10 -- overall 78.3% vs. 71.4% (+6.9 pp). Female gotcha examples improve by 10 pp (76.7% vs. 66.7%), male pronouns improve by only 3.2 pp (71.2% vs. 68.0%). Scope: Winogender zero-shot, single evaluation dataset (limited evidence for generalization to broader gender bias).

6. **C6: Compute-optimal training does not increase unconditional toxicity.** PerspectiveAPI analysis of 25,000 unprompted samples shows negligible toxicity difference between Chinchilla and Gopher. Evidence: Mean toxicity 0.087 vs. 0.081, 95th percentile 0.238 vs. 0.230 (Section 4.2.7). Scope: Unprompted generation only, single toxicity classifier. Consistent with Rae et al.'s (2021) finding that toxicity is largely independent of model quality (limited evidence: single classifier, no prompted evaluation).

---

## Open Questions

1. **Multi-epoch training:** How do scaling laws change when training for multiple epochs? All experiments used less than one epoch (Section 5). This is particularly relevant as datasets at the scale of trillions of tokens may not be available.

2. **Mixture-of-experts scaling:** Do the same scaling relationships hold for sparse MoE models? Clark et al. (2022) examined MoE scaling but used a fixed token budget, potentially underestimating benefits (Section 2).

3. **Curvature at high compute:** Appendix E shows negative curvature in the frontier at high compute budgets, suggesting even smaller models may be optimal than the power-law fit predicts. What is the asymptotic behavior beyond 10^26 FLOPs?

4. **Data quality vs. quantity:** At what point does adding more data provide diminishing returns, and how does data quality interact with the scaling relationship? The authors note speculatively that scaling data is beneficial only when data quality is maintained (Section 5).

5. **Transfer to downstream tasks:** Do compute-optimal pretraining configurations remain optimal after fine-tuning or instruction-tuning? All evaluation is on zero/few-shot performance of base models.

---

## Core References and Why They Are Referenced

### Scaling Law Foundations

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* The primary work this paper contradicts. Established N_opt proportional to C^0.73, D_opt proportional to C^0.27 using fixed learning rate schedules, leading to the "scale model size" paradigm that this paper overturns.

- **Clark et al. (2022)** -- *Unified Scaling Laws for Routed Language Models.* Examined scaling properties of MoE models, finding diminishing returns with number of experts as model size increases. Also used a fixed token budget like Kaplan et al.

- **Hernandez et al. (2021)** -- *Scaling Laws for Transfer.* Studied transfer scaling properties, contributing to the understanding of how scaling behaviour generalizes.

### Models Compared

- **Brown et al. (2020)** -- *Language Models are Few-Shot Learners.* GPT-3 (175B, 300B tokens) serves as a key comparison point and exemplifies the ~300B token training convention.

- **Rae et al. (2021)** -- *Scaling Language Models: Methods, Analysis & Insights from Training Gopher.* Gopher (280B, 300B tokens) is the direct comparison model; Chinchilla uses the same dataset, compute budget, and evaluation framework.

- **Smith et al. (2022)** -- *Using Deepspeed and Megatron to Train Megatron-Turing NLG 530B.* MT-NLG (530B, 270B tokens), the largest dense model at the time, compared on reading comprehension and common sense tasks.

- **Lieber et al. (2021)** -- *Jurassic-1: Technical Details and Evaluation.* Jurassic-1 (178B, 300B tokens), compared on Pile language modelling evaluation.

- **Thoppilan et al. (2022)** -- *LaMDA: Language Models for Dialog Applications.* LaMDA (137B, 168B tokens) included in Table 1 as a model trained on fewer tokens than the ~300B convention.

### Architecture and Training

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational transformer architecture used for all models.

- **Loshchilov and Hutter (2019)** -- *Decoupled Weight Decay Regularization.* AdamW optimizer used for Chinchilla, shown to outperform Adam (Figure A6, Figure A7).

### Evaluation Benchmarks

- **Hendrycks et al. (2020)** -- *Measuring Massive Multitask Language Understanding.* MMLU benchmark where Chinchilla achieves 67.6% vs. Gopher's 60.0%.

- **BIG-bench collaboration (2021)** -- *Beyond the Imitation Game.* 62 BIG-bench tasks where Chinchilla improves average accuracy from 54.4% to 65.1%.

- **Gao et al. (2020)** -- *The Pile: An 800GB Dataset of Diverse Text for Language Modeling.* The Pile evaluation sets where Chinchilla outperforms Gopher on all 20 subsets.

- **Lin et al. (2021)** -- *TruthfulQA: Measuring How Models Mimic Human Falsehoods.* TruthfulQA benchmark where Chinchilla's 14.1 pp improvement contradicts the finding that larger models are less truthful.

- **Kwiatkowski et al. (2019)** -- *Natural Questions.* Closed-book QA benchmark where Chinchilla achieves new SOTA.

### Retrieval-Augmented Approaches

- **Borgeaud et al. (2021)** -- *Improving Language Models by Retrieving from Trillions of Tokens.* Retrieval augmentation effectively increases training data by ~10x, suggesting model performance may depend more on data size than model size.
