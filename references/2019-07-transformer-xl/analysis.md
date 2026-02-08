---
title: "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context"
authors: "Dai, Yang, Yang, Carbonell, Le, Salakhutdinov"
year: 2019
venue: "ACL 2019"
paper_type: conference-paper
categories: ["architecture", "context-extension", "position-encoding"]
scope: ["language modeling", "character-level modeling", "word-level modeling"]
benchmarks_used: ["enwik8", "text8", "perplexity-wikitext103", "penn-treebank", "perplexity-1b-word"]
models_introduced: ["transformer-xl"]
models_evaluated: ["transformer-base", "awd-lstm"]
key_claims:
  - id: C1
    claim: "Transformer-XL achieves 0.99 bpc on enwik8, the first method to break below 1.0 bpc on widely studied character-level benchmarks"
    evidence: "Table 2, Section 4.1"
    status: supported
    magnitude: "0.99 bpc vs prior SotA 1.06 bpc (64L vanilla Transformer)"
  - id: C2
    claim: "Transformer-XL achieves 18.3 perplexity on WikiText-103, improving over the prior state-of-the-art of 20.5"
    evidence: "Table 1, Section 4.1"
    status: supported
    magnitude: "18.3 vs 20.5 perplexity (10.7% relative improvement)"
  - id: C3
    claim: "Transformer-XL learns dependencies 80% longer than RNNs and 450% longer than vanilla Transformers as measured by relative effective context length"
    evidence: "Table 8, Section 4.3, Figure 3"
    status: supported
    scope: "Measured via relative effective context length (RECL) metric on WikiText-103"
    magnitude: "RECL 900 vs 500 (QRNN) and 128 (vanilla Transformer) at r=0.1"
  - id: C4
    claim: "Transformer-XL is up to 1,874 times faster than vanilla Transformers during evaluation"
    evidence: "Table 9, Section 4.5"
    status: supported
    scope: "When caching hidden states across segments; measured at attention length 3,800"
    magnitude: "1,874x speedup at attn len 3,800"
  - id: C5
    claim: "Segment-level recurrence with relative positional encodings enables modeling dependencies beyond a fixed-length context without disrupting temporal coherence"
    evidence: "Section 3.2, Section 3.3, Table 6 (ablation, Section 4.2)"
    status: supported
    scope: "Both components are necessary; recurrence alone with absolute positions fails"
  - id: C6
    claim: "A 12-layer Transformer-XL matches the performance of a 64-layer vanilla Transformer on enwik8 (1.06 bpc each) using only 17% of the parameters"
    evidence: "Table 2, Section 4.1"
    status: supported
    magnitude: "41M vs 235M parameters (17% parameter budget)"
    scope: "enwik8 character-level language modeling"
  - id: C7
    claim: "Segment-level recurrence improves performance even on short-context tasks by resolving context fragmentation"
    evidence: "Table 7, Section 4.2"
    status: supported
    scope: "One Billion Word benchmark (sentence-shuffled, no long-term dependency)"
    magnitude: "25.2 vs 27.1 PPL (recurrence vs no recurrence)"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Transformer-XL extends the original Transformer with segment-level recurrence and relative positional encodings to enable longer context modeling"
  - target: 2019-02-gpt-2-language-models-unsupervised
    type: concurrent
    detail: "Both address context length limitations; GPT-2 uses larger fixed context (1024 tokens) while Transformer-XL uses segment-level recurrence"
  - target: 2020-04-longformer-long-document-transformer
    type: extended-by
    detail: "Longformer uses sparse attention patterns for long documents, an alternative approach to the recurrence mechanism of Transformer-XL"
  - target: 2022-04-alibi-train-short-test-long
    type: extended-by
    detail: "ALiBi proposes linear attention biases as an alternative to the relative positional encodings introduced by Transformer-XL"
  - target: 2024-01-roformer-rope
    type: extended-by
    detail: "RoPE introduces rotary position embeddings, building on the concept of relative positional encodings from Transformer-XL"
  - target: 2020-04-compressive-transformer-pg19
    type: extended-by
    detail: "Compressive Transformer extends the memory mechanism of Transformer-XL by compressing old memories rather than discarding them"
  - target: 2018-07-sharp-nearby-fuzzy-far-away
    type: extends
    detail: "Transformer-XL builds on Khandelwal et al.'s finding that LSTMs use ~200 context words on average, and proposes the RECL metric extending their ECL metric"
  - target: 2014-10-neural-turing-machines
    type: complementary
    detail: "Transformer-XL's cached memory mechanism has a clear connection to memory-augmented neural networks (Graves et al., 2014)"
open_questions:
  - question: "Can the segment-level recurrence mechanism be combined with efficient attention methods (e.g., sparse attention) to further reduce complexity?"
    addressed_by: null
  - question: "How does the relative positional encoding scheme perform on tasks beyond language modeling (e.g., translation, classification)?"
    addressed_by: null
  - question: "What is the optimal memory length and how does it interact with model depth?"
    addressed_by: null
  - question: "Can the gradient truncation limitation (stop-gradient on cached states) be overcome to enable full BPTT through the recurrence?"
    addressed_by: null
---

# Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context

**Authors:** Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc V. Le, Ruslan Salakhutdinov (Carnegie Mellon University, Google Brain)
**Date:** July 2019, ACL 2019; arXiv:1901.02860

---

## Core Research Problem

Transformers have the potential to learn longer-term dependencies than RNNs thanks to direct attention connections between distant tokens, but in the setting of language modeling they are limited by a **fixed-length context**. During training, the corpus is split into fixed-length segments (e.g., a few hundred characters), and each segment is processed independently with no information flow across segment boundaries (Al-Rfou et al., 2018; Section 3.1). This creates two fundamental problems:

1. **Context fragmentation:** The model cannot capture dependencies longer than the segment length. Fixed-length chunking ignores sentence and semantic boundaries, depriving the model of necessary context for predicting the first symbols of each segment and leading to "inefficient optimization and inferior performance" (Section 1).

2. **Extremely slow evaluation:** The vanilla Transformer uses a sliding window that shifts by one position at a time, recomputing the entire context from scratch for each prediction. This makes evaluation O(n) full forward passes for a sequence of length n (Section 3.1, Figure 1b).

Prior work attempted to address long-range context through cache-based memory augmentation (Grave et al., 2017) or deeper self-attention networks (Al-Rfou et al., 2018, up to 64 layers), but these approaches either add limited context or require massive parameter budgets. Khandelwal et al. (2018) found that LSTM language models use only about 200 context words on average, indicating significant room for improvement (Section 1).

The core challenge is: **how to enable Transformers to model dependencies beyond the fixed segment length while maintaining efficient training and inference.**

---

## Problem Solutions

The paper proposes **Transformer-XL** (eXtra Long), which introduces two complementary innovations:

1. **Segment-level recurrence mechanism:** Hidden states from the previous segment are cached (with stop-gradient) and concatenated with the current segment's hidden states to serve as extended context. This allows information to flow across segment boundaries, growing the maximum dependency length to O(N x L) where N is the number of layers and L the segment length (Section 3.2).

2. **Relative positional encodings:** A new positional encoding scheme that encodes relative distances between tokens rather than absolute positions. This is necessary because absolute positional encodings create temporal confusion when hidden states from different segments (which were computed with the same absolute position indices) are combined (Section 3.3).

The authors emphasize that these two techniques "form a complete set of solutions, as any one of them alone does not address the issue of fixed-length contexts" (Section 1).

---

## Approach Details

### Method

**Segment-Level Recurrence (Section 3.2):**

Let two consecutive segments of length L be s_tau = [x_{tau,1}, ..., x_{tau,L}] and s_{tau+1} = [x_{tau+1,1}, ..., x_{tau+1,L}]. Denote the n-th layer hidden state for segment tau as h^n_tau in R^{L x d}. The recurrence is:

> h-tilde^{n-1}_{tau+1} = [SG(h^{n-1}_tau) circ h^{n-1}_{tau+1}]
>
> q^n_{tau+1}, k^n_{tau+1}, v^n_{tau+1} = h^{n-1}_{tau+1} W^T_q, h-tilde^{n-1}_{tau+1} W^T_k, h-tilde^{n-1}_{tau+1} W^T_v
>
> h^n_{tau+1} = Transformer-Layer(q^n_{tau+1}, k^n_{tau+1}, v^n_{tau+1})

where SG(.) is the stop-gradient operator and [. circ .] denotes concatenation along the sequence dimension (Section 3.2). The key insight: **queries come only from the current segment, while keys and values include cached hidden states from the previous segment**, effectively extending the context without requiring gradient flow through cached states.

The recurrence shifts one layer downwards per segment (unlike same-layer recurrence in RNNs), so the maximum dependency length grows as O(N x L) with N layers (Section 3.2, Figure 2b). This is analogous to truncated BPTT but caches a full sequence of hidden states rather than just the last one.

In practice, a predefined length-M old hidden states are cached as memory m^n_tau in R^{M x d}. During training, M is set equal to segment length L; during evaluation, M can be increased by multiple times (Section 3.2).

**Relative Positional Encodings (Section 3.3):**

With absolute positional encodings, tokens x_{tau,j} and x_{tau+1,j} at the same position j in different segments receive identical position embeddings, making them indistinguishable when cached states are reused (Section 3.3).

The standard absolute attention score decomposes as:

> A^{abs}_{i,j} = E^T_{x_i} W^T_q W_k E_{x_j} + E^T_{x_i} W^T_q W_k U_j + U^T_i W^T_q W_k E_{x_j} + U^T_i W^T_q W_k U_j

The authors reparameterize this into a relative form with three key changes (Section 3.3):

> A^{rel}_{i,j} = E^T_{x_i} W^T_q W_{k,E} E_{x_j} (a) + E^T_{x_i} W^T_q W_{k,R} R_{i-j} (b) + u^T W_{k,E} E_{x_j} (c) + v^T W_{k,R} R_{i-j} (d)

where:
- **Term (a):** content-based addressing (query content to key content)
- **Term (b):** content-dependent positional bias (query content to relative position)
- **Term (c):** global content bias (learned bias u toward key content, independent of query position)
- **Term (d):** global positional bias (learned bias v toward relative position)

Three changes from absolute to relative: (1) absolute position U_j replaced by relative distance encoding R_{i-j} (sinusoidal, no learnable parameters); (2) query position terms U^T_i W^T_q replaced by learnable parameters u and v in R^d; (3) key projection separated into content-based W_{k,E} and location-based W_{k,R} (Section 3.3).

**Complete N-layer Procedure (Section 3.3):**

For a single attention head, for n = 1, ..., N:

> h-tilde^{n-1}_tau = [SG(m^{n-1}_tau) circ h^{n-1}_tau]
>
> q^n_tau, k^n_tau, v^n_tau = h^{n-1}_tau W^{n,T}_q, h-tilde^{n-1}_tau W^{n,T}_{k,E}, h-tilde^{n-1}_tau W^{n,T}_v
>
> A^n_{tau,i,j} = q^{n,T}_{tau,i} k^n_{tau,j} + q^{n,T}_{tau,i} W^n_{k,R} R_{i-j} + u^T k_{tau,j} + v^T W^n_{k,R} R_{i-j}
>
> a^n_tau = Masked-Softmax(A^n_tau) v^n_tau
>
> o^n_tau = LayerNorm(Linear(a^n_tau) + h^{n-1}_tau)
>
> h^n_tau = Positionwise-Feed-Forward(o^n_tau)

with h^0_tau := E_{s_tau} (word embedding sequence). A naive computation of W^n_{k,R} R_{i-j} for all (i,j) pairs is quadratic, but Appendix B shows a linear-cost procedure using matrix multiplication followed by left-shifts (Section 3.3, Appendix B).

**Comparison with Shaw et al. (2018):** Shaw et al. only have terms (a) and (b), dropping the bias terms (c) and (d). They also merge W_k R into a single trainable matrix, abandoning the inductive bias of the sinusoidal encoding. Transformer-XL's formulation retains this inductive bias, which enables generalization to memory lengths several times longer during evaluation than those seen during training (Section 3.3).

### Key Technical Components

- **Stop-gradient on cached states:** Gradients do not flow through cached hidden states h^{n-1}_tau (or memory m^{n-1}_tau). This prevents full BPTT through the recurrence, making training tractable at the cost of potentially limiting very long-range gradient-based learning (Section 3.2).

- **Memory length M:** A predefined length-M cache of old hidden states. With N layers, the maximum effective context length is O(N x M). During training M = L (segment length); during evaluation M is increased substantially (e.g., M = 3,800 for enwik8, M = 1,600 for WikiText-103) (Section 3.2, Section 4.1).

- **Sinusoidal relative distance encoding R:** Uses the sinusoidal formulation from Vaswani et al. (2017) but indexed by relative distance (i-j) rather than absolute position. R is not learned (Section 3.3).

- **Efficient relative attention computation:** Terms (b) and (d) of the attention score are computed in linear cost via a matrix-multiply-then-shift procedure described in Appendix B, avoiding the naive quadratic cost.

- **Adaptive softmax and input representations:** For word-level tasks (WikiText-103, One Billion Word), the model adopts adaptive softmax and adaptive input representations from Baevski and Auli (2018) and Grave et al. (2016) (Section 4.1).

- **Variational dropout and weight averaging:** For Penn Treebank, the model applies regularization techniques from AWD-LSTM (Merity et al., 2017) (Section 4.1).

### Experimental Setup

**Datasets (Section 4.1):**
- **WikiText-103:** ~103M training tokens from 28K articles, average article length 3.6K tokens, vocabulary 267K, word-level
- **enwik8:** 100M bytes of unprocessed Wikipedia text, character-level, vocabulary size 205
- **text8:** 100M characters of lowercased Wikipedia (26 letters + space), character-level
- **One Billion Word:** ~0.8B tokens, sentences shuffled (no long-term dependency), vocabulary ~800K, word-level
- **Penn Treebank:** ~1M tokens, vocabulary 10K, word-level

**Model Configurations (from Section 4.1, Tables 1-5):**

| Dataset | Layers | d_model | d_inner | Heads | Params |
|---|---|---|---|---|---|
| WikiText-103 (Standard) | 16 | 410 | 2100 | 10 | 151M |
| WikiText-103 (Large) | 18 | 1024 | 4096 | 16 | 257M |
| enwik8 (12L) | 12 | 512 | 2048 | 8 | 41M |
| enwik8/text8 (24L) | 24 | 1024 | 4096 | 8 | 277M |
| One Billion Word (Base) | - | - | - | - | 0.46B |
| One Billion Word (Large) | - | - | - | - | 0.8B |
| Penn Treebank | 12 | 500 | 1000 | 10 | 24M |

**Training Details (Section 4.1):**
- Attention length during training: 384 (WikiText-103), 784 (enwik8/text8)
- Attention length during evaluation: 1,600 (WikiText-103), 3,800 (enwik8/text8)
- Memory length during training equals segment length
- Adam optimizer with learning rate warmup and cosine decay

**Reproducibility:** Code available in both TensorFlow and PyTorch at https://github.com/kimiyoung/transformer-xl. Pretrained models and hyperparameters released. Specific hyperparameters for One Billion Word model dimensions not fully specified in the paper.

### Key Results

**Word-Level Language Modeling -- WikiText-103 (Table 1, Section 4.1):**

| Model | #Params | PPL |
|---|---|---|
| Grave et al. (2016) -- LSTM | - | 48.7 |
| Bai et al. (2018) -- TCN | - | 45.2 |
| Dauphin et al. (2016) -- GCNN-14 | - | 37.2 |
| Grave et al. (2016) -- LSTM + Neural cache | - | 40.8 |
| Merity et al. (2018) -- QRNN | 151M | 33.0 |
| Rae et al. (2018) -- Hebbian + Cache | - | 29.9 |
| Transformer-XL Standard | 151M | 24.0 |
| Baevski and Auli (2018) -- Adaptive Input | 247M | 20.5 |
| **Transformer-XL Large** | **257M** | **18.3** |

Transformer-XL reduces the prior SotA perplexity from 20.5 to **18.3** on WikiText-103, a **10.7% relative improvement** (Table 1, Section 4.1).

**Character-Level Language Modeling -- enwik8 (Table 2, Section 4.1):**

| Model | #Params | bpc |
|---|---|---|
| Ha et al. (2016) -- LN HyperNetworks | 27M | 1.34 |
| Chung et al. (2016) -- LN HM-LSTM | 35M | 1.32 |
| Zilly et al. (2016) -- RHN | 46M | 1.27 |
| Mujika et al. (2017) -- FS-LSTM-4 | 47M | 1.25 |
| Krause et al. (2016) -- Large mLSTM | 46M | 1.24 |
| Al-Rfou et al. (2018) -- 12L Transformer | 44M | 1.11 |
| **Transformer-XL 12L** | **41M** | **1.06** |
| Al-Rfou et al. (2018) -- 64L Transformer | 235M | 1.06 |
| Transformer-XL 18L | 88M | 1.03 |
| **Transformer-XL 24L** | **277M** | **0.99** |

- The 12-layer Transformer-XL (41M params) matches the 64-layer vanilla Transformer (235M params), both at 1.06 bpc -- **using only 17% of the parameter budget** (Table 2, Section 4.1).
- The 24-layer Transformer-XL achieves **0.99 bpc**, the **first model to break below 1.0 bpc** on this widely studied benchmark (Table 2, Section 4.1). No auxiliary losses were needed, unlike Al-Rfou et al. (2018).

**Character-Level Language Modeling -- text8 (Table 3, Section 4.1):**

| Model | #Params | bpc |
|---|---|---|
| Cooijmans et al. (2016) -- BN-LSTM | - | 1.36 |
| Chung et al. (2016) -- LN HM-LSTM | 35M | 1.29 |
| Zilly et al. (2016) -- RHN | 45M | 1.27 |
| Krause et al. (2016) -- Large mLSTM | 45M | 1.27 |
| Al-Rfou et al. (2018) -- 12L Transformer | 44M | 1.18 |
| Al-Rfou et al. (2018) -- 64L Transformer | 235M | 1.13 |
| **Transformer-XL 24L** | **277M** | **1.08** |

The best model and hyperparameters from enwik8 were transferred to text8 without further tuning (Table 3, Section 4.1).

**Word-Level Language Modeling -- One Billion Word (Table 4, Section 4.1):**

| Model | #Params | PPL |
|---|---|---|
| Jozefowicz et al. (2016) -- LSTM | 1.8B | 30.6 |
| Jozefowicz et al. (2016) -- LSTM + CNN Input | 1.04B | 30.0 |
| Shazeer et al. (2017) -- High-Budget MoE | ~5B | 28.0 |
| Shazeer et al. (2018) -- Mesh Tensorflow | 4.9B | 24.0 |
| Baevski and Auli (2018) -- Adaptive Input | 0.46B | 24.1 |
| Baevski and Auli (2018) -- Adaptive Input | 1.0B | 23.7 |
| Transformer-XL Base | 0.46B | 23.5 |
| **Transformer-XL Large** | **0.8B** | **21.8** |

One Billion Word has no long-term dependency (sentences are shuffled). Transformer-XL still improves the single-model SotA from 23.7 to **21.8**, demonstrating that the architecture's advantages generalize to short sequences -- attributed to resolving context fragmentation (Table 4, Section 4.1).

**Word-Level Language Modeling -- Penn Treebank (Table 5, Section 4.1):**

| Model | #Params | PPL |
|---|---|---|
| Merity et al. (2017) -- AWD-LSTM | 24M | 58.8 |
| Pham et al. (2018) -- Efficient NAS | 24M | 58.6 |
| Liu et al. (2018) -- Differentiable NAS | 23M | 56.1 |
| Yang et al. (2017) -- AWD-LSTM-MoS | 22M | 55.97 |
| Melis et al. (2018) -- Dropout tuning | 24M | 55.3 |
| **Transformer-XL** | **24M** | **54.52** |
| Yang et al. (2017) -- MoS+Finetune | 22M | 54.44 |

Without two-step finetuning, Transformer-XL achieves **54.52** perplexity, the best among models without finetuning. Only MoS+Finetune (54.44) with two-step finetuning is marginally better. Penn Treebank has only 1M training tokens, showing Transformer-XL generalizes well to small datasets (Table 5, Section 4.1).

### Ablation Study

**Ablation 1: Encoding Schemes on WikiText-103 (Table 6, Section 4.2):**

Using a smaller 128M-parameter model with backpropagation length 128:

| Recurrence | Encoding | Loss | PPL init | PPL best | Attn Len |
|---|---|---|---|---|---|
| Yes | Ours | Full | 27.02 | **26.77** | 500 |
| Yes | Shaw et al. (2018) | Full | 27.94 | 27.94 | 256 |
| No | Ours | Full | 29.59 | 29.02 | 260 |
| No | Al-Rfou et al. (2018) | Half | 31.16 | 31.16 | 120 |

Key findings (Table 6, Section 4.2):
- **Both recurrence and the proposed encoding are necessary** for best performance and for generalizing to longer attention lengths at evaluation time.
- Only the proposed relative encoding enables perplexity improvement when attention length is increased beyond training length (PPL init vs PPL best).
- Absolute encodings (Vaswani et al., 2017; Al-Rfou et al., 2018) only work with half losses and cannot generalize to longer attention lengths.
- With the standard 151M model, the same effect is observed: perplexity improves from 23.43 to 23.09 as attention length increases to 640 (Table 6).

**Ablation 2: Recurrence on One Billion Word (Table 7, Section 4.2):**

A 20-layer Transformer-XL (~0.3B params) trained for 400K steps on sentence-shuffled data:

| Method | PPL |
|---|---|
| **Ours (full)** | **25.2** |
| With Shaw et al. (2018) encodings | 25.7 |
| Without recurrence | 27.1 |

Even when long-term dependency is absent, segment-level recurrence improves performance by **1.9 PPL** (27.1 to 25.2), attributed to resolving context fragmentation (Table 7, Section 4.2).

### Evaluation Speed (Table 9, Section 4.5)

| Attention Length | Slowdown of vanilla Transformer vs Transformer-XL |
|---|---|
| 3,800 | 1,874x |
| 2,800 | 1,409x |
| 1,800 | 773x |
| 800 | 363x |

By reusing cached hidden states instead of recomputing the full context at each position, Transformer-XL achieves up to **1,874x speedup** over the vanilla Transformer's sliding window approach (Table 9, Section 4.5).

### Relative Effective Context Length (Table 8, Section 4.3)

The authors propose **Relative Effective Context Length (RECL)**, a new metric improving on Khandelwal et al.'s (2018) ECL by measuring gain relative to the best short-context model in a group, enabling fair cross-model comparison. RECL uses a parameter r constraining comparison to the top-r hardest positions (Section 4.3, Appendix C).

| Model | RECL (r=0.1) | RECL (r=0.5) | RECL (r=1.0) |
|---|---|---|---|
| **Transformer-XL 151M** | **900** | **800** | **700** |
| QRNN | 500 | 400 | 300 |
| LSTM | 400 | 300 | 200 |
| **Transformer-XL 128M** | **700** | **600** | **500** |
| - with Shaw et al. encoding | 400 | 400 | 300 |
| - without recurrence | 300 | 300 | 300 |
| Vanilla Transformer | 128 | 128 | 128 |

At r = 0.1, Transformer-XL (151M) captures dependencies of **900 words** on average, which is **80% longer than the best RNN** (QRNN at 500) and far exceeds the vanilla Transformer (128). Both recurrence and the proposed encoding contribute to longer RECL (Table 8, Section 4.3, Figure 3).

### Attention Visualization (Appendix D)

Analysis of the 16-layer, 10-head WikiText-103 model with memory length 640 reveals three distinct attention patterns in heads with wide attention spans (Figure 5, Figure 6):
- **Head 8, Layer 1:** nearly uniform attention over the entire memory -- lower layers screen the full memory span.
- **Head 78, Layer 8:** sparse attention scattered across all memory ranges -- mid-level layers focus on specific positions of interest.
- **Head 158, Layer 16:** each target position has its own distinct sparse focus in memory.

Decomposition of attention scores (Figure 7) shows that **term (b) (content-dependent positional bias) dominates** the overall trend of focusing on nearby context, while term (d) (global positional bias) is flatter and biases toward longer context. Term (a) (content-based) is essentially uniform when averaged over all target words (Appendix D).

---

## Limitations and Failure Modes

1. **Gradient truncation at segment boundaries:** The stop-gradient operator prevents backpropagation through cached states. While this makes training tractable, it limits the model's ability to learn dependencies that require gradient flow across multiple segments. The effective gradient context is bounded by the segment length, even though the representational context extends to O(N x M) (Section 3.2). The paper does not explore alternatives to this truncation.

2. **Memory overhead:** Caching hidden states for all N layers requires O(N x M x d) memory per sequence. For the 24-layer enwik8 model with M = 3,800 and d = 1024, this is substantial. The paper acknowledges memory constraints and provides ablations under fixed GPU memory budgets (Appendix A, Table 10).

3. **Training-evaluation mismatch:** During training, memory length equals segment length (e.g., M = L = 784 for enwik8), but evaluation uses much longer memory (M = 3,800). While the sinusoidal relative encoding enables some generalization, this gap could limit full utilization of very long contexts. The ablation study (Table 6) shows evaluation gains are real but diminish at very long attention lengths.

4. **Fixed memory length:** M is a hyperparameter without adaptive tuning. The paper does not explore content-dependent or dynamic memory management.

5. **Language modeling only:** All evaluations are on auto-regressive language modeling. Applicability to bidirectional tasks (classification, QA, translation) is not demonstrated (Section 5 mentions these as future directions).

#### Scope and Comparability

- **What was not tested:** No evaluation on downstream tasks beyond perplexity/bpc. No experiments with models at scale beyond ~277M parameters for character-level or ~0.8B for word-level. No comparison with bidirectional models (BERT-style) or sequence-to-sequence settings.
- **Comparability notes:** On One Billion Word, Transformer-XL uses substantially fewer parameters than some baselines (e.g., 0.8B vs 5B for MoE/Mesh TF), making direct comparisons favorable. On Penn Treebank, the comparison separates models with and without two-step finetuning (Table 5, dagger notation). The RECL metric is novel to this paper and comparisons use it for the first time, so external validation of the metric itself is absent.

---

## Conclusions

### Contributions

1. **Segment-level recurrence mechanism:** A method to cache and reuse hidden states across segment boundaries, enabling context modeling beyond fixed-length segments. The maximum effective context length is O(N x M) compared to O(L) for vanilla Transformers. This also resolves the context fragmentation problem (Section 3.2).

2. **Relative positional encodings for Transformers:** A reformulation of attention scores using four interpretable terms (content-based addressing, content-dependent positional bias, global content bias, global positional bias) that encode relative rather than absolute positions. Retains the sinusoidal inductive bias, enabling generalization to longer sequences at test time (Section 3.3).

3. **State-of-the-art language modeling results:** New SotA on five benchmarks: 0.99 bpc on enwik8 (first below 1.0), 1.08 bpc on text8, 18.3 perplexity on WikiText-103, 21.8 perplexity on One Billion Word, and 54.52 perplexity on Penn Treebank without finetuning (Tables 1-5, Section 4.1).

4. **Massive evaluation speedup:** Up to 1,874x faster evaluation compared to vanilla Transformer sliding window, by reusing cached hidden states (Table 9, Section 4.5).

5. **Relative effective context length metric:** Proposed RECL as a fair cross-model comparison metric for effective context length, improving upon Khandelwal et al.'s ECL (Section 4.3, Appendix C).

6. **Parameter efficiency demonstration:** A 12-layer Transformer-XL (41M params) matches the 64-layer vanilla Transformer (235M params) on enwik8, showing 17% parameter efficiency (Table 2, Section 4.1).

### Implications

1. **Recurrence without RNNs:** The segment-level recurrence demonstrates that recurrence can be beneficial even in Transformer architectures, providing an alternative path to context extension beyond simply increasing the fixed window size. This directly influenced the Compressive Transformer (Rae et al., 2020).

2. **Relative vs absolute position:** The success of relative positional encodings influenced subsequent work including RoPE (Su et al., 2024) and ALiBi (Press et al., 2022), which further developed relative position representations. The four-term decomposition provided a principled framework for understanding positional attention (speculative: the degree of influence on later methods requires tracking citation chains).

3. **Context fragmentation as a distinct problem:** The paper establishes that resolving context fragmentation (via recurrence) improves performance even when long-range dependencies are absent (Table 7, One Billion Word ablation), suggesting this is a general issue for segment-based training.

---

## Key Claims

1. **C1: First model below 1.0 bpc on enwik8.** The 24-layer Transformer-XL achieves 0.99 bpc, breaking through the 1.0 barrier. The prior SotA was 1.06 bpc by a 64-layer vanilla Transformer (Al-Rfou et al., 2018). No auxiliary losses were used. Evidence: Table 2, Section 4.1. Status: **supported**. Evidence rests on a single benchmark, though enwik8 is a widely used standard.

2. **C2: State-of-the-art on WikiText-103 with 18.3 perplexity.** Improves over the prior best of 20.5 (Baevski and Auli, 2018), a 10.7% relative improvement. Evidence: Table 1, Section 4.1. Status: **supported**. Evaluated at a single model size (257M), but the 151M model also sets a new SotA at its parameter budget (24.0 vs 33.0 QRNN).

3. **C3: Dependencies 80% longer than RNNs, 450% longer than vanilla Transformers.** Measured via the RECL metric at r = 0.1 on WikiText-103: Transformer-XL 151M achieves RECL 900, vs QRNN 500 (80% longer) and vanilla Transformer 128. The 450% figure: (700-128)/128 = 447% for the 128M model group. Evidence: Table 8, Section 4.3, Figure 3. Status: **supported**. The RECL metric is novel and has not been independently validated by other groups.

4. **C4: Up to 1,874x faster evaluation.** By caching hidden states instead of recomputing the full context at each position. Measured at attention length 3,800. Evidence: Table 9, Section 4.5. Status: **supported**. Measured on a single model configuration (enwik8).

5. **C5: Both recurrence and relative positional encodings are necessary.** The ablation study (Table 6) shows that removing either component degrades performance and prevents generalization to longer attention lengths. Evidence: Table 6, Section 4.2. Status: **supported**. Ablation covers two datasets (WikiText-103 and One Billion Word) and multiple encoding variants.

6. **C6: 12-layer Transformer-XL matches 64-layer vanilla Transformer with 17% of parameters.** On enwik8, both achieve 1.06 bpc (41M vs 235M params). Evidence: Table 2, Section 4.1. Status: **supported**. Single benchmark comparison.

7. **C7: Recurrence improves even without long-term dependency.** On the sentence-shuffled One Billion Word dataset, adding recurrence reduces perplexity from 27.1 to 25.2, attributed to resolving context fragmentation. Evidence: Table 7, Section 4.2. Status: **supported**. Single dataset, single model size (~0.3B params).

---

## Open Questions

1. **Can segment-level recurrence be combined with efficient attention methods (e.g., sparse attention) to further reduce complexity?** The paper does not explore this combination. Status: **unresolved**.

2. **How does the relative positional encoding scheme perform on tasks beyond language modeling (e.g., translation, classification)?** The paper focuses exclusively on auto-regressive language modeling. Status: **unresolved**.

3. **What is the optimal memory length and how does it interact with model depth?** The paper uses fixed memory lengths (M = L during training, increased during evaluation) without systematic exploration of this trade-off. Status: **unresolved**.

4. **Can the gradient truncation limitation be overcome?** The stop-gradient operator is necessary for tractable training but limits gradient-based learning across segment boundaries. No alternatives are explored. Status: **unresolved**.

---

## Core References and Why They Are Referenced

### Transformer Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture. Provides the base self-attention mechanism, sinusoidal positional encodings (adapted for relative positions), and the attention score decomposition that Transformer-XL reparameterizes.

### Direct Predecessors and Baselines

- **Al-Rfou et al. (2018)** -- *Character-Level Language Modeling with Deeper Self-Attention.* Achieves 1.06 bpc on enwik8 using 64-layer vanilla Transformers with auxiliary losses. Serves as the primary character-level baseline and exemplifies the fixed-length context limitation that Transformer-XL addresses. Also provides the vanilla Transformer evaluation speed baseline.

- **Baevski and Auli (2018)** -- *Adaptive Input Representations for Neural Language Modeling.* Achieves 20.5 perplexity on WikiText-103 and 23.7 on One Billion Word -- the prior word-level SotA that Transformer-XL surpasses. Also provides the adaptive softmax and input representation techniques adopted by Transformer-XL.

### Positional Encoding

- **Shaw et al. (2018)** -- *Self-Attention with Relative Position Representations.* Proposes relative position representations for self-attention in machine translation. Transformer-XL builds on this concept but introduces a more complete formulation with all four attention terms and retains sinusoidal inductive bias. Compared directly in ablation studies (Tables 6, 7, 8).

### Context Length Analysis

- **Khandelwal et al. (2018)** -- *Sharp Nearby, Fuzzy Far Away.* Finds LSTMs use about 200 context words on average and proposes the Effective Context Length (ECL) metric. Transformer-XL's RECL metric is a direct improvement, measuring relative gain to enable fair cross-model comparison.

### Language Modeling Baselines

- **Merity et al. (2017)** -- *Regularizing and Optimizing LSTM Language Models (AWD-LSTM).* The primary RNN baseline for word-level language modeling. Transformer-XL adopts its variational dropout and weight averaging for Penn Treebank experiments.

- **Merity et al. (2018)** -- *An Analysis of Neural Language Modeling at Multiple Scales (QRNN).* Provides the QRNN baseline on WikiText-103 (33.0 PPL) and the 151M parameter budget reference.

### Memory-Augmented Networks

- **Graves et al. (2014)** -- *Neural Turing Machines.* Transformer-XL's cached memory mechanism has a "clear connection" to memory-augmented neural networks, establishing the conceptual lineage for the state-reuse approach.
