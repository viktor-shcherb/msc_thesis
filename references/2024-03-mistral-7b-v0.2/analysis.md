---
title: "Mistral 7B v0.2"
authors: "Mistral AI"
year: 2024
venue: "Hugging Face model release"
paper_type: informal
categories: ["model-release", "context-extension", "position-encoding"]
scope: ["7B model update", "context window extension from 8K to 32K via RoPE theta scaling", "removal of sliding window attention"]
benchmarks_used: ["mt-bench"]
models_introduced: ["mistral-7b-v0.2"]
models_evaluated: ["mistral-7b", "mixtral-8x7b", "mistral-medium"]
key_claims:
  - id: C1
    claim: "Extending the context window from 8K to 32K tokens can be achieved by increasing RoPE theta from 10,000 to 1,000,000 and removing sliding window attention"
    evidence: "Model card specifications, Tweet announcement (Source 01, Source 04)"
    status: supported
    scope: "Mistral 7B architecture (7.3B parameters, 32 layers, GQA); inference-time evaluation only"
    magnitude: "4x context window increase (8K to 32K tokens), 100x RoPE theta increase (10,000 to 1,000,000)"
  - id: C2
    claim: "Mistral-7B-Instruct-v0.2 achieves 7.6 on MT-Bench"
    evidence: "La Plateforme blog post (Source 03)"
    status: supported
    scope: "MT-Bench evaluation, English only, instruction-tuned variant"
    magnitude: "7.6 MT-Bench (vs 6.84 for Mistral 7B v0.1 Instruct per the original paper)"
  - id: C3
    claim: "The v0.2 instruction-tuned model was created using efficient fine-tuning and direct preference optimization"
    evidence: "La Plateforme blog post (Source 03)"
    status: unvalidated
    scope: "Mistral-7B-Instruct-v0.2 only; no details on dataset, hyperparameters, or training duration"
    magnitude: "qualitative"
  - id: C4
    claim: "Sliding window attention can be removed without degrading model quality when context is extended via RoPE theta scaling"
    evidence: "Implied by model card comparison of v0.1 and v0.2 (Source 01, Source 05)"
    status: unvalidated
    scope: "Mistral 7B architecture; no ablation isolating the effect of SWA removal from RoPE theta change"
    magnitude: "qualitative (no comparative evaluation published)"
cross_references:
  - target: 2023-10-mistral-7b
    type: extends
    detail: "Direct successor model; extends Mistral 7B v0.1 context from 8K to 32K tokens via RoPE theta scaling and SWA removal"
  - target: 2023-06-rope-ntk
    type: extends
    detail: "Applies the NTK-aware RoPE scaling principle (increasing base theta) to extend context without retraining from scratch"
  - target: 2023-12-gqa-grouped-query-attention
    type: extends
    detail: "Retains GQA with 8 KV heads from v0.1 for inference efficiency"
  - target: 2022-12-flashattention
    type: complementary
    detail: "FlashAttention optimizations used for efficient inference with the extended 32K context"
  - target: 2024-05-yarn-context-extension
    type: complementary
    detail: "YaRN provides an alternative RoPE scaling strategy; v0.2 uses the simpler approach of directly increasing theta"
  - target: 2023-06-pi-positional-interpolation
    type: complementary
    detail: "Positional Interpolation is an alternative context extension method; v0.2 uses theta scaling rather than position interpolation"
  - target: 2025-04-longgenbench-long-form-generation
    type: extended-by
    detail: "LongGenBench evaluates Mistral 7B v0.2 on long-form generation tasks"
  - target: 2025-04-round-and-round-rope
    type: extended-by
    detail: "Analyzes RoPE frequency distributions and context extension methods relevant to the theta scaling approach used in v0.2"
open_questions:
  - question: "What training procedure was used to adapt the model to 32K context? Was additional continual pretraining performed on long-context data, or was only the RoPE theta parameter changed?"
    addressed_by: null
  - question: "How does v0.2 perform on standardized long-context benchmarks (RULER, LongBench, Needle-in-a-Haystack) at various context lengths up to 32K?"
    addressed_by: null
  - question: "What is the performance tradeoff of removing sliding window attention? Does the model lose any efficiency advantages that SWA provided for shorter sequences?"
    addressed_by: null
  - question: "Does the MT-Bench improvement from 6.84 (v0.1 Instruct) to 7.6 (v0.2 Instruct) come from the context extension, the DPO training, or both?"
    addressed_by: null
  - question: "Why were the base model weights released three months after the instruction-tuned variant? Was additional evaluation or training involved?"
    addressed_by: null
---

# Mistral 7B v0.2

**Authors:** Mistral AI (no individual authors credited for this release)
**Date:** December 2023 (Instruct v0.2), March 2024 (Base v0.2)
**Type:** Model weight release (not a formal peer-reviewed paper)
**URL:** https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2

The instruction-tuned variant was released on December 11, 2023, alongside the La Plateforme API announcement. The base model weights were released on March 23, 2024, at the Mistral AI hackathon in San Francisco (hosted at SHACK15). No separate technical report was published for v0.2; the original Mistral 7B paper (Jiang et al., 2023; arXiv:2310.06825) covers the shared architecture.

---

## Core Research Problem

The original Mistral 7B (v0.1) used sliding window attention (SWA) with a 4,096-token window and an 8K-token context length. While this design provided efficient inference through a rolling buffer cache, it limited the model's usable context window relative to competing models that were beginning to support 32K or longer contexts. The RoPE positional encoding with theta=10,000 was the standard setting inherited from the LLaMA family, but emerging research on NTK-aware RoPE scaling (bloc97, 2023) and positional interpolation (Chen et al., 2023) demonstrated that context windows could be extended significantly by modifying the RoPE base frequency. The core challenge was: **how to extend Mistral 7B's context window from 8K to 32K tokens while maintaining or improving model quality.**

---

## Problem Solutions

Mistral 7B v0.2 addresses the context limitation through two architectural changes applied to the v0.1 base:

1. **RoPE theta scaling.** Increase the RoPE base frequency (theta) from 10,000 to 1,000,000, enabling the model to handle positions up to 32K tokens without the positional encoding aliasing that would occur at positions beyond the original training range.

2. **Removal of sliding window attention.** Replace the 4,096-token SWA mechanism with full causal attention, allowing every token to attend to all preceding tokens within the 32K context window.

These changes were combined with instruction fine-tuning using "efficient fine-tuning, direct preference optimisation" (La Plateforme blog, Source 03) for the Instruct variant.

---

## Approach Details

### Method

Mistral 7B v0.2 retains the core architecture of v0.1 with only the context extension parameters changed. The full architecture specification (shared between v0.1 and v0.2, per Source 06):

| Parameter | v0.1 | v0.2 |
|---|---|---|
| Parameters | 7.3B | 7.3B |
| Layers | 32 | 32 |
| Hidden dim | 4096 | 4096 |
| Head dim | 128 | 128 |
| Attention heads | 32 | 32 |
| KV heads (GQA) | 8 | 8 |
| Activation | SwiGLU | SwiGLU |
| Tokenizer | Byte-fallback BPE (32K vocab) | Byte-fallback BPE (32K vocab) |
| **Context window** | **8,192** | **32,768** |
| **RoPE theta** | **10,000** | **1,000,000** |
| **Sliding window** | **4,096 tokens** | **None (removed)** |

The three bolded rows represent the only changes between v0.1 and v0.2. All other architectural components remain identical (Source 01, Source 04, Source 06).

### Key Technical Components

#### RoPE Theta Scaling

The RoPE (Rotary Position Embedding) encoding computes rotation matrices for position-dependent attention. The base frequency theta controls the wavelength of the rotary embeddings at each dimension. By increasing theta from 10,000 to 1,000,000 (a 100x increase), the rotary embeddings at higher positions change more slowly, allowing the model to handle longer sequences without the positional encoding values becoming indistinguishable or wrapping around.

This approach is consistent with the NTK-aware scaling strategy described by bloc97 (2023), which showed that increasing the RoPE base frequency is more effective than naive position interpolation for extending context windows, as it preserves the relative resolution of high-frequency components while extending the range of low-frequency components.

#### Removal of Sliding Window Attention

In v0.1, each attention layer restricted attention to only the W=4,096 preceding tokens (Source 05). The theoretical argument was that information propagates across layers, giving a theoretical attention span of W x k = 4,096 x 32 = ~131K tokens. However, this relied on the assumption that information propagates perfectly across layers, which is not guaranteed in practice.

By removing SWA in v0.2, every token can attend to all preceding tokens within the 32K context window in every layer. This trades the O(W x n) attention cost of SWA for the standard O(n^2) cost of full attention, but allows direct access to all positions without relying on multi-layer information propagation.

#### Instruction Tuning with DPO

The La Plateforme blog states that the instruction-tuned variant was created through "efficient fine-tuning, direct preference optimisation" (Source 03). No additional details about the DPO training data, reward model, or hyperparameters are provided. The resulting Mistral-7B-Instruct-v0.2 achieved 7.6 on MT-Bench, an improvement over the v0.1 Instruct model's 6.84 score (Source 03, Source 06).

### Experimental Setup

No formal experimental evaluation was published with the v0.2 release. The only reported metric is:

- **MT-Bench**: 7.6 for Mistral-7B-Instruct-v0.2 (Source 03)

For comparison, the La Plateforme blog simultaneously reported:
- **Mixtral 8x7B** (mistral-small endpoint): 8.3 on MT-Bench
- **Mistral Medium** (mistral-medium endpoint): 8.6 on MT-Bench

**Models and access:**
- Instruct variant: `mistralai/Mistral-7B-Instruct-v0.2` on HuggingFace (official)
- Base variant: released as a tarball at `https://models.mistralcdn.com/mistral-7b-v0-2/mistral-7B-v0.2.tar`, community-converted to HuggingFace format at `mistral-community/Mistral-7B-v0.2`

**Reproducibility:** Model weights are available under Apache 2.0 license. Code at https://github.com/mistralai/mistral-src. However, no training details, data composition, or optimization hyperparameters are disclosed for either the base model adaptation or the instruction tuning. The model card warns that "Transformers tokenizer may not match `mistral_common` reference implementation exactly" (Source 01).

### Key Results

The only quantitative result reported is the MT-Bench score for the instruction-tuned variant:

| Model | MT-Bench |
|---|---|
| Mistral-7B-Instruct-v0.2 | 7.6 |
| Mistral-7B-Instruct-v0.1 | 6.84 |
| Mixtral 8x7B (mistral-small) | 8.3 |
| Mistral Medium | 8.6 |

- The v0.2 Instruct model shows a **+0.76 improvement** on MT-Bench over v0.1 Instruct (7.6 vs 6.84).
- This improvement likely reflects a combination of the extended context, DPO training, and potentially different instruction-tuning data. It is **not possible to isolate which factor contributes most** because no ablation was provided (limited evidence -- single benchmark, no ablation).
- The MT-Bench score for v0.1 (6.84) comes from the original Mistral 7B paper, while the v0.2 score (7.6) comes from the La Plateforme blog post. It is unclear whether the same evaluation protocol was used (scope limitation).

### Community Adoption

The model achieved significant community adoption (as of February 2026, Source 01, Source 02):

| Metric | Instruct v0.2 | Base v0.2 (community) |
|---|---|---|
| Monthly downloads | 2,391,103 | 4,254 |
| Likes | 3,070 | 228 |
| Adapters/Finetunes | 2,162 | 46 |
| Merges | 350 | 14 |
| Quantizations | 101 | 27 |

The Instruct variant became one of the most widely used open-weight models in its class, with over 2,000 derivative models (Source 01).

---

## Limitations and Failure Modes

The v0.2 release includes no explicit discussion of limitations. The model card notes only that there are "No built-in moderation mechanisms" and that it is a "Quick demonstration model; community engagement encouraged for guardrail implementation" (Source 01).

1. **[Inferred]** No published evaluation beyond MT-Bench. The v0.2 release provides no benchmark results for the base model and only a single MT-Bench score for the Instruct variant. There is no evaluation of long-context capability despite the 32K context window being the primary feature.

2. **[Inferred]** No ablation separating context extension from instruction tuning. The MT-Bench improvement (+0.76) may come from the extended context, from DPO training, from different training data, or from a combination. Without ablations, the contribution of each factor is unknown.

3. **[Inferred]** No published training details. Neither the continual pretraining procedure (if any) for the context extension nor the DPO training details are disclosed. It is unclear whether the base model was further trained on long-context data or whether only the RoPE theta parameter was changed.

4. **[Inferred]** English only. The La Plateforme blog explicitly states the model supports English only (Source 03), limiting generalizability to multilingual settings.

5. **[Inferred]** No safety evaluation. Unlike the original Mistral 7B paper, which included system prompt safety testing and self-reflection content moderation, the v0.2 release provides no safety evaluation.

6. **[Inferred]** Staggered release with no explanation. The base model weights were released three months after the Instruct variant, with no public explanation for the delay (Source 07). This limits reproducibility for researchers who need the base model for fine-tuning experiments.

#### Scope and Comparability

- **What was not tested:** No long-context benchmarks (RULER, LongBench, Needle-in-a-Haystack, SCROLLS). No perplexity evaluation at various context lengths. No comparison of base model quality between v0.1 and v0.2. No evaluation on reasoning, code, or knowledge benchmarks that would allow comparison with the original v0.1 paper's Table 2 results.
- **Comparability notes:** The MT-Bench v0.1 score (6.84) comes from the original Mistral 7B paper's own evaluation, while the v0.2 score (7.6) comes from the La Plateforme blog post. It is unclear whether the evaluation protocol, judge model version, or prompt formatting was identical. The v0.1 MT-Bench score was reported as 6.84 +/- 0.07 (over 10 iterations); the v0.2 score is reported without confidence intervals. The DPO training in v0.2 makes it difficult to compare with v0.1's simpler SFT approach.

---

## Conclusions

### Contributions

1. **Extended Mistral 7B context from 8K to 32K tokens.** By increasing RoPE theta to 1,000,000 and removing sliding window attention, v0.2 achieves a 4x context window increase over v0.1 (Source 01, Source 04).

2. **Demonstrated a practical context extension strategy.** The RoPE theta scaling approach used in v0.2 is simpler than alternative methods like YaRN or positional interpolation, requiring only a change to one hyperparameter and the removal of SWA.

3. **Improved instruction-following quality.** The Instruct v0.2 model achieves 7.6 on MT-Bench compared to 6.84 for v0.1 Instruct, likely due in part to DPO training (Source 03).

4. **Open-weight release under Apache 2.0.** Both Instruct and base weights were released under a permissive license, enabling widespread community adoption with over 2,000 derivative models (Source 01, Source 02).

### Implications

1. **RoPE theta scaling as a lightweight context extension method.** The v0.2 release suggests that increasing the RoPE base frequency is a practical approach for extending context windows without complex modifications. However, this implication is limited by the absence of published evaluation data showing that the extended context is actually utilized effectively.

2. **SWA may not be necessary when full context is affordable.** The removal of SWA in v0.2 suggests that Mistral AI found full attention preferable at 32K context. This is speculative, as no ablation compares the two attention strategies at matched context lengths.

3. **Model releases without papers create evaluation gaps.** The v0.2 release pattern -- model weights without a technical report -- means the community must independently evaluate the model's capabilities. This is increasingly common in the open-weight model ecosystem but limits the ability to understand design decisions.

---

## Key Claims

1. **Context extension from 8K to 32K via RoPE theta scaling and SWA removal.** The model card and tweet announcement confirm the context window was increased to 32K tokens by changing RoPE theta from 10,000 to 1,000,000 and removing sliding window attention (Source 01, Source 04). Status: **supported**. Scope: Mistral 7B architecture (7.3B parameters, 32 layers, GQA); confirmed via model specifications. Magnitude: 4x context increase, 100x theta increase. Evidence breadth: architectural specification confirmed across multiple sources (model card, tweet, community conversion), but no evaluation data demonstrating effective 32K utilization (strong evidence for the architectural change, no evidence for quality at 32K).

2. **MT-Bench score of 7.6 for Instruct v0.2.** The La Plateforme blog reports this score for the instruction-tuned variant (Source 03). Status: **supported**. Scope: MT-Bench evaluation, English only, instruction-tuned variant with DPO. Magnitude: 7.6 MT-Bench (vs 6.84 for v0.1 Instruct, a +0.76 improvement). Evidence breadth: single reported score without confidence intervals or methodology details (limited evidence -- one benchmark, one score, no error bars).

3. **DPO used for instruction tuning.** The La Plateforme blog states the model was created through "efficient fine-tuning, direct preference optimisation" (Source 03). Status: **unvalidated**. Scope: Instruct v0.2 only; no details on DPO configuration, reward model, or training data. Magnitude: qualitative. Evidence breadth: single sentence in a blog post with no supporting details (limited evidence).

4. **SWA removal does not degrade model quality.** Implied by the release of v0.2 without SWA, but no comparative evaluation is published (Source 01, Source 05). Status: **unvalidated**. Scope: Mistral 7B architecture; no ablation isolating SWA removal from theta change. Magnitude: qualitative (no comparative data). Evidence breadth: no direct evidence; the claim is inferred from the fact that Mistral AI chose to release v0.2 without SWA (no evidence).

---

## Open Questions

1. **What training procedure was used for the context extension?** Was additional continual pretraining performed on long-context data, or was only the RoPE theta parameter changed at inference time? The sources provide no information on this (not addressed).

2. **How does v0.2 perform on standardized long-context benchmarks?** No evaluation on RULER, LongBench, Needle-in-a-Haystack, or perplexity at various context lengths has been published by Mistral AI for v0.2. Third-party evaluations may exist but are not part of this reference set (not addressed).

3. **What is the performance tradeoff of removing SWA?** Does full attention improve long-context quality but reduce efficiency for short sequences? No ablation exists comparing v0.1's SWA with v0.2's full attention at matched context lengths (not addressed).

4. **Does the MT-Bench improvement come from context extension, DPO, or both?** The +0.76 improvement (6.84 to 7.6) could reflect the training methodology change (DPO vs SFT), the extended context, or different training data. Without ablations, the individual contributions are unknown (not addressed).

5. **Why were base model weights released three months after the Instruct variant?** The Hacker News discussion (Source 07) raised this question but no clear answer was provided. It may reflect a business or evaluation strategy decision by Mistral AI (not addressed).

---

## Core References and Why They Are Referenced

### Direct Predecessor

- **Jiang et al. (2023)** -- *Mistral 7B.* arXiv:2310.06825. The original Mistral 7B paper provides the full architectural specification shared between v0.1 and v0.2. All non-context-related architectural details (GQA, SwiGLU, tokenizer, layer count, hidden dimensions) are described in this paper (Source 06).

### Context Extension Methods

- **bloc97 (2023)** -- *NTK-Aware Scaled RoPE.* Reddit post and community research demonstrating that increasing the RoPE base frequency theta is more effective than naive linear interpolation for context extension. The v0.2 approach of setting theta=1,000,000 follows this principle (referenced indirectly via the approach).

- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation.* An alternative context extension method that directly interpolates positions rather than scaling theta. The v0.2 approach differs by modifying the base frequency instead.

### Architecture Components

- **Ainslie et al. (2023)** -- *GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints.* Provides the grouped-query attention mechanism (8 KV heads) retained in v0.2 for inference efficiency.

- **Dao et al. (2022)** -- *FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness.* FlashAttention optimizations support efficient inference at the extended 32K context length.

### Evaluation

- **Zheng et al. (2023)** -- *MT-Bench: Multi-turn conversation benchmark.* The only evaluation metric reported for v0.2. Used to compare the Instruct variant against v0.1 and concurrent models (Mixtral 8x7B, Mistral Medium) on the La Plateforme blog.

### Comparison Models

- **Mistral AI (2023)** -- *Mixtral 8x7B.* Simultaneously announced on the La Plateforme blog as the mistral-small endpoint (MT-Bench 8.3), providing context for v0.2's positioning within Mistral AI's model lineup.
