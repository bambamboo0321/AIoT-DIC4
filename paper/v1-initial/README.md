# SmartIntake V1 source

Initial IEEE conference design manuscript. Authors/affiliations are pending. No formal E1-E5 results are available.

Build with an ordinary TeX Live installation containing IEEEtran, latexmk, BibTeX, pgf, booktabs and preprint:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

For Overleaf, upload this directory as a ZIP, choose `main.tex`, pdfLaTeX and a recent TeX Live release. Local clean ZIP builds are verified separately; an actual Overleaf service build is not claimed.
