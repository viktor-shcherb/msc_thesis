---
title: "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer"
authors: "Shazeer, Mirhoseini, Maziarz, Davis, Le, Hinton, Dean"
year: 2017
venue: "ICLR 2017"
paper_type: conference-paper
categories: ["architecture", "scaling-laws"]
scope: ["language modeling", "machine translation", "conditional computation"]
benchmarks_used: ["wmt-translation", "perplexity-1b-word"]
models_introduced: ["moe-sparsely-gated"]
models_evaluated: []
key_claims:
  - id: C1
    claim: "Sparsely-gated MoE achieves greater than 1000x improvements in model capacity with only minor losses in computational efficiency"
    evidence: "Abstract, Section 1.2, Table 1"
    status: supported
    scope: "LSTM-based models on language modeling and translation tasks"
    magnitude: ">1000x capacity increase; MoE-4096-h has 4.3B params at 8.9M ops vs baselines at 8.4M params and 8.4M ops"
  - id: C2
    claim: "MoE-4096-h with 4096 experts achieves 24% lower perplexity than computationally-matched baselines on 1B Word benchmark at ~8M ops/timestep"
    evidence: "Figure 2-left, Section 5.1, Table 7"
    status: supported
    scope: "1B Word benchmark, ~8M ops/timestep budget, 10 epochs"
    magnitude: "24% perplexity reduction (34.1 vs ~45.0)"
  - id: C3
    claim: "MoE-143M achieves 28.0 test perplexity on 1B Word benchmark after 10 epochs, an 18% improvement over the best published result of 34.7 at the same epoch count"
    evidence: "Table 1, Table 7, Section 5.1"
    status: supported
    scope: "1B Word benchmark, 10 epochs, 142.7M ops/timestep"
    magnitude: "18% lower perplexity (28.0 vs 34.7 at 10 epochs)"
  - id: C4
    claim: "MoE achieves 40.56 BLEU on WMT'14 En-Fr, surpassing GNMT (39.22) by 1.34 BLEU and GNMT+RL (39.92) by 0.64 BLEU"
    evidence: "Table 2, Section 5.3"
    status: supported
    scope: "WMT'14 En-Fr newstest2014, single language pair"
    magnitude: "+1.34 BLEU over GNMT, +0.64 BLEU over GNMT+RL"
  - id: C5
    claim: "MoE achieves 26.03 BLEU on WMT'14 En-De, surpassing GNMT (24.91) by 1.12 BLEU"
    evidence: "Table 3, Section 5.3"
    status: supported
    scope: "WMT'14 En-De newstest2014, single language pair"
    magnitude: "+1.12 BLEU over GNMT"
  - id: C6
    claim: "On 100B word corpus, MoE-65536-h achieves 39% lower perplexity than computationally-matched baseline"
    evidence: "Figure 3, Table 8, Section 5.2"
    status: supported
    scope: "100B word Google News corpus, ~8M ops/timestep, 1 epoch"
    magnitude: "39% perplexity reduction (28.9 vs 47.0)"
  - id: C7
    claim: "Single multilingual MoE model beats monolingual GNMT models on 8 of 12 language pairs"
    evidence: "Table 5, Section 5.4"
    status: supported
    scope: "12 language pairs, single multilingual model vs 12 separate monolingual models"
    magnitude: "up to +5.84 BLEU (Korean->English); 19% lower dev perplexity vs multilingual GNMT"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: concurrent
    detail: "Both papers published in 2017; the Transformer paper cites MoE En-De BLEU (26.03) as a baseline in its Table 2"
  - target: 2022-06-switch-transformers-moe
    type: extended-by
    detail: "Switch Transformer simplifies MoE routing to k=1, applies MoE to Transformer FFN layers, and scales to 1.6T parameters"
  - target: 2025-09-apertus-open-compliant-llms
    type: complementary
    detail: "Apertus investigated MoE for their 70B model but did not derisk it in time; mentioned as a future direction"
open_questions:
  - question: "Can MoE be applied to Transformer architectures rather than LSTMs?"
    addressed_by: 2022-06-switch-transformers-moe
  - question: "How does MoE scale to trillion-parameter models?"
    addressed_by: 2022-06-switch-transformers-moe
  - question: "Can recurrent MoE (replacing LSTM weight matrices with MoE) improve results further?"
    addressed_by: null
  - question: "Why do experts specialize semantically, and can this specialization be controlled?"
    addressed_by: null
  - question: "What causes quality degradation at extreme sparsity (131072 experts)?"
    addressed_by: null
---

# Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer

**Authors:** Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, Jeff Dean (Google Brain, Jagiellonian University)
**Date:** January 2017 (arXiv:1701.06538); ICLR 2017

---

## Core Research Problem

Scaling neural network capacity has been central to deep learning success, but for typical models where the entire network is activated for every example, increasing capacity leads to a **roughly quadratic blow-up in training costs** as both model size and training examples increase (Section 1.1). Conditional computation -- where parts of the network are active on a per-example basis -- had been proposed theoretically as a way to increase capacity without proportional compute increase, but prior work had not demonstrated massive improvements in practice.

The authors identify five key challenges that prevented previous conditional computation approaches from succeeding (Section 1.1):

1. **GPU arithmetic vs branching trade-off:** Modern GPUs are much faster at arithmetic than branching, requiring large chunks of the network to be activated together.
2. **Shrinking batch problem:** Conditional computation reduces batch sizes for conditionally active chunks, hurting efficiency.
3. **Network bandwidth bottleneck:** GPU clusters have computational power thousands of times greater than aggregate inter-device network bandwidth, requiring high compute-to-communication ratios.
4. **Loss function complexity:** Multiple auxiliary loss terms may be needed for load balancing and sparsity (Bengio et al. (2015) use three such terms).
5. **Dataset scale:** Prior work used small image datasets (up to 600K images) insufficient for training billion-parameter models.

Prior conditional computation approaches include stochastic neurons (Bengio et al., 2013), block-wise dropout with REINFORCE (Bengio et al., 2015), and deep mixtures of experts (Eigen et al., 2013). None demonstrated massive capacity improvements on large-scale tasks.

The core challenge is: **how to achieve massive increases in model capacity (1000x+) through conditional computation while maintaining computational efficiency on modern GPU clusters.**

---

## Problem Solutions

The paper introduces the **Sparsely-Gated Mixture-of-Experts (MoE) layer**, a general-purpose neural network component consisting of up to thousands of feed-forward expert sub-networks and a trainable gating network that selects a sparse combination of experts for each input (Section 1.2).

The solution rests on four key innovations:

1. **Noisy Top-K gating:** A differentiable gating mechanism that adds tunable Gaussian noise before selecting the top-k experts, enabling sparse expert selection while maintaining gradient flow via backpropagation.

2. **Mixed data and model parallelism:** A distributed training scheme where standard layers use data parallelism while experts are sharded across devices, allowing expert batch sizes to scale with device count.

3. **Auxiliary load-balancing losses:** Two soft constraints (importance loss and load loss) that encourage balanced expert utilization without hard constraints.

4. **Hierarchical MoE:** A two-level expert hierarchy that reduces branching factor for very large expert counts.

---

## Approach Details

### Method

The MoE layer consists of n expert networks E_1, ..., E_n and a gating network G. For input x, the output is (Equation 1, Section 2):

> y = sum_{i=1}^{n} G(x)_i * E_i(x)

Computation is saved through sparsity: wherever G(x)_i = 0, E_i(x) need not be computed. In practice, only k experts (typically k = 4) are active per input despite having thousands of experts.

**Noisy Top-K Gating (Section 2.1, Equations 3-5):**

> G(x) = Softmax(KeepTopK(H(x), k))
>
> H(x)_i = (x * W_g)_i + StandardNormal() * Softplus((x * W_noise)_i)
>
> KeepTopK(v, k)_i = v_i if v_i is in top k elements of v, else -infinity

The noise term (controlled by learnable W_noise) helps with load balancing by introducing stochasticity in expert selection. Setting non-top-k values to -infinity causes corresponding gate values to equal 0 after softmax. The gating network is trained with simple backpropagation, similar to the "occasionally-sensitive behavior" described in Bengio et al. (2013), and differs from Bengio et al. (2015) who use boolean gates and REINFORCE (Section 2.1).

### Key Technical Components

**Addressing the Shrinking Batch Problem (Section 3.1):**

The naive MoE has batch size kb/n per expert for a batch of b examples with k active experts out of n total. The solution combines three techniques:

1. *Mixed parallelism:* Distribute standard layers via data parallelism but keep one shared copy of each expert. Each expert receives examples from all data-parallel batches, achieving a d-fold improvement in expert batch size when distributed over d devices. Memory and bandwidth requirements per device remain constant as more devices are added (Section 3.1).

2. *Convolutional application:* Apply the same MoE to all timesteps together as one batch, multiplying batch size by the sequence length.

3. *Recurrent MoE (proposed but not tested):* Replacing LSTM weight matrices with MoE, using recomputation of forward activations (Gruslys et al., 2016) to maintain large batch sizes (Section 3.1).

**Network Bandwidth (Section 3.2):**

Most communication involves sending expert inputs and outputs across the network. Efficiency requires the ratio of expert computation to input/output size to exceed the ratio of computational to network capacity. Using experts with hidden layers of size 1024-8192 achieves this, since the ratio equals the hidden layer size.

**Load Balancing (Section 4, Appendix A):**

Without intervention, the gating network converges to always selecting the same few experts -- a self-reinforcing imbalance also observed by Eigen et al. (2013). Two auxiliary losses prevent this:

*Importance loss (Equations 6-7):*

> Importance(X) = sum_{x in X} G(x)
>
> L_importance(X) = w_importance * CV(Importance(X))^2

where CV is coefficient of variation. This encourages equal total gate weight across experts.

*Load loss (Equations 10-11, Appendix A):*

The smooth load estimator P(x, i) computes the probability that expert i is selected, given the noise distribution (Equations 8-9):

> P(x, i) = Phi( ((x * W_g)_i - kth_excluding(H(x), k, i)) / Softplus((x * W_noise)_i) )

where Phi is the CDF of the standard normal distribution and kth_excluding(v, k, i) is the k-th highest element of v excluding element i.

> Load(X)_i = sum_{x in X} P(x, i)
>
> L_load(X) = w_load * CV(Load(X))^2

This ensures balanced example counts, not just total weights.

**Load Balancing Ablation (Table 6, Appendix A):**

| w_importance | w_load | Test PPL | CV(Importance) | CV(Load) | max/mean Load |
|---|---|---|---|---|---|
| 0.0 | 0.0 | 39.8 | 3.04 | 3.01 | 17.80 |
| 0.2 | 0.0 | **35.6** | 0.06 | 0.17 | 1.47 |
| 0.0 | 0.2 | 35.7 | 0.22 | 0.04 | 1.15 |
| 0.1 | 0.1 | **35.6** | 0.06 | 0.05 | 1.14 |
| 0.01 | 0.01 | 35.7 | 0.48 | 0.11 | 1.37 |
| 1.0 | 1.0 | 35.7 | 0.03 | 0.02 | **1.07** |

Any nonzero combination of the two losses dramatically improves quality (39.8 -> ~35.6 PPL). Combining both losses achieves the best max/mean load ratio (1.14 at w=0.1 each, 1.07 at w=1.0 each) without degrading perplexity (Table 6, Appendix A).

**Hierarchical MoE (Appendix B):**

For very large expert counts, a two-level hierarchy reduces branching factor. A primary gating network selects among a groups, each containing b experts with a secondary gating network (Equation 12):

> y_H = sum_{i=1}^{a} sum_{j=1}^{b} G_primary(x)_i * G_i(x)_j * E_{i,j}(x)

Hierarchical importance and load metrics are defined (Equations 13-14, Appendix B) to enable backpropagation through both levels of gating.

**Strictly Balanced Gating (Appendix F):**

For the single-language-pair MT experiments, a different gating function was used that ensures every expert receives exactly the same batch size. Instead of top-k per example, the top m examples per expert are selected across the training batch, where m = k|X|/n (Equation 18). A learned per-expert threshold vector T approximates this batchwise mask at inference time (Equations 19-20).

### Experimental Setup

**1 Billion Word Language Modeling Benchmark (Section 5.1, Appendix C):**
- **Dataset:** ~829M words, 793K vocabulary (Chelba et al., 2013)
- **Architecture:** word embedding -> LSTM -> MoE -> LSTM -> softmax; all layers 512-dimensional
- **Experts:** feed-forward networks with one 1024-unit ReLU hidden layer and 512-dim output (~1M parameters each)
- **Model variants:** Flat MoE with 4, 32, 256 experts; hierarchical MoE with 256, 1024, 4096 experts; all with k=4 active experts (~8M ops/timestep). Higher-compute variants (MoE-34M at 33.8M ops, MoE-143M at 142.7M ops) use 1024-dim layers and fewer but larger experts
- **Baselines:** MoE-1-Wide, MoE-1-Deep, 4xLSTM-512, LSTM-2048-512 (all computationally matched at ~8M ops/timestep); 2xLSTM-8192-1024 from Jozefowicz et al. (2016) at 151M ops/timestep
- **Hardware:** 16-32 Tesla K40 GPUs
- **Training:** Adam optimizer, ~300K words per batch, 10 epochs (27K steps), 12-16 hours (18 hours for non-sparse MoE-4)
- **Loss weights:** w_importance = 0.1, w_load = 0.1
- **Dropout:** searched in increments of 0.1; DropProb = 0.1-0.4 depending on model
- **Reproducibility:** Trained using TensorFlow. Softmax trained via importance sampling. No code release mentioned. No variance estimates or multiple seeds reported.

**100 Billion Word Google News Corpus (Section 5.2, Appendix D):**
- **Dataset:** Internal Google dataset of shuffled unique sentences (~100B words; original corpus 130B words)
- **Architecture:** Same as above, with 32 to 131072 experts
- **Hardware:** 32-128 Tesla K40 GPUs
- **Training:** Single pass through ~100B words, batch size ~2.5M words
- **Memory optimizations (Appendix D):** Expert hidden activations not stored (recomputed on backward pass); factored Adam approximation (beta_1 = 0, second moment estimated via row-wise and column-wise averages)
- **Reproducibility:** Internal dataset, not publicly reproducible.

**Machine Translation (Section 5.3, Appendix E):**
- **Architecture:** Modified GNMT -- 3 encoder + 2 decoder LSTM layers (reduced from 9+8), MoE layers between encoder layers 2-3 and decoder layers 1-2. LSTM layers have 2048 hidden units with 512-dim output projection. Residual connections around all LSTM and MoE layers.
- **Experts:** Up to 2048 experts, each with 2048-unit hidden layer (~2M params, ~8B total in MoE layers); k=4 via flat or hierarchical gating
- **Gating:** Single-pair models use strictly balanced gating (Appendix F); multilingual model uses noisy top-k gating with n=512, k=2, 8192-unit expert hidden layers (102M ops/timestep)
- **Datasets:** WMT'14 En-Fr (36M pairs), WMT'14 En-De (5M pairs), Google Production En-Fr
- **Vocabulary:** 32K shared source-target wordpieces (Schuster & Nakajima, 2012)
- **Evaluation:** Tokenized BLEU via multi-bleu.pl from Moses; newstest2014 as test set
- **Hardware:** Up to 64 K40 GPUs
- **Loss weights:** w_importance = 0.01, w_load = 0.01
- **Training:** Adam optimizer, learning rate warmup for 2000 steps then held for 8000 steps then inverse-sqrt decay, DropProb = 0.4, ~16000 words per GPU per batch
- **Attention:** Modified attention function (Appendix G) using separable tanh products for efficiency: A(x_i, y_j) = sum_d V_d * tanh((x_i * U)_d) * tanh((y_j * W)_d)

### Key Results

**1 Billion Word Benchmark (Table 1 / Table 7):**

| Model | Test PPL (10 epochs) | Test PPL (final) | #Params (excl. embed) | ops/timestep | TFLOPS/GPU |
|---|---|---|---|---|---|
| 2xLSTM-8192-1024 (best published) | 34.7 | 30.6 | 151M | 151M | 1.09 |
| MoE-4096-h (Low-Budget) | 34.1 | - | 4303M | 8.9M | 0.74 |
| MoE-34M (Medium-Budget) | 31.3 | - | 4313M | 33.8M | 1.22 |
| MoE-143M (High-Budget) | **28.0** | - | 4371M | 142.7M | **1.56** |

- At matched compute (~8M ops/timestep), MoE-4096-h achieves **34.1 perplexity vs ~45.0** for computationally-matched baselines (LSTM-2048-512), a **24% reduction** (Figure 2-left, Section 5.1). Evidence is on a single benchmark with a single run (no variance reported).
- The Low-Budget MoE (34.1) matches the best published 10-epoch result (34.7) using **only 6% of the computation** (8.9M vs 151M ops/timestep) (Table 1).
- MoE-143M achieves **28.0 perplexity at 10 epochs** vs the best published **34.7 at 10 epochs**, an **18% improvement** at similar compute (142.7M vs 151M ops) (Table 1, Appendix C.2). The best published model reaches 30.6 after 100 epochs, but MoE models were only trained for 10 epochs.

**Detailed low-compute results (Table 7, selected rows):**

| Model | Test PPL (10 epochs) | ops/timestep (M) | #Params excl. embed (M) | TFLOPS/GPU |
|---|---|---|---|---|
| LSTM-2048-512 (re-run) | - (final: 44.7) | 9.4 | 9.4 | 1.21 |
| 4xLSTM-512 | - (final: 46.0) | 8.4 | 8.4 | 1.07 |
| MoE-4 (no sparsity) | 45.0 | 8.4 | 8.4 | 0.52 |
| MoE-32 | 39.7 | 8.4 | 37.8 | 0.87 |
| MoE-256 | 35.7 | 8.6 | 272.9 | 0.81 |
| MoE-1024-h | 34.6 | 8.5 | 1079.0 | 0.90 |
| MoE-4096-h | 34.1 | 8.9 | 4303.4 | 0.74 |

Perplexity consistently decreases as expert count increases from 4 to 4096 at matched compute, demonstrating the capacity scaling benefit of sparse MoE.

**100 Billion Word Corpus (Table 8, Figure 3):**

| Model | Test PPL (0.1 epochs) | Test PPL (1 epoch) | #Params excl. embed (M) | TFLOPS/GPU |
|---|---|---|---|---|
| 4xLSTM-512 baseline | 54.5 | 47.0 | 8.4 | **1.23** |
| MoE-4096-h | 38.9 | 30.9 | 4303.4 | 1.07 |
| MoE-16384-h | **38.2** | 29.7 | 17201.0 | 0.96 |
| MoE-65536-h | **38.2** | **28.9** | 68791.0 | 0.72 |
| MoE-131072-h | 39.8 | 29.2 | 137577.6 | 0.30 |

- **39% lower perplexity** for MoE-65536-h (28.9) vs 4xLSTM-512 baseline (47.0) at similar compute (~8-9M ops/timestep) (Table 8, Section 5.2).
- Benefits continue scaling up to 65536 experts (68.8B parameters), but **quality degrades at 131072 experts** (29.2 vs 28.9), "possibly a result of too much sparsity" (Section 5.2).
- The widening gap between 0.1-epoch and 1-epoch curves (Figure 3) demonstrates that increased capacity helps more on larger training sets.
- Even at 65536 experts (99.994% layer sparsity), computational efficiency stays at 0.72 TFLOPS/GPU.

**Machine Translation -- Single Language Pair (Tables 2-4):**

| Model | WMT'14 En-Fr BLEU | WMT'14 En-De BLEU | ops/timestep | Total #Params | Training Time |
|---|---|---|---|---|---|
| GNMT (Wu et al., 2016) | 39.22 | 24.91 | 214M | 278M | 6 days/96 K80s |
| GNMT+RL (Wu et al., 2016) | 39.92 | 24.66 | 214M | 278M | 6 days/96 K80s |
| MoE (2048 experts) | 40.35 | **26.03** | 85M | 8.7B | 3 days/64 K40s |
| MoE (2048 experts, longer) | **40.56** | - | 85M | 8.7B | 6 days/64 K40s |

- The paper states gains of **1.34 BLEU on En-Fr** (40.56 vs 39.22 GNMT) and **1.12 BLEU on En-De** (26.03 vs 24.91 GNMT) over GNMT baselines (Section 5.3, p. 9). The MoE model does not use RL refinement.
- Compared to GNMT+RL: **+0.64 BLEU** on En-Fr (40.56 vs 39.92), **+1.37 BLEU** on En-De (26.03 vs 24.66).
- Test perplexity also improves: 2.63 vs 2.96 on En-Fr, 4.64 vs 8.08 on En-De (vs GNMT+RL) (Tables 2-3).
- On Google Production En-Fr: MoE achieves 36.57 test BLEU vs 35.56 for GNMT, trained in 1/6th the time (Table 4).
- Training time comparable or shorter despite 8.7B parameters vs 278M; 85M ops/timestep vs 214M.
- Evidence breadth: single run per model, two WMT language pairs plus one internal dataset. No statistical significance testing reported.

**Multilingual Translation (Table 5):**

Single MoE model (8.7B params, 102M ops/timestep) trained on 12 language pairs for ~3B sentence pairs:

| | GNMT-Mono | GNMT-Multi | MoE-Multi | MoE vs GNMT-Multi |
|---|---|---|---|---|
| Parameters | 278M / model | 278M | 8.7B | |
| ops/timestep | 212M | 212M | 102M | |
| Training | various | 21 days, 96 K20s | 12 days, 64 K40s | |
| Dev PPL | | 4.14 | **3.35** | -19% |
| Fr->En | 36.47 | 34.40 | **37.46** | +3.06 |
| De->En | 31.77 | 31.17 | **34.80** | +3.63 |
| Ja->En | 23.41 | 21.62 | **25.91** | +4.29 |
| Ko->En | 25.42 | 22.87 | **28.71** | +5.84 |
| Pt->En | 44.40 | 42.53 | **46.13** | +3.60 |
| Es->En | 38.00 | 36.04 | **39.39** | +3.35 |
| En->Fr | 35.37 | 34.00 | **36.59** | +2.59 |
| En->De | **26.43** | 23.15 | 24.53 | +1.38 |
| En->Ja | **23.66** | 21.10 | 22.78 | +1.68 |
| En->Ko | **19.75** | 18.41 | 16.62 | -1.79 |
| En->Pt | **38.40** | 37.35 | 37.90 | +0.55 |
| En->Es | 34.50 | 34.25 | **36.21** | +1.96 |

- MoE-Multi beats multilingual GNMT on **11 of 12** language pairs (up to +5.84 BLEU on Ko->En).
- MoE-Multi beats **monolingual** GNMT on **8 of 12** pairs, despite being a single model.
- **Failure case:** En->Ko degrades by -1.79 BLEU vs GNMT-Multi, attributed to "severe overtraining" from oversampling rare language pairs (Section 5.4).

### Computational Efficiency

Observed efficiency on Tesla K40 GPUs (theoretical max: 4.29 TFLOPS/GPU, Section 5.1):

| Configuration | TFLOPS/GPU |
|---|---|
| Baseline LSTMs (no MoE) | 1.07-1.29 |
| Low-computation MoE | 0.74-0.90 |
| High-computation MoE (MoE-143M) | 1.56 |
| MoE-65536-h (99.994% sparsity) | 0.72 |
| MoE-131072-h | 0.30 |

Expert computation represents **37-46% of total FLOPs** in MoE models (Section 5.1). The low efficiency of MoE-131072-h (0.30 TFLOPS/GPU) is partly because the training batch size was not increased proportionally to the GPU count (Appendix D).

### Expert Specialization

Experts become highly specialized by syntax and semantics (Appendix E, Table 9). Examples from the WMT'14 En-Fr encoder MoE layer:
- **Expert 381:** words related to "researchers", "innovation", "technology", "generation"
- **Expert 752:** indefinite article "a" followed by importance/leadership terms ("plays a core", "assume a leadership", "plays a central")
- **Expert 2004:** words related to speed/dynamics ("rapidly growing", "swift", "volatile", "quick")

This specialization is qualitative evidence only; no quantitative analysis of expert specialization patterns was performed.

---

## Limitations and Failure Modes

1. **Diminishing returns at extreme sparsity:** At 131072 experts on the 100B word corpus, quality degrades compared to 65536 experts (29.2 vs 28.9 PPL), "possibly a result of too much sparsity" (Section 5.2). The paper does not investigate the root cause.

2. **Load balancing imperfect for rare language pairs:** In multilingual translation, En->Ko performance degrades (-1.79 BLEU vs GNMT-Multi), attributed to "severe overtraining" from oversampling rare language pairs in the training corpus (Section 5.4).

3. **Efficiency drops with extreme expert counts:** The 131072-expert model achieves only 0.30 TFLOPS/GPU vs 1.23 TFLOPS/GPU for the baseline, partly because batch size was not scaled with GPU count (Appendix D).

4. **Memory optimization required:** Fitting 1B+ parameters per GPU required not storing expert hidden activations (recomputing on backward pass) and using a factored Adam approximation (beta_1 = 0, factored second moment) (Appendix D).

5. **LSTM-based architectures only:** All experiments use LSTM backbones; applicability to Transformers or other architectures was not demonstrated.

6. **Infrastructure-dependent gating:** The single-pair MT experiments used strictly balanced gating (Appendix F) due to infrastructure constraints rather than principled design. The multilingual model used noisy top-k gating. This means the MT results involve two different gating strategies, complicating interpretation.

### Scope and Comparability

- **What was not tested:** No Transformer-based experiments; no models smaller than ~8M ops/timestep; no evaluation on tasks beyond language modeling and translation (e.g., question answering, classification). No comparison to other conditional computation methods beyond dense baselines.
- **Comparability notes:** The paper's BLEU scores use tokenized BLEU via Moses multi-bleu.pl, which differs from SacreBLEU used in later work, making cross-paper comparison imprecise. The 100B word corpus is internal to Google and not reproducible. Training was limited to 10 epochs on 1B Word (the best published baseline ran for 100 epochs to achieve 30.6 PPL, which the MoE did not attempt). Hardware (Tesla K40) is several generations old; efficiency numbers do not transfer to modern accelerators.

---

## Conclusions

### Contributions

1. **First practical demonstration of massive conditional computation gains.** The paper achieves >1000x capacity improvement with minor efficiency losses, validating conditional computation as a viable scaling approach after years of theoretical proposals that did not deliver in practice (Section 6, Abstract).

2. **Noisy Top-K gating mechanism.** A simple, differentiable sparse gating function that adds learnable Gaussian noise before top-k selection, enabling end-to-end training via backpropagation without REINFORCE (Section 2.1, Equations 3-5).

3. **Distributed training scheme for sparse models.** Mixed data and model parallelism that scales expert batch sizes with device count while keeping memory and bandwidth per device constant (Section 3.1).

4. **Auxiliary losses for load balancing.** Importance and load losses (Equations 6-7, 10-11) that ensure balanced expert utilization; demonstrated via ablation that any nonzero combination suffices for quality but both together minimize load imbalance (Table 6, Appendix A).

5. **State-of-the-art results on language modeling and translation.** New best results on 1B Word benchmark (28.0 PPL at 10 epochs vs 34.7 for best published at same epoch count) and WMT'14 translation (40.56 BLEU En-Fr, 26.03 BLEU En-De) (Tables 1-3).

6. **Scaling to 137 billion parameters.** Demonstrated training of models with up to 137B MoE parameters (131072 experts) across 128 GPUs, with 65536 experts (68.8B params) being the sweet spot for quality (Section 5.2, Table 8).

### Implications

1. **Decoupling capacity from compute:** MoE demonstrates that model capacity can scale independently of computational cost, suggesting that much larger models are tractable if sparsity can be exploited. (This was later confirmed by Switch Transformer, Mixtral, and other production MoE systems.)

2. **Foundation for modern MoE architectures:** This work established the core techniques (top-k gating, load balancing losses, mixed parallelism) that were directly adopted by subsequent MoE work including GShard, Switch Transformer, and DeepSeek MoE.

3. **Expert specialization as emergent behavior:** The observation that experts spontaneously specialize by syntax and semantics (Table 9, Appendix E) suggests MoE may learn modular representations, though this was only qualitatively characterized.

---

## Key Claims

1. **C1: >1000x capacity improvement with minor efficiency loss.** The paper demonstrates models with 4B+ parameters that match or exceed dense baselines using 6-20x less computation. MoE-4096-h has 4.3B parameters at 8.9M ops/timestep vs ~8.4M parameters at 8.4M ops for dense baselines (Table 7). Evidence: a single benchmark (1B Word) with a single run per model; no variance estimates reported. Status: **supported**.

2. **C2: 24% perplexity reduction at fixed compute.** On the 1B Word benchmark with ~8M ops/timestep, MoE-4096-h achieves 34.1 perplexity vs ~45.0 for computationally-matched baselines (LSTM-2048-512 at 45.0 after 10 epochs). Evidence: Figure 2-left, Table 7. Single benchmark, single run. Status: **supported**.

3. **C3: 18% improvement over best published at matched epochs.** MoE-143M achieves 28.0 test perplexity after 10 epochs vs the best published 34.7 at 10 epochs, at comparable compute (142.7M vs 151M ops/timestep). Note: the best published model reaches 30.6 after 100 epochs, which the MoE did not attempt. Evidence: Table 1. Single benchmark, single run. Status: **supported** (scope: 10 epochs only).

4. **C4: +1.34 BLEU on WMT'14 En-Fr over GNMT; +0.64 over GNMT+RL.** MoE achieves 40.56 BLEU vs GNMT at 39.22 and GNMT+RL at 39.92. The model does not use RL refinement. Evidence: Table 2. Single language pair, single run; trained on 64 K40s vs GNMT's 96 K80s. Status: **supported**.

5. **C5: +1.12 BLEU on WMT'14 En-De over GNMT.** MoE achieves 26.03 BLEU vs GNMT at 24.91. Evidence: Table 3. Single language pair, single run. Status: **supported**.

6. **C6: 39% perplexity reduction on 100B word corpus.** MoE-65536-h achieves 28.9 perplexity vs 47.0 for 4xLSTM-512 baseline at similar compute (~8-9M ops/timestep). Evidence: Table 8, Figure 3. Single run on internal dataset (not publicly reproducible). Status: **supported**.

7. **C7: Single multilingual model beats specialized models on 8/12 pairs.** MoE-Multi beats monolingual GNMT on 8 of 12 language pairs and multilingual GNMT on 11 of 12. Evidence: Table 5. Single model, single training run; no variance estimates. The failure case (En->Ko, -1.79 BLEU) is attributed to data oversampling, not a model limitation per se. Status: **supported**.

---

## Open Questions

1. **Can MoE be applied to Transformer architectures?** The paper uses only LSTM-based models. The combination of MoE with self-attention was not explored. **Addressed by** Switch Transformer (Fedus et al., 2022; `2022-06-switch-transformers-moe` in this repository), which applies MoE to Transformer FFN layers and scales to 1.6T parameters.

2. **How does MoE scale to trillion-parameter models?** The authors state "It is our goal to train a trillion-parameter model on a trillion-word corpus" (Section 3.1) but achieved only 137B parameters. **Addressed by** Switch Transformer (`2022-06-switch-transformers-moe`), which reaches 1.6T parameters.

3. **Can recurrent MoE improve results?** The paper suggests replacing LSTM weight matrices with MoE as a future direction (Section 3.1) but does not test this. **Unresolved** within this reference directory.

4. **Why do experts specialize semantically?** Expert specialization by syntax and semantics is observed qualitatively (Table 9, Appendix E) but not explained mechanistically. **Unresolved**.

5. **What causes quality degradation at extreme sparsity?** Performance degrades at 131072 experts (29.2 PPL) compared to 65536 experts (28.9 PPL) despite doubled capacity. The paper attributes this to "too much sparsity" but does not investigate further (Section 5.2). **Unresolved**.

---

## Core References and Why They Are Referenced

### Conditional Computation Predecessors

- **Bengio et al. (2013)** -- *Estimating or Propagating Gradients Through Stochastic Neurons.* Proposes stochastic neurons and noisy rectifiers for conditional computation. The MoE gating function builds on this "occasionally-sensitive behavior" (Section 2.1).

- **Bengio et al. (2015)** -- *Conditional Computation in Neural Networks for Faster Models.* Uses block-wise dropout, three loss terms, and REINFORCE for gating. The MoE paper differs by using straight-through top-k gating with only two losses, trained via backpropagation.

- **Eigen et al. (2013)** -- *Learning Factored Representations in a Deep Mixture of Experts.* Introduces using multiple MoEs with their own gating networks as parts of a deep model, and first observes the self-reinforcing expert imbalance. This paper extends the idea with sparse gating and convolutional application.

- **Cho & Bengio (2014)** -- *Exponentially Increasing the Capacity-to-Computation Ratio.* Proposes a parameterized weight matrix related to MoE with simple weight matrix experts.

### Mixture of Experts Foundations

- **Jacobs et al. (1991)** -- *Adaptive Mixtures of Local Experts.* Original MoE paper introducing the mixture-of-experts concept with softmax gating.

- **Jordan & Jacobs (1994)** -- *Hierarchical Mixtures of Experts and the EM Algorithm.* Introduces hierarchical MoE structure and softmax gating function used as the starting point for the paper's gating design.

### Language Modeling Baselines

- **Jozefowicz et al. (2016)** -- *Exploring the Limits of Language Modeling.* Provides the primary LSTM baselines on the 1B Word benchmark (30.6 PPL at 100 epochs, 34.7 at 10 epochs). The MoE paper's best result (28.0 PPL at 10 epochs) substantially improves on this.

- **Chelba et al. (2013)** -- *One Billion Word Benchmark.* Introduces the 1B Word benchmark dataset and evaluation protocol used for the main language modeling experiments.

### Machine Translation Baselines

- **Wu et al. (2016)** -- *Google's Neural Machine Translation System (GNMT).* The MoE architecture modifies GNMT by reducing LSTM layers and inserting MoE layers. GNMT and GNMT+RL results serve as the primary translation baselines in Tables 2-5.

- **Johnson et al. (2016)** -- *Google's Multilingual NMT System.* Provides the multilingual GNMT baseline and training dataset for the 12-language-pair experiments (Section 5.4).

### Sequence Modeling

- **Hochreiter & Schmidhuber (1997)** -- *Long Short-Term Memory.* LSTM architecture used as the backbone for all MoE models in the paper.

- **Sutskever et al. (2014)** -- *Sequence to Sequence Learning.* Establishes the encoder-decoder paradigm for sequence transduction that the translation models build upon.

### Training and Optimization

- **Kingma & Ba (2015)** -- *Adam.* Optimizer used for all experiments, with modifications (beta_1 = 0, factored second moment) for memory efficiency at the 100B-word scale (Appendix D).

- **He et al. (2015)** -- *Deep Residual Learning.* Residual connections used around all LSTM and MoE layers to encourage gradient flow (Appendix C, Appendix E).

- **Gruslys et al. (2016)** -- *Memory-Efficient Backpropagation Through Time.* Technique for reducing stored activations in unrolled RNNs, referenced as enabling larger batch sizes for recurrent MoE (Section 3.1).

### Translation Evaluation

- **Luong et al. (2015a)** -- *Effective Approaches to Attention-based NMT.* Previous WMT results used as baselines; source of the Moses multi-bleu.pl BLEU evaluation script used in the experiments.

- **Zhou et al. (2016)** -- *Deep Recurrent Models with Fast-Forward Connections.* DeepAtt and DeepAtt+PosUnk baselines in Tables 2-3 for WMT'14 translation.
