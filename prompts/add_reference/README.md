# add_reference — Add a New Reference

End-to-end workflow for adding one or more references to the `references/`
directory. This prompt orchestrates subagents in sequence.

## Pipeline

```
init_reference  →  read_paper OR read_sources  →  verify_reading  →  write_analysis (incl. cross-reference update)
```

1. **init_reference** — Research the paper, create directory, download PDF,
   write `source.md` and `cite.bib`. Reports: slug, PDF path (or null),
   standard vs non-standard flag.
2. **read_paper** (standard path) — Read the PDF in overlapping windows,
   write structured notes to `sections/`.
3. **read_sources** (non-standard path) — Fetch web content, repos, threads
   into `sources/`.
4. **verify_reading** (standard path only) — Verify completeness and accuracy
   of `sections/` against the PDF. Fix errors, fill gaps, check reference
   and section coverage.
5. **write_analysis** — Read `sections/` or `sources/`, write `analysis.md`
   with YAML front matter and all required sections, then update reciprocal
   cross-references, claim interactions, and open question resolutions in
   existing papers.

## Decision tree

After init_reference completes, inspect its report:

```
init_reference succeeds + PDF exists
  → read_paper (windowed, writes sections/)
  → verify_reading (checks sections/ against PDF)
  → write_analysis (reads sections/)

init_reference succeeds + no PDF, non-standard
  → read_sources (reads manifest, writes sources/)
  → write_analysis (reads sources/)

init_reference fails (paper not found, ambiguous input)
  → report failure to user, do not proceed
```

## Model assignments

The main orchestrator runs on **Sonnet**. Subagents use:

| Stage | Model | Rationale |
|---|---|---|
| init_reference | sonnet | Metadata lookup, straightforward extraction |
| read_paper | sonnet | High-volume windowed extraction |
| read_sources | sonnet | Web fetching and content extraction |
| verify_reading | **opus** | Requires judgment to catch subtle errors |
| write_analysis | **opus** | Synthesis, cross-referencing, claim assessment |

## Subagent usage

Each subagent has two files:
- `README.md` — usage instructions for this main agent (parameters, invocation)
- `prompt.md` — instructions the subagent reads itself

See each subdirectory for details:
- `init_reference/` — initialize reference directory
- `read_paper/` — read PDF in windowed passes
- `read_sources/` — fetch non-standard source content
- `verify_reading/` — verify section notes against PDF
- `write_analysis/` — create analysis.md

## Ontology maintenance

The file `references/metadata.yaml` contains controlled vocabularies for
categories, paper types, relationship types, benchmarks, and models. All
identifiers in YAML front matter must come from this ontology.

**When adding a new reference:**
- Use existing ontology identifiers where possible
- If a new identifier is needed (new benchmark, new model, new category),
  add it to `metadata.yaml` first with a short description
- Then use the new identifier in the paper's `analysis.md` front matter

## Batch mode

When processing multiple references at once:

1. **Init all** — Run `init_reference` for each paper (can be parallel).
   Collect the list of (slug, pdf_path, standard_flag) tuples.

2. **Read in parallel** — For standard papers, run `read_paper` windows.
   Windows for different papers can run in parallel. For non-standard
   references, run `read_sources` (one per reference, can be parallel).

3. **Verify in parallel** — For standard papers, run `verify_reading` once
   all windows for that paper are done. Verification for different papers
   can run in parallel.

4. **Analyze sequentially** — Run `write_analysis` for each paper once its
   reading/verification step completes. Run these **sequentially** (not in
   parallel) because each `write_analysis` updates cross-references in other
   papers' `analysis.md` files — parallel runs risk conflicting edits.

## Citation file maintenance

Each reference must include a `cite.bib` file. After creating or modifying
any `cite.bib`, regenerate the combined bibliography:

```bash
make references.bib
```

Citation keys must match the directory name (e.g., `2024-02-lost-in-the-middle`).
If the venue has a `@string` macro in `references/_venues.bib`, use the macro
name (e.g., `booktitle = NeurIPS`). If a major venue is missing from
`_venues.bib`, add a new `@string` definition there.
