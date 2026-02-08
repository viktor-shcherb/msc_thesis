# Guidelines for Meta-Analysis

These guidelines describe how to produce synthesis documents in the `meta-analysis/` directory. A meta-analysis synthesizes findings across multiple papers from `references/` to answer a specific research question, trace how a topic evolves over time, and assess the current state of knowledge.

**Relationship to per-paper analyses:** Each `references/*/analysis.md` file describes a single paper. A meta-analysis draws from many such files to build a cross-paper argument. It does not re-summarize individual papers — it synthesizes, compares, and evaluates findings across them.

---

## Ground Truth Rule

The same rule from the reference guidelines applies here with an additional constraint:

**No results, numbers, claims, or statements may be fabricated.** Every factual statement in a meta-analysis must be traceable to a specific per-paper analysis in `references/`. When synthesizing across papers, cite the source paper directory (e.g., `2024-02-lost-in-the-middle`) for every claim. When drawing inferences that go beyond what any single paper states, mark them explicitly as **synthesis inferences** and list the papers from which the inference is derived.

---

## Scope and Purpose

Each meta-analysis must answer a **specific, well-scoped research question** such as:

- How has position bias been characterized, explained, and mitigated across the literature?
- What do synthetic vs. realistic benchmarks tell us about long-context capabilities, and where do they agree or diverge?
- How have context extension methods evolved, and what are their comparative strengths?

A meta-analysis is **not** a literature review that summarizes papers in sequence. It is a structured argument that uses evidence from multiple papers to answer its research question. The unit of analysis is the **finding** or **claim**, not the paper.

---

## Directory Structure

Each meta-analysis lives in its own subdirectory:

```
meta-analysis/
├── GUIDELINES.md               # This file
└── short-descriptive-name/     # One directory per meta-analysis
    └── analysis.md             # The synthesis document
```

Directory names use lowercase words separated by hyphens, derived from the research question (e.g., `position-bias-landscape`, `context-extension-methods`, `benchmark-validity`).

---

## Workflow

When creating a new meta-analysis, follow these steps:

1. **Define the research question.** Write a single sentence framing the question the analysis will answer. The question must be specific enough that you can determine when it has been answered.

2. **Identify the paper corpus.** Use `search.py` to find all relevant papers. Query by category, claims, cross-references, and full-text search. Document the search strategy so the corpus is reproducible.

   ```bash
   # Example: gather papers on position bias
   python3 references/search.py category position-bias
   python3 references/search.py text "position bias"
   python3 references/search.py text "primacy"
   python3 references/search.py text "recency"
   python3 references/search.py claims contested
   ```

3. **Read all per-paper analyses** in the corpus. Do not rely on YAML front matter alone — read the full `analysis.md` for each paper to understand methodology, limitations, and context that metadata does not capture.

4. **Build a timeline.** Order the papers chronologically and identify how the understanding of the topic changed at each step. Note when new evidence confirmed, refined, or contradicted prior claims.

5. **Identify themes.** Group findings into themes that cut across papers (e.g., "mechanistic explanations", "mitigation strategies", "benchmark evidence"). These themes become sections in the analysis.

6. **Write the analysis** following the structure below.

7. **Verify all citations.** Every claim attributed to a paper must be present in that paper's `analysis.md`. Run a final pass to confirm no broken or inaccurate references.

---

## Analysis File (`analysis.md`)

### YAML Front Matter

```yaml
---
title: "Descriptive Title of the Meta-Analysis"
research_question: "Single-sentence research question this analysis answers"
date_produced: YYYY-MM-DD
corpus:
  - 2024-02-lost-in-the-middle
  - 2024-08-found-in-the-middle
  # ... all papers included in this analysis
corpus_search_strategy: |
  category position-bias
  text "position bias"
  text "primacy"
  claims contested
categories: ["cat1", "cat2"]       # from ontology.categories
themes:
  - id: theme-slug
    label: "Human-readable theme name"
  - id: theme-slug-2
    label: "Another theme"
consensus_claims:
  - claim: "Exact claim on which papers agree"
    sources: ["2024-02-lost-in-the-middle", "2025-07-position-bias-transformers"]
    strength: strong                # strong | moderate | weak
contested_claims:
  - claim: "Claim on which papers disagree"
    for: ["2024-02-lost-in-the-middle"]
    against: ["2024-08-found-in-the-middle"]
    resolution: "One sentence on current status"
    resolved: false
gaps:
  - description: "Specific gap in the literature"
    severity: high                  # high | medium | low
overall_confidence:
  - conclusion: "Main conclusion statement"
    level: high                     # high | moderate | low
    basis: "N papers, diverse methods, consistent findings"
    caveats: ["caveat 1", "caveat 2"]
---
```

**Field definitions:**

- `corpus`: Exhaustive list of paper directories included in this analysis.
- `corpus_search_strategy`: The `search.py` queries used to assemble the corpus, so it can be reproduced and updated when new papers are added.
- `categories`: Ontology categories this meta-analysis covers.
- `themes`: The cross-cutting themes used to organize the synthesis. Defined here, referenced in the body.
- `consensus_claims`: Claims where multiple papers converge. `strength` reflects the breadth and quality of supporting evidence:
  - `strong`: 3+ independent papers with consistent evidence across different methods/models.
  - `moderate`: 2+ papers agree, but with caveats (different settings, partial overlap).
  - `weak`: Multiple papers are consistent, but evidence is indirect or limited.
- `contested_claims`: Claims where papers disagree. Include which papers fall on each side and whether the disagreement has been resolved.
- `gaps`: Important questions or areas the corpus does not address.
- `overall_confidence`: Graded confidence in the meta-analysis's main conclusions. `high` = consistent evidence from 3+ papers with diverse methods; `moderate` = 2+ papers agree but with caveats; `low` = limited or conflicting evidence.

### 1. Title Block

```markdown
# Meta-Analysis Title

**Research question:** Single sentence.
**Corpus:** N papers, date range YYYY–YYYY.
**Categories:** category1, category2.
```

### 2. Executive Summary

A self-contained summary of the entire analysis in 5–10 bullet points. Each bullet should state a finding and cite the supporting papers. A reader who reads only this section should understand the current state of the topic.

### 3. Temporal Evolution

A chronological narrative of how understanding of the topic developed. This section answers: *How did we get to the current state of knowledge?*

Organize by **phases** — periods where a distinct set of assumptions or methods dominated. For each phase:

- **Date range and defining papers.** Which papers mark the beginning and end of this phase?
- **Prevailing understanding.** What was believed during this period?
- **Key evidence.** What experiments or theoretical results supported this understanding?
- **Transition.** What finding or paper caused the field to move to the next phase?

Use a timeline table to anchor the narrative:

```markdown
| Year | Paper | Key Contribution | Shift |
|------|-------|-------------------|-------|
| 2024-02 | Lost in the Middle | U-shaped performance curve | Established position bias as a first-class problem |
| 2024-08 | Found in the Middle | Mechanistic explanation via attention | Shifted focus from observation to mechanism |
| ... | ... | ... | ... |
```

### 4. Thematic Synthesis

This is the core of the meta-analysis. Organize by **themes** defined in the YAML front matter, not by paper. Each theme is a subsection (H3).

For each theme:

#### Structure

1. **Statement of the theme.** One sentence defining what this theme covers.
2. **Heterogeneity check.** Before pooling results, assess whether papers are measuring the same construct. If papers use different metrics, thresholds, or task definitions, note this explicitly. Decide whether to: pool results (comparable), report separately (incomparable), or note the discrepancy and interpret cautiously.
3. **Evidence table.** A table comparing how each relevant paper in the corpus addresses this theme:

   ```markdown
   | Paper | Method/Approach | Key Finding | Limitations |
   |-------|-----------------|-------------|-------------|
   | 2024-02-lost-in-the-middle | Multi-doc QA, NQ, 20-doc | U-shaped curve, worst at position 10/20 | Greedy decoding only, pre-2024 models |
   | ... | ... | ... | ... |
   ```

4. **Cross-paper analysis.** Prose synthesizing the evidence:
   - Where do papers **agree**? State the consensus and cite all supporting papers.
   - Where do papers **disagree**? State both positions, the evidence for each, and assess which position is better supported. Do not editorialize — evaluate based on methodological rigor, sample size, model coverage, and replicability.
   - What **moderating factors** explain apparent disagreements? (e.g., different model families, context lengths, task types, evaluation protocols).
5. **Current state.** What is the best-supported conclusion as of the most recent paper in the corpus?

#### Rules for Thematic Synthesis

- **Never summarize a paper in isolation.** Every paragraph should compare, contrast, or connect findings from at least two papers.
- **Cite the specific claim, not just the paper.** Use the claim ID from the paper's YAML front matter when possible (e.g., "C3 from `2024-02-lost-in-the-middle`").
- **Distinguish levels of evidence.** A claim supported by controlled experiments on 10+ models is stronger than a claim from a case study on one model. Make this distinction explicit.
- **Track methodology differences.** When papers reach different conclusions, check whether they used different benchmarks, models, context lengths, or evaluation metrics before concluding they truly disagree.

### 5. Consensus and Disagreements

A structured summary of where the literature converges and diverges. This section corresponds directly to the `consensus_claims` and `contested_claims` in the YAML front matter but provides prose context.

#### Consensus

For each consensus claim:

```markdown
**Claim:** [Statement]
**Supporting papers:** paper1, paper2, paper3
**Evidence strength:** strong / moderate / weak
**Qualification:** [Any important caveats or boundary conditions]
```

#### Active Disagreements

For each contested claim:

```markdown
**Claim:** [Statement]
**Position A (papers):** [Evidence summary]
**Position B (papers):** [Evidence summary]
**Methodological differences:** [How the papers' setups differ -- task type, models, controls]
**Assessment:** [Which position is better supported and why, or why the disagreement remains unresolved]
**Resolution path:** [What experiment or evidence would resolve this disagreement?]
```

### 6. Methodological Patterns

Analyze the **methods** used across the corpus, not just the results. This section answers: *How reliable is the evidence base?*

Cover:

- **Common experimental setups.** What models, benchmarks, and evaluation protocols are most frequently used? Are there blind spots (e.g., all papers test on the same 3 models)?
- **Methodological strengths.** What do the best papers in the corpus do that others do not?
- **Methodological weaknesses.** Recurring limitations across papers (e.g., lack of statistical significance testing, narrow model selection, synthetic-only evaluation).
- **Benchmark coverage matrix.** A table showing which benchmarks each paper uses, revealing overlap and gaps:

  ```markdown
  | Paper | NIAH | RULER | LongBench | InfiniteBench | Realistic Tasks |
  |-------|------|-------|-----------|---------------|-----------------|
  | paper1 | x | x | | | |
  | paper2 | | x | x | x | |
  | ... | ... | ... | ... | ... | ... |
  ```

### 7. Gaps and Open Questions

Enumerate what the corpus does **not** address. For each gap:

- **Description.** What is missing?
- **Severity.** How much does this gap limit our understanding? (`high` / `medium` / `low`)
- **Potential approach.** How might this gap be addressed? (Brief, not a full proposal.)
- **Related open questions.** Link to `open_questions` from per-paper analyses that feed into this gap.

## Style Rules

All style rules from `prompts/add_reference/write_analysis/prompt.md` apply, plus:

1. **Synthesis over summary.** Every paragraph must connect findings from multiple papers. If you find yourself describing a single paper for more than two sentences, you are summarizing, not synthesizing.
2. **Cite paper directories, not author names, for traceability.** Use the format `2024-02-lost-in-the-middle` in the text body so references are machine-searchable. Author names (e.g., "Liu et al.") may be used alongside for readability: "Liu et al. (`2024-02-lost-in-the-middle`) found that..."
3. **Quantify when possible.** "Most papers find X" is less useful than "5 of 7 papers find X; the two exceptions (paper1, paper2) used shorter contexts."
4. **Explicit evidence grading.** When stating a consensus, always qualify the strength: how many papers, how diverse the methods, how consistent the results.
5. **Tables for comparison, prose for interpretation.** Use tables to lay out the evidence, then use prose to explain what the table reveals.
6. **Temporal markers.** When describing the evolution of understanding, always note dates: "As of 2024-08, the mechanistic explanation from `2024-08-found-in-the-middle` had not yet been independently replicated."
7. **No orphan claims.** Every claim in the meta-analysis must trace back to at least one per-paper analysis. If you identify an insight that no single paper states but that emerges from the combination, mark it as a **synthesis inference** and list all contributing papers.
8. **Acknowledge heterogeneity.** When papers use different definitions, metrics, or thresholds for the same concept (e.g., "effective context length"), note this explicitly before comparing their results. Large variance in reported effects often reflects measurement heterogeneity, not genuine uncertainty about the phenomenon.

---

## Maintenance

### When new papers are added to `references/`

1. Check whether the new paper falls within the corpus of any existing meta-analysis (match on categories, cross-references, or keyword overlap).
2. If it does, update the affected meta-analysis:
   - Add the paper to the `corpus` list in the YAML front matter.
   - Integrate its findings into the relevant thematic sections.
   - Re-evaluate any `contested_claims` — the new paper may shift the balance.
   - Update `consensus_claims` strength if the new paper provides additional evidence.
   - Check whether any `gaps` have been addressed.
   - Update `overall_confidence` if the new evidence changes certainty.
3. Record the update date in `date_produced`.

### When new evidence contradicts existing conclusions

If a new paper contradicts a consensus claim:

1. **Assess heterogeneity first.** Check whether the contradiction stems from methodological differences (different benchmarks, models, metrics) rather than genuine disagreement about the same phenomenon.
2. **If genuinely contradictory:** Move the claim from `consensus_claims` to `contested_claims`. Document both positions with evidence.
3. **If methodologically explained:** Keep the consensus claim but add a qualification noting the scope conditions under which it holds.
4. **Update the thematic synthesis** to reflect the new state of evidence, including the moderating factors that explain divergent findings.

### Completeness checklist

Before considering a meta-analysis complete, verify:

- [ ] The research question is specific and answerable.
- [ ] The corpus search strategy is documented and reproducible.
- [ ] Every paper in the corpus has been read (full `analysis.md`, not just front matter).
- [ ] The temporal evolution section covers the full date range of the corpus.
- [ ] Every theme in the YAML front matter has a corresponding section in the body.
- [ ] Every consensus claim cites 2+ papers with specific evidence.
- [ ] Every contested claim presents both sides with evidence.
- [ ] The methodological patterns section includes a benchmark coverage matrix.
- [ ] Gaps are enumerated with severity ratings.
- [ ] All paper references use directory names and are verifiable in `references/`.
- [ ] No single-paper summaries appear — every paragraph synthesizes across papers.
- [ ] Synthesis inferences are marked and sourced.
- [ ] Overall confidence is graded for main conclusions with explicit basis and caveats.
- [ ] Heterogeneity is assessed before pooling results across papers with different methodologies.
