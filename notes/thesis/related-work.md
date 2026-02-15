# Thesis Related Work Note: Mechanistic Quantification of Effective Context Length

## Scope

This note proposes the `Related Work` chapter narrative for a thesis centered on a **mechanistic interpretability method** for effective context length (ECL).

## Proposed Narrative (Chapter 3)

### 1. Behavioral Measurement of Effective Context

Review benchmark-driven ECL measurement literature and its limits.

Focus:
- synthetic controllable benchmarks,
- low-overlap evaluations,
- realistic long-document evaluations,
- incompatibility of thresholds and metrics.

Suggested anchors: `2024-10-ruler-context-size`, `2024-12-babilong-long-context-reasoning`, `2025-07-nolima-long-context-evaluation`, `2026-01-longbench-pro`.

### 2. Mechanistic Explanations of Long-Context Failure

Review work that moves from behavioral degradation to mechanism-level explanations.

Focus:
- theoretical analyses of positional bias and topology,
- interventional analyses on heads/channels/masks,
- causal evidence vs observational correlation.

Suggested anchors: `2025-07-position-bias-transformers`, `2024-12-transformers-need-glasses-over-squashing`, `2025-04-retrieval-head-long-context-factuality`, `2025-04-pine-eliminating-position-bias`, `2025-07-position-bias-single-dimension-scaling`.

### 3. Methods that Attempt to Improve ECL

Treat this as supporting context, not thesis center.

Focus:
- context-extension methods (PI, NTK, YaRN, hybrids),
- inference-time mitigations (for example, retrieve-then-reason, position interventions),
- where gains transfer and where they fail.

Suggested anchors: `2023-06-pi-positional-interpolation`, `2023-06-rope-ntk`, `2024-05-yarn-context-extension`, `2024-07-qwen2-technical-report`, `2025-05-qwen3-technical-report`, `2025-10-kimi-linear-attention`, `2025-04-effective-context-length-falls-short`, `2025-11-context-length-hurts-performance`.

### 4. Gap Positioning for This Thesis

State the gap explicitly:
- prior work often either measures ECL behaviorally or explains parts of failure mechanistically,
- few works provide a unified, benchmark-robust, intervention-validated **mechanistic quantification method** for ECL,
- this thesis contribution is that unifying method and validation protocol.

## Suggested Headings for `chapters/03_related_work.tex`

- "Behavioral ECL Evaluation Literature"
- "Mechanistic Interpretability for Long-Context Failures"
- "Context-Extension and Mitigation Methods"
- "Research Gap and Thesis Positioning"

## Reusable Positioning Sentence

"This thesis addresses effective context length as a mechanistic quantity: rather than inferring capacity only from benchmark scores, it develops and validates an interpretability-based method that links behavioral degradation to internal causal mechanisms across long-context regimes."
