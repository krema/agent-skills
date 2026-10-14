# State, context, replay, and recovery

**Load for:** long sessions, context loss, interruption/resumption, concurrent workers, or repeatable external effects. Supports R07; [evidence.md](evidence.md) records sources and contracts.

## Authoritative state and model context

Keep the facts needed for correct continuation in a suitable state source. A long development task may require the goal version, current candidate, satisfied conditions, open failures, decisions, and operation status. Give the model a projection tailored to its next step. A short read-only task may need only a small structured context; a database is not a universal prerequisite.

Compaction changes the visible representation, not automatically the underlying facts. After a reset, check that open blockers, rejected candidates, and uncertain effects remain discoverable. A summary must not promote an unsupported claim into an authoritative fact. Identify the provenance and validity scope of reused memories.

## Identify the required kind of repeatability

| Objective | Record or control | Limitation |
|---|---|---|
| Explain a decision | State input, controller/policy version, relevant facts, and decision. | Missing facts remain an observation problem. |
| Replay an internal execution | Original model responses, tool results, and ordered events. | Does not perform new remote effects. |
| Execute again | Actual model configuration, inputs, toolchain, resources, and relevant environment state. | Fresh model responses and the external environment may differ. |
| Resume after a crash | Durable progress and pending or uncertain operation status. | Persistence alone does not prevent duplicate effects. |

Record version-dependent details where they affect the measured outcome. A fully pinned model interface does not guarantee an identical fresh response. Claim a hermetic environment only for dependencies actually captured. Persisted logs or checkpoints do not inherently guarantee complete observability.

## Remote operations and retry

For externally visible operations, distinguish request reservation, execution started, confirmed outcome, and uncertain effect where these states matter. The representation is system-dependent.

If a response is lost after an operation starts, first assess the available remote state. Use a stable operation key or API-provided idempotency where its contract covers the required semantics. Repeating a call is safe only when it cannot cause an unauthorized additional effect or the remote contract prevents that effect. If safe reconciliation is unavailable, retain the unknown state and pursue clarification appropriate to the task.

A local file lock protects only its actual coordination domain. Multiple processes or machines need suitable reservation and state consistency. Reserving a request and performing a remote operation do not automatically form an atomic transaction.

For frameworks, inspect the version actually deployed: an interrupt may restart a node, and an activity may be retried. Do not place non-idempotent effects before a repeatable checkpoint without checking the implications. Test the relevant crash position rather than only a successful normal execution.

## Conflicts and stopping

For concurrent workers, establish which progress is authoritative and how stale state is detected. For bounded execution loops, define budget and completion criteria outside a model claim alone. Do not adopt universal turn or token limits from a paper example.

Counterexamples include a reset with an open blocker, a crash before sending, remote success before response loss, competing reservations, and a late result for an old candidate. Test cases relevant to the actual task. Correct recovery shows handling of these controlled interruptions; it is not a general availability guarantee.
