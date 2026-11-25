# SmartIntake research context

Working title: SmartIntake: An IoT and Tool-Grounded AI Agent-Based System for Hydration and Dietary Tracking.

This is a public-safe research outline, not a verified implementation report. Confirm details against authorized project sources and team decisions before manuscript claims.

## Scope
Fixed laboratories/offices, not a portable smart bottle. Proposed architecture: Raspberry Pi 4, two separate Load Cell/HX711 scales, sensor worker, FastAPI, PostgreSQL, Discord interface and n8n tool-grounded agent.

## Research questions
1. Can weight sensing and event confirmation support reliable hydration recording despite ambiguous weight changes?
2. Can shared-device attribution and semi-automatic entry reduce recording burden relative to manual entry?
3. Can an authorized, tool-grounded agent produce traceable and numerically correct summaries?

## Method boundaries
A reduction in stable cup weight is a candidate event, not proof of ingestion. Distinguish refills, spills and container changes. Food nutrient calculations require known net weight or explicitly labeled reference portions. Session version at event start should govern attribution. Agent tools should be read-only, authorized server-side, and distinguish missing data from zero.

## Planned evaluation
E1: weight accuracy (MAE, RMSE, maximum error).
E2: event detection (precision, recall, F1 and confirmation burden; weight-delta vs FSM vs confirmation).
E3: three-user/two-scale switching (wrong attribution, success rate, time).
E4: manual vs semi-automatic recording (time, actions, omissions, completion).
E5: at least 30 agent cases (tool choice, values, provenance, authorization, safety).

No formal E1–E5 results have been supplied for this manuscript workspace. Do not report improvements as demonstrated. Any preliminary integration claim needs evidence and explicit scope. Image-based food estimation, external health imports and wellness scores are future work, not MVP claims.
