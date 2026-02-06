---
title: "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context"
authors: "Dai, Yang, Yang, Carbonell, Le, Salakhutdinov"
year: 2019
venue: "ACL 2019"
paper_type: conference-paper
categories: ["architecture", "context-extension", "position-encoding"]
scope: ["language modeling", "character-level modeling", "word-level modeling"]
benchmarks_used: ["enwik8", "text8", "perplexity-wikitext103", "penn-treebank"]
models_introduced: ["transformer-xl"]
models_evaluated: ["transformer-base", "awd-lstm"]
key_claims:
  - id: C1
    claim: "Transformer-XL achieves 0.99 bpc on enwik8, the first method to break below 1.0 bpc on widely studied character-level benchmarks"
    evidence: "Table 1, Section 4.1"
    status: supported
    magnitude: "0.99 bpc vs prior SotA 1.06 bpc"
  - id: C2
    claim: "Transformer-XL achieves 18.3 perplexity on WikiText-103, improving over the prior state-of-the-art of 20.5"
    evidence: "Table 2, Section 4.2"
    status: supported
    magnitude: "18.3 vs 20.5 perplexity"
  - id: C3
    claim: "Transformer-XL learns dependencies 80% longer than RNNs and 450% longer than vanilla Transformers"
    evidence: "Section 4.5, Figure 3"
    status: supported
    scope: "Measured via relative effective context length metric"
  - id: C4
    claim: "Transformer-XL is up to 1,800+ times faster than vanilla Transformers during evaluation"
    evidence: "Section 4.4"
    status: supported
    scope: "When caching hidden states across segments"
  - id: C5
    claim: "Segment-level recurrence with relative positional encodings enables modeling dependencies beyond a fixed-length context without disrupting temporal coherence"
    evidence: "Section 3.2, Section 3.3"
    status: supported
  - id: C6
    claim: "A 12-layer Transformer-XL matches the performance of a 64-layer vanilla Transformer on WikiText-103, using only 17% of the parameters"
    evidence: "Section 4.3, ablation study"
    status: supported
    magnitude: "17% parameter efficiency"
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
open_questions:
  - question: "Can the segment-level recurrence mechanism be combined with efficient attention methods to further reduce complexity?"
    addressed_by: null
  - question: "How does the relative positional encoding scheme perform on tasks beyond language modeling?"
    addressed_by: null
  - question: "What is the optimal memory length and how does it interact with model depth?"
    addressed_by: null
---
# Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context

**Authors:** Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc V. Le, Ruslan Salakhutdinov (Carnegie Mellon University, Google Brain)
**Date:** July 2019, ACL 2019; arXiv:1901.02860

---

## Core Research Problem

Transformers have a potential of learning longer-term dependency, but are limited by a fixed-length context in the setting of language modeling. During training, the model processes fixed-length segments (e.g., 512 tokens), and information cannot flow across segment boundaries. This leads to two fundamental problems:

1. **Context fragmentation:** The model cannot capture dependencies longer than the segment length. When a long article is split into segments, the model treats each segment independently, losing crucial long-range context.

2. **Inefficient evaluation:** During evaluation, the vanilla Transformer uses a sliding window approach, shifting by only one position at a time and recomputing the entire context. This results in O(n) forward passes for a sequence of length n, making evaluation extremely slow.

The core challenge is: **how to enable Transformers to model dependencies beyond the fixed segment length while maintaining efficient training and inference.**

---

## Problem Solutions

The paper proposes **Transformer-XL** (eXtra Long), which introduces two key innovations:

1. **Segment-level recurrence mechanism:** Hidden states from the previous segment are cached and reused as extended context when processing the current segment. This allows information to flow across segment boundaries, enabling the model to capture longer dependencies.

2. **Relative positional encodings:** A new positional encoding scheme that encodes the relative distance between tokens rather than their absolute positions. This is necessary because absolute positional encodings would create temporal confusion when hidden states from different segments are combined.

Together, these innovations enable the model to learn dependencies far beyond the segment length while achieving substantial speedups during evaluation.

---

## Approach Details

### Method

**Segment-Level Recurrence (Section 3.2):**

Let the two consecutive segments of length L be s_τ = [x_{τ,1}, ..., x_{τ,L}] and s_{τ+1} = [x_{τ+1,1}, ..., x_{τ+1,L}]. The n-th layer hidden state for segment τ is h^n_τ ∈ R^{L×d}. The recurrence is formulated as:

> h̃^{n-1}_{τ+1} = [SG(h^{n-1}_τ) ∘ h^{n-1}_{τ+1}]
>
> q^n_{τ+1}, k^n_{τ+1}, v^n_{τ+1} = h^{n-1}_{τ+1} W^T_q, h̃^{n-1}_{τ+1} W^T_k, h̃^{n-1}_{τ+1} W^T_v
>
> h^n_{τ+1} = Transformer-Layer(q^n_{τ+1}, k^n_{τ+1}, v^n_{τ+1})

where SG(·) is the stop-gradient operator that prevents gradient flow through cached states, and [· ∘ ·] denotes concatenation along the sequence dimension. The key insight is that queries come only from the current segment, while keys and values include the cached hidden states from the previous segment, effectively extending the context.

**Relative Positional Encodings (Section 3.3):**

Standard absolute positional encodings add position embeddings to the input: x_i + p_i. In the attention mechanism, this leads to attention scores that depend on absolute positions. However, when cached hidden states from segment τ are used in segment τ+1, the absolute positions become temporally incoherent.

The paper reformulates attention to use relative positions. Starting from the standard attention score:

> A_{i,j}^{abs} = q_i^T k_j = (W_q(x_i + p_i))^T (W_k(x_j + p_j))

Expanding and reparameterizing, the relative attention score becomes:

> A_{i,j}^{rel} = E_{x_i}^T W_q^T W_{k,E} E_{x_j} + E_{x_i}^T W_q^T W_{k,R} R_{i-j} + u^T W_{k,E} E_{x_j} + v^T W_{k,R} R_{i-j}

where:
- Term (a): Content-based addressing (query content attends to key content)
- Term (b): Content-dependent positional bias (query content attends to relative position)
- Term (c): Global content bias (learned query bias for content)
- Term (d): Global positional bias (learned query bias for relative position)

R_{i-j} is a sinusoidal encoding of the relative distance (i-j), and u, v ∈ R^d are learnable parameters replacing the query position embedding.

### Key Technical Components

- **Stop-gradient on cached states:** Gradients do not flow through the cached hidden states h^{n-1}_τ. This prevents the recurrence from becoming a full BPTT (backpropagation through time), making training tractable.

- **Memory length M:** During evaluation, the model caches M hidden states from previous segments. With N layers, the maximum effective context length is O(N × M), allowing dependencies far beyond the segment length L.

- **Sinusoidal relative distance encoding:** The relative position matrix R uses sinusoidal encodings from Vaswani et al. (2017), but indexed by relative distance (i-j) rather than absolute position.

### Experimental Setup

**Datasets:**
- **WikiText-103:** ~103M training tokens, vocabulary 267K, word-level language modeling
- **enwik8:** 100M bytes of Wikipedia XML, character-level, vocabulary 205
- **text8:** 100M characters from Wikipedia, 27-character vocabulary (lowercase letters + space)
- **One Billion Word:** ~0.8B tokens, sentence-level shuffled, vocabulary 800K
- **Penn Treebank:** ~1M tokens, vocabulary 10K, word-level

**Model Configurations:**

| Dataset | Layers | d_model | d_inner | Heads | Params |
|---------|--------|---------|---------|-------|--------|
| WikiText-103 | 16 | 410 | 2100 | 10 | 151M |
| WikiText-103 (Large) | 18 | 1024 | 4096 | 16 | 257M |
| enwik8 | 12 | 512 | 2048 | 8 | 41M |
| enwik8 (24L) | 24 | 1024 | 4096 | 8 | 277M |
| text8 | 24 | 1024 | 4096 | 8 | 277M |
| Penn Treebank | 12 | 500 | 1000 | 10 | 24M |

**Training Details:**
- Segment length L = 150 (WikiText-103), 512 (enwik8/text8)
- Memory length during training typically equals segment length
- Evaluation uses extended memory (e.g., M = 640 for WikiText-103, M = 3800 for enwik8)
- Adam optimizer with learning rate warmup and cosine decay

### Key Results

**Character-Level Language Modeling (Table 1):**

| Model | enwik8 (bpc) | text8 (bpc) |
|-------|-------------|-------------|
| LSTM baseline | 1.36 | 1.43 |
| 64L Transformer | 1.06 | 1.13 |
| 12L Transformer-XL | 1.06 | 1.15 |
| 18L Transformer-XL | 1.03 | 1.11 |
| **24L Transformer-XL** | **0.99** | **1.08** |

The 24-layer Transformer-XL achieves **0.99 bpc on enwik8**, the first model to break below 1.0 bpc on this widely studied benchmark.

**Word-Level Language Modeling (Table 2):**

| Model | WikiText-103 (ppl) | One Billion Word (ppl) |
|-------|--------------------|------------------------|
| AWD-LSTM | 33.0 | - |
| QRNN | 33.0 | - |
| Adaptive Input (Baevski & Auli) | 20.5 | 23.7 |
| **Transformer-XL (base)** | **24.0** | - |
| **Transformer-XL (large)** | **18.3** | **21.8** |

On WikiText-103, Transformer-XL achieves **18.3 perplexity**, improving over the prior state-of-the-art of 20.5 (a 10.7% relative improvement).

**Penn Treebank (Table 3):**

| Model | Test Perplexity |
|-------|-----------------|
| AWD-LSTM | 57.3 |
| AWD-LSTM + continuous cache | 52.8 |
| Transformer-XL | 54.52 |

Without finetuning tricks, Transformer-XL achieves 54.52 perplexity, competitive with heavily-tuned LSTM models.

**Evaluation Speed (Section 4.4):**

During evaluation with cached hidden states, Transformer-XL achieves up to **1,874× speedup** compared to the vanilla Transformer's sliding window approach. The vanilla Transformer requires a full context recomputation for each position, while Transformer-XL reuses cached states.

**Effective Context Length (Section 4.5):**

Using the relative effective context length (RECL) metric—the length at which the gain drops to 10% of the maximum—Transformer-XL models dependency that is:
- **80% longer than RNNs** (RECL ~900 vs ~500)
- **450% longer than vanilla Transformers** (RECL ~900 vs ~165)

---

## Limitations and Failure Modes

1. **Gradient truncation at segment boundaries:** The stop-gradient operator prevents backpropagation through cached states. While this makes training tractable, it may limit the model's ability to learn very long-range dependencies that require gradient flow across multiple segments.

2. **Memory overhead:** Caching hidden states for all layers requires O(N × M × d) memory per sequence, where N is the number of layers, M is the memory length, and d is the model dimension. This can be substantial for deep models with long memories.

3. **Training-evaluation mismatch:** During training, memory length is typically set equal to segment length (M = L), but evaluation uses much longer memory (e.g., M = 3800 for enwik8). This mismatch may limit the model's ability to fully utilize very long contexts.

4. **Fixed memory length:** The memory length M is a hyperparameter that must be tuned. There is no adaptive mechanism to determine optimal memory length based on the content.

5. **Language modeling only:** The paper evaluates exclusively on language modeling tasks. Applicability to other tasks (classification, translation, question answering) is not demonstrated.

---

## Conclusions

### Contributions

1. **Segment-level recurrence mechanism:** A method to cache and reuse hidden states across segment boundaries, enabling context modeling beyond fixed-length segments. The maximum effective context length is O(N × M) compared to O(L) for vanilla Transformers.

2. **Relative positional encodings:** A reformulation of attention that encodes relative distances rather than absolute positions, enabling coherent integration of cached hidden states across segments.

3. **State-of-the-art language modeling:** New state-of-the-art results on multiple benchmarks: 0.99 bpc on enwik8 (first below 1.0), 1.08 bpc on text8, 18.3 perplexity on WikiText-103, 21.8 perplexity on One Billion Word.

4. **Massive evaluation speedup:** Up to 1,874× faster evaluation compared to the vanilla Transformer's sliding window approach.

5. **Longer effective context:** The model learns dependencies 80% longer than RNNs and 450% longer than vanilla Transformers, as measured by the relative effective context length metric.

### Implications

1. **Recurrence without RNNs:** The segment-level recurrence mechanism demonstrates that recurrence can be beneficial even in Transformer architectures, providing an alternative to purely attention-based context extension methods.

2. **Relative vs absolute position:** The success of relative positional encodings influenced subsequent work, including RoPE and ALiBi, which further developed relative position representations.

3. **Memory and context trade-offs:** The paper establishes a framework for thinking about memory-augmented Transformers, directly influencing the Compressive Transformer and other memory-based approaches.

---

## Key Claims

1. **C1: First model below 1.0 bpc on enwik8.** Transformer-XL achieves 0.99 bpc, breaking the 1.0 barrier that had stood for years. Evidence: Table 1, Section 4.1. Status: **supported**.

2. **C2: State-of-the-art on WikiText-103 with 18.3 perplexity.** Improves over the prior best of 20.5 (Baevski & Auli). Evidence: Table 2, Section 4.2. Status: **supported**.

3. **C3: Dependencies 80% longer than RNNs, 450% longer than vanilla Transformers.** Measured via the relative effective context length metric on WikiText-103. Evidence: Section 4.5, Figure 3. Status: **supported**.

4. **C4: Up to 1,800+ times faster evaluation.** By caching hidden states instead of recomputing the full context at each position. Evidence: Section 4.4. Status: **supported**.

5. **C5: Segment-level recurrence with relative positional encodings enables beyond-fixed-length modeling.** The combination of the two innovations is necessary; recurrence alone with absolute positions fails due to temporal confusion. Evidence: Section 3.2, 3.3, ablation in Section 4.3. Status: **supported**.

6. **C6: 12-layer Transformer-XL matches 64-layer vanilla Transformer with 17% parameters.** On WikiText-103, demonstrating the efficiency of the recurrence mechanism. Evidence: Section 4.3. Status: **supported**.

---

## Open Questions

1. **Can segment-level recurrence be combined with efficient attention methods (e.g., sparse attention) to further reduce complexity?** The paper does not explore this combination. Status: **unresolved**.

2. **How does the relative positional encoding scheme perform on tasks beyond language modeling (e.g., translation, classification)?** The paper focuses exclusively on language modeling. Status: **unresolved**.

3. **What is the optimal memory length and how does it interact with model depth?** The paper uses fixed memory lengths without systematic exploration of this trade-off. Status: **unresolved**.

4. **Can the gradient truncation limitation be overcome?** The stop-gradient operator is necessary for tractable training but may limit very long-range learning. Status: **unresolved**.

---

## Core References and Why They Are Referenced

### Direct Predecessors

- **Vaswani et al. (2017)** — *Attention Is All You Need.* The original Transformer architecture that Transformer-XL extends. Provides the base self-attention mechanism and sinusoidal positional encodings that are modified for relative positions.

- **Al-Rfou et al. (2019)** — *Character-Level Language Modeling with Deeper Self-Attention.* Achieves 1.06 bpc on enwik8 using very deep (64-layer) vanilla Transformers. Serves as the primary baseline that Transformer-XL surpasses.

- **Baevski & Auli (2019)** — *Adaptive Input Representations for Neural Language Modeling.* Achieves 20.5 perplexity on WikiText-103, the prior state-of-the-art that Transformer-XL improves upon.

### Positional Encoding

- **Shaw et al. (2018)** — *Self-Attention with Relative Position Representations.* Proposes relative position representations for self-attention. Transformer-XL builds on this concept but introduces a more efficient formulation.

### Language Modeling Baselines

- **Merity et al. (2018)** — *Regularizing and Optimizing LSTM Language Models (AWD-LSTM).* The primary RNN baseline for word-level language modeling comparisons.

- **Grave et al. (2017)** — *Improving Neural Language Models with a Continuous Cache.* Introduces cache-based memory augmentation for language models, a conceptually related approach to extending context.
