# NTK-Aware Scaled RoPE

**Author:** bloc97 (Bowen Peng, later affiliated with Nous Research)
**Date:** June 2023
**Type:** Reddit post on r/LocalLLaMA (not a formal peer-reviewed paper)
**URL:** https://www.reddit.com/r/LocalLLaMA/comments/14lz7j5/ntkaware_scaled_rope_allows_llama_models_to_have/

This is a community contribution. The method was later formalized in the YaRN paper (Peng et al., 2023, arXiv:2309.00071) where bloc97 is the first author. Two follow-up contributions by the same author -- "NTK-by-parts" interpolation and its integration into YaRN -- were also initially released as community posts.

---

## Core Research Problem

Position Interpolation (PI, Chen et al. 2023) extends the context window of RoPE-based LLMs by uniformly downscaling all position indices by a factor s = L'/L. While this avoids the catastrophic extrapolation of raw RoPE, it treats all frequency dimensions identically -- a "blind" approach. The key insight of NTK-aware scaling is that **uniform interpolation destroys high-frequency positional information** that the network needs to distinguish close-by tokens. Drawing on Neural Tangent Kernel (NTK) theory (Tancik et al., 2020), which shows that neural networks struggle to learn high-frequency functions when input embeddings lack high-frequency components, bloc97 identified that compressing RoPE's high-frequency dimensions reduces the model's ability to resolve fine-grained local positional differences.

---

## Problem Solutions

Instead of scaling every RoPE dimension by the same factor s, NTK-aware scaling **spreads the interpolation pressure across dimensions**: high frequencies are scaled less (preserving local resolution) and low frequencies are scaled more (accommodating the extended context). The solution is built on:

1. **NTK theory insight:** Neural networks cannot learn high-frequency functions when input embeddings lack high-frequency components (Tancik et al., 2020). RoPE acts as a Fourier Feature mapping, so compressing its high-frequency dimensions directly harms local positional resolution.
2. **Non-uniform frequency scaling via base change:** Rather than rescaling position indices (as PI does), the method changes the RoPE base parameter from b to b', which non-uniformly shifts all frequencies — preserving the highest frequencies almost entirely while compressing the lowest frequencies by approximately factor s.
3. **Zero fine-tuning required:** The base change is a 3-line code modification with no architectural changes, no new parameters, and no additional training.

---

## Approach Details

### Method

RoPE defines frequencies theta_d = b^(-2d/|D|) where b = 10000 is the base, d indexes the hidden dimension, and |D| is the head dimension. NTK-aware scaling replaces b with a new base b':

> **b' = b * s^(|D| / (|D| - 2))**

where s = L'/L is the context extension factor.

In the general RoPE modification framework f'(x_m, m, theta_d) = f(x_m, g(m), h(theta_d)):
- g(m) = m (position indices are NOT rescaled, unlike PI)
- h(theta_d) = b'^(-2d/|D|) (frequencies are changed via the new base)

This means position indices remain at their original integer values, and the frequency spectrum is non-uniformly compressed. The lowest-frequency dimension (d = |D|/2 - 1) is scaled by approximately factor s (matching PI's behavior), while the highest-frequency dimension (d = 0) remains nearly unchanged, preserving the model's ability to distinguish adjacent tokens.

### Mathematical Derivation (from YaRN, Appendix A.1)

The base change is derived by requiring that the lowest frequency dimension matches PI's linear interpolation scale:

> b'^((|D|-2)/|D|) = s * b^((|D|-2)/|D|)

Solving for b' gives:

> b' = b * s^(|D| / (|D| - 2))

For LLaMA 7B with |D| = 128 (head dimension = 4096/32): b' = 10000 * s^(128/126) ≈ 10000 * s^1.016.

### Intuition from NTK Theory

RoPE closely resembles Fourier Features (Tancik et al., 2020). A token's position is one-dimensional, and RoPE expands it into a |D|/2-dimensional complex vector. NTK theory shows that when input embeddings lack high-frequency components, networks cannot learn high-frequency functions of the input. By preserving the high-frequency RoPE dimensions, NTK-aware scaling maintains the network's ability to encode fine-grained positional relationships without retraining.

### Comparison with Position Interpolation

| Property | PI | NTK-Aware |
|---|---|---|
| Position index scaling | m -> m/s | m -> m (unchanged) |
| Frequency scaling | All dimensions scaled equally | Non-uniform: high freq preserved, low freq compressed |
| High-frequency info | Lost (compressed by factor s) | Preserved |
| Out-of-bounds values | None (pure interpolation) | Some dimensions slightly extrapolated |
| Without fine-tuning | Poor (high perplexity) | Good (low perplexity, no fine-tuning needed) |
| After fine-tuning | Good | Slightly worse than PI (due to out-of-bounds dims) |
| Code changes | 1 line | 3 lines |

### Limitations

1. **Out-of-bounds extrapolation:** Because position indices are not rescaled, some dimensions see positional values beyond the pretrained range. This means NTK-aware is not a pure interpolation method, and after fine-tuning, PI can outperform it.
2. **Scale factor mismatch:** The theoretical scale factor s does not accurately describe the true context extension. In practice, s must be set higher than the target extension ratio.
3. **No frequency-dependent treatment:** NTK-aware applies a single base change globally. It does not distinguish between dimensions that should be fully interpolated (low frequency), not interpolated at all (high frequency), or partially interpolated (intermediate). This limitation was addressed by the subsequent "NTK-by-parts" method.

### Follow-Up Contributions by bloc97

**NTK-by-parts interpolation** (GitHub PR, July 2023): Splits RoPE dimensions into three regimes based on the ratio r = L/lambda_d:
- r > beta: do not interpolate (high frequency, preserve local distances)
- r < alpha: fully interpolate by s (low frequency, avoid extrapolation)
- alpha <= r <= beta: smooth ramp between the two

For LLaMA: alpha = 1, beta = 32. This method outperforms both PI and NTK-aware in both fine-tuned and non-fine-tuned settings.

**Dynamic NTK** (by emozilla/Jeffrey Quesnelle, Reddit, June 2023): Uses a dynamic scale factor s = max(1, l'/L) that updates each forward pass based on current sequence length l'. Prevents performance degradation below L and allows graceful degradation beyond L'. Works exceptionally well without fine-tuning.

Both methods were later unified with attention temperature scaling into **YaRN** (Peng et al., 2023).

### Impact and Adoption

Despite being a Reddit post, NTK-aware scaling had immediate and significant impact on the LLM ecosystem:

1. **Code Llama (Meta, August 2023):** Adopted NTK-aware scaling by setting b = 1,000,000 (equivalent to a specific base change for their target context length) to achieve 100k context windows.
2. **Qwen 7B (Alibaba, 2023):** Adopted Dynamic NTK interpolation for context extension.
3. **Hugging Face transformers v4.31.0:** Incorporated RoPE scaling support, enabling NTK-aware and related methods in the standard library.
4. **YaRN (Peng et al., 2023):** Formalized NTK-aware as Definition 1 and built the full YaRN method on top of NTK-by-parts.
5. **DroPE (Gelberg et al., 2025):** Uses NTK-aware as a baseline method throughout, including in the formal definition of scaling factors (Eq. 3) and all experimental comparisons.

---

## Conclusions

1. **High-frequency preservation is critical:** Uniform position interpolation (PI) degrades short-context performance because it compresses high-frequency positional information. A frequency-aware approach that preserves high frequencies while compressing low frequencies avoids this problem.

2. **Simple base change is effective:** The entire method reduces to changing the RoPE base from b to b * s^(|D|/(|D|-2)) -- a 3-line code change with no new parameters, no architectural modifications, and no fine-tuning required.

3. **Zero-shot context extension:** Unlike PI, which requires fine-tuning to be useful, NTK-aware scaling provides meaningful context extension without any additional training, though fine-tuning further improves results.

4. **Foundation for subsequent methods:** NTK-aware scaling established the key insight (frequency-dependent treatment of RoPE dimensions) that underpins all subsequent improvements: NTK-by-parts, Dynamic NTK, and YaRN.

5. **Community-driven research impact:** A Reddit post with a 3-line code change influenced Meta's Code Llama, Alibaba's Qwen, and the broader RoPE context extension research direction, demonstrating the role of open-source community contributions in advancing LLM capabilities.

---

## Core References and Why They Are Referenced

### Foundational
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* The positional encoding that NTK-aware modifies. Provides the frequency-based rotation formulation theta_d = b^(-2d/|D|) that the base change operates on.
- **Tancik et al. (2020)** -- *Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains.* NTK theory paper providing the theoretical motivation: neural networks struggle with high-frequency functions when input embeddings lack high-frequency components. The "NTK" in "NTK-aware" refers to this theory.

### Predecessor
- **Chen et al. (2023)** -- *Position Interpolation (PI).* The uniform interpolation method that NTK-aware improves upon. PI's blind downscaling of all position indices by 1/s loses high-frequency information; NTK-aware's non-uniform base change preserves it.
- **kaiokendev (2023)** -- *SuperHOT.* Concurrent work that independently discovered position interpolation for context extension (2K to 8K). Referenced as concurrent in PI; part of the same wave of community-driven context extension research.

### Successor Methods (Building on NTK-Aware)
- **bloc97 (2023)** -- *NTK-by-parts interpolation (GitHub PR).* Follow-up by the same author introducing frequency-dependent ramp function for targeted interpolation. Addresses NTK-aware's out-of-bounds problem.
- **emozilla (2023)** -- *Dynamic NTK (Reddit post).* Dynamic scale factor adaptation at inference time. Combined with NTK-aware, enables >2x context extension without fine-tuning.
- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension.* Unifies NTK-by-parts + attention temperature scaling. Formalizes NTK-aware as Definition 1 with full mathematical derivation. First author is bloc97.

### Models That Adopted NTK-Aware
- **Roziere et al. (2023)** -- *Code Llama.* Meta's code model uses NTK-aware scaling with b=1,000,000 to achieve 100k context windows. First major industry adoption.
- **Qwen (2023)** -- *Qwen 7B.* Alibaba's model uses Dynamic NTK interpolation for context extension.

### Subsequent Work Using NTK-Aware as Baseline
- **Gelberg et al. (2025)** -- *DroPE: Dropping Positional Embeddings.* Uses NTK-aware as one of three primary baselines (with PI and YaRN) throughout all experiments. DroPE outperforms NTK-aware on all zero-shot context extension tasks.
- **Ding et al. (2024)** -- *LongRoPE.* Advanced RoPE extension method that also builds on the frequency-aware insights from NTK-aware.

#### Cross-References in Available Papers

**How NTK-Aware Is Referenced in DroPE (Gelberg et al., 2025):**
- Listed as "bloc97, 2023" throughout as one of the three primary RoPE-scaling baselines (alongside PI and YaRN)
- Included in the formal definition of scaling factors (Eq. 3) describing how different methods modify RoPE frequencies
- Evaluated as a baseline in all experiments: Tables 1-3, Table 10
- DroPE outperforms NTK-aware on zero-shot NIAH tasks (28.0/41.6/23.3 vs 21.1/19.4/16.5 at 2x context) and LongBench (Llama2-7B: 26.08 vs 21.88 avg)

**How NTK-Aware Is Referenced in YaRN (Peng et al., 2023):**
- Referenced as [6] (bloc97's Reddit post) extensively throughout
- Section 1 (Introduction): "[6] proposed the 'NTK-aware' interpolation by taking the loss of high frequency into account"
- Section 3.1: Entire subsection "Loss of High Frequency information" dedicated to formalizing NTK-aware as Definition 1 with the mathematical derivation
- Notes Code Llama uses NTK-aware scaling (b=1M)
- NTK-by-parts referenced as [7] (bloc97's GitHub PR); Dynamic NTK referenced as [14] (emozilla's Reddit post)
- YaRN is essentially NTK-by-parts + attention temperature scaling, building directly on bloc97's contributions
- The first author of YaRN (Bowen Peng) IS bloc97

**How NTK-Aware Is Referenced in PI (Chen et al., 2023):**
- PI does **not** reference NTK-aware scaling directly. The PI paper (June 2023) was concurrent with/slightly preceded the NTK-aware Reddit post (June 2023)
- PI mentions concurrent work by kaiokendev (SuperHOT) which also interpolates RoPE, but this is a different method from NTK-aware
- PI's theoretical interpolation bound analysis implicitly motivates why NTK-aware was needed: the bound shows interpolation is stable but does not address the frequency-dependent information loss that NTK-aware solves
