# Superpowers issue index

Snapshot: 2026-10-13. This is the in-scope issue inventory from the repository-wide screen described in [evidence.md](evidence.md). “Closed” in GitHub is not treated as proof of a fix. Related reports are grouped with the canonical failure where possible.

## Skill discovery, loading, and routing

| Issue | GitHub state | What the record supports |
| --- | --- | --- |
| [#48 — how to get Claude to _actually_ read the skills files instead of pretending it did?](https://github.com/obra/superpowers/issues/48) | closed | No confirmed fix; workaround suggested |
| [#189 — superpowers:brainstorm skill cannot be invoked - 'disable-model-invocation' error](https://github.com/obra/superpowers/issues/189) | closed | Historical command/skill collision; closed |
| [#215 — Brainstorm superpower not triggered.](https://github.com/obra/superpowers/issues/215) | closed | Restart after plugin installation |
| [#237 — Claude Code subagents appear to miss \`using-superpowers\` injected context, reducing skill-first/TDD behavior](https://github.com/obra/superpowers/issues/237) | closed | Platform limit: child lacks SessionStart context |
| [#345 — Skill superpowers:brainstorm cannot be used with Skill tool due to disable-model-invocation](https://github.com/obra/superpowers/issues/345) | closed | v5 skill/command restructure |
| [#433 — [opencode] Agent not following basic workflow](https://github.com/obra/superpowers/issues/433) | closed | Closed as platform/stale |
| [#439 — [opencode] Skills are not automatically triggered when prompt contains a big file.](https://github.com/obra/superpowers/issues/439) | closed | Closed as platform limit |
| [#699 — Does superpowers skill only work well with Claude Code + Claude Opus?](https://github.com/obra/superpowers/issues/699) | closed | Codex support improvements suggested; no specific fix |
| [#793 — Subagent prompts should include explicit instructions to read CLAUDE.md](https://github.com/obra/superpowers/issues/793) | closed | Historical prompt change 0cc80b1 |
| [#794 — [Bug] Subagent prompts missing CLAUDE.md context - project conventions ignored](https://github.com/obra/superpowers/issues/794) | closed | Duplicate of #793 |
| [#805 — Subagent Implementers Use Bash Tool Instead of Dedicated Tools](https://github.com/obra/superpowers/issues/805) | closed | Tool-choice cause disputed |
| [#833 — Deprecated command aliases block skill invocation instead of forwarding](https://github.com/obra/superpowers/issues/833) | closed | Legacy aliases removed |
| [#1002 — using-superpowers SKILL.md flow diagram causes intermittent "Unknown skill: brainstorm" error](https://github.com/obra/superpowers/issues/1002) | closed | Claimed wrong name not reproduced |
| [#1039 — using-superpowers skill intercepts native custom commands — no fallthrough on Skill tool miss](https://github.com/obra/superpowers/issues/1039) | closed | Native command conflict treated as host issue |
| [#1077 — subagent-driven-development dispatches requesting-code-review as Agent type, causing 'Agent type not found' error](https://github.com/obra/superpowers/issues/1077) | closed | v6 reviewer dispatch path changed |
| [#1463 — Codex app doesn't follow Superpowers workflow](https://github.com/obra/superpowers/issues/1463) | closed | Closed for missing trace |
| [#1667 — Skills not triggered when Claude Code Plan Mode is active](https://github.com/obra/superpowers/issues/1667) | closed | Plan-mode host limitation |
| [#1878 — Sonnet 5 really doesn't like the instructions](https://github.com/obra/superpowers/issues/1878) | closed | Duplicate of open #1480 |
| [#2051 — using-superpowers' "check any skill before every action" doesn't hold once a workflow step is underway](https://github.com/obra/superpowers/issues/2051) | closed | No verified fix; rationalization investigation suggested |
| [#2160 — OpenCode: Superpowers bootstrap is injected into task subagents, causing them to restart controller workflows](https://github.com/obra/superpowers/issues/2160) | open | Open; bootstrap reaches worker |
| [#2386 — test-driven-development is not invoked for a plain "add a function" request, even with the using-superpowers injection present](https://github.com/obra/superpowers/issues/2386) | open | Open; 0/3 TDD invocation in reported trial |

## Approval, precedence, and workflow transitions

| Issue | GitHub state | What the record supports |
| --- | --- | --- |
| [#73 — brainstorming needs to try harder not to ask things with obvious answers, at least on codex](https://github.com/obra/superpowers/issues/73) | closed | Closed after model/version changes; no fix demonstrated |
| [#107 — Claude Code does not follow the After the Design section](https://github.com/obra/superpowers/issues/107) | closed | Closed stale |
| [#378 — Is the basic workflow triggered automatically?](https://github.com/obra/superpowers/issues/378) | closed | Maintainer cites 4.1.2 change |
| [#565 — Brainstorming skill skips design doc review and overwrites it with the plan](https://github.com/obra/superpowers/issues/565) | closed | v5 separate files and restored review gate |
| [#573 — Git worktree is not created sometime after brainstorming](https://github.com/obra/superpowers/issues/573) | closed | Closed; fix path not established in issue |
| [#679 — Brainstorming skill: no artifacts generated, no tools used — skill checklist entirely skipped](https://github.com/obra/superpowers/issues/679) | closed | Closed not planned; no fix demonstrated |
| [#680 — Agent pastes code in chat instead of using Write/Edit tools during brainstorming](https://github.com/obra/superpowers/issues/680) | closed | Closed not planned; same session as #679 |
| [#849 — Brainstorming skill asks generic questions despite rich project context](https://github.com/obra/superpowers/issues/849) | closed | Closed after request for transcript |
| [#939 — Brainstorming skill ignores CLAUDE.md Output Paths, always writes to docs/superpowers/specs/](https://github.com/obra/superpowers/issues/939) | open | Open; output-path override failure |
| [#1030 — superpowers:brainstorming skill skips brainstorming and jumps to execution](https://github.com/obra/superpowers/issues/1030) | closed | Closed after request for reproducible transcript |
| [#1080 — Flow inconsistency: brainstorming → writing-plans gap - missing worktrees step](https://github.com/obra/superpowers/issues/1080) | closed | Worktree flow rewritten in v5.1; retest requested |
| [#1195 — Claude writes specs against the user's instructions](https://github.com/obra/superpowers/issues/1195) | closed | Closed; no transcript |
| [#1441 — Opus 4.7 with auto mode doesn't respect execution gates](https://github.com/obra/superpowers/issues/1441) | closed | Current-host reproduction did not skip gate |
| [#2076 — Brainstorming trigger lacks a mechanical-task exclusion](https://github.com/obra/superpowers/issues/2076) | closed | v6.3 short path for bounded work |
| [#2372 — Codex Desktop: brainstorming approval gates skipped after skill read (6.4.1)](https://github.com/obra/superpowers/issues/2372) | open | Open; Codex gate skip after skill read |
| [#2506 — [Codex] using-git-worktrees is read, but design approval is used to skip worktree consent (v7.0.0)](https://github.com/obra/superpowers/issues/2506) | open | Open; Codex worktree consent conflated with design approval |

## Execution, handoff, review, and recovery

| Issue | GitHub state | What the record supports |
| --- | --- | --- |
| [#147 — After auto-compact, cc in subagent-driven-development mode has a high probability of forgetting the review.](https://github.com/obra/superpowers/issues/147) | closed | Compaction concern; no specific confirmed fix |
| [#373 — TDD process is not followed and no tests were written - please help me understand why? ](https://github.com/obra/superpowers/issues/373) | closed | Closed stale; plan unavailable |
| [#463 — Controller skips spec/quality reviewer dispatch during subagent-driven-development](https://github.com/obra/superpowers/issues/463) | closed | v6 review-package/task-review redesign |
| [#485 — Model improvised run_in_background despite subagent-driven-development skill instructions](https://github.com/obra/superpowers/issues/485) | closed | Closed platform/version dependent |
| [#528 — Claude skips spec and code quality review](https://github.com/obra/superpowers/issues/528) | closed | Duplicate of #463 |
| [#566 — # Issue: \`writing-plans\` skill doesn't enforce TDD structure, allowing Test-After-Development](https://github.com/obra/superpowers/issues/566) | closed | Closed not planned; template enforcement unresolved |
| [#602 — The plan never aligns 100% with the design (suggested fix)](https://github.com/obra/superpowers/issues/602) | closed | Plan/spec alignment checks added |
| [#633 — Subagent-driven development: subagents should verify committed state, not just working tree](https://github.com/obra/superpowers/issues/633) | closed | Closed; maintainer could not reproduce |
| [#701 — receiving-code-review skill: add explicit guidance to fetch all three GitHub PR comment types](https://github.com/obra/superpowers/issues/701) | closed | Guidance rejected after 4/4 baseline evals |
| [#853 — Plan did not use TDD requirements](https://github.com/obra/superpowers/issues/853) | closed | Current live test did not reproduce TDD skip |
| [#994 — feat: TDD subagent reports should include RED evidence (failing test output)](https://github.com/obra/superpowers/issues/994) | closed | RED/GREEN report evidence added in PR #1065 |
| [#995 — subagent-driven-development parallelizes tightly-coupled frontend tasks without coordination](https://github.com/obra/superpowers/issues/995) | closed | Sequential dispatch since v6.2; review half #463 |
| [#1040 — Worktree skill doesn't enforce file operations stay within worktree](https://github.com/obra/superpowers/issues/1040) | closed | Closed; workspace confinement assigned to host |
| [#1120 — subagent driven development could skip reviews for "easy" tasks. ](https://github.com/obra/superpowers/issues/1120) | open | Open; evidence about over-broad review exemptions |
| [#1576 — writing-plans doesn't enforce TDD, causing entire Subagent-Driven Development process to skip TDD](https://github.com/obra/superpowers/issues/1576) | closed | Duplicate of #853 |
| [#1614 — RFC: require review admission receipts before extra SDD review passes](https://github.com/obra/superpowers/issues/1614) | closed | Extra review machinery rejected on cost/eval grounds |
| [#1701 — subagent-driven-development: spec-reviewer concurs on unchanged tree when implementer silently no-ops](https://github.com/obra/superpowers/issues/1701) | closed | v6 base-to-head diff exposes no-op |
| [#1936 — SDD progress ledger carries no plan identity — a second superpowers run in the same repo reads the previous run's \`progress.md\` and silently skips the new plan's tasks](https://github.com/obra/superpowers/issues/1936) | closed | Plan-scoped ledger via PR #1943 |
| [#1986 — SDD: enforce task-to-agent ownership to prevent cross-task subagent reuse](https://github.com/obra/superpowers/issues/1986) | closed | Closed; raw trace lacking |
| [#2050 — subagent-driven-development: dispatched subagent committed to main instead of the worktree (isolation not enforced)](https://github.com/obra/superpowers/issues/2050) | closed | Duplicate of #1040; wrong-branch commit |
| [#2112 — subagent-driven development can enter an unbounded review/test ratchet and never complete](https://github.com/obra/superpowers/issues/2112) | closed | v6.3 scoped re-review and round breaker |
| [#2202 — dispatching-parallel-agents: a dispatched agent can re-delegate and return a status promise, silently losing the lane](https://github.com/obra/superpowers/issues/2202) | open | Open; child returned promise instead of deliverable |
| [#2282 — subagent-driven-development: implementer dispatches are gated on nothing — briefs get referenced unwritten and todo state never updates](https://github.com/obra/superpowers/issues/2282) | open | Open; dispatch may reference unwritten brief |
| [#2293 — subagent-driven-development: the ledger records no in-flight task, so an outage mid-task re-dispatches work that is already committed](https://github.com/obra/superpowers/issues/2293) | open | Open; in-flight task missing from ledger |
| [#2435 — subagent-driven-development: in an unattended run, a step that needs a human at the screen should move to the next available tool, not be dropped](https://github.com/obra/superpowers/issues/2435) | open | Open; manual check dropped in unattended run |
| [#2493 — task-brief / dispatch: the plan's Global Constraints and Review Focus never reach the implementer, although the plan template says they apply to every task](https://github.com/obra/superpowers/issues/2493) | open | Open; global constraints missing from child brief |
| [#2499 — subagent-driven-development: scoped re-review resumed the existing reviewer in Codex](https://github.com/obra/superpowers/issues/2499) | open | Open; Codex reused reviewer on re-review |
