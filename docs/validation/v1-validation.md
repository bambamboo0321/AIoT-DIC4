# V1 validation

Date: 2026-11-25. OpenSpec CLI 2.2.0, spec-driven schema. Pre-drafting specification commit: `0d31549`; strict preflight is saved in `v1-preflight.json`. Source was written after that validation and commit.

## Observed checks

- `SMARTINTAKE_TEXBIN=<TinyTeX bin> python3 scripts/build.py v1`: source and clean extracted-ZIP builds both exit 0. Exact source/PDF/ZIP hashes are in `v1-build.json`.
- IEEEtran conference class 2015/08/26 V1.8b, pdfLaTeX, BibTeX and IEEEtran bibliography style produced a five-page US Letter PDF.
- Eight citations resolve; all labeled figures, tables and equations resolve; final log contains no overfull boxes or fatal errors. Seven underfull table-cell diagnostics remain; visual inspection found readable content and no clipping.
- Initial build failures were missing cite.sty and three overfull diagram/table boxes. Installed cite and corrected column spacing, the FSM branch positions and the architecture label before freezing V1. No failed output is represented as a successful final build.
- ZIP contains only the 15 source/README files. It was extracted in a fresh temporary directory and rebuilt without referencing `paper/v1-initial`. Its PDF text exactly matches the direct source build.
- Render command: `pdftoppm -scale-to 1000 -png deliverables/SmartIntake_V1_Initial.pdf <temporary-prefix>`. All five final pages were opened and visually inspected after the last change.

| Page | Inspection |
|---|---|
| 1 | Title, explicit author/affiliation placeholders, abstract, keywords and column flow readable |
| 2 | Related-work table, architecture text and first equations stay within columns |
| 3 | Architecture and hydration diagrams have readable labels and non-overlapping arrows; nutrition and session text fit |
| 4 | Tool workflow, evaluation matrix and E1-E5 definitions readable; equations fit |
| 5 | Discussion, conclusion and eight references readable; balanced final columns with normal unused space below |

## Requirement evidence

- Complete IEEE manuscript: `paper/v1-initial/main.tex` and all section/figure inputs; all requested technology components and sections are present.
- Evidence-bounded claims: abstract, Introduction final paragraph, Discussion and Conclusion explicitly state design/protocol status. E1-E5 results remain pending.
- References: `research/citation-mapping.md` verifies authors, dates, titles and identifiers; `research/claim-evidence-map.md` bounds their use.
- Independent delivery: direct and ZIP builds above; source and artifact hash manifest in `v1-build.json`.
- Public safety: manually reviewed source, reports and ZIP member list. No private project files, credentials, health records or identifiable screenshots are included. Only independently written synthesis and public citation facts are released.

Authors/affiliations, physical implementation, research measurements, and Overleaf service operations remain unverified. Local ZIP validation is not an Overleaf MCP operation. Commit/tag follow the completed checks and archive; the tag points to the actual frozen milestone.
