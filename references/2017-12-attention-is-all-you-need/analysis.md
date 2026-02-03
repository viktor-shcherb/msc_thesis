# Attention Is All You Need

**Authors:** Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin (Google Brain, Google Research, University of Toronto)
**Date:** December 2017, NeurIPS 2017; arXiv:1706.03762

---

## Core Research Problem

State-of-the-art sequence transduction models in 2017 relied on recurrent neural networks (LSTMs, GRUs) or convolutional neural networks as their core building block, typically arranged in an encoder-decoder structure with an attention mechanism connecting the two. These architectures suffer from a fundamental limitation: **recurrent models process tokens sequentially**, generating hidden states h_t as a function of h_{t-1} and the input at position t. This sequential dependency precludes parallelization within training examples, which becomes a critical bottleneck at longer sequence lengths as memory constraints limit batching across examples.

Convolutional approaches (ByteNet, ConvS2S) improve parallelism but require O(n/k) or O(log_k(n)) layers to relate signals from two arbitrary positions at distance n, making long-range dependency learning difficult. Attention mechanisms had been used successfully to model dependencies regardless of distance, but almost always in conjunction with a recurrent network (Bahdanau et al., 2014; Luong et al., 2015), retaining the sequential computation bottleneck.

Prior work on reducing sequential computation (Extended Neural GPU, ByteNet, ConvS2S) used convolutions for parallel hidden-state computation, but the number of operations to relate distant positions still grew with distance. Self-attention had been applied within specific tasks (reading comprehension, sentence embeddings) but never as the sole mechanism for a full sequence transduction model.

The core challenge is: **how to build a sequence transduction model that achieves state-of-the-art quality while eliminating sequential computation entirely, enabling full parallelization during training and constant-length dependency paths between any two positions.**

---

## Problem Solutions

The paper proposes the **Transformer**, a model architecture that dispenses with recurrence and convolutions entirely, relying solely on attention mechanisms to draw global dependencies between input and output. The key insight is that self-attention alone -- applied in stacked layers with residual connections, position-wise feed-forward networks, and positional encodings -- is sufficient to achieve state-of-the-art sequence transduction while being far more parallelizable.

The solution rests on four components:

1. **Scaled dot-product attention** as the core compatibility function, computing weighted sums of values where weights are determined by query-key dot products scaled by 1/sqrt(d_k) to prevent softmax saturation.

2. **Multi-head attention** that projects queries, keys, and values into h parallel subspaces, runs attention independently in each, and concatenates the results. This allows the model to jointly attend to information from different representation subspaces at different positions.

3. **An encoder-decoder architecture** where both encoder and decoder are stacks of identical layers, each containing multi-head self-attention and position-wise feed-forward sub-layers with residual connections and layer normalization. The decoder additionally includes encoder-decoder cross-attention and causal masking.

4. **Sinusoidal positional encodings** added to input embeddings to inject sequence order information, using a geometric progression of wavelengths that the authors hypothesized would enable generalization to unseen sequence lengths.

---

## Approach Details

### Method

The Transformer uses an encoder-decoder structure. The encoder maps an input sequence (x_1, ..., x_n) to continuous representations z = (z_1, ..., z_n). The decoder generates output tokens (y_1, ..., y_m) auto-regressively, consuming previously generated symbols.

**Scaled dot-product attention (Eq. 1):**

> Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V

where Q, K, V are matrices of queries, keys, and values respectively, and d_k is the key dimension. The scaling by 1/sqrt(d_k) counteracts the growth of dot-product magnitudes for large d_k: assuming query and key components are independent with mean 0 and variance 1, the dot product has variance d_k, pushing the softmax into regions with extremely small gradients.

**Multi-head attention:**

> MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W^O
>
> where head_i = Attention(Q W^Q_i, K W^K_i, V W^V_i)

with parameter matrices W^Q_i in R^{d_model x d_k}, W^K_i in R^{d_model x d_k}, W^V_i in R^{d_model x d_v}, and W^O in R^{h*d_v x d_model}.

**Position-wise feed-forward network (Eq. 2):**

> FFN(x) = max(0, xW_1 + b_1)W_2 + b_2

Applied identically to each position but with different parameters per layer. Input/output dimension d_model = 512, inner dimension d_ff = 2048.

**Positional encoding:**

> PE(pos, 2i) = sin(pos / 10000^{2i/d_model})
>
> PE(pos, 2i+1) = cos(pos / 10000^{2i/d_model})

Each dimension corresponds to a sinusoid with wavelengths forming a geometric progression from 2*pi to 10000*2*pi. For any fixed offset k, PE_{pos+k} can be represented as a linear function of PE_pos, which the authors hypothesized would allow the model to learn relative positional attention.

### Key Technical Components

- **Encoder:** Stack of N = 6 identical layers, each with two sub-layers: (1) multi-head self-attention, (2) position-wise FFN. Each sub-layer wrapped with a residual connection and layer normalization: LayerNorm(x + Sublayer(x)). All sub-layers and embedding layers produce outputs of dimension d_model = 512.

- **Decoder:** Stack of N = 6 identical layers with three sub-layers: (1) masked multi-head self-attention (causal mask prevents attending to future positions), (2) multi-head encoder-decoder attention (queries from decoder, keys/values from encoder output), (3) position-wise FFN. Residual connections and layer normalization around each sub-layer.

- **Three uses of multi-head attention:** (1) Encoder self-attention -- all positions attend to all positions in the previous encoder layer. (2) Decoder self-attention -- positions attend only to preceding positions (causal masking via setting illegal connections to -infinity before softmax). (3) Encoder-decoder attention -- queries from decoder, keys/values from encoder, allowing every decoder position to attend over all input positions.

- **Weight sharing:** The same weight matrix is shared between the two embedding layers (source and target) and the pre-softmax linear transformation. Embedding weights are multiplied by sqrt(d_model).

- **Regularization:** (1) Residual dropout P_drop = 0.1 applied to each sub-layer output before addition and normalization, and to the sum of embeddings and positional encodings. (2) Label smoothing epsilon_ls = 0.1, which hurts perplexity but improves accuracy and BLEU.

- **Optimizer:** Adam with beta_1 = 0.9, beta_2 = 0.98, epsilon = 10^{-9}. Learning rate schedule with linear warmup for warmup_steps = 4000, then inverse square root decay:

> lrate = d_model^{-0.5} * min(step_num^{-0.5}, step_num * warmup_steps^{-1.5})

### Experimental Setup

- **Machine translation data:** WMT 2014 English-German (~4.5M sentence pairs, BPE with ~37K shared vocabulary) and WMT 2014 English-French (~36M sentence pairs, 32K word-piece vocabulary).
- **Batching:** Sentence pairs batched by approximate sequence length, ~25K source + ~25K target tokens per batch.
- **Hardware:** 8 NVIDIA P100 GPUs on a single machine.
- **Training duration:** Base model: 100K steps (12 hours), ~0.4 seconds per step. Big model: 300K steps (3.5 days), ~1.0 seconds per step.
- **Inference:** Beam search with beam size 4, length penalty alpha = 0.6, max output length = input length + 50. Base models average last 5 checkpoints (10-min intervals); big models average last 20 checkpoints.
- **Constituency parsing:** 4-layer transformer with d_model = 1024, trained on WSJ portion of Penn Treebank (~40K sentences) and semi-supervised with ~17M sentences.

### Key Results

**Machine translation (Table 2, newstest2014):**

| Model | EN-DE BLEU | EN-FR BLEU | Training Cost (FLOPs) |
|---|---|---|---|
| GNMT + RL | 24.6 | 39.92 | 2.3e19 / 1.4e20 |
| ConvS2S | 25.16 | 40.46 | 9.6e18 / 1.5e20 |
| MoE | 26.03 | 40.56 | 2.0e19 / 1.2e20 |
| GNMT + RL Ensemble | 26.30 | 41.16 | 1.8e20 / 1.1e21 |
| ConvS2S Ensemble | 26.36 | 41.29 | 7.7e19 / 1.2e21 |
| **Transformer (base)** | **27.3** | 38.1 | **3.3e18** |
| **Transformer (big)** | **28.4** | **41.8** | 2.3e19 |

- The Transformer (big) achieves **28.4 BLEU on EN-DE**, surpassing all prior models including ensembles by more than 2.0 BLEU.
- On EN-FR, the Transformer (big) achieves **41.8 BLEU**, a new single-model state-of-the-art, at less than 1/4 the training cost of the previous best single model.
- The base model alone (3.3e18 FLOPs) surpasses all previously published single models and ensembles on EN-DE, at a fraction of the training cost.

**Model variations (Table 3, newstest2013 dev set):**

| Configuration | PPL (dev) | BLEU (dev) | Params (M) |
|---|---|---|---|
| Base (h=8, d_k=d_v=64) | 4.92 | 25.8 | 65 |
| h=1, d_k=d_v=512 | 5.29 | 24.9 | 65 |
| h=16, d_k=d_v=32 | 4.91 | 25.8 | 65 |
| h=32, d_k=d_v=16 | 5.01 | 25.4 | 65 |
| N=2 layers | 6.11 | 23.7 | 36 |
| N=8 layers | 4.88 | 25.5 | 80 |
| d_model=1024, d_ff=4096 | 4.66 | 26.0 | 168 |
| Learned positional embeddings | 4.92 | 25.7 | 65 |
| Big (d_model=1024, h=16) | 4.33 | 26.4 | 213 |

- Single-head attention is 0.9 BLEU worse than h=8; quality also drops with too many heads (h=32).
- Reducing d_k hurts quality, suggesting dot-product compatibility benefits from higher dimensionality.
- Bigger models improve performance; dropout is important for avoiding overfitting.
- Learned positional embeddings produce nearly identical results to sinusoidal encodings.

**English constituency parsing (Table 4, WSJ Section 23):**

| Parser | Training | F1 |
|---|---|---|
| Dyer et al. (2016) | WSJ only, discriminative | 91.7 |
| **Transformer (4 layers)** | **WSJ only, discriminative** | **91.3** |
| Vinyals & Kaiser et al. (2014) | semi-supervised | 92.1 |
| **Transformer (4 layers)** | **semi-supervised** | **92.7** |
| Dyer et al. (2016) | generative | 93.3 |

- The Transformer generalizes to constituency parsing despite no task-specific tuning, outperforming all models except the Recurrent Neural Network Grammar in the semi-supervised setting.

### Computational Complexity Comparison

| Layer Type | Complexity per Layer | Sequential Ops | Max Path Length |
|---|---|---|---|
| Self-Attention | O(n^2 * d) | O(1) | O(1) |
| Recurrent | O(n * d^2) | O(n) | O(n) |
| Convolutional | O(k * n * d^2) | O(1) | O(log_k(n)) |
| Self-Attention (restricted) | O(r * n * d) | O(1) | O(n/r) |

- Self-attention achieves **O(1) maximum path length** between any two positions (vs. O(n) for RNNs), which is the key advantage for learning long-range dependencies.
- Self-attention is faster than recurrence when sequence length n < representation dimension d, which holds for most sentence-level NLP tasks with subword tokenization.
- The O(n^2) complexity per layer becomes a bottleneck for very long sequences; the paper suggests restricted self-attention (neighborhood size r) as a future direction.

---

## Conclusions

1. **Pure attention is sufficient for state-of-the-art sequence transduction.** The Transformer demonstrates that recurrence and convolution can be entirely replaced by multi-head self-attention without sacrificing quality, achieving new state-of-the-art results on EN-DE (28.4 BLEU) and EN-FR (41.8 BLEU) translation benchmarks.

2. **Massive parallelization advantage over recurrent models.** By eliminating sequential dependencies, the Transformer can be trained in 12 hours (base) to 3.5 days (big) on 8 P100 GPUs -- a fraction of the training cost of competitive recurrent and convolutional models that required orders of magnitude more FLOPs.

3. **Multi-head attention enables attending to multiple representation subspaces simultaneously.** The ablation study confirms that multiple heads (h=8) outperform single-head attention by 0.9 BLEU, and that the per-head key dimension d_k matters for compatibility computation quality.

4. **Sinusoidal positional encodings match learned embeddings.** The fixed sinusoidal scheme using a geometric progression of wavelengths produces equivalent results to learned positional embeddings, with the potential advantage of extrapolation to unseen sequence lengths -- a hypothesis that later work on positional encoding extensively investigated.

5. **Constant path length for long-range dependencies.** Self-attention connects any two positions in O(1) sequential operations with O(1) maximum path length, compared to O(n) for recurrent layers. This architectural property is the primary theoretical motivation for the design.

6. **The architecture generalizes beyond machine translation.** Without task-specific modifications, the Transformer achieves competitive results on English constituency parsing, outperforming the BerkeleyParser even when trained only on 40K WSJ sentences.

7. **Architectural simplicity enables scalability.** The Transformer's uniform structure -- stacked layers of self-attention and FFN with residual connections -- proved to be a foundation for subsequent scaling to much larger models (GPT, BERT, and their successors), a consequence the authors anticipated in their future work discussion.

---

## Core References and Why They Are Referenced

### Sequence Transduction Predecessors

- **Sutskever et al. (2014)** -- *Sequence to Sequence Learning with Neural Networks.* Establishes the encoder-decoder paradigm for neural sequence transduction using stacked LSTMs. The Transformer retains the encoder-decoder structure but replaces recurrence with self-attention.

- **Bahdanau et al. (2014)** -- *Neural Machine Translation by Jointly Learning to Align and Translate.* Introduces additive attention for neural machine translation, allowing the decoder to attend to different parts of the source sentence. The Transformer generalizes this with multi-head dot-product attention applied not only for encoder-decoder cross-attention but also for self-attention within encoder and decoder.

- **Cho et al. (2014)** -- *Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation.* Introduces the GRU and the basic RNN encoder-decoder. One of the recurrent architectures the Transformer aims to replace.

### Attention Mechanisms

- **Luong et al. (2015)** -- *Effective Approaches to Attention-Based Neural Machine Translation.* Proposes dot-product (multiplicative) attention as an alternative to additive attention. The Transformer adopts dot-product attention with the addition of 1/sqrt(d_k) scaling.

- **Parikh et al. (2016)** -- *A Decomposable Attention Model.* One of the few prior models using attention without recurrence, applied to natural language inference. Referenced as a predecessor to the fully attention-based approach.

### Convolutional Sequence Models

- **Gehring et al. (2017)** -- *Convolutional Sequence to Sequence Learning (ConvS2S).* Primary convolutional baseline achieving competitive translation results. Requires O(n/k) layers to connect distant positions, compared to O(1) for self-attention.

- **Kalchbrenner et al. (2017)** -- *Neural Machine Translation in Linear Time (ByteNet).* Convolutional model with O(log_k(n)) path length via dilated convolutions. Referenced as an alternative parallel architecture with worse long-range dependency characteristics.

### Architectural Components

- **He et al. (2016)** -- *Deep Residual Learning for Image Recognition.* Introduces residual connections used around each sub-layer in the Transformer. Critical for enabling deep stacking of attention and FFN layers.

- **Ba et al. (2016)** -- *Layer Normalization.* Provides the normalization technique applied after each residual connection in the Transformer.

- **Sennrich et al. (2015)** -- *Neural Machine Translation of Rare Words with Subword Units.* BPE tokenization used for the EN-DE experiments.

- **Wu et al. (2016)** -- *Google's Neural Machine Translation System (GNMT).* Word-piece tokenization used for EN-FR experiments. Also provides the primary RNN-based baseline (GNMT+RL) for translation quality comparisons.

### Regularization and Training

- **Srivastava et al. (2014)** -- *Dropout.* Residual dropout applied to sub-layer outputs and embedding sums.

- **Szegedy et al. (2015)** -- *Rethinking the Inception Architecture for Computer Vision.* Source of label smoothing (epsilon_ls = 0.1), which the paper notes hurts perplexity but improves BLEU.

- **Kingma & Ba (2015)** -- *Adam: A Method for Stochastic Optimization.* Optimizer used with the custom warmup-then-decay learning rate schedule.

- **Press & Wolf (2016)** -- *Using the Output Embedding to Improve Language Models.* Source of the weight-sharing technique between embedding layers and the pre-softmax linear transformation.

### Sequence Modeling Context

- **Hochreiter & Schmidhuber (1997)** -- *Long Short-Term Memory.* The dominant recurrent architecture for sequence modeling that the Transformer aims to replace. Referenced as the state-of-the-art approach for sequence transduction at the time.

- **Hochreiter et al. (2001)** -- *Gradient Flow in Recurrent Nets: The Difficulty of Learning Long-Term Dependencies.* Provides the theoretical motivation for minimizing path length: shorter paths between positions facilitate learning long-range dependencies, which self-attention achieves in O(1).

#### Cross-References in Available Papers

The Transformer paper is referenced by nearly every analysis in the `references/` directory, as it provides the foundational architecture upon which all subsequent work builds. The most substantive connections are:

- **Specialized Attention Heads and Pruning (`2019-07-specialized-attention-heads-pruning`):** Voita et al. (2019) use the Transformer base architecture (N=6, h=8, d_model=512) directly and study which attention heads can be pruned. The pruning results provide an empirical complement to the Transformer paper's own finding that h=8 outperforms h=1 by 0.9 BLEU (Table 3 row A), while showing that not all 8 heads are equally important.

- **BERT Attention Analysis (`2019-08-bert-attention-analysis`):** Clark et al. (2019) analyze attention patterns in BERT, a bidirectional encoder built on the Transformer. The finding that individual heads attend to specific syntactic relations parallels the Transformer paper's own attention visualizations (Figures 3--5) showing heads learning syntactic and semantic structure.

- **Dark Secrets of BERT (`2019-11-dark-secrets-of-bert`):** Kovaleva et al. (2019) categorize BERT attention patterns into types (diagonal, vertical, block, heterogeneous). The Transformer paper's appendix visualizations foreshadow this line of research, showing diverse attention behaviors across heads and layers.

- **Sixteen Heads Better Than One (`2019-12-sixteen-heads-better-than-one`):** Michel et al. (2019) extend the Transformer paper's Table 3 ablation on head count, showing that individual heads can be pruned at inference time. Their WMT experiments use the Transformer-large architecture (d_model=1024, h=16) from Table 3.

- **Quantifying Attention Flow (`2020-07-quantifying-attention-flow`):** Abnar and Zuidema (2020) analyze information propagation through the Transformer's residual connections (V_{l+1} = V_l + W_att V_l), proposing attention rollout and attention flow methods.

- **FF Layers as Key-Value Memories (`2021-11-ff-layers-key-value-memories`):** Geva et al. (2021) reinterpret the position-wise FFN (Equation 2) as key-value memories, providing a mechanistic account of the component the Transformer paper describes as "two convolutions with kernel size 1."

- **Transformer Circuits Framework (`2021-12-transformer-circuits-framework`):** Elhage et al. (2021) provide a rigorous mathematical framework for decomposing the Transformer's self-attention into interpretable circuits, directly analyzing the QKV formulation and residual stream introduced in this paper.

- **PI (`2023-06-pi-positional-interpolation`):** Chen et al. (2023) test and extend the Transformer paper's hypothesis that sinusoidal-style positional encodings allow extrapolation to longer sequences, finding that RoPE-based models require interpolation rather than extrapolation for context extension.

- **YaRN (`2024-05-yarn-context-extension`):** Peng et al. (2024) reference the Transformer paper for introducing the original sinusoidal positional encodings, which RoPE (and by extension YaRN) generalize by applying frequency-based rotations directly to query and key vectors.

- **Lost in the Middle (`2024-02-lost-in-the-middle`):** Liu et al. (2024) note that the Transformer's self-attention mechanism is theoretically capable of attending equally to any position, making the observed U-shaped serial-position bias a surprising emergent phenomenon rather than an architectural limitation.

- **Position Bias in Transformers (`2025-07-position-bias-transformers`):** Analyses position bias as an emergent property of the multi-layer attention mechanism introduced in this paper, studying how depth and attention head interaction create systematic positional preferences despite the architecture's position-agnostic design.

- **DroPE (`2025-12-drope-dropping-positional-embeddings`):** Modifies the absolute positional embedding scheme introduced in the Transformer paper, proposing to selectively drop positional embeddings for context extension.
