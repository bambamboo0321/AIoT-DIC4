# Build, inspect and reproduce

## Dependencies

A standard TeX Live installation needs IEEEtran class/style, latexmk, BibTeX, cite, amsmath/amssymb, graphics, pgf/TikZ, booktabs, url, array and preprint/balance. latexdiff generates the comparison; Poppler provides pdfinfo, pdffonts, pdftotext and pdftoppm. Python 3 uses only its standard library. OpenSpec is pinned to 2.2.0 for the recorded schema/validation.

The configured machine keeps OpenSpec and portable TinyTeX in ignored `.tools/`. Nothing in that directory is committed. From this repository root, the current machine can use:

```sh
export SMARTINTAKE_TEXBIN="$PWD/.tools/texlive/bin/universal-darwin"
export SMARTINTAKE_OPENSPEC="$PWD/.tools/openspec/node_modules/.bin/openspec"
export PATH="$SMARTINTAKE_TEXBIN:$PATH"
```

On other machines use a normal TeX Live PATH, or set `SMARTINTAKE_TEXBIN` to its bin directory. Set `SMARTINTAKE_OPENSPEC` only if the CLI is not already named `openspec` on PATH. A fresh clone does not contain the local tools.

OpenSpec's official package installation can be reproduced without npm lifecycle scripts using `npm install --prefix .tools/openspec --ignore-scripts --no-audit --no-fund @fission-ai/openspec@2.2.0`. The actual lightweight TeX installation provenance and SHA-256 are in [environment-setup.md](environment-setup.md); no remote shell installer or sudo was used. Ordinary TeX Live package-manager installation is an alternative. Do not reinitialize or overwrite archived changes to reproduce validation.

## Version builds and independent ZIP checks

```sh
python3 scripts/build.py v1
python3 scripts/build.py v2
python3 scripts/build_diff.py
python3 scripts/verify_release.py
```

`build.py` copies a snapshot to a clean temporary build directory, runs latexmk/BibTeX, rejects fatal/unresolved/overfull diagnostics, writes the PDF/source-only ZIP, extracts that ZIP to a second fresh directory, recompiles and compares PDF text. It records exact source/artifact hashes and PDF information. Successful runs do not modify manuscript sources. Rebuilding PDFs changes creation timestamps and therefore may change artifact hashes; do not replace a published artifact without recording the new validation.

The difference generator prebuilds both bibliographies in temporary copies and uses genuine flattened latexdiff with CFONT, whole-equation markup and no raster graphics framing. Equivalent generated URL-font setup, math-safe deletion styling and an intact added lifecycle table prevent parser/layout defects without deleting difference content. All exact source differences remain in `V1_V2_source.diff`.

For a source ZIP alone, extract into an empty directory and run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

No sibling snapshot or private source is needed. ZIPs use only source/README files and standard dependencies. Online Overleaf execution has not been tested.

## Rendered-page inspection

```sh
pdftoppm -scale-to 1200 -png deliverables/SmartIntake_V2_Revised.pdf /tmp/smartintake-v2-page
```

Open every rendered page. Check title/columns, readable figures/tables/equations, glyphs, references and no overlap/clipping; text extraction alone cannot establish visual quality. All 5 V1, 7 V2 and 8 diff pages were inspected for the released artifacts.

## OpenSpec

```sh
OPENSPEC_TELEMETRY=0 "$SMARTINTAKE_OPENSPEC" validate --all --strict --json --no-interactive
OPENSPEC_TELEMETRY=0 "$SMARTINTAKE_OPENSPEC" validate --archived --json --no-interactive
```

When using a normal PATH-only CLI, replace `"$SMARTINTAKE_OPENSPEC"` with `openspec`. Each genuine future manuscript revision must create a new change before editing and include goal/proposal/design/tasks/delta specs. Archive only after real artifact and review checks. CLI schema validation does not establish research validity or implementation success.
