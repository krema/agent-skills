# Research method

## Start from decisions

State the research question in terms of agent behavior and intended outcomes. Identify what would change the implementation: supported environments, observed failures, competing approaches, prerequisites, and success measures. Use the user's constraints as requirements, not as empirical findings.

Build a short coverage map of these decisions. Search with topic synonyms, mechanism names, official documentation, relevant papers, original repositories/issues, and first-party engineering reports. Include counterqueries such as failures, limitations, negative results, replications, and alternatives. Source categories are tools for coverage, not a checklist requiring irrelevant sources in every domain.

## Inspect and classify sources

Prefer a source capable of supporting the particular claim:

| Source | Can support | Does not establish by itself |
|---|---|---|
| Controlled study | Observed effect in its tested conditions | Universal benefit or current-model transfer |
| Observational study | Association, deployment experience | Causality or the effect of one bundled change |
| Official specification/documentation | A defined interface, requirement, or described behavior | Independent evidence of task effectiveness |
| Repository, test, original issue | Implementation detail or a reported failure | Prevalence, reproduction, or a released fix |
| Engineering report | Concrete experience and design hypotheses | A controlled causal comparison |
| Proposal, opinion, existing skill | Vocabulary or a candidate approach | Proven performance or permission to copy/install |

For important studies inspect the task, sample, model/version, baseline, intervention, metric, variance, and limitations. Distinguish statistical uncertainty from evidence of no difference. Note confounded comparisons, synthetic data, model graders, restricted environments, missing code, and unimplemented components.

For product claims check relevant version and publication/update dates. For fixes distinguish issue report, merged commit, and released version. Record a commit or release when implementation details materially depend on it. Popularity and installation counts do not replace source appraisal.

Open the actual source; search snippets are discovery aids. If only an abstract or excerpt was inspected, say so and limit the claim accordingly. If inaccessible, seek an author manuscript or another direct source; otherwise retain the gap. Do not invent citations, dates, passages, measurements, or inspections. Do not interpret an access date as the publication date.

## Reconcile evidence

Write narrow claims with stable IDs. For each, preserve the conditions and opposing findings rather than averaging incompatible benchmarks. Ask whether apparent disagreement comes from different methods, tasks, models, measures, or populations. A later paper does not automatically supersede a better matched earlier one.

Separate source-level quality from confidence that the proposed rule transfers to this skill. Explain confidence in words using design quality, consistency, and applicability; avoid invented numerical scores. Label author inference explicitly.

Map findings to proposed rules:

`decision → source IDs → supported conditions → caveats/alternatives → proposed action → observable evaluation`

An engineering choice may be useful without direct experimental validation. Name it as such and test it locally. Do not call the whole skill scientifically validated merely because it cites papers.

## Stop, synthesize, and refresh

Keep a compact search log: date, query families, sources examined, excluded or inaccessible material with reasons, and unresolved questions. Do not fabricate a systematic-review protocol retrospectively.

Stop when decision-critical questions are sufficiently answered for this task, or remaining uncertainty is explicit and further searching is unlikely to change the design. Respect user budgets; if they prevent adequate coverage, mark the result provisional. Weak evidence can justify a conditional recommendation or omission rather than a stronger rule.

On refresh, recheck time-sensitive sources and claims with new opposing evidence. Update affected decisions and tests. Preserve a concise reason for changed behavior; do not just append sources while leaving obsolete instructions intact.
