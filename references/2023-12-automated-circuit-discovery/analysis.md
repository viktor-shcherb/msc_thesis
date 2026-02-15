---
title: "Towards Automated Circuit Discovery for Mechanistic Interpretability"
authors: "Conmy, Mavor-Parker, Lynch, Heimersheim, Garriga-Alonso"
year: 2023
venue: "NeurIPS 2023 (Advances in Neural Information Processing Systems 36)"
paper_type: conference-paper
categories: ["mechanistic-interpretability", "attention-analysis", "probing-and-analysis", "pruning-and-sparsity"]
scope: ["post-hoc circuit extraction", "activation patching in transformer computational graphs", "GPT-2 Small and toy tracr models"]
benchmarks_used: []
models_introduced: []
models_evaluated: ["gpt-2"]
key_claims:
  - id: C1
    claim: "Mechanistic interpretability work can be systematized as a three-step workflow: choose behavior/metric/dataset, choose graph granularity, then iteratively patch activations to isolate the circuit."
    evidence: "Section 2, Table 1"
    status: supported
    scope: "mechanistic interpretability studies that use activation patching on transformer internals"
    magnitude: "qualitative framework spanning 6 benchmarked tasks"
  - id: C2
    claim: "ACDC can automate edge-level circuit extraction by recursively pruning edges whose removal produces only a small increase in divergence from the original model."
    evidence: "Algorithm 1, Section 3"
    status: supported
    scope: "directed acyclic computational graphs over model components with user-chosen threshold tau"
    magnitude: "iterative pruning over up to tens of thousands of edges per model graph"
  - id: C3
    claim: "On canonical language-model circuit benchmarks, ACDC is competitive with or better than adapted SP and HISP on edge-level AUC in several key settings."
    evidence: "Figure 3, Table 2"
    status: supported
    scope: "IOI, Greater-Than, and Docstring tasks under corrupted-activation setup"
    magnitude: "KL edge AUCs: Docstring 0.982, Greater-Than 0.853, IOI 0.869 (Table 2)"
  - id: C4
    claim: "For the Greater-Than behavior in GPT-2 Small, ACDC can rediscover all previously identified component types while selecting a tiny fraction of graph edges."
    evidence: "Abstract, Appendix G"
    status: supported
    scope: "Greater-Than task on GPT-2 Small under authors' evaluation setup"
    magnitude: "68 selected edges out of about 32,000 total edges; 5/5 component types rediscovered"
  - id: C5
    claim: "Zero-ablation variants can strongly improve recovery on toy tracr circuits, including perfect edge-level AUC in reported settings."
    evidence: "Table 3, Appendix I"
    status: supported
    scope: "tracr-proportion and tracr-reverse compiled toy transformers"
    magnitude: "edge-level loss AUC = 1.000 for both tracr tasks with ACDC (Table 3)"
  - id: C6
    claim: "Current automated methods remain brittle: results depend on metric/corruption choices and can miss negative or hard-to-localize components."
    evidence: "Section 4.1, Figure 15, Conclusion"
    status: supported
    scope: "single-metric optimization workflows on transformer circuit extraction"
    magnitude: "large task-dependent variability (e.g., IOI KL edge AUC falls to 0.539 for ACDC under zero ablation in Table 3)"
cross_references:
  - target: 2021-12-transformer-circuits-framework
    type: extends
    detail: "Operationalizes the circuits perspective into an explicit automated edge-pruning search procedure."
  - target: 2022-03-in-context-learning-induction-heads
    type: complementary
    detail: "Uses induction-related circuit benchmarks that continue the same mechanistic line, but focuses on automation and benchmarked recovery."
  - target: 2019-07-specialized-attention-heads-pruning
    type: formalizes
    detail: "Reuses pruning-style component-importance ideas (HISP baseline) in a causal patching-based circuit-recovery setting."
open_questions:
  - question: "How can circuit discovery robustly recover negative or adversarially interacting components without exploding false positives?"
    addressed_by: null
  - question: "What objective should replace single-metric optimization to better capture multi-objective mechanistic faithfulness?"
    addressed_by: null
  - question: "How well does ACDC-style edge search scale to modern frontier models with far larger graphs and longer contexts?"
    addressed_by: null
  - question: "Can step-4 functional interpretation of recovered nodes be automated with similar reliability as step-3 edge recovery?"
    addressed_by: null
  - question: "How should ACDC and Causal Scrubbing be combined into a principled end-to-end workflow with calibrated uncertainty?"
    addressed_by: null
---
# Towards Automated Circuit Discovery for Mechanistic Interpretability

**Authors:** Arthur Conmy, Augustine N. Mavor-Parker, Aengus Lynch, Stefan Heimersheim, Adrià Garriga-Alonso
**Date:** December 2023, NeurIPS 2023 (Advances in Neural Information Processing Systems 36)

---

## Core Research Problem

Mechanistic interpretability had produced several impressive reverse-engineering case studies (e.g., IOI, induction, greater-than), but those results relied on substantial manual edge-by-edge activation patching. The process was expensive, iterative, and hard to scale.

The paper targets this bottleneck directly: **how to automate the subgraph extraction step of mechanistic interpretability without losing task-specific faithfulness.**

Concretely, the authors frame two evaluation goals:
- **Q1:** recover graph structure that actually underlies the behavior.
- **Q2:** avoid extraneous components that are not part of the behavior-specific circuit.

---

## Problem Solutions

The core proposal is **Automatic Circuit DisCovery (ACDC)**, a recursive edge-pruning algorithm over a user-defined computational DAG.

High-level idea:
1. Define task prompts and a corruption distribution.
2. Start from the full graph.
3. Iteratively remove edges that do not materially harm agreement with the full model.
4. Return sparse subgraph as candidate circuit.

The paper also adapts two baselines for direct comparison:
- **SP** (Subnetwork Probing)
- **HISP** (Head Importance Score for Pruning)

Both are modified to support the same metric and corrupted-activation setup used by ACDC.

---

## Approach Details

### Method

Given full graph `G` and candidate graph `H`, outputs from removed edges are replaced by corrupted activations from paired inputs.

Primary objective (default):

> \( D_{KL}(G || H) = \frac{1}{n} \sum_i D_{KL}(G(x_i) || H(x_i, x'_i)) \)

Edge `w -> v` is removed when:

> \( D_{KL}(G || H_{new}) - D_{KL}(G || H) < \tau \)

where `tau` controls sparsity.

### Key Technical Components

- **Output-to-input traversal:** edges are tested in reverse topological order.
- **Corruption-aware intervention:** supports both corrupted activations and zero ablation variants.
- **Graph-level flexibility:** works with different granularities (heads/MLPs, QKV splits, and in some appendices position- or neuron-level variants).

### Experimental Setup

Primary benchmarks:
- IOI
- Greater-Than
- Docstring
- tracr-xproportion
- tracr-reverse
- Induction

Compared methods: ACDC, adapted SP, adapted HISP.

Core metrics:
- Edge-level ROC/AUC versus canonical circuits (where available).
- KL divergence vs edge-count tradeoff on stand-alone tasks.

### Key Results

#### Main benchmark summary

| Setting | Result |
|---|---|
| Corrupted-activation KL AUC (Docstring) | ACDC 0.982 vs HISP 0.805 vs SP 0.937 |
| Corrupted-activation KL AUC (Greater-Than) | ACDC 0.853 vs HISP 0.693 vs SP 0.806 |
| Corrupted-activation KL AUC (IOI) | ACDC 0.869 vs HISP 0.789 vs SP 0.823 |
| Zero-ablation tracr edge AUC | ACDC = 1.000 on both tracr tasks |

#### Qualitative recovery claims

- Abstract claim: ACDC rediscovered 5/5 component types for Greater-Than.
- Reported sparsity: 68 selected edges out of around 32,000 GPT-2 Small graph edges.
- On induction, ACDC tends to trace favorable KL-vs-sparsity frontiers for moderate edge counts.

---

## Limitations and Failure Modes

The paper is explicit that results are not uniformly robust.

Key limitations:
- **Metric sensitivity:** optimizing different objectives (KL vs task-specific metrics) can change recovered circuits materially.
- **Corruption sensitivity:** zero vs corrupted interventions can reverse relative performance.
- **Negative component miss-rate:** single-metric optimization may miss components that are causally relevant but locally harmful.
- **Graph and ordering dependence:** some settings depend on parent-edge iteration order and chosen abstraction level.
- **Ground-truth uncertainty:** canonical circuits from prior work are strong baselines but not guaranteed complete/correct.

The OR-gate appendix provides a small adversarial case where all three methods show failure modes.

### Scope and Comparability

- Most strong results are on GPT-2 Small-style tasks and small toy transformers.
- The work does not establish robust scaling behavior on modern large models.
- Benchmarks are mechanistic and task-specific, not broad downstream capability suites.

---

## Conclusions

### Contributions

1. **Workflow formalization:** the paper codifies mechanistic circuit work into a three-step pipeline.
2. **ACDC algorithm:** practical edge-level circuit search over computational graphs.
3. **Baseline adaptation:** fair SP/HISP comparisons under the same intervention/metric conditions.
4. **Benchmarking framework:** ROC/AUC and KL-vs-sparsity analyses across multiple canonical tasks.
5. **Case-study utility:** early evidence that ACDC can assist exploratory interpretability projects.

### Implications

- Automated circuit search is feasible and can significantly reduce manual patching overhead.
- However, automated circuit discovery is currently better viewed as **hypothesis generation + pruning**, not complete mechanistic proof.
- ACDC and Causal Scrubbing are naturally complementary: broad search first, targeted causal validation second.

---

## Key Claims

1. **The three-step workflow is a good abstraction of recent mechanistic studies.**
Evidence: task survey and worked examples across IOI, Greater-Than, Docstring, tracr, induction. **Status: supported.**

2. **ACDC can automate a substantial portion of manual circuit extraction.**
Evidence: Algorithm 1 + quantitative recovery on multiple tasks. **Status: supported.**

3. **ACDC is competitive with SP/HISP on several corrupted-activation edge-level KL benchmarks.**
Evidence: Table 2 and Figure 3. **Status: supported.**

4. **ACDC can be highly sparse while retaining behavior-relevant components (e.g., Greater-Than 68/32k).**
Evidence: abstract + appendix circuit reconstructions. **Status: supported.**

5. **Zero-ablation can dramatically help toy-circuit recovery.**
Evidence: perfect tracr edge AUC in Table 3. **Status: supported.**

6. **Current methods are brittle and can miss crucial negative components.**
Evidence: IOI appendix analysis and conclusion discussion. **Status: supported.**

---

## Open Questions

1. How to recover negative components reliably without sacrificing sparsity?
2. How to build robust multi-metric objectives for circuit faithfulness?
3. What are the runtime/quality tradeoffs of edge-level search on frontier-scale models?
4. Can node-function interpretation be automated after graph recovery?
5. How should uncertainty be quantified for recovered circuits before downstream safety use?

---

## Core References and Why They Are Referenced

- **Elhage et al. (2021), Transformer Circuits Framework:** conceptual backbone for circuit-level graph decomposition.
- **Wang et al. (2023), IOI circuit:** canonical benchmark for in-the-wild circuit recovery.
- **Hanna et al. (2023), Greater-Than circuit:** benchmark used for sparse recovery claims.
- **Heimersheim & Janiak (2023), Docstring circuit:** benchmark and qualitative head-level comparison.
- **Cao et al. (2021), Subnetwork Probing:** baseline adapted for fair comparison.
- **Michel et al. (2019), HISP:** gradient-importance baseline adapted for circuit extraction.
