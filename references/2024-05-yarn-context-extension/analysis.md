# YaRN: Efficient Context Window Extension of Large Language Models

**Authors:** Bowen Peng (bloc97), Jeffrey Quesnelle (emozilla), Honglu Fan, Enrico Shippole (Nous Research, EleutherAI, University of Geneva)
**Date:** November 2023 (arXiv:2309.00071v2); published at ICLR 2024

---

## Core Research Problem

Transformer-based LLMs using Rotary Position Embeddings (RoPE) cannot generalize beyond their pretrained context window. Position Interpolation (PI) addresses this by uniformly downscaling position indices, but treats all RoPE frequency dimensions identically -- a "blind" approach that loses high-frequency information needed for resolving close-by tokens and degrades short-context performance. The NTK-aware interpolation (bloc97) improves non-fine-tuned performance by spreading interpolation pressure across frequencies via a base change, but some dimensions are slightly extrapolated out-of-bounds, making it inferior to PI after fine-tuning. Neither method provides a principled, frequency-aware interpolation that simultaneously preserves high-frequency local information, avoids out-of-bounds extrapolation, corrects attention entropy, and enables efficient transfer learning across scale factors. The core challenge is: **how to extend context windows of RoPE-based LLMs with maximal compute efficiency while surpassing all existing methods in both fine-tuned and non-fine-tuned settings.**

---

## Problem Solutions

YaRN combines three independently motivated fixes to PI's shortcomings into a single method:

1. **NTK-by-parts interpolation (targeted, frequency-dependent scaling):** Instead of scaling all RoPE dimensions uniformly, classify dimensions by the ratio r = L/lambda between the original context length L and the dimension's wavelength lambda. High-frequency dimensions (short wavelength, r > beta) are not interpolated at all, preserving local positional resolution. Low-frequency dimensions (long wavelength, r < alpha) are fully interpolated by scale s, avoiding extrapolation. Intermediate dimensions use a smooth ramp between the two regimes.

2. **Attention temperature scaling:** Context extension increases attention entropy uniformly across positions and samples. Introducing a temperature t in the softmax (dividing logits by t*sqrt(|D|)) compensates for this. The optimal temperature follows sqrt(1/t) = 0.1*ln(s) + 1, fitted across LLaMA 7B-65B and found to generalize to Llama 2 models.

3. **Dynamic Scaling (inference-time):** Instead of fixing the scale factor s = L'/L throughout inference, dynamically set s = max(1, l'/L) where l' is the current sequence length. This prevents performance degradation below L and allows graceful degradation beyond L', rather than an abrupt cliff.

---

## Approach Details

### Method
YaRN modifies RoPE via the general form f'(x_m, m, theta_d) = f(x_m, g(m), h(theta_d)), combining:

- **NTK-by-parts interpolation (Definition 2):**
  - g(m) = m (no position index scaling)
  - h(theta_d) = (1 - gamma(r(d))) * theta_d/s + gamma(r(d)) * theta_d
  - Where r(d) = L / lambda_d = L / (2*pi*b^(2d/|D|)) is the ratio of context length to wavelength
  - gamma(r) is a ramp function: 0 if r < alpha, 1 if r > beta, linear interpolation otherwise
  - For LLaMA: alpha = 1, beta = 32

- **Attention temperature (Eq. 21):**
  - softmax(q^T_m * k_n / (t * sqrt(|D|)))
  - sqrt(1/t) = 0.1 * ln(s) + 1
  - Implemented as a "length scaling" trick: scale the complex RoPE embeddings by sqrt(1/t), requiring zero code changes to the attention mechanism and zero overhead at inference.

### Relationship to Prior Methods
| Method | g(m) | h(theta_d) | Interpolation type |
|---|---|---|---|
| PI | m/s | theta_d | Blind (uniform) |
| NTK-aware | m | b'^(-2d/\|D\|), b' = b * s^(\|D\|/(\|D\|-2)) | Blind (base change) |
| NTK-by-parts | m | ramp-based mix of theta_d/s and theta_d | Targeted (frequency-dependent) |
| YaRN | m | NTK-by-parts + temperature scaling | Targeted + entropy correction |

### Key Technical Components

- **NTK-aware interpolation (Definition 1, formalized from bloc97's Reddit post):** Change the RoPE base from b to b' = b * s^(|D|/(|D|-2)). This spreads interpolation pressure: high frequencies scale less, low frequencies scale more. Performs better than PI without fine-tuning, but worse after fine-tuning due to out-of-bounds extrapolation in some dimensions. Code Llama uses this with b=1M.

- **Dynamic NTK (from emozilla's Reddit post):** Apply NTK-aware scaling with a dynamic scale factor s = max(1, l'/L) that updates each forward pass based on current sequence length. Works exceptionally well without any fine-tuning. Adopted by Qwen 7B.

- **Wavelength analysis:** RoPE dimensions where wavelength lambda > L (low frequency) have not completed a full rotation during pretraining and encode absolute positional information. Dimensions where lambda << L (high frequency) encode relative local distances. Blind interpolation compresses all dimensions, confusing the model on local token ordering.

### Experimental Setup
- **Models:** Llama 2 7B and 13B, extended with s=16 (64k context) and s=32 (128k context). Additionally Mistral 7B v0.1.
- **Training:** 400 steps for s=16 on PG19 (64k chunks), +200 steps for s=32 starting from s=16 checkpoint. Learning rate 2e-5, AdamW, batch size 64, Flash Attention 2, FSDP. ~0.1% of original pretraining data.
- **Transfer learning:** s=32 model trained on only 64k context data successfully extrapolates to 128k -- demonstrating "train short, test long" with YaRN.
- **Evaluation:** Sliding window perplexity (S=256) on Proof-pile and GovReport, passkey retrieval (8k-128k), Hugging Face Open LLM Leaderboard (ARC-C, HellaSwag, MMLU, TruthfulQA).

### Key Results
| Setting | YaRN | Best alternative |
|---|---|---|
| Proof-pile PPL at 2048 eval (7B, s=2, 8k window) | **3.91** (400M tokens) | 3.92 (PI, 1B tokens) / 4.20 (NTK, 1B tokens) |
| Proof-pile PPL at 128k (7B, s=32) | **2.37** | 2.71 (Code Llama 7B, NTK) |
| Proof-pile PPL at 128k (13B, s=32) | **2.24** | 2.54 (Code Llama 13B, NTK) |
| GovReport PPL at 32k (7B, s=16) | **3.59** | 3.67 (Together PI) / 4.44 (Code Llama NTK) |
| Passkey retrieval at 128k (7B, s=32) | 99.4% | 94.3% (Code Llama 7B at 112k) |
| ARC-C / HellaSwag (7B, s=16) | 52.3 / **78.8** | 53.1 / 77.8 (Llama 2 base) / 47.6 / 76.1 (Together PI) |
| ARC-C / HellaSwag (13B, s=16) | 58.1 / **82.3** | 59.4 / 82.1 (Llama 2 base) / 40.9 / 63.4 (Code Llama NTK) |
| Training efficiency | 400 steps, ~0.1% data | 1000 steps (PI) / 4000 steps (Code Llama) |

- YaRN is the first method to extend Llama 2 to 128k context with declining perplexity throughout.
- s=32 model extrapolates to 128k despite training data being only 64k tokens -- successful "train short, test long."
- Transfer learning from s=16 to s=32 requires only 200 additional steps with negligible benchmark degradation (0.49% average).
- Minimal degradation on standard benchmarks vs Llama 2 baselines; Code Llama NTK shows severe degradation (e.g., ARC-C drops from 59.4 to 40.9 at 13B).
- Mistral 7B results are consistent: YaRN (s=16) achieves 2.19 PPL at 128k vs >10^3 for base and MistralLite.

---

## Conclusions

1. **Targeted interpolation outperforms blind interpolation:** Frequency-aware scaling that preserves high-frequency dimensions and only interpolates low-frequency dimensions yields better results than uniformly scaling all RoPE dimensions (PI) or uniformly changing the base (NTK-aware).

2. **Attention entropy correction is essential:** Context extension uniformly increases attention entropy. A simple temperature scaling with sqrt(1/t) = 0.1*ln(s) + 1 provides consistent perplexity improvements across all positions, samples, and model sizes, suggesting a degree of universality.

3. **Extreme compute efficiency:** YaRN achieves state-of-the-art context extension with 10x fewer tokens and 2.5x fewer training steps than PI/Code Llama, using only ~0.1% of original pretraining data.

4. **Extrapolation beyond fine-tuning context:** YaRN models trained on 64k data successfully extrapolate to 128k context, demonstrating effective "train short, test long" behavior that blind interpolation methods cannot achieve.

5. **Efficient transfer learning:** Extending from one scale factor to another (e.g., s=16 to s=32) requires minimal additional training because the targeted interpolation preserves the embedding structure across scales.

6. **Drop-in replacement:** YaRN requires no modifications to the attention mechanism code, is fully compatible with Flash Attention 2 and KV caching, and adds zero inference overhead -- only the RoPE frequency computation changes.

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations
- **Su et al. (2022) [34]** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the positional encoding that YaRN extends. The entire paper builds on RoPE's mathematical formulation (frequency-based rotations on query/key pairs).
- **Vaswani et al. (2017) [40]** -- *Attention Is All You Need.* Foundational transformer architecture with original sinusoidal positional encodings.

### Direct Predecessors (Methods That YaRN Builds On)
- **Chen et al. (2023) [9]** -- *Position Interpolation (PI).* The baseline "blind" interpolation method that YaRN improves upon. YaRN follows PI's training/evaluation methodology but requires 2.5x fewer steps. PI's uniform scaling of all RoPE dimensions is the core limitation YaRN addresses.
- **bloc97 (2023) [6]** -- *NTK-Aware Scaled RoPE (Reddit post).* Proposes spreading interpolation pressure via a base change b' = b * s^(|D|/(|D|-2)). YaRN formalizes this as Definition 1 and identifies its limitation: some dimensions are extrapolated out-of-bounds, hurting fine-tuned performance. The first author of YaRN (Bowen Peng) is bloc97.
- **bloc97 (2023) [7]** -- *NTK-by-parts interpolation (GitHub PR).* Proposes the targeted, frequency-dependent interpolation with the ramp function gamma. This becomes the core interpolation component of YaRN (Definition 2).
- **emozilla (2023) [14]** -- *Dynamic NTK (Reddit post).* Proposes dynamically updating the scale factor s at inference time based on current sequence length. YaRN adopts this as "Dynamic Scaling" for non-fine-tuned use. The second author of YaRN (Jeffrey Quesnelle) is emozilla.

### NTK Theory
- **Tancik et al. (2020) [36]** -- *Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains.* Provides the NTK-theory basis for why high-frequency information is lost under PI: low-dimensional position inputs expanded through Fourier-like features need to preserve high-frequency components. Motivates the "NTK-aware" naming and approach.

### Models Used in Evaluation
- **Touvron et al. (2023) [38]** -- *LLaMA.* Original LLaMA architecture that uses RoPE; provides the model family YaRN targets.
- **Touvron et al. (2023) [39]** -- *Llama 2.* The 7B and 13B models that YaRN extends. Primary experimental subjects.
- **Roziere et al. (2023) [31]** -- *Code Llama.* Uses NTK-aware scaling (b=1M) for 100k context. Primary comparison target; YaRN achieves better perplexity with 10x less training data.
- **Jiang et al. (2023) [20]** -- *Mistral 7B.* Additional architecture used to demonstrate YaRN's generality beyond LLaMA.

### Alternative Positional Encodings (Context)
- **Press et al. (2022) [27]** -- *ALiBi: Train Short, Test Long.* Alternative linear attention bias for length extrapolation. Referenced for context on the limitations of existing length extrapolation methods; also provides the sliding window perplexity evaluation methodology used throughout.
- **Shaw et al. (2018) [32]** -- *Self-Attention with Relative Position Representations.* Early relative position encoding scheme referenced for historical context on the evolution toward RoPE.
- **Sun et al. (2022) [35]** -- *XPos: A Length-Extrapolatable Transformer.* Another relative PE scheme listed among popular alternatives to RoPE.
- **Roberts et al. (2019) [30]** -- *T5 Relative Bias.* T5's relative position bias, listed as one of the popular relative PE schemes.

### Concurrent/Related Context Extension Work
- **kaiokendev (2023) [21]** -- *SuperHOT.* Concurrent with PI; independently discovered position interpolation for extending context from 2K to 8K.
- **Su (2023) [33]** -- *ReRoPE (Rectified RoPE).* Alternative context extension that modifies the attention mechanism rather than embeddings. Not compatible with Flash Attention 2, so not directly compared.
- **Han et al. (2023) [16]** -- *LM-Infinite.* Concurrent work proposing similar ideas to YaRN for on-the-fly length generalization. Also modifies attention mechanism, not directly comparable.
- **Kazemnejad et al. (2023) [22]** -- *Impact of Positional Encoding on Length Generalization.* Shows no existing PE method generalizes to significantly longer sequences; motivates the need for interpolation approaches.

### Community Models (Baselines)
- **Together.ai (2023) [37]** -- *LLaMA-2-7B-32K.* PI-based 32k context model; baseline in perplexity comparisons. Degrades catastrophically beyond 32k.
- **Quesnelle et al. (2023) [28]** -- *LLongMA-2.* PI-based 8k context model using RedPajama data; baseline in Table 1 comparisons.

### Evaluation Benchmarks
- **Rae et al. (2020) [29]** -- *PG-19.* Book corpus used as training data (64k chunks) and for long-sequence perplexity evaluation.
- **Azerbayev et al. (2022) [4]** -- *Proof-pile.* Primary long-sequence perplexity evaluation dataset (128k token samples).
- **Huang et al. (2021) [18]** -- *GovReport.* Long document dataset for secondary perplexity evaluation.
- **Mohtashami & Jaggi (2023) [25]** -- *Landmark Attention.* Provides the passkey retrieval evaluation task.
- **Clark et al. (2018) [11]** -- *ARC.* Reasoning benchmark from the Open LLM Leaderboard evaluation suite.
- **Zellers et al. (2019) [41]** -- *HellaSwag.* Sentence completion benchmark from the evaluation suite.
- **Hendrycks et al. (2021) [17]** -- *MMLU.* Multitask language understanding benchmark from the evaluation suite.
- **Lin et al. (2022) [23]** -- *TruthfulQA.* Truthfulness benchmark from the evaluation suite.

### Training Infrastructure
- **Dao (2023) [13]** -- *Flash Attention 2.* Efficient attention implementation used for training; YaRN's compatibility with Flash Attention 2 is a key practical advantage over ReRoPE and LM-Infinite.
- **Zhao et al. (2023) [42]** -- *PyTorch FSDP.* Distributed training framework used for all YaRN experiments.
- **Loshchilov & Hutter (2019) [24]** -- *AdamW.* Optimizer used for fine-tuning.

#### Cross-References in Available Papers

**How YaRN references papers in this directory:**
- **PI (2023-06-pi-positional-interpolation):** Referenced as [9], the baseline "blind" interpolation method. Used as primary comparison target throughout (Tables 1--3, perplexity and benchmark comparisons). YaRN follows PI's training/evaluation methodology but achieves comparable results with 2.5x fewer training steps and ~0.1% of pretraining data.
- **NTK-aware (2023-06-rope-ntk):** bloc97's Reddit post [6] is formalized as Definition 1 (NTK-aware interpolation). bloc97's GitHub PR [7] is formalized as Definition 2 (NTK-by-parts interpolation). emozilla's Reddit post [14] provides the Dynamic Scaling component (Section 3.3). The first author of YaRN (Bowen Peng) is bloc97; the second author (Jeffrey Quesnelle) is emozilla.

**How papers in this directory reference YaRN:**
- **PI (2023-06-pi-positional-interpolation):** Cross-references section notes YaRN as a successor that achieves comparable or better results with 2.5x fewer training steps by replacing PI's uniform frequency scaling with frequency-aware NTK-by-parts interpolation.
- **NTK-aware (2023-06-rope-ntk):** Extensively documents how NTK-aware, NTK-by-parts, and Dynamic NTK were unified into YaRN. Notes Peng et al. (2023) formalized NTK-aware as Definition 1 with full mathematical derivation. Lists YaRN under "Impact and Adoption."
- **RULER (2024-10-ruler-context-size):** Includes YaRN-Llama-2-7b-128k as a base model in evaluation (Table 4, Appendix A). YaRN is referenced as a context extension method enabling the long-context models benchmarked.
- **DroPE (2025-12-drope-dropping-positional-embeddings):** Uses YaRN as primary comparison target. DroPE outperforms YaRN on all zero-shot context extension tasks on RULER and LongBench benchmarks (e.g., SmolLM LongBench Avg. 30.52 vs 19.94 for YaRN). Notes that YaRN's zero-shot behavior is "equivalent to simply cropping context."
