# Design

## Context

See proposal.md. The authorized project documents remain design drafts; no formal E1-E5 results exist. The public repository may contain a newly written academic synthesis of the user-approved scope, but no copied private source, credentials, identifiable records or screenshots.

## Goals / Non-Goals

Use a complete, reasonable initial manuscript with enough methodological detail to review. Do not simulate deployment, experiments, Overleaf operations or author confirmation. No numerical performance tables without measurements.

## Decisions

- Use modular LaTeX (`main.tex`, section files, original TikZ diagrams, references.bib) and IEEEtran conference class. This keeps source readable and permits independent snapshots; a shared mutable manuscript would weaken version preservation.
- Prefer deterministic backend calculations and server-side authorization. Describe sensing as candidate-event generation, not proof of ingestion. Distinguish inferred, confirmed, corrected and missing records.
- Cite primary papers and official data documentation. Record metadata verification and limits in a citation map instead of relying on unchecked model recall.
- Define E1-E5 ground truth, baselines and metrics as prospective protocols. Proposed counts and thresholds are protocol choices, not collected data.
- Compile in temporary directories; package only source files. Rebuild from a freshly extracted ZIP outside the source tree. Inspect every rendered PDF page before release.
- Freeze V1 after verification and tag its actual commit. Archive this change only after tasks and outputs pass validation.

## Risks / Trade-offs

- Small pilot sample -> feasibility claims only; no population or clinical conclusions.
- Mass-loss ambiguity -> retain provenance and correction paths.
- Missing Overleaf authorization -> verify local import ZIP and disclose service checks as pending.
- Missing authors -> explicit placeholders remain until team confirmation.

## Migration Plan

New artifacts only. A failed build blocks the tag; repair V1 before freezing. Once frozen, subsequent substantive revision occurs in a copied V2 directory.
