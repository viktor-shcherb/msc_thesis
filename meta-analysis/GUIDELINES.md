# Guidelines for Meta-Analysis

These guidelines define how to produce synthesis documents in `meta-analysis/`.
Each meta-analysis must support two thesis needs at the same time:

1. a rigorous literature review narrative (`Related Work`)
2. an evaluative argument for analysis/discussion chapters (`Results`/`Discussion`)

Meta-analyses in this repository are expected to focus on long-context modeling,
effective context evaluation, and mechanistic interpretability.

**Relationship to per-paper analyses:** each `references/*/analysis.md` file
describes one paper. A meta-analysis builds a cross-paper argument from many
such files. Do not rewrite single-paper summaries in sequence.

---

## Ground Truth Rule

No results, numbers, claims, or statements may be fabricated.

Every factual statement in a meta-analysis must be traceable to specific
per-paper analyses in `references/`. Use paper directory names in the body
(for example, `2024-02-lost-in-the-middle`) for auditability.

If an argument goes beyond any one paper, mark it explicitly as a
**synthesis inference** and list all contributing papers.

---

## Thesis Alignment Requirement

Every meta-analysis must produce outputs that can be dropped into thesis text
with minimal editing.

Required outputs per `analysis.md`:

1. **Literature review output:** historical evolution, core themes,
   consensus/disagreement map, boundary conditions.
2. **Analysis output:** explicit evaluation of evidence quality, causal strength,
   and implications for effective context evaluation design.
3. **Traceability output:** claim-to-source mapping so all thesis statements can
   be verified quickly.

If a section does not help at least one of these outputs, tighten or remove it.

---

## Scope and Purpose

Each meta-analysis must answer one specific research question, such as:

- How has position bias been characterized, explained, and mitigated?
- What do synthetic vs realistic long-context benchmarks agree on?
- Which mechanistic findings actually explain effective-context degradation?
- Which context-extension methods improve effective (not just claimed) context?

A meta-analysis is not a chronological paper-by-paper summary. The unit of
analysis is the finding/claim and its evidence quality.

---

## Directory Structure

```
meta-analysis/
|-- GUIDELINES.md               # this file
`-- short-descriptive-name/
    `-- analysis.md
```

Directory names use lowercase hyphenated words, derived from the question
(for example, `context-extension-methods`, `benchmark-length-construction`).

---

## Workflow

When creating or updating a meta-analysis, follow this order:

1. **Define the research question and thesis target.**
   Write one sentence for the question and one sentence for why this analysis
   is needed for thesis writing.

2. **Assemble a reproducible corpus.**
   Use `references/search.py` and record all queries.

   ```bash
   python3 references/search.py category long-context-evaluation
   python3 references/search.py category mechanistic-interpretability
   python3 references/search.py text "effective context length"
   python3 references/search.py text "position bias"
   python3 references/search.py text "retrieval head"
   ```

3. **Document inclusion and exclusion criteria.**
   State why each paper class is in or out (for example, evaluation-only papers,
   mechanism-only papers, model reports without controlled evaluation).

4. **Read all per-paper analyses in full.**
   Do not rely on YAML only.

5. **Run a coverage audit before synthesis.**
   Check that your corpus covers all relevant axes:
   - task axis: retrieval, reasoning, generation, in-context learning
   - benchmark axis: synthetic controllable, natural realistic, causal-control
   - evidence axis: empirical, theoretical, mechanistic-interventional
   - model axis: scale range, open vs closed, architecture families
   If one axis is weak, report the gap explicitly.

6. **Build a timeline and theme map.**
   Identify phase transitions and cross-paper themes.

7. **Build a claim ledger.**
   For each major claim, record supporting papers, contradictory papers,
   evidence type, and boundary conditions.

8. **Write the synthesis using the structure below.**

9. **Verify traceability and consistency.**
   Ensure every claim can be traced back to corpus papers.

---

## Analysis File (`analysis.md`)

### YAML Front Matter

```yaml
---
title: "Descriptive title"
research_question: "Single-sentence question answered by this meta-analysis"
thesis_objective: "How this analysis supports thesis literature review and analysis sections"
date_produced: YYYY-MM-DD
corpus:
  - 2024-02-lost-in-the-middle
  - 2025-04-effective-context-length-falls-short
  # ... exhaustive list
corpus_search_strategy: |
  category long-context-evaluation
  category mechanistic-interpretability
  text "effective context"
  text "position bias"
inclusion_criteria:
  - "Criterion 1"
  - "Criterion 2"
exclusion_criteria:
  - "Criterion 1"
categories: ["long-context-evaluation", "mechanistic-interpretability"]
themes:
  - id: theme-slug
    label: "Human-readable theme name"
consensus_claims:
  - claim: "Exact statement of agreement"
    sources: ["2024-02-lost-in-the-middle", "2025-07-position-bias-transformers"]
    strength: strong      # strong | moderate | weak
contested_claims:
  - claim: "Exact statement of disagreement"
    for: ["paper-a", "paper-b"]
    against: ["paper-c"]
    resolution: "Current status in one sentence"
    resolved: false
evaluation_validity_summary:
  construct_validity: "high: definition of effective length is mostly consistent across key papers"
  causal_validity: "moderate: few direct causal-isolation experiments"
  external_validity: "moderate: synthetic-heavy corpus with limited realistic tasks"
mechanistic_evidence_summary:
  interventional_papers: ["paper-a", "paper-b"]  # ablation/patching/masking interventions
  observational_papers: ["paper-c"]              # attention patterns/correlations only
  theoretical_papers: ["paper-d"]                # formal analysis
thesis_mapping:
  literature_review:
    - claim: "High-level thesis-ready claim"
      sources: ["paper-a", "paper-b"]
  analysis_section:
    - claim: "Evaluative claim for discussion chapter"
      sources: ["paper-c", "paper-d"]
      uncertainty: "Main caveat/assumption"
gaps:
  - description: "Specific gap in current evidence"
    severity: high       # high | medium | low
overall_confidence:
  - conclusion: "Main conclusion statement"
    level: high          # high | moderate | low
    basis: "N papers, method diversity, consistency"
    caveats: ["caveat 1", "caveat 2"]
---
```

### Field Definitions

- `thesis_objective`: one sentence linking this document to thesis writing.
- `inclusion_criteria` / `exclusion_criteria`: make corpus boundaries explicit.
- `evaluation_validity_summary`: quick quality judgment on effective-context
  evaluation evidence (construct/causal/external validity).
- `mechanistic_evidence_summary`: separate interventional, observational, and
  theoretical mechanism evidence.
- `thesis_mapping`: direct, thesis-ready claims for:
  - literature review narrative
  - analysis/discussion argument

---

## Required Structure in `analysis.md`

### 1. Title Block

```markdown
# Meta-analysis title

**Research question:** single sentence.
**Thesis objective:** single sentence.
**Corpus:** N papers, date range YYYY-YYYY.
**Categories:** category1, category2.
```

### 2. Executive Summary

5-10 bullets, each with a claim and paper-directory citations.

### 3. Thesis-Ready Outputs

This section is mandatory and has two subsections:

1. **For literature review (related work):**
   - 1-2 paragraphs with the most defensible storyline.
   - include what changed over time and why.
   - include major agreement and one unresolved disagreement.
2. **For analysis/discussion:**
   - 1-2 paragraphs with explicit evaluative claims.
   - state what current evidence implies for effective context evaluation design.
   - state key uncertainty that limits strong conclusions.

Write this section in near-final thesis prose.

### 4. Temporal Evolution

Chronological narrative with phase transitions:

- date range and defining papers
- prevailing assumptions
- key evidence
- what changed the field

Include a timeline table:

```markdown
| Year | Paper | Key Contribution | Shift |
|------|-------|------------------|-------|
| 2024-02 | 2024-02-lost-in-the-middle | U-shaped degradation | Position bias became first-class |
```

### 5. Thematic Synthesis

Organize by themes (from YAML), not by paper.

For each theme:

1. one-sentence theme statement
2. heterogeneity check (metrics/thresholds/task definitions)
3. evidence table
4. cross-paper synthesis (agreement, disagreement, moderators)
5. best-supported current conclusion

Rules:

- every paragraph must connect at least two papers
- cite claim IDs from per-paper analyses when available
- separate evidence quality from claim popularity
- report boundary conditions (model family, scale, benchmark, length regime)

### 6. Consensus and Active Disagreements

Map directly to `consensus_claims` and `contested_claims`.

For each contested claim, include:

- position A evidence
- position B evidence
- methodological differences
- current assessment
- concrete resolution path (what experiment would settle it)

### 7. Effective Context Evaluation Validity Audit

This section is mandatory for long-context work.

Include:

1. **Construct validity table** (what is "effective context" in each paper?)
2. **Confound audit** (what covaries with length?)
3. **Causal evidence ladder**:
   - Level A: direct causal isolation (controls/interventions)
   - Level B: controlled but non-isolating comparisons
   - Level C: observational correlations
4. **External validity judgment**:
   - what transfers to realistic tasks
   - what is synthetic-only

Suggested table:

```markdown
| Paper | Effective-length definition | Length manipulation | Main confound | Causal level |
|------|------------------------------|---------------------|---------------|--------------|
| paper-a | 85% threshold on task score | haystack padding | lexical overlap | B |
```

### 8. Mechanistic Interpretability Evidence Synthesis

This section is mandatory when mechanism claims are in scope.

For each mechanism (for example: position bias, over-squashing, retrieval
heads, attention sinks):

1. mechanism statement
2. evidence type and strength:
   - interventional (ablation, patching, masking): strongest
   - theoretical formalization
   - observational analysis: weakest causal status
3. what behavior the mechanism explains
4. what remains unexplained

Suggested table:

```markdown
| Mechanism | Papers | Evidence type | Causal strength | Explains | Open limits |
|----------|--------|---------------|-----------------|----------|-------------|
| retrieval heads | paper-a | interventional | high | factual retrieval failures | cross-model generalization |
```

### 9. Methodological Patterns

Assess the reliability of the whole corpus:

- common setups and blind spots
- recurring strengths and weaknesses
- benchmark coverage matrix
- reproducibility signals (code/data availability, seed reporting)

### 10. Gaps and Open Questions

For each gap:

- description
- severity (`high` / `medium` / `low`)
- why it matters for thesis claims
- minimal experiment/evidence needed to reduce uncertainty

---

## Style Rules

All style rules from `prompts/add_reference/write_analysis/prompt.md` apply.
In addition:

1. **Synthesis over summary.** Do not spend more than two consecutive sentences
   on one paper unless absolutely necessary.
2. **Traceable citations.** Use paper directory names in body text.
3. **Quantify scope.** Replace "many papers" with explicit counts.
4. **Separate claimed vs effective context.** Never use "context length"
   ambiguously when numbers matter.
5. **Separate capability vs proxy metrics.** Do not treat perplexity or passkey
   scores as direct capability evidence without justification.
6. **Label inference type.** Distinguish:
   - direct paper claim
   - synthesis inference
   - thesis implication
7. **Be explicit about uncertainty.** State what is unknown, not only what is
   known.
8. **Use absolute dates** (`YYYY-MM` or `YYYY-MM-DD`) when describing shifts.
9. **No orphan claims.** Every substantive claim must map to corpus evidence.

---

## Maintenance

### When new papers are added to `references/`

1. Check whether the paper fits existing corpora by category, claims, and text.
2. If it fits:
   - add it to `corpus`
   - update themes, consensus, and contested claims
   - update validity and mechanistic summaries
   - update `thesis_mapping` outputs
   - refresh `date_produced`

### When new evidence contradicts existing conclusions

1. First test whether disagreement is methodological or substantive.
2. If substantive:
   - move claim from `consensus_claims` to `contested_claims`
   - document both positions and evidence quality
3. If methodological:
   - keep consensus claim but qualify scope conditions clearly

---

## Completeness Checklist

Before marking a meta-analysis complete, verify:

- [ ] Research question and thesis objective are explicit.
- [ ] Corpus search strategy is reproducible.
- [ ] Inclusion and exclusion criteria are documented.
- [ ] Full per-paper analyses were read (not YAML only).
- [ ] Coverage audit across task/benchmark/evidence/model axes is complete.
- [ ] Temporal evolution covers full corpus date range.
- [ ] Every YAML theme has a body section.
- [ ] Consensus claims cite 2+ papers and include evidence strength.
- [ ] Contested claims present both sides and a resolution path.
- [ ] Effective-context validity audit is present.
- [ ] Mechanistic evidence synthesis is present (if mechanisms are in scope).
- [ ] Methodological patterns include benchmark coverage and reproducibility notes.
- [ ] Gaps include severity and why they matter for thesis conclusions.
- [ ] `thesis_mapping` includes both literature-review and analysis outputs.
- [ ] All claims are traceable to paper directories.
- [ ] Synthesis inferences and thesis implications are explicitly labeled.
- [ ] Overall confidence is graded with basis and caveats.
