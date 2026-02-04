---
title: "Compressive Transformers for Long-Range Sequence Modelling"
authors: "Rae, Potapenko, Jayakumar, Hillier, Lillicrap"
year: 2020
venue: "ICLR 2020"
paper_type: conference-paper
categories: ["architecture", "attention-efficiency", "benchmarking"]
scope: ["memory compression", "long-range sequence modelling", "book-level language modelling"]
benchmarks_used: ["enwik8", "perplexity-wikitext103", "perplexity-pg19"]
models_introduced: ["compressive-transformer"]
models_evaluated: []
key_claims:
  - id: C1
    claim: "Compressive Transformer achieves 0.97 BPC on Enwik8, state-of-the-art at time of publication"
    evidence: "Table 4, Section 5.2"
    status: supported
  - id: C2
    claim: "Compressive Transformer achieves 17.1 perplexity on WikiText-103, 1.2 points over prior state-of-the-art TransformerXL"
    evidence: "Table 6, Section 5.3"
    status: supported
  - id: C3
    claim: "Convolution with attention-reconstruction loss is the best compression approach, achieving 0.973 BPC on Enwik8"
    evidence: "Table 5, Section 5.2"
    status: supported
  - id: C4
    claim: "Compression disproportionately improves rare word modelling: ~20% improvement for infrequent words vs 2.6% for frequent words over TransformerXL"
    evidence: "Table 7, Section 5.3"
    status: supported
  - id: C5
    claim: "Compressive Transformer achieves 33.6 test perplexity on PG-19 vs TransformerXL's 36.3"
    evidence: "Table 3, Section 5.1"
    status: supported
  - id: C6
    claim: "Attention weight increases at the transition from memory to compressed memory, indicating the network preserves salient information"
    evidence: "Figure 2, Section 5.5"
    status: supported
  - id: C7
    claim: "Reducing optimisation update frequency improves generalisation for long-context models, improving the TransformerXL baseline from 0.995 to 0.984 BPC on Enwik8"
    evidence: "Figure 3, Section 5.5.1"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Extends the Transformer with a secondary compressed memory that stores lossy representations of old activations evicted from the TransformerXL-style granular memory"
  - target: 2020-04-longformer-long-document-transformer
    type: concurrent
    detail: "Contemporary approach to long-range attention; Longformer uses sparse local+global attention patterns, while Compressive Transformer uses memory compression -- complementary strategies"
  - target: 2023-06-pi-positional-interpolation
    type: complementary
    detail: "PI uses PG-19 (introduced by this paper) as the primary long-sequence perplexity benchmark for evaluating context extension"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "StreamingLLM uses PG-19 for perplexity evaluation over sequences up to 4M tokens"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong uses PG-19 books as the background 'haystack' text for embedding reasoning facts"
  - target: 2023-12-landmark-attention-infinite-context
    type: complementary
    detail: "Landmark attention uses PG-19 for language modelling evaluation and addresses a similar problem of extending effective context via selective memory mechanisms"
open_questions:
  - question: "Can adaptive compression rates per layer improve performance, given that compression loss varies non-monotonically across layers?"
    addressed_by: null
  - question: "Can RNNs serve as effective compression functions, combining the benefits of learned sequential compression with the Compressive Transformer framework?"
    addressed_by: null
  - question: "How does the Compressive Transformer scale to modern large language models with billions of parameters?"
    addressed_by: null
  - question: "Can the attention-reconstruction compression loss be combined with dynamic attention spans for further improvements?"
    addressed_by: null
---

# Compressive Transformers for Long-Range Sequence Modelling

**Authors:** Jack W. Rae, Anna Potapenko, Siddhant M. Jayakumar, Chloe Hillier, Timothy P. Lillicrap (DeepMind; University College London)
**Date:** November 2019, arXiv:1911.05507; ICLR 2020

---

## Core Research Problem

The Transformer (Vaswani et al., 2017) stores the hidden activation of every time-step and integrates information via attention, representing the past with a tensor of depth x memory size x dimension -- an order of magnitude larger than an LSTM's hidden state. This granular memory yields strong performance but incurs two costs: the **computational cost** of attending to every time-step (O(n^2)) and the **storage cost** of preserving the full memory.

The TransformerXL (Dai et al., 2019) partially addresses this by maintaining a fixed-size FIFO memory of past activations and using relative positional embeddings, achieving a maximum temporal range of l x n (layers x memory size). However, when memory slots are exhausted, the oldest activations are simply **discarded**. This limits the model's effective temporal horizon: beyond l x n steps, all information is lost.

Sparse attention approaches (Child et al., 2019; Sukhbaatar et al., 2019) reduce the computational cost of attention by attending to roughly sqrt(n) locations, but they do not solve the storage problem -- all memories must still be kept around during training. Furthermore, sparse approaches often require custom sparse kernels for efficient implementation, which are incompatible with dense-linear-algebra accelerators such as TPUs.

Existing language modelling benchmarks also limit progress on long-range modelling. WikiText-103 articles average 3,600 words, and existing Transformer models appear able to exploit dependencies at this scale (Dai et al., 2019). The Billion Word Benchmark (Chelba et al., 2013) contains only individual sentences (average 27 words), and Penn Treebank articles average 355 words (Table 1, Section 4).

The core challenge is: **how to extend the temporal receptive field of Transformer-based sequence models beyond the TransformerXL's fixed memory window, while using simple dense linear-algebra components that are efficient on GPUs and TPUs, and how to benchmark such models on data with genuinely long-range dependencies.**

---

## Problem Solutions

The paper proposes the **Compressive Transformer**, an extension of the TransformerXL that compresses old memories into a secondary compressed memory instead of discarding them. The solution rests on three components:

1. **Two-tier memory hierarchy.** A granular FIFO memory (size n_m) stores recent activations exactly, as in TransformerXL. When the oldest n_s activations are evicted, they are compressed by a factor c into floor(n_s / c) compressed memory slots and stored in a secondary FIFO compressed memory (size n_cm).

2. **Learned compression via attention-reconstruction loss.** A compression function f_c (e.g., 1D convolution) maps n_s old memories to floor(n_s / c) compressed memories. An auxiliary loss trains the compression network to reconstruct the content-based attention over the original memories, preserving task-relevant information while discarding unattended details.

3. **PG-19 benchmark.** A new open-vocabulary language modelling benchmark derived from 28,752 Project Gutenberg books published before 1919, with an average length of 69K words and 10.9GB of text -- over double the size of existing LM benchmarks.

---

## Approach Details

### Method

The Compressive Transformer builds on the TransformerXL by adding a second memory tier. At each layer, the model maintains a memory m of size n_m and a compressed memory cm of size n_cm. The overall input sequence S = x_1, x_2, ..., x_{|S|} is split into fixed-size windows of size n_s. At each step (Algorithm 1, Section 3.1):

1. The input window is embedded: h^(1) = x * W_emb
2. For each layer i = 1, ..., l:
   - Concatenate compressed memory and memory: mem^(i) = concat(cm_t^(i), m_t^(i))
   - Compute multi-head attention over both memory types: a~^(i) = MHA(h^(i), mem_t^(i))
   - Apply skip connection and layer norm: a^(i) = LayerNorm(a~^(i) + h^(i))
   - Extract oldest memories: old_mem^(i) = m_t^(i)[:n_s]
   - Compress: new_cm^(i) = f_c^(i)(old_mem^(i)), mapping R^{n_s x d} to R^{floor(n_s/c) x d}
   - Update memory FIFO: m_{t+1}^(i) = concat(m_t^(i), h^(i))[-n_m:]
   - Update compressed memory FIFO: cm_t^(i) = concat(cm_t^(i), new_cm^(i))[-n_cm:]
   - Feedforward: h^(i+1) = LayerNorm(MLP(a^(i)) + a^(i))

The model attends over both memory types using the same attention mechanism, with the TransformerXL's relative positional embedding scheme (Section 3, Section 3.1).

### Key Technical Components

**Compression functions.** Four compression approaches are considered (Section 3.2):
- **Max/mean pooling:** kernel and stride set to compression rate c. No learned parameters.
- **1D convolution:** kernel and stride set to c. Learned parameters.
- **Dilated convolutions:** learned, with dilation.
- **Most-used:** memories sorted by average attention (usage); most-used are preserved. Inspired by the garbage collection mechanism in the Differentiable Neural Computer (Graves et al., 2016).

**Compression losses.** Three training strategies for the compression function (Section 3.2):
- **BPTT:** gradients from the task loss flow through long unrolls into the compression function. Requires doubling the unroll length and halving the batch size.
- **Auto-encoding loss:** L^ae = ||old_mem^(i) - g(new_cm^(i))||_2, where g is a learned decoder. This is a lossless objective that attempts to retain all information.
- **Attention-reconstruction loss:** reconstructs the content-based attention over old memories from the compressed memories (Algorithm 2). Specifically:

> L^attn = sum_i ||attn(h^(i), old_mem^(i)) - attn(h^(i), new_cm^(i))||_2

where attn(h, m) = sigma((hQ)(mK)^T)(mV) uses content-based attention without relative positional embeddings. Gradients from L^attn are stopped from flowing into the main Transformer network. This is a **lossy** objective: information that is no longer attended to can be discarded. This approach worked best (Table 5).

**Temporal range analysis.** The TransformerXL has maximum temporal range l x n with attention cost O(n_s^2 + n_s * n). The Compressive Transformer has maximum temporal range l x (n_m + c * n_cm) with attention cost O(n_s^2 + n_s * (n_m + n_cm)). Setting n_cm = n_m = n/2 and c = 3, the temporal range doubles compared to TransformerXL at identical attention cost (Section 3.3).

**Optimisation schedule.** Reducing the learning rate (or setting it to zero) during training degrades performance drastically for both TransformerXL and Compressive Transformer, due to distributional shift between training mode (with ongoing parameter updates) and evaluation mode. Instead of decaying the learning rate, the authors reduce the frequency of optimisation updates after 60,000 iterations (e.g., updates every 4 steps). This increases the effective batch size and improves generalisation. This technique improved the TransformerXL baseline from 0.995 to 0.984 BPC on Enwik8, matching the then state-of-the-art Adaptive Transformer (Figure 3, Section 5.5.1).

### Experimental Setup

**Enwik8 (character-level LM):**
- 100M bytes of unprocessed Wikipedia text; 90MB train, 5MB validation, 5MB test.
- 24-layer models, sequence window size 768.
- TransformerXL: memory size 2304 (training), 4096 (evaluation).
- Compressive Transformer: memory 768, compressed memory 1152, C = 3 (training); compressed memory 3072 (evaluation, swept over validation set).
- Embedding size 1024, 8 attention heads, MLP hidden size 3072.
- Compression rate sweep: 2, 3, 4; best reported per compression function (Table 5).

**WikiText-103 (word-level LM):**
- Closed-vocabulary benchmark from Wikipedia articles.
- 18-layer Compressive Transformer, compressed memory size = memory size = sequence window = 512.
- 64 TPU v3, batch size 2 per core (total 128); converged in ~12 hours.
- Single-layer 1D convolution, C = 4.
- Evaluation: memory 500, compressed memory 1500 (tuned on validation set).
- Embedding size 1024, 16 attention heads, MLP hidden size 4096, adaptive inputs (following Sukhbaatar et al., 2019).

**PG-19 (book-level word LM):**
- 28,602 training books, 50 validation, 100 test; 1.97B / 3.0M / 6.97M words (Table 2).
- 36-layer Compressive Transformer, window 512, memory and compressed memory both 512, C = 2.
- SubwordTextEncoder vocabulary of 32,000 tokens.
- 256 TPU v3 cores, total batch size 512; converged after ~100 billion subword tokens.
- Compared against 36-layer TransformerXL with window 512, attention window 1024.
- Word-level perplexity computed as e^{L/n_words} using exact word counts from Table 2.

**Speech (raw waveform):**
- 24.6 hours of 24kHz North American speech data.
- 20-layer Compressive Transformer vs 20-layer TransformerXL vs 30-layer WaveNet; all ~40M parameters.
- Window size 3840 (~80ms); memory 768 + 768 compressed for Compressive Transformer.
- 32 V100 GPUs, batch size 1 per core (total 32).

**Reinforcement learning:**
- IMPALA agent (Espeholt et al., 2018) on DMLab-30 rooms_select_nonmatching_object task.
- Compressive Transformer replaces LSTM as memory component.
- Memory and compressed memory sizes both 64; compression rates 1, 2, 4, 8 tested.
- Fixed learning rate 1.5e-5, entropy cost coefficient 2e-3; averaged over 3 seeds.

**All models:** optimised with Adam (Kingma and Ba, 2014), linear warmup from 1e-6 to 3e-4 with cosine decay, gradient norm clipping at 0.1. Parameter updates every 4 steps after 60,000 iterations (Section 5).

### Key Results

**Enwik8 (BPC, lower is better, Table 4):**

| Model | BPC |
|---|---|
| 64L Transformer (Al-Rfou et al., 2019) | 1.06 |
| 24L TransformerXL (Dai et al., 2019) | 0.99 |
| Sparse Transformer (Child et al., 2019) | 0.991 |
| Adaptive Transformer (Sukhbaatar et al., 2019) | 0.98 |
| 24L TransformerXL (authors' reproduction) | 0.98 |
| **24L Compressive Transformer** | **0.97** |

- State-of-the-art at time of publication. The 0.01 BPC improvement over the authors' TransformerXL baseline (0.98) comes from the compressed memory.

**Compression function comparison on Enwik8 (Table 5):**

| Compression fn | Compression loss | BPC |
|---|---|---|
| Conv | BPTT | 0.996 |
| Max Pooling | N/A | 0.986 |
| Conv | Auto-encoding | 0.984 |
| Mean Pooling | N/A | 0.982 |
| Most-used | N/A | 0.980 |
| Dilated conv | Attention | 0.977 |
| **Conv** | **Attention** | **0.973** |

- 1D convolution with attention-reconstruction loss is the best combination (0.973 BPC).
- The attention-reconstruction (lossy) loss outperforms auto-encoding (lossless) loss: 0.973 vs 0.984 for convolution.
- BPTT alone (0.996) is worse than all auxiliary loss approaches, suggesting local compression objectives are more effective than long-range gradient flow for training the compression function.

**WikiText-103 (word-level perplexity, lower is better, Table 6):**

| Model | Valid. | Test |
|---|---|---|
| LSTM+Hebb. (Rae et al., 2018) | 29.0 | 29.2 |
| Transformer (Baevski and Auli, 2019) | - | 18.7 |
| 18L TransformerXL, M=384 (Dai et al., 2019) | - | 18.3 |
| 18L TransformerXL, M=1024 (authors' reproduction) | - | 18.1 |
| **18L Compressive Transformer, M=1024** | **16.0** | **17.1** |

- 1.0 perplexity improvement over the authors' TransformerXL (18.1 vs 17.1), and 1.2 over the published TransformerXL result (18.3). This means the model places ~5% higher probability on the correct word.
- With naive dynamic evaluation (one epoch of continued training on test set): 16.1 perplexity, slightly better than Krause et al. (2019)'s 16.4 with more sophisticated dynamic evaluation.

**WikiText-103 perplexity by word frequency (Table 7):**

| Frequency | LSTM* | TransformerXL | Compressive Transformer | Relative gain over TXL |
|---|---|---|---|---|
| > 10K | 12.1 | 7.8 | 7.6 | 2.6% |
| 1K--10K | 219 | 61.2 | 55.9 | 9.5% |
| 100--1K | 1,197 | 188 | 158 | 21% |
| < 100 | 9,725 | 1,123 | 937 | 19.9% |
| All | 36.4 | 18.1 | 17.1 | 5.8% |

- Compression disproportionately improves modelling of rare words: ~20% improvement for words appearing fewer than 1,000 times in training, vs 2.6% for words appearing more than 10,000 times.
- 10x improvement in modelling rare words (< 100 occurrences) over the prior state-of-the-art LSTM (9,725 vs 937).

**PG-19 (word-level perplexity, Table 3):**

| Model | Valid. | Test |
|---|---|---|
| 36L TransformerXL | 45.5 | 36.3 |
| **36L Compressive Transformer** | **43.4** | **33.6** |

- 2.7 perplexity improvement on test set (36.3 vs 33.6). The domain is challenging despite the dataset size.

**Compressed memory size vs performance (Supplementary Tables 8--9):**

| Compressed Memory Size | Enwik8 BPC | WikiText-103 PPL |
|---|---|---|
| 256 / 512 | 1.01 | 18.2 |
| 512 / 512 | - | 17.9 |
| 1024 / 1024 | 0.99 | 17.6 |
| 2048 / 1536 | 0.98 | **17.1** |
| 3072 / 2048 | **0.97** | 17.7 |
| 4096 / - | 1.00 | - |

- Performance is non-monotonic with compressed memory size: too large a compressed memory degrades performance (Enwik8: 1.00 at 4096; WikiText-103: 17.7 at 2048), suggesting an optimal compression horizon exists.

### Attention Analysis

Attention weights averaged over 20,000 Enwik8 sequences show an **increase** in attention at the transition from regular memory to compressed memory (Figure 2, Section 5.5). This goes against the expected trend of older memories being accessed less frequently, and provides evidence that the network learns to preserve salient information in the compressed representation.

### Speech and RL Results

**Speech modelling (Section 5.6):** The Compressive Transformer with C = 4 outperforms the TransformerXL and maintains a slim advantage over WaveNet in test NLL at 400K training iterations (Figure 4). However, models were trained for only one week, and full convergence was not reached.

**Reinforcement learning (Section 5.7):** On the DMLab-30 rooms_select_nonmatching_object task, agents with compression rate 4 achieve human-level performance. Compression rate 1 (no compression, equivalent to standard memory) fails to learn the task to the same proficiency. Learning speed and stability increase proportionally with compression rate up to 4 (Figure 5).

### Layer Compressibility

The attention-reconstruction compression loss varies across layers but does not follow a monotonic trend with depth. The first layer is highly compressible. Word-level compression loss (WikiText-103) is approximately one order of magnitude higher than character-level compression loss (Enwik8). Some non-contiguous layer pairs (e.g., layers 4 & 6, 5 & 7) have very similar compression loss, suggesting information routing via skip connections (Section 5.4, Supplementary Figure 6).

---

## Limitations and Failure Modes

- **Additional complexity for short-range tasks.** The authors acknowledge that "if the task one wishes to solve does not contain long-range reasoning then the Compressive Transformer is unlikely to provide additional benefit" (Section 6).

- **Meta-learning artefact during training.** Reducing the learning rate during training causes drastic performance degradation for both TransformerXL and Compressive Transformer. This distributional shift between training (with ongoing parameter updates) and evaluation mode is an undesirable property that requires the optimisation schedule workaround of reducing update frequency (Section 5.5.1, Figure 3).

- **Non-monotonic performance with compressed memory size.** Performance degrades when the compressed memory is too large (Enwik8: 1.00 BPC at size 4096 vs 0.97 at 3072; WikiText-103: 17.7 at 2048 vs 17.1 at 1536), requiring careful tuning of this hyperparameter (Supplementary Tables 8--9).

- **Speech experiments not converged.** The speech modelling comparison against WaveNet was conducted with only one week of training (32 V100 GPUs), and the authors note that "it would be advantageous to continue training until full convergence -- before definitive conclusions are made" (Section 5.6).

- **Single RL task.** The reinforcement learning evaluation uses only one memory task (rooms_select_nonmatching_object). The generalisability of compressed memory for RL is not established (Section 5.7).

- **Autoregressive only.** The paper evaluates only autoregressive language models. The applicability of the compression mechanism to bidirectional or encoder-decoder architectures is not explored. The Compressive Transformer's memory system is inherently left-to-right, making it unsuitable for the pretrain-finetune paradigm used by BERT and Longformer.

- **Compression introduces hyperparameters.** The approach adds several hyperparameters beyond TransformerXL: compression rate c, compressed memory size n_cm, choice of compression function, and choice of auxiliary loss. The optimal settings differ across tasks (c = 2 for PG-19, c = 3 for Enwik8, c = 4 for WikiText-103 and speech).

---

## Conclusions

### Contributions

1. **Compressed memory extends temporal range without increasing attention cost.** By compressing old memories instead of discarding them, the Compressive Transformer achieves a maximum temporal range of l x (n_m + c x n_cm) at the same attention cost as a TransformerXL with memory n_m + n_cm. With n_cm = n_m = n/2 and c = 3, this doubles the temporal range (Section 3.3).

2. **State-of-the-art character-level language modelling.** The 24-layer Compressive Transformer achieves 0.97 BPC on Enwik8, surpassing the prior state-of-the-art Adaptive Transformer (0.98 BPC) with a simpler architecture that requires only dense linear algebra (Table 4).

3. **State-of-the-art word-level language modelling.** The 18-layer Compressive Transformer achieves 17.1 perplexity on WikiText-103, a 1.2-point improvement over the published TransformerXL result (18.3) (Table 6).

4. **Attention-reconstruction loss is the most effective compression training signal.** This lossy objective (0.973 BPC) outperforms lossless auto-encoding (0.984 BPC), parameter-free pooling (0.982 BPC for mean), and direct BPTT (0.996 BPC) (Table 5).

5. **Compression disproportionately improves rare word modelling.** On WikiText-103, the Compressive Transformer improves modelling of infrequent words (< 100 training occurrences) by 19.9% over TransformerXL, compared to only 2.6% for frequent words (> 10K occurrences) (Table 7).

6. **PG-19 benchmark for long-range language modelling.** The paper introduces PG-19, an open-vocabulary benchmark of 28,752 books (10.9GB, average 69K words) -- over double the size of existing LM benchmarks -- with the first baselines: TransformerXL at 36.3 and Compressive Transformer at 33.6 test perplexity (Tables 1--3).

7. **Cross-modal applicability.** The Compressive Transformer is effective beyond text: it outperforms TransformerXL on raw speech waveform modelling and achieves human-level performance as a memory module in an RL agent (Figures 4--5).

### Implications

1. **Lossy compression of past activations is a viable alternative to sparse attention.** Unlike sparse attention approaches that require custom kernels, compression uses simple dense operations (convolutions) that are efficient on GPUs and TPUs. This suggests that granular short-term memory combined with coarser long-term memory may be a general design principle for sequence models. [Inference: this two-tier memory hierarchy anticipates later work on memory-augmented and streaming Transformers.]

2. **Rare word modelling as a diagnostic for long-range memory.** The disproportionate improvement on rare words suggests that rare words benefit more from distant context, and that frequency-stratified perplexity is a useful diagnostic for evaluating memory mechanisms (Table 7).

3. **Book-length text demands new benchmarks.** WikiText-103 articles (3,600 words average) are within reach of existing Transformer memory windows. PG-19's 69K-word average requires genuinely long-range modelling, making it suitable for future long-context evaluation. [Inference: PG-19 has since become a standard evaluation corpus for context extension methods.]

---

## Key Claims

1. **C1: State-of-the-art on Enwik8.** The 24-layer Compressive Transformer achieves 0.97 BPC on Enwik8 (Table 4), surpassing the Adaptive Transformer (0.98 BPC) and matching the Sparse Transformer (0.99 BPC) with 1D convolution compression and attention-reconstruction loss. The result uses compressed memory size 3072 at evaluation time, swept over the validation set (Supplementary Table 8). Status: **supported**.

2. **C2: State-of-the-art on WikiText-103.** The 18-layer Compressive Transformer achieves 17.1 test perplexity on WikiText-103, improved from 17.6 with training-time memory sizes to 17.1 after tuning memory (500) and compressed memory (1500) over the validation set (Table 6, Supplementary Table 9). This is 1.2 points over the published TransformerXL (18.3) and 1.0 over the authors' stronger TransformerXL baseline (18.1). Status: **supported**.

3. **C3: Attention-reconstruction loss is the best compression approach.** Convolution with attention-reconstruction loss achieves 0.973 BPC vs 0.984 for auto-encoding, 0.982 for mean pooling, and 0.996 for BPTT-only training (Table 5). The lossy objective allows the compression network to discard information no longer attended to. Status: **supported**.

4. **C4: Compression disproportionately improves rare word modelling.** On WikiText-103, the Compressive Transformer improves over TransformerXL by 2.6% for words with > 10K training occurrences, 9.5% for 1K--10K, 21% for 100--1K, and 19.9% for < 100 occurrences (Table 7). Status: **supported**.

5. **C5: Compressive Transformer outperforms TransformerXL on PG-19.** The 36-layer Compressive Transformer achieves 33.6 test perplexity vs 36.3 for the matched TransformerXL, a reduction of 2.7 perplexity points on this book-level benchmark (Table 3). Status: **supported**.

6. **C6: Compressed memory receives non-trivial attention.** Average attention weights over 20,000 Enwik8 sequences show an increase at the memory-to-compressed-memory boundary, against the expected decay trend. This indicates the network learns to preserve and retrieve salient information from compressed memory (Figure 2). Status: **supported**.

7. **C7: Reducing update frequency improves generalisation.** Applying parameter updates every 4 steps after 60,000 iterations improves the TransformerXL baseline on Enwik8 from 0.995 to 0.984 BPC, matching the Adaptive Transformer without any architectural change (Figure 3, Section 5.5.1). Status: **supported**.

---

## Open Questions

1. **Can adaptive compression rates per layer improve performance?** The compression loss varies non-monotonically across layers (Supplementary Figure 6), suggesting different layers may benefit from different compression rates. The authors note this as a future direction (Section 6). Not addressed by subsequent work in this directory.

2. **Can RNNs serve as effective compression functions?** The authors suggest RNNs as potential compressors (Section 6), which could combine learned sequential compression with the Compressive Transformer framework. Not addressed.

3. **How does the Compressive Transformer scale to modern LLMs?** The largest model tested has 277M parameters (36 layers on PG-19). The applicability to models with billions of parameters is unknown. Not directly addressed, though subsequent work has moved to different approaches for long-context modelling (position interpolation, context extension).

4. **Can the attention-reconstruction loss be combined with dynamic attention spans?** The paper notes compatibility with Sukhbaatar et al. (2019)'s adaptive attention spans as a future direction (Section 2). Not addressed.

---

## Core References and Why They Are Referenced

### Architectural Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture that stores all past activations and integrates them via multi-head attention. The Compressive Transformer inherits this attention mechanism but adds compressed memory to extend temporal range.

- **Dai et al. (2019)** -- *Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context.* The direct predecessor. The Compressive Transformer builds on TransformerXL's FIFO memory and relative positional embeddings, adding compression of evicted memories instead of discarding them. TransformerXL serves as the primary baseline across all experiments.

### Efficient Attention

- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Uses fixed sparse attention masks to attend to ~sqrt(n) locations. On Enwik8, the much larger attention window of 8,000 improves performance but does not significantly outperform a simpler TransformerXL with a smaller window. Sparse Transformer still requires keeping all memories and custom sparse kernels.

- **Sukhbaatar et al. (2019)** -- *Adaptive Attention Span in Transformers.* Learns per-head attention span lengths, achieving prior state-of-the-art on Enwik8 (0.98 BPC). The authors note this idea could be combined with compression but is not efficient on dense-linear-algebra accelerators due to dynamic and sparse computation requirements.

### Memory Systems

- **Graves et al. (2016)** -- *Hybrid Computing Using a Neural Network with Dynamic External Memory (DNC).* The "most-used" compression scheme is inspired by the DNC's garbage collection mechanism, where low-usage memories are erased.

- **Rae et al. (2016)** -- *Scaling Memory-Augmented Neural Networks with Sparse Reads and Writes.* Prior work by the first author on sparse access mechanisms for memory-augmented networks.

### Language Modelling Benchmarks

- **Merity et al. (2016)** -- *Pointer Sentinel Mixture Models.* Introduces WikiText-103, the word-level LM benchmark where the Compressive Transformer achieves 17.1 perplexity.

- **Chelba et al. (2013)** -- *One Billion Word Benchmark.* Sentence-level LM benchmark (average 27 words) that does not stress long-range modelling, motivating the need for PG-19.

- **Hutter (2012)** -- *The Human Knowledge Compression Contest.* Provides Enwik8 (100M bytes of Wikipedia), the character-level LM benchmark where the Compressive Transformer achieves 0.97 BPC.

### Speech and RL Baselines

- **van den Oord et al. (2016)** -- *WaveNet: A Generative Model for Raw Audio.* State-of-the-art speech synthesis model used as the baseline for the speech modelling experiments. The Compressive Transformer shows competitive NLL with a trend toward lower likelihood at 400K steps.

- **Espeholt et al. (2018)** -- *IMPALA: Scalable Distributed Deep-RL.* The RL agent framework in which the Compressive Transformer replaces the LSTM memory component for the object matching task.
