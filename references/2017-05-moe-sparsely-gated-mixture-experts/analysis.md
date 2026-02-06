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
    evidence: "Abstract, Section 1.2"
    status: supported
  - id: C2
    claim: "MoE with 4096 experts achieves 24% lower perplexity than computationally-matched baselines on 1B Word benchmark"
    evidence: "Figure 2-left, Section 5.1"
    status: supported
    scope: "8M ops/timestep budget"
    magnitude: "24% perplexity reduction"
  - id: C3
    claim: "MoE model achieves 28.0 test perplexity on 1B Word benchmark vs 30.6 for best published LSTM at comparable compute"
    evidence: "Table 1, Section 5.1"
    status: supported
    magnitude: "8.5% lower perplexity"
  - id: C4
    claim: "MoE achieves 40.56 BLEU on WMT'14 En-Fr, surpassing GNMT+RL (39.92) by 0.64 BLEU"
    evidence: "Table 2, Section 5.3"
    status: supported
  - id: C5
    claim: "MoE achieves 26.03 BLEU on WMT'14 En-De vs GNMT (24.91), a gain of 1.12 BLEU"
    evidence: "Table 3, Section 5.3"
    status: supported
  - id: C6
    claim: "On 100B word corpus, 65536-expert MoE achieves 39% lower perplexity than computationally-matched baseline"
    evidence: "Figure 3, Section 5.2"
    status: supported
    scope: "100B word training set"
    magnitude: "39% perplexity reduction"
  - id: C7
    claim: "Multilingual MoE beats single-pair GNMT models on 8 of 12 language pairs while using a single model"
    evidence: "Table 5, Section 5.4"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: concurrent
    detail: "Both papers published in 2017; the Transformer paper cites MoE results as a baseline in Table 2 (26.03 BLEU on EN-DE)"
open_questions:
  - question: "Can MoE be applied to Transformer architectures rather than LSTMs?"
    addressed_by: null
  - question: "How does MoE scale to trillion-parameter models?"
    addressed_by: null
  - question: "Can recurrent MoE (replacing LSTM weight matrices with MoE) improve results further?"
    addressed_by: null
---
# Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer

**Authors:** Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, Jeff Dean (Google Brain, Jagiellonian University)
**Date:** April 2017, ICLR 2017; arXiv:1701.06538

---

## Core Research Problem

Scaling neural network capacity has been central to deep learning success, but for typical models where the entire network is activated for every example, increasing capacity leads to a **roughly quadratic blow-up in training costs** as both model size and training examples increase (Section 1.1). Conditional computation -- where parts of the network are active on a per-example basis -- had been proposed theoretically as a way to increase capacity without proportional compute increase, but prior work had not demonstrated massive improvements in practice.

The authors identify five key challenges that prevented previous conditional computation approaches from succeeding (Section 1.1):

1. **GPU arithmetic vs branching trade-off:** Modern GPUs are much faster at arithmetic than branching, requiring large chunks of the network to be activated together.
2. **Shrinking batch problem:** Conditional computation reduces batch sizes for conditionally active chunks, hurting efficiency.
3. **Network bandwidth bottleneck:** GPU clusters have computational power thousands of times greater than network bandwidth, requiring high compute-to-communication ratios.
4. **Loss function complexity:** Multiple auxiliary loss terms may be needed for load balancing and sparsity.
5. **Dataset scale:** Prior work used small image datasets (up to 600K images) insufficient for training billion-parameter models.

The core challenge is: **how to achieve massive increases in model capacity (1000x+) through conditional computation while maintaining computational efficiency on modern GPU clusters.**

---

## Problem Solutions

The paper introduces the **Sparsely-Gated Mixture-of-Experts (MoE) layer**, a general-purpose neural network component consisting of up to thousands of feed-forward expert sub-networks and a trainable gating network that selects a sparse combination of experts for each input (Section 1.2).

The solution rests on four key innovations:

1. **Noisy Top-K gating:** A differentiable gating mechanism that adds tunable Gaussian noise before selecting the top-k experts, enabling sparse expert selection while maintaining gradient flow.

2. **Mixed data and model parallelism:** A distributed training scheme where standard layers use data parallelism while experts are sharded across devices, allowing batch sizes to scale with device count.

3. **Auxiliary load-balancing losses:** Two soft constraints (importance loss and load loss) that encourage balanced expert utilization without hard constraints.

4. **Hierarchical MoE:** A two-level expert hierarchy that reduces branching factor for very large expert counts.

---

## Approach Details

### Method

The MoE layer consists of n expert networks E_1, ..., E_n and a gating network G. For input x, the output is (Equation 1):

> y = sum_{i=1}^{n} G(x)_i * E_i(x)

Computation is saved through sparsity: wherever G(x)_i = 0, E_i(x) need not be computed. In practice, only k experts (typically k=4) are active per input despite having thousands of experts.

**Noisy Top-K Gating (Section 2.1, Equations 3-5):**

> G(x) = Softmax(KeepTopK(H(x), k))
>
> H(x)_i = (x * W_g)_i + StandardNormal() * Softplus((x * W_noise)_i)
>
> KeepTopK(v, k)_i = v_i if v_i is in top k elements of v, else -infinity

The noise term (controlled by learnable W_noise) helps with load balancing by introducing stochasticity in expert selection. Setting non-top-k values to -infinity causes corresponding gate values to equal 0 after softmax.

### Key Technical Components

**Addressing the Shrinking Batch Problem (Section 3.1):**

The naive MoE has batch size kb/n per expert for a batch of b examples with k active experts out of n total. The solution combines:

1. *Mixed parallelism:* Distribute standard layers via data parallelism but keep one shared copy of each expert. Each expert receives examples from all data-parallel batches, achieving a d-fold improvement in expert batch size when distributed over d devices.

2. *Convolutional application:* Apply the same MoE to all timesteps together as one batch, multiplying batch size by the sequence length.

**Load Balancing (Section 4, Appendix A):**

Without intervention, the gating network converges to always selecting the same few experts. Two auxiliary losses prevent this:

*Importance loss (Equations 6-7):*

> Importance(X) = sum_{x in X} G(x)
>
> L_importance(X) = w_importance * CV(Importance(X))^2

where CV is coefficient of variation. This encourages equal total gate weight across experts.

*Load loss (Equations 10-11):*

> Load(X)_i = sum_{x in X} P(x, i)

where P(x, i) is the probability that expert i is selected given the noise distribution. This ensures balanced example counts, not just total weights.

**Hierarchical MoE (Appendix B):**

For very large expert counts, a two-level hierarchy reduces branching factor. A primary gating network selects among groups, each containing a secondary MoE with its own gating network (Equation 12):

> y_H = sum_{i=1}^{a} sum_{j=1}^{b} G_primary(x)_i * G_i(x)_j * E_{i,j}(x)

### Experimental Setup

**1 Billion Word Language Modeling Benchmark (Section 5.1):**
- Dataset: ~829M words, 793K vocabulary (Chelba et al., 2013)
- Architecture: embedding -> LSTM -> MoE -> LSTM -> softmax
- All layers have 512 dimensions; LSTM layers have 2048 hidden units with 512-dim output projection
- Experts: feed-forward networks with one 1024-unit ReLU hidden layer and 512-dim output (~1M parameters each)
- Hardware: 16-32 Tesla K40 GPUs
- Training: Adam optimizer, ~300K words per batch, 10 epochs (27K steps), 12-18 hours
- Loss weights: w_importance = 0.1, w_load = 0.1

**100 Billion Word Google News Corpus (Section 5.2):**
- Internal Google dataset of shuffled unique sentences
- Same architecture as above, scaled to 131K experts (137B MoE parameters)
- Hardware: 32-128 Tesla K40 GPUs
- Training: once through ~100B words

**Machine Translation (Section 5.3):**
- Modified GNMT architecture: 3 encoder + 2 decoder LSTM layers (reduced from 9+8)
- MoE layers inserted between encoder layers 2-3 and decoder layers 1-2
- Up to 2048 experts, each with 2048-unit hidden layer (~2M parameters, ~8B total in MoE)
- Datasets: WMT'14 En-Fr (36M pairs), WMT'14 En-De (5M pairs), Google Production En-Fr
- 32K shared wordpiece vocabulary
- Hardware: up to 64 K40 GPUs

### Key Results

**1 Billion Word Benchmark (Table 1, Table 7):**

| Model | Test PPL (10 epochs) | Test PPL (final) | #Params (excl. embed) | ops/timestep |
|-------|---------------------|------------------|----------------------|--------------|
| Best Published (2xLSTM-8192) | 34.7 | 30.6 | 151M | 151M |
| Low-Budget MoE | 34.1 | - | 4.3B | 8.9M |
| Medium-Budget MoE | 31.3 | - | 4.3B | 33.8M |
| High-Budget MoE | **28.0** | - | 4.4B | 142.7M |

- The Low-Budget MoE matches SOTA quality using only **6% of the computation**
- MoE-4096-h (hierarchical, 4096 experts) achieves 34.1 perplexity at 8.9M ops/timestep vs LSTM baseline at 45.0 perplexity -- a **24% reduction**

**100 Billion Word Corpus (Table 8, Figure 3):**

| Model | Test PPL (1 epoch) | #Params (excl. embed) |
|-------|-------------------|----------------------|
| 4xLSTM-512 baseline | 47.0 | 8.4M |
| MoE-65536-h | **28.9** | 68.8B |

- 39% lower perplexity than computationally-matched baseline
- Benefits continue scaling up to 65536 experts (68B parameters)
- Quality degrades at 131072 experts, possibly due to excessive sparsity

**Machine Translation (Tables 2-4):**

| Model | WMT'14 En-Fr BLEU | WMT'14 En-De BLEU | Training Time |
|-------|-------------------|-------------------|---------------|
| GNMT+RL | 39.92 | 24.66 | 6 days/96 K80s |
| MoE (2048 experts) | **40.56** | **26.03** | 3-6 days/64 K40s |

- **+0.64 BLEU** on En-Fr, **+1.12 BLEU** on En-De over GNMT+RL baseline
- Training time comparable or shorter despite 8.7B parameters vs 278M

**Multilingual Translation (Table 5):**

Single MoE model (8.7B params) trained on 12 language pairs:
- Beats multilingual GNMT on 11 of 12 language pairs (up to +5.84 BLEU on Korean->English)
- Beats monolingual GNMT models on 8 of 12 pairs
- 19% lower dev perplexity than multilingual GNMT

### Computational Efficiency

Observed efficiency on Tesla K40 GPUs (theoretical max: 4.29 TFLOPS):
- Baseline LSTMs: 1.07-1.29 TFLOPS/GPU
- Low-computation MoE: 0.74-0.90 TFLOPS/GPU
- High-computation MoE: 1.56 TFLOPS/GPU
- Even at 65536 experts (99.994% sparsity): 0.72 TFLOPS/GPU

Expert computation represents 37-46% of total FLOPs in MoE models.

### Expert Specialization

The paper provides qualitative evidence that experts specialize by syntax and semantics (Appendix E, Table 9). For example:
- Expert 381: words related to "researchers", "innovation", "technology"
- Expert 752: phrases with indefinite article "a" followed by importance/leadership terms ("plays a core", "assume a leadership")
- Expert 2004: words related to speed/dynamics ("rapidly growing", "swift", "volatile")

---

## Limitations and Failure Modes

1. **Diminishing returns at extreme sparsity:** At 131072 experts on the 100B word corpus, quality degrades compared to 65536 experts, "possibly a result of too much sparsity" (Section 5.2).

2. **Load balancing imperfect for rare language pairs:** In multilingual translation, English->Korean performance degrades (-1.79 BLEU vs GNMT-Multi), attributed to "severe overtraining" from oversampling rare pairs (Section 5.4).

3. **Efficiency drops with extreme expert counts:** The 131072-expert model achieves only 0.30 TFLOPS/GPU vs 1.23 TFLOPS/GPU for the baseline, partly due to not scaling batch size with GPU count (Section 5.2).

4. **Memory optimization required:** Fitting 1B+ parameters per GPU required not storing expert hidden activations (recomputing on backward pass) and using a factored Adam approximation (Appendix D).

5. **LSTM-based only:** All experiments use LSTM architectures; applicability to other architectures (e.g., Transformers) not demonstrated.

---

## Conclusions

### Contributions

1. **First practical demonstration of massive conditional computation gains.** The paper achieves >1000x capacity improvement with minor efficiency losses, validating conditional computation as a viable scaling approach (Section 6).

2. **Noisy Top-K gating mechanism.** A simple, differentiable sparse gating function that adds learnable noise before top-k selection, enabling end-to-end training via backpropagation (Section 2.1).

3. **Distributed training scheme for sparse models.** Mixed data and model parallelism that scales expert batch sizes with device count while keeping memory and bandwidth per device constant (Section 3.1).

4. **Auxiliary losses for load balancing.** Importance and load losses that ensure balanced expert utilization without hard constraints (Section 4, Appendix A).

5. **State-of-the-art results on language modeling and translation.** New best results on 1B Word benchmark (28.0 perplexity) and WMT'14 translation (40.56/26.03 BLEU on En-Fr/En-De) (Tables 1-3).

6. **Scaling to 137 billion parameters.** Demonstrated training of models with up to 137B MoE parameters across 128 GPUs (Section 5.2).

### Implications

1. **Decoupling capacity from compute:** MoE demonstrates that model capacity can scale independently of computational cost, suggesting that much larger models are tractable if sparsity can be exploited.

2. **Foundation for modern MoE architectures:** This work established the core techniques (top-k gating, load balancing losses, mixed parallelism) later adopted by Mixtral, DeepSeek, and other production MoE systems.

3. **Expert specialization as emergent behavior:** The observation that experts spontaneously specialize by syntax/semantics suggests MoE may learn modular representations, though this was not rigorously studied.

---

## Key Claims

1. **C1: >1000x capacity improvement with minor efficiency loss.** The paper demonstrates models with 4B+ parameters that match or exceed dense baselines using 6-20x less computation. Evidence: Table 1 shows MoE-Low matching best published results at 6% compute. Status: **supported**.

2. **C2: 24% perplexity reduction at fixed compute.** On the 1B Word benchmark with ~8M ops/timestep, MoE-4096-h achieves 34.1 perplexity vs 45.0 for computationally-matched baselines. Evidence: Figure 2-left. Status: **supported**.

3. **C3: State-of-the-art language modeling.** High-Budget MoE achieves 28.0 test perplexity after 10 epochs vs 34.7 for best published LSTM. Evidence: Table 1. Status: **supported**.

4. **C4: +0.64 BLEU on WMT'14 En-Fr.** MoE achieves 40.56 BLEU vs GNMT+RL at 39.92 BLEU, trained in half the time on 2/3 the GPUs. Evidence: Table 2. Status: **supported**.

5. **C5: +1.12 BLEU on WMT'14 En-De.** MoE achieves 26.03 BLEU vs GNMT at 24.91 BLEU. Evidence: Table 3. Status: **supported**.

6. **C6: 39% perplexity reduction on 100B word corpus.** MoE-65536-h achieves 28.9 perplexity vs 47.0 for 4xLSTM-512 baseline at similar compute. Evidence: Table 8. Status: **supported**.

7. **C7: Single multilingual model beats specialized models.** MoE-Multi beats monolingual GNMT on 8/12 language pairs. Evidence: Table 5. Status: **supported**.

---

## Open Questions

1. **Can MoE be applied to Transformer architectures?** The paper uses only LSTM-based models. The combination of MoE with self-attention was not explored. **Addressed by** subsequent work (GShard, Switch Transformer, Mixtral), though not in this reference directory.

2. **How does MoE scale to trillion-parameter models?** The authors state "It is our goal to train a trillion-parameter model on a trillion-word corpus" (Section 3.1) but do not achieve this. **Unresolved** within this paper.

3. **Can recurrent MoE improve results?** The paper suggests replacing LSTM weight matrices with MoE as a future direction (Section 3.1). **Unresolved**.

4. **Why do experts specialize semantically?** Expert specialization by syntax/semantics is observed but not explained mechanistically. **Unresolved**.

5. **What causes quality degradation at extreme sparsity?** Performance degrades at 131072 experts despite continued capacity growth. The paper attributes this to "too much sparsity" but does not investigate further. **Unresolved**.

---

## Core References and Why They Are Referenced

### Conditional Computation Predecessors

- **Bengio et al. (2013)** -- *Estimating or Propagating Gradients Through Stochastic Neurons.* Proposes stochastic neurons and noisy rectifiers for conditional computation. The MoE gating function builds on this "occasionally-sensitive behavior" (Section 2.1).

- **Bengio et al. (2015)** -- *Conditional Computation in Neural Networks for Faster Models.* Uses block-wise dropout and REINFORCE for gating. The MoE paper differs by using straight-through top-k gating trained via backpropagation.

- **Eigen et al. (2013)** -- *Learning Factored Representations in a Deep Mixture of Experts.* Introduces using multiple MoEs as components within a deep model. This paper extends the idea with sparse gating and convolutional application.

### Mixture of Experts Foundations

- **Jacobs et al. (1991)** -- *Adaptive Mixtures of Local Experts.* Original MoE paper introducing the mixture-of-experts concept with softmax gating.

- **Jordan & Jacobs (1994)** -- *Hierarchical Mixtures of Experts and the EM Algorithm.* Introduces hierarchical MoE structure used in the paper's large-scale experiments.

### Language Modeling Baselines

- **Jozefowicz et al. (2016)** -- *Exploring the Limits of Language Modeling.* Provides the primary LSTM baselines on the 1B Word benchmark. The MoE paper's best results (28.0 perplexity) substantially improve on this work's 30.6 perplexity.

- **Chelba et al. (2013)** -- *One Billion Word Benchmark.* Introduces the 1B Word benchmark used for evaluation.

### Machine Translation Baselines

- **Wu et al. (2016)** -- *Google's Neural Machine Translation System (GNMT).* The MoE architecture modifies GNMT by reducing LSTM layers and inserting MoE layers. GNMT+RL results serve as the primary translation baseline.

### Sequence Modeling

- **Hochreiter & Schmidhuber (1997)** -- *Long Short-Term Memory.* LSTM architecture used as the backbone for all MoE models in the paper.

- **Sutskever et al. (2014)** -- *Sequence to Sequence Learning.* Establishes the encoder-decoder paradigm for sequence transduction that the translation models build upon.

### Training and Optimization

- **Kingma & Ba (2015)** -- *Adam.* Optimizer used for all experiments, with modifications (factored second moment) for memory efficiency at scale.

- **He et al. (2015)** -- *Deep Residual Learning.* Residual connections used around all LSTM and MoE layers to encourage gradient flow.
