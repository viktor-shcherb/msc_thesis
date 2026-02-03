# Longformer: The Long-Document Transformer

**Authors:** Iz Beltagy, Matthew E. Peters, Arman Cohan (Allen Institute for AI)
**Date:** April 2020, arXiv:2004.05150

---

## Core Research Problem

Transformer-based models achieve state-of-the-art results across NLP tasks, but their self-attention mechanism has O(n^2) time and memory complexity in the sequence length n, making it infeasible to process long documents. BERT-style pretrained models are limited to 512 tokens, forcing practitioners to adopt task-specific workarounds: truncating documents, splitting them into overlapping chunks processed independently, or using two-stage retrieve-then-read pipelines. All of these approaches lose cross-partition information or introduce cascading errors.

Prior work on efficient Transformers (Transformer-XL, Adaptive Span, Compressive Transformer) focused on left-to-right autoregressive language modeling and did not explore the pretrain-finetune transfer learning setting that drives state-of-the-art results on downstream NLP tasks. Sparse attention models (Sparse Transformer, Reformer, Routing Transformer) addressed the quadratic cost but also limited their evaluation to language modeling. Blockwise attention (Qiu et al., 2019) explored QA but only on short-context datasets (SQuAD, MRQA) where the 512-token limit is rarely exceeded. The core challenge is: **how to build a Transformer with attention that scales linearly with sequence length while supporting the pretrain-finetune paradigm for long document NLP tasks including classification, question answering, coreference resolution, and summarization.**

---

## Problem Solutions

The paper introduces **Longformer**, a Transformer architecture with an attention mechanism that combines local windowed attention with task-motivated global attention, scaling linearly with sequence length. The solution rests on three components:

1. **Sliding window attention** provides each token with a local receptive field of size w. Stacking multiple layers gives top layers access to the entire input through a receptive field of l * w (where l is the number of layers), similar to how CNNs build large receptive fields.

2. **Dilated sliding window attention** increases the receptive field to l * d * w without additional computation by introducing gaps of size d between attended positions, analogous to dilated CNNs.

3. **Global attention** on a small number of task-specific tokens (e.g., [CLS] for classification, question tokens for QA) allows the model to build full-sequence representations while keeping overall complexity O(n).

---

## Approach Details

### Method

Longformer sparsifies the full n^2 self-attention matrix by defining an attention pattern that specifies which pairs of input locations attend to one another.

**Sliding Window.** Each token attends to 1/2 * w tokens on each side, where w is the window size. The computation complexity is O(n * w), linear in n. With l layers and fixed w, the top-layer receptive field is l * w tokens.

**Dilated Sliding Window.** The window has gaps of size dilation d between attended positions. With fixed d and w across all layers, the receptive field is l * d * w. In multi-head attention, different heads use different dilation configurations: some heads have no dilation (focusing on local context) while others have dilation (focusing on longer context).

**Global Attention.** A small number of pre-selected tokens receive global attention: they attend to all tokens in the sequence, and all tokens attend to them. This operation is symmetric. For classification, global attention is assigned to [CLS]; for QA, to all question tokens. Since the number of global tokens is small and independent of n, the combined complexity of local and global attention remains O(n).

**Separate Linear Projections.** Two sets of projection matrices are used: Q_s, K_s, V_s for sliding window attention, and Q_g, K_g, V_g for global attention. The global projections are initialized from the sliding window projections. This separation is critical for downstream task performance -- removing it drops WikiHop accuracy by 1.6 points (Table 10), and removing both global attention and separate projections drops it by 8.3 points.

### Key Technical Components

- **Increasing window sizes across layers.** For autoregressive language modeling, lower layers use small windows to capture local information efficiently, while higher layers use larger windows for richer representation. This configuration outperforms both fixed and decreasing window size arrangements (Table 4: increasing w yields 1.21 dev BPC vs. 1.24 for decreasing w and 1.23 for fixed w on text8).

- **Dilation on a subset of heads.** Only 2 attention heads per layer use dilation, with dilation values increasing across layers (0 for lower layers, 1--3 for higher layers). This preserves local context capacity while enabling direct long-range attention (Table 4: dilation on 2 heads yields 1.20 BPC vs. 1.21 without dilation).

- **Position embedding initialization by copying.** To extend RoBERTa's 512 learned position embeddings to 4,096 positions, the original 512 embeddings are copied 8 times. This preserves the learned local attention bias (neighboring tokens have similar embeddings) and enables rapid convergence during continued pretraining. Without copy initialization, MLM BPC starts at 10.299 vs. 1.957 with copying (Table 5).

- **Three implementation strategies.** (1) `Longformer-loop`: naive per-diagonal computation, memory efficient but slow, used for testing only. (2) `Longformer-chunks`: chunks Q and K into overlapping blocks of size w with overlap 1/2 * w, uses a single matrix multiplication, 2x memory overhead but fast; used for pretrain/finetune. (3) `Longformer-cuda`: custom CUDA kernel via TVM, fully featured (supports dilation), most memory efficient, as fast as optimized full self-attention; used for character-level LM experiments.

- **Staged training for language modeling.** Training starts with short sequences and small windows, then doubles both the window size and sequence length while halving the learning rate at each phase. This allows the model to learn local context first before utilizing longer context. Five phases, starting at sequence length 2,048 and ending at 23,040.

### Experimental Setup

**Character-level language modeling:**
- Datasets: text8 and enwik8 (100M characters each, 90M/5M/5M train/dev/test).
- Small model: 12 layers, 8 heads, 512 hidden size, 41M parameters.
- Large model: 30 layers, 8 heads, 512 hidden size, 102M parameters.
- Evaluation: sequences of length 32,256, overlapping with step 512, reporting on last 512 tokens.
- Hardware: 4 RTX8000 GPUs (small, 16 days), 8 RTX8000 GPUs (large, 13 days).

**Pretraining:**
- Continued MLM pretraining from RoBERTa checkpoint.
- Corpus: Books corpus + English Wikipedia + 1/3 Realnews (docs > 1,200 tokens) + 1/3 Stories corpus (~6.5B tokens total).
- Sequence length 4,096, batch size 64 (2^18 tokens), 65K gradient updates.
- Maximum learning rate 3e-5, linear warmup of 500 steps, power-3 polynomial decay.
- Two model sizes: base and large.
- Sliding window attention with w = 512 (matching RoBERTa's computational budget).

**Downstream tasks:**
- QA: WikiHop, TriviaQA (Wikipedia setting), HotpotQA (distractor setting).
- Coreference resolution: OntoNotes.
- Classification: IMDB, Hyperpartisan news detection.
- Summarization (LED): arXiv summarization dataset.

### Key Results

**Character-level language modeling (BPC, lower is better):**

| Model | #Params | text8 Test | enwik8 Test |
|---|---|---|---|
| T12 (Al-Rfou et al., 2018) | 44M | 1.18 | 1.11 |
| Transformer-XL (Dai et al., 2019) | 41M | - | 1.06 |
| Adaptive Span (Sukhbaatar et al., 2019) | 38M | 1.11 | 1.02 |
| BP-Transformer (Ye et al., 2019) | 39M | 1.11 | 1.02 |
| **Longformer (small)** | **41M** | **1.10** | **1.00** |

| Model | #Params | enwik8 Test |
|---|---|---|
| Sparse Transformer (Child et al., 2019) | ~100M | 0.99 |
| Adaptive Span (Sukhbaatar et al., 2019) | 209M | 0.98 |
| Compressive (Rae et al., 2020) | 277M | 0.97 |
| **Longformer (large)** | **102M** | **0.99** |

- Longformer achieves state-of-the-art BPC on both text8 (1.10) and enwik8 (1.00) among small models.
- Large Longformer (102M) matches Sparse Transformer (~100M) and is within 0.02 BPC of models with 2--3x more parameters.

**Pretrained Longformer vs. RoBERTa (development sets):**

| Task | RoBERTa-base | Longformer-base | Metric |
|---|---|---|---|
| WikiHop | 72.4 | **75.0** | Accuracy |
| TriviaQA | 74.3 | **75.2** | F1 |
| HotpotQA | 63.5 | **64.4** | Joint F1 |
| OntoNotes | 78.4 | **78.6** | Avg F1 |
| IMDB | 95.3 | **95.7** | Accuracy |
| Hyperpartisan | 87.4 | **94.8** | F1 |

- Longformer-base consistently outperforms RoBERTa-base across all tasks.
- Gains are largest on tasks requiring long context: +7.4 F1 on Hyperpartisan, +2.6 accuracy on WikiHop.
- Gains are smaller where local context suffices (TriviaQA, IMDB, OntoNotes).

**Longformer-large leaderboard results (test sets, May 2020):**

| Task | Prior SOTA | Longformer-large |
|---|---|---|
| WikiHop | 78.3 | **81.9** |
| TriviaQA | 73.3 | **77.3** |
| HotpotQA | **74.2** | 73.2 |

- New state-of-the-art on WikiHop (+3.6) and TriviaQA (+4.0).
- On HotpotQA, second-best published result; top models use GNNs for entity graph reasoning, an orthogonal inductive bias.

**LED summarization (arXiv dataset, ROUGE scores):**

| Model | R-1 | R-2 | R-L |
|---|---|---|---|
| Pegasus (Zhang et al., 2020) | 44.21 | 16.95 | 38.83 |
| BigBird (seqlen: 4,096) | 46.63 | 19.02 | 41.77 |
| LED-large (seqlen: 4,096) | 44.40 | 17.94 | 39.76 |
| **LED-large (seqlen: 16,384)** | **46.63** | **19.62** | **41.83** |

- LED-large at 16K tokens slightly outperforms BigBird at 4K tokens, despite BigBird being initialized from Pegasus (a summarization-specific pretrained model) and using 16x more pretraining compute.
- Increasing input length from 1K to 16K tokens improves ROUGE-1 from 35.21 to 46.23 and ROUGE-2 from 11.54 to 19.62.

### WikiHop Ablations

Table 10 isolates the contribution of each Longformer component:

| Configuration | Accuracy | Delta |
|---|---|---|
| Longformer (seqlen: 4,096) | 73.8 | - |
| RoBERTa-base (seqlen: 512) | 72.4 | -1.4 |
| Longformer (seqlen: 512, n^2 attention) | 71.7 | -2.1 |
| Longformer (seqlen: 2,048) | 73.1 | -0.7 |
| Longformer (no MLM pretraining) | 73.2 | -0.6 |
| Longformer (no separate linear proj.) | 72.2 | -1.6 |
| Longformer (no linear proj., no global attn.) | 65.5 | -8.3 |

- Global attention is the single most important component (-8.3 without it).
- Separate projection matrices for global attention contribute 1.6 points.
- Longer sequences consistently help; halving from 4,096 to 2,048 costs 0.7 points.
- When configured identically to RoBERTa (512 tokens, full attention), Longformer performs slightly worse, confirming gains are not due to additional pretraining.

### Limitations

- Longformer's sliding window attention pattern is **fixed at training time** and does not adapt to content. Each head uses the same window size regardless of the input, unlike Adaptive Span (Sukhbaatar et al., 2019) which learns per-head span lengths.
- Dilation is **incompatible with continued pretraining from RoBERTa** -- adding dilation to the pretrained model hurt performance (footnote 6), likely because the pretrained weights encode a non-dilated attention pattern. Dilation is only used for the from-scratch character-level LM experiments.
- The **custom CUDA kernel** is required for the most efficient implementation and dilation support, but the `Longformer-chunks` implementation (used for pretrain/finetune) consumes 2x optimal memory.
- Global attention token selection is **task-specific and manually specified**, not learned. Each downstream task requires choosing which tokens get global attention.
- The paper does not evaluate on **autoregressive generation** or decoder-only models. Longformer is an encoder-only architecture (or encoder-decoder in the LED variant); its applicability to causal language models used in modern LLMs is not explored.

---

## Conclusions

1. **Sparse attention with linear scaling enables long-document Transformers.** Combining sliding window attention with a small number of global attention tokens produces O(n) complexity while preserving the ability to build full-sequence representations through stacked layers.

2. **Global attention is essential for downstream task performance.** Removing global attention and separate projections drops WikiHop accuracy by 8.3 points. The local sliding window alone builds contextual representations, but global tokens are required for the model to aggregate information across the entire sequence for prediction.

3. **Continued pretraining from existing checkpoints is practical and effective.** By initializing from RoBERTa and copying position embeddings, Longformer achieves strong performance with only 65K gradient updates of continued pretraining, a fraction of full pretraining cost. This establishes a template for extending pretrained models to longer contexts.

4. **Pretrained Longformer outperforms RoBERTa on long document tasks.** Consistent gains across QA, coreference resolution, and classification demonstrate that efficient long-context attention is a direct improvement over chunking-based approaches, setting new state-of-the-art on WikiHop and TriviaQA.

5. **Encoder-decoder variants extend the approach to generative tasks.** LED (Longformer-Encoder-Decoder), initialized from BART with no additional pretraining, achieves state-of-the-art on arXiv summarization at 16K input tokens, demonstrating that longer input processing directly improves output quality for summarization.

6. **Increasing input length yields consistent gains.** Both the downstream task experiments (4,096 vs. 512 tokens) and the LED summarization ablation (1K vs. 4K vs. 16K tokens) show that the ability to process more context translates directly to better performance, supporting the value of efficient attention mechanisms.

---

## Core References and Why They Are Referenced

### Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer with O(n^2) self-attention that Longformer's sparse attention replaces. Longformer uses the same attention score computation (Eqn. 1) but restricts it to a sparse pattern.
- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* BERT's 512-token limit is the practical constraint that motivates Longformer. The paper follows BERT's pretrain-finetune paradigm and uses BERT's QA model for HotpotQA span extraction.
- **Liu et al. (2019)** -- *RoBERTa: A Robustly Optimized BERT Pretraining Approach.* Longformer is initialized from RoBERTa's released checkpoint and uses its tokenizer, training infrastructure, and hyperparameters. RoBERTa-base serves as the primary baseline for all downstream task comparisons.

### Direct Predecessors and Concurrent Work

- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Sparse Transformer is the most similar prior model, using dilated sliding windows of 8x8 blocks via BlockSparse. Longformer's custom CUDA kernel is more flexible and maintainable. Longformer's large model architecture (30 layers, 512 hidden) follows Child et al.'s configuration.
- **Sukhbaatar et al. (2019)** -- *Adaptive Attention Span in Transformers.* Longformer follows this work's strategy of using different window sizes across layers. Adaptive Span learns per-head span lengths, while Longformer uses manually configured fixed windows.
- **Dai et al. (2019)** -- *Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context.* Left-to-right approach with segment-level recurrence. Longformer's character-level LM implementation is based on the Transformer-XL codebase. Transformer-XL is unsuitable for pretrain-finetune because its memory mechanism requires left-to-right processing.
- **Zaheer et al. (2020)** -- *BigBird: Transformers for Longer Sequences.* Contemporaneous work extending ETC with evaluation on additional tasks including summarization. BigBird proves that sparse Transformers are universal approximators. On arXiv summarization, BigBird at 4K tokens is compared directly with LED at 4K and 16K tokens. BigBird uses 16x more pretraining compute than Longformer.
- **Ainslie et al. (2020)** -- *ETC: Encoding Long and Structured Inputs in Transformers.* Contemporaneous work using local + global attention similar to Longformer, but with relative position embeddings and CPC pretraining loss. ETC-large achieves 73.6 joint F1 on HotpotQA vs. Longformer's 73.2.

### Models Used in Evaluation

- **Lewis et al. (2020)** -- *BART: Denoising Sequence-to-Sequence Pre-training.* LED is initialized from BART parameters. BART's 1K position embeddings are copied 16 times to support LED's 16K input length.

### Evaluation Benchmarks

- **Welbl et al. (2018)** -- *Constructing Datasets for Multi-Hop Reading Comprehension Across Documents.* Provides the WikiHop dataset, where Longformer-large achieves state-of-the-art 81.9 F1.
- **Joshi et al. (2017)** -- *TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension.* Longformer-large achieves state-of-the-art 77.3 F1 on the Wikipedia setting.
- **Yang et al. (2018)** -- *HotpotQA: A Dataset for Diverse, Explainable Multi-Hop Question Answering.* Longformer-large achieves 73.2 joint F1 (second-best published result) using a simpler architecture than GNN-based top models.
- **Cohan et al. (2018)** -- *A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents.* Provides the arXiv summarization dataset used to evaluate LED.
- **Mahoney (2009)** -- *Large Text Compression Benchmark.* Provides the text8 and enwik8 datasets for character-level language modeling evaluation.

### Attention Analysis

- **Kovaleva et al. (2019)** -- *Revealing the Dark Secrets of BERT.* Referenced for demonstrating the importance of local context in BERT's attention patterns, motivating the sliding window design.
- **Clark et al. (2019)** -- *What Does BERT Look At? An Analysis of BERT's Attention.* Shows BERT attention heads have a strong learned bias toward attending to neighboring tokens, motivating the copy initialization strategy for position embeddings.

#### Cross-References in Available Papers

- **Attention Is All You Need (`2017-12-attention-is-all-you-need`):** Longformer directly builds on the Transformer architecture from Vaswani et al. (2017), replacing the O(n^2) self-attention with a sparse attention pattern while preserving the same attention score formula. Vaswani et al.'s original encoder-decoder design is also the basis for the LED variant.
- **Revealing the Dark Secrets of BERT (`2019-11-dark-secrets-of-bert`):** Kovaleva et al. (2019) is cited to justify the sliding window design: BERT attention heads primarily attend to local context, supporting the hypothesis that a fixed local window captures most of the useful information per layer.
- **Attention Sinks (`2024-05-attention-sinks-streaming`):** Xiao et al. (2024) cite Longformer as introducing the window attention baseline that StreamingLLM improves upon. StreamingLLM shows that pure window attention collapses when initial tokens (attention sinks) are evicted, a failure mode not addressed in Longformer's design since Longformer uses bidirectional encoder attention rather than autoregressive decoding.
- **Lost in the Middle (`2024-02-lost-in-the-middle`):** Liu et al. (2024) reference Longformer as an efficient attention variant in their related work on how language models use long contexts.
- **SCROLLS (`2022-12-scrolls-long-language-sequences`):** Shaham et al. (2022) use LED as a baseline model in the SCROLLS benchmark, showing that LED without long-text pretraining underperforms, highlighting that Longformer's continued pretraining strategy is critical for strong downstream performance.
- **Landmark Attention (`2023-12-landmark-attention-infinite-context`):** Mohtashami and Jaggi (2023) cite Longformer as a representative sparse attention method that restricts attention flexibility through fixed patterns, contrasting it with their learned landmark-based retrieval approach.
- **Position Bias in Transformers (`2025-07-position-bias-transformers`):** The sliding-window attention mask introduced by Longformer is formally analyzed in Theorem 4.2, characterizing the position bias it induces in Transformer representations.
- **Effective Context Length Falls Short (`2025-04-effective-context-length-falls-short`):** Longformer's sliding window attention is one of the two attention patterns that the STRING method combines for efficient long-context processing.
