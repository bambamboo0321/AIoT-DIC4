# GitHub publication verification

Observed: 2026-11-25T20:56:34+08:00.

The user-authorized final publication batch succeeded:

```text
git push --atomic origin main refs/tags/v1.0-initial-draft refs/tags/v2.0-revised-draft
exit 0
519b555..8b03980  main -> main
[new tag] v1.0-initial-draft
[new tag] v2.0-revised-draft
```

A separate live `git ls-remote origin` check matched every local target:

| Remote ref | Observed SHA |
|---|---|
| `refs/heads/main` | `8b03980dda5aee954973f1a82e76aaecd84f564e` |
| `refs/tags/v1.0-initial-draft` | `a37eb243b0ed4a12900298426588bdfcd6fe7fb9` |
| `refs/tags/v1.0-initial-draft^{}` | `c90dadace2cee9ec43be0499dfbd33792ed4e393` |
| `refs/tags/v2.0-revised-draft` | `d326dd00c74c36e733d9cc87e204a8f96fd4dfb2` |
| `refs/tags/v2.0-revised-draft^{}` | `c09bd4283be50c0aa1cffa2c5115a1c182f9ff5b` |

Repository: [bambamboo0321/AIoT-DIC4](https://github.com/bambamboo0321/AIoT-DIC4). The peeled annotated-tag targets are the genuine V1 and V2 release commits. No force push, tag replacement or write to another repository occurred.

This receipt records the publication batch at the observation time. A subsequent ordinary documentation commit preserves this receipt and updated validation; it does not move either manuscript tag. Final branch synchronization is checked again after that push. Research results, authors and live Overleaf operations remain pending as documented.
