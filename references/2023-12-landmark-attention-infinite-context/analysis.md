# Random-Access Infinite Context Length for Transformers

**Authors:** Amirkeivan Mohtashami, Martin Jaggi (EPFL)
**Date:** December 2023, NeurIPS 2023 (arXiv:2305.16300)

---

## Core Research Problem

Standard Transformer attention allows each token to access the representation of any other token in the sequence, but this flexibility comes with quadratic computational cost and memory footprint in the sequence length, limiting the context that can be processed. Prior approaches to overcoming this limit fall into two categories, each with fundamental drawbacks:

1. **Recurrent memory methods** (e.g., Transformer-XL, Memory Transformers, Infinite Memory Transformers) compress past context into a fixed-size memory state. This sacrifices the **random-access flexibility** of attention -- the model can no longer attend to specific tokens from the past, only to a lossy summary. Mu et al. (2024) -- *Learning to Compress Prompts with Gist Tokens* -- demonstrate this concretely: gist tokens trained to summarize prompts fail to remember specific details that must be copied into the output.

2. **Retrieval-augmented methods** (e.g., REALM, Atlas, kNN-LM) use a separate retriever module to find relevant documents from a knowledge base. The retriever is not fully compatible with the model's own attention mechanism, cannot easily be updated for fresh long input data, and may fail to retrieve what the model's attention would actually find useful.

3. **Approximate and sparse attention methods** (e.g., Longformer, BigBird, Performer, Reformer, Linformer) reduce attention cost but significantly restrict which tokens can be attended to, using fixed patterns (local windows, random subsets, global tokens) or heuristic reductions (max-pooling for block representations in Combiner) that limit the current token's control over attention weights.

The core challenge is: **how to enable Transformers to access arbitrarily long contexts while retaining the random-access flexibility of full attention, without requiring a separate retrieval mechanism or compressing past context into lossy summaries.**

---

## Problem Solutions

The paper proposes **Landmark Attention**, a method that uses special "landmark" tokens inserted between fixed-size blocks of the input to act as learned gates for block-level retrieval directly through the attention mechanism.

1. **Landmark tokens as block representatives.** A new special token is inserted after every `ℓ_block` tokens. The model is trained so that the key vector of each landmark token becomes a representative for its block: a high attention score to any token inside a block leads to a high attention score to the block's landmark.
2. **Grouped Softmax for gated attention.** A modified softmax function (Grouped Softmax) trains the model to use landmark attention scores as multiplicative gates for within-block token attention, creating a two-level retrieval: first select relevant blocks via landmarks, then attend to tokens within selected blocks.
3. **Cache-based inference at arbitrary lengths.** At inference, the input is processed in chunks. A cache stores key-value vectors for all previous blocks. Only landmark key vectors need to remain in fast memory; block contents can be offloaded to CPU/disk and loaded on demand. The top-k most relevant blocks are retrieved per token per head per layer, enabling inference at context lengths far exceeding the training length.

---

## Approach Details

### Method

The input text is preprocessed by inserting a landmark token after every `ℓ_block` tokens. Training proceeds with standard batching over windows of `ℓ_seq` tokens.

Let `p_i` denote the index of the landmark token corresponding to the i-th token's block. If the last block is incomplete (no landmark), `p_i := ℓ_seq`. If the i-th token is itself a landmark, `p_i := i`.

**Grouped Softmax.** Given a vector `v ∈ R^ℓ_seq` and a group index `g ∈ N^ℓ_seq`, Grouped Softmax applies softmax separately within each group:

> σ_G(v, g)_x := exp(v_x) / Σ_{y: g_y = g_x} exp(v_y)

Using `g = 1` for all elements recovers standard softmax.

**Grouping scheme.** When computing attention for the i-th token, the grouping `G_i,j` is:

> G_{i,j} := p_j if p_j ≠ j (normal tokens grouped by their block)
> G_{i,j} := -1 if p_i = j (current block's landmark is ignored)
> G_{i,j} := p_i if p_i ≠ j ∧ p_j = j (other blocks' landmarks placed in i-th token's group)

This grouping ensures: (a) normal tokens within a block share a softmax group, (b) landmark tokens for other blocks compete in the same softmax group as tokens in the current block, and (c) the current block's own landmark is excluded.

**Attention weights.** After computing `S_{i,j} := GroupedSoftmax(Q_i^T K / √d_head, G_i)`, the final attention weights are:

> AttWeight(Q, K)_{i,j} := 0 if p_j = j (landmark tokens receive zero final weight)
> AttWeight(Q, K)_{i,j} := S_{i,j} if G_{i,j} = G_{i,i} ∧ p_j ≠ j (same-group tokens: direct weight)
> AttWeight(Q, K)_{i,j} := S_{i,j} · S_{i,p_j} if G_{i,j} ≠ G_{i,i} ∧ p_j ≠ j (other-group tokens: gated by landmark)

Attention weights sum to one under this scheme. The key property is that **attending to tokens in other blocks is gated by the attention score to their landmark token**. Since landmarks and current-block tokens share a softmax group, the model must trade off between attending to its local context and retrieving from other blocks.

### Key Technical Components

**Stingy position mapping.** Transformers cannot extrapolate to positional indices beyond those seen during training. To handle arbitrarily long contexts at inference, the paper uses an approximate position mapping scheme. A prefix segment of length `(k+1) · (ℓ_block + 1)` is allocated before the current chunk. The latest k cached blocks are mapped to their corresponding positions within the last k slots of this prefix. All older blocks are mapped to the position of the (k+1)-th last block. Retrieved blocks are then distributed across the prefix respecting their relative order. This allows the model to use accurate positional information for the k most recent blocks while collapsing older blocks to approximate positions. The scheme uses RoPE (Su et al.) which adds position information to key and query vectors just before computing attention, enabling position-free storage in the cache.

**Positional augmentation (Appendix E).** To improve extrapolation, the authors propose inserting random positional jumps (between 1 and `p_jump`) after each landmark token during training. With `p_jump = 100` and 10-11 landmarks per input (training length 512), the model can extrapolate to ~1600 tokens, compared to ~1024 tokens with standard positional encoding.

**Context Miss Token (CMT) (Appendix D).** A hierarchical extension where a special token at position -1 acts as a gate over landmark tokens themselves. By extending the grouping scheme so that some landmarks are controlled by CMT, the model learns to signal whether retrieval from memory is necessary. With a cutoff threshold of 0.3 on the CMT score, 57% of retrieval calls can be dropped with only 0.05 perplexity degradation (16.43 vs. 16.38 without cutoff on PG19).

**Retrieval granularity.** At the most permissive level, each token and each head can retrieve different blocks. Efficiency can be improved by merging scores across tokens (taking the maximum landmark score across all tokens in a chunk per head) or across heads (taking the maximum across heads). This reduces bandwidth for cache loading at a moderate perplexity cost.

### Experimental Setup

**Language modeling (from scratch).**

- Architecture: GPT-2-like, 12-layer decoder-only transformer, 8 heads, head dimension 128 (embedding dimension 1024), FFN hidden size 4096.
- Optimizer: AdamW with β_1 = 0.9, β_2 = 0.95, weight decay 0.001, base learning rate 0.002, 2% warmup, cosine scheduler to minimum learning rate 0.0004.
- Tokenizer: GPT-2 tokenizer.
- Training: 240K steps with ℓ_seq = 512, ℓ_block = 50. Effective batch size 128 via gradient accumulation and data-parallel training across 4 nodes. Mixed-precision bfloat16 on up to 4 NVIDIA A100 GPUs.
- Datasets: PG-19 (3.7B tokens, English books) and arXiv Math (5.6B tokens, cleaned arXiv math subset of proof-pile).
- Baseline: Transformer-XL with window size 256 (effective context 512), trained for 60K steps over segments of length 2048 (same total tokens as landmark method).

**Fine-tuning LLaMA 7B.**

- 15,000 steps with context length 512, using the sample subset of RedPajama.
- Evaluation: pass key retrieval task -- a randomly generated pass key (integer 1--50000) is hidden at a random position within a text padded with filler, and the model must generate the correct key. Averaged over 50 random prompts per context length.
- Inference: chunks of 250 tokens, top k = 4 retrieved blocks.
- For context lengths exceeding GPU memory (e.g., 32K), KV cache (except landmarks) is offloaded to CPU.

### Key Results

**Language modeling perplexity (PG-19):**

| Eval. Length | Method | ℓ_local | Blocks in Memory | k | Attention Size | PG19 PPL |
|---|---|---|---|---|---|---|
| 512 | Baseline | 512 | - | - | 512 | 16.12 |
| 512 | Baseline | 360 | - | - | 360 | 16.76 |
| 512 | Landmark | 250 | 10 | 2 | 360 | 16.23 |
| 2048 | Transformer-XL | 256 | - (XL cache 256) | - | 512 | 14.72 |
| 2048 | Landmark | 250 | 40 | 4 | 460 | 14.92 |
| 4096 | Transformer-XL | 256 | - (XL cache 256) | - | 512 | 14.55 |
| 4096 | Landmark | 250 | 80 | 4 | 470 | 14.72 |

- At eval length 512, landmark attention with ℓ_local = 250 and k = 2 (attending to 360 tokens total: 250 local + 10 landmarks + 100 retrieved) achieves 16.23 perplexity, close to the full-attention baseline at 512 tokens (16.12) and substantially better than the baseline truncated to 360 tokens (16.76).
- At eval length 2048, landmark attention (14.92 with k = 4) approaches Transformer-XL (14.72) despite being trained only on 512-token windows.
- At eval length 4096, landmark attention (14.72 with 80 blocks, k = 4) closes the gap further with Transformer-XL (14.55). The model continues to improve from 2048 to 4096 tokens, demonstrating effective utilization of longer contexts not seen during training.
- On arXiv Math, landmark attention achieves 3.18 perplexity at eval length 4096 with 80 blocks and k = 4, compared to 4.01 at eval length 512 -- a 20.6% reduction.

**Retrieval granularity (PG-19, eval length 2048, k = 4):**

| Per Head | Per Token | Perplexity |
|---|---|---|
| Yes | Yes | 14.92 |
| Yes | No | 15.10 |
| No | Yes | 15.04 |

- Restricting retrieval to vary only across heads (not tokens) costs 0.18 perplexity but substantially reduces the number of unique blocks loaded from cache (typically below 10 unique blocks out of 32 theoretically possible).
- Restricting to vary only across tokens (not heads) costs 0.12 perplexity.

**Fine-tuning LLaMA 7B -- pass key retrieval accuracy:**

| Context Length | Base LLaMA 7B | Landmark Fine-Tuned |
|---|---|---|
| ~2K (within training length) | ~100% | ~100% |
| ~5K | 0% | ~100% |
| ~10K | 0% | ~100% |
| ~32K | OOM | 98% |

- Base LLaMA 7B retrieves the pass key within and slightly beyond its 2048-token training context but completely fails beyond ~3K tokens.
- Landmark fine-tuned LLaMA 7B maintains near-perfect accuracy up to 32K tokens (using CPU offloading for the KV cache), demonstrating context length extension by a factor of ~16x from the 512-token fine-tuning length.

### Computation and Memory

- **Training overhead:** Negligible -- only the Grouped Softmax computation is added. No cache is maintained during training. Training cost is O(1) relative to inference context length, compared to O(n^2) for standard attention.
- **Inference reduction:** The number of attention operations is reduced by a factor of ℓ_block (50 in the experiments) since only landmark tokens are scanned to identify relevant blocks. The cost of attending to retrieved blocks is constant regardless of total context length.
- **Memory reduction:** Only landmark key vectors need to reside in fast memory. All other tokens' KV vectors can be offloaded to CPU or disk and loaded on demand when their block is retrieved.
- **Compatibility with FlashAttention:** Landmark Attention integrates naturally with FlashAttention by matching the landmark frequency to the FlashAttention block size. A Triton implementation is provided.

### Limitations

- **Positional encoding extrapolation.** The stingy position mapping is an approximation: older blocks lose precise positional information when mapped to the same prefix position. The model can only attend to distant tokens based on semantics, not their exact position.
- **Block granularity.** The fixed block size (ℓ_block = 50) means the smallest retrievable unit is 50 tokens. If relevant information spans a block boundary, two blocks must be retrieved.
- **No cache during training.** The model never sees the cache-based retrieval during training, relying on the GroupedSoftmax mechanism to approximate it. Training with a cache might improve results but is left for future work.
- **Evaluation limited to perplexity and pass key retrieval.** No evaluation on downstream tasks such as question answering, summarization, or multi-document reasoning over long contexts.

---

## Conclusions

1. **Attention-based block retrieval via landmark tokens.** Landmark tokens trained with Grouped Softmax enable the attention mechanism itself to perform block-level retrieval, eliminating the need for a separate retriever while maintaining random-access flexibility over the full context.

2. **Context length generalization beyond training.** Models trained on 512-token windows can effectively operate at 2048--4096 token evaluation lengths (from-scratch experiments) and up to 32K tokens (LLaMA fine-tuning), demonstrating that the landmark mechanism enables robust length extrapolation.

3. **Comparable performance to Transformer-XL at reduced cost.** On PG-19, landmark attention at eval length 4096 (14.72 perplexity) approaches Transformer-XL (14.55) while offering interpretable retrieval patterns and direct access to exact past tokens rather than compressed recurrent states.

4. **Efficient fine-tuning for context extension.** Fine-tuning LLaMA 7B for 15,000 steps with ℓ_seq = 512 is sufficient to extend its effective context to 32K tokens with 98% pass key retrieval accuracy, demonstrating that landmark attention can be retrofitted to existing pretrained models at low cost.

5. **Computation and memory reduction proportional to block size.** At inference, the number of attention operations scales as O(n / ℓ_block) for block selection plus O(k · ℓ_block) for retrieved-block attention, yielding up to 50x reduction in both compute and memory compared to full attention, with the retrieved-block cost independent of total context length.

6. **Hierarchical retrieval via Context Miss Token.** The CMT extension demonstrates that the Grouped Softmax framework can be extended to create multiple retrieval levels, with 57% of retrieval calls eliminable at 0.05 perplexity cost, pointing toward cache-miss-style hierarchical memory architectures.

---

## Core References and Why They Are Referenced

### Memory and Recurrence for Transformers

- **Dai et al. (2019)** -- *Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context.* Primary baseline for the language modeling experiments. Transformer-XL uses segment-level recurrence to extend context but sacrifices random-access flexibility -- past information is only accessible through compressed hidden states from the previous segment.
- **Bulatov et al. (2022)** -- *Recurrent Memory Transformer.* Representative of methods that add recurrent memory tokens to Transformers. Referenced as a category of approaches that compress past context, losing the ability to attend to specific past tokens.
- **Burtsev et al. (2022)** -- *Memory Transformer.* Introduces special memory tokens prepended to the input, with final-layer representations carried forward. Like Transformer-XL, this limits access to past context to a compressed form.
- **Martins et al. (2022)** -- *∞-former: Infinite Memory Transformer.* Maps input to a continuous space and samples memory points based on attention probabilities. Referenced as another recurrent memory approach that cannot recover specific past tokens.
- **Mu et al. (2023)** -- *Learning to Compress Prompts with Gist Tokens.* Simultaneous work showing that special "gist" tokens trained to summarize prompts fail to remember specific details. This directly motivates the landmark approach: compression tokens lose fine-grained information, while landmark tokens enable retrieval of exact past tokens.

### Retrieval-Augmented Language Models

- **Guu et al. (2020)** -- *REALM: Retrieval-Augmented Language Model Pre-Training.* Jointly trains a retriever and reader, both transformers. Referenced as a representative retrieval-augmented method that relies on a separate retriever incompatible with the model's own attention.
- **Izacard et al. (2022)** -- *Atlas: Few-Shot Learning with Retrieval Augmented Language Models.* Investigates retriever training losses. Referenced alongside REALM as a retrieval-augmented approach requiring a separate mechanism.
- **Karpukhin et al. (2020)** -- *Dense Passage Retrieval for Open-Domain Question Answering.* Representative dense retriever method. Referenced in the context of separate retrieval mechanisms.

### Approximate and Sparse Attention

- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Uses dilated sliding window patterns with manually chosen window sizes. Referenced as a sparse attention method that restricts attention flexibility.
- **Zaheer et al. (2020)** -- *Big Bird: Transformers for Longer Sequences.* Combines local windows, random token subsets, and global tokens. Referenced as a sparse attention approach with limited flexibility.
- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Limits attention to a local window. Referenced as the simplest form of sparse attention.
- **Kitaev et al. (2020)** -- *Reformer: The Efficient Transformer.* Uses locality-sensitive hashing (LSH) to retrieve nearest keys. Referenced as an alternative nearest-neighbor retrieval approach.
- **Ren et al. (2021)** -- *Combiner: Full Attention Transformer with Sparse Computation Cost.* Uses max-pooling to derive block-level key and query vectors. Referenced as a contrast: Combiner limits the current token's control over within-block weights via heuristic pooling, while landmark attention preserves full query-controlled attention within retrieved blocks.
- **Wang et al. (2020)** -- *Linformer: Self-Attention with Linear Complexity.* Uses low-rank approximation of the attention matrix. Referenced as an approximation method.
- **Choromanski et al. (2022)** -- *Rethinking Attention with Performers.* Uses non-softmax kernels for efficient attention. Referenced alongside other approximation methods.

### kNN-Augmented Transformers

- **Khandelwal et al. (2020)** -- *Generalization through Memorization: Nearest Neighbor Language Models.* Stores hidden representations and uses kNN distribution to predict next tokens. Referenced as a kNN augmentation method that uses a fixed interpolation weight between kNN and local predictions, unlike landmark attention where the retrieval gate is input-dependent.
- **Wu et al. (2022)** -- *Memorizing Transformers.* Performs nearest-neighbor search over previous keys and computes attention to top results. Referenced as the closest kNN approach, but noted for using a tuned (not learned, input-dependent) interpolation weight.

### Positional Encoding

- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Provides the RoPE positional encoding used in the experiments. RoPE's property of adding position information to key and query vectors just before attention computation enables position-free cache storage.
- **Press et al. (2022)** -- *Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation (ALiBi).* Demonstrates that relative positional encodings still fail to extrapolate, and proposes ALiBi which dampens long-range attention. Referenced as evidence of the extrapolation problem and as a method incompatible with landmark attention's goal of attending to distant tokens.
- **Sun et al. (2022)** -- *A Length-Extrapolatable Transformer.* Proposes solutions for length extrapolation that require windowed attention. Referenced alongside ALiBi as methods that limit long-range attention, which is undesirable for the landmark approach.
- **Haviv et al. (2022)** -- *Transformer Language Models without Positional Encodings Still Learn Positional Information.* Shows that causal masking alone provides implicit positional information. Referenced to explain why Transformers fail to extrapolate: they learn their own positional encoding from the causal mask.

### Attention Pattern Analysis

- **Kovaleva et al. (2019)** -- *Revealing the Dark Secrets of BERT.* Analyzes attention patterns in BERT, finding that many heads attend to local context. Referenced for observed classic attention patterns that motivate retrieving blocks (with local context) rather than individual tokens.
- **Sukhbaatar et al. (2019)** -- *Adaptive Attention Span in Transformers.* Shows that earlier layers tend to use local attention. Referenced alongside the finding that initial layers in landmark models retrieve few blocks, consistent with locality of attention in early layers.

### Models and Infrastructure

- **Touvron et al. (2023)** -- *LLaMA: Open and Efficient Foundation Language Models.* Provides the LLaMA 7B model used for fine-tuning experiments, demonstrating that landmark attention can be retrofitted to existing pretrained models.
- **Radford et al. (2019)** -- *Language Models Are Unsupervised Multitask Learners (GPT-2).* Provides the architecture template and tokenizer used for from-scratch language modeling experiments.
- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* Referenced for compatibility: landmark attention integrates naturally with FlashAttention by aligning block sizes, and the authors provide a combined Triton implementation.
- **Johnson et al. (2019)** -- *Billion-Scale Similarity Search with GPUs (FAISS).* Referenced as an advanced data structure that can be applied on top of landmark tokens for further retrieval speedup.

### Evaluation Datasets

- **Rae et al. (2020)** -- *Compressive Transformers for Long-Range Sequence Modelling.* Introduces PG-19, the English books dataset (3.7B tokens) used for language modeling evaluation.

#### Cross-References in Available Papers

- **Kovaleva et al. (2019) (2019-11-dark-secrets-of-bert):** Cited [20] in the landmark paper for its analysis of BERT attention patterns (locality bias, diagonal patterns), which motivates the design choice of retrieving blocks of consecutive tokens rather than individual tokens. The finding that attention in early layers is predominantly local is consistent with the landmark paper's observation that initial layers retrieve very few blocks from memory.
- **PI (2023-06-pi-positional-interpolation) and NTK-Aware RoPE (2023-06-rope-ntk):** Both address context length extension for RoPE-based models via position interpolation. The landmark approach is complementary: PI and NTK-Aware RoPE modify positional encodings to support longer sequences, while landmark attention modifies the attention mechanism to selectively retrieve relevant past blocks. The positional augmentation method proposed in Appendix E of the landmark paper addresses the same extrapolation problem that PI and NTK-Aware RoPE solve.
- **YaRN (2024-05-yarn-context-extension):** YaRN improves upon PI and NTK-Aware RoPE for context extension. The landmark paper's stingy position mapping scheme is an alternative approach to the same problem. YaRN and landmark attention could in principle be combined: YaRN for positional extrapolation and landmark attention for efficient block retrieval.
- **Lost in the Middle (2024-02-lost-in-the-middle):** Liu et al. show that language models exhibit a U-shaped performance curve when retrieving information from long contexts, with degradation for information in the middle. Landmark attention addresses this problem by design: the attention-based block retrieval mechanism selects blocks based on semantic relevance regardless of position, potentially mitigating the positional bias that Lost in the Middle documents.
- **Attention Sinks (2024-05-attention-sinks-streaming):** StreamingLLM identifies attention sinks in the first tokens of a sequence. The landmark attention mechanism's Grouped Softmax implicitly handles the attention distribution differently: landmark tokens in the current block's group compete for attention mass, potentially absorbing some of the "sink" behavior that StreamingLLM identifies in the initial tokens.
