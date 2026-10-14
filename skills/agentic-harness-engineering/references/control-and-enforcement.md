# Control, rules, and evidence

**Load for:** mandatory action rules, phase prerequisites, privileges, evidence, or controller audits. Supports R03–R05; [evidence.md](evidence.md) records sources and limitations.

## Turn an instruction into an executable condition

Choose the mechanism for the rule. A format condition needs a parser; a resource rule needs an effective action boundary; an ordering rule needs an observable event model; a functional condition needs a suitable oracle. Natural-language policy may describe this intent. The selected mechanism must actually evaluate exact conditions.

| Observable requirement | Possible implementation | Failure or uncertainty case |
|---|---|---|
| Input must satisfy a format. | Schema/grammar checks plus semantic validation of required values. | Valid structure with an incorrect reference remains invalid. |
| An action requires an earlier check. | State transition or temporal monitor over bound events. | A check for another candidate does not satisfy the prerequisite. |
| Access is limited to certain resources. | Permission checks in the executor or an unavoidable mediation layer. | The resolved access violates the boundary despite an apparently acceptable text path. |
| A property requires semantic assessment. | Calibrated review/judge decisions, complemented by suitable external checks. | Report uncertainty; do not invent a formal guarantee. |
| Known steps have dependencies. | Validated DAG or state machine. | A cycle, unknown reference, or missing state prevents the corresponding execution. |

A fixed phase model is useful when transitions and prerequisites are stable and known. For open-ended solution search, a small control core may enforce only invariant boundaries. An architecture does not enforce complete correctness merely through its name.

## Mediate actual execution

Start with the actions and resources the task identifies as relevant. Follow where the model proposes an action, where policy decides, and where the effect occurs. Check whether another executor, subprocess, MCP/API tool, or delegated worker can produce the same relevant effect without checking the rule.

If a mandatory boundary misses a path, fix the path or narrow the promised property. A post-action hook can support diagnosis; it cannot prevent an action that already occurred. A model labeling an action safe does not replace a missing resource check.

Trusted rules and permissions must derive authority from the intended issuer. Repository text, tool responses, and model proposals must not expand mandatory privileges themselves. Generated policy is a candidate to check against the task and trust boundaries. Bound unrestricted code execution where it could bypass protected effects; expressive code actions can remain useful within a suitable environment.

## Evidence for the same subject

When completion or an effect depends on evidence, identify:

- the candidate or resource state covered by the evidence;
- relevant inputs, check configuration, and environment where needed;
- the entity that actually issued the result;
- the result and limits of the check performed.

A suitable binding mechanism may be trusted process state, a database relation, a manifest, or an attestation. Cryptographic signatures are not mandatory for every local workflow. Where a candidate could change its own evidence, verifier, or approval identity, protect their integrity separately.

At the later decision point, verify that the binding still holds. With concurrent changes, a pre-action check may observe a different state from the action itself. Depending on the system, use a snapshot, atomic state check, versioning, or appropriately bounded effect adapter. A hash that omits relevant inputs does not automatically solve this problem.

## Make failure decisions observable

Distinguish confirmed satisfaction, established violation, pending verification, and an unknown fact. `ALLOW`, `DENY`, `WAIT`, and `UNKNOWN` are one possible interface, not a required API. An unknown mandatory prerequisite cannot become an affirmative decision from a model claim alone. Retain a justified recovery or clarification path rather than counting safe but unusable permanent refusal as success.

## Relevant counterexamples

Test cases that could falsify the actual boundary: correct ordering for the wrong subject, a forged issuer, changed check inputs, valid JSON with an unauthorized resource, an alternative effect path, and a legitimate exception. A monitor may reject safely while blocking too many permitted tasks. Measure both when assessing effectiveness.
