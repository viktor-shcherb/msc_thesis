---
title: "YaRN: Efficient Context Window Extension of Large Language Models"
authors: "Peng, Quesnelle, Fan, Shippole"
year: 2024
venue: "ICLR 2024"
paper_type: conference-paper
categories: ["context-extension", "position-encoding"]
scope: ["RoPE-based LLMs", "context window extension", "positional encoding interpolation"]
benchmarks_used: ["perplexity-proofpile", "perplexity-govreport", "passkey-retrieval", "arc", "hellaswag", "mmlu", "truthfulqa"]
models_introduced: []
models_evaluated: ["llama-2-7b", "llama-2-13b", "mistral-7b", "code-llama-7b"]
key_claims:
  - id: C1
    claim: "YaRN achieves state-of-the-art context extension with 10x fewer tokens than Code Llama and 2.5x fewer training steps than PI"
    evidence: "Section 4, Table 1 (400M tokens vs 1B for PI/NTK at s=2)"
    status: supported
  - id: C2
    claim: "NTK-by-parts interpolation preserves high-frequency RoPE dimensions while interpolating low-frequency dimensions, outperforming both PI and NTK-aware after fine-tuning"
    evidence: "Section 3.2, Definition 2, Tables 1-2"
    status: supported
  - id: C3
    claim: "Attention temperature scaling with sqrt(1/t) = 0.1*ln(s) + 1 uniformly improves perplexity across positions and samples, with near-universal applicability across LLaMA and Llama 2 model sizes"
    evidence: "Section 3.4, Equation 22, Figures 2-4, Appendix A.2"
    status: supported
  - id: C4
    claim: "YaRN (s=32) models trained on 64k data extrapolate to 128k context with continued declining perplexity, demonstrating train-short-test-long"
    evidence: "Table 2, Section 4.2"
    status: supported
  - id: C5
    claim: "Transfer learning from s=16 to s=32 requires only 200 additional steps with average 0.49% benchmark score drop"
    evidence: "Table 3, Section 4.3.3"
    status: supported
  - id: C6
    claim: "YaRN 7B/13B (s=32) achieve >99% passkey retrieval accuracy at 128k context"
    evidence: "Table 5, Section 4.3.2"
    status: supported
  - id: C7
    claim: "Dynamic-YaRN outperforms Dynamic-PI for context extension of pretrained models without any fine-tuning"
    evidence: "Figure 5, Appendix B.3"
    status: supported
cross_references:
  - target: 2023-06-pi-positional-interpolation
    type: extends
    detail: "YaRN improves on PI's uniform interpolation by preserving high-frequency dimensions through NTK-by-parts and adding attention temperature scaling"
  - target: 2023-06-rope-ntk
    type: extends
    detail: "YaRN formalizes NTK-aware scaling (Definition 1) and extends it with NTK-by-parts to avoid out-of-bounds extrapolation; first author (bloc97) is the same"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "YaRN modifies the RoPE frequency allocation per dimension via targeted interpolation"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "ALiBi provides built-in extrapolation via linear biases; YaRN extends RoPE-based models post-hoc. ALiBi's sliding window perplexity methodology (S=256) is adopted by YaRN"
  - target: 2023-12-landmark-attention-infinite-context
    type: complementary
    detail: "Landmark attention handles block retrieval via random-access tokens; YaRN handles positional extrapolation. YaRN adopts the passkey retrieval evaluation task from this paper"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: contradicts
    detail: "DroPE shows YaRN's zero-shot extension is equivalent to context cropping (Figure 5) and outperforms YaRN on zero-shot LongBench (30.52 vs 19.94 avg) and NIAH evaluations"
  - target: 2023-10-mistral-7b
    type: evaluates
    detail: "YaRN extends Mistral 7B's context window as one of its evaluation models alongside Llama 2"
  - target: 2024-12-babilong-long-context-reasoning
    type: complementary
    detail: "BABILong evaluates YaRN-extended models on reasoning-in-a-haystack tasks, testing whether context extension methods support genuine long-range reasoning beyond perplexity and passkey retrieval"
  - target: 2024-07-qwen2-technical-report
    type: extended-by
    detail: "Qwen2 adopts YARN combined with Dual Chunk Attention to extend context from 32K to 131K tokens, achieving near-perfect NIAH accuracy at 128K for the 72B and 7B models"
  - target: 2025-04-kimi-vl-technical-report
    type: complementary
    detail: "Kimi-VL uses direct RoPE base frequency scaling (50K to 800K) rather than YARN for 128K context extension"
  - target: 2025-10-kimi-linear-attention
    type: complementary
    detail: "Kimi Linear adopts NoPE for full attention layers, delegating positional encoding entirely to KDA linear attention, avoiding RoPE/YARN extrapolation issues entirely and achieving superior long-context performance (RULER@128k: 84.3 vs 78.8 with RoPE)"
  - target: 2025-07-kimi-k2-open-agentic-intelligence
    type: extended-by
    detail: "Kimi K2 uses YaRN to extend context from 32K (pre-training) to 128K (inference) for its 1.04T parameter MoE model"
  - target: 2024-05-deepseek-v2-moe
    type: extended-by
    detail: "DeepSeek-V2 uses YaRN to extend context from 4K base to 128K, achieving continued perplexity decline at 128K with its Multi-head Latent Attention architecture"
  - target: 2024-12-deepseek-v3-technical-report
    type: extended-by
    detail: "DeepSeek-V3 uses YaRN for two-stage context extension (4K→32K→128K) with 119K H800 GPU hours, achieving perfect NIAH retrieval at 128K"
open_questions:
  - question: "Why does perplexity improvement from context extension not always translate to downstream task performance?"
    addressed_by: 2025-12-drope-dropping-positional-embeddings
  - question: "Can the temperature formula sqrt(1/t) = 0.1*ln(s) + 1 be derived theoretically rather than empirically fitted?"
    addressed_by: null
  - question: "What are the optimal alpha and beta parameters for architectures beyond the LLaMA family?"
    addressed_by: null
  - question: "Does YaRN's targeted interpolation generalize to non-RoPE positional encodings?"
    addressed_by: null
---
# YaRN: Efficient Context Window Extension of Large Language Models

**Authors:** Bowen Peng (bloc97), Jeffrey Quesnelle (emozilla), Honglu Fan, Enrico Shippole (Nous Research, EleutherAI, University of Geneva)
**Date:** November 2023, arXiv:2309.00071v2; published at ICLR 2024

---

## Core Research Problem

Transformer-based LLMs using Rotary Position Embeddings (RoPE) cannot generalize past the sequence length they were trained on. Position Interpolation (PI) by Chen et al. (2023) addresses this by uniformly downscaling position indices from [0, L') to [0, L), but this "blind" approach treats all RoPE frequency dimensions identically. This causes two problems: (1) high-frequency components that encode fine-grained local token distinctions are compressed, degrading short-context performance (Section 3.1, Section 3.2), and (2) the method requires relatively expensive fine-tuning (1000 steps on 1B tokens) (Section 4).

The NTK-aware interpolation by bloc97 (2023) improves non-fine-tuned performance by spreading interpolation pressure across frequencies via a base change from b to b' = b * s^(|D|/(|D|-2)). However, this method slightly extrapolates some dimensions to "out-of-bound" values, making it inferior to PI after fine-tuning (Section 3.1). Furthermore, the theoretical scale factor s does not accurately describe the true context extension scale, requiring the scale to be set higher than expected in practice.

Neither method provides a principled, frequency-aware interpolation that simultaneously preserves high-frequency local information, avoids out-of-bounds extrapolation, corrects for attention entropy changes, and enables efficient transfer learning across scale factors. The core challenge is: **how to extend context windows of RoPE-based LLMs with maximal compute efficiency while surpassing all existing methods in both fine-tuned and non-fine-tuned settings.**

---

## Problem Solutions

YaRN (Yet another RoPE extensioN method) combines three independently motivated fixes to PI's shortcomings into a single method:

1. **NTK-by-parts interpolation** (targeted, frequency-dependent scaling): Classify RoPE dimensions by the ratio r = L/lambda between the original context length L and the dimension's wavelength lambda. High-frequency dimensions (r > beta) are not interpolated at all. Low-frequency dimensions (r < alpha) are fully interpolated by scale s. Intermediate dimensions use a smooth ramp between the two extremes (Section 3.2, Definition 2).

2. **Attention temperature scaling:** Context extension increases attention entropy uniformly across positions and samples. A temperature t in the softmax compensates for this. The optimal temperature follows sqrt(1/t) = 0.1 * ln(s) + 1, fitted empirically across LLaMA 7B-65B and found to generalize to Llama 2 models (Section 3.4, Equation 22).

3. **Dynamic Scaling** (inference-time): Instead of fixing the scale factor s = L'/L throughout inference, dynamically set s = max(1, l'/L) where l' is the current sequence length. This prevents performance degradation below L and allows graceful degradation beyond L' (Section 3.3).

---

## Approach Details

### Method

YaRN modifies RoPE via the general form f'(x_m, m, theta_d) = f(x_m, g(m), h(theta_d)) (Equation 12), combining NTK-by-parts interpolation with attention temperature scaling.

**NTK-by-parts interpolation (Definition 2):**

> g(m) = m
>
> h(theta_d) = (1 - gamma(r(d))) * theta_d/s + gamma(r(d)) * theta_d

Where:
- r(d) = L / lambda_d = L / (2*pi*b^(2d/|D|)) is the ratio of context length to wavelength (Equation 17)
- gamma(r) is a ramp function: 0 if r < alpha, 1 if r > beta, (r - alpha)/(beta - alpha) otherwise (Equation 18)
- For the LLaMA family: alpha = 1, beta = 32

This ensures:
- Dimensions with short wavelength (lambda << L, high frequency): no interpolation, preserving local positional resolution
- Dimensions with long wavelength (lambda >= L, low frequency): full interpolation by s, avoiding any extrapolation
- Intermediate dimensions: smooth blend between the two regimes

**Attention temperature (Equation 21):**

> softmax(q^T_m * k_n / (t * sqrt(|D|)))

With the recommended formula:

> sqrt(1/t) = 0.1 * ln(s) + 1

Implemented as a "length scaling" trick: scale the complex RoPE embeddings by sqrt(1/t), requiring zero changes to the attention mechanism code and zero overhead at inference (Section 3.4).

**YaRN (Definition 3):** The combination of NTK-by-parts interpolation and attention temperature scaling.

### Key Technical Components

**NTK-aware interpolation (Definition 1, formalized from bloc97's Reddit post [6]):** Change the RoPE base from b to b' = b * s^(|D|/(|D|-2)) (Equations 14-16). This spreads interpolation pressure across dimensions: high frequencies scale less, low frequencies scale more. Performs better than PI without fine-tuning, but worse after fine-tuning because some dimensions are slightly extrapolated to out-of-bound values. Code Llama [31] uses this approach with b = 1M. Appendix A.1 provides the mathematical derivation: the constraint is that the lowest frequency dimension must scale by s (matching PI) while the highest frequency stays constant (Equations 23-24).

**Dynamic Scaling (from emozilla's Reddit post [14]):** At each forward pass, update the scale factor to s = max(1, l'/L) where l' is the current sequence length (Section 3.3). Prevents performance discount below L and avoids abrupt degradation at L'. The "Dynamic NTK" interpolation (Dynamic Scaling combined with NTK-aware) works exceptionally well on pretrained models without any fine-tuning (Appendix B.3). Implementation note: when using KV-caching, the KV-embeddings must be cached before applying RoPE, since the RoPE embedding of every token changes when s changes.

**Wavelength analysis (Section 3.2):** RoPE dimensions where wavelength lambda > L have not completed a full rotation during pretraining and encode absolute positional information. Dimensions where lambda << L encode relative local distances. Blind interpolation compresses all dimensions, confusing the model on the positional order of close-by tokens. The ratio r = L/lambda determines which regime each dimension falls into: r < alpha (interpolate fully), r > beta (do not interpolate), with a linear ramp in between.

**Temperature fitting (Appendix A.2):** The formula sqrt(1/t) = 0.1 * ln(s) + 1 is found by fitting sqrt(1/t) at the lowest perplexity against scale extension factor s using NTK-by-parts on LLaMA 7B, 13B, 33B, and 65B without fine-tuning. Tested on 896 16k-token RedPajama documents (Figure 2). The same values apply to Llama 2 7B, 13B, and 70B, suggesting "universality" of the temperature constant (Section 3.4). The optimal value of t is consistent across different samples and different token positions (Figure 4).

### Relationship to Prior Methods

| Method | g(m) | h(theta_d) | Interpolation Type |
|---|---|---|---|
| PI | m/s | theta_d | Blind (uniform) |
| NTK-aware | m | b'^(-2d/\|D\|), b' = b * s^(\|D\|/(\|D\|-2)) | Blind (base change) |
| NTK-by-parts | m | ramp-based mix of theta_d/s and theta_d | Targeted (frequency-dependent) |
| YaRN | m | NTK-by-parts + temperature scaling | Targeted + entropy correction |

### Experimental Setup

**Models.** Llama 2 7B and 13B, extended with s = 16 (64k context) and s = 32 (128k context). Additionally Mistral 7B v0.1 (Appendix B.4). No changes to the LLaMA model architecture other than the RoPE frequency computation (Section 4.1).

**Training (Llama 2).** 400 steps for s = 16 on PG19 dataset chunked into 64k segments, bookended with BOS and EOS tokens. For s = 32: continued from the s = 16 checkpoint for 200 additional steps on the same dataset. Learning rate 2 * 10^{-5}, no weight decay, linear warmup of 20 steps, AdamW with beta_1 = 0.9, beta_2 = 0.95, global batch size 64, Flash Attention 2, PyTorch FSDP (Section 4.1).

**Training (Mistral).** 1000 steps for s = 8 (64k context) using 16k sequence lengths, constant learning rate 1 * 10^{-6}. Then 500 additional steps at s = 16 (128k context). Sliding window attention size set to context window size (effectively disabled). Training data: Together Computer's Long-Data Collections (Appendix B.4).

**Evaluation.** (1) Sliding window perplexity (S = 256, following Press et al. [27]) on Proof-pile (10 random samples with >= 128k tokens) and GovReport (50 documents with >= 16k tokens). (2) Passkey retrieval (10 iterations per context size, passkey placed at random uniform location, 8k-128k range). (3) Hugging Face Open LLM Leaderboard: 25-shot ARC-Challenge, 10-shot HellaSwag, 5-shot MMLU, 0-shot TruthfulQA (Sections 4.3.1-4.3.3).

### Key Results

**Proof-pile perplexity at s = 2 (Table 1, 8k context, Llama 2 7B):**

| Extension Method | Trained Tokens | 2048 | 4096 | 6144 | 8192 | 10240 |
|---|---|---|---|---|---|---|
| PI (s = 2) | 1B | 3.92 | 3.51 | 3.51 | 3.34 | 8.07 |
| NTK (theta = 20k) | 1B | 4.20 | 3.75 | 3.74 | 3.59 | 6.24 |
| YaRN (s = 2) | 400M | **3.91** | **3.50** | 3.51 | **3.35** | **6.04** |

- YaRN matches or surpasses PI and NTK-aware at all evaluation windows while using 2.5x fewer tokens.
- All three methods degrade beyond 8k (their target context), but YaRN degrades least at 10240 (6.04 vs 8.07 for PI, 6.24 for NTK).

**Proof-pile perplexity at extended context (Table 2):**

| Size | Model | Context Window | Method | 8192 | 32768 | 65536 | 98304 | 131072 |
|---|---|---|---|---|---|---|---|---|
| 7B | Together | 32k | PI | **3.50** | 2.64 | >10^2 | >10^3 | >10^4 |
| 7B | Code Llama | 100k | NTK | 3.71 | 2.74 | 2.55 | 2.54 | 2.71 |
| 7B | YaRN (s = 16) | 64k | YaRN | 3.51 | 2.65 | **2.42** | >10^1 | >10^1 |
| 7B | YaRN (s = 32) | 128k | YaRN | 3.56 | 2.70 | 2.45 | **2.36** | **2.37** |
| 13B | Code Llama | 100k | NTK | 3.54 | 2.63 | 2.41 | 2.37 | 2.54 |
| 13B | YaRN (s = 16) | 64k | YaRN | **3.25** | **2.50** | **2.29** | >10^1 | >10^1 |
| 13B | YaRN (s = 32) | 128k | YaRN | 3.29 | 2.53 | 2.31 | **2.23** | **2.24** |

- YaRN is the first method to extend Llama 2's effective context to 128k with declining perplexity throughout.
- The s = 32 models show continued declining perplexity through 128k despite training data limited to 64k tokens, demonstrating successful "train short, test long" (Section 4.2).
- PI-based Together model catastrophically fails beyond 32k. Code Llama perplexity increases beyond ~96k (2.54 to 2.71 at 128k for 7B).
- Transfer learning from s = 16 to s = 32 required only 200 additional steps (Section 4.2).

**GovReport perplexity at 32k context (Table 4):**

| Size | Model | Context Window | Method | Perplexity |
|---|---|---|---|---|
| 7B | Together | 32k | PI | 3.67 |
| 7B | Code Llama | 100k | NTK | 4.44 |
| 7B | YaRN (s = 16) | 64k | YaRN | **3.59** |
| 7B | YaRN (s = 32) | 128k | YaRN | 3.64 |
| 13B | Code Llama | 100k | NTK | 4.22 |
| 13B | YaRN (s = 16) | 64k | YaRN | **3.35** |
| 13B | YaRN (s = 32) | 128k | YaRN | 3.39 |

- YaRN outperforms both PI and NTK-aware baselines on GovReport, consistent with Proof-pile results.

**Open LLM Leaderboard benchmarks (Table 3):**

| Size | Model | Context Window | Method | ARC-c | HellaSwag | MMLU | TruthfulQA |
|---|---|---|---|---|---|---|---|
| 7B | Llama 2 | 4k | None | **53.1** | 77.8 | **43.8** | 39.0 |
| 7B | Together | 32k | PI | 47.6 | 76.1 | 43.3 | **39.2** |
| 7B | Code Llama | 100k | NTK | 39.9 | 60.8 | 31.1 | 37.8 |
| 7B | YaRN (s = 16) | 64k | YaRN | 52.3 | **78.8** | 42.5 | 38.2 |
| 7B | YaRN (s = 32) | 128k | YaRN | 52.1 | 78.4 | 41.7 | 37.3 |
| 13B | Llama 2 | 4k | None | **59.4** | 82.1 | **55.8** | 37.4 |
| 13B | Code Llama | 100k | NTK | 40.9 | 63.4 | 32.8 | **43.8** |
| 13B | YaRN (s = 16) | 64k | YaRN | 58.1 | **82.3** | 52.8 | 37.8 |
| 13B | YaRN (s = 32) | 128k | YaRN | 58.0 | 82.2 | 51.9 | 37.3 |

- YaRN shows minimal degradation from Llama 2 baselines: 7B s = 16 loses 0.8 on ARC-c, gains 1.0 on HellaSwag, loses 1.3 on MMLU, loses 0.8 on TruthfulQA.
- Code Llama NTK shows severe degradation: 13B ARC-c drops from 59.4 to 40.9 (-18.5), HellaSwag from 82.1 to 63.4 (-18.7), MMLU from 55.8 to 32.8 (-23.0).
- Average drop from s = 16 to s = 32 is 0.49%, indicating negligible cost of iterative context extension (Section 4.3.3).

**Passkey retrieval (Table 5):**

| Size | Model | s | Context Window | Training Data | Method | Max Passkey Context | Accuracy |
|---|---|---|---|---|---|---|---|
| 7B | Together | 4 | 32k | 32k | PI | 32k | 100% |
| 7B | Code Llama | 88.6 | 100k | 16k | NTK | 112k | 94.3% |
| 7B | YaRN | 16 | 64k | 64k | YaRN | 64k | 96.3% |
| 7B | YaRN | 32 | 128k | 64k | YaRN | 128k | 99.4% |
| 13B | Code Llama | 88.6 | 100k | 16k | NTK | 128k | 99.4% |
| 13B | YaRN | 16 | 64k | 64k | YaRN | 64k | 97.5% |
| 13B | YaRN | 32 | 128k | 64k | YaRN | 128k | 99.4% |

- YaRN (s = 32) passes passkey retrieval with > 99% accuracy at 128k context for both 7B and 13B models.
- The s = 16 models have lower accuracy (96.3% for 7B, 97.5% for 13B) than s = 32 models despite similar perplexity, which the authors hypothesize indicates the s = 16 models are undertrained for the passkey task (Appendix B.2).

**Mistral 7B results (Table 6, Appendix B.4):**

| Model | Context Window | Method | 4096 | 8192 | 16384 | 65536 | 131072 |
|---|---|---|---|---|---|---|---|
| Mistral v0.1 | 8k | -- | **3.09** | **2.96** | 36.8 | >10^3 | >10^3 |
| MistralLite | 16k | NTK | 3.26 | 3.13 | 47.3 | >10^3 | >10^3 |
| YaRN (s = 8) | 64k | YaRN | 3.18 | 3.04 | **2.65** | **2.20** | 57.4 |
| YaRN (s = 16) | 128k | YaRN | 3.21 | 3.08 | 2.68 | 2.24 | **2.19** |

- Results are consistent with the Llama family: YaRN successfully extends Mistral to 128k context.
- MistralLite (NTK-aware with theta = 1M) fails completely beyond 16k, performing worse than the base model.
- Base Mistral v0.1 catastrophically fails beyond its 8k pretrained window.

### Dynamic Scaling Without Fine-Tuning

Dynamic-YaRN (combining YaRN with Dynamic Scaling) on the original Llama 2 7B (pretrained context L = 4096, no fine-tuning) prevents perplexity blow-up beyond the pretrained window and outperforms Dynamic-PI on a GovReport sample (Figure 5, Appendix B.3). This demonstrates that the NTK-by-parts + temperature approach provides benefits even without any fine-tuning.

---

## Limitations and Failure Modes

1. **Scale factor must match target context.** The s = 16 models (64k target) degrade catastrophically beyond 64k (perplexity > 10^1 at 98k and 128k, Table 2). The scale factor s must be set to at least L'/L for the desired context length. YaRN does not provide unbounded extrapolation.

2. **Short-context benchmark degradation.** While minimal, YaRN does degrade performance within the original context window. At 7B s = 16: ARC-c drops 0.8 points, MMLU drops 1.3 points vs Llama 2 baseline. At 13B s = 16: MMLU drops 3.0 points (55.8 to 52.8) (Table 3).

3. **Passkey retrieval below 100% for s = 16 models.** YaRN 7B s = 16 achieves only 96.3% passkey accuracy at 64k, and 13B s = 16 achieves 97.5%. The authors hypothesize these models are undertrained for the passkey task (Appendix B.2).

4. **Perplexity may not indicate downstream task performance.** The paper observes that Code Llama 13B maintains strong passkey retrieval at 128k despite increasing perplexity beyond 100k, suggesting perplexity alone "does not exhaustively determine long context performance" (Appendix B.2). The paper does not evaluate on downstream long-context tasks such as multi-hop QA or summarization.

5. **Empirically fitted parameters.** The temperature formula sqrt(1/t) = 0.1 * ln(s) + 1 and the alpha/beta values (1 and 32 for LLaMA) are empirically determined without theoretical justification (Section 3.4, Section 3.2). Applicability to architectures beyond LLaMA/Llama 2/Mistral is unknown.

6. **No evaluation on complex long-context tasks.** Evaluation is limited to perplexity, passkey retrieval, and short-context benchmarks. The paper does not test whether extended models can effectively reason over information distributed across the full extended context (e.g., multi-hop QA, long-form summarization, or tasks requiring information integration from distant positions).

7. **Limited to RoPE-based models.** The method is specific to models using RoPE positional encoding. The paper states applicability to "the LLaMA, the GPT-NeoX, and the PaLM families" (Section 1) but only evaluates on Llama 2 and Mistral.

---

## Conclusions

### Contributions

1. **Targeted, frequency-aware interpolation.** Introduced NTK-by-parts interpolation (Definition 2) that treats RoPE dimensions differently based on wavelength, preserving high-frequency local position information while fully interpolating low-frequency dimensions. This outperforms both PI's uniform scaling and NTK-aware's base change in both fine-tuned and non-fine-tuned scenarios (Tables 1-2).

2. **Attention entropy correction.** Identified that context extension uniformly increases attention entropy and proposed a temperature scaling fix (Equation 21) with an empirically fitted formula sqrt(1/t) = 0.1 * ln(s) + 1 (Equation 22) that generalizes across model sizes from 7B to 65B (Section 3.4, Appendix A.2).

3. **Extreme compute efficiency.** Achieved state-of-the-art context extension with 400 training steps and ~0.1% of original pretraining data -- a 10x token reduction from Code Llama and 2.5x step reduction from PI (Section 4).

4. **Extrapolation beyond fine-tuning context.** Demonstrated that YaRN (s = 32) models trained on 64k data successfully extrapolate to 128k context with declining perplexity throughout, unlike blind interpolation methods (Table 2, Section 4.2).

5. **Efficient transfer learning across scales.** Showed that extending from s = 16 to s = 32 requires only 200 additional steps with negligible benchmark degradation (0.49% average), because targeted interpolation preserves embedding structure across scales (Table 3, Section 4.3.3).

6. **Zero-overhead drop-in replacement.** YaRN requires no modifications to the attention mechanism code, is fully compatible with Flash Attention 2 and KV caching, and adds zero overhead -- only the RoPE frequency computation changes (Section 3.4).

7. **Formalization of community methods.** Provided formal definitions and unified treatment of NTK-aware (Definition 1), Dynamic NTK, and NTK-by-parts (Definition 2) interpolation methods that had previously existed only as informal community contributions (Sections 3.1-3.3).

### Implications

1. **Frequency-dependent treatment of positional encodings is essential.** The consistent superiority of targeted over blind interpolation suggests that RoPE dimensions carry fundamentally different types of positional information (local vs. global) that must be treated differently during context extension.

2. **Entropy correction may be a general requirement for context extension.** The temperature scaling formula's applicability across model sizes and families (LLaMA 7B-65B, Llama 2 7B-70B) suggests that increased attention entropy is a universal side effect of context extension, not model-specific (speculative, based on limited model families).

3. **Iterative context extension is viable.** The successful transfer from s = 16 to s = 32 with minimal additional training suggests that context windows could potentially be extended incrementally rather than requiring a single large extension step (speculative, only tested for one hop from 16 to 32).

---

## Key Claims

**C1. YaRN achieves state-of-the-art context extension with 10x fewer tokens than Code Llama and 2.5x fewer training steps than PI.** At s = 2, YaRN uses 400M tokens vs 1B for PI and NTK-aware, while matching or surpassing perplexity at all evaluation windows (Table 1). At s = 16/32, YaRN achieves the best Proof-pile perplexity at 128k (2.37 for 7B, 2.24 for 13B) vs Code Llama's 2.71/2.54 trained with 10x more data (Table 2). Status: **supported**.

**C2. NTK-by-parts interpolation preserves high-frequency RoPE dimensions while interpolating low-frequency dimensions, outperforming both PI and NTK-aware after fine-tuning.** The ramp function gamma classifies dimensions by wavelength ratio r = L/lambda: no interpolation for r > beta (high frequency), full interpolation for r < alpha (low frequency). With alpha = 1, beta = 32 for LLaMA, this avoids the out-of-bounds extrapolation of NTK-aware while preserving local positional resolution that PI destroys (Definition 2, Section 3.2). Status: **supported**.

**C3. Attention temperature scaling with sqrt(1/t) = 0.1*ln(s) + 1 uniformly improves perplexity across positions and samples.** Tested on 896 16k-token RedPajama documents at s = 8: the optimal sqrt(1/t) value is consistent across 8 position segments (0-2048, 2048-4096, ..., 14336-16384) and across different samples (Figures 2-4, Appendix A.2). The formula generalizes from LLaMA 7B-65B to Llama 2 7B-70B (Section 3.4). Status: **supported**.

**C4. YaRN (s = 32) models trained on 64k data extrapolate to 128k context with continued declining perplexity.** Both 7B and 13B s = 32 models show perplexity declining from 8192 through 131072 evaluation windows (7B: 3.56 to 2.37; 13B: 3.29 to 2.24), despite training data limited to 64k tokens (Table 2, Section 4.2). Status: **supported**.

**C5. Transfer learning from s = 16 to s = 32 requires only 200 additional steps with 0.49% average benchmark drop.** Benchmark scores for 7B: ARC-c 52.3 to 52.1, HellaSwag 78.8 to 78.4, MMLU 42.5 to 41.7, TruthfulQA 38.2 to 37.3. For 13B: ARC-c 58.1 to 58.0, HellaSwag 82.3 to 82.2, MMLU 52.8 to 51.9, TruthfulQA 37.8 to 37.3 (Table 3, Section 4.3.3). Status: **supported**.

**C6. YaRN 7B/13B (s = 32) achieve > 99% passkey retrieval accuracy at 128k context.** Both 7B and 13B models achieve 99.4% average accuracy across all context sizes up to 128k on the passkey retrieval task (Table 5, Section 4.3.2). Status: **supported**.

**C7. Dynamic-YaRN outperforms Dynamic-PI for context extension without fine-tuning.** On a GovReport sample evaluated with Llama 2 7B (pretrained at 4k context, no fine-tuning), Dynamic-YaRN maintains lower perplexity than Dynamic-PI across the extended range beyond 4k tokens, while both prevent the catastrophic blow-up seen with standard RoPE (Figure 5, Appendix B.3). Status: **supported**.

---

## Open Questions

1. **Why does perplexity improvement not always translate to downstream task performance?** The paper notes that Code Llama 13B maintains strong passkey retrieval at 128k despite increasing perplexity beyond 100k, and that perplexity "does not exhaustively determine long context performance" (Appendix B.2). YaRN itself is not evaluated on any complex downstream long-context tasks. Addressed by: `2025-12-drope-dropping-positional-embeddings` (DroPE shows that YaRN's zero-shot extension fails to improve downstream task performance despite good perplexity).

2. **Can the temperature formula be derived theoretically?** The formula sqrt(1/t) = 0.1 * ln(s) + 1 is empirically fitted by searching over sqrt(1/t) values for minimal perplexity (Appendix A.2). No theoretical explanation is provided for why this specific functional form (logarithmic in s) should be optimal, or why the coefficient 0.1 is appropriate. Unresolved.

3. **What are the optimal alpha and beta for non-LLaMA architectures?** The paper uses alpha = 1, beta = 32 for the LLaMA family and states these "should be tuned on a case-by-case basis" (Section 3.2). No principled method for selecting these values is provided. Unresolved.

4. **Does YaRN generalize to non-RoPE positional encodings?** The method is defined specifically in terms of RoPE's rotary frequency structure. Whether analogous targeted interpolation principles apply to learned position embeddings or other PE schemes is unknown. Unresolved.

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations

- **Su et al. (2022) [34]** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the positional encoding that YaRN modifies. The entire paper builds on RoPE's mathematical formulation -- frequency-based rotations on query/key pairs with theta_d = b^{-2d/|D|} and b = 10000 (Equations 1-9).
- **Vaswani et al. (2017) [40]** -- *Attention Is All You Need.* Foundational Transformer architecture with original sinusoidal positional encodings. YaRN applies to models descended from this architecture.

### Direct Predecessors (Methods That YaRN Builds On)

- **Chen et al. (2023) [9]** -- *Extending Context Window via Positional Interpolation.* The "blind" interpolation baseline that YaRN improves upon. PI uniformly scales all position indices by L/L'. YaRN follows PI's training and evaluation methodology but requires 2.5x fewer steps and 10x fewer tokens. PI's uniform scaling is the core limitation YaRN addresses.
- **bloc97 (2023) [6]** -- *NTK-Aware Scaled RoPE (Reddit post).* Proposes spreading interpolation pressure via a base change b' = b * s^(|D|/(|D|-2)). YaRN formalizes this as Definition 1 and identifies its limitation: some dimensions are extrapolated out-of-bounds, hurting fine-tuned performance. The first author of YaRN (Bowen Peng) is bloc97.
- **bloc97 (2023) [7]** -- *NTK-by-parts interpolation (GitHub PR).* Proposes the targeted, frequency-dependent interpolation with the ramp function gamma. This becomes the core interpolation component of YaRN (Definition 2).
- **emozilla (2023) [14]** -- *Dynamic NTK (Reddit post).* Proposes dynamically updating the scale factor s at inference time based on current sequence length. YaRN adopts this as "Dynamic Scaling." The second author of YaRN (Jeffrey Quesnelle) is emozilla.

### NTK Theory

- **Tancik et al. (2020) [36]** -- *Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains.* Provides the NTK-theory basis for why high-frequency information is lost under PI: low-dimensional position inputs expanded through Fourier-like features need to preserve high-frequency components. Motivates the "NTK-aware" naming and the high-frequency preservation approach (Section 3.1).

### Models Used in Evaluation

- **Touvron et al. (2023) [38]** -- *LLaMA: Open and Efficient Foundation Language Models.* Original LLaMA architecture using RoPE. The temperature formula is fitted on LLaMA 7B, 13B, 33B, and 65B.
- **Touvron et al. (2023) [39]** -- *Llama 2.* The 7B and 13B models that YaRN extends. Primary experimental subjects for all results in the main paper.
- **Roziere et al. (2023) [31]** -- *Code Llama.* Uses NTK-aware scaling with b = 1M for 100k context. Primary comparison target. YaRN achieves better perplexity with 10x less training data, and Code Llama shows severe benchmark degradation (e.g., 13B ARC-c drops from 59.4 to 40.9).
- **Jiang et al. (2023) [20]** -- *Mistral 7B.* Additional architecture demonstrating YaRN's generality beyond LLaMA (Appendix B.4).

### Concurrent/Related Context Extension Work

- **kaiokendev (2023) [21]** -- *SuperHOT.* Concurrent with PI; independently discovered position interpolation for extending context from 2K to 8K.
- **Su (2023) [33]** -- *ReRoPE (Rectified Rotary Position Embeddings).* Alternative context extension modifying the attention mechanism rather than embeddings. Not compatible with Flash Attention 2 and requires two attention passes, so not directly compared (Section 2.4).
- **Han et al. (2023) [16]** -- *LM-Infinite.* Concurrent work proposing similar ideas for on-the-fly length generalization. Also modifies the attention mechanism, making it incompatible with Flash Attention 2 (Section 2.4).
- **Kazemnejad et al. (2023) [22]** -- *The Impact of Positional Encoding on Length Generalization.* Shows no existing PE method generalizes to significantly longer sequences, motivating the need for interpolation approaches (Section 1).

### Alternative Positional Encodings

- **Press et al. (2022) [27]** -- *ALiBi: Train Short, Test Long.* Linear attention bias for length extrapolation. Referenced for context and provides the sliding window perplexity evaluation methodology (S = 256) used throughout.
- **Shaw et al. (2018) [32]** -- *Self-Attention with Relative Position Representations.* Early relative PE scheme referenced for historical context.
- **Roberts et al. (2019) [30]** -- *T5 Relative Bias.* T5's relative position bias, listed among popular alternatives.
- **Sun et al. (2022) [35]** -- *XPos: A Length-Extrapolatable Transformer.* Another relative PE scheme listed as a popular alternative.

### Community Models (Baselines)

- **Together.ai (2023) [37]** -- *LLaMA-2-7B-32K.* PI-based 32k context model; baseline in perplexity and benchmark comparisons. Degrades catastrophically beyond 32k (Table 2).
- **Quesnelle et al. (2023) [28]** -- *LLongMA-2.* PI-based 8k context model using RedPajama data; baseline in Table 1 comparison.
- **MistralLite [1]** -- NTK-aware (theta = 1M) version of Mistral v0.1; comparison target in Appendix B.4. Fails completely beyond 16k.

### Evaluation Benchmarks

- **Azerbayev et al. (2022) [4]** -- *Proof-pile.* Primary long-sequence perplexity evaluation dataset (128k token samples). Used for Tables 1-2 and Figure 1.
- **Huang et al. (2021) [18]** -- *GovReport.* Long document dataset for secondary perplexity evaluation (Table 4) and Dynamic Scaling comparison (Figure 5).
- **Rae et al. (2020) [29]** -- *PG19.* Book corpus used as training data (64k chunks). Not used for evaluation in YaRN (unlike in PI).
- **Mohtashami & Jaggi (2023) [25]** -- *Landmark Attention.* Provides the passkey retrieval evaluation task (Table 5, Section 4.3.2).
- **Clark et al. (2018) [11]** -- *ARC.* Reasoning benchmark from the Open LLM Leaderboard.
- **Zellers et al. (2019) [41]** -- *HellaSwag.* Sentence completion benchmark from the evaluation suite.
- **Hendrycks et al. (2021) [17]** -- *MMLU.* Multitask language understanding benchmark.
- **Lin et al. (2022) [23]** -- *TruthfulQA.* Truthfulness benchmark.

### Training Infrastructure

- **Dao (2023) [13]** -- *Flash Attention 2.* Efficient attention implementation. YaRN's compatibility with Flash Attention 2 is a key practical advantage over ReRoPE and LM-Infinite, both of which modify the attention mechanism (Section 2.4).
- **Zhao et al. (2023) [42]** -- *PyTorch FSDP.* Distributed training framework used for all experiments.
- **Loshchilov & Hutter (2019) [24]** -- *AdamW.* Optimizer used for fine-tuning.
