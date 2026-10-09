# Worked example: one shared hierarchy

The following is a fictional, fully specified exercise. Its product decisions and paths are illustrative, not defaults for real systems.

## Epic E1 — Let account administrators export an audit history

Administrators currently assemble audit records manually. Enable self-service export so they can prepare an account review. Reduced preparation effort is an outcome hypothesis; no measured baseline or target is supplied.

Scope: export the account's stored audit records as CSV. Scheduled exports and cross-account reports are excluded. Delivery acceptance: authorized administrators can download the agreed records and format through the UI; unauthorized requests cannot expose records. Outcome evaluation: investigate preparation effort after adoption; target and observation period remain a product decision.

Children: S1 delivers authorized CSV export end to end. S2 adds the UI download and failure presentation using S1's endpoint. S1 can be exercised through the existing API client independently of S2. Integration acceptance checks the complete download flow. This sequencing is a real dependency, not a reason to pretend independence.

## Story S1 — Download an account's audit records as CSV

As an account administrator, I want to download my account's audit records so I can prepare a review without assembling records manually.

Exercise decisions: use existing account authorization. Export all currently stored records for the selected account; no date filtering in this increment. Columns in order: event_id, occurred_at, actor_id, action. Use the existing timestamp serialization and CSV library conventions. Order by occurred_at ascending, then event_id ascending. Do not expose records from other accounts.

- AC1: An authorized administrator requesting export receives a downloadable CSV containing exactly the selected account's stored records, ordered and serialized as specified.
- AC2: An account with no records returns a CSV containing the header only.
- AC3: A requester without account administrator permission receives the application's existing forbidden response and no audit data.
- AC4: Fields containing commas, quotes, or newlines round-trip through the CSV reader without altering field values.

Dependency: existing account authorization and audit storage. API route naming may follow repository conventions; this is implementation discretion, not a hidden acceptance criterion.

## Subtask T1 — Implement CSV serialization for S1

Contributes to AC1, AC2, AC4. Implement serialization of supplied audit records using the agreed column order, ordering, timestamp convention, and CSV escaping. Authorization and HTTP download wiring belong to adjacent work; T1 alone does not complete S1.

Completion: serializer output satisfies the populated, empty, tied-timestamp, and escaping cases. Integration of account isolation and forbidden responses remains part of S1 acceptance.

## Agent handoff for T1

Assignment: local implementation and relevant tests only. No deployment is requested.

Starting state: fictional exercise repository provided separately. Supplied entry points: audit serialization module, existing timestamp helper, and serializer tests. These are roles for discovery, not verified file paths. The agent should inspect the repository and confirm actual locations before editing. No runnable test command is supplied; discover it from the repository's authoritative tooling configuration and instructions.

Constraints: preserve S1's specified data contract. Reuse existing CSV and timestamp conventions. Implementation structure is discretionary. If repository timestamp behavior contradicts an agreed product requirement, report the conflict instead of silently changing acceptance.

Verification: populated and tied-time records → AC1; empty records → AC2; escaping round-trip → AC4. Report the command actually used and result. AC3 is outside this subtask and must be checked in the parent integration work.

Completion report: changed artifacts, observed criterion results, and any integration/environment limitations. This example is a discovery-capable handoff; it does not assert verified environment setup.

## Ambiguity example

Input: “Make search fast and support export. Export must include deleted records; never export deleted records.”

Revision behavior: separate search and export unless their value requires a combined slice. Search performance needs an agreed workload and target. Export has a direct product contradiction: ask which rule applies, rather than choosing one. Draft uncontested purpose and scope while marking execution readiness unresolved. Never invent a latency target or conceal the contradiction in an assumption.

## Investigation boundary

Input: “Find out whether migrating the export engine is worth it.”

Describe a research task: decision to inform, current engine evidence, candidates if supplied, relevant constraints, comparative checks possible in the available environment, and a recommendation artifact. Do not invent an approved migration or code-change acceptance criteria.
