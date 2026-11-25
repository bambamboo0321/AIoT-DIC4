# Design

## Context

Review commit 6a8971e evaluates actual V1 c90dada. The existing ieee-manuscript spec was read in full. All its requirements remain in force; this change adds specific reproducibility obligations.

## Goals / Non-Goals

Improve the proposed design's precision using a copied V2 snapshot. Do not claim that specified invariants have passed implementation tests. V3 requires a fresh substantive reason after reviewing V2.

## Decisions

| Review | Requirement | Method / rationale | Task |
|---|---|---|---|
| R1 | Operational research questions | RQ/outcome map and scoped literature contrast; separates test obligations from algorithm novelty | 1.1 |
| R2 | Reproducible sensing lifecycle | State/guard/re-arm table plus parameter manifest; fail closed on initialization and timeout | 1.2 |
| R3 | Valid quantities and correction totals | Reject invalid net mass; state uncertainty assumptions; current-revision/status partitions | 1.3 |
| R4 | Coordinated session attribution | Pause/install/activate barrier across two workers with durable in-flight IDs; quarantine stale events | 1.4 |
| R5 | Reproducible sensing evaluation | Prospective trial blocks and frozen one-to-one event matching; explicit duplicate/timeout rules | 2.1 |
| R6 | Transparent pilot denominators | Coverage plus wrong-owner rates; two-session within-person schedule; noncompletion retained | 2.2 |
| R7 | Consistent authorized query envelope | Half-open calendar queries, one DB snapshot, record revision IDs, explicit data-status semantics | 1.5 |
| R8 | Reproducible agent scoring | 30 cases, six families, three reset runs; component conjunction and case-level reliability | 2.3 |
| R9 | Readable reference and comparison presentation | Ragged-right table cells, compact labels and printed DOI URLs | 1.6 |

Alternatives: a backend-only session transaction cannot prevent a stale worker starting new events; use an acknowledged barrier and fail-closed availability trade-off. Perfect-confirmation simulation would leak the oracle into E2; retain actual user responses separately. Pooling all repeated trials would overstate independence; report scale/block/person/case units explicitly.

## Risks / Trade-offs

- Session barrier reduces availability during disconnection -> report held events and failed switches.
- Planned counts may require adjustment after hardware setup -> freeze changes before test collection and disclose deviations.
- Added detail increases manuscript length -> use labeled concise tables without shrinking body text or violating IEEE layout.
- Lack of research data persists -> present design/protocol status in every evidence statement.

## Migration Plan

Copy the frozen V1, edit only V2, build and inspect all pages, independently rebuild ZIP, generate real latexdiff, compare V1 hashes to its frozen manifest. Archive only after review mappings and actual validations are complete.
