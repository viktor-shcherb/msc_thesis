---
title: "Mamba: Linear-Time Sequence Modeling with Selective State Spaces"
authors: "Gu, Dao"
year: 2024
venue: "ICLR 2024"
paper_type: conference-paper
categories: ["architecture", "attention-efficiency", "state-space-models"]
scope: ["alternative to Transformers", "linear-time sequence modeling", "selective state spaces", "hardware-aware algorithms"]
benchmarks_used: ["perplexity-pile", "lambada", "hellaswag", "piqa", "arc", "winogrande"]
models_introduced: ["mamba-130m", "mamba-370m", "mamba-790m", "mamba-1.4b", "mamba-2.8b"]
models_evaluated: ["pythia-series", "rwkv-1.5b", "rwkv-3b", "h3", "hyena", "transformer-base"]
key_claims:
  - id: C1
    claim: "Mamba achieves 4-5x higher inference throughput than Transformers of similar size"
    evidence: "Figure 8, Section 4.5, Appendix E.5"
    status: supported
    scope: "A100 80GB PCIe GPU, autoregressive generation with prompt length 2048"
    magnitude: "4-5x throughput improvement; Mamba-6.9B exceeds throughput of Transformer-1.3B"
  - id: C2
    claim: "Mamba-3B matches Transformer quality at twice the model size on language modeling"
    evidence: "Table 3, Section 4.2.2"
    status: supported
    scope: "zero-shot downstream evaluation on 6 commonsense benchmarks, 300B training tokens on the Pile, GPT-NeoX tokenizer"
    magnitude: "Mamba-2.8B averages 63.3% vs Pythia-2.8B 59.1%; matches GPT-J-6B at 63.0% (tested across 6 tasks, controlled data, strong evidence)"
  - id: C3
    claim: "Mamba is the first linear-time sequence model to match Transformer++ performance on language modeling scaling laws"
    evidence: "Figure 4, Section 4.2.1"
    status: supported
    scope: "125M to 1.3B parameters, Pile dataset, context lengths 2K and 8K"
    magnitude: "matches Transformer++ perplexity at all scales; gap widens in Mamba's favor at 8K context"
  - id: C4
    claim: "Selection mechanism enables content-aware reasoning that LTI models cannot perform"
    evidence: "Table 1, Table 2, Section 4.1"
    status: supported
    scope: "synthetic tasks (selective copying, induction heads), 2-layer models"
    magnitude: "selective copying: S4 18.3% vs S6 97.0% accuracy; induction heads: perfect extrapolation to 1M tokens"
  - id: C5
    claim: "Mamba extrapolates to 1M+ token sequences on induction heads task while attention fails beyond training length"
    evidence: "Table 2, Table 11, Section 4.1.2"
    status: supported
    scope: "trained on 256 tokens, tested up to 2^20 = 1M tokens, 2-layer model with D=64"
    magnitude: "4000x length extrapolation with perfect accuracy; MHA variants fail beyond 2x training length"
  - id: C6
    claim: "Mamba's performance improves with longer context up to 1M tokens on DNA and audio"
    evidence: "Figure 5 Right, Figure 7, Section 4.3.2, Section 4.4"
    status: supported
    scope: "HG38 DNA pretraining (1.4M params), YouTubeMix audio pretraining (3.5M params), controlling for compute"
    magnitude: "DNA perplexity monotonically decreases from ~2.95 at 1K to ~2.78 at 1M; HyenaDNA degrades at long context"
  - id: C7
    claim: "Delta is the most important selective parameter due to its connection to RNN gating"
    evidence: "Table 7, Theorem 1, Section 4.6.2"
    status: supported
    scope: "~350M language model on the Pile"
    magnitude: "selective Delta alone: 9.81 ppl; selective B alone: 10.15 ppl; selective C alone: 9.98 ppl; all selective: 8.71 ppl; non-selective baseline: 10.93 ppl"
  - id: C8
    claim: "Increasing SSM state dimension N dramatically improves performance only when B and C are selective"
    evidence: "Table 10, Section 4.6.2"
    status: supported
    scope: "~350M language model, N varied from 1 to 16"
    magnitude: "selective B/C: N=1 gives 9.73 ppl, N=16 gives 8.71 ppl (1.02 improvement); constant B/C: N=1 gives 9.88, N=16 gives 9.81 (0.07 improvement)"
  - id: C9
    claim: "Selection mechanism hurts performance on continuous-signal modalities like raw audio waveforms"
    evidence: "Figure 10, Section 5, Appendix E.4"
    status: supported
    scope: "YouTubeMix audio pretraining, homogeneous models"
    magnitude: "S4+MLP outperforms Mamba (S6) on long-form audio; effect diminishes when only inner U-Net blocks are ablated"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: complementary
    detail: "Mamba proposes a fundamentally different architecture that eliminates attention entirely while matching Transformer performance on language modeling"
  - target: 2022-12-flashattention
    type: complementary
    detail: "Mamba's hardware-aware scan algorithm is analogous to FlashAttention's approach of exploiting GPU memory hierarchy; both achieve similar memory efficiency (~16 bytes vs ~32 bytes per token per layer)"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Both address Transformer quadratic complexity; Longformer uses sparse attention patterns while Mamba uses selective state spaces for true linear scaling"
  - target: 2020-12-bigbird-sparse-attention
    type: complementary
    detail: "BigBird and Mamba both aim for linear-time sequence modeling; BigBird approximates attention while Mamba replaces it entirely with selective SSMs"
  - target: 2022-03-in-context-learning-induction-heads
    type: extends
    detail: "Mamba uses induction heads as a key synthetic benchmark demonstrating that the selection mechanism enables associative recall; Mamba extrapolates perfectly to 1M tokens on this task"
  - target: 2023-02-llama-open-efficient-foundation
    type: evaluates
    detail: "Mamba compares against LLaMA-style Transformer++ architecture (RoPE, SwiGLU, RMSNorm) in scaling law experiments, matching its performance"
  - target: 2021-05-long-range-arena
    type: extends
    detail: "Mamba builds on S4's success on Long Range Arena, extending SSMs with selection to handle discrete modalities where LTI SSMs fail"
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: complementary
    detail: "RWKV is a concurrent linear-time sequence model using channel-wise time decay instead of selective state spaces; Mamba outperforms RWKV at matched model sizes on downstream evaluation"
  - target: 2024-10-rwkv-eagle-finch-matrix-states
    type: concurrent
    detail: "Eagle/Finch (RWKV-5/6) add matrix-valued states and data-dependent decay to RWKV; Finch outperforms Mamba on MQAR and achieves competitive efficiency"
  - target: 2023-07-retnet-retentive-network
    type: concurrent
    detail: "RetNet is a concurrent Transformer alternative using fixed exponential decay; Mamba uses input-dependent selection and outperforms RetNet on scaling law experiments"
  - target: 2023-07-hyena-hierarchy-long-convolutions
    type: extends
    detail: "Mamba builds on Hyena and H3, replacing implicit long convolutions with input-dependent selective state spaces while maintaining subquadratic complexity"
  - target: 2022-04-s4-structured-state-spaces
    type: extends
    detail: "Mamba directly extends S4 by making parameters input-dependent (S4 to S6), overcoming the LTI limitation while preserving linear-time computation"
  - target: 2025-04-gated-delta-networks
    type: extended-by
    detail: "Gated Delta Networks build on the selective state space concept with delta rule updates and hybrid architectures combining linear recurrence with sliding window attention"
open_questions:
  - question: "Does Mamba scale comparably to Transformers at 7B+ parameters?"
    addressed_by: null
  - question: "Can selective SSMs match Transformer in-context learning capabilities on complex tasks beyond induction heads?"
    addressed_by: null
  - question: "Do Mamba models support the same fine-tuning and adaptation affordances (LoRA, PEFT, RLHF, quantization) as Transformers?"
    addressed_by: null
  - question: "How do hybrid Mamba-attention architectures compare to pure Mamba at scale?"
    addressed_by: 2025-04-gated-delta-networks
  - question: "Is the continuous-discrete spectrum a fundamental tradeoff, or can a single model handle both modality types?"
    addressed_by: null
---

# Mamba: Linear-Time Sequence Modeling with Selective State Spaces

**Authors:** Albert Gu, Tri Dao (Machine Learning Department, Carnegie Mellon University; Department of Computer Science, Princeton University)
**Date:** May 2024, ICLR 2024 (arXiv:2312.00752)

---

## Core Research Problem

Foundation models are almost universally based on the Transformer architecture and its core attention module. While attention enables dense information routing within a context window, it has fundamental drawbacks: (1) inability to model anything outside a finite window, and (2) **quadratic scaling** with respect to window length (Section 1). Many subquadratic architectures have been proposed -- linear attention, gated convolutions, recurrent models, and structured state space models (SSMs) -- but none have matched attention's performance on important modalities such as language.

Prior structured SSMs (S4, H3, Hyena) achieved linear or near-linear scaling and dominated benchmarks like Long Range Arena for continuous signals (audio, vision), but have been less effective on discrete, information-dense data such as text (Section 1). The authors identify that a key weakness of these models is their **linear time invariance (LTI)**: the model dynamics are constant through time, preventing content-based reasoning. LTI models cannot selectively focus on or ignore inputs depending on their content -- they can only perform time-aware operations (Section 3.1). From the convolutional view, global convolutions can solve the vanilla Copying task (which requires only time-awareness) but fail the Selective Copying task (which requires content-awareness) because the spacing between inputs-to-outputs varies and cannot be modeled by static convolution kernels (Figure 2, Section 3.1).

The core challenge is: **how to build a sequence model that achieves Transformer-quality performance while scaling linearly in sequence length, by enabling content-aware selection in state space models.**

---

## Problem Solutions

Mamba addresses this through three key innovations:

1. **Selection mechanism.** Make SSM parameters (Delta, **B**, **C**) functions of the input, allowing the model to selectively propagate or forget information along the sequence depending on the current token. This enables content-aware reasoning while maintaining the recurrent structure (Section 3.2).

2. **Hardware-aware algorithm.** The selection mechanism prevents efficient convolution-based computation (the model is no longer LTI). The authors design a parallel scan algorithm that exploits GPU memory hierarchy -- loading parameters from HBM to SRAM, performing discretization and recurrence in SRAM, avoiding materialization of the expanded state in HBM. This reduces memory IOs by a factor of N (state dimension), achieving 20-40x speedup over naive scan (Section 3.3, Appendix D).

3. **Simplified architecture.** Combine the H3 SSM block with the Transformer MLP block into a single homogeneous block (the Mamba block), eliminating attention and separate MLP layers entirely. Two Mamba blocks have roughly 12D^2 parameters, matching a Transformer layer (Section 3.4, Figure 3).

---

## Approach Details

### Method

#### State Space Model Background

Structured SSMs (S4) define a sequence-to-sequence transformation through a latent state. The continuous-time system is (Equation 1):

> h'(t) = **A**h(t) + **B**x(t)
> y(t) = **C**h(t)

This is discretized using a step size Delta to produce discrete parameters via zero-order hold (ZOH) (Equation 4):

> **A_bar** = exp(Delta * **A**)
> **B_bar** = (Delta * **A**)^{-1}(exp(Delta * **A**) - **I**) * Delta * **B**

The discrete recurrence is (Equation 2):

> h_t = **A_bar** * h_{t-1} + **B_bar** * x_t
> y_t = **C** * h_t

Prior SSMs are **linear time invariant (LTI)**: parameters (Delta, **A**, **B**, **C**) are fixed for all timesteps. This allows efficient computation as either recurrence O(BLDN) or convolution O(BLD log L), but fundamentally limits modeling capability on discrete data (Section 2).

#### Selection Mechanism

The key innovation is making parameters input-dependent (Algorithm 2, "S6"):

- **B**: (B, L, N) <- s_B(x) = Linear_N(x)
- **C**: (B, L, N) <- s_C(x) = Linear_N(x)
- **Delta**: (B, L, D) <- tau_Delta(Parameter + s_Delta(x))

where s_Delta(x) = Broadcast_D(Linear_1(x)) and tau_Delta = softplus (Section 3.2).

This transforms the model from time-invariant to **time-varying**. The discretized parameters expand from (D, N) in S4 to (B, L, D, N) in S6 -- they now vary across both batch and sequence length dimensions. This loses equivalence to convolutions but gains the ability to selectively process inputs. The model can only be computed via recurrence (scan), not convolution.

### Key Technical Components

#### Hardware-Aware Parallel Scan

The selection mechanism creates a computational challenge: naive implementation requires materializing O(BLDN) state in GPU HBM. The solution uses three classical techniques (Section 3.3, Appendix D):

1. **Kernel fusion.** Load (Delta, **A**, **B**, **C**) from HBM to SRAM, perform discretization and scan in SRAM, write only final outputs of size (B, L, D) to HBM. This reduces memory IOs by factor N (state dimension), achieving **20-40x speedup** over a standard PyTorch scan implementation (Section 4.5).

2. **Parallel associative scan.** Use work-efficient parallel scan algorithm (Blelloch, 1990) instead of sequential recurrence, enabling parallelism during training.

3. **Recomputation.** Don't save intermediate states of size (B, L, D, N) for backpropagation; recompute them in the backward pass when inputs are loaded from HBM to SRAM. This matches FlashAttention memory efficiency: each selective SSM layer stores ~16 bytes of activations per token, compared to ~12 bytes for an attention layer + ~20 bytes for an MLP layer (32 bytes total for a Transformer layer) (Appendix D).

#### Mamba Architecture

The Mamba block combines the H3 block and MLP block into a single block (Figure 3):

- Input projection expands dimension D by factor E=2
- Depthwise convolution (kernel size 4) on the main branch
- SiLU/Swish activation on the main branch
- Selective SSM (S6) on the main branch
- Multiplicative gating with a second branch (which passes through SiLU)
- Output projection

Two Mamba blocks have roughly 12D^2 parameters (3ED^2 per block with E=2), matching a Transformer layer (MHA + MLP). The architecture is homogeneous: only Mamba blocks stacked with normalization (RMSNorm) and residual connections (Section 3.4).

#### Model Configurations

| Model | Params | Layers | d_model | Training Tokens |
|-------|--------|--------|---------|-----------------|
| Mamba-130M | 130M | 24 | 768 | 300B |
| Mamba-370M | 370M | 48 | 1024 | 300B |
| Mamba-790M | 790M | 48 | 1536 | 300B |
| Mamba-1.4B | 1.4B | 48 | 2048 | 300B |
| Mamba-2.8B | 2.8B | 64 | 2560 | 300B |

State dimension N=16 for all models. Context length 2048 for pretraining. All models trained on the Pile with GPT-NeoX tokenizer (Appendix E.2.3).

#### Selective Parameter Interpretation

Three mechanistic effects of selection are elaborated (Section 3.5.2):

- **Variable spacing:** Selectivity allows filtering out irrelevant noise tokens between inputs of interest (exemplified by the Selective Copying task). Mechanically, when g_t -> 0, the input x_t is ignored.
- **Filtering context:** Selective models can reset their state at any time to remove extraneous history, so performance improves monotonically with context length (unlike LTI models).
- **Boundary resetting:** When Delta_t -> infinity (equivalently g_t -> 1), the state resets, allowing the model to handle document boundaries in packed training sequences.

### Theoretical Analysis

**Theorem 1** (Section 3.5.1, Appendix C): When N=1, **A**=-1, **B**=1, s_Delta = Linear(x), and tau_Delta = softplus, the selective SSM recurrence reduces to a gated RNN:

> g_t = sigma(Linear(x_t))
> h_t = (1 - g_t) * h_{t-1} + g_t * x_t

This establishes that **discretization of SSMs provides a principled foundation for heuristic gating mechanisms** in RNNs. The specific choices of s_Delta and tau_Delta in the Mamba parameterization are motivated by this connection: the input is projected down to 1 dimension before broadcasting with Delta, ensuring all D channels can jointly ignore an irrelevant token (Section 3.5.1).

### Experimental Setup

**Language modeling:** Trained on the Pile dataset with GPT-NeoX tokenizer, following the GPT-3 training recipe with improvements: RMSNorm instead of LayerNorm, no linear bias, higher learning rate (5x GPT-3 specification) with cosine decay to 1e-5, AdamW with beta=(0.9, 0.95), weight decay 0.1, gradient clip 1.0 (Appendix E.2).

**Scaling law models:** 125M, 350M, 760M, 1.3B parameters following Chinchilla token counts (2.5B to 26B tokens proportional to size). Context lengths 2048 and 8192 (Table 12).

**Baselines:** Transformer (GPT-3 architecture), Transformer++ (RoPE, SwiGLU, RMSNorm -- the LLaMA recipe), Hyena, H3++, RWKV, RetNet (Section 4.2.1, Appendix E.2.1).

**Downstream evaluation:** Zero-shot on LAMBADA (acc), HellaSwag (acc_norm), PIQA (acc), ARC-E (acc), ARC-C (acc_norm), WinoGrande (acc), using the EleutherAI LM evaluation harness. Compared against Pythia (same data/tokenizer/300B tokens), RWKV (same tokenizer/300B tokens, but context 1024 vs Mamba's 2048), GPT-Neo, OPT, Hybrid H3, GPT-J (Appendix E.2.3).

**DNA modeling:** HG38 dataset (~4.5B base pairs), causal language modeling. Model size scaling at context 1024 with models from ~250K to ~40M parameters. Context length scaling with 1.4M-parameter models at lengths 2^10 to 2^20. Great Apes species classification (5-way: human, chimpanzee, gorilla, orangutan, bonobo) fine-tuning at context lengths up to 1M (Appendix E.3).

**Audio modeling:** YouTubeMix piano dataset (16kHz, mu-law 8-bit), SaShiMi U-Net backbone with Mamba blocks replacing S4+MLP blocks. SC09 speech generation (1-second clips, 16kHz). Models 3.5M-24.3M parameters (Appendix E.4).

**Reproducibility:** Code and pretrained checkpoints released at https://github.com/state-spaces/mamba. All hyperparameters fully specified across appendices E.1-E.5. Seeds not explicitly reported.

### Key Results

#### Language Modeling Scaling Laws

Figure 4 shows scaling laws on the Pile from ~125M to ~1.3B parameters under the Chinchilla protocol at context lengths 2048 and 8192:

- **Mamba is the first attention-free model to match Transformer++** (the strong LLaMA-style recipe) on perplexity scaling laws (Section 4.2.1).
- The gap between Mamba and Transformer++ is negligible at 2K context and widens slightly in Mamba's favor at 8K context.
- All other subquadratic models (Hyena, H3++, RWKV, RetNet) fall below Transformer++ at all scales.
- RWKV and RetNet results are missing at 8K context due to out-of-memory or unrealistic computation requirements (single scaling law experiment per architecture; limited evidence for the 8K claim).

#### Zero-Shot Downstream Evaluation

| Model | Pile PPL | LAMBADA acc | HellaSwag acc_n | PIQA acc | ARC-E acc | ARC-C acc_n | WinoGrande acc | Avg |
|-------|----------|-------------|-----------------|----------|-----------|-------------|----------------|-----|
| Pythia-1.4B | 7.51 | 61.7 | 52.1 | 71.0 | 60.5 | 28.5 | 57.2 | 55.2 |
| RWKV-1.5B | 7.70 | 56.4 | 52.5 | 72.4 | 60.5 | 29.4 | 54.6 | 54.3 |
| **Mamba-1.4B** | **6.80** | **64.9** | **59.1** | **74.2** | **65.5** | **32.8** | **61.5** | **59.7** |
| GPT-Neo-2.7B | -- | 62.2 | 55.8 | 72.1 | 61.1 | 30.2 | 57.6 | 56.5 |
| Pythia-2.8B | 6.73 | 64.7 | 59.3 | 74.0 | 64.1 | 32.9 | 59.7 | 59.1 |
| RWKV-3B | 7.00 | 63.9 | 59.6 | 73.7 | 67.8 | 33.1 | 59.6 | 59.6 |
| **Mamba-2.8B** | **6.22** | **69.2** | **66.1** | **75.2** | **69.7** | **36.3** | **63.5** | **63.3** |
| GPT-J-6B | -- | 68.3 | 66.3 | 75.4 | 67.0 | 36.6 | 64.1 | 63.0 |

*(Table 3, Section 4.2.2. Mamba models compared to baselines trained on the same data/tokenizer. Mamba is best-in-class at every size and matches baselines at 2x model size.)*

**Key findings** (tested across 6 benchmarks with controlled training data -- strong evidence):
- Mamba-1.4B (59.7% avg) exceeds Pythia-2.8B (59.1%), RWKV-3B (59.6%), and GPT-Neo-2.7B (56.5%).
- Mamba-2.8B (63.3% avg) matches GPT-J-6B (63.0%) and exceeds Pythia-6.9B (61.7%), RWKV-7.4B (62.5%).

#### Synthetic Tasks

**Selective Copying** (Table 1, Section 4.1.1):

| Arch. | Layer | Accuracy |
|-------|-------|----------|
| No gate | S4 | 18.3 |
| No gate | S6 | **97.0** |
| H3 | S4 | 57.0 |
| H3 | Hyena | 30.1 |
| H3 | S6 | **99.7** |
| Mamba | S4 | 56.4 |
| Mamba | Hyena | 28.4 |
| Mamba | S6 | **99.8** |

The selection mechanism (S4->S6) is the critical factor, not architectural gating: H3 with S4 gets 57.0% while No-gate with S6 gets 97.0% (controlled ablation, strong evidence).

**Induction Heads** (Table 2/Table 11, Section 4.1.2): Mamba generalizes perfectly to 2^20 = 1,048,576 tokens (trained on 256 tokens) -- a **4000x length extrapolation**. All attention variants (MHA-Abs, MHA-RoPE, MHA-xPos) fail beyond ~2x training length and go OOM beyond 2^14 = 16384. H3 and Hyena also fail to extrapolate (single synthetic task; limited evidence for generalization to natural language ICL).

#### DNA Modeling

**Model size scaling** (Figure 5 Left, Section 4.3.1): At context length 1024, Mamba scales better than both HyenaDNA and Transformer++ from ~200K to ~40M parameters. At ~40M parameters, **Mamba matches Transformer++ and HyenaDNA with roughly 3-4x fewer parameters** (10K gradient steps, 10B tokens, single run per configuration -- limited evidence).

**Context length scaling** (Figure 5 Right, Section 4.3.2): At fixed 1.4M parameters, Mamba perplexity monotonically improves from context 1K to 1M. HyenaDNA perplexity initially improves but then degrades at longer contexts -- consistent with the hypothesis that LTI models cannot selectively filter irrelevant context (20K gradient steps, ~330B tokens, single run per length -- moderate evidence).

**Great Apes species classification** (Table 13, Figure 6, Section 4.3.3):

| Model | Params | 2^10 | 2^14 | 2^18 | 2^20 |
|-------|--------|------|------|------|------|
| HyenaDNA | 1.4M | 28.04 | 41.17 | 31.10 | 54.87 |
| Mamba | 1.4M | 31.47 | 27.66 | 42.41 | **71.67** |
| Mamba | 7M | 30.00 | 31.48 | 56.60 | **81.31** |

*(Random baseline is 20%. Task classifies 5 great apes species sharing 99% DNA.)*

At the longest context of 1M tokens, Mamba-7M achieves 81.31% accuracy while HyenaDNA reaches only 54.87% (single run at 2^20 length -- limited evidence at longest context, but consistent trend across multiple lengths).

#### Audio Modeling

**YouTubeMix pretraining** (Figure 7, Section 4.4.1): Both Mamba and SaShiMi (S4+MLP) improve with longer context (8K to ~1M); **Mamba achieves lower bits-per-byte throughout, with the gap widening at longer lengths** (reaching ~1.300 BPB vs ~1.350 BPB at ~1M). This experiment used complex-valued SSMs -- the only experiment in the paper to do so (single model size of 3.5M params -- limited scale evidence).

**SC09 speech generation** (Table 4, Section 4.4.2):

| Model | Params | FID | IS | mIS | AM |
|-------|--------|-----|----|-----|----|
| WaveNet | 4.2M | 5.08 | 2.27 | 5.80 | 1.47 |
| SaShiMi | 5.8M | 1.99 | 5.13 | 42.57 | 0.74 |
| DiffWave + SaShiMi | 23.0M | 1.42 | 5.94 | 69.17 | 0.59 |
| **Mamba** | **6.1M** | **0.94** | **6.26** | **88.54** | **0.52** |
| **Mamba** | **24.3M** | **0.67** | **7.33** | **144.9** | **0.36** |

A small 6.1M Mamba model outperforms all baselines including much larger GAN- and diffusion-based models on all automated metrics. The larger 24.3M model further improves dramatically (strong evidence across 5 metrics, but automated metrics only -- no human evaluation).

**SC09 architecture ablation** (Table 5): In SaShiMi's U-Net backbone (8 outer + 8 center + 8 outer blocks at each of 3 stages), Mamba is consistently better than S4+MLP in the outer blocks, and Mamba > S4+MLP > MHA+MLP in the center blocks. The fully Mamba model achieves FID 0.94 vs 1.43 for the fully S4+MLP model (controlled ablation, strong evidence).

#### Efficiency Benchmarks

**Scan speed** (Figure 8 Left, Section 4.5): The fused selective scan is faster than FlashAttention-2 beyond sequence length 2K, and **up to 7x faster at 32K** (Appendix D). The fused scan is **20-40x faster** than a standard PyTorch scan implementation. All measurements on A100 80GB PCIe GPU with D=1024, N=16, BF16 (Appendix E.5).

**Inference throughput** (Figure 8 Right): Mamba achieves **4-5x higher throughput** than Transformers of similar size because no KV cache is needed, allowing much higher batch sizes. A Mamba-6.9B (untrained) achieves higher inference throughput than a Transformer-1.3B at most batch sizes (prompt length 2048, generation length 128, A100 80GB).

**Memory** (Table 15, Appendix E.5):

| Batch size | Transformer (FlashAttention-2) | Mamba |
|------------|-------------------------------|-------|
| 1 | 4.6 GB | 4.8 GB |
| 8 | 11.5 GB | 12.3 GB |
| 32 | 34.5 GB | 38.2 GB |

Mamba's training memory is comparable to an optimized Transformer, with Mamba slightly higher due to the expanded state dimension (125M models, sequence length 2048).

#### Ablation Studies

**Architecture ablation** (Table 6, Section 4.6.1): At ~350M parameters on the Pile:
- Among LTI SSMs (Hyena, S4 complex, S4 real), performance is nearly identical (~10.24-10.56 ppl).
- Replacing any LTI SSM with selective S6 dramatically improves performance: H3+S6 achieves 8.95 ppl, Mamba+S6 achieves **8.69 ppl** (vs ~10.3 for LTI variants).
- Real-valued SSMs perform similarly to complex-valued for language modeling (S4 real 10.34 vs S4 complex 10.30).

**Selective parameter ablation** (Table 7, Section 4.6.2):

| Selective Delta | Selective B | Selective C | Perplexity |
|-----------------|-------------|-------------|------------|
| no | no | no | 10.93 |
| no | yes | no | 10.15 |
| no | no | yes | 9.98 |
| yes | no | no | 9.81 |
| yes | yes | yes | 8.71 |

**Delta is the most important** selective parameter (9.81 vs 10.93 baseline), consistent with its connection to RNN gating (Theorem 1). All three parameters together synergize to achieve 8.71 (controlled ablation on ~350M model, strong evidence).

**Initialization** (Table 8): Real-valued S4D-Real initialization (A_n = -(n+1), ppl 8.71) matches random initialization and outperforms complex-valued S4D-Lin (A_n = -1/2 + ni, ppl 9.16).

**State dimension** (Table 10): Increasing N from 1 to 16 with selective B/C improves perplexity from 9.73 to 8.71 (a **1.02 improvement for only 1% additional parameters**). With constant B/C, the same increase yields only 0.07 improvement (9.88 to 9.81). This validates that state expansion is only beneficial when B/C are selective, confirming the core motivation (Section 3.1, 3.3).

**Hybrid architectures** (Figure 9, Appendix E.2.2): Interleaving Mamba blocks with MLP blocks (Mamba-MLP) performs only slightly worse than homogeneous Mamba. Interleaving with MHA blocks (Mamba-MHA) performs only slightly better, which is somewhat surprising given prior work showing LTI SSM + attention hybrids yield substantial improvements.

---

## Limitations and Failure Modes

### Acknowledged Limitations

1. **Scale.** Experiments limited to <=3B parameters. The authors explicitly note that RWKV and RetNet have been evaluated at 7B+, but it remains unknown whether Mamba's advantages hold at larger scales (Section 5).

2. **Continuous-discrete modality tradeoff.** The selection mechanism helps discrete data (text, DNA) but can hurt continuous signals. Audio ablations (Figure 10, Appendix E.4) show that S4+MLP (LTI) outperforms Mamba (S6) on long-form audio waveform pretraining when used in homogeneous models. The effect diminishes when only the inner U-Net blocks are ablated, suggesting layers close to raw continuous signals benefit from LTI while "tokenized" representations benefit from selection (Section 5).

3. **Downstream affordances unknown.** The authors acknowledge uncertainty about whether Mamba supports the same fine-tuning, prompting, RLHF, instruction tuning, and quantization patterns as Transformers (Section 5).

### Inferred Limitations

- **[Inferred]** No evaluation on non-English languages, limiting generalizability of language modeling claims.
- **[Inferred]** No evaluation on tasks requiring explicit multi-hop reasoning, retrieval, or long-form generation.
- **[Inferred]** No variance estimates or confidence intervals reported for any experiment; all results appear to be single runs.
- **[Inferred]** The downstream evaluation uses only commonsense reasoning benchmarks (LAMBADA, HellaSwag, PIQA, ARC, WinoGrande); no evaluation on knowledge-intensive tasks (MMLU), math, or code generation.
- **[Inferred]** RWKV trained with context length 1024 vs Mamba's 2048, which may disadvantage RWKV in comparisons.

### Scope and Comparability

**What was not tested:**
- Models larger than 3B parameters
- Instruction tuning, RLHF, or chat applications
- Tasks requiring explicit retrieval, multi-hop reasoning, or long-form generation
- Comparison with sparse attention variants (Longformer, BigBird) at long context
- Non-English language evaluation
- Knowledge-intensive benchmarks (MMLU, ARC-Challenge in extended evaluation)

**Comparability notes:**
- All language models trained on same data (Pile, 300B tokens) with same tokenizer (GPT-NeoX), making the Pythia/RWKV comparison well-controlled.
- Transformer++ baseline uses the modern LLaMA recipe (RoPE, SwiGLU, RMSNorm) -- this is a strong comparison, not a straw-man vanilla Transformer.
- RWKV was trained with context length 1024 vs Mamba's 2048, which may partially explain Mamba's advantage.
- RetNet was trained with the improved recipe; RWKV used its own specified recipe with 2-3x learning rates on certain parameters (Appendix E.2.1).
- DNA and audio experiments use much smaller models (1.4M-40M params) than the language experiments, so cross-domain scaling conclusions are speculative.

---

## Conclusions

### Contributions

1. **Selection mechanism for SSMs.** Introduced input-dependent parameterization of state space model parameters (Delta, B, C), enabling content-aware reasoning while maintaining linear complexity. Formally connected this to classical RNN gating through principled discretization (Theorem 1) (Section 3.2, 3.5).

2. **Hardware-aware selective scan.** Designed a fused CUDA kernel that exploits GPU memory hierarchy (HBM/SRAM), achieving 20-40x speedup over naive scan and matching FlashAttention memory efficiency at ~16 bytes per token (Section 3.3, Appendix D).

3. **First linear-time model matching Transformer quality.** Demonstrated that Mamba matches Transformer++ on language modeling scaling laws from 125M to 1.3B parameters, and matches downstream zero-shot performance at 2x model size across 6 benchmarks (Section 4.2).

4. **State-of-the-art on DNA and audio.** Achieved best results on HG38 genomics pretraining (with improving performance up to 1M context), Great Apes species classification (81.31% at 1M context), and SC09 speech generation (FID 0.67, more than halving SaShiMi's FID of 1.99) (Sections 4.3, 4.4).

5. **Comprehensive ablation analysis.** Isolated the contributions of selection (Delta most important), state dimension expansion (1.02 ppl improvement from N=1 to N=16 only with selective B/C), architecture (Mamba vs H3 similar), and initialization (real-valued sufficient for language) (Section 4.6).

### Implications

1. **Attention may not be necessary for language modeling.** Mamba achieves Transformer-quality performance without attention, suggesting the architectural dominance of Transformers may be contingent rather than fundamental (speculative at >3B scale).

2. **Selection is the critical capability.** The dramatic gap between LTI and selective SSMs on synthetic tasks (18.3% vs 97.0% on selective copying), combined with ablations showing Delta selectivity as the dominant factor, suggests that content-aware selection -- not convolution or recurrence per se -- is the key capability for discrete-data modeling.

3. **Linear-time long context is achievable with quality gains.** Unlike sparse attention approximations, Mamba truly scales linearly while actually improving quality with longer context (demonstrated up to 1M tokens on DNA and audio), enabled by the selection mechanism's ability to filter irrelevant context.

4. **Inference efficiency implications for deployment.** Eliminating the KV cache enables much higher batch sizes and 4-5x throughput at inference time, with potential implications for deployment costs (though this is measured on a single GPU type).

---

## Key Claims

1. **C1:** Mamba achieves 4-5x higher inference throughput than Transformers of similar size (Figure 8, Section 4.5). **Supported** by controlled benchmarks on A100 80GB GPU measuring tokens/second at batch sizes 1-128 with prompt length 2048. Mamba-6.9B exceeds throughput of Transformer-1.3B at most batch sizes. Single GPU type tested (limited generalization evidence).

2. **C2:** Mamba-3B matches Transformer quality at twice the model size (Table 3, Section 4.2.2). **Supported** by zero-shot evaluation across 6 commonsense reasoning benchmarks: Mamba-2.8B averages 63.3% vs Pythia-2.8B at 59.1% and GPT-J-6B at 63.0%. All compared models trained on the Pile with 300B tokens (strong evidence: 6 benchmarks, controlled data).

3. **C3:** Mamba is the first linear-time model matching Transformer++ on scaling laws (Figure 4, Section 4.2.1). **Supported** by perplexity curves from 125M to 1.3B parameters at 2K and 8K context lengths. Mamba tracks Transformer++ closely at 2K and slightly outperforms at 8K. All other subquadratic models fall below (moderate evidence: 4 model sizes, single run per configuration).

4. **C4:** Selection enables content-aware reasoning that LTI models cannot perform (Table 1, Table 2, Section 4.1). **Supported** by controlled ablations: S6 solves selective copying (97.0%) while S4 fails (18.3%); the architectural gating of H3 provides only partial improvement (57.0%) without selection (strong evidence: controlled ablation isolating selection vs architecture).

5. **C5:** Mamba extrapolates to 1M+ tokens while attention fails beyond training length (Table 2, Table 11, Section 4.1.2). **Supported** by induction heads evaluation at powers of 2 from 64 to 1M tokens, with training on 256 tokens. All attention variants (MHA-Abs, MHA-RoPE, MHA-xPos) fail beyond ~512 tokens and go OOM beyond 16K (single synthetic task with 2-layer models -- limited evidence for generalization to natural settings).

6. **C6:** Performance improves with context up to 1M tokens on DNA and audio (Figure 5 Right, Figure 7, Sections 4.3.2, 4.4). **Supported** by perplexity/BPB curves on HG38 and YouTubeMix, controlling for total compute per batch. HyenaDNA degrades at long context while Mamba continues to improve (single model size per domain -- limited scale evidence, but consistent across two modalities).

7. **C7:** Delta is the most important selective parameter due to its connection to RNN gating (Table 7, Theorem 1, Section 4.6.2). **Supported** by controlled ablation at ~350M scale: selective Delta alone (9.81 ppl) provides more benefit than selective B (10.15) or selective C (9.98) from a 10.93 baseline. Formal connection to gating established by Theorem 1 (single model size -- moderate evidence).

8. **C8:** Increasing SSM state dimension N dramatically improves performance only when B and C are selective (Table 10, Section 4.6.2). **Supported** by controlled ablation: selective B/C with N=16 gives 8.71 vs 9.73 at N=1 (1.02 improvement); constant B/C gives only 0.07 improvement across the same range. Only 1% additional parameters for N=16 vs N=1 (single model size -- moderate evidence, but clean ablation design).

9. **C9:** Selection mechanism hurts performance on continuous-signal modalities (Figure 10, Section 5, Appendix E.4). **Supported** by audio ablation: S4+MLP outperforms Mamba (S6) on long-form audio waveform pretraining with homogeneous models. Effect diminishes in inner U-Net blocks where the signal is already compressed. Consistent with the LTI inductive bias being beneficial for continuous data (single dataset and model size -- limited evidence).

---

## Open Questions

1. **Does Mamba scale to 7B+ parameters?** The paper only evaluates up to 3B. RWKV and RetNet have been evaluated at 7B. It remains unknown whether Mamba's advantages persist at larger scales, and the authors note that scaling may require additional engineering. Not yet addressed in the references directory.

2. **Can selective SSMs match Transformer in-context learning on complex tasks?** While Mamba solves synthetic induction heads, more complex ICL tasks (e.g., multi-step reasoning, task learning from demonstrations) may require attention-like mechanisms. Not yet addressed.

3. **Do Mamba models support standard fine-tuning affordances?** The ecosystem of Transformer fine-tuning (LoRA, PEFT, RLHF, quantization, instruction tuning) may not transfer directly to SSM architectures. Not yet addressed.

4. **How do hybrid Mamba-attention architectures compare at scale?** The paper briefly shows Mamba-MHA is only slightly better than pure Mamba at <=1.3B scale (Figure 9), but hybrid architectures may become more important at larger scales. Partially addressed by Gated Delta Networks (2025-04-gated-delta-networks), which combine linear recurrence with sliding window attention.

5. **Is the continuous-discrete spectrum a fundamental tradeoff?** The selection mechanism helps discrete data but hurts continuous audio. Can a single model or training recipe handle both modality types without sacrificing performance on either? Not yet addressed.

---

## Core References and Why They Are Referenced

### State Space Model Foundations

- **Gu et al. (2022)** -- *S4: Efficiently Modeling Long Sequences with Structured State Spaces.* Foundation work introducing structured state space models with efficient convolutional computation; Mamba's S6 is a direct extension of S4 with input-dependent parameterization.

- **Gu et al. (2022)** -- *S4D: On the Parameterization and Initialization of Diagonal State Space Models.* Showed diagonal SSMs match structured SSMs, providing the S4D-Real and S4D-Lin initializations used in Mamba's ablations.

- **Smith et al. (2023)** -- *S5: Simplified State Space Layers for Sequence Modeling.* First to use parallel scan for SSM computation, but with reduced state dimension (MIMO formulation); Mamba keeps SISO dimensions for larger effective state.

- **Gu et al. (2020)** -- *HIPPO: Recurrent Memory with Optimal Polynomial Projections.* Provides the theoretical foundation for SSM initialization and connections between discretization and gating.

### SSM Architectures

- **Dao et al. (2023)** -- *H3: Hungry Hungry Hippos.* Combined S4 with linear attention in a gated architecture, establishing the block structure that Mamba simplifies into a single homogeneous block.

- **Poli et al. (2023)** -- *Hyena Hierarchy.* Replaced S4 with MLP-parameterized global convolutions; serves as a key baseline showing architecture matters beyond the SSM layer.

- **Ma et al. (2023)** -- *Mega: Moving Average Equipped Gated Attention.* First to show real-valued SSMs (as EMA) are effective, supporting Mamba's default real-valued parameterization.

### Concurrent Subquadratic Models

- **Peng et al. (2023)** -- *RWKV: Reinventing RNNs for the Transformer Era.* Concurrent linear-time language model using LTI recurrence with channel-wise time decay; serves as a primary baseline in downstream evaluation.

- **Sun et al. (2023)** -- *RetNet: Retentive Network.* Concurrent Transformer alternative using fixed exponential decay with parallel computation via multi-head retention; serves as a scaling law baseline.

### Transformer Baselines

- **Touvron et al. (2023)** -- *LLaMA.* Established the Transformer++ recipe (RoPE, SwiGLU, RMSNorm) that serves as the strongest baseline Mamba matches in scaling laws.

- **Biderman et al. (2023)** -- *Pythia.* Provides controlled baselines trained on identical data (Pile, 300B tokens, GPT-NeoX tokenizer) for fair downstream comparison.

### Efficiency

- **Dao et al. (2022)** -- *FlashAttention.* Hardware-aware attention algorithm exploiting memory hierarchy; Mamba's scan algorithm uses analogous techniques (kernel fusion, recomputation) and achieves similar memory efficiency.

### Synthetic Task Motivation

- **Olsson et al. (2022)** -- *In-context Learning and Induction Heads.* Identified induction heads as a key mechanism for in-context learning, motivating their use as a benchmark for the selection mechanism's associative recall capability.

### DNA and Audio Baselines

- **Nguyen et al. (2023)** -- *HyenaDNA: Long-range Genomic Sequence Modeling.* Primary DNA baseline; Mamba outperforms HyenaDNA on both pretraining and downstream classification, particularly at long context.

- **Goel et al. (2022)** -- *SaShiMi: It's Raw! Audio Generation with State-Space Models.* Provides the U-Net backbone architecture and training protocol for audio experiments; Mamba replaces S4+MLP blocks in this architecture.
