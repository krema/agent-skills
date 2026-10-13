# Validation record — 12 October 2026

## Scope and revision

Package revision: initial `stateful-evidence-reasoning` skill drafted from LongHarness v1 and the sources in `evidence.md`. Target environment: a general Codex-style agent with search, source reading, notes, and optional computation tools. No helper scripts or live-account actions are included.

## Checks performed

- Structural author check: frontmatter name matches folder; description states the trigger; both relative links in `SKILL.md` resolve; evidence file has no template placeholders. Passed.
- Built-in `quick_validate.py`: could not start because the host's `python3` lacks PyYAML (`ModuleNotFoundError: No module named 'yaml'`). This was a tool-dependency issue, not a reported skill-format failure. A standard-library frontmatter and link check was used instead.
- Ruby's YAML parser loaded the frontmatter and confirmed the expected name and description. Passed.
- ZIP packaging check: one top-level skill folder, all four intended files present, links resolved after extraction, and every extracted file matched its source by SHA-256. Passed.
- Author walkthrough against `evals/cases.md`, with expected outcomes visible: Case 1 requires superseding 81.0 with 84.0 and recomputing 84.0 - 80.0 = 4.0; Case 2 directs the agent to retain the fiscal/calendar conflict; Case 3 activates the direct-answer path; Case 4 rejects an uninspected search hit as established evidence. The instructions cover these decisions. This is design review, not a behavioral execution trial.

## Unverified behavior

No fresh agent executed the evaluation requests. Citation fidelity, whether the record remains compact in a real long search, and whether the skill improves answer accuracy or efficiency are behaviorally untested. The paper's benchmark outcomes must not be reported as outcomes of this package.

## 13 October 2026 — Scoped coverage update

Revision: added a conditional coverage check for overall-evidence or corpus-wide conclusions, with E07 and synthetic Case 5. The existing source-revision, computation, and simple-question decisions are retained.

Author walkthrough, with expected outcomes visible: Case 5 activates the new condition, requires checking the other workload reports, and supports a conditional result. Case 1 remains a defined numerical question; Case 3 still permits a direct answer. This review does not establish actual agent execution or effectiveness. No independent behavior trial was run; completeness of source-group discovery and resistance to premature stopping remain untested.

Structural checks: YAML frontmatter parsed successfully; internal resources and portable-path checks passed. The rebuilt ZIP was extracted and its complete four-file inventory and SHA-256 hashes matched the package.
