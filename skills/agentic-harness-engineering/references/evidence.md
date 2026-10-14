# Evidence and operational implications

**Package and English edition: 2026-10-14. Research cutoff and source access: 2026-10-13.** Intended tasks: general design, audit, and improvement of harnesses for agentic software development. No project-specific repository layout, approval sequence, platform, or installation is assumed.

The targeted narrative review covers **95 sources**: 79 scientific works, including surveys/position papers, and 16 engineering/documentation sources. Selected full-text passages were inspected for 36 scientific works; abstracts and metadata for 43; relevant article/documentation passages for the other 16. This is not complete reading, replication, or an exhaustive systematic review. The [catalog](sources.md), [JSON](sources.json), and [search log](search-log.md) record versions, access, and inspection depth.

**EMP:** empirical finding in the evaluated setup. **FORM:** property within an explicit formal model. **API:** documented interface/specification contract. **ENG:** experience or an engineering inference. **PREF:** user objective/scope. Skill rules are primarily conditional engineering inferences supported by these categories. ArXiv metadata alone does not establish peer review; the review status and independent replication of every work were not verified.

## Decisions covered

| Question | Research families | Transfer and remaining boundary |
|---|---|---|
| Where should control reside? | Pipelines, adaptive decomposition, DAGs, symbolic planning. | Known prerequisites can reside in code; open-ended solution search needs discretion. |
| How do rules become effective? | Runtime enforcement, privileges, dataflow, classic security monitors. | Guarantees require suitable facts and mediated effect paths. |
| How can functional quality improve? | Test oracles, external critique, search, tool design, context. | No universal accuracy gain from a single method. |
| How do long runs remain traceable? | Event-based runtimes, checkpoints, retry, idempotency. | Persistence proves neither identical fresh execution nor global exactly-once effects. |
| How can a harness learn? | Workflow search, code optimization, diagnosis, experience banks. | Tuning effects and transfer require separate assessment. |

## E01 — A simple control core can retain adaptive work

[P02](https://arxiv.org/abs/2407.01489v2) (2407.01489v2, 2024-10-29), [P04](https://arxiv.org/abs/2410.20285v6) (2410.20285v6), and [P55](https://arxiv.org/abs/2311.05772v2) (2311.05772v2, 2024-04-08); selected architecture/method passages, EMP/ENG. Pipelines and search are different interventions with different budgets. ADaPT uses an LLM completion heuristic. **Implication:** type known transitions when the objective calls for it; retain autonomous inner work and valid alternatives. No universal state machine is mandatory.

## E02 — Guarantees end at the observation and execution model

[P46](https://www.cs.cornell.edu/fbs/publications/EnfSecPols.pdf)/[P47](https://web.mit.edu/Saltzer/www/publications/protection/Basic.html) (classic monitor literature), [P36](https://arxiv.org/abs/2503.18666v3) (2503.18666v3), [P37](https://arxiv.org/abs/2602.16708v3) (2602.16708v3), [P38](https://arxiv.org/abs/2512.23738v1) (2512.23738v1), and [P44](https://arxiv.org/abs/2504.11703v3) (2504.11703v3); selected mechanisms and limitations, FORM/EMP/ENG. Correct facts and effective instrumentation are prerequisites. Unobserved communication and model-based checks limit guarantees. **Implication:** inspect actual relevant effect paths and disclose unprotected areas.

## E03 — Correct structure is one verification layer

[P25](https://arxiv.org/abs/2501.10868v3) (2501.10868v3), [P20](https://arxiv.org/abs/2311.07911v1)/[P21](https://arxiv.org/abs/2507.02833v3), and [P40](https://arxiv.org/abs/2609.23742v1)/[P41](https://arxiv.org/abs/2607.18357v1): abstracts/metadata. [P68](https://arxiv.org/abs/2312.13382v2) (2312.13382v2, 2024-02-02): selected semantics and examples, EMP/ENG. Assert may halt after a repair budget; Suggest may continue; predicates may themselves use an LLM. **Implication:** separate syntactic, semantic, and mandatory conditions; a judge decision is not a formal truth guarantee.

## E04 — External oracles are useful but bounded by coverage

[P65](https://arxiv.org/abs/2411.14484v1) (2411.14484v1, 2024-11-20), sections 3–4, and [P72](https://arxiv.org/abs/2305.01210v3) (2305.01210v3, 2023-10-30), test methods/oracles selectively inspected, EMP/FORM/ENG. Scheduling critics assume complete task conditions; differential testing assumes a reference and input domain. [P08](https://arxiv.org/abs/2310.01798v2)/[P09](https://arxiv.org/abs/2305.11738v4) offer contrasting evidence about intrinsic versus tool-supported correction. **Implication:** tie acceptance to suitable verifiers, check translation and coverage rather than assuming them; search may still fail.

## E05 — Provenance is not functional quality

[P48](https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias) (in-toto, 2019) and [D16](https://slsa.dev/spec/v1.2/build-provenance) (SLSA v1.2): relevant provenance passages, API/ENG. Provenance relations help bind results to artifacts and issuers. They do not make an inadequate oracle complete. **Implication:** verify subject, relevant inputs, and issuer for the actual trust boundary; no universal signature requirement for every local workflow.

## E06 — Runtime reliability and task success are different metrics

[P51](https://arxiv.org/abs/2511.03690v2) (2511.03690v2, 2026-04-22), sections 4–5 and limitations selectively inspected, observational/EMP/ENG. The production comparison bundles changes and excludes provider failures. Table 3 reports a maximum crash-recovery time of 32.1 ms, despite text claiming less than 20 ms. **Implication:** consider state and events as architecture options; infer no causal accuracy gain or universal latency promise.

## E07 — Resumption can repeat operations

[D10](https://docs.langchain.com/oss/python/langgraph/persistence)–[D13](https://docs.temporal.io/activities): live documentation passages inspected on 2026-10-13, API/ENG. Persistence, interrupt/resume, and activity retries have different contracts. Re-execution may require idempotency. **Implication:** check the repeat point in the deployed version; reconcile uncertain remote effects first. Local locks and persisted history alone do not prove global exactly-once semantics.

## E08 — More information or roles do not universally help

[P01](https://arxiv.org/abs/2405.15793v3) and [P57](https://arxiv.org/abs/2409.07429v1): selected interface/memory methods. [P45](https://arxiv.org/abs/2402.01030v4), [P42](https://arxiv.org/abs/2503.13657v3), and [P69](https://arxiv.org/abs/2410.13825v2): abstracts/metadata. [P66](https://arxiv.org/abs/2602.11988v3) (2602.11988v3, 2026-09-29), sections 3–4 selectively inspected, EMP/ENG. Context files show no significant general success gain over None; developer files outperform generated files. **Implication:** choose information and methods for the bottleneck; retain a simple pipeline baseline, without banning or requiring additional instructions universally.

## E09 — Long error-free demonstrations are task-dependent

[P50](https://arxiv.org/abs/2511.09030v1) (2511.09030v1, 2025-11-12): decomposition/voting and limitations selectively inspected. [P73](https://arxiv.org/abs/2203.11171v4) (2203.11171v4) and [P56](https://arxiv.org/abs/2310.04406v3) (2310.04406v3): abstracts/metadata, EMP/ENG. MAKER uses a predetermined repetitive Hanoi decomposition and particular error conditions. **Implication:** investigate search and voting with justified budgets and suitable selection; a classical algorithm remains an alternative for exactly computable tasks.

## E10 — Harness optimization needs separate transfer assessment

[P35](https://arxiv.org/abs/2609.24130v1), [P52](https://arxiv.org/abs/2606.06324v2) (2606.06324v2), [P53](https://arxiv.org/abs/2607.14159v1) (2607.14159v1), [P70](https://arxiv.org/abs/2410.10762v4) (2410.10762v4), and [P74](https://arxiv.org/abs/2603.28052v1) (2603.28052v1): methods and relevant evaluation limits selectively inspected, EMP/ENG. HarnessFix separates data splits; MemoHarness has small primary holdouts and lacks uncertainty intervals. Meta-Harness uses the same search/evaluation tasks for Terminal-Bench. **Implication:** do not present improvement on known cases as general effectiveness; assess regression and transfer separately.

## E11 — Portable text policy requires executed mechanisms

[P75](https://arxiv.org/abs/2603.25723v2) (2603.25723v2, 2026-05-18): mechanism separation and Appendix G selectively inspected, EMP/ENG. Text can lose important meaning or be interpreted differently; exact mechanisms remain in code. [S02](https://picrew.github.io/LLM-Harness/main.pdf)–[S04](https://www.preprints.org/manuscript/202603.1756) provide descriptive taxonomies/reporting. **Implication:** use policy text as an inspectable artifact; describing rules does not observe their actual enforcement.

## Evidence to behavior

| Rule | Conditional action and rationale | Counterweight or fallback | Observable outcome |
|---|---|---|---|
| R01 | Preserve requested mode and existing scope; PREF/ENG. | General guidance defines no project approvals. | Artifacts and actual changes match the task. |
| R02 | Separate reliability objectives; E03/E06/E07, ENG. | Without new experiments, make no downstream effectiveness promise. | Report identifies the checked property and its boundary. |
| R03 | Express mandatory checkable conditions technically; E02/E03. | For semantic criteria, retain uncertainty and other oracles. | A violation or unknown prerequisite does not authorize a positive transition. |
| R04 | Mediate relevant effects on the actual path; E02. | Disclose a bounded threat model. | Test a bypass and a legitimate case at the actual boundary. |
| R05 | Bind authorizing evidence to subject/issuer; E05. | Choose a mechanism appropriate to the trust boundary. | Detect stale evidence or manipulated issuance. |
| R06 | Use external checks for repair when available; E04. | Do not treat weak oracles as complete. | An incorrect candidate fails; budget exhaustion remains unresolved. |
| R07 | Persist relevant state for long resumable work; E06/E07. | Short simple tasks need no unnecessary infrastructure. | Reset/crash preserves relevant facts and uncertain effects. |
| R08 | Select methods for the bottleneck and budget; E01/E08/E09/E10. | Simple baselines and deterministic solvers remain valid. | A comparison supports the additional method or limits the hypothesis. |
| R09 | Test relevant effects and qualify claims; E10, [P10](https://arxiv.org/abs/2406.12045v1)/[P43](https://arxiv.org/abs/2407.01502v1). | Without live/holdout trials, limit the assertion. | Distinguish performed checks from untested effectiveness. |

## Confidence, gaps, and refresh triggers

Conceptual confidence is high in separating format, functional checks, effect boundaries, and evidence trust. Transfer confidence is moderate for particular context, tool, and repair strategies. A universal benefit from additional roles or self-optimizing harnesses is not established. This package has not demonstrated downstream effectiveness in a comparative trial.

Relevant new models, runtime/API contracts, opposing studies, fact-extraction failures, or a changed threat model justify targeted updates to affected rules and evaluations. The skill creates no automatic schedule. Validation of this edition is recorded in [validation.md](../evals/validation.md).
