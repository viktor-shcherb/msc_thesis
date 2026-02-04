---
title: "Are Sixteen Heads Really Better than One?"
authors: "Michel, Levy, Neubig"
year: 2019
venue: "NeurIPS 2019"
paper_type: conference-paper
categories: ["attention-analysis", "pruning-and-sparsity"]
scope: ["multi-head attention", "head pruning", "encoder-decoder models", "BERT"]
benchmarks_used: ["wmt-translation", "mnli", "sst-2", "cola", "mrpc"]
models_introduced: []
models_evaluated: ["transformer-base", "bert-base"]
key_claims:
  - id: C1
    claim: "Most individual attention heads can be removed at test time without statistically significant performance loss"
    evidence: "Table 1, Section 3.2, Figure 1"
    status: supported
  - id: C2
    claim: "Many layers can be reduced to a single attention head without significant degradation"
    evidence: "Tables 2-3, Section 3.3"
    status: supported
  - id: C3
    claim: "20-60% of heads can be iteratively pruned across the full model without noticeable performance impact"
    evidence: "Figures 3 and 6, Section 4.2, Appendix B"
    status: supported
  - id: C4
    claim: "Encoder-decoder attention is far more sensitive to head pruning than self-attention"
    evidence: "Figure 4, Table 2, Section 5"
    status: supported
  - id: C5
    claim: "The distinction between important and unimportant heads emerges early during training, suggesting two-phase dynamics"
    evidence: "Figure 5, Section 6"
    status: supported
  - id: C6
    claim: "Pruning 50% of BERT heads yields up to 17.5% inference speedup at large batch sizes"
    evidence: "Table 4, Section 4.3"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Tests the importance of multi-head attention introduced in the original Transformer"
  - target: 2019-07-specialized-attention-heads-pruning
    type: concurrent
    detail: "Both show head pruning is possible; Voita et al. use learned pruning via gradient descent on mask variables while Michel et al. study post-hoc removal, extend analysis to BERT, and study training dynamics"
  - target: 2019-08-bert-attention-analysis
    type: concurrent
    detail: "Both analyze attention heads in BERT; Clark et al. study what heads learn while Michel et al. study which heads are needed"
  - target: 2019-11-dark-secrets-of-bert
    type: concurrent
    detail: "Both analyze BERT attention; Kovaleva et al. characterize attention patterns while Michel et al. study head redundancy"
  - target: 2021-12-transformer-circuits-framework
    type: complementary
    detail: "The circuits framework provides mechanistic explanations for why some heads contribute little (e.g., small OV eigenvalues)"
  - target: 2019-06-bert-pretraining-language-understanding
    type: evaluates
    detail: "Tests head pruning and redundancy in the BERT model introduced by Devlin et al."
open_questions:
  - question: "What is the principled explanation for the two-phase training dynamics of head importance?"
    addressed_by: null
  - question: "Can pruning during training (rather than only at test time) yield models with fewer but more effective heads?"
    addressed_by: 2019-07-specialized-attention-heads-pruning
  - question: "How do these findings generalize to much larger models (billions of parameters) and longer contexts?"
    addressed_by: null
  - question: "Why is encoder-decoder attention more reliant on multi-headedness than self-attention?"
    addressed_by: null
---

# Are Sixteen Heads Really Better than One?

**Authors:** Paul Michel, Omer Levy, Graham Neubig (Carnegie Mellon University, Facebook AI Research)
**Date:** December 2019, NeurIPS 2019; arXiv:1905.10650

---

## Core Research Problem

Multi-headed attention (MHA) is a central component of Transformer architectures, applying Nh independently parameterized attention mechanisms in parallel. Each head operates with reduced dimensionality dh = d/Nh, making MHA an ensemble of low-rank vanilla attention layers. When dh = d, MHA is strictly more expressive than single-headed attention, but in practice dh = d/Nh to keep parameter counts constant (Section 2.2).

Prior work had shown that MHA helps with subject-verb agreement (Tang et al., 2018) and that some heads are predictive of dependency structures (Raganato and Tiedemann, 2018). However, **it remained unclear whether all attention heads are necessary for a trained model's performance, or whether many are redundant after training.** No prior work had systematically evaluated the contribution of individual heads across different Transformer applications, nor studied the interaction between multi-headedness and training dynamics. The core challenge is: **how much of multi-headed attention is actually utilized at test time, and which parts of the Transformer architecture are most reliant on having multiple heads.**

---

## Problem Solutions

The paper addresses this through ablation and pruning experiments across machine translation and natural language inference models. The key findings are:

1. **Most individual attention heads can be removed at test time** without statistically significant degradation in performance, and many layers can be reduced to a single head.
2. **A gradient-based importance score** (first-order Taylor expansion of the loss with respect to head mask variables) provides an efficient proxy for head importance, enabling greedy iterative pruning across the entire model.
3. **Encoder-decoder attention is far more sensitive to pruning** than self-attention in machine translation models, indicating a more critical role for multi-headedness in cross-attention.
4. **The distinction between important and unimportant heads emerges early during training**, suggesting an interaction between multi-headedness and training dynamics.

---

## Approach Details

### Method

The paper introduces binary mask variables ξh for each attention head, modifying the MHA formula to:

> MHAtt(x, q) = Σ_{h=1}^{Nh} ξh Att_{Wh_k, Wh_q, Wh_v, Wh_o}(x, q)

Setting ξh = 0 masks head h (replaces its output with zeros). When all ξh = 1, this is equivalent to standard MHA (Section 2.3). Three types of ablation experiments are performed:

1. **Ablating one head:** Mask a single head and measure performance change. If the model's performance without head h is significantly worse, h is important; if comparable, h is redundant given the rest (Section 3.2).
2. **Ablating all heads but one:** Within each layer, keep only the single best-performing head and mask the rest (Section 3.3).
3. **Iterative pruning across layers:** Sort all heads by importance score and remove them globally, 10% at a time (Section 4).

### Key Technical Components

**Head importance score Ih.** Defined as the expected absolute sensitivity of the loss to the mask variable (Equation 2):

> Ih = E_{x~X} |∂L(x)/∂ξh|

Applying the chain rule to the MHA formula yields:

> Ih = E_{x~X} |Att_h(x)^T ∂L(x)/∂Att_h(x)|

This is equivalent to the Taylor expansion method from Molchanov et al. (2017). The **absolute value is crucial** to prevent positive and negative contributions from canceling across datapoints (Section 4.1). The expectation is computed over training data or a subset. For the WMT model, all newstest20[09-12] sets are used to estimate Ih. Importance scores are **normalized per layer** using the l2 norm, as recommended by Molchanov et al. (2017).

**Computational cost.** Computing Ih requires only a single forward and backward pass, making it no slower than a training step (Section 4.1).

**Pruning procedure.** Heads are sorted globally by increasing Ih. At each step, 10% of the total heads are removed. Performance is evaluated after each pruning step. This greedy, iterative approach avoids combinatorial search over head subsets (Section 4).

### Experimental Setup

**WMT model:** Transformer-large (Vaswani et al., 2017) with 6 layers and 16 heads per layer, pretrained on WMT2014 English-to-French (Ott et al., 2018). Three attention types: encoder self-attention (Enc-Enc), encoder-decoder attention (Enc-Dec), and decoder self-attention (Dec-Dec). Evaluated with BLEU on newstest2013, tokenized with Moses (Koehn et al., 2007). Statistical significance tested with paired bootstrap resampling (1000 resamples) using compare-mt (Neubig et al., 2019) at p < 0.01 (Section 3.1).

**BERT model:** BERT base-uncased (Devlin et al., 2018) with 12 layers and 12 attention heads, fine-tuned and evaluated on MultiNLI (Williams et al., 2018). Accuracy reported on the matched validation set. Statistical significance tested with t-test at p < 0.01. BERT has only self-attention (no encoder-decoder attention) (Section 3.1).

**Additional datasets for pruning experiments (Appendix B):**
- SST-2 (Socher et al., 2013): GLUE version, fine-tuned BERT.
- CoLA (Warstadt et al., 2018): GLUE version, fine-tuned BERT.
- MRPC (Dolan and Brockett, 2005): GLUE version, fine-tuned BERT.
- IWSLT 2014 German-to-English (Cettolo et al., 2015): smaller Transformer with 6 layers and 8 heads per layer.

**Inference speed experiments (Section 4.3):** Conducted on two machines with GeForce GTX 1080Ti GPUs, 3 runs each (6 total datapoints per setting), across batch sizes 1, 4, 16, 64. Measured on the MNLI-matched validation set.

### Key Results

#### Single-Head Ablation (WMT Encoder Self-Attention)

Table 1 reports the BLEU difference when each of the 96 encoder self-attention heads (6 layers x 16 heads) is individually masked. Base BLEU is 36.05.

| Observation | Result |
|---|---|
| Total heads tested | 96 (6 layers x 16 heads) |
| Heads causing statistically significant change (p < 0.01) | 8 out of 96 |
| Of those 8, heads whose removal *increases* BLEU | 4 |

For BERT on MultiNLI, Figure 1b shows a similarly concentrated distribution: the majority of heads can be removed without deviating much from the baseline accuracy of ~0.834 (Figure 1b).

#### Ablating All Heads but One (Best Single Head per Layer)

Tables 2 and 3 report the best performance delta when reducing each layer to its single most important head. Underlined values indicate statistical significance at p < 0.01.

| Layer | WMT Enc-Enc | WMT Enc-Dec | WMT Dec-Dec |
|---|---|---|---|
| 1 | **-1.31** | **+0.24** | -0.03 |
| 2 | -0.16 | +0.06 | +0.12 |
| 3 | +0.12 | +0.05 | +0.18 |
| 4 | -0.15 | -0.24 | +0.17 |
| 5 | +0.02 | **-1.55** | -0.04 |
| 6 | **-0.36** | **-13.56** | +0.24 |

Bold values are statistically significant (p < 0.01, Table 2). For Enc-Enc, only layers 1 and 6 show significant degradation. For Enc-Dec, layers 5 and 6 show significant degradation (layer 1 is significant but positive, i.e. removing heads helps). For Dec-Dec, no layer shows significant degradation.

For BERT (Table 3), reducing each of the 12 layers to a single head produces no statistically significant change at p < 0.01. The largest drop is layer 9 at -0.96% accuracy.

| Layer | Delta Acc. | Layer | Delta Acc. |
|---|---|---|---|
| 1 | -0.01% | 7 | +0.05% |
| 2 | +0.10% | 8 | -0.72% |
| 3 | -0.14% | 9 | -0.96% |
| 4 | -0.53% | 10 | +0.07% |
| 5 | -0.29% | 11 | -0.19% |
| 6 | -0.52% | 12 | -0.12% |

The paper verifies these findings generalize to held-out test sets: selecting the best head on a validation set (newstest2013 for WMT, 5000 training examples for BERT) and evaluating on a separate test set (newstest2014, MNLI-matched validation) yields consistent results. Keeping only one head does not result in statistically significant change for 50% of WMT layers and 100% of BERT layers (Section 3.3, Appendix A, Tables 5-6).

#### Iterative Pruning (Percentage of Heads Removable)

Figures 3 and 6 show the effect of iterative pruning, removing 10% of total heads at each step in order of increasing Ih.

| Model / Dataset | Heads prunable without noticeable impact |
|---|---|
| WMT (newstest2013) | ~20% (Figure 3a) |
| BERT (MultiNLI matched) | ~40% (Figure 3b) |
| BERT (SST-2) | ~60% (Figure 6a) |
| BERT (CoLA) | ~50% (Figure 6b) |
| BERT (MRPC) | ~50% (Figure 6c) |

Performance drops sharply beyond these thresholds, meaning neither model can be fully reduced to single-head attention without retraining (Section 4.2). The importance score Ih yields better pruning order than the per-head oracle score from Section 3.2 (dashed lines in Figure 3).

#### Inference Speed (BERT, 50% Heads Pruned)

Table 4 reports inference speed on MNLI-matched when heads are actually removed (not just masked).

| Batch size | Original (ex/s) | Pruned 50% (ex/s) | Speedup |
|---|---|---|---|
| 1 | 17.0 +/- 0.3 | 17.3 +/- 0.6 | +1.9% |
| 4 | 67.3 +/- 1.3 | 69.1 +/- 1.3 | +2.7% |
| 16 | 114.0 +/- 3.6 | 134.0 +/- 3.6 | +17.5% |
| 64 | 124.7 +/- 2.9 | 146.6 +/- 3.4 | +17.5% |

The speedup is substantial at larger batch sizes (+17.5%) but vanishes at small batch sizes (+1.9% at batch size 1) (Section 4.3). Each head represents 6.25% (WMT) or ~8.34% (BERT) of parameters per attention layer, and approximately one third of total model parameters are in MHA layers.

### Attention Type Sensitivity (WMT)

When pruning each attention type separately (Section 5, Figure 4), encoder-decoder (Enc-Dec) attention degrades catastrophically beyond 60% pruning, while encoder self-attention (Enc-Enc) and decoder self-attention (Dec-Dec) retain ~30 BLEU with only 20% of heads remaining. This indicates that **multi-headedness is most critical for cross-attention** between encoder and decoder.

### Cross-Dataset Validation

To test whether important heads are "universally" important, Section 3.4 repeats the single-head ablation on out-of-domain test sets: MNLI mismatched for BERT and MTNT English-to-French (Michel and Neubig, 2018) for WMT. The effect of removing a head correlates positively across domains: Pearson r = 0.56 (p < 0.01) for WMT and r = 0.68 (p < 0.01) for BERT (Figures 2a, 2b). Heads that most affect performance on one domain tend to have the same effect on the other.

### Training Dynamics

Experiments on the IWSLT model (6 layers, 8 heads, German-to-English, IWSLT 2014) reveal two distinct phases of head importance during training (Section 6, Figure 5):

1. **Early training (epochs 1-2):** Performance decreases linearly with pruning percentage, independent of Ih. All heads are roughly equally important.
2. **Later training (epoch 10 onward):** A concentration of unimportant heads emerges. Up to 40% of heads can be pruned while retaining 85-90% of the un-pruned model's BLEU score.

This suggests that the important heads are determined early (but not immediately) during training. The paper draws an analogy to the two-phase training analysis of Shwartz-Ziv and Tishby (2017), which decomposes training into an "empirical risk minimization" phase followed by a "compression" phase.

---

## Limitations and Failure Modes

1. **Limited architecture scope.** Experiments use only two architectures: Transformer-large for NMT and BERT-base for NLI. Generalization to larger models or different architectures is not tested.
2. **Test-time pruning only.** All pruning is applied post-training without retraining. The paper does not explore whether retraining after pruning could recover additional performance or enable more aggressive pruning.
3. **Greedy pruning is heuristic.** The iterative pruning procedure removes heads greedily by increasing Ih, which may not find the globally optimal subset of heads (Section 4).
4. **Training dynamics on small model only.** The training dynamics analysis (Section 6) uses the smaller IWSLT model (6 layers, 8 heads), not the full WMT or BERT models. Whether the two-phase pattern generalizes to larger models is not established.
5. **Sharp performance cliff.** Despite many heads being individually removable, jointly pruning beyond the identified thresholds (20-60% depending on task) causes catastrophic degradation. The models cannot be reduced to purely single-head attention without retraining (Section 4.2).
6. **Modest speedup at small batch sizes.** Inference speedup from pruning 50% of heads is only +1.9% at batch size 1 (Table 4), limiting practical benefit for latency-sensitive single-example inference.
7. **No analysis of what pruned heads compute.** The paper identifies which heads can be removed but does not analyze what functions those heads perform or why they are redundant. The authors leave "a more principled investigation" of training dynamics to future work (Section 6).

---

## Conclusions

### Contributions

1. **Demonstrated widespread head redundancy at test time.** In both WMT and BERT, the majority of individual attention heads can be removed without statistically significant performance loss. Only 8 out of 96 encoder self-attention heads in WMT cause significant change, and half of those changes are improvements (Table 1, Section 3.2).

2. **Showed many layers reduce to single-head attention.** All 12 BERT layers and all 6 WMT decoder self-attention layers can be reduced to a single head without significant degradation at p < 0.01 (Tables 2-3, Section 3.3).

3. **Established gradient-based importance scoring for head pruning.** The first-order Taylor expansion importance score Ih provides a fast, effective proxy for head contribution, requiring only one forward-backward pass and outperforming per-head oracle scoring (Section 4.1, Figure 3).

4. **Quantified prunable head percentages across tasks.** Iterative greedy pruning removes 20% (WMT) to 40-60% (BERT on various GLUE tasks) of heads without noticeable degradation (Figures 3, 6, Section 4.2).

5. **Identified encoder-decoder attention as most reliant on multi-headedness.** In machine translation, cross-attention degrades catastrophically beyond 60% pruning while self-attention retains ~30 BLEU with only 20% of heads (Figure 4, Section 5).

6. **Provided evidence for two-phase head importance dynamics during training.** On the IWSLT model, head importance distinction emerges between epochs 2 and 10, paralleling the ERM-compression decomposition of Shwartz-Ziv and Tishby (2017) (Figure 5, Section 6).

### Implications

1. **MHA may be over-parameterized for trained models.** Despite being strictly more expressive than single-head attention when dh = d, trained models do not fully exploit MHA's theoretical capacity, suggesting room for more parameter-efficient attention designs (Section 8).

2. **Structured head pruning is a viable model compression strategy.** Pruning 50% of BERT heads yields up to 17.5% inference speedup at larger batch sizes while maintaining task performance, making this approach practical for deployment in memory-constrained settings (Table 4, Section 4.3).

3. **The role of multi-headedness may differ by attention type.** The stark contrast between self-attention and encoder-decoder attention sensitivity suggests that the function of multi-headedness is not uniform across the model (Section 5). This is speculative but points toward architecture-specific pruning strategies.

---

## Key Claims

1. **C1: Most individual heads are redundant at test time.** Only 8 out of 96 WMT encoder self-attention heads cause a statistically significant BLEU change when individually removed, and 4 of those 8 are actually improvements (Table 1, Section 3.2). Status: **supported**.

2. **C2: Many layers can function with a single attention head.** All 12 BERT layers produce no significant accuracy change when reduced to one head (Table 3). For WMT, all Dec-Dec layers and most Enc-Enc and Enc-Dec layers can use a single head (Table 2, Section 3.3). Status: **supported**.

3. **C3: 20-60% of heads are globally prunable without noticeable impact.** Iterative Ih-based pruning removes ~20% of WMT heads and ~40-60% of BERT heads (task-dependent) before performance degrades (Figures 3, 6, Section 4.2, Appendix B). Status: **supported**.

4. **C4: Encoder-decoder attention is far more sensitive to pruning than self-attention.** Pruning >60% of Enc-Dec heads causes catastrophic BLEU degradation, while Enc-Enc and Dec-Dec retain ~30 BLEU with only 20% of heads (Figure 4, Section 5). Status: **supported**.

5. **C5: Head importance distinction emerges early during training.** On the IWSLT model, all heads are roughly equally important at epochs 1-2, but by epoch 10 a clear concentration of unimportant heads develops (Figure 5, Section 6). Status: **supported** (on the IWSLT model; generalization to larger models not tested).

6. **C6: Head pruning yields measurable inference speedup.** Pruning 50% of BERT heads achieves +17.5% speedup at batch sizes 16 and 64, though only +1.9% at batch size 1 (Table 4, Section 4.3). Status: **supported**.

---

## Open Questions

1. **What explains the two-phase training dynamics of head importance?** The paper observes that head importance distinction emerges between epochs 2 and 10 on the IWSLT model (Section 6) and draws an analogy to the ERM-compression decomposition, but leaves a more principled investigation to future work. Not yet formally addressed.

2. **Can pruning during training yield models with fewer but more effective heads?** The paper only prunes at test time. Voita et al. (2019) propose gradient descent on mask variables during training, partially addressing this.

3. **How do these findings generalize to much larger models?** All experiments use models with 12-16 heads per layer and at most 12 layers. Whether the same redundancy patterns hold at billion-parameter scales remains open.

4. **Why is encoder-decoder attention more reliant on multi-headedness?** The paper observes this (Section 5, Figure 4) but does not provide a mechanistic explanation. Not yet addressed.

---

## Core References and Why They Are Referenced

### Transformer Architecture and Multi-Headed Attention

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduced the Transformer and multi-headed attention. The WMT model used in experiments follows this architecture.
- **Bahdanau et al. (2015)** -- *Neural Machine Translation by Jointly Learning to Align and Translate.* Foundational attention mechanism that MHA extends.
- **Luong et al. (2015)** -- *Effective Approaches to Attention-Based Neural Machine Translation.* Scaled bilinear attention variant used in MHA layers.

### Models and Datasets Used in Experiments

- **Ott et al. (2018)** -- *Scaling Neural Machine Translation.* Provides the pretrained WMT English-to-French Transformer-large model used in experiments.
- **Devlin et al. (2018)** -- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* The BERT base-uncased model fine-tuned and evaluated in experiments.
- **Williams et al. (2018)** -- *A Broad-Coverage Challenge Corpus for Sentence Understanding Through Inference.* MultiNLI dataset used for BERT evaluation.
- **Cettolo et al. (2015)** -- *IWSLT 2014 Evaluation Campaign.* Provides the IWSLT German-to-English dataset used for training dynamics experiments.

### Neural Network Pruning

- **LeCun et al. (1990)** -- *Optimal Brain Damage.* Foundational work on pruning neural networks by removing weights with small saliency.
- **Hassibi and Stork (1993)** -- *Second Order Derivatives for Network Pruning: Optimal Brain Surgeon.* Extended weight pruning using second-order information.
- **Molchanov et al. (2017)** -- *Pruning Convolutional Neural Networks for Resource Efficient Inference.* The Taylor expansion method for importance scoring that Ih is equivalent to. Also provides the per-layer l2 normalization recommendation.
- **Han et al. (2015)** -- *Learning Both Weights and Connections for Efficient Neural Network.* Fine-grained weight-by-weight pruning approach.

### Concurrent Work on Attention Analysis

- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned.* Concurrent work reaching similar conclusions about head redundancy in NMT. Uses LRP for determining important heads and proposes gradient descent on mask variables ξh. Michel et al. extend the analysis beyond NMT to BERT and study training dynamics.

### Training Dynamics

- **Shwartz-Ziv and Tishby (2017)** -- *Opening the Black Box of Deep Neural Networks via Information.* Two-phase training analysis (ERM + compression) that the observed head importance dynamics parallel.
