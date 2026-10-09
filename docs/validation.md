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

After publication, the GitHub source `krema/agent-skills` was also checked:

- Claude Code registered the remote marketplace and installed `skills@krema` 1.0.0 successfully in a fresh temporary profile.
- GitHub Copilot CLI registered the remote marketplace and installed all five skills successfully in a fresh temporary profile.
- `npx skills add krema/agent-skills --list` cloned the public repository and discovered all five public names.
- The initial [GitHub Actions validation run](https://github.com/krema/agent-skills/actions/runs/37982613289) passed.

These checks verify packaging, installation, and discovery, not successful execution of every skill on each agent. No model tasks or comparative behavioral benchmarks were run for this packaging release.

Source-package evaluation reports are historical and may use original skill names or source version numbers. Collection version 1.0.0 describes this distribution, not a reset of the source research history.

Package delivery, manifest acceptance, skill discovery, and correct agent behavior are different checks. This publication does not claim a measured performance improvement or cross-model behavioral equivalence.

## Version 1.1.0 additions — 2026-10-09

- Eight skills and six native manifests pass collection validation, including all 70 skill-file hashes and relative Markdown links.
- All six synchronization tests and 28 included Python-tooling tests pass.
- The skills CLI discovers all eight public identifiers from the local release candidate.
- A repeat selective import reports no changes. Ticket Craft preserves the original writing rules; Research to Skill changes installation guidance; Learning Loop is a substantial adaptation.
- The plugin layout is unchanged. Native installation checks above apply to version 1.0.0; they were not rerun for 1.1.0. No new cross-agent behavioral trial was performed. Learning Loop has author walkthroughs and structural checks only; background capture is neither bundled nor tested.
- The privacy review is documented in [privacy-review.md](privacy-review.md).
