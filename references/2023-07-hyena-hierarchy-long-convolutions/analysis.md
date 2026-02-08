---
title: "Hyena Hierarchy: Towards Larger Convolutional Language Models"
authors: "Poli, Massaroli, Nguyen, Fu, Dao, Baccus, Bengio, Ermon, Ré"
year: 2023
venue: "ICML 2023"
paper_type: conference-paper
categories: ["architecture", "attention-efficiency", "state-space-models"]
scope: ["subquadratic attention replacement", "long convolutions", "data-controlled gating", "language modeling", "image classification"]
benchmarks_used: ["perplexity-wikitext103", "perplexity-pile", "perplexity-pg19", "superglue", "imagenet-1k", "lambada"]
models_introduced: ["hyena"]
models_evaluated: ["transformer-base", "gpt-2", "h3", "s4", "linear-transformer", "rwkv-169m"]
key_claims:
  - id: C1
    claim: "Hyena improves accuracy by more than 50 points over operators relying on state spaces and other implicit and explicit methods on associative recall at sequences of thousands to hundreds of thousands of tokens"
    evidence: "Table 4.2, Section 4.1"
    status: supported
    scope: "associative recall, vocabulary size 30, sequence lengths 30K-131K, 2-layer models, width 64"
    magnitude: "50+ percentage points over H3, GSS, AFT, RWKV; 100.0% vs 6.5% best alternative at 64K"
  - id: C2
    claim: "Hyena is the first attention-free architecture to match Transformer perplexity on WikiText-103 at the 125M parameter scale"
    evidence: "Table 4.3, Section 4.2"
    status: supported
    scope: "125M parameters, WikiText-103, GPT-2 tokenizer, same training conditions as Dao et al. (2022c) baselines"
    magnitude: "18.6 perplexity, identical to Transformer (18.6); previous best attention-free AFT-conv at 28.2"
  - id: C3
    claim: "Hyena matches GPT perplexity on The Pile with a 20% reduction in total FLOPs at the 355M parameter scale"
    evidence: "Table 4.4, Figure 4.2, Section 4.2"
    status: supported
    scope: "355M parameters, 15B training tokens, GPT-2 tokenizer, sequence length 2048"
    magnitude: "17.6% FLOP reduction (3.93 vs 4.77 x 10^19); perplexity 9.2 vs 9.1 (GPT slightly better)"
  - id: C4
    claim: "Hyena operators are 100x faster than optimized attention at sequence length 64K"
    evidence: "Figure 4.3, Section 4.4"
    status: supported
    scope: "batch size 64, operator-level benchmark, fused FFTConv CUDA kernel, order-2 Hyena"
    magnitude: "100x speedup at 64K; 2x over FlashAttention at 8K; crossover with FlashAttention between 4K-8K"
  - id: C5
    claim: "Hyena matches ViT accuracy on ImageNet-1k when used as a drop-in replacement for attention"
    evidence: "Table 4.7, Section 4.5"
    status: supported
    scope: "87-88M parameters, 16x16 and 8x8 patches, ImageNet-1k, single model size"
    magnitude: "78.5% vs 78.5% (16x16); 79.8% vs 80.0% (8x8)"
  - id: C6
    claim: "Hyena is the only attention-free operator able to solve associative recall on long sequences, where all other subquadratic operators fail"
    evidence: "Table 4.2, Section 4.1"
    status: supported
    scope: "2-layer models, width 64, vocabulary size 30, sequence lengths 30K-131K"
    magnitude: "97.2% at 131K vs next-best CKConv 14.3% (Table A.2); all other operators below 12.4% at 30K"
  - id: C7
    claim: "Implicit filter parameterizations (Hyena, CKConv) outperform SSM-based, frequency-domain, and explicit parameterizations on associative recall, with the gap widening at longer sequences and larger vocabularies"
    evidence: "Figure 4.1, Table A.2, Section 4.1"
    status: supported
    scope: "order-2 Hyena, 2-layer models, vocabulary sizes 10-40, sequence lengths 128-131K"
    magnitude: "97.2% vs 14.3% (CKConv) vs 0.6% (H3) vs 0.3% (FNO) at 131K, vocab 30"
  - id: C8
    claim: "Hyena matches GPTNeo on SuperGLUE few-shot despite training on less than half the tokens"
    evidence: "Table 4.6, Section 4.3"
    status: supported
    scope: "153M Hyena (137B tokens) vs GPTNeo 125M (300B tokens), SuperGLUE 3-shot"
    magnitude: "49.3 vs 49.1 average; Hyena outperforms RWKV (43.0) by 6.3 points"
  - id: C9
    claim: "Rankings on synthetic mechanistic benchmarks correlate with language modeling performance at scale"
    evidence: "Table C.1, Appendix C"
    status: supported
    scope: "associative recall at fixed seq len 2048, vocab sizes 10-40, correlated with Pile loss at 5B tokens"
    magnitude: "qualitative correlation: Hyena matches Transformer on both recall (100/100/98/85) and Pile loss (2.59 vs 2.59)"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: complementary
    detail: "Hyena proposes a subquadratic drop-in replacement for the attention operator in Transformers, matching quality at sub-billion scale"
  - target: 2022-04-s4-structured-state-spaces
    type: extends
    detail: "Hyena generalizes S4's long convolution approach by replacing SSM-parameterized filters with FFN-based implicit convolutions and adding data-controlled gating"
  - target: 2022-12-flashattention
    type: complementary
    detail: "Hyena benchmarks runtime against FlashAttention, achieving crossover at 4K-8K sequence length and 100x speedup at 64K"
  - target: 2022-03-in-context-learning-induction-heads
    type: extends
    detail: "Hyena extends the mechanistic interpretability benchmark suite (associative recall, induction) to longer sequences and larger vocabularies to probe subquadratic operators"
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: concurrent
    detail: "RWKV is evaluated alongside Hyena on associative recall and SuperGLUE; Hyena significantly outperforms RWKV on recall tasks"
  - target: 2024-05-mamba-selective-state-spaces
    type: extended-by
    detail: "Mamba builds on Hyena and H3, replacing implicit long convolutions with input-dependent selective state spaces for content-aware reasoning"
open_questions:
  - question: "Can Hyena scale to multi-billion parameter models while maintaining the quality gap closure with Transformers?"
    addressed_by: null
  - question: "Can hardware utilization of FFT-based convolutions be improved to match attention's GPU efficiency?"
    addressed_by: null
  - question: "Do Hyena's advantages extend to tasks requiring complex multi-step reasoning beyond associative recall?"
    addressed_by: null
  - question: "Would hybridizing Hyena with attention layers (as done with H3) improve downstream performance at shorter context lengths?"
    addressed_by: null
  - question: "Can the correlation between synthetic mechanistic benchmarks and language modeling performance be formalized into predictive scaling laws?"
    addressed_by: null
---

# Hyena Hierarchy: Towards Larger Convolutional Language Models

**Authors:** Michael Poli*, Stefano Massaroli*, Eric Nguyen*, Daniel Y. Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, Christopher Re (Stanford University; Mila and Universite de Montreal)
**Date:** July 2023, ICML 2023 (Oral), arXiv:2302.10866

---

## Core Research Problem

The attention operator at the heart of Transformers scales quadratically with sequence length L, placing a strict upper bound on the amount of context a model can process. Existing subquadratic alternatives -- linearized attention (Katharopoulos et al., 2020), sparse approximations (Child et al., 2019; Kitaev et al., 2020), low-rank methods (Wang et al., 2020), and state-space models (Gu et al., 2022; Dao et al., 2022c) -- consistently underperform dense attention on language tasks, requiring **hybridization with standard attention layers** to reach Transformer quality (Mehta et al., 2022; Dao et al., 2022c).

The authors identify three computational properties of attention that correlate with its quality advantage and are absent from existing subquadratic operators:

1. **Data control:** Attention implements a data-controlled dense linear operator A(u), parameterizing an entire family of linear functions conditioned on the input. Self-attention can be expressed as y = A(k, q)v where A is the attention matrix conditioned by linear projections k, q of the input (Section 2.2).
2. **Sublinear parameter scaling:** Parameter counts are decoupled from sequence length, allowing allocation of parameters to FFN layers (Remark 2.1).
3. **Unrestricted context:** Attention can approximate dependencies between any two positions without locality restrictions.

Evidence from mechanistic interpretability research (Olsson et al., 2022) suggests that attention mechanisms only utilize a small portion of their quadratic capabilities for language processing, leading to the core question: **whether subquadratic operators can match the quality of attention at scale by intentionally incorporating these three properties.**

---

## Problem Solutions

Hyena is a class of data-controlled operators constructed from a recurrence of two efficient subquadratic primitives:

1. **Long convolutions** with implicitly parameterized filters (via a feed-forward network), providing unrestricted context and sublinear parameter scaling.
2. **Element-wise multiplicative gating** of input projections, providing data control.

The depth (order N) of the recurrence controls the operator's expressivity. For short recurrences, existing models are recovered as special cases: H3 corresponds to Hyena_2 and GSS to Hyena_1 with SSM-parameterized filters (Remark 3.2). Hyena generalizes to arbitrary order N with free-form implicit filters. The key insight is that the interleaving of convolutions and element-wise products operates alternately in the time and frequency domains: convolution in the time domain increases memory length, while element-wise multiplication in the time domain (convolution in the frequency domain) allows fine-grained selection of specific frequency components (Section 3.1).

---

## Approach Details

### Method

#### Hyena Operator Definition

Given N+1 linear projections of the input (v, x^1, ..., x^N) and N learnable filters h^1, ..., h^N, the order-N Hyena operator is defined by the recurrence (Definition 3.1):

> z^1_t = v_t
> z^{n+1}_t = x^n_t * (h^n * z^n)_t,  for n = 1, ..., N
> y_t = z^{N+1}_t

where * denotes (causal) convolution and the centered dot denotes element-wise multiplication.

**Time complexity:** O(NL log_2 L) per Remark 3.1, since each of the N convolutions is performed in the Fourier domain via FFT. The full computational complexity including all operations is given by Proposition 3.2:

> O(NDL(log_2 L + D))

where D is the model width, accounting for projections, short convolutions, FFTConv, and output projection.

#### Matrix Form

The Hyena recurrence can be equivalently expressed as a data-controlled matrix decomposition. Let D^n_x = diag(x^n) be L-by-L diagonal matrices and S^n_h be Toeplitz matrices corresponding to filter h^n. Then:

> y = H(u)v = D^N_x S^N_h ... D^2_x S^2_h D^1_x S^1_h v

This decomposition reveals that Hyena implicitly defines a data-controlled matrix H(u) analogous to the attention matrix A(q,k), but evaluated efficiently without materialization. The connection to fast evaluation algorithms for structured dense matrices based on **butterfly decompositions** (Li et al., 2015; Dao et al., 2019, 2022a) is explicit: the Hyena operator blends data control with a special case of butterfly decomposition, with length of the decomposition closely tied to expressivity (Section 3.2).

#### Hyena Filters (Implicit Parameterization)

Each filter h^n is represented as a map from time (or position) t to filter values, learned with a shallow feed-forward neural network (Equation 7):

> h_t = Window(t) * (FFN o PositionalEncoding)(t)

where Window(t) = exp{-alpha * t} is an exponential decay with learnable rate alpha that varies across channels. The FFN uses **sine activations** (high-frequency periodic functions) to address the low-frequency bias of neural networks (Basri et al., 2020). The positional encoding maps scalar t to a higher-dimensional representation using a truncated complex exponential basis (Appendix D.3):

> PositionalEncoding(t) = [t, Re[rho_0](t), ..., Re[rho_{K-1}](t), Im[rho_0](t), ..., Im[rho_{K-1}](t)]

where rho_k(t) = e^{i*2*pi*k*t/L} for k = 0, ..., K-1, giving D_e = 2K + 1 features. The number of positional encoding features K induces a bias in modeled frequencies at initialization, with filters resembling low-pass filters with cut-off frequency approximately 2K + 1 (Appendix D.3). Rather than increasing K (which increases parameter count), the authors increase the frequency omega_a of the sinusoidal activation to achieve full spectral coverage efficiently: with K = 8 and omega_a = 10, the filters cover the full spectrum (Figure D.9).

This implicit parameterization decouples the filter length from the parameter count: the FFN has a fixed number of parameters regardless of sequence length L.

### Key Technical Components

#### Projection Layer (Algorithm 1)

1. Input u in R^{L x D} is linearly projected to (N+1)D dimensions.
2. A short depthwise convolution (filter size 3) is applied.
3. Output is split into N+1 projections: x^1, ..., x^N, v in R^{D x L}.

#### Filter Generation (Algorithm 2)

1. Positional encoding maps positions 0, ..., L-1 to R^{L x D_e}.
2. FFN (depth 4, width 64, sine activations) maps to filter values.
3. Multiply by exponential decay window.
4. Split into N filters h^1, ..., h^N.

#### Causality

Causal convolutions are guaranteed by evaluating filters only at non-negative positions t = 0, ..., L-1 and zero-padding before FFT (Proposition 3.1). The proof follows from the fact that the Hyena operator H is a product of alternating diagonal and Toeplitz matrices; if all Toeplitz matrices S^n_h are lower triangular (causal filters), then H is lower triangular (Appendix B.1).

#### Architecture Configurations

| Size | Depth | Width | FFN Width | Filter FFN Width | Filter FFN Depth | Sine Freq |
|---|---|---|---|---|---|---|
| 125M | 12 | 768 | 3072 | 64 | 4 | 14 |
| 125M-slim | 18 | 768 | 1536 | 64 | 4 | 14 |
| 153M | 18 | 864 | 1728 | 64 | 4 | 14 |
| 355M | 36 | 1024 | 2048 | 64 | 4 | 14 |
| 1.3B | 36 | 2048 | 4096 | 64 | 4 | 14 |

*Table A.4. All models use order 2 Hyena with filter FFN width 64 and depth 4. Deeper and thinner models (slim) achieve lower perplexity by trading width for depth, enabled by the FLOP reduction from replacing attention.*

#### FLOP Computation

FLOPs are computed using the strategy from Hoffmann et al. (2022). For Hyena, attention layers are replaced by (Appendix A.2): (i) Projections: order x d_model x d_model x seq_len; (ii) Short conv on projections: order x d_model x seq_len x filter_len; (iii) FFTConv: 5 x (order - 1) x d_model x log(seq_len) x seq_len; (iv) Output: d_model x d_model x seq_len. A leading factor of 2 accounts for additions and multiplications.

### Theoretical Analysis

#### Surrogate Attention Matrix (Appendix B.2)

For Hyena-2 (the H3 mechanism), the data-controlled operator can be decomposed to isolate a surrogate attention matrix. Given q, k, v projections and filters phi, psi:

> z_t = k_t (phi * v)_t
> y_t = q_t (psi * z)_t

The surrogate attention matrix A^psi_phi(q, k) is defined such that y = A^psi_phi(q, k) v, with entries:

> [A^psi_phi(q, k)]_{t,t'} = q_t sum_{m=0}^{L-1} psi_{t-m} k_m phi_{m-t'}

This matrix admits the operator decomposition (Equation 18):

> A^psi_phi(q, k) = D_q S_psi D_k S_phi

where D_q, D_k are diagonal matrices and S_psi, S_phi are lower-triangular causal Toeplitz matrices. This decomposition allows evaluation in O(L log L) time via two FFT convolutions and two element-wise products.

#### Fourier Decomposition and Non-Commutativity (Appendix B.2)

The convolution operators can be diagonalized by the Fourier transform:

> S_psi = W* D_Psi W,  S_phi = W* D_Phi W

Substituting into the surrogate attention matrix:

> A = D_q W* D_Psi W D_k W* D_Phi W

The critical insight is the **non-commutativity** of D_q and D_k with W*. If these operators commuted, the entire layer would reduce to a simple convolution (Equation 22). The non-commutativity of the gating term acts as a nonlinearity in the chain of convolution operators, which is essential for the expressivity of the Hyena operator (Appendix B.2).

#### Continuous Signal Extension

The analysis extends to continuous signals on a group G, where the surrogate attention kernel is:

> K(t, t') = q_t integral_G psi_{t-g} k_g phi_{g-t'} dg

This provides a theoretical foundation for the operator decomposition in the continuous domain (Equations 13-15).

### Experimental Setup

**Mechanistic design benchmarks (Section 4.1):** Synthetic tasks inspired by mechanistic interpretability research (Elhage et al., 2021; Olsson et al., 2022): associative recall, majority voting, counting, ICL of linear functions, arithmetic. 2-layer models, width 64, trained for 200 epochs with AdamW (lr=0.0005, weight decay 0.1, cosine schedule, batch size 32, 2000 samples). Sequence lengths from 1024 to 131,136; vocabulary sizes 10, 20, 30, 40.

**WikiText-103 (Section 4.2):** 125M parameter models with GPT-2 tokenizer (vocab 50,257). Order-3 Hyena with implicit filters for two long convolutions and a short explicit convolution on the third. Baselines from Dao et al. (2022c) trained under identical conditions.

**The Pile (Section 4.2):** 125M and 355M models trained for 5, 10, 15 billion tokens using GPT-2 tokenizer, sequence length 2048, batch size 256, 8x A100 80GB GPUs. Optimizer: AdamW (beta_1=0.9, beta_2=0.98), peak lr 6x10^-4 (125M) / 4x10^-4 (355M), cosine schedule, weight decay 0.1. Preliminary 1.3B results at lr 2.2x10^-4. Order-2 Hyena used for Pile experiments.

**PG-19 (Appendix A.2):** 153M model trained for 8 epochs at context length 16K tokens on the PG-19 long-range corpus (Rae et al., 2019) with GPT-2 tokenizer.

**SuperGLUE (Section 4.3):** 153M Hyena trained for 137B tokens compared against GPTNeo (125M, 300B tokens) and RWKV-v4 (169M, 332B tokens). Zero-shot and 3-shot evaluation using parsing pipeline of Arora et al. (2022). For WIC, CB, and BoolQ, logit scoring is used instead of generation; other tasks use greedy decoding.

**LAMBADA (Appendix A.3):** Same 153M Hyena model. Stop word filter applied; check whether predictions for all tokens corresponding to the last word match ground truth.

**Runtime benchmarking (Section 4.4):** Operator-level comparison of order-2 Hyena vs attention and FlashAttention (Dao et al., 2022b). Batch size 64, fused FFTConv CUDA kernel.

**ImageNet-1k (Section 4.5):** Drop-in replacement of attention in ViT (87M) with Hyena operator (88M). Trained from scratch with T2T-ViT procedure (Yuan et al., 2021), 300 epochs, batch size 1024, 8x A100 GPUs. Augmentations: RandAugment, Mixup (0.8), CutMix (1.0), Random erasing (0.25), label smoothing (0.1), stochastic depth (0.1). ViT base lr 1e-3 vs Hyena-ViT lr 2e-4; ViT weight decay 0.05 vs Hyena-ViT 0.01.

**CIFAR-10 (Section 4.5, Appendix A.4):** Sequential CIFAR with same Hyena operator as language. 2D CIFAR with Hyena filters in both x and y dimensions, forgoing gating mechanism. Compared with S4ND (Nguyen et al., 2022) isometric model (4 residual blocks, width 128). 100 epochs, 0.1 dropout, 0.03 weight decay, Nvidia T4 GPU.

**Reproducibility:** Code released at https://github.com/HazyResearch/safari. All hyperparameters specified in Appendix A. Seeds not explicitly reported; single run per configuration (no variance reported).

### Key Results

#### Associative Recall (Table 4.2, Vocabulary Size 30)

| Sequence Length | Hyena | FlashTransformer | Transformer | GSS | H3 | AFT | RWKV |
|---|---|---|---|---|---|---|---|
| 30K | 100.0 | 32.4 | X | 5.3 | 8.4 | 2.3 | 12.4 |
| 64K | 100.0 | 26.7 | X | 2.1 | 4.3 | 1.2 | 6.5 |
| 131K | 97.2 | X | X | 0.1 | 0.6 | 0.8 | 2.3 |

- **Hyena is the only attention-free operator to solve associative recall** at long sequences (single configuration, no variance reported -- limited evidence for generalization)
- At 131K tokens, Hyena outperforms CKConv by 83 points (97.2 vs 14.3, Table A.2)
- Standard Transformer and FlashTransformer run out of memory at 64K+ and 131K+ respectively
- A single layer of Hyena (width 64) solves associative recall even at vocabulary size 40 (Appendix C), unlike Transformers which require 2 layers

#### Long Convolution Parameterization Comparison (Table A.2, 131K Tokens, Vocab 30)

| Hyena | CKConv | TransferFunc | H3 | FNO | Conv1d |
|---|---|---|---|---|---|
| 97.2 | 14.3 | 0.5 | 0.6 | 0.3 | 0.5 |

- Implicit FFN-based parameterizations (Hyena, CKConv) dramatically outperform SSM-based (H3), frequency-domain (FNO), and explicit (Conv1d) approaches
- Gap widens with increasing vocabulary size and sequence length (Figure 4.1, tested across 4 vocabulary sizes and 8 sequence lengths -- moderate evidence)

#### WikiText-103 Perplexity (125M Parameters, Table 4.3)

| Model | Perplexity |
|---|---|
| Transformer (125M) | 18.6 |
| Hybrid H3 (125M) | 18.5* |
| Performer (125M) | 26.8* |
| Reformer (125M) | 25.6* |
| AFT-conv (125M) | 28.2 |
| Linear Attention (125M) | 25.6* |
| **Hyena-3 (125M)** | **18.6** |
| Hyena-3-slim (125M) | 18.5 |

*\*Results from Dao et al. (2022c) under identical conditions. Hyena-3-slim is deeper (18 layers) and thinner (FFN width 1536 vs 3072).*

- Hyena matches Transformer perplexity **without any attention layers** (single model size, single dataset -- limited evidence for generalization to other scales)
- Previous best attention-free result was Hybrid H3, which still used one attention layer

#### The Pile Perplexity (Table 4.4)

| Model | 5B tokens | 10B tokens | 15B tokens | FLOPs (x10^19) |
|---|---|---|---|---|
| GPT (125M) | 13.3 | 11.9 | 11.2 | 1.88 |
| Hyena-2 (153M) | 13.3 | 11.8 | 11.1 | 1.87 |
| GPT (355M) | 11.4 | 9.8 | 9.1 | 4.77 |
| **Hyena-2 (355M)** | **11.3** | **9.8** | **9.2** | **3.93** |

- At 355M, Hyena matches GPT quality with **17.6% fewer FLOPs** (3.93 vs 4.77 x 10^19). Hyena perplexity at 15B tokens is 9.2 vs GPT's 9.1 -- close but not identical (2 model sizes, 3 data scales -- moderate evidence)
- Preliminary 1.3B results: 10.8 perplexity after 5B tokens
- 153M model trained for 130B tokens reaches 9.8 perplexity on The Pile

#### PG-19 Long-Range Benchmark (Appendix A.2)

- Hyena 153M trained at context length 16K tokens reaches **14.6 test perplexity** in 8 epochs (single model, single run -- limited evidence)

#### SuperGLUE Zero-Shot (Table 4.5)

| Model | WSC | WIC | RTE | CB | MultiRC | ReCoRD | BoolQ | COPA | Average |
|---|---|---|---|---|---|---|---|---|---|
| GPTNeo (300B tokens) | **27.9** | 50.0 | 45.1 | **41.1** | 0.0 | **61.7** | **62.2** | 62.0 | **43.8** |
| RWKV (332B tokens) | 13.4 | **52.3** | **46.9** | 25.0 | 0.0 | 58.5 | 59.2 | **66.0** | 40.2 |
| Hyena (137B tokens) | 21.2 | 50.5 | 46.6 | 39.3 | **1.1** | 59.4 | 51.8 | **70.0** | 41.5 |

#### SuperGLUE Few-Shot (3) (Table 4.6)

| Model | WSC | WIC | RTE | CB | MultiRC | ReCoRD | BoolQ | COPA | Average |
|---|---|---|---|---|---|---|---|---|---|
| GPTNeo (300B tokens) | 38.5 | **50.0** | **53.8** | **42.9** | **22.4** | **61.4** | **61.0** | 63.0 | **49.1** |
| RWKV (332B tokens) | 32.7 | 49.4 | 47.2 | 37.5 | 0.0 | 58.3 | 55.0 | **64.0** | 43.0 |
| **Hyena (137B tokens)** | **39.4** | **50.1** | 47.6 | **46.4** | **26.7** | 58.1 | **56.0** | **70.0** | **49.3** |

- Hyena matches GPTNeo (49.3 vs 49.1) **despite training on less than half the tokens** (137B vs 300B). Hyena outperforms RWKV by 6.3 points average (3 models compared -- limited evidence)
- Characteristic few-shot capabilities: MultiRC sees a lift of 25.6 points from zero-shot (1.1) to 3-shot (26.7), demonstrating that additional prompts help align Hyena's generation to the task format (Section 4.3)

#### LAMBADA (Appendix A.3)

- Small Hyena model (153M, 137B tokens) reaches **44.64% accuracy** on LAMBADA word prediction (single model, single evaluation -- limited evidence)

#### ImageNet-1k and CIFAR-10 Classification (Table 4.7)

| Model | Patch Size | Seq Len | Dataset | Acc (%) |
|---|---|---|---|---|
| ViT (87M) | 16x16 | 196 | ImageNet-1k | 78.5 |
| Hyena-ViT (88M) | 16x16 | 196 | ImageNet-1k | 78.5 |
| ViT (87M) | 8x8 | 1024 | ImageNet-1k | 80.0 |
| Hyena-ViT (88M) | 8x8 | 1024 | ImageNet-1k | 79.8 |
| S4ND-ISO (268k) | - | - | CIFAR-10 | 89.9 |
| Hyena-ISO (202k) | - | - | CIFAR-10 | 91.2 |

- Hyena matches ViT at both patch sizes as a **drop-in replacement** without architectural changes beyond removing class token and positional embeddings (single model size -- limited evidence)
- On CIFAR-10 2D, Hyena-ISO outperforms S4ND-ISO (91.2% vs 89.9%) with **25% fewer parameters** (202k vs 268k) and 8% speedup
- On sequential CIFAR, Hyena matches S4 accuracy (91%) at the same model size (Section 4.5)

#### Runtime Benchmarks (Figure 4.3)

- Hyena crossover with standard attention: ~2048 sequence length
- Hyena crossover with FlashAttention: between 4096 and 8192
- **100x speedup** over FlashAttention at 64K sequence length
- At 64K, standard attention runs out of memory in PyTorch
- Despite absolute FLOP reduction, speedups materialize only on longer sequences because hardware utilization of Hyena is lower than FlashAttention (operator-level benchmark only, not end-to-end training -- limited evidence for training speedups)

#### Synthetic-to-Scale Correlation (Table C.1)

| Model | Acc @ 10 | Acc @ 20 | Acc @ 30 | Acc @ 40 | Loss @ 5B on Pile |
|---|---|---|---|---|---|
| Conv1d | 32 | 11 | 10 | 8 | 4.21 |
| AFT-conv | 55 | 21 | 12 | 10 | 3.57 |
| H3 | 92 | 60 | 13 | 10 | 2.69 |
| Transformer | 100 | 100 | 92 | 82 | 2.59 |
| Hyena | 100 | 100 | 98 | 85 | 2.59 |

*Associative recall accuracy (%) at fixed seq len 2048, varying vocabulary sizes, vs test loss on The Pile at 5B tokens.*

- Rankings on synthetic tasks correlate with language modeling performance, suggesting mechanistic benchmarks may be predictive proxies for architecture design (5 models compared at fixed sequence length -- moderate evidence)

#### Arithmetic Learning (Appendix C.1)

- A single Hyena layer learns addition up to 4 digits. Longer numbers require deeper models: 2 layers handle 8 digits, 3 layers handle 16 digits (Figure C.1)
- Alternative architectures such as AFT-conv struggle to learn arithmetic, indicating a capability gap (qualitative observation, no formal ablation)

### Filter Visualization Insights (Appendix D)

- Hyena matrices visualized on test strings show **qualitatively similar patterns to attention matrices** (diagonal, vertical stripes, off-diagonal structure) without the attention mechanism (Figures D.1-D.4). Hyena produces a separate matrix per channel rather than per head.
- At convergence, Hyena learns lower-order filters with similar structure across layers, which could be exploited for post-training inference speedup (Figure D.5).
- Substantial performance difference (up to 5% perplexity) between initialization schemes: excessively smooth filters at initialization lead to worse solutions and slower convergence (Appendix D.2).
- Magnitude of Hyena matrices in pre-trained models is around 10^-3, with entries that can be positive or negative (unlike softmax-normalized attention) (Appendix D.1).

---

## Limitations and Failure Modes

### Acknowledged Limitations

1. **Sub-billion parameter scale.** All language modeling experiments are at <=355M parameters (with only preliminary 1.3B results at 10.8 perplexity after 5B tokens). Whether the quality gap closure with Transformers holds at larger scales is unknown (Section 5).

2. **Hardware utilization.** FFT-based long convolutions have lower GPU utilization than optimized attention kernels. Deep learning primitives like FFNs and attention usually reach 50-70% or higher utilization, while FFTConv is lower (Section 3.4, footnote 7). The speedup over FlashAttention materializes only at sequence lengths >=4K-8K. The authors expect this gap to shrink with improved FFTConv implementations and specialized hardware.

3. **Training hyperparameters.** Standard GPT training hyperparameters are used but acknowledged as likely suboptimal for Hyena. The authors find that slightly lower learning rates and modified warmup schedules improve Hyena convergence (Appendix A.2), but use standard GPT hyperparameters for fair comparison.

4. **Transformers may be better with limited data on recall.** Transformers solve associative recall easily even with limited training data at shorter sequences, while the experiments use a fixed small dataset of 2000 samples (Appendix A.1). This may explain why Transformers underperform Hyena on recall in these specific experimental conditions.

### Scope and Comparability

**What was not tested:**
- Models larger than 355M (1.3B is preliminary only, single data point)
- Instruction tuning, RLHF, or chat applications
- Tasks requiring complex multi-step reasoning beyond synthetic tasks
- **[Inferred]** Comparison with sparse attention methods (Longformer, BigBird) on long-context tasks
- **[Inferred]** Inference throughput (only operator-level runtime benchmarked, not end-to-end generation)
- **[Inferred]** Non-English languages
- **[Inferred]** Multiple runs with different seeds (no variance estimates reported)

**Comparability notes:**
- WikiText-103 baselines are from Dao et al. (2022c) under identical conditions
- On The Pile, GPT and Hyena use the same tokenizer (GPT-2) and training recipe, but Hyena models differ slightly in parameter count (153M Hyena vs 125M GPT)
- SuperGLUE comparison is unequal in training tokens: Hyena trained on 137B tokens vs GPTNeo on 300B and RWKV on 332B. Despite this disadvantage, Hyena matches GPTNeo
- Speed benchmarks measure operator-level runtime, not full model throughput; actual speedups in training depend on the fraction of compute in the attention replacement layer
- Hyena-ViT uses different learning rate (2e-4 vs 1e-3) and weight decay (0.01 vs 0.05) from ViT, which may confound the comparison

---

## Conclusions

### Contributions

1. **Hyena operator.** Introduced a subquadratic drop-in replacement for attention constructed from a recurrence of implicitly parameterized long convolutions and element-wise multiplicative gating. The operator achieves data control, sublinear parameter scaling, and unrestricted context -- three properties identified as key to attention's quality advantage.

2. **Implicit filter parameterization.** Demonstrated that FFN-based implicit convolution filters (with exponential decay windowing and sine activations) significantly outperform SSM-based (S4/H3), frequency-domain (FNO), transfer function, and explicit (Conv1d) parameterizations on associative recall, with the gap widening at longer sequences and larger vocabularies (Figure 4.1, Table A.2). At 131K tokens, Hyena achieves 97.2% vs CKConv 14.3% vs H3 0.6%.

3. **First purely attention-free architecture matching Transformer quality.** Hyena matches Transformer perplexity on WikiText-103 (18.6, Table 4.3) and The Pile with ~18% fewer FLOPs at 355M (Table 4.4), without hybridization with attention layers.

4. **Dominant performance on long-range associative recall.** Hyena is the only subquadratic operator to solve associative recall at 64K-131K tokens, outperforming H3, GSS, AFT, RWKV, and FlashTransformer by 50+ points (Table 4.2). Notably, a single Hyena layer solves recall at vocab size 40 (Appendix C).

5. **Generality beyond language.** Hyena matches ViT accuracy on ImageNet-1k as a drop-in replacement (Table 4.7) and outperforms S4ND on CIFAR-10 2D classification (91.2% vs 89.9%) with 25% fewer parameters.

6. **Theoretical analysis of data-controlled operators.** Provided a matrix decomposition framework (surrogate attention matrix) showing how Hyena's interleaving of Toeplitz and diagonal matrices produces data-controlled behavior, with the non-commutativity of gating acting as a nonlinearity essential for expressivity (Appendix B.2).

7. **Synthetic-to-scale correlation.** Demonstrated that rankings on mechanistic design benchmarks (associative recall at fixed length) correlate with language modeling performance on The Pile (Table C.1), suggesting fast synthetic-task evaluation may be predictive of architecture quality at scale.

### Implications

1. **Attention may not be necessary for quality.** (Inference) The results at sub-billion scale suggest that simpler, principled subquadratic designs can match attention quality without hybridization, but this has not been confirmed at larger scales.

2. **Mechanistic benchmarks as architecture design proxies.** (Inference) Rankings on synthetic tasks (associative recall, induction) correlate with perplexity rankings at fixed sequence length on The Pile (Table C.1), suggesting these benchmarks are useful proxies for architecture design. However, the correlation is demonstrated on only 5 operators at one sequence length -- further validation is needed.

3. **Implicit parameterizations scale better than explicit ones.** (Inference) The gap between implicit (Hyena, CKConv) and explicit (Conv1d, FNO) filter parameterizations widens with sequence length and vocabulary size, suggesting implicit methods are essential for long-context modeling.

4. **Filter initialization matters significantly.** (Inference) Up to 5% perplexity differences between initialization schemes (Appendix D.2) suggest that optimization landscape, not just architecture, plays a critical role in long convolution model quality.

---

## Key Claims

1. **C1: Hyena improves accuracy by 50+ points over SSM-based and other subquadratic operators on associative recall at long sequences.** Hyena achieves 100% at 64K while the best alternative (RWKV) achieves 6.5%. At 131K, Hyena achieves 97.2% vs 0.1-2.3% for all others. Evidence: Table 4.2. Status: **supported**. Scope: vocabulary size 30, 2-layer models, width 64. Single experimental configuration, no variance reported (limited evidence for generalization to other configurations).

2. **C2: Hyena matches Transformer perplexity on WikiText-103.** 18.6 perplexity for both Hyena-3 (125M) and Transformer (125M). Previous best attention-free model (AFT-conv) achieved 28.2. Evidence: Table 4.3. Status: **supported**. Scope: 125M parameters only, GPT-2 tokenizer; baselines from Dao et al. (2022c). Single model size (limited evidence for scale generalization).

3. **C3: Hyena matches GPT perplexity with ~18% fewer FLOPs at 355M.** At 15B training tokens, Hyena-355M reaches 9.2 perplexity with 3.93x10^19 FLOPs vs GPT-355M at 9.1 perplexity with 4.77x10^19 FLOPs. Evidence: Table 4.4, Figure 4.2. Status: **supported**. Scope: The Pile, GPT-2 tokenizer, sequence length 2048. Hyena perplexity is 9.2 vs GPT's 9.1 -- close but not identical. Two model sizes tested at three data scales (moderate evidence).

4. **C4: Hyena achieves 100x speedup over attention at 64K.** Measured at operator level with batch size 64 using fused FFTConv CUDA kernel. Crossover with FlashAttention occurs between 4K and 8K. Evidence: Figure 4.3. Status: **supported**. Scope: operator-level benchmark only; actual training speedups are smaller because non-attention FLOPs are unchanged and hardware utilization is lower (single hardware setup -- limited evidence for other configurations).

5. **C5: Hyena matches ViT on ImageNet-1k.** Hyena-ViT (88M) achieves 78.5% top-1 accuracy at 16x16 patches, identical to ViT (87M). At 8x8 patches (seq len 1024), Hyena achieves 79.8% vs ViT's 80.0%. Evidence: Table 4.7. Status: **supported**. Scope: single model size, different hyperparameters for Hyena-ViT vs ViT (limited evidence; no comparison at larger ViT scales).

6. **C6: Hyena is the only attention-free operator to solve long-range associative recall.** Among seven operators tested (Hyena, H3, GSS, AFT, RWKV, FlashTransformer, standard Transformer), only Hyena solves the task at 30K+ tokens. At 131K, Hyena (97.2%) outperforms next-best CKConv (14.3%) by 83 points (Table A.2). Evidence: Table 4.2, Table A.2. Status: **supported**. Scope: 2-layer models, fixed width 64, vocabulary size 30. Seven operators and six parameterizations compared (moderate evidence across alternatives).

7. **C7: Implicit filter parameterizations outperform SSM-based and explicit approaches.** Hyena (97.2%) and CKConv (14.3%) dramatically outperform H3 (0.6%), FNO (0.3%), and Conv1d (0.5%) at 131K tokens, vocab 30. The gap widens with sequence length and vocabulary size. Evidence: Figure 4.1, Table A.2. Status: **supported**. Scope: order-2 Hyena, 2-layer models. Tested across 4 vocabulary sizes and 8 sequence lengths (strong evidence for the trend within this setting).

8. **C8: Hyena matches GPTNeo on SuperGLUE few-shot with less than half the training tokens.** Hyena (153M, 137B tokens) achieves 49.3 average vs GPTNeo (125M, 300B tokens) at 49.1, and outperforms RWKV (169M, 332B tokens) at 43.0. Evidence: Table 4.6. Status: **supported**. Scope: 3 models of similar size, SuperGLUE 8 tasks, 3-shot evaluation. Models trained on different token counts, making the comparison not fully controlled (moderate evidence).

9. **C9: Synthetic mechanistic benchmark rankings correlate with language modeling performance.** Associative recall accuracy at vocab sizes 10-40 correlates with Pile loss at 5B tokens: Hyena and Transformer both reach loss 2.59 and score 100/100/98/85 and 100/100/92/82 on recall. Evidence: Table C.1. Status: **supported**. Scope: fixed seq len 2048, 5 operators, single correlation. Qualitative correlation without formal statistical test (limited evidence).

---

## Open Questions

1. **Does Hyena scale to multi-billion parameters?** The paper only provides preliminary 1.3B results (10.8 perplexity at 5B tokens). Whether the quality gap closure holds at GPT-3/LLaMA scale is unknown. **Partially addressed by** Mamba (Gu & Dao, 2024), which matches Transformer++ scaling at 130M-2.8B but uses selective SSMs rather than Hyena's implicit filters. **Unresolved for Hyena specifically.**

2. **Can FFT-based operations achieve attention-level hardware utilization?** The paper acknowledges that low GPU utilization of FFTConv is a bottleneck (Section 3.4, footnote 7: attention reaches 50-70% utilization). Improved implementations and specialized hardware could narrow this gap. **Unresolved.**

3. **Do Hyena's advantages extend to complex multi-step reasoning?** The synthetic benchmarks test recall, induction, and arithmetic, but more complex reasoning (multi-hop, chain-of-thought) is not evaluated. **Unresolved.**

4. **Would Hyena-attention hybrids outperform pure Hyena at shorter contexts?** The paper notes that at shorter training lengths (up to 8K), hybridization with attention (as in H3) may yield better downstream results (Appendix A.1). This suggests hybrid architectures may be optimal for shorter contexts. **Unresolved.**

5. **Can the synthetic-to-scale correlation be formalized into predictive scaling laws?** Table C.1 shows a correlation between associative recall accuracy and Pile loss for 5 operators, but this is qualitative. The authors speculate that "it may be possible to derive predictive laws for performance at scale, based on fast experimentation on synthetic tasks with models of 1 or 2 layers" (Appendix C). **Unresolved.**

---

## Core References and Why They Are Referenced

### Attention and Transformer Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the attention operator that Hyena aims to replace. Hyena's design is motivated by three identified properties of attention: data control, sublinear parameter scaling, and unrestricted context.

- **Olsson et al. (2022)** -- *In-Context Learning and Induction Heads.* Identifies induction heads and associative recall as key mechanisms for in-context learning in Transformers. Hyena's evaluation suite (Table 4.1) is grounded in this mechanistic interpretability work.

- **Elhage et al. (2021)** -- *A Mathematical Framework for Transformer Circuits.* Provides the circuits-based analysis framework motivating Hyena's synthetic benchmark design and the choice of 2-layer models for mechanistic analysis.

### State Space Models and Long Convolutions

- **Gu et al. (2021/2022)** -- *S4: Efficiently Modeling Long Sequences with Structured State Spaces.* Foundational SSM work establishing long convolutions as viable sequence modeling primitives. S4 is one of the long convolution parameterizations benchmarked against Hyena's implicit approach.

- **Dao et al. (2022c)** -- *H3: Hungry Hungry Hippos.* H3 combines SSM-based long convolutions with gating, establishing the architecture that Hyena directly generalizes. H3 corresponds to Hyena_2 with SSM-parameterized filters (Remark 3.2). Also provides the WikiText-103 baselines under identical conditions and the FFTConv CUDA kernel used in benchmarking.

- **Mehta et al. (2022)** -- *GSS: Long Range Language Modeling via Gated State Spaces.* GSS composes gating with SSM-based convolutions. Corresponds to Hyena_1 (Remark 3.2). Evaluated alongside Hyena on associative recall.

### Subquadratic Attention Alternatives

- **Zhai et al. (2021)** -- *AFT: An Attention Free Transformer.* Attention-Free Transformer combining gating and softmax or explicit convolutions. Evaluated alongside Hyena on associative recall (Table 4.2) and WikiText-103 (Table 4.3).

- **Peng (2021)** -- *RWKV-LM.* Linear-complexity RNN-based language model. Compared against Hyena on associative recall (Table 4.2) and SuperGLUE (Tables 4.5, 4.6). RWKV-v4 169M model is the primary attention-free baseline for downstream evaluation.

- **Katharopoulos et al. (2020)** -- *Linear Transformers.* Linearized attention baseline achieving 25.6 perplexity on WikiText-103 (Table 4.3), demonstrating the quality gap that Hyena aims to close.

### Implicit Representations and Filter Design

- **Romero et al. (2021b)** -- *CKConv: Continuous Kernel Convolution for Sequential Data.* Implicit parameterization of convolution filters using neural networks. CKConv's approach directly inspires Hyena's filter design (Equation 7) and is the second-best filter parameterization on long-range associative recall (14.3% at 131K, Table A.2).

- **Li et al. (2020)** -- *Fourier Neural Operator.* Frequency-domain filter parameterization used as baseline in long convolution comparisons (Figure 4.1, Table A.2).

- **Li et al. (2022)** -- *SGConv: What Makes Convolutional Models Great on Long Sequence Modeling?* Findings on exponential decay filters directly inform Hyena's window function design.

### Efficiency and Fast Algorithms

- **Dao et al. (2022b)** -- *FlashAttention.* Hardware-aware exact attention algorithm providing the primary speed comparison target for Hyena's benchmarks (Figure 4.3, Section 4.4). Crossover between Hyena and FlashAttention occurs at 4K-8K.

- **Selesnick and Burrus (2017)** -- *Fast Convolution and Filtering.* FFT-based fast convolution algorithms underlying Hyena's O(L log L) computation via FFTConv, including the circular convolution technique with zero-padding.

- **Li et al. (2015)** and **Dao et al. (2019, 2022a)** -- *Butterfly Factorization* and *Monarch Matrices.* The Hyena operator's matrix decomposition as alternating diagonal and Toeplitz matrices is connected to butterfly decompositions for fast structured matrix multiplication.

### Evaluation and Vision

- **Wang et al. (2019)** -- *SuperGLUE.* The multi-task NLU benchmark used for downstream evaluation (Tables 4.5, 4.6).

- **Dosovitskiy et al. (2020)** -- *ViT: An Image Is Worth 16x16 Words.* The Vision Transformer architecture in which Hyena is used as a drop-in replacement for attention (Table 4.7).

- **Nguyen et al. (2022)** -- *S4ND: Modeling Images and Videos as Multidimensional Signals.* The 2D state-space model baseline for CIFAR-10 image classification, against which Hyena-ISO achieves better accuracy with fewer parameters.
