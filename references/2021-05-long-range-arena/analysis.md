# Long Range Arena: A Benchmark for Efficient Transformers

**Authors:** Yi Tay, Mostafa Dehghani, Samira Abnar, Yikang Shen, Dara Bahri, Philip Pham, Jinfeng Rao, Liu Yang, Sebastian Ruder, Donald Metzler (Google Research, Google DeepMind)
**Date:** May 2021, ICLR 2021 (arXiv:2011.04006)

---

## Core Research Problem

Transformers suffer from quadratic self-attention complexity, restricting their application to long sequences. A large number of efficient Transformer variants ("xformers") have been proposed to address this -- Sparse Transformers (Child et al., 2019), Reformers (Kitaev et al., 2020), Linformers (Wang et al., 2020), Longformers (Beltagy et al., 2020), Performers (Choromanski et al., 2020), and others -- each claiming comparable quality to vanilla Transformers while reducing memory complexity.

However, evaluation of these models is inconsistent and inadequate:

1. **No consensus on benchmarking.** Every model is evaluated on a different set of tasks and datasets, making cross-model comparison difficult.
2. **Arbitrary task selection.** Benchmarks used for evaluation are often chosen without considering whether they actually test long-range modeling ability. Standard NLU benchmarks (GLUE, MultiNLI, SST) average under 100 tokens per example.
3. **Conflation with pretraining.** Many papers mix the benefits of architectural inductive bias with the effects of pretraining (Ainslie et al., 2020; Zaheer et al., 2020; Wang et al., 2020), obfuscating the true value of the architecture.
4. **Language modeling limitations.** Language modeling perplexity, a common evaluation for xformers, is dominated by short-range word co-occurrences rather than long-range dependencies (Daniluk et al., 2017; Rae & Razavi, 2020).

**The core challenge is how to create a systematic, unified benchmark that isolates the ability of efficient Transformer architectures to reason over long-range dependencies across diverse data types.**

---

## Problem Solutions

LRA provides a suite of 6 tasks with sequence lengths ranging from 1K to 16K tokens, spanning text, mathematical expressions, natural images, and synthetic images. The benchmark is designed to be model-agnostic and pretraining-free.

1. **Diverse task types.** Tasks probe different capabilities: hierarchical reasoning (ListOps), compositionality (byte-level text classification), compressed representation quality (document retrieval), spatial reasoning (image classification, Pathfinder), and extreme-length generalization (Path-X).
2. **Pretraining excluded by design.** All models are trained from scratch on each task, isolating architectural inductive bias from pretraining effects.
3. **Unified framework.** All models share the same hyperparameter budget (layers, heads, embedding dimensions), and the benchmark is implemented in a single JAX/FLAX codebase for reproducible side-by-side comparison.

---

## Approach Details

### Method

LRA defines 6 tasks, each probing a different aspect of long-range modeling:

| Task | Data Type | Sequence Length | # Classes | Metric | What It Probes |
|---|---|---|---|---|---|
| Long ListOps | Synthetic math | 2K | 10 | Accuracy | Hierarchical reasoning |
| Byte-Level Text | IMDb reviews (bytes) | 4K | 2 | Accuracy | Compositionality over characters |
| Byte-Level Retrieval | AAN corpus (bytes) | 4K + 4K = 8K | 2 | Accuracy | Compressed representation matching |
| Image Classification | CIFAR-10 (pixels) | 1K (32x32) | 10 | Accuracy | 2D spatial reasoning from 1D sequence |
| Pathfinder | Synthetic images | 1K (32x32) | 2 | Accuracy | Long-range spatial dependency |
| Path-X | Synthetic images | 16K (128x128) | 2 | Accuracy | Extreme-length spatial dependency |

**Long ListOps.** An extended version of ListOps (Nangia & Bowman, 2018) with sequences up to 2K tokens. Sequences have hierarchical structure with operators MAX, MEAN, MEDIAN, SUM_MOD enclosed in brackets. The model must access all tokens and model the logical structure to classify into one of 10 classes.

**Byte-Level Text Classification.** IMDb sentiment classification (Maas et al., 2011) at the byte/character level (max 4K bytes), forcing the model to compose characters into words into phrases. Without pretraining, word-level models achieve high-80s accuracy while byte-level models score only mid-60s.

**Byte-Level Document Retrieval.** Citation link prediction on the ACL Anthology Network (Radev et al., 2013) using a two-tower setup: each document is encoded independently (no cross-attention), representations are concatenated and classified. 4K bytes per document, 8K total.

**Image Classification.** CIFAR-10 images flattened to a 1D sequence of 1,024 grayscale pixels (8-bit intensity, vocabulary 256). No CNN stem or 2D positional information is allowed -- the model must learn spatial structure from a flat sequence.

**Pathfinder.** A synthetic visual task (Linsley et al., 2018; Kim et al., 2020) where the model decides whether two circles are connected by a dashed path amid distractors. Images are 32x32 (1,024 pixels).

**Path-X.** An extreme version of Pathfinder with 128x128 images (16,384 pixels). Included as a litmus test for whether models that solve Pathfinder at 1K can generalize to 16K.

### Key Technical Components

**Required attention span.** The authors define a metric to quantify how much long-range attention each task demands: the mean distance between query and attended tokens, weighted by attention weights, averaged over all attention modules in a trained vanilla Transformer. All LRA tasks show high required attention spans (300--1,400 tokens), confirming that models must look beyond local context.

**Fixed hyperparameter protocol.** To ensure fair comparison, all models share:
- ListOps: 512 embedding dim, 8 heads, 6 layers, FFN dim 2048, trained 5K steps
- Text: 512 embedding dim, 8 heads, 6 layers, FFN dim 2048, trained 20K steps, batch 32
- Retrieval: 128 embedding dim, 4 heads, 4 layers, FFN dim 512, trained 5K steps, batch 32
- Image: 64 QKV dim, 4 heads, 3 layers, FFN dim 128, trained 200 epochs
- Pathfinder: 128 QKV dim, 8 heads, 4 layers, FFN dim 128, trained 200 epochs

Optimizer: Adam with warmup. Softmax cross-entropy loss throughout. [CLS] token pooling with 2-layer MLP classifier for all tasks. For retrieval, the scoring function is:

> Y = MLP([X1, X2, X1 * X2, X1 - X2])

where X1, X2 are [CLS] embeddings from shared encoders.

**Desiderata.** The benchmark was designed with six explicit criteria: (1) generality -- all xformers must be applicable (encoding-only tasks); (2) simplicity -- no data augmentation or pretraining; (3) challenging -- room for improvement; (4) long inputs -- 1K to 16K tokens; (5) probing diverse aspects -- hierarchical, spatial, compositional reasoning; (6) non-resource-intensive -- accessible without industry-grade compute.

### Experimental Setup

**Models evaluated (10 xformers + 2 baselines):**
- Vanilla Transformer (Vaswani et al., 2017)
- Local Attention baseline
- Sparse Transformer (Child et al., 2019)
- Longformer (Beltagy et al., 2020)
- Linformer (Wang et al., 2020)
- Reformer (Kitaev et al., 2020)
- Sinkhorn Transformer (Tay et al., 2020b)
- Synthesizer (Tay et al., 2020a)
- BigBird (Zaheer et al., 2020)
- Linear Transformer (Katharopoulos et al., 2020)
- Performer (Choromanski et al., 2020)

**Hardware:** 4x4 TPU V3 chips. Efficiency benchmarks use batch size 32 on the text classification task across sequence lengths {1K, 2K, 3K, 4K}.

**Implementation:** All models re-implemented in JAX/FLAX. Sparse Transformer and Longformer use equivalent mask-based implementations (no custom CUDA kernels) and are therefore excluded from speed benchmarks.

### Key Results

| Model | ListOps | Text | Retrieval | Image | Pathfinder | Path-X | Avg |
|---|---|---|---|---|---|---|---|
| Transformer | 36.37 | 64.27 | 57.46 | 42.44 | 71.40 | FAIL | 54.39 |
| Local Attention | 15.82 | 52.98 | 53.39 | 41.46 | 66.63 | FAIL | 46.06 |
| Sparse Trans. | 17.07 | 63.58 | **59.59** | **44.24** | 71.71 | FAIL | 51.24 |
| Longformer | 35.63 | 62.85 | 56.89 | 42.22 | 69.71 | FAIL | 53.46 |
| Linformer | 35.70 | 53.94 | 52.27 | 38.56 | 76.34 | FAIL | 51.36 |
| Reformer | **37.27** | 56.10 | 53.40 | 38.07 | 68.50 | FAIL | 50.67 |
| Sinkhorn Trans. | 33.67 | 61.20 | 53.83 | 41.23 | 67.45 | FAIL | 51.39 |
| Synthesizer | 36.99 | 61.68 | 54.67 | 41.61 | 69.45 | FAIL | 52.88 |
| BigBird | 36.05 | 64.02 | 59.29 | 40.83 | 74.87 | FAIL | **55.01** |
| Linear Trans. | 16.13 | **65.90** | 53.09 | 42.34 | 75.30 | FAIL | 50.55 |
| Performer | 18.01 | 65.40 | 53.82 | 42.77 | **77.05** | FAIL | 51.41 |

Average score excludes Path-X (all models FAIL, achieving at best 50% = random chance).

- **No one-size-fits-all.** BigBird achieves the best average (55.01) through consistent performance across tasks, not dominance on any single task. No model wins on more than one task.
- **Kernel-based models show task-dependent behavior.** Performers and Linear Transformers excel on Text (65--66%) and Pathfinder (75--77%) but collapse on ListOps (16--18%), suggesting kernel approximations struggle with hierarchical reasoning.
- **Fixed-pattern sparse models win on retrieval.** Sparse Transformer (59.59) and BigBird (59.29) are best on retrieval, while kernel-based and low-rank models score near random chance.
- **All models fail on Path-X.** Despite solving Pathfinder (avg 72%), no model learns anything on the 16K-token Path-X variant, demonstrating that extreme sequence length alone can prevent learning entirely.
- **Image classification has severe generalization gap.** Most models overfit training data (e.g., Linformer: 97.23% train vs. 38.56% test) but fail to generalize, even with extensive regularization. Adding a CNN stem to vanilla Transformer raises test accuracy from 42.44% to 75.32%.

### Efficiency Results

| Model | Speed at 4K (relative to Transformer) | Memory at 4K (GB/device) |
|---|---|---|
| Transformer | 1.0x (1.4 steps/s) | 9.48 |
| Performer | **5.7x** (8.0 steps/s) | 1.06 |
| Linear Trans. | 5.6x (7.8 steps/s) | **1.03** |
| Linformer | 5.5x (7.7 steps/s) | **0.99** |
| Local Attention | 5.3x (7.4 steps/s) | 1.37 |
| Sinkhorn Trans. | 3.8x (5.3 steps/s) | 1.48 |
| Synthesizer | 1.4x (1.9 steps/s) | 6.99 |
| BigBird | 1.1x (1.5 steps/s) | 2.88 |
| Reformer | 0.8x (1.1 steps/s) | 2.28 |

- **Kernel-based models are fastest.** Performer, Linear Transformer, and Linformer achieve 5.5--5.7x speedup at 4K tokens and ~10x memory reduction (0.99--1.06 GB vs. 9.48 GB).
- **BigBird trades speed for quality.** Best average accuracy but similar speed to vanilla Transformer (1.1x at 4K).
- **Reformer is slower than Transformer.** 0.8x at 4K and 0.5x at 1K, contrary to its theoretical efficiency, due to implementation overhead.

### Limitations

1. **Byte tokenization as length proxy.** The two text tasks use byte-level tokenization to artificially inflate sequence length. This conflates compositional challenge (learning to compose bytes into words) with long-range dependency challenge.
2. **Encoder-only scope.** All tasks require encoding only, excluding autoregressive generation tasks where some xformers (e.g., Linformer) are inapplicable.
3. **Maximum 16K tokens.** Path-X at 16K is the longest task, far below the context lengths of modern LLMs (128K--1M+ tokens).
4. **No natural language long-range tasks.** The two NLP tasks (Text, Retrieval) are byte-level and relatively short (~4K bytes each). No task involves reasoning over naturally long documents.

---

## Conclusions

1. **First systematic xformer benchmark.** LRA provides the first unified, pretraining-free benchmark for comparing efficient Transformer architectures across diverse data types and sequence lengths (1K--16K), enabling reproducible side-by-side evaluation of 10 models.

2. **No single model dominates.** BigBird achieves the best average score (55.01) through consistency, but different architectures excel on different tasks. Kernel-based models (Performers, Linear Transformers) trade hierarchical reasoning ability for speed, while sparse-pattern models (BigBird, Sparse Transformer) sacrifice speed for quality.

3. **Efficiency-quality trade-off is real.** Kernel-based models achieve 5--6x speedup and ~10x memory reduction, but the fastest models are not the most accurate. The Pareto-optimal models are Performer, Linformer, and Linear Transformer (best speed-quality trade-off).

4. **Extreme length breaks all models.** All 10 xformers and the vanilla Transformer fail on Path-X (16K tokens), despite solving the identical Pathfinder task at 1K tokens. This demonstrates that scaling sequence length can fundamentally obstruct learning, not merely degrade it.

5. **Catalyzed the state-space model revolution.** LRA's unsolved Path-X challenge directly motivated the development of S4 (Gu et al., 2022), which achieved 86.05% on Path-X and 80.48% average -- far exceeding all Transformer baselines. LRA thus became the proving ground for a new class of sequence models beyond the Transformer paradigm.

---

## Core References and Why They Are Referenced

### Transformer Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that defines the quadratic-complexity self-attention mechanism LRA is designed to benchmark alternatives to.

### Efficient Transformer Models Evaluated

- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Fixed sparse attention patterns. Best on Retrieval (59.59) and Image (44.24).
- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Sliding-window attention with global tokens. Consistent but not best on any task. Excluded from speed benchmarks due to CUDA kernel requirements.
- **Wang et al. (2020)** -- *Linformer: Self-Attention with Linear Complexity.* Low-rank projection of keys/values. Smallest memory footprint (0.99 GB at 4K) and 5.5x speedup, but weak on Image and Text tasks.
- **Kitaev et al. (2020)** -- *Reformer: The Efficient Transformer.* LSH-based attention. Surprisingly slower than vanilla Transformer in practice (0.5--0.8x) due to implementation overhead.
- **Tay et al. (2020b)** -- *Sparse Sinkhorn Attention.* Learned sparse patterns via Sinkhorn normalization. Mid-range performance on all tasks.
- **Tay et al. (2020a)** -- *Synthesizer: Rethinking Self-Attention in Transformer Models.* Dense attention without explicit dot-product. Moderate performance, slow at longer sequences.
- **Zaheer et al. (2020)** -- *BigBird: Transformers for Longer Sequences.* Combines random, window, and global attention. Best overall LRA score (55.01) but nearly as slow as vanilla Transformer.
- **Katharopoulos et al. (2020)** -- *Transformers Are RNNs: Fast Autoregressive Transformers with Linear Attention.* Kernel-based linear attention. 5.6x speedup, strong on Text and Pathfinder, collapses on ListOps.
- **Choromanski et al. (2020)** -- *Rethinking Attention with Performers.* FAVOR+ random feature approximation. Fastest model (5.7x), best on Pathfinder (77.05), but worst on ListOps (18.01).

### Benchmark Tasks and Datasets

- **Nangia & Bowman (2018)** -- *ListOps: A Diagnostic Dataset for Latent Tree Learning.* The original short-sequence ListOps task that LRA extends to 2K tokens for hierarchical reasoning evaluation.
- **Maas et al. (2011)** -- *Learning Word Vectors for Sentiment Analysis.* IMDb reviews dataset used for the byte-level text classification task.
- **Radev et al. (2013)** -- *The ACL Anthology Network Corpus.* Citation link dataset used for the byte-level document retrieval task.
- **Linsley et al. (2018)** -- *Learning Long-Range Spatial Dependencies with Horizontal Gated Recurrent Units.* Original Pathfinder challenge for spatial dependency learning, adapted by LRA for the Pathfinder and Path-X tasks.
- **Krizhevsky (2009)** -- *Learning Multiple Layers of Features from Tiny Images.* CIFAR-10 dataset used for the image classification task.

### Attention Span and Language Modeling Analysis

- **Daniluk et al. (2017)** -- *Frustratingly Short Attention Spans in Neural Language Modeling.* Shows LSTM attention rarely extends beyond 7 words, motivating LRA's explicit long-range span requirement.
- **Rae & Razavi (2020)** -- *Do Transformers Need Deep Long-Range Memory?* Argues language modeling perplexity is dominated by short-range signal, supporting LRA's choice of non-LM tasks.

### Survey

- **Tay et al. (2020c)** -- *Efficient Transformers: A Survey.* Comprehensive survey of efficient Transformer methods by the same authors, providing the taxonomy that motivates LRA's model selection.

#### Cross-References in Available Papers

- **SCROLLS (2022-12-scrolls-long-language-sequences):** Directly critiques LRA for having only two natural language tasks, using byte tokenization to artificially inflate sequence length, and truncating at ~1,000 words. SCROLLS proposes a purely NLP-focused benchmark with naturally long texts (1.7K--51.6K words).
- **LongBench (2024-08-longbench-bilingual-benchmark):** Argues LRA's synthetic-only evaluation does not mirror real-world scenarios. Proposes bilingual, multi-task evaluation with real documents.
- **L-Eval (2024-08-l-eval-standardized-evaluation):** Contrasts LRA's encoder-only classification scope with generative LLM evaluation, targeting open-ended generation and long-form QA.
- **InfinityBench (2024-08-infinitebench-long-context-evaluation):** Notes LRA averages ~10K tokens, far below the 100K+ contexts modern LLMs claim to handle. Proposes tasks requiring 100K+ tokens.
- **LongICLBench (2025-03-longiclbench-long-in-context-learning):** Cites LRA as an early long-context benchmark with 1K--16K tokens, foundational to the evaluation landscape that LongICLBench extends.
