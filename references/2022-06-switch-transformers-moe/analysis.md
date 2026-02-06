---
title: "Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity"
authors: "Fedus, Zoph, Shazeer"
year: 2022
venue: "JMLR 2022"
paper_type: journal-paper
categories: ["architecture", "scaling-laws"]
scope: ["mixture-of-experts", "sparse models", "efficient training", "conditional computation"]
benchmarks_used: ["glue", "squad", "cnndm", "triviaqa", "natural-questions", "arc", "winogrande"]
models_introduced: ["switch-transformer"]
models_evaluated: ["transformer-base"]
key_claims:
  - id: C1
    claim: "Switch Transformer achieves 7x pre-training speedup over T5-Base with the same FLOPS per token"
    evidence: "Figure 5, Section 3.2, Table 1"
    status: supported
    scope: "T5-Base scale, 128 experts, C4 pre-training"
    magnitude: "7x speedup to reach same perplexity"
  - id: C2
    claim: "Routing to a single expert (k=1) outperforms top-k routing while reducing computation"
    evidence: "Table 1, Section 2.1"
    status: supported
    scope: "FLOP-matched comparison with MoE top-2 routing"
  - id: C3
    claim: "Selective float32 precision in the router enables stable bfloat16 training"
    evidence: "Table 2, Section 2.4"
    status: supported
    scope: "Router softmax computation only"
  - id: C4
    claim: "Large sparse models can be distilled into dense models preserving ~30% of quality gains"
    evidence: "Tables 6-8, Section 4.2"
    status: supported
    scope: "99% parameter compression"
    magnitude: "30% quality preservation"
  - id: C5
    claim: "Switch Transformer improves over mT5-Base on all 101 languages with mean 5x speedup"
    evidence: "Figures 7-8, Section 4.3"
    status: supported
    scope: "mC4 multilingual pre-training"
    magnitude: "91% of languages achieve 4x+ speedup"
  - id: C6
    claim: "Switch-C (1.6T parameters) achieves 4x speedup over T5-XXL"
    evidence: "Table 9, Section 5.6"
    status: supported
    scope: "Pre-training on C4, same compute budget"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Switch Transformer modifies the Transformer FFN layer with sparse expert routing"
  - target: 2020-12-gpt-3-few-shot-learners
    type: complementary
    detail: "Both address scaling language models; GPT-3 scales dense parameters while Switch scales sparse experts"
open_questions:
  - question: "How to fully translate upstream pre-training gains to downstream fine-tuning for largest models?"
    addressed_by: null
  - question: "How to stabilize training for Switch-XXL scale models?"
    addressed_by: null
  - question: "What is the optimal balance between FLOPs per token and number of parameters for fine-tuning?"
    addressed_by: null
---

# Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

**Authors:** William Fedus, Barret Zoph, Noam Shazeer (Google Brain)
**Date:** January 2021, arXiv:2101.03961; JMLR 2022, Vol. 23, No. 120, pp. 1-40

---

## Core Research Problem

Scaling neural language models has proven effective but is computationally expensive. Dense Transformers increase model size by expanding dimensions like `d_model` or `d_ff`, which proportionally increases both parameters and FLOPs per token. Mixture of Experts (MoE) models offer an alternative by activating only a subset of parameters per input, enabling parameter scaling without proportional compute increase. However, prior MoE approaches (Shazeer et al., 2017; Lepikhin et al., 2020) suffered from three key limitations:

1. **Complexity:** Top-k routing requires computing and combining outputs from multiple experts per token.
2. **Communication costs:** Routing tokens to multiple experts increases cross-device communication.
3. **Training instability:** Large sparse models diverge when using efficient low-precision (bfloat16) formats.

The core challenge was: **how to simplify MoE routing to enable stable, efficient training of sparse models at massive scale while maintaining or improving quality.**

---

## Problem Solutions

Switch Transformer addresses these issues through a simplified routing strategy and improved training techniques:

1. **Single-expert routing (k=1).** Each token is routed to exactly one expert instead of top-k experts, reducing routing computation, halving expert capacity requirements, and simplifying implementation.

2. **Selective precision training.** The router's softmax computation uses float32 precision locally while the rest of the model trains in bfloat16, achieving training stability without the communication cost of full float32.

3. **Reduced initialization scale.** Weight matrices are initialized with 10x smaller scale than standard Transformers, improving stability and reducing variance across runs.

4. **Expert dropout for fine-tuning.** Higher dropout rates (0.4) applied specifically to expert layers during fine-tuning prevent overfitting on small downstream datasets.

---

## Approach Details

### Method

The Switch Transformer replaces the dense feed-forward network (FFN) in each Transformer block with a "Switch FFN layer" containing N experts. For each input token x, a router produces a probability distribution over experts:

> p_i(x) = exp(h(x)_i) / sum_j exp(h(x)_j)

where h(x) = W_r * x and W_r is the router weight matrix. Unlike prior MoE work using top-k routing, Switch Transformer selects only the single highest-probability expert:

> y = p_i(x) * E_i(x)

where i = argmax p(x). The output is scaled by the router probability, maintaining differentiability through the gate value.

### Key Technical Components

#### Expert Capacity and Token Dropping

Each expert has a fixed batch size (expert capacity) determined by:

> expert_capacity = (tokens_per_batch / num_experts) * capacity_factor

A capacity factor > 1.0 provides buffer for uneven token distribution. Tokens exceeding expert capacity are "dropped" and passed through the residual connection without expert processing. The paper uses capacity factors of 1.0-2.0 and observes <1% token dropping with proper load balancing.

#### Load Balancing Loss

An auxiliary loss encourages uniform routing across experts:

> loss = alpha * N * sum_i(f_i * P_i)

where:
- f_i = fraction of tokens dispatched to expert i (non-differentiable)
- P_i = fraction of router probability allocated to expert i (differentiable)
- alpha = 10^-2 (loss coefficient)
- N = number of experts

The loss is minimized when both f and P are uniform (1/N for each expert).

#### Selective Precision Training

To enable bfloat16 training while avoiding router instability:
1. Cast router input to float32
2. Compute softmax in float32
3. Recast dispatch/combine tensors to bfloat16 before communication

This achieves the speed of bfloat16 training (1390 examples/sec) with the stability of float32 (-1.716 Neg. Log Perp.), compared to pure bfloat16 which diverges (Table 2).

#### Smaller Initialization Scale

Standard Transformer initialization uses scale s=1.0 for truncated normal with sigma = sqrt(s/n). Switch Transformer uses s=0.1, reducing initialization scale by 10x. This improves average quality from -3.60 to -2.72 Neg. Log Perp. and reduces standard deviation from 0.68 to 0.01 across random seeds (Table 3).

#### Expert Dropout

During fine-tuning, expert FFN layers use dropout rate 0.4 while non-expert layers use 0.1. This outperforms uniform dropout (Table 4):

| Dropout Configuration | GLUE | SuperGLUE |
|---|---|---|
| Uniform d=0.1 | 84.7 | 73.0 |
| Uniform d=0.2 | 84.4 | 73.2 |
| d=0.1 non-expert, d=0.4 expert | **85.2** | **73.0** |

### Experimental Setup

**Pre-training:**
- Dataset: C4 (Colossal Clean Crawled Corpus), 180B+ target tokens
- Objective: Masked language modeling (15% token dropout, sentinel replacement)
- Batch size: 2^20 (1,048,576) tokens
- Training steps: 550k (576B total tokens)
- Hardware: TPUv3 clusters (32-2048 cores)

**Model configurations (Table 9):**

| Model | Parameters | FLOPs/seq | Experts | Layers |
|---|---|---|---|---|
| T5-Base | 0.2B | 124B | - | 12 |
| Switch-Base | 7B | 124B | 128 | 12 |
| T5-Large | 0.7B | 425B | - | 24 |
| Switch-Large | 26B | 425B | 128 | 24 |
| T5-XXL | 11B | 6.3T | - | 24 |
| Switch-XXL | 395B | 6.3T | 64 | 24 |
| Switch-C | 1571B | 890B | 2048 | 15 |

Switch models place experts at every other FFN layer (Expert Freq. = 1/2), except Switch-C which uses experts at every layer.

**Fine-tuning:**
- Batch size: 1M tokens
- Steps: 16k
- Dropout: 0.1 (non-expert), 0.4 (expert)
- Evaluation: every 200 steps, report peak validation performance

### Key Results

#### Pre-training Speed (Table 1, Figures 5-6)

| Model | Capacity Factor | Quality @100k steps | Time to -1.50 | Speed (ex/sec) |
|---|---|---|---|---|
| T5-Base | - | -1.731 | Not achieved | 1600 |
| T5-Large | - | -1.550 | 131.1h | 470 |
| MoE-Base | 2.0 | -1.547 | 68.7h | 840 |
| Switch-Base | 2.0 | -1.554 | 72.8h | 860 |
| Switch-Base | 1.0 | -1.561 | **62.8h** | **1000** |

Switch-Base with capacity factor 1.0 achieves 7x speedup over T5-Base to reach the same perplexity (Figure 5). Even compared to T5-Large (3.5x more FLOPs per token), Switch-Base achieves 2.5x speedup (Figure 6).

#### Downstream Fine-tuning (Table 5)

| Model | GLUE | SQuAD | SuperGLUE | Winogrande | XSum | CB Trivia QA |
|---|---|---|---|---|---|---|
| T5-Base | 84.3 | 85.5 | 75.1 | 66.6 | 18.7 | 24.5 |
| Switch-Base | **86.7** | **87.2** | **79.5** | **73.3** | **20.3** | **30.7** |
| T5-Large | 87.8 | 88.1 | 82.7 | 79.1 | 20.9 | 29.5 |
| Switch-Large | **88.5** | **88.6** | **84.7** | **83.0** | **22.3** | **36.9** |

Notable improvements: SuperGLUE +4.4 points (Base), +2.0 points (Large); Winogrande +6.7 points (Base), +3.9 points (Large); closed-book TriviaQA +6.2 points (Base), +7.4 points (Large).

#### Distillation (Tables 6-7)

Sparse models can be compressed into dense students:

| Teacher | Student Params | Compression | Quality Preserved |
|---|---|---|---|
| Switch-Base 1.1B | 223M | 82% | 37% |
| Switch-Base 3.8B | 223M | 95% | 30% |
| Switch-Base 14.7B | 223M | 99% | 28% |

Best distillation technique: initialize student with non-expert weights from teacher + 0.75 hard / 0.25 soft loss mixture.

#### Multilingual Learning (Figures 7-8)

On 101 languages from mC4:
- Switch Transformer improves over mT5-Base on **all 101 languages**
- Mean step speedup: **5x** over mT5-Base
- 91% of languages achieve **4x+ speedup**

#### Trillion-Parameter Models (Table 9)

| Model | Parameters | Neg. Log Perp. @250k | Neg. Log Perp. @500k |
|---|---|---|---|
| T5-XXL | 11B | -1.147 | -1.095 |
| Switch-XXL | 395B | **-1.086** | **-1.008** |
| Switch-C | 1571B | -1.096 | -1.043 |

Switch-XXL outperforms T5-XXL by 0.061 at 250k steps and 0.087 at 500k steps. Switch-C achieves **4x speedup** over T5-XXL to reach the same perplexity.

---

## Limitations and Failure Modes

**Explicitly acknowledged by authors:**

1. **Training instability at largest scale.** Switch-XXL (395B parameters, 64 experts) exhibits sporadic instability despite stability techniques working for smaller models. Switch-C (1.6T parameters, 2048 experts) is stable, suggesting instability correlates with FLOPs per token rather than parameter count alone (Section 5.6).

2. **Upstream-downstream gap for largest models.** Despite superior pre-training perplexity, Switch-C (1.6T) achieves only 87.7 exact match on SQuAD vs. 89.6 for smaller Switch-XXL (395B). The paper notes "a poorly understood dependence between fine-tuning quality, FLOPS per token and number of parameters" (Section 8).

3. **Fine-tuning regularization required.** Sparse models overfit more severely on small downstream tasks due to higher parameter count. Expert dropout mitigates but does not fully resolve this (Section 2.4, Table 4).

4. **ARC Challenge regression.** T5-Base outperforms Switch-Base on ARC Challenge (35.5 vs. 32.8), the only task where Switch underperforms (Table 5).

**Not explicitly acknowledged:**

1. **Limited fine-tuning evaluation.** All downstream results use validation sets; test set performance is not reported for most tasks.
2. **Single architecture family.** All experiments use T5-based encoder-decoder architecture; generalization to decoder-only models not demonstrated.
3. **Expert specialization analysis absent.** The paper does not analyze what individual experts learn or whether they specialize semantically.

### Scope and Comparability

- **Evaluation regime:** Pre-training on C4 only; no comparison with other pre-training corpora.
- **Hardware-specific:** All experiments on TPUv3; GPU performance characteristics may differ.
- **Batch size dependency:** Expert capacity formula assumes large batch sizes; performance at small batch sizes unclear.

---

## Conclusions

### Contributions

1. **Simplified MoE routing.** Single-expert routing (k=1) outperforms top-k routing while reducing computation, communication, and implementation complexity. This contradicts prior assumptions that k>1 was necessary for gradient flow (Section 2.1).

2. **Stable sparse training at scale.** The combination of selective float32 precision, reduced initialization, and load balancing loss enables training trillion-parameter models in bfloat16 (Section 2.4).

3. **7x pre-training speedup.** FLOP-matched Switch Transformers achieve the same perplexity as dense T5 baselines in 1/7th the training time (Figure 5).

4. **Effective knowledge distillation.** Large sparse teachers can be compressed 99% while preserving 30% of quality gains over dense baselines (Table 7).

5. **Universal multilingual improvement.** Switch Transformer improves on all 101 languages in mC4, demonstrating broad applicability beyond English (Section 4.3).

6. **Trillion-parameter training.** Combining expert, model, and data parallelism enables training models with 1.6T parameters that achieve 4x speedup over T5-XXL (Section 5.6).

### Implications

1. **Parameter count as independent scaling axis.** The paper demonstrates that parameters can be scaled independently of FLOPs, opening a new dimension for model scaling beyond Kaplan et al. (2020).

2. **Sparse models for deployment via distillation.** The distillation results suggest a training paradigm: pre-train massive sparse models, then compress to deployable dense models.

3. **Routing simplicity suffices.** The success of k=1 routing suggests that sophisticated routing mechanisms may be unnecessary, enabling simpler MoE implementations. [Speculative: this was validated by subsequent MoE work including Mixtral.]

---

## Key Claims

1. **C1: 7x pre-training speedup.** Switch-Base with 128 experts achieves the same perplexity as T5-Base in 1/7th the wall-clock time on identical hardware (32 TPUv3 cores). Evidence: Figure 5, red dashed line showing "7x Speedup" (Section 3.2). Status: **supported**.

2. **C2: Single-expert routing outperforms top-k.** At capacity factor 1.0, Switch-Base (-1.561) outperforms MoE-Base top-2 (-1.572) on quality while being faster (1000 vs. 860 ex/sec). Evidence: Table 1 (Section 2.3). Status: **supported**.

3. **C3: Selective precision enables bfloat16 training.** Pure bfloat16 diverges (-3.780) while selective float32 precision in the router achieves stable training (-1.716) at bfloat16 speed (1390 ex/sec). Evidence: Table 2 (Section 2.4). Status: **supported**.

4. **C4: 30% quality preservation at 99% compression.** Distilling Switch-Base 14.7B to 223M parameters preserves 28% of quality improvement over T5-Base. Evidence: Table 7 (Section 4.2). Status: **supported**.

5. **C5: Improvement on all 101 languages.** mSwitch-Base improves final perplexity over mT5-Base on every language in mC4. Evidence: Figure 7 showing Switch above Dense for all languages (Section 4.3). Status: **supported**.

6. **C6: 4x speedup at trillion scale.** Switch-C (1.6T) reaches -1.095 perplexity 4x faster than T5-XXL. Evidence: Table 9, implicit from perplexity progression (Section 5.6). Status: **supported**.

---

## Open Questions

1. **How to stabilize Switch-XXL scale training?** The 395B parameter model with 64 experts shows sporadic instability despite techniques that work for smaller models. Switch-C (1.6T, 2048 experts) is stable, suggesting the issue relates to FLOPs per token rather than parameters. Not addressed.

2. **What explains the upstream-downstream gap for largest models?** Switch-C has better pre-training perplexity but worse fine-tuning performance than Switch-XXL on reasoning tasks. The relationship between FLOPs, parameters, and fine-tuning quality remains unclear. Not addressed.

3. **How do experts specialize?** The paper does not analyze expert activations or whether experts develop semantic specialization. Addressed by subsequent work on expert specialization analysis.

4. **Can Switch routing benefit decoder-only architectures?** All experiments use encoder-decoder T5; applicability to GPT-style models not demonstrated. Partially addressed by subsequent MoE decoder models.

---

## Core References and Why They Are Referenced

### Mixture of Experts Foundations

- **Shazeer et al. (2017)** -- *Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer.* Introduced MoE for Transformers with top-k routing and load balancing loss. Switch Transformer simplifies this to k=1 routing while keeping the load balancing objective.

- **Lepikhin et al. (2020)** -- *GShard: Scaling Giant Models with Conditional Computation.* Scaled MoE to 600B parameters for multilingual translation. Switch Transformer addresses GShard's training instability with selective precision and improved initialization.

### Scaling Laws

- **Kaplan et al. (2020)** -- *Scaling Laws for Neural Language Models.* Established power-law relationships between model size, data, compute, and performance. Switch Transformer proposes parameters as a fourth independent axis for scaling.

### Baseline Architecture

- **Raffel et al. (2019)** -- *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5).* Provides the base architecture and pre-training setup. All Switch models are compared against T5 baselines trained on improved C4.

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that Switch Transformer modifies by replacing dense FFN with sparse Switch FFN layers.

### Training Infrastructure

- **Shazeer et al. (2018)** -- *Mesh-TensorFlow: Deep Learning for Supercomputers.* The distributed computing framework used for implementing expert parallelism. Switch Transformer leverages MTF's tensor sharding and all-to-all communication primitives.

### Distillation

- **Hinton et al. (2015)** -- *Distilling the Knowledge in a Neural Network.* The knowledge distillation framework adapted for compressing sparse models into dense students.

- **Sanh et al. (2019)** -- *DistilBERT.* Distillation techniques for BERT that Switch Transformer builds on for sparse-to-dense distillation.

### Evaluation Benchmarks

- **Wang et al. (2018, 2019)** -- *GLUE* and *SuperGLUE.* Multi-task benchmarks for evaluating language understanding. Switch Transformer shows consistent improvements across these composite benchmarks.
