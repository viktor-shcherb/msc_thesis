---
title: "Random-Access Infinite Context Length for Transformers"
authors: "Mohtashami, Jaggi"
year: 2023
venue: "NeurIPS 2023"
paper_type: conference-paper
categories: ["attention-efficiency", "context-extension", "streaming-inference"]
scope: ["block-level retrieval via attention", "landmark tokens as learned gates", "infinite context inference"]
benchmarks_used: ["perplexity-pg19", "perplexity-proofpile", "passkey-retrieval"]
models_introduced: []
models_evaluated: ["llama-7b", "transformer-xl"]
key_claims:
  - id: C1
    claim: "Landmark tokens trained with Grouped Softmax enable attention-based block retrieval without a separate retriever"
    evidence: "Section 3.1, Equations 1-4, Figure 1"
    status: supported
    scope: "causal language modeling, GPT-2-like 12-layer architecture and LLaMA 7B"
    magnitude: "qualitative — mechanism demonstrated via perplexity parity with full attention (16.23 vs 16.12 at 512 tokens) and interpretable retrieval patterns"
  - id: C2
    claim: "Landmark attention trained on 512-token windows achieves 14.72 perplexity at 4096-token evaluation on PG-19, matching Transformer-XL at 14.55"
    evidence: "Table 1, Section 4.1"
    status: supported
    scope: "PG-19 English books corpus, GPT-2-like 12-layer architecture, l_block=50, k=4, 80 cached blocks"
    magnitude: "14.72 PPL vs Transformer-XL 14.55 PPL at eval length 4096 (0.17 PPL gap); 3.18 PPL on arXiv Math at same setting"
  - id: C3
    claim: "Fine-tuning LLaMA 7B with landmarks for 15K steps at context length 512 extends retrieval to 32K tokens with 98% passkey accuracy"
    evidence: "Figure 3b, Section 4.2, Appendix G"
    status: supported
    scope: "LLaMA 7B, passkey retrieval task only, per-head retrieval with k=5, KV cache offloaded to CPU"
    magnitude: "98% accuracy at 32K tokens (16x training context length) vs 0% for base LLaMA 7B beyond ~3K tokens"
  - id: C4
    claim: "Landmark attention reduces inference computation by a factor of block length (50x in experiments) compared to full attention"
    evidence: "Section 3.3"
    status: supported
    scope: "autoregressive generation, l_block=50, excluding retrieved-block attention cost"
    magnitude: "50x reduction in attention operations for block selection; retrieved-block cost constant regardless of total context length"
  - id: C5
    claim: "Context Miss Token can eliminate 57% of retrieval calls with only 0.05 perplexity degradation"
    evidence: "Table 3, Appendix D"
    status: supported
    scope: "PG-19, eval length 2048, k=4, 60K training steps (not full 240K), cutoff threshold 0.3"
    magnitude: "57% drop rate at 0.05 PPL cost (16.43 vs 16.38); baseline without CMT is 16.28"
  - id: C6
    claim: "Reducing retrieval flexibility to per-head only (not per-token) costs 0.18 perplexity at eval length 2048 with k=4"
    evidence: "Table 2, Section 4.1"
    status: supported
    scope: "PG-19, eval length 2048, k=4, GPT-2-like 12-layer architecture"
    magnitude: "0.18 PPL increase (15.10 vs 14.92); unique retrieved blocks typically below 10 out of 32 possible"
cross_references:
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer uses fixed sparse attention patterns; landmark attention learns block retrieval via the attention mechanism itself"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "ALiBi dampens long-range attention via linear distance penalty, incompatible with selective retrieval; landmark attention enables position-independent retrieval of distant blocks"
  - target: 2019-11-dark-secrets-of-bert
    type: complementary
    detail: "Cites Kovaleva et al.'s finding that many heads attend to local context, motivating block-level rather than token-level retrieval"
  - target: 2023-02-llama-open-efficient-foundation
    type: evaluates
    detail: "Fine-tunes LLaMA 7B with landmark tokens to demonstrate context extension to 32K tokens"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Uses RoPE's property of adding position information just before attention computation to enable position-free cache storage"
  - target: 2023-06-pi-positional-interpolation
    type: complementary
    detail: "PI modifies positional encodings for context extension; landmark attention modifies the attention mechanism; approaches are orthogonal and could be combined"
  - target: 2023-06-rope-ntk
    type: complementary
    detail: "NTK-aware RoPE scaling addresses extrapolation at the positional level; landmark attention addresses it at the attention mechanism level"
  - target: 2024-05-yarn-context-extension
    type: complementary
    detail: "YaRN and landmark attention could be combined: YaRN for positional extrapolation, landmarks for block retrieval"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Landmark attention's position-independent retrieval could mitigate the U-shaped performance curve documented in Lost in the Middle"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "Grouped Softmax distributes attention differently among landmark tokens, potentially interacting with attention sink behavior"
  - target: 2024-08-infinitebench-long-context-evaluation
    type: extended-by
    detail: "InfiniteBench adapts the passkey retrieval task to 100K+ contexts with 59 positions and 590 examples"
  - target: 2020-04-compressive-transformer-pg19
    type: uses-benchmark
    detail: "Uses PG-19 (introduced by Rae et al., 2020) for language modelling perplexity evaluation"
  - target: 2024-10-ruler-context-size
    type: extended-by
    detail: "RULER extends the passkey retrieval task format and reuses the noise sentence format from landmark attention as one of its haystack options in the NIAH retrieval category"
open_questions:
  - question: "Can positional encoding extrapolation be fully solved so landmark attention uses exact rather than approximate positions for distant blocks?"
    addressed_by: null
  - question: "Can hierarchical landmark tokens create multi-level memory caches analogous to hardware cache hierarchies?"
    addressed_by: null
  - question: "Would training with cache (exposing the model to the retrieval mechanism during training) improve results?"
    addressed_by: null
  - question: "How does landmark attention perform on downstream tasks beyond perplexity and passkey retrieval (e.g., question answering, summarization, multi-document reasoning)?"
    addressed_by: null
---

# Random-Access Infinite Context Length for Transformers

**Authors:** Amirkeivan Mohtashami, Martin Jaggi (EPFL)
**Date:** December 2023, NeurIPS 2023 (arXiv:2305.16300)

The method is commonly referred to as **Landmark Attention** in follow-up literature; the arXiv version uses the title "Landmark Attention: Random-Access Infinite Context Length for Transformers."

---

## Core Research Problem

Standard Transformer attention allows each token to access the representation of any other token, but this flexibility comes with **quadratic computational cost and memory footprint** in sequence length, limiting the context that can be processed. Prior approaches to overcoming this limit fall into three categories, each with fundamental drawbacks:

1. **Recurrent memory methods** (Transformer-XL, Memory Transformers, Infinite Memory Transformer, Recurrent Memory Transformer) compress past context into fixed-size memory states. This sacrifices the **random-access flexibility** of attention -- the model can no longer attend to specific past tokens, only to lossy summaries. Mu et al. (2023) -- *Learning to Compress Prompts with Gist Tokens* -- show concretely that gist tokens trained to summarize prompts fail to remember specific details that must be copied into the output (Section 2).

2. **Retrieval-augmented methods** (REALM, Atlas, Dense Passage Retrieval) use a separate retriever module to find relevant documents from a knowledge base. The retriever is not fully compatible with the model's own attention mechanism, cannot easily be updated for fresh long input data, and may fail to retrieve what the model's attention would find useful. Previous work using attention in the reader to build a retriever relied on manually crafted rules to reduce token scores to document scores (Section 2).

3. **Approximate and sparse attention methods** (Longformer, BigBird, Performer, Reformer, Linformer, Combiner) reduce attention cost but significantly restrict which tokens can be attended to, using fixed patterns (local windows, random subsets, global tokens) or heuristic reductions (max-pooling for block representations in Combiner) that limit the current token's control over attention weights (Section 2).

Additionally, Transformers have a well-known limitation in **extrapolating to context lengths not observed during training**, even with relative positional encodings. Current solutions to this problem often weaken attention scores for long-range tokens or require windowed attention, undermining the benefits of a longer context (Section 2, citing Press et al. (2022) and Sun et al. (2022)).

The core challenge is: **how to enable Transformers to access arbitrarily long contexts while retaining the random-access flexibility of full attention, without requiring a separate retrieval mechanism or compressing past context into lossy summaries.**

---

## Problem Solutions

The paper proposes **Landmark Attention**, a method that uses special "landmark" tokens inserted between fixed-size blocks of the input to act as learned gates for block-level retrieval directly through the attention mechanism.

1. **Landmark tokens as block representatives.** A new special token is inserted after every `l_block` tokens. The model is trained so that the key vector of each landmark token becomes a representative for its block: a high attention score to any token inside a block leads to a high attention score to the block's landmark (Section 3).
2. **Grouped Softmax for gated attention.** A modified softmax function (Grouped Softmax) trains the model to use landmark attention scores as multiplicative gates for within-block token attention, creating a two-level retrieval: first select relevant blocks via landmarks, then attend to tokens within selected blocks (Section 3.1).
3. **Cache-based inference at arbitrary lengths.** At inference, the input is processed in chunks. A cache stores key-value vectors for all previous blocks. Only landmark key vectors need to remain in fast memory; block contents can be offloaded to CPU/disk and loaded on demand. The top-k most relevant blocks are retrieved per token per head per layer (Section 3.2).

---

## Approach Details

### Method

The input text is preprocessed by inserting a landmark token after every `l_block` tokens. Training proceeds with standard batching over windows of `l_seq` tokens. Let `p_i` denote the index of the landmark token corresponding to the i-th token's block. If the last block is incomplete (no landmark), `p_i := l_seq`. If the i-th token is itself a landmark, `p_i := i`.

**Grouped Softmax.** Given a vector `v in R^{l_seq}` and a group index `g in N^{l_seq}`, Grouped Softmax applies softmax separately within each group (using `g = 1` for all elements recovers standard softmax):

> sigma_G(v, g)_x := exp(v_x) / sum_{y: g_y = g_x} exp(v_y)   (Eq. 1)

**Grouping scheme.** When computing attention for the i-th token, the grouping `G_{i,j}` is defined as (Eq. 2):

> G_{i,j} := p_j   if p_j != j   (normal tokens grouped by their block)
> G_{i,j} := -1    if p_i = j    (current block's landmark is ignored)
> G_{i,j} := p_i   if p_i != j and p_j = j   (other blocks' landmarks placed in the i-th token's group)

This grouping ensures: (a) normal tokens within a block share a softmax group, (b) landmark tokens for other blocks compete in the same softmax group as tokens in the current block, and (c) the current block's own landmark is excluded.

**Attention weights.** After computing `S_{i,j} := GroupedSoftmax(Q_i^T K / sqrt(d_head), G_i)`, the final attention weights are (Eqs. 3-4):

> AttWeight(Q, K)_{i,j} := 0   if p_j = j   (landmark tokens receive zero final weight)
> AttWeight(Q, K)_{i,j} := S_{i,j}   if G_{i,j} = G_{i,i} and p_j != j   (same-group tokens: direct weight)
> AttWeight(Q, K)_{i,j} := S_{i,j} * S_{i,p_j}   if G_{i,j} != G_{i,i} and p_j != j   (other-group tokens: gated by landmark)

Attention weights sum to one under this scheme. The key property is that **attending to tokens in other blocks is gated by the attention score to their landmark token**. Since landmarks and current-block tokens share a softmax group, the model must trade off between attending to its local context and retrieving from other blocks. The intuition is to force the model to only attend to relevant blocks due to this trade-off (Section 3.1).

### Key Technical Components

**Stingy position mapping.** Transformers cannot extrapolate to positional indices beyond those seen during training. To handle arbitrarily long contexts at inference, the paper uses an approximate position mapping scheme (Section 3.2.1, Figure 2). A prefix segment of length `(k+1) * (l_block + 1)` is allocated before the current chunk. The latest k cached blocks are mapped to their corresponding positions within the last k slots of this prefix. All older blocks are mapped to the position of the `(k+1)`-th last block. Retrieved blocks are then distributed across the prefix respecting their relative order. This uses RoPE (Su et al., 2021), which adds position information to key and query vectors just before computing attention, enabling **position-free storage** in the cache.

When k = 1, mapping memory blocks to a segment of at least 2 blocks is crucial: using only a single block maps all memory blocks to the same index, making it impossible to retrieve the last block based on position information alone (Section 3.2.1).

**Positional augmentation (Appendix E).** To improve extrapolation, the authors propose inserting random positional jumps (between 1 and `p_jump`) after each landmark token during training. With `p_jump = 100` and 10-11 landmarks per input (training length 512), the model extrapolates to ~1400 tokens without cache, compared to ~1024 tokens with standard positional encoding (Figure 6).

**Context Miss Token (CMT) (Appendix D).** A hierarchical extension where a special token at position -1 acts as a gate over landmark tokens themselves. The grouping scheme is extended so that some landmarks (randomly selected during training with probability P_CMT = 0.5) are controlled by CMT, and the attention weight for tokens in CMT-controlled blocks becomes `S_{i,j} * S_{i,p_j} * S_{i,-1}` (Eqs. 5-6). At inference, setting `S_{i,-1}` to zero when below a cutoff threshold emulates skipping retrieval entirely.

**Retrieval granularity.** At the most permissive level, each token and each head can retrieve different blocks. Efficiency can be improved by merging scores across tokens (taking the maximum landmark score across all tokens in a chunk per head) or across heads (taking the maximum across heads). This reduces bandwidth for cache loading at a moderate perplexity cost (Section 4.1, Table 2).

**FlashAttention compatibility.** Landmark Attention integrates naturally with FlashAttention by matching the landmark frequency to the FlashAttention block size. A Triton implementation is provided. This combination allows fine-tuning LLaMA 7B with 2048 context length instead of the maximum 512 without FlashAttention (Appendix F).

### Experimental Setup

**Language modeling (from scratch).**

- Architecture: GPT-2-like, 12-layer decoder-only transformer, 8 heads, head dimension 128 (embedding dimension 1024), FFN hidden size 4096.
- Optimizer: AdamW with beta_1 = 0.9, beta_2 = 0.95, weight decay 0.001, base learning rate 0.002, 2% warmup, cosine scheduler to minimum learning rate 0.0004.
- Tokenizer: GPT-2 tokenizer.
- Training: 240K steps with l_seq = 512, l_block = 50. Effective batch size 128 via gradient accumulation and data-parallel training across 4 nodes. Mixed-precision bfloat16 on up to 4 NVIDIA A100 GPUs.
- Datasets: PG-19 (3.7B tokens, English books) and arXiv Math (5.6B tokens, cleaned arXiv math subset of proof-pile).
- Baseline: Transformer-XL with window size 256 (effective context 512), trained for 60K steps over segments of length 2048, observing the same total number of tokens as the landmark method (Section 4.1).
- **Reproducibility:** Code released at https://github.com/epfml/landmark-attention/. No variance estimates reported; single run per configuration (limited evidence for individual perplexity comparisons). Seeds not reported.

**Fine-tuning LLaMA 7B.**

- 15,000 steps with context length 512, using the sample subset of RedPajama.
- Evaluation: passkey retrieval task -- a randomly generated passkey (integer 1-50000) hidden at a random position within filler text. Accuracy measured as generating the correct key within the first 100 tokens, averaged over 50 random prompts per context length.
- Inference: chunks of 250 tokens, top k = 4 retrieved blocks. For 32K context, KV cache (except landmarks) offloaded to CPU with retrieval flexibility reduced to per-head only (not per-token), k = 5 (Section 4.2, Appendix G).

### Key Results

**Language modeling perplexity (Table 1):**

| Eval. Length | Method | l_local | Blocks | k | Attention Size | PG19 PPL | arXiv PPL |
|---|---|---|---|---|---|---|---|
| 512 | Baseline | 512 | - | - | 512 | 16.12 | 4.01 |
| 512 | Baseline | 360 | - | - | 360 | 16.76 | 4.31 |
| 512 | Landmark | 250 | 10 | 2 | 360 | 16.23 | 4.01 |
| 2048 | Transformer-XL | 256 | - | - | 512 | 14.72 | - |
| 2048 | Landmark | 250 | 40 | 2 | 360 | 15.14 | 3.43 |
| 2048 | Landmark | 350 | 40 | 2 | 460 | 15.07 | 3.41 |
| 2048 | Landmark | 300 | 40 | 3 | 460 | 14.97 | 3.36 |
| 2048 | Landmark | 250 | 20 | 4 | 460 | 15.02 | 3.37 |
| 2048 | Landmark | 250 | 40 | 4 | 460 | 14.92 | 3.35 |
| 4096 | Transformer-XL | 256 | - | - | 512 | 14.55 | - |
| 4096 | Landmark | 250 | 40 | 4 | 460 | 14.79 | 3.19 |
| 4096 | Landmark | 250 | 80 | 2 | 370 | 15.00 | 3.29 |
| 4096 | Landmark | 250 | 80 | 4 | 470 | 14.72 | 3.18 |

- At eval length 512, landmark attention with l_local = 250 and k = 2 (attending to 360 tokens: 250 local + 10 landmarks + 100 retrieved) achieves **16.23 perplexity**, close to the full-attention baseline at 512 (16.12) and substantially better than the baseline truncated to 360 tokens (16.76) (Table 1, single run per configuration, limited evidence).
- At eval length 4096, landmark attention (14.72 with 80 blocks, k = 4) **closes the gap with Transformer-XL** (14.55) despite being trained only on 512-token windows (Table 1, two datasets tested -- moderate evidence).
- On arXiv Math, landmark attention achieves **3.18 perplexity** at eval length 4096 vs. 4.01 at eval length 512 -- a 20.7% reduction demonstrating effective utilization of longer contexts not seen during training. Transformer-XL results not reported for arXiv Math due to computation limitations (Table 1).
- The model still improves over the baseline even with only k = 2 retrieved blocks at context lengths of 2048 and 4096, and keeping only 40 blocks in memory at eval length 4096 outperforms eval length 2048 with the same configuration, suggesting the model also learns recurrent-like mechanisms (Table 1, Section 4.1).

**Retrieval granularity (PG-19, Table 2):**

| Per Head | Per Token | Eval. Length | k | Blocks (theoretical) | Perplexity |
|---|---|---|---|---|---|
| Yes | Yes | 2048 | 2 | 250 * 8 * 2 | 15.14 |
| Yes | Yes | 2048 | 4 | 250 * 8 * 4 | 14.92 |
| Yes | Yes | 4096 | 4 | 250 * 8 * 4 | 14.72 |
| Yes | No | 2048 | 2 | 8 * 2 | 15.48 |
| Yes | No | 2048 | 4 | 8 * 4 | 15.10 |
| Yes | No | 4096 | 4 | 8 * 4 | 14.95 |
| No | Yes | 2048 | 2 | 250 * 2 | 15.44 |
| No | Yes | 2048 | 4 | 250 * 4 | 15.04 |
| No | Yes | 4096 | 4 | 250 * 4 | 14.89 |

- Restricting retrieval to vary only across heads (not tokens) at k = 4, eval 2048 costs **0.18 perplexity** (15.10 vs 14.92) but substantially reduces unique blocks loaded from cache -- typically below 10 out of 32 theoretically possible (Table 2, Figure 5, single dataset, limited evidence).
- Restricting to vary only across tokens (not heads) at k = 4, eval 2048 costs **0.12 perplexity** (15.04 vs 14.92) (Table 2).
- The most restricted setting (same blocks across heads, per-token only) at k = 2, eval 2048 costs **0.30 perplexity** (15.44 vs 15.14) (Table 2).

**Fine-tuning LLaMA 7B -- passkey retrieval accuracy (Figure 3b):**

| Context Length | Base LLaMA 7B | Landmark Fine-Tuned |
|---|---|---|
| ~2K (within training length) | ~100% | ~100% |
| ~5K | 0% | ~100% |
| ~10K | 0% | ~100% |
| ~32K | OOM | 98% |

- Base LLaMA 7B retrieves the passkey within and slightly beyond its 2048-token training context but completely fails beyond ~3K tokens.
- Landmark fine-tuned LLaMA 7B maintains near-perfect accuracy up to **32K tokens** (using CPU offloading for the KV cache), demonstrating context length extension by a factor of ~16x from the 512-token fine-tuning length (Figure 3b, averaged over 50 random prompts per context length -- moderate evidence for the specific task, but only tested on passkey retrieval).

**Context Miss Token (PG-19, eval length 2048, k = 4, Table 3, 60K training steps):**

| Cutoff | Perplexity | Drop Rate |
|---|---|---|
| Baseline (no CMT) | 16.28 | 0% |
| 0.0 (CMT, no cutoff) | 16.38 | 0% |
| 0.1 | 16.38 | 23% |
| 0.3 | 16.43 | 57% |
| 0.5 | 16.86 | 84% |
| 1.0 | 19.49 | 100% |

- With cutoff 0.3, **57% of retrieval calls are dropped** with only 0.05 perplexity degradation (16.43 vs. 16.38 without cutoff) (Table 3).
- The 0.10 perplexity gap between training without CMT (16.28) and with CMT (16.38, no cutoff) reflects the harder training task; the authors conjecture longer training would close this gap (Table 3, single dataset at 60K steps -- limited evidence, not validated at full 240K steps).

### Computation and Memory

- **Training overhead:** Negligible -- only the Grouped Softmax computation is added. No cache is maintained during training. Training cost is O(1) relative to inference context length, compared to O(n^2) for standard attention (Section 3.3).
- **Inference reduction:** The number of attention operations is reduced by a factor of l_block (50 in experiments) since only landmark tokens are scanned to identify relevant blocks. The cost of attending to retrieved blocks is constant regardless of total context length (Section 3.3).
- **Memory reduction:** Only landmark key vectors need to reside in fast memory. All other tokens' KV vectors can be offloaded to CPU or disk and loaded on demand when their block is retrieved (Section 3.3, Appendix G).
- **Additional overhead:** The two matrix multiplications (block selection + retrieved-block attention) instead of one become relatively negligible for larger inputs (Section 3.3).
- **Data structure compatibility:** The method can be combined with FAISS or similar nearest-neighbor data structures on top of landmark tokens for further retrieval speedup (Section 3.3).

---

## Limitations and Failure Modes

1. **Positional encoding extrapolation.** The stingy position mapping is an approximation: older blocks lose precise positional information when mapped to the same prefix position. The model can only attend to distant tokens based on semantics, not their exact position. Positional augmentation (Appendix E) partially addresses this but does not fully solve the problem (Section 3.2.1, Section 5).

2. **Block granularity.** The fixed block size (l_block = 50) means the smallest retrievable unit is 50 tokens. If relevant information spans a block boundary, two blocks must be retrieved. The block size also creates a trade-off: larger blocks reduce landmark overhead but require smaller chunks to fit within the training context length (Appendix F).

3. **No cache during training.** The model never sees the cache-based retrieval during training, relying on the Grouped Softmax mechanism to approximate it. Training with a cache might improve results but is left for future work (Section 5).

4. **[Inferred]** **Evaluation limited to perplexity and passkey retrieval.** No evaluation on downstream tasks such as question answering, summarization, or multi-document reasoning over long contexts. The passkey retrieval task tests exact-match retrieval but does not assess reasoning over retrieved content (Sections 4.1-4.2).

5. **[Inferred]** **Perplexity gap with Transformer-XL.** At eval length 2048 on PG-19, landmark attention (14.92) trails Transformer-XL (14.72) by 0.20 PPL. At eval length 4096, the gap narrows to 0.17 PPL (14.72 vs 14.55), suggesting Transformer-XL's recurrence may capture some information the landmark mechanism misses at shorter evaluation windows (Table 1).

6. **CMT increases training difficulty.** Training with Context Miss Token yields 0.10 higher perplexity than training without it (16.38 vs. 16.28 at 60K steps), indicating the additional hierarchical retrieval mechanism makes optimization harder (Table 3).

7. **[Inferred]** **Single model scale tested.** From-scratch experiments use a single GPT-2-like architecture; fine-tuning experiments use only LLaMA 7B. Behavior at larger scales is unknown.

#### Scope and Comparability

- **What was not tested:** No models larger than 7B parameters. No evaluation on downstream tasks (QA, summarization, multi-document reasoning). No comparison with other context extension methods (Position Interpolation, NTK-aware scaling, YaRN). No evaluation on non-English data. The CMT extension was only evaluated at 60K training steps (25% of full training), not at the full 240K steps used for the main experiments.
- **Comparability notes:** The Transformer-XL baseline was trained over segments of length 2048 (using recurrence over 256-token windows) while landmark attention was trained on 512-token windows, meaning Transformer-XL sees longer contiguous contexts during training. Both methods observed the same total number of tokens. The Transformer-XL baseline was only evaluated on PG-19 due to computation constraints, so cross-method comparison on arXiv Math is not possible. The passkey retrieval task is a synthetic exact-match test that may not reflect performance on naturalistic long-context tasks.

---

## Conclusions

### Contributions

1. **Attention-based block retrieval via landmark tokens.** Landmark tokens trained with Grouped Softmax enable the attention mechanism itself to perform block-level retrieval, eliminating the need for a separate retriever while maintaining random-access flexibility over the full context (Section 3.1, Equations 1-4).

2. **Context length generalization beyond training.** Models trained on 512-token windows effectively operate at 2048-4096 token evaluation lengths (from-scratch experiments) and up to 32K tokens (LLaMA fine-tuning), demonstrating that the landmark mechanism enables robust length extrapolation (Table 1, Figure 3b).

3. **Comparable performance to Transformer-XL at reduced cost.** On PG-19, landmark attention at eval length 4096 (14.72 perplexity) approaches Transformer-XL (14.55) while offering interpretable retrieval patterns and direct access to exact past tokens rather than compressed recurrent states (Table 1).

4. **Efficient fine-tuning for context extension.** Fine-tuning LLaMA 7B for 15,000 steps with l_seq = 512 extends its effective context to 32K tokens with 98% passkey retrieval accuracy, demonstrating that landmark attention can be retrofitted to existing pretrained models at low cost (Section 4.2, Appendix G).

5. **Inference cost reduction proportional to block size.** At inference, the number of attention operations for block selection scales as O(n / l_block) plus O(k * l_block) for retrieved-block attention, yielding up to 50x reduction in both compute and memory compared to full attention, with retrieved-block cost independent of total context length (Section 3.3).

6. **Hierarchical retrieval via Context Miss Token.** The CMT extension demonstrates that the Grouped Softmax framework can create multiple retrieval levels, with 57% of retrieval calls eliminable at 0.05 perplexity cost (Table 3, Appendix D).

### Implications

1. **Landmark attention as a building block for infinite-context architectures.** The method's compatibility with FlashAttention and KV cache offloading suggests it could serve as a practical building block for production systems requiring very long contexts, though this has not been validated at scale beyond LLaMA 7B (speculative).

2. **Potential complementarity with positional encoding methods.** The paper explicitly notes that landmark attention is orthogonal to positional encoding methods (PI, NTK-aware scaling, YaRN), suggesting the two approaches could be combined. This remains untested (Section 5).

3. **Attention sinks and landmark tokens.** The Grouped Softmax mechanism distributes attention differently from standard softmax. Whether landmark tokens interact with or mitigate the attention sink phenomenon is an open question (speculative).

---

## Key Claims

1. **C1: Attention-based block retrieval without separate retriever.** Landmark tokens trained with Grouped Softmax produce key vectors that serve as block representatives, enabling block selection directly through the attention mechanism (Section 3.1, Equations 1-4, Figure 1). The mechanism is validated on two datasets (PG-19, arXiv Math) with a single architecture (12-layer GPT-2-like) and one fine-tuned model (LLaMA 7B) -- moderate evidence for the mechanism, though limited to two tasks. **Status: supported.** **Scope:** causal language modeling, GPT-2-like 12-layer architecture and LLaMA 7B. **Magnitude:** qualitative mechanism; achieves 16.23 vs 16.12 full-attention PPL at 512 tokens.

2. **C2: Comparable perplexity to Transformer-XL at reduced computation.** At eval length 4096 on PG-19, landmark attention achieves **14.72 perplexity** vs. Transformer-XL's 14.55, while attending to 470 tokens per step compared to Transformer-XL's effective 512 (Table 1, Section 4.1). Single run per configuration, no variance reported (limited evidence for the exact gap). **Status: supported.** **Scope:** PG-19 English books, GPT-2-like architecture, l_block=50, k=4, 80 cached blocks. **Magnitude:** 14.72 vs 14.55 PPL (0.17 gap); 3.18 vs 4.01 PPL improvement on arXiv Math from 512 to 4096 eval length.

3. **C3: Context extension to 32K tokens via fine-tuning.** Fine-tuning LLaMA 7B with landmarks for 15K steps at context length 512 yields **98% passkey retrieval accuracy** at 32K tokens, averaged over 50 random prompts (Figure 3b, Section 4.2, Appendix G). The passkey retrieval task is synthetic exact-match; downstream task performance is unknown (limited task diversity). **Status: supported.** **Scope:** LLaMA 7B, passkey retrieval only, per-head retrieval with k=5, CPU offloading. **Magnitude:** 98% at 32K vs 0% for base LLaMA beyond ~3K tokens (16x context extension from 512 training length).

4. **C4: 50x computation and memory reduction at inference.** With l_block = 50, landmark scanning reduces attention operations by a factor of 50 for block selection. Retrieved-block attention cost is constant regardless of total context length (Section 3.3). This is a theoretical analysis, not an empirical throughput measurement (no wall-clock timing reported). **Status: supported.** **Scope:** autoregressive generation, l_block=50, excluding retrieved-block attention cost. **Magnitude:** 50x reduction in block-selection attention operations.

5. **C5: CMT eliminates 57% of retrieval calls at minimal perplexity cost.** With cutoff threshold 0.3, the CMT score drops below threshold for 57% of retrieval operations, and perplexity increases by only 0.05 (16.43 vs. 16.38, Table 3, Appendix D). Only tested at 60K training steps on PG-19 at eval length 2048 (limited evidence -- not validated at full training or on other datasets). **Status: supported.** **Scope:** PG-19, eval length 2048, k=4, 60K steps, cutoff 0.3. **Magnitude:** 57% drop rate at 0.05 PPL cost.

6. **C6: Retrieval flexibility reduction trades perplexity for efficiency.** Constraining retrieval to vary across heads but not tokens costs **0.18 perplexity** (15.10 vs. 14.92 at eval length 2048, k = 4) while reducing unique retrieved blocks to typically below 10 out of 32 possible (Table 2, Figure 5). Single dataset (PG-19), single architecture (limited evidence). **Status: supported.** **Scope:** PG-19, eval length 2048, k=4, GPT-2-like 12-layer architecture. **Magnitude:** 0.18 PPL increase; unique blocks typically <10 out of 32.

---

## Open Questions

1. **Can positional encoding extrapolation be fully solved for landmark attention?** The stingy position mapping loses exact positional information for distant blocks. The positional augmentation approach (Appendix E) partially addresses this but a general solution is needed for exact position-aware retrieval. Not addressed by subsequent work in this repository.

2. **Can hierarchical landmark tokens create multi-level memory?** The CMT extension (Appendix D) demonstrates a two-level hierarchy. The authors suggest extending this to multiple levels analogous to hardware cache hierarchies, with higher-level landmarks controlling lower-level ones (Section 5). Not addressed by subsequent work in this repository.

3. **Would training with cache improve results?** The model never sees the cache-based retrieval mechanism during training. The authors hypothesize that incorporating the cache during training could improve performance, especially given the stingy position mapping (Section 5). Not addressed by subsequent work in this repository.

4. **How does landmark attention perform on downstream tasks?** Evaluation is limited to perplexity and passkey retrieval. Performance on question answering, summarization, multi-document reasoning, and other tasks requiring long-context understanding is unknown (Sections 4.1-4.2). Not addressed by subsequent work in this repository.

---

## Core References and Why They Are Referenced

### Memory and Recurrence for Transformers

- **Dai et al. (2019)** -- *Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context.* Primary baseline for the language modeling experiments. Transformer-XL uses segment-level recurrence to extend context but sacrifices random-access flexibility -- past information is only accessible through compressed hidden states from the previous segment.
- **Bulatov et al. (2022)** -- *Recurrent Memory Transformer.* Representative of methods that add recurrent memory tokens to Transformers. Referenced as a category of approaches that compress past context, losing the ability to attend to specific past tokens.
- **Burtsev et al. (2022)** -- *Memory Transformer.* Introduces special memory tokens prepended to the input, with final-layer representations carried forward. Like Transformer-XL, this limits access to past context to a compressed form.
- **Martins et al. (2022)** -- *Infinite Memory Transformer.* Maps input to a continuous space and samples memory points based on attention probabilities. Referenced as another recurrent memory approach that cannot recover specific past tokens.
- **Mu et al. (2023)** -- *Learning to Compress Prompts with Gist Tokens.* Simultaneous work showing that special "gist" tokens trained to summarize prompts fail to remember specific details. Directly motivates the landmark approach: compression tokens lose fine-grained information, while landmark tokens enable retrieval of exact past tokens.

### Retrieval-Augmented Language Models

- **Guu et al. (2020)** -- *REALM: Retrieval-Augmented Language Model Pre-Training.* Jointly trains a retriever and reader. Referenced as a representative retrieval-augmented method that relies on a separate retriever incompatible with the model's own attention.
- **Izacard et al. (2022)** -- *Atlas: Few-Shot Learning with Retrieval Augmented Language Models.* Investigates retriever training losses. Referenced alongside REALM as a retrieval-augmented approach requiring a separate mechanism.
- **Karpukhin et al. (2020)** -- *Dense Passage Retrieval for Open-Domain Question Answering.* Representative dense retriever method.

### Approximate and Sparse Attention

- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Uses dilated sliding window patterns with manually chosen window sizes. Referenced as a sparse attention method that restricts attention flexibility.
- **Zaheer et al. (2020)** -- *Big Bird: Transformers for Longer Sequences.* Combines local windows, random token subsets, and global tokens. Referenced as a sparse attention approach with limited flexibility.
- **Child et al. (2019)** -- *Generating Long Sequences with Sparse Transformers.* Limits attention to a local window. Referenced as the simplest form of sparse attention.
- **Kitaev et al. (2020)** -- *Reformer: The Efficient Transformer.* Uses locality-sensitive hashing (LSH) to retrieve nearest keys. Referenced as an alternative nearest-neighbor retrieval approach.
- **Ren et al. (2021)** -- *Combiner: Full Attention Transformer with Sparse Computation Cost.* Uses max-pooling to derive block-level key and query vectors. Referenced as a contrast: Combiner limits the current token's control over within-block weights via heuristic pooling, while landmark attention preserves full query-controlled attention within retrieved blocks.
- **Wang et al. (2020)** -- *Linformer: Self-Attention with Linear Complexity.* Uses low-rank approximation of the attention matrix.
- **Choromanski et al. (2022)** -- *Rethinking Attention with Performers.* Uses non-softmax kernels for efficient attention.

### kNN-Augmented Transformers

- **Khandelwal et al. (2020)** -- *Generalization through Memorization: Nearest Neighbor Language Models.* Stores hidden representations and uses kNN distribution to predict next tokens. Referenced as a kNN method that uses a fixed interpolation weight, unlike landmark attention where the retrieval gate is input-dependent.
- **Wu et al. (2022)** -- *Memorizing Transformers.* Performs nearest-neighbor search over previous keys and computes attention to top results. Referenced as the closest kNN approach, but noted for using a tuned (not learned, input-dependent) interpolation weight.

### Positional Encoding

- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Provides the RoPE positional encoding used in the experiments. RoPE's property of adding position information to key and query vectors just before attention computation enables position-free cache storage.
- **Press et al. (2022)** -- *Train Short, Test Long: Attention with Linear Biases (ALiBi).* Demonstrates that relative positional encodings still fail to extrapolate, and proposes ALiBi which dampens long-range attention. Referenced as evidence of the extrapolation problem and as a method incompatible with landmark attention's goal of attending to distant tokens.
- **Sun et al. (2022)** -- *A Length-Extrapolatable Transformer.* Proposes solutions for length extrapolation that require windowed attention. Referenced alongside ALiBi as methods that limit long-range attention.
- **Haviv et al. (2022)** -- *Transformer Language Models without Positional Encodings Still Learn Positional Information.* Shows that causal masking alone provides implicit positional information. Referenced to explain why Transformers fail to extrapolate.

### Attention Pattern Analysis

- **Kovaleva et al. (2019)** -- *Revealing the Dark Secrets of BERT.* Analyzes attention patterns in BERT, finding that many heads attend to local context. Referenced for observed attention patterns that motivate block-level (with local context) rather than token-level retrieval.
- **Sukhbaatar et al. (2019)** -- *Adaptive Attention Span in Transformers.* Shows that earlier layers tend to use local attention. Referenced alongside the finding that initial layers in landmark models retrieve few blocks, consistent with locality of attention in early layers.

### Models and Infrastructure

- **Touvron et al. (2023)** -- *LLaMA: Open and Efficient Foundation Language Models.* Provides the LLaMA 7B model used for fine-tuning experiments, demonstrating that landmark attention can be retrofitted to existing pretrained models.
- **Radford et al. (2019)** -- *Language Models Are Unsupervised Multitask Learners (GPT-2).* Provides the architecture template and tokenizer used for from-scratch language modeling experiments.
- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* Referenced for compatibility: landmark attention integrates with FlashAttention by aligning block sizes, and the authors provide a combined Triton implementation.
- **Johnson et al. (2019)** -- *Billion-Scale Similarity Search with GPUs (FAISS).* Referenced as an advanced data structure applicable on top of landmark tokens for further retrieval speedup.

### Evaluation Datasets

- **Rae et al. (2020)** -- *Compressive Transformers for Long-Range Sequence Modelling.* Introduces PG-19, the English books dataset (3.7B tokens) used for language modeling evaluation.
