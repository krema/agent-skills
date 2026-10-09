---
name: ticket-craft
description: Write, refine, or review software epics, user stories, and subtasks for human teams and AI agent handoffs, with shared acceptance criteria and explicit unresolved decisions.
---
# Ticket Craft

Create descriptions that explain the purpose to people and give an executor enough information to act and verify the result. Use one canonical set of requirements; add agent execution context when needed. This shared-core design is an engineering synthesis, not a proven universal format.

## Establish the item and its audience

Choose drafting, revision, or review-only from the request. In review-only mode, return findings and suggested corrections without rewriting the descriptions or changing artifacts. For revisions, preserve existing item IDs, links, agreed requirements, and criterion IDs referenced by other items; identify any necessary contract change explicitly.

Use the request and supplied artifacts to identify the item type, intended audience, parent outcome, and stage: discovery, refinement, or execution. Respect local tracker terminology. An epic organizes a larger outcome; a story describes a useful behavior; a subtask contributes a bounded deliverable. Technical enablers and investigations need a concrete beneficiary or decision, not an invented user persona.

Read [templates](assets/templates.md) when drafting. Read [examples](references/examples.md) when hierarchy or audience differences need clarification. Read [evidence](references/evidence.md) when explaining the basis, evaluating a disputed rule, or refreshing the guidance.

## Build the shared description

- Lead with the desired change and why it matters. For a story, name the actor, capability, and benefit in natural language; use “As a …” only when it helps. Keep supporting detail outside the short story sentence.
- Distinguish supplied facts, verified facts, proposed decisions, and open questions. Do not invent metrics, deadlines, owners, interfaces, commands, source paths, or acceptance behavior. A plausible proposal remains a proposal until adopted.
- State the scope and relevant boundaries. Make ambiguous domain terms concrete. Describe constraints as requirements only when supplied or verified; label implementation suggestions separately.
- Make acceptance criteria observable: condition/input, action or event, expected result. Include failure and boundary behavior when they change the accepted solution. Quantified quality requirements need a supplied or agreed threshold, workload, environment, and measurement method; otherwise name the unresolved decision.
- Keep outcome measurement distinct from delivery acceptance. Passing software tests does not demonstrate an epic's business impact. Reference the team's Definition of Done when provided; do not replace it with item-specific criteria.
- Link dependencies and state what they must provide. For a hierarchy, map each child to its parent's outcome or criterion and check gaps, overlaps, and contradictions. Prefer end-to-end story slices when they preserve useful value; internal layer work can be a subtask or enabler. Do not split mechanically on the word “and.”

INVEST and SMART are practitioner review prompts, not evidence-backed pass/fail scoring systems. Preserve real dependencies and negotiable design; do not manufacture independence, estimates, or arbitrary size limits.

## Add the agent handoff when requested or needed

An agent executing asynchronously cannot rely on an unwritten conversation. Capture the consequential decisions and add only context that changes execution:

- Starting repository/artifact and version when known; relevant entry points, accessible source links, and why each matters. Verify references when access is available. Label unverified pointers; if a required source is inaccessible, include the necessary supplied excerpt or mark the dependency unresolved.
- Task-specific constraints, allowed discretion, and the authorized deliverable/action boundary. An agent description does not authorize publication, deployment, or unrelated work.
- Relevant verification commands and prerequisites when known. Keep acceptance criteria authoritative; tests should cover them without enforcing unrequested implementation choices. If tools cannot verify a criterion, name the alternate inspection or the remaining limitation.
- Unresolved decisions and recovery: inspect available authoritative artifacts for repository questions; ask the decision owner about missing product behavior that would change correctness. Continue independent drafting, but do not label that portion executable. Routine implementation choices may remain the executor's discretion.
- Expected completion evidence: artifact/change summary, criterion results, checks actually run, and remaining blockers. A failed environment check is not proof the implementation fails; report what remains unverified.

Keep essential outcome, constraints, and acceptance visible. Link substantial supporting detail with a clear reason to load it. Avoid copying a repository overview or generic workflow into every ticket. Evidence about repository context files and older retrieval models does not establish an optimal ticket length or guarantee current-agent performance.

## Review and deliver

Use [review checks](references/review.md) before finishing. For drafting or revision, return the description(s), any consequential questions, and a concise readiness judgment: discovery, needs refinement, or ready for the stated executor with disclosed limitations. These are descriptive judgments, not mandatory workflow gates. A human-readable discovery epic need not contain implementation instructions. An agent tasked only with analysis needs an analysis deliverable, not a fabricated coding plan.

For reviews, identify the source location, exact ambiguity or inconsistency, its execution consequence, and a suggested correction. If no material defect is found, report that with review limits rather than manufacturing findings. Preserve existing intent. Writing descriptions does not execute the work or update a live tracker unless requested.
