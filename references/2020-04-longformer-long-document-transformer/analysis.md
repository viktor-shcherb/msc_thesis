---
title: "Longformer: The Long-Document Transformer"
authors: "Beltagy, Peters, Cohan"
year: 2020
venue: "arXiv 2020"
paper_type: preprint
categories: ["attention-efficiency", "architecture"]
scope: ["long document processing", "O(n) attention", "pretrain-finetune for long context"]
benchmarks_used: ["text8", "enwik8", "wikihop", "triviaqa", "hotpotqa", "ontonotes-coref", "imdb-sentiment", "hyperpartisan", "arxiv-summarization"]
models_introduced: ["longformer-base", "longformer-large", "led-large"]
models_evaluated: ["roberta-base"]
key_claims:
  - id: C1
    claim: "Longformer's attention mechanism scales linearly with sequence length while achieving competitive or superior performance to full attention on downstream tasks"
    evidence: "Figure 1, Table 7, Table 8"
    status: supported
    scope: "encoder-only and encoder-decoder settings, up to 16K tokens"
  - id: C2
    claim: "Pretrained Longformer-base consistently outperforms RoBERTa-base across all six downstream tasks"
    evidence: "Table 7"
    status: supported
    scope: "base model size, six long-document tasks"
    magnitude: "+0.2 to +7.4 points across tasks"
  - id: C3
    claim: "Global attention is the single most important component — removing global attention and separate projections drops WikiHop accuracy by 8.3 points"
    evidence: "Table 10, Section 6.5"
    status: supported
    scope: "WikiHop development set, Longformer-base"
    magnitude: "8.3 point accuracy drop"
  - id: C4
    claim: "Copy initialization of position embeddings enables rapid convergence, reducing initial MLM BPC from 10.299 to 1.957"
    evidence: "Table 5, Section 5"
    status: supported
    scope: "base and large models, MLM pretraining"
    magnitude: "BPC from 10.299 to 1.957 (base), 8.738 to 1.597 (large)"
  - id: C5
    claim: "Small Longformer (41M params) achieves state-of-the-art BPC of 1.10 on text8 and 1.00 on enwik8"
    evidence: "Table 2"
    status: supported
    scope: "41M parameter small model, character-level LM"
    magnitude: "1.10 BPC text8, 1.00 BPC enwik8 (vs. prior best 1.11/1.02)"
  - id: C6
    claim: "Longformer-large achieves state-of-the-art on WikiHop (81.9 F1) and TriviaQA (77.3 F1) as of May 2020"
    evidence: "Table 8"
    status: supported
    scope: "large model, May 2020 leaderboards"
    magnitude: "+3.6 on WikiHop, +4.0 on TriviaQA over prior SOTA"
  - id: C7
    claim: "LED at 16K tokens slightly outperforms BigBird at 4K tokens on arXiv summarization despite no task-specific pretraining"
    evidence: "Table 11"
    status: supported
    scope: "arXiv summarization, LED-large at 16K vs. BigBird at 4K"
    magnitude: "R-2 +0.60, R-L +0.06 over BigBird"
  - id: C8
    claim: "Increasing LED input length from 1K to 16K tokens improves ROUGE-1 from 35.21 to 46.23 and ROUGE-2 from 11.54 to 19.62"
    evidence: "Figure 3"
    status: supported
    scope: "arXiv validation set, LED-large"
    magnitude: "ROUGE-1 +11.02, ROUGE-2 +8.08 from 1K to 16K tokens"
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Replaces O(n^2) full self-attention with sparse local+global attention while preserving the attention score computation (Eqn. 1)"
  - target: 2019-11-dark-secrets-of-bert
    type: complementary
    detail: "Cites Kovaleva et al.'s finding that BERT attention is predominantly local to motivate the sliding window design"
  - target: 2019-08-bert-attention-analysis
    type: complementary
    detail: "Cites Clark et al.'s finding of strong local bias in BERT attention heads to motivate copy initialization of position embeddings"
  - target: 2021-05-long-range-arena
    type: complementary
    detail: "LRA benchmarks efficient attention mechanisms including Longformer's sparse attention pattern"
  - target: 2022-12-scrolls-long-language-sequences
    type: complementary
    detail: "SCROLLS evaluates models on long-document understanding tasks that Longformer targets"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "ALiBi enables length extrapolation without additional long-sequence training, unlike Longformer which requires partial training on longer inputs"
  - target: 2023-12-landmark-attention-infinite-context
    type: complementary
    detail: "Landmark attention uses learned block retrieval via the attention mechanism, as an alternative to Longformer's fixed sparse attention patterns"
  - target: 2025-07-position-bias-transformers
    type: extended-by
    detail: "Theoretically analyzes the sliding-window attention mask: context still converges to the first token but at a slower rate governed by ceil((N-1)/(w-1)) (Theorem 4.2)"
  - target: 2025-04-effective-context-length-falls-short
    type: extended-by
    detail: "STRING combines Longformer's sliding window attention with shifted self-attention in its FlashAttention implementation for training-free context improvement"
  - target: 2020-04-compressive-transformer-pg19
    type: concurrent
    detail: "Contemporary approach to long-range attention; Longformer uses sparse local+global attention for bidirectional pretrain-finetune, while Compressive Transformer compresses old memories for autoregressive LM"
  - target: 2020-12-bigbird-sparse-attention
    type: concurrent
    detail: "Concurrent sparse attention work; BigBird adds random attention and provides theoretical proofs of universal approximation and Turing completeness"
  - target: 2024-08-gemma-2-technical-report
    type: extended-by
    detail: "Gemma 2 adopts interleaved local-global attention in decoder-only LLMs: alternating layers use 4096-token sliding window (local) and 8192-token span (global)"
  - target: 2025-10-kimi-linear-attention
    type: complementary
    detail: "Kimi Linear takes a different approach to O(n) attention: hybrid architecture interleaving linear attention (KDA) with full attention at 3:1 ratio, achieving 6× decoding speedup at 1M context while outperforming full attention on benchmarks"
  - target: 2022-12-flashattention
    type: complementary
    detail: "FlashAttention provides IO-aware exact attention with O(N) memory; orthogonal to Longformer's sparse attention — combining FlashAttention with Longformer's patterns yields efficient long-context implementations"
  - target: 2024-05-ring-attention-near-infinite-context
    type: complementary
    detail: "Ring Attention distributes exact full attention across devices for even longer contexts (up to 100M+ tokens), taking a different approach than Longformer's sparse attention patterns"
  - target: 2024-05-mamba-selective-state-spaces
    type: complementary
    detail: "Mamba takes a fundamentally different approach to O(n) complexity: replacing attention entirely with selective state space models rather than sparsifying attention patterns, achieving 5× faster inference while matching Transformer quality"
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: complementary
    detail: "RWKV uses channel-wise time decay for linear attention rather than Longformer's sparse local+global attention, achieving O(d) memory during inference at up to 14B parameters"
  - target: 2025-12-ttt-e2e-long-context
    type: complementary
    detail: "TTT-E2E uses sliding-window attention as its base architecture and adds test-time training on MLP weights for long-range context compression, achieving constant latency and full-attention-level scaling up to 128K"
open_questions:
  - question: "Can pretraining objectives beyond MLM further improve Longformer and LED?"
    addressed_by: null
  - question: "Can dilation be made compatible with continued pretraining from existing checkpoints?"
    addressed_by: null
  - question: "Would dedicated pretraining of LED (rather than just BART initialization) yield further improvements on seq2seq tasks?"
    addressed_by: null
  - question: "Can the global attention token selection be learned rather than manually specified per task?"
    addressed_by: null
  - question: "Can the approach extend to autoregressive decoder-only language models?"
    addressed_by: null
---

# Longformer: The Long-Document Transformer

**Authors:** Iz Beltagy, Matthew E. Peters, Arman Cohan (Allen Institute for AI)
**Date:** April 2020, arXiv:2004.05150

---

## Core Research Problem

Transformer self-attention has O(n^2) time and memory complexity in the sequence length n, making it infeasible to process long documents. BERT-style pretrained models are limited to 512 tokens, forcing practitioners to adopt task-specific workarounds: truncating documents, splitting them into overlapping chunks processed independently, or using two-stage retrieve-then-read pipelines. All of these approaches lose cross-partition information or introduce cascading errors.

Prior work on efficient Transformers addressed the quadratic cost but focused almost exclusively on autoregressive language modeling. Transformer-XL (Dai et al., 2019), Adaptive Span (Sukhbaatar et al., 2019), and Compressive Transformer (Rae et al., 2020) use left-to-right processing unsuitable for bidirectional pretrain-finetune transfer learning. Sparse attention models (Sparse Transformer by Child et al., 2019; Reformer by Kitaev et al., 2020; Routing Transformer by Roy et al., 2020) also limited their evaluation to language modeling. BP-Transformer (Ye et al., 2019) evaluated on machine translation but not in the pretrain-finetune setting. Blockwise attention (Qiu et al., 2019) pretrained and evaluated on QA, but only on short-context datasets (SQuAD, MRQA) where the 512-token limit is rarely exceeded (Table 1, Section 2).

The core challenge is: **how to build a Transformer with attention that scales linearly with sequence length while supporting the pretrain-finetune paradigm for long document NLP tasks including classification, question answering, coreference resolution, and summarization.**

---

## Problem Solutions

The paper introduces **Longformer**, a Transformer architecture with an attention mechanism that combines local windowed attention with task-motivated global attention, scaling linearly with sequence length. The solution rests on three components:

1. **Sliding window attention** provides each token with a local receptive field of size w. Stacking multiple layers gives top layers access to the entire input through a receptive field of l x w (where l is the number of layers), analogous to how CNNs build large receptive fields.

2. **Dilated sliding window attention** increases the receptive field to l x d x w without additional computation by introducing gaps of size d between attended positions, analogous to dilated CNNs.

3. **Global attention** on a small number of task-specific tokens (e.g., [CLS] for classification, question tokens for QA) allows the model to build full-sequence representations while keeping overall complexity O(n).

The paper further introduces **LED (Longformer-Encoder-Decoder)**, an encoder-decoder variant initialized from BART that uses Longformer's efficient attention in the encoder for long-document sequence-to-sequence tasks.

---

## Approach Details

### Method

Longformer sparsifies the full n^2 self-attention matrix by defining an attention pattern that specifies which pairs of input locations attend to one another. The standard attention computation is preserved:

> Attention(Q, K, V) = softmax(QK^T / sqrt(d_k)) V

but is restricted to a sparse pattern rather than computed over all pairs.

**Sliding Window.** Each token attends to 1/2 * w tokens on each side, where w is the window size (Figure 2b). The computation complexity is O(n * w), linear in n. With l layers and fixed w, the top-layer receptive field is l * w tokens (Section 3.1).

**Dilated Sliding Window.** The window has gaps of size dilation d between attended positions (Figure 2c). With fixed d and w across all layers, the receptive field is l * d * w. In multi-headed attention, different heads use different dilation configurations: some heads have no dilation (focusing on local context) while others have dilation (focusing on longer context) (Section 3.1).

**Global Attention.** A small number of pre-selected tokens receive global attention: they attend to all tokens in the sequence, and all tokens in the sequence attend to them. This operation is symmetric. For classification, global attention is assigned to [CLS]; for QA, to all question tokens. Since the number of global tokens is small and independent of n, the combined complexity of local and global attention remains O(n) (Section 3.1).

**Separate Linear Projections.** Two sets of projection matrices are used: Q_s, K_s, V_s for sliding window attention, and Q_g, K_g, V_g for global attention. The global projections are initialized from the sliding window projections. This separation is critical for downstream task performance (Section 3.1).

### Key Technical Components

**Increasing window sizes across layers.** For autoregressive language modeling, lower layers use small windows to capture local information efficiently, while higher layers use larger windows for richer representation. This configuration outperforms both fixed and decreasing window size arrangements (Table 4: increasing w yields 1.21 dev BPC vs. 1.24 for decreasing w and 1.23 for fixed w on text8 at 150K steps, Section 4.2.2).

**Dilation on a subset of heads.** Only 2 attention heads per layer use dilation, with dilation values increasing across layers: 0 for lower layers, increasing to 3 for the highest layers. This preserves local context capacity while enabling direct long-range attention (Table 4: dilation on 2 heads yields 1.20 BPC vs. 1.21 without dilation on text8, Section 4.2.2). Specific dilation configuration for the small model: 0 (layers 0--5), 1 (layers 6--7), 2 (layers 8--9), 3 (layers 10--11) (Table 12).

**Position embedding initialization by copying.** To extend RoBERTa's 512 learned absolute position embeddings to 4,096 positions, the original 512 embeddings are copied 8 times. This preserves the learned local attention bias where neighboring tokens have similar embeddings (Clark et al., 2019), enabling rapid convergence during continued pretraining. Without copy initialization, MLM BPC starts at 10.299 vs. 1.957 with copying for the base model (Table 5, Section 5).

**Staged training for language modeling.** Training starts with short sequences and small windows, then doubles both the window size and sequence length while halving the learning rate at each phase. Five phases, starting at sequence length 2,048 and ending at 23,040, the GPU memory limit (Section 4.2, Table 12).

**Three implementation strategies.** (1) `Longformer-loop`: naive per-diagonal computation, memory efficient but slow, used for testing only. (2) `Longformer-chunks`: chunks Q and K into overlapping blocks of size w with overlap 1/2 * w, uses a single matrix multiplication, 2x memory overhead but fast; used for pretrain/finetune. (3) `Longformer-cuda`: custom CUDA kernel via TVM (Chen et al., 2018), fully featured with dilation support, most memory efficient, as fast as optimized full self-attention; used for character-level LM experiments (Section 3.2, Appendix A).

### Experimental Setup

**Character-level language modeling:**
- Datasets: text8 and enwik8 (100M characters each, 90M/5M/5M train/dev/test; Mahoney, 2009).
- Small model: 12 layers, 8 heads, 512 hidden size, 41M parameters (following Dai et al., 2019).
- Large model: 30 layers, 8 heads, 512 hidden size, 102M parameters (following Child et al., 2019).
- Position embeddings: relative, sinusoidal (Dai et al., 2019).
- Evaluation: sequences of length 32,256, overlapping with step 512, reporting on last 512 tokens (following Dai et al., 2019).
- Optimizer: AdamW, weight decay 0.01, gradient clipping 0.25.
- Mixed precision training (fp16/fp32) with attention in fp32 to avoid numerical instability.
- Hardware: 4 RTX8000 GPUs (small, 16 days), 8 RTX8000 GPUs (large, 13 days).

**Continued MLM pretraining:**
- Initialized from RoBERTa (Liu et al., 2019) checkpoint (base and large).
- Corpus: Books corpus (0.5B tokens) + English Wikipedia (2.1B tokens) + Realnews subset with docs > 1,200 tokens (1.8B tokens) + Stories corpus (2.1B tokens), totaling ~6.5B tokens (Table 13, Appendix C).
- Sequence length 4,096, batch size 64 (2^18 tokens per batch), 65K gradient updates.
- Maximum learning rate 3e-5, linear warmup of 500 steps, power-3 polynomial decay.
- Sliding window attention with w = 512 (matching RoBERTa's computational budget per layer).
- No dilation in the pretrained model — adding dilation hurt performance, likely incompatible with pretrained RoBERTa weights (footnote 6).

**Downstream tasks:**
- QA: WikiHop (Welbl et al., 2018), TriviaQA (Joshi et al., 2017, Wikipedia setting), HotpotQA (Yang et al., 2018, distractor setting).
- Coreference resolution: OntoNotes (Pradhan et al., 2012), using the coarse-to-fine model from Joshi et al. (2019).
- Classification: IMDB (Maas et al., 2011), Hyperpartisan news detection (Kiesel et al., 2019; 80/10/10 train/dev/test split, mean F1 across 5 seeds).
- Summarization (LED): arXiv summarization dataset (Cohan et al., 2018).
- Global attention assignment per task: [CLS] for classification; question tokens for TriviaQA; question tokens + answer candidates for WikiHop; question, paragraph title, and sentence tokens for HotpotQA; no global attention for coreference; first `<s>` token for LED encoder.
- Baseline: RoBERTa-base, breaking context into 512-token segments processed independently with activations concatenated.

### Key Results

**Character-level language modeling (BPC, lower is better):**

| Model | #Params | text8 Test | enwik8 Test |
|---|---|---|---|
| T12 (Al-Rfou et al., 2018) | 44M | 1.18 | 1.11 |
| Transformer-XL (Dai et al., 2019) | 41M | - | 1.06 |
| Reformer (Kitaev et al., 2020) | - | - | 1.05 |
| Adaptive Span (Sukhbaatar et al., 2019) | 38--39M | 1.11 | 1.02 |
| BP-Transformer (Ye et al., 2019) | 38--39M | 1.11 | 1.02 |
| **Longformer (small)** | **41M** | **1.10** | **1.00** |

| Model | #Params | enwik8 Test |
|---|---|---|
| Sparse Transformer (Child et al., 2019) | ~100M | 0.99 |
| Adaptive Span (Sukhbaatar et al., 2019) | 209M | 0.98 |
| Compressive (Rae et al., 2020) | 277M | 0.97 |
| Routing (Roy et al., 2020) | ~223M | 0.99 |
| **Longformer (large)** | **102M** | **0.99** |

- Longformer achieves state-of-the-art BPC on both text8 (1.10) and enwik8 (1.00) among small models (Table 2).
- Large Longformer (102M) matches Sparse Transformer (~100M) at 0.99 BPC and is within 0.01--0.02 BPC of models with 2--3x more parameters (Table 3).

**Pretrained Longformer vs. RoBERTa (development sets):**

| Task | RoBERTa-base | Longformer-base | Metric |
|---|---|---|---|
| WikiHop | 72.4 | **75.0** | Accuracy |
| TriviaQA | 74.3 | **75.2** | F1 |
| HotpotQA | 63.5 | **64.4** | Joint F1 |
| OntoNotes | 78.4 | **78.6** | Avg F1 |
| IMDB | 95.3 | **95.7** | Accuracy |
| Hyperpartisan | 87.4 | **94.8** | F1 |

- Longformer-base consistently outperforms RoBERTa-base across all tasks (Table 7).
- Gains are largest on tasks requiring long context: +7.4 F1 on Hyperpartisan, +2.6 accuracy on WikiHop.
- Gains are smaller where local context suffices: +0.9 F1 on TriviaQA, +0.4 on IMDB, +0.2 on OntoNotes.

**Longformer-large leaderboard results (test sets, May 2020):**

| Task | Prior SOTA | Longformer-large |
|---|---|---|
| WikiHop | 78.3 | **81.9** |
| TriviaQA | 73.3 | **77.3** |
| HotpotQA | **74.2** | 73.2 |

- New state-of-the-art on WikiHop (+3.6) and TriviaQA (+4.0) (Table 8).
- On HotpotQA, second-best published result. Top models (HGN: 74.2 joint F1) use GNNs for entity graph reasoning, an orthogonal inductive bias. Longformer outperforms all non-GNN methods (Table 9).

**LED summarization (arXiv dataset, ROUGE scores):**

| Model | R-1 | R-2 | R-L |
|---|---|---|---|
| Discourse-aware (Cohan et al., 2018) | 35.80 | 11.05 | 31.80 |
| Pegasus (Zhang et al., 2020) | 44.21 | 16.95 | 38.83 |
| LED-large (seqlen: 4,096) | 44.40 | 17.94 | 39.76 |
| BigBird (seqlen: 4,096) | 46.63 | 19.02 | 41.77 |
| **LED-large (seqlen: 16,384)** | **46.63** | **19.62** | **41.83** |

- LED-large at 16K tokens slightly outperforms BigBird at 4K tokens, despite BigBird being initialized from Pegasus (a summarization-specific pretrained model) and using 16x more pretraining compute (Table 11).
- Increasing input length from 1K to 16K tokens improves ROUGE-1 from 35.21 to 46.23 and ROUGE-2 from 11.54 to 19.62 on the validation set (Figure 3).

### WikiHop Ablations

Table 10 isolates the contribution of each Longformer component on the WikiHop development set (all using Longformer-base, 5 epochs except where noted):

| Configuration | Accuracy | Delta |
|---|---|---|
| Longformer (seqlen: 4,096) | 73.8 | -- |
| Longformer (seqlen: 4,096, 15 epochs) | 75.0 | +1.2 |
| RoBERTa-base (seqlen: 512) | 72.4 | -1.4 |
| Longformer (seqlen: 512, n^2 attention) | 71.7 | -2.1 |
| Longformer (seqlen: 2,048) | 73.1 | -0.7 |
| Longformer (no MLM pretraining) | 73.2 | -0.6 |
| Longformer (no separate linear proj.) | 72.2 | -1.6 |
| Longformer (no linear proj., no global attn.) | 65.5 | -8.3 |
| Longformer (pretrain extra pos. embed. only) | 73.5 | -0.3 |

- **Global attention is the single most important component** (-8.3 without it) (Table 10).
- Separate projection matrices for global attention contribute 1.6 points.
- Longer sequences consistently help; halving from 4,096 to 2,048 costs 0.7 points.
- When configured identically to RoBERTa (512 tokens, full attention), Longformer performs slightly worse (71.7 vs. 72.4), confirming gains are not from additional pretraining but from longer context and the attention pattern.
- Freezing all RoBERTa weights and only training extra position embeddings yields 73.5, showing Longformer can learn long-range context during task-specific fine-tuning alone.

### MLM Pretraining Progression

Table 5 tracks the MLM BPC during continued pretraining:

| Configuration | base | large |
|---|---|---|
| RoBERTa (seqlen: 512) | 1.846 | 1.496 |
| Longformer (seqlen: 4,096, random pos. init) | 10.299 | 8.738 |
| + copy position embeddings | 1.957 | 1.597 |
| + 2K gradient updates | 1.753 | 1.414 |
| + 65K gradient updates | 1.705 | 1.358 |
| Longformer (train extra pos. embed. only) | 1.850 | 1.504 |

- Copy initialization reduces initial BPC from 10.299 to 1.957, close to RoBERTa's 1.846 (Table 5).
- 65K gradient updates of continued pretraining reduce BPC further to 1.705, demonstrating the model learns to better utilize longer context.
- Training only the extra position embeddings (freezing all RoBERTa weights) achieves 1.850 BPC, preserving original short-document performance.

---

## Limitations and Failure Modes

- **Fixed attention pattern.** Longformer's sliding window attention pattern is fixed at training time and does not adapt to content. Each head uses the same window size regardless of the input, unlike Adaptive Span (Sukhbaatar et al., 2019) which learns per-head span lengths (Section 2).

- **Dilation incompatible with continued pretraining.** Adding dilation to the pretrained model hurt performance, likely because the pretrained RoBERTa weights encode a non-dilated attention pattern. Dilation is only used for the from-scratch character-level LM experiments (footnote 6, Section 5).

- **Manual global attention token selection.** Global attention token selection is task-specific and manually specified, not learned. Each downstream task requires choosing which tokens get global attention (Section 3.1).

- **Sub-optimal chunked implementation.** The `Longformer-chunks` implementation used for pretrain/finetune consumes 2x optimal memory because it computes some zero values. The memory-optimal `Longformer-cuda` kernel is only used for character-level LM experiments (Section 3.2, Appendix A).

- **Encoder-only architecture.** The paper does not evaluate on autoregressive generation or decoder-only models. Longformer is encoder-only (or encoder-decoder in the LED variant); its applicability to causal language models used in modern LLMs is not explored.

- **HotpotQA underperformance vs. GNN methods.** On HotpotQA, Longformer-large (73.2 joint F1) underperforms HGN-large (74.2), which uses graph neural networks for entity reasoning, suggesting that long-context attention alone does not replace structured reasoning inductive biases for certain multi-hop tasks (Table 8, Table 9).

- **Limited pretraining of LED.** LED is initialized from BART with no additional pretraining. The authors note that "further improvements should be possible through pre-training of LED" (Section 7), but this is not explored.

---

## Conclusions

### Contributions

1. **Sparse attention with linear scaling enables long-document Transformers.** Combining sliding window attention with a small number of global attention tokens produces O(n) complexity while preserving the ability to build full-sequence representations through stacked layers (Section 3).

2. **Global attention is essential for downstream task performance.** Removing global attention and separate projections drops WikiHop accuracy by 8.3 points. The local sliding window builds contextual representations, but global tokens are required for the model to aggregate information across the entire sequence for prediction (Table 10, Section 6.5).

3. **Continued pretraining from existing checkpoints is practical and effective.** By initializing from RoBERTa and copying position embeddings, Longformer achieves strong performance with only 65K gradient updates of continued pretraining. Copy initialization is the key enabler, reducing initial BPC from 10.299 to 1.957 (Table 5, Section 5).

4. **State-of-the-art character-level language modeling.** Small Longformer (41M params) achieves new state-of-the-art on text8 (1.10 BPC) and enwik8 (1.00 BPC). Large Longformer (102M params) matches Sparse Transformer at 0.99 BPC on enwik8 with comparable parameter count (Tables 2--3).

5. **State-of-the-art on long document QA.** Longformer-large sets new state-of-the-art on WikiHop (81.9, +3.6) and TriviaQA (77.3, +4.0) as of May 2020, and achieves second-best on HotpotQA (73.2) with a simpler architecture than GNN-based top models (Tables 8--9).

6. **Encoder-decoder extension to generative tasks.** LED, initialized from BART with no additional pretraining, achieves state-of-the-art on arXiv summarization at 16K input tokens, slightly outperforming BigBird despite BigBird using 16x more pretraining compute and task-specific initialization (Table 11).

### Implications

1. **The pretrain-finetune paradigm extends to long documents without full retraining.** The copy initialization strategy for position embeddings enables efficient adaptation of pretrained models to longer contexts, establishing a template later adopted widely for context length extension. [Inference: this approach foreshadows position interpolation and related methods.]

2. **Efficient attention mechanisms should be evaluated beyond language modeling.** The paper demonstrates that most prior efficient Transformers were only evaluated on autoregressive LM, whereas the pretrain-finetune downstream evaluation reveals qualitatively different patterns (e.g., the critical role of global attention) (Table 1, Section 2).

3. **Longer input directly translates to better performance.** Both the downstream task ablations (4,096 vs. 512 tokens, Table 10) and the LED summarization experiments (1K vs. 16K, Figure 3) show monotonic improvements with input length, supporting the value of efficient attention mechanisms for practical NLP.

---

## Key Claims

1. **C1: Linear-scaling attention with competitive downstream performance.** Longformer's attention mechanism scales linearly with sequence length (O(n * w) for sliding window) while achieving competitive or superior performance to full O(n^2) attention on downstream tasks (Figure 1, Table 7, Table 8). Status: **supported**.

2. **C2: Consistent improvement over RoBERTa-base.** Pretrained Longformer-base outperforms RoBERTa-base on all six downstream tasks: WikiHop (+2.6), TriviaQA (+0.9), HotpotQA (+0.9), OntoNotes (+0.2), IMDB (+0.4), Hyperpartisan (+7.4) (Table 7). Status: **supported**.

3. **C3: Global attention is essential.** Removing global attention and separate projections drops WikiHop accuracy from 73.8 to 65.5 (-8.3 points). Removing only separate projections drops it to 72.2 (-1.6) (Table 10). Status: **supported**.

4. **C4: Copy initialization enables rapid convergence.** Copying RoBERTa's 512 position embeddings 8 times to initialize 4,096-position Longformer reduces initial MLM BPC from 10.299 to 1.957 (base) and from 8.738 to 1.597 (large) (Table 5). Status: **supported**.

5. **C5: State-of-the-art character-level LM.** Small Longformer (41M params) achieves 1.10 BPC on text8 and 1.00 BPC on enwik8, surpassing Adaptive Span (1.11/1.02) and BP-Transformer (1.11/1.02) (Table 2). Status: **supported**.

6. **C6: State-of-the-art on WikiHop and TriviaQA.** Longformer-large achieves 81.9 F1 on WikiHop (prior SOTA: 78.3) and 77.3 F1 on TriviaQA (prior SOTA: 73.3) as of May 2020 (Table 8). Status: **supported** (later surpassed by BigBird with 16x more pretraining compute, per footnote 9).

7. **C7: LED outperforms BigBird on arXiv summarization.** LED-large at 16K tokens achieves R-1/R-2/R-L of 46.63/19.62/41.83, slightly outperforming BigBird at 4K tokens (46.63/19.02/41.77) despite no task-specific pretraining (Table 11). Status: **supported**.

8. **C8: Longer input improves LED summarization monotonically.** Increasing LED input from 1K to 4K to 16K tokens improves ROUGE-1 from 35.21 to 44.48 to 46.23 and ROUGE-2 from 11.54 to 17.99 to 19.62 on the arXiv validation set (Figure 3). Status: **supported**.

---

## Open Questions

1. **Can pretraining objectives beyond MLM further improve Longformer and LED?** The paper explicitly lists this as future work (Section 8): "we would like to study other pretraining objectives, especially for LED." Not yet addressed by subsequent work in this directory.

2. **Can dilation be made compatible with continued pretraining from existing checkpoints?** Dilation hurt performance when added to the pretrained RoBERTa model (footnote 6). Retraining from scratch might be needed. Not addressed.

3. **Would dedicated pretraining of LED yield further improvements?** LED achieves state-of-the-art on arXiv summarization with zero additional pretraining beyond BART initialization. The authors note "further improvements should be possible through pre-training of LED" (Section 7). Not addressed.

4. **Can the global attention token selection be learned rather than manually specified per task?** The current design requires task-specific decisions about which tokens receive global attention. Not addressed.

5. **Can the approach extend to autoregressive decoder-only language models?** The paper evaluates only encoder-only (Longformer) and encoder-decoder (LED) architectures. The applicability to the decoder-only models that dominate modern LLM development is not explored. Not directly addressed, though the general long-context extension problem has been approached differently through position interpolation and related methods in later work.

---

## Core References and Why They Are Referenced

### Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer with O(n^2) self-attention that Longformer's sparse attention replaces. Longformer preserves the same attention score computation (Eqn. 1) but restricts it to a sparse pattern.

- **Devlin et al. (2019)** -- *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.* BERT's 512-token limit is the practical constraint that motivates Longformer. The paper follows BERT's pretrain-finetune paradigm and adapts BERT's QA model architecture for HotpotQA.

- **Liu et al. (2019)** -- *RoBERTa: A Robustly Optimized BERT Pretraining Approach.* Longformer is initialized from RoBERTa's released checkpoint and uses its tokenizer, training infrastructure, and hyperparameters. RoBERTa-base serves as the primary baseline for all downstream task comparisons.

### Direct Predecessors and Concurrent Work

- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* The most similar prior model, using dilated sliding windows of 8x8 blocks via BlockSparse. Longformer's custom CUDA kernel is more flexible and maintainable. Longformer's large model architecture (30 layers, 512 hidden) follows Child et al.'s configuration.

- **Sukhbaatar et al. (2019)** -- *Adaptive Attention Span in Transformers.* Longformer follows this work's strategy of using different window sizes across layers. Adaptive Span learns per-head span lengths, while Longformer uses manually configured fixed windows.

- **Dai et al. (2019)** -- *Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context.* Left-to-right approach with segment-level recurrence. Longformer's character-level LM implementation is based on the Transformer-XL codebase with the memory mechanism disabled. Transformer-XL is unsuitable for pretrain-finetune because it requires left-to-right processing.

- **Zaheer et al. (2020)** -- *BigBird: Transformers for Longer Sequences.* Contemporaneous work extending ETC with additional tasks including summarization. BigBird proves sparse Transformers are universal approximators. On arXiv summarization, BigBird at 4K tokens is compared directly with LED at 4K and 16K tokens. BigBird uses 16x more pretraining compute.

- **Ainslie et al. (2020)** -- *ETC: Encoding Long and Structured Inputs in Transformers.* Contemporaneous work using local + global attention similar to Longformer, but with relative position embeddings and CPC pretraining loss. ETC-large achieves 73.6 joint F1 on HotpotQA vs. Longformer's 73.2.

### Attention Analysis

- **Kovaleva et al. (2019)** -- *Revealing the Dark Secrets of BERT.* Referenced for demonstrating that BERT attention is predominantly local, motivating the sliding window design.

- **Clark et al. (2019)** -- *What Does BERT Look At? An Analysis of BERT's Attention.* Shows BERT attention heads have a strong learned bias toward attending to neighboring tokens, motivating the copy initialization strategy for position embeddings.

### Encoder-Decoder Initialization

- **Lewis et al. (2020)** -- *BART: Denoising Sequence-to-Sequence Pre-training.* LED is initialized from BART parameters. BART's 1K position embeddings are copied 16 times to support LED's 16K input length.

### Evaluation Benchmarks

- **Welbl et al. (2018)** -- *Constructing Datasets for Multi-Hop Reading Comprehension Across Documents.* Provides the WikiHop dataset, where Longformer-large achieves 81.9 accuracy.

- **Joshi et al. (2017)** -- *TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension.* Longformer-large achieves 77.3 F1 on the Wikipedia setting.

- **Yang et al. (2018)** -- *HotpotQA: A Dataset for Diverse, Explainable Multi-Hop Question Answering.* Longformer-large achieves 73.2 joint F1 (second-best published) using a simpler architecture than GNN-based top models.

- **Cohan et al. (2018)** -- *A Discourse-Aware Attention Model for Abstractive Summarization of Long Documents.* Provides the arXiv summarization dataset used to evaluate LED.

- **Mahoney (2009)** -- *Large Text Compression Benchmark.* Provides the text8 and enwik8 datasets for character-level language modeling evaluation.
