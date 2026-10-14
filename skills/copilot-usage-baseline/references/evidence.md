# Evidence: Copilot CLI historical usage baselines

Reviewed: 2026-10-14. Intended tasks/environment: answering requests to aggregate GitHub Copilot CLI token and AIU/AIC usage across accessible local or cloud session history, using the interfaces actually available in the host.

Review type and limits: targeted review of current GitHub documentation and the available local session-usage schema. No independent billing statement or account-level reconciliation was available. A cloud cross-session query failed during the originating investigation; local usage data was available. This is not an exhaustive source review.

Publication review: the three public GitHub pages in E01 and E02 were reopened on 2026-10-14, confirming the SDK conversion caveat and current billing unit. E03 remains an observation supplied with the source package; its private database, runtime version, and query failures were not independently reproduced. The public skill discovers its host's schema rather than assuming that observation applies everywhere.

## Research coverage

| Decision/question | Queries/source families examined | Finding or unresolved gap |
|---|---|---|
| What does the SDK usage metric contain, and can it be converted to AI Credits? | GitHub Copilot SDK usage-and-billing docs; inspected the accumulated totals section and its examples and note. | `totalNanoAiu` is described as session-wide AI-credit cost in nano-AI units. The SDK examples divide by `1e9`, but the same page warns that the exact conversion is defined by Copilot billing and says to verify it. Treat the result as a provisional SDK-style estimate, not reconciled billing. |
| What does GitHub billing define? | GitHub Copilot models-and-pricing docs and individual billing docs. | AI Credits are based on model/token costs; the docs define 1 AI Credit as USD $0.01. They do not establish an AIU-to-AI-Credit conversion factor. |
| What usage fields exist in this runtime? | Inspected the local `assistant_usage_events` table definition and representative rows. The available cross-session usage interface describes `session_usage` fields and its `cost` semantics. | Local records include per-event token counters and `total_nano_aiu`; some records include token-detail breakdowns. The cross-session `cost` field is a model billing-multiplier measure, not AI Credit spend. These are runtime-specific interfaces, not universal Copilot CLI guarantees. |
| What happens when remote history is unavailable? | Tried two bounded cloud `session_usage` queries; both returned an internal server error. Queried the local usage table instead. | Local history provided usable usage events. This demonstrates a fallback in this environment only; local records may not cover all cloud sessions. |

## E01 — SDK displays nano-AIU and warns that billing owns the conversion

- Source: GitHub, [Copilot SDK: Usage and billing metrics](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/usage-and-billing#accumulated-ai-credit-and-token-totals).
- Dates/version: accessed 2026-10-14; the retrieved page did not expose a publication or revision date.
- Inspection: directly inspected the accumulated metrics field table, explicit note, and TypeScript/Python examples.
- Type and design: official product documentation describing an SDK interface and example behavior.
- Finding: `totalNanoAiu` is described as session-wide AI-credit cost in nano-AI units. Examples divide the field by `1e9` and display “AI credits used.” The note explicitly says exact conversion to AI Credits is defined by GitHub Copilot billing, not the SDK, and says to confirm before relying on the division.
- Quality and limits: authoritative for the documented SDK field and caveat; does not independently establish the billing reconciliation or prove every CLI/runtime version uses the same behavior.
- Counterevidence/alternatives: E02 defines credit billing but gives no AIU conversion factor.
- Skill implication: show division by `1e9` only as a provisional SDK-style estimate; keep raw nano-AIU visible and avoid asserting billed credits.
- Aggregation implication: `session.usage.getMetrics` returns running session totals, so repeated snapshots must not be summed. The page also documents `assistant.usage.cost` as a premium-request multiplier and says those live events are not replayed on session resume. A history store must therefore be discovered and its coverage checked separately.

## E02 — Billing prices model tokens in AI Credits

- Source: GitHub, [Models and pricing for GitHub Copilot](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing#how-model-pricing-works) and [Usage-based billing for individuals](https://docs.github.com/en/copilot/concepts/billing-and-usage/individuals/billing#what-are-github-ai-credits).
- Dates/version: accessed 2026-10-14; retrieved pages did not expose a publication or revision date.
- Inspection: inspected the pricing explanation, per-token pricing context, and individual AI Credit definition.
- Type and design: official billing documentation.
- Finding: Copilot usage costs depend on model and token counts; GitHub converts the token cost into AI Credits. The docs define one AI Credit as USD $0.01.
- Quality and limits: authoritative for the stated current billing model and unit value; the published pages inspected do not state how `total_nano_aiu` converts to the billable balance.
- Counterevidence/alternatives: the SDK's illustrative division (E01) is explicitly caveated and does not supersede billing's own conversion.
- Skill implication: do not infer the official AIU-to-credit mapping from the USD value or current prices. Use billing records for confirmed spend; historical token repricing requires applicable historical rates.

## E03 — Runtime usage records and query failure

- Source: local Copilot session database schema and sample `assistant_usage_events` records; session-history query interface schema available in the current runtime.
- Dates/version: inspected 2026-10-14; current local CLI version reported as 1.0.97.
- Inspection: queried table metadata and sampled event fields; ran a bounded local aggregation after two cloud queries failed with internal server errors.
- Type and design: direct local implementation observation, not a public product guarantee.
- Finding: this local schema contains `session_id`, `model`, token counters, `total_nano_aiu`, and optional token-detail JSON. The cross-session `session_usage.cost` field is documented by the tool interface as a sum of model billing multipliers. In this investigation the cloud query failed while a local query succeeded.
- Quality and limits: directly observed, but specific to this machine/runtime, local retention, and the records available at the time. The local store does not prove complete cloud-history coverage.
- Counterevidence/alternatives: local files may contain raw event data, but the structured usage table is easier to aggregate; if absent or incomplete, inspect available event files and report the coverage limitation.
- Skill implication: prefer structured usage records; on repeated query failure, fall back to the available local source and report the source. Never treat `cost` as AI Credits.

## Evidence to behavior

| Condition and action | Source IDs or user requirement | Applicability and inference | Counterweight / fallback | Completion or failure check |
|---|---|---|---|---|
| User requests a cross-session baseline → inspect the available schema, distinguish events from snapshots, and aggregate by session and model, reporting source/date coverage. | E01, E03 | Structured counters support aggregation in the originating environment; the exact history interface varies by runtime. SDK metrics are accumulated session totals. | If unavailable, inspect event files or report the data gap; keep local/cloud populations separate unless reconciled. | Report distinct session and event counts, date bounds, fields summed, contributing counts for incomplete metrics, and query errors; repeated snapshots are not summed. |
| Result includes `total_nano_aiu` and user asks for AIC → show raw value; optionally divide by `1e9` with an explicit provisional label. | E01, E02 | The SDK demonstrates the arithmetic, but billing conversion is explicitly caveated. | Do not calculate a confirmed credit total without an authoritative billing record or conversion. | Output labels make raw, estimated, and confirmed billing quantities distinct. |
| Data includes token and cache/reasoning counters → state which counters are totals and which are breakdowns; avoid adding overlapping metrics. | E03 | Local row fields alone do not establish overlap semantics across every runtime/model. | Preserve separate columns when semantic overlap is unclear. | Totals are reproducible from stated fields and do not sum suspected subcategories twice. |
| Remote history query fails → retry once with a simpler bounded query, then try local history if available. | E03 | Local fallback worked in this observed environment; no universal availability is implied. | If fallback is absent or fails, report the task as blocked/incomplete rather than zero. | Successful fallback source is named, or failure is explicit. |

## Open questions and refresh triggers

- Recheck the SDK and billing pages before using this skill for an actual credit conversion; product billing rules and rates can change.
- No verified billable conversion from nano-AIU to AI Credits was found in the pages inspected.
- Cloud history coverage and retention were not verified because the cross-session query returned an internal server error.
- No matched independent behavioral trial of this skill has been run; validation is structural plus an author walkthrough. See [publication validation](../evals/validation.md).
