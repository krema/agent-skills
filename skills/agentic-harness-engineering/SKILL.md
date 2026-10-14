---
name: agentic-harness-engineering
description: Design, audit, or improve harnesses for agentic software development using research on lifecycle control, rule enforcement, execution reliability, and functional correctness. Use for harness architecture, harness audits, or concrete reliability problems in agentic development workflows.
---

# Agentic Harness Engineering

Translate a harness objective into executable decisions and verifiable outcomes. A harness organizes model calls, tools, context, state, checks, and actions. This guidance applies to different custom harnesses, frameworks, and software agents; it assumes no particular platform, repository layout, or approval sequence.

## Establish the task and objective

**R01 — Work in the requested mode:** advice/design, audit, or implementation. Use the available tasks, artifacts, and existing authorization. During an audit, inspect actual call and data paths; identify what cannot be verified. Implement within the requested scope and preserve existing contracts. Do not derive additional human approval requirements, installation authority, or external actions from this skill.

**R02 — Separate the objectives:** deterministic controller decisions, replay of recorded events, reproducible fresh execution, rule compliance, and functional task success. Ask only for missing information that changes a decision. A new model call or a changed external environment is not replay. JSON Schema, temperature zero, or majority voting does not prove functional correctness.

Identify the relevant task, failure class, permitted effects, and observable success conditions. For known workflows, a simple pipeline is a suitable comparison baseline; open-ended tasks may retain flexible solution search. A small advisory task does not require rebuilding a complete controller.

## Place rules and verification

**R03 — Classify requirements before implementing them.** For machine-checkable mandatory conditions, define the predicate, trusted inputs, checkpoint, and failure decision. For preferences or model-assessed criteria, identify uncertainty. A deterministic branch on an LLM judgment does not guarantee the judgment is correct. If a mandatory prerequisite is unknown, do not treat it as satisfied.

**R04 — When rules must constrain relevant actions, enforce them on the actual execution path.** Within the agreed threat model, inspect alternative tools, shell/API access, and delegated execution. A log written after an action cannot prevent it. Remaining uninstrumented paths limit any guarantee. Read [control-and-enforcement.md](references/control-and-enforcement.md) for these decisions.

**R05 — When a check authorizes a later action, bind its evidence to the subject and issuer.** Verify the current candidate or resource state, relevant inputs, check specification, and evidence issuer. After relevant changes, recheck or justify which evidence remains valid. Hashes detect changes; they do not authenticate an issuer or prove test quality by themselves. Choose integrity protection appropriate to the actual trust boundary.

**R06 — When external verifiers are available, use their results for bounded repair.** Compilers, tests, solvers, and state comparisons check different properties. Do not accept generated tests or formally translated tasks as complete oracles without checking them. Define a stopping condition appropriate to the task; unresolved or unverified candidates remain identifiable. For oracles, search, and context, read [quality-and-optimization.md](references/quality-and-optimization.md).

## Preserve continuity and improve the harness

**R07 — For long-running or resumable execution, keep authoritative state outside model context.** Preserve the decisions, candidate references, open blockers, and uncertain effects needed by the task. Replay uses recorded model responses and tool results. If retries could repeat external effects, establish operation identity, remote reconciliation, and idempotency; do not claim exactly-once effects from a local lock alone. Read [execution-and-recovery.md](references/execution-and-recovery.md).

**R08 — Select additional methods for the observed bottleneck.** Decomposition, parallel DAG execution, search, voting, roles, memory, and harness learning are options. Justify their use and additional budget. Do not turn narrow benchmark results or one platform architecture into universal obligations. In new situations, retain valid alternatives that satisfy the defined conditions.

**R09 — Check consequential mechanism changes and qualify success claims.** Use relevant normal, failure, and boundary cases. For performance claims, compare a suitable baseline and revision under documented conditions; separate search/tuning cases from unused evaluation cases. Task success, false acceptance, executed rule violations, blocked legitimate cases, cost, and repeatability answer different questions. Read [evaluation.md](references/evaluation.md) when validating a change or assessing evaluations.

## Deliver the result

Provide architecture decisions, concrete audit findings, or verified changes appropriate to the requested mode. Connect material recommendations to a trigger, action, prerequisite, and observable success or failure. Report actual checks and remaining limits. Do not present a formally modeled property, an empirical finding, and an engineering hypothesis as the same guarantee.

For disputed guarantees, source questions, or transfer of a paper result, read [evidence.md](references/evidence.md); use [sources.md](references/sources.md) or [sources.json](references/sources.json) for targeted source lookup. The research cutoff is **2026-10-13**. During concrete implementation, check version-dependent API contracts against the version in use. The literature does not automatically validate the effectiveness of this skill or a harness designed with it.
