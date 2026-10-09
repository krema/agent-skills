# Evidence for descriptions used by humans and AI agents

Reviewed/accessed: 2026-10-09. Intended use: software backlog authoring and review in English, including asynchronous coding-agent handoff. Targeted narrative review, not a systematic review or meta-analysis. Sources inform design; this package is not scientifically validated.

## Research scope and findings

The decision questions were: what information makes a story understandable and verifiable; how epics and subtasks differ; what must survive asynchronous handoff; whether more structure/context helps agents; and what makes acceptance unfair or incomplete.

Searches on 2026-10-09 used these query families: Lucassen / Quality User Story / empirical ambiguity; user stories / acceptance criteria / requirements ambiguity; SWE-bench / underspecified descriptions / tests; Lost in the Middle / context utilization; AGENTS.md / context files / coding agents; Three Cs; INVEST / SMART tasks; Patton / story mapping / epic outcomes. Counterevidence came from context-file ablations, reported efficiency benefits, and limitations of syntax-based story checks. Searches covered primary research, originating practitioner guidance, and first-party evaluation experience.

Direct evidence is strongest for defects in story text, model context sensitivity under tested conditions, and benchmark statement/test mismatch. Exact epic and subtask schemas have substantially weaker direct empirical support in this review. Repository instruction-file studies are adjacent evidence, not direct trials of ticket templates. No controlled comparison of this package's shared-core format versus separate human/agent descriptions was found in this search.

## E01 — Story text quality is inspectable, but text linting is incomplete

Source: Lucassen, Dalpiaz, van der Werf, Brinkkemper, [Improving agile requirements: the Quality User Story framework and tool](https://link.springer.com/article/10.1007/s00766-016-0250-x), Requirements Engineering 21, 383–403, published 2016-04-01; DOI 10.1007/s00766-016-0250-x. Inspected full relevant text: §§3–5, proposed criteria, evaluation procedure, and validity threats.

Type: framework proposal plus empirical tool evaluation on 1,023 stories from 18 companies. The evaluation concerns defect detection against framework judgments, not a randomized test of delivery outcomes. The tool missed defects and produced false positives; domain interpretation matters. Sampling concentrated on independent software vendors, largely Dutch; confidential datasets limit reproduction.

Implication: examine meaning, scope, consistency, duplication, and explicit dependencies, as well as wording. Keep supporting detail separate from the compact story sentence. Do not treat syntax compliance as product correctness, split automatically on conjunctions, or infer that a fixed template improves delivery. Confidence is reasonable for these review concerns, limited for transfer to autonomous agents. Practitioner slicing guidance (E03/E04) counterbalances mechanical atomicity.

## E02 — A human story includes shared conversation and confirmation

Source: Agile Alliance, [Three Cs](https://agilealliance.org/glossary/three-cs/), inspected glossary definition and origins; page publication/update date not established, origins attribute the model to Ron Jeffries in 2001.

Type: established practitioner convention, not controlled effectiveness evidence. A story's card is supported by conversation and confirmation. Implication: a brief human story can be appropriate during discovery; record consequential conversation decisions for asynchronous handoff. This transfer to agents is an engineering inference. Do not claim more prose replaces collaboration or that every early epic must be implementation-ready.

## E03 — INVEST and SMART distinguish value slices from implementation work

Source: Bill Wake, [INVEST in Good Stories, and SMART Tasks](https://xp123.com/invest-in-good-stories-and-smart-tasks/), 2003-08-17, postscript 2011-02-16. Inspected full article, including independence caveat, slicing, testability, and task sections.

Type: originating practitioner advice, not comparative empirical proof. It distinguishes customer-value stories from relevant, bounded development tasks and permits real dependencies. Implication: use these ideas as review prompts, retain parent contribution and observable completion, and allow technical subtasks. Do not enforce invented estimates, universal time limits, or independence. Concrete quality checks are useful; their exact template and effectiveness remain engineering choices.

## E04 — Epics need decomposition that preserves the larger user activity

Source: Jeff Patton, [The New User Story Backlog Is a Map](https://www.jpattonassociates.com/wp-content/uploads/2015/01/patton_story_mapping_bettersw_1109.pdf), Better Software, November/December 2009. Inspected the six-page article, especially activities, tasks, granularity, and release slicing.

Type: first-person practitioner method and experience, not a controlled evaluation. Larger activities organize finer user tasks; the epic/story distinction can remain fluid before work is understood. Implication: preserve the parent purpose and useful end-to-end increments; respect local terminology. The package's epic delivery/outcome distinction and child-coverage checks are engineering synthesis. No universal optimal hierarchy depth, epic size, or field list is established.

## E05 — Long context does not guarantee relevant information is used

Source: Liu et al., [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/html/2307.03172v3), arXiv 2307.03172, initial 2023-07-06; inspected v3 HTML methods/results §§2–4; journal version TACL 2024. Controlled changes in document position and context length for multi-document question answering and synthetic key-value retrieval; QA used 2,655 NaturalQuestions queries.

Finding: tested models used positions unevenly and could degrade with more context. These were older models and retrieval tasks, not modern ticket-to-code agents. Implication: foreground essential task decisions and supply purposeful pointers rather than indiscriminate background. This is a cautious transfer inference, not proof that all current agents lose middle content, nor support for a word cap or mandatory repetition. E06–E08 provide more directly relevant but mixed coding-agent evidence.

## E06 — Generic generated context can add cost without improved resolution

Source: Gloaguen et al., [Evaluating AGENTS.md](https://arxiv.org/html/2602.11988v1), v1, 2026-02-12. Inspected §§3–5 and experimental setup/results. Version pinned deliberately; later revisions were not assessed.

Design: 300 SWE-bench Lite tasks and 138 AGENTbench tasks from 12 Python repositories; four model/harness combinations including Sonnet 4.5 and GPT-5.2, one completion per setting. Conditions: absent, generated, and where available developer-written context. Generated context generally increased cost and sometimes reduced resolution; developer-written context showed modest benefits in some settings. Task statements/tests in AGENTbench were partly generated from reference patches, limiting ecological validity.

Implication: do not assume extra context or generic process obligations help. Include task-specific constraints and useful tooling information. This study concerns repository guidance, not ticket schema. E07 found efficiency benefits under different sampling/metrics; E08 found no detectable correctness effect in a smaller study. Confidence in a universal direction is low; confidence that content should earn its place is higher as engineering judgment.

## E07 — Efficiency benefits do not establish correctness benefits

Source: Lulla et al., [On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents](https://arxiv.org/html/2601.20404v1), v1, 2026-01-28. Inspected study design, results table, and research roadmap.

Design: paired with/without context runs, 124 PR-derived tasks from 10 repositories, GPT-5.2-Codex. Small code changes were selected; issue-like descriptions were generated from patches. Reported lower median runtime and output tokens with context. Input-token medians did not fall; correctness and alignment were explicitly left for future evaluation.

Implication: useful context can affect efficiency, so do not ban it on E06's basis. Measure correctness separately from cost/latency. Single-agent sampling, generated tasks, and limited scope constrain transfer. This source does not establish that shorter or longer ticket descriptions are superior.

## E08 — A small ablation found no detectable correctness benefit

Source: Khatri, [Do Context Files Help Coding Agents?](https://arxiv.org/html/2607.27250v1), v1, 2026-07-28. Inspected methods, result tables, and limitations.

Design: 17 Codex / 15 Claude tasks across three Python repositories, three repeats, no context versus always-on versus selective; 288 runs with valid gold-test evaluation. No detectable correctness effect in this sample. Small task sample, floor/ceiling behavior, agent-specific screening, different injection channels, and unmatched selective content in two repositories restrict inference. The paper's equivalence bounds are descriptive rather than a powered demonstration of no meaningful effect.

Implication: more context is not a dependable correctness intervention; evaluate the actual task/model. Does not prove selective loading is best, context useless, or a ticket template ineffective. E06/E07 differ in tasks, contents, agents, and outcome metrics; they cannot be averaged into one causal estimate.

## E09 — Statements and tests can disagree in consequential ways

Source: OpenAI, [Separating signal from noise in coding evaluations](https://openai.com/index/separating-signal-from-noise-coding-evaluations/), 2026-07-08. Inspected methodology, annotation campaign, failure taxonomy, and discussion.

Type: first-party benchmark audit, not peer-reviewed ticket-authoring experiment. Agent-assisted review and five-engineer assessments examined flagged tasks from SWE-bench Pro's public split. Reported failures include omitted requirements, misleading statements, overly restrictive tests, and insufficient test coverage. Screening and the provider's benchmark interests constrain interpretation; benchmark prevalence is not general workplace prevalence.

Implication: map promised behavior to checks and examine contradictions in both directions. Do not require hidden design choices or infer completion from passing weak tests. Reasonable repository conventions can resolve implementation details; missing product decisions require clarification. This supports fairness checks, not a guarantee of agent success.

## Excluded and limited-access material

- Utrecht's direct repository PDF for The Use and Effectiveness of User Stories in Practice returned an access error. Search discovery indicated self-reported practitioner perceptions; it was not used as causal evidence or a package rule basis.
- Ambiguity in user stories: A systematic literature review (2022) and AmbiTRUS (2025) were discovered, but their full methods were not inspected. They are not used to substantiate claims here; omission leaves coverage of newer linguistic interventions incomplete.
- A 2025 robustness-diagram acceptance-criteria study was discovered and its landing page opened; full methods/results were not assessed. It was excluded from design support because modeling-diagram accuracy is indirect for execution handoffs.
- Positive long-context mitigation papers were discovered but not method-reviewed. E05 is therefore explicitly historical and conditional, not a claim about all 2026 models.

## Evidence to behavior

| Decision/action | Basis and classification | Applicability/counterweight | Observable check |
|---|---|---|---|
| Keep a shared core and optional agent handoff | Dual-audience design objective; engineering synthesis with E02/E09 | Not a directly tested format; separate tracker views are fine if one canonical contract remains | Both readers accept the same behavior |
| Put actor/capability/benefit in a compact story, details nearby | E01–E03 practitioner/framework support | No mandatory sentence syntax; technical enablers need honest purpose | Purpose is understandable; no hidden capability in rationale |
| Distinguish epic, story, subtask and map contribution | E03/E04 practitioner support; engineering hierarchy checks | Local definitions vary; discovery epics may remain broad | Children contribute and do not contradict parent |
| Use observable criteria and align checks both ways | E03 practitioner advice, E09 audit; engineering synthesis | Relevant boundary/error cases only; no mandatory Gherkin | Each accepted behavior can be inspected; no hidden obligation |
| Separate delivery from outcome measurement | Engineering choice | No causal validation in this review; supplied metrics take precedence | Software completion does not claim business impact |
| Record consequential missing decisions; do not invent facts | Engineering constraint for faithful authoring | Routine design remains discretionary; drafts can proceed independently | Unknown behavior is visible and readiness qualified |
| Add accessible starting state, pointers, constraints, verification for agents | E02/E09 transfer inference; engineering design | Not a universal required-field list; analysis-only tasks differ | Pickup can identify relevant input/action and success evidence |
| Omit redundant context and foreground essentials | E05–E08 conditional empirical support plus inference | Mixed results; neither a context ban nor fixed word cap | Every retained detail changes a decision or identifies a needed source |
| Preserve action scope in description-only work | Task scope plus engineering safeguard | Requested tracker updates or execution may be authorized separately | Output is description/package, not unrequested operational action |

## Open questions and refresh triggers

Exact hierarchy schemas, shared-core effectiveness, required agent fields, and readiness judgments remain unproven design choices. Test on representative human and agent assignments before claiming productivity or correctness gains. Revisit when the target model/harness changes, repeated pickup failures occur, or new direct ticket-description experiments appear. Refresh source versions before quantitative reuse. No recurring refresh or installation was authorized.
