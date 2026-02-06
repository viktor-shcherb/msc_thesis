---
title: "Long Range Arena: A Benchmark for Efficient Transformers"
authors: "Tay, Dehghani, Abnar, Shen, Bahri, Pham, Rao, Yang, Ruder, Metzler"
year: 2021
venue: "ICLR 2021"
paper_type: conference-paper
categories: ["benchmarking", "attention-efficiency"]
scope: ["efficient Transformer evaluation", "long-range dependency benchmarking", "synthetic and real-world probing tasks"]
benchmarks_used: ["lra"]
models_introduced: []
models_evaluated: ["transformer-base"]
key_claims:
  - id: C1
    claim: "No single efficient Transformer variant dominates across all LRA tasks; BigBird achieves the best average (55.01) through consistency, not dominance on any individual task"
    evidence: "Table 1, Section 3.5"
    status: supported
  - id: C2
    claim: "Kernel-based models (Performer, Linear Transformer) collapse on hierarchically structured data (ListOps: 16--18%) while excelling on text classification (65--66%) and spatial tasks (Pathfinder: 75--77%)"
    evidence: "Table 1, Section 3.3"
    status: supported
  - id: C3
    claim: "Fixed sparse pattern models (Sparse Transformer, BigBird) outperform other approaches on document retrieval (59.59 and 59.29 respectively)"
    evidence: "Table 1, Section 3.3"
    status: supported
  - id: C4
    claim: "All 10 efficient Transformers and the vanilla Transformer fail on Path-X (16K tokens), achieving at best random chance (50%)"
    evidence: "Table 1, Section 3.3"
    status: supported
  - id: C5
    claim: "Performer achieves 5.7x speedup over vanilla Transformer at 4K tokens; Linformer achieves the smallest memory footprint (0.99 GB vs 9.48 GB, ~10x reduction)"
    evidence: "Table 2, Section 3.4"
    status: supported
  - id: C6
    claim: "Reformer is slower than vanilla Transformer in practice (0.8x at 4K, 0.5x at 1K) despite its theoretical efficiency gains"
    evidence: "Table 2, Section 3.4"
    status: supported
  - id: C7
    claim: "All LRA tasks exhibit high required attention spans (300--1300 tokens), confirming they test genuine long-range dependencies rather than local co-occurrences"
    evidence: "Figure 2, Section 2.3"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: evaluates
    detail: "Vanilla Transformer serves as the primary baseline across all LRA tasks"
  - target: 2020-04-longformer-long-document-transformer
    type: evaluates
    detail: "Longformer is one of the 10 efficient Transformer architectures benchmarked on LRA"
  - target: 2020-07-quantifying-attention-flow
    type: complementary
    detail: "LRA uses attention rollout (Abnar & Zuidema, 2020) for Pathfinder attention visualization in the appendix"
  - target: 2022-12-scrolls-long-language-sequences
    type: complementary
    detail: "SCROLLS critiques LRA for having only 2 NL tasks, using byte tokenization to inflate sequence length, and truncating at ~1000 words"
  - target: 2024-08-longbench-bilingual-benchmark
    type: complementary
    detail: "LongBench evaluates long-context ability on natural-text tasks, contrasting with LRA's synthetic and byte-level probing tasks"
  - target: 2025-03-longiclbench-long-in-context-learning
    type: complementary
    detail: "LongICLBench tests real-world classification at 2K-50K tokens via extreme-label ICL, complementing LRA's synthetic probing tasks at 1K-16K tokens"
  - target: 2024-05-mamba-selective-state-spaces
    type: extended-by
    detail: "Mamba uses LRA to demonstrate selective SSMs match or exceed Transformer attention on long-range tasks while being faster and using less memory"
  - target: 2025-04-longgenbench-long-form-generation
    type: complementary
    detail: "LongGenBench evaluates long-form generation quality (output-side), complementing LRA's focus on efficient input processing; both are synthetic benchmarks for long-sequence capabilities"
open_questions:
  - question: "Do LRA results on synthetic and byte-level tasks predict model performance on natural language long-context tasks?"
    addressed_by: null
  - question: "Can any architecture solve the Path-X task (16K tokens) without modifications such as a CNN stem or 2D positional information?"
    addressed_by: null
  - question: "Would aggressive per-model hyperparameter tuning change the relative ordering of efficient Transformer models on LRA?"
    addressed_by: null
---

# Long Range Arena: A Benchmark for Efficient Transformers

**Authors:** Yi Tay, Mostafa Dehghani, Samira Abnar, Yikang Shen, Dara Bahri, Philip Pham, Jinfeng Rao, Liu Yang, Sebastian Ruder, Donald Metzler (Google Research, Google DeepMind)
**Date:** May 2021, ICLR 2021 (arXiv:2011.04006)

---

## Core Research Problem

Transformers suffer from quadratic self-attention complexity, restricting their application to long sequences. A large number of efficient Transformer variants ("xformers") have been proposed -- Sparse Transformers (Child et al., 2019), Reformers (Kitaev et al., 2020), Linformers (Wang et al., 2020), Longformers (Beltagy et al., 2020), Performers (Choromanski et al., 2020), and others -- each claiming comparable quality to the vanilla Transformer while reducing memory complexity.

However, evaluation of these models is inconsistent and inadequate:

1. **No consensus on benchmarking.** Every model is evaluated on a different set of tasks and datasets, making cross-model comparison difficult (Section 1).
2. **Arbitrary task selection.** Benchmarks used for evaluation are often chosen without considering whether they actually test long-range modeling ability. Standard NLU benchmarks (GLUE, MultiNLI, SST) average under 100 tokens per example (Section 4.2).
3. **Conflation with pretraining.** Many papers mix architectural inductive bias with pretraining effects (Ainslie et al., 2020; Zaheer et al., 2020; Wang et al., 2020), obfuscating the true value of the architecture (Section 1).
4. **Language modeling limitations.** Language modeling perplexity, a common evaluation for xformers, is dominated by short-range word co-occurrences rather than long-range dependencies. LSTM attention rarely extends beyond 7 preceding words (Daniluk et al., 2017), and even Transformer-XL is sensitive to only ~900 tokens of context (Rae & Razavi, 2020; Section 4.2).

**The core challenge is how to create a systematic, unified benchmark that isolates the ability of efficient Transformer architectures to reason over long-range dependencies across diverse data types, without confounding effects of pretraining.**

---

## Problem Solutions

LRA provides a suite of 6 tasks with sequence lengths ranging from 1K to 16K tokens, spanning text, mathematical expressions, natural images, and synthetic images. The benchmark is designed to be model-agnostic and pretraining-free.

1. **Diverse task types.** Tasks probe different capabilities: hierarchical reasoning (ListOps), compositionality (byte-level text classification), compressed representation quality (document retrieval), spatial reasoning (image classification, Pathfinder), and extreme-length generalization (Path-X).
2. **Pretraining excluded by design.** All models are trained from scratch on each task, isolating architectural inductive bias from pretraining effects.
3. **Unified framework.** All models share a fixed hyperparameter budget (layers, heads, embedding dimensions) per task, and the benchmark is implemented in a single JAX/FLAX codebase for reproducible side-by-side comparison.

---

## Approach Details

### Method

LRA defines 6 tasks, each probing a different aspect of long-range modeling:

| Task | Data Type | Sequence Length | # Classes | Metric | What It Probes |
|---|---|---|---|---|---|
| Long ListOps | Synthetic math | 2K | 10 | Accuracy | Hierarchical reasoning |
| Byte-Level Text | IMDb reviews (bytes) | 1K--4K | 2 | Accuracy | Compositionality over characters |
| Byte-Level Retrieval | AAN corpus (bytes) | 4K + 4K = 8K | 2 | Accuracy | Compressed representation matching |
| Image Classification | CIFAR-10 (pixels) | 1K (32x32) | 10 | Accuracy | 2D spatial reasoning from 1D sequence |
| Pathfinder | Synthetic images | 1K (32x32) | 2 | Accuracy | Long-range spatial dependency |
| Path-X | Synthetic images | 16K (128x128) | 2 | Accuracy | Extreme-length spatial dependency |

**Long ListOps.** An extended version of ListOps (Nangia & Bowman, 2018) with sequences up to 2K tokens. Sequences have hierarchical structure with operators MAX, MEAN, MEDIAN, SUM_MOD enclosed in brackets. The model must access all tokens and model the logical structure to classify into one of 10 classes. Example: `[MAX 4 3 [MIN 2 3 ] 1 0 [MEDIAN 1 5 8 9, 2]]` → `5` (Section 2.2.1).

**Byte-Level Text Classification.** IMDb sentiment classification (Maas et al., 2011) at the byte/character level (max 4K bytes), forcing the model to compose characters into words into phrases. This setup differs from character-level language modeling, where nearby context suffices; here the model must reason with compositional, unsegmented data. Without pretraining, word-level models achieve high-80s accuracy while byte-level models score only mid-60s (Section 2.2.2, footnote 3).

**Byte-Level Document Retrieval.** Citation link prediction on the ACL Anthology Network (Radev et al., 2013) using a two-tower setup: each document is encoded independently (no cross-attention), representations are combined and classified. 4K bytes per document, 8K total. The scoring function is:

> Y = MLP([X1, X2, X1 * X2, X1 - X2])

where X1, X2 are [CLS] embeddings from shared encoders, and MLP is a 2-layer MLP with ReLU activations (Appendix A.1.3, Equation 1).

**Image Classification.** CIFAR-10 images flattened to a 1D sequence of 1,024 grayscale pixels (8-bit intensity, vocabulary size 256). No CNN stem or 2D positional information is allowed -- the model must learn spatial structure from a flat sequence (Section 2.2.4).

**Pathfinder.** A synthetic visual task (Linsley et al., 2018; Kim et al., 2020) motivated by cognitive psychology (Houtkamp & Roelfsema, 2010). The model decides whether two circles are connected by a dashed path amid distractors. Images are 32x32 (1,024 pixels) (Section 2.2.5).

**Path-X.** An extreme version of Pathfinder with 128x128 images (16,384 pixels). Included as a litmus test for whether models that solve Pathfinder at 1K can generalize to 16K (Section 2.2.6).

### Key Technical Components

**Required attention span.** The authors define a quantitative metric for how much long-range attention each task demands: the mean distance between the query token and the attended tokens, weighted by attention weights, averaged over all attention modules in the best vanilla Transformer for each task, over 1K validation samples. All LRA tasks show high required attention spans, confirming that models must look beyond local context. From Figure 2, approximate values range from ~300 tokens (ListOps, Text) to ~1,300 tokens (Pathfinder) (Section 2.3, Figure 2).

**Fixed hyperparameter protocol.** To ensure fair comparison, all models share task-specific hyperparameters (Appendix A.1--A.3):

- **ListOps:** 512 embedding dim, 8 heads, 6 layers, FFN dim 2048, trained 5K steps
- **Text:** 512 hidden dim, 8 heads, 6 layers, FFN dim 2048, lr 0.05, weight decay 0.1, Adam with warmup, 20K steps, batch 32. Sequence lengths {1K, 2K, 3K, 4K} evaluated; best result reported.
- **Retrieval:** 128 embedding dim, 4 heads, 4 layers, FFN dim 512, batch 32, Adam, 5K steps, lr 0.5
- **Image:** 64 QKV dim, 4 heads, 3 layers, FFN dim 128, lr 0.01, 200 epochs
- **Pathfinder:** 128 QKV dim, 8 heads, 4 layers, FFN dim 128, lr 0.01, 200 epochs

All tasks use softmax cross-entropy loss, [CLS] token pooling, and a 2-layer MLP classifier head with ReLU activations.

**Desiderata.** The benchmark was designed with six explicit criteria (Section 2.1): (1) **generality** -- all xformers must be applicable (encoding-only tasks); (2) **simplicity** -- no data augmentation or pretraining; (3) **challenging** -- room for improvement; (4) **long inputs** -- 1K to 16K tokens; (5) **probing diverse aspects** -- hierarchical, spatial, compositional reasoning; (6) **non-resource intensive** -- accessible without industry-grade compute.

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
- Performer (Choromanski et al., 2020b) -- uses FAVOR+

**Hardware:** 4x4 TPU V3 chips. Efficiency benchmarks use batch size 32 on the text classification task across sequence lengths {1K, 2K, 3K, 4K} (Section 3.4).

**Implementation:** All models re-implemented in JAX/FLAX. Sparse Transformer and Longformer use equivalent mask-based implementations (no custom CUDA kernels) and are therefore **excluded from speed benchmarks** (Appendix B.2). Reformer is implemented using VMAP over batch and head dimensions rather than the standard batched tensor approach (Appendix B.2). For Linformer, projections are shared between key and value but not across layers. For Performer, the FAVOR+ variant is used (Appendix B.1).

### Key Results

**Task performance (Table 1):**

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
| Task Avg (Std) | 29 (9.7) | 61 (4.6) | 55 (2.6) | 41 (1.8) | 72 (3.7) | FAIL | 52 (2.4) |

Average score excludes Path-X (all models FAIL, achieving at best 50% = random chance on a binary task). FAIL denotes models that did not learn anything above random chance (Table 1 caption).

- **No one-size-fits-all.** BigBird achieves the best average (55.01) through consistent performance across tasks, not dominance on any single task. No model wins on more than one task (Section 3.5).
- **Kernel-based models show task-dependent behavior.** Performers and Linear Transformers excel on Text (65--66%) and Pathfinder (75--77%) but collapse on ListOps (16--18%), suggesting kernel approximations struggle with hierarchical reasoning (Section 3.3).
- **Fixed-pattern sparse models win on retrieval.** Sparse Transformer (59.59) and BigBird (59.29) perform best on retrieval. Models based on low-rank factorization and kernels perform relatively worse on this task, with some scoring near random chance (Section 3.3).
- **All models fail on Path-X.** Despite solving Pathfinder (avg 72%), no model learns anything on the 16K-token Path-X variant, demonstrating that extreme sequence length alone can prevent learning entirely (Section 3.3).
- **Image classification has a severe generalization gap.** Most models overfit training data but fail to generalize. For example, Linformer achieves 97.23% train accuracy but only 38.56% test accuracy; Synthesizer achieves 97.31% train but 41.61% test (Table 3, Appendix A.2.1). The authors note that replacing the embedding layer with a CNN stem raises vanilla Transformer test accuracy from 42.44% to 75.32%, and adding 2D relative positional embedding yields 61.72% (Appendix A.2.1). However, these modifications are excluded from the benchmark by design.

### Efficiency Results

**Speed and memory at varying sequence lengths (Table 2, batch size 32, 4x4 TPU V3):**

| Model | Speed at 4K (steps/s) | Speedup vs Transformer | Memory at 4K (GB/device) |
|---|---|---|---|
| Transformer | 1.4 | 1.0x | 9.48 |
| Local Attention | 7.4 | 5.3x | 1.37 |
| Linformer | 7.7 | 5.5x | **0.99** |
| Reformer | 1.1 | 0.8x | 2.28 |
| Sinkhorn Trans. | 5.3 | 3.8x | 1.48 |
| Synthesizer | 1.9 | 1.4x | 6.99 |
| BigBird | 1.5 | 1.1x | 2.88 |
| Linear Trans. | 7.8 | 5.6x | 1.03 |
| Performer | **8.0** | **5.7x** | 1.06 |

Sparse Transformer and Longformer are excluded from speed benchmarks because their implementations use equivalent mask-based approaches rather than custom CUDA kernels (Appendix B.2).

- **Kernel-based models are fastest.** Performer, Linear Transformer, and Linformer achieve 5.5--5.7x speedup at 4K tokens and ~10x memory reduction (0.99--1.06 GB vs. 9.48 GB) (Section 3.4).
- **BigBird trades speed for quality.** Best average accuracy but similar speed to vanilla Transformer (1.1x at 4K) (Section 3.5, Figure 3).
- **Reformer is slower than Transformer.** 0.8x at 4K and 0.5x at 1K, contrary to its theoretical efficiency, due to implementation overhead (Section 3.4).
- **Memory scales well for kernel-based models.** Linformer and Performer memory consumption at 3K and 4K is approximately equal, indicating favorable scaling behavior (Section 3.4).

---

## Limitations and Failure Modes

1. **Byte tokenization as length proxy.** The two text tasks use byte-level tokenization to artificially inflate sequence length. This conflates the compositional challenge of learning to compose bytes into words with the long-range dependency challenge. The paper acknowledges this design choice differs from standard word-level evaluation (Section 2.2.2).
2. **Encoder-only scope.** All tasks require encoding only, excluding autoregressive generation tasks where some xformers (e.g., Linformer) are inapplicable. The authors state this is deliberate to ensure generality (desideratum 1, Section 2.1).
3. **Maximum 16K tokens.** Path-X at 16K is the longest task, far below the context lengths of modern LLMs (128K--1M+ tokens). The benchmark does not test behavior at these extreme scales. [Inference: this limits the benchmark's applicability to evaluating modern long-context models.]
4. **No natural language long-range tasks.** The two NLP tasks (Text, Retrieval) are byte-level and relatively short (~4K bytes each). No task involves reasoning over naturally long documents such as books or legal texts.
5. **Fixed hyperparameters may disadvantage some models.** The authors acknowledge that "the best performance and relative order of the models may change if we aggressively tune hyperparameters for all models" (Section 3.2). The results are presented as a starting point, not a definitive ranking.
6. **Implementation artifacts affect efficiency comparisons.** Sparse Transformer and Longformer are excluded from speed benchmarks due to the lack of custom CUDA kernels in the JAX implementation. Reformer's poor speed is attributed to implementation overhead rather than algorithmic inefficiency (Section 3.4, Appendix B.2).
7. **Image classification generalization gap.** All models struggle to generalize on the image task despite overfitting training data (e.g., Linformer: 97.23% train vs 38.56% test). The task tests whether models can learn pixel ordinality and spatial structure from raw symbols, which proved extremely difficult for all architectures (Appendix A.2.1, Table 3).

---

## Conclusions

### Contributions

1. **First systematic xformer benchmark.** LRA provides the first unified, pretraining-free benchmark for comparing efficient Transformer architectures across diverse data types and sequence lengths (1K--16K), with 6 tasks probing hierarchical, compositional, spatial, and retrieval capabilities. All models are implemented in a single JAX/FLAX codebase (Section 2, Section 5).

2. **Comprehensive side-by-side evaluation of 10 models.** The paper presents the most extensive evaluation of efficient Transformers at the time of publication, covering Sparse Transformers, Longformers, Linformers, Reformers, Sinkhorn Transformers, Synthesizers, BigBird, Linear Transformers, and Performers alongside the vanilla Transformer and a local attention baseline (Section 1, Section 3).

3. **Demonstrated no-one-size-fits-all result.** BigBird achieves the best average score (55.01) through consistency, but different architectures excel on different tasks. Kernel-based models trade hierarchical reasoning for speed; sparse-pattern models sacrifice speed for quality (Table 1, Section 3.5).

4. **Quantified efficiency-quality trade-off.** Kernel-based models (Performer, Linformer, Linear Transformer) achieve 5.5--5.7x speedup and ~10x memory reduction but are not the most accurate. BigBird is the most accurate but nearly as slow as vanilla Transformer (Table 2, Figure 3, Section 3.5).

5. **Identified Path-X as an unsolved challenge.** All models fail on the 16K-token Path-X task despite solving the identical Pathfinder task at 1K tokens, demonstrating that extreme sequence length can fundamentally obstruct learning (Table 1, Section 3.3).

6. **Introduced required attention span as a task characterization metric.** The metric quantifies how much long-range attention a task demands, validating that all LRA tasks require genuinely long-range dependencies (Figure 2, Section 2.3).

### Implications

1. **Architectural inductive biases matter more than efficiency class.** The divergent performance profiles of kernel-based vs. sparse-pattern vs. low-rank models suggest that the choice of attention approximation has task-dependent consequences that cannot be predicted from computational complexity alone. [Inference from Table 1 patterns.]

2. **Pretraining-free evaluation reveals fundamental architectural properties.** By removing pretraining, LRA exposes whether architectural design choices (e.g., kernel approximation, sparse patterns, low-rank projection) are inherently suited to different types of long-range reasoning. [Inference from Section 1 and Section 3.2.]

3. **Length itself is a qualitative, not just quantitative, barrier.** The total failure on Path-X (16K) despite success on Pathfinder (1K) implies that scaling sequence length does not merely degrade performance but can categorically prevent learning. [Supported by Section 3.3.]

---

## Key Claims

1. **C1: No single model dominates LRA.** BigBird achieves the best average (55.01) through consistency across tasks, but no model wins on more than one individual task. The ranking varies substantially across tasks (Table 1, Section 3.5). **Status: supported.**

2. **C2: Kernel-based models fail on hierarchical data.** Performer and Linear Transformer score 18.01 and 16.13 on ListOps (10-way classification, random chance = 10%) while achieving 65.40/65.90 on Text and 77.05/75.30 on Pathfinder. The authors suggest "kernel-based models (e.g., Performer, Linear Transformers) are possibly not as effective on hierarchically structured data" (Table 1, Section 3.3). **Status: supported.**

3. **C3: Sparse pattern models excel at retrieval.** Sparse Transformer (59.59) and BigBird (59.29) are the top two models on document retrieval. "Models that follow fixed sparse patterns do well on this task. Models that are based on low-rank factorization and kernels perform relatively worse" (Table 1, Section 3.3). **Status: supported.**

4. **C4: All models fail on Path-X.** All 10 xformers, vanilla Transformer, and the local attention baseline achieve at most 50% (random chance) on the 16K-token Path-X task. "The extreme length of the task can significantly obstruct a model from learning anything meaningful" (Table 1, Section 3.3). **Status: supported.**

5. **C5: Performer is the fastest model; Linformer has the smallest memory footprint.** At 4K tokens, Performer achieves 5.7x speedup (8.0 steps/s vs. 1.4). Linformer uses 0.99 GB per device vs. 9.48 GB for vanilla Transformer, a ~10x reduction (Table 2, Section 3.4). **Status: supported.**

6. **C6: Reformer is slower than vanilla Transformer in practice.** Reformer achieves 0.8x speed at 4K tokens and 0.5x at 1K tokens, attributed to implementation overhead despite theoretical efficiency gains (Table 2, Section 3.4). **Status: supported.**

7. **C7: All LRA tasks require high attention spans.** The required attention span metric, computed from a trained vanilla Transformer, shows all tasks require attention beyond local context, with spans ranging from ~300 tokens (ListOps, Text) to ~1,300 tokens (Pathfinder) (Figure 2, Section 2.3). **Status: supported.**

---

## Open Questions

1. **Do LRA results predict natural language performance?** LRA uses synthetic tasks and byte-level text; the paper does not evaluate whether model rankings transfer to word-level or document-level NLP tasks. The authors note that LRA is "model-agnostic" but do not validate against downstream NLP benchmarks (Section 1). **Addressed by:** null.

2. **Can any architecture solve Path-X?** The 16K-token task was left as an open challenge. Both training from scratch and transferring from Pathfinder-trained models failed for all architectures tested (Appendix A.3). **Addressed by:** null.

3. **Would per-model hyperparameter tuning change the rankings?** The authors explicitly note the fixed hyperparameter protocol may disadvantage some models: "the best performance and relative order of the models may change if we aggressively tune hyperparameters for all models" (Section 3.2). **Addressed by:** null.

4. **How would results change with pretraining?** LRA deliberately excludes pretraining to isolate architectural inductive bias. Whether the relative ordering of models holds when pretraining is included is an open question that the authors leave unaddressed (Section 1, Section 2.1). **Addressed by:** null.

---

## Core References and Why They Are Referenced

### Transformer Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that defines the quadratic-complexity self-attention mechanism LRA is designed to benchmark alternatives to. Vanilla Transformer serves as the primary baseline across all tasks.

### Efficient Transformer Models Evaluated

- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Fixed sparse attention patterns. Best on Retrieval (59.59) and Image (44.24). Excluded from speed benchmarks due to CUDA kernel requirements.
- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Sliding-window attention with global tokens. Consistent but not best on any task (avg 53.46). Excluded from speed benchmarks due to CUDA kernel requirements.
- **Wang et al. (2020)** -- *Linformer: Self-Attention with Linear Complexity.* Low-rank projection of keys/values. Smallest memory footprint (0.99 GB at 4K) and 5.5x speedup, but weak on Image (38.56) and Text (53.94).
- **Kitaev et al. (2020)** -- *Reformer: The Efficient Transformer.* LSH-based attention. Surprisingly slower than vanilla Transformer in practice (0.5--0.8x) due to implementation overhead.
- **Tay et al. (2020b)** -- *Sparse Sinkhorn Attention.* Learned sparse patterns via Sinkhorn normalization. Mid-range performance on all tasks (avg 51.39).
- **Tay et al. (2020a)** -- *Synthesizer: Rethinking Self-Attention in Transformer Models.* Dense attention without explicit dot-product. Moderate performance (avg 52.88), slow at longer sequences.
- **Zaheer et al. (2020)** -- *BigBird: Transformers for Longer Sequences.* Combines random, window, and global attention. Best overall LRA score (55.01) but nearly as slow as vanilla Transformer (1.1x at 4K).
- **Katharopoulos et al. (2020)** -- *Transformers Are RNNs: Fast Autoregressive Transformers with Linear Attention.* Kernel-based linear attention. 5.6x speedup, strong on Text (65.90) and Pathfinder (75.30), collapses on ListOps (16.13).
- **Choromanski et al. (2020b)** -- *Rethinking Attention with Performers.* FAVOR+ random feature approximation. Fastest model (5.7x), best on Pathfinder (77.05), but worst on ListOps (18.01).

### Benchmark Tasks and Datasets

- **Nangia & Bowman (2018)** -- *ListOps: A Diagnostic Dataset for Latent Tree Learning.* The original short-sequence ListOps task that LRA extends to 2K tokens for hierarchical reasoning evaluation.
- **Maas et al. (2011)** -- *Learning Word Vectors for Sentiment Analysis.* IMDb reviews dataset used for the byte-level text classification task.
- **Radev et al. (2013)** -- *The ACL Anthology Network Corpus.* Citation link dataset used for the byte-level document retrieval task.
- **Linsley et al. (2018)** -- *Learning Long-Range Spatial Dependencies with Horizontal Gated Recurrent Units.* Original Pathfinder challenge for spatial dependency learning, adapted by LRA for the Pathfinder and Path-X tasks.
- **Kim et al. (2020)** -- *Disentangling Neural Mechanisms for Perceptual Grouping.* Further development of the Pathfinder task used in LRA.
- **Krizhevsky (2009)** -- *Learning Multiple Layers of Features from Tiny Images.* CIFAR-10 dataset used for the image classification task.

### Attention Span and Language Modeling Analysis

- **Daniluk et al. (2017)** -- *Frustratingly Short Attention Spans in Neural Language Modeling.* Shows LSTM attention rarely extends beyond 7 words, motivating LRA's explicit long-range span requirement and the required attention span metric.
- **Rae & Razavi (2020)** -- *Do Transformers Need Deep Long-Range Memory?* Argues language modeling perplexity is dominated by short-range signal, supporting LRA's choice of non-LM tasks for evaluating long-range ability.

### Attention Visualization

- **Abnar & Zuidema (2020)** -- *Quantifying Attention Flow in Transformers.* Attention rollout method used for visualizing Pathfinder attention maps in the appendix (Appendix A.3.1).

### Survey

- **Tay et al. (2020c)** -- *Efficient Transformers: A Survey.* Comprehensive survey of efficient Transformer methods by the same authors, providing the taxonomy that motivates LRA's model selection.
