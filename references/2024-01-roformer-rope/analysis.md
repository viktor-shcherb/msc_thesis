# RoFormer: Enhanced Transformer with Rotary Position Embedding

**Authors:** Jianlin Su, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, Yunfeng Liu (Zhuiyi Technology Co., Ltd.)
**Date:** April 2021, arXiv:2104.09864; published in Neurocomputing 568, 127063, January 2024

---

## Core Research Problem

Transformer-based language models are inherently position-agnostic (Yun et al., 2020), requiring explicit injection of positional information. Existing approaches fall into two categories:

1. **Absolute position embeddings** (Vaswani et al., 2017; Devlin et al., 2019) add a position-dependent vector to the word embedding before projecting into queries, keys, and values: `f_t(x_i, i) = W_t(x_i + p_i)`. This couples absolute position into the representation and limits sequence length to a fixed maximum L.

2. **Relative position embeddings** (Shaw et al., 2018; Dai et al., 2019; Raffel et al., 2020; He et al., 2020) decompose the query-key inner product `q^T_m k_n` into terms from Equation (3) and replace absolute position embeddings with relative counterparts. These methods modify individual terms in the additive decomposition, introducing additional trainable parameters and complicating the formulation.

Both categories share a fundamental limitation: they **add** position information to context representations. This makes them incompatible with linear self-attention architectures (Katharopoulos et al., 2020), where the attention computation relies on separable kernel feature maps applied to queries and keys independently. Additive position encodings break this separability.

**The core challenge is to design a position encoding that encodes absolute position, incorporates explicit relative position dependency in the self-attention inner product, decays with increasing relative distance, and remains compatible with linear self-attention -- all without adding position information to the context representations.**

---

## Problem Solutions

RoPE (Rotary Position Embedding) encodes position by **multiplying** (not adding) query and key vectors with a rotation matrix whose angle is proportional to the token's absolute position. The resulting query-key inner product depends only on relative position.

1. **Multiplicative encoding via rotation.** Position information is injected by rotating the affine-transformed word embedding by an angle proportional to the position index: `f_{q,k}(x_m, m) = R^d_{Θ,m} W_{q,k} x_m`. The rotation matrix R is block-diagonal with 2x2 rotation blocks, each rotating a pair of dimensions by `m * θ_i`.
2. **Relative position from rotation matrix product.** The inner product `q^T_m k_n = x^T_m W_q R^d_{Θ,n-m} W_k x_n` depends only on the relative position `n - m` through the product `(R^d_{Θ,m})^T R^d_{Θ,n}`.
3. **Long-term decay.** With the frequency schedule `θ_i = 10000^{-2(i-1)/d}`, the upper bound on the inner product magnitude decays as relative distance increases.
4. **Linear attention compatibility.** Because rotation preserves vector norms, RoPE can be applied after the non-negative feature maps in linear attention without breaking the kernel decomposition.

---

## Approach Details

### Method

The paper formulates the position encoding problem as finding functions `f_q`, `f_k` such that the query-key inner product depends only on word embeddings and relative position:

> ⟨f_q(x_m, m), f_k(x_n, n)⟩ = g(x_m, x_n, m − n)

**2D case.** Using complex number representation, the paper derives (with initial condition `f_{q,k}(x, 0) = W_{q,k} x`):

> f_q(x_m, m) = (W_q x_m) e^{imθ}
> f_k(x_n, n) = (W_k x_n) e^{inθ}
> g(x_m, x_n, m − n) = Re[(W_q x_m)(W_k x_n)* e^{i(m−n)θ}]

The derivation proceeds by decomposing `f_{q,k}` into radial and angular components in polar form (Eq. 23), showing that the radial component is independent of position (Eq. 27) and the angular component is an arithmetic progression `ϕ(m) = mθ + γ` (Eq. 30). Setting `γ = 0` yields the final solution (Eq. 33).

In matrix form for 2D:

> f_{q,k}(x_m, m) = [[cos mθ, −sin mθ], [sin mθ, cos mθ]] W_{q,k} x_m

**General d-dimensional case.** The d-dimensional space (d even) is divided into d/2 two-dimensional subspaces, each with its own rotation angle. The position-encoded query/key is:

> f_{q,k}(x_m, m) = R^d_{Θ,m} W_{q,k} x_m

where R^d_{Θ,m} is a block-diagonal matrix of d/2 rotation blocks (Eq. 15):

> R^d_{Θ,m} = diag(R(mθ_1), R(mθ_2), ..., R(mθ_{d/2}))

with each block R(mθ_i) = [[cos mθ_i, −sin mθ_i], [sin mθ_i, cos mθ_i]] and frequency parameters:

> Θ = {θ_i = 10000^{−2(i−1)/d}, i ∈ [1, 2, ..., d/2]}

The self-attention inner product becomes:

> q^T_m k_n = (R^d_{Θ,m} W_q x_m)^T (R^d_{Θ,n} W_k x_n) = x^T_m W_q R^d_{Θ,n−m} W_k x_n

where R^d_{Θ,n−m} = (R^d_{Θ,m})^T R^d_{Θ,n}. Since R^d_Θ is orthogonal, encoding position preserves vector norms and ensures numerical stability.

### Key Technical Components

**Efficient computation.** The sparse block-diagonal structure of R^d_{Θ,m} enables an element-wise implementation avoiding full matrix multiplication (Eq. 34):

> R^d_{Θ,m} x = x ⊗ [cos mθ_1, cos mθ_1, ..., cos mθ_{d/2}, cos mθ_{d/2}] + [−x_2, x_1, −x_4, x_3, ..., −x_d, x_{d−1}] ⊗ [sin mθ_1, sin mθ_1, ..., sin mθ_{d/2}, sin mθ_{d/2}]

where ⊗ denotes element-wise multiplication. This requires only two element-wise multiplications and one addition -- the same computational cost as applying sinusoidal absolute position embeddings.

**No position in value vectors.** RoPE is applied only to queries and keys, not to values. The value computation remains `v_n = W_v x_n`, consistent with the trend in relative position encoding methods (Dai et al., 2019; Raffel et al., 2020).

**Linear attention integration.** For linear attention with feature maps ϕ, φ (Eq. 18), RoPE is applied after the feature maps:

> Attention(Q, K, V)_m = [Σ_n (R^d_{Θ,m} ϕ(q_m))^T (R^d_{Θ,n} φ(k_n)) v_n] / [Σ_n ϕ(q_m)^T φ(k_n)]

The denominator is kept unchanged (without rotation) to avoid division by zero, since the rotated numerator may contain negative terms.

### Theoretical Analysis

**Derivation of uniqueness (Section 3.4.1).** The 2D solution is derived from first principles using complex number decomposition. Setting `m = n` in the constraint equation shows the radial component is position-independent (Eq. 27). The angular component satisfies the recurrence `ϕ(m + 1) − ϕ(m) = constant`, yielding the arithmetic progression `ϕ(m) = mθ` (Eq. 30).

**Long-term decay (Section 3.4.3).** Using Abel transformation (summation by parts), the inner product can be bounded:

> |Σ_{i=0}^{d/2−1} q_{[2i:2i+1]} k*_{[2i:2i+1]} e^{i(m−n)θ_i}| ≤ (max_i |h_{i+1} − h_i|) Σ_{i=0}^{d/2−1} |S_{i+1}|

where h_i = q_{[2i:2i+1]} k*_{[2i:2i+1]} and S_j = Σ_{i=0}^{j−1} e^{i(m−n)θ_i}. The average of |S_i| decays as relative distance |m − n| increases with the frequency schedule θ_i = 10000^{−2i/d} (Figure 2). This provides a desirable inductive bias: tokens at large relative distances contribute less to each other's attention.

### Experimental Setup

**Machine translation:** WMT 2014 English-German (~4.5M sentence pairs), Transformer-base architecture, fairseq toolkit, Adam optimizer (β_1 = 0.9, β_2 = 0.98), beam search (size 4, length penalty 0.6), label smoothing 0.1, 37k BPE vocabulary.

**Pre-training (English):** bert-base-uncased architecture with RoPE replacing sinusoidal PE. BookCorpus + Wikipedia, 80/20 train/validation split, batch size 64, max sequence length 512, 100k steps, AdamW with learning rate 1e-5.

**GLUE fine-tuning:** MRPC, SST-2, QNLI, STS-B, QQP, MNLI. 3 epochs, max sequence length 512, batch size 32, learning rates {2, 3, 4, 5}e-5, best-averaged validation results.

**Performer with RoPE:** 12-layer char-based Performer, 768 dimensions, 12 heads, Enwik8 dataset, learning rate 1e-4, batch size 128, max sequence length 1024.

**Chinese long text:** RoFormer pre-trained on ~34GB Chinese data (Wikipedia, news, forums) in multiple stages with varying max sequence lengths (128--1536) and batch sizes (256--512). Evaluated on CAIL2019-SCM (8964 case triplets, similar case matching). Hardware: two cloud servers with 4x V100 GPUs each.

### Key Results

**Machine translation (Table 1):**

| Model | BLEU |
|---|---|
| Transformer-base (Vaswani et al., 2017) | 27.3 |
| RoFormer | **27.5** |

**GLUE fine-tuning (Table 2):**

| Model | MRPC (F1) | SST-2 (Acc) | QNLI (Acc) | STS-B (Spearman) | QQP (F1) | MNLI (m/mm Acc) |
|---|---|---|---|---|---|---|
| BERT | 88.9 | **93.5** | **90.5** | 85.8 | 71.2 | **84.6/83.4** |
| RoFormer | **89.5** | 90.7 | 88.0 | **87.0** | **86.4** | 80.2/79.8 |

- RoFormer outperforms BERT on MRPC (+0.6), STS-B (+1.2), and QQP (+15.2 F1). BERT outperforms RoFormer on SST-2, QNLI, and MNLI.

**Chinese long text -- CAIL2019-SCM (Table 5):**

| Model | Validation | Test |
|---|---|---|
| BERT-512 | 64.13% | 67.77% |
| WoBERT-512 | 64.07% | 68.10% |
| RoFormer-512 | 64.13% | 68.29% |
| RoFormer-1024 | **66.07%** | **69.79%** |

- At 512 tokens, RoFormer is comparable to baselines. At 1024 tokens, it outperforms WoBERT-512 by +1.69% absolute on the test set, demonstrating RoPE's sequence length flexibility.

**Pre-training convergence (Figure 3):** RoFormer achieves faster MLM loss convergence than BERT. Performer with RoPE achieves lower LM loss than Performer without RoPE under identical training conditions.

### Impact and Adoption

RoPE's practical impact far exceeds what the paper's original experimental results suggest. RoPE became the standard positional encoding for decoder-only LLMs:

- **LLaMA / LLaMA 2 / LLaMA 3** (Meta): All variants use RoPE. LLaMA's adoption of RoPE established it as the default for open-weight LLMs.
- **Falcon** (TII): Falcon-7B and Falcon-40B use RoPE.
- **Pythia** (EleutherAI): All Pythia models use RoPE.
- **Qwen / Qwen 2** (Alibaba): Uses RoPE with modified base frequencies.
- **Mistral / Mixtral** (Mistral AI): Uses RoPE.
- **Gemma** (Google DeepMind): Uses RoPE.
- **Code Llama** (Meta): Uses RoPE with NTK-aware base change (b = 1,000,000).

RoPE's frequency-based structure enabled a family of context extension methods: Position Interpolation (Chen et al., 2023), NTK-Aware Scaled RoPE (bloc97, 2023), YaRN (Peng et al., 2023), LongRoPE (Ding et al., 2024), and STRING (Chen et al., 2025). All operate by modifying RoPE's frequency parameters or position indices.

Integrated into Hugging Face Transformers (v4.31.0+) with built-in support for RoPE scaling methods.

### Limitations

The paper acknowledges two limitations:

1. **No explanation for faster convergence.** Despite demonstrating that RoFormer converges faster than BERT during pre-training, the paper does not provide a theoretical explanation for why multiplicative position encoding leads to faster learning.
2. **No explanation for long-text superiority.** While the long-term decay property is proved, the paper does not explain why this specific decay profile leads to superior performance on long texts compared to other position encodings with similar decay properties.

---

## Conclusions

1. **Multiplicative position encoding via rotation.** RoPE introduces a fundamentally different approach to position encoding: instead of adding position embeddings to context representations, it multiplies query and key vectors by a rotation matrix. This naturally encodes relative position through the rotation matrix product R^d_{Θ,n−m}.

2. **Principled derivation from a relative position constraint.** The rotation formulation is derived from first principles by requiring the query-key inner product to depend only on relative position (Eq. 11), yielding a unique solution (up to constants) in the 2D case, which generalizes cleanly to arbitrary even dimensions via block-diagonal structure.

3. **Long-term decay property.** Using the frequency schedule θ_i = 10000^{−2(i−1)/d}, RoPE provably produces decaying attention scores with increasing relative distance, providing a useful inductive bias for natural language.

4. **Linear attention compatibility.** Because rotation preserves norms, RoPE can be combined with linear attention by applying the rotation after the kernel feature maps, enabling relative position encoding in O(N) attention architectures.

5. **De facto standard for modern LLMs.** Despite the paper's modest experimental improvements on BERT-scale models, RoPE became the dominant positional encoding in the LLM era, adopted by LLaMA, Falcon, Pythia, Qwen, Mistral, and Gemma, and spawning an entire research direction on RoPE-based context extension.

---

## Core References and Why They Are Referenced

### Position Encoding Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the Transformer architecture and sinusoidal absolute position embeddings. RoPE's frequency schedule θ_i = 10000^{−2(i−1)/d} is directly inherited from Vaswani et al.'s sinusoidal formulation, but applied multiplicatively rather than additively.
- **Shaw et al. (2018)** -- *Self-Attention with Relative Position Representations.* Introduces clipped relative position embeddings added to keys and values (Eq. 5). Represents the first approach to relative position encoding in Transformers; RoPE addresses the same goal through rotation.
- **Dai et al. (2019)** -- *Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context.* Decomposes the query-key product into four terms (Eq. 6--7) and introduces sinusoid-encoded relative position, with trainable vectors replacing absolute position. RoPE avoids this additive decomposition entirely.
- **Raffel et al. (2020)** -- *T5: Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer.* Simplifies relative position encoding to a trainable bias `b_{i,j}` added to the attention logits (Eq. 8). RoPE achieves relative position encoding without any additive bias terms.
- **He et al. (2020)** -- *DeBERTa: Decoding-Enhanced BERT with Disentangled Attention.* Uses the middle two terms of the four-way decomposition (Eq. 10) for relative position encoding. Represents the state of the art in additive relative PE at the time.

### Linear Attention

- **Katharopoulos et al. (2020)** -- *Transformers Are RNNs: Fast Autoregressive Transformers with Linear Attention.* Introduces linear attention via kernel feature maps (Eq. 18). RoPE's norm-preserving rotation enables combining relative position encoding with linear attention (Eq. 19), which additive methods cannot support.
- **Choromanski et al. (2020)** -- *Rethinking Attention with Performers.* Provides the Performer architecture used in RoPE's linear attention experiments (Section 4.4). RoPE with Performer achieves lower LM loss than Performer without position encoding.

### Baseline Models

- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* Primary baseline for pre-training and GLUE experiments. Uses trainable absolute position embeddings limited to 512 tokens.
- **Wei et al. (2019)** -- *NEZHA: Neural Contextualized Representation for Chinese Language Understanding.* Chinese pre-trained model using relative position encoding; baseline comparison in Chinese experiments (Table 3).

### Evaluation

- **Bojar et al. (2014)** -- *Findings of the 2014 Workshop on Statistical Machine Translation.* Provides the WMT 2014 English-German dataset used in the machine translation experiment.
- **Singh et al. (2018)** -- *GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding.* Provides the benchmark tasks (MRPC, SST-2, QNLI, STS-B, QQP, MNLI) used for fine-tuning evaluation.
- **Xiao et al. (2019)** -- *CAIL2019-SCM: A Dataset of Similar Case Matching in Legal Domain.* Provides the Chinese long text classification dataset (documents > 512 characters) used to demonstrate RoPE's sequence length flexibility.

### Cross-References in Available Papers

This paper is foundational to the majority of papers in the `references/` directory that deal with positional encoding or context extension. The key cross-references are:

- **PI (`2023-06-pi-positional-interpolation`):** Builds directly on RoPE's mathematical formulation (Eq. 1--2 in PI). PI rescales position indices `m → mL/L'` before applying RoPE, achieving context extension through interpolation rather than extrapolation. PI improves upon the extrapolation bound derived from RoPE (~600x tighter).
- **NTK-Aware Scaled RoPE (`2023-06-rope-ntk`):** Modifies RoPE's base parameter from `b` to `b' = b * s^{|D|/(|D|-2)}`, spreading interpolation pressure non-uniformly across frequencies. Operates directly on the frequency formulation `θ_i = b^{-2i/|D|}` introduced in this paper.
- **YaRN (`2024-05-yarn-context-extension`):** Extends RoPE via frequency-aware interpolation (NTK-by-parts) plus learned attention temperature scaling. Formalizes the wavelength analysis of RoPE dimensions and identifies which encode relative vs. absolute position. The entire paper builds on RoPE's frequency-based rotation formulation.
- **DroPE (`2025-12-drope-dropping-positional-embeddings`):** Proposes removing RoPE after pretraining and recalibrating, arguing that RoPE-scaling methods inevitably fail because low-frequency compression shifts semantic attention heads. Shows RoPE is essential for efficient pretraining convergence (Proposition 3.3) but harmful for context extension.
- **STRING (`2025-04-effective-context-length-falls-short`):** Identifies the left-skewed position frequency distribution in RoPE's relative position matrix as the root cause of ineffective long-context utilization. Manipulates RoPE's position matrix directly at inference time by shifting position indices.
- **Position Bias in Transformers (`2025-07-position-bias-transformers`):** Provides formal characterization of RoPE's decay effect: single-layer Gaussian-like decay proportional to `(i-j)^2 θ_1^2` (Lemma 4.6), and multi-layer decay incorporating both the causal mask primacy effect and RoPE's distance decay (Theorem 4.7). Shows RoPE's decay is substantially weaker than the decay mask's due to `θ_1 ~ 1/10000`.
- **Pos2Distill (`2025-11-pos2distill-position-bias-distillation`):** Identifies RoPE's long-range decay as one root cause of positional bias in retrieval and reasoning tasks, and proposes distillation-based mitigation.
- **StreamingLLM (`2024-05-attention-sinks-streaming`):** Designs cache position re-indexing specifically for RoPE by caching Keys before the rotary transformation, enabling correct relative position computation in the sliding window.
- **Landmark Attention (`2023-12-landmark-attention-infinite-context`):** Leverages RoPE's property of adding position information to Q/K just before attention computation, enabling position-free cache storage for retrieved blocks.
- **RULER (`2024-10-ruler-context-size`):** Finds that top-performing open-source models share larger RoPE base frequencies, and that training context length alone does not explain long-context performance (LWM-1M underperforms LWM-512K, likely due to insufficient training for the new RoPE base).
- **Lost in the Middle (`2024-02-lost-in-the-middle`):** Evaluates models using condensed RoPE (LongChat-13B-16K). The U-shaped performance pattern is later explained by the interaction between RoPE's decay and the causal mask's primacy bias (formalized in Position Bias in Transformers).
- **LongBench (`2024-08-longbench-bilingual-benchmark`):** Evaluates several models using linear RoPE scaling (LongChat-v1.5-7B-32k, Vicuna-v1.5-7B-16k).
- **L-Eval (`2024-08-l-eval-standardized-evaluation`):** References RoPE as the basis for PI and NTK-aware scaling techniques; demonstrates that increasing the NTK base improves retrieval but degrades reasoning.
- **Ada-LEval (`2024-06-ada-leval-length-adaptable-benchmark`):** Evaluates NTK-aware Scaled RoPE, ReRoPE, and Leaky ReRoPE, showing scalable position embeddings are viable alternatives to long-context training.
- **NoLiMA (`2025-07-nolima-long-context-evaluation`):** Uses RoPE's relative-distance property in Llama 3.x to disentangle position from context-length effects in the aligned-depth analysis.
- **∞Bench (`2024-08-infinitebench-long-context-evaluation`):** References RoPE as the encoding modified by context extension methods like YaRN that are evaluated on the benchmark.
