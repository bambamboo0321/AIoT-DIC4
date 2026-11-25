# Simulated IEEE-style review of the actual V1

Reviewed 2026-11-25 after V1 commit `c90dada`, tag `v1.0-initial-draft`. Artifact: `deliverables/SmartIntake_V1_Initial.pdf` (5 pages), source in `paper/v1-initial`. This is an agent-performed academic review, not an external peer review or conference decision. All pages/source were read; the initial draft was complete and usable, not deliberately weakened.

## Overall assessment

V1 presents a coherent integration design, appropriately cautious novelty claims, verified literature and a credible E1-E5 outline. Its strongest points are the explicit ingestion ambiguity, server-side user authorization, source retention and honest absence of measurements. It is a suitable initial course research draft. As an empirical conference submission it would require real implementation and experiments; that cannot be fixed by inventing results. The actionable concerns below concern the reproducibility of the proposed method and its evaluation, not a demand for fabricated performance.

## Review issues

### R1 — Operationalize the research contribution

- **Severity:** Moderate
- **Section:** I-II, V; pp. 1-2, 3-4.
- **Problem:** The research questions and selected literature are clear, but the paper does not identify a primary observable outcome for each question. Table I's design implications do not distinguish what will be tested from the relevance of earlier work.
- **Evidence:** RQ2 combines attribution and interaction burden; Table II lists five experiments without explicit RQ-to-outcome mapping. The related-work conclusion describes a scoped integration gap but not a falsifiable boundary for that contribution.
- **Recommendation:** Add a compact RQ/claim/primary-outcome map and a paragraph distinguishing the integration's testable obligations from new sensing/model algorithms.
- **Acceptance Criteria:** Every RQ maps to E1-E5 and a named primary outcome; no global first-of-kind or proven-benefit claim is introduced.

### R2 — Make FSM lifecycle executable as a specification

- **Severity:** Major
- **Section:** IV-A/B, Fig. 2; pp. 2-3.
- **Problem:** The workflow lacks full state exit/re-entry guards. An implementer cannot determine how cold start, timeout, a changed container, or unresolved mass comparison re-establishes the next baseline.
- **Evidence:** Fig. 2 ends in two disposition boxes without reset transitions. IV-A defines window range/dwell but no sampling/window parameters or initialization rule; IV-B refers to timeout and calibrated thresholds without their lifecycle semantics.
- **Recommendation:** Define states, guards, disposition and re-arming, with a parameter manifest and a fail-closed reset path. Do not assign measured thresholds before calibration.
- **Acceptance Criteria:** A state/transition table covers initialization, lift, stable return, timeout, disturbance and container reset; all guards reference defined parameters and invalid paths cannot generate a new inferred intake.

### R3 — Define invalid quantities and correction-aware totals

- **Severity:** Moderate
- **Section:** IV-A/C, Eqs. (1)-(3); pp. 2-3.
- **Problem:** Mass-to-volume and nutrient formulas are dimensionally useful, but behavior for negative tared mass and uncertain differences is unspecified. Totals are described without a formal rule excluding rejected/superseded versions or separating inferred from confirmed amounts.
- **Evidence:** Eq. (3) permits an algebraic negative net mass. IV-B preserves correction history; IV-E says the backend computes totals without defining which record versions contribute.
- **Recommendation:** State invalid-input rejection and uncertainty assumptions, and define aggregation over current non-rejected records with confidence/status partitions and missing-value semantics.
- **Acceptance Criteria:** Negative/unstable/unknown inputs cannot produce ordinary nutrient values; equations define a single active correction version and inferred/confirmed totals; any uncertainty relation states its assumptions.

### R4 — Resolve the sensor/backend session race

- **Severity:** Major
- **Section:** III, IV-D, V-C; pp. 2-4.
- **Problem:** Event-start version binding is an appropriate invariant, but a transactional backend switch alone does not coordinate the two sensor workers, especially on delayed messages, restart or disconnection.
- **Evidence:** IV-D gives `v_e = v(t_start)` and a transaction, but does not specify how the server validates a stale worker's claimed event start or when a switch becomes effective at both scales. E3 mentions replay without a fault schedule.
- **Recommendation:** Specify a two-worker switch barrier, durable in-flight event binding, stale-grant quarantine and explicit backend commit/activation ordering. Extend E3 with corresponding failure cases.
- **Acceptance Criteria:** A mid-lift switch, lost acknowledgement, delayed old completion, duplicate replay and worker restart have unambiguous expected outcomes; new events never inherit ownership solely from upload time.

### R5 — Fix E1/E2 trial units and event matching

- **Severity:** Major
- **Section:** V-A/B, Eq. (5); pp. 3-4.
- **Problem:** The experiments identify appropriate reference methods but do not provide planned repetition counts or a one-to-one event-matching policy. Different implementations can produce different precision/recall from the same trace.
- **Evidence:** E1 says reference loads are placed repeatedly; E2 says 'For matched events' without defining matching tolerance, duplicate candidates or timeouts. The external protocol file also leaves counts and final rules for a later freeze.
- **Recommendation:** Define prospective counts, independent calibration/test blocks, frozen matching tolerance, maximum-cardinality one-to-one matching and treatment of duplicate/missing/unresolved records. Keep physical load values conditional on the documented capacity.
- **Acceptance Criteria:** Another evaluator can calculate TP/FP/FN and trial denominators without choosing rules after seeing outputs; no proposed count is represented as measured data.

### R6 — Clarify pilot estimands and incomplete trials

- **Severity:** Moderate
- **Section:** V-C/D; p. 4.
- **Problem:** The three-person feasibility restriction is appropriate, but the repeated-task unit, switch denominator and noncompletion treatment remain underspecified.
- **Evidence:** E3 reports wrong attribution over 'attributable events' without a coverage denominator. E4 asks to counterbalance an odd-sized pilot but does not define a schedule, timeout rule or participant-level comparison statistic.
- **Recommendation:** Report resolved-event coverage alongside wrong attribution. Specify a balanced within-person two-session schedule, proposed task count, noncompletion deadline and descriptive participant-level paired summaries.
- **Acceptance Criteria:** Failed/unresolved events and timed-out tasks cannot disappear from denominators; repeated tasks are not presented as independent participants or a powered effectiveness study.

### R7 — Specify the query/provenance consistency boundary

- **Severity:** Major
- **Section:** III, IV-E, VI, Fig. 3; pp. 2-5.
- **Problem:** Authorization and missingness are described well, but the answer lacks an explicitly required query snapshot, day-boundary rule and minimum provenance envelope. Concurrent correction could make a total and its cited records inconsistent.
- **Evidence:** IV-E lists interval/timezone/units/sources but does not define interval inclusion, aggregate snapshot consistency or record revision IDs. VI mentions timezone and prompt-injection risks without concrete acceptance cases.
- **Recommendation:** Define half-open local-calendar queries converted to UTC, one consistent database snapshot, returned record/correction versions and tool/schema versions. Treat source text as untrusted data; test forged subjects and unsupported tool requests.
- **Acceptance Criteria:** The contract distinguishes no data, observed zero, partial coverage and denied access; one answer's numeric total can be recomputed from its authorized record revisions as of the returned snapshot.

### R8 — Make E5 scoring reproducible

- **Severity:** Major
- **Section:** V-E; p. 4.
- **Problem:** 'At least 30' and 'repeatedly' leave case allocation, number of repeats, numeric tolerance and the conjunction of correctness/safety undefined.
- **Evidence:** V-E lists families and metadata but not a scoring rule or independent answer oracle. Per-run correctness and repeat consistency have no explicit denominator/formula.
- **Recommendation:** Propose 30 cases in six families, three reset runs each, deterministic fixture arithmetic, separate tool/number/provenance/authorization scores and strict all-components success. Define empirical repeated-case reliability rather than borrowing τ-bench's state-changing task metric unchanged.
- **Acceptance Criteria:** The 90 planned runs have explicit pass criteria and case/run denominators; an unauthorized disclosure or fabricated zero fails despite other correct fields; results remain unfilled.

### R9 — Improve comparison-table and reference usability

- **Severity:** Minor
- **Section:** Table I, bibliography; pp. 2, 5.
- **Problem:** Narrow justified cells cause fragmented work names and conspicuous word spacing. Three publication DOIs exist in the BibTeX source but are not printed by this IEEEtran bibliography style.
- **Evidence:** Table I breaks Playful Bottle and ReAct/Toolformer into multiple short lines; the rendered bibliography lacks DOI links for the three DOI-verified publications.
- **Recommendation:** Use ragged-right table columns and compact work labels; expose DOI URLs in the bibliography without changing verified metadata.
- **Acceptance Criteria:** Revised table and reference links are readable in rendered pages, with zero overfull boxes and no new missing citation.

## Coverage of requested review dimensions

| Dimension | Assessment / issues |
|---|---|
| Motivation, gap, novelty/contribution | Appropriate scope; sharpen operationalization (R1) |
| Related work, citation quality | Eight verified sources; scoped comparison and metadata discoverability (R1, R9) |
| Architecture, methodology, reproducibility | Coherent data flow; lifecycle, quantity and race details (R2-R5, R7) |
| Experimental design | Relevant E1-E5; matching, units, denominators and scoring (R5, R6, R8) |
| Agent reliability, security/privacy | Server boundary is sound in design; snapshot and adversarial acceptance details needed (R7, R8) |
| Writing, figures/tables | Complete readable IEEE draft; formalize workflow and refine table typography (R2, R9) |
| Evidence limits | No results invented; physical implementation, authors and human research approvals remain pending |

Recommended next action: revise the proposed methods and evaluation specificity under a new OpenSpec change, preserve the frozen V1, and continue to label this work as design/protocol research.
