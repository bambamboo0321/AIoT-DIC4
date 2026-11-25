# Changelog

## Workspace initialization — 2026-11-25

Created initial README, agent guidance, research outline, roadmap, acceptance checklist and placeholder directory documentation. No paper, experiment, OpenSpec validation or MCP execution is claimed. Next: local Phase 0 environment audit.

## Continuous DIC4 delivery — 2026-11-25

- Committed the real Phase 0 audit (`d62f977`), confirmed matching GitHub noreply identity and set repository-local Git config.
- Installed official OpenSpec 2.2.0 without npm lifecycle scripts; initialized the installed spec-driven schema. Configured checksum-verified portable TinyTeX/TeX Live 2026, required packages and Poppler; recorded actual missing-package failures and successful smoke retries.
- Validated/committed V1 specifications before drafting (`0d31549`). Released complete five-page IEEE V1, independently rebuilt source ZIP, verified bibliography/pages/hashes, archived the completed change and tagged `v1.0-initial-draft` at `c90dada`.
- Reviewed the actual V1 in a separate commit (`6a8971e`), then validated/committed R1-R9 V2 requirements before editing (`dfbca8e`).
- Released seven-page V2 with lifecycle, quantity, session, snapshot and E1-E5 scoring refinements; preserved V1, independently rebuilt V2 ZIP and produced a real eight-page latexdiff including bibliographies. Archived the verified change and tagged `v2.0-revised-draft` at `c09bd42`.
- Completed V2 follow-up review (`f29f96e`); deferred V3 because no further substantive manuscript issue or new implementation/measurement evidence was supplied.
- Documented actual Overleaf MCP/configuration blockers and locally verified ZIP fallback (`956bb7a`); no service operation was fabricated.
- Moved local tools to ignored `.tools/` for persistence, rechecked tool lookup and smoke compilation, and updated release instructions/acceptance evidence. Generated comparison files retain native whitespace under repository attributes.
- Authors, physical implementation verification, actual E1-E5 results and live Overleaf execution remain pending. Final normal GitHub push occurs only after the public-package validation; no force push or unrelated repository mutation is used.

- Final atomic publication succeeded at `8b03980`; a separate live remote query verified main and both annotated/peeled tags. Preserved the observed publication receipt in a subsequent documentation commit without moving version tags.
