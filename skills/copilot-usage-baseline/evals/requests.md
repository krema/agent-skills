# Evaluation requests

Use these raw requests with synthetic usage fixtures in an isolated workspace. Keep expected outcomes in `rubrics.md`; do not give rubrics to a test worker.

## Case 1: Baseline from all accessible sessions

> Search all accessible Copilot CLI sessions for the last 30 days. Give me the median and mean input/output tokens per session, overall totals, a model breakdown, and any AI Credits used.

Input fixture: usage records across 8 sessions and 2 models. Include input/output counters, cache breakdown fields, two null credit values, and `total_nano_aiu` values. State that the fixture represents a local source with a known earliest record.

## Case 2: Remote query failure

> Find my historical Copilot usage since the beginning of the year and summarize tokens and credits.

Input fixture: first bounded history query returns an internal server error; a local usage table is available but covers fewer sessions than requested cloud history.

## Case 3: AIU conversion ambiguity

> Convert this session's `total_nano_aiu` into the exact number of GitHub AI Credits billed.

Input fixture: a raw `total_nano_aiu` value and the current SDK documentation showing `/ 1e9` as an example with an explicit warning that billing defines the exact conversion.

## Case 4: Cumulative snapshots and missing metrics

> Compare input/output tokens per session for these exported sessions. Include the mean and median and explain the history coverage.

Input fixture: the export schema identifies its rows as cumulative session snapshots, ordered by snapshot timestamp. One session has two snapshots with increasing totals; another has a null output-token total. Include a session spanning the requested date boundary. The host has no `session_usage` tool or `assistant_usage_events` table.
