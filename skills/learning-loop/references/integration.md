# Host-independent capture

The learning rules accept current conversation evidence, supplied logs, or an authorized event adapter. None requires a particular agent. Repeated observation needs an actual recurring invocation or host integration; this package includes no running service, hook configuration, or scheduler.

When continuous capture is requested, inspect the installed host/version and its current official hook or export documentation. Select events based on their actual payload and semantics. Do not translate event names mechanically between Claude Code, Codex, Copilot CLI, and editor integrations. Turn completion and session termination are different boundaries; not every event exposes assistant output or a full transcript.

An adapter must establish:

1. Authorized projects, sessions, readable source locations, private destination, and retention rules.
2. Stable source event identity, host/session context, and exact coverage. Missing transcripts are a coverage failure, not an empty successful session.
3. Minimal capture with redaction before persistence, exclusion of observer-generated events, and deduplication across retries or overlapping exports.
4. Bounded incremental reads, serialized durable writes, and checkpoints committed after recording. Report failed capture without claiming observation succeeded.
5. A bounded analysis cadence appropriate to the task, such as a requested session review or scheduled batch. Do not invoke an expensive recursive analysis on every tool event.

Keep passive capture separate from control decisions. A logger should not deliberately block task completion or request another agent turn merely to log an event. Honor host failure semantics and report degraded capture. Test missing fields, duplicates, partial records, concurrent writes, sensitive content, and observer recursion in an isolated destination before calling capture operational.

Where hooks are unavailable or payload access is insufficient, offer explicit reviews of provided logs or a separately authorized batch schedule. Report that fallback accurately. Setting up one client's adapter does not establish coverage in the others.

Official starting points, whose supported versions and payloads must be checked at setup time:

- [Claude Code hooks](https://code.claude.com/docs/en/hooks)
- [Codex documentation](https://developers.openai.com/codex/)
- [GitHub Copilot hooks reference](https://docs.github.com/en/copilot/reference/hooks-reference)

These links are interface discovery aids, not a claim that this package has implemented or tested adapters for all hosts.
