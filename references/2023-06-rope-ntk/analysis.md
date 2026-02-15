---
title: "NTK-Aware Scaled RoPE"
authors: "bloc97"
year: 2023
venue: "Reddit post / community contribution"
paper_type: "informal"
categories: ["context-extension", "position-encoding"]
scope: ["RoPE-based LLMs", "context window extension without fine-tuning"]
benchmarks_used: []
models_introduced: []
models_evaluated: ["llama-7b"]
key_claims:
  - id: C1
    claim: "Scaling the RoPE base frequency preserves high-frequency components that uniform position interpolation (PI) destroys"
    evidence: "Frequency analysis in the post; formalized in YaRN Definition 1 and Appendix A.1"
    status: supported
    scope: "RoPE-based models, base change b' = b * s^(|D|/(|D|-2))"
    magnitude: "qualitative — highest-frequency dimension (d=0) remains nearly unchanged while lowest is compressed by ~s"
  - id: C2
    claim: "NTK-aware interpolation extends context to 8k+ tokens zero-shot without fine-tuning and with minimal perplexity degradation"
    evidence: "Perplexity comparison graph in the post (alpha=8 on LLaMA 7B)"
    status: supported
    scope: "LLaMA 7B, alpha=8, zero-shot (no fine-tuning)"
    magnitude: "8x context extension (2048 to 16384+) with perplexity close to pretrained baseline within original range"
  - id: C3
    claim: "Without fine-tuning, NTK-aware scaling achieves lower perplexity than PI at extended context lengths"
    evidence: "Perplexity comparison graph in the post; confirmed by YaRN Table 1"
    status: supported
    scope: "LLaMA 7B, zero-shot evaluation on extended context (2048-8192 tokens)"
    magnitude: "substantially lower perplexity than PI across extended range (single model, limited evidence)"
  - id: C4
    claim: "After fine-tuning on longer context data, PI outperforms NTK-aware scaling because NTK-aware has some dimensions in the extrapolation regime"
    evidence: "Noted in the post and follow-up discussions; confirmed by YaRN Table 2"
    status: supported
    scope: "RoPE-based models fine-tuned on extended context data"
    magnitude: "PI achieves lower perplexity than NTK-aware after fine-tuning (confirmed by YaRN Table 2)"
cross_references:
  - target: 2024-01-roformer-rope
    type: extends
    detail: "Modifies the base frequency in the RoPE formulation from Su et al."
  - target: 2023-06-pi-positional-interpolation
    type: concurrent
    detail: "Addresses the same context extension problem; NTK-aware preserves high frequencies that PI destroys through uniform scaling"
  - target: 2023-02-llama-open-efficient-foundation
    type: extends
    detail: "NTK-aware scaling is designed specifically for LLaMA's RoPE-based positional encoding"
  - target: 2024-05-yarn-context-extension
    type: extended-by
    detail: "YaRN formalizes NTK-aware as Definition 1 and builds NTK-by-parts + attention temperature scaling on top"
  - target: 2025-12-drope-dropping-positional-embeddings
    type: complementary
    detail: "DroPE includes NTK-aware as one of three primary baselines and outperforms it on NIAH and LongBench"
  - target: 2022-04-alibi-train-short-test-long
    type: complementary
    detail: "ALiBi uses linear attention biases for length extrapolation; NTK-aware addresses the same problem by modifying RoPE frequencies"
  - target: 2024-05-pose-positional-skip-wise-training
    type: extended-by
    detail: "PoSE uses NTK interpolation as a compatible positional strategy and evaluates its long-range turning-point behavior under fixed short-window training"
  - target: 2024-03-mistral-7b-v0.2
    type: extended-by
    detail: "Mistral 7B v0.2 applies the NTK-aware principle by increasing RoPE theta from 10K to 1M to extend context from 8K to 32K tokens"
open_questions:
  - question: "Is there an optimal interpolation strategy that balances high-frequency preservation with avoidance of out-of-bounds extrapolation?"
    addressed_by: 2024-05-yarn-context-extension
  - question: "What is the optimal base value for a given target context extension ratio without empirical search?"
    addressed_by: null
  - question: "Can dynamic scale factor adjustment at inference time fully replace static scaling for all use cases?"
    addressed_by: null
---

# NTK-Aware Scaled RoPE

**Author:** bloc97 (Bowen Peng, later affiliated with Nous Research)
**Date:** June 2023
**Type:** Reddit post on r/LocalLLaMA (not a formal peer-reviewed paper)
**URL:** https://www.reddit.com/r/LocalLLaMA/comments/14lz7j5/ntkaware_scaled_rope_allows_llama_models_to_have/

This is a community contribution. The method was later formalized in the YaRN paper (Peng et al., 2023, arXiv:2309.00071, published at ICLR 2024) where bloc97 is the first author. Two follow-up contributions by the same author -- "NTK-by-parts" interpolation and its integration into YaRN -- were also initially released as community posts.

---

## Core Research Problem

Position Interpolation (PI, Chen et al. 2023) extends the context window of RoPE-based LLMs by uniformly downscaling all position indices by a factor s = L'/L, where L is the pretrained context length and L' is the target length. While this avoids the catastrophic extrapolation of raw RoPE beyond L, it treats all frequency dimensions identically -- a "blind" approach. The key insight of NTK-aware scaling is that **uniform interpolation destroys high-frequency positional information** that the network needs to distinguish close-by tokens.

Drawing on Neural Tangent Kernel (NTK) theory (Tancik et al., 2020), which shows that neural networks struggle to learn high-frequency functions when input embeddings lack high-frequency components, bloc97 identified that compressing RoPE's high-frequency dimensions reduces the model's ability to resolve fine-grained local positional differences. PI compresses all dimensions by the same factor s, including the highest-frequency dimensions where adjacent token positions differ most. This makes the problem analogous to the low-dimensional input problem studied in NTK theory: without high-frequency embedding components, the network cannot represent high-frequency functions of position.

The core challenge is: **how to extend the context window of RoPE-based LLMs while preserving the high-frequency positional information needed for local token discrimination.**

---

## Problem Solutions

Instead of scaling every RoPE dimension by the same factor s, NTK-aware scaling **spreads the interpolation pressure across dimensions**: high frequencies are scaled less (preserving local resolution) and low frequencies are scaled more (accommodating the extended context). The solution is built on:

1. **NTK theory insight:** Neural networks cannot learn high-frequency functions when input embeddings lack high-frequency components (Tancik et al., 2020). RoPE acts as a Fourier Feature mapping, so compressing its high-frequency dimensions directly harms local positional resolution.
2. **Non-uniform frequency scaling via base change:** Rather than rescaling position indices (as PI does), the method changes the RoPE base parameter from b to b', which non-uniformly shifts all frequencies -- preserving the highest frequencies almost entirely while compressing the lowest frequencies by approximately factor s.
3. **Zero fine-tuning required:** The base change is a 3-line code modification with no architectural changes, no new parameters, and no additional training.

---

## Approach Details

### Method

RoPE defines frequencies theta_d = b^(-2d/|D|) where b = 10000 is the base, d indexes the hidden dimension pair (0, 1, ..., |D|/2 - 1), and |D| is the head dimension. NTK-aware scaling replaces b with a new base b':

> **b' = b * s^(|D| / (|D| - 2))**

where s = L'/L is the context extension factor (referred to as "alpha" in the original post).

In the general RoPE modification framework f'(x_m, m, theta_d) = f(x_m, g(m), h(theta_d)):
- g(m) = m (position indices are NOT rescaled, unlike PI)
- h(theta_d) = b'^(-2d/|D|) (frequencies are changed via the new base)

This means position indices remain at their original integer values, and the frequency spectrum is non-uniformly compressed. The lowest-frequency dimension (d = |D|/2 - 1) is scaled by approximately factor s (matching PI's behavior), while the highest-frequency dimension (d = 0) remains nearly unchanged, preserving the model's ability to distinguish adjacent tokens.

The derivation (formalized in YaRN Appendix A.1) requires that the lowest frequency dimension matches PI's linear interpolation scale:

> b'^((|D|-2)/|D|) = s * b^((|D|-2)/|D|)

Solving for b' gives b' = b * s^(|D| / (|D| - 2)). For LLaMA 7B with |D| = 128 (head dimension = 4096/32): b' = 10000 * s^(128/126) ≈ 10000 * s^1.016.

### Key Technical Components

**NTK theory connection.** RoPE closely resembles Fourier Features (Tancik et al., 2020). A token's position is one-dimensional, and RoPE expands it into a |D|/2-dimensional complex vector spanning a range of frequencies. NTK theory shows that when input embeddings lack high-frequency components, networks cannot learn high-frequency functions of the input. The "NTK" in "NTK-aware" refers to this theoretical motivation: the method is designed to avoid destroying the high-frequency components that the network needs to represent fine-grained positional relationships.

**Base-to-alpha correspondence.** In the implementation, the `--rope-freq-base` parameter encodes the alpha scaling. For models with |D|/2 dimension pairs, the base b' = 10000 * alpha^(|D|/(|D|-2)). For LLaMA with |D| = 128: b' ≈ 10000 * alpha^(128/126) ≈ 10000 * alpha^1.016.

**Comparison with Position Interpolation.**

| Property | PI | NTK-Aware |
|---|---|---|
| Position index scaling | m -> m/s | m -> m (unchanged) |
| Frequency scaling | All dimensions scaled equally | Non-uniform: high freq preserved, low freq compressed |
| High-frequency info | Lost (compressed by factor s) | Preserved |
| Out-of-bounds values | None (pure interpolation) | Some dimensions slightly extrapolated |
| Without fine-tuning | Poor (high perplexity) | Good (minimal perplexity degradation) |
| After fine-tuning | Good | Slightly worse than PI (due to out-of-bounds dims) |
| Code changes | [not in notes] | 3 lines |

### Experimental Setup

- **Model:** LLaMA 7B (pretrained context length L = 2048 tokens)
- **Extension factor:** alpha = 8 (target context: 8k+ tokens)
- **Evaluation:** Perplexity on long-context text, compared against baseline RoPE (no extension) and linear Position Interpolation (PI with scale factor 4)
- **Setting:** Zero-shot (no fine-tuning on longer sequences)
- **Code:** Accompanying Colab notebook demonstrating the 3-line modification

### Key Results

The perplexity comparison graph in the original post shows three conditions on LLaMA 7B:

| Method | Within pretrained range (<=2048) | Extended range (2048-8192) |
|---|---|---|
| Baseline RoPE (no scaling) | Normal perplexity | Perplexity explodes |
| PI (linear interpolation, scale=4) | Degraded (all frequencies compressed) | Moderate perplexity |
| NTK-aware (alpha=8) | Near-normal perplexity | Low perplexity, gradual increase |

Key takeaways from the perplexity comparison (graph in the post):
- **Baseline RoPE** catastrophically fails beyond the pretrained context length of 2048 tokens.
- **NTK-aware scaling** maintains substantially lower perplexity than PI across the extended context range without any fine-tuning.
- **NTK-aware preserves short-context performance** better than PI because it does not compress high-frequency dimensions.
- After fine-tuning, PI can outperform NTK-aware because PI stays strictly within the interpolation regime while NTK-aware has some dimensions in the extrapolation regime (confirmed by YaRN experiments, Table 2 in Peng et al., 2023).

### Follow-Up Contributions by bloc97

**NTK-by-parts interpolation** (GitHub PR on jquesnelle/scaled-rope, July 2023): Splits RoPE dimensions into three regimes based on the ratio r = L/lambda_d (where lambda_d = 2*pi * b^(2d/|D|) is the wavelength of dimension d):
- r > beta: do not interpolate (high frequency, preserve local distances)
- r < alpha: fully interpolate by s (low frequency, avoid extrapolation)
- alpha <= r <= beta: smooth ramp between the two

For LLaMA: alpha = 1, beta = 32. This method outperforms both PI and NTK-aware in both fine-tuned and non-fine-tuned settings by eliminating both the high-frequency destruction of PI and the out-of-bounds extrapolation of NTK-aware.

**Dynamic NTK** (by emozilla/Jeffrey Quesnelle, Reddit, June 2023): Uses a dynamic scale factor s = max(1, l'/L) that updates each forward pass based on current sequence length l'. Prevents performance degradation below L and allows graceful degradation beyond L'. Works well without fine-tuning.

Both methods were later unified with attention temperature scaling into **YaRN** (Peng et al., 2023).

### Impact and Adoption

Despite being a Reddit post, NTK-aware scaling had immediate and significant impact on the LLM ecosystem:

1. **Code Llama (Meta):** Adopted NTK-aware/dynamic NTK scaling for context extension (source 01, _references.md).
2. **Qwen (Alibaba):** Adopted Dynamic NTK-aware scaling for context extension (source 04).
3. **HuggingFace Transformers (PR #24653):** Incorporated RoPE scaling support, enabling linear (PI), NTK-aware, and dynamic NTK methods in the standard library. Merged by July 13, 2023 (source 05).
4. **YaRN (Peng et al., 2023):** Formalized NTK-aware as Definition 1 and built the full YaRN method on top of NTK-by-parts.
5. **DroPE (Gelberg et al., 2025):** Uses NTK-aware as a baseline method throughout all experimental comparisons.

---

## Limitations and Failure Modes

1. **Out-of-bounds extrapolation.** Because position indices are not rescaled, some dimensions see positional values beyond the pretrained range. This means NTK-aware is not a pure interpolation method. After fine-tuning on longer context data, PI can outperform NTK-aware because PI stays strictly within the interpolation regime (noted in the post; confirmed by YaRN Table 2).

2. **Scale factor mismatch.** The theoretical scale factor s (alpha) does not accurately describe the true context extension achieved. In practice, alpha must be set higher than the target extension ratio. For example, alpha = 8 does not yield exactly 8x context extension. The optimal base value must be found empirically, increasing the difficulty of deployment.

3. **No frequency-dependent treatment of intermediate dimensions.** NTK-aware applies a single base change globally. It does not distinguish between dimensions that should be fully interpolated (low frequency), not interpolated at all (high frequency), or partially interpolated (intermediate). All dimensions receive a non-uniform but continuous transformation. This limitation was addressed by the subsequent "NTK-by-parts" method, which uses a piecewise ramp function with separate treatment for three frequency regimes.

4. **[Inferred] Perplexity degradation at the tail end.** While NTK-aware maintains lower perplexity than PI at extended lengths without fine-tuning, perplexity still increases gradually beyond the pretrained context, as visible in the perplexity comparison graph. Sufficiently long sequences would likely exhibit further degradation, analogous to baseline RoPE and static PI.

5. **[Inferred] Limited formal evaluation.** As a Reddit post, the evaluation is limited to perplexity on a single model (LLaMA 7B) without downstream task evaluation, systematic hyperparameter sweeps, or comparison across model scales.

#### Scope and Comparability

- **What was not tested:** Only LLaMA 7B was evaluated; no testing on larger model scales (13B, 33B, 65B), non-LLaMA architectures, or models with different head dimensions. No downstream task evaluation (e.g., question answering, summarization) -- only perplexity. No comparison with ALiBi or other non-RoPE position encoding methods. No evaluation of fine-tuned NTK-aware models (the post focuses on zero-shot extension only).
- **Comparability notes:** The original post's perplexity comparisons use PI with scale=4 and NTK-aware with alpha=8 on LLaMA 7B. These are not directly comparable scale factors (PI scale=4 targets 4x extension while alpha=8 targets 8x extension). The YaRN paper (Peng et al., 2023) provides controlled comparisons with matched scale factors. Different papers in the context extension literature use different effective-length thresholds and perplexity evaluation protocols, making cross-paper comparison difficult without controlling for these variables.

---

## Conclusions

### Contributions

1. **High-frequency preservation is critical for zero-shot context extension.** Uniform position interpolation (PI) degrades short-context performance because it compresses high-frequency positional information. The NTK-aware base change preserves high frequencies while compressing low frequencies, enabling context extension without fine-tuning (perplexity comparison in the post).

2. **Simple base change achieves effective context extension.** The entire method reduces to changing the RoPE base from b to b * s^(|D|/(|D|-2)) -- a 3-line code change with no new parameters, no architectural modifications, and no fine-tuning required (code in the post).

3. **Identification of the frequency-aware principle.** NTK-aware scaling established the key insight that RoPE's frequency dimensions should be treated non-uniformly for context extension, with high frequencies preserved and low frequencies compressed. This principle underpins all subsequent improvements: NTK-by-parts, Dynamic NTK, and YaRN.

4. **Demonstration of community-driven research impact.** A Reddit post with a 3-line code change directly influenced Meta's Code Llama, Alibaba's Qwen (Dynamic NTK), HuggingFace Transformers, and the broader RoPE context extension research direction, demonstrating the role of open-source community contributions in LLM development (sources 01, 04, 05).

### Implications

1. **RoPE frequencies, not positions, are the right abstraction level for context extension.** [Inference: the success of base-change scaling over position scaling suggests that future context extension methods should operate on the frequency spectrum rather than position indices directly.]

2. **Zero-shot context extension may be sufficient for many practical applications.** NTK-aware achieves meaningful 8k+ context with no training, suggesting that some fraction of the pretrained model's capacity can be reallocated to longer context through frequency manipulation alone. [Inference: this may be speculative for tasks requiring precise long-range retrieval.]

3. **The trade-off between interpolation safety and zero-shot performance is fundamental.** NTK-aware (better zero-shot, worse fine-tuned) and PI (worse zero-shot, better fine-tuned) represent two endpoints of this trade-off, suggesting that optimal methods must find a middle ground. [Inference: this was confirmed by the NTK-by-parts and YaRN methods.]

---

## Key Claims

1. **C1: High-frequency preservation.** Scaling the RoPE base frequency preserves high-frequency components that uniform position interpolation (PI) destroys. RoPE's highest-frequency dimensions (d = 0) remain nearly unchanged under the base change, while PI compresses all dimensions equally by factor s. Evidence: frequency analysis in the post; formalized in YaRN Definition 1 and Appendix A.1. Status: **supported**. Scope: RoPE-based models using base change b' = b * s^(|D|/(|D|-2)). Magnitude: qualitative -- highest-frequency dimension remains nearly unchanged while lowest is compressed by approximately factor s.

2. **C2: Zero-shot context extension with minimal degradation.** NTK-aware interpolation extends LLaMA 7B's context to 8k+ tokens without fine-tuning, maintaining perplexity close to the pretrained model within the original context range and achieving gradual degradation beyond it. Evidence: perplexity comparison graph in the post (alpha=8 on LLaMA 7B). Status: **supported**. Scope: LLaMA 7B, alpha=8, zero-shot (no fine-tuning). Magnitude: 8x context extension (2048 to 16384+) with perplexity close to pretrained baseline within original range (single model, limited evidence).

3. **C3: Outperforms PI without fine-tuning.** Without fine-tuning, NTK-aware scaling achieves lower perplexity than PI across extended context lengths. Evidence: perplexity comparison graph in the post; confirmed by YaRN Table 1 (Peng et al., 2023). Status: **supported**. Scope: LLaMA 7B, zero-shot evaluation on extended context (2048-8192 tokens). Magnitude: substantially lower perplexity than PI across extended range (single model, limited evidence).

4. **C4: Underperforms PI after fine-tuning.** After fine-tuning on longer context data, PI outperforms NTK-aware scaling because NTK-aware leaves some dimensions in the extrapolation regime while PI stays strictly within interpolation bounds. Evidence: noted in the post and follow-up discussions; confirmed by YaRN Table 2 (Peng et al., 2023). Status: **supported**. Scope: RoPE-based models fine-tuned on extended context data. Magnitude: PI achieves lower perplexity than NTK-aware after fine-tuning (confirmed across multiple settings in YaRN Table 2).

---

## Open Questions

1. **Is there an optimal interpolation strategy that balances high-frequency preservation with avoidance of out-of-bounds extrapolation?** NTK-aware preserves high frequencies but extrapolates in some dimensions; PI avoids extrapolation but destroys high frequencies. The ideal method would combine both properties. Addressed by: `2024-05-yarn-context-extension` (YaRN's NTK-by-parts with attention temperature scaling).

2. **What is the optimal base value for a given target context extension ratio without empirical search?** The alpha parameter "inconsistently predicted effective context length across models" (NTK-by-parts PR), and the optimal value must be found empirically. No closed-form solution exists for determining the optimal base given a target extension ratio. Not addressed.

3. **Can dynamic scale factor adjustment at inference time fully replace static scaling for all use cases?** Dynamic NTK (emozilla, 2023) adjusts the scale factor per forward pass, which works well without fine-tuning but has not been extensively compared to static scaling in fine-tuned settings across diverse tasks. Not addressed.

---

## Core References and Why They Are Referenced

### Foundational

- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* The positional encoding that NTK-aware modifies. Provides the frequency-based rotation formulation theta_d = b^(-2d/|D|) that the base change operates on.

- **Tancik et al. (2020)** -- *Fourier Features Let Networks Learn High Frequency Functions in Low Dimensional Domains.* NTK theory paper providing the theoretical motivation: neural networks struggle with high-frequency functions when input embeddings lack high-frequency components. The "NTK" in "NTK-aware" refers to this theory. RoPE is identified as a Fourier Feature mapping, making NTK theory directly applicable to understanding frequency compression effects.

### Direct Predecessor

- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* The uniform interpolation method that NTK-aware improves upon. PI's blind downscaling of all position indices by 1/s loses high-frequency information; NTK-aware's non-uniform base change preserves it. Both methods address the same problem of extending RoPE-based LLMs beyond their pretrained context length.

### Successor Methods (Building on NTK-Aware)

- **bloc97 (2023)** -- *NTK-by-parts interpolation (GitHub PR).* Follow-up by the same author introducing a piecewise ramp function for frequency-dependent interpolation. Addresses NTK-aware's out-of-bounds problem by splitting dimensions into three regimes (extrapolation, interpolation, and ramp).

- **emozilla/Jeffrey Quesnelle (2023)** -- *Dynamic NTK (Reddit post).* Dynamic scale factor adaptation at inference time. Combined with NTK-aware, enables context extension without fine-tuning and without the catastrophic blowup at the tail end.

- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension.* Unifies NTK-by-parts + attention temperature scaling. Formalizes NTK-aware as Definition 1 with full mathematical derivation (Appendix A.1). First author is bloc97. Published at ICLR 2024.

### Models That Adopted NTK-Aware

- **Roziere et al. (2023)** -- *Code Llama.* Meta's code model adopted NTK-aware/dynamic NTK scaling for context extension. First major industry adoption of the base change method.

- **Bai et al. (2023)** -- *Qwen Technical Report.* Alibaba's model series adopted Dynamic NTK-aware scaling for context extension.

### Subsequent Work Using NTK-Aware as Baseline

- **Gelberg et al. (2025)** -- *DroPE: Dropping Positional Embeddings.* Uses NTK-aware as one of three primary baselines (with PI and YaRN) throughout all experiments. DroPE outperforms NTK-aware on all zero-shot context extension tasks.
