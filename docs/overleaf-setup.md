# Overleaf status and verified ZIP fallback

Assessed 2026-11-25. **No live Overleaf MCP read, edit, compile or PDF download was performed.** The active tool directory and local MCP list expose no Overleaf server. Plugin Management search returned no matching plugin. A local LaTeX command is not MCP operation evidence.

## Configuration investigation

The source-available [kimhyunji24/mcp-overleaf](https://github.com/kimhyunji24/mcp-overleaf) is explicitly unofficial. Its README was reviewed (blob `3d1c29d3d01a3500f0ac6e355d53bfd4b74f53b9`); this is not a security audit or successful installation. The documented Git mode uses Overleaf's supported Git bridge, requires an authorized project and token, and depends on the project's plan. Remote ChatGPT use adds HTTPS hosting/OAuth configuration. Optional web/session-cookie mode talks to internal endpoints and was not enabled.

Official sources checked: [Git/token authentication](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration/git-integration-authentication-tokens), [Git integration and plan context](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization). Git support alone does not establish remote compilation support.

Missing prerequisites: a user-authorized Overleaf project ID, appropriate account/plan access, token provision through trusted settings, a reviewed/pinned server implementation, and a live client connection. Do not place credentials in this repository or paste them into manuscript artifacts. No credentials were requested or extracted, and no unreviewed remote installer was executed. No Overleaf error code is fabricated: there was no callable service tool to invoke. The exact local-tool and discovery observations are in the environment reports.

## Delivered fallback

- [V1 source ZIP](../deliverables/Overleaf_V1.zip): source-only, direct and freshly extracted clean build passed.
- [V2 source ZIP](../deliverables/Overleaf_V2.zip): same independent-build verification.
- Both include `main.tex`, the complete preamble/sections/original TikZ figures, references.bib and source README; no cross-version inputs or secrets.
- Choose pdfLaTeX, `main.tex`, and a recent TeX Live release when uploading to Overleaf. IEEEtran and the documented packages are standard TeX dependencies.
- Exact checks/hashes: [V1](validation/v1-build.json), [V2](validation/v2-build.json). Both extracted-ZIP PDFs matched their direct-source PDF text. Actual online import/rendering remains unverified.

## Future live MCP verification

After the user establishes the trusted project connection, verify read access first. A genuine manuscript edit requires a fresh OpenSpec change and an independent version; do not rewrite the frozen V1/V2 snapshots. Execute the authorized edit, re-read the affected content, compile only if supported, and retain sanitized tool responses and artifact checks. Never equate a successful local or Git-only operation with Overleaf's web compiler.
