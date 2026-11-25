# V2 validation

Date: 2026-11-25. OpenSpec CLI 2.2.0; spec-driven schema. Strict pre-edit validation passed and was saved in `v2-preflight.json` before editing V2. Specification commit `dfbca8e` follows actual V1 review commit `6a8971e`.

## Observed V2 artifact checks

- `SMARTINTAKE_TEXBIN=<TinyTeX bin> python3 scripts/build.py v2` passed both direct and independent fresh-ZIP builds (exit 0); their PDF text matches exactly.
- Seven-page IEEEtran conference PDF; eight resolved citations, resolved figure/table/equation references, zero overfull boxes/fatal errors. One underfull paragraph diagnostic remains; visually inspected as readable.
- `pdffonts` shows all V2 fonts embedded Type 1. Authors and affiliations remain explicit pending-confirmation markers.
- All seven final pages were rendered with Poppler and opened after the last source change. Source and artifact hashes are in `v2-build.json`.

| Page | Visual inspection |
|---|---|
| 1 | Title/abstract/placeholders and RQ/outcome table readable; two-column body flow intact |
| 2 | Ragged-right literature comparison readable; architecture text and calibration equation fit |
| 3 | Architecture/FSM diagrams and uncertainty/nutrition equations readable with no label overlap |
| 4 | Full-width lifecycle table, current-revision sum, switch steps and snapshot contract readable |
| 5 | Tool workflow and E1-E3 protocol table/equations fit; planned counts identified as proposals |
| 6 | E4/E5 scoring equations and discussion readable; no numeric performance results presented |
| 7 | Limitations, conclusion and bibliography readable; three DOI URLs appear; last columns balanced |

## Difference-artifact checks

The difference build is a real `latexdiff --flatten --type=CFONT --math-markup=whole --graphics-markup=none` comparison. It prebuilds both source snapshots in temporary copies to obtain their bibliographies. No temporary build file is added to V1. A generated URL-font setup is replaced with equivalent `urlstyle{same}` before comparison, and the deletion-font macro is made valid in math mode; these do not remove changed text. Whole-equation markup avoids invalid fine-grained equation edits. Graphics framing is disabled because the diagrams are native TikZ; actual source differences remain in the unified comparison.

Initial difference attempts exposed an optional `settobox.sty` graphics-markup dependency; installing a package under that name failed because it is not a standalone TeX Live package. The final no-graphics-framing mode does not require it. The first comparison also omitted bibliography markup and later warned on IEEEtran's generated URL-font macro; both were corrected in the generator. The final warnings and actual build outcomes are retained in `v1-v2-diff.json`, rather than presenting failed attempts as successful checks.

Final difference build: exit 0, eight pages, zero overfull boxes, resolved citations/cross-references. The only remaining latexdiff diagnostic is that listings is absent and verbatim markup is disabled; neither manuscript contains a verbatim/listings environment. All eight final rendered pages were opened: pp.1-2 show question/literature changes; pp.3-4 show equations, lifecycle and food/current-revision changes; pp.5-7 show session/query and E1-E5 changes; p.8 shows scope and DOI-bearing bibliography. No clipping or overlapping content was observed. CFONT uses smaller red deleted prose and blue additions; the newly introduced lifecycle table is rendered as one intact blue block to prevent the token matcher relocating old fragments into its cells. The unified source diff remains complete.

Both V1 and V2 source file hashes and release PDF/ZIP hashes were recomputed against their build manifests and all passed. V1 source/PDF/ZIP also show no Git differences against `v1.0-initial-draft`.

## Evidence boundary

R1-R9 are addressed as manuscript method/protocol specifications; see `reviews/revision-report.md` for each requirement, design/task mapping and actual changed file. No E1-E5 executable implementation or measured result is asserted. ZIP verification is local, not an Overleaf MCP operation. The barrier's availability trade-off and lack of implementation verification remain explicit limitations.
