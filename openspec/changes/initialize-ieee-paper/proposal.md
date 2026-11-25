# Proposal

## Why

The workspace has no manuscript. DIC4 requires an initial IEEE paper with traceable evidence and independently usable artifacts before any review-driven revision.

## What Changes

- Create a complete English IEEEtran conference manuscript in `paper/v1-initial`.
- Cover the two-scale Raspberry Pi design, FastAPI/Supabase, Discord/n8n agent, session switching, food calculations and E1-E5 plans.
- Add verified references, original diagrams, labeled equations/tables, a build/package command and version-specific validation evidence.
- Preserve author placeholders and explicitly distinguish proposed design from unverified implementation and pending measurements.

## Capabilities

### New Capabilities

- `ieee-manuscript`: Readers receive an evidence-bounded manuscript and reproducible, independently buildable versioned deliverables.

### Modified Capabilities

None. `openspec list --specs` returned no existing specifications.

## Impact

Adds manuscript, research provenance, build tooling, evaluation documentation and deliverables. Does not implement the private SmartIntake application, collect participant data, or access Overleaf without credentials. Dependencies are IEEEtran/TeX Live, BibTeX, latexmk, latexdiff and Poppler.
