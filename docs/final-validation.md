# Final manuscript-package validation

Date: 2026-11-25. Scope: DIC4 research design/protocol manuscripts, authentic revision history and public-safe delivery. This is not verification of a running SmartIntake application or a completed empirical study.

## Delivered and observed

| Item | Actual evidence |
|---|---|
| Environment | OpenSpec 2.2.0; TeX Live 2026/pdfTeX 1.40.29, IEEEtran V1.8b, latexmk 4.88, BibTeX 0.99e, latexdiff 1.4.0, Poppler 26.11.0; real smoke checks passed |
| V1 | Independent source, 5-page PDF and cleanly rebuilt ZIP; all five pages inspected; eight references resolved |
| Review | Actual V1/source review R1-R9, with severity/evidence/recommendations/acceptance |
| V2 | Independent source, 7-page PDF and cleanly rebuilt ZIP; all seven pages inspected; nine source paths genuinely changed |
| Difference | Real 8-page latexdiff, flattened bibliographies, complete unified source diff; all eight pages inspected |
| OpenSpec | Two verified archived changes with goal/proposal/design/tasks/deltas; 13 current requirements; strict and completed-archive checks pass |
| Preservation | V1 source/PDF/ZIP hashes unchanged from V1 manifest/tag; V2 hashes and ZIP content checked |
| Publication safety | Manual source/PDF/package review plus selected secret-pattern checks; no copied private files, credentials, health records or identifiable screenshots |
| Local tool persistence | Ignored `.tools/` contains dependencies; relocated paths/IEEE style lookup and smoke build pass; tools are not committed |

The exact checks/hashes are in `validation/v1-build.json`, `v2-build.json`, `v1-v2-diff.json`, version validation reports and `final-checks.json`. The two ZIPs were rebuilt in separate fresh directories and matched direct-build PDF text. Word-level semantic truth and visual quality are not claimed to follow from a hash or secret scanner alone.

## Actual milestone history

| Commit | Milestone |
|---|---|
| d62f977 | Phase 0 report |
| 8f92432 / 30e50e1 | Environment/OpenSpec setup and completed smoke verification |
| 0d31549 | V1 specification before drafting |
| c90dada | Verified V1; annotated tag `v1.0-initial-draft` |
| 6a8971e | Actual V1 academic review |
| dfbca8e | Validated R1-R9 V2 specification before editing |
| c09bd42 | Verified V2/diff/revision report; annotated tag `v2.0-revised-draft` |
| f29f96e | V2 follow-up review and justified V3 deferral |
| 956bb7a | Overleaf investigation and verified fallback record |

Generated comparison files intentionally retain native diff whitespace under `.gitattributes`; ordinary source/documentation retains Git whitespace checks. No milestone is backdated, no existing tag/history is overwritten, and no forced push is used.

## Unresolved items

- Authors/affiliations/contact need team confirmation; explicit placeholders remain.
- Hardware/calibration, runnable module integration, race/fault/security verification and physical parameter freeze need genuine implementation evidence.
- Formal E1-E5 measurements, participant consent/review as applicable and statistical analysis remain pending. Planned counts are not results.
- No authorized live Overleaf MCP project/token/connection was supplied. Configuration feasibility and reliable supported-Git direction are documented; no MCP operation or online compilation is claimed. Locally verified import ZIPs are the fallback.
- V3 is deferred until a substantive new issue, review or real evidence justifies another change.

## Publication execution

The user explicitly authorized the final normal push to `bambamboo0321/AIoT-DIC4`, including the two new version tags. This report is a pre-publication validation record. Check origin before pushing, publish the prepared commits/tags without force, then verify remote branch/tag targets and record actual transport results. Do not interpret authorization as a successful network operation before it happens.
