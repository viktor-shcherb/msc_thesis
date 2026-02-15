---
title: "Locating and Editing Factual Associations in GPT"
authors: "Meng, Bau, Andonian, Belinkov"
year: 2022
venue: "NeurIPS 2022"
paper_type: conference-paper
categories: ["mechanistic-interpretability", "probing-and-analysis"]
scope: ["autoregressive GPT-style language models", "single-fact editing", "causal-intervention analysis"]
benchmarks_used: ["zsre", "counterfact"]
models_introduced: []
models_evaluated: ["gpt-2-xl", "gpt-j-6b", "gpt-neox-20b"]
key_claims:
  - id: C1
    claim: "Factual recall in GPT-2 XL is mediated by a localized early-site computation in middle-layer MLPs at the final subject token."
    evidence: "Figure 2, Figure 3, Section 2.2"
    status: supported
    scope: "GPT-2 XL, 1000 known factual prompts, causal restoration interventions"
    magnitude: "Average total effect 18.6%; individual-state AIE peak 8.7% (layer ~15); MLP early-site AIE peak 6.6% vs attention 1.6% at subject token"
  - id: C2
    claim: "A single rank-one MLP weight update can insert a target subject-relation-object association while minimizing interference with existing associations."
    evidence: "Equation 2-4, Figure 4, Appendix A"
    status: supported
    scope: "Single-layer intervention in autoregressive GPT models; key/value computed from subject-context activations"
    magnitude: "Closed-form update W_hat = W + Lambda(C^-1 k*)^T; practical edit runtime ~2s on GPT-2 XL (Appendix E.5)"
  - id: C3
    claim: "ROME is highly effective on zsRE factual editing and remains competitive with tuned hypernetwork editors on paraphrase generalization."
    evidence: "Table 1, Section 3.2"
    status: supported
    scope: "GPT-2 XL, 10K zsRE evaluation records"
    magnitude: "ROME: Efficacy 99.8%, Paraphrase 88.1%, Specificity 24.2%"
  - id: C4
    claim: "On COUNTERFACT, ROME provides the strongest observed specificity-generalization tradeoff among compared editors."
    evidence: "Table 4, Section 3.4"
    status: supported
    scope: "GPT-2 XL (7,500 records) and GPT-J (2,000 records), multi-metric counterfactual editing evaluation"
    magnitude: "Score S=89.2 (GPT-2 XL) and S=91.5 (GPT-J), with both high ES and high NS compared to baselines"
  - id: C5
    claim: "The best-performing edit location aligns with the causal-trace early site, linking mechanistic localization and intervention success."
    evidence: "Figure 5, Section 3.4"
    status: supported
    scope: "Layer-token sweep over GPT-2 XL edits"
    magnitude: "Peak generalization and strong specificity at middle layers near the final subject token (consistent with causal-trace peak around layer 18)"
  - id: C6
    claim: "Human evaluators judge ROME generations as more counterfactual-consistent than FT+L but somewhat less fluent."
    evidence: "Section 3.6, Figure 26, Appendix J"
    status: supported
    scope: "15 volunteers; 50 counterfactual scenarios; pairwise ranking against FT+L"
    magnitude: "ROME judged 1.8x more likely to be more consistent; 1.3x less likely to be more fluent than FT+L"
cross_references:
  - target: 2023-12-rwkv-reinventing-rnns-transformer
    type: extended-by
    detail: "RWKV adopts Meng et al.'s causal tracing methodology to analyze factual retrieval pathways in a non-attention architecture"
  - target: 2021-12-transformer-circuits-framework
    type: complementary
    detail: "Both works use mechanistic internal-circuit analysis, but ROME adds direct factual parameter editing and quantitative edit benchmarks"
open_questions:
  - question: "How can ROME-style single-fact interventions be scaled to reliable multi-fact batch editing without interference?"
    addressed_by: null
  - question: "Do the same localization/editability patterns hold for non-factual knowledge (logical, spatial, numerical)?"
    addressed_by: null
  - question: "Can the consistency gains of ROME be retained while reducing observed fluency degradation in generation?"
    addressed_by: null
  - question: "What causal mechanisms determine the exception cases where decisive token positions are not subject-final?"
    addressed_by: null
  - question: "Can attention-targeted interventions be combined with MLP-targeted edits to improve paraphrase generalization without regurgitation?"
    addressed_by: null
---

# Locating and Editing Factual Associations in GPT

**Authors:** Kevin Meng, David Bau, Alex Andonian, Yonatan Belinkov (MIT CSAIL; Northeastern University; Technion - IIT)  
**Date:** December 2022, NeurIPS 2022 (arXiv:2202.05262)

---

## Core Research Problem

Large language models can recall many factual statements, but **the internal mechanism of factual recall is unclear**. Prior probing and editing work mostly focused on masked models or indirect interventions, and it was not established where, and through which computations, factual associations are represented in autoregressive GPT models.

The paper frames two linked questions:

1. **Mechanism question:** which internal states/modules causally mediate factual recall?
2. **Intervention question:** can one directly edit that mechanism to write a new factual association while preserving nearby knowledge?

The concrete challenge is to move from descriptive probing to **causally grounded, minimally invasive model editing** with measurable specificity and generalization.

---

## Problem Solutions

The paper combines causal analysis and weight intervention:

1. **Causal Tracing:** run clean vs corrupted prompts, then restore selected hidden states to measure indirect causal effects on factual prediction.
2. **ROME (Rank-One Model Editing):** treat one MLP projection as an associative memory and insert a new key-value pair via a closed-form rank-one update.
3. **Counterfactual-focused evaluation:** introduce COUNTERFACT to measure efficacy, paraphrase generalization, neighborhood specificity, generation consistency, and fluency jointly.

The central thesis is that **middle-layer MLP computation at subject-token processing is both causally decisive and directly editable**.

---

## Approach Details

### Method

The intervention logic has three steps.

1. **Locate decisive states** with causal tracing.  
   Corrupt subject token embeddings, then restore candidate hidden states one at a time; measure object-token probability recovery.
2. **Construct edit key and value.**  
   - `k*`: average MLP key-side activation at the final subject token across multiple random-prefix contexts.
   - `v*`: optimized vector that makes the edited model prefer target object `o*` while regularizing subject-essence behavior.
3. **Apply rank-one edit.**  
   Update one projection matrix to satisfy `W_hat k* = v*` while minimizing disturbance to existing keys.

Key equations:

> `W_hat = W + Lambda (C^-1 k*)^T`  
> where `Lambda = (v* - Wk*) / ((C^-1 k*)^T k*)`.

And value optimization objective:

> `L(z) = E[-log P(o* | x_j + p)] + KL(P_edited(.|p') || P_original(.|p'))`

### Key Technical Components

- **Causal intervention protocol:** clean run, corrupted run, corrupted-with-restoration run.
- **Token-position sensitivity:** decisive site is not uniformly distributed; strongest effects concentrate at final subject token (with exceptions).
- **Essence regularization term:** KL term in value optimization penalizes broad semantic drift.
- **Second-moment correction:** uses `C^-1 k*` to reduce interference with previously stored associations in the edited layer.

### Theoretical Analysis

The method's algebraic core is a constrained least-squares solution (Appendix A).

- Base memory fit: solve `WK ≈ V`.
- Add linear equality `W_hat k* = v*`.
- Solve with Lagrangian to obtain the closed-form rank-one correction.

Interpretation: ROME performs **minimal structured movement** in weight space that exactly enforces a desired key-value mapping for the chosen subject representation.

### Experimental Setup

Primary model/evaluation setup:

- **Models:** GPT-2 XL (main), GPT-J (main COUNTERFACT extension), with causal-trace comparisons on GPT-NeoX and smaller GPT-2 variants.
- **zsRE:** 10,000-record editing slice, with FT, FT+L, KE, MEND and task-tuned KE/MEND variants.
- **COUNTERFACT:** 21,919 records; includes paraphrase prompts, relation-neighborhood prompts, and generation prompts.
- **Human eval:** 15 volunteers, 50 counterfactual scenarios, consistency and fluency ranking.

### Key Results

| Setting | Proposed Method (ROME) | Best Baseline in Paper |
|---|---|---|
| zsRE efficacy/paraphrase/specificity (GPT-2 XL) | 99.8 / 88.1 / 24.2 | MEND-zsRE 99.4 / 99.3 / 24.1 |
| COUNTERFACT score `S` (GPT-2 XL) | 89.2 | FT+L 66.9 |
| COUNTERFACT score `S` (GPT-J) | 91.5 | FT+L 68.7 |
| Human consistency vs FT+L | 1.8x more likely better | FT+L lower consistency |
| Human fluency vs FT+L | 1.3x less likely better | FT+L higher fluency |

Main takeaways:

- **Localization validated by intervention:** best edit sites align with causal-trace peaks.
- **Tradeoff advantage:** ROME avoids common baseline failure modes (overfit regurgitation vs broad bleedover) more consistently on COUNTERFACT.
- **Residual cost:** generation fluency can degrade even when factual consistency improves.

### Additional Subsections

#### Evidence Breadth

- Strong evidence: multiple metrics, two large autoregressive model families, and both automatic and human evaluations.
- Limited evidence: single-fact editing formulation; no large-scale multi-edit experiment in this paper.

#### Negative Results

- zsRE specificity metric is relatively insensitive to localized bleedover.
- Attention-weight-only intervention (Appendix I) can regurgitate the rewrite prompt but often fails on paraphrase/generalization.

---

## Limitations and Failure Modes

Author-acknowledged limits:

- single-fact edits (not a complete retraining substitute),
- directional edits (inverse relation may require separate intervention),
- incomplete coverage of non-factual knowledge categories,
- edited models can still produce plausible but unsupported text.

In evaluation failures across methods:

- some baselines overfit direct rewrite prompt without robust paraphrase transfer,
- some methods induce neighborhood bleedover,
- fluency degradation can appear despite better factual consistency.

### Scope and Comparability

- **What was not tested:** multi-fact simultaneous edits, non-autoregressive architectures as primary targets, strong multilingual robustness, and long-run persistence under downstream finetuning.
- **Comparability notes:** zsRE and COUNTERFACT emphasize different failure modes; high zsRE performance does not imply strong neighborhood specificity. Human fluency judgments and n-gram entropy (`GE`) are related but not interchangeable.

---

## Conclusions

### Contributions

1. **Causal localization of factual recall.** The paper identifies a reproducible early-site causal signature in middle-layer MLP activity at subject-token processing, with quantitative intervention evidence.
2. **Closed-form factual editing mechanism.** ROME provides a simple rank-one update rule that operationalizes mechanistic insights into direct parameter intervention.
3. **Richer editing benchmark design.** COUNTERFACT broadens evaluation beyond direct prompt success to include paraphrase generalization, neighborhood specificity, consistency, and fluency.
4. **Cross-check between mechanism and efficacy.** Layer-token edit sweeps align with causal-trace peaks, strengthening the mechanistic interpretation.

### Implications

1. **Mechanistic editing is feasible.** Directly editing targeted internal computations can outperform broader optimization methods on precision-sensitive factual rewrites.
2. **Metric design matters.** Benchmarks that include neighborhood and generation criteria expose failure modes hidden by simpler edit-success metrics.
3. **Safety dual-use remains material.** The same capability that enables correction can also enable targeted misinformation insertion.

---

## Key Claims

1. **Localized MLP-mediated factual recall:** middle-layer MLP activity at final subject token causally mediates object prediction (Figure 2/3, Section 2.2).  
   Evidence quality: tested on 1000 prompts with explicit interventions (strong for analyzed setup).
2. **Rank-one edit sufficiency for single-fact insertion:** constrained least-squares update can enforce new association with limited collateral disruption (Eq. 2-4, Appendix A).  
   Evidence quality: algebraic derivation + empirical edits (moderate-to-strong).
3. **High zsRE edit efficacy:** ROME achieves near-perfect efficacy with strong paraphrase performance on GPT-2 XL (Table 1).  
   Evidence quality: large benchmark slice; specificity metric limited (moderate).
4. **Best COUNTERFACT tradeoff among compared methods:** ROME leads on aggregate score while maintaining both generalization and specificity (Table 4).  
   Evidence quality: multi-metric comparison across two model families (strong).
5. **Causal-site and edit-site alignment:** highest edit performance occurs at layer-token regions identified by causal tracing (Figure 5 vs Section 2 traces).  
   Evidence quality: direct alignment test within same model (strong).
6. **Consistency-fluency tension in human judgments:** ROME improves factual consistency but can reduce fluency relative to FT+L (Section 3.6, Appendix J).  
   Evidence quality: human evaluation with limited participant/sample size (moderate).

---

## Open Questions

1. How can closed-form single-fact editing be generalized to stable multi-fact batch editing without compounding interference?
2. Does the same causal localization hold for non-factual internal knowledge (logical, procedural, numerical)?
3. Which algorithmic changes best recover fluency while preserving ROME-level specificity and generalization?
4. What mechanistically distinguishes exception cases where decisive token locations shift away from subject-final positions?
5. Can hybrid MLP+attention interventions improve paraphrase generalization beyond current single-site ROME edits?

---

## Core References and Why They Are Referenced

### Causal and Mechanistic Foundations

- **Pearl (2001)** -- *Direct and indirect effects.* Provides the mediation framework used to define indirect causal effect in hidden-state interventions.
- **Vig et al. (2020b)** -- *Investigating gender bias in language models using causal mediation analysis.* Prior NLP causal-mediation application that motivates intervention-based attribution.
- **Elhage et al. (2021)** -- *A mathematical framework for transformer circuits.* Mechanistic-circuits framing referenced when interpreting information routing/composition inside transformers.

### Direct Predecessors for Editing

- **Geva et al. (2021)** -- *Transformer feed-forward layers are key-value memories.* Motivates the MLP key-value interpretation used by ROME.
- **Bau et al. (2020)** -- *Rewriting a deep generative model.* Supplies the constrained rank-one rewriting perspective adapted to transformer MLPs.
- **Dai et al. (2022)** -- *Knowledge neurons in pretrained transformers.* Neuron-level editing baseline and conceptual comparator.
- **De Cao et al. (2021)** -- *Editing factual knowledge in language models.* KE hypernetwork baseline.
- **Mitchell et al. (2021)** -- *Fast model editing at scale.* MEND baseline and evaluation conventions.
- **Zhu et al. (2020)** -- *Modifying memories in transformer models.* Constrained fine-tuning baseline (FT+L).

### Benchmark and Evaluation Inputs

- **Elazar et al. (2021a)** -- *Measuring and Improving Consistency in Pretrained Language Models.* Source material (ParaRel) used to construct COUNTERFACT.
- **Levy et al. (2017)** -- *Zero-Shot Relation Extraction.* Base dataset lineage for zsRE editing evaluation.
- **Hase et al. (2021)** -- *Do language models have belief state?* Cited for benchmark-difficulty concerns motivating stronger counterfactual testing.
