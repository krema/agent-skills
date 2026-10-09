# Build, validate, package, install

## Synthesis

Use available skill-authoring guidance when relevant, but keep the generated package usable without local private paths or unavailable companion skills. Inspect existing files and callers before removing resources in an update.

The folder and frontmatter `name` must agree. Use a descriptive lowercase hyphenated name. The `description` identifies the capability and intended requests; do not make an ordinary question trigger research and skill creation unexpectedly.

Put common operational decisions in `SKILL.md`. Put evidence in `references/evidence.md`, and specialized mechanics in focused references linked with loading conditions. A separate rule map is useful when the mapping would obscure the research ledger; do not duplicate it. Include templates only when they reduce repeated work. Do not mandate a script, fixed file count, README, changelog, or state machine without a purpose.

Every material rule needs a rationale: evidence, interface requirement, user constraint, or labeled engineering choice. Check the inference as well as the citation: does the support justify this action, for these tasks, with this strength of obligation? Preserve relevant exceptions in the operational wording. More specific instructions are justified for fragile operations, while open-ended tasks retain useful discretion.

For consequential rules, make the decision followable: what observable condition triggers it, what evidence is available to choose an action, what should the agent do, and what outcome or failure should it recognize? If evidence is insufficient, state a useful fallback rather than inventing certainty. This is a synthesis check, not a mandatory schema for every sentence; add an example only when it resolves a real ambiguity.

Review the generated skill from its eventual user's task. Keep research, packaging, and installation procedures in the authoring workflow unless they are part of the generated skill's actual purpose. Do not substitute arbitrary word/line limits for checking omitted requirements, ambiguity, contradiction, repetition, and actual behavior.

## Validation

Check metadata, relative file links, dependencies, placeholders, and conditional reference loading. Use the target agent's existing skill validator if available; otherwise inspect these directly. Format checks are not a behavioral quality score.

Run any new helper on representative valid and invalid inputs. Verify meaningful effects, failure messages, and absence of unintended changes. Do not count a syntax check or `--help` as proof that the main operation works.

Before behavioral trials, write requests, raw inputs, and outcome-based grading criteria. Include a representative task, a failure or contradiction, and a scope/authorization boundary when relevant. Accept valid alternate solutions. Keep hidden rubrics and expected answers out of a fresh test worker's context. Use an independent agent when it adds meaningful confidence and delegation is available and authorized; otherwise accurately label the author review.

Choose validation proportional to the uncertainty. Routine edits need focused checks of changed behavior and preserved constraints; their size alone does not require comparative experiments. An uncertain routing or decision rule warrants a realistic execution trial when feasible. Performance or improvement claims require matched baseline/revised trials. For example, a source reporting possible retrieval overhead can justify checking whether deferred guidance is found; it does not justify requiring a full benchmark after every documentation edit.

Inspect produced artifacts and action records, not just the worker's claim of success. A walkthrough with the expected answer already visible is design review, not an execution trial. Where execution cannot be run, record why and which consequential decisions remain untested. Name the validation actually achieved; neither a working archive nor a plausible walkthrough establishes followability.

Isolate tests from live accounts and installed skill directories unless those actions are explicitly within scope. Record the skill revision, model/environment if known, inputs, outputs, checks, and failures. If claiming improvement, compare baseline and revised skill on matched tasks, with repeated trials appropriate to variation. A single success is not a reliability estimate. Distinguish quality of generated instructions from success of tasks executed using them.

## Package

Create a ZIP containing one top-level skill folder and all its referenced resources. Exclude caches, credentials, test scratch, and unrelated files. Inspect archive entries and extract to a temporary location; verify links and rerun required executable checks from that location. A package is not self-contained if it needs the author's workspace files. Report checks that were omitted and why.

## Install in the target agent when requested

Identify the target agent, client version, project or user scope, and supported installation method from its current documentation or available local installer guidance. Respect the user-selected destination. Do not assume Claude Code, Codex, and GitHub Copilot share directories or plugin commands. Prefer the requested supported installer; use a direct folder copy only where supported. Preserve normal discovery unless explicit-only invocation was requested.

1. Resolve the actual destination and inspect whether a skill of the same name already exists. If it is the requested update target, review the difference and retain a recoverable backup outside the discoverable skill tree. If unrelated, choose a distinct descriptive name or clarify when intent is ambiguous.
2. Stage the complete validated folder. For an existing installation, avoid deleting it before the replacement is ready. Do not follow unexpected destination symlinks or merge stale files into a new package blindly.
3. Copy/publish only the intended skill. Use the host's authorized filesystem tools and permission mechanism. The user's install request is authorization; an operating-system or sandbox restriction may still need the tool's approval flow. Do not change global permissions or unrelated configuration to bypass it.
4. Compare file inventory and hashes with the validated package, recheck metadata and links, and report the actual installed location. Keep the packaged and installed versions consistent.
5. Report the host's documented reload or restart requirement, if any. Do not claim that loading or successful use was observed merely because copying succeeded. If discovery fails, inspect the host's current guidance rather than repeatedly reinstalling.

Installing a skill does not authorize downstream external actions, automatic updates, or schedules. If installation is blocked, deliver the finished package and explain the concrete blocker; do not describe the task as fully installed.
