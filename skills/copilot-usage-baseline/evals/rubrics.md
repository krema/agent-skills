# Evaluation rubrics

## Case 1: Baseline from all accessible sessions

- States the actual source, covered date range, earliest available record, session count, and any missing fields.
- Computes per-session totals before the mean/median; keeps input and output distinct.
- Does not add cache/reasoning breakdowns to totals unless the fixture establishes they are non-overlapping.
- Shows raw nano-AIU separately; calls divided values provisional rather than confirmed billing.
- Does not claim the local fixture covers every cloud session.

## Case 2: Remote query failure

- Does not interpret the query failure as zero usage.
- Makes at most one simpler retry, then falls back to the available local source.
- Clearly reports that local data is narrower than requested cloud history and labels the result incomplete.
- Does not merge local and cloud counts without a deduplication and coverage basis.

## Case 3: AIU conversion ambiguity

- States that the SDK demonstrates division by `1e9` as an estimate but explicitly defers the exact conversion to Copilot billing.
- Refuses to label the result an exact or confirmed billed AI Credit amount without authoritative billing data.
- Gives the raw nano-AIU value and, if useful, a separately labeled provisional calculation.

## Case 4: Cumulative snapshots and missing metrics

- Uses the provided export schema without assuming the originating history tool or table exists.
- Selects the latest snapshot for each session rather than summing its running totals; retains missing metrics instead of silently substituting older values.
- Keeps the missing output total unknown, labels partial aggregates, and states the contributing session count for each baseline.
- States the timezone and whether the date range filters usage timestamps or session start dates. Does not claim that a final lifetime snapshot establishes usage within a narrower period.
