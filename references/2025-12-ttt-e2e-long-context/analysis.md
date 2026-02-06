---
title: "End-to-End Test-Time Training for Long Context"
authors: "Tandon, Dalal, Li, Koceja, Rød, Buchanan, Wang, Leskovec, Koyejo, Hashimoto, Guestrin, McCaleb, Choi, Sun"
year: 2025
venue: "arXiv 2025"
paper_type: preprint
categories: ["architecture", "context-extension", "streaming-inference"]
scope: ["long-context language modeling up to 128K tokens", "3B parameter models trained from scratch", "Books and DCLM evaluation corpora"]
benchmarks_used: ["perplexity-books", "perplexity-dclm", "ruler", "niah"]
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "TTT-E2E scales with context length in the same way as Transformer with full attention for 3B models trained with 164B tokens"
    evidence: "Figure 1 left panel, Section 3.4"
    status: supported
    scope: "3B models, 164B training tokens, up to 128K context, Books evaluation"
    magnitude: "Loss delta with full attention stays roughly constant across 8K-128K"
  - id: C2
    claim: "TTT-E2E has constant inference latency regardless of context length, making it 2.7x faster than full attention for 128K context"
    evidence: "Figure 1 right panel, Section 3.7"
    status: supported
    scope: "3B models, H100 GPU, prefill latency measurement"
    magnitude: "2.7x faster at 128K; ~0.02 sec per 1K tokens constant"
  - id: C3
    claim: "Mamba 2 and Gated DeltaNet do not scale with context length as effectively as full attention"
    evidence: "Figure 1 left panel, Section 3.4"
    status: supported
    scope: "3B models, 164B training tokens, 8K-128K context"
    magnitude: "Loss delta worsens beyond 32K for both methods"
  - id: C4
    claim: "TTT-E2E is the only method that always achieves lower losses than full attention throughout the entire context length"
    evidence: "Figure 6, Section 3.4.1"
    status: supported
    scope: "3B models, 32K and 128K context, Books evaluation, token-level breakdown"
  - id: C5
    claim: "Transformer with full attention dramatically outperforms all other methods including TTT-E2E on Needle-in-a-Haystack retrieval tasks"
    evidence: "Table 2, Section 3.5"
    status: supported
    scope: "3B models, S-NIAH tasks from RULER at 128K"
    magnitude: "Full attention: 0.99 vs TTT-E2E: 0.06 on S-NIAH-1 passkey retrieval at 128K"
  - id: C6
    claim: "TTT-E2E exhibits a similar scaling trend to full attention under large training compute budget"
    evidence: "Figure 5, Section 3.3"
    status: supported
    scope: "125M-3B models, up to 5x Chinchilla token budget, DCLM and Books 32K evaluation"
  - id: C7
    claim: "Training latency is a significant limitation: TTT-E2E is 3.4x slower than full attention at 8K context"
    evidence: "Figure 8, Section 3.7"
    status: supported
    scope: "H200 GPU training"
    magnitude: "3.4x slower at 8K; 1.2x faster at 128K"
cross_references:
  - target: 2024-07-mamba-2-transformers-ssms
    type: evaluates
    detail: "Evaluates Mamba 2 as a baseline; shows it does not scale with context length as well as full attention"
  - target: 2025-04-gated-delta-networks
    type: evaluates
    detail: "Evaluates Gated DeltaNet as a baseline; shows it does not scale with context length as well as full attention"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Applies test-time training to a standard Transformer architecture with sliding-window attention"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Uses sliding-window attention as base architecture, the core local-attention mechanism from Longformer"
open_questions:
  - question: "Can TTT-E2E training latency be significantly reduced, e.g., by initializing from a pre-trained Transformer or using custom attention kernels that support gradients of gradients?"
    addressed_by: null
  - question: "Does TTT-E2E scale to very long contexts beyond 128K (e.g., 1M+ tokens)?"
    addressed_by: null
  - question: "Can gating mechanisms guard against spurious inputs during TTT self-training on decoded tokens?"
    addressed_by: null
  - question: "How does TTT-E2E perform after instruction fine-tuning or RLHF?"
    addressed_by: null
---

# End-to-End Test-Time Training for Long Context

**Authors:** Arnuv Tandon, Karan Dalal, Xinhao Li, Daniel Koceja, Marcel Rød, Sam Buchanan (Astera Institute, NVIDIA, Stanford University, UC Berkeley, UC San Diego)
**Date:** December 2025, arXiv:2512.23675

---

## Core Research Problem

Transformers with self-attention struggle to efficiently process long context because full attention must scan through the keys and values of all previous tokens for every new token. Its cost per token grows linearly with context length and quickly becomes prohibitive. As an alternative, RNNs such as Mamba 2 and Gated DeltaNet have constant cost per token but become less effective in longer context -- they do not scale with context length the way full attention does (Figure 1).

Modern architectures attempt to approximate full attention with sliding windows, stack attention and RNN layers together, or use hybrid designs, but these techniques remain less effective than full attention at using longer context.

**The core challenge: how to achieve the scaling properties of full attention with the constant inference cost of RNNs for long-context language modeling.**

---

## Problem Solutions

The paper reformulates long-context language modeling as a **continual learning problem** rather than an architecture design problem. The key insight is that training with next-token prediction compresses data into model weights, and this same compression can happen at test time on the given context.

1. **Test-Time Training (TTT) via next-token prediction:** At test time, the model continues training on the context it reads, compressing information into its MLP weights rather than storing it in a KV cache.
2. **End-to-End meta-learning at training time:** The model's initialization is optimized via meta-learning so that it produces low loss *after* TTT, rather than out of the box. This eliminates the mismatch between training and test-time behavior.
3. **Mini-batch TTT with sliding-window attention:** Tokens are grouped into mini-batches for TTT gradient steps, and sliding-window attention provides local context within each batch, addressing both efficiency and the "bigram problem" of purely sequential TTT.

---

## Approach Details

### Method

The method operates on a standard Transformer with sliding-window attention (SWA). At test time, the model's MLP layers are updated via gradient descent on the next-token prediction loss computed over mini-batches of context tokens.

**Token-level test loss.** For a sequence `X = (x_1, ..., x_T)` and model `f` with weights `W`, the token-level test loss at time `t` is:

> `l_t(W_{t-1}) = CE(f(x_{t-1}; W_{t-1}), x_t)`

**Online gradient descent (b = 1).** Weights are updated at each token:

> `W_t = W_{t-1} - eta * grad(l_t(W_{t-1}))`

**Mini-batch TTT (general form).** To improve parallelism and stability, tokens are partitioned into `T/b` mini-batches of size `b`:

> `W_i = W_{i-1} - (eta/b) * sum_{t=(i-1)b+1}^{ib} grad(l_t(W_{i-1}))`

The output prediction is `p_{T+1} = f(x_T; W_{T/b})`.

**E2E training loss.** At training time, the E2E loss is the average test loss after TTT:

> `L(W_0; X) = (1/T) * sum_{i=1}^{T/b} sum_{t=(i-1)b+1}^{ib} l_t(W_{i-1})`

The initial weights `W_0` are optimized via meta-learning: `grad(L(W_0))` involves gradients of gradients, since `l_t(W_{i-1})` depends on `W_0` through the chain of gradient updates. This is the "E2E at training time" component.

**Contrast with TTT-naive.** The naive approach (dynamic evaluation) optimizes `L_naive(W_0; X) = (1/T) * sum l_t(W_0)` -- a static model that does not account for weight updates at test time. TTT-E2E performs almost as well as full attention on the toy example, while TTT-naive performs only slightly better than the no-attention baseline (Figure 2).

### Key Technical Components

**TTT only MLP layers.** Embedding layers, normalization layers, and attention layers are frozen during TTT. Only MLP layers are updated, as updating attention layers in the inner loop causes instability in the outer loop.

**TTT only the last 1/4 of blocks.** For a model with `L` blocks, only the last `L/4` blocks have their MLP layers updated. This trades off between compression capacity (more layers = more storage) and computational cost (more layers = more backward passes). Updating 6 layers performs comparably to 12 layers for a 24-block 760M model, while 1 or 3 layers fail to scale with context length (Figure 4, right panel).

**Two MLP layers per block.** In blocks updated during TTT, a second static MLP is added as "safe storage" for pre-trained knowledge. The hidden dimension of all MLPs throughout the network is reduced to maintain the total parameter count. The updatable MLP has 88M parameters (5x larger than the multi-head MLP in TTT-KVB's 18M) for the 760M model.

**Default hyperparameters for main results (3B model, 128K context):**
- Sliding window size `k = 8K`
- TTT mini-batch size `b = 1K`
- Updated layers: last 1/4 of blocks
- Constraint: `k >= b` (so the model can attend to the full mini-batch before TTT updates weights)

**QK norm.** Normalizing queries and keys in attention layers makes training more stable for TTT-E2E and improves all Transformer baselines.

**RoPE.** The architecture uses RoPE with `theta = 500K` for pre-training at 8K context, and adjusts `theta` for extension fine-tuning following a log-linear relationship with context length (`theta = 10M` at 128K).

### Alternative Derivation via Key-Value Binding

Section 2.4 provides an alternative derivation starting from TTT-KVB (Zhang et al., 2025). The key differences between TTT-KVB and TTT-E2E are:
1. TTT-KVB uses layer-wise reconstruction losses; TTT-E2E uses a single next-token prediction loss at the end.
2. TTT-KVB has additional outer-loop parameters `theta_K` and `theta_V` per layer; TTT-E2E has none.
3. TTT-KVB updates an MLP in every block; TTT-E2E updates only the last 1/4 of blocks.
4. TTT-KVB uses smaller multi-head MLPs with LoRA; TTT-E2E uses regular full-size MLPs.

Replacing the KVB loss with next-token prediction loss is the key step (Table 1: loss drops from 2.818 to 2.806). The final TTT-E2E method has 5x larger hidden state (88M vs 18M) and half the inference latency compared to the multi-head variant.

### Experimental Setup

**Training pipeline.** Two stages: (1) pre-training at 8K context on DCLM-Baseline (a filtered Common Crawl subset, 3.8T tokens available), (2) extension fine-tuning on Books (a standard long-context dataset from the Pile) at target context lengths up to 128K. Fine-tuning uses 5% of the pre-training token count.

**Model sizes.** Five sizes following GPT-3/Mamba 2 recipes: 125M, 350M, 760M, 1.3B, 2.7B (referred to as 3B). The basic recipe uses Chinchilla-optimal token counts for pre-training (Table 3).

| Params | Blocks | Dim  | Heads | Pre-train LR | Pre-train tokens | Fine-tune LR | Fine-tune tokens |
|--------|--------|------|-------|-------------|-----------------|-------------|-----------------|
| 125M   | 12     | 768  | 12    | 3e-3        | 2.5B            | 4e-4        | 125M            |
| 350M   | 24     | 1024 | 16    | 1.5e-3      | 7B              | 4e-4        | 350M            |
| 760M   | 24     | 1536 | 16    | 1.25e-3     | 15B             | 4e-4        | 750M            |
| 1.3B   | 24     | 2048 | 32    | 1e-3        | 26B             | 4e-4        | 1.3B            |
| 3B     | 32     | 2560 | 32    | 8e-4        | 54B             | 4e-4        | 2.7B            |

**Baselines (6 methods, all at same window size k = 8K):**
1. Transformer with full attention
2. Transformer with Sliding-Window Attention (SWA)
3. Hybrid SWA and full attention (5:1 ratio, Gemma-style)
4. Mamba 2 (hybrid with Mamba 2 and SWA layers)
5. Gated DeltaNet (hybrid with Gated DeltaNet and SWA layers)
6. TTT-KVB (hybrid with TTT-MLP layers using KV Binding and SWA layers)

All baselines implemented in JAX (1--3) or using official code (4--6). RNN baselines upgraded to FlashAttention 3 for fair latency comparison. All use QK norm in attention layers.

**Evaluation.** Language modeling loss (log perplexity) on held-out Books partition. S-NIAH tasks from RULER at 128K for retrieval. Qwen-3-8B-Base as evaluator for decoding quality.

**Reproducibility.** Code and datasets are publicly available at https://github.com/test-time-training/e2e. All experiments are reproducible from the basic recipe in Appendix B. Learning rate is the only swept hyperparameter for fine-tuning (best: 4e-4 across all sizes and context lengths).

### Key Results

#### Scaling with Context Length (3B, 164B tokens)

| Method                    | 8K loss | 16K loss | 32K loss | 64K loss | 128K loss |
|---------------------------|---------|----------|----------|----------|-----------|
| Full attention            | 2.254   | 2.263    | 2.278    | 2.285    | 2.286     |
| SWA                       | 2.267   | 2.285    | 2.298    | 2.310    | 2.316     |
| Hybrid SWA + full (5:1)   | 2.256   | 2.268    | 2.282    | 2.289    | 2.295     |
| Mamba 2                   | 2.282   | 2.292    | 2.301    | 2.313    | 2.318     |
| Gated DeltaNet            | 2.277   | 2.283    | 2.289    | 2.303    | 2.308     |
| TTT-KVB                   | 2.273   | 2.279    | 2.289    | 2.299    | 2.308     |
| TTT-E2E (ours)            | 2.243   | 2.250    | 2.263    | 2.273    | 2.275     |

*Values read from Figure 9 (absolute loss plot). TTT-E2E is the only method that consistently outperforms full attention at all context lengths.*

- TTT-E2E turns the worst baseline (SWA, which is its architecture without TTT) into the best method.
- The loss delta between TTT-E2E and full attention stays roughly constant from 8K to 128K, while other methods' deltas worsen.
- For SWA, Mamba 2, Gated DeltaNet, and TTT-KVB, longer context beyond 32K actually hurts loss -- a trend attributed to higher gradient variance from fewer sequences per batch during fine-tuning.

#### Needle-in-a-Haystack (S-NIAH from RULER, 3B models at 128K)

| Method           | S-NIAH-1 (passkey) | S-NIAH-2 (number) | S-NIAH-3 (UUID) |
|------------------|--------------------:|-------------------:|----------------:|
| Full attention   | 0.99               | 0.86               | 0.64            |
| SWA              | 0.07               | 0.05               | 0.05            |
| Hybrid SWA+full  | 0.21               | 0.29               | 0.04            |
| Mamba 2          | 0.07               | 0.05               | 0.04            |
| Gated DeltaNet   | 0.07               | 0.05               | 0.03            |
| TTT-KVB          | 0.01               | 0.05               | 0.04            |
| TTT-E2E          | 0.06               | 0.05               | 0.03            |

*Values at 128K context. Full attention dramatically outperforms all other methods, supporting the intuition that full attention's strength lies in nearly lossless recall.*

#### Inference Latency (prefill, H100, 3B models)

| Method           | 8K (sec/1K tok) | 128K (sec/1K tok) | Trend        |
|------------------|----------------:|------------------:|-------------|
| Full attention   | ~0.015          | ~0.07             | Linear growth |
| SWA              | ~0.015          | ~0.015            | Constant     |
| TTT-E2E          | ~0.02           | ~0.025            | ~Constant    |
| Mamba 2          | ~0.03           | ~0.03             | Constant     |
| Gated DeltaNet   | ~0.035          | ~0.04             | Constant     |

*TTT-E2E has constant latency like RNNs and SWA. At 128K, it is 2.7x faster than full attention.*

#### Training Latency (H200)

| Method           | 8K (sec/1K tok) | 128K (sec/1K tok) |
|------------------|----------------:|------------------:|
| Full attention   | ~0.07           | ~0.35             |
| SWA              | ~0.04           | ~0.04             |
| TTT-E2E          | ~0.24           | ~0.30             |

*TTT-E2E training is 3.4x slower than full attention at 8K but 1.2x faster at 128K. Training latency is the method's most significant practical limitation.*

### Ablation Summary

**Sliding window size k** (760M, DCLM): All methods improve with larger k. TTT-E2E has similar sensitivity to SWA and Gated DeltaNet. Default: k = 8K.

**TTT mini-batch size b** (760M, DCLM): Larger b significantly hurts performance for both TTT-E2E and TTT-KVB. Smaller b < 1K hurts hardware utilization and stability. Default: b = 1K.

**Architecture without TTT** (760M): Without TTT, the loss of TTT-E2E's modified architecture (2.825) and TTT-KVB's architecture (2.826) are nearly identical to standard full attention (2.827), confirming that the architectural modifications play a minor role and the gains come from TTT itself.

**TTT-E2E on top of full attention** (760M, DCLM, 8K): TTT-E2E improves test loss by 0.018 even on top of full attention, and this improvement does not diminish as k increases, suggesting TTT-E2E provides an orthogonal benefit beyond compensating for the gap between SWA and full attention.

---

## Limitations and Failure Modes

1. **Near-complete failure on retrieval tasks.** TTT-E2E scores 0.06 on S-NIAH-1 (passkey retrieval) at 128K, compared to 0.99 for full attention (Table 2). The compression mechanism inherently discards details it deems irrelevant, including synthetic needle strings. This is the most significant functional limitation.

2. **Training latency.** TTT-E2E takes gradients of gradients, making training 3.4x slower than full attention at 8K context (Figure 8). Since most training compute is spent on short-context pre-training, this is a major practical limitation. The current implementation cannot use cuDNN FlashAttention at training time because it does not support gradients of gradients.

3. **Instability at small scales during fine-tuning.** Fine-tuning 125M and 350M models at 64K and 128K context lengths is unstable, requiring doubled batch sizes and limiting evaluation to 32K context for scaling experiments (Section 3.3, footnotes 6-7).

4. **Limited evaluation scope for generation.** The decoding evaluation (Section 3.6) uses only base models evaluated by an external LLM (Qwen-3-8B-Base), without instruction fine-tuning or RLHF. The practical deployment scenario is not directly evaluated.

5. **Sensitivity to tokenizer and data quality.** Anecdotal observations indicate that switching from Llama 2 to Llama 3 tokenizer improved advantage by ~0.01, and switching from SlimPajama to DCLM changed scaling behavior after 48B tokens (Section 3.3). These effects are not systematically studied.

### Scope and Comparability

- **All models are trained from scratch** with the same recipe. Results may not generalize to fine-tuning existing pretrained models.
- **Evaluation is primarily on Books** (language modeling loss). No evaluation on downstream NLU/NLG tasks (e.g., LongBench, InfiniteBench).
- **Only models up to 3B parameters** are evaluated. The boundary between RNN-advantageous and attention-advantageous compute regimes (roughly 760M/48B tokens) may shift at larger scales.
- **No variance estimates** are reported for any experiments.
- **Hardware-specific.** Latency measurements are on H100 (inference) and H200 (training). No measurements on consumer GPUs or with different batch sizes.

---

## Conclusions

### Contributions

1. **Reformulation of long-context modeling as continual learning.** The paper shows that continuing to train a Transformer at test time via next-token prediction, with meta-learned initialization, achieves the same context-length scaling as full attention while maintaining constant inference latency.

2. **End-to-End training for TTT.** Unlike prior TTT methods (TTT-naive / dynamic evaluation) where the training loss does not match the test-time procedure, TTT-E2E is end-to-end at both training time (via meta-learning) and test time (via next-token prediction), closing the train-test mismatch.

3. **Empirical demonstration that RNN baselines do not scale with context length.** Mamba 2 and Gated DeltaNet -- the most popular RNN alternatives -- produce worse loss deltas relative to full attention as context increases from 8K to 128K.

4. **Scaling analysis.** Under sufficient training compute (roughly >760M parameters or >48B tokens), TTT-E2E follows a similar scaling trend to full attention across both model size and token count.

5. **Alternative derivation from TTT-KVB.** Shows that replacing layer-wise reconstruction loss with next-token prediction loss, removing outer-loop parameters, and using regular full-size MLPs recovers TTT-E2E, providing a connection between the continual-learning and architecture-design perspectives.

### Implications

1. **Compression vs. recall as distinct memory mechanisms.** TTT-E2E excels at compression-based use of context (lower perplexity) but fails at lossless recall (NIAH). Full attention excels at recall. This suggests that the two mechanisms are complementary, and combining them (e.g., different context lengths for each) may produce even stronger models. *Speculative.*

2. **Standard infrastructure advantage.** TTT-E2E's hidden state takes the form of regular MLP weights that can be sharded across GPUs with standard tools, unlike RNN hidden states that must fit on individual chips. This may be a practical advantage at very large scales. *Speculative.*

3. **The advantage of focusing on the present.** The paper offers an intuitive explanation for why TTT-E2E beats full attention on early tokens: full attention weights must prepare for all possible futures, while TTT-E2E weights only need to be good for the present mini-batch, since future weights will be produced by TTT (Section 3.4.1).

---

## Key Claims

1. **TTT-E2E matches full attention's context-length scaling.** For 3B models trained with 164B tokens (3x Chinchilla), TTT-E2E scales with context length in the same way as Transformer with full attention, maintaining a roughly constant loss advantage across 8K--128K (Figure 1 left, Section 3.4). Status: **supported** (single training recipe, Books evaluation only, no variance estimates).

2. **Constant inference latency.** TTT-E2E has constant prefill latency regardless of context length, 2.7x faster than full attention at 128K context on H100 (Figure 1 right, Section 3.7). Status: **supported** (H100 only, 3B model only).

3. **RNN baselines fail to scale with context.** Mamba 2 and Gated DeltaNet produce worse loss deltas relative to full attention in longer context, while other methods (SWA, Hybrid, TTT-KVB) also degrade (Figure 1 left). For SWA, Mamba 2, Gated DeltaNet, and TTT-KVB, longer context beyond 32K actually hurts absolute loss (Figure 9). Status: **supported** (3B scale, Books evaluation, single recipe).

4. **TTT-E2E always achieves lower loss than full attention across all token positions.** Token-level loss breakdown shows TTT-E2E beats full attention at every position in both 32K and 128K contexts, with the advantage concentrated in earlier tokens (Figure 6, Section 3.4.1). Status: **supported** (3B models, Books evaluation).

5. **Full attention dramatically outperforms on retrieval.** On S-NIAH tasks from RULER at 128K, full attention achieves 0.99 on passkey retrieval while TTT-E2E achieves only 0.06 (Table 2, Section 3.5). Status: **supported** (3B models, 128K context, S-NIAH subtasks only).

6. **Similar scaling trend under large compute budget.** Beyond roughly 760M parameters or 48B training tokens, TTT-E2E follows a similar trend to full attention for scaling with both model size and number of tokens (Figure 5, Section 3.3). Below this boundary, RNN-like methods (including TTT-E2E) have an advantage. Status: **supported** (up to 3B, up to 5x Chinchilla tokens).

7. **Training latency is a significant limitation.** Training is 3.4x slower than full attention at 8K context due to computing gradients of gradients, though it becomes 1.2x faster at 128K (Figure 8). Status: **supported**.

---

## Open Questions

1. **Can training latency be reduced to match standard Transformers?** The paper suggests two directions: custom attention kernels that support gradients of gradients (eliminating cuDNN FlashAttention limitation), and initializing TTT-E2E from a pre-trained Transformer (so TTT-specific training is only a small fraction of total compute). Neither is validated.

2. **Does TTT-E2E scale beyond 128K context?** The paper only evaluates up to 128K. Whether the constant loss delta with full attention persists at 1M+ tokens is unknown.

3. **How does TTT-E2E perform on downstream tasks after instruction tuning?** All evaluations are on base models with language modeling loss or synthetic retrieval. Real-world utility requires instruction fine-tuning and task-specific evaluation.

4. **Can TTT-E2E be combined with gating mechanisms for self-training on decoded tokens?** The paper notes that gating in RNNs can guard against spurious inputs, and suggests that self-generation during TTT (e.g., filtering or rephrasing the current mini-batch) could play a similar role.

5. **What is the effect of TTT-E2E at scales beyond 3B?** The scaling analysis shows the advantage over full attention diminishes with more compute. Whether this trend continues or stabilizes at larger scales is unknown.

---

## Core References and Why They Are Referenced

### Direct Predecessors (Test-Time Training)

- **Sun et al. (2023)** -- *Learning to (Learn at Test Time).* Introduced the TTT framework for language models, formulating learning problems at test time.
- **Sun et al. (2024)** -- *Learning to (Learn at Test Time): RNNs with Expressive Hidden States.* TTT-KVB predecessor: proposed TTT layers with MLP hidden states as drop-in replacements for self-attention, using key-value binding loss.
- **Zhang et al. (2025)** -- *Test-Time Training Done Right.* TTT-KVB with hybrid architecture (TTT-MLP + SWA layers); the starting point for the alternative derivation in Section 2.4.
- **Clark et al. (2022)** -- *Meta-Learning Fast Weight Language Models.* Most relevant prior work in methodology: adds MLP fast weights to a Transformer, updated via next-token prediction on mini-batches, with meta-learned initialization.

### RNN Baselines

- **Dao and Gu (2024)** -- *Transformers Are SSMs.* Mamba 2: a popular RNN used as a baseline; demonstrates the SSM-Transformer duality.
- **Yang et al. (2024)** -- *Gated Delta Networks.* Gated DeltaNet: extends Mamba 2 and DeltaNet with gating; used as the RNN baseline representative for scaling experiments.

### Attention and Architecture Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Original Transformer architecture with self-attention.
- **Beltagy et al. (2020)** -- *Longformer.* Sliding-window attention for long documents, which TTT-E2E uses as its base architecture.
- **Gemma Team (2024)** -- *Gemma 2.* The hybrid SWA + full attention (5:1) baseline follows the Gemma architecture pattern.

### Meta-Learning

- **Finn et al. (2017)** -- *MAML: Model-Agnostic Meta-Learning.* The meta-learning framework for learning initialization through gradients of gradients, directly used for the outer loop of TTT-E2E.
- **Andrychowicz et al. (2016)** -- *Learning to Learn by Gradient Descent by Gradient Descent.* Foundational work on learning the optimization process itself.

### Fast Weights

- **Schmidhuber (1992)** -- *Learning to Control Fast-Weight Memories.* Fast weight programmers: the general idea of updating a "fast" model at test time with a "slow" model, of which TTT-E2E is a special case.
- **Schlag et al. (2021)** -- *Linear Transformers Are Secretly Fast Weight Programmers.* Connects linear attention to fast weight memory, providing theoretical grounding for TTT-KVB's derivation.

### Dynamic Evaluation

- **Mikolov et al. (2013)** -- *Efficient Estimation of Word Representations in Vector Space.* Pioneered dynamic evaluation in NLP.
- **Krause et al. (2018)** -- *Dynamic Evaluation of Neural Sequence Models.* Extended dynamic evaluation to modern neural LMs; the TTT-naive baseline corresponds to this approach.

### Scaling and Training

- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models (Chinchilla).* Provides the Chinchilla-optimal token counts used for the basic training recipe.
- **Brown et al. (2020)** -- *GPT-3.* Model configurations and pre-training recipe form the basis of the basic recipe.
- **Li et al. (2024)** -- *DCLM.* The pre-training dataset (DCLM-Baseline, a filtered Common Crawl subset).

### Evaluation Benchmarks

- **Hsieh et al. (2024)** -- *RULER.* Provides the S-NIAH tasks used for evaluating retrieval at 128K context.
