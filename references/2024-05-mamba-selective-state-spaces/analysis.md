---
title: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
authors: "Gu, Dao"
year: 2024
venue: "ICLR 2024"
paper_type: conference-paper
categories: ["architecture", "attention-efficiency", "state-space-models"]
scope: ["alternative to Transformers", "linear-time sequence modeling", "selective state spaces", "hardware-aware algorithms"]
benchmarks_used: ["perplexity-pile", "lambada", "hellaswag", "piqa", "arc", "winogrande", "lra"]
models_introduced: ["mamba-130m", "mamba-370m", "mamba-790m", "mamba-1.4b", "mamba-2.8b"]
models_evaluated: ["pythia-series", "gpt-2", "transformer-base"]
key_claims:
  - id: C1
    claim: "Mamba achieves 5x higher inference throughput than Transformers of similar size"
    evidence: "Figure 8, Section 4.5"
    status: supported
    scope: "A100 GPU, autoregressive generation"
    magnitude: "5x throughput improvement"
  - id: C2
    claim: "Mamba-3B matches Transformer quality at twice the model size on language modeling"
    evidence: "Table 3, Section 4.2.2"
    status: supported
    scope: "zero-shot downstream evaluation, 300B training tokens"
    magnitude: "4 points higher average on commonsense reasoning vs Pythia-3B"
  - id: C3
    claim: "Mamba is the first linear-time sequence model to match Transformer++ performance on language modeling scaling laws"
    evidence: "Figure 4, Section 4.2.1"
    status: supported
    scope: "125M to 1.3B parameters, Pile dataset"
  - id: C4
    claim: "Selection mechanism enables content-aware reasoning that LTI models cannot perform"
    evidence: "Table 1, Table 2, Section 4.1"
    status: supported
    scope: "synthetic tasks (selective copying, induction heads)"
  - id: C5
    claim: "Mamba extrapolates to 1M+ token sequences on induction heads task while attention fails beyond 16K"
    evidence: "Table 2, Table 11"
    status: supported
    scope: "trained on 256 tokens, tested up to 1M tokens"
    magnitude: "4000x length extrapolation"
  - id: C6
    claim: "Mamba's performance improves with longer context up to 1M tokens on DNA and audio"
    evidence: "Figure 5 (Right), Figure 7, Section 4.3.2, Section 4.4"
    status: supported
    scope: "HG38 DNA, YouTubeMix audio"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: complementary
    detail: "Mamba proposes a fundamentally different architecture that eliminates attention entirely while matching Transformer performance"
  - target: 2022-12-flashattention
    type: complementary
    detail: "Mamba's hardware-aware scan algorithm is analogous to FlashAttention's approach of exploiting GPU memory hierarchy; both achieve similar memory efficiency"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Both address Transformer quadratic complexity; Longformer uses sparse attention patterns while Mamba uses selective state spaces for true linear scaling"
  - target: 2020-12-bigbird-sparse-attention
    type: complementary
    detail: "BigBird and Mamba both aim for linear-time sequence modeling; BigBird approximates attention while Mamba replaces it entirely with selective SSMs"
  - target: 2022-03-in-context-learning-induction-heads
    type: extends
    detail: "Mamba uses induction heads as a key synthetic benchmark to demonstrate that selection mechanism enables associative recall capabilities"
  - target: 2023-02-llama-open-efficient-foundation
    type: evaluates
    detail: "Mamba compares against LLaMA-style Transformer++ architecture in scaling law experiments, matching its performance"
  - target: 2021-05-long-range-arena
    type: uses-benchmark
    detail: "Mamba builds on S4's success on Long Range Arena benchmarks, extending SSMs with selection"
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: complementary
    detail: "RWKV is a concurrent approach to linear-time sequence modeling using channel-wise time decay instead of selective state spaces; both achieve Transformer-level performance at scale"
  - target: 2024-10-rwkv-eagle-finch-matrix-states
    type: concurrent
    detail: "Eagle/Finch (RWKV-5/6) add matrix-valued states and data-dependent decay to RWKV; Finch outperforms Mamba on MQAR and achieves competitive efficiency"
  - target: 2023-07-retnet-retentive-network
    type: concurrent
    detail: "RetNet is a concurrent proposal for a Transformer alternative; both achieve O(1) inference through recurrent formulations but RetNet uses fixed exponential decay while Mamba uses input-dependent selection"
  - target: 2023-07-hyena-hierarchy-long-convolutions
    type: extends
    detail: "Mamba builds on Hyena and H3, replacing implicit long convolutions with input-dependent selective state spaces for content-aware reasoning while maintaining subquadratic complexity"
open_questions:
  - question: "Does Mamba scale comparably to Transformers at 7B+ parameters?"
    addressed_by: null
  - question: "Can selective SSMs match Transformer in-context learning capabilities on complex tasks?"
    addressed_by: null
  - question: "Do Mamba models support the same fine-tuning and adaptation affordances as Transformers?"
    addressed_by: null
  - question: "How do hybrid Mamba-attention architectures compare to pure Mamba?"
    addressed_by: 2025-04-gated-delta-networks
---

# Mamba: Linear-Time Sequence Modeling with Selective State Spaces

**Authors:** Albert Gu, Tri Dao (Carnegie Mellon University, Princeton University)
**Date:** May 2024, ICLR 2024 (arXiv:2312.00752)

---

## Core Research Problem

Foundation models are almost universally based on the Transformer architecture. While attention enables dense information routing within a context window, it has fundamental drawbacks: (1) inability to model anything outside a finite window, and (2) quadratic scaling with respect to window length. Many subquadratic architectures have been proposed---linear attention, gated convolutions, recurrent models, and structured state space models (SSMs)---but none have matched attention's performance on important modalities such as language.

Prior structured SSMs (S4, H3, Hyena) achieved linear or near-linear scaling and dominated benchmarks like Long Range Arena for continuous signals (audio, vision), but have been less effective on discrete, information-dense data such as text. The authors identify that a key weakness of these models is their **linear time invariance (LTI)**: the model dynamics are constant through time, preventing content-based reasoning. LTI models cannot selectively focus on or ignore inputs depending on their content---they can only perform time-aware operations.

The core challenge is: **how to build a sequence model that achieves Transformer-quality performance while scaling linearly in sequence length, by enabling content-aware selection in state space models.**

---

## Problem Solutions

Mamba addresses this through three key innovations:

1. **Selection mechanism.** Make SSM parameters (Δ, B, C) functions of the input, allowing the model to selectively propagate or forget information along the sequence depending on the current token. This enables content-aware reasoning while maintaining the recurrent structure.

2. **Hardware-aware algorithm.** The selection mechanism prevents efficient convolution-based computation. The authors design a parallel scan algorithm that exploits GPU memory hierarchy---loading parameters from HBM to SRAM, performing discretization and recurrence in SRAM, avoiding materialization of the expanded state.

3. **Simplified architecture.** Combine the H3 SSM block with the Transformer MLP block into a single homogeneous block, eliminating attention and separate MLP layers entirely.

---

## Approach Details

### Method

#### State Space Model Background

Structured SSMs (S4) define a sequence-to-sequence transformation through a latent state. The continuous-time system is:

> h'(t) = **A**h(t) + **B**x(t)
> y(t) = **C**h(t)

This is discretized using a step size Δ to produce discrete parameters (**A̅**, **B̅**) via zero-order hold (ZOH):

> **A̅** = exp(Δ**A**)
> **B̅** = (Δ**A**)^(-1)(exp(Δ**A**) - **I**) · Δ**B**

The discrete recurrence is:

> h_t = **A̅**h_{t-1} + **B̅**x_t
> y_t = **C**h_t

Prior SSMs are **linear time invariant (LTI)**: parameters (Δ, **A**, **B**, **C**) are fixed for all timesteps. This allows efficient computation as either recurrence O(BLDN) or convolution O(BLD log L), but limits modeling capability.

#### Selection Mechanism

The key innovation is making parameters input-dependent:

- **B**: (B, L, N) ← s_B(x) = Linear_N(x)
- **C**: (B, L, N) ← s_C(x) = Linear_N(x)
- **Δ**: (B, L, D) ← τ_Δ(Parameter + s_Δ(x))

where s_Δ(x) = Broadcast_D(Linear_1(x)) and τ_Δ = softplus.

This transforms the model from time-invariant to **time-varying**. The parameters now have a length dimension L, losing equivalence to convolutions but gaining the ability to selectively process inputs.

**Connection to RNN gating (Theorem 1):** When N=1, **A**=-1, **B**=1, the selective SSM reduces to a gated RNN:

> g_t = σ(Linear(x_t))
> h_t = (1 - g_t)h_{t-1} + g_t x_t

This shows that discretization of SSMs provides a principled foundation for heuristic gating mechanisms.

### Key Technical Components

#### Hardware-Aware Parallel Scan

The selection mechanism poses computational challenges: naive implementation requires O(BLDN) memory for the expanded state. The solution uses three techniques:

1. **Kernel fusion.** Load (Δ, **A**, **B**, **C**) from HBM to SRAM, perform discretization and scan in SRAM, write only final outputs to HBM. This reduces memory IOs by factor N (state dimension), achieving 20-40x speedup.

2. **Parallel scan.** Use work-efficient parallel associative scan algorithm instead of sequential recurrence.

3. **Recomputation.** Don't save intermediate states for backpropagation; recompute them in backward pass from SRAM. This matches FlashAttention memory efficiency.

#### Mamba Architecture

The Mamba block combines H3 and MLP blocks:

- Input projection expands dimension D by factor E=2
- Depthwise convolution (kernel size 4)
- SiLU/Swish activation on one branch
- Selective SSM on main branch
- Multiplicative gating
- Output projection

Two Mamba blocks have roughly 12D² parameters, matching a Transformer layer (MHA + MLP). The architecture is homogeneous: only Mamba blocks stacked with normalization and residual connections.

#### Model Configurations

| Model | Params | Layers | d_model | Training Tokens |
|-------|--------|--------|---------|-----------------|
| Mamba-130M | 130M | 24 | 768 | 300B |
| Mamba-370M | 370M | 48 | 1024 | 300B |
| Mamba-790M | 790M | 48 | 1536 | 300B |
| Mamba-1.4B | 1.4B | 48 | 2048 | 300B |
| Mamba-2.8B | 2.8B | 64 | 2560 | 300B |

State dimension N=16 for all models. Context length 2048 for pretraining.

### Experimental Setup

**Language modeling:** Trained on the Pile dataset with GPT-NeoX tokenizer, following GPT-3 training recipe with improvements (RMSNorm, no bias, higher LR with cosine decay, AdamW β=(0.9, 0.95)).

**Baselines:** Transformer (GPT-3 architecture), Transformer++ (RoPE, SwiGLU, RMSNorm), Hyena, H3++, RWKV, RetNet.

**Evaluation:** Zero-shot on LAMBADA, HellaSwag, PIQA, ARC-E, ARC-C, WinoGrande.

**Reproducibility:** Code and pretrained checkpoints released at https://github.com/state-spaces/mamba. All hyperparameters specified.

### Key Results

#### Language Modeling Scaling Laws

| Model | 125M PPL | 350M PPL | 760M PPL | 1.3B PPL |
|-------|----------|----------|----------|----------|
| Transformer | ~10.5 | ~9.0 | ~8.0 | ~7.5 |
| Transformer++ | ~9.5 | ~8.5 | ~7.5 | ~7.0 |
| Hyena | ~11.0 | ~9.5 | ~8.5 | ~8.0 |
| Mamba | ~9.5 | ~8.5 | ~7.5 | ~7.0 |

*Approximate values from Figure 4 at 2K context length.*

**Key findings:**
- Mamba is the **first attention-free model to match Transformer++** scaling
- Gap widens at longer context lengths (8K), favoring Mamba
- RWKV and RetNet could not complete 8K experiments due to memory/efficiency issues

#### Zero-Shot Downstream Evaluation

| Model | Pile PPL | LAMBADA | HellaSwag | PIQA | ARC-E | ARC-C | WinoGrande | Avg |
|-------|----------|---------|-----------|------|-------|-------|------------|-----|
| Pythia-1.4B | 7.51 | 61.7 | 52.1 | 71.0 | 60.5 | 28.5 | 57.2 | 55.2 |
| RWKV-1.5B | 7.70 | 56.4 | 52.5 | 72.4 | 60.5 | 29.4 | 54.6 | 54.3 |
| **Mamba-1.4B** | **6.80** | **64.9** | **59.1** | **74.2** | **65.5** | **32.8** | **61.5** | **59.7** |
| Pythia-2.8B | 6.73 | 64.7 | 59.3 | 74.0 | 64.1 | 32.9 | 59.7 | 59.1 |
| **Mamba-2.8B** | **6.22** | **69.2** | **66.1** | **75.2** | **69.7** | **36.3** | **63.5** | **63.3** |

*Table 3. Mamba matches Pythia at 2x model size.*

#### Synthetic Tasks

**Selective Copying:** S4 achieves 18.3% accuracy; adding selection (S6) achieves 97.0%. Mamba block with S6 achieves 99.8%.

**Induction Heads:** Mamba extrapolates perfectly to 1M tokens (trained on 256). Attention models fail beyond 2x training length. H3/Hyena fail similarly.

#### Efficiency Benchmarks

- **Scan vs Attention:** Mamba scan is faster than FlashAttention-2 beyond 2K sequence length, up to 7x faster at 32K
- **Inference throughput:** Mamba achieves 4-5x higher throughput than Transformers (no KV cache required)
- **Memory:** Comparable to FlashAttention (~16 bytes per token vs ~32 bytes for Transformer layer)

---

## Limitations and Failure Modes

### Acknowledged Limitations

1. **Scale.** Experiments limited to ≤3B parameters. Unclear if advantages hold at 7B+ scale.

2. **Continuous vs discrete modality tradeoff.** Selection mechanism helps discrete data (text, DNA) but may hurt continuous signals. Audio ablations show real-valued selective SSMs underperform complex-valued LTI SSMs on raw waveforms (Figure 10).

3. **Downstream affordances.** Unknown whether Mamba supports the same fine-tuning, prompting, RLHF, and quantization patterns as Transformers.

### Scope and Comparability

**What was not tested:**
- Models larger than 3B parameters
- Instruction tuning, RLHF, or chat applications
- Tasks requiring explicit retrieval or multi-step reasoning
- Comparison with sparse attention variants at long context

**Comparability notes:**
- All language models trained on same data (Pile, 300B tokens) with same tokenizer (GPT-NeoX)
- Transformer++ baseline uses modern recipe (RoPE, SwiGLU) making it a strong comparison
- RWKV and RetNet trained with context length 1024 vs Mamba's 2048

---

## Conclusions

### Contributions

1. **Selection mechanism for SSMs.** Introduced input-dependent parameterization of state space models, enabling content-aware reasoning while maintaining linear complexity. Connected to classical RNN gating through principled discretization (Theorem 1).

2. **Hardware-aware selective scan.** Designed fused CUDA kernel exploiting GPU memory hierarchy, achieving 20-40x speedup over naive implementation and matching FlashAttention memory efficiency.

3. **First linear-time model matching Transformer quality.** Demonstrated that Mamba matches Transformer++ on language modeling scaling laws from 125M to 1.3B parameters, and matches downstream zero-shot performance at 2x model size.

4. **State-of-the-art on DNA and audio.** Achieved best results on HG38 genomics pretraining and SC09 speech generation, with performance improving up to 1M token context.

### Implications

1. **Attention may not be necessary.** Mamba achieves Transformer-quality performance without attention, suggesting the architectural dominance of Transformers may be contingent rather than fundamental.

2. **Selection is the key capability.** The gap between LTI and selective SSMs on synthetic tasks suggests that content-aware selection---not convolution or recurrence per se---is the critical capability for language modeling.

3. **Linear-time long context is achievable.** Unlike sparse attention approximations, Mamba truly scales linearly while maintaining quality, enabling efficient modeling of million-token sequences.

4. **Inference efficiency gains.** Eliminating the KV cache enables much higher batch sizes and throughput at inference time, with implications for deployment costs.

---

## Key Claims

1. **C1:** Mamba achieves 5x higher inference throughput than Transformers of similar size (Figure 8, Section 4.5). Supported by controlled benchmarks on A100 GPU measuring tokens/second at various batch sizes.

2. **C2:** Mamba-3B matches Transformer quality at twice the model size (Table 3). Supported by zero-shot evaluation on 6 commonsense reasoning benchmarks, comparing to Pythia trained on identical data.

3. **C3:** Mamba is the first linear-time model matching Transformer++ on scaling laws (Figure 4). Supported by perplexity curves from 125M to 1.3B parameters at 2K and 8K context.

4. **C4:** Selection enables content-aware reasoning that LTI models cannot perform (Table 1, Table 2). Supported by controlled ablations showing S6 solves selective copying/induction heads while S4 fails.

5. **C5:** Mamba extrapolates to 1M+ tokens while attention fails beyond 16K (Table 11). Supported by induction heads evaluation at powers of 2 from 64 to 1M tokens.

6. **C6:** Performance improves with context up to 1M tokens on DNA/audio (Figure 5, Figure 7). Supported by perplexity curves on HG38 and YouTubeMix, controlling for compute.

---

## Open Questions

1. **Does Mamba scale to 7B+ parameters?** The paper only evaluates up to 3B. RWKV and RetNet have been evaluated at 7B, but Mamba's comparative advantage at that scale is unknown.

2. **Can selective SSMs match Transformer in-context learning?** While Mamba solves induction heads, more complex ICL tasks may require attention-like mechanisms.

3. **Do Mamba models support standard fine-tuning affordances?** The ecosystem of Transformer fine-tuning (LoRA, PEFT, RLHF) may not transfer directly.

4. **How do hybrid architectures compare?** The paper briefly shows Mamba-MHA is slightly better than pure Mamba, but hybrid architectures are not extensively explored.

---

## Core References and Why They Are Referenced

### State Space Model Foundations

- **Gu et al. (2022)** -- *S4: Efficiently Modeling Long Sequences with Structured State Spaces.* Foundation work introducing structured state space models with efficient convolutional computation.

- **Gu et al. (2022)** -- *S4D: On the Parameterization and Initialization of Diagonal State Space Models.* Showed diagonal SSMs match structured SSMs, enabling simpler parameterization.

- **Smith et al. (2023)** -- *S5: Simplified State Space Layers for Sequence Modeling.* First to use parallel scan for SSM computation, but with reduced state dimension.

### SSM Architectures

- **Dao et al. (2023)** -- *H3: Hungry Hungry Hippos.* Combined S4 with linear attention in a gated architecture, establishing the block structure Mamba simplifies.

- **Poli et al. (2023)** -- *Hyena Hierarchy.* Replaced S4 with MLP-parameterized global convolutions, showing architecture matters beyond the SSM layer.

### Transformer Baselines

- **Touvron et al. (2023)** -- *LLaMA.* Established the Transformer++ recipe (RoPE, SwiGLU, RMSNorm) that Mamba matches in scaling laws.

- **Biderman et al. (2023)** -- *Pythia.* Provides controlled baselines trained on identical data for fair downstream comparison.

### Efficiency

- **Dao et al. (2022)** -- *FlashAttention.* Hardware-aware attention algorithm exploiting memory hierarchy; Mamba's scan algorithm is analogous.

### Synthetic Task Motivation

- **Olsson et al. (2022)** -- *In-context Learning and Induction Heads.* Identified induction heads as key mechanism for ICL, motivating it as benchmark for selection capability.
