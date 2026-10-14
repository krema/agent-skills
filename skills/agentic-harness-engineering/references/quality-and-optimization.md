# Functional quality and method selection

**Load for:** accuracy problems, false completion, tool failures, context problems, or selecting decomposition, search, roles, and learning methods. Supports R06/R08. [evidence.md](evidence.md) assesses the sources; [evaluation.md](evaluation.md) describes measurement.

## Check the oracle before adding another loop

Connect the desired property to an actual check. Tests cover evaluated inputs; type and schema checks cover other conditions; formally sound verifiers apply to their correctly specified model. Passing a check establishes only the conditions it covers.

For generated tests, check that they fail on the faulty initial state and pass on a valid solution where these controls are available. Also check whether they overfit a particular implementation. For relevant input domains, targeted boundary cases, property/differential testing, or other suitable oracles can help. A reference solution can itself be wrong or incomplete; state that assumption.

For planners, verify that the formal representation, initial state, and resources capture the functional task. A correct solver output does not replace a correct translation. For an LLM judge, consider misclassification and shared model errors; multiple roles do not automatically provide verifier independence.

## Drive repair with concrete feedback

Generate candidates, actually check them, and repair identified failures. If only self-critique is available, label the loop heuristic. Distinguish mandatory assertions from recommendations that permit continuation. After the budget is exhausted, unproven mandatory conditions remain open; a soft preference may remain unresolved with a documented limitation, depending on the task.

If a candidate can change its verifier, separate evaluation from the candidate or protect the relevant check specification. More repair attempts against a weak oracle can exploit its gaps. Observe false acceptance alongside successful repair.

## Choose a method for the bottleneck

| Observation | Method to investigate | Condition or competing hypothesis |
|---|---|---|
| Invalid tool inputs | Typed inputs, schema/grammar checks, and better error feedback. | Semantic values still need separate checks. |
| Difficult navigation or editing | Task-appropriate search, editing, and observation interfaces. | Overly narrow tools can remove necessary expressiveness. |
| A difficult subtask in an otherwise solvable task | Adaptive decomposition with verifiable subgoals. | Decomposition may introduce wrong dependencies or completion heuristics. |
| Independent steps dominate latency | Validated DAG and parallel scheduling. | Dependent or conflicting steps must not run in parallel. |
| Several plausible candidates | Budgeted search, sampling, and suitable selection checks. | Correlated errors and poor value functions can undermine additional search. |
| Lost context | Targeted context projection and durable working state. | More text or aggressive compaction can introduce disadvantages. |
| Recurring subroutines | Bounded reuse of experience. | Stale or incorrect memories must remain revisable. |
| Missing specialist information or independent assessment | An additional role with clear inputs and responsibilities. | Keep a simple pipeline as a baseline; coordination costs resources. |
| Recurring harness failures with usable traces | Scoped harness repair or workflow optimization. | Without separate evaluations, optimization may only fit known tasks. |

The table describes possible interventions, not an automatic escalation sequence. Choose the smallest plausible change addressing the observed failure. For an exactly computable task, retain a suitable classical algorithm as an alternative or baseline.

## Limits of generalization

MAKER's long error-free execution relies on a narrow task with a predetermined decomposition; it does not establish arbitrary software correctness. Majority voting needs favorable error conditions and appropriate selection. AGENTS.md v3 challenges a blanket success benefit from extra context files, not every useful repository instruction.

For harness learning, preserve failure context, changes, and actual results so improvement remains traceable. Keep a separate introduction path for changes to mandatory boundary mechanisms. Online strategy adaptation is not authorization to rewrite its own permissions. If claiming generalization, assess improvements and protected counterexamples on separate tasks not previously used for optimization.
