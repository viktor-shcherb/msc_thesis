# add_reference — Add a New Reference

End-to-end workflow for adding one or more references to the `references/`
directory. This prompt orchestrates four subagents in sequence.

## Pipeline

```
init_reference  →  read_paper OR read_sources  →  write_analysis  →  cross-reference update
```

1. **init_reference** — Research the paper, create directory, download PDF,
   write `source.md` and `cite.bib`. Reports: slug, PDF path (or null),
   standard vs non-standard flag.
2. **read_paper** (standard path) — Read the PDF in overlapping windows,
   write structured notes to `sections/`.
3. **read_sources** (non-standard path) — Fetch web content, repos, threads
   into `sources/`.
4. **write_analysis** — Read `sections/` or `sources/`, write `analysis.md`
   with YAML front matter and all required sections.
5. **Cross-reference update** — Update existing analyses to reflect the new
   paper (see below).

## Decision tree

After init_reference completes, inspect its report:

```
init_reference succeeds + PDF exists
  → read_paper (windowed, writes sections/)
  → write_analysis (reads sections/)

init_reference succeeds + no PDF, non-standard
  → read_sources (reads manifest, writes sources/)
  → write_analysis (reads sources/)

init_reference fails (paper not found, ambiguous input)
  → report failure to user, do not proceed
```

## Subagent usage

Each subagent has two files:
- `README.md` — usage instructions for this main agent (parameters, invocation)
- `prompt.md` — instructions the subagent reads itself

See each subdirectory for details:
- `init_reference/` — initialize reference directory
- `read_paper/` — read PDF in windowed passes
- `read_sources/` — fetch non-standard source content
- `write_analysis/` — create analysis.md

## Cross-reference update procedure

After `write_analysis` completes for a new paper, update the broader
reference network:

1. **Read the new paper's YAML front matter.** Note its `cross_references`,
   `categories`, `key_claims`, and `open_questions`.

2. **Add reciprocal cross-references.** For every `cross_references` entry
   in the new paper:
   - Open the target paper's `analysis.md`
   - Add a reciprocal entry in its `cross_references` YAML block
   - Relationship type mapping:
     - `extends` ↔ `extended-by`
     - `contradicts` ↔ `contradicts`
     - `uses-benchmark` — no reciprocal needed
     - `evaluates` — no reciprocal needed
     - `concurrent` ↔ `concurrent`
     - `complementary` ↔ `complementary`
     - `formalizes` — add `formalized-by` note in target (use `complementary` type)

3. **Check for claim interactions.** If the new paper contests or validates
   claims from existing papers:
   - Update the `status` and `contested_by` fields on the relevant
     `key_claims` entries in the existing paper's YAML
   - Update the existing paper's "Key Claims" prose section if needed

4. **Check for open question resolution.** If the new paper addresses an
   `open_question` from an existing paper:
   - Update the `addressed_by` field in the existing paper's YAML
   - Add a note in the existing paper's "Open Questions" prose section

5. **Update meta-analyses.** Check whether the new paper falls within the
   corpus of any existing meta-analysis in `meta-analysis/` (match on
   categories, cross-references, or keyword overlap). If it does, follow the
   maintenance procedure in `meta-analysis/GUIDELINES.md`.

## Metadata validation

After all updates, validate consistency using `search.py`:

```bash
# Check the new paper's relationships
python3 references/search.py related <SLUG>

# Verify no broken references
python3 references/search.py info <SLUG>

# List all contradictions (should include any new ones)
python3 references/search.py contradictions
```

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

3. **Analyze in parallel** — Run `write_analysis` for each paper once its
   reading step completes.

4. **Cross-reference update** — Do this sequentially after all analyses are
   written to avoid conflicting edits to the same files.

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
