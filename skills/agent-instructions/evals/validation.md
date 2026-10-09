# Version 2 validation — 2026-10-07

This version has two independent maintenance execution trials and one fresh downstream consumer trial, each run once in synthetic isolated repositories. It has no measured performance advantage over version 1 and no reliability estimate.

## Test design and independence

Requests, raw inputs, and outcome rubrics were written before dispatch; [cases.md](cases.md) contains the reproducible inputs. Workers started without conversation history and did not receive expected answers or the grading rubric. T1 and T2 received the operational skill and relevant references. T3 received only the repository produced by T1, its ordinary schema task, and an instruction to follow applicable AGENTS.md; no guide path or retrieval reminder was provided.

The parent reviewed actual files, before/after content and hashes, reports, and the checker event log. Parent grading was not blind. Worker model settings were inherited; the exact model identifier was not exposed in the tool record. Host was macOS with Python 3 and shell tools. These are lightweight fixtures, not representative coding benchmarks.

## Outcomes

| Trial | Actual execution | Parent verification | Result and limit |
|---|---|---|---|
| T1 Refactor | Worker edited AGENTS.md, migration guide, and release-conflict documentation | Exact migration commands, preconditions, recovery, wrapper rationale, and invoice invariant survived; only the three allowed documentation files changed before the consumer task | Met criteria. Retained essential migration constraints upfront because loading was unknown. Release approval count remained explicitly unresolved. |
| T2 Read-only audit | Worker read original/imported files and produced a report | Audit fixture hashes stayed unchanged; imported content matched original; report rejected a startup-saving claim | Met criteria under stipulated import semantics. No live Claude loader was exercised. |
| T3 Consume revised guidance | Fresh worker added optional string field note and ran precheck, postcheck, and wrapper | Event log records successful before check on unchanged schema, then successful after checks with note; original required invoice_id and sample 00042 preserved | Met task and command-order criteria once. Worker reported reading guide before editing; the parent corroborated resulting actions, not native file-read telemetry. |

The consumer logged a shell startup parse warning during initial discovery and switched to a non-login shell. Discovery and subsequent commands succeeded; this did not require an instruction change.

## Artifact checks

The parent compared all original fixture hashes. Audit files, tools, baseline schema, and owner notes were unchanged. The schema consumer's only substantive repository change beyond T1 documentation was the requested schema field, plus check-event output. Checker results were before=true on the original schema and after=true on the updated schema; both direct postcheck and timezone wrapper passed.

All five package files are present. Name/frontmatter, internal file links, portable paths, and operational placeholder checks passed using standard-library checks. The evidence and evaluation documents intentionally contain illustrative code and complete synthetic fixture text. No operational scripts or external runtime dependencies ship with the skill. ZIP extraction and file-hash equality were checked against the final source folder.

The standard skill validator was unavailable without PyYAML in the previously checked Python environments; structural fallback does not constitute a general YAML-parser validation.

## Draft limitation and repair

T1 and T2 started while the evidence ledger was being finalized and reported that its linked file was absent. SKILL.md and runtime-notes.md were already complete and did not change after those trials. The ledger and this validation record are now included, and final archive/link checks cover them. The workers did not validate the finished research ledger; its appraisal remains the author's work. No missing required resource remains in the final package.

## Untested decisions

No native loader diagnostics, unrelated-task retrieval execution, failed-check recovery execution, long-session adherence trial, matched v1/v2 comparison, latency/cost comparison, or live repository rollout was run. T2 covers an audit boundary; T1 covers unresolved policy, but neither establishes correctness for all conflicting-authority cases. T3 demonstrates one explicit reference path, not reliable implicit skill invocation. Static preservation of recovery text is not evidence that an agent will recover correctly after a failure.

A no-change result, missing destination, stale enforcement, ambiguous triggers, and later-session violations remain future execution cases. Research findings justify conditional decisions, not a claim that the complete skill is scientifically validated.
