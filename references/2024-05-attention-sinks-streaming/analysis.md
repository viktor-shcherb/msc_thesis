# Efficient Streaming Language Models with Attention Sinks

**Authors:** Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, Mike Lewis (MIT, Meta AI, CMU, NVIDIA)
**Date:** May 2024, ICLR 2024 (arXiv:2309.17453)

---

## Core Research Problem

Deploying LLMs in streaming applications -- such as multi-round dialogue or persistent assistants -- requires processing input sequences that grow indefinitely over time. Two challenges make this intractable with standard Transformer-based LLMs: (1) the KV cache grows linearly with sequence length, leading to unbounded memory consumption during decoding, and (2) LLMs cannot generalize beyond their pre-training attention window size (e.g., 4K tokens for Llama-2), with performance degrading sharply on longer inputs.

Window attention (caching only the most recent L tokens' KV states) is the natural efficiency solution, but empirically collapses the moment the initial tokens are evicted from the cache -- even evicting just the first token causes perplexity to spike from 5.40 to 5158 on Llama-2-13B. Sliding window with re-computation recovers quality but incurs O(TL^2) cost per token, making it impractical for real-time streaming. Context window extension methods (PI, NTK-RoPE, YaRN) expand the finite window but do not enable truly infinite-length generation. The core challenge is: **how to enable LLMs trained with a finite attention window to handle infinite-length input streams without fine-tuning, while maintaining bounded memory and constant decoding latency.**

---

## Problem Solutions

The paper identifies the **attention sink** phenomenon -- autoregressive LLMs allocate disproportionately high attention scores to initial tokens regardless of their semantic content -- and leverages this insight to propose **StreamingLLM**, a simple framework for infinite-length streaming inference. The solution rests on three observations:

1. **Window attention fails because it evicts attention sinks.** The perplexity spike occurs precisely when initial tokens are removed from the cache, because these tokens serve as a "dump" for excess attention probability mass required by the SoftMax normalization.

2. **Initial tokens are attention sinks due to SoftMax and autoregressive visibility.** SoftMax requires attention scores to sum to one, so the model must allocate residual attention somewhere even when the current query has no strong match among context tokens. Initial tokens, being visible to all subsequent tokens in autoregressive modeling, are the easiest targets to learn as sinks during pre-training.

3. **Preserving a few sink tokens alongside the sliding window restores performance.** Keeping just 4 initial tokens' KV states together with the rolling window's KV is sufficient to stabilize the attention score distribution and match the quality of full re-computation.

---

## Approach Details

### Method

StreamingLLM maintains a KV cache with two components:

1. **Attention sink tokens:** The KV states of the first few tokens (4 by default), which anchor the attention computation.
2. **Rolling KV cache:** The KV states of the most recent L tokens, which provide the actual contextual information for language modeling.

When the cache is full and a new token arrives, the oldest token in the rolling window is evicted (not the sink tokens). The total cache size remains constant at (number of sink tokens) + L.

**Position encoding handling:** StreamingLLM assigns positions based on the token's position *within the cache*, not its position in the original text. For a cache containing tokens [0, 1, 2, 3, 6, 7, 8] decoding token 9, positions are assigned as [0, 1, 2, 3, 4, 5, 6, 7] rather than [0, 1, 2, 3, 6, 7, 8, 9]. For RoPE-based models, Keys are cached *before* applying the rotary transformation, and the position transformation is reapplied at each decoding step. For ALiBi-based models, a contiguous linear bias is applied rather than a "jumping" bias.

### Key Technical Components

- **Number of sink tokens:** Four initial tokens suffice for all tested models. Introducing only 1--2 tokens does not fully restore perplexity; adding more than 4 yields diminishing returns (Table 2). This is because most models lack a consistent starting token across pre-training samples, so the model distributes the sink role across the first few positions.

- **Dedicated sink token for pre-training:** Pre-training with a learnable placeholder token prepended to all training samples consolidates the attention sink into a single token. A 160M-parameter model trained with this sink token achieves stable streaming perplexity with just the sink token (PPL 18.01), while the vanilla model requires 4 initial tokens to reach the same level (PPL 18.05). Including the sink token does not harm convergence or downstream task performance (Table 4).

- **SoftMax-off-by-One (Zero Sink):** An alternative formulation:

> SoftMax_1(x)_i = e^{x_i} / (1 + sum_{j=1}^{N} e^{x_j})

which is equivalent to prepending a token with all-zero Key and Value features. This partially alleviates the attention sink problem but is less effective than a learnable sink token (Table 3).

- **Cache position re-indexing:** Critical for correctness with relative position encodings. Without re-indexing, the gap between sink token positions and rolling window positions would create out-of-distribution positional distances.

### Experimental Setup

- **Models:** Llama-2-[7, 13, 70]B (RoPE), MPT-[7, 30]B (ALiBi), Falcon-[7, 40]B (RoPE), Pythia-[2.8, 6.9, 12]B (RoPE).
- **Pre-training experiments:** 160M-parameter models trained from scratch using the Pythia-160M codebase on the deduplicated Pile dataset, 143K steps, batch size 256, 8x A6000 GPUs.
- **Evaluation -- language modeling:** Concatenated PG19 test set (100 books, up to 4M tokens). Cache sizes: 2048 for Llama-2, 1024 for Falcon/Pythia/MPT (half the pre-training window).
- **Evaluation -- streaming QA:** ARC-[Easy, Challenge] concatenated into a continuous stream; StreamEval benchmark (custom dataset inspired by LongEval, querying every 10 lines with answers 20 lines prior).
- **Evaluation -- downstream tasks:** ARC-E/C, HellaSwag, LAMBADA, OpenbookQA, PIQA, Winogrande (zero-shot, for sink token pre-training experiments).
- **Efficiency benchmarks:** Per-token decoding latency and memory usage on a single NVIDIA A6000 GPU.

### Key Results

| Setting | StreamingLLM | Best Alternative |
|---|---|---|
| Llama-2-13B PPL (65K tokens, cache 1024) | 5.40 (4+1020) | 5158 (window), 5.43 (recompute) |
| Llama-2-7B PPL (400K tokens, cache 4096) | 9.59 (4+4092) | 3359.95 (window) |
| Falcon-7B PPL (400K tokens, cache 2048) | 12.12 (4+2044) | 17.90 (window) |
| MPT-7B PPL (400K tokens, cache 2048) | 14.99 (4+2044) | 460.29 (window) |
| ARC-E streaming (Llama-2-70B-Chat) | 91.37% | 0.12% (window), 91.29% (one-shot) |
| ARC-C streaming (Llama-2-70B-Chat) | 80.20% | 0.32% (window), 78.50% (one-shot) |
| Decoding speedup vs. recomputation (cache 256) | 22.2x (Llama-2-7B) | 1x (recomputation) |

- StreamingLLM matches the sliding window with re-computation baseline in perplexity while achieving up to **22.2x speedup** in per-token decoding latency.
- All tested model families (Llama-2, MPT, Falcon, Pythia) across scales (2.8B--70B) maintain stable perplexity over **4 million tokens**.
- Window attention collapses immediately when initial tokens are evicted; dense attention fails when sequence length exceeds the pre-training window.
- StreamingLLM's accuracy on StreamEval drops to zero when the query-answer distance exceeds the cache size (Table 7), confirming it does **not** extend the context window.
- Models pre-trained with a sink token need only that single token (not 4 initial tokens) for stable streaming, with no degradation on standard benchmarks (Table 4).

### Limitations

- StreamingLLM does **not** extend the context window or provide long-term memory. The model can only utilize information within its current cache. It is unsuitable for tasks requiring long-range dependencies such as long-document QA or summarization.
- Increasing cache size does not consistently lower perplexity (Table 6), suggesting models may not fully utilize the provided context -- a finding consistent with observations by Liu et al. (2023).
- The framework is designed for streaming (sequential generation) settings; it does not address the prefill phase for long prompts.

### Impact and Adoption

StreamingLLM has been integrated into NVIDIA TensorRT-LLM, Intel Extension for Transformers, HuggingFace Transformers, and MLC LLM, indicating substantial practical adoption in production LLM serving infrastructure.

---

## Conclusions

1. **Attention sinks are a fundamental property of SoftMax-based Transformers.** Autoregressive LLMs consistently assign disproportionate attention to initial tokens regardless of semantic content, driven by SoftMax's constraint that attention weights must sum to one. This phenomenon extends beyond autoregressive decoders to encoder models (BERT) and Vision Transformers.

2. **Window attention fails because it disrupts the attention distribution, not because it loses semantic information.** The perplexity collapse is caused by removing the dominant terms in the SoftMax denominator, shifting the entire attention score distribution away from its trained regime.

3. **StreamingLLM enables infinite-length streaming with bounded resources.** By preserving 4 initial tokens as attention sinks alongside a rolling KV cache, LLMs can process arbitrarily long input streams with O(TL) complexity, constant memory, and no fine-tuning.

4. **Dedicated sink tokens improve streaming deployment.** Pre-training with a learnable sink token consolidates the attention sink role into a single token, simplifying streaming deployment while preserving model quality on standard benchmarks.

5. **StreamingLLM is orthogonal to context extension.** The framework does not extend the effective context window; it enables stable generation conditioned on recent tokens. It can be combined with context extension methods (e.g., LongChat, Llama-2-32K) to broaden the cache size of the rolling window.

---

## Core References and Why They Are Referenced

### Positional Encoding and Length Extrapolation

- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE is the positional encoding used by Llama-2, Falcon, and Pythia. StreamingLLM's cache position re-indexing strategy is specifically designed to work with RoPE by caching Keys before the rotary transformation.
- **Press et al. (2022)** -- *ALiBi: Train Short, Test Long.* ALiBi is the positional encoding used by MPT models. StreamingLLM handles ALiBi by applying contiguous linear biases within the cache. ALiBi is also noted as having improved but still limited length extrapolation.
- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* PI is cited as a representative context window extension method. StreamingLLM addresses a different problem (infinite streaming) that PI cannot solve.
- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Another context extension method noted as orthogonal to StreamingLLM's goal; extending the window remains finite.

### Attention Mechanism Analysis

- **Bondarenko et al. (2023)** -- *Quantizable Transformers: Removing Outliers by Helping Attention Heads Do Nothing.* Observed that attention heads allocate outsized values to specific tokens, linking the attention sink phenomenon to quantization outliers.
- **Miller (2023)** -- *Attention is Off by One.* Proposes SoftMax-off-by-One (SoftMax_1) as a remedy for the attention sink problem. This is evaluated in the paper as the "Zero Sink" baseline and found partially effective but inferior to a learnable sink token.
- **Darcet et al. (2023)** -- *Vision Transformers Need Registers.* Concurrent work observing analogous attention concentration on background patch tokens in ViTs. Their "register" tokens parallel the sink token concept, suggesting attention sinks are a universal Transformer phenomenon.

### Models Used in Evaluation

- **Touvron et al. (2023b)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Provides the Llama-2-[7, 13, 70]B models (pre-training window 4K) and their chat variants for streaming QA evaluation.
- **Team (2023)** -- *Introducing MPT-7B.* Provides MPT-[7, 30]B models using ALiBi positional encoding.
- **Almazrouei et al. (2023)** -- *Falcon-40B.* Provides Falcon-[7, 40]B models using RoPE.
- **Biderman et al. (2023)** -- *Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.* Provides Pythia-[2.8, 6.9, 12]B models and the codebase used for from-scratch pre-training experiments with sink tokens.

### Evaluation Benchmarks and Datasets

- **Rae et al. (2020)** -- *Compressive Transformers for Long-Range Sequence Modelling.* Provides the PG19 dataset (100 long books) used for language modeling perplexity evaluation over sequences up to 4M tokens.
- **Bai et al. (2023)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* Used in Appendix D to evaluate StreamingLLM on long-range NLP tasks (QA, summarization), demonstrating that StreamingLLM does not extend context but matches truncation baselines for in-cache performance.
- **Li et al. (2023)** -- *How Long Can Open-Source LLMs Truly Promise on Context Length?* Provides the LongEval benchmark that inspired StreamEval, and the LongChat-7b-v1.5-32k model used to demonstrate complementarity with context extension.
- **Liu et al. (2023)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Referenced to support the observation that LLMs do not fully utilize information within their context window, aligning with StreamingLLM's finding that increasing cache size does not consistently improve perplexity.

### Efficient Attention

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* System-level optimization for attention computation; orthogonal to StreamingLLM's KV cache management.
- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Introduces window attention (the baseline that StreamingLLM improves upon) and sparse attention patterns.
- **Zhang et al. (2023b)** -- *H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models.* KV cache eviction policy based on attention score accumulation; a complementary approach to StreamingLLM's fixed sink + rolling window strategy.

#### Cross-References in Available Papers

- **PI (`2023-06-pi-positional-interpolation`):** Xiao et al. cite PI (Chen et al., 2023) as a representative context window extension method. StreamingLLM addresses a fundamentally different problem: PI extends the finite context window via frequency scaling, while StreamingLLM enables infinite-length streaming without extending the window.
- **RoPE-NTK (`2023-06-rope-ntk`):** bloc97's NTK-aware scaling is cited alongside PI and YaRN as context extension work orthogonal to StreamingLLM. StreamingLLM's position re-indexing within the cache specifically handles RoPE by caching Keys before the rotary transformation.
- **YaRN (`2024-05-yarn-context-extension`):** Peng et al. (2023) is cited as the most recent RoPE-scaling method at the time of publication. Like PI and NTK, YaRN extends the finite window but does not address infinite streaming.
- **Lost in the Middle (`2024-02-lost-in-the-middle`):** Liu et al. (2023) is referenced to support StreamingLLM's observation that LLMs do not fully utilize their context window. StreamingLLM's finding that increasing cache size does not consistently lower perplexity (Table 6) aligns with Liu et al.'s "lost in the middle" phenomenon.
- **LongBench (`2024-08-longbench-bilingual-benchmark`):** Bai et al. (2023) provides the benchmark used in Appendix D to evaluate StreamingLLM on long-range tasks. Results show StreamingLLM with a 4+3496 cache underperforms the truncation baseline due to loss of initial prompt information, but matching the number of sink tokens to the prompt length (1750+1750) restores performance.
- **DroPE (`2025-12-drope-dropping-positional-embeddings`):** DroPE does not directly cite the attention sinks paper, but the phenomena are related: attention sinks reveal that initial tokens serve a structural rather than semantic role in attention computation, while DroPE shows that positional embeddings themselves are a transient training scaffold. Both papers challenge assumptions about which components of the Transformer are essential at inference time.
