# DroPE: Extending the Context of Pretrained LLMs by Dropping Their Positional Embeddings

**Authors:** Yoav Gelberg, Koshi Eguchi, Takuya Akiba, Edoardo Cetin (Sakana AI, University of Oxford)
**Date:** December 2025, arXiv:2512.12167

---

## Core Research Problem

Transformer-based language models suffer sharp performance degradation when inference sequence lengths exceed the pretraining context window. This is directly caused by their reliance on explicit positional embeddings (PEs), particularly Rotary Positional Embeddings (RoPE), which become out-of-distribution at unseen sequence lengths. Existing solutions -- RoPE-scaling methods such as PI, RoPE-NTK, and YaRN -- still require expensive long-context finetuning to meaningfully use tokens beyond the original sequence length and fail to generalize zero-shot to downstream tasks. The quadratic cost of self-attention makes pretraining at long sequence lengths computationally intractable, making **zero-shot context extension** (using contexts beyond pretraining length without additional long-context finetuning) a central open challenge.

---

## Problem Solutions

DroPE proposes a fundamentally different paradigm: **remove positional embeddings entirely from a pretrained transformer** and perform a short recalibration phase at the original context length. This is grounded in three key observations:

1. **Observation 1 -- PEs accelerate training:** Positional embeddings provide a critical inductive bias that significantly facilitates pretraining convergence. NoPE (no positional embedding) transformers are equally expressive but develop positional bias at a bounded, slower rate due to bounded gradients of the attention positional bias functional at initialization.

2. **Observation 2 -- PEs prevent context extension:** RoPE-scaling methods must compress low frequencies to keep positional phases in-distribution. This compression shifts semantic attention heads at large relative distances, causing failures on downstream tasks that require attending to information deep in the context. This effect is inevitable for any post-hoc frequency scaling approach.

3. **Observation 3 -- PEs can be safely removed post-training:** Positional embeddings are not an inherent requirement for effective language modeling and can be removed after pretraining. A short recalibration phase (at the original context size) recovers in-context capabilities while unlocking zero-shot generalization to unseen sequence lengths.

---

## Approach Details

### Method
- **Phase 1 (Pretraining):** Train a standard RoPE transformer normally, leveraging the inductive bias of positional embeddings for efficient convergence.
- **Phase 2 (DroPE recalibration):** At the end of pretraining, remove all positional embeddings from every layer and continue training for a small fraction of the original budget at the original context length.

### Key Technical Components
- **Recalibration budget:** For from-scratch training, DroPE replaces the final portion of the pretraining schedule at no extra cost (e.g., the last 2B of 16B tokens). For adapting pretrained models in the wild, recalibration requires 0.5-2% of the original pretraining budget (e.g., 20B tokens for SmolLM-1.7B pretrained on 1T = 2%, and 20B tokens for Llama2-7B pretrained on 4T = 0.5%). For SmolLM-360M (600B tokens pretrained), >95% of in-context performance is recovered after <5B recalibration tokens (0.8% of original budget).
- **QKNorm:** For extended recalibration periods, query-key normalization (Henry et al., 2020) is added after dropping PEs to stabilize training at higher learning rates and mitigate gradient spikes.
- **Softmax temperature scaling at inference:** Following Wang et al. (2024), a single scalar logit temperature is tuned on a held-out set at the target length to calibrate attention for longer sequences. The optimal scale follows the form: `beta* = 1 + c * ln(s)`, where s = C_test / C_train is the context extension factor. For the from-scratch DroPE model, c = 0.412; for SmolLM-DroPE, c = 0.103.

### Theoretical Analysis
- **Theorem 3.4:** For NoPE transformers, the prefix-spread of hidden states, the attention positional bias, and its gradients w.r.t. query/key projections are all bounded by O(epsilon) at initialization, where epsilon is the initial embedding spread. Constants depend only on architecture (layers, heads), not sequence length.
- **Proposition 3.2:** NoPE transformers on constant input sequences have uniform attention, vanishing Q/K gradients, and zero positional bias -- a pathological case that RoPE avoids.
- **Proposition 3.3:** RoPE heads maintain non-zero positional bias and non-zero gradients even on constant sequences, enabling faster learning of positional patterns.

### Experimental Setup
- **From-scratch experiments:** 494M parameter Qwen2-style transformer on 16.8B FineWeb tokens (context 1024). DroPE applied at step 14K of 16K total, replacing the final 2K steps (2.1B tokens) with PE-free recalibration at no extra training cost.
- **Pretrained model experiments:** SmolLM-360M (600B tokens pretrained), recalibrated with 30B/60B/120B tokens. SmolLM-1.7B and Llama2-7B recalibrated with only 20B tokens each.
- **Evaluation:** RULER benchmark (multi-query, multi-key, multi-value NIAH), LongBench (MultiFieldQA, MuSiQue, GovReport, LCC), and six standard LM benchmarks (ARC-E/C, HellaSwag, OpenBookQA, PIQA, WinoGrande).

### Key Results
| Setting | DroPE | Best RoPE-scaling baseline |
|---|---|---|
| Zero-shot NIAH at 2x (from scratch) | 28.0 / 41.6 / 23.3 | 21.1 / 19.4 / 16.5 (RoPE-NTK) |
| SmolLM LongBench Avg. | 30.52 | 19.94 (YaRN) |
| SmolLM NIAH at 2x / 4x / 8x | 74.9 / 55.0 / 52.2 | 48.3 / 26.2 / 16.5 (YaRN / LongRoPE2) |
| Llama2-7B LongBench Avg. | 26.08 | 21.88 (RoPE-NTK) |
| In-context benchmarks (SmolLM-360M) | 53.4 avg | 53.1 avg (original SmolLM) |

DroPE recovers >95% of SmolLM's in-context performance after <5B tokens (0.8% of original budget).

---

## Conclusions

1. **Positional embeddings are a transient training scaffold:** They are essential for efficient pretraining convergence but are not required for effective language modeling at inference. This reinterpretation challenges the conventional permanent role of PEs in transformers.

2. **DroPE enables zero-shot context extension:** By removing PEs after pretraining and performing a short recalibration, models generalize to sequences far beyond their training context without any long-context finetuning -- a capability that all existing RoPE-scaling methods fail to achieve.

3. **No compromise on in-context performance:** DroPE preserves both perplexity and downstream task performance within the original training context, matching or exceeding the base model.

4. **Scalability:** Results hold across model sizes (360M to 7B parameters), pretraining budgets (16B to 4T tokens), and architectures, with recalibration costs as low as 0.5% of the pretraining budget.

5. **Broader implication:** Canonical trade-offs in LM architecture design can be reconciled by employing different architectural choices for different stages of training and inference, then recalibrating.

---

## Core References and Why They Are Referenced

### Positional Embedding Foundations
- **Su et al. (2024)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the dominant PE scheme in modern LLMs. DroPE specifically targets removing RoPE after pretraining.
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational transformer architecture paper; introduced absolute positional embeddings and the self-attention mechanism that DroPE modifies.

### NoPE (No Positional Embedding) Transformers
- **Haviv et al. (2022)** -- *Transformer Language Models Without Positional Encodings Still Learn Positional Information.* Shows NoPE transformers can learn positional information implicitly via causal masking, but underperform RoPE. Motivates the question of why PEs help training.
- **Kazemnejad et al. (2023)** -- *The Impact of Positional Encoding on Length Generalization in Transformers.* Proves NoPE's first attention layer can perfectly reconstruct positions; shows NoPE has the same expressivity as RoPE. DroPE builds on this by showing the gap is in optimization, not expressivity.

### RoPE Context Extension Methods (Baselines)
- **Chen et al. (2023)** -- *Extending Context Window of Large Language Models via Positional Interpolation (PI).* Uniform frequency scaling baseline; DroPE substantially outperforms it.
- **bloc97 (2023)** -- *NTK-Aware Scaled RoPE.* Non-uniform scaling that preserves high frequencies; used as a baseline throughout DroPE's evaluations.
- **Peng et al. (2023)** -- *YaRN: Efficient Context Window Extension of Large Language Models.* Most popular RoPE-scaling method; DroPE's primary comparison target. DroPE shows YaRN's zero-shot behavior is equivalent to simply cropping context.
- **Ding et al. (2024)** -- *LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens.* Advanced RoPE extension; DroPE outperforms it on NIAH tasks.

### Models Used in Evaluation
- **Allal et al. (2024)** -- *SmolLM.* Provides the 360M and 1.7B parameter models used for DroPE's "LMs in the wild" experiments, demonstrating post-hoc applicability.
- **Touvron et al. (2023)** -- *Llama 2.* Provides the 7B parameter model demonstrating DroPE's scalability to large pretrained models.

### Evaluation Benchmarks
- **Hsieh et al. (2024)** -- *RULER.* Provides the multi-query/key/value NIAH tasks used for zero-shot long-context evaluation.
- **Bai et al. (2023)** -- *LongBench.* Bilingual multitask long-context benchmark (MultiFieldQA, MuSiQue, GovReport, LCC) used for downstream evaluation.
- **Kamradt (2023)** -- *Needle in a Haystack.* Original NIAH evaluation framework for pressure-testing LLM context utilization.

### Theoretical Analysis Support
- **Barbero et al. (2024)** -- *Round and Round We Go! What Makes Rotary Positional Encodings Useful?* Demonstrates that high RoPE frequencies are used by positional heads and low frequencies by semantic heads. This directly supports DroPE's analysis of why RoPE-scaling inevitably fails (Observation 2).
- **Nesterov (2013)** -- *Introductory Lectures on Convex Optimization.* Provides convexity and smoothness results used in the proof of the softmax Lipschitz bound (Lemma B.4) underlying Theorem 3.4.
- **Vershynin (2018)** -- *High-Dimensional Probability.* Used for bounding operator norms of random weight matrices at initialization in Theorem 3.4's proof.

### Alternative Architectures (Compared Against)
- **Press et al. (2021)** -- *ALiBi: Train Short, Test Long.* Alternative PE scheme using linear attention biases for length extrapolation. DroPE outperforms ALiBi on all NIAH tasks.
- **Yang et al. (2025b)** -- *RoPE to NoPE and Back Again (RNoPE-SWA).* Hybrid attention strategy between RoPE and NoPE. DroPE outperforms it; the approach is noted as complementary.
- **Puvvada et al. (2025)** -- *SWAN-GPT.* Scalable long-context modeling approach occupying middle ground between RoPE and NoPE. Noted as complementary to DroPE.

### Training Stability
- **Henry et al. (2020)** -- *Query-Key Normalization for Transformers.* QKNorm technique adopted by DroPE during longer recalibration phases to stabilize training at higher learning rates.
- **OLMo et al. (2024b)** -- *2 OLMo 2 Furious.* Documents loss spikes at high learning rates that QKNorm mitigates; motivates DroPE's use of QKNorm for extended recalibration.

### Data and Training
- **Penedo et al. (2024)** -- *The FineWeb Datasets.* Training data for from-scratch experiments and recalibration of SmolLM models.
- **Hoffmann et al. (2022)** -- *Training Compute-Optimal Large Language Models (Chinchilla).* Provides compute-optimal scaling reference; DroPE experiments train well beyond chinchilla-optimal rates.

#### Cross-References in Available Papers

- **PI (`2023-06-pi-positional-interpolation`):** DroPE uses PI (Chen et al., 2023) as a baseline throughout. PI is the simplest RoPE-scaling method (uniform frequency scaling by 1/s). DroPE substantially outperforms PI in all zero-shot evaluations: PI scores 0.0 on all NIAH tasks at 2x context (Table 1), while DroPE scores 28.0/41.6/23.3.
- **RoPE-NTK (`2023-06-rope-ntk`):** bloc97's NTK-aware scaling is used as a baseline throughout DroPE's evaluations. It is the strongest RoPE-scaling baseline on the from-scratch NIAH tasks (Table 1). DroPE outperforms it on all metrics. The analysis of why low-frequency compression is inevitable (Section 4.1) directly applies to NTK scaling via Equation 3.
- **YaRN (`2024-05-yarn-context-extension`):** YaRN is DroPE's primary comparison target and the most popular RoPE-scaling method. DroPE's key empirical finding (Figure 5) is that YaRN's zero-shot behavior is equivalent to cropping the context to the pretraining length -- maintaining perplexity but ignoring distant information. DroPE outperforms YaRN on LongBench (30.52 vs. 19.94 average, Table 2) and NIAH at all extension factors (Table 10).
- **Lost in the Middle (`2024-02-lost-in-the-middle`):** Liu et al. (2023b) is cited (Section 4) as demonstrating that RoPE-scaling methods exhibit sharp performance drops on downstream tasks when important information is deep in the context, supporting Observation 2.
- **RULER (`2024-10-ruler-context-size`):** The RULER benchmark (Hsieh et al., 2024) provides the multi-query, multi-key, and multi-value NIAH tasks used for zero-shot long-context evaluation in Tables 1 and 10.
