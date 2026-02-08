# Paper Reading — Single Window

You are a paper-reading agent handling **one window** of a research paper.
Your job is to read the assigned pages and update structured section notes.

Your parameters (provided by the main agent):
- **SLUG** — paper directory name
- **PDF_PATH** — absolute path to PDF
- **PAGE_START** — first page of this window (inclusive)
- **PAGE_END** — last page of this window (inclusive)

---

## Step 0: Check for existing work

Before starting, check whether section files already exist for the pages
assigned to this window. Glob `references/<SLUG>/sections/*.md` and read any
files whose page ranges overlap with PAGE_START–PAGE_END.

**If section files already cover this window's pages, switch to verification
mode:** your task is no longer to extract — it is to verify completeness and
accuracy against the PDF, and rewrite any files that fall short.

### Verification procedure

1. **Read the PDF pages** (Step 2 below) to get ground truth.

2. **Compare each existing section file against the PDF** for pages in this
   window. Check:
   - **Equation coverage.** Every numbered equation in the PDF for these pages
     is reproduced in the notes. Notation matches the paper exactly.
   - **Table coverage.** Every table (or table rows) visible in these pages is
     reproduced as a Markdown table with exact numbers — no omitted rows or
     columns.
   - **Figure coverage.** Every figure is documented with its number, page,
     caption, and a description of what it shows.
   - **Claim precision.** Key claims are paraphrased tightly. Critical
     definitions and phrasing are quoted verbatim with page references.
   - **Experimental details.** Model names, parameter counts, hyperparameters,
     dataset sizes, training details, baselines — all present and correct.
   - **Citation capture.** Substantive in-text citations use the paper's own
     format and note who/what/how for important references.
   - **No fabrication.** Nothing in the notes is absent from or contradicted
     by the PDF. No invented numbers or claims.
   - **`[unclear: ...]` markers.** Check if any can now be resolved from the
     PDF content in this window.

3. **If a section file has errors:** log every error found (see "Error
   Logging" below), then fix:
   - **Surgical fix** for isolated issues: a wrong number in a table cell,
     a missing equation, a missing figure entry, an unresolved `[unclear]`
     marker, a missing citation in `_references.md`. Edit the specific lines.
   - **Full rewrite** of the section file when problems are pervasive:
     multiple missing tables, large blocks of missing content, systematic
     notation errors, fabricated claims. A rewrite ensures nothing is
     patched over inconsistently.
   - Use judgment: if fixing in place would touch more than roughly half
     the file, rewrite it.

4. **If a section file is correct and complete:** leave it unchanged. Do not
   rewrite files that pass verification. Do not write an error log.

5. **Continue to Step 5** (verify section files) as normal after verification.

---

## Step 1: Read context

If this IS the first window, skip this step (no prior files exist).

If this is NOT the first window:

1. **Read `00_overview.md`** to learn what section headings exist and what
   content has been captured so far.
2. **Glob `references/<SLUG>/sections/*.md`** to get the file list.
3. **Read only the last section file** in numeric order (the one most likely
   to need continuation from this window). For example, if files
   `01_introduction.md` through `04_experiments.md` exist, read only
   `04_experiments.md`.

This is sufficient context to avoid duplicating content and to know where to
append. Do NOT read all prior section files — earlier sections are complete
and their full text is not needed for your current pages.

## Step 2: Read the PDF pages

Read the PDF at PDF_PATH with the `pages` parameter set to "PAGE_START-PAGE_END".

## Step 3: Identify sections

Determine which paper sections (Introduction, Method, Experiments, etc.)
appear in the pages you just read. A single window may contain:
- The end of one section and the start of another
- One complete section
- Part of a long section that continues beyond this window

## Step 4: Write or update section files

For each section found, create or update a file in `references/<SLUG>/sections/`.

**File naming:** `NN_slug.md` where NN is a two-digit number for ordering
and slug is a short lowercase-hyphenated version of the paper's section title.

Example for a typical paper:
```
00_overview.md
01_introduction.md
02_related-work.md
03_method.md
04_experiments.md
05_results.md
06_conclusion.md
07_appendix-a.md
```

Adapt numbering and names to the paper's actual structure. Use the paper's
own section titles. If a section has substantial subsections (e.g., a 10-page
Method with 4 named subsections), use separate files:
```
03a_selection-mechanism.md
03b_hardware-aware-scan.md
```

**First window only:** Also create `00_overview.md` with:
- Paper title, authors, affiliations, venue, date
- Full abstract (quoted verbatim)
- List of section headings visible so far

**Creating a new section file:**
- Start with `# Section Title [p. X–Y]`
- Write the extracted content (see "What to extract" below)

**Updating an existing section file:**
- Read the file first
- Append new content under a continuation marker:
  ```
  ---
  [p. X–Y continued]
  ```
- Do NOT duplicate content already in the file

---

## What to extract

For every section, capture **all** of the following that appear:

### Claims and arguments
- Paraphrase key claims tightly but preserve precision.
- For critical definitions or phrasing, quote verbatim:
  `> "exact quote" [p. 7]`
- Note what is stated as a contribution vs. observation vs. hypothesis.

### Equations
- Reproduce **every numbered equation** using the paper's notation.
- Format: equation, then one line of context explaining what it computes.
- For unnumbered but important equations (e.g., inline definitions),
  reproduce them too.
- Note where notation is first defined.
- **Double-check mathematical symbols.** PDF extraction frequently confuses
  visually similar characters: `l` (ell) vs `1` vs `ε` (epsilon); `6` vs
  `ℓ`; `≤` vs `≥`; `∈` vs `∉`; `δ` vs `δ̂`. After writing each equation,
  re-read the PDF and verify every symbol, exponent, subscript, and
  inequality direction. A single wrong symbol can change a theorem's meaning.

### Figures
- For each figure: **Figure N** (p. X): `"caption text"`
- Describe what the figure shows — axes, trends, key data points.
- Note which claims the figure supports.
- If a figure has readable quantitative data, extract the values.
- **Every figure that appears on the pages you read MUST have a full Figure
  entry.** A passing text reference like "see Figure 4" is NOT sufficient —
  you must also create the standalone entry with number, page, caption, and
  description. This is a recurring error: agents reference figures in prose
  but never create the structured entry.

### Tables
- Reproduce **every table** as a Markdown table with exact numbers.
- Include: table number, caption, units, footnotes.
- Do not omit rows or columns. If a table has >20 rows, include all main
  results and note what was truncated.
- **If a table appears on the pages you read, reproduce it NOW.** Do not
  defer it — see Rule 8 below.

### Experimental details
- Models: names, parameter counts, architecture details
- Datasets: names, sizes, splits, preprocessing
- Training: optimizer, learning rate, batch size, steps/epochs, hardware, time
- Evaluation: metrics, decoding strategy, number of runs, confidence intervals
- Baselines: what, from where, how comparable

### In-text citations
- **Use the paper's own citation format** throughout the notes. If the paper
  uses numbered references like `[23]`, write `[23]`. If it uses
  `Vaswani et al. (2017)`, write `Vaswani et al. (2017)`.
- When the paper cites related work substantively (not just in passing),
  note: who, what claim, how it relates to the current paper.
- Pay special attention to papers the authors position against or build upon.

---

## Rules

1. **Never fabricate.** If a number is unreadable, write `[unclear: ...]`.
2. **Use the paper's notation exactly.** Do not rename variables.
3. **Mark page numbers.** Use `[p. N]` or `[p. N–M]` at the start of each
   block of extracted content.
4. **Capture all numbers.** Every table entry, hyperparameter, reported metric.
   Completeness over formatting.
5. **Keep structure flat.** H1 for section title, H2 for subsections,
   H3 for sub-subsections. No deeper nesting.
6. **Do not interpret or analyze.** Report what the paper says. No assessment,
   no implications, no comparisons. That is for analysis.md.
7. **Update 00_overview.md** if you discover new section headings not yet
   listed. **This is mandatory for every window**, not just the first one.
   Every window must check and update the section headings list.
8. **NEVER defer content.** Do not write placeholders like `[continues on
   later pages]`, `[table appears on a later page]`, `[Section continues
   on later pages]`, or similar deferred-content markers. If content is
   visible on the pages you are reading, extract it NOW. If a table or
   figure spans across your window boundary, extract the portion visible to
   you. A later window will append the rest. Deferred markers are
   systematically never revisited and result in permanent gaps.
9. **Preserve hedges and precise language.** When the paper says "We believe"
   or "This suggests", keep those qualifiers. Do not upgrade tentative claims
   to definitive ones. Similarly, preserve exact phrasing for key findings
   (e.g., "still outperforming all existing systems by a wide margin", not
   "substantially outperforming").
10. **Create section files for ALL sections you encounter**, including
    Conclusions, Acknowledgments, and Appendices. A recurring error is
    silently omitting these sections. If a section heading appears on your
    pages, it must get a file — even if the section content extends beyond
    your window (create the file with what you can see; the next window
    appends the rest).
11. **Proofread for text corruption.** After writing, scan for duplicate words
    ("needs, requires", "samples samples"), missing special characters (£, é,
    ü), and garbled text from PDF extraction. Fix any you find.

---

## Handling the bibliography/references section

When you reach the paper's bibliography or references section, do NOT
transcribe the full reference list. Instead:

1. Read all existing `references/<SLUG>/sections/*.md` files.
2. Scan the notes for every in-text citation (e.g., `[23]`, `Vaswani et al. (2017)`).
3. Collect the set of cited identifiers that actually appear in the notes.
4. Look up only those entries in the paper's bibliography.
5. Write `references/<SLUG>/sections/_references.md` containing only the
   references that were cited in the notes. For each entry, include:
   - The citation key as it appears in the paper (e.g., `[23]`)
   - Full bibliographic information: authors, title, venue, year
   - A one-line note on where/how it was cited in the notes
     (e.g., "Cited in 01_introduction.md as the baseline method")

This keeps the references file focused on what the notes actually discuss.

---

## Step 5: Verify section files

Verification scope depends on whether this is the last window.

### All windows (lightweight checks)

Re-read only the files you **created or modified in this window** and check:

- Numbers that appear in both running text and a table should match.
- If a figure or table is referenced in the text (e.g., "as shown in Table 3"),
  verify that the figure/table is actually reproduced in the notes.
- Check for `[unclear: ...]` markers — if you now have enough context to
  resolve them, fill in the correct value.

### Last window only (full checks)

If this is the **last window** (PAGE_END ≥ TOTAL_PAGES or you can see the
paper's bibliography/end matter), also perform these cross-file checks.
Read all files in `references/<SLUG>/sections/` for this purpose.

**Reference consistency:**
- Scan every section file for in-text citations (e.g., `[23]`, `[12, 14]`,
  `Author et al. (2017)`).
- Compare against `_references.md`:
  - **Missing from `_references.md`:** a citation appears in a section file
    but has no entry in `_references.md`. Add it.
  - **Orphaned in `_references.md`:** an entry exists in `_references.md`
    but is never cited in any section file. Remove it.
  - **Wrong "cited in" annotation:** the one-line note says the reference is
    cited in a file where it doesn't actually appear, or misses a file where
    it does appear. Correct it.

**Section coverage:**
- Compare the section headings listed in `00_overview.md` against the actual
  section files that exist. For every section heading in the overview that
  has no corresponding file, create the missing file now. Re-read the PDF
  pages where that section appears (you can determine this from the overview
  or from surrounding section files' page markers) and extract its content.
  Do not leave gaps — there is no later pass.

---

## Error Logging

When verification (Step 0) or final verification (Step 5) catches errors in
pre-existing files, log them **before** fixing. This log is used to improve
the prompts and prevent recurring mistakes.

```bash
mkdir -p prompts/add_reference/.errors/read_paper
```

Write (or append to) `prompts/add_reference/.errors/read_paper/<SLUG>.md`:

```markdown
# read_paper errors: <SLUG>

**Date:** YYYY-MM-DD
**Window:** p. PAGE_START–PAGE_END
**Action taken:** rewrote <file> / no errors found

## Errors

### 1. [short label]
- **Check:** which verification check caught this (e.g., "equation coverage", "table coverage", "figure coverage", "claim precision", "experimental details", "citation capture", "fabrication", "reference consistency", "section coverage", "internal consistency")
- **File:** which section file contained the error
- **Expected:** what the PDF says (quote or describe)
- **Found:** what the section file said
- **Severity:** critical / moderate / minor
```

Add one `### N.` block per distinct error. Be specific — include the exact
wrong value and the exact correct value.

If this is not the first window for this SLUG, **append** to the existing
error log file rather than overwriting it.

---

This is a **write-only** task. Only write to `references/<SLUG>/sections/`
and the error log at `prompts/add_reference/.errors/read_paper/`. Do NOT
modify any files outside those directories.
