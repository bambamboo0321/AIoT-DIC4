# Phase 0.5 environment configuration

Date: 2026-11-25 (Asia/Taipei). The continuous-execution instruction authorizes necessary dependency installation, repository-local identity configuration, commits, and a final push. The original Phase 0 audit is preserved as a historical observation; this document records remediation.

## Identity and Git

Authenticated GitHub login and numeric ID match the identity already used by the repository's existing commits. Reused that account's GitHub noreply identity in repository-local `user.name` and `user.email`; no global Git configuration changed. These are commit metadata, not manuscript author attribution.

The authenticated-user email endpoint returned HTTP 404 because its required user scope was absent. No additional scope was requested: the existing matching noreply identity provided reliable attribution. Phase 0 report commit: `d62f977` (`docs: record Phase 0 environment audit`).

## Installed toolchain

| Component | Observed version / location | Method |
|---|---|---|
| Node / npm | 24.13.1 / 11.8.0 | Existing nvm environment |
| OpenSpec | 2.2.0 | Official npm package, fixed version, `--ignore-scripts --no-audit --no-fund`, prefix `/private/tmp/smartintake-tools/openspec` |
| TinyTeX | Stable v2026.11; TeX Live 2026 | RStudio release archive, extracted without a shell installer or sudo |
| pdfTeX | 3.141592653-2.6-1.40.29 | TinyTeX `bin/universal-darwin` |
| latexmk | 4.88 | Same installation |
| BibTeX | 0.99e | Same installation |
| latexdiff | 1.4.0 | TeX Live package manager |
| Poppler | 26.11.0 | Homebrew; `pdfinfo` and `pdftoppm` return versions successfully |

OpenSpec npm metadata reported Node >=22.20.0, satisfied by the existing runtime. No npm upgrade was performed. Project schema is `spec-driven` (package schema version 1); `init --tools none --scope project --no-animation` created the local config without global assistant skill installation. Inspected the installed templates and `new change`, `validate`, and `archive` help. The course-required `goal.md` supplements the schema's four standard artifacts; CLI validation alone does not verify that extra course file or manuscript quality.

BasicTeX was considered first: its official Homebrew cask uses a macOS package installer. Selected the portable TinyTeX alternative to keep the TeX installation small and avoid administrator rights. Downloaded `TinyTeX-1-darwin-v2026.11.tar.xz` (67,211,812 bytes); its SHA-256 matched the release metadata:

```text
9416a257c4caea2f82351fa2f89252b8bd75dceeb0ce6e442d25530b1922a02d
```

The archive is from the [RStudio TinyTeX release](https://github.com/rstudio/tinytex-releases/releases/tag/v2026.11). The archive's paths were checked before extraction. No `curl | sh`, sudo, shell-startup edit, or credential disclosure was used. Tool paths are supplied per command; the `/private/tmp` installation is temporary and must be recreated if cleaned by the OS. Build instructions will describe ordinary PATH-based use on other machines.

IEEEtran and its BibTeX style are resolved successfully by `kpsewhich` from `texmf-dist` after installing `ieeetran`. Installed `pgf` for original TikZ diagrams; `booktabs` was already present. The first package attempt exited 255 because tlmgr required a self-update. Updated tlmgr from the verified CTAN repository, then the package installation succeeded. The toolchain's package manager verifies the selected mirror metadata.

The first IEEEtran/BibTeX smoke build exited 0 and produced a one-page PDF. The first latexdiff command exited 0 with a harmless warning that no listings package was detected; its PDF build initially failed because `ulem.sty` was missing. Remediation and subsequent checks are recorded below.

Homebrew automatically refreshed its metadata and installed/upgraded Poppler dependencies, then performed its normal cleanup of old dependency versions. This affected the Homebrew prefix; it did not change Git global config, shell startup files or authentication. No separate broad `brew upgrade` was invoked.

## Overleaf boundary

No Overleaf server is exposed in the active tool set or local MCP list. Phase 0 Plugin Management search returned no matching plugin. Investigated the source-available, **unofficial** [mcp-overleaf](https://github.com/kimhyunji24/mcp-overleaf) README (blob `3d1c29d3d01a3500f0ac6e355d53bfd4b74f53b9`). This was a documentation assessment, not a source-code security audit or execution test.

Its Git mode uses the documented Overleaf Git integration and needs an authorized project ID and Git token. Its remote mode additionally requires an HTTPS deployment and OAuth configuration. Web compilation uses an optional session-cookie mode and internal endpoints; this path was not enabled. The [official token documentation](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/git-integration/git-integration-authentication-tokens) confirms token-based Git authentication; the [official integration documentation](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization) describes plan requirements.

No Overleaf project ID, token or authenticated MCP connection was supplied. No server was installed with credentials, no browser cookies were extracted, and no Overleaf read/edit/compile operation is claimed. Continue with independently compiled ZIPs; service verification remains a separate blocked operation.

## Sources checked

- [OpenSpec official installation](https://github.com/Fission-AI/OpenSpec/blob/main/docs/installation.md): package installation and runtime requirement; installed schema/help took precedence for actual CLI usage.
- [BasicTeX cask](https://formulae.brew.sh/cask/basictex): compact macOS package option.
- [TinyTeX maintainer repository](https://github.com/rstudio/tinytex-releases): portable prebuilt distribution and release metadata.
- [TeX Live documentation](https://tug.org/texlive/doc/texlive-en/texlive-en.pdf): installation in user-writable locations.

## Verification completion

Pending final smoke recheck after the missing latexdiff dependency is installed. Manuscript-specific compilation, bibliography and visual evidence belong to each version's validation report.
