# Extending Context Window of Large Language Models via Position Interpolation

**Authors:** Shouyuan Chen, Sherman Wong, Liangjian Chen, Yuandong Tian (Meta Platforms Inc.)
**Date:** June 2023, arXiv:2306.15595v2

---

## Core Research Problem

Large language models using RoPE-based positional encodings (e.g., LLaMA) are pretrained with a fixed context window (e.g., 2048 tokens) and suffer catastrophic performance degradation when inference sequences exceed this length. Direct extrapolation -- simply using the model at longer positions -- causes attention scores to explode to extremely large values (perplexity >10^3), completely breaking the self-attention mechanism. This occurs because the trigonometric basis functions {phi_j} underlying RoPE form a universal approximator: while the learned attention score function a(s) is well-behaved within the trained range [0, L], the same coefficients can produce arbitrarily large values outside this range. Naive fine-tuning on longer contexts is extremely inefficient, extending the effective window from 2048 to only 2560 after 10,000 training steps. The core challenge is: **how to extend the context window of existing pretrained RoPE-based LLMs efficiently, without retraining from scratch.**

---

## Problem Solutions

Position Interpolation proposes a conceptually simple solution: **linearly down-scale input position indices** so they fall within the original pretrained range, rather than extrapolating beyond it. For a model pretrained with context window L and a target context window L', replace the RoPE function f(x, m) with:

> f'(x, m) = f(x, mL/L')

This maps position indices from [0, L') back to [0, L), ensuring all inputs to RoPE remain within the distribution seen during pretraining. The key insight is that while extrapolation is catastrophically unstable, **interpolation between known grid points is smooth and well-bounded** thanks to the smoothness of the trigonometric basis functions.

---

## Approach Details

### Method
- **Position rescaling:** Replace every position index m with mL/L' before computing RoPE. No architectural changes, no new parameters, no modifications to the attention mechanism.
- **Fine-tuning:** After rescaling, fine-tune the model on the extended context window for a small number of steps (1000 steps on the Pile dataset) using next-token prediction. The model adapts quickly because it starts from a good initialization -- it only needs to adjust to the denser interpolated position encodings, not learn new knowledge.

### Key Technical Components
- **Drop-in position rescaling:** The only change is replacing position index m with mL/L' before passing to RoPE. No new parameters, no architectural modifications, no changes to the attention mechanism. This makes PI compatible with existing optimizations (Flash Attention, FSDP).
- **Optimizer:** AdamW with β1 = 0.9, β2 = 0.95. Weight decay set to zero.
- **Learning rate schedule:** Linear warmup of 20 steps starting from 10% of the maximum learning rate. Maximum LR is 2×10⁻⁵ for 7B/13B models and 10⁻⁵ for 33B/65B models.
- **Batch size:** 64 global batch size for extending 7B/13B/33B to 8192; 128 global batch size for all other configurations.
- **Dataset insensitivity:** Fine-tuning results are not sensitive to the choice of dataset (Pile vs. RedPajama), likely because the model is adapting to the new position encoding distribution rather than acquiring new knowledge.

### Theoretical Analysis
- **Theorem 2.1 (Interpolation bound):** For attention score a(s) = Re[sum_j h_j e^{is*theta_j}], the deviation from linear interpolation between two known grid points s1, s2 is bounded by:
  |a(s) - a_linear(s)| <= d * max_j|h_j| * (s-s1)(s2-s) / (8 ln c)
  where c=10000, d is head dimension. For integer grid points this gives a bound ~d*max|h_j|/294.73.
- **Comparison with extrapolation:** The extrapolation bound from RoPE (Su et al., 2021) is |a(s)| <= 2*max|h_j| * B(s), where B(s) >= d numerically. The interpolation bound is therefore at least **~600x smaller** than the extrapolation bound (in the LLaMA 7B setting), explaining why interpolation is far more stable.
- **Implication:** Regularizing max_j|h_j| during pretraining could further reduce both bounds, potentially mitigating extrapolation failures entirely (left as future work).

### Experimental Setup
- **Models:** LLaMA 7B, 13B, 33B, 65B extended to context windows of 8192, 16384, and 32768 (up to 16x the original 2048).
- **Fine-tuning:** 1000 steps with AdamW (lr=2e-5 for 7B/13B, lr=1e-5 for 33B/65B), on the Pile dataset. 32-128 A100 GPUs depending on configuration.
- **Evaluation:** Perplexity on PG-19 (books) and Arxiv Math Proof-pile, passkey retrieval for effective context window measurement, GovReport long document summarization, and standard LLaMA benchmarks (BoolQ, PIQA, Race-M/H, WinoGrande).

### Key Results
| Setting | PI Result | Baseline |
|---|---|---|
| LLaMA 7B perplexity at 8192 (PG-19) | 6.95 | 7.20 (original at 2048) / 7.69 (direct FT) |
| LLaMA 7B perplexity at 16384 (PG-19) | 6.83 | >10^3 (extrapolation) |
| LLaMA 13B perplexity at 32768 (Proof-pile) | 2.35 | 2.66 (original at 2048) |
| Effective context window (7B, PI to 8192) | 8192 at 200 steps | 2560 at 10,000 steps (direct FT) |
| Effective context window (7B, PI to 32768) | 32768 at 200 steps | N/A |
| GovReport ROUGE-1 (7B, 16K context) | 60.0 | 58.7 (CoLT5 Base) / 61.3 (CoLT5 XL) |
| Original benchmarks (7B, extended to 8192) | <2% degradation | Original LLaMA 7B |

- Perplexity consistently improves with longer context windows, confirming the model genuinely leverages extended context.
- Without any fine-tuning (step 0), PI to 8192 already achieves ~16 perplexity vs >10^3 for extrapolation.
- At 200 fine-tuning steps, models already surpass original perplexity and achieve full effective context window.
- Extending to 32768 (16x) works well for 7B and 13B models with no diminishing returns on PG-19.

---

## Conclusions

1. **Interpolation over extrapolation:** The failure of RoPE at extended contexts is due to extrapolation of positional encodings, not a fundamental limitation. Interpolating position indices keeps attention scores within a stable, well-bounded regime (~600x tighter bound than extrapolation).

2. **Minimal fine-tuning:** Position Interpolation requires only ~1000 fine-tuning steps to fully adapt models to greatly extended context windows (up to 32768 from 2048), a negligible cost compared to pretraining.

3. **Effective long-context utilization:** Extended models genuinely leverage longer contexts, showing consistent perplexity improvements with increasing context window size and achieving 100% passkey retrieval across the full extended window.

4. **Preserved original capabilities:** Models extended to 8192 show less than 2% degradation on standard benchmarks within the original 2048 context window. Larger extensions show more regression but remain in reasonable ranges.

5. **Practical simplicity:** No architectural changes, no new parameters, and full compatibility with existing infrastructure and optimizations (Flash Attention, FSDP, etc.).

6. **Generality:** Results hold across model sizes from 7B to 65B and extension factors up to 16x, suggesting Position Interpolation is broadly applicable to RoPE-based LLMs.

---

## Core References and Why They Are Referenced

### Positional Encoding Foundations
- **Su et al. (2021)** -- *RoFormer: Enhanced Transformer with Rotary Position Embedding.* Introduces RoPE, the positional encoding used by LLaMA and the direct target of PI's rescaling. PI builds on RoPE's mathematical formulation (Eq. 1-2) and improves upon its extrapolation bound (Sec. 3.4.3).
- **Vaswani et al. (2017)** -- *Attention Is All You Need.* Foundational transformer paper. PI reaffirms its hypothesis that transformers can generalize to longer sequences than seen during training.

### Target Model
- **Touvron et al. (2023)** -- *LLaMA: Open and Efficient Foundation Language Models.* The family of models extended by PI. All experiments are conducted on LLaMA 7B through 65B.

### Length Extrapolation Alternatives
- **Press et al. (2022)** -- *ALiBi: Train Short, Test Long.* Alternative positional encoding enabling length extrapolation via linear attention biases. Not applicable to existing RoPE-based LLMs like LLaMA, motivating PI's different approach.
- **Sun et al. (2022)** -- *LeX: A Length-Extrapolatable Transformer.* Another extrapolation-capable architecture, similarly not retroactively applicable to pretrained RoPE models.
- **Haviv et al. (2022)** -- *Transformer Language Models Without Positional Encodings Still Learn Positional Information.* Shows NoPE transformers can learn positional information implicitly. Referenced in the context of length extrapolation research.

### Concurrent Work
- **kaiokendev (2023)** -- *SuperHOT.* Concurrent blogpost that also interpolates RoPE positional encodings, extending context from 2K to 8K. PI provides theoretical justification and scales to 65B with full fine-tuning.

### Related Interpolation Technique
- **Dosovitskiy et al. (2021)** -- *ViT: An Image is Worth 16x16 Words.* Proposed interpolating learned position embeddings for Vision Transformers at higher resolutions (up to 4x). PI extends this concept to position indices (not weights) for RoPE encodings, achieving up to 32x extension.

### Training Data and Infrastructure
- **Gao et al. (2020)** -- *The Pile.* Primary fine-tuning dataset for PI experiments.
- **Together Computer (2023)** -- *RedPajama.* Alternative fine-tuning dataset used in ablation (Section 3.4).
- **Dao et al. (2022)** -- *FlashAttention.* Used for efficient training of extended models.
- **Zhao et al. (2023)** -- *PyTorch FSDP.* Fully Sharded Data Parallel used for distributed training.

### Evaluation Benchmarks and Tasks
- **Rae et al. (2020)** -- *PG-19 / Compressive Transformers.* Book corpus used for long-sequence perplexity evaluation.
- **Azerbayev et al. (2022)** -- *Proof-pile.* Arxiv math dataset for perplexity evaluation.
- **Mohtashami & Jaggi (2023)** -- *Landmark Attention.* Provides the passkey retrieval evaluation task used to measure effective context window size.
- **Huang et al. (2021)** -- *GovReport.* Long document summarization dataset for downstream task evaluation.
- **Shaham et al. (2022)** -- *SCROLLS.* Leaderboard providing baselines for GovReport summarization comparison.

### Efficient Attention and Memory (Related Work)
- **Ainslie et al. (2023)** -- *CoLT5.* Provides summarization baselines on GovReport; PI's extended LLaMA achieves competitive ROUGE-1 scores.
- **Hu et al. (2021)** -- *LoRA.* Referenced as a parameter-efficient fine-tuning method shown by the community to also work with position interpolation.

#### Cross-References in Available Papers

- **NTK-Aware Scaled RoPE (2023-06-rope-ntk):** References PI as the "uniform interpolation method" that NTK-aware improves upon. The analysis notes that PI's blind downscaling of all position indices by 1/s loses high-frequency information, which NTK-aware's non-uniform base change preserves. PI is concurrent with NTK-aware (both June 2023) and does not reference it.
- **YaRN (2024-05-yarn-context-extension):** References PI as "[9] the baseline 'blind' interpolation method that YaRN improves upon." PI is used as a comparison target throughout (Table 1, perplexity and benchmark comparisons). YaRN achieves comparable or better results with 2.5× fewer training steps and ~0.1% of pretraining data. YaRN's core contribution is replacing PI's uniform frequency scaling with frequency-aware NTK-by-parts interpolation.
- **DroPE (2025-12-drope-dropping-positional-embeddings):** Lists PI as a "uniform frequency scaling baseline" that DroPE substantially outperforms across all zero-shot context extension tasks on RULER and LongBench benchmarks.
