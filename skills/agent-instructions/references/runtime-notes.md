# Runtime checks before moving instructions

Documentation checked 2026-10-07. Recheck the installed runtime and applicable settings; these are interface snapshots, not performance guarantees.

## Codex

[Official discovery guide](https://developers.openai.com/codex/guides/agents-md/): discovery follows the project-root-to-working-directory chain. Each directory contributes at most one file, prioritizing `AGENTS.override.md`, then `AGENTS.md`, then configured fallback names. Global guidance also participates. The documented default project-document cap is 32 KiB. A limit is not a recommended writing budget.

Before relying on a nested file, verify it is loaded in the actual launch/workflow. Do not assume placing a file below the working directory makes startup discovery load it. Observe instruction-source diagnostics where available; a model's summary is supplementary evidence.

## Claude Code

[Official memory guide](https://code.claude.com/docs/en/memory): `@path` imports expand eagerly. Splitting text into imported files does not defer it. Unscoped `.claude/rules/` files also load eagerly; `paths` scopes and nested CLAUDE.md files have conditional loading behavior. AGENTS.md support depends on version and project-instruction settings. Do not assume CLAUDE.md and AGENTS.md always both load.

Inspect `/context` or instruction-loading diagnostics and the installed configuration before claiming reduced context. Prefer a plain path with a clear reading condition when intentional task-time retrieval fits the workflow.

## Portable acceptance check

This is an engineering procedure, not a shared file-format guarantee:

1. Identify the runtime, launch directory, applicable parent files, and relevant overrides/imports.
2. Pick one general task and one task requiring moved guidance.
3. Confirm the general task retains its requirements without fetching unrelated detail.
4. Confirm the specialized task obtains the detail before its first affected action.
5. If loading cannot be observed, describe the layout as statically checked and leave runtime behavior unverified.

Preserve one canonical policy where practical, with compatible entry points. Avoid symlink or import changes until every supported consumer's behavior is understood. A maintenance improvement may still be worthwhile when eager-loaded size is unchanged; report it accurately.
