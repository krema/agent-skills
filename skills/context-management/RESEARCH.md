# Context rot: 2026 research synthesis

Research cutoff: October 9, 2026. Scope: practical guidance for long research, coding and tool-use sessions. The [evidence ledger](references/evidence.md) contains twenty primary-source appraisals, exact links, inspected sections, opposing findings, search scope and exclusions. The [operational skill](SKILL.md) translates the findings into conditional actions.

The linked [Chroma report](https://www.trychroma.com/research/context-rot) was published July 14, 2025. It is excluded from the evidence supporting this package, as requested. Older models and datasets appear in eligible 2026 experiments; that is different from treating an older result as a new finding.

The defensible recommendation is to manage information according to the next decision and preserve what continuation will require. Neither indiscriminate accumulation nor indiscriminate shortening is supported as a universal policy. This synthesis is deliberately more conditional than a rule such as “reset at 50% context.” The studies vary in tasks, models, state persistence, measurement, and interventions, so their percentages cannot be pooled into one reliability curve.

| Practical question | Conclusion of this synthesis | Evidence entries |
|---|---|---|
| Is a long session itself evidence of failure? | No. Inspect missing information, stale state, retrieval quality and task errors before attributing a failure to context length. | E01, E06, E08, E13 |
| Should old content always be discarded? | No. The value of content depends on future dependencies and recoverability, not just age. | E04–E07, E11 |
| Is a good summary enough? | Check continuation, exact state, constraints and provenance. Fluency is not a validation metric. | E07, E08, E10, E12 |
| Is an archive enough? | Confirm that the agent can retrieve the needed evidence within the task's practical budget. | E04, E05, E14 |
| What should policy evaluation measure? | Completion, constraint adherence, state correctness, recovery burden, total resources and repeated-run behavior. | E04, E07, E09 |

These distinctions change implementation. A constraint omitted during compaction requires recovery from the original instruction. A stale repository path requires checking the checkout. Repeated searches may call for revising the working hypothesis. A difficult corpus-wide question may require broader coverage even when that increases context. Each problem calls for a different response; the generic label “context rot” does not choose one.

The package uses a compact working record with source pointers as an engineering design. No included study directly validates this exact Markdown workflow. Likewise, it does not implement a trained memory manager, modify model attention, control a hidden runtime compactor, or establish a safe context budget for the target model. Those capabilities must be assessed in their actual environment.

Several attractive claims were intentionally omitted: that shuffling prose improves real work; that any specific number of recent turns is optimal; that more reflection or extra agents always help; that confidence indicates recovery; and that preserved bytes guarantee preserved behavior. These omissions follow the evidence limits and the review scope, rather than a preference for a particular agent architecture.

The most consequential next validation is an actual continuation test on representative user tasks, especially a compaction boundary containing a changed requirement, an exact identifier, and an already-completed external action. The [evaluation protocol](references/evaluation.md) specifies normal, failure and boundary cases and distinguishes design review from an execution trial. See [validation](VALIDATION.md) for what was actually checked in this delivery.

Revision 1.1 strengthens the continuation checks derived from the already-included September studies and adds FOCUS and DTOC appraisals. The practical additions are batch membership/progress preservation, a check of proposed omissions, and selective reversible output hiding where the host supports it. These remain conditional engineering guidance.

Revision 1.2 adds E17–E19: cache-aware evaluation of context edits and boundary/order checks for partitioned work. These conditional engineering changes retain the existing host-capability and authorization boundaries. New October sources close a discovery gap in revision 1.1; no local performance improvement has been measured.

Revision 1.3 qualifies trigger selection and strengthens its evaluation. E01 also records the newer version discovered during source rotation. Local effectiveness remains unmeasured.
