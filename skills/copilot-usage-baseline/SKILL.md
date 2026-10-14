---
name: copilot-usage-baseline
description: 'Analyze historical GitHub Copilot CLI session usage. Use when asked to search prior sessions, calculate token-consumption baselines, compare usage by session or model, or estimate AIU/AIC credits.'
---

# Copilot Usage Baseline

Help users quantify historical Copilot CLI usage without overstating coverage or treating estimated AIU as billed AI Credits.

## When to Use This Skill

- The user asks to search prior Copilot CLI sessions for token or credit usage.
- The user asks for an average, median, trend, or comparison by session, model, or period.
- The user asks how `total_nano_aiu` maps to AIC / GitHub AI Credits.

## Workflow

1. Establish the requested period, timezone, session population, grouping, and metric. State whether the period filters usage timestamps or session start dates; sessions crossing a boundary can produce different totals. If unspecified, analyze all sessions available in the accessible history source and report its actual date and source coverage; do not imply it includes every cloud or local session.
2. Prefer structured usage records over scanning conversation text. Discover the available history interface or local store and inspect its schema before querying. Some runtimes expose `session_usage` or `assistant_usage_events`; these names are examples, not required interfaces. Follow the source's time-bound query and pagination requirements. For an all-available-history request, use its documented retention boundary or paginate to the earliest accessible record, and state that lower bound. If the boundary cannot be established, describe the queried interval as partial. When an SDK session is accessible, `session.usage.getMetrics` can provide accumulated totals; these do not establish cross-session or period-specific coverage.
3. If a cross-session query fails, retry once with a simpler bounded query. If it still fails, try an available local usage store or session event files. Report which source succeeded and which failed. Do not silently merge local and cloud results: IDs and coverage may differ.
4. Determine whether records represent individual usage events or cumulative snapshots. Sum distinct events, or use the latest snapshot for each session while retaining its missing fields; never sum repeated running totals or add snapshots to events covering the same calls. A final lifetime snapshot cannot establish usage within a narrower period: use timestamped events or documented snapshot deltas covering that period, otherwise label the result as lifetime session usage with period usage unavailable. Aggregate per session before computing a baseline. Report session count, period, and total and per-session statistics; include mean and median when available. Break down by model when useful. Keep null or missing metrics distinct from zero: label partial sums and give each metric's contributing session count and missing-data count alongside its mean or median.
5. State exactly which fields were summed. Keep input and output token counts distinct; show cache and reasoning counters separately unless the source establishes that they are additional, non-overlapping counts. Avoid double-counting breakdown fields already included in input/output totals.
6. For credits, report the raw `total_nano_aiu` (or equivalent) separately. Recheck the current SDK and billing documentation before conversion. You may show `total_nano_aiu / 1e9` as a **provisional SDK-style estimate** because the SDK illustrates that calculation, but state that its documentation says the exact conversion is defined by Copilot billing and must be verified. Do not label the result as confirmed billed AI Credits.
7. Cite the official usage and billing documentation and summarize coverage gaps, query errors, and any assumptions next to the results.

## Gotchas

- **A multiplier is not AI Credit spend.** The originating `session_usage.cost` interface describes a sum of model billing multipliers; the SDK's `assistant.usage.cost` is a per-call premium-request multiplier. Verify the current source's semantics before interpreting a field named `cost`.
- **Do not call `total_nano_aiu / 1e9` a verified billing conversion.** The SDK shows it as an example and explicitly warns that exact AI-credit conversion is defined by billing.
- **Current model prices do not establish historical billed spend.** Rates can change; do not reconstruct past credits from present-day prices unless the user accepts an estimate and the applicable historical rates are available.
- **“All sessions” means all sessions in the queried source and retention window.** Distinguish local from cloud history and disclose the earliest record observed.
- **A failed history query is not evidence of zero usage.** Retry narrowly, try an available local source, and report unresolved gaps.

## Report Format

Include:

- Source(s), date range, timezone and date-filter basis, earliest accessible record, and number of sessions/events.
- Token totals and per-session baseline, with the exact fields and grouping.
- Model breakdown when relevant.
- Raw nano-AIU, and a separately labeled provisional estimate only when useful.
- Whether figures are measured, estimated, partial, or unavailable, plus contributing counts and source/query limitations.

## References

- See [evidence and source limits](./references/evidence.md) for claim-level support and search coverage.
- Evaluation requests and separate grading criteria are in [evals/requests.md](./evals/requests.md) and [evals/rubrics.md](./evals/rubrics.md); publication checks and their limits are in [evals/validation.md](./evals/validation.md).
