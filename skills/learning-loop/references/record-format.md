# Private learning records

Use `observations.jsonl` in the selected private storage directory. Each observation needs a stable ID, source event identity, timestamp when known, project/session aliases, host when known, coverage, kind, concise observation, outcome, affected target, scope, counterevidence, and status. Use null for unknown data rather than fabricating it. Project aliases and relative locators usually suffice; avoid usernames and absolute machine paths.

Synthetic example (one JSON object per line):

```json
{"id":"obs-001","type":"observation","source_event":"session-a:turn-4:user-1","timestamp":null,"project":"sample-project","session":"session-a","host":null,"source_locator":"provided-log:turn-4","coverage":"provided excerpt only","kind":"durable-preference","observation":"The user explicitly requested concise change summaries for this project.","outcome":"preference stated; future compliance untested","affected_target":"project instructions","scope":"sample-project","counterevidence":[],"status":"observed"}
```

Prefer source-native event IDs combined with origin/session identity. When unavailable, record an explicitly derived locator with enough stable provenance to recognize replay. Similar wording across unrelated tasks is not sufficient to deduplicate; identical copied source events across hosts are not independent support. If identity is uncertain, label it instead of counting it as corroboration.

Append evidence and lifecycle events referencing the observation or proposal ID. Derive current state from those events rather than overwriting older conclusions. Useful states are observed, proposed, applied, validated, rejected, superseded, and reverted; no mandatory transition to validated exists. A validation event includes the task, target revision, result artifact, and remaining limits. Redactions and retention deletions are exceptions to append-only storage: remove sensitive payloads and retain only a non-sensitive notice where appropriate.

Store a proposal at `proposals/<pattern-id>.md` containing:

- Source observation IDs and provenance, coverage, cause hypothesis, and counterevidence.
- Exact target, current revision or content hash, scope, and concrete patch or before/after text.
- Expected outcome and a realistic check capable of contradicting it.
- Authorization scope if applying, recoverable baseline, and rollback approach.
- Actual state, action/check evidence, and reason for rejection or supersession when applicable.

Do not put raw secrets in patches, source snippets, or hashes intended as identifiers. Hashes do not anonymize low-entropy personal data. Private records must remain outside published packages and PRs; only an explicitly authorized, generalized instruction change belongs there.

For concurrent writers use a single writer or a real locking/transaction mechanism. A partially written line must be quarantined or repaired before processing; do not silently discard it and advance the checkpoint. A checkpoint records the durable processed source position, not merely the last event seen. Retry safely using stable IDs after interruption.

On a write failure, keep the checkpoint at the last confirmed durable position. Check the concrete cause (destination, permission, disk, or lock) and retry only after a relevant correction within scope. If the cause cannot be resolved, or the same failure recurs without new information, stop persistence and report the blocker without copying sensitive pending content into the report. Leave the source available for a later deduplicated replay; do not label unwritten evidence recorded.
