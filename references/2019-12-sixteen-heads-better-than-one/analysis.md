# Are Sixteen Heads Really Better than One?

**Authors:** Paul Michel, Omer Levy, Graham Neubig (Carnegie Mellon University, Facebook AI Research)
**Date:** December 2019, NeurIPS 2019; arXiv:1905.10650

---

## Core Research Problem

Multi-headed attention (MHA) is a central component of Transformer architectures, applying Nh independent attention mechanisms in parallel. Each head operates with reduced dimensionality dh = d/Nh, making MHA an ensemble of low-rank vanilla attention layers. While MHA has been shown to help with subject-verb agreement (Tang et al., 2018) and to encode dependency structures (Raganato and Tiedemann, 2018), it remained unclear **what the multiple heads actually buy in practice** -- whether all heads are necessary for the model's final performance, or whether many are redundant after training. Prior work had not systematically evaluated the contribution of individual heads across different Transformer applications, nor studied the interaction between multi-headedness and training dynamics. The core challenge is: **how much of multi-headed attention is actually utilized at test time, and which components of the Transformer are most reliant on having multiple heads.**

---

## Problem Solutions

The paper addresses this through a series of ablation and pruning experiments. The key findings are:

1. **Most individual attention heads can be removed at test time** without statistically significant degradation in performance, and some layers can be reduced to a single head.
2. **A gradient-based importance score** (first-order Taylor expansion of the loss with respect to head mask variables) provides an efficient proxy for head importance, enabling greedy iterative pruning across the entire model.
3. **Encoder-decoder attention is far more sensitive to pruning** than self-attention in machine translation models, indicating that multi-headedness plays a more critical role in cross-attention.
4. **The distinction between important and unimportant heads emerges early during training**, suggesting an interaction between multi-headedness and training dynamics.

---

## Approach Details

### Method

The paper introduces binary mask variables ξh for each attention head, modifying the MHA formula to:

> MHAtt(x, q) = Σ_{h=1}^{Nh} ξh Att_{Wh_k, Wh_q, Wh_v, Wh_o}(x, q)

Setting ξh = 0 masks head h (replaces its output with zeros). Three types of ablation experiments are performed:

1. **Ablating one head:** Mask a single head and measure performance change.
2. **Ablating all heads but one:** Within each layer, keep only the single best-performing head and mask the rest.
3. **Iterative pruning across layers:** Sort all heads by importance score and remove them one by one from the entire model.

### Key Technical Components

- **Head importance score Ih:** Defined as the expected absolute sensitivity of the loss to the mask variable:

> Ih = E_{x~X} |∂L(x)/∂ξh|

Applying the chain rule yields:

> Ih = E_{x~X} |Att_h(x)^T ∂L(x)/∂Att_h(x)|

This is equivalent to the Taylor expansion method from Molchanov et al. (2017). The absolute value is crucial to prevent positive and negative contributions from canceling. The expectation is computed over training data (or a subset). Importance scores are normalized per layer using the l2 norm.

- **Efficiency:** Computing Ih requires only a single forward and backward pass, making it no slower than a training step.

- **Pruning procedure:** Heads are sorted globally by increasing Ih. At each step, 10% of the total heads are removed. Performance is evaluated after each pruning step.

### Experimental Setup

- **WMT model:** Transformer-large (Vaswani et al., 2017) with 6 layers and 16 heads per layer, pretrained on WMT2014 English-to-French (Ott et al., 2018). Three attention types: encoder self-attention (Enc-Enc), encoder-decoder attention (Enc-Dec), decoder self-attention (Dec-Dec). Evaluated with BLEU on newstest2013. Statistical significance tested with paired bootstrap resampling (1000 resamples).
- **BERT model:** BERT base-uncased (12 layers, 12 heads) fine-tuned on MultiNLI. Evaluated with accuracy on the matched validation set. Statistical significance tested with t-test.
- **Additional datasets for pruning:** SST-2, CoLA, MRPC (all via fine-tuned BERT), and IWSLT 2014 German-to-English (smaller Transformer with 6 layers and 8 heads).
- **Efficiency experiments:** Inference speed measured on two machines with GeForce GTX 1080Ti GPUs, 3 runs each (6 total datapoints per setting), across batch sizes 1, 4, 16, 64.

### Key Results

#### Single-Head Ablation (WMT Encoder Self-Attention)

| Observation | Result |
|---|---|
| Total heads in encoder self-attention | 96 (6 layers × 16 heads) |
| Heads causing statistically significant change (p < 0.01) | 8 out of 96 |
| Of those 8, heads whose removal *increases* BLEU | 4 |

#### Ablating All Heads but One (Best Single Head per Layer)

| Model / Attention Type | Layers where single head suffices (no significant degradation) |
|---|---|
| WMT Enc-Enc | 3 out of 6 layers |
| WMT Enc-Dec | 4 out of 6 layers (layer 6 degrades by -13.56 BLEU) |
| WMT Dec-Dec | All 6 layers |
| BERT | All 12 layers (none statistically significant at p < 0.01) |

#### Iterative Pruning (Percentage of Heads Removable Without Noticeable Impact)

| Model / Dataset | Heads prunable without impact |
|---|---|
| WMT (newstest2013) | ~20% |
| BERT (MultiNLI) | ~40% |
| BERT (SST-2) | ~60% |
| BERT (CoLA) | ~50% |
| BERT (MRPC) | ~50% |

#### Inference Speed (BERT, 50% Heads Pruned)

| Batch size | Original (ex/s) | Pruned 50% (ex/s) | Speedup |
|---|---|---|---|
| 1 | 17.0 ± 0.3 | 17.3 ± 0.6 | +1.9% |
| 4 | 67.3 ± 1.3 | 69.1 ± 1.3 | +2.7% |
| 16 | 114.0 ± 3.6 | 134.0 ± 3.6 | +17.5% |
| 64 | 124.7 ± 2.9 | 146.6 ± 3.4 | +17.5% |

- Only 8 out of 96 encoder self-attention heads in WMT cause a statistically significant change when removed; half of those changes are *improvements*.
- For BERT on MultiNLI, **every layer** can be reduced to a single head without statistically significant degradation.
- Encoder-decoder attention is far more sensitive to pruning than self-attention: pruning >60% of Enc-Dec heads causes catastrophic degradation, while Enc-Enc and Dec-Dec self-attention retain ~30 BLEU with only 20% of heads remaining.
- Pruning 50% of BERT heads yields up to 17.5% inference speedup at larger batch sizes.

### Attention Type Sensitivity (WMT)

When pruning each attention type separately, encoder-decoder (Enc-Dec) attention degrades catastrophically beyond 60% pruning, while encoder self-attention (Enc-Enc) and decoder self-attention (Dec-Dec) degrade more gracefully. This indicates that **multi-headedness is most critical for cross-attention** between encoder and decoder.

### Training Dynamics

Experiments on the IWSLT model (6 layers, 8 heads, German-to-English) reveal two distinct phases:

1. **Early training (epochs 1--2):** Performance decreases linearly with pruning percentage, independent of Ih. All heads are roughly equally important.
2. **Later training (epoch 10 onward):** A concentration of unimportant heads emerges. Up to 40% of heads can be pruned while retaining 85--90% of unpruned BLEU.

This suggests that head importance is determined early (but not immediately) during training, reminiscent of the two-phase training analysis by Shwartz-Ziv and Tishby (2017) (empirical risk minimization followed by compression).

---

## Conclusions

1. **Most attention heads are redundant at test time.** In both WMT and BERT, the majority of individual heads can be removed without statistically significant performance loss. Many layers can be reduced to a single attention head.

2. **Gradient-based importance scoring enables efficient pruning.** The first-order Taylor expansion importance score Ih provides a fast, effective proxy for head contribution, requiring only one forward-backward pass to compute.

3. **20--60% of heads can be pruned across the full model.** Iterative greedy pruning using Ih removes 20% (WMT) to 40--60% (BERT, depending on task) of heads without noticeable degradation, with up to 17.5% inference speedup.

4. **Encoder-decoder attention is most reliant on multi-headedness.** In machine translation, cross-attention layers are far more sensitive to pruning than self-attention layers, indicating that multi-headedness serves a more critical function in attending across sequences.

5. **Head importance emerges early in training.** The distinction between important and unimportant heads develops within the first few epochs, paralleling two-phase training dynamics observed in other neural network analyses.

6. **MHA does not fully exploit its theoretical expressiveness.** Despite being strictly more expressive than single-head attention (when dh = d), trained models do not leverage this capacity fully, suggesting room for more parameter-efficient attention designs.

---

## Core References and Why They Are Referenced

### Transformer Architecture and Multi-Headed Attention

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduced the Transformer and multi-headed attention. The WMT model used in experiments is this architecture.
- **Bahdanau et al. (2015)** -- *Neural Machine Translation by Jointly Learning to Align and Translate.* Foundational attention mechanism that MHA extends.
- **Luong et al. (2015)** -- *Effective Approaches to Attention-Based Neural Machine Translation.* Scaled bilinear attention variant used in MHA layers.

### Models Used in Experiments

- **Ott et al. (2018)** -- *Scaling Neural Machine Translation.* Provides the pretrained WMT English-to-French model used in experiments.
- **Devlin et al. (2018)** -- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* The BERT base-uncased model used in experiments.
- **Williams et al. (2018)** -- *A Broad-Coverage Challenge Corpus for Sentence Understanding Through Inference.* MultiNLI dataset used for BERT evaluation.

### Neural Network Pruning

- **LeCun et al. (1990)** -- *Optimal Brain Damage.* Foundational work on pruning neural networks by removing weights with small saliency.
- **Hassibi and Stork (1993)** -- *Second Order Derivatives for Network Pruning: Optimal Brain Surgeon.* Extended weight pruning using second-order information.
- **Molchanov et al. (2017)** -- *Pruning Convolutional Neural Networks for Resource Efficient Inference.* The Taylor expansion method for importance scoring that Ih is equivalent to. Also provides the per-layer l2 normalization recommendation.
- **Han et al. (2015)** -- *Learning Both Weights and Connections for Efficient Neural Network.* Fine-grained weight-by-weight pruning approach.

### Concurrent Work

- **Voita et al. (2019)** -- *Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned.* Concurrent work reaching similar conclusions about head redundancy in NMT. Uses LRP for determining important heads and proposes gradient descent on mask variables ξh. Michel et al. extend the analysis beyond NMT to BERT and study training dynamics.

### Training Dynamics

- **Shwartz-Ziv and Tishby (2017)** -- *Opening the Black Box of Deep Neural Networks via Information.* Two-phase training analysis (ERM + compression) that the observed head importance dynamics parallel.

#### Cross-References in Available Papers

- **Voita et al. (2019)** is available as `2019-07-specialized-attention-heads-pruning`. Michel et al. explicitly acknowledge this as concurrent work (Section 7), noting complementary approaches: Voita et al. use LRP and focus on identifying specific head functions (positional, syntactic, rare-word heads), while Michel et al. use gradient-based importance scores and additionally study BERT, cross-attention sensitivity, and training dynamics.
