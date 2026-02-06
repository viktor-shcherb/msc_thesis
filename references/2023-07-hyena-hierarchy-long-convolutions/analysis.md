---
title: "Hyena Hierarchy: Towards Larger Convolutional Language Models"
authors: "Poli, Massaroli, Nguyen, Fu, Dao, Baccus, Bengio, Ermon, Ré"
year: 2023
venue: "ICML 2023"
paper_type: conference-paper
categories: ["architecture", "attention-efficiency", "state-space-models"]
scope: ["subquadratic attention replacement", "long convolutions", "data-controlled gating", "language modeling", "image classification"]
benchmarks_used: ["perplexity-wikitext103", "perplexity-pile", "perplexity-pg19", "superglue", "imagenet-1k"]
models_introduced: ["hyena"]
models_evaluated: ["transformer-base", "gpt-2", "h3", "s4", "linear-transformer"]
key_claims:
  - id: C1
    claim: "Hyena improves accuracy by more than 50 points over operators relying on state spaces and other implicit and explicit methods on associative recall at sequences of thousands to hundreds of thousands of tokens"
    evidence: "Table 4.2, Section 4.1"
    status: supported
    scope: "associative recall, vocabulary size 30, sequence lengths 30K-131K"
    magnitude: "50+ percentage points over H3, GSS, AFT, RWKV"
  - id: C2
    claim: "Hyena is the first attention-free architecture to match Transformer perplexity on WikiText-103 at the 125M parameter scale"
    evidence: "Table 4.3, Section 4.2"
    status: supported
    scope: "125M parameters, WikiText-103, GPT-2 tokenizer"
    magnitude: "18.6 perplexity, identical to Transformer"
  - id: C3
    claim: "Hyena matches GPT perplexity on The Pile with a 20% reduction in total FLOPs at the 355M parameter scale"
    evidence: "Table 4.4, Figure 4.2, Section 4.2"
    status: supported
    scope: "355M parameters, 15B training tokens"
    magnitude: "20% FLOP reduction (3.93 vs 4.77 × 10^19)"
  - id: C4
    claim: "Hyena operators are 100× faster than optimized attention at sequence length 64K"
    evidence: "Figure 4.3, Section 4.4"
    status: supported
    scope: "batch size 64, operator-level benchmark, fused FFTConv CUDA kernel"
    magnitude: "100× speedup at 64K; 2× at 8K vs FlashAttention"
  - id: C5
    claim: "Hyena matches ViT accuracy on ImageNet-1k when used as a drop-in replacement for attention"
    evidence: "Table 4.7, Section 4.5"
    status: supported
    scope: "87-88M parameters, 16×16 and 8×8 patches, ImageNet-1k"
    magnitude: "78.5% vs 78.5% (16×16); 79.8% vs 80.0% (8×8)"
  - id: C6
    claim: "Hyena is the only attention-free operator able to solve associative recall on long sequences, where all other subquadratic operators fail"
    evidence: "Table 4.2, Section 4.1"
    status: supported
    scope: "2-layer models, width 64, vocabulary size 30"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: complementary
    detail: "Hyena proposes a subquadratic drop-in replacement for the attention operator in Transformers, matching quality at sub-billion scale"
  - target: 2022-04-s4-structured-state-spaces
    type: extends
    detail: "Hyena generalizes S4's long convolution approach by replacing SSM-parameterized filters with FFN-based implicit convolutions and adding data-controlled gating"
  - target: 2022-12-flashattention
    type: complementary
    detail: "Hyena benchmarks runtime against FlashAttention, achieving crossover at 4K-8K sequence length and 100× speedup at 64K"
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
---

# Hyena Hierarchy: Towards Larger Convolutional Language Models

**Authors:** Michael Poli, Stefano Massaroli, Eric Nguyen, Daniel Y. Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, Christopher Ré (Stanford University, Mila and Université de Montréal)
**Date:** July 2023, ICML 2023 (Oral), arXiv:2302.10866

---

## Core Research Problem

The attention operator at the heart of Transformers scales quadratically with sequence length L, placing a strict upper bound on the amount of context a model can process. Existing subquadratic alternatives---linearized attention (Katharopoulos et al., 2020), sparse approximations (Child et al., 2019; Kitaev et al., 2020), low-rank methods (Wang et al., 2020), and state-space models (Gu et al., 2022; Dao et al., 2022c)---consistently underperform dense attention on language tasks, requiring hybridization with standard attention layers to reach Transformer quality (Mehta et al., 2022; Dao et al., 2022c).

The authors identify three computational properties of attention that correlate with its quality advantage and are absent from existing subquadratic operators:

1. **Data control:** Attention implements a data-controlled dense linear operator A(u), parameterizing an entire family of linear functions conditioned on the input.
2. **Sublinear parameter scaling:** Parameter counts are decoupled from sequence length, allowing allocation of parameters to FFN layers.
3. **Unrestricted context:** Attention can approximate dependencies between any two positions without locality restrictions.

The core challenge is: **whether subquadratic operators can match the quality of attention at scale by intentionally incorporating these three properties.**

---

## Problem Solutions

Hyena is a class of data-controlled operators constructed from a recurrence of two efficient subquadratic primitives:

1. **Long convolutions** with implicitly parameterized filters (via a feed-forward network), providing unrestricted context and sublinear parameter scaling.
2. **Element-wise multiplicative gating** of input projections, providing data control.

The depth (order N) of the recurrence controls the operator's expressivity. For short recurrences, existing models are recovered as special cases: H3 corresponds to Hyena_2 and GSS to Hyena_1 with SSM-parameterized filters (Remark 3.2). Hyena generalizes to arbitrary order N with free-form implicit filters.

---

## Approach Details

### Method

#### Hyena Operator Definition

Given N+1 linear projections of the input (v, x^1, ..., x^N) and N learnable filters h^1, ..., h^N, the order-N Hyena operator is defined by the recurrence (Definition 3.1):

> z^1_t = v_t
> z^{n+1}_t = x^n_t · (h^n * z^n)_t,  for n = 1, ..., N
> y_t = z^{N+1}_t

where * denotes (causal) convolution and · denotes element-wise multiplication.

**Time complexity:** O(NL log_2 L) (Remark 3.1), since each of the N convolutions is performed in the Fourier domain via FFT in O(L log_2 L).

#### Matrix Form

The Hyena recurrence can be equivalently expressed as a data-controlled matrix decomposition. Let D^n_x = diag(x^n) be L-by-L diagonal matrices and S^n_h be Toeplitz matrices corresponding to filter h^n. Then:

> y = H(u)v = D^N_x S^N_h ... D^2_x S^2_h D^1_x S^1_h v

This decomposition reveals that Hyena implicitly defines a data-controlled matrix H(u) analogous to the attention matrix A(q,k), but evaluated efficiently without materialization.

#### Hyena Filters (Implicit Parameterization)

Each filter h^n is represented as a map from time (or position) t to filter values, learned with a shallow feed-forward neural network (Equation 7):

> h_t = Window(t) · (FFN ∘ PositionalEncoding)(t)

where Window(t) = exp{-αt} is an exponential decay with learnable rate α that varies across channels. The FFN uses sine activations (high-frequency periodic functions) to address the low-frequency bias of neural networks (Basri et al., 2020). The positional encoding maps scalar t to a higher-dimensional representation.

This implicit parameterization decouples the filter length from the parameter count: the FFN has a fixed number of parameters regardless of sequence length L.

### Key Technical Components

#### Projection Layer (Algorithm 1)

1. Input u ∈ ℝ^{L×D} is linearly projected to (N+1)D dimensions
2. A short depthwise convolution (filter size 3) is applied
3. Output is split into N+1 projections: x^1, ..., x^N, v ∈ ℝ^{D×L}

#### Filter Generation (Algorithm 2)

1. Positional encoding maps positions 0, ..., L-1 to ℝ^{L×D_e}
2. FFN (depth 4, width 64, sine activations) maps to filter values
3. Multiply by exponential decay window
4. Split into N filters h^1, ..., h^N

#### Causality

Causal convolutions are guaranteed by evaluating filters only at non-negative positions t = 0, ..., L-1 and zero-padding before FFT (Proposition 3.1).

#### Architecture Configurations

| Size | Depth | Width | FFN Width | Filter FFN Width | Filter FFN Depth | Sine Freq |
|---|---|---|---|---|---|---|
| 125M | 12 | 768 | 3072 | 64 | 4 | 14 |
| 125M-slim | 18 | 768 | 1536 | 64 | 4 | 14 |
| 153M | 18 | 864 | 1728 | 64 | 4 | 14 |
| 355M | 36 | 1024 | 2048 | 64 | 4 | 14 |
| 1.3B | 36 | 2048 | 4096 | 64 | 4 | 14 |

*Table A.4. All models use order 2 Hyena with filter FFN width 64 and depth 4.*

### Experimental Setup

**Mechanistic design benchmarks (Section 4.1):** Synthetic tasks inspired by mechanistic interpretability research (Elhage et al., 2021; Olsson et al., 2022): associative recall, majority voting, counting, ICL of linear functions, arithmetic. 2-layer models, width 64, trained for 200 epochs with AdamW (lr=0.0005, weight decay 0.1, cosine schedule). Sequence lengths from 1024 to 131,136; vocabulary sizes 10, 20, 30, 40.

**WikiText-103 (Section 4.2):** 125M parameter models with GPT-2 tokenizer (vocab 50,257). Baselines from Dao et al. (2022c) trained under identical conditions.

**The Pile (Section 4.2):** 125M and 355M models trained for 5, 10, 15 billion tokens using GPT-2 tokenizer, sequence length 2048, batch size 256, 8× A100 80GB GPUs. Optimizer: AdamW (β₁=0.9, β₂=0.98), peak lr 6×10⁻⁴ (125M) / 4×10⁻⁴ (355M), cosine schedule, weight decay 0.1.

**SuperGLUE (Section 4.3):** 153M Hyena trained for 137B tokens compared against GPTNeo (300B tokens) and RWKV (332B tokens) of similar size. Zero-shot and 3-shot evaluation.

**Runtime benchmarking (Section 4.4):** Operator-level comparison of order-2 Hyena vs attention and FlashAttention (Dao et al., 2022b). Batch size 64, fused FFTConv CUDA kernel.

**ImageNet-1k (Section 4.5):** Drop-in replacement of attention in ViT (87M) with Hyena operator. Trained from scratch with patch sizes 16×16 (seq len 196) and 8×8 (seq len 1024).

**Reproducibility:** Code released at https://github.com/HazyResearch/safari. All hyperparameters specified in Appendix A.

### Key Results

#### Associative Recall (Table 4.2, Vocabulary Size 30)

| Sequence Length | Hyena | FlashTransformer | Transformer | GSS | H3 | AFT | RWKV |
|---|---|---|---|---|---|---|---|
| 30K | 100.0 | 32.4 | ✗ | 5.3 | 8.4 | 2.3 | 12.4 |
| 64K | 100.0 | 26.7 | ✗ | 2.1 | 4.3 | 1.2 | 6.5 |
| 131K | 97.2 | ✗ | ✗ | 0.1 | 0.6 | 0.8 | 2.3 |

- **Hyena is the only attention-free operator to solve associative recall** at long sequences
- At 131K tokens, Hyena outperforms CKConv by 83 points (97.2 vs 14.3, Table A.2)
- Standard Transformer and FlashTransformer run out of memory at 64K+ and 131K+ respectively

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

*\*Results from Dao et al. (2022c). Hyena-3-slim is deeper (18 layers) and thinner.*

- Hyena matches Transformer perplexity **without any attention layers**
- Previous best attention-free result was Hybrid H3, which still used one attention layer

#### The Pile Perplexity (Table 4.4)

| Model | 5B tokens | 10B tokens | 15B tokens | FLOPs (×10¹⁹) |
|---|---|---|---|---|
| GPT (125M) | 13.3 | 11.9 | 11.2 | 1.88 |
| Hyena-2 (153M) | 13.3 | 11.8 | 11.1 | 1.87 |
| GPT (355M) | 11.4 | 9.8 | 9.1 | 4.77 |
| **Hyena-2 (355M)** | **11.3** | **9.8** | **9.2** | **3.93** |

- At 355M, Hyena matches GPT quality with **17.6% fewer FLOPs** (3.93 vs 4.77 × 10¹⁹)
- Preliminary 1.3B results: 10.8 perplexity after 5B tokens

#### SuperGLUE Few-Shot (3) (Table 4.6)

| Model | WSC | WIC | RTE | CB | MultiRC | ReCoRD | BoolQ | COPA | Average |
|---|---|---|---|---|---|---|---|---|---|
| GPTNeo (300B tokens) | 38.5 | 50.0 | 53.8 | 42.9 | 22.4 | 61.4 | 61.0 | 63.0 | 49.1 |
| RWKV (332B tokens) | 32.7 | 49.4 | 47.2 | 37.5 | 0.0 | 58.3 | 55.0 | 64.0 | 43.0 |
| **Hyena (137B tokens)** | **39.4** | **50.1** | **47.6** | **46.4** | **26.7** | **58.1** | **56.0** | **70.0** | **49.3** |

- Hyena matches GPTNeo (49.3 vs 49.1) **despite training on less than half the tokens**
- Hyena outperforms RWKV by 6.3 points average

#### ImageNet-1k Classification (Table 4.7)

| Model | Patch Size | Seq Len | Acc (%) |
|---|---|---|---|
| ViT (87M) | 16×16 | 196 | 78.5 |
| Hyena-ViT (88M) | 16×16 | 196 | 78.5 |
| ViT (87M) | 8×8 | 1024 | 80.0 |
| Hyena-ViT (88M) | 8×8 | 1024 | 79.8 |

- Hyena matches ViT at both patch sizes as a **drop-in replacement** without architectural changes

#### Runtime Benchmarks (Figure 4.3)

- Hyena crossover with standard attention: ~2048 sequence length
- Hyena crossover with FlashAttention: between 4096 and 8192
- **100× speedup** over FlashAttention at 64K sequence length
- At 64K, standard attention runs out of memory in PyTorch

---

## Limitations and Failure Modes

### Acknowledged Limitations

1. **Sub-billion parameter scale.** All language modeling experiments are at ≤355M parameters (with only preliminary 1.3B results). Whether the quality gap closure with Transformers holds at larger scales is unknown (Section 5).

2. **Hardware utilization.** FFT-based long convolutions have lower GPU utilization than optimized attention kernels (Section 3.4, footnote 7). The speedup over FlashAttention materializes only at sequence lengths ≥4K-8K. The authors expect this gap to shrink with improved FFTConv implementations.

3. **Training hyperparameters.** Standard GPT training hyperparameters are used but acknowledged as likely suboptimal for Hyena. The authors note that slightly lower learning rates and modified warmup schedules improve Hyena convergence (Appendix A.2).

### Scope and Comparability

**What was not tested:**
- Models larger than 355M (1.3B is preliminary only)
- Instruction tuning, RLHF, or chat applications
- Tasks requiring complex multi-step reasoning (beyond synthetic tasks)
- Comparison with sparse attention methods (Longformer, BigBird) on long-context tasks
- Inference throughput (only operator-level runtime benchmarked, not end-to-end generation)

**Comparability notes:**
- WikiText-103 baselines are from Dao et al. (2022c) under identical conditions
- On The Pile, GPT and Hyena use the same tokenizer (GPT-2) and training recipe
- SuperGLUE comparison is unequal in training tokens: Hyena trained on 137B tokens vs GPTNeo on 300B and RWKV on 332B. Despite this disadvantage, Hyena matches GPTNeo
- Speed benchmarks measure operator-level runtime, not full model throughput; actual speedups in training depend on the fraction of compute in the attention replacement

---

## Conclusions

### Contributions

1. **Hyena operator.** Introduced a subquadratic drop-in replacement for attention constructed from a recurrence of implicitly parameterized long convolutions and element-wise multiplicative gating. The operator achieves data control, sublinear parameter scaling, and unrestricted context---three properties identified as key to attention's quality advantage.

2. **Implicit filter parameterization.** Demonstrated that FFN-based implicit convolution filters (with exponential decay windowing and sine activations) significantly outperform SSM-based (S4/H3), frequency-domain (FNO), transfer function, and explicit (Conv1d) parameterizations on associative recall, with the gap widening at longer sequences and larger vocabularies (Figure 4.1, Table A.2).

3. **First purely attention-free architecture matching Transformer quality.** Hyena matches Transformer perplexity on WikiText-103 (18.6, Table 4.3) and The Pile with 20% fewer FLOPs at 355M (Table 4.4), without hybridization with attention layers.

4. **Dominant performance on long-range associative recall.** Hyena is the only subquadratic operator to solve associative recall at 64K-131K tokens, outperforming H3, GSS, AFT, RWKV, and FlashTransformer by 50+ points (Table 4.2).

5. **Generality beyond language.** Hyena matches ViT accuracy on ImageNet-1k as a drop-in replacement (Table 4.7) and outperforms S4ND on CIFAR-10 2D classification (91.2% vs 89.9%) with 25% fewer parameters.

### Implications

1. **Attention may not be necessary for quality.** (Inference) The results at sub-billion scale suggest that simpler, principled subquadratic designs can match attention quality without hybridization, but this has not been confirmed at larger scales.

2. **Mechanistic benchmarks predict language modeling performance.** (Inference) Rankings on synthetic tasks (associative recall, induction) correlate with perplexity rankings at fixed sequence length on The Pile (Appendix C), suggesting these benchmarks are useful proxies for architecture design.

3. **Implicit parameterizations scale better than explicit ones.** (Inference) The gap between implicit (Hyena, CKConv) and explicit (Conv1d, FNO) filter parameterizations widens with sequence length and vocabulary size, suggesting implicit methods are essential for long-context modeling.

---

## Key Claims

1. **C1: Hyena improves accuracy by 50+ points over SSM-based and other subquadratic operators on associative recall at long sequences.** Hyena achieves 100% at 64K while the best alternative (RWKV) achieves 6.5%. At 131K, Hyena achieves 97.2% vs 0.1-2.3% for all others. Evidence: Table 4.2. Status: **supported**. Scope: vocabulary size 30, 2-layer models. Single experimental configuration.

2. **C2: Hyena matches Transformer perplexity on WikiText-103.** 18.6 perplexity for both Hyena-3 (125M) and Transformer (125M). Previous best attention-free model (AFT-conv) achieved 28.2. Evidence: Table 4.3. Status: **supported**. Scope: 125M parameters only; baselines from Dao et al. (2022c).

3. **C3: Hyena matches GPT perplexity with ~20% fewer FLOPs at 355M.** At 15B training tokens, Hyena-355M reaches 9.2 perplexity with 3.93×10¹⁹ FLOPs vs GPT-355M at 9.1 perplexity with 4.77×10¹⁹ FLOPs. Evidence: Table 4.4, Figure 4.2. Status: **supported**. Scope: The Pile, GPT-2 tokenizer. Hyena perplexity is 9.2 vs GPT's 9.1, so quality is close but not identical.

4. **C4: Hyena achieves 100× speedup over attention at 64K.** Measured at operator level with batch size 64 using fused FFTConv CUDA kernel. Crossover with FlashAttention occurs between 4K and 8K. Evidence: Figure 4.3. Status: **supported**. Scope: operator-level benchmark only; actual training speedups are smaller because non-attention FLOPs are unchanged.

5. **C5: Hyena matches ViT on ImageNet-1k.** Hyena-ViT (88M) achieves 78.5% top-1 accuracy at 16×16 patches, identical to ViT (87M). At 8×8 patches (seq len 1024), Hyena achieves 79.8% vs ViT's 80.0%. Evidence: Table 4.7. Status: **supported**. Scope: single model size; no comparison at larger ViT scales.

6. **C6: Hyena is the only attention-free operator to solve long-range associative recall.** Among seven operators tested (Hyena, H3, GSS, AFT, RWKV, FlashTransformer, standard Transformer), only Hyena solves the task at 30K+ tokens. Evidence: Table 4.2. Status: **supported**. Scope: 2-layer models, fixed width, vocabulary size 30.

---

## Open Questions

1. **Does Hyena scale to multi-billion parameters?** The paper only provides preliminary 1.3B results (10.8 perplexity at 5B tokens). Whether the quality gap closure holds at GPT-3/LLaMA scale is unknown. **Partially addressed by** Mamba (Gu & Dao, 2024), which matches Transformer++ scaling at 130M-2.8B but uses selective SSMs rather than Hyena's implicit filters.

2. **Can FFT-based operations achieve attention-level hardware utilization?** The paper acknowledges that low GPU utilization of FFTConv is a bottleneck (Section 3.4). Improved implementations and specialized hardware could narrow this gap. **Unresolved.**

3. **Do Hyena's advantages extend to complex multi-step reasoning?** The synthetic benchmarks test recall and induction, but more complex reasoning (multi-hop, chain-of-thought) is not evaluated. **Unresolved.**

4. **Would Hyena-attention hybrids outperform pure Hyena at shorter contexts?** The paper notes that at shorter training lengths (up to 8K), hybridization with attention (as in H3) may yield better downstream results (Appendix A, operator comparisons). **Unresolved.**

---

## Core References and Why They Are Referenced

### Attention and Transformer Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduces the attention operator that Hyena aims to replace. Hyena's design is motivated by three identified properties of attention: data control, sublinear parameter scaling, and unrestricted context.

- **Olsson et al. (2022)** -- *In-Context Learning and Induction Heads.* Identifies induction heads and associative recall as key mechanisms for in-context learning in Transformers. Hyena's evaluation suite (Table 4.1) is grounded in this mechanistic interpretability work.

### State Space Models and Long Convolutions

- **Gu et al. (2021/2022)** -- *S4: Efficiently Modeling Long Sequences with Structured State Spaces.* Foundational SSM work establishing long convolutions as viable sequence modeling primitives. S4 is one of the long convolution parameterizations benchmarked against Hyena's implicit approach.

- **Dao et al. (2022c)** -- *H3: Hungry Hungry Hippos.* H3 combines SSM-based long convolutions with gating, establishing the architecture that Hyena directly generalizes. H3 corresponds to Hyena_2 with SSM-parameterized filters (Remark 3.2).

- **Mehta et al. (2022)** -- *GSS: Long Range Language Modeling via Gated State Spaces.* GSS composes gating with SSM-based convolutions. Corresponds to Hyena_1 (Remark 3.2).

### Subquadratic Attention Alternatives

- **Zhai et al. (2021)** -- *AFT: An Attention Free Transformer.* Attention-Free Transformer combining gating and softmax or explicit convolutions. Evaluated alongside Hyena on associative recall (Table 4.2).

- **Peng (2021)** -- *RWKV-LM.* Linear-complexity RNN-based language model. Compared against Hyena on associative recall (Table 4.2) and SuperGLUE (Tables 4.5, 4.6).

### Implicit Representations and Filter Design

- **Romero et al. (2021b)** -- *CKConv: Continuous Kernel Convolution for Sequential Data.* Implicit parameterization of convolution filters using neural networks. CKConv's approach directly inspires Hyena's filter design (Equation 7).

- **Li et al. (2020)** -- *Fourier Neural Operator.* Frequency-domain filter parameterization used as baseline in long convolution comparisons (Figure 4.1).

### Efficiency

- **Dao et al. (2022b)** -- *FlashAttention.* Hardware-aware exact attention algorithm providing the primary speed comparison target for Hyena's benchmarks (Figure 4.3, Section 4.4).

- **Selesnick and Burrus (2017)** -- *Fast Convolution and Filtering.* FFT-based fast convolution algorithms underlying Hyena's O(L log L) computation via FFTConv.
