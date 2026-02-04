---
title: "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation"
authors: "Press, Smith, Lewis"
year: 2022
venue: "ICLR 2022"
paper_type: "conference-paper"
categories: ["position-encoding", "context-extension"]
scope: ["positional encoding", "length extrapolation", "language modeling"]
benchmarks_used: ["perplexity-wikitext103"]
models_introduced: []
models_evaluated: []
key_claims:
  - id: C1
    claim: "Sinusoidal position embeddings fail to extrapolate beyond 20-50 tokens past the training length"
    evidence: "Section 2.2, Figure 1, Tables 2-3"
    status: supported
  - id: C2
    claim: "Extrapolation ability is determined by the position method, not other architecture choices"
    evidence: "Section 2.2, controlled comparison holding all other hyperparameters constant"
    status: supported
  - id: C3
    claim: "ALiBi trained on L=512 outperforms sinusoidal trained on L=3072 on WikiText-103 (18.40 vs 18.67 PPL)"
    evidence: "Section 4.1, Figure 4, Table 5"
    status: supported
  - id: C4
    claim: "ALiBi incurs no runtime penalty vs sinusoidal (within 1% training, 3% inference) and only 0-100MB extra memory"
    evidence: "Section 3, Figure 2, Table 1"
    status: supported
  - id: C5
    claim: "At 1.3B scale, ALiBi L=1024 outperforms sinusoidal L=2048 (8.92 vs 9.01 PPL) while being 11% faster and using 3.1 GB less memory"
    evidence: "Section 4.2, Figure 5, Table 11"
    status: supported
  - id: C6
    claim: "ALiBi's extrapolation gains under nonoverlapping inference are primarily explained by reduced early token curse, not genuine long-range context utilization"
    evidence: "Appendix B, Figure 11, Tables 13-15"
    status: supported
  - id: C7
    claim: "The geometric slope set generalizes across text domains (Wikipedia, books, web text), model sizes (247M to 1.3B), and training compute budgets without retuning"
    evidence: "Section 4, Tables 5, 8, 11-12"
    status: supported
cross_references:
  - target: 2017-12-attention-is-all-you-need
    type: extends
    detail: "Replaces the Transformer's sinusoidal positional encodings with linear attention biases"
  - target: 2024-01-roformer-rope
    type: contradicts
    detail: "ALiBi finds RoPE fails at extrapolation; later work (PI, NTK, YaRN) shows RoPE can be adapted for extrapolation"
  - target: 2023-06-pi-positional-interpolation
    type: complementary
    detail: "PI addresses the same extrapolation problem for RoPE that ALiBi avoids by design"
  - target: 2023-06-rope-ntk
    type: complementary
    detail: "NTK-aware RoPE scaling proposes an alternative approach to RoPE-based extrapolation"
  - target: 2024-05-yarn-context-extension
    type: complementary
    detail: "YaRN extends RoPE with NTK-aware scaling, offering a post-hoc alternative to ALiBi's built-in extrapolation"
  - target: 2023-12-landmark-attention-infinite-context
    type: complementary
    detail: "Landmark attention cites ALiBi as a method that dampens long-range attention, incompatible with selective retrieval"
  - target: 2020-04-longformer-long-document-transformer
    type: complementary
    detail: "Longformer adapts models to longer sequences but requires partial training on longer inputs, unlike ALiBi which needs no additional long-sequence training"
  - target: 2024-05-attention-sinks-streaming
    type: complementary
    detail: "Attention sinks work relates to ALiBi's finding that vertical attention patterns target special tokens; both address how models handle position beyond training length"
  - target: 2025-07-position-bias-transformers
    type: extended-by
    detail: "Provides theoretical characterization of ALiBi's decay mask: per-layer exponential decay (Lemma 4.4) and a non-monotonic multi-layer trade-off with critical point x* = t/(e^m - 1) (Theorem 4.5)"
  - target: 2025-04-attention-sink-emerges
    type: complementary
    detail: "Gu et al. evaluate ALiBi alongside other PE types and show PE choice does not affect attention sink emergence; proves (Proposition 3) that ALiBi produces no attention sink with repeated tokens due to monotonic distance penalties"
  - target: 2025-04-pine-eliminating-position-bias
    type: complementary
    detail: "PINE's mechanistic analysis identifies ALiBi-style PE-induced distance penalties as one of two causes of position bias; PINE eliminates this bias through importance-based position re-assignment"
open_questions:
  - question: "Does ALiBi's recency bias limit its effectiveness on tasks requiring long-range retrieval?"
    addressed_by: 2024-02-lost-in-the-middle
  - question: "Can ALiBi be combined with methods that genuinely exploit contexts longer than L tokens, given that its extrapolation gains appear to come from reduced early token curse rather than longer-range attention?"
    addressed_by: null
  - question: "How does ALiBi perform in encoder-decoder or bidirectional settings?"
    addressed_by: null
  - question: "Can slope hyperparameters be automatically optimized rather than manually chosen, without sacrificing extrapolation?"
    addressed_by: null
---
# Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation

**Authors:** Ofir Press, Noah A. Smith, Mike Lewis (University of Washington, Facebook AI Research, Allen Institute for AI)
**Date:** April 2022, ICLR 2022 (arXiv:2108.12409)

---

## Core Research Problem

Since the introduction of the Transformer by Vaswani et al. (2017), a fundamental question remained unanswered: how can a model achieve **extrapolation** at inference time for sequences longer than those seen during training? Training on longer sequences improves predictions but is expensive -- training speed decreases substantially as input subsequence length L increases (Figure 7, Appendix). Before Transformers, RNN language models were routinely trained on shorter sequences and assumed to generalize to longer contexts at inference (Mikolov et al., 2010; Zaremba et al., 2014). Vaswani et al. (2017) speculated that Transformers "may [...] extrapolate to sequence lengths longer than the ones encountered during training," but this was never verified.

The authors show for the first time that:

1. **Sinusoidal position embeddings** (Vaswani et al., 2017), despite being theoretically capable of representing arbitrary positions, fail to extrapolate in practice -- perplexity degrades after just 20--50 tokens beyond L (Section 2.2, Figure 1).
2. **Rotary position embeddings** (Su et al., 2021) improve over sinusoidal by 100--200 extra tokens but still degrade, and are 32% slower to train and 48% slower for inference (Table 1).
3. **T5 bias** (Raffel et al., 2020) achieves meaningful extrapolation (600--800 extra tokens) but is at least 2x slower than sinusoidal during training, eliminating any efficiency advantage from training on shorter sequences (Table 1).

**The core challenge is: enabling Transformer language models to train on short sequences and reliably extrapolate to longer sequences at inference time, without incurring additional runtime cost or requiring extra learned parameters.**

---

## Problem Solutions

The paper introduces **Attention with Linear Biases (ALiBi)**, a position method that replaces positional embeddings entirely with a static, non-learned linear bias added to attention scores.

1. **No positional embeddings.** ALiBi removes all position embeddings from the network. Instead, it adds a penalty to each query-key attention score that is proportional to the distance between the query and key positions.
2. **Head-specific slopes.** Each attention head uses a different slope m, drawn from a fixed geometric sequence, creating a multi-scale distance penalty across heads -- some heads attend more locally, others more broadly.
3. **Zero-cost implementation.** The linear biases are folded into the existing causal mask matrix, adding no operations to the network. Runtime is within 1% of sinusoidal during training and within 3% for inference, and memory overhead is negligible (0--100MB).

---

## Approach Details

### Method

In standard Transformer attention, position embeddings are added to word embeddings at the bottom of the network. The attention sublayer computes, for the ith query q_i and the first i keys K:

> softmax(q_i K^T)

ALiBi removes all position embeddings and instead modifies the attention computation to:

> softmax(q_i K^T + m * [-(i-1), ..., -2, -1, 0])

where m is a **head-specific scalar slope** that is fixed before training and never updated. The bias vector assigns a penalty of 0 to the most recent key (position i), -m to the key one step back, -2m two steps back, and so on. The ALiBi bias is **not** multiplied by the sqrt(d_k) scaling factor from Vaswani et al. (2017) (footnote 10, Section 3).

### Key Technical Components

**Slope selection.** For a model with n heads, the slopes form a geometric sequence starting at 2^(-8/n) with ratio 2^(-8/n):

- For 8 heads: 1/2^1, 1/2^2, ..., 1/2^8
- For 16 heads: the 8-head slopes are interpolated by geometrically averaging consecutive pairs, yielding 1/2^0.5, 1/2^1, 1/2^1.5, ..., 1/2^8

The authors found that slopes in the (0, 1) range work best, with density increasing toward 0. This slope set was chosen once on WikiText-103 and reused without modification across all other domains, model sizes, and compute budgets (Section 4). Making slopes trainable did not yield strong extrapolation and slowed training by 3% (footnote 11).

**Implementation.** ALiBi is implemented by modifying the causal mask matrix: instead of a binary mask, the mask incorporates the per-head linear biases. Since the mask is already applied before softmax, this adds no extra operations. The mask grows from L x L to n x L x L (where n is the number of heads), accounting for the small memory increase (Section 3).

**Inductive bias toward recency.** ALiBi penalizes attention between distant query-key pairs, with different heads applying different penalty rates. This creates a recency bias that the authors hypothesize is beneficial both for language modeling quality and for extrapolation.

**Design principles shared with rotary and T5 bias.** Like these methods, ALiBi (1) injects position information at every layer (not just the first), and (2) does not add position information to the value vectors of self-attention. The authors hypothesize that both properties are beneficial for extrapolation: since the output of each attention sublayer is a weighted sum of value vectors, keeping values position-free means layer outputs contain no explicit position information (Section 3).

### Experimental Setup

**WikiText-103 experiments.** The base model is the Transformer LM of Baevski & Auli (2018): 16 layers, dimension 1024, 8 heads, feedforward dimension 4096, tied embeddings, 247M parameters. Training corpus: ~103M tokens from English Wikipedia. Training: 205 epochs, varying L from 64 to 3072. No hyperparameters other than the position method and L are changed between runs, including the random seed (Section 2.1).

**Toronto BookCorpus experiments.** Same architecture with tied word embedding/softmax (29K BPE vocabulary). Corpus: ~700M tokens (2.9 GB). Same ALiBi slopes as WikiText-103, no retuning (Appendix A.3).

**CC100+RoBERTa experiments.** 1.3B parameter model: 25 layers, dimension 2048, 16 heads, feedforward dimension 8192. Dataset: 461 GB (RoBERTa corpus + English CC-100). Training: 1 epoch, 50k updates on 128 V100 GPUs (Section 4.2).

Evaluation: nonoverlapping inference (splitting evaluation sequences into L_valid-length subsequences) unless otherwise stated. Sliding window evaluation (stride S=1 or S=512) used for analysis and comparison with prior work (Appendix B).

### Key Results

**Extrapolation on WikiText-103 (247M model, nonoverlapping inference):**

| Model | L_train | L_valid | PPL |
|---|---|---|---|
| Sinusoidal | 3072 | 3072 | 18.67 |
| Rotary | 3072 | 3072 | 18.57 |
| T5 Bias | 3072 | 3072 | 18.01 |
| ALiBi | 512 | 3072 | 18.40 |
| ALiBi | 1024 | 3072 | 17.96 |
| ALiBi | 3072 | 3072 | 17.60 |

- ALiBi trained on L=512 **outperforms** the sinusoidal model trained on L=3072 (18.40 vs. 18.67, statistically significant given sinusoidal std. dev. = 0.24) while being 1.84x faster to train (Section 4.1, Figure 4, Table 5).
- All ALiBi models (L=512 through L=2048) outperform the sinusoidal L=3072 baseline when extrapolating to L_valid=3072.
- ALiBi continually improves perplexity until approximately 3L on WikiText-103; the L=512 model improves even when L_valid exceeds 12k tokens (Figure 1, Table 2). Performance peaks at around 2L.
- At L_valid = L (no extrapolation), ALiBi outperforms sinusoidal, rotary, and T5 bias for every L tested on WikiText-103 (Table 5).

**1.3B parameter model on CC100+RoBERTa:**

| Model | L_train | L_valid | Memory | PPL |
|---|---|---|---|---|
| Sinusoidal | 1024 | 1024 | 26.2 GB | 9.24 |
| ALiBi | 512 | 1024 | 24.6 GB | 9.30 |
| Sinusoidal | 2048 | 2048 | 29.3 GB | 9.01 |
| ALiBi | 1024 | 2048 | 26.2 GB | 8.92 |

- ALiBi trained on L=1024 **outperforms** sinusoidal trained on L=2048 by 0.09 perplexity while using 3.1 GB less memory and training 11% faster (Section 4.2, Figure 5 right, Table 11).
- ALiBi trained on L=512 comes within 0.06 perplexity of sinusoidal trained on L=1024 while using 1.6 GB less memory and training 7% faster (Figure 5 left).
- The sinusoidal model cannot extrapolate at all in this setting -- perplexity degrades immediately when L_valid > L (Figure 6, Table 12).
- When both methods are trained on the same L with 50k updates, ALiBi performs similarly to sinusoidal at L_valid = L (e.g., 9.16 vs. 9.15 for L=1024), but ALiBi maintains performance when extrapolating while sinusoidal degrades catastrophically (Table 12).

**Efficiency comparison (WikiText-103, one V100 GPU, L=1024):**

| Method | Train WPS | Eval WPS | Memory |
|---|---|---|---|
| Sinusoidal | 26.0k | 77.8k | 19.2 GB |
| Rotary | 17.7k | 39.4k | 22.8 GB |
| T5 Bias | 13.0k | 20.2k | 20.9 GB |
| ALiBi | 25.8k | 76.4k | 19.3 GB |

- Speed differences between ALiBi and sinusoidal are within 1% during training and 3% for inference (Figure 2, Table 1).
- T5 Bias is 2x slower for training and 3.8x slower for inference than ALiBi.
- Rotary is 32% slower for training and 48% slower for inference than ALiBi.

**Toronto BookCorpus results (Table 8-9):**

| Model | L_train | L_valid | Valid PPL | Test PPL |
|---|---|---|---|---|
| Sinusoidal | 3072 | 3072 | 14.46 | 11.67 |
| ALiBi | 512 | 3072 | 13.55 | 10.98 |
| ALiBi | 3072 | 3072 | 13.15 | 10.73 |

- Results fully transfer to a different domain (books) using the same slope hyperparameters without retuning (Appendix A.3).

**Sliding window test results on WikiText-103 (Table 7):**

| Model | Params | Test PPL |
|---|---|---|
| Transformer-XL | 257M | 18.3 |
| Shortformer | 247M | 18.15 |
| Staged Training | 247M | 17.56 |
| kNN-LM | 247M | 15.79 |
| Sinusoidal L=3072 | 247M | 18.67 |
| ALiBi L=3072, L_valid=3072 | 247M | 17.66 |

- ALiBi L=3072 surpasses Transformer-XL, Shortformer, and Sandwich Transformer on WikiText-103 test set (Table 7). Results are similar to staged training but fall short of kNN-LM and Routing Transformer, which use orthogonal techniques.

### Analysis: Why ALiBi Works

The authors investigate two possible explanations for ALiBi's improved perplexity at L_valid > L: (1) the model genuinely uses longer contexts for better predictions, or (2) longer subsequences reduce the **early token curse** -- tokens at the beginning of each evaluation subsequence have little context (Appendix B).

Using sliding window evaluation with stride S=1 (giving every prediction maximal context), ALiBi's perplexity remains **flat** as L_valid increases beyond L -- unlike nonoverlapping evaluation where it improves (Figure 11, Table 15). For the L=512 model, sliding window perplexity is 17.98 at L_valid=512 and 18.3 at L_valid=3072. This contrasts with nonoverlapping evaluation where the same model drops from 19.73 to 18.40.

This suggests ALiBi's gains during extrapolation are primarily explained by **reduced early token curse** (explanation 2), not by leveraging longer-range patterns. The sinusoidal model still degrades catastrophically under sliding window evaluation when L_valid > L (PPL explodes from 18.35 to 360.12 for L=512 to L_valid=3072, Table 13).

---

## Limitations and Failure Modes

1. **Extrapolation mechanism is primarily early token curse reduction.** Sliding window analysis (Appendix B) suggests ALiBi may not actually attend beyond L tokens when extrapolating -- it succeeds by gracefully handling positions beyond L rather than exploiting them for richer context. This limits the potential gains from longer contexts.
2. **Performance peaks at ~2L.** While ALiBi maintains stable perplexity beyond 2L, it does not continue improving, limiting the practical extrapolation range. On the CC100+RoBERTa corpus, the L=512 model peaks at L_valid=1012 and the L=1024 model at L_valid=2024 (Section 4.2).
3. **Recency bias tradeoff.** The linear penalty on distance inherently limits long-range attention, which may be undesirable for tasks requiring retrieval of specific information from distant positions (as noted by Mohtashami & Jaggi, 2023, in the context of landmark attention).
4. **Decoder-only evaluation.** All experiments use autoregressive language models; the method's behavior in encoder-decoder or bidirectional settings is not explored.
5. **Limited scale validation.** The largest model is 1.3B parameters. Behavior at 10B+ scale, where models may have different attention dynamics, is unknown.
6. **Slope selection is manual.** The geometric slope sequence was found through a "brief manual exploration of around ten slope sets" (Section 3). Trainable slopes did not work, and random sampling from the exponential distribution had high variance.
7. **Diminishing advantage at larger scale.** On the CC100+RoBERTa corpus, ALiBi no longer outperforms sinusoidal at L_valid = L when both are trained for 50k updates (e.g., 9.16 vs. 9.15 for L=1024, Table 12), unlike the smaller-scale WikiText-103 experiments where ALiBi consistently outperforms at every L.

---

## Conclusions

### Contributions

1. **First systematic demonstration of sinusoidal extrapolation failure.** The paper provides the first controlled experiments showing that sinusoidal position embeddings fail to extrapolate beyond 20--50 tokens past the training length, despite their theoretical design for arbitrary positions (Section 2.2).

2. **Extrapolation depends on the position method.** Holding all other factors constant (architecture, hyperparameters, random seed), the T5 bias enables substantially better extrapolation than sinusoidal or rotary methods, establishing that extrapolation is primarily a function of the position representation (Section 2.2).

3. **ALiBi enables efficient extrapolation.** By replacing position embeddings with a static linear attention bias, ALiBi achieves extrapolation comparable to or better than the T5 bias while matching the sinusoidal method's speed and memory efficiency (Sections 3-4).

4. **Train-short-test-long as a practical strategy.** A 1.3B parameter model trained on L=1024 with ALiBi outperforms a sinusoidal model trained on L=2048, while being 11% faster and using 3.1 GB less memory, demonstrating concrete computational savings (Section 4.2, Table 11).

5. **Robust hyperparameters.** The geometric slope sequence generalizes across text domains (Wikipedia, books, web text), model sizes (247M to 1.3B), and training compute budgets without retuning (Sections 4.1, 4.2, Appendix A.3).

6. **Recency bias benefits language modeling.** Even when not extrapolating, ALiBi matches or outperforms sinusoidal embeddings on WikiText-103 and Toronto BookCorpus, suggesting that the inductive bias toward recency is beneficial for language modeling at smaller scales (Table 5, Figure 4).

### Implications

1. **Position method as the key to context extension.** The finding that extrapolation is controlled by the position method, not other architecture choices, implies that future context extension work should focus on position representations -- a direction validated by subsequent work on PI, NTK-RoPE, and YaRN.

2. **Early token curse as the primary extrapolation mechanism.** The sliding window analysis suggests that ALiBi's nonoverlapping extrapolation gains come from reduced early token curse rather than genuine long-range context utilization (Appendix B). This highlights an open problem: designing position methods that truly exploit longer contexts, not just gracefully degrade.

3. **Trade-off between recency bias and retrieval capability.** ALiBi's success suggests recency is a useful inductive bias for language modeling, but this comes at the cost of limiting long-range retrieval -- a tension that subsequent work on landmark attention, attention sinks, and RoPE-based extensions has attempted to resolve.

---

## Key Claims

**C1. Sinusoidal embeddings cannot extrapolate.** Sinusoidal position embeddings fail after just 20--50 tokens beyond L. For L=512 on WikiText-103, perplexity degrades from 19.91 at L_valid=532 to 20.40 at L_valid=602, then rapidly worsens to 406.01 at L_valid=15512 (Table 2). Status: **supported**.

**C2. Extrapolation is determined by the position method.** Holding architecture, hyperparameters, and random seed constant, the four position methods (sinusoidal, rotary, T5 bias, ALiBi) produce dramatically different extrapolation behavior (Section 2.2, Figure 1). Status: **supported**.

**C3. ALiBi L=512 outperforms sinusoidal L=3072.** On WikiText-103, ALiBi trained on L=512 achieves 18.40 PPL at L_valid=3072, surpassing sinusoidal trained on L=3072 at 18.67 (std. dev. 0.24) while being 1.84x faster to train (Section 4.1, Table 5). Status: **supported**.

**C4. ALiBi matches sinusoidal efficiency.** Speed differences are within 1% for training (25.8k vs. 26.0k WPS at L=1024) and 3% for inference (76.4k vs. 77.8k WPS). Memory overhead is 0--100MB (Table 1). Status: **supported**.

**C5. ALiBi scales to 1.3B parameters.** At 1.3B scale, ALiBi L=1024 outperforms sinusoidal L=2048 by 0.09 PPL (8.92 vs. 9.01) while using 3.1 GB less memory and training 11% faster (Table 11, Figure 5). Status: **supported**.

**C6. Extrapolation gains come from reduced early token curse.** Under sliding window evaluation (S=1), ALiBi perplexity remains flat as L_valid increases beyond L, unlike nonoverlapping evaluation where it improves. This suggests ALiBi does not genuinely attend to longer contexts during extrapolation (Appendix B, Figure 11, Tables 13-15). Status: **supported**.

**C7. Slope hyperparameters generalize without retuning.** The geometric slope set chosen on WikiText-103 transfers to Toronto BookCorpus (different domain) and CC100+RoBERTa (different scale) without modification (Sections 4.1, 4.2, Appendix A.3). Status: **supported**.

---

## Open Questions

1. **Does ALiBi's recency bias limit retrieval tasks?** The linear distance penalty inherently suppresses long-range attention. Subsequent work by Liu et al. (2024) on lost-in-the-middle effects and by Mohtashami & Jaggi (2023) on landmark attention suggests this is a real limitation, but direct evaluation of ALiBi on retrieval-heavy tasks is limited.

2. **Can ALiBi be combined with genuine long-context exploitation?** The analysis in Appendix B shows ALiBi may not actually use contexts beyond L. Can future methods build on ALiBi's stability while genuinely leveraging longer histories?

3. **How does ALiBi perform in encoder-decoder or bidirectional settings?** All experiments are on autoregressive (decoder-only) language models. The behavior of linear attention biases in encoder-decoder settings or bidirectional models remains untested.

4. **Can slope optimization be automated?** The current slope selection process involved manual exploration of ~10 slope sets (Section 3). Trainable slopes did not work, and randomly sampling from the exponential distribution had high variance. An automatic slope selection method that preserves extrapolation would make ALiBi more robust.

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduced the Transformer with sinusoidal position embeddings. ALiBi is proposed as a replacement for this position method, and the paper's inability to extrapolate is a key motivating finding.
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces rotary position embeddings (RoPE), which multiply keys and queries by sinusoidal embeddings at every layer. Used as a baseline; shows better extrapolation than sinusoidal but worse than ALiBi, and is 32--48% slower.
- **Raffel et al. (2020)** -- *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5).* Introduces the T5 relative position bias, which adds learned distance-dependent biases to attention scores. Used as the strongest extrapolation baseline; achieves good extrapolation but is 2x slower than sinusoidal.
- **Shaw et al. (2018)** -- *Self-Attention with Relative Position Representations.* Proposes relative position representations for self-attention. The T5 bias builds on this approach.

### Base Model and Evaluation

- **Baevski & Auli (2018)** -- *Adaptive Input Representations for Neural Language Modeling.* Provides the base 247M Transformer LM architecture used for all WikiText-103 experiments. Uses sinusoidal embeddings with tied embedding and softmax matrices.
- **Merity et al. (2016)** -- *Pointer Sentinel Mixture Models.* Introduces the WikiText-103 corpus used as the primary evaluation benchmark.
- **Khandelwal et al. (2020)** -- *Generalization through Memorization: Nearest Neighbor Language Models (kNN-LM).* Achieves state-of-the-art on WikiText-103 (15.79 test PPL); the method is orthogonal to ALiBi and could potentially be combined.

### Models Compared

- **Dai et al. (2019)** -- *Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context.* Uses a cache-based approach to attend to more tokens during inference. ALiBi's L=3072 model surpasses Transformer-XL on WikiText-103 test set (17.66 vs. 18.3).
- **Press et al. (2021)** -- *Shortformer: Better Language Modeling Using Shorter Inputs.* Introduces staged training and the early token curse concept. ALiBi achieves comparable results to staged training on WikiText-103.
- **Wang & Komatsuzaki (2021)** -- *GPT-J-6B.* Open-source GPT-3 implementation using rotary position embeddings. Cited as evidence of rotary's adoption in large models.
- **Brown et al. (2020)** -- *Language Models Are Few-Shot Learners (GPT-3).* Uses learned position embeddings. ALiBi's 1.3B model trains to match GPT-3's evaluation sequence length (2048) while training on shorter sequences.

### Concurrent and Related Work

- **Wennberg & Henter (2021)** -- *The Case for Translation-Invariant Self-Attention.* Concurrent work adding a radial-basis function bias to attention scores; unlike ALiBi, uses trainable parameters and does not explore extrapolation.
- **Wu et al. (2021)** -- *DA-Transformer: Distance-Aware Transformer.* Multiplies (rather than adds) attention scores by a distance-dependent bias. In the authors' experiments, multiplication degraded performance compared to ALiBi's additive approach (Section 5).
- **Beltagy et al. (2020)** -- *Longformer: The Long-Document Transformer.* Adapts models to longer sequences but requires partial training on longer inputs, unlike ALiBi which requires no additional long-sequence training (Section 5).
