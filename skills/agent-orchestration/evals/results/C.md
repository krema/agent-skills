# C — Candidate evaluation

Do not accept the candidate fold in its current form. Preserve or restore the recoverable baseline while repairing the candidate: the matched replay contains a new violation of the mandatory shipping-data requirement, despite lower latency.

Match on `(task, rep)`. The six shared runs produce:

| Matched outcome | Count |
|---|---:|
| Both pass | 4 |
| Baseline passes, candidate fails | 1 |
| Baseline fails, candidate passes | 1 |
| Both fail | 0 |

Both variants pass 5/6 matched runs (83.3%). Candidate-only `c4`, repetition 1, has no baseline counterpart and is excluded from both matched quality and latency calculations.

Including all six matched attempts, baseline latency totals 96 seconds, or 16 seconds per run; candidate latency totals 60 seconds, or 10 seconds per run. The mean change is −6 seconds, a 37.5% reduction: `(10 − 16) / 16`. This describes this controlled sandbox replay, not production improvement. Token and cost data are unavailable.

The two switched outcomes matter individually:

- In `c2`, repetition 2, the baseline passes and the candidate answers a delivery date from dispatch without `get_shipping`. That directly violates the requirement. The candidate loaded the returns procedure in both repetitions of `c2`; repetition 1 also calls `get_shipping` and passes. Loading the skill is therefore insufficient evidence of compliance, and the failure is intermittent across these repetitions.
- In `c3`, repetition 2, folding preserves the replacement size and stages the correct proposal, fixing the baseline's redundant request for a size already supplied. This is a meaningful local improvement, but it does not offset a mandatory-rule regression elsewhere.

Next, repair the candidate's delivery-source obligation at the point where estimates can be produced, including adjacent order and return paths; preserve the size-retention improvement. Add a required check tying each delivery estimate to the actual `get_shipping` result, with honest handling of unavailable data. Repeat `c2` under matched controls to probe the intermittent failure, then rerun the affected combined capabilities and existing suite, resetting state between runs. Inspect traces and final outcomes, not merely tool/skill selection, and collect missing usage data if cost is a decision criterion. Keep the baseline as the rollback point until the repaired candidate satisfies the invariant and has adequate coverage; the baseline's known size failure still needs attention. No app rerun or configuration change was performed; only the supplied metrics were calculated.
