# Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation

**Authors:** Ofir Press, Noah A. Smith, Mike Lewis (University of Washington, Facebook AI Research, Allen Institute for AI)
**Date:** April 2022, ICLR 2022 (arXiv:2108.12409)

---

## Core Research Problem

Since the introduction of the transformer by Vaswani et al. (2017), a fundamental question remained unanswered: how can a model achieve **extrapolation** at inference time for sequences longer than those seen during training? Training on longer sequences improves predictions but is expensive -- training speed decreases substantially as input subsequence length L increases. Before transformers, RNN language models were routinely trained on shorter sequences and assumed to generalize to longer contexts. Vaswani et al. (2017) speculated that transformers "may [...] extrapolate to sequence lengths longer than the ones encountered during training," but this was never verified.

The authors show for the first time that:

1. **Sinusoidal position embeddings** (Vaswani et al., 2017), despite being theoretically capable of representing arbitrary positions, fail to extrapolate in practice -- perplexity degrades after just 20--50 tokens beyond L.
2. **Rotary position embeddings** (Su et al., 2021) improve over sinusoidal by 100--200 extra tokens but still degrade, and are slower to train and run inference.
3. **T5 bias** (Raffel et al., 2020) achieves meaningful extrapolation (600--800 extra tokens) but is at least 2x slower than sinusoidal during training, eliminating any efficiency advantage from training on shorter sequences.

**The core challenge is: enabling transformer language models to train on short sequences and reliably extrapolate to longer sequences at inference time, without incurring additional runtime cost or requiring extra learned parameters.**

---

## Problem Solutions

The paper introduces **Attention with Linear Biases (ALiBi)**, a position method that replaces positional embeddings entirely with a static, non-learned linear bias added to attention scores.

1. **No positional embeddings.** ALiBi removes all position embeddings from the network. Instead, it adds a penalty to each query-key attention score that is proportional to the distance between the query and key positions.
2. **Head-specific slopes.** Each attention head uses a different slope m, drawn from a fixed geometric sequence, creating a multi-scale distance penalty across heads -- some heads attend more locally, others more broadly.
3. **Zero-cost implementation.** The linear biases are folded into the existing causal mask matrix, adding no operations to the network. Runtime is within 1% of sinusoidal during training, and memory overhead is negligible (0--100MB).

---

## Approach Details

### Method

In standard transformer attention, position embeddings are added to word embeddings at the bottom of the network. The attention sublayer computes, for the ith query q_i and the first i keys K:

> softmax(q_i K^T)

ALiBi removes all position embeddings and instead modifies the attention computation to:

> softmax(q_i K^T + m · [-(i-1), ..., -2, -1, 0])

where m is a **head-specific scalar slope** that is fixed before training and never updated. The bias vector assigns a penalty of 0 to the most recent key (position i), -m to the key one step back, -2m two steps back, and so on. The ALiBi bias is **not** multiplied by the sqrt(d_k) scaling factor from Vaswani et al. (2017).

### Key Technical Components

**Slope selection.** For a model with n heads, the slopes form a geometric sequence starting at 2^(-8/n) with ratio 2^(-8/n):

- For 8 heads: 1/2^1, 1/2^2, ..., 1/2^8
- For 16 heads: the 8-head slopes are interpolated by geometrically averaging consecutive pairs, yielding 1/2^0.5, 1/2^1, 1/2^1.5, ..., 1/2^8

The authors found that slopes in the (0, 1) range work best, with density increasing toward 0. This slope set was chosen once on WikiText-103 and reused without modification across all other domains, model sizes, and compute budgets. Making slopes trainable did not yield strong extrapolation and slowed training by 3%.

**Implementation.** ALiBi is implemented by modifying the causal mask matrix: instead of a binary mask, the mask incorporates the per-head linear biases. Since the mask is already applied before softmax, this adds no extra operations. The mask grows from L x L to n x L x L (where n is the number of heads), accounting for the small memory increase.

**Inductive bias toward recency.** ALiBi penalizes attention between distant query-key pairs, with different heads applying different penalty rates. This creates a recency bias that the authors hypothesize is beneficial both for language modeling quality and for extrapolation.

**Design principles shared with rotary and T5 bias.** Like these methods, ALiBi (1) injects position information at every layer (not just the first), and (2) does not add position information to the value vectors of self-attention. The authors hypothesize that both properties are beneficial for extrapolation: since the output of each attention sublayer is a weighted sum of value vectors, keeping values position-free means layer outputs contain no explicit position information.

### Experimental Setup

**WikiText-103 experiments.** The base model is the transformer LM of Baevski & Auli (2018): 16 layers, dimension 1024, 8 heads, feedforward dimension 4096, tied embeddings, 247M parameters. Training corpus: ~103M tokens from English Wikipedia. Training: 205 epochs, varying L from 64 to 3072. No hyperparameters other than the position method and L are changed between runs.

**Toronto BookCorpus experiments.** Same architecture with tied word embedding/softmax (29K BPE vocabulary). Corpus: ~700M tokens. Same ALiBi slopes as WikiText-103, no retuning.

**CC100+RoBERTa experiments.** 1.3B parameter model: 25 layers, dimension 2048, 16 heads, feedforward dimension 8192. Dataset: 461 GB (RoBERTa corpus + English CC-100). Training: 1 epoch, 50k updates on 128 V100 GPUs.

Evaluation: nonoverlapping inference (splitting evaluation sequences into L_valid-length subsequences) unless otherwise stated. Sliding window evaluation (stride S=1 or S=512) used for analysis and comparison with prior work.

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

- ALiBi trained on L=512 **outperforms** the sinusoidal model trained on L=3072 (18.40 vs. 18.67) while being 1.84x faster to train and requiring far less GPU memory.
- All ALiBi models (L=512 through L=2048) outperform the sinusoidal L=3072 baseline when extrapolating to L_valid=3072.
- ALiBi continually improves perplexity until approximately 3L on WikiText-103; the L=512 model improves even at L_valid > 12k tokens. Performance peaks at around 2L.
- At L_valid = L (no extrapolation), ALiBi outperforms sinusoidal, rotary, and T5 bias on WikiText-103 for every L tested.

**1.3B parameter model on CC100+RoBERTa:**

| Model | L_train | L_valid | Memory | PPL |
|---|---|---|---|---|
| Sinusoidal | 1024 | 1024 | 26.2 GB | 9.24 |
| ALiBi | 512 | 1024 | 24.6 GB | 9.30 |
| Sinusoidal | 2048 | 2048 | 29.3 GB | 9.01 |
| ALiBi | 1024 | 2048 | 26.2 GB | 8.92 |

- ALiBi trained on L=1024 **outperforms** sinusoidal trained on L=2048 by 0.09 perplexity while using 3.1 GB less memory and training 11% faster.
- ALiBi trained on L=512 comes within 0.06 perplexity of sinusoidal trained on L=1024 while using 1.6 GB less memory and training 7% faster.
- The sinusoidal model cannot extrapolate at all in this setting -- perplexity degrades immediately when L_valid > L.

**Efficiency comparison (WikiText-103, one V100 GPU):**

| Method | L=1024 Train WPS | L=1024 Eval WPS | L=1024 Memory |
|---|---|---|---|
| Sinusoidal | 26.0k | 77.8k | 19.2 GB |
| Rotary | 17.7k | 39.4k | 22.8 GB |
| T5 Bias | 13.0k | 20.2k | 20.9 GB |
| ALiBi | 25.8k | 76.4k | 19.3 GB |

- Speed differences between ALiBi and sinusoidal are within 1% during training and 3% for inference.
- T5 Bias is 2x slower for training and 3.8x slower for inference than ALiBi.
- Rotary is 32% slower for training and 48% slower for inference than ALiBi.

### Analysis: Why ALiBi Works

The authors investigate two possible explanations for ALiBi's improved perplexity at L_valid > L: (1) the model genuinely uses longer contexts for better predictions, or (2) longer subsequences reduce the **early token curse** -- tokens at the beginning of each evaluation subsequence have little context.

Using sliding window evaluation with stride S=1 (giving every prediction maximal context), ALiBi's perplexity remains **flat** as L_valid increases beyond L -- unlike nonoverlapping evaluation where it improves. This suggests ALiBi's gains during extrapolation are primarily explained by **reduced early token curse** (explanation 2), not by leveraging longer-range patterns. The sinusoidal model still degrades catastrophically under sliding window evaluation when L_valid > L.

### Limitations

1. **Extrapolation mechanism.** The sliding window analysis suggests ALiBi may not actually attend beyond L tokens when extrapolating -- it succeeds by gracefully handling positions beyond L rather than exploiting them for richer context.
2. **Performance peaks at ~2L.** While ALiBi maintains stable perplexity beyond 2L, it does not continue improving, limiting the practical extrapolation range.
3. **Recency bias tradeoff.** The linear penalty on distance inherently limits long-range attention, which may be undesirable for tasks requiring retrieval of specific information from distant positions (as noted by Mohtashami & Jaggi, 2023, in the context of landmark attention).
4. **Decoder-only evaluation.** All experiments use autoregressive language models; the method's behavior in encoder-decoder or bidirectional settings is not explored.

---

## Conclusions

1. **Sinusoidal embeddings cannot extrapolate.** The paper provides the first systematic demonstration that sinusoidal position embeddings, despite their theoretical design for arbitrary positions, fail to extrapolate beyond a few dozen tokens past the training length.

2. **Extrapolation depends on the position method.** Holding all other factors constant, the T5 bias enables substantially better extrapolation than sinusoidal or rotary methods, establishing that extrapolation is primarily a function of the position representation.

3. **ALiBi enables efficient extrapolation.** By replacing position embeddings with a static linear attention bias, ALiBi achieves extrapolation comparable to or better than the T5 bias while matching the sinusoidal method's speed and memory efficiency.

4. **Train-short-test-long as a practical strategy.** A 1.3B parameter model trained on L=1024 with ALiBi outperforms a sinusoidal model trained on L=2048, while being 11% faster and using 3.1 GB less memory -- demonstrating concrete computational savings.

5. **Robust hyperparameters.** The geometric slope sequence generalizes across text domains (Wikipedia, books, web text), model sizes (247M to 1.3B), and training compute budgets without retuning, making ALiBi a drop-in replacement for position embeddings.

6. **Recency bias improves language modeling.** Even when not extrapolating, ALiBi matches or outperforms sinusoidal embeddings, suggesting that the inductive bias toward recency is beneficial for language modeling. This benefit is more pronounced for smaller-scale models and datasets.

7. **Early token curse as the extrapolation mechanism.** Analysis with sliding window evaluation reveals that ALiBi's improved perplexity during extrapolation is largely explained by reduced early token curse rather than genuine long-range context utilization, highlighting a direction for future work.

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations

- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Introduced the transformer with sinusoidal position embeddings. ALiBi is proposed as a replacement for this position method, and the paper's inability to extrapolate is a key motivating finding.
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces rotary position embeddings (RoPE), which multiply keys and queries by sinusoidal embeddings at every layer. Used as a baseline; shows better extrapolation than sinusoidal but worse than ALiBi, and is slower.
- **Raffel et al. (2020)** -- *Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5).* Introduces the T5 relative position bias, which adds learned distance-dependent biases to attention scores. Used as the strongest baseline; achieves good extrapolation but is 2x slower than sinusoidal.
- **Shaw et al. (2018)** -- *Self-Attention with Relative Position Representations.* Proposes relative position representations for self-attention. The T5 bias builds on this approach.

### Base Model and Evaluation

- **Baevski & Auli (2018)** -- *Adaptive Input Representations for Neural Language Modeling.* Provides the base transformer LM architecture used for all WikiText-103 experiments. The model uses sinusoidal embeddings with tied embedding and softmax matrices.
- **Merity et al. (2016)** -- *Pointer Sentinel Mixture Models.* Introduces the WikiText-103 corpus used as the primary evaluation benchmark.
- **Khandelwal et al. (2020)** -- *Generalization through Memorization: Nearest Neighbor Language Models (kNN-LM).* Achieves state-of-the-art on WikiText-103; the method is orthogonal to ALiBi and could potentially be combined with it.

### Models Compared

- **Dai et al. (2019)** -- *Transformer-XL.* Uses a cache-based approach to attend to more tokens during inference. ALiBi's L=3072 model surpasses Transformer-XL on WikiText-103 test set (17.66 vs. 18.3).
- **Press et al. (2021)** -- *Shortformer: Better Language Modeling Using Shorter Inputs.* Introduces staged training and the early token curse concept. ALiBi achieves comparable results to staged training on WikiText-103.
- **Wang & Komatsuzaki (2021)** -- *GPT-J-6B.* Open-source GPT-3 implementation using rotary position embeddings. Cited as evidence of rotary's adoption in large models.
- **Brown et al. (2020)** -- *Language Models Are Few-Shot Learners (GPT-3).* Uses learned position embeddings. ALiBi's 1.3B model trains to match GPT-3's evaluation sequence length (2048) while training on shorter sequences.

### Concurrent and Related Work

- **Wennberg & Henter (2021)** -- *The Case for Translation-Invariant Self-Attention.* Concurrent work adding a radial-basis function bias to attention scores; unlike ALiBi, uses trainable parameters and does not explore extrapolation.
- **Wu et al. (2021)** -- *DA-Transformer: Distance-Aware Transformer.* Multiplies (rather than adds) attention scores by a distance-dependent bias. In the authors' experiments, multiplication degraded performance compared to ALiBi's additive approach.
- **Beltagy et al. (2020)** -- *Longformer.* Adapts models to longer sequences but requires partial training on longer inputs, unlike ALiBi which requires no additional long-sequence training.

---

### Cross-References in Available Papers

- **Mohtashami & Jaggi (2023)** -- *Random-Access Infinite Context Length for Transformers* (`2023-12-landmark-attention-infinite-context`) cites ALiBi as evidence that relative positional encodings fail to extrapolate and notes that ALiBi's approach of dampening long-range attention is incompatible with landmark attention's goal of attending to distant tokens.
- **Liu et al. (2024)** -- *Lost in the Middle* (`2024-02-lost-in-the-middle`) notes ALiBi as the positional encoding method used by MPT-30B-Instruct, one of the evaluated models.
- **Xiao et al. (2024)** -- *Efficient Streaming Language Models with Attention Sinks* (`2024-05-attention-sinks-streaming`) evaluates MPT models using ALiBi and describes how StreamingLLM handles ALiBi by applying contiguous linear biases within the cache. Notes that ALiBi has improved but still limited length extrapolation.
- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation* (`2023-06-pi-positional-interpolation`) cites ALiBi as an alternative positional encoding for length extrapolation but notes it is not applicable to existing RoPE-based LLMs like LLaMA.
- **Peng et al. (2024)** -- *YaRN: Efficient Context Window Extension* (`2024-05-yarn-context-extension`) references ALiBi for context on length extrapolation limitations and credits it for the sliding window perplexity evaluation methodology.
- **Hsieh et al. (2024)** -- *Found in the Middle* (`2024-08-found-in-the-middle`) connects ALiBi's distance-based decay to the positional attention bias patterns they study.
- **Barbero et al. (2025)** -- *Position Bias in Transformers* (`2025-07-position-bias-transformers`) analyzes ALiBi's decay mask formulation as one of the key positional encoding schemes exhibiting recency bias, with formal results in Lemma 4.4 and Theorem 4.5.
- **Lee et al. (2025)** -- *Pos2Distill: Position Bias Distillation* (`2025-11-pos2distill-position-bias-distillation`) cites ALiBi as a relative positional encoding that contributes to recency bias through its integration of token distances into attention computation.
- **Gao et al. (2025)** -- *DroPE: Dropping Positional Embeddings* (`2025-12-drope-dropping-positional-embeddings`) reports that DroPE outperforms ALiBi on all NIAH (Needle-in-a-Haystack) tasks.
