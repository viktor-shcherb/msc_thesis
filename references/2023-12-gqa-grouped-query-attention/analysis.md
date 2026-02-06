---
title: "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"
authors: "Ainslie, Lee-Thorp, de Jong, Zemlyanskiy, Lebrón, Sanghai"
year: 2023
venue: "EMNLP 2023"
paper_type: conference-paper
categories: ["architecture", "attention-efficiency"]
scope: ["encoder-decoder models", "T5 architecture", "inference optimization"]
benchmarks_used: ["triviaqa", "wmt-translation", "arxiv-summarization"]
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "GQA achieves quality close to multi-head attention while being almost as fast as multi-query attention"
    evidence: "Table 1, Figure 3"
    status: supported
    scope: "T5-XXL encoder-decoder, 5% uptraining"
    magnitude: "GQA-8-XXL: 47.1 avg vs MHA-XXL 47.2 avg; 0.28s vs 1.51s inference"
  - id: C2
    claim: "MHA checkpoints can be uptrained to MQA/GQA using only 5% of original pre-training compute"
    evidence: "Section 2.1, Figure 5"
    status: supported
    scope: "T5 models, mean pooling initialization"
    magnitude: "~600 TPUv3 chip-days for T5-XXL"
  - id: C3
    claim: "Mean pooling of K/V heads is the best initialization method for checkpoint conversion"
    evidence: "Figure 4"
    status: supported
    scope: "T5-Large uptrained to MQA"
    magnitude: "Mean: 55.4 vs First: 55.0 vs Random: 54.5"
  - id: C4
    claim: "GQA is more training-stable than MQA"
    evidence: "Appendix A"
    status: supported
    scope: "T5-Large trained from scratch, long-input fine-tuning"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Introduces GQA as a modification to the standard multi-head attention mechanism"
  - target: 2023-07-llama-2-open-foundation-chat
    type: extended-by
    detail: "Llama 2 70B adopts GQA for efficient inference at scale"
open_questions:
  - question: "How does GQA perform when trained from scratch vs uptrained?"
    addressed_by: null
  - question: "Does GQA provide the same benefits for decoder-only models?"
    addressed_by: 2023-07-llama-2-open-foundation-chat
---

# GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints

**Authors:** Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebrón, Sumit Sanghai (Google Research)
**Date:** December 2023, EMNLP 2023; arXiv:2305.13245

---

## Core Research Problem

Autoregressive decoder inference in Transformers is bottlenecked by memory bandwidth overhead from loading decoder weights and attention keys/values at every decoding step. Multi-query attention (MQA), proposed by Shazeer (2019), reduces this overhead by using a single key-value head shared across all query heads, but comes with quality degradation and training instability.

Moreover, many existing language models (T5, LLaMA) use multi-head attention (MHA) and would require training from scratch to adopt MQA. The fundamental challenge is:

**How can we efficiently convert existing MHA models to use fewer KV heads while preserving quality and maintaining training stability?**

---

## Problem Solutions

The paper proposes two contributions:

1. **Uptraining recipe:** Convert MHA checkpoints to MQA by mean-pooling K/V projection matrices and continuing pre-training for only 5% of original training steps.

2. **Grouped-Query Attention (GQA):** An interpolation between MHA and MQA where query heads are divided into G groups, each sharing a single key-value head. GQA-G with G groups generalizes both MHA (G=H) and MQA (G=1).

---

## Approach Details

### Method

**Checkpoint Conversion:** To convert an MHA checkpoint to MQA or GQA:
1. Mean-pool the key projection matrices across heads: $K_{MQ} = \frac{1}{H}\sum_{i=1}^{H} K_i$
2. Mean-pool the value projection matrices similarly
3. For GQA-G, mean-pool within each of G groups

**Uptraining:** Continue pre-training the converted checkpoint for proportion α of original pre-training steps using the same recipe and dataset.

### Key Technical Components

**GQA Structure:**
- GQA-G divides H query heads into G groups
- Each group shares one key head and one value head
- GQA-1 ≡ MQA (single KV head)
- GQA-H ≡ MHA (H KV heads)

**Memory Bandwidth Analysis:**
- MHA→MQA reduces KV cache size by factor of H
- Larger models have more heads, making MQA more aggressive
- GQA maintains proportional decrease in bandwidth as model scales
- Standard sharding replicates single KV head across partitions; GQA removes this waste

### Experimental Setup

**Models:** T5.1.1 Large and XXL with multi-head attention; uptrained XXL variants with MQA and GQA-8

**Uptraining:**
- α = 0.05 (5% of original pre-training steps)
- ~600 TPUv3 chip-days for T5-XXL
- Initialized from public T5.1.1 checkpoints

**Datasets:**
- Summarization: CNN/Daily Mail, arXiv, PubMed, MediaSum, Multi-News
- Translation: WMT 2014 English-to-German
- QA: TriviaQA

**Fine-tuning:** Learning rate 0.001, batch size 128, dropout 0.1, greedy decoding

**Timing:** Time per sample per TPUv4 chip, 8 TPUs, batch size up to 32

### Key Results

| Model | T_infer (s) | Average | CNN R1 | arXiv R1 | PubMed R1 | MediaSum R1 | MultiNews R1 | WMT BLEU | TriviaQA F1 |
|-------|-------------|---------|--------|----------|-----------|-------------|--------------|----------|-------------|
| MHA-Large | 0.37 | 46.0 | 42.9 | 44.6 | 46.2 | 35.5 | 46.6 | 27.7 | 78.2 |
| MHA-XXL | 1.51 | 47.2 | 43.8 | 45.6 | 47.5 | 36.4 | 46.9 | 28.4 | 81.9 |
| MQA-XXL | 0.24 | 46.6 | 43.0 | 45.0 | 46.9 | 36.1 | 46.5 | 28.5 | 81.3 |
| GQA-8-XXL | 0.28 | 47.1 | 43.5 | 45.4 | 47.7 | 36.3 | 47.2 | 28.4 | 81.6 |

**Key Takeaways:**
- GQA-8-XXL achieves 99.8% of MHA-XXL quality at 18.5% of inference time
- MQA-XXL is faster (0.24s vs 0.28s) but loses 0.5 points average quality
- Uptrained MQA-XXL outperforms MHA-Large in both quality and speed

**Checkpoint Conversion Ablation (T5-Large → MQA, α=0.05):**
- Mean pooling: 55.4
- First head selection: 55.0
- Random initialization: 54.5

**Uptraining Proportion:**
- GQA achieves reasonable performance immediately after conversion
- MQA requires uptraining to be useful
- Both gain from 5% uptraining with diminishing returns at 10%

**Number of GQA Groups:**
- Going from 1 (MQA) to 8 groups adds modest inference overhead
- Increasing cost as groups approach H (MHA)
- 8 groups selected as favorable middle ground

---

## Limitations and Failure Modes

**Explicitly Acknowledged:**
- Evaluation uses ROUGE score for summarization, which is a flawed metric
- No comparison of uptrained GQA vs GQA trained from scratch
- Experiments only on encoder-decoder models (T5); decoder-only models may show different trade-offs

**Training Stability:**
- MQA trained from scratch shows frequent loss spikes during pre-training
- MQA models diverge on long-input fine-tuning tasks
- Uptrained MQA models are more stable but still have high variance
- GQA appears stable (no further investigation of MQA instability root causes)

**Scope and Comparability:**
- GQA not applied to encoder self-attention (parallel computation, not bandwidth-bound)
- All timing on TPUv4; different hardware may show different trade-offs
- Only evaluated on T5 architecture

---

## Conclusions

### Contributions

1. **Uptraining recipe for attention head reduction:** Demonstrated that MHA models can be converted to MQA/GQA using mean-pooling initialization and only 5% additional pre-training, providing a cost-effective path to faster inference.

2. **Grouped-Query Attention:** Introduced GQA as a principled interpolation between MHA and MQA that achieves near-MHA quality with near-MQA speed, particularly beneficial for larger models where the KV cache overhead is proportionally smaller.

3. **Training stability improvement:** Showed that GQA is more stable than MQA during both pre-training and fine-tuning, addressing a practical concern with MQA adoption.

### Implications

1. **Practical deployment:** Organizations with existing MHA models can adopt GQA for inference speedup without full retraining.

2. **Architectural design:** GQA provides a tunable knob (number of groups G) for trading off quality vs speed based on deployment constraints.

3. **Scalability:** The proportional nature of GQA's KV reduction makes it particularly attractive for large models with many attention heads.

---

## Key Claims

1. **GQA achieves near-MHA quality at near-MQA speed:** On T5-XXL, GQA-8 achieves 47.1 average performance (vs MHA 47.2) with 0.28s inference time (vs MHA 1.51s, MQA 0.24s).

2. **5% uptraining is sufficient for checkpoint conversion:** Mean-pooling K/V heads followed by 5% additional pre-training recovers most of the quality, with diminishing returns beyond 10%.

3. **Mean pooling outperforms alternatives:** Information preservation ordering: mean pooling > first head selection > random initialization.

4. **GQA is more training-stable than MQA:** MQA shows loss spikes and fine-tuning divergence; GQA does not exhibit these issues.

---

## Open Questions

1. **Uptraining vs training from scratch:** The paper does not compare uptrained GQA to GQA trained from scratch with the same total compute. What is the quality gap?

2. **Decoder-only models:** The paper evaluates only encoder-decoder models. How does GQA perform in decoder-only architectures where there is no separate cross-attention? (Subsequently addressed by Llama 2's adoption of GQA.)

3. **Optimal group count:** Is 8 the optimal number of groups across different model sizes and architectures, or should G scale with model size?

---

## Core References and Why They Are Referenced

### Foundational Work

**Shazeer (2019)** -- *Fast Transformer Decoding: One Write-Head is All You Need.* Introduced multi-query attention (MQA), which this paper generalizes with GQA.

**Vaswani et al. (2017)** -- *Attention Is All You Need.* Original multi-head attention mechanism that MQA and GQA modify.

### Memory Bandwidth Analysis

**Pope et al. (2022)** -- *Efficiently Scaling Transformer Inference.* Analyzed memory bandwidth bottlenecks in large-scale inference, showing MQA benefits for long sequences.

**Williams et al. (2009)** -- *Roofline: An Insightful Visual Performance Model.* Theoretical framework for understanding compute vs memory bandwidth trade-offs.

### Uptraining Methodology

**Komatsuzaki et al. (2022)** -- *Sparse Upcycling.* Inspired the uptraining approach; demonstrated converting dense checkpoints to Mixture-of-Experts with minimal compute.

### Complementary Efficiency Methods

**Dao et al. (2022)** -- *FlashAttention.* Memory-efficient attention computation; orthogonal to GQA's KV-cache reduction.

**de Jong et al. (2022)** -- *FiDO.* Layer-sparse cross-attention; another approach to reducing attention overhead for long inputs.
