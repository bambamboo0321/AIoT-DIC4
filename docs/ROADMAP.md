# DIC4 execution roadmap

## Phase 0 — Environment audit
Inspect repository, local tools and MCP availability. Record versions, missing prerequisites and proposed remediation in docs/environment-audit.md. Stop for user review.

## Phase 1 — V1 initial paper
Create and validate OpenSpec change initialize-ieee-paper before editing. Use IEEEtran conference class. Draft abstract, introduction, related work, system architecture, methods, evaluation plan, limitations and conclusion. Verify sources; distinguish planned evaluation from results. Compile, inspect and package independent V1 source/PDF/ZIP. Commit and tag after validation.

## Phase 2 — Academic review
Review actual V1 as an IEEE-style reviewer. Assign issue IDs and severity, identify evidence gaps and reproducibility issues; save reviews/v1-review.md. Do not invent reviews that did not occur.

## Phase 3 — V2 revision
Create a new OpenSpec change based on review findings before editing. Preserve V1; revise actual manuscript, compile and inspect V2, generate latexdiff or documented comparison, create review-to-change traceability report. Validate change, commit, tag, archive when appropriate.

## Phase 4 — V3 research refinement
Proceed only after V2 review. Improve methodology, experiment protocol and evidence alignment based on actual feedback or new evidence. Use separate change and validation. Results remain pending until measured.

## Phase 5 — Overleaf and delivery
Discover configured Overleaf MCP; if available, demonstrate authorized read/edit/verification and record sanitized evidence. Otherwise record blocker and offer verified import ZIPs. Update README with actual artifact links and tags. Final results revision follows genuine experiments, not a fabricated deadline.
