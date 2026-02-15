# MSc Thesis

## Prerequisites

A TeX distribution with `pdflatex`, `biber`, and `latexmk`. On macOS, install [MacTeX](https://www.tug.org/mactex/):

```
brew install --cask mactex
```

On Ubuntu/Debian:

```
sudo apt install texlive-base texlive-bibtex-extra texlive-latex-base \
                 texlive-latex-extra texlive-latex-recommended \
                 texlive-science texlive-fonts-extra biber latexmk
```

## Building the PDF

```
make all
```

This first concatenates the per-reference BibTeX files into `references.bib`, then runs `latexmk -pdf` (which handles the pdflatex/biber cycle automatically).

To clean build artifacts:

```
make clean
```

## How references are managed

References are **not** edited in `references.bib` directly. That file is auto-generated.

Each reference lives in its own subdirectory under `references/`:

```
references/
  _venues.bib                          # shared @string venue macros
  2017-12-attention-is-all-you-need/
    cite.bib                            # BibTeX entry for this paper
    source.md                           # bibliographic metadata
    analysis.md                         # structured analysis
    1706.03762.pdf                      # paper PDF
  2024-02-lost-in-the-middle/
    cite.bib
    source.md
    analysis.md
    ...
```

`references/_venues.bib` defines `@string` macros for commonly used venues (e.g., `NeurIPS`, `ACL`, `ICML`). The Makefile concatenates `_venues.bib` first, then all `*/cite.bib` files, so macros are defined before any entry uses them.

Each `analysis.md` file includes YAML front matter with structured metadata (categories, key claims, cross-references, benchmarks, models). The shared ontology of controlled vocabularies is in `references/metadata.yaml`.

### Searching references

`references/search.py` queries the YAML front matter across all analysis files. Requires PyYAML (`pip install pyyaml`).

```
python3 references/search.py category context-extension
python3 references/search.py benchmark ruler
python3 references/search.py model llama-2-7b
python3 references/search.py lineage 2023-06-pi-positional-interpolation
python3 references/search.py contradictions
python3 references/search.py claims contested
python3 references/search.py open-questions --unresolved
python3 references/search.py text "attention sink"
python3 references/search.py info 2024-05-yarn-context-extension
python3 references/search.py related 2024-05-yarn-context-extension
```

### Adding a new reference

Run the `add_reference` prompt pipeline (see `prompts/add_reference/README.md`). The pipeline handles directory creation, PDF download, metadata, reading, and analysis automatically. See "Prompt system" below for how it works.

### Regenerating references.bib

```
make references.bib
```

This runs: `cat references/_venues.bib references/*/cite.bib > references.bib`

## Meta-analyses

Cross-paper synthesis documents live in `meta-analysis/`. Guidelines for scoping, structuring, and maintaining meta-analyses are in `meta-analysis/GUIDELINES.md`.

## Prompt system

Agent prompts live in `prompts/`. The main workflow is `add_reference`, a Sonnet-orchestrated pipeline that goes from a paper title or URL to a complete reference directory with analysis.

### How it works

```
init_reference → read_paper OR read_sources → verify_reading → write_analysis (incl. cross-reference update)
```

1. **init_reference** (opus) creates the directory, downloads the PDF, writes `source.md` and `cite.bib`
2. **read_paper** (sonnet) reads the PDF in overlapping 6-page windows, writing structured notes to `sections/`. For non-standard contributions (blogs, repos, Reddit), **read_sources** (sonnet) fetches web content into `sources/` instead
3. **verify_reading** (opus) checks all section files against the full PDF for completeness, accuracy, reference consistency, and section coverage. Can selectively re-read specific page ranges for critical issues
4. **write_analysis** (opus) synthesizes the notes into `analysis.md` with YAML front matter, all 9 required sections, and 13 style rules. Also updates reciprocal cross-references, claim interactions, and open questions in existing papers

Subagents that re-run on already-completed work enter **verification mode**: they verify existing output against ground truth and rewrite anything that falls short. Errors caught during verification are logged to `prompts/add_reference/.errors/` for prompt improvement.

### Where to find what

| Topic | Location |
|---|---|
| Full pipeline + decision tree + batch mode + model assignments | `prompts/add_reference/README.md` |
| `source.md` structure + `cite.bib` rules | `prompts/add_reference/init_reference/prompt.md` |
| PDF reading procedure + extraction rules | `prompts/add_reference/read_paper/prompt.md` |
| Non-standard source fetching | `prompts/add_reference/read_sources/prompt.md` |
| Post-reading verification + targeted re-reads | `prompts/add_reference/verify_reading/prompt.md` |
| `analysis.md` structure + YAML schema + 13 style rules | `prompts/add_reference/write_analysis/prompt.md` |
| Controlled vocabularies (categories, benchmarks, models) | `references/metadata.yaml` |
| Cross-reference types + ontology maintenance | `prompts/add_reference/README.md` § "Ontology maintenance" |
| Meta-analysis guidelines | `meta-analysis/GUIDELINES.md` |
| Verification error logs (gitignored) | `prompts/add_reference/.errors/<stage>/<slug>.md` |
