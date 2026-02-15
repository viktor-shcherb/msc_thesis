# Chapter 5: Experimental Setup

Draft — 2026-02-15

## Purpose

Short "materials" chapter. Describe the concrete models, datasets, and infrastructure used to instantiate the methodology from Chapter 4. The reader should finish this chapter knowing exactly what was measured on what, and be able to reproduce the setup.

---

## 5.1 — Cross-Model Study

**~2 pages**

### Argument

We analyze 13 models spanning 3 primary families and 2 predecessor models, covering diverse architectures, scales, and long-context training strategies. This enables within-family scaling comparisons, across-family architectural comparisons, and cross-generation comparisons.

### Content

1. **Primary families (11 models).**
   - **Ministral-3** (3B/8B/14B): Mistral's latest generation. 256K claimed context. GQA. Represents the current frontier for open-weight long-context models in the small-to-medium range.
   - **Qwen-3** (0.6B/1.7B/4B/8B/14B): Five scales from the same architecture, enabling clean scaling analysis. 128K claimed context. GQA with YaRN RoPE scaling.
   - **Llama 3.2** (1B/3B/11B-Vision): Meta's latest. 128K claimed context. Includes a vision-language model (11B) with NoPE (no position encoding) layers, providing an architectural outlier. GQA.

2. **Predecessor models for cross-benchmark validation (2 models).**
   - **Llama-3.1-8B**: Previous-generation Llama with full 128K attention. Enables cross-generation comparison with Llama-3.2 and provides per-length RULER scores for direct plasticity-to-benchmark correlation.
   - **Mistral-v0.2-7B**: Predecessor of Ministral-3 with 32K sliding-window attention. Has a catastrophic RULER cliff at 64K (49.0→13.8 at 128K), providing a critical test case: does plasticity detect architectural context limits?

3. **Selection criteria.** All models have open weights (reproducibility) and 128K+ claimed context. The primary families provide multiple scales for within-family comparisons. The predecessor models provide cross-generation comparisons and RULER per-length scores at 6 bins (4K–128K).

4. **Model configuration table.**

   | Model | Params | Layers | Heads (Q/KV) | Head dim | Context | Attention | Position enc. |
   |---|---|---|---|---|---|---|---|
   | Ministral-3-3B | 3B | ... | ... | ... | 256K | Full | RoPE |
   | Ministral-3-8B | 8B | ... | ... | ... | 256K | Full | RoPE |
   | Ministral-3-14B | 14B | ... | ... | ... | 256K | Full | RoPE |
   | Qwen-3-0.6B | 0.6B | ... | ... | ... | 128K | Full | RoPE + YaRN |
   | Qwen-3-1.7B | 1.7B | ... | ... | ... | 128K | Full | RoPE + YaRN |
   | Qwen-3-4B | 4B | ... | ... | ... | 128K | Full | RoPE + YaRN |
   | Qwen-3-8B | 8B | ... | ... | ... | 128K | Full | RoPE + YaRN |
   | Qwen-3-14B | 14B | ... | ... | ... | 128K | Full | RoPE + YaRN |
   | Llama-3.2-1B | 1B | ... | ... | ... | 128K | Full | RoPE |
   | Llama-3.2-3B | 3B | ... | ... | ... | 128K | Full | RoPE |
   | Llama-3.2-11B | 11B | ... | ... | ... | 128K | Full | RoPE + NoPE |
   | Llama-3.1-8B | 8B | ... | ... | ... | 128K | Full | RoPE |
   | Mistral-v0.2-7B | 7B | ... | ... | ... | 32K | Sliding (32K) | RoPE |

   (Fill from model configs during writing. Note: Llama-11B has alternating RoPE/NoPE layers. Ministral-3 uses full attention only. Mistral-v0.2 uses sliding-window attention.)

### Transition to 5.2

> The cross-model study provides a snapshot of how different training recipes and architectures shape the Q/K geometry. To understand how this geometry develops, we trace a single model across training.

---

## 5.2 — Training Dynamics Study

**~1.5 pages**

### Argument

SmolLM3-3B provides a rare opportunity: open intermediate checkpoints spanning pre-training through long-context extension, from a model with an interesting architectural feature (NoPE layers).

### Content

1. **Why SmolLM3.** Open intermediate checkpoints are uncommon — most labs release only final weights. SmolLM3 provides:
   - 10 checkpoints across three pre-training stages + two long-context extension phases
   - Clear phase transitions (4K → 32K → 64K context)
   - NoPE (no position encoding) layer pattern
   - 3B scale — comparable to Ministral-3-3B and Llama-3.2-3B, enabling cross-model comparison at matched scale

2. **Checkpoint table.**

   | # | Phase | Checkpoint ID | Training steps | Context length | Notes |
   |---|---|---|---|---|---|
   | 1 | Pre-train stage 1 | step-040000 | 40K | 4K | Early training |
   | 2 | Pre-train stage 1 | step-1200000 | 1.2M | 4K | |
   | 3 | Pre-train stage 1 | step-2400000 | 2.4M | 4K | |
   | 4 | Pre-train stage 1 | step-3440000 | 3.44M | 4K | End of stage 1 |
   | 5 | Pre-train stage 2 | step-4200000 | 4.2M | 4K | Data mix change |
   | 6 | Pre-train stage 3 | step-4720000 | 4.72M | 4K | Annealing |
   | 7 | LC 4K→32K | step-004000 | +4K | 32K | LC onset |
   | 8 | LC 4K→32K | step-020000 | +20K | 32K | LC converged |
   | 9 | LC 32K→64K | step-004000 | +4K | 64K | Extended LC onset |
   | 10 | LC 32K→64K | step-020000 | +20K | 64K | Final checkpoint |

3. **Reproducibility notes.** Specific HuggingFace branches, config overrides (e.g., tokenizer handling for early checkpoints), dtype (bfloat16).

---

## 5.3 — Benchmarks

**~1.5 pages**

### Argument

Two complementary benchmarks validate the mechanistic metrics against behavioral performance. LongBench-Pro provides realistic task evaluation; RULER provides synthetic per-length evaluation. Together they test whether plasticity predicts performance on both content-dependent reasoning and controlled retrieval tasks.

### Content

1. **LongBench-Pro (primary benchmark).** 1,500 samples, 25 tasks, bilingual (EN/ZH), 8K–256K context, multiple-choice format. Non-thinking mode scores used (matching our capture: base model behavior, not chain-of-thought).

2. **LBP model overlap.** 7 of 13 models have exact matches: Ministral-3 3B/8B/14B, Qwen-3 4B/8B/14B, Llama-3.2-3B.

3. **Why LongBench-Pro.** Realistic tasks requiring content-dependent reasoning — not just retrieval. Our plasticity metric measures content-vs-position competition, so a benchmark that rewards content comprehension is the appropriate primary validation target.

4. **LBP per-length structure.** Samples are binned by length (8K/16K/32K/64K/128K/256K). Per-length scores available for Ministral-14B from the paper's Figure 7; other models have aggregate scores only.

5. **RULER (secondary benchmark).** 13 synthetic tasks (NIAH variants, multi-key/value/query, variable tracking, aggregation, QA), evaluated at 4K–128K. Provides per-length scores at 6 bins for standardized length-dependent evaluation.

6. **RULER model overlap.** 2 models with both RULER scores and plasticity data: Llama-3.1-8B (full attention, RULER 95.5→77.0) and Mistral-v0.2-7B (sliding window, RULER 93.6→13.8). The Mistral-v0.2 catastrophic cliff at 64K/128K provides a critical diagnostic: plasticity can measure attention flexibility within a model's attention span but cannot detect architectural range limits.

7. **Complementary roles.** LBP tests realistic content comprehension across 7 models at aggregate level. RULER tests controlled retrieval across 2 models at per-length granularity. The two benchmarks exercise different aspects of long-context capability, providing convergent validation if plasticity predicts both.

---

## 5.4 — Implementation

**~1 page**

### Content

1. **Hardware.** Single NVIDIA B200 GPU on Vast.ai. All models fit in bfloat16 within 192GB VRAM.

2. **Capture parameters.**
   - dtype: bfloat16 (matching model training precision)
   - Position sampling: uniform bucket sampling, min_bucket_size=8192
   - Head sampling: 300 query heads per model (uniform random without replacement; full set if model has ≤300)
   - Full attention heads only (not GQA key-sharing heads)

3. **Analysis pipeline.** Three analyses (PCA, Rotation, Plasticity) applied to the same captured vectors. Each produces per-head metrics aggregated into model-level summaries. All code in the project repository.

4. **Computational cost.** Capture: ~X GPU-hours per model. Analysis: ~Y CPU-hours total. (Fill during writing.)

---

## Appendix A candidates from Chapter 5

- Full model configuration details (exact layer counts, head counts, head dimensions, GQA group sizes, RoPE parameters).
- SmolLM3 checkpoint config overrides and tokenizer handling.
- LongBench-Pro task list and sample counts per length bin.
