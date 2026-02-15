# Thesis Background Note: Mechanistic Quantification of Effective Context Length

## Scope

This note proposes the `Background` chapter narrative for a thesis centered on a **mechanistic interpretability method** to quantify effective context length (ECL).

## Proposed Narrative (Chapter 2)

### 1. Effective Context Length as a Formal Construct

Define claimed vs effective context and make explicit that ECL is task-conditional and metric-conditional.

Include:
- operational ECL definitions (absolute threshold, relative-to-base threshold),
- why ECL is not a single model constant,
- construct-validity caveats.

Suggested anchors: `2024-10-ruler-context-size`, `2025-07-nolima-long-context-evaluation`, `2024-12-babilong-long-context-reasoning`, `2026-01-longbench-pro`.

### 2. Transformer Information-Flow Primitives Relevant to ECL

Introduce the architectural primitives your method depends on:
- causal masking,
- positional encoding effects,
- attention topology/path structure,
- head specialization and retrieval circuits.

Suggested anchors: `2025-07-position-bias-transformers`, `2024-12-transformers-need-glasses-over-squashing`, `2025-04-retrieval-head-long-context-factuality`, `2025-04-round-and-round-rope`.

### 3. Mechanistic Failure Modes Behind ECL Collapse

Present the multi-causal failure picture your method should disentangle:
- position-frequency undertraining,
- position-bias accumulation,
- over-squashing/representational collapse,
- sparse retrieval-head fragility,
- length-alone degradation.

Suggested anchors: `2025-04-effective-context-length-falls-short`, `2025-04-pine-eliminating-position-bias`, `2025-07-position-bias-single-dimension-scaling`, `2024-12-transformers-need-glasses-over-squashing`, `2025-11-context-length-hurts-performance`.

### 4. Mechanistic Interpretability Toolkit (Method Preliminaries)

Set up the toolbox used later in methodology:
- observational probes (attention/activation profiling),
- interventional probes (masking, patching, scaling, counterfactual edits),
- causal-claim criteria,
- mapping internal signals to behavioral ECL.

Suggested anchors: `2025-04-retrieval-head-long-context-factuality`, `2025-04-pine-eliminating-position-bias`, `2025-07-position-bias-single-dimension-scaling`, `2025-11-context-length-hurts-performance`.

### 5. Validity Framework for Mechanistic ECL Methods

Define the evidence-quality lens used by the thesis:
- construct validity,
- causal validity,
- external validity.

Suggested anchors: `2024-08-flenqa-input-length-reasoning`, `2025-11-context-length-hurts-performance`, `2025-07-nolima-long-context-evaluation`, `2026-01-longbench-pro`.

## Suggested Headings for `chapters/02_background.tex`

- "Effective Context Length: Definitions and Validity"
- "Mechanisms of Long-Context Information Flow"
- "Mechanistic Failure Modes Limiting ECL"
- "Interpretability and Causal Intervention Preliminaries"
