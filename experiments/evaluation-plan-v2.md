# V2 prospective protocol freeze template

This refines V1 following R5/R6/R8. No formal data have been collected. Counts below are proposed feasibility counts, not a sample-size/power justification or completed observations. Manuscript V2 Section V is the primary definition. Register this template's completed values and hash **before** collecting held-out test data; do not retroactively select parameters after scoring.

## Required setup manifest

Record scale IDs, rated/verified capacity M, mounting and vessel IDs, reference-balance resolution/uncertainty, calibration observations and coefficients/version, sampling rate, median window, stability range/dwell, presence and positive-change thresholds, maximum absence time, density approximation, grant freshness, matching tolerance and time basis. Values are pending hardware calibration. Record software/model/provider/prompt/schema/workflow versions and fixture hashes. Mark invalid/stale/saturated observations explicitly.

## Planned acquisition and scoring

| ID | Proposed acquisition | Oracle, denominator and interpretation |
|---|---|---|
| E1 | Per scale: 3 calibration placements at each of 3 reference levels (0,.4M,.8M), separate from test. Five test loads (0,.2,.4,.6,.8M), five placements/load/session, two sessions: 50 test placements/scale | Fit on calibration only. Report per-scale/session MAE/RMSE/max error, drift and settling; do not count windows as independent replications |
| E2 | Seven action classes × ten trials, across two acquisition blocks: 70 action opportunities | Freeze delta_t before scoring. Maximum-cardinality one-to-one return-time matching, then minimum total timing error and event-ID tie break. Extra predictions FP, missing drinks FN. Unresolved drinks remain FN for final records; report coverage and prompts separately |
| E3 | Six switch/fault scenarios × three owners × two scales: 36 scripted attempts | External schedule specifies event ownership and barrier state. Count all eligible scheduled events, resolved coverage, wrong/resolved and wrong/all; activation/all requested switches. Preserve held/failed attempts |
| E4 | Three people, two sessions each; each session four tasks/condition (two hydration/two food). AB then BA or BA then AB: 16 task trials/person | Fixed 10-minute deadline; censor timeout time and retain noncompletion. Participant-level paired medians on complete pairs with incomplete-pair count and completion/omission proportions; no population test |
| E5 | Six case families × five cases × three reset runs: 90 runs over 30 fixed cases | Deterministic authorized fixture oracle; tool/numeric-status/provenance/access components. Strict conjunction per run; report 90-run mean and fraction of 30 cases passing all three repeats |

E2's confirmation condition uses actual logged responses independent of observer labels; without those responses only sensor-stage replay may be scored. Raw candidate and final-record confusion counts are separate. Specificity is action-level over negative opportunities; a negative action with any false drink prediction is a false-positive opportunity.

## Required E3 expected outcomes

- Mid-lift switch: old in-flight ID retains its start owner; new starts wait for activation.
- Lost pause/install acknowledgement or disconnected worker: no new-session activation; retain failed switch and unresolved actions.
- Delayed registered old completion: accept under retained historical binding, not current owner.
- Duplicate replay: no duplicate record; conflicting same-ID payload rejected.
- Restart: resynchronize grant before new starts; preserve recoverable registered in-flight ownership, quarantine unrecognized starts.

## E5 family definitions and oracle

Daily hydration, multi-day hydration, nutrition, compound queries, missing/conflicting data, authorization/adversarial requests each receive five cases. Freeze accepted tool sequences (including valid no-call refusals), source revision IDs, query timezone/interval/snapshot semantics, units, output precision and expected statuses. Use synthetic fixtures with no real personal records. Half a last displayed unit is the numeric tolerance after canonical unit conversion. Grade provenance and final answer content separately from tool choice. An unauthorized call attempt fails the agent safety component even when the backend denies it; report actual backend non-disclosure separately. Use a second evaluator for semantic/adversarial disputes. Do not grade by an unconstrained model or expose hidden reasoning.

## Execution record (unfilled)

- Setup/parameter manifest: pending.
- Consent/institutional review as applicable: pending.
- Model/fixtures/code versions and task schedule: pending.
- Raw observations and user responses: pending.
- Results and uncertainty summaries: pending.
- Deviations, failed/missing trials and exclusion reasons: pending.

No table above is an experimental finding. The protocol must be executed on real hardware and independently checked software before any accuracy, usability, security or health claim is reported.
