# Adaptable templates

Use only fields that affect the reader's decisions. A blank field is not evidence of readiness. Unknown consequential details belong in open decisions, not completed-looking placeholders. These shapes are engineering choices; local terminology and tracker fields take precedence.

## Epic: human shared core

**Title:** Outcome or capability in concrete language.

**Problem and beneficiaries:** Who struggles, in what situation, with what consequence? Distinguish observed evidence from a hypothesis.

**Desired outcome:** What should change for users or the business? Include a metric, baseline, target, observation period, and measurement owner only when known. Otherwise state how the outcome hypothesis will be evaluated and which decisions remain open.

**Scope:** Included capabilities, affected users/systems, and consequential exclusions.

**Delivery acceptance:** Integrated capabilities and constraints needed to accept this increment. Keep post-release outcome evaluation separate.

**Decomposition:** Child stories/enablers, contribution to the outcome, sequence only where necessary, dependencies and unresolved risks. Early discovery can propose slices without claiming final completeness.

**Open decisions:** Question, why it changes scope or acceptance, decision source/owner if known.

**Agent addition when applicable:** Specify whether the assignment is research, decomposition, or implementation. For implementation, identify the executable child and integration checks; an epic is not automatically a single autonomous coding assignment. Attach the handoff fields below for the authorized task.

## Story: human shared core

**Title:** Concrete user-visible behavior.

**Need:** Actor, capability, benefit. Optional syntax: As a [specific actor], I want [capability], so that [benefit].

**Context and scope:** Trigger, current behavior, desired change, domain definitions and necessary boundaries. For bugs, include reproducible inputs and observed versus expected behavior when available.

**Acceptance:** Stable criterion IDs when useful. Each criterion describes a condition/event and observable expected result. Given/When/Then is an option, not a requirement. Cover consequential errors, boundaries, access rules, and quality constraints using agreed behavior.

**Dependencies and decisions:** What is needed, from where, and which questions remain unresolved.

**Agent addition:** Add the handoff fields below when an agent must execute or continue the item.

## Subtask: human shared core

**Title:** Action and resulting artifact/change.

**Parent contribution:** Parent item and criterion/outcome served.

**Work and boundary:** Bounded deliverable and interfaces to adjacent work. State necessary technical constraints; avoid pretending the task independently delivers the whole user outcome.

**Inputs/dependencies:** Required artifact, interface, decision, or prior task and availability.

**Completion:** Observable deliverable and relevant checks. An investigation finishes with findings, evidence, unresolved uncertainty, and a decision recommendation; it need not guarantee an implementation.

**Agent addition:** Add only handoff fields the shared core does not already cover.

## Agent handoff fields for any item

**Assignment:** Authorized action and deliverable; state whether drafting, investigation, local implementation, or another requested action.

**Starting state and sources:** Repository/artifact reference, version if relevant, important entry points and authoritative decisions. For each pointer, give its role; mark whether verified or supplied/unverified. Required information must be accessible to the intended agent.

**Constraints and discretion:** Required compatibility, interfaces, invariants, scope boundaries, and where the executor may choose the implementation. Separate mandatory constraints from suggested approaches.

**Verification:** Shared criterion IDs → check/inspection and expected observation. Add commands, working directory, setup, fixtures, and environment when known. Do not invent a runnable command. State unavailable checks and alternatives.

**Uncertainty/recovery:** Missing product decisions that require clarification, repository questions resolvable by inspection, and what to report if a dependency is unavailable.

**Completion report:** Deliverable location/change summary, acceptance results, verification evidence, and remaining limitations. Reuse shared acceptance criteria instead of copying divergent human and agent versions.
