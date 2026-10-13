---
name: agent-instruction-reliability
description: Diagnose and repair cases where a coding agent skips, misreads, or cannot execute a skill or workflow instruction; use when reviewing an instruction-following failure or hardening an agent skill against a reproduced failure.
---

# Agent Instruction Reliability

Use this for a concrete report that an agent ignored a user, project, or skill instruction, or for an instruction change tied to such a report. The outcome is a narrow diagnosis, a repair at the right layer, and a check that observes the missing behavior. Read [the evidence ledger](references/evidence.md) when choosing a repair; read [the Superpowers issue index](references/issue-index.md) or [cross-framework cases](references/cross-framework.md) when comparing a report with prior cases.

## Locate the failure

1. **Record the contract.** Quote the exact instruction and its version. Identify its source and priority, the task and phase it applied to, and the observable action it required. Compare co-applicable user, project, skill, and runbook guidance for contradictory steps at the point of action. Preserve a user's new directive accurately when it changes an earlier decision. A user's or project's instruction may override a skill default. Approval of one artifact or phase does not by itself approve another.
2. **Inspect the trace.** Check what the agent actually saw and did: skill discovery and read calls, bootstrap or hook output, selected mode, dispatch prompt and child context, file changes, commands, approvals, and timestamps. If the trace is missing, ask for the smallest reproduction that separates the suspected causes; do not call a proposed root cause confirmed.
3. **Classify the break before changing prose:**

   | Observation | Likely layer to inspect | First check |
   | --- | --- | --- |
   | Skill unavailable or never loaded | Installation, discovery, hook, trigger wording, mode | Skill inventory and invocation trace |
   | Skill loaded but a step was skipped | Ambiguous gate, conflicting instructions, model behavior | Exact step, tool record, and claimed exemption |
   | Child acts without a requirement | Dispatch handoff and context boundary | Compare parent source with child brief |
   | Child repeats the controller workflow | Bootstrap injected into child | Child startup context and role routing |
   | Child re-delegates the same task | Worker ownership and host delegation settings | First child actions and repeated task identity |
   | Nested workflow ends without parent's next step | Return path and parent step | Last child action and parent continuation |
   | A cross-skill call is reported as a timeout | Skill invocation versus Task wrapper | Did the target skill actually start? |
   | Work is reported done but missing | Evidence or resume state | Artifact, commit, diff, test, reviewer receipt |
   | Requested tool/action cannot run | Harness or tool contract | Available tools and platform behavior |

## Repair the controlling layer

- **Discovery or invocation:** Fix registration, startup, command names, or trigger text and test an actual invocation. A stronger instruction inside an unloaded skill cannot help. For a skill-to-skill handoff, use the host's documented skill mechanism; if absent, use a compatible in-session route or report that the target was unreachable. Do not present a generic Task wrapper's failure as a failure inside a skill that never started.
- **Gate or priority:** Put the decision at the moment of action: check the applicable user/project preference, then use the default; name what counts as approval and where to stop. When a nested workflow may edit additional files, compare its planned write targets and resulting diff with the approved scope; use a report-only path for writes outside that scope. If the agent used “simple” or “faster” as an exemption from a required step, make the allowed exceptions explicit. Do not add a new permission requirement when the user already authorized that phase.
- **Handoff:** Give the worker the task's relevant requirements, binding global constraints, expected workspace, and report contract. Verify that every referenced brief exists before dispatch. Keep the child's role distinct from the controller's; use host routing where available instead of relying only on a conflicting text warning. If the child re-enters the same workflow for the same task, state that task's ownership boundary in the dispatch and test the first child action; use a host guard only when the host supports it. When a nested workflow returns, re-read the parent's pending step before reporting completion.
- **Completion and recovery:** When the failure was a skipped review, missing commit, or wrong resume, make the required evidence inspectable before marking completion. Compare the actual diff and files with the task, not only the worker's claim. Bind recovery state to the specific plan or task. Use the lightest receipt that makes the observed skip visible; repeated review loops or mandatory artifacts for every task need evidence that their cost is justified.
- **Platform boundary:** When a skill cannot enforce a tool behavior, workspace confinement, or mode transition, state the boundary and prefer a host capability or an explicit verification step. Do not describe a closed issue as a fix unless a merged/released change or a current reproduction check supports it.

## Check the repair

Write the failure case as a test request before editing: environment/version, exact prompt, relevant instructions, expected tool or artifact sequence, and a disallowed sequence. Include a negative or boundary case where the rule should *not* fire. After the change, inspect the trace or artifacts, not the agent's assertion that it complied. For a skill trigger, observe invocation before the first dependent action; for a gate, observe a stop before downstream work; for a handoff, inspect what the child received and produced. If only a walkthrough is possible, report the behavior as untested.

Report four things: observed failure, established cause or uncertainty, the smallest supported repair, and the validation result. Keep unresolved platform or model behavior visible; do not turn a single issue report into a universal rule.
