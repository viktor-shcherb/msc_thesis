---
title: "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"
authors: "Snell, Lee, Xu, Kumar"
year: 2025
venue: "ICLR 2025"
paper_type: conference-paper
categories: ["scaling-laws", "reasoning-evaluation"]
scope: ["test-time compute scaling", "math reasoning", "compute-optimal inference"]
benchmarks_used: ["math-hendrycks"]
models_introduced: []
models_evaluated: ["palm-2-s"]
key_claims:
  - id: C1
    claim: "Compute-optimal test-time scaling achieves more than 4× efficiency over best-of-N baseline for both search and revisions"
    evidence: "Figure 1, Figure 4, Figure 8, Sections 5.3 and 6.2"
    status: supported
    scope: "MATH benchmark, PaLM 2-S* model, generation budgets up to 256/512"
    magnitude: ">4× efficiency (e.g. 16 vs 64 generations for search, 64 vs 256 for revisions)"
  - id: C2
    claim: "The efficacy of test-time compute strategies depends critically on prompt difficulty"
    evidence: "Figure 3 right, Figure 7 right, Sections 5.3 and 6.2"
    status: supported
    scope: "MATH benchmark, 5-level difficulty binning based on pass@1 from 2048 samples"
    magnitude: "qualitative — optimal strategy shifts from revisions (easy) to beam search (hard) across 5 difficulty bins"
  - id: C3
    claim: "Beam search outperforms best-of-N on harder problems but degrades performance on easier problems due to PRM over-optimization"
    evidence: "Figure 3 right, Section 5.3"
    status: supported
    scope: "PaLM 2-S* with PRM, beam width M=4, MATH benchmark"
    magnitude: "beam search degrades on bins 1-2 at high budgets; consistently outperforms best-of-N on bins 3-4; no method improves bin 5"
  - id: C4
    claim: "Sequential revisions outperform parallel sampling when combined with verifier-based or majority selection"
    evidence: "Figure 6 right, Section 6.1"
    status: supported
    scope: "PaLM 2-S* revision model, MATH benchmark"
    magnitude: "narrow margin — sequential narrowly outperforms parallel across all generation budgets with both selection methods"
  - id: C5
    claim: "Easy questions benefit from purely sequential test-time compute, while harder questions perform best with an ideal ratio of sequential to parallel"
    evidence: "Figure 7 right, Section 6.2"
    status: supported
    scope: "MATH benchmark, generation budget of 128"
    magnitude: "bins 1-2 peak at fully sequential; bins 3-5 peak at intermediate sequential/parallel ratio"
  - id: C6
    claim: "A smaller model with compute-optimal test-time scaling can outperform a ~14× larger model on easy and medium problems in a FLOPs-matched evaluation"
    evidence: "Figure 9, Section 7"
    status: supported
    scope: "PaLM 2-S* vs ~14× larger model, MATH difficulty bins 1-3, R << 1 to R ~= 1"
    magnitude: "~14× parameter gap closed by test-time compute on bins 1-3; up to +27.6% relative improvement at R << 1 for revisions"
  - id: C7
    claim: "On the hardest problems, test-time compute provides very little benefit; pretraining compute is more effective"
    evidence: "Figure 9, Section 7"
    status: supported
    scope: "MATH difficulty bin 5, all R values; difficulty bins 4-5 at R >> 1"
    magnitude: "bin 5 accuracy ~20% with no meaningful improvement from test-time compute; -37.2% relative at R >> 1 for hard questions in revisions"
  - id: C8
    claim: "PRM consistently outperforms ORM, with the gap growing as number of samples increases"
    evidence: "Figure 14, Appendix F"
    status: supported
    scope: "PaLM 2-S* base model, best-of-N evaluation up to 2048 samples"
    magnitude: "PRM ~40% vs ORM ~35% at 2048 samples; gap widens from ~0% at N=1 to ~5% at N=2048"
cross_references:
  - target: 2022-12-chinchilla-scaling-laws
    type: extends
    detail: "Extends compute-optimal scaling analysis from pretraining to test-time, comparing FLOPs allocated to pretraining vs inference"
  - target: 2022-12-chain-of-thought-prompting
    type: extends
    detail: "Builds on chain-of-thought as a mechanism for using test-time compute for reasoning tasks"
open_questions:
  - question: "Can PRM tree-search be combined with revision models for further test-time scaling improvements?"
    addressed_by: null
  - question: "How can question difficulty be estimated more efficiently than generating 2048 samples per question?"
    addressed_by: null
  - question: "Can outputs from test-time compute be distilled back into the base model for iterative self-improvement?"
    addressed_by: null
  - question: "Do the findings transfer beyond math reasoning to other domains requiring complex inference?"
    addressed_by: null
---

# Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

**Authors:** Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar (UC Berkeley, Google DeepMind)
**Date:** August 2024, arXiv:2408.03314; ICLR 2025

---

## Core Research Problem

Prior work on scaling LLM test-time computation provides **mixed results**: some studies show test-time compute can improve outputs via techniques like best-of-N sampling and self-critique, while others demonstrate that effectiveness on complex reasoning tasks remains highly limited. Critically, existing approaches apply test-time computation uniformly without considering the difficulty of the specific problem at hand. The fundamental question is: **given a fixed test-time compute budget, how should it be optimally allocated to maximize performance, and to what extent can test-time compute substitute for additional pretraining?**

The root cause of mixed prior results is that different test-time strategies (search, revisions, parallel sampling) have fundamentally different properties that are more or less effective depending on the problem. Easy problems benefit from local refinement (revisions), while hard problems require broader exploration (parallel sampling, tree search). No prior work had systematically analyzed these tradeoffs or proposed adaptive allocation strategies.

---

## Problem Solutions

The paper proposes a **compute-optimal test-time scaling strategy** that adaptively allocates test-time compute based on prompt difficulty:

1. **Unification of test-time methods** under a proposer-verifier framework: modifying the proposal distribution (via sequential revisions) and optimizing the verifier (via search against a process reward model).
2. **Difficulty-dependent allocation**: using a model-derived estimate of question difficulty to select the optimal test-time strategy and hyperparameters per prompt.
3. **Two complementary mechanisms**: (a) search against dense process-based verifiers (PRMs) with beam search, and (b) iterative revision models that refine the proposal distribution sequentially.

---

## Approach Details

### Method

The paper frames test-time computation through the lens of **modifying the model's predicted distribution** at test time. Two independent axes are studied:

**(1) Optimizing the verifier** — search against a process reward model (PRM):

- A PRM is trained to predict per-step correctness using Monte Carlo rollout estimates (not human labels), following Wang et al. (2023) -- *Math-Shepherd*.
- Three search methods are compared:
  - **Best-of-N weighted**: sample N full solutions, select via PRM scores aggregated with best-of-N weighted selection (marginalizing scores across solutions with the same final answer).
  - **Beam search**: at each solution step, sample N candidates, retain top N/M by PRM score, expand M new candidates from each retained beam. Repeat up to 40 rounds.
  - **Lookahead search**: extends beam search by rolling out k additional steps at temperature 0 before scoring, using the PRM value at the end of the rollout. A special case of MCTS with stochastic elements removed.

**(2) Modifying the proposal distribution** — revision models:

- A PaLM 2-S* model is finetuned to iteratively revise its own answers by conditioning on previous incorrect attempts.
- Training data: 64 parallel samples per question, post-hoc assembled into multi-turn trajectories (up to 4 incorrect answers followed by a correct one), using character edit distance to select correlated incorrect-correct pairs.
- At inference: the model generates sequences of revisions, with the best answer selected via a trained ORM or majority voting.

**Compute-optimal strategy** — formally defined as:

> θ*_{q,y*(q)}(N) = argmax_θ (E_{y ~ Target(θ,N,q)} [1_{y = y*(q)}])

where Target(θ, N, q) is the distribution induced by test-time compute hyperparameters θ with budget N for prompt q. In practice, approximated by binning questions into five difficulty levels (based on pass@1 rate from 2048 samples) and selecting the best strategy per bin via cross-validation.

### Key Technical Components

**Difficulty estimation.** Question difficulty is defined as a function of the base LLM's pass@1 rate, binned into five quantiles from 2048 samples. Two variants:
- **Oracle difficulty**: uses ground-truth correctness checks.
- **Model-predicted difficulty**: uses averaged PRM final-answer scores instead of ground truth, removing the need for labels but incurring additional compute.

**PRM training details:**
- Binary classifier predicting per-step values between 0 and 1.
- Trained with soft values from Monte Carlo rollouts, using binary cross-entropy loss.
- AdamW optimizer, lr 3e-5, batch size 128, dropout 0.05, betas (0.9, 0.95).
- 16 samples per question, 16 Monte Carlo rollouts per step for value estimation.

**Step-wise aggregation.** The paper finds that using the PRM's **last step prediction** as the full-answer score outperforms taking the minimum or product across steps (Figure 13). This effectively makes the PRM function like an ORM at inference, suggesting PRM training may serve primarily as a form of **representation learning**.

**Revision model training:**
- Finetuned with AdamW, lr 1e-5, batch size 128, no dropout, betas (0.9, 0.95).
- Checkpoint selected slightly after overfitting begins on validation (off-policy data makes validation loss unreliable).
- ~38% of correct answers get reverted to incorrect in subsequent revisions, necessitating selection mechanisms.

**Revision model verifier.** A separate ORM is trained on the revision model's outputs (not the base model PRM) to handle distribution shift. The ORM includes previous revisions in context. Hierarchical selection: best-of-N weighted within each chain, then across chains.

### Experimental Setup

- **Model:** PaLM 2-S* (Codey) base model. Authors state this model is "representative of the capabilities of many contemporary LLMs."
- **Dataset:** MATH benchmark, 12K train / 500 test split from Lightman et al. (2023).
- **Search budget sweep:** Up to 256 generations for search experiments, up to 512 for revision experiments.
- **Beam search configurations:** beam width M = √N and M = 4; lookahead k = 1 and k = 3.
- **FLOPs comparison:** PaLM 2-S* vs a ~14× larger pretrained model (greedy decoding), with three R values (D_inference/D_pretrain): 0.16 (R << 1), 0.79 (R ≈ 1), 22 (R >> 1).
- **Difficulty estimation:** Two-fold cross-validation on difficulty bins to avoid confounding.
- **Prompting:** 4-shot prompt from PRM800k data for step-by-step format.
- **Reproducibility:** Code and data are not publicly released. The approach relies on PaLM 2-S*, a proprietary model. Difficulty estimation requires 2048 samples per question, which is a substantial computational cost not accounted for in the main comparisons.

### Key Results

#### Search against PRM verifiers (Section 5)

| Setting | Best-of-N Weighted (256) | PRM Compute Optimal Oracle (64) | PRM Compute Optimal Predicted (64) |
|---|---|---|---|
| MATH overall | ~36% | ~36% | ~34% |

- Beam search significantly outperforms best-of-N at **low generation budgets** but diminishing returns and PRM over-optimization cause it to underperform at high budgets (Figure 3 left).
- Lookahead search generally underperforms due to additional compute cost of rollouts.
- **By difficulty:** beam search degrades on easy problems (bins 1-2) at high budgets due to PRM exploitation, but consistently outperforms best-of-N on harder problems (bins 3-4). On the hardest problems (bin 5), no method makes meaningful progress (Figure 3 right).
- **Compute-optimal search** nearly matches best-of-N performance using up to **4× less compute** (e.g., 16 vs 64 generations) (Figure 4).

#### Proposal distribution refinement via revisions (Section 6)

| Setting | Parallel Best-of-N Weighted (256) | Compute Optimal Oracle (64) | Compute Optimal Predicted (64) |
|---|---|---|---|
| MATH overall | ~38% | ~40% | ~38% |

- Sequential revisions narrowly outperform parallel sampling with both verifier and majority selection (Figure 6 right).
- An **ideal sequential-to-parallel ratio** exists and depends on difficulty: easy questions benefit from purely sequential compute; hard questions need a balanced ratio (Figure 7 right).
- Compute-optimal revisions outperform parallel best-of-N with up to **4× less compute** (e.g., 64 vs 256 generations) (Figure 8).
- Unlike parallel sampling which plateaus, compute-optimal scaling demonstrates **continued improvements** at higher budgets.

#### Pretraining vs test-time compute tradeoff (Section 7)

| Difficulty | R << 1 (low inference) | R ≈ 1 | R >> 1 (high inference) |
|---|---|---|---|
| Easy (bins 1-2) | Test-time preferred | Test-time preferred | Test-time preferred |
| Medium (bin 3) | Test-time preferred | Test-time preferred | Mixed |
| Hard (bin 4) | Test-time preferred | Mixed | Pretraining preferred |
| Hardest (bin 5) | Pretraining preferred | Pretraining preferred | Pretraining preferred |

- On easy/medium problems (where the base model has non-trivial success rates), test-time compute with PaLM 2-S* can outperform a **~14× larger model** in FLOPs-matched evaluation (Figure 9).
- On the hardest problems (bin 5), test-time compute provides minimal benefit regardless of R.
- The tradeoff depends heavily on R = D_inference/D_pretrain: lower inference requirements favor test-time compute.

### Additional Findings

- **PRM vs ORM:** PRM consistently outperforms ORM for best-of-N selection, with the gap growing with sample count (Figure 14). This holds even though the best PRM aggregation strategy (last step) effectively uses the PRM like an ORM, suggesting per-step training provides better learned representations.
- **ReST^EM on revision models:** Applying RL-inspired optimization to the revision model via ReST^EM substantially hurt performance, likely due to exacerbated spurious correlations in revision data (Figure 16, Appendix K).
- **Predicted vs oracle difficulty bins:** Model-predicted difficulty bins (using PRM scores) perform comparably to oracle bins derived from ground-truth correctness, demonstrating practical feasibility (Figures 4, 8, 11, 12).

---

## Limitations and Failure Modes

1. **Single model, single benchmark.** All experiments use PaLM 2-S* on MATH. Transfer to other models, scales, and domains is claimed but not demonstrated.
2. **Difficulty estimation cost.** Estimating question difficulty requires 2048 samples per question, a substantial cost not included in the main compute accounting. The authors acknowledge this but do not address it experimentally.
3. **No benefit on hardest problems.** On difficulty bin 5 (hardest questions), no test-time compute strategy provides meaningful improvement. The authors state this represents a fundamental limitation of current approaches.
4. **PRM over-optimization.** At high generation budgets, search methods exploit the PRM, producing low-information repetitive steps or overly short solutions (Appendix M examples).
5. **Revision model distribution shift.** ~38% of correct answers are reverted to incorrect ones during revision, requiring selection mechanisms. The base model PRM is ineffective for scoring revision model outputs due to distribution shift.
6. **[Inferred] Proprietary model.** PaLM 2-S* is not publicly available, limiting reproducibility.
7. **No combination of PRM search with revisions.** The two primary mechanisms (verifier search and proposal refinement) are not combined, which could yield further improvements.

#### Scope and Comparability

- **What was not tested:** Models at different scales, non-math reasoning tasks, combination of PRM tree search with revisions, alternative difficulty estimation methods, open-source models.
- **Comparability notes:** The ~14× larger model comparison uses fixed training data with scaled parameters (LLaMA-style scaling), not compute-optimal Chinchilla-style scaling where data and parameters are both scaled. This affects the FLOPs-matched comparison interpretation.

---

## Conclusions

### Contributions

1. **Compute-optimal test-time scaling framework.** Introduced the concept of adaptively allocating test-time compute based on prompt difficulty, achieving >4× efficiency over best-of-N baselines for both search and revision mechanisms.
2. **Systematic analysis of test-time compute strategies.** Showed that efficacy of different strategies (beam search, best-of-N, revisions) depends critically on question difficulty, with beam search superior on hard problems and best-of-N/revisions on easy problems.
3. **FLOPs-matched pretraining vs test-time comparison.** First demonstration that test-time compute with simple methods can outperform a ~14× larger model on easy/medium problems, while pretraining remains superior for the hardest problems.
4. **Proposer-verifier unification.** Unified test-time compute approaches under a framework of proposal distribution modification and verifier optimization, identifying them as complementary axes.

### Implications

1. **Foundational for o1-style reasoning.** The adaptive difficulty-dependent allocation of test-time compute directly prefigures the approach taken by subsequent reasoning models (e.g., OpenAI o1), suggesting that the compute-optimal framework has broad practical impact.
2. **Pretraining may not be the only path to performance.** On problems within a model's capability range, test-time compute can substitute for substantial pretraining scale, suggesting a future where "fewer FLOPs are spent during pretraining and more FLOPs are spent at inference."
3. **Hard problems may require fundamentally new approaches.** The failure to improve on the hardest problems suggests that test-time compute, as studied here, cannot substitute for knowledge and capabilities that are absent from the base model.

---

## Key Claims

1. **C1: >4× efficiency over best-of-N.** Compute-optimal scaling outperforms best-of-N using up to 4× less test-time compute for both PRM search (16 vs 64 generations, Figure 4) and revisions (64 vs 256 generations, Figure 8). Evidence is strong: consistent across oracle and predicted difficulty bins, replicated for both major mechanisms studied. Scope: MATH benchmark, PaLM 2-S*, generation budgets up to 256/512.

2. **C2: Difficulty-dependent efficacy.** The effectiveness of any given test-time strategy depends critically on the problem's difficulty from the base model's perspective. Easy problems benefit from revisions/best-of-N; hard problems benefit from beam search. Evidence: Figure 3 right, Figure 7 right. Strong evidence with 5-level difficulty analysis across multiple strategies.

3. **C3: Beam search over-optimization.** Beam search degrades performance on easy problems (difficulty bins 1-2) at high generation budgets due to exploitation of PRM signal, while consistently outperforming best-of-N on harder problems (bins 3-4). Evidence: Figure 3 right. Qualitative evidence in Appendix M showing repetitive/degenerate outputs.

4. **C4: Sequential outperforms parallel.** Sequential revision sampling narrowly outperforms parallel sampling when combined with either verifier or majority selection (Figure 6 right). Limited evidence: single model, single benchmark, narrow margin.

5. **C5: Difficulty-dependent sequential/parallel ratio.** The optimal ratio of sequential to parallel test-time compute varies by difficulty: purely sequential for easy questions, balanced for hard questions (Figure 7 right). Evidence from sweep over ratios at budget 128.

6. **C6: Smaller model can outperform 14× larger model.** In FLOPs-matched evaluation on easy/medium problems (bins 1-3) with R << 1 to R ≈ 1, PaLM 2-S* with compute-optimal test-time scaling outperforms a ~14× larger model using greedy decoding (Figure 9). Scope conditions: does not hold for hardest problems or R >> 1.

7. **C7: Pretraining superior for hardest problems.** On difficulty bin 5, test-time compute provides minimal benefit; pretraining is more effective at all R values (Figure 9). On bin 4, pretraining is preferred when R >> 1.

8. **C8: PRM outperforms ORM.** PRM consistently outperforms ORM in best-of-N selection with growing gap as sample count increases (Figure 14). The best PRM aggregation (last step) is effectively ORM-like, suggesting per-step training provides better representations.

---

## Open Questions

1. **Can PRM tree search be combined with revision models?** The paper studies these mechanisms separately but acknowledges they could be complementary. Not addressed by subsequent work in this directory.

2. **How can question difficulty be estimated efficiently?** The current approach requires 2048 samples per question. The authors suggest finetuning models to predict difficulty directly. Not addressed by subsequent work in this directory.

3. **Can test-time compute outputs be distilled back for self-improvement?** The paper envisions an iterative loop where test-time compute outputs improve the base model. Not addressed by subsequent work in this directory.

4. **Do findings generalize beyond math reasoning?** All experiments use the MATH benchmark. Transfer to other reasoning domains, code generation, or open-ended language tasks is hypothesized but untested. Not addressed by subsequent work in this directory.

---

## Core References and Why They Are Referenced

### Scaling Laws and Compute Tradeoffs

- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models (Chinchilla).* Establishes compute-optimal pretraining scaling; this paper extends the concept to test-time compute scaling and directly compares the two regimes.
- **Sardana & Frankle (2023)** -- *Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws.* Analyzes the tradeoff between training and inference compute; this paper provides empirical evidence for specific mechanisms.
- **Jones (2021)** -- *Scaling Scaling Laws with Board Games.* Prior work on train-time vs test-time compute tradeoffs using MCTS on Hex; this paper extends to full-scale language model reasoning.

### Process Reward Models and Verification

- **Lightman et al. (2023)** -- *Let's Verify Step by Step.* Introduces PRM800k dataset and process-based reward models; provides the foundation for the PRM-based search studied in this paper.
- **Wang et al. (2023)** -- *Math-Shepherd: Verify and Reinforce LLMs Step-by-Step Without Human Annotations.* Provides the Monte Carlo rollout approach for PRM training used in this paper (instead of human labels).
- **Cobbe et al. (2021)** -- *Training Verifiers to Solve Math Word Problems.* Introduces outcome-based verifiers (ORMs) and best-of-N with verifiers as a baseline.

### Revision and Self-Improvement

- **Qu et al. (2024)** -- *Recursive Introspection: Teaching Foundation Models How to Self-Improve.* Direct predecessor for the revision model training approach; this paper modifies the on-policy recipe for computational feasibility.
- **Madaan et al. (2023)** -- *Self-Refine: Iterative Refinement with Self-Feedback.* Self-critique and revision baseline; this paper shows off-the-shelf prompting is insufficient, motivating capability-specific finetuning.

### Chain-of-Thought and Reasoning

- **Wei et al. (2023)** -- *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.* Foundational work on using test-time compute for reasoning via chain-of-thought; this paper builds on this for test-time compute analysis.
- **Huang et al. (2023)** -- *Large Language Models Cannot Self-Correct Reasoning Yet.* Provides negative results on self-correction; this paper addresses this by finetuning for revision capabilities rather than relying on prompting.

### Search Methods

- **Yao et al. (2023)** -- *Tree of Thoughts: Deliberate Problem Solving with Large Language Models.* Tree search for LLM reasoning; this paper compares beam search and best-of-N variants as test-time search strategies.
- **Feng et al. (2024)** -- *AlphaZero-like Tree-Search Can Guide Large Language Model Decoding and Training.* BFS-V search against verifiers; beam search implementation in this paper follows a similar approach.

### Base Model

- **Anil et al. (2023)** -- *PaLM 2 Technical Report.* The base model (PaLM 2-S*) used for all experiments in the paper.
