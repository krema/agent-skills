# Krema Skills

A growing collection of reusable skills for **Claude Code, Codex, and GitHub Copilot**.

Install the complete collection as **`skills@krema`**, or choose individual skills with `npx skills`. Each skill includes practical instructions and supporting references. The initial collection focuses on agent workflows; future skills can cover other topics.

[Browse the skills](#skills) · [Install](#install) · [Updates](#updates) · [Evidence and validation](#evidence-and-validation) · [Contributing](CONTRIBUTING.md)

## Skills

| Skill | Use it when… | Example request |
| --- | --- | --- |
| [Agent Instructions](skills/agent-instructions/SKILL.md) | Repository instructions are stale, contradictory, or hard to follow. | “Audit our AGENTS.md and CLAUDE.md. Fix conflicts while preserving project requirements.” |
| [Context Management](skills/context-management/SKILL.md) | A long task loses constraints, repeats work, or needs a reliable handoff. | “Prepare a handoff that preserves decisions, unfinished work, and source references.” |
| [Technical Documentation](skills/technical-documentation/SKILL.md) | Human readers need clearer, maintainable technical guides. | “Improve this onboarding guide so a new developer can complete their first task.” |
| [Context Loading](skills/context-loading/SKILL.md) | An agent needs the right information at the right time. | “Restructure these instructions so task-specific details load when needed.” |
| [Skill Refinement](skills/skill-refinement/SKILL.md) | A skill or agent-facing document needs a substantive review or rewrite. | “Improve this skill: remove redundant guidance and preserve its conditions and recovery steps.” |

Agent Instructions focuses on repository rules; Skill Refinement reviews the content of skills and other agent-facing documents. Context Loading decides what to retrieve; Context Management preserves useful state across long tasks. Technical Documentation is for human readers.

## Install

Choose **one installation method per agent** to avoid loading duplicate copies. Native plugins install all five skills together. `npx skills` also supports selecting individual skills.

### Claude Code — native marketplace

Run these commands inside Claude Code:

```text
/plugin marketplace add krema/agent-skills
/plugin install skills@krema
```

Or use the terminal:

```sh
claude plugin marketplace add krema/agent-skills
claude plugin install skills@krema
```

Restart the session if the new skills are not visible. For an explicit invocation, use a namespaced skill such as `/skills:agent-instructions`.

### Codex — native marketplace

```sh
codex plugin marketplace add krema/agent-skills
codex plugin add skills@krema
```

In a Codex desktop version with marketplace management, add `krema/agent-skills` as a GitHub marketplace, then install **Krema Skills** from **Krema**. If your CLI lacks `plugin add`, use the desktop plugin browser or update the CLI.

### GitHub Copilot CLI — native marketplace

```sh
copilot plugin marketplace add krema/agent-skills
copilot plugin install skills@krema
```

Use `copilot plugin list` to check installation. These commands target **Copilot CLI**; plugin controls in other Copilot clients depend on that client's version and policies.

### Any of the three — `npx skills`

Requires Node.js and npm. Browse before installing:

```sh
npx skills add krema/agent-skills --list
```

Install all skills into the current project for the three agents:

```sh
npx skills add krema/agent-skills --skill '*' \
  --agent claude-code codex github-copilot
```

Or install a single skill:

```sh
npx skills add krema/agent-skills --skill context-management --agent codex
```

Add `--global` if you want skills available across projects. The CLI handles agent-specific directories; no separate npm package is needed.

## Use

Ask the agent for the task you want completed, using the examples above as a starting point. Skill descriptions help the host select relevant instructions. Explicit skill selection and invocation syntax depend on the client.

The Markdown skills need no API keys or additional services. Skill Refinement includes optional structural checks and evaluation helpers requiring **Python 3.10+**, using only the standard library.

## Updates

Updates are reviewed through one rolling pull request. The maintainer's local automation checks completed research packages daily at **09:00 Europe/Berlin**, imports validated changes, and creates or updates the existing PR. It does not merge automatically. A run without changes creates no PR.

The existing research schedules continue to maintain their local packages. The publication job synchronizes their results; it does not repeat the research. This local schedule is not a GitHub Actions cron job and needs its Codex execution environment to be available. GitHub Actions validates pushes and pull requests.

Once a PR is merged, refresh your installation:

```sh
# Claude Code
claude plugin marketplace update krema
claude plugin update skills@krema

# Codex
codex plugin marketplace upgrade krema
codex plugin add skills@krema

# GitHub Copilot CLI
copilot plugin marketplace update krema
copilot plugin update skills@krema

# Installations managed by the skills CLI
npx skills check
npx skills update
```

`npx skills update` can update other skills managed by that CLI too. See [maintenance](docs/maintenance.md) for the publication workflow and versioning.

## Evidence and validation

The initial five skills were developed from research and practical task requirements. Their evidence files distinguish empirical findings, platform documentation, and engineering judgment. Research informs the guidance; it does not guarantee better results for every model or task.

- **Evidence:** [instructions](skills/agent-instructions/references/evidence.md), [context management](skills/context-management/references/evidence.md), [documentation](skills/technical-documentation/references/evidence.md), [context loading](skills/context-loading/references/evidence.md), [refinement](skills/skill-refinement/references/evidence.md).
- **Checks:** metadata, native manifests, file hashes, local links, synchronization guards, and the included Python tooling tests.
- **Compatibility:** actual installation checks and their limits are recorded in [validation](docs/validation.md).
- **Provenance:** [provenance.json](provenance.json) records original and published file hashes, with no private source paths.

Source-package evaluation reports remain with the skills as historical evidence. They are not fresh cross-client benchmarks. Public packaging changes identifiers and the entrypoint headings; it preserves the underlying instructions.

## Repository layout

```text
skills/                    One canonical copy of each skill and its resources
.claude-plugin/            Claude Code plugin and marketplace manifests
.codex-plugin/             Codex plugin manifest
.agents/plugins/           Codex marketplace manifest
.github/plugin/            GitHub Copilot plugin and marketplace manifests
scripts/                   Synchronization, manifest generation, and validation
tests/                     Tests for the publication tooling
docs/                      Maintenance and compatibility notes
```

The repository is `krema/agent-skills`, the marketplace is `krema`, and the bundled plugin is `skills`. This repository hosts a directly installable marketplace; it does not imply inclusion in any vendor's official directory.

## License

[MIT](LICENSE) for the original material in this repository. Referenced publications and third-party material retain their respective rights; links and citations do not relicense those sources.

## Platform references

- [Claude Code marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Codex plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [GitHub Copilot plugin installation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing)
- [The skills CLI](https://github.com/vercel-labs/skills)
