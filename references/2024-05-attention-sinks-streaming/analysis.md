---
title: "Efficient Streaming Language Models with Attention Sinks"
authors: "Xiao, Tian, Chen, Han, Lewis"
year: 2024
venue: "ICLR 2024"
paper_type: conference-paper
categories: ["streaming-inference", "attention-analysis"]
scope: ["streaming LLM inference", "attention sink phenomenon", "KV cache management"]
benchmarks_used: ["perplexity-pg19", "arc", "hellaswag", "piqa", "winogrande", "longbench"]
models_introduced: []
models_evaluated: ["llama-2-7b", "llama-2-13b", "llama-2-70b", "falcon-7b", "mpt-7b", "pythia-series"]
key_claims:
  - id: C1
    claim: "Autoregressive LLMs allocate massive attention scores to initial tokens regardless of semantic content — the attention sink phenomenon"
    evidence: "Figure 2, Figure 12 (Appendix F), Table 1, Section 3.1"
    status: supported
  - id: C2
    claim: "Window attention fails because evicting initial tokens removes dominant terms from the SoftMax denominator, not because of lost semantic information"
    evidence: "Table 1 (linebreak substitution recovers PPL from 5158 to 5.60), Figure 3, Section 3.1"
    status: supported
  - id: C3
    claim: "StreamingLLM with 4 sink tokens + sliding window enables stable language modeling over 4M+ tokens across model families and scales"
    evidence: "Figure 5 (Llama-2-[7,13,70]B, Falcon-[7,40]B, Pythia-[2.8,6.9,12]B, MPT-[7,30]B), Section 4.1"
    status: supported
  - id: C4
    claim: "Four initial tokens generally suffice as attention sinks; fewer tokens do not fully restore perplexity, more yield diminishing returns"
    evidence: "Table 2, Section 4.4"
    status: supported
  - id: C5
    claim: "Pre-training with a learnable sink token consolidates the attention sink into a single token without harming convergence or downstream performance"
    evidence: "Table 3, Table 4, Figure 6, Figure 7, Section 3.3 and 4.2"
    status: supported
  - id: C6
    claim: "StreamingLLM achieves up to 22.2x speedup over sliding window with recomputation at equivalent perplexity"
    evidence: "Figure 10, Section 4.5"
    status: supported
  - id: C7
    claim: "StreamingLLM does not extend context length — accuracy drops to zero when query-answer distance exceeds cache size"
    evidence: "Table 7 (Appendix C), Section A (Limitations)"
    status: supported
  - id: C8
    claim: "Increasing cache size does not consistently lower perplexity, suggesting models do not fully utilize the provided context"
    evidence: "Table 6, Section 4.4"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Discovers the attention sink property of standard SoftMax-based Transformer attention and exploits it for streaming inference"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Window attention (the baseline that StreamingLLM improves upon) was introduced by Longformer; StreamingLLM adds sink tokens to stabilize window attention"
  - target: 2024-01-roformer-rope
    type: complementary
    detail: "RoPE is used by Llama-2, Falcon, and Pythia; StreamingLLM's cache position re-indexing requires caching Keys before the rotary transformation"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "ALiBi is used by MPT models; StreamingLLM handles ALiBi by applying contiguous linear biases within the cache rather than jumping biases"
  - target: 2023-06-pi-positional-interpolation
    type: complementary
    detail: "PI extends context windows to a finite length; StreamingLLM addresses a different problem (infinite streaming) that PI cannot solve"
  - target: 2024-05-yarn-context-extension
    type: complementary
    detail: "YaRN is cited as orthogonal to StreamingLLM; context extension broadens the finite window while StreamingLLM enables unbounded streaming"
  - target: 2024-02-lost-in-the-middle
    type: complementary
    detail: "Referenced for the observation that LLMs do not fully utilize long context; aligns with StreamingLLM's finding that increasing cache size does not consistently lower perplexity (Table 6)"
  - target: 2019-11-dark-secrets-of-bert
    type: complementary
    detail: "Kovaleva et al. observed attention concentrating on [CLS] and [SEP] in BERT; the paper extends this to show [SEP] acts as an attention sink in encoder Transformers (Appendix H)"
  - target: 2021-12-transformer-circuits-framework
    type: complementary
    detail: "QK/OV circuit analysis provides a framework for understanding why certain tokens become sinks: when QK produces no strong match, residual mass falls on globally visible tokens"
  - target: 2023-12-landmark-attention-infinite-context
    type: complementary
    detail: "Landmark attention provides an alternative KV cache management strategy; its grouped SoftMax may interact differently with the attention sink phenomenon"
  - target: 2023-07-llama-2-open-foundation-chat
    type: evaluates
    detail: "Llama-2-[7,13,70]B and their Chat variants are the primary models evaluated in StreamingLLM experiments"
  - target: 2025-07-position-bias-single-dimension-scaling
    type: complementary
    detail: "Yu et al. identify positional hidden states as an additional mechanism beyond attention sinks that causes position-dependent attention patterns, and propose scaling these channels to mitigate position bias"
  - target: 2025-07-position-bias-transformers
    type: complementary
    detail: "Position bias analysis provides theoretical context for why attention concentrates at boundary positions, related to the attention sink phenomenon"
  - target: 2025-11-pos2distill-position-bias-distillation
    type: complementary
    detail: "Pos2Distill leverages the attention sink to define the advantageous position for retrieval distillation, exploiting the fact that sink-position overlap with gold content produces high-quality outputs"
  - target: 2025-04-attention-sink-emerges
    type: extended-by
    detail: "Gu et al. comprehensively investigate when and why attention sinks emerge during pre-training, identifying softmax normalization as the root cause and showing sigmoid attention without normalization eliminates sinks up to 1B parameters"
  - target: 2024-12-transformers-need-glasses-over-squashing
    type: complementary
    detail: "Barbero et al. provide a complementary theoretical perspective: attention sinks relate to the over-squashing phenomenon where the causal mask topology funnels information from all tokens through the final position, with initial tokens having exponentially more pathways"
  - target: 2020-04-compressive-transformer-pg19
    type: uses-benchmark
    detail: "Uses PG-19 (introduced by Rae et al., 2020) for streaming perplexity evaluation over sequences up to 4M tokens"
open_questions:
  - question: "Are attention sinks a side effect of SoftMax normalization or do they serve a functional computational role in the residual stream?"
    addressed_by: 2025-04-attention-sink-emerges
  - question: "Would sink token pre-training improve streaming performance at larger scales (validated only at 160M parameters)?"
    addressed_by: null
  - question: "Can StreamingLLM be combined with memory or retrieval mechanisms to provide long-term recall beyond the cache?"
    addressed_by: null
  - question: "Why does increasing cache size sometimes increase perplexity (Table 6), and how does this relate to models' inability to utilize full context?"
    addressed_by: null
---

# Efficient Streaming Language Models with Attention Sinks

**Authors:** Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, Mike Lewis (MIT, Meta AI, CMU, NVIDIA)
**Date:** May 2024, ICLR 2024 (arXiv:2309.17453)

---

## Core Research Problem

Deploying LLMs in streaming applications — such as multi-round dialogue or persistent assistants — requires processing input sequences that grow indefinitely over time. Two challenges make this intractable with standard Transformer-based LLMs: (1) the KV cache grows linearly with sequence length, leading to unbounded memory consumption during decoding, and (2) LLMs cannot generalize beyond their pre-training attention window size (e.g., 4,096 tokens for Llama-2), with performance degrading sharply on longer inputs (Section 1).

Window attention (caching only the most recent L tokens' KV states) is the natural efficiency solution, but empirically collapses the moment the initial tokens are evicted from the cache — even evicting just the first token causes perplexity to spike from 5.40 to 5,158 on Llama-2-13B (Table 1, Figure 3). Sliding window with re-computation rebuilds KV states from the L most recent tokens for each new token, recovering quality but incurring O(TL^2) cost per token, making it impractical for real-time streaming. Context window extension methods (PI, NTK-RoPE, YaRN) expand the finite window but do not enable truly infinite-length generation (Section 2).

The core challenge is: **how to enable LLMs trained with a finite attention window to handle infinite-length input streams without fine-tuning, while maintaining bounded memory and constant decoding latency.**

---

## Problem Solutions

The paper identifies the **attention sink** phenomenon — autoregressive LLMs allocate disproportionately high attention scores to initial tokens regardless of their semantic content — and leverages this insight to propose **StreamingLLM**, a simple framework for infinite-length streaming inference. The solution rests on three observations:

1. **Window attention fails because it evicts attention sinks.** The perplexity spike occurs precisely when initial tokens are removed from the cache, because these tokens serve as a repository for excess attention probability mass required by SoftMax normalization (Section 3.1, Figure 3).

2. **Initial tokens are attention sinks due to SoftMax and autoregressive visibility.** SoftMax requires attention scores to sum to one, so the model must allocate residual attention somewhere even when the current query has no strong match among context tokens. Initial tokens, being visible to all subsequent tokens due to the autoregressive causal mask, are the easiest targets for the model to learn as sinks during pre-training (Section 3.1).

3. **Preserving a few sink tokens alongside the sliding window restores performance.** Keeping just 4 initial tokens' KV states together with the rolling window's KV is sufficient to stabilize the attention score distribution and match the quality of full re-computation (Table 2, Section 3.2).

---

## Approach Details

### Method

StreamingLLM maintains a KV cache with two components:

1. **Attention sink tokens:** The KV states of the first few tokens (4 by default), which anchor the attention computation.
2. **Rolling KV cache:** The KV states of the most recent L tokens, which provide the actual contextual information for language modeling.

When the cache is full and a new token arrives, the oldest token in the rolling window is evicted (not the sink tokens). The total cache size remains constant at (number of sink tokens) + L. This yields O(TL) complexity for streaming over T tokens, identical to window attention (Figure 1d, Figure 4, Section 3.2).

**Position encoding handling:** StreamingLLM assigns positions based on the token's position *within the cache*, not its position in the original text. For a cache containing tokens [0, 1, 2, 3, 6, 7, 8] decoding token 9, positions are assigned as [0, 1, 2, 3, 4, 5, 6, 7] rather than [0, 1, 2, 3, 6, 7, 8, 9]. For RoPE-based models, Keys are cached *before* applying the rotary transformation, and the position transformation is reapplied at each decoding step. For ALiBi-based models, a contiguous linear bias is applied rather than a "jumping" bias (Section 3.2).

### Key Technical Components

**Why initial tokens become sinks.** The SoftMax function prevents all attended tokens from having zero attention:

> SoftMax(x)_i = e^{x_i} / (e^{x_1} + sum_{j=2}^{N} e^{x_j}), where x_1 >> x_j, j in {2, ..., N}

Even when the current embedding has sufficient self-contained information, the model must aggregate some information from other tokens across all heads in all layers. Due to the autoregressive causal mask, initial tokens are visible to all subsequent tokens, making them the path of least resistance for the model to learn as attention dumps (Section 3.1, Equation 1).

**Semantic content is irrelevant.** Replacing the first four tokens with linebreak tokens "\n" restores perplexity from 5,158 to 5.60 on Llama-2-13B (vs. 5.40 with original tokens), confirming that the absolute position, not the semantic value, drives the sink effect (Table 1).

**Number of sink tokens.** Four initial tokens suffice across all tested models. Introducing only 1 token does not fully restore perplexity for models lacking a consistent starting token: for Llama-2-7B, 1 sink token yields PPL 11.88 vs. 9.59 with 4 tokens (cache 4,096). Adding more than 4 yields diminishing returns (Table 2, Section 4.4). This occurs because most models do not have a consistent starting token across pre-training samples — although Llama-2 prepends "<s>", text chunking places a mostly random token at position zero.

**Dedicated sink token for pre-training.** Pre-training with a learnable placeholder token prepended to all training samples consolidates the attention sink into a single token. Three 160M-parameter models were trained from scratch under identical settings (Section 3.3, 4.2):

| Cache Config | 0+1024 | 1+1023 | 2+1022 | 4+1020 |
|---|---|---|---|---|
| Vanilla | 27.87 | 18.49 | 18.05 | 18.05 |
| Zero Sink | 29,214 | 19.90 | 18.27 | 18.01 |
| Learnable Sink | 1,235 | **18.01** | 18.01 | 18.02 |

The learnable sink model achieves stable streaming perplexity with just the sink token (1+1023 = PPL 18.01), while the vanilla model requires 4 initial tokens (4+1020 = PPL 18.05). The sink token does not harm convergence (Figure 6) or downstream task performance (Table 4, Section 4.2).

**SoftMax-off-by-One (Zero Sink).** An alternative formulation:

> SoftMax_1(x)_i = e^{x_i} / (1 + sum_{j=1}^{N} e^{x_j})

This is equivalent to prepending a token with all-zero Key and Value features. It partially alleviates the attention sink problem but the model still relies on other initial tokens as sinks, making it less effective than a learnable sink token (Table 3, Section 3.3).

**Cache position re-indexing.** Critical for correctness with relative position encodings. Without re-indexing, the gap between sink token positions and rolling window positions would create out-of-distribution positional distances. For RoPE, Keys are stored pre-rotation and the rotary transformation is reapplied each step; for ALiBi, contiguous linear biases are applied within the cache (Section 3.2).

### Experimental Setup

**Models:** Llama-2-[7, 13, 70]B (RoPE, 4K pre-training window), MPT-[7, 30]B (ALiBi), Falcon-[7, 40]B (RoPE), Pythia-[2.8, 6.9, 12]B (RoPE). Chat variants (Llama-2-[7, 13, 70]B-Chat) for streaming QA (Section 4).

**Pre-training experiments:** 160M-parameter models trained from scratch using the Pythia-160M codebase on the deduplicated Pile dataset, 143K steps, batch size 256, 8x A6000 GPUs. Three variants: Vanilla, Zero Sink (SoftMax_1), Learnable Sink Token (Section 4.2).

**Language modeling evaluation:** Concatenated PG19 test set (100 long books, up to 4M tokens). Cache sizes: 2,048 for Llama-2, 1,024 for Falcon/Pythia/MPT (half the pre-training window) (Section 4.1).

**Streaming QA evaluation:** ARC-[Easy, Challenge] concatenated into a continuous stream with cache size 1,024; StreamEval benchmark (custom dataset inspired by LongEval — queries every 10 lines, answers 20 lines prior, 100 samples with 100 queries each, each line containing 23 tokens) (Section 4.3, Figure 8).

**Downstream tasks for sink token validation:** ARC-E/C, HellaSwag, LAMBADA, OpenbookQA, PIQA, Winogrande (zero-shot) (Table 4).

**Efficiency benchmarks:** Per-token decoding latency and memory usage on a single NVIDIA A6000 GPU using Llama-2-7B and Llama-2-13B, implemented in HuggingFace Transformers (Section 4.5).

### Key Results

**Language modeling perplexity (PG19, 400K tokens):**

| Model | Window (0+cache) | StreamingLLM (4+cache) |
|---|---|---|
| Llama-2-7B (cache 4,096) | 3,359.95 | 9.59 |
| Falcon-7B (cache 2,048) | 17.90 | 12.12 |
| MPT-7B (cache 2,048) | 460.29 | 14.99 |
| Pythia-12B (cache 2,048) | 21.62 | 12.09 |

**Perplexity on first book (65K tokens), Llama-2-13B:**

| Method | PPL |
|---|---|
| Dense Attention | 5,641 |
| Window Attention (0+1,024) | 5,158 |
| Sliding Window w/ Recomputation | 5.43 |
| StreamingLLM (4+1,020) | 5.40 |

**Streaming QA accuracy (%, cache 1,024):**

| Model | Method | ARC-E | ARC-C |
|---|---|---|---|
| Llama-2-7B-Chat | One-shot | 71.25 | 53.16 |
| | Window | 3.58 | 1.39 |
| | StreamingLLM | 71.34 | 55.03 |
| Llama-2-70B-Chat | One-shot | 91.29 | 78.50 |
| | Window | 0.12 | 0.32 |
| | StreamingLLM | 91.37 | 80.20 |

**Decoding efficiency (Llama-2-7B, single A6000):**

| Cache Size | StreamingLLM (ms) | Recomputation (ms) | Speedup |
|---|---|---|---|
| 256 | 31 | 63 | 2.0x |
| 4,096 | 65 | 1,411 | 22.2x |

- StreamingLLM matches the sliding window with re-computation baseline in perplexity while achieving up to **22.2x speedup** in per-token decoding latency (Figure 10, Section 4.5).
- All tested model families across scales (2.8B–70B) maintain stable perplexity over **4 million tokens** (Figure 5).
- Window attention collapses immediately when initial tokens are evicted; dense attention fails when sequence length exceeds the pre-training window (Figure 3).
- StreamingLLM's accuracy on StreamEval drops to zero when the query-answer distance exceeds the cache size (Table 7, Appendix C), confirming it does **not** extend the context window.
- Models pre-trained with a sink token need only that single token (not 4 initial tokens) for stable streaming, with no degradation on standard benchmarks (Table 3, Table 4).

### Cache Size Ablation

Increasing cache size does not consistently lower perplexity (Table 6, Section 4.4):

| Model | 4+252 | 4+508 | 4+1,020 | 4+2,044 |
|---|---|---|---|---|
| Falcon-7B | 13.61 | 12.84 | **12.34** | 12.84 |
| MPT-7B | **14.12** | 14.25 | 14.33 | 14.99 |
| Pythia-12B | 13.17 | 12.52 | **12.08** | 12.09 |

| Model | 4+508 | 4+1,020 | 4+2,044 | 4+4,092 |
|---|---|---|---|---|
| Llama-2-7B | 9.73 | 9.32 | **9.08** | 9.59 |

For Llama-2-7B, Falcon-7B, and MPT-7B, the best perplexity is not at the largest cache size. This suggests these models may not fully utilize the provided context, consistent with observations by Liu et al. (2023).

### Attention Sinks in Other Architectures

The paper demonstrates that attention sinks extend beyond autoregressive decoders:
- **BERT-base-uncased** exhibits disproportionately high attention scores on the [SEP] token across most layers (Figure 14, Appendix H).
- **Vision Transformers** show analogous attention concentration on background patch tokens (concurrent work by Darcet et al., 2023, who term these "register" tokens).

This suggests attention sinks are a universal property of SoftMax-based Transformer architectures, not specific to autoregressive language models (Section A, Appendix H).

### Impact and Adoption

StreamingLLM has been integrated into NVIDIA TensorRT-LLM, Intel Extension for Transformers, HuggingFace Transformers, and MLC LLM (Impact Statement, page 10).

---

## Limitations and Failure Modes

- **No context extension or long-term memory.** StreamingLLM does not extend the context window. The model can only utilize information within its current cache. On LongBench (Appendix D, Table 8), StreamingLLM with 4+3,496 cache underperforms the truncation baseline (1,750+1,750) because it loses initial input prompt information. Matching the attention sink count to 1,750 recovers performance to the truncation baseline level, confirming the method is limited to in-cache information (Section A, Appendix D).

- **Accuracy drops to zero beyond cache.** On StreamEval, when the query-answer distance exceeds the cache size (e.g., 100 lines / 2,300 tokens with a 4+2,044 cache), accuracy drops to 0.00% (Table 7, Appendix C).

- **Increasing cache size does not consistently improve perplexity.** For Llama-2-7B, perplexity is 9.08 at cache 4+2,044 but rises to 9.59 at 4+4,092 (Table 6). This limitation is not specific to StreamingLLM but reflects a broader issue with LLMs' context utilization.

- **Streaming-only design.** The framework is designed for streaming (sequential token-by-token decoding) settings. It does not address the prefill phase for long prompts (Section A).

- **Sink token pre-training validated only at small scale.** The dedicated sink token experiments use 160M-parameter models. Whether the benefits scale to larger models (7B+) is not validated.

- **Additional sink tokens do not help.** Adding 2 sink tokens during pre-training does not improve streaming performance over 1 sink token, and the model becomes dependent on both tokens (Table 10, Appendix I). This contrasts with ViTs where multiple registers are beneficial (Darcet et al., 2023).

---

## Conclusions

### Contributions

1. **Identified the attention sink phenomenon in autoregressive Transformers.** Autoregressive LLMs consistently assign disproportionate attention to initial tokens regardless of semantic content, driven by SoftMax's constraint that attention weights must sum to one and the autoregressive visibility of initial tokens (Section 3.1, Figure 2, Figure 12).

2. **Explained why window attention fails.** The perplexity collapse is caused by removing the dominant terms in the SoftMax denominator, shifting the entire attention score distribution away from its trained regime — not by losing semantically important information (Table 1, Section 3.1).

3. **Introduced StreamingLLM for infinite-length streaming.** By preserving 4 initial tokens as attention sinks alongside a rolling KV cache, LLMs can process arbitrarily long input streams with O(TL) complexity, constant memory, and no fine-tuning. Stable perplexity is demonstrated over 4M tokens across four model families and scales from 2.8B to 70B (Figure 5, Section 4.1).

4. **Proposed dedicated sink tokens for improved streaming deployment.** Pre-training with a learnable sink token consolidates the attention sink role into a single token, simplifying streaming deployment while preserving model quality on standard benchmarks (Table 3, Table 4, Section 3.3).

5. **Demonstrated practical speedups for streaming inference.** StreamingLLM achieves up to 22.2x per-token decoding speedup over the sliding window with recomputation baseline at equivalent perplexity, with comparable memory footprint (Figure 10, Section 4.5).

6. **Showed attention sinks are universal across Transformer architectures.** The phenomenon extends to encoder models (BERT concentrates attention on [SEP]) and Vision Transformers (concurrent work by Darcet et al. on "register" tokens), suggesting a fundamental property of SoftMax attention (Appendix H, Section A).

### Implications

1. **Streaming deployment is feasible for existing LLMs.** StreamingLLM decouples the pre-training window size from the generation length, enabling persistent LLM deployments (e.g., day-long conversations) with bounded resources and no model modification.

2. **Future LLMs should include a dedicated sink token.** The paper recommends training all future LLMs with a sink token prepended to all training samples to optimize streaming deployment. This recommendation applies to any SoftMax-based autoregressive model. [Inference: Mistral-7B's sliding window attention with initial token retention may implicitly leverage this insight.]

3. **Context extension and streaming are orthogonal.** StreamingLLM can be combined with context-extended models (e.g., LongChat-7b-v1.5-32k, Llama-2-7B-32K-Instruct) to broaden the rolling cache window. Context extension increases the finite window; StreamingLLM makes any finite window work indefinitely (Figure 9, Section 4.3).

4. **SoftMax normalization has under-appreciated structural consequences.** The attention sink phenomenon suggests that the sum-to-one constraint of SoftMax forces models to develop structural patterns (concentrating residual probability on globally visible tokens) that may interact with quantization outliers, position biases, and context utilization in ways not yet fully understood. [Inference: this may motivate alternatives like SoftMax_1 or gated attention mechanisms.]

---

## Key Claims

1. **C1: Attention sinks are a universal property of autoregressive Transformers.** LLMs consistently assign massive attention scores to initial tokens regardless of their semantic content. In Llama-2-7B with 4,096-token sequences, attention scores on the first token exceed 50% of total attention in most layers beyond the bottom two (Figure 2, Figure 12, Appendix F). Status: **supported**.

2. **C2: Window attention fails due to SoftMax distribution shift, not lost semantics.** Replacing the first four tokens with linebreak tokens "\n" restores perplexity from 5,158 to 5.60 (vs. 5.40 with original tokens) on Llama-2-13B (Table 1). The failure is caused by removing the dominant terms e^{x_1} from the SoftMax denominator (Equation 1, Section 3.1). Status: **supported**.

3. **C3: StreamingLLM enables stable streaming over 4M+ tokens.** All tested model families — Llama-2-[7,13,70]B, Falcon-[7,40]B, Pythia-[2.8,6.9,12]B, MPT-[7,30]B — maintain stable perplexity when processing 4 million tokens with StreamingLLM, matching the sliding window with recomputation baseline (Figure 5, Section 4.1). Status: **supported**.

4. **C4: Four initial tokens suffice as attention sinks.** Introducing 4 initial tokens generally restores perplexity; 1–2 tokens are insufficient (Llama-2-7B: 1 token = PPL 11.88, 4 tokens = PPL 9.59, cache 4,096). Adding more than 4 yields diminishing returns (Table 2, Section 4.4). Status: **supported**.

5. **C5: A dedicated learnable sink token eliminates the need for multiple initial tokens.** A 160M-parameter model pre-trained with a sink token achieves PPL 18.01 with just the sink token (1+1,023), matching the vanilla model with 4 initial tokens (PPL 18.05 at 4+1,020). The sink token does not harm convergence or zero-shot accuracy across 7 benchmarks (Table 3, Table 4, Figure 6). Status: **supported**.

6. **C6: StreamingLLM achieves up to 22.2x decoding speedup.** At cache size 4,096, StreamingLLM decodes at 65ms/token vs. 1,411ms/token for sliding window with recomputation on Llama-2-7B (Figure 10). The speedup grows with cache size because StreamingLLM scales linearly while recomputation scales quadratically (Section 4.5). Status: **supported**.

7. **C7: StreamingLLM does not extend context length.** On StreamEval with Llama-2-7B-32K-Instruct, accuracy drops to 0.00% when the query-answer distance (100 lines, 2,300 tokens) exceeds the cache capacity (4+2,044 = 2,048 tokens). Accuracy is maintained only when the relevant information falls within the cache window (Table 7, Appendix C). Status: **supported**.

8. **C8: Larger cache does not consistently improve perplexity.** For Llama-2-7B, best perplexity is 9.08 at cache 4+2,044, rising to 9.59 at 4+4,092 (Table 6). Similar non-monotonic behavior is observed for Falcon-7B and MPT-7B. This aligns with Liu et al.'s observation that LLMs do not fully utilize long contexts (Section 4.4). Status: **supported**.

---

## Open Questions

1. **Are attention sinks a side effect of SoftMax normalization or do they serve a functional computational role in the residual stream?** The paper attributes sinks to SoftMax's sum-to-one constraint but does not determine whether sink tokens carry useful information (e.g., global statistics) through their Value vectors or merely absorb unused probability mass. Darcet et al.'s finding that ViT "registers" store global image information suggests a functional role. Not yet addressed by subsequent work in this directory.

2. **Would sink token pre-training improve streaming performance at larger scales?** The dedicated sink token experiments are conducted at 160M parameters only. Whether the single-token sufficiency and zero-cost-to-benchmarks results hold for 7B+ parameter models is unvalidated. Not addressed.

3. **Can StreamingLLM be combined with memory or retrieval mechanisms to provide long-term recall beyond the cache?** The paper explicitly notes StreamingLLM is unsuitable for tasks requiring long-term memory. Combining it with external memory, retrieval augmentation, or H2O-style KV cache eviction policies (Zhang et al., 2023b) could extend its utility. Not addressed.

4. **Why does increasing cache size sometimes increase perplexity, and how does this relate to models' inability to utilize full context?** Table 6 shows non-monotonic perplexity as a function of cache size for multiple models. The paper notes this aligns with Liu et al.'s (2023) findings but does not offer an explanation. Not addressed.

---

## Core References and Why They Are Referenced

### Positional Encoding and Length Extrapolation

- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE is the positional encoding used by Llama-2, Falcon, and Pythia. StreamingLLM's cache position re-indexing strategy caches Keys before the rotary transformation and reapplies it at each decoding step.

- **Press et al. (2022)** -- *ALiBi: Train Short, Test Long.* ALiBi is the positional encoding used by MPT models. StreamingLLM handles ALiBi by applying contiguous linear biases within the cache. ALiBi's improved but still limited length extrapolation motivates the need for streaming solutions.

- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* PI is cited as a representative context window extension method that expands a finite window. StreamingLLM addresses a different problem (infinite streaming) that PI cannot solve.

- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Another context extension method noted as orthogonal to StreamingLLM; context extension remains finite while StreamingLLM enables unbounded streaming.

### Attention Mechanism Analysis

- **Bondarenko et al. (2023)** -- *Quantizable Transformers: Removing Outliers by Helping Attention Heads Do Nothing.* Observed that attention heads allocate outsized values to specific tokens, linking the attention sink phenomenon to quantization outliers.

- **Miller (2023)** -- *Attention is Off by One.* Proposes SoftMax-off-by-One (SoftMax_1) as a remedy for attention sinks. Evaluated in the paper as the "Zero Sink" baseline and found partially effective but inferior to a learnable sink token (Table 3).

- **Darcet et al. (2023)** -- *Vision Transformers Need Registers.* Concurrent work observing analogous attention concentration on background patch tokens in ViTs. Their "register" tokens parallel the sink token concept, suggesting attention sinks are a universal Transformer phenomenon. A key difference: ViT registers function as global information holders in intermediate layers, whereas attention sinks are positionally determined in autoregressive models.

- **Han et al. (2023)** -- *LM-Infinite: Simple On-the-Fly Length Generalization for Large Language Models.* Concurrent work using a "Lambda-shaped" attention pattern and reconfiguring position encoding distances. Similar methodology to StreamingLLM but does not identify or analyze the attention sink phenomenon.

### Models Used in Evaluation

- **Touvron et al. (2023b)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Provides the Llama-2-[7, 13, 70]B models (pre-training window 4K) and their Chat variants for streaming QA evaluation.

- **Team (2023)** -- *Introducing MPT-7B.* Provides MPT-[7, 30]B models using ALiBi positional encoding, ensuring StreamingLLM is validated on non-RoPE architectures.

- **Almazrouei et al. (2023)** -- *Falcon-40B.* Provides Falcon-[7, 40]B models using RoPE, extending the evaluation to a third model family.

- **Biderman et al. (2023)** -- *Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.* Provides Pythia-[2.8, 6.9, 12]B models and the codebase used for the 160M-parameter sink token pre-training experiments.

### Evaluation Benchmarks and Datasets

- **Rae et al. (2020)** -- *Compressive Transformers for Long-Range Sequence Modelling.* Provides the PG19 dataset (100 long books) used for language modeling perplexity evaluation over sequences up to 4M tokens.

- **Li et al. (2023)** -- *How Long Can Open-Source LLMs Truly Promise on Context Length?* Provides the LongEval benchmark that inspired StreamEval, and the LongChat-7b-v1.5-32k model used to demonstrate complementarity with context extension methods.

- **Liu et al. (2023)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Referenced to support the observation that LLMs do not fully utilize information within their context window, aligning with StreamingLLM's finding that increasing cache size does not consistently improve perplexity (Table 6).

- **Bai et al. (2023)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* Used in Appendix D to evaluate StreamingLLM on long-range NLP tasks (QA, summarization), demonstrating that StreamingLLM does not extend context but matches truncation baselines for in-cache performance.

### Efficient Attention and KV Cache Management

- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Introduces window attention (the baseline that StreamingLLM improves upon) and sparse attention patterns. StreamingLLM's key insight is that window attention fails not because of its limited receptive field but because it evicts attention sinks.

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* System-level optimization for attention computation; orthogonal to StreamingLLM's KV cache management strategy.

- **Zhang et al. (2023b)** -- *H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models.* KV cache eviction policy based on accumulated attention scores. Complementary to StreamingLLM's fixed sink + rolling window strategy — H2O dynamically selects which tokens to retain based on attention patterns.

### Attention Sink Precursors

- **Kovaleva et al. (2019)** -- *Revealing the Dark Secrets of BERT.* Observed attention concentrating on [CLS] and [SEP] special tokens in BERT, an early observation related to the attention sink phenomenon. The paper extends this to show BERT's [SEP] token acts as an attention sink (Appendix H).
