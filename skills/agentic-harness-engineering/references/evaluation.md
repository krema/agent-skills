# Evaluate a harness or harness change

**Load for:** consequential mechanism changes, benchmark design, guarantee claims, or auditing existing evaluations. Supports R09. This guidance evaluates harness behavior; it does not install a skill or authorize external test effects.

## Define the question, comparison, and outcome first

Identify the actual claim: does a monitor prevent defined violations, does a resume protocol recover interrupted execution, does a verifier reject incorrect candidates, or does a strategy improve task success? Choose checks accordingly. Format validation does not establish behavior. An effectiveness experiment is not required for every purely editorial change.

Write representative tasks, relevant failure and boundary cases, and an outcome rubric before trials. Assess outcomes and actual actions rather than preferred wording. Accept valid alternative solutions. Keep expected answers out of a fresh test worker's context if one is used. An author walkthrough with a known answer is design review.

## Separate the metrics

| Question | Suitable observation | Common confusion |
|---|---|---|
| Was the task completed correctly? | Appropriate final states and functional checks. | The model claims completion, or the oracle is weak. |
| Was an incorrect candidate accepted? | Counterexamples violating a relevant condition. | Only success cases are tested. |
| Was a rule violation prevented? | Executed effects and rejected proposals, reported separately. | A detected violation is counted as prevented. |
| Was a legitimate task unnecessarily blocked? | Representative permitted counterexamples. | Permanent refusal appears safe. |
| Is execution reliable across repetitions? | Repeated trials under documented conditions. | One success is treated as stability. |
| Is replay correct? | Recorded responses/events reconstruct the same controller state. | A fresh live call is confused with replay. |
| Is it efficient? | Costs, latency, aborts, and verification work. | Search or evaluation overhead is omitted. |

`pass@k` describes at least one success in k attempts; `pass^k` describes success in all k repetitions. Document the estimator, repetition protocol, and task aggregation. Neither metric replaces functional coverage or investigation of rare harms.

## Choose proportional tests

For a deterministic predicate/controller fix, check affected normal, failure, and boundary cases. For uncertain routing, context, or repair rules, realistic execution with available tools and artifacts is more informative than static reading. Simulated interfaces establish only their simulated semantics.

For performance claims, compare baseline and revision with suitable model, task, and budget controls. Repeat enough to assess decision-relevant variance; justify the scope instead of imposing a universal trial count. Document observed uncertainty. Changing several components together does not support simple causal attribution to one feature.

For generalization, keep final evaluation cases separate from search and repeated selection. A repeatedly tuned test is no longer an untouched holdout. For online memory, ordering, state initialization, and permitted feedback are part of the experiment. Without independent cases, limit claims to known tasks and describe a later transfer test.

## Test boundaries and authorization

Isolate tests from live accounts, production resources, and installed configurations unless their use already belongs to the task. Authorized implementation does not grant blanket permission for new external effects. If a necessary live check is unavailable, deliver unaffected work and identify the particular untested decision.

Retain the revisions, inputs, results, action observations, and known environment conditions needed for interpretation. Check counterexamples relevant to the mechanism: stale evidence, uninstrumented effect paths, valid structure with incorrect content, a manipulated oracle, lost remote responses, concurrent workers, or context reset with an open blocker.

Report separately: structural validation, author review, actual execution, and demonstrated downstream effectiveness. Neither citations nor one successful test justify unrestricted claims of complete determinism, 100% accuracy, or scientific validation.
