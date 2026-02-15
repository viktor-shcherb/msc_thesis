# Interventions on Weights for Understanding Factual Association Storage [p. 4-9]

## 3.1 Rank-One Model Editing (ROME)

[p. 5] MLP is treated as key-value memory:

- `W_fc` maps hidden input to key-like features.
- `W_proj` maps to value-like factual content.

[p. 5] Core constrained update objective (Equation 2):

`min ||W_hat K - V||  subject to  W_hat k* = v*`

Closed-form update:

`W_hat = W + Lambda (C^-1 k*)^T`, with `C = K K^T`.

[p. 5-6] ROME pipeline:

1. **Key selection** (`k*`): average MLP key activations at the final subject token over sampled prefixes (Equation 3).
2. **Value optimization** (`v*`): optimize a vector inserted at decisive MLP site to increase target-object likelihood while regularizing KL on subject-essence prompt (Equation 4).
3. **Insertion**: apply rank-one weight update using Eq. 2.

[p. 6] Eq. 4 has two terms:

- maximize target object probability after intervention,
- KL regularization to reduce "essence drift".

## 3.2 zsRE Evaluation

[p. 6] Compared methods: FT, FT+L, KE, MEND, plus tuned KE-zsRE and MEND-zsRE.

**Table 1** (p. 6): zsRE editing results on GPT-2 XL.

| Editor | Efficacy | Paraphrase | Specificity |
|---|---:|---:|---:|
| GPT-2 XL | 22.2 | 21.3 | 24.2 |
| FT | 99.6 | 82.1 | 23.2 |
| FT+L | 92.3 | 47.2 | 23.4 |
| KE | 65.5 | 61.4 | 24.9 |
| KE-zsRE | 92.4 | 90.0 | 23.8 |
| MEND | 75.9 | 65.3 | 24.1 |
| MEND-zsRE | 99.4 | 99.3 | 24.1 |
| **ROME** | **99.8** | 88.1 | 24.2 |

[p. 6] Main interpretation: regurgitation on direct prompts is easy for multiple methods; paraphrase robustness improves for tuned hypernetworks; zsRE specificity metric is weak for local bleedover detection.

## 3.3 COUNTERFACT Evaluation Design

[p. 7] COUNTERFACT introduced to separate superficial rewriting from robust factual-association change.

[p. 7] Metrics:

- Efficacy score/magnitude (`ES`, `EM`): success on rewritten fact (`P[o*] > P[o_c]`).
- Paraphrase score/magnitude (`PS`, `PM`): generalization across paraphrases.
- Neighborhood score/magnitude (`NS`, `NM`): specificity on nearby subjects.
- Harmonic aggregate `S` over ES/PS/NS.
- Generation consistency `RS` via TF-IDF similarity.
- Fluency `GE` via weighted bi/tri-gram entropy.

**Table 2** (p. 7): COUNTERFACT composition highlights.

| Item | Total |
|---|---:|
| Records | 21,919 |
| Subjects | 20,391 |
| Objects | 749 |
| Counterfactual statements | 21,595 |
| Paraphrase prompts | 42,876 |
| Neighborhood prompts | 82,650 |
| Generation prompts | 62,346 |

**Table 3** (p. 7): benchmark capability comparison (includes efficacy/generalization/bleedover/consistency/fluency dimensions), motivating COUNTERFACT.

## 3.4-3.6 Main Quantitative/Qualitative Findings

[p. 7-9] Layer-token sweep confirms best performance at middle layers and final subject token, matching causal-trace early site.

**Figure 5** (p. 7): layer-token sweep; peak near mid-layers at final subject token.

**Table 4** (p. 8): COUNTERFACT results (key values)

- GPT-2 XL baseline score `S = 30.5`.
- ROME on GPT-2 XL: `S = 89.2`, `ES = 100.0`, `PS = 96.4`, `NS = 75.4`, `RS = 41.9`.
- GPT-J baseline score `S = 23.6`.
- ROME on GPT-J: `S = 91.5`, `ES = 99.9`, `PS = 74.1`, `NS = 78.9`, `RS = 43.0`.

[p. 8] Failure pattern summarized for non-ROME methods:

- F1: overfit/regurgitate without paraphrase generalization.
- F2: bleedover to unrelated neighboring subjects.

[p. 8-9] Figure 6 and Appendix G qualitative examples show:

- FT can generalize but with heavy specificity damage.
- FT+L can preserve specificity but under-generalize.
- KE/MEND can show instability and semantic drift in generations.
- ROME more often preserves both specificity and paraphrase robustness, with some fluency degradation.

[p. 8] Human evaluation (15 volunteers, 50 counterfactuals):

- ROME rated about **1.8x** more likely than FT+L to be more consistent with inserted fact.
- ROME rated about **1.3x** less likely than FT+L to be more fluent.

## 3.7 Limitations

[p. 9] Stated limitations:

- single-fact editing method (not large-scale retraining solution),
- directional association edits (inverse fact may require separate edit),
- not validated for non-factual belief types (logical/spatial/numerical),
- edited models still hallucinate plausible but unsupported claims.

**Figure 4** (p. 5): ROME edit mechanism in one MLP layer.
- Subject-conditioned key selection and object-conditioned value optimization.
- Rank-one projection update inserts new association while minimizing collateral interference.

**Figure 6** (p. 9): qualitative generation comparison for counterfactual "Pierre Curie's area of work is medicine".
