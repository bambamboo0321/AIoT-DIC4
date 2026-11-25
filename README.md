# SmartIntake — AIoT DIC4

**Verified deliverables:** a complete IEEE conference V1, an actual academic review, a substantive V2 revision, independent Overleaf source ZIPs and a genuine V1/V2 latexdiff. V1 is preserved. Both papers describe a proposed system and prospective E1-E5 evaluation; no measured research results or verified running deployment are claimed.

| Version | Source | PDF | Overleaf ZIP | Git tag |
|---|---|---|---|---|
| V1 (5 pages) | [Source](paper/v1-initial/) | [Initial paper](deliverables/SmartIntake_V1_Initial.pdf) | [V1 ZIP](deliverables/Overleaf_V1.zip) | `v1.0-initial-draft` |
| V2 (7 pages) | [Source](paper/v2-revised/) | [Revised paper](deliverables/SmartIntake_V2_Revised.pdf) | [V2 ZIP](deliverables/Overleaf_V2.zip) | `v2.0-revised-draft` |

Compare the [8-page latexdiff PDF](deliverables/SmartIntake_V1_V2_Diff.pdf), [flattened diff source](deliverables/SmartIntake_V1_V2_Diff.tex) and [complete unified source diff](deliverables/V1_V2_source.diff). Blue denotes additions; red denotes deletions. The diff includes both bibliographies and renders the entirely new lifecycle table as one intact added block.

Read the [actual V1 review](reviews/v1-review.md), [R1-R9 revision trace](reviews/revision-report.md) and [V2 follow-up/V3 decision](reviews/v2-review.md). V3 is deliberately deferred until a substantive new method issue, external feedback, implementation verification or measured evidence exists.

## Research scope

SmartIntake targets fixed laboratories/offices using a Raspberry Pi 4, two separate Load Cell/HX711 scales, FastAPI, Supabase PostgreSQL, Discord and an n8n tool-grounded read-only agent. The method distinguishes weight change from ingestion, inferred from confirmed records, physical session ownership from query identity, and missing observations from zero. Food calculations require known net mass or explicitly labeled reference portions.

The [latest prospective protocol](experiments/evaluation-plan-v2.md) covers E1 weight accuracy, E2 event detection, E3 shared-session consistency, E4 recording burden and E5 agent reliability. All counts are proposed, not completed trials. [Verified citations](research/citation-mapping.md) and the [claim-evidence map](research/claim-evidence-map.md) bound the literature and research claims.

## Verification and OpenSpec

- [Phase 0 audit](docs/environment-audit.md) preserves the initial failures; [environment remediation](docs/environment-setup.md) records actual installations, retries and final paths.
- [V1 validation](docs/validation/v1-validation.md) and [V2 validation](docs/validation/v2-validation.md) record builds, bibliography, all-page visual inspection and clean extracted-ZIP builds. Hash manifests are linked there and in the validation directory.
- OpenSpec 2.2.0 strict checks passed. Two completed changes are [archived](openspec/changes/archive/) with course `goal.md`, proposal, design, tasks and delta specs; the [current specification](openspec/specs/ieee-manuscript/spec.md) has 13 requirements.
- [Final automated checks](docs/validation/final-checks.json) verify frozen hashes, ZIP members, readable PDFs, embedded fonts, completed archives and selected secret patterns. Manual content/visual review remains necessary.
- [Build and package instructions](docs/build-instructions.md) describe the ordinary TeX Live dependencies and reproducible commands. No private implementation repository is needed to build these manuscripts.

## Overleaf and remaining prerequisites

**Overleaf MCP was unavailable:** no authorized project/token/live server connection was supplied. [Configuration investigation and fallback](docs/overleaf-setup.md) distinguish actual observations from future setup. Both ZIPs compiled independently locally; online Overleaf import/compilation remains unverified.

Authors and affiliations remain explicit placeholders pending team confirmation. Hardware parameters, implementation/concurrency/security tests, participant consent/review as applicable and formal E1-E5 results remain pending. This is a course design/protocol manuscript package, not an empirical or clinical effectiveness claim.

## Project guidance

[AGENTS.md](AGENTS.md), [project context](docs/PROJECT_CONTEXT.md), [roadmap](docs/ROADMAP.md), [acceptance status](docs/ACCEPTANCE_CRITERIA.md), [final validation](docs/final-validation.md), and [changelog](CHANGELOG.md).

The authorized [original SmartIntake project](https://github.com/bambamboo0321/AIOT-final) is the implementation authority; private files were not copied here. [RayWu576/AIoT-DIC4](https://github.com/RayWu576/AIoT-DIC4) was used only for delivery structure, not its research content or results. No tokens, credentials, private source files, health records or identifiable screenshots belong in this public repository.
