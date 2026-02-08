---
title: "Quantizable Transformers: Removing Outliers by Helping Attention Heads Do Nothing"
authors: "Bondarenko, Nagel, Blankevoort"
year: 2023
venue: "NeurIPS 2023"
paper_type: conference-paper
categories: ["quantization", "attention-analysis", "architecture"]
scope: ["activation outliers", "post-training quantization", "attention head no-op behavior", "clipped softmax", "gated attention"]
benchmarks_used: ["mnli", "imagenet-1k"]
models_introduced: []
models_evaluated: ["bert-base", "opt-125m", "opt-350m", "opt-1.3b", "vit-s-16"]
key_claims:
  - id: C1
    claim: "Strong activation outliers are caused by attention heads learning no-op behavior: heads that do not update the residual concentrate attention on low-information tokens with small value outputs, but softmax's inability to produce exact zeros forces ever-larger input magnitudes, creating outliers in FFN outputs"
    evidence: "Section 3, Figure 1, Figure 2, Figure 3 (BERT: >97% of outliers at delimiter tokens; ViT: >99% in 10 hidden dims at background patches)"
    status: supported
    scope: "BERT-base (MNLI fine-tuned), ViT-S/16 (ImageNet-1K), outlier analysis on FFN outputs in later layers"
    magnitude: ">97% outlier-delimiter correlation in BERT layers #10-#11; >99% of ViT outliers in 10 hidden dimensions"
  - id: C2
    claim: "Clipped softmax eliminates outliers in BERT while improving FP16 perplexity: max infinity norm drops from 735 to 21.5, W8A8 perplexity from 1294 to 4.52, FP16 perplexity improves from 4.49 to 4.39"
    evidence: "Table 2, Table 5 (gamma=-0.025, zeta=1)"
    status: supported
    scope: "BERT-base-uncased, MLM pre-training, sequence length 128, per-tensor W8A8 PTQ"
    magnitude: "max inf norm 735->21.5 (97% reduction), W8A8 ppl 1294->4.52, FP16 ppl 4.49->4.39"
  - id: C3
    claim: "Gated attention eliminates outliers across all tested architectures (BERT, OPT, ViT) while maintaining or improving FP performance"
    evidence: "Table 2 (OPT: FP16 ppl 15.84->15.55, max inf norm 340->8.7; ViT: FP32 acc 80.75->81.01%), Table 3 (OPT-350m, OPT-1.3B)"
    status: supported
    scope: "BERT-base, OPT-125m/350m/1.3B, ViT-S/16, per-tensor W8A8 PTQ"
    magnitude: "OPT-125m: inf norm 340->8.7, W8A8 ppl 21.18->16.02; ViT: W8A8 acc 69.24%->79.82%; OPT-1.3B: W8A8 ppl 989.6->29.95"
  - id: C4
    claim: "Both methods enable full INT8 post-training quantization of activations without any additional workarounds, closing the gap between quantized and floating-point performance"
    evidence: "Table 2 (BERT W8A8 ppl: 4.52 vs FP16 4.39; OPT W8A8 ppl: 16.02 vs FP16 15.55; ViT W8A8 acc: 79.82% vs FP32 81.01%)"
    status: supported
    scope: "BERT-base, OPT-125m, ViT-S/16, uniform affine per-tensor PTQ, symmetric weights/asymmetric activations"
    magnitude: "BERT W8A8 ppl gap 0.13 from FP16; OPT W8A8 ppl gap 0.47 from FP16; ViT W8A8 acc gap 1.19% from FP32"
  - id: C5
    claim: "Clipped softmax fails on OPT decoder models, dramatically increasing kurtosis while reducing max infinity norm"
    evidence: "Table 6 (kurtosis increases from 1777 to 19727 with clipped softmax on OPT-125m)"
    status: supported
    scope: "OPT-125m, causal LM, with LN gamma weight decay"
    magnitude: "kurtosis 1777->19727 (11x increase), W8A8 ppl 21.18->37.22 despite inf norm 340->63.2"
  - id: C6
    claim: "Only the lower clipping parameter gamma < 0 matters for outlier reduction; the upper stretch parameter zeta > 1 has negligible effect"
    evidence: "Table 1, Table 8, Section 5.1"
    status: supported
    scope: "BERT-base and ViT-S/16, tested across multiple gamma/zeta combinations"
    magnitude: "gamma=-0.03 alone: inf norm 735->20, kurtosis 3076->80; zeta=1.03 alone: inf norm 741, kurtosis 1707 (similar to vanilla)"
  - id: C7
    claim: "Both methods extend to low-bit quantization: at W4A8 on BERT, clipped softmax achieves 4.90 ppl vs vanilla 6.52; at W6A6, gated attention achieves 5.90 vs vanilla 42.8"
    evidence: "Table 10, Appendix B.7"
    status: supported
    scope: "BERT-base only, MSE weight range estimation, W6A8/W4A8/W6A6 bitwidths"
    magnitude: "W4A8: CS 4.90 vs vanilla 6.52 (25% improvement); W6A6: GA 5.90 vs vanilla 42.8 (86% improvement)"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Proposes two modifications to the softmax attention mechanism (clipped softmax and gated attention) that address a fundamental limitation: softmax's inability to output exact zeros forces attention heads to learn outlier-producing workarounds for no-op behavior"
  - target: 2019-11-dark-secrets-of-bert
    type: extends
    detail: "Kovaleva et al. observed attention concentrating on [CLS] and [SEP] tokens in BERT; Bondarenko et al. explain the causal mechanism: these tokens serve as sinks for no-op attention heads, and the softmax normalization constraint drives outlier growth in FFN outputs"
  - target: 2019-07-specialized-attention-heads-pruning
    type: complementary
    detail: "Voita et al. identify specialized attention head roles (positional, syntactic, rare-word); Bondarenko et al. identify 'no-op' heads as an additional specialization caused by softmax constraints, with consequences for quantization"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "Concurrent work: both papers identify attention heads concentrating probability mass on specific tokens, but from different perspectives. Bondarenko et al. focus on quantization outliers caused by no-op heads; Xiao et al. focus on streaming inference and the attention sink phenomenon. Xiao et al. explicitly cite this paper as observing 'outsized values' linked to the attention sink"
  - target: 2025-04-attention-sink-emerges
    type: extended-by
    detail: "Gu et al. build on Bondarenko et al.'s observation of no-op heads to comprehensively study when and why attention sinks emerge during pre-training, identifying softmax normalization as the root cause and showing sigmoid attention eliminates sinks"
  - target: 2024-12-transformers-need-glasses-over-squashing
    type: complementary
    detail: "Both papers identify pathological consequences of softmax normalization: Bondarenko et al. focus on quantization outliers from no-op heads; Barbero et al. focus on representational collapse and over-squashing from the sum-to-one constraint"
open_questions:
  - question: "Why does clipped softmax fail on OPT decoder models, dramatically increasing kurtosis despite reducing max infinity norm?"
    addressed_by: null
  - question: "Do the proposed methods scale to very large models (>1.3B parameters) trained for significantly longer?"
    addressed_by: null
  - question: "Can clipped softmax and gated attention be combined for complementary benefits?"
    addressed_by: null
  - question: "Would the outlier reduction from these methods improve inference efficiency beyond quantization (e.g., mixed-precision, pruning)?"
    addressed_by: null
---

# Quantizable Transformers: Removing Outliers by Helping Attention Heads Do Nothing

**Authors:** Yelysei Bondarenko, Markus Nagel, Tijmen Blankevoort (Qualcomm AI Research, Amsterdam)
**Date:** December 2023, NeurIPS 2023 (arXiv:2306.12929)

---

## Core Research Problem

Modern Transformer models learn strong activation outliers — values exceeding 6 standard deviations from the mean — that make post-training quantization (PTQ) extremely difficult. These outliers appear in a small fixed set of hidden dimensions but occur consistently across layers and data sequences, and are critical to model predictions: clipping or zeroing them significantly degrades task performance. When per-tensor INT8 PTQ is applied, the large dynamic range created by outliers forces a trade-off between rounding error (using a large quantization range for small values) and clipping error (using a small range that clips the outliers). Frequently no good trade-off can be found, resulting in catastrophic quantized performance — e.g., BERT-base W8A8 perplexity degrades from 4.49 to 1294 (Table 2, Section 4).

The outlier problem has been documented across diverse Transformer architectures: BERT, RoBERTa, DistilBERT, MobileBERT, ELECTRA, BART, XLNet, GPT-2, OPT (Section 1, [4, 13, 62, 63, 67]). Prior work addresses outliers post-hoc — through mixed-precision formats, activation smoothing (SmoothQuant), or quantization-aware fine-tuning — but does not address the root cause.

The core challenge is: **how to prevent Transformers from learning activation outliers during pre-training, enabling simple per-tensor INT8 quantization without additional workarounds.**

---

## Problem Solutions

The paper identifies a causal mechanism linking outliers to specific attention head behavior and proposes two independent, drop-in modifications to the attention mechanism:

1. **Root cause identification.** Certain attention heads learn to perform a "no-op" — not updating the hidden representation via the residual connection. To achieve this, they concentrate attention on low-information tokens (e.g., [SEP], periods, commas in BERT; background patches in ViT) learned to have small Value outputs. However, softmax can never output exact zeros (requiring infinite input dynamic range), so the FFN output in the preceding layer must grow to very large magnitudes to produce sufficiently peaked softmax inputs after LayerNorm normalization. This creates the outliers.

2. **Clipped softmax.** Replace softmax with a stretched-and-clipped variant that can represent exact zeros (and exact ones) with finite input range, breaking the positive feedback loop that grows outliers.

3. **Gated attention.** Add a lightweight per-head sigmoid gate that element-wise multiplies the attention output, giving the model an explicit mechanism to suppress or nullify updates without relying on softmax to produce near-zero values.

---

## Approach Details

### Method

#### Clipped Softmax

Standard softmax output is stretched from (0, 1) to (gamma, zeta) and then clipped back to [0, 1]:

> clipped_softmax(x; zeta, gamma) := clip( (zeta - gamma) * softmax(x) + gamma, 0, 1 )

where zeta >= 1 is the upper stretch factor and gamma <= 0 is the lower stretch factor. When gamma < 0, softmax values smaller than (-gamma) / (zeta - gamma) are clipped to exactly zero. Once clipped, these values produce no gradient, breaking the positive feedback loop that drives outlier growth (Section 4.1, Equation 4).

#### Gated Attention

A learned per-head gate multiplies the attention output:

> Gated_attention(x) := sigmoid(G(x)) * softmax( Q(x) K(x)^T / sqrt(d_head) ) V(x)

where G is a learned gating function operating independently per head. For each head i, a gating function G_i: R^{d_head} -> R produces a scalar per token position:

> pi_hat_{i,t} = G_i(x_{i,t,:})
> pi_{i,:} = sigmoid(pi_hat_{i,:})

The gating modules are shared across token positions but not across heads (Section 4.2, Equations 5--7).

### Key Technical Components

**Why softmax cannot produce zeros.** From the definition of softmax:

> softmax(x)_i = 0  <=>  there exists j != i such that x_j - x_i = +infinity

Even approximating zero requires a very large dynamic range in the softmax input. Since LayerNorm normalizes activations, the FFN output in the previous layer must have very high magnitude to produce a sufficiently large dynamic range after normalization. The partial derivative dy_i/dx_j != 0 for all i, j, so softmax always back-propagates a non-zero gradient signal, driving outliers to grow stronger throughout training (Section 3, footnote 5).

**Outlier localization.** In BERT-base, >97% of outliers correlate with delimiter token positions ([SEP], ".", ","). The dominant outlier dimensions (#180, #720) correspond to attention heads #3 and #12 (with n_heads = 12, d_head = 64). In ViT-S/16, >99% of outliers occur in only 10 hidden dimensions (primarily #48 and #43, corresponding to attention head #1), and outlier patches correlate with uninformative background regions (Section 3, Figure 1, Appendix A).

**Clipped softmax parameterization.** The authors find that only gamma < 0 matters; zeta > 1 has negligible effect (Table 1, Table 8, Section 5.1). To generalize across sequence lengths, gamma is parameterized as gamma = -alpha/T, where T is the sequence length and alpha in [2, 4] works well across T in {32, 64, 128, 192, 256} (Section 5.2, Figure 6).

**Gating architecture variants.** Three parameterizations are evaluated (Table 4):

| Configuration | G | Extra params per layer | Extra token equiv. |
|---|---|---|---|
| Linear | n_heads x Linear(d_head -> 1) | n_heads(d_head + 1) | ~1 |
| MLP | n_heads x MLP(d_head -> n_hid -> 1) | n_heads(n_hid(d_head + 2) + 1) | ~n_hid |
| All-heads-linear | Linear(d_model -> n_heads) | n_heads(d_model + 1) | ~n_heads |

The Linear variant adds ~0.009% extra parameters for BERT-base. Bias initialization b_init controls the initial gating probability pi_init = sigmoid(b_init); effective ranges are [0.25, 0.9] for BERT and [0.1, 0.5] for ViT (Section 5.3, Figure 7).

**Architectural fixes for specific models.** Applying weight decay to LayerNorm gamma weights (not default) reduces outliers independently for OPT. Adding LayerNorm after patch embeddings (absent by default) dramatically reduces outliers for ViT: max infinity norm drops from 358.5 to 81.1, kurtosis from 1018.3 to 24.5, W8A8 accuracy improves from 69.24% to 79.62% even for vanilla attention (Table 7, Appendix B.3--B.4).

### Experimental Setup

**Models:** BERT-base-uncased (109M parameters, 12 layers, n_heads=12, d_head=64), OPT-125m/350m/1.3B (decoder, causal LM), ViT-S/16 (22M parameters, 16x16 patches). All models trained from scratch except OPT-1.3B fine-tuning experiment.

**BERT pre-training:** BookCorpus + English Wikipedia, max sequence length 128, MLM with masking p=0.15, batch size 256, 10^6 steps, AdamW with max LR=10^-4, warmup 10^4 steps, linear decay, weight decay 0.01, FP16 mixed precision.

**OPT-125m pre-training:** BookCorpus + Wikipedia, sequence length 512, batch size 48 with 4 gradient accumulation steps (effective 192), 125,000 steps, AdamW with (beta1, beta2) = (0.9, 0.95), max LR = 4*10^-4, weight decay 0.1, single A100 80GB GPU. OPT-350m and OPT-1.3B: 10^5 steps, batch size 256.

**ViT pre-training:** ImageNet-1K, resolution 224x224, batch size 512, 300 epochs, AdamW with weight decay 0.03, cosine LR schedule, RandAugment, Mixup, CutMix, label smoothing 0.1.

**Quantization:** 8-bit uniform affine PTQ — symmetric weights, asymmetric activations, static activation range. All weights and activations quantized except final linear layer. Weight range: min-max (BERT, ViT) or MSE (OPT). Activation range: running min-max with 0.9 momentum over 16 calibration batches. Each PTQ experiment repeated 3 times (different calibration subsets); each network trained 2 times (different random seeds).

**Hardware:** Nvidia A100 80GB GPUs. Total compute: ~320 GPU days for main results, ~1400 GPU days total including ablations (Table 11, Appendix D).

### Key Results

**Main results (Table 2):**

| Model | Method | FP perf. | Max inf. norm | Avg. kurtosis | W8A8 perf. |
|---|---|---|---|---|---|
| BERT (ppl) | Vanilla | 4.49 +/- 0.01 | 735 +/- 55 | 3076 +/- 262 | 1294 +/- 1046 |
| | Clipped softmax | **4.39 +/- 0.00** | **21.5 +/- 1.5** | **80 +/- 6** | **4.52 +/- 0.01** |
| | Gated attention | 4.45 +/- 0.03 | 39.2 +/- 26.0 | 201 +/- 181 | 4.65 +/- 0.04 |
| OPT-125m (ppl) | Vanilla | 15.84 +/- 0.05 | 340 +/- 47 | 1778 +/- 444 | 21.18 +/- 1.89 |
| | Clipped softmax | 16.29 +/- 0.07 | 63.2 +/- 8.8 | 19728 +/- 7480 | 37.20 +/- 2.40 |
| | Gated attention | **15.55 +/- 0.05** | **8.7 +/- 0.6** | **18.9 +/- 0.9** | **16.02 +/- 0.07** |
| ViT-S/16 (acc %) | Vanilla | 80.75 +/- 0.10 | 359 +/- 81 | 1018 +/- 471 | 69.24 +/- 6.93 |
| | Clipped softmax | 80.89 +/- 0.13 | **73.7 +/- 14.9** | **22.9 +/- 1.6** | 79.77 +/- 0.25 |
| | Gated attention | **81.01 +/- 0.06** | 79.8 +/- 0.5 | **19.9 +/- 0.3** | **79.82 +/- 0.11** |

- Both methods maintain or improve floating-point performance while drastically reducing outliers.
- Clipped softmax is the strongest method for BERT (W8A8 ppl gap: 0.13 from FP16).
- Gated attention is the only method that works for OPT (clipped softmax fails on OPT, increasing kurtosis to 19728).
- Gated attention achieves the best ViT results (W8A8 accuracy within 1.19% of FP32).

**Scaling to larger OPT models (Table 3):**

| Model | Method | FP16 ppl | Max inf. norm | Avg. kurtosis | W8A8 ppl |
|---|---|---|---|---|---|
| OPT-350m | Vanilla | 13.19 | 253 | 2689 | 37.52 +/- 3.84 |
| | Gated attention | 13.01 | 65.4 | 261 | **14.42 +/- 0.06** |
| OPT-1.3B | Vanilla | 12.13 | 428 | 2756 | 989.6 +/- 175 |
| | Gated attention | 12.21 | 67.2 | 444 | **29.95 +/- 0.42** |

- At OPT-1.3B scale, vanilla W8A8 is catastrophic (ppl 989.6); gated attention brings it to 29.95.

**Low-bit quantization on BERT (Table 10):**

| Bitwidths | Weight range | Vanilla | Clipped softmax | Gated attention |
|---|---|---|---|---|
| W8A8 | min-max | 1294 +/- 1046 | 4.52 +/- 0.01 | 4.65 +/- 0.04 |
| W6A8 | MSE | 6.49 +/- 0.38 | 4.56 +/- 0.01 | 4.71 +/- 0.03 |
| W4A8 | MSE | 6.52 +/- 0.02 | 4.90 +/- 0.02 | 5.02 +/- 0.03 |
| W6A6 | MSE | 42.8 +/- 11.7 | 6.64 +/- 0.14 | 5.90 +/- 0.11 |

**Compute overhead (Table 11):**

| Model | Vanilla | Clipped softmax | Gated attention (Linear) |
|---|---|---|---|
| BERT | 92.8 h | 93.6 h (+0.9%) | 97.7 h (+5.3%) |
| OPT | 53.6 h | 54.4 h (+1.5%) | 55.7 h (+3.9%) |
| ViT | 101.8 h | 104.0 h (+2.2%) | 110.8 h (+8.8%) |

### Clipped Softmax: gamma vs. zeta Ablation

Only gamma < 0 (enabling exact zeros) reduces outliers. Setting zeta > 1 alone (enabling exact ones) yields results similar to vanilla softmax. Combining both yields results similar to gamma < 0 alone. Confirmed on both BERT (Table 1) and ViT (Table 8, Section 5.1).

### Fine-Tuning Existing Models

OPT-1.3B pre-trained checkpoint fine-tuned with gated attention for 4000 steps (b_init=0, gating probability multiplied by 2, small FFN output activation regularization):

| Method | FP16 ppl | Max inf. norm | Avg. kurtosis |
|---|---|---|---|
| Vanilla fine-tuning | 29.46 | 79.3 | 2086 |
| Fine-tuning w/ gated attention | 29.18 | 50.9 | 665 |

Fine-tuning reduces outliers without training from scratch, though improvements are smaller than pre-training with the method (Table 9, Appendix B.6).

---

## Limitations and Failure Modes

- **Clipped softmax fails on OPT.** Applying clipped softmax to OPT-125m increases kurtosis from 1777 to 19727 and worsens W8A8 perplexity from 21.18 to 37.22, despite reducing max infinity norm. The authors state: "At the moment, we do not have an explanation of why this is the case and leave it for future work" (Table 6, Section 4.3).

- **Scalability beyond 1.3B not validated.** All pre-training experiments use models up to 1.3B parameters. Whether the same benefits hold for very large models trained for significantly longer is not demonstrated (Section 6).

- **Requires training from scratch.** The full benefits require pre-training with the modified attention mechanism. Fine-tuning an existing model (Appendix B.6) partially reduces outliers but is less effective than training from scratch.

- **Hyperparameter sensitivity.** Both methods introduce a hyperparameter each: gamma (or alpha) for clipped softmax, pi_init for gated attention. While the effective ranges are reasonably wide (alpha in [2, 4]; pi_init in [0.1, 0.9] depending on model), optimal values differ across architectures.

- **[Inferred]** **ViT outlier source extends beyond attention.** In ViT, distinct outliers already originate after patch embeddings (before the attention mechanism). Adding LayerNorm after patch embeddings addresses this independently; the proposed attention modifications provide incremental improvement on top (Table 7). The authors note this observation but do not explicitly flag it as a limitation of their attention-focused approach.

- **FP performance improvements are small.** The authors note: "We show a very small improvement in FP16/FP32 performance due to our methods, but we do not deem our results exhaustive enough to claim that this will hold in general" (Section 6).

- **[Inferred]** No evaluation on non-English languages or tasks beyond MLM perplexity and image classification accuracy, limiting generalizability claims for downstream NLP tasks.

### Scope and Comparability

- **What was not tested:** Models larger than 1.3B parameters trained from scratch; decoder-only models beyond the OPT family (e.g., LLaMA, GPT); tasks beyond MLM perplexity, CLM perplexity, and ImageNet top-1 accuracy (no downstream fine-tuning evaluation with the proposed methods); non-English data; quantization schemes beyond uniform affine (e.g., non-uniform, mixed-precision); dynamic activation quantization (only static range estimation used).
- **Comparability notes:** The paper trains all models from scratch on BookCorpus + Wikipedia (not the original OPT training data), making direct comparison to publicly released OPT checkpoints imprecise. The ViT experiments add LayerNorm after patch embeddings (not standard), which independently reduces outliers -- the vanilla ViT baseline without this LN has much worse W8A8 performance (69.24%) than vanilla with LN (79.62%), complicating attribution of improvements to the proposed methods vs. the LN fix. The quantization setup uses per-tensor granularity, which is the most challenging setting; per-channel or per-group quantization would likely reduce the gap between vanilla and proposed methods.

---

## Conclusions

### Contributions

1. **Identified the causal mechanism linking attention head behavior to activation outliers.** Certain attention heads learn to perform no-ops by concentrating attention on low-information tokens with small Value outputs. Softmax's inability to produce exact zeros forces ever-larger input magnitudes via LayerNorm, creating outliers in FFN outputs. This is supported by >97% outlier-delimiter correlation in BERT and >99% concentration in 10 hidden dimensions in ViT (Section 3, Figures 1--3).

2. **Proposed clipped softmax as a drop-in attention modification.** By stretching and clipping softmax outputs to allow exact zeros, outliers are eliminated with negligible compute overhead (<2.2% training time increase). On BERT, max infinity norm drops from 735 to 21.5 and W8A8 perplexity from 1294 to 4.52 while FP16 perplexity improves from 4.49 to 4.39 (Table 2, Section 4.1).

3. **Proposed gated attention as a universal outlier-prevention mechanism.** A lightweight per-head sigmoid gate (~0.009% extra parameters for BERT) enables explicit no-op behavior. Unlike clipped softmax, gated attention works across all tested architectures including OPT decoders and ViT (Table 2, Table 3, Section 4.2).

4. **Enabled full INT8 quantization without workarounds.** Both methods close the gap between quantized and floating-point performance using simple per-tensor symmetric/asymmetric PTQ, without requiring mixed-precision, activation smoothing, or quantization-aware training (Tables 2--3, Table 10).

5. **Demonstrated scalability to OPT-1.3B and effectiveness for low-bit quantization.** Gated attention reduces OPT-1.3B W8A8 perplexity from 989.6 to 29.95 (Table 3). Both methods improve quantized performance down to W4A8 and W6A6 (Table 10).

### Implications

1. **Softmax has under-appreciated structural consequences.** The sum-to-one constraint forces models to develop workarounds (concentrating residual probability on globally visible tokens) that produce quantization outliers. This implies that any SoftMax-based Transformer will tend to develop outliers, motivating architectural alternatives. [Inference: this connects to the attention sink phenomenon identified concurrently by Xiao et al. (2024).]

2. **Pre-training decisions affect deployment efficiency.** The methods demonstrate that small architectural changes during pre-training can eliminate a major deployment bottleneck (quantization difficulty) with negligible training cost. Future model releases could incorporate gated attention to improve quantizability.

3. **Clipped softmax and gated attention are orthogonal to post-hoc quantization methods.** The authors explicitly note compatibility with SmoothQuant, GPTQ, AWQ, BRECQ, and Outlier Suppression+. Combining pre-training modifications with advanced quantization techniques may yield further improvements. [Inference: this is unvalidated.]

---

## Key Claims

1. **C1: Attention head no-op behavior causes activation outliers.** Attention heads that do not update the residual concentrate attention on delimiter tokens ([SEP], ".", ",") with small Value outputs. Over 97% of outliers in BERT-base layers #10--#11 correlate with delimiter positions; >99% of ViT outliers occur in 10 hidden dimensions corresponding to head #1 at background patches (Section 3, Figure 1, Appendix A). Status: **supported**.

2. **C2: Clipped softmax eliminates BERT outliers while improving FP perplexity.** With gamma=-0.025, zeta=1: max infinity norm drops from 735 +/- 55 to 21.5 +/- 1.5, average kurtosis from 3076 +/- 262 to 80 +/- 6, W8A8 perplexity from 1294 +/- 1046 to 4.52 +/- 0.01, and FP16 perplexity improves from 4.49 +/- 0.01 to 4.39 +/- 0.00 (Table 2, Table 5). Status: **supported**.

3. **C3: Gated attention works across all tested architectures.** OPT-125m: FP16 ppl improves from 15.84 to 15.55, max inf norm from 340 to 8.7, W8A8 ppl from 21.18 to 16.02 (Table 2). ViT: FP32 acc improves from 80.75% to 81.01%, W8A8 acc from 69.24% to 79.82% (Table 2). OPT-1.3B: W8A8 ppl from 989.6 to 29.95 (Table 3). Status: **supported**.

4. **C4: Both methods enable full INT8 PTQ without workarounds.** Simple per-tensor uniform affine quantization with standard range estimation yields near-FP performance for all models when trained with the proposed methods (Tables 2--3). Status: **supported**.

5. **C5: Clipped softmax fails on OPT.** Kurtosis increases from 1777 +/- 444 to 19728 +/- 7480 despite max inf norm dropping from 340 to 63.2; W8A8 perplexity worsens from 21.18 to 37.22 (Table 6, Section 4.3). The authors provide no explanation. Status: **supported**.

6. **C6: Only gamma < 0 matters for outlier reduction.** Setting zeta > 1 alone yields results similar to vanilla softmax on both BERT (Table 1) and ViT (Table 8). Combining zeta > 1 with gamma < 0 yields results similar to gamma < 0 alone. Status: **supported**.

7. **C7: Methods extend to low-bit quantization.** On BERT at W4A8 (MSE), clipped softmax achieves ppl 4.90 vs vanilla 6.52. At W6A6 (MSE), gated attention achieves ppl 5.90 vs vanilla 42.8 (Table 10). Status: **supported**.

---

## Open Questions

1. **Why does clipped softmax fail on OPT decoder models?** Kurtosis increases dramatically despite reduced max infinity norm. The authors leave this unexplained. Not addressed by subsequent work in this directory.

2. **Do the methods scale to very large models (>1.3B) trained for significantly longer?** Pre-training experiments reach 1.3B parameters; modern LLMs are 10--100x larger with much longer training. Not addressed.

3. **Can clipped softmax and gated attention be combined?** The methods are presented as independent alternatives, but their complementary mechanisms (exact zeros in softmax vs. explicit gating) might yield additional benefits. Not addressed.

4. **Would outlier reduction improve inference beyond quantization?** Smaller activation ranges could benefit mixed-precision inference, pruning, or hardware-specific optimizations. Not addressed.

---

## Core References and Why They Are Referenced

### Outlier Analysis in Transformers

- **Bondarenko et al. (2021)** -- *Understanding and Overcoming Challenges of Efficient Transformer Quantization.* Prior work by the same authors establishing the outlier definition (>6 standard deviations) and documenting the quantization challenge across Transformer families.

- **Dettmers et al. (2022)** -- *GPT3.int8(): 8-bit Matrix Multiplication for Transformers at Scale.* Showed that for large enough models, strong outliers appear after every linear layer. Proposed mixed-precision decomposition as a workaround; Bondarenko et al. instead prevent outliers from forming.

- **Xiao et al. (2022)** -- *SmoothQuant: Accurate and Efficient Post-Training Quantization for Large Language Models.* Post-hoc method that migrates quantization difficulty from activations to weights. Positioned as orthogonal to the proposed pre-training modifications.

- **Kovaleva et al. (2021)** -- *BERT Busters: Outlier Dimensions that Disrupt Transformers.* Identified outlier dimensions in BERT embeddings that disrupt downstream tasks.

### Attention Mechanism Analysis

- **Kovaleva et al. (2019)** -- *Revealing the Dark Secrets of BERT.* Observed attention concentrating on [CLS] and [SEP] tokens in BERT, an early observation related to the no-op attention head behavior identified in this paper.

- **Clark et al. (2019)** -- *What Does BERT Look At?* Complementary BERT attention analysis showing attention concentration on special tokens and punctuation.

### Transformer Architectures Used in Evaluation

- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* BERT-base-uncased is the primary encoder model used for evaluation.

- **Zhang, S. et al. (2022)** -- *OPT: Open Pre-trained Transformer Language Models.* Provides the OPT architecture and training recipe used for decoder language model experiments at 125M, 350M, and 1.3B scales.

- **Dosovitskiy et al. (2020)** -- *An Image Is Worth 16x16 Words.* Provides the ViT-S/16 architecture used for vision transformer experiments.

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer with softmax attention, whose fundamental limitation (inability to output exact zeros) is the root cause identified in this paper.

### Quantization Methodology

- **Jacob et al. (2018)** -- *Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference.* Provides the uniform affine quantization framework used throughout the paper.

- **Nagel et al. (2021)** -- *A White Paper on Neural Network Quantization.* Comprehensive reference for PTQ methodology and best practices applied in the evaluation.

### Technical Inspirations

- **Louizos et al. (2017)** -- *Learning Sparse Neural Networks Through L0 Regularization.* The stretched and clipped sigmoid formulation from L0 regularization inspired the clipped softmax design (stretching a function to allow exact zeros via finite inputs).
