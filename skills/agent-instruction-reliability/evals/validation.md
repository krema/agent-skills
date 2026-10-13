# Validation record

**Package revision:** cross-framework extension, 2026-10-13. **Target environment:** generic coding agent skill; no installation requested. Source tree inspected at Superpowers `bb92a777` (v7.0.0 release commit).

## Structural checks

- Ruby's standard YAML parser loaded the `SKILL.md` frontmatter; `name` matches the folder and `description` is nonempty.
- A local link check passed for all six Markdown files after this extension; the Superpowers index has 64 unique issue rows.
- The bundled skill-creator `quick_validate.py` was attempted, but its Python environment lacked `yaml` (`ModuleNotFoundError`). The direct checks above cover the metadata and link conditions it would have helped inspect; they do not replace a behavioral trial.

## Author walkthrough

The author applied the `SKILL.md` decision path to cases A–J in `cases.md`:

| Case | Decision the text directs | Result |
| --- | --- | --- |
| A | Inspect delivery/invocation before TDD prose; test a plain trigger | Covered |
| B | Inspect reviewer receipt before DONE; keep receipt proportional | Covered |
| C | Compare global requirements with child brief and verify its file | Covered |
| D | Separate the approved artifact from the next phase; check project preference before default | Covered |
| E | Inspect whether the child got controller bootstrap; route by role | Covered |
| F | Identify host isolation boundary and verify branch/commit state | Covered |
| G | Check same-plan identity, handoff ownership, and first child action | Covered |
| H | Verify target skill entry before labeling a timeout | Covered |
| I | Compare co-applicable guidance and nested writes with approved scope | Covered |
| J | Resume the parent's pending step after a nested workflow | Covered |

This was a design walkthrough with the rubric visible, **not** a fresh-agent execution trial. The package is structurally validated and behaviorally untested. No claim is made that it improves compliance rates across models or hosts.

## Readiness decision

The evidence is sufficient to use this as a **supervised diagnostic checklist** on a real failure: its branches are tied to primary reports, several implemented fixes, and explicit unresolved cases. It is not yet validated as an automatic instruction-following guard. To make that stronger claim, run fresh agents with and without the skill on the same cases, including A (discovery), D (approval boundary), G (same-plan recursion), H (pre-entry failure), I (guidance conflict and nested writes), and their negative variants. Inspect tool traces and diffs against the rubrics; record host/model/version and any false positive. A comparison across at least two hosts would test whether the guidance transfers beyond one runtime.
