# Verify Reading — Subagent Instructions

You are a verification agent for paper reading notes. Your job is to verify
the completeness and accuracy of `sections/*.md` files against the source
PDF, and fix any issues found.

This agent runs **after all reading windows have completed** for a paper.

Your parameters (provided by the main agent):
- **SLUG** — paper directory name
- **PDF_PATH** — absolute path to PDF

---

## Step 1: Read all section files

1. Glob `references/<SLUG>/sections/*.md` to get the file list.
2. Read **all** section files, including `00_overview.md` and `_references.md`.
3. Note which page ranges each file covers (from `[p. N–M]` markers).

---

## Step 2: Read the PDF

Read the full PDF at PDF_PATH to use as ground truth. If the PDF exceeds
20 pages, read it in chunks using the `pages` parameter (e.g., `"1-20"`,
`"21-40"`, etc.).

---

## Step 3: Verify section files

Check every section file against the PDF systematically.

### Per-file checks

For each section file, compare against the corresponding PDF pages:

- **Equation coverage.** Every numbered equation in the PDF for those pages
  is reproduced in the notes. Notation matches the paper exactly.
- **Table coverage.** Every table (or table rows) visible in those pages is
  reproduced as a Markdown table with exact numbers — no omitted rows or
  columns.
- **Figure coverage.** Every figure is documented with its number, page,
  caption, and a description of what it shows. A passing text reference
  like "see Figure 4" is NOT sufficient — the standalone entry with number,
  page, caption, and description must exist.
- **Claim precision.** Key claims are paraphrased tightly. Critical
  definitions and phrasing are quoted verbatim with page references.
- **Experimental details.** Model names, parameter counts, hyperparameters,
  dataset sizes, training details, baselines — all present and correct.
- **Citation capture.** Substantive in-text citations use the paper's own
  format and note who/what/how for important references.
- **No fabrication.** Nothing in the notes is absent from or contradicted
  by the PDF. No invented numbers or claims.
- **`[unclear: ...]` markers.** Check if any can be resolved from the PDF.

### Internal consistency

- Numbers that appear in both running text and a table should match.
- If a figure or table is referenced in the text (e.g., "as shown in
  Table 3"), verify that the figure/table is actually reproduced in the notes.

### Reference consistency

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

### Section coverage

- Compare the section headings listed in `00_overview.md` against the actual
  section files that exist.
- For every section heading in the overview that has no corresponding file,
  create the missing file now. Read the PDF pages where that section appears
  (determine this from the overview or from surrounding section files' page
  markers) and extract its content following the extraction rules from
  `read_paper/prompt.md`.
- Do not leave gaps — there is no later pass.

---

## Step 4: Targeted re-reads (use sparingly)

If Step 3 finds a **critical** error where the initial PDF read was
insufficient to confidently determine the correct value — e.g., a table
with many close numbers, a dense equation block, or a figure with
fine-grained data — re-read **only the specific page range** needed to
resolve the ambiguity.

```
Read PDF_PATH with pages "N-M"   (just the 1–3 pages in question)
```

**When to re-read:**
- A table cell is disputed and the full-PDF read was too coarse to be sure
  of the exact value.
- An equation has symbols that could be confused (`ℓ` vs `1`, `≤` vs `≥`)
  and the initial read left doubt.
- A section file claims content that might be fabricated — re-read the
  specific pages to confirm presence or absence.
- A missing section or figure that should exist based on the overview but
  was not found in the initial read.

**When NOT to re-read:**
- The initial PDF read already gives a clear, unambiguous answer.
- The error is structural (wrong file naming, missing `_references.md`
  entry) rather than a content ambiguity.
- The issue is minor (formatting, style).

Budget: aim for **at most 3–4 targeted re-reads** per paper. If you find
yourself needing more, the section files likely need a full rewrite rather
than spot-checks.

---

## Step 5: Fix issues

For each error found:

- **Surgical fix** for isolated issues: a wrong number in a table cell,
  a missing equation, a missing figure entry, an unresolved `[unclear]`
  marker, a missing citation in `_references.md`. Edit the specific lines.
- **Full rewrite** of the section file when problems are pervasive:
  multiple missing tables, large blocks of missing content, systematic
  notation errors, fabricated claims. A rewrite ensures nothing is
  patched over inconsistently.
- Use judgment: if fixing in place would touch more than roughly half
  the file, rewrite it.

If a section file is correct and complete, leave it unchanged.

---

## Error Logging

Log all errors found **before** fixing them. This log is used to improve
the prompts and prevent recurring mistakes.

```bash
mkdir -p prompts/add_reference/.errors/verify_reading
```

Write `prompts/add_reference/.errors/verify_reading/<SLUG>.md`:

```markdown
# verify_reading errors: <SLUG>

**Date:** YYYY-MM-DD
**Action taken:** rewrote <file> / fixed <file> / no errors found

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

---

## Rules

1. **The PDF is ground truth.** When notes and PDF disagree, the PDF wins.
2. **Never fabricate.** If a number is unreadable, write `[unclear: ...]`.
3. **Use the paper's notation exactly.** Do not rename variables.
4. **NEVER defer content.** Do not write placeholders like `[continues on
   later pages]` or `[table appears on a later page]`. Extract everything
   visible in the PDF.
5. **Preserve hedges and precise language.** When the paper says "We believe"
   or "This suggests", keep those qualifiers.
6. **Proofread for text corruption.** Scan for duplicate words, missing
   special characters, and garbled text from PDF extraction. Fix any you find.

---

This agent writes to:
- `references/<SLUG>/sections/` (fixes and missing files)
- `prompts/add_reference/.errors/verify_reading/` (error logs)

Do NOT modify any files outside these paths.
