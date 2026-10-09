# Validation — version 3.0.0

Checked 2026-10-07. Results separate software checks, actual editing, downstream execution, and unmeasured effectiveness.

## Executed software checks

- 28 analyzer and evaluation-preparation unit tests passed. The read-only analyzer is unchanged; measurements remain opt-in and content review is required regardless of size or findings.
- 20/20 static fixture cases passed. These check declared structural signals, not their semantic rubrics.
- Skill metadata validation passed; structural self-analysis has no findings. Its JSON is in [self-analysis.json](evals/self-analysis.json).
- Final ZIP integrity, extracted-file comparison, and extracted unit/fixture reruns passed.

## Actual optimizer editing trials

Three agents without authoring history each received three raw case requests and their files, plus this optimizer. Evaluator rubrics and worked outputs were withheld. The parent inspected the edited artifacts against the prewritten case rubrics: **9/9 passed**. This is execution of the optimizer's editing task, not merely a walkthrough of what it should do.

| Case | Observed outcome |
|---|---|
| compact_paraphrases | Edited a tiny file with no exact-duplicate signal; retained collision handling. |
| needed_specificity | Added verified command and scope, even though the resulting instruction grew. |
| unresolved_conflict | Fixed an independent command while preserving the unresolved format decision. |
| large_useful | Retained all 350 exact mappings and rejection behavior; refined discovery wording. |
| scope_sensitive_repetition | Kept the opposite duplicate policies while consolidating a shared rule. |
| audit_only | Source remained byte-identical; proposed rewrite stayed in the report. |
| conditional_rewrite | Replaced accidental read-all behavior with complete inline import/export branches; a small self-contained file needed no split. |
| research_transfer | Preserved the skill; did not turn hypothetical QA evidence into a universal repetition rule. |
| short_overloaded | Removed the three owner-disowned prerequisites; preserved leading-zero fidelity. |

One worker received parent confirmation that its already-written inline routing alternative was acceptable before its final completion notice. These are not fully blinded trials. Cases within each three-case session may influence later cases; the parent is both author and grader. Outputs, reports, grading reasons, and raw downstream requests/results are preserved in [execution-results.json](evals/execution-results.json); original editing inputs and rubrics are in [cases.json](evals/cases.json).

## Downstream execution of a revised skill

Two additional fresh agents used the edited inventory skill, each on a separate local task. The parent checked actual files:

- **Export passed:** CSV preserved all three records, order, Unicode, quoting, duplicate IDs, and leading zeros, with exactly the requested columns. Only the requested output was added.
- **Import rejection passed:** the same duplicate-containing records triggered an explicit rejection and no output file. Inputs and instructions were unchanged.

These are actual downstream actions for two selected branches. They do not establish general reliability, better performance than the original, or host discovery behavior. The rewrite inlined its small branches, so no successful deferred-reference retrieval is claimed.

## Content and evidence review

The core now makes consequential decisions followable, preserves applicability in the rule, handles unresolved conflicts, and chooses verification by uncertainty rather than diff size. It retains apply-versus-audit mode, factual authority, essential exceptions, and conditional references. Research and tooling details remain outside the common workflow.

The refresh reappraised decision-critical findings and added E30 with explicit limitations. Papers, product guidance, task authority, and engineering inference remain distinct. The helper does not edit files or judge semantic quality; the agent performs those tasks.

## Limits

The other eleven editing cases remain behaviorally unrun. There is no matched original/revised or no-optimizer comparison, repeated-run success estimate, cross-model study, independent human grading, or measured cost/latency gain. Full action transcripts and reference-read telemetry were not retained. Worker walkthroughs in the reports are labeled as such and are not additional execution trials.

The historical seven worked revisions remain author-produced illustrations from version 2. The archive was updated; no installed optimizer or recurring schedule was changed.
