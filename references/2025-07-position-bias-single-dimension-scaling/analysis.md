---
title: "Mitigate Position Bias in LLMs via Scaling a Single Hidden States Channel"
authors: "Yu, Jiang, Luo, Wu, Lin, Li, Yang, Huang, Qiu"
year: 2025
venue: "Findings of ACL 2025"
paper_type: conference-paper
categories: ["position-bias", "attention-analysis", "mechanistic-interpretability"]
scope: ["positional hidden states in decoder-only LLMs", "causal mask as source of positional information", "inference-time position bias mitigation"]
benchmarks_used: ["natural-questions", "longbench", "mmlu"]
models_introduced: []
models_evaluated: ["llama-2-7b", "llama-2-13b", "vicuna-7b-v1.5-16k", "mistral-7b", "gemma-7b", "qwen1.5-7b", "mpt-7b"]
key_claims:
  - id: C1
    claim: "Attention weights in retrieval-related layers (layers 15-20 in Mistral-7B) exhibit a U-shaped pattern matching the lost-in-the-middle performance curve, and this pattern becomes more pronounced with longer contexts"
    evidence: "Figure 2, Section 2.1"
    status: supported
  - id: C2
    claim: "Positional information in hidden states, introduced by the causal attention mask, is an independent source of position bias beyond position embeddings: modifying the causal mask in layers 2-8 changes attention in retrieval-related layers 15-20 even though PE and masks in those layers are unmodified"
    evidence: "Figure 3, Section 2.2"
    status: supported
  - id: C3
    claim: "Specific hidden states channels exist whose activation values change monotonically with absolute token position (positional channels), and these are primarily determined by the causal mask rather than position embeddings"
    evidence: "Figure 4, Definition 2.1, Section 2.3, Appendix D.4 (Figure 11)"
    status: supported
  - id: C4
    claim: "Modifying a single positional channel (e.g., channel 213 in Mistral-7B) significantly shifts attention to the modified tokens, confirming that individual positional channels can affect position bias"
    evidence: "Figure 10, Appendix D.5"
    status: supported
  - id: C5
    claim: "Scaling positional hidden states improves average performance by up to 9.3% on NaturalQuestions multi-document QA and 15.2% on KV retrieval across multiple model families including RoPE, context-extended, and ALiBi models"
    evidence: "Table 1, Section 4.2"
    status: supported
  - id: C6
    claim: "The method has minimal side effects: MMLU scores and timeline reorder accuracy remain essentially unchanged after applying positional hidden state scaling"
    evidence: "Table 3, Section 4.3"
    status: supported
  - id: C7
    claim: "Scaling factor controls the direction of position bias: factors > 1 amplify primacy bias, factors between 0 and 1 reduce it, and negative factors reverse it toward recency bias"
    evidence: "Figure 6, Section 4.3"
    status: supported
cross_references:
  - target: 2024-02-lost-in-the-middle
    type: extends
    detail: "Directly uses Liu et al.'s NaturalQuestions and KV retrieval benchmarks to evaluate position bias; extends the analysis by identifying positional hidden states as a mechanistic cause beyond position embeddings"
  - target: 2024-08-found-in-the-middle
    type: complementary
    detail: "Both mitigate position bias at inference time without training: Found-in-the-Middle calibrates document-level attention via dummy-document subtraction, while this paper scales a single hidden states channel; both use NaturalQuestions with 20 documents"
  - target: 2025-07-position-bias-transformers
    type: complementary
    detail: "Both identify causal masking as a source of position bias: Wu et al. prove this theoretically via exponential convergence (Theorem 4.1), while this paper demonstrates it empirically through perturbation experiments on hidden states channels"
  - target: 2025-11-pos2distill-position-bias-distillation
    type: complementary
    detail: "Pos2Distill mitigates position bias through training-based knowledge distillation, while this paper proposes a training-free inference-time intervention via hidden state scaling; both evaluate on NaturalQuestions multi-document QA"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "Attention sinks at initial tokens contribute to the primacy component of position bias; this paper identifies positional hidden states as an additional mechanism beyond attention sinks that causes position-dependent attention patterns"
  - target: 2024-01-roformer-rope
    type: evaluates
    detail: "Evaluates position bias mitigation on multiple RoPE-based models (LLaMA-2, Mistral, Gemma, Qwen); identifies that positional hidden states contribute to position bias independently of RoPE"
  - target: 2022-04-alibi-train-short-test-long
    type: evaluates
    detail: "Evaluates the method on MPT-30B (ALiBi model), demonstrating that positional hidden states and position bias exist regardless of the position encoding scheme"
open_questions:
  - question: "What is the optimal strategy for selecting which layers to apply scaling to, beyond the current engineering heuristic of middle layers?"
    addressed_by: null
  - question: "Do positional channels exist and carry the same significance in models trained with bidirectional attention or prefix-LM architectures?"
    addressed_by: null
  - question: "Can positional hidden states be eliminated or controlled during pretraining rather than requiring post-hoc inference-time intervention?"
    addressed_by: null
  - question: "How does the method perform on newer models (e.g., Qwen2.5) that already achieve near-perfect retrieval on traditional benchmarks?"
    addressed_by: null
---
# Mitigate Position Bias in LLMs via Scaling a Single Hidden States Channel

**Authors:** Yijiong Yu, Huiqiang Jiang, Xufang Luo, Qianhui Wu, Chin-Yew Lin, Dongsheng Li, Yuqing Yang, Yongfeng Huang, Lili Qiu (Tsinghua University, Microsoft Corporation)
**Date:** July 2025, Findings of ACL 2025 (arXiv:2406.02536)

---

## Core Research Problem

Long-context language models exhibit position bias — the "lost in the middle" phenomenon (Liu et al., 2024) — where placing key information in the middle of the context significantly degrades performance. Prior work has analyzed this from two angles: data distribution (An et al., 2024; Yu, 2023) and position embeddings (Zhang et al., 2024; Chen et al., 2024). Methods such as FILM (An et al., 2024) require supervised fine-tuning with diverse key-information placements, and Ms-PoE (Zhang et al., 2024) interpolates RoPE with head-wise scaling factors. However, prior work (Haviv et al., 2022; Wang et al., 2024; Chi et al., 2023) has shown that the causal attention mask also introduces positional information into hidden states, independent of position embeddings. No prior work has investigated whether this hidden-state positional information contributes to position bias.

**The core challenge is: determining whether positional information stored in hidden states by the causal mask is an independent cause of position bias, and if so, developing a training-free method to mitigate it.**

---

## Problem Solutions

The paper identifies positional information in hidden states as an additional source of position bias beyond position embeddings, and proposes "scaling positional hidden states" to mitigate it. The key contributions are:

1. **Attention patterns mirror position bias.** In retrieval-related layers (layers 15-20 in Mistral-7B), attention weights to key information follow the same U-shaped pattern as the lost-in-the-middle performance curve, and this pattern intensifies with longer contexts.
2. **Hidden states carry positional information that affects position bias.** Modifying the causal mask in early layers (2-8) changes attention in deep layers (15-20) even though position embeddings and masks in those layers are unchanged, proving the effect propagates through hidden states.
3. **Positional channels exist.** Specific hidden states channels have activation values that change monotonically with absolute token position across layers and models, including models without position embeddings.
4. **Single-channel scaling mitigates position bias.** Scaling the activation values of one identified positional channel — applied only to the last token's attention computation in middle layers — reduces position bias by up to 15.2% while preserving general model capabilities.

---

## Approach Details

### Method

The paper proceeds in two phases: (1) identifying positional hidden states and establishing their causal role in position bias, and (2) scaling them to mitigate position bias.

**Phase 1: Identifying the causal chain.**

The authors analyze Mistral-7B-v0.2 on a KV retrieval task with 50 key-value pairs. Attention is measured as the average attention weight from the last token of the question to the tokens of each KV pair (Eq. 4):

> A_G = (1/|G|) * sum_{j in G} a_{l,j}

where G is the set of token positions of a KV pair and a_{l,j} is the attention weight from the last token l to token j. Three observations establish the causal chain:

1. **Attention U-shape.** In retrieval-related layers (15-20), attention to the gold KV exhibits the same U-shaped pattern as task accuracy. Attention to mid-sequence gold KVs is lower (Figure 2c), and this worsens with context length.

2. **Causal mask perturbation.** The "Crop Mask" experiment modifies the causal mask in layers 2-8 so that gold KV tokens can only attend to themselves and the first token, but cannot see preceding tokens. Despite no changes to layers 15-20, attention to the gold KV in those retrieval-related layers significantly increases — to nearly the level of beginning-position KVs. In contrast, shifting position embedding IDs ("PE to Beginning" or "PE to End") has weaker and asymmetric effects (Figure 3, Section 2.2).

3. **Positional channels.** The authors hypothesize that positional information manifests as channels whose activation values change monotonically with token position:

> h'_t(p) > 0, for all p  OR  h'_t(p) < 0, for all p  (Definition 2.1)

To find them, hidden states are averaged over 2000 random 1000-token strings, and each channel (along the hidden size axis) is checked for monotonicity after sliding-window averaging (window size 100) and discarding the first 30 tokens. Such positional channels exist consistently across layers in Mistral-7B (dim 213), LLaMA-2-7B (dim 2393), MPT-30B (dim 1942), and even TinyLlama-NoPE-1.1B (dim 1156) — a model without position embeddings (Figure 4). Additional perturbation experiments (Appendix D.4, Figure 11) confirm that cropping the causal mask significantly disrupts positional hidden states, while modifying PE position IDs has minimal effect, proving the causal mask is the primary source.

### Key Technical Components

**Positional hidden state search algorithm (Algorithm 1).** The search identifies the optimal channel to scale:

1. For each of the *hidden_size* channels, compute a least-squares cubic polynomial fit across token positions. Count the number of layers where the fitted curve is monotonic (c_t) and accumulate the smoothness score g_t = integral |h''_t(p)|^2. A channel is a candidate if c_t > epsilon (where epsilon = L/4, and L is the total number of layers).

2. Select the top-K (K = 10) candidates by lowest smoothness score (smoothest monotonic curves).

3. Evaluate each candidate on a 100-sample KV retrieval calibration dataset. The channel yielding the lowest loss is selected.

4. The scaling factor s is chosen via grid search over {0.5, 0, -0.5, -1}, selecting the value with lowest loss.

The entire search process completes in approximately 10 minutes on an A100 GPU.

**Scaling mechanism (Section 3.3).** To minimize side effects, scaling is applied only to the attention computation of the last token in the sequence. For a sequence of length l:

> q_bar_l = P(W^Q f(h(l), p, s), l)
> K_bar = P(W^K f(h, p, s), [1, 2, ..., l])

where f(h, p, s) scales the p-th channel of h by factor s, and P denotes the positional encoding application. The combined attention is:

> z_i = Softmax((q_i K^T + Mask) / sqrt(d)) V,  for i < l
> z_l = Softmax((q_bar_l K_bar^T) / sqrt(d)) V,  for i = l

All other tokens use the original, unmodified attention. Scaling is applied only to middle layers (e.g., layers 10-25 for 32-layer models) to avoid instability from modifying early or late layers. The method is implemented using FlashAttention-2 with minimal latency overhead (Table 5: 32 vs 22 minutes on 500-sample KV retrieval for LLaMA-2-7B, compared to 61 minutes for Ms-PoE).

**Per-model parameters (Table 4, Appendix C.3):**

| Model | Channel Index | Scale Factor | Applied Layers |
|---|---|---|---|
| LLaMA-2-7b-chat | 2,393 | -1 | 10-25 |
| LLaMA-2-13b-chat | 4,283 | -1 | 10-34 |
| Vicuna-7b-v1.5-16k | 2,393 | 0 | 10-25 |
| Vicuna-13b-v1.5-16k | 4,923 | 0 | 10-34 |
| Mistral-7B-Instruct-v0.2 | 213 | 0 | 10-25 |
| Gemma-1.1-7b-it | 1,665 | 0 | 10-22 |
| Qwen1.5-7b-chat | 1,081 | 0.2 | 10-25 |
| MPT-30b-chat | 6,926 | 0 | 10-42 |

### Experimental Setup

**Models:** 8 instruction-tuned models spanning three position encoding families:

- RoPE: LLaMA-2-7b-chat, LLaMA-2-13b-chat, Mistral-7B-Instruct-v0.2, Gemma-1.1-7b-it, Qwen1.5-7b-chat
- Context-window-extended: Vicuna-7b-v1.5-16k, Vicuna-13b-v1.5-16k
- ALiBi: MPT-30b-chat

**Evaluation tasks:**

1. *Position-bias-related:* NaturalQuestions multi-document QA (20 documents, ~2.3k tokens) and KV retrieval (140 KV pairs, ~10k tokens) from Liu et al. (2024), with gold information placed at positions 1st, 5th/25%, 10th/50%, 15th/75%, 20th/100%.
2. *General long-context:* LongBench (Bai et al., 2024) — 16 tasks across 6 categories (single-doc QA, multi-doc QA, summarization, few-shot, synthetic, code), average length 37k tokens.
3. *Side-effect evaluation:* MMLU (Hendrycks et al., 2021) and LooGLE timeline reorder (Li et al., 2024).

**Baseline:** Ms-PoE (Zhang et al., 2024), a head-wise position embedding scaling method with default scale coefficients 1.2 to 1.8 starting from the 3rd layer.

**Hardware:** A100 GPU. Greedy decoding throughout.

### Key Results

**NaturalQuestions multi-document QA (Table 1, selected models, accuracy %):**

| Model | Method | 1st | 5th | 10th | 15th | 20th | Avg. |
|---|---|---|---|---|---|---|---|
| LLaMA-2-7b | Original | 32.4 | 23.8 | 30.6 | 31.6 | 38.2 | 31.3 |
| LLaMA-2-7b | Ms-PoE | 40.8 | 29.2 | 33.0 | 32.8 | 39.6 | 35.1 |
| LLaMA-2-7b | **Ours** | 33.6 | **34.0** | **40.6** | **43.0** | **51.8** | **40.6** |
| Qwen1.5-7b | Original | 72.4 | 53.8 | 52.2 | 51.2 | 54.4 | 56.8 |
| Qwen1.5-7b | Ms-PoE | 67.4 | 49.8 | 48.2 | 47.4 | 47.0 | 52.0 |
| Qwen1.5-7b | **Ours** | 67.4 | **55.2** | **53.6** | **56.0** | **59.4** | **58.3** |
| Gemma-7b | Original | 29.6 | 25.2 | 28.2 | 29.6 | 27.4 | 28.0 |
| Gemma-7b | **Ours** | **35.4** | **31.4** | **36.0** | **35.4** | **35.0** | **34.6** |

**KV retrieval (Table 1, selected models, accuracy %):**

| Model | Method | 0% | 25% | 50% | 75% | 100% | Avg. |
|---|---|---|---|---|---|---|---|
| Qwen1.5-7b | Original | 100.0 | 97.2 | 84.6 | 60.0 | 56.4 | 79.6 |
| Qwen1.5-7b | Ms-PoE | 3.4 | 1.4 | 2.8 | 2.6 | 0.6 | 2.2 |
| Qwen1.5-7b | **Ours** | 97.2 | **95.6** | **98.8** | **76.6** | **94.4** | **92.5** |
| Gemma-7b | Original | 98.6 | 67.0 | 62.4 | 83.4 | 100.0 | 82.3 |
| Gemma-7b | Ms-PoE | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Gemma-7b | **Ours** | 97.6 | **95.8** | **97.6** | **96.8** | **99.6** | **97.5** |

Key observations:

- Average NQ improvement up to +9.3% (LLaMA-2-7b: 31.3 to 40.6), average KV retrieval improvement up to +15.2% (Gemma: 82.3 to 97.5).
- Performance gains are concentrated in middle and rear positions. When considering only the last four positions, improvements increase to +11.3% (NQ) and +16.8% (KV retrieval).
- Ms-PoE causes output instability on Qwen and Gemma in KV retrieval (near-zero accuracy), while the proposed method works stably across all tested models.
- Exception: LLaMA-2-13b on KV retrieval shows a decrease (71.0 to 53.9).

**LongBench (Table 2):** Improvements vary by task category. Most significant gains: +9.2% single-doc QA (LLaMA-2-13b), +4% synthetic tasks (Vicuna-13b), +3.4% code (LLaMA-2-13b). Average scores remain stable or slightly improve, demonstrating the method does not impair general long-context capabilities.

**Side effects (Table 3):**

| Model | MMLU (original / ours) | Reorder (original / ours) |
|---|---|---|
| Vicuna-7b-v1.5-16k | 48.22 / 48.38 | 20.83 / 20.83 |
| Qwen1.5-7b-chat | 60.84 / 61.43 | 28.13 / 28.13 |
| Mistral-7B-Instruct-v0.2 | 60.31 / 60.38 | 18.75 / 19.79 |

No significant degradation on either benchmark.

### Ablation Study

Ablation results on NaturalQuestions with 20 documents (Table 6, Appendix E):

| Variant | LLaMA-2-7b | Vicuna-13b | Gemma-7b | Mistral-7b | Qwen1.5-7b |
|---|---|---|---|---|---|
| Not applied | 31.3 | 50.2 | 28.0 | 59.5 | 56.8 |
| **Ours (full)** | **40.6** | **52.7** | **34.6** | **60.9** | **58.3** |
| w/o monotonicity | 40.6 | 51.8 | 34.6 | 60.9 | 58.3 |
| w/o smoothness | 40.6 | 52.7 | 27.8 | 60.9 | 58.3 |
| w/o validation set | 30.1 | 51.8 | 26.5 | 60.9 | 58.3 |
| w/ scale top-2 channels | 37.2 | 50.8 | 31.7 | 60.1 | 57.2 |
| w/ modify all tokens | 44.0 | 50.8 | 31.7 | 59.5 | 57.4 |

Removing the validation set causes the most degradation. Scaling 2 channels or modifying all tokens (rather than just the last) reduces performance for most models, justifying the design choice of single-channel, last-token-only intervention.

### Scaling Factor Analysis

Varying the scaling factor on the 2,393rd channel of Vicuna-7b (Figure 6) reveals a continuous control mechanism:

- Factors > 1 amplify primacy bias (attention concentrated at the beginning).
- Factor = 1 (no change) retains original bias.
- Factors between 0.5 and -1 yield relatively balanced attention distribution, where average accuracy peaks.
- Factors < -1 reverse bias toward recency (attention concentrated at the end).

---

## Limitations and Failure Modes

1. **Layer selection is heuristic.** The choice of which layers to apply scaling (e.g., layers 10-25 for 32-layer models) is based on engineering experience, not a principled criterion. The paper identifies these as "retrieval-related layers" but provides no automated selection procedure (Limitations, Section 5).

2. **Sensitivity to channel and scale factor.** Choosing a too-large scaling factor or an inappropriate channel can cause significant performance degradation. The method requires a per-model search process (Limitations, Section 5).

3. **LLaMA-2-13b regression on KV retrieval.** The method decreases KV retrieval accuracy from 71.0% to 53.9% on LLaMA-2-13b-chat, the only model where overall performance drops on either benchmark (Table 1).

4. **Limited gains on LongBench.** Because LongBench focuses on comprehensiveness and real-world tasks where position bias has less influence, the method provides only marginal average improvements (Table 2).

5. **Newer models may not benefit.** Models like Qwen2.5 already achieve near-perfect performance on retrieval-based long-context tasks. The method may not bring further improvement on such models (Limitations, Section 5).

6. **No theoretical analysis.** The paper provides empirical evidence for positional hidden states but no formal proof of why they arise or why single-channel scaling works. The causal chain (causal mask -> positional hidden states -> attention bias -> position bias) is established empirically, not theoretically.

---

## Conclusions

### Contributions

1. **Positional information in hidden states causes position bias.** The paper establishes through perturbation experiments that positional information introduced by the causal mask into hidden states is an independent contributor to position bias, beyond position embeddings (Figure 3, Section 2.2).

2. **Discovery of positional channels.** Specific hidden states channels whose activation values correlate monotonically with absolute token position are identified across diverse model families, including models without position embeddings (Figure 4, Section 2.3).

3. **Causal mask as primary source.** Perturbation experiments show that the causal mask, not position embeddings, is the primary determinant of positional hidden states. Cropping the causal mask disrupts positional hidden states significantly; modifying PE position IDs has minimal effect (Appendix D.4, Figure 11).

4. **Training-free mitigation method.** A practical method consisting of a heuristic search algorithm (using monotonicity, smoothness, and validation loss) followed by single-channel scaling of the last token's attention achieves up to 9.3% (NQ) and 15.2% (KV retrieval) average improvement with minimal side effects (Tables 1, 3).

5. **Cross-architecture generalization.** The method works across RoPE models (LLaMA-2, Mistral, Gemma, Qwen), context-extended models (Vicuna-16k), and ALiBi models (MPT-30b), demonstrating that positional hidden states are a general phenomenon not tied to a specific position encoding scheme (Table 1).

### Implications

1. **Position bias has multiple sources.** The finding that both position embeddings and causal-mask-induced hidden states contribute to position bias suggests that methods targeting only PE (e.g., RoPE scaling) address only part of the problem. A comprehensive solution may need to address both sources. [Supported by experimental evidence.]

2. **Controllable position attention.** The scaling factor provides a continuous knob to steer position bias from primacy toward recency, suggesting that positional hidden states could be exploited for tasks where controlled positional attention is desirable. [Speculative: not tested on such tasks.]

3. **Architectural implications.** The existence of positional channels even in NoPE models implies that the causal mask itself encodes position inescapably. This aligns with theoretical analyses showing that causal masking induces exponential convergence to the first token (Wu et al., 2025). [Inference: connection to theoretical work not made by authors.]

---

## Key Claims

1. **C1: Attention patterns are a micro-level expression of position bias.** In retrieval-related layers, attention to key information follows the U-shaped pattern, with attenuation becoming more pronounced at longer contexts (Figure 2, Section 2.1). Status: **supported**.

2. **C2: Positional information in hidden states is an independent source of position bias.** Modifying the causal mask in layers 2-8 (Crop Mask) improves attention to gold KV in layers 15-20 to nearly beginning-level, even though PE and masks in those layers are unmodified. PE modification has weaker effects (Figure 3, Section 2.2). Status: **supported**.

3. **C3: Positional channels exist across model families.** Monotonically varying hidden states channels are found in Mistral-7B (dim 213), LLaMA-2-7B (dim 2393), MPT-30B (dim 1942), and TinyLlama-NoPE-1.1B (dim 1156). Perturbation confirms the causal mask is the primary source (Figure 4, Figure 11, Section 2.3, Appendix D.4). Status: **supported**.

4. **C4: Single-channel modification affects position bias.** Subtracting 0.3 from channel 213 of the 26th or 36th KV in Mistral-7B increases attention to those KVs above the level of the 1st KV, regardless of whether they contain the gold information (Figure 10, Appendix D.5). Status: **supported**.

5. **C5: Scaling positional hidden states improves performance across model families.** Average improvements up to +9.3% (NQ) and +15.2% (KV retrieval) across 8 models spanning RoPE, context-extended, and ALiBi architectures. Ms-PoE causes instability on Qwen and Gemma (Table 1, Section 4.2). Status: **supported**.

6. **C6: Minimal side effects on general capabilities.** MMLU and timeline reorder scores show no significant change (Table 3, Section 4.3). Status: **supported**.

7. **C7: Scaling factor provides continuous position bias control.** Factors > 1 amplify primacy bias, factors between 0.5 and -1 yield balanced attention, negative factors shift toward recency (Figure 6, Section 4.3). Status: **supported**.

---

## Open Questions

1. **What principled criterion determines the optimal layers for scaling?** The current approach selects middle layers based on engineering heuristics and observation that these correspond to retrieval-related layers. An automated layer selection method would improve generalizability. Not yet addressed.

2. **Do positional channels exist and carry the same significance in bidirectional or prefix-LM architectures?** The paper tests only causal (decoder-only) models. Whether the causal mask's role generalizes to other masking strategies is unknown. Not yet addressed.

3. **Can positional hidden states be controlled during pretraining?** If the causal mask inevitably introduces position information into hidden states, architectural modifications (e.g., bidirectional attention in early layers, modified causal masks) might prevent position bias at training time. Not yet addressed.

4. **How does the method perform on newer models with near-perfect retrieval?** The authors note that models like Qwen2.5 already achieve near-perfect retrieval accuracy, suggesting the method may have diminishing returns on state-of-the-art models. Not yet addressed.

---

## Core References and Why They Are Referenced

### Position Bias Foundations

- **Liu et al. (2024)** -- *Lost in the Middle: How Language Models Use Long Contexts.* Defines the lost-in-the-middle phenomenon and provides the NaturalQuestions multi-document QA and KV retrieval benchmarks used directly in this paper's evaluation.
- **Zhang et al. (2024)** -- *Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding (Ms-PoE).* The primary baseline; a head-wise RoPE scaling method that the proposed approach outperforms in generalization and stability.

### Positional Information in Hidden States

- **Haviv et al. (2022)** -- *Transformer Language Models Without Positional Encodings Still Learn Positional Information.* Establishes that position information can be linearly probed from hidden states even without PE, motivating the search for explicit positional channels.
- **Wang et al. (2024)** -- *Length Generalization of Causal Transformers Without Position Encoding.* Proves the causal mask can introduce positional information, a key theoretical foundation for this paper's perturbation experiments.
- **Chi et al. (2023)** -- *Latent Positional Information Is in the Self-Attention Variance of Transformer Language Models Without Positional Embeddings.* Demonstrates positional information exists in attention variance without PE, supporting the paper's claim that the causal mask is the primary source.

### Models Used in Evaluation

- **Touvron et al. (2023)** -- *Llama 2: Open Foundation and Fine-Tuned Chat Models.* Provides LLaMA-2-7B and LLaMA-2-13B, two primary evaluation models.
- **Jiang et al. (2023)** -- *Mistral 7B.* Provides Mistral-7B-Instruct-v0.2, the model used for most analysis experiments (attention patterns, perturbation, positional channel identification).
- **Press et al. (2022)** -- *Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation.* Introduces ALiBi, used via MPT-30b to demonstrate cross-architecture generalization.

### Attention Analysis

- **Sun et al. (2024)** -- *Massive Activations in Large Language Models.* Referenced for the observation that initial token hidden states have abnormally large values, motivating the decision to discard the first 30 tokens when checking monotonicity.
- **Wu et al. (2025)** -- *Retrieval Head Mechanistically Explains Long-Context Factuality.* Referenced for the concept of retrieval heads, which correspond to the diagonal attention patterns observed in retrieval-related layers.

### Evaluation Benchmarks

- **Bai et al. (2024)** -- *LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding.* Provides the general long-context evaluation benchmark used to assess side effects.
- **Hendrycks et al. (2021)** -- *Measuring Massive Multitask Language Understanding (MMLU).* Used to verify that scaling does not impair general model capabilities.
- **Li et al. (2024)** -- *LooGLE: Can Long-Context Language Models Understand Long Contexts?* Provides the timeline reorder task used for side-effect evaluation.
