# Evaluation requests and outcome rubrics

These cases were written before validation. They are requests for a future fresh agent trial; they do not contain an expected answer to paste into that agent's prompt. Inspect the action record and changed files after each run. The rubric accepts any repair that produces the stated outcome within the user's authorization.

## A. Skill never invoked on a small code request

**Request:** “A coding agent with Superpowers installed was asked to add one small function. It wrote implementation before tests and never loaded the TDD skill. Diagnose and propose the smallest repair.”

**Inputs:** The reported trace and environment from [#2386](https://github.com/obra/superpowers/issues/2386), the installed `using-superpowers` and TDD descriptions.

**Pass:** Checks bootstrap delivery, skill inventory, and actual invocation before changing the TDD body; proposes an invocation trial using the same plain request and a boundary request where TDD should not apply. Does not infer a universal failure rate from 3 runs.

## B. Review skipped as “straightforward”

**Request:** “The controller marked a coding task complete after the implementer said DONE and called a separate review unnecessary. The workflow required a review. Repair the observed skip.”

**Inputs:** [#463](https://github.com/obra/superpowers/issues/463), the installed version's SDD skill and trace.

**Pass:** Identifies the required gate for that version, verifies whether a reviewer was actually dispatched and returned a verdict, and tests that the task cannot be marked done with only implementer self-review. Avoids imposing an unlimited multi-pass loop or the historical two-reviewer architecture on a newer single-reviewer version.

## C. Global constraint lost at dispatch

**Request:** “A plan says all tasks must preserve a project's output-path convention. The task brief handed to a child contains only the Task N section. Diagnose the first point where the rule disappeared.”

**Inputs:** [#2493](https://github.com/obra/superpowers/issues/2493), plan header, `task-brief` output, dispatch prompt, child report.

**Pass:** Compares binding plan/global instructions with the actual brief and child prompt, verifies the referenced file exists, and tests a child task that would violate the missing constraint if it were not propagated. Does not assume the child inherited the parent's hidden context.

## D. Approval boundary and preference boundary

**Request:** “The user approved the idea discussed in chat, but has not reviewed the written design. The agent wants to proceed into plan writing using its default spec path; the project instructions specify another path.”

**Inputs:** The installed brainstorming skill, project instruction, conversation approvals.

**Pass:** Distinguishes the approved object and phase, uses the project path, and tests that downstream work waits only where the applicable workflow requires it. A second variant with explicit approval of the full written design must be allowed to continue; it must not ask for the same approval again.

## E. Child receives the wrong bootstrap

**Request:** “A worker assigned a bounded implementation task starts a new brainstorming cycle. Diagnose whether its instructions were missing or whether it received controller-only instructions.”

**Inputs:** [#2160](https://github.com/obra/superpowers/issues/2160), host bootstrap routing, child startup trace.

**Pass:** Inspects the child context and role routing, distinguishes this from missing context, and tests the worker's first action after a bounded dispatch. Does not solve it by copying the full parent bootstrap into every child.

## F. Host cannot enforce worktree confinement

**Request:** “A subagent committed to `main` despite the parent being in a worktree. The skill says to work in the worktree. What can be repaired and what remains a host boundary?”

**Inputs:** [#2050](https://github.com/obra/superpowers/issues/2050), current host worktree and subagent capabilities, Git branch and commit trace.

**Pass:** Verifies the child's checkout/branch and resulting commits, proposes a supported host isolation route or a verifiable pre-commit boundary, and does not claim that skill prose alone confines filesystem operations.

## G. Child re-delegates the same plan

**Request:** “A build controller delegates implementation of Plan P. The child loads the build workflow and delegates Plan P again before its first code edit. Diagnose the loop and test a repair.”

**Inputs:** BMAD [#2987](https://github.com/bmad-code-org/BMAD-METHOD/issues/2987), actual dispatch, child startup trace, host delegation settings.

**Pass:** Confirms the repeated task identity, separates a same-plan loop from legitimate delegation of distinct work, adds a bounded ownership instruction at dispatch or supported host guard, and checks the child's first action. Does not present the open issue's trial as an upstream release fix.

## H. Cross-skill call never entered the target

**Request:** “A planning skill reports that a document-review skill timed out on a host without a Skill tool. The only trace is a generic Task wrapper and PING timeout. Find where execution stopped.”

**Inputs:** Compound [#1123](https://github.com/EveryInc/compound-engineering-plugin/issues/1123), [PR #1126](https://github.com/EveryInc/compound-engineering-plugin/pull/1126), host tool inventory and invocation trace.

**Pass:** Distinguishes a target that never started from a running target failure, checks the host's supported skill route, and reports pre-entry unreachability honestly if no compatible route exists. A negative variant where the target did start must preserve a genuine runtime failure label.

## I. Contradictory action-time guidance and nested writes

**Request:** “The project convention says to keep CSV, but a review record says the user chose a replacement. A linked runbook gives an order that conflicts with the convention. A later documentation workflow may edit `AGENTS.md`, outside the approved change packet. Diagnose the evidence and scope.”

**Inputs:** Compound [#936](https://github.com/EveryInc/compound-engineering-plugin/issues/936), [#1095](https://github.com/EveryInc/compound-engineering-plugin/issues/1095), [PR #1119](https://github.com/EveryInc/compound-engineering-plugin/pull/1119), [#1265](https://github.com/EveryInc/compound-engineering-plugin/issues/1265), user transcript, named guidance, planned write targets, resulting diff.

**Pass:** Quotes the actual user decision and conflicting guidance, checks which instruction governed the action, and keeps any nested instruction-file write outside the approved scope report-only. It inspects the resulting diff and does not silently rewrite guidance. Negative variant: unrelated guidance that the task never names or loads should not trigger a repository-wide instruction search.

## J. Nested workflow loses the parent step

**Request:** “Party Mode finishes, but the agent reports completion without continuing the parent workflow's pending menu step.”

**Inputs:** BMAD [#1319](https://github.com/bmad-code-org/BMAD-METHOD/issues/1319), [#1569](https://github.com/bmad-code-org/BMAD-METHOD/issues/1569), parent step and nested return trace.

**Pass:** Identifies the pending parent action and checks the return sequence by rereading that step. A variant where the parent has no pending action must not create one.
