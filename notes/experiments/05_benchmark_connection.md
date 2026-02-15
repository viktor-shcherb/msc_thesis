# Connecting Mechanistic Metrics to Benchmark Performance

## Benchmark: LongBench Pro (2026-01)

1,500 samples, 25 tasks, bilingual EN/ZH, 8K-256K, multiple-choice format.
Source: `references/2026-01-longbench-pro/`.

### Model Overlap

| Sniffed Model | LongBench Pro Model | Match |
|---|---|---|
| qwen3-4b | Qwen3-4B (Mixed, 128k) | exact |
| qwen3-8b | Qwen3-8B (Mixed, 128k) | exact |
| qwen3-14b | Qwen3-14B (Mixed, 128k) | exact |
| ministral3-3b | Ministral-3-3B-Instruct-2512 (Instruct, 256k) | exact |
| ministral3-8b | Ministral-3-8B-Instruct-2512 (Instruct, 256k) | exact |
| ministral3-14b | Ministral-3-14B-Instruct-2512 (Instruct, 256k) | exact |
| llama3.2-3b | Llama-3.2-3B-Instruct (Instruct, 128k) | exact |
| qwen3-0.6b | — | not in benchmark |
| qwen3-1.7b | — | not in benchmark |
| llama3.2-1b | — | not in benchmark |
| llama3.2-11b | — | not in benchmark (vision) |

7 of 11 sniffed models have exact matches in LongBench Pro.

---

## Table 1: Aggregate Scores and Mechanistic Metrics

LongBench Pro Overall from Table 3 (non-thinking). Rotation metrics from `qk-rotation/results/rotation/rotated.csv`. Plasticity from `attention-plasticity/results/attention-plasticity/model_report.csv` (2026-02-15 run).

| Model | LBP Overall | bias_strength | |r_k_a| | |r_q_a| | plane var | plasticity | ap_first_20% | ap_last_20% | ap_drop |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ministral3-14b | 40.14 | 3.00e-4 | 0.743 | 0.782 | 0.365 | 0.6145 | 0.6551 | 0.5870 | 0.068 |
| ministral3-8b | 37.80 | 3.00e-4 | 0.834 | 0.860 | 0.340 | 0.6081 | 0.6535 | 0.5713 | 0.082 |
| qwen3-14b | 37.11 | 8.00e-4 | 0.882 | 0.750 | 0.295 | 0.5902 | 0.6803 | 0.5188 | 0.161 |
| qwen3-8b | 33.41 | 9.00e-4 | 0.895 | 0.754 | 0.317 | 0.5965 | 0.6941 | 0.5166 | 0.178 |
| qwen3-4b | 31.26 | 1.00e-3 | 0.894 | 0.750 | 0.327 | 0.5943 | 0.6985 | 0.5122 | 0.186 |
| ministral3-3b | 30.18 | 3.00e-4 | 0.813 | 0.855 | 0.368 | 0.6224 | 0.6638 | 0.5917 | 0.072 |
| llama3.2-3b | 15.71 | 6.00e-4 | 0.898 | 0.814 | 0.433 | 0.5646 | 0.6860 | 0.4563 | 0.230 |

Notes:
- bias_strength = μ_Q^a · α_K (rotation analysis, mean across heads).
- plasticity = ap_overall from model_report.csv.
- ap_drop = ap_first_20pct - ap_last_20pct (larger = steeper degradation with position).

### All models with mechanistic data (including those not in LBP)

From model_report.csv, sorted by ap_overall descending:

| Model | LBP Overall | RULER 128K | plasticity | ap_first_20% | ap_last_20% | ap_drop | bias_strength |
|---|---:|---:|---:|---:|---:|---:|---:|
| mistral-v0.2-7b | — | 13.8 | 0.6449* | 0.6830* | 0.6196* | 0.063* | 1.57e-3 |
| ministral3-3b | 30.18 | — | 0.6224 | 0.6638 | 0.5917 | 0.072 | 3.00e-4 |
| qwen3-1.7b | — | — | 0.6155 | 0.7017 | 0.5392 | 0.162 | 1.30e-3 |
| ministral3-14b | 40.14 | — | 0.6145 | 0.6551 | 0.5870 | 0.068 | 3.00e-4 |
| ministral3-8b | 37.80 | — | 0.6081 | 0.6535 | 0.5713 | 0.082 | 3.00e-4 |
| qwen3-0.6b | — | — | 0.6045 | 0.6943 | 0.5261 | 0.168 | 1.40e-3 |
| llama3.2-1b | — | — | 0.6018 | 0.7023 | 0.4868 | 0.216 | 6.00e-4 |
| qwen3-8b | 33.41 | — | 0.5965 | 0.6941 | 0.5166 | 0.178 | 9.00e-4 |
| qwen3-4b | 31.26 | — | 0.5943 | 0.6985 | 0.5122 | 0.186 | 1.00e-3 |
| qwen3-14b | 37.11 | — | 0.5902 | 0.6803 | 0.5188 | 0.161 | 8.00e-4 |
| llama3.2-11b | — | — | 0.5665 | 0.6578 | 0.4886 | 0.169 | 7.00e-4 |
| llama3.2-3b | 15.71 | — | 0.5646 | 0.6860 | 0.4563 | 0.230 | 6.00e-4 |
| llama3.1-8b | — | 77.0 | 0.5386 | 0.6310 | 0.4727 | 0.158 | 7.83e-4 |

*Mistral-v0.2-7B: plasticity computed over ~32K sliding window only, not comparable to 128K-range models.

---

## Table 2: Per-Length-Bin Plasticity Profile

Plasticity aggregated by position range using `bucket_position` from `head_bucket_plasticity.csv`.

| Model | 0–8K | 8K–16K | 16K–32K | 32K–64K | 64K–128K | total drop |
|---|---:|---:|---:|---:|---:|---:|
| qwen3-4b | 0.7460 | 0.7084 | 0.6672 | 0.6159 | 0.5346 | -0.211 |
| qwen3-8b | 0.7411 | 0.7027 | 0.6644 | 0.6180 | 0.5397 | -0.201 |
| qwen3-14b | 0.7250 | 0.6918 | 0.6494 | 0.6045 | 0.5405 | -0.184 |
| ministral3-3b | 0.6887 | 0.6684 | 0.6490 | 0.6268 | 0.6017 | -0.087 |
| ministral3-8b | 0.6793 | 0.6579 | 0.6394 | 0.6163 | 0.5832 | -0.096 |
| ministral3-14b | 0.6840 | 0.6597 | 0.6391 | 0.6154 | 0.5957 | -0.088 |
| llama3.2-3b | 0.7339 | 0.6926 | 0.6596 | 0.6023 | 0.4882 | -0.246 |

Notes:
- Total drop = (64K–128K) - (0–8K).
- Llama-3.2-3B has the steepest decline: 0.734 → 0.488 (-0.246).
- Ministral family is uniformly flatter than Qwen3 and Llama (-0.087 to -0.096 vs -0.184 to -0.246).
- Qwen3 models are remarkably similar across scales (4B/8B/14B differ by <0.02 at each bin).

---

## Table 3: Per-Length LongBench Pro Scores

### Ministral-3-14B-Instruct-2512 (from Figure 7, thinking mode)

| Length | LBP Score | Plasticity (matched bin) |
|---:|---:|---:|
| 8K | 51.88 | 0.6840 |
| 16K | 48.52 | 0.6597 |
| 32K | 48.75 | 0.6391 |
| 64K | 45.70 | 0.6154 |
| 128K | 42.36 | 0.5957 |
| 256K | 37.59 | — |

### Other models (per-length LBP scores not in Figure 7)

| Model | 8K | 16K | 32K | 64K | 128K | 256K |
|---|---:|---:|---:|---:|---:|---:|
| qwen3-4b | `ext` | `ext` | `ext` | `ext` | `ext` | `ext` |
| qwen3-8b | `ext` | `ext` | `ext` | `ext` | `ext` | `ext` |
| qwen3-14b | `ext` | `ext` | `ext` | `ext` | `ext` | `ext` |
| ministral3-3b | `ext` | `ext` | `ext` | `ext` | `ext` | `ext` |
| ministral3-8b | `ext` | `ext` | `ext` | `ext` | `ext` | `ext` |
| llama3.2-3b | `ext` | `ext` | `ext` | `ext` | `ext` | `ext` |

`ext` = only remaining gap.

### Reference models from Figure 7 (not sniffed, for calibration)

| Model | 8K | 16K | 32K | 64K | 128K | 256K |
|---|---:|---:|---:|---:|---:|---:|
| Gemini-2.5-Pro | 74.50 | 74.79 | 75.31 | 74.18 | 70.00 | 71.77 |
| GPT-5 | 75.37 | 76.27 | 74.34 | 76.46 | 69.36 | 63.82 |
| Claude-4-Sonnet | 72.73 | 71.48 | 72.82 | 70.52 | 66.43 | 65.26 |
| DeepSeek-V3.2 | 75.54 | 74.49 | 69.53 | 69.47 | 64.77 | 53.12 |
| Qwen3-235B-A22B-Thk | 72.06 | 70.43 | 69.69 | 66.85 | 64.05 | 58.77 |
| GLM-4.6 | 71.23 | 66.04 | 63.53 | 58.97 | 47.55 | 41.95 |
| Kimi-K2-Instruct | 59.79 | 58.17 | 58.73 | 53.61 | 52.29 | 50.61 |
| MiniMax-M2 | 65.48 | 58.32 | 58.31 | 52.02 | 50.61 | 34.51 |
| Llama-3.1-405B | 52.38 | 51.80 | 46.41 | 41.82 | 26.01 | 25.54 |

---

## Table 4: Decile Plasticity Profile

From model_report.csv. Position ranges split into 10 equal bins across the context window.

| Model | 0–10% | 10–20% | 20–30% | 30–40% | 40–50% | 50–60% | 60–70% | 70–80% | 80–90% | 90–100% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ministral3-3b | 0.676 | 0.651 | 0.638 | 0.628 | 0.618 | 0.612 | 0.609 | 0.603 | 0.595 | 0.588 |
| ministral3-8b | 0.666 | 0.641 | 0.630 | 0.617 | 0.607 | 0.596 | 0.592 | 0.584 | 0.574 | 0.568 |
| ministral3-14b | 0.669 | 0.641 | 0.627 | 0.612 | 0.612 | 0.601 | 0.600 | 0.603 | 0.597 | 0.577 |
| qwen3-0.6b | 0.726 | 0.663 | 0.636 | 0.619 | 0.600 | 0.584 | 0.574 | 0.560 | 0.541 | 0.511 |
| qwen3-1.7b | 0.729 | 0.674 | 0.648 | 0.631 | 0.612 | 0.594 | 0.585 | 0.573 | 0.554 | 0.525 |
| qwen3-4b | 0.724 | 0.673 | 0.636 | 0.620 | 0.596 | 0.565 | 0.545 | 0.534 | 0.521 | 0.503 |
| qwen3-8b | 0.718 | 0.670 | 0.638 | 0.622 | 0.598 | 0.571 | 0.551 | 0.539 | 0.526 | 0.507 |
| qwen3-14b | 0.705 | 0.655 | 0.624 | 0.606 | 0.586 | 0.565 | 0.552 | 0.543 | 0.532 | 0.506 |
| llama3.2-1b | 0.731 | 0.674 | 0.649 | 0.656 | 0.652 | 0.610 | 0.549 | 0.505 | 0.489 | 0.484 |
| llama3.2-3b | 0.710 | 0.662 | 0.642 | 0.599 | 0.582 | 0.540 | 0.504 | 0.474 | 0.458 | 0.454 |
| llama3.2-11b | 0.676 | 0.639 | 0.604 | 0.569 | 0.532 | 0.535 | 0.553 | 0.560 | 0.517 | 0.460 |
| llama3.1-8b | 0.654 | 0.608 | 0.566 | 0.530 | 0.499 | 0.506 | 0.526 | 0.537 | 0.500 | 0.445 |
| mistral-v0.2-7b* | 0.695 | 0.671 | 0.661 | 0.651 | 0.641 | 0.633 | 0.627 | 0.628 | 0.627 | 0.612 |

*Mistral-v0.2-7B deciles computed over ~32K window only.

Key patterns:
- **Ministral3**: gradual, near-linear decline. Flattest profiles of all families.
- **Qwen3**: steeper decline, accelerating in the second half. Larger models slightly flatter.
- **Llama3.2**: steepest decline overall. Llama-3.2-3B drops from 0.710 to 0.454 (-0.256).
- **Llama-3.2-11b**: anomalous non-monotone profile — dips at 40–50%, recovers at 60–80%, then collapses at 90–100%. Possibly related to NoPE layers or vision-encoder interaction.
- **Llama-3.1-8B**: same non-monotone pattern as Llama-3.2-11B — dips at 40–50% (0.499), recovers at 70–80% (0.537), collapses at 90–100% (0.445). This pattern is now confirmed as a **Llama-family trait**, not 3.2-11B-specific.
- **Mistral-v0.2-7B**: flattest profile of all models (0.695→0.612), but only spans ~32K (sliding window). Not comparable to 128K-range deciles.

---

## Observations

### Aggregate plasticity does NOT predict LBP Overall across families

| Model | LBP Overall | Plasticity |
|---|---:|---:|
| ministral3-14b | **40.14** | 0.615 |
| ministral3-8b | **37.80** | 0.608 |
| qwen3-14b | **37.11** | 0.590 |
| qwen3-8b | **33.41** | 0.597 |
| qwen3-4b | **31.26** | 0.594 |
| ministral3-3b | **30.18** | 0.622 |
| llama3.2-3b | **15.71** | 0.565 |

Ministral3-3b has the highest plasticity (0.622) but scores only 30.18. Cross-family comparison is confounded by architecture, training data, tokenizer, instruction tuning quality.

### ap_last_20% separates families better

| Model | LBP Overall | ap_last_20% |
|---|---:|---:|
| ministral3-14b | **40.14** | 0.587 |
| ministral3-8b | **37.80** | 0.571 |
| qwen3-14b | **37.11** | 0.519 |
| qwen3-8b | **33.41** | 0.517 |
| qwen3-4b | **31.26** | 0.512 |
| ministral3-3b | **30.18** | 0.592 |
| llama3.2-3b | **15.71** | 0.456 |

The last-20% plasticity ranks Llama-3.2-3B (0.456) clearly last, matching its LBP position. Ministral3 maintains ~0.57-0.59 at distant positions, Qwen3 drops to ~0.51-0.52.

### ap_drop (plasticity degradation) is the most informative signal

| Model | LBP Overall | ap_drop | Family |
|---|---:|---:|---|
| ministral3-14b | **40.14** | 0.068 | Ministral |
| ministral3-8b | **37.80** | 0.082 | Ministral |
| qwen3-14b | **37.11** | 0.161 | Qwen |
| qwen3-8b | **33.41** | 0.178 | Qwen |
| qwen3-4b | **31.26** | 0.186 | Qwen |
| ministral3-3b | **30.18** | 0.072 | Ministral |
| llama3.2-3b | **15.71** | 0.230 | Llama |

Within each family, ap_drop correlates inversely with LBP:
- **Ministral3**: 14B (0.068) > 8B (0.082) > 3B (0.072) — nearly flat, and 3B is anomalously low-drop.
- **Qwen3**: 14B (0.161) > 8B (0.178) > 4B (0.186) — monotone, larger models degrade less.
- **Llama3.2-3B**: 0.230 — steepest drop, worst LBP score.

Across families, ap_drop separates Ministral (~0.07) from Qwen (~0.17) from Llama (0.23), matching the LBP ordering. Ministral3-3b is the exception: low drop (0.072) but low LBP (30.18) — suggesting base capability (not context degradation) is the bottleneck at small scale.

---

## SmolLM3-3B Training Dynamics: Bias Collapse vs Plasticity

10 checkpoints spanning pre-training (4K context) → long-context extension (4K→32K→64K).
Rotation metrics from `qk-rotation/results/smollm3_training_progress/rotated.csv`.
Plasticity from `attention-plasticity/results/attention-plasticity/smollm3_model_report.csv`.

### Table 5: Joint Rotation + Plasticity Trajectory

| Phase | Checkpoint | bias_str | |α_K| | |r_k_a| | sep_str | plane_var | ap_overall | ap_first_20% | ap_last_20% | ap_drop |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Pre-train | stage1 40K | 0.0092 | 3.19e-3 | 0.861 | 0.233 | 0.237 | 0.585 | 0.609 | 0.569 | 0.040 |
| Pre-train | stage1 1.2M | 0.0160 | 3.23e-3 | 0.886 | 0.299 | 0.333 | 0.542 | 0.579 | 0.516 | 0.062 |
| Pre-train | stage1 2.4M | 0.0165 | 3.32e-3 | 0.893 | 0.301 | 0.335 | 0.545 | 0.582 | 0.521 | 0.061 |
| Pre-train | stage1 3.44M | 0.0166 | 3.34e-3 | 0.894 | 0.302 | 0.334 | 0.545 | 0.579 | 0.522 | 0.057 |
| Pre-train | stage2 4.2M | 0.0168 | 3.33e-3 | 0.893 | 0.297 | 0.334 | 0.548 | 0.585 | 0.523 | 0.062 |
| Anneal | stage3 4.72M | 0.0194 | 4.08e-3 | 0.918 | 0.317 | 0.344 | 0.516 | 0.552 | 0.494 | 0.058 |
| LC 4K→32K | step 4K | 0.0032 | 5.01e-4 | 0.911 | 0.348 | 0.382 | 0.507 | 0.585 | 0.432 | 0.153 |
| LC 4K→32K | step 20K | 0.0032 | 5.07e-4 | 0.913 | 0.347 | 0.380 | 0.507 | 0.582 | 0.437 | 0.147 |
| LC 32K→64K | step 4K | 0.0018 | 2.68e-4 | 0.906 | 0.347 | 0.388 | 0.502 | 0.590 | 0.422 | 0.168 |
| LC 32K→64K | step 20K | 0.0018 | 2.69e-4 | 0.905 | 0.347 | 0.387 | 0.503 | 0.588 | 0.427 | 0.161 |

### Table 6: Per-Position Plasticity During Pre-Training (4K context)

| Checkpoint | 0–256 | 256–512 | 512–1K | 1K–1.5K | 1.5K–2K | 2K–2.5K | 2.5K–3K | 3K–3.5K | 3.5K–4K |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| stage1 40K | 0.619 | 0.610 | 0.604 | 0.594 | 0.583 | 0.574 | 0.574 | 0.576 | 0.565 |
| stage1 1.2M | 0.593 | 0.586 | 0.566 | 0.553 | 0.544 | 0.529 | 0.526 | 0.527 | 0.510 |
| stage2 4.2M | 0.601 | 0.592 | 0.572 | 0.557 | 0.548 | 0.533 | 0.532 | 0.535 | 0.516 |
| stage3 4.72M | 0.571 | 0.558 | 0.539 | 0.524 | 0.516 | 0.501 | 0.500 | 0.504 | 0.488 |

### Table 7: Per-Position Plasticity During Long-Context Extension

| Checkpoint | 0–1K | 1K–2K | 2K–4K | 4K–8K | 8K–16K | 16K–32K | 32K–48K | 48K–64K |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| lc 4K→32K 4K | 0.651 | 0.629 | 0.598 | 0.556 | 0.525 | 0.464 | — | — |
| lc 4K→32K 20K | 0.657 | 0.626 | 0.594 | 0.553 | 0.524 | 0.467 | — | — |
| lc 32K→64K 4K | — | 0.676 | 0.641 | 0.600 | 0.560 | 0.526 | 0.479 | 0.426 |
| lc 32K→64K 20K | — | 0.679 | 0.639 | 0.598 | 0.557 | 0.526 | 0.480 | 0.430 |

### Interpretation: Bias Collapse Is Necessary but Not Sufficient

Three training phases with distinct plasticity signatures:

**Phase 1 — Pre-training (40K → 4.72M steps, 4K context)**
- bias_strength doubles (0.009 → 0.019), driven by α_K growth
- ap_overall drops uniformly (0.585 → 0.516)
- ap_drop is mild (~0.04–0.06) within the 4K window
- Growing positional bias reduces plasticity globally but the short context limits gradient steepening

**Phase 2 — LC extension onset (4K→32K, first 4K steps)**
- bias_strength collapses 6× (0.019 → 0.003): α_K drops 8× while |r_k_a| is preserved
- ap_first_20% **recovers** from 0.552 → 0.585 (back to stage1 levels)
- ap_last_20% **plummets** to 0.432
- ap_drop **triples** (0.058 → 0.153)
- separation_strength and plane_var_fraction both jump (+10%, +11%)

**Phase 3 — LC extension continued (32K→64K)**
- bias_strength halves again (0.003 → 0.002)
- ap_first_20% holds at 0.588–0.590
- ap_last_20% drops further to 0.422–0.427
- ap_drop reaches 0.161–0.168

The critical finding: **bias reduction recovers near-position plasticity but cannot ensure distant-position plasticity.** After a 10× bias collapse, attention at 0–2K positions is as flexible as early training — but at 48K–64K positions, plasticity is 0.43, far below the 0.57 the model achieved at 3.5K–4K during pre-training at the same bias level.

What fills the gap between bias_strength and distant-position plasticity? Two candidates:
1. **Content signal decay**: at 48K–64K, the content component of q^T(k₁ − k₂) may have lower variance, so even minimal positional bias dominates
2. **RoPE rotation accumulation**: the symmetric rotation planes in the complement create relative-position structure that increasingly decorrelates distant keys from the query, independent of asymmetric drift

### Connection to Cross-Model Observations

SmolLM3 at end of LC training (ap_drop ≈ 0.16) is comparable to Qwen3 models (0.16–0.19). This matches: both are 3B-class models with standard LC fine-tuning. The Ministral3 family achieves ap_drop ≈ 0.07 — whatever Ministral3's training recipe does differently, it goes beyond what standard bias collapse achieves.

| Model/Checkpoint | ap_drop | bias_strength | Context trained |
|---|---:|---:|---|
| Ministral3-3B | 0.072 | 3.0e-4 | 256K |
| SmolLM3-3B (lc 32K→64K) | 0.161 | 1.8e-3 | 64K |
| Qwen3-1.7B | 0.162 | 1.3e-3 | 128K |
| Llama-3.2-3B | 0.230 | 6.0e-4 | 128K |

Ministral3 has comparable bias_strength to SmolLM3's post-LC level but achieves 2× flatter plasticity over 2× longer context. The low ap_drop is not explained by bias alone — Ministral3's training produces attention heads whose content signal maintains competitive strength at distance.

---

## Visual Analysis: 2D Heatmaps and Per-Head Profiles

### Bucket Heatmaps: Plasticity Is a Function of Two Distances

The `bucket_heatmap.png` plots reveal that plasticity depends on **both** inter-key distance (x-axis: how far apart the two competing keys are) and key-to-query distance (y-axis: how far both keys are from the query). The 1D position profiles in Tables 2/4 collapse over the inter-key axis and lose this structure.

The geometry of the competition:
- **Top-left** (keys close together, far from query): content always wins → high plasticity regardless of absolute distance
- **Bottom-right** (keys far apart, close to query): positional bias strongly favors the nearer key → low plasticity
- The transition between these regimes is where families diverge

**Ministral3** (3B, 8B, 14B): Strikingly uniform. The warm (>0.55) region fills nearly the entire triangle. The dark corner is confined to extreme inter-key distances (>90K) at moderate key-to-query distances. Even at 80K inter-key separation, plasticity stays above 0.5 for most key-to-query distances. The 3B, 8B, and 14B heatmaps are nearly identical in structure.

**Qwen3** (0.6B, 4B, 8B, 14B): Clear diagonal gradient from warm top-left to dark bottom-right. The dark region (plasticity <0.4) starts at ~50K inter-key distance. Remarkably, the pattern is nearly identical across model scales — Qwen3-0.6B and Qwen3-14B have the same 2D shape, just shifted slightly in absolute values. The architecture determines the geometry; scale adjusts the level.

**Llama 3.2** (1B, 3B): Similar diagonal pattern to Qwen3 but the dark zone starts earlier (~40K inter-key distance) and reaches lower values (<0.2 in the extreme corner). Llama-3.2-3B has the most extreme contrast of any model.

**Llama 3.2-11B**: Uniquely non-smooth. Dark patches appear at specific distance combinations (~16K, ~25K inter-key) rather than forming a clean diagonal gradient. A bright recovery zone appears around key-to-query distances 57K–65K. This matches the anomalous non-monotone decile profile (Table 4) and may reflect NoPE (no position encoding) layer interference at characteristic distance scales.

### Per-Head Plasticity Profiles

The `plasticity.png` line plots show per-head traces (gray) with mean (red):

**Ministral3-3B**: Tight gray bundle. Low inter-head variance. Nearly all heads decline gently and uniformly. Few outlier heads — the architecture produces homogeneous attention behavior.

**Qwen3-4B**: Wider gray spread. Bimodal distribution visible — a bundle of highly plastic heads near 0.8–1.0 and a bundle of position-locked heads near 0.2–0.3, with the mean threading between them. Content heads and position heads coexist.

**Llama-3.2-3B**: Wide spread that **converges at distance** — at 120K+, all heads cluster near 0.45, erasing individual differences. Position bias eventually dominates every head.

**Llama-3.2-11B**: The red mean line shows the non-monotone bump clearly: dip around 30K–50K, recovery to ~0.55 around 70K–100K, then collapse at 120K+. Distinctive among all models.

### Component Weights: RoPE Dimension Structure

The `component_weights.png` plots show share of positional information per embedding dimension. All models exhibit the same bimodal structure: two clusters of position-encoding dimensions (roughly indices 33–70 and 100–128) separated by a dead zone (indices 0–33 and 73–100) carrying zero positional information. This directly reflects RoPE's rotation structure.

Differences between families:
- **Ministral3**: Sharp, narrow peaks — positional information concentrated in fewer dimensions
- **Qwen3**: Broader peaks (especially first cluster spans ~40–53), more distributed positional encoding
- **Llama**: Intermediate between Ministral and Qwen

The dead-zone dimensions (0–33, 73–100) are pure content dimensions — they contribute zero to position encoding and carry only semantic signal. This connects to the rotation analysis: the complement of the {a,b} plane contains both RoPE rotation planes and these content-only dimensions.

---

## Hypotheses

**H1 (nuanced): ap_drop predicts LBP ordering better than ap_overall.**
Across families: ap_drop separates Ministral < Qwen < Llama, matching LBP ordering.
Within families: holds for Qwen3, ambiguous for Ministral3 (3B is an outlier).

**H2 (supported): ap_last_20% tracks with LBP more than ap_overall.**
Llama-3.2-3B: 0.456 (last) maps to 15.71 (last). Ministral: 0.57-0.59 maps to 37-40.

**H3 (testable with per-length LBP): Per-position plasticity predicts per-length LBP.**
The key test: does the relative ordering of models at each length bin match plasticity at corresponding positions? For Ministral-14b, plasticity is flat while LBP still drops 51.88 → 37.59 — length-independent difficulty explains some of the LBP decline. The interesting question is whether models with steeper plasticity decline show steeper *relative* LBP decline.

**H4 (supported by SmolLM3): Bias reduction is necessary but not sufficient for flat plasticity.**
SmolLM3 training dynamics show: 10× bias_strength collapse recovers near-position plasticity (first_20%: 0.552 → 0.588) but distant-position plasticity remains poor (last_20%: 0.427). ap_drop triples from 0.06 to 0.16 despite bias collapsing. Ministral3 achieves ap_drop 0.07 at comparable bias levels — something beyond bias reduction is required.

**H5: Ministral3-3B is capability-bottlenecked, not context-bottlenecked.**
Its plasticity profile is flat (ap_drop=0.072, comparable to 14B) but its LBP is low (30.18). This model has good attention mechanics but insufficient base capability. This distinction — context degradation vs base capability — is exactly what plasticity can diagnose.

**H6 (from SmolLM3): ap_drop decomposes into a bias component and a content-decay component.**
During pre-training (4K context): ap_drop ≈ 0.06, driven by growing bias_strength.
After LC training (64K context): ap_drop ≈ 0.16, despite 10× lower bias. The excess drop (0.16 − 0.06 = 0.10) reflects content signal decay at distance — the content component of q^T(k₁ − k₂) loses variance at distant positions, independent of positional bias. Models with low ap_drop (Ministral3) have somehow maintained content signal strength at distance.

**H7 (from RULER): Plasticity measures degradation, not truncation.**
Mistral-v0.2-7B has the best within-window plasticity (0.645, ap_drop 0.063) of all 13 models yet catastrophically fails on RULER at 64K/128K. Its failure is architectural (sliding window capped at 32K), not a gradual attention flexibility loss. Plasticity cannot detect this failure mode — it only measures what happens within the model's effective attention span. Two distinct failure modes exist: **context degradation** (plasticity-detectable, gradual) vs **context truncation** (architecture-level, hard cutoff).

**H8 (from RULER + NoPE study): Llama-family models share a non-monotone plasticity signature at 32+ layers.**
Llama-3.1-8B (dip at 40–50%, recovery at 70–80%, collapse at 90–100%) matches Llama-3.2-11B's pattern. NoPE (cross-attention) layers ruled out as cause — Llama-3.1-8B has zero NoPE layers but identical pattern. Recovery is distributed across nearly all self-attention layers (29/32 in 3.1-8B, 26/32 in 3.2-11B), not localized. Absent in smaller Llama models (1B/16L, 3B/28L) and all Ministral/Qwen models regardless of depth (Ministral3-14B has 40 layers, no recovery). The feature is specific to Llama architecture at ≥32 layers. See `notes/experiments/06_nope_layer_study.md`.

---

## Benchmark: RULER (2024-10)

13 synthetic tasks (NIAH variants, multi-key, multi-value, multi-query, variable tracking, aggregation, QA), evaluated at 4K–128K for 17 models.
Source: `references/2024-10-ruler-context-size/`.

### New Models

Two models sniffed and analyzed to connect with RULER's per-length scores:

| Model | Params | Window | RULER 4K→128K | ap_overall | ap_drop | bias_strength |
|---|---|---|---|---:|---:|---:|
| **Llama-3.1-8B** | 8B | 128K (full) | 95.5 → 77.0 | 0.539 | 0.158 | 7.83e-4 |
| **Mistral-v0.2-7B** | 7B | 32K (sliding) | 93.6 → 13.8 | 0.645 | 0.063 | 1.57e-3 |

### Table 8: RULER Score vs Per-Position Plasticity

Plasticity binned at positions matching RULER evaluation lengths.

| Model | Metric | 4K | 8K | 16K | 32K | 64K | 128K |
|---|---|---:|---:|---:|---:|---:|---:|
| Llama-3.1-8B | RULER | 95.5 | 93.8 | 91.6 | 87.2 | 84.7 | 77.0 |
| | Plasticity | 0.729 | 0.677 | 0.635 | 0.601 | 0.530 | 0.506 |
| Mistral-v0.2-7B | RULER | 93.6 | 91.2 | 87.2 | 75.4 | 49.0 | 13.8 |
| | Plasticity | 0.700 | 0.686 | 0.655 | 0.627 | — | — |

Notes:
- Mistral-v0.2-7B has no plasticity data beyond 32K due to sliding window attention (window size ~32K). Positions beyond the window are architecturally unreachable.
- Llama-3.1-8B has full 128K coverage.

### Table 9: Rotation Metrics for RULER Models

| Model | bias_strength | |α_K| | |r_k_a| | |r_q_a| | sep_str | plane_var |
|---|---:|---:|---:|---:|---:|---:|
| Llama-3.1-8B | 7.83e-4 | 1.67e-4 | 0.843 | 0.704 | 0.370 | 0.369 |
| Mistral-v0.2-7B | 1.57e-3 | 3.69e-4 | 0.855 | 0.719 | 0.475 | 0.410 |

### Table 10: Decile Plasticity Profiles

| Model | 0–10% | 10–20% | 20–30% | 30–40% | 40–50% | 50–60% | 60–70% | 70–80% | 80–90% | 90–100% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Llama-3.1-8B | 0.654 | 0.608 | 0.566 | 0.530 | 0.499 | 0.506 | 0.526 | 0.537 | 0.500 | 0.445 |
| Mistral-v0.2-7B | 0.695 | 0.671 | 0.661 | 0.651 | 0.641 | 0.633 | 0.627 | 0.628 | 0.627 | 0.612 |

### Analysis

#### Mistral-v0.2-7B: Sliding Window Exposes a Plasticity Blind Spot

Mistral-v0.2-7B has the **lowest ap_drop** (0.063) and **highest ap_overall** (0.645) of all 13 models — yet it catastrophically fails on RULER at 64K (49.0) and 128K (13.8). The paradox resolves immediately: its sliding window attention caps at ~32K tokens, so plasticity is measured only within that window (positions 3.5K–31.6K). Within the window, attention IS flexible. The RULER failure is architectural — the model physically cannot attend to tokens beyond its window. Needles placed at the start of a 128K context are unreachable.

This is a fundamental **limitation of attention plasticity as a metric**: it measures flexibility of attention within the model's attention span, but cannot capture architectural range constraints. A model can have perfect within-window plasticity and still fail at long context if the window is too short.

**Implication for the thesis**: plasticity predicts context degradation (gradual ECL loss) but not context truncation (hard window cutoff). These are distinct failure modes. Mistral-v0.2-7B fails by truncation; Llama/Qwen models fail by degradation.

#### Llama-3.1-8B: Graceful Decline with Non-Monotone Profile

Llama-3.1-8B shows a steady RULER decline (95.5 → 77.0, effective length ~32K by RULER's criterion) alongside steady plasticity decline (0.729 → 0.506). Both metrics degrade monotonically at the bin level, though RULER is shallower (-19%) than plasticity (-31%).

The decile profile reveals a **non-monotone bump**: plasticity dips to 0.499 at 40–50%, recovers to 0.537 at 70–80%, then collapses to 0.445 at 90–100%. This is the same pattern seen in Llama-3.2-11B (dip at 30–50%, recovery at 60–80%, collapse at 90–100%). The pattern appears to be a Llama-family trait, possibly related to NoPE layers or RoPE base frequency choices that create characteristic interference at specific distance scales.

The 2D heatmap confirms: a warm band at key-to-query distance ~49K–65K corresponds to the recovery zone, with a dark zone at short key-to-query distances for large inter-key separations (same as Llama-3.2-3B but more nuanced).

#### Llama-3.1-8B vs Llama-3.2-3B: Generational Comparison

| Metric | Llama-3.1-8B | Llama-3.2-3B |
|---|---:|---:|
| ap_overall | 0.539 | 0.565 |
| ap_drop | 0.158 | 0.230 |
| ap_last_20% | 0.473 | 0.456 |
| bias_strength | 7.83e-4 | 6.00e-4 |
| RULER 128K | 77.0 | — |
| LBP Overall | — | 15.71 |

Llama-3.1-8B has lower ap_drop (0.158 vs 0.230) and slightly higher ap_last_20% (0.473 vs 0.456) than Llama-3.2-3B. This matches its better long-context performance on RULER. The 3.1 generation maintains more plasticity at distance than the 3.2 generation, despite 3.2 being newer — possibly reflecting different LC training strategies or the 8B vs 3B parameter difference.

Both share the distinctive Llama convergence pattern where per-head differences narrow at distance, but Llama-3.1-8B retains more heterogeneity at 128K (not all heads collapse to the same value).

#### Mistral-v0.2-7B vs Ministral3: Predecessor Comparison

| Metric | Mistral-v0.2-7B | Ministral3-3B | Ministral3-8B | Ministral3-14B |
|---|---:|---:|---:|---:|
| ap_overall | 0.645* | 0.622 | 0.608 | 0.615 |
| ap_drop | 0.063* | 0.072 | 0.082 | 0.068 |
| bias_strength | 1.57e-3 | 3.00e-4 | 3.00e-4 | 3.00e-4 |
| plane_var | 0.410 | 0.368 | 0.340 | 0.365 |

*Mistral-v0.2-7B metrics computed over ~32K window only.

Mistral-v0.2-7B has **5× higher bias_strength** (1.57e-3 vs 3.0e-4) and higher plane_var_fraction (0.410 vs ~0.36) than the Ministral3 family, yet its within-window plasticity is higher. The short window means the bias term never grows large enough to dominate. Ministral3's bias is lower in absolute terms, but it maintains that low bias over a 256K window — a much harder achievement.

#### Per-Length Correlation: Llama-3.1-8B

For Llama-3.1-8B (the only RULER model with full-range plasticity data), per-position correlation between RULER score and plasticity:

| RULER Length | RULER Score | Plasticity | RULER Δ from 4K | Plasticity Δ from 4K |
|---:|---:|---:|---:|---:|
| 4K | 95.5 | 0.729 | — | — |
| 8K | 93.8 | 0.677 | -1.8% | -7.1% |
| 16K | 91.6 | 0.635 | -4.1% | -12.9% |
| 32K | 87.2 | 0.601 | -8.7% | -17.6% |
| 64K | 84.7 | 0.530 | -11.3% | -27.3% |
| 128K | 77.0 | 0.506 | -19.4% | -30.6% |

Plasticity degrades faster than RULER scores: -31% plasticity decline maps to -19% RULER decline. This suggests that either (a) RULER tasks don't require the full flexibility measured by plasticity (many tasks are retrieval-based where moderate plasticity suffices), or (b) task-level redundancy (multiple valid retrieval paths) buffers against plasticity loss.

---

## Instructions: Collecting Per-Length LBP Scores

This is the only remaining data gap.

### Option A: Extract from LongBench Pro GitHub (preferred)

1. Clone https://github.com/THUDM/LongBench
2. Check for prediction files or a leaderboard with per-length breakdowns
3. Each LBP sample has an explicit `length_bucket` label (8K/16K/32K/64K/128K/256K)
4. If raw predictions exist, group by length_bucket and compute per-task metrics, then average

### Option B: Run evaluation locally

1. `datasets.load_dataset("caskcsg/LongBench-Pro")`
2. Run inference on 6 models (Llama-3.2-3B, Ministral-3-{3,8}B, Qwen3-{4,8,14}B)
3. Non-thinking mode, output budget 1K, middle truncation, per Appendix D
4. Score and group by length_bucket

Models ordered by GPU memory: 3B (~7GB), 3B (~7GB), 4B (~9GB), 8B (~17GB), 8B (~17GB), 14B (~30GB).
Estimated: ~12-24 GPU hours total on A100.

### Option C: Contact paper authors

Email corresponding author requesting per-model per-length-bucket Overall scores for the 7 models.
