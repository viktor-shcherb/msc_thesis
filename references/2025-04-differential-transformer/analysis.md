---
title: "Differential Transformer"
authors: "Ye, Dong, Xia, Sun, Zhu, Huang, Wei"
year: 2025
venue: "ICLR 2025"
paper_type: conference-paper
categories: ["architecture", "attention-analysis"]
scope:
  - "differential attention mechanism"
  - "attention noise cancellation"
  - "attention sinks and irrelevant context"
  - "foundation architecture for large language models"
benchmarks_used:
  - "arc"
  - "hellaswag"
  - "boolq"
  - "piqa"
  - "winogrande"
  - "openbookqa"
  - "niah"
  - "trec"
  - "banking-77"
  - "clinic-150"
  - "xsum"
  - "cnn-dm"
  - "multinews"
  - "qasper"
  - "hotpotqa"
  - "2wikimultihopqa"
  - "gsm8k"
  - "math-hendrycks"
  - "svamp"
  - "asdiv"
  - "mawps"
  - "carp"
  - "tabmwp"
  - "collegemath"
models_introduced:
  - "diff-transformer-3b"
models_evaluated:
  - "transformer-base"
key_claims:
  - id: C1
    claim: "Differential attention computes scores as the difference of two softmax attention maps, cancelling common-mode attention noise"
    evidence: "Section 2.1, Equation 1, Figure 2"
    status: supported
  - id: C2
    claim: "DIFF Transformer requires only ~62% of parameters or ~64% of training tokens to match Transformer's language modeling loss"
    evidence: "Section 3.2, Figure 3"
    status: supported
    magnitude: "6.8B DIFF matches 11B Transformer (62.2%); 160B tokens matches 251B tokens (63.7%)"
  - id: C3
    claim: "DIFF Transformer maintains stable multi-needle retrieval accuracy up to 64K context while Transformer degrades"
    evidence: "Section 3.4, Figure 5, Table 2"
    status: supported
    magnitude: "76% accuracy improvement at 25% depth in 64K context; 30% gap at N=6, R=2 in 4K"
  - id: C4
    claim: "DIFF Transformer improves many-shot in-context learning accuracy by 5.2--21.6% across classification datasets"
    evidence: "Section 3.5, Figure 6"
    status: supported
    scope: "64K context, TREC/Banking-77/Clinic-150 classification"
    magnitude: "5.2% (Clinic-150) to 21.6% (TREC-fine)"
  - id: C5
    claim: "DIFF Transformer is more robust to order permutations in ICL demonstrations"
    evidence: "Section 3.5, Figure 7"
    status: supported
    magnitude: "4.0 vs 19.0 variance range (random arrangement); 13.4 vs 56.7 (class arrangement)"
  - id: C6
    claim: "DIFF Transformer reduces contextual hallucination on text summarization and question answering"
    evidence: "Section 3.6, Table 4"
    status: supported
    magnitude: "XSum: 0.53 vs 0.44; Qasper: 0.39 vs 0.28; HotpotQA: 0.46 vs 0.36"
  - id: C7
    claim: "DIFF Transformer produces substantially fewer activation outliers than Transformer"
    evidence: "Section 3.7, Table 5"
    status: supported
    magnitude: "Top-1 attention logits: 38.8 vs 318.0 (~8.2x reduction)"
  - id: C8
    claim: "4-bit quantized DIFF Transformer achieves comparable accuracy to 6-bit Transformer on HellaSwag"
    evidence: "Section 3.7, Figure 8"
    status: supported
    magnitude: "~25% accuracy advantage at 4-bit quantization"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Replaces single softmax attention with differential attention (difference of two softmax maps) to cancel attention noise"
  - target: 2022-12-flashattention
    type: complementary
    detail: "Provides FlashAttention-compatible implementation of differential attention; directly reuses FlashAttention kernels"
  - target: 2024-01-roformer-rope
    type: complementary
    detail: "Uses RoPE positional encoding with theta increased to 640,000 for long-context extension"
  - target: 2023-02-llama-open-efficient-foundation
    type: extends
    detail: "Adopts LLaMA architecture template (RMSNorm, SwiGLU, bias removal) as the baseline Transformer and starting point for DIFF Transformer"
open_questions:
  - question: "Does differential attention maintain its advantages at larger scale (e.g., 70B+ parameters) and longer pretraining (10T+ tokens)?"
    addressed_by: null
  - question: "Can the reduced activation outliers be exploited for efficient low-bit KV cache compression?"
    addressed_by: null
  - question: "What is the interaction between differential attention and alternative positional encodings beyond RoPE?"
    addressed_by: null
  - question: "How does differential attention affect induction head formation and other mechanistic circuits?"
    addressed_by: null
  - question: "Can pretrained Transformers be converted to differential attention via fine-tuning, or is training from scratch required?"
    addressed_by: null
---

# Differential Transformer

**Tianzhu Ye, Li Dong, Yuqing Xia, Yutao Sun, Yi Zhu, Gao Huang, Furu Wei**
ICLR 2025 (Oral) — Microsoft Research, Tsinghua University

---

## Core Research Problem

Standard Transformer attention using softmax tends to **overallocate attention scores to irrelevant context**, a phenomenon the authors term **attention noise**. When retrieving information from long contexts, Transformers assign only a small fraction of attention to the correct answer while dispersing the remainder across irrelevant tokens (Figure 1). This attention noise drowns out the signal from key information, causing:

1. **Degraded information retrieval** in long contexts, especially multi-needle retrieval tasks
2. **Contextual hallucination** where models generate outputs contradicting provided context
3. **Sensitivity to demonstration order** in in-context learning
4. **Large activation outliers** that hinder quantization

The root cause is that softmax produces a probability distribution that must sum to 1, forcing non-zero attention scores on every token regardless of relevance.

---

## Problem Solutions

The paper proposes **Differential Transformer (DIFF Transformer)**, which replaces conventional softmax attention with **differential attention**. The key ideas are:

1. **Differential attention mechanism** — compute attention scores as the difference between two independent softmax attention maps, analogous to differential amplifiers in electrical engineering that cancel common-mode noise
2. **Drop-in architectural replacement** — the overall architecture maintains the same macro layout as Transformer (stacked layers with attention + FFN), enabling direct reuse of hyperparameters and FlashAttention kernels

---

## Approach Details

### Method

Given input $X \in \mathbb{R}^{N \times d_{\text{model}}}$, the differential attention operator projects to two query-key pairs and a shared value:

> $[Q_1; Q_2] = XW^Q, \quad [K_1; K_2] = XW^K, \quad V = XW^V$
>
> $\text{DiffAttn}(X) = \left(\text{softmax}\left(\frac{Q_1 K_1^T}{\sqrt{d}}\right) - \lambda\, \text{softmax}\left(\frac{Q_2 K_2^T}{\sqrt{d}}\right)\right) V$ (Equation 1)

where $Q_1, Q_2, K_1, K_2 \in \mathbb{R}^{N \times d}$, $V \in \mathbb{R}^{N \times 2d}$, and $\lambda$ is a learnable scalar.

The subtraction cancels common-mode noise present in both attention maps, retaining only the differential signal that distinguishes relevant tokens from irrelevant ones.

**Multi-head differential attention** normalizes each head independently with LayerNorm and applies a fixed multiplier $(1 - \lambda_{\text{init}})$:

> $\text{head}_i = \text{DiffAttn}(X; W_i^Q, W_i^K, W_i^V, \lambda)$
>
> $\overline{\text{head}}_i = (1 - \lambda_{\text{init}}) \cdot \text{LN}(\text{head}_i)$ (Equation 3)
>
> $\text{MultiHead}(X) = \text{Concat}(\overline{\text{head}}_1, \ldots, \overline{\text{head}}_h) W^O$

The number of heads is set to $h = d_{\text{model}} / 2d$, keeping parameters and FLOPs aligned with standard Transformer.

### Key Technical Components

**Lambda reparameterization.** The scalar $\lambda$ is reparameterized as:

> $\lambda = \exp(\lambda_{\mathbf{q}_1} \cdot \lambda_{\mathbf{k}_1}) - \exp(\lambda_{\mathbf{q}_2} \cdot \lambda_{\mathbf{k}_2}) + \lambda_{\text{init}}$ (Equation 2)

where $\lambda_{\mathbf{q}_1}, \lambda_{\mathbf{k}_1}, \lambda_{\mathbf{q}_2}, \lambda_{\mathbf{k}_2} \in \mathbb{R}^d$ are learnable vectors and $\lambda_{\text{init}} \in (0, 1)$ is a constant.

**Exponential initialization.** Default strategy uses layer-dependent initialization: $\lambda_{\text{init}} = 0.8 - 0.6 \times \exp(-0.3 \cdot (l-1))$ where $l \in [1, L]$ is the layer index. Models are robust to this choice — constant $\lambda_{\text{init}} = 0.8$ or $0.5$ gives similar results (Table 6).

**Headwise GroupNorm.** LayerNorm is applied independently per head before concatenation, critical for training stability since differential attention produces sparser and more diverse statistics across heads. Removing GroupNorm degrades DIFF Transformer from 3.062 to 3.122 validation loss, while adding GroupNorm to standard Transformer has negligible effect (Table 6).

**Gradient flow preservation.** The $(1 - \lambda_{\text{init}})$ multiplier after GroupNorm ensures gradient flow magnitude matches conventional Transformer, allowing direct reuse of existing hyperparameters (Appendix G).

**FlashAttention compatibility.** Differential attention decomposes into two standard attention computations that can directly use existing FlashAttention kernels (Appendix A). Three implementation variants are provided depending on whether the kernel supports different dimensions between Q, K and V.

### Overall Architecture

Each Differential Transformer layer:

> $Y^l = \text{MultiHead}(\text{LN}(X^l)) + X^l$ (Equation 4)
>
> $X^{l+1} = \text{SwiGLU}(\text{LN}(Y^l)) + Y^l$ (Equation 5)

using pre-RMSNorm (Zhang & Sennrich, 2019) and SwiGLU activation (Shazeer, 2020), following the LLaMA architecture template (Touvron et al., 2023).

### Experimental Setup

**3B language models (main experiments, Section 3.1):**

| Parameter | Value |
|-----------|-------|
| Layers | 28 |
| Hidden size | 3072 |
| FFN size | 8192 |
| Heads (DIFF / Transformer) | 12 / 24 |
| Head dimension $d$ | 128 |
| Parameters | ~2.8B |
| Vocab size | 100,288 |
| Training tokens | 1T (main) / 350B (Appendix B) |
| Sequence length | 4096 |
| Optimizer | AdamW ($\beta = 0.9, 0.95$) |
| Learning rate | $3.2 \times 10^{-4}$ |
| Batch size | 4M tokens |
| Tokenizer | tiktoken cl100k_base |

**Scaling experiments** (Section 3.2): 830M, 1.4B, 2.8B, 6.8B, 13.1B models trained for 40K steps (~10B tokens) with sequence length 2048 and batch size 0.25M tokens.

**Long-context extension** (Section 3.3): Continue training 3B checkpoints with 64K context for 1.5B additional tokens. RoPE $\theta$ increased to 640,000. Learning rate 8e-5.

**Baselines:** "Transformer" refers to the augmented Transformer with LLaMA-style improvements (RMSNorm, SwiGLU, no bias), not the vanilla Transformer. Additionally compared with OpenLLaMA-v2-3B, StableLM-base-alpha-3B-v2, and StableLM-3B-4E1T (all trained on 1T tokens).

### Key Results

**Language modeling (Table 1, 3B models, 1T tokens, zero-shot on LM Eval Harness):**

| Model | ARC-C | ARC-E | BoolQ | HellaSwag | OBQA | PIQA | WinoGrande | Avg |
|-------|-------|-------|-------|-----------|------|------|------------|-----|
| OpenLLaMA-v2-3B | 33.9 | 67.6 | 65.7 | 70.0 | 26.0 | 76.7 | 62.9 | 57.5 |
| StableLM-alpha-3B-v2 | 32.4 | 67.3 | 64.6 | 68.6 | 26.4 | 76.0 | 62.1 | 56.8 |
| **DIFF-3B** | **37.8** | **72.9** | **69.0** | **71.4** | **29.0** | **76.8** | **67.1** | **60.6** |

**Scaling properties (Section 3.2, Figure 3):**
- 6.8B DIFF Transformer achieves validation loss comparable to 11B Transformer (**62.2%** of parameters)
- 7.8B DIFF Transformer matches 13.1B Transformer (**59.5%** of parameters)
- DIFF Transformer trained on 160B tokens matches Transformer trained on 251B tokens (**63.7%** of tokens)

**Multi-needle retrieval (Table 2, 4K context, 3B models):**

| Model | N=1, R=1 | N=2, R=2 | N=4, R=2 | N=6, R=2 |
|-------|----------|----------|----------|----------|
| Transformer | **1.00** | 0.85 | 0.62 | 0.55 |
| **DIFF** | **1.00** | **0.92** | **0.84** | **0.85** |

**Multi-needle retrieval (Figure 5, 64K context, N=8, R=1):** DIFF Transformer maintains average accuracy of 0.85 across all context lengths (8K--64K), while Transformer drops to 0.52 at 64K.

**Attention score analysis (Table 3, key information retrieval):**

| Model | Attention to Answer (avg) | Attention Noise (avg) |
|-------|--------------------------|----------------------|
| Transformer | 0.03--0.09 | 0.49--0.54 |
| **DIFF** | **0.27--0.40** | **0.01--0.02** |

**Many-shot ICL (Section 3.5, Figure 6, 64K context):** Average accuracy improvements: +18.0% (TREC-6), +21.6% (TREC-fine-50), +10.4% (Banking-77), +5.2% (Clinic-150).

**ICL robustness (Figure 7, TREC):** Performance variance across 10 random orderings: DIFF range 4.0 (random) / 13.4 (by class) vs Transformer range 19.0 (random) / 56.7 (by class).

**Hallucination evaluation (Table 4, GPT-4o judged accuracy):**

| Task Type | Dataset | Transformer | DIFF |
|-----------|---------|-------------|------|
| Summarization | XSum | 0.44 | **0.53** |
| Summarization | CNN/DM | 0.32 | **0.41** |
| Summarization | MultiNews | 0.42 | **0.61** |
| QA | Qasper | 0.28 | **0.39** |
| QA | HotpotQA | 0.36 | **0.46** |
| QA | 2WikiMQA | 0.29 | **0.36** |

**Activation outliers (Table 5, statistics over 0.4M tokens):**

| Activation Type | Transformer Top-1 | DIFF Top-1 | Transformer Median | DIFF Median |
|-----------------|-------------------|------------|-------------------|-------------|
| Attention logits | 318.0 | 38.8 | 5.4 | 3.3 |
| Hidden states | 3608.6 | 1688.2 | 0.6 | 1.2 |

**Quantization (Figure 8, HellaSwag zero-shot):** DIFF Transformer retains high performance from 16 to 6 bits. At 4 bits, DIFF outperforms 4-bit Transformer by ~25% accuracy, matching 6-bit Transformer.

**Throughput (Table 7, H100 GPUs):**

| Setting | Forward+Backward Overhead | Forward-only Overhead |
|---------|--------------------------|----------------------|
| 3B, 2K | -9% | -9% |
| 3B, 4K | -12% | -10% |
| 13B, 2K | -6% | -5% |

**Math reasoning (Appendix C, Figure 10, o1-style fine-tuning):** DIFF Transformer achieves 50.8% average across 8 math benchmarks vs 43.3% for Transformer (+7.5%). Generates reasoning with average length 6144 tokens vs 6913 for Transformer.

### Ablation Studies (Table 6, 1.4B models, 350B tokens)

| Configuration | #Heads | $d$ | GN | Valid. Set $\downarrow$ | AR-Hit $\downarrow$ | Others $\downarrow$ |
|---------------|--------|-----|-----|-------------|---------|---------|
| Transformer | 16 | 128 | No | 3.087 | 0.898 | 3.272 |
| Transformer (halved heads) | 8 | 256 | No | 3.088 | 0.899 | 3.273 |
| Transformer + GroupNorm | 8 | 256 | Yes | 3.086 | 0.899 | 3.271 |
| **DIFF Transformer** | **8** | **128** | **Yes** | **3.062** | **0.880** | **3.247** |
| DIFF − GroupNorm | 8 | 128 | No | 3.122 | 0.911 | 3.309 |
| DIFF with $\lambda_{\text{init}}=0.8$ | 8 | 128 | Yes | 3.065 | 0.883 | 3.250 |
| DIFF with $\lambda_{\text{init}}=0.5$ | 8 | 128 | Yes | 3.066 | 0.882 | 3.251 |

Key findings:
- **GroupNorm is essential for DIFF Transformer** — removing it degrades loss from 3.062 to 3.122
- Adding GroupNorm to standard Transformer has negligible effect (3.088 → 3.086)
- $\lambda$ initialization strategy is robust: exponential and constant (0.5, 0.8) give similar results
- Halving Transformer heads to match DIFF head count has minimal effect, confirming improvements come from differential attention itself

---

## Limitations and Failure Modes

1. **Limited scale validation.** Experiments reach only 3B parameters for full training and 13.1B for scaling law studies. No validation at production LLM scales (70B+).
2. **Throughput overhead.** 6--12% training throughput reduction and 5--10% inference overhead due to doubled attention computation, though the authors note custom kernels could reduce this gap.
3. **Single training corpus.** All experiments use the StableLM-3B-4E1T training recipe and corpus. Generalization to other data mixtures and domains is not evaluated.
4. **No long-context benchmarks beyond NIAH.** Long-context evaluation focuses on multi-needle retrieval and cumulative NLL; no evaluation on established benchmarks like RULER, LongBench, or InfiniteBench.
5. **Hallucination evaluation relies on GPT-4o judgments.** While previous work (Chuang et al., 2024) shows high agreement with human annotations, this is still an approximate evaluation protocol.
6. **No comparison with other attention variants.** The paper does not compare against sliding window attention, grouped-query attention, linear attention, or sparse attention patterns — only against full softmax attention.
7. **Math reasoning evaluation confounded with fine-tuning recipe.** The o1-style reasoning results (Appendix C) involve distillation from DeepSeek-R1 and synthetic math data, making it unclear how much improvement comes from differential attention vs the fine-tuning procedure.

---

## Conclusions

### Contributions

1. **Differential attention mechanism** that computes attention as the difference between two softmax maps to cancel common-mode noise, directly analogous to differential amplifiers in electrical engineering (Section 2.1, Equation 1).
2. **Improved parameter and data efficiency:** DIFF Transformer achieves comparable language modeling loss with ~60--65% of the parameters or training tokens of standard Transformer (Section 3.2, Figure 3).
3. **Superior information retrieval from long context:** substantially better multi-needle retrieval accuracy, especially as context length and number of distractors increase (Section 3.4, Tables 2--3, Figure 5).
4. **Reduced contextual hallucination** across both summarization and question answering tasks, likely due to reduced attention on irrelevant context (Section 3.6, Table 4).
5. **Improved robustness of in-context learning** — both higher accuracy and lower sensitivity to demonstration order permutations (Section 3.5, Figures 6--7).
6. **Reduced activation outliers** enabling more effective low-bit quantization: 4-bit DIFF Transformer matches 6-bit Transformer performance (Section 3.7, Table 5, Figure 8).
7. **FlashAttention compatibility** — differential attention decomposes into standard attention operations, enabling efficient implementation with existing kernels (Appendix A).

### Implications

1. The success of differential attention suggests that **attention noise is a fundamental bottleneck** in standard Transformers, not merely an artifact of insufficient scale or training.
2. The ~8x reduction in attention logit outliers opens opportunities for **efficient low-bit attention kernels and KV cache compression**.
3. The robustness to ICL order permutations could improve reliability of **few-shot prompted deployments** where demonstration ordering is hard to control.

---

## Key Claims

- **C1:** Differential attention computes scores as the difference of two softmax attention maps, cancelling common-mode attention noise (Section 2.1, Equation 1, Figure 2). **Status: supported.**
- **C2:** DIFF Transformer requires only ~62% of parameters or ~64% of training tokens to match Transformer's language modeling loss (Section 3.2, Figure 3). **Status: supported.** Magnitude: 6.8B matches 11B (62.2%); 160B tokens matches 251B tokens (63.7%).
- **C3:** DIFF Transformer maintains stable multi-needle retrieval accuracy up to 64K context while Transformer degrades — 76% improvement at 25% depth in 64K context; 30pp gap at N=6, R=2 in 4K (Section 3.4, Figure 5, Table 2). **Status: supported.**
- **C4:** DIFF Transformer improves many-shot ICL accuracy by 5.2--21.6% across classification datasets at 64K context (Section 3.5, Figure 6). **Status: supported.**
- **C5:** DIFF Transformer is more robust to order permutations in ICL demonstrations — variance range 4.0 vs 19.0 on TREC with random arrangement (Section 3.5, Figure 7). **Status: supported.**
- **C6:** DIFF Transformer reduces contextual hallucination on summarization (XSum, CNN/DM, MultiNews) and QA (Qasper, HotpotQA, 2WikiMQA) by 7--19 percentage points (Section 3.6, Table 4). **Status: supported.** Evidence relies on GPT-4o as evaluator.
- **C7:** DIFF Transformer produces ~8x fewer activation outliers in attention logits (Top-1: 38.8 vs 318.0) and ~2x fewer in hidden states (Section 3.7, Table 5). **Status: supported.**
- **C8:** 4-bit quantized DIFF Transformer achieves comparable accuracy to 6-bit Transformer and outperforms 4-bit Transformer by ~25% on HellaSwag (Section 3.7, Figure 8). **Status: supported.**

---

## Open Questions

1. **Does differential attention maintain its advantages at production scale (70B+)?** The scaling curves (Figure 3) suggest yes, but no direct validation exists beyond 13.1B. Unresolved.
2. **Can the reduced activation outliers be exploited for efficient KV cache compression?** The paper mentions this as future work but provides no experiments. Unresolved.
3. **What is the interaction between differential attention and alternative positional encodings beyond RoPE (e.g., ALiBi)?** Unresolved.
4. **How does differential attention affect mechanistic interpretability circuits like induction heads?** The sparser attention patterns could make circuits more interpretable, but this is unexplored. Unresolved.
5. **Can pretrained Transformers be converted to differential attention via fine-tuning?** All experiments train from scratch. Whether lightweight adaptation could retrofit existing models is unknown. Unresolved.
6. **Would differential attention benefit from or interact with grouped-query attention (GQA)?** The paper uses multi-head attention; GQA compatibility is not discussed. Unresolved.

---

## Core References and Why They Are Referenced

### Architecture Foundations
- **Vaswani et al. (2017)** — Original Transformer with softmax attention; the baseline architecture that DIFF Transformer modifies by replacing single softmax with differential attention
- **Touvron et al. (2023)** — LLaMA architecture template adopted as the augmented Transformer baseline (RMSNorm, SwiGLU, bias removal)
- **Zhang & Sennrich (2019)** — RMSNorm used as pre-normalization in each layer
- **Shazeer (2020); Ramachandran et al. (2017)** — SwiGLU activation used in the feed-forward module
- **Wu & He (2018)** — GroupNorm applied per-head in the differential attention mechanism

### Conceptual Foundation
- **Laplante et al. (2018)** — Differential amplifiers in electrical engineering; the conceptual analogy for differential attention's noise cancellation
- **Naderi et al. (2024)** — Prove differential attention makes spectral distribution of attention matrices more balanced, resolving rank collapse

### Attention Analysis
- **Kamradt (2023)** — Needle-in-a-haystack test used for key information retrieval evaluation
- **Liu et al. (2024b)** — "Lost in the middle" documenting LLMs' difficulty retrieving information from middle of long contexts

### Efficient Implementation
- **Dao et al. (2022)** — FlashAttention reused for efficient differential attention implementation
- **Dao (2023)** — FlashAttention-2 used as basis for custom differential attention kernels

### Evaluation Baselines
- **Gao et al. (2023)** — LM Eval Harness framework for zero-shot/few-shot evaluation
- **Geng & Liu (2023)** — OpenLLaMA-v2-3B comparison baseline
- **Tow et al. (2023)** — StableLM-3B-4E1T training recipe and comparison baseline
- **Arora et al. (2023)** — Zoology framework for fine-grained loss analysis (AR-Hit vs Others) in ablation studies

### Context, Hallucination, and ICL
- **Chuang et al. (2024)** — Lookback Lens hallucination evaluation protocol using GPT-4o judgments
- **Huang et al. (2024)** — OPERA: connects attention score misallocation to contextual hallucination, directly motivating the hallucination reduction hypothesis
- **Lu et al. (2022)** — Demonstration order sensitivity in ICL; the robustness issue DIFF Transformer addresses
- **Bertsch et al. (2024)** — Many-shot ICL evaluation protocol used for the classification experiments

### Quantization
- **Bondarenko et al. (2024)** — Quantizable Transformers identifying attention heads and activation outliers as quantization bottleneck
- **Sun et al. (2024)** — Massive activations analysis in LLMs; activation outlier phenomenon that DIFF Transformer mitigates
