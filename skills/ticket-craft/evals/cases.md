# Evaluation cases and outcome rubrics

Revision: 2026-10-09 initial package. These requests and criteria are authored before the review outputs in validation.md. A future independent execution worker should receive the skill and request/input only; keep these rubrics out of its context.

## C1 — Shared hierarchy and agent pickup

Request: Write an epic, one implementable story, and a serializer subtask for account audit CSV export, for humans and an AI agent.

Raw input: Administrators need export of their own account's stored audit records. Use current authorization. Export all records, no date filters. Columns: event_id, occurred_at, actor_id, action; sort by occurred_at then event_id ascending; timestamps use current serialization. Empty account gives headers only; existing forbidden response for non-admins, no records disclosed. CSV special characters must preserve values. No repository, command, measured outcome target, or deployment request is supplied.

Rubric: purpose and hierarchy clear; acceptance covers stated behaviors; subtask does not claim authorization/integration completion; same criteria govern both readers; repository and commands not invented; unmeasured impact remains hypothesis; local implementation scope preserved. Accept alternative decomposition if contribution and integration are clear.

## C2 — Contradictory requirements and vague quality

Request: Turn this into execution-ready stories for an agent.

Raw input: Make search fast and support export. Export must include deleted records. Never export deleted records. No workload, latency target, decision owner, or repo is supplied.

Rubric: direct contradiction identified; no arbitrary interpretation or threshold; independent drafting continues; readiness remains qualified; unrelated capabilities need a reason to stay together; required decisions listed concretely. Correct behavior may refuse the requested readiness claim while delivering a useful draft.

## C3 — Discovery and scope boundary

Request: Write a subtask for an agent to investigate whether migrating our export engine is worthwhile.

Raw input: Current engine exists but implementation, alternatives, costs, and constraints are not supplied. User requests a description only.

Rubric: investigation deliverable and decision to inform are explicit; requests/inspection needs acknowledged; no approved migration, fabricated baseline, code edits, tracker writes, or deployment; completeness judged by useful evidence and recommendation with limits.

## C4 — Inaccessible context and unfair test

Request: Review an agent handoff for readiness.

Raw input: “Implement the export per last week's private meeting. AC: valid CSV matching current export fields. Test must assert the helper is named build_export_v2. Private meeting notes unavailable. Existing public interface does not require a helper name.”

Rubric: required meeting decisions unavailable; field contract not fabricated; helper-name test recognized as unsupported implementation restriction; check is revised or requirement clarified; ready status withheld for missing correctness-relevant information. Do not imply implementation restriction is always invalid if an authoritative interface later establishes it.

## Future execution trial

Use an isolated fixture with a real serializer and test command. Compare accepted behavior, scope deviation, clarification decisions, and verification evidence; do not grade exact headings. For improvement claims, compare matched baseline/revised descriptions on the same tasks with enough repeats to characterize variation. Human interpretation trials and coding-agent trials are distinct. Structural checks and author walkthroughs below do not establish either outcome.

## Revision and selection boundaries

- Review only: “Review this story; do not rewrite it.” Expected: actionable findings or no material findings, with review limits; no replacement description or tracker mutation.
- Existing contract: “Clarify wording without changing behavior”; supplied story ID S7 and criteria AC2/AC5 are referenced by subtasks. Expected: preserve IDs, references, and accepted behavior; flag a real contract conflict instead of renumbering or silently deciding it.
- Adjacent non-case: “Implement the already approved story.” Expected: implementation workflow, not unsolicited ticket authoring; clarify only missing decisions that affect execution.
