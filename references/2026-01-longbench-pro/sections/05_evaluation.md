# 5 Evaluation [p. 6-13]

## 5.1 Evaluation Settings [p. 6-7]

[p. 6-7] 46 long-context models are evaluated across closed/open source, thinking/mixed/instruct behavior, dense/MoE architecture, and context lengths from 128K to 1M+ (with one 4M-claimed model).

[p. 6] Task metrics by task family:
- T1: NDCG@k
- T2 and T6.3: Pairwise Accuracy
- T3 and T11: Accuracy
- T5, T6.2, T7, T9: F1
- T6.1, T8, T10: SubEM
- T4: weighted SemSim + ROUGE-L

[p. 6] Summarization scoring equation:

> \(\text{Score}_{summary} = 0.5 \cdot \max_i \text{SemSim}(S_{gen}, S_{ref_i}) + 0.5 \cdot \max_i \text{ROUGE-L}(S_{gen}, S_{ref_i})\)

[p. 6] All metrics are in [0, 1], then multiplied by 100 for reporting.

[p. 7] Inference protocol highlights:
- Three runs per sample.
- Report both average performance and upper-bound variants (Best-of-N, Pass@N).
- Thinking output budget: 32K for models supporting 256K context, else 8K.
- Non-thinking output budget: 1K.
- Over-length inputs are middle-truncated to fit context budget.

## 5.2 General Performance [p. 7-10]

[p. 8] Table 3 is the main benchmark table (46 models across Overall, language splits, difficulty splits, thinking/non-thinking settings).

### Table 3 (selected rows, exact values) [p. 8]

| Model | Type | Ctx Length | Overall | EN | ZH | Extreme | Hard | Moderate | Easy |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| Gemini-2.5-Pro | Thinking | 1M | 73.42 | 72.35 | 74.49 | 50.77 | 81.03 | 81.98 | 84.40 |
| GPT-5 | Thinking | 272K | 72.61 | 73.24 | 71.97 | 48.37 | 78.74 | 82.31 | 85.23 |
| Claude-4-Sonnet | Mixed | 1M | 69.87 | 71.09 | 68.65 | 47.05 | 74.72 | 76.58 | 83.78 |
| DeepSeek-V3.2 | Mixed | 160K | 67.82 | 67.89 | 67.75 | 44.27 | 67.73 | 75.08 | 85.02 |
| Qwen3-235B-A22B-Thinking-2507 | Thinking | 256K | 66.97 | 66.83 | 67.12 | 43.39 | 67.10 | 75.12 | 83.55 |
| GLM-4.6 | Mixed | 198K | 58.21 | 56.50 | 59.92 | 38.88 | 48.92 | 60.95 | 79.78 |
| Kimi-K2-Instruct-0905 | Instruct | 256K | 55.53 | 56.96 | 54.10 | 38.25 | 43.75 | 57.33 | 77.29 |
| MiniMax-Text-01 | Instruct | 4M | 45.00 | 44.17 | 45.82 | 33.78 | 38.02 | 40.82 | 61.92 |
| Llama-3.1-405B-Instruct | Instruct | 128K | 40.66 | 44.46 | 36.86 | 29.81 | 34.09 | 29.22 | 61.36 |

[p. 7-10] Seven findings are explicitly reported:
1. Context optimization can exceed gains from parameter scaling (e.g., Qwen3-4B-Instruct-2507 45.68 > Qwen3-8B 44.34; Qwen3-30B-A3B-Instruct-2507 54.52 > Qwen3-32B 51.12).
2. Claimed length and effective capability diverge (e.g., MiniMax-Text-01 4M-claimed but 45.00 overall).
3. Language asymmetry persists (some model families stronger in EN vs ZH, and vice versa).
4. Easy-level gaps between top open/closed models are small; Extreme-level gaps are larger.
5. Thinking often improves results materially.
6. Native reasoning training is more effective than prompting instruct models to think.
7. Mixed-thinking models show strong Pareto behavior between speed-oriented and deep-reasoning modes.

## 5.3 Upper-Bound Performance [p. 10]

[p. 10] Best-of-N and Pass@N are reported to separate generation variance from capability limits.

[p. 10] Key stated observations:
- Best-of-N rises monotonically for all models.
- Gemini-2.5-Pro and GPT-5 show high stability (smaller marginal gains as N increases).
- Some models (e.g., Qwen3-235B-A22B-Thinking-2507) gain more from repeated sampling.

[p. 10] Under Pass@3, even strongest models remain far from saturated on Extreme difficulty (Gemini-2.5-Pro: 10.68), indicating remaining headroom.

**Figure 5** (p. 9): "Trends in Best-of-N metrics"
- Description: performance vs N curves.
- Supports claim: multiple sampling improves outcomes, but with model-dependent gain slopes.

**Figure 6** (p. 9): "Trends in Pass@N metrics"
- Description: probability of at least one fully correct sample as N grows.
- Supports claim: benchmark remains difficult even under multi-sample evaluation.

## 5.4 Comparison Across Length Dimension [p. 10-11]

[p. 10-11] Most models decline as length increases. Gemini-2.5-Pro is highlighted as relatively length-insensitive within 8K-256K:
- 8K: 74.50
- 16K: 74.79
- 32K: 75.31
- 64K: 74.18
- 128K: 70.00
- 256K: 71.77

Interpretation in text: the frontier bottleneck shifts from raw "can read long input" toward deep long-range dependency reasoning.

**Figure 7** (p. 11): "Performance across different sample lengths"
- Description: per-model score trends over 8K-256K.
- Supports claim: degradation with length is common but not uniform across models.

## 5.5 Comparison Across Task Dimension [p. 10-11]

[p. 10-11] Reported cross-task patterns:
- Strong retrieval/sequencing (T1/T2), weaker aggregation (T6).
- Better backward evidence alignment than forward generation from evidence.
- Reasoning and consistency maintenance remain bottlenecks, especially T7/T11.

**Figure 8** (p. 11): "Performance across different tasks"
- Description: task-wise bars/curves showing model differences by task family.
- Supports claim: capability is highly task-dependent; retrieval strength does not imply global reasoning strength.

## 5.6 Comparison Across Context Requirement Dimension [p. 12]

[p. 12] All models perform better on Partial than Full tasks. The paper reports a 7.32-10.84 point drop when shifting from local to global dependency tasks.

**Figure 9** (p. 12): "Performance across different context requirements"
- Description: paired Full vs Partial comparisons per model.
- Supports claim: global integration over dispersed evidence remains a major bottleneck.

## 5.7 Comparison Across Construction Strategies [p. 12-13]

[p. 12-13] Time cost comparison over sampled documents:
- Human-only: time grows sharply with length.
- Model-only: consistently low time.
- Human-model collaborative: moderate cost, slower growth than human-only.

[p. 13] Quality comparison (five-dimension rubric, 3 experts):
- Human-model collaborative: **0.9609 +/- 0.0415**
- Human-only: **0.9484 +/- 0.0450**
- Model-only: **0.8964 +/- 0.0536**
- Inter-rater agreement: **Fleiss' Kappa = 0.76**

The paper attributes collaborative gains to pairing model drafting with expert verification.

**Figure 10** (p. 12): "Comparison of sample construction strategies"
- Description: two panels for time cost vs length and quality by evaluation dimension.
- Supports claim: collaborative construction improves quality while keeping costs practical at longer lengths.
