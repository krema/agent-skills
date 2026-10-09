# Distribution validation

Validation performed for the initial publication on 2026-10-09:

| Check | Result |
| --- | --- |
| Collection structure | Five skills, six native manifests, all 47 skill-file hashes, and Markdown file links passed. |
| Synchronization | Six tests passed: renaming without source edits, idempotency, independent-edit protection, symlink/private-path rejection, stale-file removal, omitted-skill protection, and selective import of completed sources. Some tests cover more than one property. |
| Included Python tooling | All 28 analyzer and evaluation-preparation tests passed after publication renaming. |
| Claude Code 2.1.7 | Plugin and marketplace validation passed. Registered the local marketplace and installed `skills@krema` in a temporary `CLAUDE_CONFIG_DIR`; plugin list reported version 1.0.0 enabled. All 47 installed skill files matched the published files byte-for-byte. |
| GitHub Copilot CLI 1.0.88 | Registered the local marketplace and installed `skills@krema` in a temporary `COPILOT_HOME`. The client reported five installed skills and an enabled plugin. Local marketplaces load live from the source directory in this client. |
| Codex CLI 0.161.0 | Native catalog discovery with an ephemeral marketplace configuration returned `skills@krema`, version 1.0.0, with installation policy AVAILABLE. No personal-profile native installation was performed. |
| `npx skills` | Installed all five skills into a temporary project targeting `claude-code`, `codex`, and `github-copilot` with `--copy`. Both the shared `.agents/skills` tree and `.claude/skills` tree matched all 47 files. |
| Repeat import | A second source-map check reported no changes. |

These initial client checks used the local source directory. They verify packaging and discovery, not successful execution of every skill on each agent. No model tasks or comparative behavioral benchmarks were run for this packaging release.

Source-package evaluation reports are historical and may use original skill names or source version numbers. Collection version 1.0.0 describes this distribution, not a reset of the source research history.

Package delivery, manifest acceptance, skill discovery, and correct agent behavior are different checks. This publication does not claim a measured performance improvement or cross-model behavioral equivalence.
