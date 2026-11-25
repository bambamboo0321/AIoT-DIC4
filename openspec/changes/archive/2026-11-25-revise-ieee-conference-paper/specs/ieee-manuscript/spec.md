## ADDED Requirements

### Requirement: Operational research questions
The manuscript SHALL map each research question to named primary observable outcomes and E1-E5 experiments, and distinguish the scoped integration contribution from a new sensing algorithm or trained language model.

#### Scenario: R1 question map
- **WHEN** a reviewer examines the contribution
- **THEN** the RQ/outcome map and scoped related-work interpretation identify what can be tested without claiming demonstrated benefit.

### Requirement: Reproducible sensing lifecycle
The methodology SHALL define initialization, stable presence, lift, return, classification, unresolved/reset and re-arming guards with an explicit parameter manifest and no inferred intake on invalid reset paths.

#### Scenario: R2 lifecycle
- **WHEN** a cold start, timeout or vessel reset occurs
- **THEN** the state specification determines baseline reacquisition and prevents an unsupported inferred intake.

### Requirement: Valid quantities and correction totals
The methodology SHALL reject invalid net mass and unknown nutrient inputs, state uncertainty assumptions, and define aggregation over current non-rejected revisions with inferred and confirmed status partitions.

#### Scenario: R3 correction
- **WHEN** a record is corrected or has an invalid quantity
- **THEN** the total counts at most one valid current revision and does not convert invalid or missing data into zero.

### Requirement: Coordinated session attribution
The design SHALL define an acknowledged two-worker switch barrier, durable in-flight event ownership, historical completion validation, and fail-closed handling of stale or unverifiable starts.

#### Scenario: R4 concurrent switch
- **WHEN** a switch races with a lifted cup, delayed replay or worker restart
- **THEN** the specified outcome preserves event-start ownership or holds the event unresolved instead of assigning upload-time ownership.

### Requirement: Reproducible sensing evaluation
The protocol SHALL define prospective E1/E2 repetition blocks, independent calibration/test separation, frozen one-to-one event matching and explicit duplicate, unmatched and timeout treatment.

#### Scenario: R5 trace scoring
- **WHEN** two evaluators score the same observation trace
- **THEN** the fixed matching and denominator rules determine the same TP, FP and FN without outcome-dependent choices.

### Requirement: Transparent pilot denominators
The E3/E4 protocol SHALL retain failed or unresolved events and incomplete tasks in reported coverage and completion denominators and define descriptive within-person summaries without treating repeated tasks as independent people.

#### Scenario: R6 incomplete task
- **WHEN** a pilot task times out or an event cannot be attributed
- **THEN** reported coverage/completion retains that case and participant-level summaries disclose noncompletion.

### Requirement: Consistent authorized query envelope
The agent design SHALL specify server-authorized subjects, half-open local-calendar intervals converted to UTC, one consistent query snapshot, record revision provenance, tool versions and separate zero, missing, partial and denied statuses.

#### Scenario: R7 correction during query
- **WHEN** a correction occurs while a daily total is queried
- **THEN** the total and its authorized sources correspond to one returned snapshot and interval.

### Requirement: Reproducible agent scoring
The E5 protocol SHALL propose 30 frozen cases across six families and three reset runs per case, with deterministic numeric and provenance oracles, separate component scores and strict conjunction success.

#### Scenario: R8 unsafe correct number
- **WHEN** a response discloses unauthorized data or invents a zero despite correct arithmetic elsewhere
- **THEN** the run fails strict success and the case fails all-repeat reliability.

### Requirement: Readable reference and comparison presentation
The revised manuscript SHALL provide readable comparison tables and printed links for verified publication DOIs, preserve V1, and map every review ID to actual changes and validation.

#### Scenario: R9 release review
- **WHEN** a reviewer opens V2 and the revision report
- **THEN** table text and reference links are readable and each issue maps to a source difference and observed acceptance check.
