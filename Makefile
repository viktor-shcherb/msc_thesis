
name=thesis

references.bib: references/_venues.bib references/*/cite.bib
	cat references/_venues.bib references/*/cite.bib > references.bib

all: references.bib *.tex
	latexmk -pdf $(name).tex

clean:
	latexmk -C $(name).tex
