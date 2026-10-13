# Krema Skills

A growing collection of reusable skills for **Claude Code, Codex, and GitHub Copilot**.

Install the complete collection as **`skills@krema`**, or choose individual skills with `npx skills`.

[Browse the skills](#skills) · [Install](#install) · [Updates](#updates) · [Contributing](CONTRIBUTING.md)

## Skills

Choose a category for your task and use an example request to get started.

[Agent instructions and context](#agent-instructions-and-context) · [Research and evidence](#research-and-evidence) · [Documentation and work planning](#documentation-and-work-planning) · [Skill and workflow improvement](#skill-and-workflow-improvement)

### Agent instructions and context

Set up repository guidance, load relevant information, and preserve decisions across long tasks.

| Skill | Use it when… | Example request |
| --- | --- | --- |
| [Agent Instructions](skills/agent-instructions/SKILL.md) | Repository instructions are stale, contradictory, or hard to follow. | “Audit our AGENTS.md and CLAUDE.md. Fix conflicts while preserving project requirements.” |
| [Context Loading](skills/context-loading/SKILL.md) | An agent needs the right information at the right time. | “Restructure these instructions so task-specific details load when needed.” |
| [Context Management](skills/context-management/SKILL.md) | A long task loses constraints, repeats work, or needs a reliable handoff. | “Prepare a handoff that preserves decisions, unfinished work, and source references.” |

### Research and evidence

Reconcile source material or turn research into reusable guidance.

| Skill | Use it when… | Example request |
| --- | --- | --- |
| [Stateful Evidence Reasoning](skills/stateful-evidence-reasoning/SKILL.md) | An answer depends on multiple documents, conflicting versions, or calculations. | “Reconcile these reports, recompute using the final values, and cite the evidence.” |
| [Research to Skill](skills/research-to-skill/SKILL.md) | Research should become an actionable skill with traceable evidence. | “Research this topic, build a skill, and report what was actually validated.” |

### Documentation and work planning

Help people understand a system and give humans or agents clear work to carry out.

| Skill | Use it when… | Example request |
| --- | --- | --- |
| [Technical Documentation](skills/technical-documentation/SKILL.md) | Human readers need clearer, maintainable technical guides. | “Improve this onboarding guide so a new developer can complete their first task.” |
| [Ticket Craft](skills/ticket-craft/SKILL.md) | Epics, stories, or subtasks need clear scope and observable acceptance criteria. | “Turn these requirements into stories with a useful handoff for an agent.” |

### Skill and workflow improvement

Refine existing guidance and learn from corrections and verified outcomes.

| Skill | Use it when… | Example request |
| --- | --- | --- |
| [Skill Refinement](skills/skill-refinement/SKILL.md) | A skill or agent-facing document needs a substantive review or rewrite. | “Improve this skill: remove redundant guidance and preserve its conditions and recovery steps.” |
| [Learning Loop](skills/learning-loop/SKILL.md) | Corrections and verified outcomes should improve future workflows. | “Review these supplied logs and propose scoped improvements to our guidance.” |

## Install

Choose **one installation method per agent** to avoid loading duplicate copies. Native plugins install the complete collection; `npx skills` lets you choose individual skills. See [compatibility notes](docs/validation.md) for tested clients and limitations.

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

Learning Loop keeps observations in private project storage and proposes evidence-backed changes. It includes no background observer: continuous capture requires a separately authorized host integration or recurring invocation. Applying improvements respects the user’s existing authorization.

## Updates

Updates are reviewed in pull requests. After a merge to `main` passes validation, GitHub Actions publishes any new collection version. See [releases](https://github.com/krema/agent-skills/releases) for changes and [maintenance](docs/maintenance.md) for the publication workflow.

Refresh your installation after an update:

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

`npx skills update` can update other skills managed by that CLI too.

## Security

See the [security policy](SECURITY.md) for private vulnerability reporting and the limits of automated publication checks.

## License

[MIT](LICENSE) for the original material in this repository. Referenced publications and third-party material retain their respective rights; links and citations do not relicense those sources.
