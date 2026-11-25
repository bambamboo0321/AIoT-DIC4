# V1 to V2 revision report

V1 reviewed: commit `c90dada`, tag `v1.0-initial-draft`. Actual review: `v1-review.md`, commit `6a8971e`. V2 change: `revise-ieee-conference-paper`, pre-edit specification commit `dfbca8e`; OpenSpec 2.2.0 strict preflight passed before V2 source was copied/edited.

V1 remains unchanged. V2 is a complete independent seven-page snapshot. The real source comparison is [V1_V2_source.diff](../deliverables/V1_V2_source.diff); the visual markup is [latexdiff PDF](../deliverables/SmartIntake_V1_V2_Diff.pdf). Nine source paths changed. Additions are blue; deletions are red (smaller prose font). Whole equations are compared as units. Unchanged diagrams remain in context.

## Review-to-requirement-to-difference trace

Requirement names below are the exact delta-spec headers. Task numbers refer to the V2 change; design.md contains the same R1-R9 decision map. Acceptance here means the proposed manuscript contract is now defined and readable, **not** that a hardware/software implementation has passed E1-E5.

| Review | Requirement / task | Actual changed source and location | Acceptance evidence |
|---|---|---|---|
| R1 | Operational research questions / 1.1 | `sections/introduction.tex`: new `tab:questions`; `sections/related.tex`: operational comparison paragraph | V2 Table I p.1 maps all RQs to primary outcomes/E1-E5; scoped gap and algorithm/model novelty boundaries retained |
| R2 | Reproducible sensing lifecycle / 1.2 | `sections/method.tex` IV-A/B; new `figures/states.tex`, `tab:states` | V2 Table III p.4 covers INIT/PRESENT/ABSENT/RETURN/CLASSIFY/RESOLVE, timeout/re-entry and invalid comparison; parameter manifest is explicitly uncalibrated |
| R3 | Valid quantities and correction totals / 1.3 | `sections/method.tex`, `eq:uncertainty`, `eq:nutrition`, `eq:totals` | pp.3-4 define covariance assumptions, invalid taring, null nutrients and one-current-revision/status-partition sums; displayed equations fit |
| R4 | Coordinated session attribution / 1.4 | `sections/method.tex` IV-D; `sections/evaluation.tex` E3 | p.4 defines pause/install/activate acknowledgements, durable in-flight IDs, failed activation, historical completion, replay and restart; E3 fault attempts/coverage on pp.5-6 |
| R5 | Reproducible sensing evaluation / 2.1 | `sections/evaluation.tex` E1/E2; `experiments/evaluation-plan-v2.md` | p.5 specifies independent calibration/test placements, 50 planned tests/scale, 70 action opportunities, fixed one-to-one matching and extra/missing prediction rules; none are results |
| R6 | Transparent pilot denominators / 2.2 | `sections/evaluation.tex` E3/E4; V2 protocol | pp.5-6 retain unresolved coverage and failed-switch denominators; two-session within-person schedule, 16 tasks/person, censored 10-minute deadlines, participant-level summaries |
| R7 | Consistent authorized query envelope / 1.5 | `sections/method.tex` IV-E; `sections/discussion.tex` | p.4 defines trusted subject, half-open calendar boundaries, UTC conversion, snapshot-consistent sources/revisions, data statuses and denied-data isolation; design-only limitation reiterated p.7 |
| R8 | Reproducible agent scoring / 2.3 | `sections/evaluation.tex` E5, `eq:agent`, `eq:repeat`; V2 protocol | p.6 defines 30 cases/six families/three resets, oracle/tolerance and component conjunction; unauthorized attempts fail even if backend blocks; no-data is not zero; all-repeat denominator 30 |
| R9 | Readable reference and comparison presentation / 1.6 | `preamble.tex`, `sections/related.tex`, `sections/evaluation.tex`, `references.bib` | Ragged-right column type P improves Tables I-IV; DOI URLs for three verified publications appear on p.7; all eight references resolve |

`README.md` inside the V2 source also changes its version description; V1's source README is preserved. No author identities or empirical findings were added. The three original diagrams and the evidence boundaries remain intact rather than manufacturing cosmetic changes to every file.

## Integrated verification

Direct V2 and clean extracted ZIP builds, exact hashes, citation/reference resolution and source preservation are recorded in `docs/validation/v2-build.json` and `v2-validation.md`. The source comparison includes all nine changed paths, and the actual latexdiff includes generated bibliographies so DOI-link changes are visible. Its math-safe deletion font and equivalent generated URL-font setup are presentation adjustments only; no difference content is discarded.

No formal E1-E5 results, user study, deployed API assurance or Overleaf service success is claimed. Author confirmation and real implementation/measurement evidence remain future work.
