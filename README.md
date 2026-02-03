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

### Adding a new reference

1. Create a subdirectory: `references/YYYY-MM-short-name/`
2. Add the paper PDF, `source.md`, and `analysis.md` (see `references/GUIDELINES.md` for details).
3. Add a `cite.bib` with the BibTeX entry. Use `@string` macros from `_venues.bib` where applicable.
4. Run `make references.bib` to regenerate the combined file.

### Regenerating references.bib

```
make references.bib
```

This runs:

```
cat references/_venues.bib references/*/cite.bib > references.bib
```
