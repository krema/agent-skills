---
name: agent-orchestration
description: Design, review, or simplify agent orchestration by deciding which work belongs in a shared agent loop, a tool, a skill, or a separate subagent. Use for delegation-boundary decisions, costly or lossy handoffs, and migrations that fold specialists into the main loop.
---

# Agent Orchestration

Choose boundaries from context dependencies and task outcomes. A separate team, domain name, or reasoning phase is a candidate module, not sufficient reason for another agent.

## Inspect the actual boundary

Establish the requested outcome and scope: architecture advice, an audit, or an implemented change. Inspect available prompts, tools, traces, and evaluations. For each candidate boundary, identify:

- Information needed on both sides, including user constraints, mutable state, exact identifiers, and earlier decisions.
- Work that can proceed independently, and whether its bulky intermediate material can be discarded.
- Evidence of repeated handbacks, missing information, duplicated investigation, tool-selection errors, or context-related failures.
- Effective tool access and enforcement, rather than permissions asserted only in a prompt.

Missing traces mean an architectural hypothesis, not a measured bottleneck. Do not invent usage frequencies or performance gains.

## Choose the least costly adequate arrangement

| Observable condition | Candidate arrangement | What would change the choice |
|---|---|---|
| Phases repeatedly need the same evolving state or conversation | Keep reasoning in the main loop; load occasional procedures as skills | A separate context measurably helps despite the exchange cost |
| Existing specialists routinely operate together on the same evidence | Evaluate folding them into the main loop, or merging the coupled pair as an intermediate step | A necessary isolation boundary or a task regression |
| Work is a deterministic lookup, transformation, or API operation | Use a tool without an extra model loop | Adaptive investigation is actually required |
| Independent investigations produce much more intermediate material than the caller needs | Consider bounded workers with separate contexts and evidence-bearing results | Dependencies, duplication, or synthesis losses outweigh the benefit |
| A separate verifier can check an artifact against requirements without reconstructing its author's reasoning | Consider an independent check when its value justifies the cost | A superficial verdict adds no useful verification |
| Tool choice or instructions conflict in the shared loop | First clarify interfaces and defer irrelevant guidance; evaluate isolation if the conflict persists | Better discovery resolves the failure without another agent |
| A specialist genuinely needs to own an extended conversation with the user | Consider a full handoff with explicit state and ownership transfer | A bounded result is sufficient for the main agent to continue |

For new systems, one loop is a useful initial hypothesis when dependencies dominate. Parallel tool calls can handle independent operations without separate reasoning agents. For existing systems, retain the working baseline until a candidate is evaluated. Neither default establishes universal superiority.

## Make a retained worker's boundary usable

When delegation is within the user's scope and the host permits it, give the worker the task, necessary inputs, constraints, allowed effects, completion condition, and expected result. Choose effort and concurrency from the task and available budget; this skill supplies no fixed agent count.

Require a usable result: status, findings or artifact location, supporting source/data identifiers, unresolved issues, and what was actually checked. Preserve exact values needed downstream. Inspect consequential evidence or artifacts before relying on a worker's conclusion; a summary can omit the decisive detail. Treat timeout or partial work as partial. If repeated clarification exposes hidden coupling, bring the dependent reasoning together or revise the boundary.

Separate contexts alone do not prove security isolation. Preserve actual restrictions when merging or folding; verify the host's effective permissions and tool behavior. An architecture review does not authorize spawning workers, changing live systems, or expanding access.

## Change and verify

For migrations or comparisons of measured variants, read [migration-and-evaluation.md](references/migration-and-evaluation.md). It covers obligation preservation, matched evaluations, regression handling, and rollback.

Deliver the proposed or implemented boundaries, their task-specific rationale, what the evidence establishes, and remaining uncertainty. Distinguish a plausible design, an executed test, and a demonstrated improvement.

Read [evidence.md](references/evidence.md) when the recommendation needs source appraisal, conflicting findings, or a refresh. For evaluating this skill, use [requests.md](evals/requests.md); keep [rubric.md](evals/rubric.md) out of a test worker's context.
