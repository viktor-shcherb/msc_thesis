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

Full guidelines for writing `source.md` and `analysis.md` files, maintaining metadata, and the YAML front matter schema are in `references/GUIDELINES.md`.

### Searching references

`references/search.py` queries the YAML front matter across all analysis files:

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

Requires PyYAML (`pip install pyyaml`).

### Adding a new reference

1. Create a subdirectory: `references/YYYY-MM-short-name/`
2. Add the paper PDF, `source.md`, `analysis.md`, and `cite.bib` following `references/GUIDELINES.md`.
3. Add YAML front matter to `analysis.md` using identifiers from `references/metadata.yaml`. Add new identifiers to the ontology if needed.
4. Update cross-references in related papers' front matter.
5. Run `make references.bib` to regenerate the combined file.

### Regenerating references.bib

```
make references.bib
```

This runs:

```
cat references/_venues.bib references/*/cite.bib > references.bib
```

## Meta-analyses

Cross-paper synthesis documents live in `meta-analysis/`, each in its own subdirectory:

```
meta-analysis/
├── GUIDELINES.md               # Full guidelines for writing meta-analyses
└── short-descriptive-name/
    └── analysis.md             # The synthesis document
```

A meta-analysis draws from multiple per-paper analyses in `references/` to answer a specific research question. Guidelines for scoping, structuring, and maintaining meta-analyses are in `meta-analysis/GUIDELINES.md`.
