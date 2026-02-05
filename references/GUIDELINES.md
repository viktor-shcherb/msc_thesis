# Guidelines for Reference Analysis

These guidelines describe how to write the `source.md` and `analysis.md` files for a paper or contribution added to the `references/` directory.

---

## Ground Truth Rule

**No results, numbers, claims, or statements may be fabricated.** Everything in an `analysis.md` file must be traceable to the paper text. If the paper does not report a number, do not invent one. If a claim is ambiguous, flag the ambiguity rather than resolving it editorially. Quote the paper where precision matters (equations, key definitions, exact metrics). When describing implications or limitations not explicitly stated by the authors, mark them clearly as inferences.

---

## Directory Structure

Each reference lives in its own subdirectory named with the pattern:

```
YYYY-MM-short-descriptive-name/
```

- `YYYY-MM` is the publication year and month.
- The short name uses lowercase words separated by hyphens, derived from the paper's title or commonly used abbreviation (e.g., `2023-06-pi-positional-interpolation`, `2024-05-yarn-context-extension`).

Place the `source.md`, `analysis.md`, and paper PDF at the root of this subdirectory.

---

## Workflow

When adding a new reference, follow these steps in order:

1. **Determine the correct publication date first.** Before creating any directory, verify the publication date by checking the paper PDF, arXiv page, or venue proceedings. Use the peer-reviewed publication date when available (e.g., conference date, not arXiv submission date). Only after confirming the correct `YYYY-MM` should you proceed.
2. **Create the subdirectory** following the `YYYY-MM-short-descriptive-name/` pattern. Double-check that the slug matches the verified date before proceeding.
3. **Download the paper PDF** into the subdirectory. Use the arXiv ID as the filename (e.g., `2302.00093.pdf`). If no arXiv version exists, use the DOI-based or proceedings PDF. Skip this step only if no PDF is publicly available (e.g., some blog posts or Reddit contributions).
4. **Write `source.md`** with bibliographic metadata (see below). **Verify the directory slug matches the publication date** in `source.md`. If they differ, rename the directory now before proceeding further.
5. **Add a `cite.bib` file** with the BibTeX entry for this reference. The citation key **must match the directory name** (e.g., `2024-02-lost-in-the-middle`). This allows citing with `\cite{2024-02-lost-in-the-middle}`. If the venue has a `@string` macro defined in `references/_venues.bib`, use the macro name (e.g., `booktitle = NeurIPS`). If the venue is a major conference or journal not yet in `_venues.bib`, add a new `@string` definition there. Only spell out the full venue name inline for one-off venues (e.g., workshops). Run `make references.bib` to regenerate the combined bibliography.
6. **Read the PDF thoroughly**, then write `analysis.md` following the structure below. Always base the analysis on the actual paper content, not summaries or abstracts alone.
   - **Check the PDF length first.** Before reading, check how many pages the PDF has (e.g., using `pdfinfo` or by reading the first page and noting the total). If the PDF is long (roughly >10 pages including appendices), do **not** attempt to read and process it in a single pass.
   - **Split long PDFs into parts.** For long papers, divide the reading into roughly equal parts. Process each part separately in parallel, extracting the relevant information for the corresponding `analysis.md` sections.
   - **Aggregate into the final file.** After all parts have been processed, combine the extracted information into the complete `analysis.md`. Verify consistency across parts (e.g., notation, claim numbering, cross-references) during this aggregation step.
7. **Update the YAML front matter** in the new `analysis.md` (see "YAML Front Matter" below).
8. **Update cross-references** in other papers' `analysis.md` front matter to reflect the new paper (see "Metadata Maintenance" below).

---

## Source File (`source.md`)

Every reference must include a `source.md` file containing bibliographic metadata. Follow this structure:

### 1. Title Block

```markdown
# Full Paper Title

**Authors:** Name1, Name2, Name3
**Affiliation(s):** Institution1, Institution2
```

Use `**Affiliation:**` (singular) when all authors share one institution, `**Affiliations:**` (plural) when multiple institutions are involved.

### 2. Publication Status

A bullet list covering:

```markdown
## Publication Status

- **arXiv preprint:** Month Year, arXiv:XXXX.XXXXX (if applicable)
- **Peer-reviewed:** Yes / No
- **Conference/Journal:** Full venue name with year, volume, pages, location, and dates (if peer-reviewed)
- **Status:** One of: Preprint / Published conference paper / Published journal paper / Informal community contribution
```

For unpublished or informal contributions, add a note explaining the publication context (e.g., that a Reddit post was later formalized in a peer-reviewed paper, or that an influential preprint remains unpublished).

### 3. Preferred Citation

Provide the recommended citation in a blockquote. Prefer the peer-reviewed version when available:

```markdown
## Preferred Citation

Cite the [Venue Year] version:

> Author, A., Author, B., & Author, C. (Year). Title. In Venue, Volume:Pages.
```

For informal contributions, include both a direct citation and a pointer to any formalized version.

### 4. Additional Sections (as needed)

- **Related Contributions by Same Author:** When the contribution is part of a series (e.g., community follow-ups).
- **Notes:** Any additional context about publication history, retractions, or version differences.

### 5. Links

```markdown
## Links

- arXiv: https://arxiv.org/abs/XXXX.XXXXX
- Proceedings: https://...
- Code: https://github.com/...
- Dataset: https://...
```

Include all relevant URLs: arXiv, official proceedings (PMLR, ACL Anthology, OpenReview, DOI), code repositories, datasets, blog posts, or Reddit threads.

### Source Style Rules

1. **Use the peer-reviewed publication date** for the directory name when available (e.g., `2024-05-yarn-context-extension` for an ICLR 2024 paper, not the arXiv date).
2. **Be precise about venue names.** Include full conference name, year, pages, and location when known.
3. **Distinguish publication status clearly.** A "Findings" paper is peer-reviewed. An arXiv preprint without venue acceptance is not.
4. **Keep it factual and concise.** The `source.md` is metadata only -- save analysis for `analysis.md`.

---

## Analysis File (`analysis.md`)

Every analysis must begin with a **YAML front matter block** (see next section) and then contain the following sections in order:

### YAML Front Matter

Every `analysis.md` must begin with a YAML front matter block enclosed in `---` delimiters. This block holds structured metadata used by `search.py` for cross-referencing, categorization, and search. See the schema below.

```yaml
---
title: "Full Paper Title"
authors: "Last1, Last2, Last3"
year: YYYY
venue: "Venue Name Year"
paper_type: conference-paper   # from ontology.paper_types
categories: ["cat1", "cat2"]   # from ontology.categories
scope: ["freeform scope 1"]   # freeform scope constraints
benchmarks_used: ["bench1"]    # from ontology.benchmarks
models_introduced: ["model1"]  # from ontology.models (if any)
models_evaluated: ["model2"]   # from ontology.models (if any)
key_claims:
  - id: C1
    claim: "Exact claim, traceable to paper"
    evidence: "Table 2, Section 4"
    status: supported           # supported | contested | unvalidated
    contested_by: YYYY-MM-ref   # if contested (optional)
    scope: "32K+ context, greedy decoding"  # conditions under which claim holds (optional)
    magnitude: "50% utilization"            # effect size when quantifiable (optional)
cross_references:
  - target: YYYY-MM-other-ref
    type: extends               # from ontology.relationship_types
    detail: "One sentence explaining the relationship"
open_questions:
  - question: "..."
    addressed_by: YYYY-MM-ref   # or null if unresolved
---
```

All category, benchmark, model, and relationship type identifiers must come from the controlled vocabularies defined in `references/metadata.yaml`. If a new identifier is needed, add it to the ontology first.

### 1. Title Block

```markdown
# Full Paper Title

**Authors:** Name1, Name2 (Affiliation1, Affiliation2)
**Date:** Month Year, arXiv:XXXX.XXXXX (or venue and DOI)
```

For non-peer-reviewed contributions (blog posts, Reddit posts, GitHub PRs), also include:

```markdown
**Type:** Reddit post / Blog post / GitHub PR (not a formal peer-reviewed paper)
**URL:** direct link
```

Add a brief note on how the contribution was later formalized, if applicable.

### 2. Core Research Problem

State the specific problem the paper addresses. This section should:

- Identify the concrete technical limitation or gap.
- Explain *why* the problem exists (root cause, not just symptoms).
- Reference prior work that attempted to solve it and where those attempts fall short.
- End with a bold statement framing the core challenge, e.g.: **how to extend context windows of RoPE-based LLMs with maximal compute efficiency.**

### 3. Problem Solutions

Summarize the paper's solution at a high level. This section should:

- State the key idea in one or two sentences.
- List the main components or observations the solution is built on (numbered list).
- Stay conceptual -- save implementation details for the next section.

### 4. Approach Details

This is the longest section. Organize it with the following subsections:

#### Method
- Describe the concrete procedure or algorithm.
- Use mathematical notation where the paper does; reproduce key equations.
- Use blockquotes (`>`) for important formulas.

#### Key Technical Components
- Explain each non-obvious component (e.g., normalization tricks, temperature scaling, dynamic inference strategies).
- Include parameter values and hyperparameter choices that are important for reproducibility.

#### Theoretical Analysis (if applicable)
- State the main theorems, propositions, or lemmas with their implications.
- Focus on what the results mean, not full proofs.

#### Experimental Setup
- Models, sizes, datasets, training details (steps, learning rate, hardware).
- Evaluation benchmarks and metrics.
- **Reproducibility:** Note code/data availability, whether seeds are reported, and any missing details that would impede replication.

#### Key Results
- Present a comparison table with the proposed method vs. the strongest baselines.
- Use the format:

```markdown
| Setting | Proposed Method | Best Baseline |
|---|---|---|
| ... | ... | ... |
```

- Follow the table with bullet points highlighting the most important takeaways.

#### Additional Subsections
- Add subsections as needed for the specific paper (e.g., "Comparison with Prior Methods", "Follow-Up Contributions", "Impact and Adoption").

### 5. Limitations and Failure Modes

Describe the paper's limitations, negative results, and known failure modes. This section should:

- List limitations explicitly acknowledged by the authors.
- Note any failure modes observed in the experiments (e.g., tasks where the method underperforms baselines).
- Identify assumptions or constraints that limit generalizability.

If the paper does not discuss limitations, state this explicitly.

#### Scope and Comparability (optional but recommended)

When relevant for meta-analysis, note:

- **What was not tested:** Models, scales, conditions, or settings excluded from evaluation (whether or not authors acknowledge this).
- **Comparability notes:** How this paper's experimental setup differs from related work in ways that affect cross-paper comparison (e.g., different effective-length thresholds, different baseline definitions, different decoding strategies).

### 6. Conclusions

Split into two subsections:

#### Contributions

Numbered list of what the paper **established** — direct technical contributions supported by evidence. Each item should:

- Open with a **bold phrase** summarizing the point.
- Follow with one to two sentences of explanation.

#### Implications

Numbered list of what the paper **suggests** — broader implications that may be contested or require further validation. Mark speculative implications as such.

### 7. Key Claims

Discrete numbered claims extracted from the paper, each with:

- The claim statement (traceable to a specific section, figure, or table).
- The evidence supporting it.
- Status: `supported`, `contested`, or `unvalidated`.
- **Scope conditions** (when relevant): Under what conditions does the claim hold? E.g., "greedy decoding only," "7B--70B scale," "synthetic benchmarks."
- **Effect magnitude** (when quantifiable): The size of the effect, e.g., "20 percentage point drop," "50% utilization ratio."

This section mirrors the `key_claims` field in the YAML front matter but in human-readable prose. Keep them consistent.

### 8. Open Questions

Questions raised by the paper that remain unresolved, or questions the paper explicitly leaves for future work. For each question, note whether it has been addressed by subsequent work in the `references/` directory.

### 9. Core References and Why They Are Referenced

Group references by role using H3 headers (e.g., "Positional Encoding Foundations", "Direct Predecessors", "Models Used in Evaluation", "Evaluation Benchmarks"). For each reference:

```markdown
- **Author et al. (Year)** -- *Paper Title.* One to two sentences explaining why this reference matters to the paper being analyzed.
```

---

## Style Rules

1. **Accuracy over brevity.** Include specific numbers, equations, and parameter values. Vague summaries are not useful.
2. **Use the paper's own notation.** Do not invent new variable names. If the paper writes `theta_d`, use `theta_d`.
3. **Reproduce key equations.** Use blockquotes for the most important formulas. Inline math (e.g., `b' = b * s^(|D|/(|D|-2))`) is acceptable for shorter expressions.
4. **Tables for comparisons.** Always present quantitative comparisons in markdown tables, not prose.
5. **Bold for emphasis.** Use bold for key terms and the core insight of each section.
6. **No editorializing, but do assess methodology.** Report what the paper claims and demonstrates. Do not inject opinions about paper quality. However, *do* note objective methodological concerns (e.g., "no variance estimates reported," "single model tested," "greedy decoding only") -- these are factual observations that inform evidence quality, not editorial judgments.
7. **Horizontal rules.** Use `---` between major sections for visual separation.
8. **Concrete over abstract.** Prefer "0.5-2% of pretraining tokens" over "a small fraction of pretraining compute."
9. **Reference format.** Use `Author et al. (Year)` in text. Include the short title in italics after a double dash.
10. **Consistent structure.** Follow the section order defined above. Readers should be able to find the same information in the same place across all analyses.
11. **Capture negative results explicitly.** If the paper reports cases where the method fails, underperforms, or produces unexpected results, include them in the "Limitations and Failure Modes" section. Negative results are as informative as positive ones.
12. **Distinguish claims from evidence.** When reporting a finding, always cite the specific table, figure, or section where the evidence appears. Use the format: "Method X improves by Y% (Table Z, Section W)." Do not present claims without evidence pointers.
13. **Note evidence breadth.** When a claim rests on limited evidence (e.g., one model, one benchmark, no ablation), note this. When evidence is strong (multiple models, controlled ablations, statistical testing), note that too. This information is critical for meta-analysis.

---

## Metadata Maintenance

### Ontology (`metadata.yaml`)

The file `references/metadata.yaml` contains the shared ontology: controlled vocabularies for categories, paper types, relationship types, benchmarks, and models. Per-paper metadata lives in the YAML front matter of each `analysis.md` file.

**When to update the ontology:**

- When a new paper introduces a category, benchmark, or model not yet in the vocabulary.
- Add the new identifier to the relevant list in `metadata.yaml` with a short description.
- Then use the new identifier in the paper's `analysis.md` front matter.

**When adding a new reference:**

1. Write the YAML front matter for the new `analysis.md` using existing ontology identifiers. Add new identifiers to `metadata.yaml` if needed.
2. Add `cross_references` entries in the new paper's front matter pointing to related papers already in the directory.
3. **Update existing papers' front matter** to add reciprocal cross-references. For example, if the new paper extends Paper A, add an `extended-by` entry in Paper A's front matter pointing to the new paper.
4. **Update affected meta-analyses.** Check whether the new paper falls within the corpus of any existing meta-analysis in `meta-analysis/` (match on categories, cross-references, or keyword overlap). If it does, follow the maintenance procedure in `meta-analysis/GUIDELINES.md` § "Maintenance": add the paper to the corpus, integrate its findings into relevant thematic sections, and re-evaluate consensus and contested claims.

**Relationship type conventions:**

- `extends` / `extended-by`: Direct methodological lineage.
- `contradicts`: Findings are in tension. Include the specific claim and evidence.
- `uses-benchmark`: This paper uses a benchmark introduced by the target.
- `evaluates`: This paper evaluates a model or method from the target.
- `concurrent`: Published around the same time addressing similar questions.
- `complementary`: Related problem, different approach.
- `formalizes`: Provides theoretical grounding for empirical findings.

### Validating metadata

Run `search.py` to verify cross-references are consistent:

```bash
# Check a specific paper's relationships
python3 references/search.py related 2024-05-yarn-context-extension

# Verify no broken references
python3 references/search.py info <dir-name>

# List all contradictions
python3 references/search.py contradictions
```

---

## Search Script Usage

The `references/search.py` script reads YAML front matter from all `analysis.md` files and the ontology from `metadata.yaml`. It requires PyYAML.

### Commands

```bash
# Find papers by category
python3 references/search.py category context-extension

# Find papers using a benchmark
python3 references/search.py benchmark ruler

# Find papers introducing or evaluating a model
python3 references/search.py model llama-2-7b

# Trace methodological lineage (extends/extended-by chains)
python3 references/search.py lineage 2023-06-pi-positional-interpolation

# Find all contradictions between papers
python3 references/search.py contradictions

# List key claims by status
python3 references/search.py claims contested
python3 references/search.py claims unvalidated

# List open questions
python3 references/search.py open-questions --unresolved

# Full-text search across titles, claims, and details
python3 references/search.py text "attention sink"

# Show full metadata for a paper
python3 references/search.py info 2024-05-yarn-context-extension

# Show all cross-references (both directions) for a paper
python3 references/search.py related 2024-05-yarn-context-extension
```
