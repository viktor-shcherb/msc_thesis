---
title: "LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens"
authors: "Ding, Zhang, Zhang, Xu, Shang, Xu, Yang, Yang"
year: 2024
venue: "ICML 2024"
paper_type: conference-paper
categories: ["context-extension", "position-encoding"]
scope: ["RoPE-based LLMs", "context window extension", "positional encoding interpolation", "non-uniform rescaling"]
benchmarks_used: ["perplexity-pg19", "passkey-retrieval", "arc", "hellaswag", "mmlu", "truthfulqa"]
models_introduced: []
models_evaluated: ["llama-2-7b", "mistral-7b"]
key_claims:
  - id: C1
    claim: "LongRoPE extends context windows to 2048k tokens with only 1k fine-tuning steps at 256k training lengths, achieving an 8x extension beyond fine-tuning length without additional training"
    evidence: "Section 1, Section 4.1, Table 1"
    status: supported
  - id: C2
    claim: "Non-uniform positional interpolation with evolutionary search discovers that lower RoPE dimensions and initial token positions benefit from less aggressive interpolation, outperforming linear and human-designed methods"
    evidence: "Section 3.1, Section 3.2, Figures 3-4"
    status: supported
  - id: C3
    claim: "Progressive extension strategy (pretrained -> 256k -> 2048k via secondary search) is more effective than direct extension to very long contexts"
    evidence: "Section 3.3, Section 4.1, Table 1"
    status: supported
  - id: C4
    claim: "LongRoPE maintains >90% passkey retrieval accuracy from 4k to 2048k tokens on LLaMA2-7B"
    evidence: "Section 4.2, Figure 6"
    status: supported
  - id: C5
    claim: "Short-context recovery via additional RoPE factor search restores original context window performance while maintaining extended context capabilities"
    evidence: "Section 3.4, Section 4.3, Table 2"
    status: supported
  - id: C6
    claim: "LongRoPE-extended models maintain comparable performance on standard benchmarks (ARC, HellaSwag, MMLU, TruthfulQA) at 4096 context despite massive extension ratio"
    evidence: "Section 4.3, Table 2"
    status: supported
cross_references:
  - target: 2024-05-yarn-context-extension
    type: extends
    detail: "LongRoPE builds on YaRN's targeted interpolation by discovering non-uniform rescale factors via evolutionary search rather than using fixed frequency-dependent formulas"
  - target: 2023-06-pi-positional-interpolation
    type: extends
    detail: "LongRoPE improves on PI's uniform linear interpolation by discovering non-uniform dimension-wise and position-wise rescaling factors"
  - target: 2024-01-roformer-rope
    type: extends
    detail: "LongRoPE modifies RoPE's per-dimension frequencies via learned non-uniform rescale factors rather than the original fixed theta_d values"
open_questions:
  - question: "Can the evolutionary search be replaced with a principled analytical formula for optimal rescale factors?"
    addressed_by: null
  - question: "Does the progressive extension strategy generalize to other architectures beyond LLaMA2 and Mistral?"
    addressed_by: null
  - question: "What is the optimal trade-off between search cost and extension quality at extreme context lengths?"
    addressed_by: null
  - question: "Why does Mistral degrade more than LLaMA2 at very long contexts (>256k)?"
    addressed_by: null
---
# LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens

**Authors:** Yiran Ding, Li Lyna Zhang, Chengruidong Zhang, Yuanyuan Xu, Ning Shang, Jiahang Xu, Fan Yang, Mao Yang (Microsoft Research)
**Date:** February 2024, arXiv:2402.13753; published at ICML 2024

---

## Core Research Problem

Large context windows are a desirable feature in LLMs, enabling applications such as long document understanding, multi-turn conversations, and in-context learning with many examples. However, extending context windows of pretrained models faces three core challenges: (1) high fine-tuning costs, since training on very long sequences requires extensive compute; (2) scarcity of long training texts, since most corpora lack documents of millions of tokens; and (3) catastrophic performance degradation, since positional embeddings encounter out-of-distribution values at novel positions.

Prior methods like Position Interpolation (PI) and YaRN address these challenges by interpolating positional encodings, but they are limited to around 128k tokens. PI uses uniform linear interpolation across all RoPE dimensions, which compresses high-frequency positional information. YaRN improves on this with frequency-aware interpolation but uses fixed formulas (NTK-by-parts with predetermined alpha/beta parameters) rather than learning optimal rescale factors. Furthermore, both methods require fine-tuning at or near the target context length.

The core challenge is: **how to extend context windows to millions of tokens while minimizing fine-tuning costs, maintaining short-context performance, and achieving effective utilization of the extended context.**

---

## Problem Solutions

LongRoPE introduces three key innovations that together enable 2048k token context windows:

1. **Non-uniform positional interpolation via evolutionary search:** Rather than using uniform or fixed frequency-dependent interpolation, LongRoPE discovers that RoPE dimensions and token positions have varying interpolation requirements. An evolutionary search algorithm efficiently finds per-dimension rescale factors that minimize perplexity at the target context length.

2. **Progressive extension strategy:** Instead of directly fine-tuning to 2048k tokens, LongRoPE first extends to 256k via search and fine-tuning, then performs a second search on the fine-tuned model to achieve 2048k without additional training. This leverages the observation that searched rescale factors enable approximately 8x extension beyond the fine-tuning length.

3. **Short-context recovery:** Extended models often suffer performance degradation at original context lengths. LongRoPE performs additional evolutionary search to find RoPE factors optimized for short contexts (4k-8k), then dynamically selects appropriate factors during inference based on input length.

---

## Approach Details

### Method

LongRoPE formulates context extension as an optimization problem over RoPE rescale factors. For a model pretrained with context length L and target extension to L' = s * L, the method searches for:

1. **Per-dimension rescale factors** lambda_i for each RoPE dimension i
2. **Starting token threshold** n_hat, below which original RoPE values are preserved

The modified RoPE embedding becomes:

> theta'_i = theta_i / lambda_i for position m >= n_hat
> theta'_i = theta_i for position m < n_hat

where theta_i = 10000^(-2i/d) is the original RoPE frequency for dimension i.

**Evolutionary search algorithm:**
- Population size: 64 individuals
- Each individual: vector of rescale factors (lambda_1, ..., lambda_{d/2}) plus starting threshold n_hat
- Fitness function: perplexity on 5 PG19 samples of target context length
- Constraints: lambda_i values must be monotonically non-decreasing (lambda_i <= lambda_{i+1})
- Initialization: population seeded with PI (uniform), NTK-aware, and YaRN solutions
- Search space: lambda_i in [1.0, s * 1.25] with 0.01 step size; n_hat in {0, 1, 2, 4, 8, 12, 16, 20, 24, 28, 32, 64, 128, 256}

### Key Technical Components

**Non-uniform dimension rescaling:** The search reveals that lower RoPE dimensions (higher frequencies) benefit from smaller rescale factors than higher dimensions (lower frequencies). This is consistent with YaRN's insight that high-frequency components encode local positional information that should be preserved, but LongRoPE discovers the optimal rescaling empirically rather than using a fixed formula.

**Non-uniform position rescaling:** The search also discovers that initial token positions (positions < n_hat) benefit from no rescaling at all. This preserves the model's ability to correctly process the beginning of sequences, which is particularly important for instruction-following models where system prompts appear at the start.

**Progressive extension:** The key observation is that searched rescale factors enable approximately 8x effective context extension beyond the fine-tuning length without additional training. Thus:
1. Search optimal factors for 256k, fine-tune with these factors on 256k training data
2. Search again on the fine-tuned 256k model to find factors for 2048k
3. Use the 2048k factors for inference without any 2048k fine-tuning

**Short-context recovery:** Extended models show degraded performance on short contexts. LongRoPE addresses this by:
1. Searching for separate RoPE factors optimized for short contexts (4k-8k evaluation length)
2. Storing both short-context and long-context factors
3. At inference time, selecting factors based on the input sequence length

### Experimental Setup

**Models.** LLaMA2-7B and Mistral-7B v0.1, both using RoPE positional encoding with base b = 10000.

**Fine-tuning (LLaMA2):**
- 128k extension: 400 steps on 8 A100 GPUs, learning rate 2e-5 with linear decay, batch size 32
- 256k extension: 600 additional steps on 16 A100 GPUs
- Dataset: RedPajama (segments of 128k tokens)

**Fine-tuning (Mistral):**
- Both 128k and 256k: 400 steps on 4 A100 GPUs, learning rate 1e-6 (constant), batch size 64
- Training sequence length: 16k (following YaRN methodology)
- Dataset: Together Long-Data Collections

**Search costs:**
- Up to 256k: approximately 3 days on a single A100
- 2048k search: 5-day limit using 8 A100 GPUs
- Per-evaluation at 2048k: approximately 50 minutes

**Evaluation:**
1. Perplexity on Books3 corpus (PG19 variant) at lengths 8k to 2048k
2. Passkey retrieval at lengths 4k to 2048k (passkey placed at random location)
3. Standard benchmarks: ARC-Challenge (25-shot), HellaSwag (10-shot), MMLU (5-shot), TruthfulQA (0-shot) at 4096 context

### Key Results

**Perplexity at extended contexts (Books3, Table 1):**

| Model | Fine-tune Length | 8k | 32k | 128k | 256k | 512k | 1024k | 2048k |
|---|---|---|---|---|---|---|---|---|
| LLaMA2-7B YaRN | 128k | 6.56 | 5.51 | 5.11 | 5.60 | -- | -- | -- |
| LLaMA2-7B LongRoPE | 256k | 6.55 | 5.52 | 5.10 | 4.81 | 5.32 | 6.38 | 7.80 |
| Mistral-7B YaRN | 128k | 6.55 | 5.63 | 5.63 | 5.99 | -- | -- | -- |
| Mistral-7B LongRoPE | 256k | 6.63 | 5.65 | 5.60 | 5.54 | 6.68 | 9.19 | 13.71 |

- LongRoPE-LLaMA2 maintains reasonable perplexity (7.80) at 2048k, while YaRN degrades beyond 256k
- LongRoPE achieves 8x extension beyond fine-tuning length (256k fine-tune -> 2048k inference)
- Mistral shows more degradation than LLaMA2 at very long contexts

**Passkey retrieval (Figure 6):**

| Model | Fine-tune Length | 4k-512k | 1024k | 2048k |
|---|---|---|---|---|
| LLaMA2-7B LongRoPE | 256k | >90% | >90% | >90% |
| Mistral-7B LongRoPE | 128k | 100% | 90% | 60% |

- LLaMA2-LongRoPE maintains >90% passkey accuracy throughout 4k-2048k range
- Mistral degrades more at extreme lengths (60% at 2048k)

**Short-context benchmark performance (Table 2, 4096 context):**

| Model | Extension | ARC-c | HellaSwag | MMLU | TruthfulQA |
|---|---|---|---|---|---|
| LLaMA2-7B | Original | 53.1 | 77.7 | 45.9 | 38.8 |
| LLaMA2-7B LongRoPE | 2048k (ft=128k) | 52.9 | 76.5 | 43.4 | 38.8 |
| Mistral-7B | Original | 59.5 | 81.3 | 60.1 | 42.6 |
| Mistral-7B LongRoPE | 2048k (ft=128k) | 59.0 | 81.2 | 61.3 | 43.1 |

- Short-context recovery maintains near-original performance on standard benchmarks
- LLaMA2: ARC-c drops 0.2, HellaSwag drops 1.2, MMLU drops 2.5, TruthfulQA unchanged
- Mistral: maintains or slightly improves on all benchmarks

---

## Limitations and Failure Modes

1. **Perplexity degradation at extreme lengths.** LLaMA2-LongRoPE perplexity increases from 4.81 at 256k to 7.80 at 2048k -- nearly 62% increase. Mistral degrades even more severely: 5.54 at 256k to 13.71 at 2048k -- 147% increase.

2. **Model-dependent effectiveness.** Mistral shows substantially worse long-context performance than LLaMA2 at >256k despite similar architecture. The paper does not analyze why.

3. **Computationally expensive search.** Finding optimal rescale factors for 2048k requires 5 days on 8 A100 GPUs, with each fitness evaluation taking approximately 50 minutes.

4. **No downstream task evaluation at extended lengths.** The paper evaluates perplexity and passkey retrieval but not complex reasoning or information synthesis tasks at 2048k context.

5. **Fixed search budget may be suboptimal.** The evolutionary search uses fixed population size and evaluation budget; different hyperparameters might yield better rescale factors.

6. **Limited model coverage.** Only evaluated on LLaMA2-7B and Mistral-7B; scaling behavior to larger models is unknown.

---

## Conclusions

### Contributions

1. **Non-uniform positional interpolation.** Discovered that RoPE dimensions and token positions have varying interpolation requirements, and that evolutionary search can efficiently find optimal per-dimension rescale factors that outperform fixed formulas (Section 3.1-3.2, Figures 3-4).

2. **Progressive extension strategy.** Introduced a two-stage approach (256k fine-tune -> 2048k search) that exploits the 8x non-fine-tuning extension capability, enabling 2048k context with only 256k training data (Section 3.3).

3. **Short-context recovery.** Developed a method to maintain original context window performance through separate RoPE factor search and dynamic factor selection at inference time (Section 3.4, Table 2).

4. **First 2048k context extension.** Achieved the first published extension of LLM context windows to 2048k tokens while maintaining reasonable perplexity and >90% passkey retrieval accuracy on LLaMA2-7B (Section 4.1-4.2).

5. **Compute-efficient extension.** Extended context by 512x (4k -> 2048k) with only 1000 fine-tuning steps at 256k training length, compared to prior methods that required fine-tuning at or near the target length.

### Implications

1. **Learned rescale factors outperform fixed formulas.** The success of evolutionary search suggests that optimal context extension parameters are model-specific and data-specific, favoring learned over hand-designed approaches.

2. **Progressive extension enables extreme lengths.** The 8x non-fine-tuning extension capability suggests that context extension methods need not be trained at the final target length, significantly reducing compute requirements.

3. **Short-context performance is recoverable.** The short-context recovery mechanism demonstrates that extended models can dynamically adapt their positional encoding behavior based on input length, potentially enabling a single model to handle diverse context requirements (speculative).

---

## Key Claims

**C1. LongRoPE extends context windows to 2048k tokens with only 1k fine-tuning steps at 256k training lengths.** The progressive extension strategy fine-tunes to 256k (400+600 steps for LLaMA2, 400 steps for Mistral), then searches for 2048k factors without additional fine-tuning, achieving 8x extension beyond fine-tuning length (Section 4.1, Table 1). Status: **supported**.

**C2. Non-uniform positional interpolation discovers that lower RoPE dimensions and initial token positions benefit from less aggressive interpolation.** The evolutionary search finds rescale factors that are smaller for lower dimensions and identifies optimal starting thresholds n_hat that preserve original RoPE values for initial positions. These searched factors outperform PI, NTK, and YaRN baselines in perplexity (Section 3.1-3.2, Figures 3-4). Status: **supported**.

**C3. Progressive extension is more effective than direct extension.** Fine-tuning directly to 256k then searching for 2048k factors yields better results than attempting to search/fine-tune directly to very long contexts, as demonstrated by the 8x extension capability (Section 3.3, Section 4.1). Status: **supported**.

**C4. LongRoPE maintains >90% passkey retrieval accuracy from 4k to 2048k tokens.** LLaMA2-7B with LongRoPE (fine-tuned at 256k) achieves >90% passkey retrieval throughout the 4k-2048k range. Mistral shows lower accuracy at extreme lengths (60% at 2048k) (Section 4.2, Figure 6). Status: **supported** for LLaMA2, partially supported for Mistral.

**C5. Short-context recovery restores original context window performance.** Additional evolutionary search finds RoPE factors optimized for 4k-8k contexts, and dynamic factor selection during inference maintains near-baseline performance on ARC, HellaSwag, MMLU, and TruthfulQA benchmarks (Section 3.4, Section 4.3, Table 2). Status: **supported**.

**C6. LongRoPE-extended models maintain comparable performance on standard benchmarks.** At 4096 context, LLaMA2-LongRoPE (2048k capable) achieves 52.9 ARC-c (vs 53.1 original), 76.5 HellaSwag (vs 77.7), 43.4 MMLU (vs 45.9), 38.8 TruthfulQA (vs 38.8). Mistral-LongRoPE maintains or slightly improves all metrics (Table 2). Status: **supported**.

---

## Open Questions

1. **Can evolutionary search be replaced with analytical formulas?** The paper uses computationally expensive search to find rescale factors. Whether these factors follow predictable patterns that could be captured by closed-form expressions remains unknown. Unresolved.

2. **Does progressive extension generalize beyond LLaMA2/Mistral?** The 8x non-fine-tuning extension capability is demonstrated only on these two models. Whether this ratio holds for other architectures (different dimensions, attention patterns) is untested. Unresolved.

3. **What is the optimal trade-off between search cost and extension quality?** The paper uses fixed search budgets; a systematic study of how search cost affects final quality (and diminishing returns) is not provided. Unresolved.

4. **Why does Mistral degrade more than LLaMA2 at very long contexts?** Despite similar architecture and RoPE configuration, Mistral shows substantially worse perplexity and passkey accuracy beyond 256k. The architectural or training differences responsible are not analyzed. Unresolved.

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations

- **Su et al. (2022) -- RoFormer.** Introduces Rotary Position Embeddings (RoPE), the positional encoding that LongRoPE modifies. The entire method is built on RoPE's per-dimension frequency structure theta_d = 10000^(-2d/|D|).

- **Vaswani et al. (2017) -- Attention Is All You Need.** Foundational Transformer architecture; provides context for positional encoding requirements.

### Direct Predecessors

- **Chen et al. (2023) -- Position Interpolation.** The uniform linear interpolation baseline that LongRoPE improves upon. PI's limitation of treating all dimensions identically motivates the non-uniform search.

- **Peng et al. (2024) -- YaRN.** The frequency-aware interpolation method that LongRoPE builds on. YaRN's NTK-by-parts interpolation uses fixed formulas; LongRoPE replaces these with searched factors and achieves longer extension.

- **bloc97 (2023) -- NTK-Aware Scaling.** Proposes spreading interpolation pressure via base frequency change. LongRoPE's evolutionary search is initialized with NTK solutions.

### Context Extension Methods

- **Roziere et al. (2023) -- Code Llama.** Uses NTK-aware scaling for 100k context; comparison baseline showing limitations of fixed rescaling.

- **kaiokendev (2023) -- SuperHOT.** Concurrent position interpolation work referenced for context.

### Models Evaluated

- **Touvron et al. (2023) -- Llama 2.** Primary evaluation model; LongRoPE extends LLaMA2-7B to 2048k tokens.

- **Jiang et al. (2023) -- Mistral 7B.** Secondary evaluation model demonstrating generalization beyond LLaMA family.

### Evaluation

- **Rae et al. (2020) -- PG19/Books3.** Long-document corpus used for perplexity evaluation.

- **Mohtashami & Jaggi (2023) -- Landmark Attention.** Provides the passkey retrieval evaluation task.

- **Clark et al. (2018) -- ARC, Zellers et al. (2019) -- HellaSwag, Hendrycks et al. (2021) -- MMLU, Lin et al. (2022) -- TruthfulQA.** Standard benchmarks for short-context performance evaluation.
