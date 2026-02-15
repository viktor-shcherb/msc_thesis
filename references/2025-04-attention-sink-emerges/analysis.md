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
models_evaluated: ["gpt-2", "llama-2-7b", "llama-2-13b", "llama-3-8b", "llama-3.1-8b", "mistral-7b", "pythia-series", "opt-125m", "opt-350m", "opt-1.3b"]
# NOTE: Paper also evaluates GPT2-Medium, GPT2-Large, GPT2-XL, OPT-2.7B, OPT-6.7B, OPT-13B,
# Jamba-v0.1, and Jamba-1.5-Mini — these need metadata.yaml entries before they can be listed here.
key_claims:
  - id: C1
    claim: "Attention sinks exist universally in auto-regressive LMs with various inputs, even in small models (Pythia-14M) and with random token sequences"
    evidence: "Table 1, Figure 4(Left), Section 3.3"
    status: supported
    scope: "Auto-regressive LMs from 14M to 13B parameters, English text and random tokens, T=64"
    magnitude: "Pythia-14M exhibits sinks; random token Sink ranges from 70.29% (GPT2-XL) to 91.23% (LLaMA3-8B)"
  - id: C2
    claim: "Attention sink emerges during pre-training after effective optimization on sufficient training data; smaller learning rates reduce sink amplitude even with compensating training steps"
    evidence: "Figure 4(Middle, Right), Table 9, Figure 5(Right), Section 4-5"
    status: supported
    scope: "~60M LLaMA-style models trained on the Pile, LR range 1e-4 to 8e-4, data range 50M to 5B tokens"
    magnitude: "Sink emerges between 1k-2k steps; LR 1e-4 at 80k steps yields 6.29% vs 18.18% at LR 4e-4 at 20k steps"
  - id: C3
    claim: "The sink position is determined by the loss function and data distribution, not by positional embedding type -- all PE types (NoPE, absolute, learnable, relative, ALiBi, RoPE) produce attention sinks"
    evidence: "Table 3, Table 10(Right), Figure 5(Middle), Section 5-7.1"
    status: supported
    scope: "~60M LLaMA-style models, 6 PE types tested, single architecture"
    magnitude: "Sink^epsilon_1 ranges from 18.18% (RoPE) to 35.53% (Relative PE) across PE types, all at comparable valid loss except Relative PE"
  - id: C4
    claim: "The first token acts as key biases: its keys have small l2-norm but high cosine similarity with queries, storing extra attention scores while not contributing to value computation"
    evidence: "Figure 2, Table 4 (K biases setup: Sink_*=73.34%, Sink_1=0.00%), Section 3.1, 7.3"
    status: supported
    scope: "LLaMA3-8B (visualization), ~60M controlled models (K biases experiment)"
    magnitude: "K biases absorb 73.34% of sink heads; first-token sink drops to 0.00% with identical valid loss 3.72"
  - id: C5
    claim: "Attention sink stems at least partially from tokens' inner dependence on attention scores due to softmax normalization; replacing softmax with sigmoid attention without normalization eliminates sinks in LMs up to 1B parameters"
    evidence: "Table 6, Figure 8, Table 14(Right), Section 7.4"
    status: supported
    scope: "~60M and 1B LLaMA-style models, sigmoid/ELU+1/identity/MLP kernels tested"
    magnitude: "Sigmoid (no norm) Sink=0.44% vs softmax 18.18% at 60M; Sink=2.46% vs 45.11% at 1B; valid loss gap 3.10 vs 3.07 at 1B"
  - id: C6
    claim: "Weight decay encourages the emergence of attention sink, with moderate values (gamma=0.5) inducing the strongest sink (41.08%), while excessive values (gamma>=2.0) hurt optimization and eliminate it"
    evidence: "Table 2, Section 6"
    status: supported
    scope: "~60M LLaMA-style models, weight decay range 0.0 to 5.0, AdamW optimizer"
    magnitude: "Non-monotonic: 15.20% at gamma=0.0, peak 41.08% at gamma=0.5, collapse to 0.01% at gamma=5.0"
  - id: C7
    claim: "Instruction tuning has insignificant impact on attention sink -- base and chat models have comparable sink metrics"
    evidence: "Table 1(Right), Section 3.4"
    status: supported
    scope: "Mistral-7B, LLaMA2-7B/13B, LLaMA3-8B base vs chat/instruct variants"
    magnitude: "Differences range from 0.17pp (LLaMA3-8B) to 9.15pp (Mistral-7B); no consistent direction"
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
  - target: 2023-12-quantizable-transformers-attention-do-nothing
    type: extends
    detail: "Builds on Bondarenko et al.'s observation that attention heads learn no-op behavior by concentrating on low-information tokens, extending the analysis to identify when and why sinks emerge during pre-training and showing sigmoid attention eliminates sinks"
  - target: 2024-12-transformers-need-glasses-over-squashing
    type: complementary
    detail: "Barbero et al. provide a complementary theoretical analysis: over-squashing from the causal mask topology creates exponentially more information pathways for initial tokens, connecting attention sinks to GNN over-squashing theory"
  - target: 2023-10-mistral-7b
    type: evaluates
    detail: "Mistral 7B is one of five model families used to study attention sink emergence across architectures"
  - target: 2025-10-kimi-linear-attention
    type: extended-by
    detail: "Kimi Linear adopts sigmoid output gating (vs swish) in KDA, citing gated attention as alleviating attention sink; ablation shows sigmoid outperforms no gating and swish gating"
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

Auto-regressive LMs assign disproportionately high attention scores to the first token regardless of its semantic content -- a phenomenon termed **attention sink** by Xiao et al. (2023). This pattern has been exploited for practical applications including streaming generation, KV cache optimization, efficient inference, and model quantization. However, the phenomenon remained poorly understood: it was unclear *when* attention sinks emerge during training, *what factors* cause them, and *why* they appear.

Prior work (Cancedda, 2024; Sun et al., 2024) attributed attention sinks to massive activations -- the first token develops disproportionately large hidden state norms. But this observation described a symptom rather than a root cause. Key questions remained unanswered: Do sinks depend on the positional encoding scheme? Do they require large-scale models? What role does the softmax normalization play?

The core challenge is: **what conditions in LM pre-training -- optimization, data distribution, loss function, and model architecture -- cause attention sinks to emerge, and what is their mechanistic role.**

---

## Problem Solutions

The paper provides a comprehensive empirical study that systematically varies each component of LM pre-training to identify the conditions under which attention sinks emerge. The key findings are:

1. **Attention sinks are universal** -- they appear in all auto-regressive LMs tested, from Pythia-14M to LLaMA3-8B, across all input types (natural text, random tokens), and persist through instruction tuning.
2. **The first token acts as key biases** -- the cosine similarity between the first token's keys and all queries is high despite small key norms, allowing it to store excess attention probability without contributing meaningfully to value computation.
3. **Softmax normalization is the root cause** -- replacing softmax with sigmoid attention without normalization eliminates attention sinks entirely in LMs up to 1B parameters, maintaining comparable validation loss.

---

## Approach Details

### Method

The paper trains a series of controlled ~60M parameter LLaMA-style models, systematically varying one training factor at a time while holding others constant. Each trained model is evaluated using a threshold-based attention sink metric:

> Sink^epsilon_k = (1/L) * Sum_{l=1}^{L} (1/H) * Sum_{h=1}^{H} I(alpha^{l,h}_k > epsilon)

where alpha^{l,h}_k = (1/(T-k+1)) * Sum_{i=k}^{T} A^{l,h}_{i,k} is the importance score for the k-th token in head h of block l. The metric measures the fraction of attention heads across all blocks that exhibit sink behavior at position k. The threshold epsilon = 0.3 is selected for being both strict and relatively insensitive to token length T (Figure 3). All measurements use T = 64.

### Key Technical Components

**First token as key biases.** The first token's hidden state h^l_1 has no involvement of self-attention (since there are no preceding tokens), making it a pure MLP output of the word embedding. From certain blocks onward, h^l_1 develops massive activations (large l2-norm), but layer normalization suppresses these in the key/value projections, producing keys k^{l,h}_1 and values v^{l,h}_1 with *smaller* l2-norms than other tokens (Figure 2, Top). Despite this small norm, the cosine similarity cos(q^{l,h}_t, k^{l,h}_1) is significantly larger than cos(q^{l,h}_t, k^{l,h}_{j!=1}), driving the attention sink (Figure 2, Bottom).

**Learnable key biases experiment.** To confirm the key-bias interpretation, the paper introduces explicit learnable key biases k^{*l,h} with fixed zero value biases v^{*l,h} = 0 (K biases setup). With this design, attention sink shifts entirely from the first token (Sink^epsilon_1 = 0.00%) to the bias position (Sink^epsilon_* = 73.34%), demonstrating that the sink token stores extra attention scores without contributing to value computation (Table 4). Furthermore, when the fixed v^{*l,h} is set to non-zero vectors with increasing l2-norm, attention gradually shifts back from k^{*l,h} to the first token -- because the model cannot cancel out the non-zero value contribution, it prefers to use the first token whose values it can optimize (Table 5).

**Sigmoid attention without normalization.** The paper generalizes the attention output as:

> v^dag_i = Z_i^{-1} * Sum_{j=1}^{i} sim(phi(q_i), phi(k_j)) * v_j

For softmax, phi(.) is identity and sim(q, k) = exp(qk^T/sqrt(d_h)) with Z_i = Sum_j sim(q_i, k_j). Without normalization (Z_i = 1), attention scores for individual tokens are independent -- there is no need to "dump" probability mass on a sink token. Sigmoid attention without normalization achieves comparable validation loss (3.70 vs. 3.73 for softmax) but eliminates attention sinks entirely (Sink^epsilon_1 = 0.44% by proxy attention scores vs. 18.18% for softmax), and also eliminates massive activations (Table 6, Figure 8).

### Theoretical Analysis

**Propositions 1-4** prove that for LMs with NoPE, relative PE, ALiBi, or RoPE, when all input tokens are identical, all hidden states are equal across positions (since P = 0 for these PE types). This disperses the attention sink and produces uniform or distance-dependent attention. For NoPE: A^{l,h}_{t,i} = 1/t uniformly (Proposition 1). For ALiBi: attention follows the monotonic distance penalty, so no sink on the first token (Proposition 3). For RoPE: attention scores are bounded by e^{2*xi}/(e^{2*xi} + (t-1)), decreasing to zero as t grows (Proposition 4). GPT2 (learnable PE) retains attention sinks even with repeated tokens because p_t differs across positions (Table 1, Table 7).

### Experimental Setup

**Controlled pre-training models:** LLaMA-style, d = 768, L = 10, H = 8, FFN intermediate = 1536, ~60M parameters (excluding embeddings). RoPE, pre-norm, RMSNorm, SwiGLU. Trained on 5B tokens from the Pile, context length 2048, batch size 1M tokens, 20k steps (100 warmup), LR = 4e-4 with cosine scheduling, AdamW with weight decay 0.1. Validation: Pile-CC loss. Sink metric: 100 sequences of T = 64 from out-of-training data.

**1B parameter scale-up:** Softmax vs. sigmoid (without normalization). Softmax achieves validation loss 3.07 with Sink^epsilon_1 = 45.11%; sigmoid achieves 3.10 with Sink^epsilon_1 = 2.46% (proxy). Training stability verified through supervised fine-tuning on UltraChat (200k samples, LR = 2e-5, batch size 64, 1 epoch).

**Open-source model evaluation:** GPT2 (124M-1.5B), Pythia (14M-12B), OPT (125M-13B), LLaMA2 (7B, 13B), LLaMA3/3.1 (8B), Mistral (7B), Jamba (v0.1, 1.5 Mini). Input domains: 17 Pile subsets. Downstream evaluation: HellaSwag accuracy (Figure 10, Appendix C.3).

**Reproducibility:** Code available at https://github.com/sail-sg/Attention-Sink. Seeds not explicitly reported. Controlled experiments use a single architecture (~60M LLaMA-style) with one factor varied at a time. No variance estimates across runs reported (limited evidence on run-to-run variability).

### Key Results

**Optimization effects (Section 4):**

| Learning Rate | Training Steps (k) | Sink^epsilon_1 (%) | Valid Loss |
|---|---|---|---|
| 8e-4 | 10 | 23.44 | 3.79 |
| 8e-4 | 20 | 32.23 | 3.70 |
| 4e-4 | 20 (default) | 18.18 | 3.73 |
| 2e-4 | 20 | 11.21 | 3.78 |
| 2e-4 | 40 | 16.81 | 3.68 |
| 1e-4 | 20 | 2.90 | 3.92 |
| 1e-4 | 80 | 6.29 | 3.67 |

- Attention sink emerges between 1k and 2k training steps and increases with continued training (Figure 4, Middle).
- Smaller learning rates delay emergence and reduce final sink amplitude, even with compensating training steps (Table 9). At constant LR x steps product, smaller LR yields less sink (moderate evidence: 3 LR values tested with compensation).
- Batch size (0.25M, 0.5M, 1M, 2M) has no effect on attention sink (Table 10, Left; limited evidence: 4 values tested, single run each).

**Data distribution effects (Section 5):**

- With 50M-100M training tokens, sinks do not emerge even after 5k steps, independent of overfitting behavior (Figure 28 -- 50M and 100M models overfit early but sink stays below 1%).
- Randomizing x_1 ~ Uniform(V) increases the sink (27.03%) because the first token carries even less semantic information.
- When x_1, x_2 ~ Uniform(V), the sink shifts to position 2 (Sink^epsilon_2 = 14.08%, Sink^epsilon_1 = 1.98%).
- Fixing a specific token at position k during pre-training always places the sink at position k (Table 10, Right: fixed at pos 1 yields Sink^epsilon_1 = 74.11%, fixed at pos 2 yields Sink^epsilon_2 = 69.03%, fixed at pos 3 yields Sink^epsilon_3 = 69.64%).

**Loss function effects (Section 6):**

| Weight Decay gamma | 0.0 | 0.001 | 0.01 | 0.1 | 0.5 | 1.0 | 2.0 | 5.0 |
|---|---|---|---|---|---|---|---|---|
| Sink^epsilon_1 (%) | 15.20 | 15.39 | 15.23 | 18.18 | 41.08 | 37.71 | 6.13 | 0.01 |
| Valid Loss | 3.72 | 3.72 | 3.72 | 3.73 | 3.80 | 3.90 | 4.23 | 5.24 |

- Moderate weight decay encourages attention sink; excessive weight decay hurts optimization and eliminates it.
- Prefix language modeling (p > 1) distributes the sink among prefix tokens rather than concentrating it on the first token (Figure 5, Middle).
- Shifted window attention: the sink appears on the absolute first token, not the "relative" first token within each window. Smaller window sizes (64, 128) prevent sink emergence; larger window sizes (512, 1024) allow it (Figure 6, Right).

**Architecture effects (Section 7):**

| PE Type | Sink^epsilon_1 (%) | Valid Loss |
|---|---|---|
| NoPE | 20.35 | 3.81 |
| Absolute PE | 32.73 | 3.74 |
| Learnable PE | 33.13 | 3.79 |
| Relative PE | 35.53 | 5.45 |
| ALiBi | 20.78 | 3.71 |
| Rotary (RoPE) | 18.18 | 3.73 |

- PE type does not affect emergence -- even NoPE models develop sinks (Table 3).
- Post-norm LMs also develop sinks (Sink^epsilon_1 = 13.54%); massive activations exist before post-LN rather than in the hidden states (Figure 7, Left).
- FFN activation function (ReLU, GeLU, Swish, SwiGLU, ReGLU, GeGLU) does not affect sinks; Sink^epsilon_1 ranges from 13.88% to 18.18% across all 6 variants (Table 11).
- Multi-head design (number of heads H = 1, 2, 4, 8; concatenation vs. addition) does not affect sinks (Table 12, Left).

**Attention operation effects (Section 7.4):**

| Attention Operation | Normalization | Sink^epsilon_1 (%) | Valid Loss |
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
- Sigmoid attention (no normalization) has no attention sink across varying learning rates (4e-4, 1e-3, 1e-4) and weight decay ratios (0.0, 0.1, 0.5, 1.0), all yielding Sink^epsilon_1 < 1% (Table 14, Right).

### SFT Training Stability

At the 1B scale, both softmax and sigmoid (no normalization) models show stable supervised fine-tuning on UltraChat: training loss decreases from ~2.6 to ~1.8, gradient norms stabilize around 0.2-0.4 after initial spike, with no instability issues for either attention type (Figure 30, Appendix E).

---

## Limitations and Failure Modes

1. **Scale limited to 1B parameters.** The sigmoid attention experiments scale to 1B parameters, but it is unclear whether attention sinks would remain absent at the 7B+ scales where they are most practically relevant (Section 7.4).

2. **Narrow model family for causal ablations.** Controlled experiments use only LLaMA-style architectures (~60M parameters). While open-source evaluation covers multiple families (GPT2, Pythia, OPT, LLaMA2/3, Mistral, Jamba), the causal ablations isolating individual factors are limited to one architecture.

3. **Only the first-position sink is studied.** Sun et al. (2024) and Yu et al. (2024) observed attention sinks on word tokens with limited semantic information (e.g., periods, newlines) at non-fixed positions. This paper focuses exclusively on the positionally fixed first-token sink (Section 8).

4. **Downstream impact unclear.** The paper establishes that attention sinks emerge during pre-training but does not determine whether they benefit or harm downstream performance. Within the Pythia family, larger models have both more sinks and better HellaSwag accuracy, but the correlation does not hold across model families (Figure 10, Appendix C.3).

5. **Sigmoid attention trade-offs not fully characterized.** The 1B sigmoid model achieves slightly higher validation loss (3.10 vs. 3.07) than softmax. Whether this gap widens or narrows at larger scales, and how it affects downstream tasks beyond SFT training stability, is not established.

6. **Training data limited to English.** All controlled experiments use the Pile dataset. Whether the findings generalize to multilingual or domain-specific pre-training is untested.

7. **Metric sensitivity.** The Sink^epsilon_k metric depends on the threshold epsilon and sequence length T, and the paper acknowledges there is no principled way to select an optimal threshold (Section 3.2).

8. **[Inferred]** No variance estimates or repeated runs are reported for the controlled experiments. All comparisons appear to be single-run, making it difficult to assess whether small differences in Sink^epsilon_1 (e.g., 15.20% vs. 15.39% for gamma=0.0 vs 0.001) are meaningful.

#### Scope and Comparability

- **What was not tested:** Models larger than 1B for the sigmoid attention experiments; non-English training data; models with different tokenizers; architectures beyond decoder-only Transformers (Jamba is evaluated but only for sink metrics, not for the causal ablations); effect of attention sinks on downstream task performance beyond HellaSwag correlation.
- **Comparability notes:** The ~60M model used for controlled experiments is substantially smaller than the open-source models evaluated (7B-13B), so the magnitude of sink metrics may not transfer directly across scales. The paper uses T = 64 for all sink measurements; other work may use different sequence lengths, making direct cross-paper comparison of sink metrics difficult. The proxy attention score computation used for non-softmax operations (replacing the normalization term) is not directly comparable to standard softmax attention scores. The HellaSwag evaluation in Appendix C.3 uses the lm-evaluation-harness platform (Gao et al., 2024), which should be comparable to standard evaluations.

---

## Conclusions

### Contributions

1. **Comprehensive taxonomy of factors affecting attention sink emergence.** Systematically varied optimization (learning rate, batch size, steps), data (amount, distribution, token fixing), loss function (weight decay, prefix LM, window attention), and architecture (PE, normalization, attention design), establishing which factors matter and which do not (Sections 4-7; tested across 6 PE types, 6 FFN activations, 8 attention operations, 8 weight decay values).

2. **Identified the key-bias mechanism.** Demonstrated that the first token's keys act as implicit biases -- minimizing angles with all queries to absorb excess attention -- while its values have negligible l2-norm and do not contribute to the output computation. Confirmed by the K-biases experiment where explicit zero-value key biases absorb 73.34% of attention sink heads (Table 4, Section 7.3).

3. **Identified softmax normalization as a root cause.** Showed that attention sinks stem from tokens' inner dependence on attention scores imposed by the softmax sum-to-one constraint. Removing normalization (sigmoid, ELU+1, or identity kernel without normalization) eliminates sinks while maintaining comparable model quality (Table 6, Figure 8).

4. **Proposed a quantitative metric for attention sink.** The Sink^epsilon_k metric provides a scalar measurement of attention sink strength across all heads and layers, enabling systematic comparisons across architectures and training configurations (Section 3.2).

5. **Proved attention properties under repeated tokens.** Propositions 1-4 establish that for NoPE/relative PE/ALiBi/RoPE, repeated token sequences produce uniform or distance-dependent attention (no sink), while learnable PE models retain sinks due to position-dependent initial embeddings (Section 3.3, Appendix C.1).

### Implications

1. **Alternative attention mechanisms can avoid sinks.** Sigmoid attention without normalization is a viable replacement for softmax that eliminates sinks and massive activations, with comparable training stability through SFT. This could simplify KV cache management, quantization, and streaming inference. [Inference: this aligns with concurrent work by Ramapuram et al. (2024) on sigmoid self-attention.]

2. **Attention sinks are a learned optimization strategy, not an architectural necessity.** The emergence depends on effective optimization with sufficient data, not on any specific architectural component. This suggests sinks are the model's learned solution to the softmax normalization constraint rather than a fundamental requirement for language modeling.

3. **Practical interventions are possible.** Weight decay tuning, prefix language modeling, learnable key biases, or architectural changes to the attention normalizer can control sink behavior without fundamentally changing the model (Sections 6-7).

---

## Key Claims

1. **C1: Attention sinks are universal across auto-regressive LMs.** Even Pythia-14M (14 million parameters) exhibits attention sinks. Sinks persist with random token inputs (GPT2-XL: 70.29%, LLaMA3-8B: 91.23%) but disappear with repeated tokens for RoPE/ALiBi models due to dispersed massive activations (Table 1, Figure 4, Left). Input domain across 17 Pile subsets has negligible effect (Figure 9). Scope: auto-regressive LMs from 14M to 13B, English text and random tokens. Magnitude: Pythia-14M through LLaMA3-8B all show sinks; random-token sinks range 70-91%. Tested across 5 model families and 17 data domains (strong evidence for universality within tested scope). Status: **supported**.

2. **C2: Attention sink emerges during pre-training after effective optimization on sufficient data.** Sinks appear between 1k-2k training steps in the default setup and grow with continued training (Figure 4, Middle). With 50M-100M training tokens, sinks do not emerge even after 5k steps, independent of overfitting (Figure 28). Smaller learning rates (1e-4 vs. 4e-4) reduce sink amplitude from 18.18% to 2.90% at 20k steps, and to 6.29% even with 4x compensating steps (Table 9). Scope: ~60M LLaMA-style model, Pile dataset, LR range 1e-4 to 8e-4. Magnitude: 6.29% (LR 1e-4, 80k steps) vs. 18.18% (LR 4e-4, 20k steps). Single architecture tested (moderate evidence). Status: **supported**.

3. **C3: Sink position depends on loss function and data distribution, not PE type.** All PE types -- NoPE (20.35%), absolute (32.73%), learnable (33.13%), relative (35.53%), ALiBi (20.78%), RoPE (18.18%) -- produce sinks at comparable validation loss except relative PE (Table 3). Fixing a token at position k during pre-training always places the sink at position k: pos 1 yields 74.11%, pos 2 yields 69.03%, pos 3 yields 69.64% (Table 10, Right). Prefix LM distributes sinks among prefix tokens (Figure 5, Middle). Scope: ~60M model, 6 PE types, 3 fixed positions. Magnitude: Sink^epsilon_1 varies 18-36% across PE types but is present in all. Tested with 6 PE types and 3 position-fixing conditions (moderate evidence). Status: **supported**.

4. **C4: The first token acts as key biases, not value contributors.** Introducing explicit learnable key biases with zero-value biases (K biases) absorbs 73.34% of sink heads while reducing first-token sinks to 0.00%, with identical validation loss 3.72 (Table 4). The key biases eliminate massive activations entirely (Figure 7, Middle). Increasing the l2-norm of fixed value biases gradually shifts the sink back to the first token: at v' the sink* drops from 73.34% to 70.03%, at 5v' to 44.43%, at 20v' to 1.51% while Sink_1 rises from 0.00% to 25.88% (Table 5). Scope: ~60M model, 5 bias configurations. Magnitude: 73.34% absorption by K biases with 0.00% first-token sink. Confirmed by graded value-bias experiments with 7 norm settings (strong evidence). Status: **supported**.

5. **C5: Softmax normalization is the root cause.** With sigmoid attention (no normalization): Sink^epsilon_1 = 0.44% and no massive activations. With sigmoid attention (sum-normalized): Sink^epsilon_1 = 30.24%. The presence vs. absence of normalization is the decisive factor, not the similarity function (Table 6). At 1B parameters, sigmoid (no normalization) achieves validation loss 3.10 vs. 3.07 for softmax, with Sink^epsilon_1 dropping from 45.11% to 2.46% (Section 7.4, Figure 8, Right). Robustness confirmed across varying LR and weight decay (Table 14, Right -- 6 configurations, all Sink < 1%). Scope: ~60M and 1B LLaMA-style models, 8 attention operation variants. Magnitude: 0.44% vs. 18.18% at 60M; 2.46% vs. 45.11% at 1B. Tested with 8 attention operations and 2 model scales (strong evidence, though limited to 1B max). Status: **supported**.

6. **C6: Weight decay has a non-monotonic effect on attention sink.** No weight decay yields 15.20% sink; gamma = 0.001 yields 15.39%; gamma = 0.5 peaks at 41.08%; gamma >= 2.0 collapses to near zero as optimization degrades (valid loss rising from 3.80 at gamma = 0.5 to 5.24 at gamma = 5.0) (Table 2). Scope: ~60M model, gamma range 0.0-5.0, AdamW. Magnitude: non-monotonic from 15.20% to peak 41.08% to 0.01%. Tested with 8 weight decay values (moderate evidence; single architecture, no repeated runs). Status: **supported**.

7. **C7: Instruction tuning does not significantly affect attention sink.** Base vs. chat comparisons: Mistral-7B 97.49% vs. 88.34%, LLaMA2-7B 92.47% vs. 92.88%, LLaMA2-13B 91.69% vs. 90.94%, LLaMA3-8B 99.02% vs. 98.85% (Table 1, Right). Block-wise and head-wise distributions are also similar between base and instruct variants (Figures 19-21). Scope: 4 model pairs (Mistral-7B, LLaMA2-7B/13B, LLaMA3-8B). Magnitude: differences range from 0.17pp to 9.15pp with no consistent direction. Limited evidence: 4 model pairs, no controlled instruction tuning experiment. Status: **supported**.

---

## Open Questions

1. **How do attention sinks on non-initial word tokens relate to pre-training?** Sun et al. (2024) and Yu et al. (2024) observed sinks on semantically light tokens (periods, newlines) at varying positions. This paper studies only the fixed first-position sink. The authors explicitly leave this for future work (Section 8). Not addressed.

2. **Does attention sink benefit or harm downstream performance?** Within the Pythia family, larger models show both stronger sinks and higher HellaSwag accuracy. But across families, OPT has stronger sinks than Pythia at comparable scale with similar downstream performance (Figure 10). The causal relationship remains unclear. Not addressed.

3. **Would sigmoid attention maintain no attention sink at scales significantly beyond 1B?** The 1B model shows near-zero sinks (2.46% by proxy scores), but scaling behavior beyond this is unknown. The slight validation loss gap (3.10 vs. 3.07) may widen or narrow. Not addressed.

4. **How does attention sink interact with context extension and long-context performance?** The paper focuses on pre-training dynamics but does not study how sinks affect context utilization -- a connection relevant to the streaming inference and KV cache applications that motivate the work. Not addressed.

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

- **Biderman et al. (2023)** -- *Pythia: A Suite for Analyzing Large Language Models.* The Pythia suite (14M-12B) provides the smallest model (14M) demonstrating attention sinks and the complete scaling analysis across 10 model sizes.

- **Radford et al. (2019)** -- *Language Models Are Unsupervised Multitask Learners.* GPT2 family evaluated; GPT2-XL uniquely retains sinks with repeated tokens due to learnable PE (Table 1, Table 7).

- **Zhang et al. (2022)** -- *OPT: Open Pre-trained Transformer Language Models.* OPT family (125M-13B) evaluated; OPT shows stronger sinks than Pythia at comparable scale but similar downstream performance (Figure 10).

### Training and Optimization

- **Loshchilov & Hutter (2017)** -- *Decoupled Weight Decay Regularization.* AdamW optimizer used in all pre-training experiments. Weight decay's non-monotonic effect on attention sink is a key finding (Table 2).

- **Gao et al. (2020)** -- *The Pile: An 800GB Dataset of Diverse Text for Language Modeling.* The Pile provides training data (5B tokens) and the 17-domain evaluation for input domain analysis.
