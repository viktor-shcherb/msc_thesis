---
title: "RoFormer: Enhanced Transformer with Rotary Position Embedding"
authors: "Su, Lu, Pan, Murtadha, Wen, Liu"
year: 2024
venue: "Neurocomputing 2024"
paper_type: journal-paper
categories: ["position-encoding", "architecture"]
scope: ["rotary positional encoding", "relative position information", "linear attention compatibility"]
benchmarks_used: ["wmt-translation", "glue", "enwik8", "cail2019-scm"]
models_introduced: ["roformer"]
models_evaluated: ["transformer-base", "bert-base", "wobert", "nezha", "performer"]
key_claims:
  - id: C1
    claim: "RoPE encodes absolute position with a rotation matrix and incorporates explicit relative position dependency in the self-attention inner product"
    evidence: "Section 3.1--3.2, Equations 11--16"
    status: supported
    scope: "even-dimensional query/key vectors, standard and linear self-attention"
    magnitude: "qualitative"
  - id: C2
    claim: "RoPE has a long-term decay property: the inner-product upper bound decays as relative distance increases when using theta_i = 10000^{-2i/d}"
    evidence: "Section 3.3, Section 3.4.3, Figure 2, Equations 35--37"
    status: supported
    scope: "frequency schedule theta_i = 10000^{-2i/d}, d-dimensional query/key vectors"
    magnitude: "upper bound on average |S_i| decays from ~20 to ~6-8 over 0-275 relative distance (Figure 2)"
  - id: C3
    claim: "RoPE is compatible with linear self-attention because rotation preserves vector norms"
    evidence: "Section 3.3, Equation 19, Performer experiment (Figure 3, right)"
    status: supported
    scope: "linear attention with non-negative kernel feature maps (e.g., elu+1)"
    magnitude: "qualitative -- denominator kept unchanged, weights not strictly probabilistically normalized"
  - id: C4
    claim: "RoFormer achieves 27.5 BLEU on WMT 2014 EN-DE, outperforming Transformer-base at 27.3 BLEU"
    evidence: "Table 1, Section 4.1.3"
    status: supported
    scope: "WMT 2014 EN-DE, Transformer-base architecture, beam search (size 4, penalty 0.6), single model averaged over last 5 checkpoints"
    magnitude: "+0.2 BLEU (27.5 vs 27.3)"
  - id: C5
    claim: "RoFormer converges faster than BERT during MLM pre-training"
    evidence: "Figure 3 (left), Section 4.2.3"
    status: supported
    scope: "bert-base-uncased architecture, BookCorpus + Wikipedia, batch size 64, max length 512, 100k steps, AdamW lr 1e-5"
    magnitude: "visual convergence advantage in MLM loss curve (Figure 3 left); no numerical gap reported"
  - id: C6
    claim: "RoFormer outperforms BERT on MRPC (+0.6 F1), STS-B (+1.2 Spearman), and QQP (+15.2 F1) but underperforms on SST-2, QNLI, and MNLI"
    evidence: "Table 2, Section 4.3.3"
    status: supported
    scope: "bert-base-uncased, 100k pre-training steps, 6 GLUE tasks, best-averaged validation results across lr {2,3,4,5}e-5"
    magnitude: "wins: MRPC +0.6 F1, STS-B +1.2 Spearman, QQP +15.2 F1; losses: SST-2 -2.8 Acc, QNLI -2.5 Acc, MNLI -4.4/-3.6 Acc"
  - id: C7
    claim: "RoFormer-1024 outperforms WoBERT-512 by +1.69% absolute accuracy on CAIL2019-SCM test set, demonstrating RoPE's sequence length flexibility"
    evidence: "Table 5, Section 4.5.4"
    status: supported
    scope: "CAIL2019-SCM Chinese legal case matching, documents >512 characters, RoFormer pre-trained on ~34GB Chinese data"
    magnitude: "+1.69% absolute test accuracy (69.79% vs 68.10%)"
  - id: C8
    claim: "Performer with RoPE achieves lower LM loss than Performer without RoPE under identical training conditions"
    evidence: "Figure 3 (right), Section 4.4.2"
    status: supported
    scope: "12-layer char-based Performer, 768 dims, 12 heads, Enwik8, lr 1e-4, batch 128, max length 1024"
    magnitude: "visual convergence advantage in LM loss curve (Figure 3 right); no numerical gap reported"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Replaces sinusoidal positional encodings with rotation-based encoding; inherits frequency schedule theta_i = 10000^{-2(i-1)/d}"
  - target: 2022-04-alibi-train-short-test-long
    type: concurrent
    detail: "ALiBi is an alternative position encoding; ALiBi finds RoPE fails at extrapolation beyond training length, though later work (PI, NTK, YaRN) shows RoPE can be adapted"
  - target: 2023-02-llama-open-efficient-foundation
    type: extended-by
    detail: "LLaMA adopts RoPE, establishing it as the default positional encoding for open-weight LLMs"
  - target: 2023-06-pi-positional-interpolation
    type: extended-by
    detail: "PI extends RoPE's context window by linearly interpolating position indices"
  - target: 2023-06-rope-ntk
    type: extended-by
    detail: "NTK-aware scaling modifies RoPE's base frequency for context extension"
  - target: 2023-12-landmark-attention-infinite-context
    type: extended-by
    detail: "Landmark Attention exploits RoPE's property of adding position information just before attention to enable position-free cache storage"
  - target: 2024-05-yarn-context-extension
    type: extended-by
    detail: "YaRN provides a comprehensive RoPE scaling method combining NTK interpolation and attention temperature"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: extended-by
    detail: "DroPE removes all RoPE embeddings after pretraining with a short recalibration phase, enabling zero-shot context extension without long-context finetuning"
  - target: 2025-07-position-bias-transformers
    type: extended-by
    detail: "Provides theoretical characterization of RoPE's decay: Gaussian-like decay proportional to (i-j)^2 * theta_1^2 per layer (Lemma 4.6), substantially weaker than ALiBi, with multi-layer non-monotonic trade-off (Theorem 4.7)"
  - target: 2025-04-effective-context-length-falls-short
    type: extended-by
    detail: "STRING manipulates RoPE's relative position matrix by shifting well-trained position indices to replace undertrained tail positions, achieving training-free long-context improvements"
  - target: 2025-04-attention-sink-emerges
    type: extended-by
    detail: "Gu et al. evaluate RoPE alongside five other PE types and show that PE type does not affect attention sink emergence; proves (Proposition 4) that RoPE attention scores with repeated tokens are bounded by e^{2xi}/(e^{2xi} + (t-1))"
  - target: 2024-07-llama-3-herd-of-models
    type: extended-by
    detail: "Llama 3 uses RoPE with increased base frequency theta=500,000 for 128K context support"
  - target: 2025-04-kimi-vl-technical-report
    type: extended-by
    detail: "Kimi-VL uses 2D RoPE in MoonViT vision encoder for spatial position encoding and extends RoPE base frequency from 50K to 800K for 128K context in the MoE language model"
  - target: 2025-04-pine-eliminating-position-bias
    type: extended-by
    detail: "PINE identifies RoPE's recency bias as one of two causes of position bias and designs importance-based position re-assignment that aligns with RoPE's inherent distance decay"
  - target: 2025-10-kimi-linear-attention
    type: complementary
    detail: "Kimi Linear interprets linear attention with gated delta rule as learnable multiplicative position encoding that relaxes RoPE's orthogonality constraint; uses NoPE for full attention layers, delegating positional encoding to KDA layers"
  - target: 2024-07-longrope-context-extension
    type: extended-by
    detail: "LongRoPE modifies RoPE's per-dimension frequencies via learned non-uniform rescale factors found by evolutionary search, extending context to 2048k tokens"
  - target: 2024-06-effective-long-context-scaling
    type: extended-by
    detail: "Llama 2 Long modifies RoPE base frequency from 10,000 to 500,000 to reduce attention decay for distant tokens, enabling 32K context through continual pretraining"
  - target: 2023-07-retnet-retentive-network
    type: extended-by
    detail: "RetNet derives its retention mechanism from xPos (a decay-augmented RoPE variant), connecting rotary position encodings to a linear recurrence with exponential decay"
  - target: 2025-04-differential-transformer
    type: complementary
    detail: "DIFF Transformer uses RoPE for positional encoding within its differential attention mechanism, which subtracts two softmax attention maps to cancel noise"
open_questions:
  - question: "Why does multiplicative position encoding (RoPE) converge faster than additive position encoding (sinusoidal PE) during pre-training?"
    addressed_by: null
  - question: "Why does RoPE's specific long-term decay profile lead to superior long-text performance compared to other position encodings with similar decay properties?"
    addressed_by: null
  - question: "Which RoPE dimensions encode positional vs semantic information?"
    addressed_by: 2025-12-drope-dropping-positional-embeddings
  - question: "Can RoPE extrapolate to sequence lengths beyond those seen during training without modification?"
    addressed_by: 2023-06-pi-positional-interpolation
---
# RoFormer: Enhanced Transformer with Rotary Position Embedding

**Authors:** Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, Yunfeng Liu (Zhuiyi Technology Co., Ltd., Shenzhen, China)
**Date:** April 2021, arXiv:2104.09864; published in Neurocomputing 568, 127063, January 2024

---

## Core Research Problem

Transformer-based language models are inherently position-agnostic (Yun et al., 2020), requiring explicit injection of positional information. Existing approaches fall into two categories:

1. **Absolute position embeddings** (Vaswani et al., 2017; Devlin et al., 2019; Lan et al., 2020; Clark et al., 2020; Radford et al., 2019) add a position-dependent vector to the word embedding before projection: `f_t(x_i, i) = W_t(x_i + p_i)` (Eq. 3). Trainable variants are limited to a fixed maximum sequence length L. Vaswani et al. (2017) proposed generating p_i via sinusoidal functions (Eq. 4).

2. **Relative position embeddings** (Shaw et al., 2018; Dai et al., 2019; Raffel et al., 2020; Ke et al., 2020; He et al., 2020) decompose the query-key inner product `q^T_m k_n` into multiple terms (Eq. 6) and replace absolute position embeddings with relative counterparts. Shaw et al. (2018) added clipped trainable relative position vectors to keys and values (Eq. 5). Dai et al. (2019) replaced absolute embeddings with sinusoid-encoded relative positions and position-independent trainable vectors (Eq. 7). Raffel et al. (2020) simplified this to a trainable bias `b_{i,j}` (Eq. 8). He et al. (2020) used the middle two terms of the four-way decomposition (Eq. 10).

Both categories share a fundamental limitation: they **add** position information to context representations. This makes them incompatible with linear self-attention architectures (Katharopoulos et al., 2020), where the computation relies on separable kernel feature maps applied to queries and keys independently. Additive position encodings break this separability (Section 1).

**The core challenge is to design a position encoding that encodes absolute position, incorporates explicit relative position dependency in the self-attention inner product, decays with increasing relative distance, and remains compatible with linear self-attention -- all without adding position information to the context representations.**

---

## Problem Solutions

RoPE (Rotary Position Embedding) encodes position by **multiplying** query and key vectors with a rotation matrix whose angle is proportional to the token's absolute position. The resulting query-key inner product depends only on relative position.

1. **Multiplicative encoding via rotation.** Position information is injected by rotating the affine-transformed word embedding by an angle proportional to the position index: `f_{q,k}(x_m, m) = R^d_{Theta,m} W_{q,k} x_m` (Eq. 14). The rotation matrix is block-diagonal with d/2 two-dimensional rotation blocks.
2. **Relative position from rotation matrix product.** The inner product `q^T_m k_n = x^T_m W_q R^d_{Theta,n-m} W_k x_n` depends only on the relative position `n - m` through `R^d_{Theta,n-m} = (R^d_{Theta,m})^T R^d_{Theta,n}` (Eq. 16).
3. **Long-term decay.** With the frequency schedule `theta_i = 10000^{-2i/d}`, the upper bound on the inner product magnitude decays as relative distance increases (Section 3.3, Section 3.4.3).
4. **Linear attention compatibility.** Because rotation preserves vector norms, RoPE can be applied after the non-negative feature maps in linear attention without breaking the kernel decomposition (Eq. 19).

---

## Approach Details

### Method

The paper formulates the position encoding problem as finding functions f_q, f_k such that the query-key inner product depends only on word embeddings and relative position (Eq. 11):

> <f_q(x_m, m), f_k(x_n, n)> = g(x_m, x_n, m - n)

**2D case (Section 3.2.1, Section 3.4.1).** Using complex number representation, the paper derives (with initial condition f_{q,k}(x, 0) = W_{q,k} x):

> f_q(x_m, m) = (W_q x_m) e^{im*theta}
> f_k(x_n, n) = (W_k x_n) e^{in*theta}
> g(x_m, x_n, m - n) = Re[(W_q x_m)(W_k x_n)* e^{i(m-n)*theta}]

The derivation proceeds by decomposing f_{q,k} into radial and angular components in polar form (Eq. 23). Setting m = n in the constraint (Eq. 24) and applying initial conditions (Eq. 25) shows that the radial component is independent of position (Eq. 27). The angular component satisfies the recurrence `phi(m+1) - phi(m) = constant` (Eq. 29), yielding the arithmetic progression `phi(m) = m*theta + gamma` (Eq. 30). Setting gamma = 0 yields the final solution (Eq. 33).

In matrix form for 2D (Eq. 13):

> f_{q,k}(x_m, m) = [[cos m*theta, -sin m*theta], [sin m*theta, cos m*theta]] W_{q,k} x_m

**General d-dimensional case (Section 3.2.2).** The d-dimensional space (d even) is divided into d/2 two-dimensional subspaces, each with its own rotation angle (Eq. 14):

> f_{q,k}(x_m, m) = R^d_{Theta,m} W_{q,k} x_m

where R^d_{Theta,m} is a block-diagonal matrix of d/2 rotation blocks (Eq. 15):

> R^d_{Theta,m} = diag(R(m*theta_1), R(m*theta_2), ..., R(m*theta_{d/2}))

with each block R(m*theta_i) = [[cos m*theta_i, -sin m*theta_i], [sin m*theta_i, cos m*theta_i]] and frequency parameters:

> Theta = {theta_i = 10000^{-2(i-1)/d}, i in [1, 2, ..., d/2]}

The self-attention inner product becomes (Eq. 16):

> q^T_m k_n = (R^d_{Theta,m} W_q x_m)^T (R^d_{Theta,n} W_k x_n) = x^T_m W_q R^d_{Theta,n-m} W_k x_n

where R^d_{Theta,n-m} = (R^d_{Theta,m})^T R^d_{Theta,n}. Since R^d_Theta is an orthogonal matrix, encoding position preserves vector norms and ensures numerical stability.

### Key Technical Components

**Efficient computation (Section 3.4.2).** The sparse block-diagonal structure of R^d_{Theta,m} enables an element-wise implementation avoiding full matrix multiplication (Eq. 34):

> R^d_{Theta,m} x = x (element-wise) [cos m*theta_1, cos m*theta_1, ..., cos m*theta_{d/2}, cos m*theta_{d/2}] + [-x_2, x_1, -x_4, x_3, ..., -x_d, x_{d-1}] (element-wise) [sin m*theta_1, sin m*theta_1, ..., sin m*theta_{d/2}, sin m*theta_{d/2}]

This requires only two element-wise multiplications and one addition -- the same computational cost as applying sinusoidal absolute position embeddings.

**No position in value vectors.** RoPE is applied only to queries and keys, not to values. The value computation remains v_n = W_v x_n, consistent with relative position encoding methods (Dai et al., 2019; Raffel et al., 2020) that remove position information from the value term.

**Linear attention integration (Section 3.3).** For linear attention with feature maps phi, varphi (Eq. 18), RoPE is applied after the feature maps (Eq. 19):

> Attention(Q, K, V)_m = [sum_n (R^d_{Theta,m} phi(q_m))^T (R^d_{Theta,n} varphi(k_n)) v_n] / [sum_n phi(q_m)^T varphi(k_n)]

The denominator is kept unchanged (without rotation) to avoid division by zero, since the rotated numerator may contain negative terms. The authors acknowledge the weights in Eq. 19 are "not strictly probabilistic normalized" but argue "the computation can still model the importance of values" (Section 3.3).

### Theoretical Analysis

**Derivation of uniqueness (Section 3.4.1).** The 2D solution is derived from first principles using complex number decomposition. Functions f_{q,k} and g are decomposed into radial (R) and angular (Theta) components (Eq. 23). Setting m = n in the constraint equation (Eq. 24) and applying initial conditions (Eq. 25) shows the radial component is position-independent: R_q(x_q, m) = ||q||, R_k(x_k, n) = ||k|| (Eq. 27). The angular component satisfies phi(m+1) - phi(m) = Theta_g(x_q, x_k, 1) + theta_q - theta_k (Eq. 29), which is constant with respect to m, yielding the arithmetic progression phi(m) = m*theta + gamma (Eq. 30).

**Long-term decay (Section 3.4.3).** The inner product of RoPE-encoded queries and keys can be written as a complex number multiplication (Eq. 35):

> (R^d_{Theta,m} W_q x_m)^T (R^d_{Theta,n} W_k x_n) = Re[sum_{i=0}^{d/2-1} q_{[2i:2i+1]} k*_{[2i:2i+1]} e^{i(m-n)*theta_i}]

Using Abel transformation (summation by parts, Eq. 36), the inner product is bounded by (Eq. 37):

> |sum| <= (max_i |h_{i+1} - h_i|) * sum_{i=0}^{d/2-1} |S_{i+1}|

where h_i = q_{[2i:2i+1]} k*_{[2i:2i+1]} and S_j = sum_{i=0}^{j-1} e^{i(m-n)*theta_i}. The average of |S_i| decays as relative distance |m - n| increases with the frequency schedule theta_i = 10000^{-2i/d} (Figure 2). This provides an inductive bias: tokens at large relative distances contribute less to each other's attention.

### Experimental Setup

**Machine translation (Section 4.1):** WMT 2014 English-German (~4.5M sentence pairs). Transformer-base architecture, fairseq toolkit (MIT License). Adam optimizer (beta_1 = 0.9, beta_2 = 0.98), learning rate warmed linearly from 1e-7 to 5e-4 then decayed by inverse square root. Beam search (size 4, length penalty 0.6), label smoothing 0.1, 37k BPE vocabulary. Single model obtained by averaging last 5 checkpoints.

**Pre-training (Section 4.2):** bert-base-uncased architecture with RoPE replacing sinusoidal PE. BookCorpus + Wikipedia, 80/20 train/validation split. Batch size 64, max sequence length 512, 100k steps. AdamW optimizer, learning rate 1e-5.

**GLUE fine-tuning (Section 4.3):** MRPC, SST-2, QNLI, STS-B, QQP, MNLI. 3 epochs, max sequence length 512, batch size 32, learning rates {2, 3, 4, 5}e-5. Best-averaged validation results reported. Hugging Face Transformers library (Apache License 2.0).

**Performer with RoPE (Section 4.4):** 12-layer char-based Performer, 768 dimensions, 12 heads. Enwik8 dataset (English Wikipedia with markup). Learning rate 1e-4, batch size 128, max sequence length 1024. Code from lucidrains/performer-pytorch (MIT License).

**Chinese long text (Section 4.5):** RoFormer pre-trained on ~34GB Chinese data (Wikipedia, news, forums) in multiple stages with varying max sequence lengths (128--1536) and batch sizes (256--512) over 6 stages totaling ~452.5k steps (Table 4). Evaluated on CAIL2019-SCM (8964 case triplets, similar case matching in legal domain). Hardware: two cloud servers with 4x V100 GPUs each.

**Reproducibility:** Code released on GitHub (MIT License for fairseq and Performer), pre-trained models available. Seeds not explicitly reported. No variance estimates or confidence intervals provided for any experiment.

### Key Results

**Machine translation (Table 1):**

| Model | BLEU |
|---|---|
| Transformer-base (Vaswani et al., 2017) | 27.3 |
| RoFormer | **27.5** |

- RoFormer gives a modest +0.2 BLEU improvement over the Transformer baseline on WMT 2014 EN-DE (Table 1, Section 4.1.3). Single dataset, single model configuration, no variance reported (limited evidence).

**Pre-training convergence (Figure 3):**

- RoFormer achieves faster MLM loss convergence than BERT under identical training conditions (Figure 3, left). Only visual comparison from loss curves; no numerical convergence speed metric reported (limited evidence -- single configuration, single training run).
- Performer with RoPE achieves lower LM loss than Performer without RoPE (Figure 3, right). Single dataset (Enwik8), single configuration, no numerical values reported (limited evidence).

**GLUE fine-tuning (Table 2):**

| Model | MRPC (F1) | SST-2 (Acc) | QNLI (Acc) | STS-B (Spearman) | QQP (F1) | MNLI (m/mm Acc) |
|---|---|---|---|---|---|---|
| BERT | 88.9 | **93.5** | **90.5** | 85.8 | 71.2 | **84.6/83.4** |
| RoFormer | **89.5** | 90.7 | 88.0 | **87.0** | **86.4** | 80.2/79.8 |

- RoFormer outperforms BERT on MRPC (+0.6 F1), STS-B (+1.2 Spearman), and QQP (+15.2 F1). BERT outperforms RoFormer on SST-2 (-2.8), QNLI (-2.5), and MNLI (-4.4/-3.6) (Table 2, Section 4.3.3). Best-averaged validation results across 4 learning rates; no variance across runs reported (moderate evidence -- 6 tasks but no statistical significance testing).

**Chinese long text -- CAIL2019-SCM (Table 5):**

| Model | Validation | Test |
|---|---|---|
| BERT-512 | 64.13% | 67.77% |
| WoBERT-512 | 64.07% | 68.10% |
| RoFormer-512 | 64.13% | 68.29% |
| RoFormer-1024 | **66.07%** | **69.79%** |

- At 512 tokens, RoFormer is comparable to baselines. At 1024 tokens, RoFormer-1024 outperforms WoBERT-512 by +1.69% absolute on the test set, demonstrating RoPE's sequence length flexibility (Table 5, Section 4.5.4). Single dataset in a specialized domain (Chinese legal), no variance reported (limited evidence for generalizability of length flexibility).

**Chinese pre-training progression (Table 4):**

| Stage | Max seq length | Batch size | Training steps | Loss | Accuracy |
|---|---|---|---|---|---|
| 1 | 512 | 256 | 200k | 1.73 | 65.0% |
| 2 | 1536 | 256 | 12.5k | 1.61 | 66.8% |
| 3 | 256 | 256 | 120k | 1.75 | 64.6% |
| 4 | 128 | 512 | 80k | 1.83 | 63.4% |
| 5 | 1536 | 256 | 10k | 1.58 | 67.4% |
| 6 | 512 | 512 | 30k | 1.66 | 66.2% |

- Accuracy improves when the maximum sequence length is increased to 1536 (stages 2 and 5), confirming RoPE's ability to adapt to longer sequences without architectural changes (Table 4, Section 4.5.2). Single pre-training run, no comparison with alternative position encodings at varying lengths (limited evidence).

**Cross-comparison of Chinese models (Table 3):**

| Model | BERT | WoBERT | NEZHA | RoFormer |
|---|---|---|---|---|
| Tokenization level | char | word | char | word |
| Position embedding | abs. | abs. | rel. | RoPE |

- Table 3 provides a qualitative comparison of tokenization and position encoding choices across Chinese pre-trained models (Section 4.5.1).

---

## Limitations and Failure Modes

The paper explicitly acknowledges the following limitations (Section 4.5.5):

1. **No explanation for faster convergence.** Despite demonstrating that RoFormer converges faster than BERT during pre-training, the paper states: "there lacks of thorough explanations on why it converges faster than baseline models that incorporates other position encoding strategies."

2. **No explanation for long-text superiority.** While the long-term decay property is proved, the paper acknowledges: "our model shows superior performance on long texts than peer models, we have not come up with a faithful explanation."

3. **Hardware requirements.** The paper notes: "Our proposed RoFormer is built upon the Transformer-based infrastructure, which requires hardware resources for pre-training purpose" (Section 4.5.5).

4. **[Inferred] Mixed GLUE results.** RoFormer underperforms BERT on 3 of 6 GLUE tasks (SST-2, QNLI, MNLI), with MNLI showing a -4.4/-3.6 point gap. The paper describes RoFormer as outperforming "in three out of six datasets" (Section 4.3.3) but does not analyze why RoPE hurts performance on the remaining tasks.

5. **[Inferred] Modest machine translation improvement.** The +0.2 BLEU improvement over Transformer-base on WMT 2014 EN-DE is small and may not be statistically significant. The paper does not report confidence intervals or significance tests (Table 1).

6. **[Inferred] Linear attention integration is approximate.** The weights in the linear attention formulation (Eq. 19) are "not strictly probabilistic normalized" because the numerator may contain negative terms after rotation. The paper does not analyze the practical impact of this approximation beyond showing lower loss for Performer with RoPE (Section 3.3).

#### Scope and Comparability

- **What was not tested:** RoPE is not evaluated on autoregressive language modeling with standard Transformer (only with Performer's linear attention). No evaluation on sequence lengths beyond 1536 tokens. No evaluation on non-English, non-Chinese languages. No evaluation on models larger than BERT-base scale. No evaluation on decoder-only architectures. No ablation of the frequency schedule theta_i -- the paper uses only the inherited Vaswani et al. (2017) schedule.
- **Comparability notes:** The GLUE fine-tuning comparison is between models pre-trained for only 100k steps (vs. BERT's original 1M steps), which may not reflect performance at full pre-training convergence. The Chinese experiments use different pre-training data and stages from the English experiments, making cross-language comparison indirect. The WMT 2014 EN-DE result uses Transformer-base (not Transformer-big), so the absolute BLEU scores are not directly comparable to papers using the larger configuration.

---

## Conclusions

### Contributions

1. **Multiplicative position encoding via rotation.** RoPE introduces a fundamentally different approach to position encoding: instead of adding position embeddings to context representations, it multiplies query and key vectors by a rotation matrix. This naturally encodes relative position through the rotation matrix product R^d_{Theta,n-m} (Eq. 16, Section 3.2).

2. **Principled derivation from a relative position constraint.** The rotation formulation is derived from first principles by requiring the query-key inner product to depend only on relative position (Eq. 11). The 2D case yields a unique solution (up to constants) via complex number decomposition (Eqs. 23--33), which generalizes to arbitrary even dimensions via block-diagonal structure (Section 3.4.1).

3. **Long-term decay property.** Using the frequency schedule theta_i = 10000^{-2(i-1)/d}, RoPE provably produces decaying attention score upper bounds with increasing relative distance, providing a useful inductive bias for natural language (Section 3.4.3, Figure 2).

4. **Linear attention compatibility.** Because rotation preserves norms, RoPE can be combined with linear attention by applying the rotation after the kernel feature maps (Eq. 19), enabling relative position encoding in O(N) attention architectures. This is demonstrated empirically with Performer (Section 4.4).

5. **Sequence length flexibility.** RoPE uses no trainable position parameters and can be applied at any sequence length without modification. The Chinese experiments demonstrate that a model pre-trained with one maximum length can be evaluated at a different length (Table 4, Table 5, Section 4.5).

### Implications

1. **De facto standard for modern LLMs.** (Inference) Despite the paper's modest experimental improvements on BERT-scale models, RoPE became the dominant positional encoding in the LLM era, adopted by LLaMA, Falcon, Pythia, Qwen, Mistral, and Gemma. The paper itself notes integration into Hugging Face Transformers (Abstract).

2. **Foundation for context extension research.** (Inference) RoPE's frequency-based structure enabled a family of context extension methods -- Position Interpolation (Chen et al., 2023), NTK-Aware Scaled RoPE (bloc97, 2023), YaRN (Peng et al., 2023) -- all operating by modifying RoPE's frequency parameters or position indices.

3. **Multiplicative encoding may have broader advantages.** (Inference) The faster convergence observed for RoFormer suggests that multiplicative position injection may interact differently with the optimization landscape than additive injection, though this remains unexplained (Section 4.5.5).

---

## Key Claims

1. **C1: RoPE encodes absolute position with a rotation matrix and incorporates explicit relative position dependency.** The derivation shows f_{q,k}(x_m, m) = R^d_{Theta,m} W_{q,k} x_m encodes absolute position m, while the inner product q^T_m k_n = x^T_m W_q R^d_{Theta,n-m} W_k x_n depends only on relative position n-m. Scope: even-dimensional query/key vectors, standard and linear self-attention. Evidence: Section 3.1--3.2, Equations 11--16. Status: **supported** (mathematical proof, not dependent on empirical evidence).

2. **C2: RoPE has a long-term decay property.** Using Abel transformation, the paper bounds the inner product and shows the average of |S_i| decays with increasing relative distance under theta_i = 10000^{-2i/d}. Scope: specific to the frequency schedule theta_i = 10000^{-2i/d}. Magnitude: upper bound on average |S_i| decays from ~20 to ~6-8 over relative distance 0-275 (Figure 2). Evidence: Section 3.3, Section 3.4.3, Figure 2, Equations 35--37. Status: **supported** (mathematical proof with numerical illustration).

3. **C3: RoPE is compatible with linear self-attention.** Rotation preserves vector norms, so RoPE can be applied after non-negative kernel feature maps without breaking their properties. Scope: linear attention with non-negative feature maps (e.g., elu+1). Magnitude: qualitative compatibility; the denominator normalization is approximate. Evidence: Section 3.3, Equation 19, Performer experiment (Figure 3, right). Status: **supported** (theoretical argument confirmed by one empirical experiment -- limited evidence breadth).

4. **C4: RoFormer achieves 27.5 BLEU on WMT 2014 EN-DE vs 27.3 for Transformer-base.** A +0.2 BLEU improvement. Scope: WMT 2014 EN-DE, Transformer-base, beam search size 4. Magnitude: +0.2 BLEU. Evidence: Table 1, Section 4.1.3. Status: **supported** (single dataset, single model, no variance reported -- limited evidence).

5. **C5: RoFormer converges faster than BERT during pre-training.** The MLM loss curve shows faster convergence for RoFormer under identical settings (batch size 64, max length 512, 100k steps, AdamW lr 1e-5). Scope: bert-base-uncased, BookCorpus + Wikipedia, specific hyperparameters. Magnitude: visual only -- no numerical convergence speed metric. Evidence: Figure 3 (left), Section 4.2.3. Status: **supported** (single configuration, single run, visual evidence only -- limited evidence).

6. **C6: RoFormer outperforms BERT on 3 of 6 GLUE tasks.** MRPC: 89.5 vs 88.9 F1. STS-B: 87.0 vs 85.8 Spearman. QQP: 86.4 vs 71.2 F1. BERT outperforms on SST-2 (93.5 vs 90.7), QNLI (90.5 vs 88.0), MNLI (84.6/83.4 vs 80.2/79.8). Scope: bert-base-uncased, 100k pre-training steps, best-averaged results across 4 learning rates. Magnitude: wins up to +15.2 F1 (QQP), losses up to -4.4 Acc (MNLI). Evidence: Table 2, Section 4.3.3. Status: **supported** (6 tasks, but only 100k pre-training steps and no variance estimates -- moderate evidence).

7. **C7: RoFormer-1024 outperforms WoBERT-512 on CAIL2019-SCM.** RoFormer-1024: 69.79% test accuracy. WoBERT-512: 68.10%. Delta: +1.69% absolute. Scope: CAIL2019-SCM Chinese legal case matching, documents >512 characters. Magnitude: +1.69% absolute test accuracy. Evidence: Table 5, Section 4.5.4. Status: **supported** (single dataset in specialized domain, no variance reported -- limited evidence for generalizability).

8. **C8: Performer with RoPE achieves lower loss than Performer without RoPE.** Under identical training conditions on Enwik8 (12 layers, 768 dims, 12 heads, lr 1e-4, batch 128, max length 1024), adding RoPE leads to faster convergence and lower final LM loss. Scope: char-based Performer on Enwik8 only. Magnitude: visual from loss curves; no numerical values reported. Evidence: Figure 3 (right), Section 4.4.2. Status: **supported** (single dataset, single configuration, visual evidence only -- limited evidence).

---

## Open Questions

1. **Why does multiplicative position encoding converge faster than additive position encoding?** The paper demonstrates faster convergence for RoFormer vs BERT but explicitly acknowledges lacking an explanation (Section 4.5.5). **Unresolved.**

2. **Why does RoPE's specific decay profile lead to superior long-text performance?** The long-term decay property is shared conceptually with other position encodings, yet RoPE shows superior empirical performance on long texts. The paper acknowledges this as an open question (Section 4.5.5). **Unresolved.**

3. **Which RoPE dimensions encode positional vs semantic information?** The block-diagonal structure assigns each dimension pair a different frequency theta_i. Whether different frequencies serve different roles (positional vs semantic) is not investigated. **Addressed by** Su et al. (2025) -- *DroPE*, which shows that high-frequency dimensions primarily encode positional information and can be dropped for context extension.

4. **Can RoPE extrapolate to sequence lengths beyond training without modification?** The paper does not evaluate extrapolation, but ALiBi (Press et al., 2022) found RoPE fails at direct extrapolation. **Addressed by** Chen et al. (2023) -- *Position Interpolation*, which showed RoPE can be adapted for context extension via interpolation rather than extrapolation.

---

## Core References and Why They Are Referenced

### Position Encoding Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer architecture and sinusoidal absolute position embeddings (Eq. 4). RoPE's frequency schedule theta_i = 10000^{-2(i-1)/d} is directly inherited from Vaswani et al.'s sinusoidal formulation, but applied multiplicatively via rotation rather than additively. Primary baseline for machine translation (Table 1).

- **Shaw et al. (2018)** -- *Self-Attention with Relative Position Representations.* Introduces clipped relative position embeddings added to keys and values (Eq. 5). Represents the first approach to relative position encoding in Transformers; RoPE addresses the same goal through rotation rather than addition.

- **Dai et al. (2019)** -- *Transformer-XL.* Decomposes the query-key product into four terms (Eq. 6--7) and introduces sinusoid-encoded relative positions, with trainable vectors replacing absolute position terms. RoPE avoids this additive decomposition entirely.

- **Raffel et al. (2020)** -- *T5.* Simplifies relative position encoding to a trainable bias b_{i,j} added to attention logits (Eq. 8). RoPE achieves relative position encoding without any additive bias terms.

- **He et al. (2020)** -- *DeBERTa.* Uses the middle two terms of the four-way decomposition (Eq. 10) for relative position encoding. Represents the state of the art in additive relative PE at the time of RoPE's development.

- **Ke et al. (2020)** -- *Rethinking Positional Encoding.* Investigated correlations between absolute positions and words, finding little correlation. Used different projection matrices for words and positions (Eq. 9).

### Linear Attention

- **Katharopoulos et al. (2020)** -- *Transformers Are RNNs.* Introduces linear attention via kernel feature maps (Eq. 18). RoPE's norm-preserving rotation enables combining relative position encoding with linear attention (Eq. 19), which additive methods cannot support.

- **Choromanski et al. (2020)** -- *Rethinking Attention with Performers.* Provides the Performer architecture used in RoPE's linear attention experiments (Section 4.4). RoPE with Performer achieves lower LM loss than Performer without RoPE on Enwik8 (Figure 3, right).

### Baseline Models

- **Devlin et al. (2019)** -- *BERT.* Primary baseline for pre-training and GLUE experiments. Uses trainable absolute position embeddings limited to 512 tokens. RoFormer replaces BERT's sinusoidal PE with RoPE (Section 4.2).

- **Su (2020)** -- *WoBERT.* Chinese word-based BERT model with absolute position embeddings. RoFormer modifies WoBERT by replacing absolute PE with RoPE for Chinese experiments. Baseline for CAIL2019-SCM (Table 5).

- **Wei et al. (2019)** -- *NEZHA.* Chinese pre-trained model using relative position encoding at character level. Included in cross-comparison (Table 3) to contrast tokenization and position encoding approaches.

### Theoretical Context

- **Yun et al. (2020)** -- *Are Transformers Universal Approximators?* Shows that the self-attention architecture is position-agnostic, motivating the need for explicit position encoding.

- **Wang et al. (2020)** -- *Encoding Word Order in Complex Embeddings.* Proposes modeling position in complex space. Related approach referenced as prior work on complex-valued position encoding.

### Evaluation

- **Bojar et al. (2014)** -- *Findings of the 2014 Workshop on Statistical Machine Translation.* Provides the WMT 2014 English-German dataset used in the machine translation experiment (Section 4.1).

- **Singh et al. (2018)** -- *GLUE.* Provides the benchmark tasks (MRPC, SST-2, QNLI, STS-B, QQP, MNLI) used for fine-tuning evaluation (Section 4.3).

- **Mahoney (2006)** -- *Large Text Compression Benchmark (Enwik8).* Provides the character-level dataset from English Wikipedia used in the Performer experiment (Section 4.4).

- **Xiao et al. (2019)** -- *CAIL2019-SCM.* Provides the Chinese legal case matching dataset (documents >512 characters) used to demonstrate RoPE's sequence length flexibility (Section 4.5).
