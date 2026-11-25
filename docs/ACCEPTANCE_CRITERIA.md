# Acceptance criteria

Observed status as of 2026-11-25. Checks below attest the manuscript package, not physical implementation or research outcomes.

- [x] Phase 0 reports real environment/tool availability and repository status. Evidence: `environment-audit.md`; subsequent remediation is in `environment-setup.md`.
- [x] IEEEtran conference source compiles without fatal errors; bibliography resolves; rendered pages inspected. V1: 5 pages; V2: 7; actual diff: 8. See version validation reports.
- [ ] Author attribution confirmed by team. Explicit author/affiliation/contact placeholders remain; no names were invented. Commit identity is separate.
- [x] References verified against original sources; claims mapped to evidence. Eight references; `research/citation-mapping.md` and `claim-evidence-map.md`.
- [x] Each manuscript revision has prior OpenSpec goal, proposal, design, tasks and valid delta specs. Specification commits precede V1/V2 writing; archives preserve all course artifacts.
- [x] OpenSpec validation command, version and actual result recorded. CLI 2.2.0; strict checks and completed-archive checks passed.
- [x] V1 preserved; V2 addresses actual numbered review findings. R1-R9 map to requirements/design/tasks/source differences/validation. V2 was re-reviewed; V3 deferred for substantive evidence.
- [x] Separate source snapshots, compiled PDFs, import ZIPs and comparison/report verified. Both ZIPs rebuilt in clean directories with equal PDF text to direct builds.
- [x] Git commits and local tags correspond to actual milestones; no fabricated chronology. V1 `c90dada`; V2 `c09bd42`; two annotated version tags.
- [x] E1-E5 protocols define ground truth, baselines, metrics and limitations; results remain pending until measured. V2 defines prospective counts and scoring without fabricated data.
- [x] Explicit Overleaf MCP unavailable status and verified ZIP fallback exist. Actual online MCP/import/compiler operations remain unverified; see `overleaf-setup.md`.
- [x] Public artifacts reviewed for secrets, personal records and private source material. Hash/package/selected secret-pattern checks supplement manual source/PDF/ZIP inspection; no scan is represented as a universal proof.
- [x] README links verified deliverables, reviews, tags and status; unresolved blockers are visible.

## Still required for research completion

- [ ] Hardware configuration/calibration and executable module/concurrency/security verification.
- [ ] Frozen physical parameter manifest and actual E1-E5 measurements/analysis.
- [ ] Participant consent/institutional review as applicable before personal-data collection.
- [ ] Team-confirmed author metadata and genuine Overleaf service verification if required later.

V3 is not an unmet version-count target: it requires a substantive new research reason. These pending items must not be marked complete by additional prose, generated logs or invented data.
