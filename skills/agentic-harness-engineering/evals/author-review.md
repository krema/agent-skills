# Author review of the decision rules

**2026-10-14, edition 1; translated to English without changing the case conclusions.** Requests and grading criteria were written before this review. The author knows the rules and criteria; this is **not an independent execution trial by a fresh agent**. The review assesses decision coverage and concrete audit evidence. The code fixture was actually executed with Python and has only in-memory effects.

## C01 — Bounded build-repair harness

An appropriate design records the authorized workspace, current candidate, and available build/test results. The loop generates changes, runs appropriate checks, and uses failures to guide repair. Changing the candidate invalidates affected results. The task determines the budget; exhaustion leaves the candidate unresolved. Evidence-bound success and unsuccessful execution require neither publication privileges nor extra roles. R01/R05/R06 support these decisions without prescribing a complete platform.

**Review outcome:** Instructions allow a proportionate simple solution. Actual followability by a new test worker remains untested.

## C02 — Audit with an executed fixture

Execution observed five cases. The normal positive report produces an in-memory effect; the negative report produces none. `other_subject` publishes C2 using a report for C1. `caller_report` publishes with a caller-originated report. `alternate_path` publishes C3 directly, without the dispatcher.

Causes are concrete: `dispatch()` uses only `passed`, without checking subject binding or verified issuance. `Executor.publish()` can be called directly. Comparing an issuer string alone would still not authenticate it. An improvement must mediate relevant effects, bind evidence to the current candidate, and verify issuer authority at the real trust boundary. Positive and negative controls remain relevant; every actual effect here is only a list entry.

**Review outcome:** The fixture supplies traceable evidence for R04/R05 decisions. Observing its execution does not prove that a fresh agent would apply the skill correctly.

## C03 — Guarantees from temperature, schema, and voting

A defensible response separates reproducible controller decisions from fresh model generation and functional correctness. Schema-covered structural conditions and shared reviewer errors remain separate limitations. Suitable external verifiers can support defined properties; correct translation into a formal model and sound checks are assumptions. The supplied mechanisms do not establish 100% accuracy for arbitrary development tasks. R02/R03/R06/R08 qualify these claims in operational guidance.

**Review outcome:** The case supports no unconditional guarantee; current empirical model performance and followability were not measured.

## C04 — Tuning on known tasks

The given results show 14 versus 17 successes among 20 previously used tasks. The best of 40 variants was selected on the same set. Describe this as an observed search/tuning effect without inventing independent transfer evidence or confidence intervals. Appropriate next steps include unused tasks, documented comparison conditions, and decision-relevant repetitions including search cost. R09 and the evaluation reference separate these levels.

**Review outcome:** The instructions limit generalization appropriately; no matched experiment was performed here.

## C05 — Recovery from static operations

A is confirmed according to the log and needs no repeated effect. B remains uncertain after connection loss; later authorized reconciliation must distinguish an existing effect from safely repeatable execution. Under the supplied, assumed-authoritative log semantics, C has not been sent; continuation must respect its reservation and authorization. D remains uncertain, and a machine-local lock does not protect against a second machine. For B/D, unknown idempotency semantics cannot become a guarantee. Advice needs no live call or new approval ceremony.

**Review outcome:** R01/R07 support a design within scope; real remote contracts and recovery execution were not tested.

## C06 — Losing failures after compaction

A bounded change retains open test failures with candidate bindings in authoritative state and projects them into the next step. A check resets context with an open failure and requires that unsupported completion remains detectable. Suitable successful verification may resolve the blocker; a relevant new change requires reassessing validity. This does not justify a large agent team or framework replacement. R07/R08 permit the small intervention and proportionate evaluation.

**Review outcome:** Scope and counterexamples are expressible. A running agent trial of actual context loss remains open.

## Overall assessment

All six cases were covered by author review; code-fixture execution confirms the described local observations. There are **no independent agent trials, matched baseline/revised comparisons, or downstream effectiveness results** for this edition. Proposed decisions are structurally and argumentatively reviewed; actual compliance by a fresh agent remains untested.
