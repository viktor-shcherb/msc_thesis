---
title: "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints"
authors: "Ainslie, Lee-Thorp, de Jong, Zemlyanskiy, Lebrón, Sanghai"
year: 2023
venue: "EMNLP 2023"
paper_type: conference-paper
categories: ["architecture", "attention-efficiency"]
scope: ["encoder-decoder models", "T5 architecture", "inference optimization", "KV-cache reduction"]
benchmarks_used: ["cnn-dm", "arxiv-summarization", "multinews", "wmt-translation", "triviaqa"]
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "GQA achieves quality close to multi-head attention while being almost as fast as multi-query attention"
    evidence: "Table 1, Figure 3"
    status: supported
    scope: "T5-XXL encoder-decoder, 5% uptraining, greedy decoding, TPUv4"
    magnitude: "GQA-8-XXL: 47.1 avg vs MHA-XXL 47.2 avg; 0.28s vs MHA 1.51s inference"
  - id: C2
    claim: "MHA checkpoints can be uptrained to MQA/GQA using only 5% of original pre-training compute"
    evidence: "Section 2.1, Figure 5"
    status: supported
    scope: "T5 models, mean pooling initialization, same pre-training recipe"
    magnitude: "~600 TPUv3 chip-days for T5-XXL; diminishing returns beyond 10%"
  - id: C3
    claim: "Mean pooling of K/V heads is the best initialization method for checkpoint conversion"
    evidence: "Figure 4"
    status: supported
    scope: "T5-Large uptrained to MQA, alpha=0.05, subset of 3 tasks"
    magnitude: "Mean: ~55.6 vs First: ~55.1 vs Random: ~54.6 (approximate from bar chart)"
  - id: C4
    claim: "GQA is more training-stable than MQA"
    evidence: "Appendix A"
    status: supported
    scope: "T5-Large trained from scratch and uptrained, long-input fine-tuning tasks"
    magnitude: "MQA shows frequent loss spikes and divergence on long-input fine-tuning; GQA does not"
  - id: C5
    claim: "GQA presents a particularly good trade-off for larger models due to proportional KV reduction"
    evidence: "Section 2.2, Figure 6"
    status: supported
    scope: "T5-XXL, GQA groups from 1 to 64"
    magnitude: "Going from 1 (MQA) to 8 groups adds modest inference overhead; sharper increase beyond 8"
  - id: C6
    claim: "Uptrained MQA provides a favorable tradeoff relative to smaller MHA models"
    evidence: "Table 1, Figure 3"
    status: supported
    scope: "T5-XXL uptrained to MQA vs T5-Large MHA, greedy decoding"
    magnitude: "MQA-XXL: 46.6 avg at 0.24s vs MHA-Large: 46.0 avg at 0.37s"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Introduces GQA as a modification to the standard multi-head attention mechanism from the original Transformer"
  - target: 2023-07-llama-2-open-foundation-chat
    type: extended-by
    detail: "Llama 2 70B adopts GQA for efficient inference at scale, validating GQA in decoder-only models"
  - target: 2022-12-flashattention
    type: complementary
    detail: "FlashAttention addresses memory-efficient attention computation; orthogonal to GQA's KV-cache reduction"
  - target: 2023-02-llama-open-efficient-foundation
    type: evaluates
    detail: "LLaMA is cited as a prominent model using MHA that could benefit from GQA uptraining"
open_questions:
  - question: "How does uptrained GQA compare to GQA trained from scratch with the same total compute?"
    addressed_by: null
  - question: "Does GQA provide the same benefits for decoder-only models as for encoder-decoder models?"
    addressed_by: 2023-07-llama-2-open-foundation-chat
  - question: "Is 8 the optimal number of GQA groups across different model sizes and architectures, or should G scale with model size?"
    addressed_by: null
---

# GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints

**Authors:** Joshua Ainslie*, James Lee-Thorp*, Michiel de Jong*+ (Google Research; +University of Southern California)
**Date:** December 2023, EMNLP 2023; arXiv:2305.13245

---

## Core Research Problem

Autoregressive decoder inference in Transformers is bottlenecked by **memory bandwidth overhead** from loading decoder weights and all attention keys and values at every decoding step (Shazeer, 2019; Pope et al., 2022; de Jong et al., 2022). Multi-query attention (MQA), proposed by Shazeer (2019), reduces this overhead by using a single key-value head shared across all query heads, but introduces two practical problems: (1) **quality degradation** compared to standard multi-head attention, and (2) **training instability**, including loss spikes during pre-training and divergence during fine-tuning (Appendix A).

Moreover, many existing language models -- including T5 (Raffel et al., 2020) and LLaMA (Touvron et al., 2023) -- use multi-head attention (MHA) and would require complete retraining to adopt MQA. Some models like PaLM (Chowdhery et al., 2022) already use MQA, but the quality-speed tradeoff remains suboptimal.

**How can we efficiently convert existing MHA models to use fewer KV heads while preserving quality, maintaining training stability, and achieving near-MQA inference speed?**

---

## Problem Solutions

The paper proposes two complementary contributions:

1. **Uptraining recipe:** A method to convert existing MHA checkpoints to MQA or GQA by mean-pooling K/V projection matrices and continuing pre-training for only 5% of original training steps (alpha = 0.05), providing a cost-effective path to faster inference without training from scratch.

2. **Grouped-Query Attention (GQA):** An interpolation between MHA and MQA where H query heads are divided into G groups, each sharing a single key-value head. GQA-G generalizes both MHA (G = H) and MQA (G = 1), allowing a tunable quality-speed tradeoff that scales better with model size than MQA.

---

## Approach Details

### Method

**Checkpoint Conversion (Section 2.1):** Converting an MHA checkpoint to MQA or GQA proceeds in two steps:

1. **Mean-pool projection matrices:** The key and value projection matrices from all H heads are mean-pooled into the target number of heads. For MQA (single KV head):

> K_MQ = (1/H) * sum_{i=1}^{H} K_i

where each K_i is a d_model x d_h projection matrix. For GQA-G, the H heads are divided into G groups and mean-pooled within each group.

2. **Additional pre-training (uptraining):** The converted checkpoint is pre-trained for a proportion alpha of its original training steps using the same pre-training recipe and dataset.

**Grouped-Query Attention (Section 2.2):** GQA divides the H query heads into G groups, each sharing one key head and one value head:

- **GQA-1** (single group) is equivalent to **MQA**
- **GQA-H** (H groups) is equivalent to **MHA**

An intermediate G yields an interpolated model that is higher quality than MQA but faster than MHA.

### Key Technical Components

**Memory Bandwidth Analysis (Section 2.2):**
- MHA to MQA reduces KV cache size by a factor of H, but larger models have more heads, making MQA a more aggressive cut in both memory bandwidth and capacity
- GQA maintains the **same proportional decrease** in bandwidth and capacity as model size increases
- KV-cache scales with model dimension d, while model FLOPs and parameters scale with d^2; therefore larger models suffer relatively less from KV attention overhead
- Standard sharding for large models **replicates the single KV head** across model partitions (Pope et al., 2022); GQA with G >= number of partitions removes this waste

**Encoder Exclusion:** GQA is not applied to encoder self-attention layers because encoder representations are computed in parallel, making memory bandwidth not the primary bottleneck (Section 2.2).

### Experimental Setup

**Models (Section 3.1):** T5.1.1 architecture (Raffel et al., 2020) implemented in JAX/Flax/Flaxformer:
- T5-Large and T5-XXL with multi-head attention
- Uptrained T5-XXL variants with MQA and GQA-8

**Uptraining (Section 3.1):**
- alpha = 0.05 (5% of original pre-training steps)
- ~600 TPUv3 chip-days for T5-XXL
- Initialized from public T5.1.1 checkpoints
- Same pre-training setup and dataset as Raffel et al. (2020)
- Adafactor optimizer with same hyperparameters and learning rate schedule as T5

**Datasets (Section 3.1):**
- Summarization: CNN/Daily Mail (Nallapati et al., 2016), arXiv, PubMed (Cohan et al., 2018), MediaSum (Zhu et al., 2021), Multi-News (Fabbri et al., 2019)
- Translation: WMT 2014 English-to-German
- Question answering: TriviaQA (Joshi et al., 2017)
- Classification benchmarks (e.g., GLUE) explicitly excluded as autoregressive inference is less applicable

**Fine-tuning (Section 3.1):**
- Constant learning rate 0.001, batch size 128, dropout 0.1 for all tasks
- CNN/Daily Mail and WMT: input length 512, output length 256
- Other summarization datasets: input length 2048, output length 512
- TriviaQA: input length 2048, output length 32
- Train until convergence, select checkpoint with highest dev performance
- **Greedy decoding** for inference

**Timing (Section 3.1):** Time per sample reported per TPUv4 chip, measured with xprof (Google, 2020). 8 TPUs used with largest batch size fitting up to 32 per TPU, parallelization optimized separately for each model.

**Reproducibility:** Code available at https://github.com/google/flaxformer. Initialized from public T5.1.1 checkpoints. No variance estimates reported for main results; for unstable MQA fine-tuning tasks, average over three runs is reported (Appendix A).

### Key Results

**Table 1 (Section 3.2):** Inference time and average dev set performance across all tasks.

| Model | T_infer (s) | Average | CNN (R1) | arXiv (R1) | PubMed (R1) | MediaSum (R1) | MultiNews (R1) | WMT (BLEU) | TriviaQA (F1) |
|---|---|---|---|---|---|---|---|---|---|
| MHA-Large | 0.37 | 46.0 | 42.9 | 44.6 | 46.2 | 35.5 | 46.6 | 27.7 | 78.2 |
| MHA-XXL | 1.51 | 47.2 | 43.8 | 45.6 | 47.5 | 36.4 | 46.9 | 28.4 | 81.9 |
| MQA-XXL | 0.24 | 46.6 | 43.0 | 45.0 | 46.9 | 36.1 | 46.5 | 28.5 | 81.3 |
| GQA-8-XXL | 0.28 | 47.1 | 43.5 | 45.4 | 47.7 | 36.3 | 47.2 | 28.4 | 81.6 |

**Key takeaways:**
- **GQA-8-XXL achieves 99.8% of MHA-XXL quality** (47.1 vs 47.2 average) at 18.5% of the inference time (0.28s vs 1.51s) (Table 1; tested across 7 tasks on a single architecture, no variance reported -- moderate evidence)
- **MQA-XXL is faster** (0.24s) but loses 0.6 points in average quality relative to MHA-XXL (46.6 vs 47.2) (Table 1)
- **Uptrained MQA-XXL outperforms MHA-Large** in both quality (46.6 vs 46.0) and speed (0.24s vs 0.37s), showing uptraining yields a favorable quality-speed tradeoff (Table 1, Figure 3)

### Ablations

**Checkpoint Conversion Methods (Figure 4, Section 3.3):** Comparison on T5-Large uptrained to MQA with alpha = 0.05, evaluated on CNN/DM, MultiNews, and TriviaQA:
- Mean pooling: ~55.6
- First head selection: ~55.1
- Random initialization: ~54.6

Results are ordered by degree of information preservation from the pre-trained model (moderate evidence -- single model size, 3 tasks).

**Uptraining Proportion (Figure 5, Section 3.3):** Performance as a function of alpha for T5-XXL:
- GQA already achieves reasonable performance after conversion (alpha = 0) while MQA requires uptraining to be useful
- Both MQA and GQA gain from 5% uptraining, with diminishing returns at 10%
- MHA baseline shown as dotted horizontal line at ~57 average on the 3-task subset

**Number of GQA Groups (Figure 6, Section 3.3):** Time per sample for GQA-XXL as a function of groups with input length 2048, output length 512:
- Going from 1 (MQA) to 8 groups adds modest inference overhead
- Sharper increase in time as groups increase beyond 8 toward H (MHA at ~2s)
- 8 groups selected as a favorable middle ground (limited evidence -- single model, timing only, no quality comparison across group counts beyond MQA vs GQA-8)

---

## Limitations and Failure Modes

**Explicitly acknowledged by authors (Section 5, Limitations):**
- ROUGE score is a flawed evaluation metric for summarization; it does not capture the full quality picture, making it difficult to be certain the quality-speed tradeoffs are correct
- Due to limited computation, the XXL GQA model is not compared to a model trained from scratch, so relative performance of uptraining vs training from scratch is unknown
- Evaluated only on encoder-decoder models (T5); decoder-only models (which do not have separate cross-attention) may show different tradeoffs -- the authors expect GQA to have a stronger advantage over MQA in decoder-only settings
- The memory bandwidth overhead from KV loading is most important when generating longer sequences, for which quality is inherently difficult to evaluate

**Training Stability (Appendix A):**
- MQA trained from scratch shows frequent loss spikes during pre-training
- MQA models trained from scratch diverge immediately on long-input fine-tuning tasks
- Uptrained MQA models are more stable but still display high variance (average over 3 runs reported)
- GQA appears stable; root causes of MQA instability were not further investigated

**[Inferred]** No evaluation on decoder-only architectures limits the direct applicability of the quantitative claims to the now-dominant decoder-only paradigm.

**[Inferred]** No variance or confidence intervals reported for the main Table 1 results (single run per configuration for GQA and MHA), limiting statistical confidence.

**[Inferred]** All timing measurements are on TPUv4; GPU or other hardware may show different memory bandwidth profiles and different quality-speed tradeoffs.

#### Scope and Comparability

- **What was not tested:** Decoder-only models (GPT-style), models smaller than T5-Large or larger than T5-XXL, non-English tasks, classification/NLI tasks (explicitly excluded), beam search or sampling decoding strategies (only greedy decoding used), GQA trained from scratch (only uptraining evaluated for XXL).
- **Comparability notes:** All timing is on TPUv4 with xprof, using 8 TPUs with up to 32 batch size. Inference time measurements are per sample per chip. Other inference timing studies (e.g., Pope et al., 2022) may use different hardware/parallelization setups, limiting direct comparison. ROUGE-1 is used for summarization comparison, which may differ from ROUGE-L or human evaluation commonly used in other work.

---

## Conclusions

### Contributions

1. **Uptraining recipe for MHA-to-MQA/GQA conversion:** Demonstrated that existing MHA checkpoints can be converted to MQA or GQA using mean-pooling initialization and only 5% additional pre-training (~600 TPUv3 chip-days for T5-XXL), providing a cost-effective alternative to training from scratch (Figure 5, Section 2.1).

2. **Grouped-Query Attention as a principled interpolation:** Introduced GQA as a generalization of MHA and MQA that achieves near-MHA quality (47.1 vs 47.2 average) at near-MQA speed (0.28s vs 0.24s), with a tunable quality-speed tradeoff through the number of groups G (Table 1, Section 2.2).

3. **Training stability improvement over MQA:** Showed that GQA avoids the loss spikes and fine-tuning divergence observed with MQA, making it a more reliable choice for deployment (Appendix A).

4. **Mean-pooling as the best conversion strategy:** Established that mean-pooling projection matrices preserves more information than selecting a single head or random initialization, yielding ~55.6 vs ~54.6 average performance (Figure 4, Section 3.3).

### Implications

1. **Practical deployment path:** Organizations with existing MHA models can adopt GQA for inference speedup without full retraining, requiring only 5% of original training compute.

2. **Scalability advantage:** GQA's proportional KV reduction makes it particularly attractive for larger models where standard sharding wastes capacity by replicating single KV heads; this has been validated by Llama 2's adoption of GQA at 70B scale.

3. **Architectural design knob:** GQA provides a tunable parameter G for trading quality vs speed based on deployment constraints, with 8 groups identified as a favorable middle ground for T5-XXL (speculative whether this generalizes to other architectures and scales).

---

## Key Claims

1. **GQA achieves near-MHA quality at near-MQA speed.** On T5-XXL, GQA-8 achieves 47.1 average performance vs MHA-XXL 47.2, with 0.28s inference time vs MHA 1.51s and MQA 0.24s (Table 1, Figure 3). Scope: T5-XXL encoder-decoder, 5% uptraining, greedy decoding, TPUv4. Tested across 7 tasks on one architecture with no variance reported (moderate evidence).

2. **5% uptraining is sufficient for checkpoint conversion.** Mean-pooling K/V heads followed by 5% additional pre-training recovers most quality, with diminishing returns beyond 10% (Figure 5, Section 2.1). Scope: T5-XXL with MQA and GQA-8. Magnitude: ~600 TPUv3 chip-days. Single model tested (limited evidence for generalization).

3. **Mean pooling outperforms alternative conversion methods.** Information preservation ordering: mean pooling (~55.6) > first head selection (~55.1) > random initialization (~54.6) on a 3-task average (Figure 4, Section 3.3). Scope: T5-Large uptrained to MQA, alpha = 0.05. Values are approximate from bar chart; single model size tested (limited evidence).

4. **GQA is more training-stable than MQA.** MQA trained from scratch shows frequent loss spikes during pre-training and diverges on long-input fine-tuning; uptrained MQA has high variance; GQA does not exhibit these issues (Appendix A). Scope: T5-Large trained from scratch and uptrained, long-input fine-tuning tasks. Magnitude: qualitative -- MQA diverges, GQA does not. Root causes not investigated (limited evidence -- observation without systematic analysis).

5. **GQA presents a particularly good trade-off for larger models.** Because KV-cache scales with d while model FLOPs scale with d^2, larger models suffer relatively less from KV attention overhead, and GQA's proportional KV reduction avoids the waste from standard MQA sharding (Section 2.2, Figure 6). Scope: theoretical argument supported by T5-XXL timing. Magnitude: going from 1 to 8 groups adds modest overhead; sharper increase beyond 8 (Figure 6). Single model size timed (limited evidence for the scaling argument).

6. **Uptrained MQA provides a favorable tradeoff relative to smaller MHA models.** MQA-XXL achieves higher quality (46.6 vs 46.0) and faster inference (0.24s vs 0.37s) than MHA-Large (Table 1, Figure 3). Scope: T5-XXL uptrained to MQA vs T5-Large MHA, greedy decoding, TPUv4.

---

## Open Questions

1. **Uptraining vs training from scratch:** The paper does not compare uptrained GQA to GQA trained from scratch with the same total compute. What is the quality gap, and does uptraining introduce any systematic biases from the MHA initialization? (Explicitly left as future work, Section 5.)

2. **Decoder-only models:** The paper evaluates only encoder-decoder models (T5). How does GQA perform in decoder-only architectures where there is no separate cross-attention? The authors expect GQA to have a stronger advantage in this setting. (Subsequently addressed by Llama 2's adoption of GQA at 70B scale.)

3. **Optimal group count:** Is 8 the optimal number of groups across different model sizes and architectures, or should G scale with model size? The paper selects 8 as a "favorable middle ground" for T5-XXL but does not systematically explore this for other scales (Section 3.3, Figure 6).

---

## Core References and Why They Are Referenced

### Foundational Work

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Original multi-head attention mechanism that MQA and GQA modify.

- **Shazeer (2019)** -- *Fast Transformer Decoding: One Write-Head is All You Need.* Introduced multi-query attention (MQA), the direct predecessor that GQA generalizes. Foundational to the entire paper.

### Memory Bandwidth Analysis

- **Pope et al. (2022)** -- *Efficiently Scaling Transformer Inference.* Analyzed memory bandwidth bottlenecks in large-scale inference, showed MQA is especially helpful for long inputs, and identified the sharding replication issue that GQA addresses.

- **Williams et al. (2009)** -- *Roofline: An Insightful Visual Performance Model for Multicore Architectures.* Theoretical framework for understanding compute vs memory bandwidth tradeoffs underlying the paper's motivation.

### Uptraining Methodology

- **Komatsuzaki et al. (2022)** -- *Sparse Upcycling.* Inspired the uptraining approach by demonstrating conversion of dense T5 checkpoints to sparsely activated Mixture-of-Experts models.

### Models Used in Evaluation

- **Raffel et al. (2020)** -- *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5).* Base architecture for all experiments; public checkpoints used for initialization.

- **Touvron et al. (2023)** -- *LLaMA: Open and Efficient Foundation Language Models.* Cited as a prominent MHA model that could benefit from GQA conversion.

### Complementary Efficiency Methods

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* Memory-efficient attention computation; orthogonal to GQA's KV-cache reduction approach.

- **de Jong et al. (2022)** -- *FiDO: Fusion-in-Decoder Optimized.* Layer-sparse cross-attention approach; showed MQA is helpful for long inputs. Complementary KV overhead reduction.

- **Chen et al. (2023) and Leviathan et al. (2022)** -- *Speculative Sampling / Speculative Decoding.* Alternative approaches to ameliorating the memory bandwidth bottleneck by proposing multiple tokens with a smaller model.

### Independent and Related Work on Grouped Attention

- **Rabe (2023)** -- *Memory-efficient attention (Flaxformer implementation).* Independently developed GQA with public implementation.

- **Park et al. (2020), Luo et al. (2022), Ni et al. (2023)** -- Explored grouping attention heads for computational efficiency in various settings, without specifically targeting key-value heads and memory bandwidth overhead.

### Evaluation Datasets

- **Nallapati et al. (2016)** -- CNN/Daily Mail summarization.
- **Cohan et al. (2018)** -- arXiv and PubMed long-document summarization.
- **Fabbri et al. (2019)** -- Multi-News multi-document summarization.
- **Zhu et al. (2021)** -- MediaSum interview summarization.
- **Joshi et al. (2017)** -- TriviaQA question answering.
