---
title: "When Attention Sink Emerges in Language Models: An Empirical View"
authors: "Gu, Pang, Du, Liu, Zhang, Du, Wang, Lin"
year: 2025
venue: "ICLR 2025"
paper_type: conference-paper
categories: ["attention-analysis", "mechanistic-interpretability"]
scope: ["attention sink phenomenon", "softmax normalization", "pre-training dynamics", "attention mechanism design"]
benchmarks_used: ["hellaswag"]
models_introduced: []
models_evaluated: ["gpt-2", "llama-2-7b", "llama-3-8b", "mistral-7b", "pythia-series"]
key_claims:
  - id: C1
    claim: "Attention sinks exist universally in auto-regressive LMs with various inputs, even in small models (Pythia-14M) and with random token sequences"
    evidence: "Table 1, Figure 4(Left), Section 3.3"
    status: supported
  - id: C2
    claim: "Attention sink emerges during pre-training after effective optimization on sufficient training data; smaller learning rates reduce sink amplitude even with compensating training steps"
    evidence: "Figure 4(Middle, Right), Table 9, Figure 5(Right), Section 4-5"
    status: supported
  - id: C3
    claim: "The sink position is determined by the loss function and data distribution, not by positional embedding type — all PE types (NoPE, absolute, learnable, relative, ALiBi, RoPE) produce attention sinks"
    evidence: "Table 3, Table 10(Right), Figure 5(Middle), Section 5-7.1"
    status: supported
  - id: C4
    claim: "The first token acts as key biases: its keys have small l2-norm but high cosine similarity with queries, storing extra attention scores while not contributing to value computation"
    evidence: "Figure 2, Table 4 (K biases setup: Sink_*=73.34%, Sink_1=0.00%), Section 3.1, 7.3"
    status: supported
  - id: C5
    claim: "Attention sink stems at least partially from tokens' inner dependence on attention scores due to softmax normalization; replacing softmax with sigmoid attention without normalization eliminates sinks in LMs up to 1B parameters"
    evidence: "Table 6, Figure 8, Table 14(Right), Section 7.4"
    status: supported
  - id: C6
    claim: "Weight decay encourages the emergence of attention sink, with moderate values (gamma=0.5) inducing the strongest sink (41.08%), while excessive values (gamma>=2.0) hurt optimization and eliminate it"
    evidence: "Table 2, Section 6"
    status: supported
  - id: C7
    claim: "Instruction tuning has insignificant impact on attention sink — base and chat models have comparable sink metrics"
    evidence: "Table 1(Right), Section 3.4"
    status: supported
cross_references:
  - target: 2024-05-attention-sinks-streaming
    type: extends
    detail: "Directly extends Xiao et al.'s attention sink discovery with comprehensive empirical analysis of when and why sinks emerge during pre-training, identifying softmax normalization as a root cause"
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Analyzes the softmax attention mechanism from the original Transformer, showing its normalization constraint is a root cause of attention sinks"
  - target: 2024-01-roformer-rope
    type: evaluates
    detail: "Evaluates RoPE alongside other PEs (NoPE, absolute, learnable, relative, ALiBi) and shows PE type does not affect attention sink emergence (Table 3)"
  - target: 2022-04-alibi-train-short-test-long
    type: evaluates
    detail: "Evaluates ALiBi PE and proves (Proposition 3) that repeated token sequences produce no attention sink with ALiBi due to monotonic distance penalties"
  - target: 2019-11-dark-secrets-of-bert
    type: complementary
    detail: "Kovaleva et al. observed attention concentrating on [CLS]/[SEP] in BERT; Gu et al. extend this to auto-regressive LMs and identify the softmax mechanism as the underlying cause"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: complementary
    detail: "DroPE removes all positional embeddings after pretraining; Gu et al. show PE type does not affect attention sink emergence, suggesting sinks persist in NoPE models"
  - target: 2021-12-transformer-circuits-framework
    type: complementary
    detail: "Elhage et al.'s circuit analysis framework provides context for understanding how the first token's key vectors act as implicit biases in the QK circuit"
  - target: 2024-12-transformers-need-glasses-over-squashing
    type: complementary
    detail: "Barbero et al. provide a complementary theoretical analysis: over-squashing from the causal mask topology creates exponentially more information pathways for initial tokens, connecting attention sinks to GNN over-squashing theory"
open_questions:
  - question: "How do attention sinks on non-initial word tokens (e.g., period, newline tokens) relate to pre-training dynamics?"
    addressed_by: null
  - question: "Does attention sink benefit or harm downstream task performance? Cross-family comparisons show no clear correlation (Figure 10)."
    addressed_by: null
  - question: "Would sigmoid attention without normalization maintain no attention sink at scales significantly larger than 1B parameters?"
    addressed_by: null
  - question: "How does attention sink interact with context extension methods and long-context performance?"
    addressed_by: null
---

# When Attention Sink Emerges in Language Models: An Empirical View

**Authors:** Xiangming Gu, Tianyu Pang, Chao Du, Qian Liu, Fengzhuo Zhang, Cunxiao Du, Ye Wang, Min Lin (Sea AI Lab, National University of Singapore)
**Date:** April 2025, ICLR 2025 Spotlight (arXiv:2410.10781)

---

## Core Research Problem

Auto-regressive LMs assign disproportionately high attention scores to the first token regardless of its semantic content — a phenomenon termed **attention sink** by Xiao et al. (2023). This pattern has been exploited for practical applications including streaming generation, KV cache optimization, efficient inference, and model quantization. However, the phenomenon remained poorly understood: it was unclear *when* attention sinks emerge during training, *what factors* cause them, and *why* they appear.

Prior work (Cancedda, 2024; Sun et al., 2024) attributed attention sinks to massive activations — the first token develops disproportionately large hidden state norms. But this observation described a symptom rather than a root cause. Key questions remained unanswered: Do sinks depend on the positional encoding scheme? Do they require large-scale models? What role does the softmax normalization play?

The core challenge is: **what conditions in LM pre-training — optimization, data distribution, loss function, and model architecture — cause attention sinks to emerge, and what is their mechanistic role.**

---

## Problem Solutions

The paper provides a comprehensive empirical study that systematically varies each component of LM pre-training to identify the conditions under which attention sinks emerge. The key findings are:

1. **Attention sinks are universal** — they appear in all auto-regressive LMs tested, from Pythia-14M to LLaMA3-8B, across all input types (natural text, random tokens), and persist through instruction tuning.
2. **The first token acts as key biases** — the cosine similarity between the first token's keys and all queries is high despite small key norms, allowing it to store excess attention probability without contributing meaningfully to value computation.
3. **Softmax normalization is the root cause** — replacing softmax with sigmoid attention without normalization eliminates attention sinks entirely in LMs up to 1B parameters, maintaining comparable validation loss.

---

## Approach Details

### Method

The paper trains a series of controlled ~60M parameter LLaMA-style models, systematically varying one training factor at a time while holding others constant. Each trained model is evaluated using a threshold-based attention sink metric:

> Sink^ε_k = (1/L) * Σ_{l=1}^{L} (1/H) * Σ_{h=1}^{H} I(α^{l,h}_k > ε)

where α^{l,h}_k = (1/(T-k+1)) * Σ_{i=k}^{T} A^{l,h}_{i,k} is the importance score for the k-th token in head h of block l. The metric measures the fraction of attention heads across all blocks that exhibit sink behavior at position k. The threshold ε = 0.3 is selected for being both strict and relatively insensitive to token length T (Figure 3). All measurements use T = 64.

### Key Technical Components

**First token as key biases.** The first token's hidden state h^l_1 has no involvement of self-attention (since there are no preceding tokens), making it a pure MLP output of the word embedding. From certain blocks onward, h^l_1 develops massive activations (large ℓ2-norm), but layer normalization suppresses these in the key/value projections, producing keys k^{l,h}_1 and values v^{l,h}_1 with *smaller* ℓ2-norms than other tokens (Figure 2, Top). Despite this small norm, the cosine similarity cos(q^{l,h}_t, k^{l,h}_1) is significantly larger than cos(q^{l,h}_t, k^{l,h}_{j≠1}), driving the attention sink (Figure 2, Bottom).

**Learnable key biases experiment.** To confirm the key-bias interpretation, the paper introduces explicit learnable key biases k^{*l,h} with fixed zero value biases v^{*l,h} = 0 (K biases setup). With this design, attention sink shifts entirely from the first token (Sink^ε_1 = 0.00%) to the bias position (Sink^ε_* = 73.34%), demonstrating that the sink token stores extra attention scores without contributing to value computation (Table 4). Furthermore, when the fixed v^{*l,h} is set to non-zero vectors with increasing ℓ2-norm, attention gradually shifts back from k^{*l,h} to the first token — because the model cannot cancel out the non-zero value contribution, it prefers to use the first token whose values it can optimize (Table 5).

**Sigmoid attention without normalization.** The paper generalizes the attention output as:

> v^†_i = Z_i^{-1} * Σ_{j=1}^{i} sim(φ(q_i), φ(k_j)) * v_j

For softmax, φ(·) is identity and sim(q, k) = exp(qk^⊤/√d_h) with Z_i = Σ_j sim(q_i, k_j). Without normalization (Z_i = 1), attention scores for individual tokens are independent — there is no need to "dump" probability mass on a sink token. Sigmoid attention without normalization achieves comparable validation loss (3.70 vs. 3.73 for softmax) but eliminates attention sinks entirely (Sink^ε_1 = 0.44% by proxy attention scores vs. 18.18% for softmax), and also eliminates massive activations (Table 6, Figure 8).

### Theoretical Analysis

**Propositions 1–4** prove that for LMs with NoPE, relative PE, ALiBi, or RoPE, when all input tokens are identical, all hidden states are equal across positions (since P = 0 for these PE types). This disperses the attention sink and produces uniform or distance-dependent attention. For NoPE: A^{l,h}_{t,i} = 1/t uniformly. For ALiBi: attention follows the monotonic distance penalty. For RoPE: attention scores are bounded by e^{2ξ}/(e^{2ξ} + (t−1)), decreasing to zero as t grows (Proposition 4). GPT2 (learnable PE) retains attention sinks even with repeated tokens because p_t differs across positions (Table 1, Table 7).

### Experimental Setup

**Controlled pre-training models:** LLaMA-style, d = 768, L = 10, H = 8, FFN intermediate = 1536, ~60M parameters (excluding embeddings). RoPE, pre-norm, RMSNorm, SwiGLU. Trained on 5B tokens from the Pile, context length 2048, batch size 1M tokens, 20k steps (100 warmup), LR = 4e-4 with cosine scheduling, AdamW with weight decay 0.1. Validation: Pile-CC loss. Sink metric: 100 sequences of T = 64 from out-of-training data.

**1B parameter scale-up:** Softmax vs. sigmoid (without normalization). Softmax achieves validation loss 3.07 with Sink^ε_1 = 45.11%; sigmoid achieves 3.10 with Sink^ε_1 = 2.46% (proxy). Training stability verified through supervised fine-tuning on UltraChat (200k samples, LR = 2e-5).

**Open-source model evaluation:** GPT2 (124M–1.5B), Pythia (14M–12B), OPT (125M–13B), LLaMA2 (7B, 13B), LLaMA3/3.1 (8B), Mistral (7B), Jamba (v0.1, 1.5 Mini). Input domains: 17 Pile subsets.

### Key Results

**Optimization effects (Section 4):**

| Factor | Condition | Sink^ε_1 (%) | Valid Loss |
|---|---|---|---|
| Learning rate | 8e-4, 20k steps | 32.23 | 3.70 |
| Learning rate | 4e-4, 20k steps (default) | 18.18 | 3.73 |
| Learning rate | 2e-4, 40k steps | 16.81 | 3.68 |
| Learning rate | 1e-4, 80k steps | 6.29 | 3.67 |

- Attention sink emerges between 1k and 2k training steps and increases with continued training (Figure 4, Middle).
- Smaller learning rates delay emergence and reduce final sink amplitude, even with compensating training steps (Table 9).
- Batch size has no effect on attention sink (Table 10, Left).

**Data distribution effects (Section 5):**

| Training Data | Sink^ε_1 (%) | Valid Loss |
|---|---|---|
| 5B tokens | 18.18 | 3.73 |
| 500M tokens | ~4 | ~3.8 |
| 50M tokens | <1 | ~4.5 (overfit) |

- With less training data, sinks disappear — this is driven by data amount, not overfitting (Figure 28).
- Randomizing x_1 ~ Uniform(V) increases the sink (27.03%) because the first token carries even less semantic information.
- When x_1, x_2 ~ Uniform(V), the sink shifts to position 2 (Sink^ε_2 = 14.08%, Sink^ε_1 = 1.98%).
- Fixing a specific token at position k during pre-training always places the sink at position k (Table 10, Right).

**Loss function effects (Section 6):**

| Weight Decay γ | 0.0 | 0.01 | 0.1 | 0.5 | 1.0 | 2.0 | 5.0 |
|---|---|---|---|---|---|---|---|
| Sink^ε_1 (%) | 15.20 | 15.23 | 18.18 | 41.08 | 37.71 | 6.13 | 0.01 |
| Valid Loss | 3.72 | 3.72 | 3.73 | 3.80 | 3.90 | 4.23 | 5.24 |

- Moderate weight decay encourages attention sink; excessive weight decay hurts optimization and eliminates it.
- Prefix language modeling (p > 1) distributes the sink among prefix tokens rather than concentrating it on the first token (Figure 5, Middle).
- Shifted window attention: the sink appears on the absolute first token, not the "relative" first token within each window. Smaller window sizes prevent sink emergence (Figure 6).

**Architecture effects (Section 7):**

| PE Type | Sink^ε_1 (%) | Valid Loss |
|---|---|---|
| NoPE | 20.35 | 3.81 |
| Absolute PE | 32.73 | 3.74 |
| Learnable PE | 33.13 | 3.79 |
| Relative PE | 35.53 | 5.45 |
| ALiBi | 20.78 | 3.71 |
| Rotary (RoPE) | 18.18 | 3.73 |

- PE type does not affect emergence — even NoPE models develop sinks (Table 3).
- Post-norm LMs also develop sinks (Sink^ε_1 = 13.54%); massive activations exist before post-LN rather than in the hidden states (Figure 7, Left).
- FFN activation function (ReLU, GeLU, Swish, SwiGLU variants) does not affect sinks (Table 11).
- Multi-head design (number of heads, concatenation vs. addition) does not affect sinks (Table 12, Left).

**Attention operation effects (Section 7.4):**

| Attention Operation | Normalization | Sink^ε_1 (%) | Valid Loss |
|---|---|---|---|
| Softmax (exp) | sum-to-one | 18.18 | 3.73 |
| Sigmoid | none | 0.44* | 3.70 |
| Sigmoid | sum-normalized | 30.24 | 3.74 |
| ELU+1 | none | 0.80* | 3.69 |
| ELU+1 kernel | sum-normalized | 53.65* | 4.19 |
| Identity kernel | none | 0.00* | 3.99 |
| MLP kernel | with normalization | 0.19* | 3.85 |
| MLP kernel | none | 0.74* | 3.91 |

(*) denotes proxy attention scores.

- **With normalization**: attention sinks emerge regardless of the similarity function.
- **Without normalization**: attention sinks do not emerge, even at 1B parameters (Figure 8, Right).
- MLP kernel is the only function that avoids sinks both with and without normalization.

---

## Limitations and Failure Modes

1. **Scale limited to 1B parameters.** The sigmoid attention experiments scale to 1B parameters, but it is unclear whether attention sinks would remain absent at the 7B+ scales where they are most practically relevant (Section 7.4).

2. **Narrow model family.** Controlled experiments use only LLaMA-style architectures. While open-source evaluation covers multiple families, the causal ablations are limited to one architecture.

3. **Only the first-position sink is studied.** Sun et al. (2024) and Yu et al. (2024) observed attention sinks on word tokens with limited semantic information (e.g., periods, newlines) at non-fixed positions. This paper focuses exclusively on the positionally fixed first-token sink (Section 8).

4. **Downstream impact unclear.** The paper establishes that attention sinks emerge during pre-training but does not determine whether they benefit or harm downstream performance. Within the Pythia family, larger models have both more sinks and better HellaSwag accuracy, but the correlation does not hold across model families (Figure 10, Appendix C.3).

5. **Sigmoid attention trade-offs not fully characterized.** The 1B sigmoid model achieves slightly higher validation loss (3.10 vs. 3.07) than softmax. Whether this gap widens or narrows at larger scales, and how it affects downstream tasks beyond SFT training stability, is not established.

6. **Training data limited to English.** All controlled experiments use the Pile dataset. Whether the findings generalize to multilingual or domain-specific pre-training is untested.

7. **Metric sensitivity.** The Sink^ε_k metric depends on the threshold ε and sequence length T, and the paper acknowledges there is no principled way to select an optimal threshold (Section 3.2).

---

## Conclusions

### Contributions

1. **Comprehensive taxonomy of factors affecting attention sink emergence.** Systematically varied optimization (learning rate, batch size, steps), data (amount, distribution, token fixing), loss function (weight decay, prefix LM, window attention), and architecture (PE, normalization, attention design), establishing which factors matter and which do not (Sections 4–7).

2. **Identified the key-bias mechanism.** Demonstrated that the first token's keys act as implicit biases — minimizing angles with all queries to absorb excess attention — while its values have negligible ℓ2-norm and do not contribute to the output computation. Confirmed by the K-biases experiment where explicit zero-value key biases absorb 73.34% of attention sink heads (Table 4, Section 7.3).

3. **Identified softmax normalization as a root cause.** Showed that attention sinks stem from tokens' inner dependence on attention scores imposed by the softmax sum-to-one constraint. Removing normalization (sigmoid, ELU+1, or identity kernel without normalization) eliminates sinks while maintaining comparable model quality (Table 6, Figure 8).

4. **Proposed a quantitative metric for attention sink.** The Sink^ε_k metric provides a scalar measurement of attention sink strength across all heads and layers, enabling systematic comparisons across architectures and training configurations (Section 3.2).

5. **Proved attention properties under repeated tokens.** Propositions 1–4 establish that for NoPE/relative PE/ALiBi/RoPE, repeated token sequences produce uniform or distance-dependent attention (no sink), while learnable PE models retain sinks due to position-dependent initial embeddings (Appendix C.1).

### Implications

1. **Alternative attention mechanisms can avoid sinks.** Sigmoid attention without normalization is a viable replacement for softmax that eliminates sinks and massive activations, with comparable training stability through SFT. This could simplify KV cache management, quantization, and streaming inference. [Inference: this aligns with concurrent work by Ramapuram et al. (2024) on sigmoid self-attention.]

2. **Attention sinks are a learned optimization strategy, not an architectural necessity.** The emergence depends on effective optimization with sufficient data, not on any specific architectural component. This suggests sinks are the model's learned solution to the softmax normalization constraint rather than a fundamental requirement for language modeling.

3. **Practical interventions are possible.** Weight decay tuning, prefix language modeling, learnable key biases, or architectural changes to the attention normalizer can control sink behavior without fundamentally changing the model (Sections 6–7).

---

## Key Claims

1. **C1: Attention sinks are universal across auto-regressive LMs.** Even Pythia-14M (14 million parameters) exhibits attention sinks. Sinks persist with random token inputs (GPT2-XL: 70.29%, LLaMA3-8B: 91.23%) but disappear with repeated tokens for RoPE/ALiBi models due to dispersed massive activations (Table 1, Figure 4, Left). Input domain across 17 Pile subsets has negligible effect (Figure 9). Status: **supported**.

2. **C2: Attention sink emerges during pre-training after effective optimization on sufficient data.** Sinks appear between 1k–2k training steps in the default setup and grow with continued training (Figure 4, Middle). With 50M–100M training tokens, sinks do not emerge even after 5k steps, independent of overfitting (Figure 28). Smaller learning rates (1e-4 vs. 4e-4) reduce sink amplitude from 18.18% to 2.90% at 20k steps, and to 6.29% even with 4x compensating steps (Table 9). Status: **supported**.

3. **C3: Sink position depends on loss function and data distribution, not PE type.** All PE types — NoPE (20.35%), absolute (32.73%), learnable (33.13%), relative (35.53%), ALiBi (20.78%), RoPE (18.18%) — produce sinks at comparable validation loss (Table 3). Fixing a token at position k during pre-training always places the sink at position k (Table 10, Right). Prefix LM distributes sinks among prefix tokens (Figure 5, Middle). Status: **supported**.

4. **C4: The first token acts as key biases, not value contributors.** Introducing explicit learnable key biases with zero-value biases (K biases) absorbs 73.34% of sink heads while reducing first-token sinks to 0.00%, with identical validation loss 3.72 (Table 4). The key biases eliminate massive activations entirely (Figure 7, Middle). Increasing the ℓ2-norm of fixed value biases gradually shifts the sink back to the first token (Table 5). Status: **supported**.

5. **C5: Softmax normalization is the root cause.** With sigmoid attention (no normalization): Sink^ε_1 = 0.44% and no massive activations. With sigmoid attention (sum-normalized): Sink^ε_1 = 30.24%. The presence vs. absence of normalization is the decisive factor, not the similarity function (Table 6). At 1B parameters, sigmoid (no normalization) achieves validation loss 3.10 vs. 3.07 for softmax, with Sink^ε_1 dropping from 45.11% to 2.46% (Section 7.4, Figure 8, Right). Status: **supported**.

6. **C6: Weight decay has a non-monotonic effect on attention sink.** No weight decay yields 15.20% sink; γ = 0.5 peaks at 41.08%; γ ≥ 2.0 collapses to near zero as optimization degrades (valid loss rising from 3.80 to 5.24). Status: **supported**.

7. **C7: Instruction tuning does not significantly affect attention sink.** Base vs. chat comparisons: Mistral-7B 97.49% vs. 88.34%, LLaMA2-7B 92.47% vs. 92.88%, LLaMA2-13B 91.69% vs. 90.94%, LLaMA3-8B 99.02% vs. 98.85% (Table 1, Right). Status: **supported**.

---

## Open Questions

1. **How do attention sinks on non-initial word tokens relate to pre-training?** Sun et al. (2024) and Yu et al. (2024) observed sinks on semantically light tokens (periods, newlines) at varying positions. This paper studies only the fixed first-position sink. The authors explicitly leave this for future work (Section 8). Not addressed.

2. **Does attention sink benefit or harm downstream performance?** Within the Pythia family, larger models show both stronger sinks and higher HellaSwag accuracy. But across families, OPT has stronger sinks than Pythia at comparable scale with similar downstream performance (Figure 10). The causal relationship remains unclear. Not addressed.

3. **Would sigmoid attention maintain no attention sink at scales significantly beyond 1B?** The 1B model shows near-zero sinks (2.46% by proxy scores), but scaling behavior beyond this is unknown. The slight validation loss gap (3.10 vs. 3.07) may widen or narrow. Not addressed.

4. **How does attention sink interact with context extension and long-context performance?** The paper focuses on pre-training dynamics but does not study how sinks affect context utilization — a connection relevant to the streaming inference and KV cache applications that motivate the work. Not addressed.

---

## Core References and Why They Are Referenced

### Direct Predecessors

- **Xiao et al. (2023)** -- *Efficient Streaming Language Models with Attention Sinks.* Coined the term "attention sink" and exploited it for streaming inference (StreamingLLM). The present paper extends this by systematically investigating when and why sinks emerge during pre-training, identifying softmax normalization as the root cause.

- **Sun et al. (2024)** -- *Massive Activations in Large Language Models.* Identified massive activations (disproportionately large hidden state values) in the first token and proposed KV biases to alleviate them. The present paper builds on this by showing key biases alone suffice (value biases unnecessary) and traces the root cause to softmax normalization.

- **Cancedda (2024)** -- *Spectral Filters, Dark Signals, and Attention Sinks.* Attributed attention sinks to large hidden state norms of the first token. The present paper goes further by showing that the cosine similarity (not the norm product) between first-token keys and queries drives the phenomenon.

### Attention Mechanism Analysis

- **Bondarenko et al. (2023)** -- *Quantizable Transformers.* Observed strong outliers in Transformer attention linked to heads learning "not to update residuals." Hypothesized that the interplay among softmax, residual connections, and LayerNorm encourages this behavior.

- **Guo et al. (2024a)** -- *Active-Dormant Attention Heads.* Concurrent work providing theoretical analysis on the Bigram-Backcopy task showing that replacing softmax with ReLU removes attention sink, consistent with this paper's findings about normalization.

- **Ramapuram et al. (2024)** -- *Theory, Analysis, and Best Practices for Sigmoid Self-Attention.* Concurrent work providing theoretical and practical analysis of sigmoid attention in Transformers, complementing this paper's empirical findings on sigmoid attention eliminating sinks.

### Foundational Architecture

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* The original Transformer architecture whose softmax attention mechanism is identified as the root cause of attention sinks.

- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* RoPE is used in the controlled experiments and evaluated alongside other PE types. Proposition 4 derives bounds on attention scores for RoPE with repeated tokens.

- **Press et al. (2021)** -- *Train Short, Test Long: ALiBi.* ALiBi evaluated alongside other PE types. Proposition 3 proves no attention sink exists for repeated tokens with ALiBi.

### Models Used in Evaluation

- **Touvron et al. (2023)** -- *Llama 2.* LLaMA2-7B/13B Base and Chat models evaluated for attention sink metrics across model scales and base/chat comparisons.

- **Dubey et al. (2024)** -- *The Llama 3 Herd of Models.* LLaMA3-8B Base provides the primary visualization model (Figure 2) and is evaluated for attention sink across different inputs and model variants.

- **Biderman et al. (2023)** -- *Pythia: A Suite for Analyzing Large Language Models.* The Pythia suite (14M–12B) provides the smallest model (14M) demonstrating attention sinks and the complete scaling analysis across 10 model sizes.

- **Radford et al. (2019)** -- *Language Models Are Unsupervised Multitask Learners.* GPT2 family evaluated; GPT2-XL uniquely retains sinks with repeated tokens due to learnable PE (Table 1, Table 7).

### Training and Optimization

- **Loshchilov & Hutter (2017)** -- *Decoupled Weight Decay Regularization.* AdamW optimizer used in all pre-training experiments. Weight decay's non-monotonic effect on attention sink is a key finding (Table 2).

- **Gao et al. (2020)** -- *The Pile: An 800GB Dataset of Diverse Text for Language Modeling.* The Pile provides training data (5B tokens) and the 17-domain evaluation for input domain analysis.
