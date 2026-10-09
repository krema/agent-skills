---
name: context-management
description: Diagnose and mitigate context-related failures during long research, coding, and tool-use tasks. Use when preparing a compaction or handoff, selecting evidence for a large task, or recovering from repeated work, stale state, or lost constraints. Preserve recoverable evidence and verify continuation; do not treat every agent error as context rot.
---

# Context Management

Improve the next task decision while retaining the information needed to finish. This is a conditional workflow informed by 2026 research, not a guarantee of better performance or a model-independent token limit. Read [evidence](references/evidence.md) when assessing support or transfer to another model. Read [evaluation](references/evaluation.md) when changing a context policy or claiming an improvement.

## 1. Diagnose the observable problem

Identify the current objective, binding constraints, next action, and its required evidence. For a short, progressing task, continue without adding a context-management routine.

When progress stalls, classify the evidence before intervening:

| Observation | First response |
|---|---|
| Required information was never obtained | Retrieve it; shortening history cannot supply it. |
| A summary omitted a known fact, constraint, or artifact | Recover the original and repair the working state. |
| Old and current values conflict | Reconstruct the current value from authoritative updates, including dependencies and scope. A historical mention is not an update. |
| Bulky or repetitive context obscures evidence already available | Try focused evidence selection or reversible offloading. |
| A command, calculation, or action is wrong despite sufficient evidence | Check the tool contract and task logic; repair the error directly. |
| A remembered repository path or command no longer works | Verify against the current checkout; distinguish stale documentation from long-input degradation. |

Repeated searches, user corrections, and unsupported early stopping are diagnostic cues, not proof of a mechanism. An uncertainty statement can be correct. Never force a confident answer to make a run appear recovered. [E01, E06, E08, E13]

## 2. Select evidence for the next decision

For a large corpus, start with relevant files or passages and retain their source locators. Expand when dependencies, contradictory evidence, or corpus-wide coverage require it. Preserve counterevidence that bears on the question even when it complicates the answer. Do not equate low lexical similarity with irrelevance.

Before dropping history, identify what the next action and remaining obligations depend on. Review proposed omissions for failed attempts, prohibitions, and exact state that a broad plan may overlook. This is a lightweight engineering check, not an implementation of FOCUS or a requirement to simulate future actions. [E15]

For batch tasks, retain the complete item set with stable identifiers and each item’s completion status; “process all remaining items” is not sufficient if the item list disappears. Verify coverage against the original set before declaring completion. [E15]

For aggregation, absence claims, or cross-document synthesis, cover the relevant corpus rather than selecting only promising matches. Partition work with a coverage record if necessary; do not discard dependencies between parts. When splitting records, finish boundary-spanning items and assign each item once; preserve update order for stateful tasks. Check intermediate tallies or state before merging. These checks do not require delegation or reproduce a trained decomposition policy. [E02, E19; engineering inference]

Use bounded tool output where feasible, while retaining access to the original. Keep action/result associations and exact values needed for execution. Choose among full retention, selection, offloading, or summarization based on the task; no fixed percentage, token count, or number of recent turns is prescribed. [E01, E04–E06, E11]

## 3. Preserve state before compression or handoff

When history actually needs to be condensed, construct a working record containing only applicable fields:

- Current objective and completion condition.
- User constraints and authorization boundaries, preserving their scope, exceptions, and explicit revocations separately from progress.
- Verified current state: exact identifiers, values, units, paths, dates and time zones when consequential; provenance and update order.
- Completed actions and observed results, including pending operations and whether external effects already occurred.
- Unresolved questions, conflicting evidence, rejected approaches and the reason they failed.
- Next action, prerequisites, and precise locations of supporting originals.

Keep task facts and concise decision rationale, not a transcript of private reasoning. Preserve temporal anchors when chronology matters. Do not promote guesses into facts or turn provisional conclusions into settled ones. [E03, E04, E07, E08, E10, E12; record layout is an engineering choice]

Before relying on an offloaded artifact, verify that its locator resolves and that the needed contents can be recovered. Use an authorized workspace or existing store. If retrieval is unavailable, retain essential source material inline and narrow the task if necessary. Raw storage is not a guarantee that the agent will find or use it. [E04, E05]

If the host exposes reversible output hiding, retain stable handles and restore the original before an exact-detail action. Use this selectively: model-dependent results do not justify hiding every old output. Without such a host capability, use ordinary source pointers and focused future reads. [E16]

When evaluating or configuring an exposed context-editing policy, account for cache invalidation, rewrite calls and restoration alongside task correctness. Compare less frequent edits if repeated rewrites increase total cost; do not adopt a fixed interval from a paper. If cache telemetry is unavailable, report that limit rather than infer savings from a shorter prompt. [E17, E18; engineering inference]

Compare the proposed record with the original constraints and consequential state before replacement when both are available. If the host compacts automatically, perform this check against surviving originals when resuming. Use only capabilities actually exposed by the host: writing a summary file does not clear earlier model context. Preserve ongoing authorization; compaction grants no new permission. [E12; environment constraint; engineering inference]

## 4. Verify continuation and recover

When choosing a compaction trigger, treat recent errors or prior writes as unvalidated cues. Compare both harm frequency and total recovery burden at matched opportunities; observe runtime limits. [E20; engineering inference]

At a compaction boundary, check that the next action’s prerequisites and unresolved obligations remain available. Track unnecessary reacquisition and repeated actions as well as completion; a successful result can still hide recovery overhead. [E04, E07]

Resume the next useful action and check its result against the task's completion condition. Look specifically for lost constraints, outdated values, duplicated external actions, missing evidence, and unnecessary retrieval of information already obtained.

If a detail is missing, retrieve the relevant original and patch that detail. If a checkpoint is stale, update it from verified state. If an action may already have happened, inspect the external state before retrying. Avoid cycling through broader summaries when targeted repair is possible. [E04, E07, E08; engineering inference]

If no evidence-preserving recovery is possible, state the missing dependency and continue independent work; ask for essential unavailable information. Do not label absence of access as absence of evidence. Finish when the original task is complete, not merely when the context is smaller.

For an authorized transcript-review task, keep exact action evidence and consider checks at meaningful intermediate states; do not rely solely on a final compressed narrative. This specialized precaution is supported by monitoring studies, not proof that periodic reminders improve all tasks. [E09]

## Deliverable

Return the requested task result. When intervention materially affects confidence or continuity, briefly identify the state preserved, the check performed, and any unresolved limitation. Provide a handoff record only when useful or requested. Do not add installation, new chats, delegation, or recurring monitoring as an automatic consequence of this skill.
