# Guidelines for Reference Analysis

These guidelines describe how to write the `source.md` and `analysis.md` files for a paper or contribution added to the `references/` directory.

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

1. **Create the subdirectory** following the `YYYY-MM-short-descriptive-name/` pattern.
2. **Download the paper PDF** into the subdirectory. Use the arXiv ID as the filename (e.g., `2302.00093.pdf`). If no arXiv version exists, use the DOI-based or proceedings PDF. Skip this step only if no PDF is publicly available (e.g., some blog posts or Reddit contributions).
3. **Write `source.md`** with bibliographic metadata (see below).
4. **Read the PDF thoroughly**, then write `analysis.md` following the structure below. Always base the analysis on the actual paper content, not summaries or abstracts alone.

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

Every analysis must contain the following sections in order:

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
- Add subsections as needed for the specific paper (e.g., "Comparison with Prior Methods", "Limitations", "Follow-Up Contributions", "Impact and Adoption").

### 5. Conclusions

Numbered list of the paper's main contributions and implications. Each item should:

- Open with a **bold phrase** summarizing the point.
- Follow with one to two sentences of explanation.
- Cover both the direct technical contribution and any broader implications.

### 6. Core References and Why They Are Referenced

Group references by role using H3 headers (e.g., "Positional Encoding Foundations", "Direct Predecessors", "Models Used in Evaluation", "Evaluation Benchmarks"). For each reference:

```markdown
- **Author et al. (Year)** -- *Paper Title.* One to two sentences explaining why this reference matters to the paper being analyzed.
```

If this paper is part of a lineage with other analyzed references, add a subsection:

#### Cross-References in Available Papers

Describe how the paper is cited or used in other papers within the `references/` directory and vice versa, with specific section and table references.

---

## Style Rules

1. **Accuracy over brevity.** Include specific numbers, equations, and parameter values. Vague summaries are not useful.
2. **Use the paper's own notation.** Do not invent new variable names. If the paper writes `theta_d`, use `theta_d`.
3. **Reproduce key equations.** Use blockquotes for the most important formulas. Inline math (e.g., `b' = b * s^(|D|/(|D|-2))`) is acceptable for shorter expressions.
4. **Tables for comparisons.** Always present quantitative comparisons in markdown tables, not prose.
5. **Bold for emphasis.** Use bold for key terms and the core insight of each section.
6. **No editorializing.** Report what the paper claims and demonstrates. Do not inject personal opinions about the quality of the work.
7. **Horizontal rules.** Use `---` between major sections for visual separation.
8. **Concrete over abstract.** Prefer "0.5-2% of pretraining tokens" over "a small fraction of pretraining compute."
9. **Reference format.** Use `Author et al. (Year)` in text. Include the short title in italics after a double dash.
10. **Consistent structure.** Follow the section order defined above. Readers should be able to find the same information in the same place across all analyses.
