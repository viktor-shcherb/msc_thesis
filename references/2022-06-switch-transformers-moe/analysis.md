---
title: "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity"
authors: "Fedus, Zoph, Shazeer"
year: 2022
venue: "JMLR 2022"
paper_type: journal-paper
categories: ["architecture", "scaling-laws"]
scope: ["mixture-of-experts", "sparse models", "efficient training", "conditional computation"]
benchmarks_used: ["glue", "superglue", "squad", "cnn-dm", "xsum", "triviaqa", "natural-questions", "webqa", "arc", "winogrande", "anli"]
models_introduced: ["switch-transformer"]
models_evaluated: ["transformer-base", "moe-sparsely-gated"]
key_claims:
  - id: C1
    claim: "Switch Transformer achieves 7x pre-training speedup over T5-Base with the same FLOPS per token"
    evidence: "Figure 5, Section 3.2, Table 1"
    status: supported
    scope: "T5-Base scale, 64 experts, 32 TPUv3 cores, C4 pre-training"
    magnitude: "7x wall-clock speedup to reach same perplexity"
  - id: C2
    claim: "Routing to a single expert (k=1) outperforms top-k routing while reducing computation"
    evidence: "Table 1, Section 2.1"
    status: supported
    scope: "FLOP-matched comparison with MoE top-2 routing, 128 experts, C4 pre-training"
    magnitude: "quality -1.561 vs -1.572 Neg. Log Perp.; speed 1000 vs 860 ex/sec at capacity factor 1.0"
  - id: C3
    claim: "Selective float32 precision in the router enables stable bfloat16 training"
    evidence: "Table 2, Section 2.4"
    status: supported
    scope: "Router softmax computation only, 32 expert model"
    magnitude: "Neg. Log Perp. -1.716 (stable) vs -3.780 (diverged) at nearly equal speed (1390 ex/sec)"
  - id: C4
    claim: "Large sparse models can be distilled into dense models preserving ~30% of quality gains"
    evidence: "Tables 6-8, Section 4.2"
    status: supported
    scope: "Switch-Base teachers distilled to T5-Base students, 82-99% compression"
    magnitude: "28-37% quality preservation depending on compression ratio"
  - id: C5
    claim: "Switch Transformer improves over mT5-Base on all 101 languages with mean 5x speedup"
    evidence: "Figures 7-8, Section 4.3"
    status: supported
    scope: "mC4 multilingual pre-training, mSwitch-Base vs mT5-Base"
    magnitude: "improvement on all 101 languages; 91% of languages achieve 4x+ speedup; mean 5x speedup"
  - id: C6
    claim: "Switch-C (1.6T parameters) achieves 4x speedup over T5-XXL"
    evidence: "Table 9, Section 5.6"
    status: supported
    scope: "Pre-training on C4, expert+data parallelism, 2048 experts"
    magnitude: "4x speedup; 0.061 Neg. Log Perp. improvement at 250k steps, 0.087 at 500k steps"
  - id: C7
    claim: "Reduced initialization scale (0.1x) dramatically improves training stability"
    evidence: "Table 3, Section 2.4"
    status: supported
    scope: "32 expert Switch-Base model, 3.5k steps, 3 random seeds"
    magnitude: "quality from -3.60 to -2.72 Neg. Log Perp.; std. dev. from 0.68 to 0.01"
  - id: C8
    claim: "Expert dropout (0.4 at expert layers, 0.1 elsewhere) improves fine-tuning performance"
    evidence: "Table 4, Section 2.4"
    status: supported
    scope: "Switch-Base fine-tuned on GLUE, CNNDM, SQuAD, SuperGLUE"
    magnitude: "GLUE 85.2 vs 84.7 with uniform dropout; best or tied on 3 of 4 tasks"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Switch Transformer modifies the Transformer FFN layer with sparse expert routing"
  - target: 2017-05-moe-sparsely-gated-mixture-experts
    type: extends
    detail: "Switch Transformer simplifies Shazeer et al.'s top-k MoE routing to k=1 and introduces stability techniques"
  - target: 2020-12-gpt-3-few-shot-learners
    type: complementary
    detail: "Both address scaling language models; GPT-3 scales dense parameters while Switch scales sparse experts"
open_questions:
  - question: "How to fully translate upstream pre-training gains to downstream fine-tuning for largest models?"
    addressed_by: null
  - question: "How to stabilize training for Switch-XXL scale models (high FLOPs per token with many experts)?"
    addressed_by: null
  - question: "What is the optimal balance between FLOPs per token and number of parameters for fine-tuning?"
    addressed_by: null
  - question: "Do experts develop semantic specialization, and what do individual experts learn?"
    addressed_by: null
  - question: "Can Switch routing benefit decoder-only architectures beyond encoder-decoder T5?"
    addressed_by: null
  - question: "Can heterogeneous experts (varying sizes) improve adaptive computation?"
    addressed_by: null
---

# Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

**Authors:** William Fedus, Barret Zoph, Noam Shazeer (Google Brain)
**Date:** January 2021, arXiv:2101.03961; JMLR 2022, Vol. 23, No. 120, pp. 1-40

---

## Core Research Problem

Scaling neural language models has proven effective but is computationally expensive. Dense Transformers increase model size by expanding dimensions like `d_model` or `d_ff`, which proportionally increases both parameters and FLOPs per token. Mixture of Experts (MoE) models offer an alternative by activating only a subset of parameters per input, enabling parameter scaling without proportional compute increase. However, prior MoE approaches -- Shazeer et al. (2017) and Lepikhin et al. (2020) (GShard) -- suffered from three key limitations:

1. **Complexity:** Top-k routing requires computing and combining outputs from multiple experts per token.
2. **Communication costs:** Routing tokens to multiple experts increases cross-device communication.
3. **Training instability:** Large sparse models diverge when using efficient low-precision (bfloat16) formats.

Kaplan et al. (2020) established power-law scaling with model size, data, and compute, but treated these as coupled axes. The authors hypothesize that **parameter count is a separately important axis** on which to scale, independent of FLOPs. The core challenge was: **how to simplify MoE routing to enable stable, efficient training of sparse models at massive scale while maintaining or improving quality.**

---

## Problem Solutions

Switch Transformer addresses these issues through a simplified routing strategy and improved training techniques:

1. **Single-expert routing (k=1).** Each token is routed to exactly one expert instead of top-k experts, reducing routing computation, halving expert capacity requirements, and simplifying implementation (Section 2.1).

2. **Selective precision training.** The router's softmax computation uses float32 precision locally while the rest of the model trains in bfloat16, achieving training stability without the communication cost of full float32 (Section 2.4).

3. **Reduced initialization scale.** Weight matrices are initialized with 10x smaller scale (s=0.1 vs standard s=1.0) for truncated normal initialization, improving stability and reducing variance across runs (Section 2.4).

4. **Expert dropout for fine-tuning.** Higher dropout rates (0.4) applied specifically to expert layers during fine-tuning prevent overfitting on small downstream datasets while keeping 0.1 dropout at non-expert layers (Section 2.4).

5. **Simplified load balancing loss.** A single auxiliary loss term replaces the separate load-balancing and importance-weighting losses of Shazeer et al. (2017), encouraging uniform routing across experts (Section 2.2).

---

## Approach Details

### Method

The Switch Transformer replaces the dense feed-forward network (FFN) in each Transformer block with a "Switch FFN layer" containing N experts. For each input token x, a router produces a probability distribution over experts:

> p_i(x) = exp(h(x)_i) / sum_j^N exp(h(x)_j)    (Equation 1)

where h(x) = W_r . x and W_r is the router weight matrix. Unlike prior MoE work using top-k routing, Switch Transformer selects only the single highest-probability expert:

> y = p_i(x) * E_i(x)

where i = argmax p(x). The output is scaled by the router probability p_i(x), maintaining differentiability through the gate value. Contrary to the conjecture of Shazeer et al. (2017) that k > 1 was necessary for non-trivial gradients, the authors show this k=1 simplification preserves model quality and performs better (Section 2.1).

The three benefits of the Switch layer are: (1) reduced router computation, (2) at least halved expert capacity since each token goes to a single expert, and (3) simplified routing implementation and reduced communication costs.

### Key Technical Components

#### Expert Capacity and Token Dropping

Each expert has a fixed batch size (expert capacity) determined by:

> expert_capacity = (tokens_per_batch / num_experts) * capacity_factor    (Equation 3)

A capacity factor > 1.0 provides buffer for uneven token distribution. Tokens exceeding expert capacity are "dropped" and passed through the residual connection without expert processing. The paper uses capacity factors of 1.0-2.0 and observes typically < 1% token dropping with proper load balancing. The impact of capacity factor on quality and speed is studied in Table 1, where **lower capacity factors (1.0, 1.25) perform better** -- important for the large model regime where memory is scarce (Section 2.3).

#### Load Balancing Loss

An auxiliary loss encourages uniform routing across experts:

> loss = alpha * N * sum_{i=1}^{N} f_i * P_i    (Equation 4)

where:
- f_i = (1/T) * sum_{x in B} 1{argmax p(x) = i} -- fraction of tokens dispatched to expert i (non-differentiable) (Equation 5)
- P_i = (1/T) * sum_{x in B} p_i(x) -- fraction of router probability allocated to expert i (differentiable) (Equation 6)
- alpha = 10^-2 (loss coefficient, selected from sweep of 10^-1 to 10^-5)
- N = number of experts

The loss is minimized when both f and P are uniform (1/N for each expert). The scaling by N keeps the loss constant as the number of experts varies, since under uniform routing sum(f_i * P_i) = 1/N (Section 2.2).

#### Selective Precision Training

To enable bfloat16 training while avoiding router instability:
1. Cast router input to float32
2. Compute softmax in float32
3. Recast dispatch/combine tensors to bfloat16 before all-to-all communication

This achieves the speed of bfloat16 training (1390 examples/sec) with the stability of float32 (Neg. Log Perp. -1.716), compared to pure bfloat16 which diverges (Neg. Log Perp. -3.780). Float32 throughout achieves -1.718 at only 1160 examples/sec (Table 2, Section 2.4).

#### Smaller Initialization Scale

Standard Transformer initialization uses scale s=1.0 for truncated normal with sigma = sqrt(s/n) where n is fan-in. Values > 2 standard deviations are resampled. Switch Transformer uses s=0.1, reducing initialization scale by 10x. Results after 3.5k steps with 3 random seeds (Table 3, Section 2.4):

| Model (Initialization scale) | Avg Quality (Neg. Log Perp.) | Std. Dev. |
|---|---|---|
| Switch-Base (0.1x-init) | **-2.72** | **0.01** |
| Switch-Base (1.0x-init) | -3.60 | 0.68 |

This same initialization scheme is broadly effective from the 223M parameter baseline to models in excess of one trillion parameters.

#### Expert Dropout

During fine-tuning, expert FFN layers use dropout rate 0.4 while non-expert layers use 0.1. Full results from Table 4 (Section 2.4), pre-trained on 34B tokens of C4:

| Model (dropout) | GLUE | CNNDM | SQuAD | SuperGLUE |
|---|---|---|---|---|
| T5-Base (d=0.1) | 82.9 | **19.6** | 83.5 | 72.4 |
| Switch-Base (d=0.1) | 84.7 | 19.1 | **83.7** | **73.0** |
| Switch-Base (d=0.2) | 84.4 | 19.2 | **83.9** | **73.2** |
| Switch-Base (d=0.3) | 83.9 | 19.6 | 83.4 | 70.7 |
| Switch-Base (d=0.1, ed=0.4) | **85.2** | 19.6 | **83.7** | **73.0** |

Simply increasing dropout uniformly across all layers leads to worse performance at d=0.3. The selective expert dropout strategy achieves the best GLUE score while matching or exceeding baseline on other tasks.

#### Exploration Across Experts

The router faces an exploration-exploitation dilemma analogous to a contextual bandit (Appendix C). Four strategies were compared (Table 11):

| Strategy | Quality (Neg. Log Perp.) |
|---|---|
| Input jitter | **-1.468** |
| Argmax | -1.471 |
| Input dropout | -1.480 |
| Sample softmax | -1.570 |

Input jitter (multiplicative noise on the incoming representation) performs best and is used throughout the paper. There is no material speed difference between variants.

### Experimental Setup

**Pre-training:**
- Dataset: C4 (Colossal Clean Crawled Corpus), improved version with intra-example deduplication (Lee et al., 2021), 180B+ target tokens
- Objective: Masked language modeling (15% token dropout, sentinel replacement)
- Batch size: 2^20 (1,048,576) tokens
- Training steps: 550k (576B total tokens)
- Hardware: TPUv3 clusters (32-2048 cores)
- Metric: Negative log perplexity (log base-e, units are nats)

**Model configurations (Table 9):**

| Model | Parameters | FLOPs/seq | d_model | d_ff | d_kv | Num. Heads | Num. Layers | Num Experts | Expert Freq. |
|---|---|---|---|---|---|---|---|---|---|
| T5-Base | 0.2B | 124B | 768 | 2048 | 64 | 12 | 12 | -- | -- |
| Switch-Base | 7B | 124B | 768 | 2048 | 64 | 12 | 12 | 128 | 1/2 |
| T5-Large | 0.7B | 425B | 1024 | 2816 | 64 | 16 | 24 | -- | -- |
| Switch-Large | 26B | 425B | 1024 | 2816 | 64 | 16 | 24 | 128 | 1/2 |
| T5-XXL | 11B | 6.3T | 4096 | 10240 | 64 | 64 | 24 | -- | -- |
| Switch-XXL | 395B | 6.3T | 4096 | 10240 | 64 | 64 | 24 | 64 | 1/2 |
| Switch-C | 1571B | 890B | 2080 | 6144 | 64 | 32 | 15 | 2048 | 1 |

All T5 and Switch models use FFN_GEGLU (Shazeer, 2020) except Switch-C. Switch models place experts at every other FFN layer (Expert Freq. = 1/2), except Switch-C which uses experts at every layer. Switch-C is designed using only expert-parallelism (no model-parallelism), so its d_model, d_ff, and head dimensions are smaller than T5-XXL. Switch-XXL is FLOP-matched to T5-XXL.

**Fine-tuning:**
- Batch size: 1M tokens
- Steps: 16k
- Dropout: 0.1 (non-expert), 0.4 (expert)
- Evaluation: every 200 steps, report peak validation performance
- Tasks: GLUE (composite), SuperGLUE (composite), SQuAD, CNNDM, XSum, ARC Easy, ARC Challenge, ANLI, Winogrande, closed-book Natural Questions, Web Questions, TriviaQA

**Reproducibility:** Code released for both JAX/T5X and TensorFlow/Mesh-TF. Pre-training uses 32-2048 TPUv3 cores. Initialization scale and load balancing coefficient (alpha=10^-2) are specified. All models pre-trained on the same improved C4 corpus for fair comparison. Validation sets are used for all reported fine-tuning results (test set performance not reported for most tasks).

### Key Results

#### Pre-training Speed (Table 1, Figures 5-6)

| Model | Capacity Factor | Quality @100k steps (Neg. Log Perp.) | Time to -1.50 (hours) | Speed (ex/sec) |
|---|---|---|---|---|
| T5-Base | -- | -1.731 | Not achieved | 1600 |
| T5-Large | -- | -1.550 | 131.1 | 470 |
| MoE-Base | 2.0 | -1.547 | 68.7 | 840 |
| Switch-Base | 2.0 | -1.554 | 72.8 | 860 |
| MoE-Base | 1.25 | -1.559 | 80.7 | 790 |
| Switch-Base | 1.25 | -1.553 | 65.0 | 910 |
| MoE-Base | 1.0 | -1.572 | 80.1 | 860 |
| Switch-Base | 1.0 | -1.561 | **62.8** | 1000 |
| Switch-Base+ | 1.0 | **-1.534** | 67.6 | 780 |

All models trained on 32 TPUv3 cores with 128 experts at every other FFN layer. Switch-Base+ increases hidden size from 768 to 896 and heads from 14 to 16 to match MoE speed. Three key findings from Table 1 (Section 2.3): (1) Switch Transformers outperform both dense models and MoE on speed-quality basis; (2) Switch has a smaller computational footprint than MoE; (3) Switch performs better at lower capacity factors (1.0, 1.25), important for the memory-scarce large model regime.

Switch-Base 64 expert model achieves the same perplexity as T5-Base in **1/7th the wall-clock time** (Figure 5). Compared to T5-Large (3.5x more FLOPs per token), Switch-Base still achieves a **2.5x speedup** (Figure 6). On a step basis, Switch-Base 64 expert achieves T5-Base quality at step 60k vs step 450k, a ~7.5x speedup (Figure 4, Section 3.1). Scaling is consistent from 2 to 256 experts (tested across 9 expert counts, strong evidence).

#### Downstream Fine-tuning (Table 5)

*Part 1: GLUE, SQuAD, SuperGLUE, Winogrande*

| Model | GLUE | SQuAD | SuperGLUE | Winogrande (XL) |
|---|---|---|---|---|
| T5-Base | 84.3 | 85.5 | 75.1 | 66.6 |
| Switch-Base | **86.7** | **87.2** | **79.5** | **73.3** |
| T5-Large | 87.8 | 88.1 | 82.7 | 79.1 |
| Switch-Large | **88.5** | **88.6** | **84.7** | **83.0** |

*Part 2: XSum, ANLI, ARC Easy, ARC Challenge*

| Model | XSum | ANLI (R3) | ARC Easy | ARC Chal. |
|---|---|---|---|---|
| T5-Base | 18.7 | 51.8 | 56.7 | **35.5** |
| Switch-Base | **20.3** | **54.0** | **61.3** | 32.8 |
| T5-Large | 20.9 | 56.6 | **68.8** | **35.5** |
| Switch-Large | **22.3** | **58.6** | 66.0 | **35.5** |

*Part 3: Closed-Book QA*

| Model | CB Web QA | CB Natural QA | CB Trivia QA |
|---|---|---|---|
| T5-Base | 26.6 | 25.8 | 24.5 |
| Switch-Base | **27.4** | **26.8** | **30.7** |
| T5-Large | 27.7 | 27.6 | 29.5 |
| Switch-Large | **31.3** | **29.5** | **36.9** |

Notable improvements: SuperGLUE +4.4 points (Base), +2.0 points (Large); Winogrande +6.7 points (Base), +3.9 points (Large); closed-book TriviaQA +6.2 points (Base), +7.4 points (Large); XSum +1.6 (Base), +1.4 (Large). The only task where Switch underperforms at Base scale is **ARC Challenge** (32.8 vs 35.5 for T5-Base), and at Large scale Switch-Large underperforms T5-Large on **ARC Easy** (66.0 vs 68.8). All results on validation sets (tested across 11 diverse tasks at 2 model scales, strong evidence).

#### Distillation (Tables 6-7)

Best distillation technique combines: (1) initializing the dense student with non-expert weights from the sparse teacher, and (2) using a mixture of 0.75 ground-truth label loss + 0.25 teacher probability loss (Table 6). Compression rates across model sizes (Table 7):

| Dense | 1.1B sparse | 2.0B sparse | 3.8B sparse | 7.4B sparse | 14.7B sparse |
|---|---|---|---|---|---|
| -1.636 | -1.505 | -1.474 | -1.444 | -1.432 | -1.427 |
| -- | -1.587 | -1.585 | -1.579 | -1.582 | -1.578 |
| -- | 37% | 32% | 30% | 27% | 28% |
| -- | 82% | 90% | 95% | 97% | 99% |

Row 1: pre-trained Neg. Log Perp. Row 2: distilled Neg. Log Perp. Row 3: percent of teacher quality preserved. Row 4: compression percent. All distilled into 223M T5-Base. At 99% compression (14.7B to 223M), 28% of quality gains are preserved (moderate evidence -- single distillation protocol, no variance reported).

Fine-tuned distillation (Table 8): Switch-Base 7.4B fine-tuned on SuperGLUE distilled to T5-Base (223M) preserves 30% of gains (76.6 vs teacher's 81.3 and baseline's 74.6 on SuperGLUE).

#### Multilingual Learning (Figures 7-8)

On 101 languages from mC4 (pre-training for 1M steps):
- mSwitch-Base improves over mT5-Base on **all 101 languages** (Figure 7)
- Mean step speedup: **5x** over mT5-Base
- **91% of languages** achieve **4x+ speedup** (Figure 8)
- Distribution is right-skewed with peak around 6-7x speedup (~48 languages)

This demonstrates Switch Transformers are effective multi-task and multi-lingual learners (tested across 101 languages, strong evidence for breadth).

#### Trillion-Parameter Models (Table 9, Section 5.6)

| Model | Parameters | Neg. Log Perp. @250k | Neg. Log Perp. @500k |
|---|---|---|---|
| T5-XXL | 11B | -1.147 | -1.095 |
| Switch-XXL | 395B | **-1.086** | **-1.008** |
| Switch-C | 1571B | -1.096 | -1.043 |

Switch-XXL outperforms T5-XXL by 0.061 at 250k steps and 0.087 at 500k steps. To contextualize: T5-XXL required an additional 250k steps to improve by only 0.052 (Section 5.6). Switch-C achieves **4x speedup** over T5-XXL to reach the same perplexity. Note: the quality gap at 250k steps is a lower bound because T5-XXL was pre-trained on an easier C4 dataset that included duplicated snippets (footnote 10).

**Reasoning fine-tuning (Switch-XXL, partially pre-trained on 503B tokens):** SQuAD 89.7 (vs SOTA 91.3); SuperGLUE test 87.5 (vs T5 89.3, SOTA 90.0); ANLI 65.7 (new SOTA, vs prior 49.4). **Knowledge fine-tuning (without SSM):** Natural Questions 34.4 (vs 32.8 prior), Web Questions 41.0 (vs 37.2), TriviaQA 47.5 (vs 42.9). Pre-training gains translate better to knowledge tasks than reasoning tasks (limited evidence -- single partially-trained checkpoint, multi-task rather than individual fine-tuning).

### Additional Results

#### Switch for Attention (Appendix A)

Replacing the Q, K, V weight matrices in Self-Attention with expert layers shows quality improvements (Table 10, float32 precision, 32 experts):

| Model | Precision | Quality @100k Steps | Speed (ex/sec) |
|---|---|---|---|
| Experts FF | float32 | -1.548 | 1480 |
| Expert Attention | float32 | -1.524 | 1330 |
| Experts FF + Attention | float32 | **-1.513** | 1240 |

However, expert attention layers **diverge in bfloat16**, preventing practical use. Left as future work.

#### No-Token-Left-Behind Routing (Appendix B)

An iterative rerouting strategy that sends overflowed tokens to their second-highest expert. Despite the intuition that avoiding dropped tokens should help, **no empirical benefits were observed**. The authors suspect that once the network learns token-expert associations, reassigning a token to its second-best expert degrades performance.

#### Low-Compute Regimes (Appendix D)

As few as **2 experts** produce compelling gains over FLOP-matched T5-Base (Figure 12). At 100k steps: 8 experts reaches approximately -1.68 Neg. Log Perp., 4 experts ~-1.72, 2 experts ~-1.75, vs T5-Base ~-1.77. This validates the approach even without supercomputer-scale resources.

#### Upstream-Downstream Correlation (Appendix E)

For SuperGLUE, improved pre-training perplexity loosely correlates with downstream score for both dense and Switch models, but the dense model often performs better at a fixed perplexity in the large-scale regime (Figure 13, left). For TriviaQA, Switch may follow an improved scaling relationship: for a given upstream perplexity, Switch does better than a dense counterpart (Figure 13, right). This suggests **knowledge-heavy tasks benefit more from sparse models** than reasoning tasks at the largest scales (limited evidence -- expensive to collect additional statistics).

---

## Limitations and Failure Modes

**Explicitly acknowledged by authors:**

1. **Training instability at largest scale.** Switch-XXL (395B parameters, 64 experts) exhibits sporadic instability despite stability techniques working for smaller models. Switch-C (1.6T parameters, 2048 experts) is stable, suggesting instability correlates with FLOPs per token rather than parameter count alone. The authors tried regularizers and adapted gradient clipping but the issue remains unsolved (Sections 5.6, 8).

2. **Upstream-downstream gap for largest models.** Despite superior pre-training perplexity, Switch-C (1.6T) achieves only 87.7 exact match on SQuAD, which compares unfavorably to 89.6 for the smaller Switch-XXL (395B). Switch-XXL applies approximately 10x the FLOPs per token but has approximately 4x fewer unique parameters (395B vs 1.6T). The paper notes "a poorly understood dependence between fine-tuning quality, FLOPS per token and number of parameters" (Section 8).

3. **Fine-tuning regularization required.** Sparse models overfit more severely on small downstream tasks due to higher parameter count. Expert dropout mitigates but does not fully resolve this (Section 2.4, Table 4).

4. **ARC Challenge regression.** T5-Base outperforms Switch-Base on ARC Challenge (35.5 vs 32.8), and T5-Large outperforms Switch-Large on ARC Easy (68.8 vs 66.0) -- the only tasks where Switch underperforms (Table 5).

5. **Expert attention instability in bfloat16.** Adding expert layers to Self-Attention diverges in bfloat16 precision, preventing practical deployment (Table 10, Appendix A).

6. **No-Token-Left-Behind provides no benefit.** The iterative rerouting strategy to avoid dropped tokens showed no empirical improvement (Appendix B).

**[Inferred]** limitations not explicitly acknowledged:

- **[Inferred]** All downstream results use validation sets; test set performance is not reported for most tasks, limiting comparability with published results on test sets.
- **[Inferred]** All experiments use T5-based encoder-decoder architecture; generalization to decoder-only models is not demonstrated.
- **[Inferred]** Expert specialization is not analyzed -- the paper does not examine what individual experts learn or whether they develop semantic specialization.
- **[Inferred]** Only English pre-training corpus (C4) used for main experiments; multilingual results use mC4 but no analysis of cross-lingual transfer dynamics.

### Scope and Comparability

- **Evaluation regime:** Pre-training on C4 only; no comparison with other pre-training corpora (e.g., the Pile, RedPajama).
- **Hardware-specific:** All experiments on TPUv3; GPU performance characteristics may differ, particularly for the all-to-all communication patterns in expert routing.
- **Batch size dependency:** Expert capacity formula (Equation 3) assumes large batch sizes (2^20 tokens); performance at small batch sizes is unclear.
- **Architecture scope:** Only encoder-decoder T5 architecture tested. Decoder-only (GPT-style) models not evaluated, limiting comparisons with GPT-3 and subsequent work.
- **Fine-tuning protocol:** Uses multi-task training for the largest models rather than individual task fine-tuning, which differs from standard T5 fine-tuning and may affect comparability.
- **MoE comparison scope:** Only compared against MoE top-2 routing (Shazeer et al., 2017) and GShard. No comparison with other sparse routing strategies beyond those.

---

## Conclusions

### Contributions

1. **Simplified MoE routing.** Single-expert routing (k=1) outperforms top-k routing while reducing computation, communication, and implementation complexity. This contradicts the prior conjecture that k>1 was necessary for gradient flow (Table 1, Section 2.1).

2. **Stable sparse training at scale.** The combination of selective float32 precision, reduced initialization (0.1x), and load balancing loss enables training trillion-parameter models in bfloat16. Switch-C (1.6T) trained with no instability (Section 2.4, Section 5.6).

3. **7x pre-training speedup.** FLOP-matched Switch Transformers achieve the same perplexity as dense T5 baselines in 1/7th the training time, and 2.5x faster than T5-Large which uses 3.5x more FLOPs (Figures 5-6).

4. **Consistent downstream improvements.** Significant gains on 9 out of 11 fine-tuning tasks at Base scale, with largest improvements on SuperGLUE (+4.4), Winogrande (+6.7), and closed-book TriviaQA (+6.2) (Table 5).

5. **Effective knowledge distillation.** Large sparse teachers can be compressed 82-99% while preserving 28-37% of quality gains over dense baselines, using weight initialization and mixed hard/soft losses (Tables 6-8).

6. **Universal multilingual improvement.** Switch Transformer improves on all 101 languages in mC4 with 91% achieving 4x+ speedup, demonstrating broad applicability beyond English (Figures 7-8).

7. **Trillion-parameter training.** Combining expert, model, and data parallelism enables training models with 1.6T parameters that achieve 4x speedup over T5-XXL (Table 9, Section 5.6).

### Implications

1. **Parameter count as independent scaling axis.** The paper demonstrates that parameters can be scaled independently of FLOPs, opening a new dimension for model scaling beyond Kaplan et al. (2020). This challenges the assumption that parameters and compute must grow together.

2. **Sparse models for deployment via distillation.** The distillation results suggest a training paradigm: pre-train massive sparse models, then compress to deployable dense models, preserving a meaningful fraction of quality gains.

3. **Routing simplicity suffices.** The success of k=1 routing suggests that sophisticated routing mechanisms may be unnecessary, enabling simpler MoE implementations. [Speculative: this was validated by subsequent MoE work including Mixtral (Jiang et al., 2024) and DeepSeekMoE (Dai et al., 2024).]

4. **Low-compute applicability.** Even 2-expert models improve over dense baselines (Appendix D), making sparse models accessible beyond supercomputer settings.

---

## Key Claims

1. **C1: 7x pre-training speedup.** Switch-Base with 64 experts achieves the same perplexity as T5-Base in 1/7th the wall-clock time on identical hardware (32 TPUv3 cores). Evidence: Figure 5, red dashed line showing "7x Speedup" (Section 3.2). Scope: T5-Base scale, C4 pre-training, 32 TPUv3 cores. Status: **supported** (tested across multiple expert counts from 2 to 256, consistent improvement -- strong evidence).

2. **C2: Single-expert routing outperforms top-k.** At capacity factor 1.0, Switch-Base (-1.561) outperforms MoE-Base top-2 (-1.572) on quality while being faster (1000 vs 860 ex/sec). At all three capacity factors tested (2.0, 1.25, 1.0), Switch matches or outperforms MoE. Evidence: Table 1 (Section 2.3). Scope: FLOP-matched, 128 experts, C4 pre-training. Magnitude: 0.011 Neg. Log Perp. improvement + 16% speed increase at CF=1.0. Status: **supported** (3 capacity factors compared, single architecture -- moderate evidence).

3. **C3: Selective precision enables bfloat16 training.** Pure bfloat16 diverges (-3.780) while selective float32 precision in the router achieves stable training (-1.716) at bfloat16 speed (1390 ex/sec). Float32 throughout achieves -1.718 at 1160 examples/sec. Evidence: Table 2 (Section 2.4). Scope: 32-expert model, early training. Magnitude: prevented divergence while maintaining 1390 ex/sec vs 1160 for full float32. Status: **supported** (single experiment at one model size -- limited evidence, but divergence vs. stability is unambiguous).

4. **C4: 28-37% quality preservation at 82-99% compression.** Distilling Switch-Base teachers (1.1B to 14.7B) into 223M T5-Base students preserves 28-37% of quality improvement. Best technique: initialize with non-expert weights + 0.75/0.25 hard/soft loss mixture. Evidence: Tables 6-7 (Section 4.2). Scope: Switch-Base teacher models only, single student size (223M). Magnitude: 37% preserved at 82% compression, 28% at 99% compression. Status: **supported** (5 teacher sizes tested, single distillation protocol -- moderate evidence).

5. **C5: Improvement on all 101 languages.** mSwitch-Base improves final perplexity over mT5-Base on every language in mC4 with mean 5x speedup and 91% of languages achieving 4x+ speedup. Evidence: Figures 7-8 (Section 4.3). Scope: mC4 multilingual pre-training, 1M steps, mSwitch-Base vs mT5-Base. Magnitude: universal improvement, mean 5x step speedup. Status: **supported** (101 languages tested -- strong evidence for breadth).

6. **C6: 4x speedup at trillion scale.** Switch-C (1.6T) reaches -1.095 perplexity 4x faster than T5-XXL, and improves by 0.061 Neg. Log Perp. at 250k steps. Evidence: Table 9 (Section 5.6). Scope: pre-training on C4, expert+data parallelism, 2048 experts. Magnitude: 4x speedup, 0.087 improvement at 500k steps. Status: **supported** (single run comparison -- limited evidence for the specific 4x claim, but the perplexity gap is documented at two checkpoints).

7. **C7: Reduced initialization scale improves stability.** Using s=0.1 instead of s=1.0 improves average quality from -3.60 to -2.72 and reduces standard deviation from 0.68 to 0.01 across 3 random seeds. Evidence: Table 3 (Section 2.4). Scope: 32 expert Switch-Base model, 3.5k steps early in training. Magnitude: 0.88 Neg. Log Perp. improvement, 68x variance reduction. Status: **supported** (3 seeds at one model size, early training only -- moderate evidence).

8. **C8: Expert dropout improves fine-tuning.** Differential dropout (0.1 non-expert, 0.4 expert) achieves 85.2 GLUE vs 84.7 for uniform 0.1 dropout and 83.9 for uniform 0.3 dropout. Evidence: Table 4 (Section 2.4). Scope: Switch-Base fine-tuned on 4 tasks after 34B token pre-training. Magnitude: +0.5 GLUE, matched or improved on 3 of 4 tasks. Status: **supported** (4 tasks, single model -- moderate evidence).

---

## Open Questions

1. **How to stabilize Switch-XXL scale training?** The 395B parameter model with 64 experts shows sporadic instability despite techniques that work for smaller models. Switch-C (1.6T, 2048 experts) is stable, suggesting the issue relates to FLOPs per token rather than parameters. Not addressed.

2. **What explains the upstream-downstream gap for largest models?** Switch-C has better pre-training perplexity but worse fine-tuning performance than Switch-XXL on reasoning tasks. The relationship between FLOPs, parameters, and fine-tuning quality remains unclear. Not addressed.

3. **What is the optimal balance between FLOPs per token and number of parameters for fine-tuning?** The paper identifies this as "a poorly understood dependence" (Section 8). Not addressed.

4. **Do experts develop semantic specialization?** The paper does not analyze expert activations or whether experts develop specialization. Addressed by subsequent work on expert specialization analysis.

5. **Can Switch routing benefit decoder-only architectures?** All experiments use encoder-decoder T5; applicability to GPT-style models not demonstrated. Partially addressed by subsequent MoE decoder models (Mixtral, DeepSeekMoE).

6. **Can heterogeneous experts improve adaptive computation?** The paper uses identical, homogeneous experts but suggests heterogeneous experts of varying sizes as future work (Section 8). Not addressed.

---

## Core References and Why They Are Referenced

### Mixture of Experts Foundations

- **Jacobs et al. (1991)** -- *Adaptive Mixtures of Local Experts.* Originated the Mixture of Experts paradigm. Switch Transformer is a modern descendant of this framework.

- **Shazeer et al. (2017)** -- *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer.* Introduced MoE for NLP with top-k routing, load balancing loss, and importance weighting. Switch Transformer directly simplifies this to k=1 routing while keeping the load balancing objective (with simplified single loss).

- **Lepikhin et al. (2020)** -- *GShard: Scaling Giant Models with Conditional Computation.* Scaled MoE to 600B parameters for multilingual translation using the XLA compiler. Switch Transformer addresses GShard's training instability with selective precision and improved initialization.

### Scaling Laws

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Established power-law relationships between model size, data, compute, and performance. Switch Transformer proposes parameters as a fourth independent axis for scaling.

### Baseline Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that Switch Transformer modifies by replacing dense FFN with sparse Switch FFN layers.

- **Raffel et al. (2019)** -- *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5).* Provides the base architecture, pre-training setup, and C4 corpus. All Switch models are compared against T5 baselines.

### Training Infrastructure

- **Shazeer et al. (2018)** -- *Mesh-TensorFlow: Deep Learning for Supercomputers.* The distributed computing framework used for implementing expert parallelism, tensor sharding, and all-to-all communication primitives.

### Distillation

- **Hinton et al. (2015)** -- *Distilling the Knowledge in a Neural Network.* The knowledge distillation framework adapted for compressing sparse models into dense students.

- **Sanh et al. (2019)** -- *DistilBERT.* Distillation techniques for BERT that Switch Transformer builds on for sparse-to-dense distillation (weight initialization + mixed hard/soft loss).

### Evaluation Benchmarks

- **Wang et al. (2018, 2019)** -- *GLUE* and *SuperGLUE.* Multi-task benchmarks for evaluating language understanding. Switch Transformer shows consistent improvements across these composite benchmarks.

- **Rajpurkar et al. (2016)** -- *SQuAD.* Question answering benchmark used for fine-tuning evaluation.

### Multilingual

- **Xue et al. (2020)** -- *mT5: A Massively Multilingual Pre-trained Text-to-Text Transformer.* Provides the mT5 baseline and mC4 multilingual corpus that Switch Transformer improves upon across all 101 languages.
