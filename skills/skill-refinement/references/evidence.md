# Evidence ledger

Research checked: **2026-10-07 (Europe/Berlin)**. This is a targeted review, not an exhaustive systematic review or independent replication. Links are primary papers, first-party documentation, author-run experiments, and original GitHub reports. Publication dates and revisions are separated from access dates. All entries were accessed on the date above; undated live documents are snapshots, not timeless guarantees.

## Research question and search scope

**Question:** Which practices improve the task usefulness of agent-facing Markdown, and what evidence supports selecting, rewriting, retaining, or removing its content? Length is neither the eligibility criterion nor the primary outcome.

The renewed review searched primary agent-context/skill experiments, prompt optimization and compression studies, official authoring/evaluation documentation, original GitHub implementations/issues, and first-party engineering reports. Search families included instruction adherence, skills presentation, prompt repetition, brevity bias/context collapse, outcome-driven prompt optimization, negative optimization results, and skill discovery failures. Publication and revision pages were checked through 2026-10-07, including a 2026-10-05 preprint. Sources were selected for a concrete bearing on content decisions or verification, not simply for recency or agreement. This is a purposive evidence review, without a systematic database export, formal risk-of-bias instrument, or independent replication.

Papers received more weight for tested outcomes than vendor recommendations; product docs govern current format/behavior only. Repository popularity, duplicate blog coverage, and closed issue status do not establish effectiveness. Newest does not mean strongest. Abstract-only review is labeled below. No meta-analysis pools incompatible populations or metrics.

## Navigation and decision synthesis

- **Content and optimization outcomes:** E07–E08, E18–E25. Useful knowledge can help; summarization and reflection can also destroy it. Compare actual results.
- **Counterexamples to simplistic editing:** E02, E06, E18, E20, E22. Neither shortness, deduplication, detailed playbooks, nor automatic rewriting is universally better.
- **Loading and operational context:** E01, E09–E12, E15–E17, E26–E28. Separate discovery, retrieval, execution, and UI visibility.
- **Indirect or emerging evidence:** E03, E13, E19, E23, E29. Do not translate other task regimes or preliminary findings into universal Markdown rules.

The [decision matrix](decision-rules.md) connects each operational choice to supporting and contradictory entries, confidence limits, and a local check. The defensible objective is minimal *sufficient* task guidance. Evidence supports testing content utility; it does not establish a universally optimal Markdown style, file size, number of rules, or compression ratio. Individual edits require verified local facts or local task evidence; research-based transfer and editorial judgment are labeled hypotheses.

Quality labels describe the support for the stated claim, not a numeric score: **controlled** = comparative experiment (external validity still limited); **observational** = association, not causation; **normative** = authoritative format/product behavior, not effectiveness evidence; **case study** = narrow first-party experiment; **anecdotal** = unreplicated report. A preprint is not called peer reviewed without a verified venue statement.

## Research

### E01 — Agent Skills specification

**Source:** [Agent Skills specification](https://agentskills.io/specification). **Date/version:** undated live documentation, accessed 2026-10-07. **Quality:** normative; high authority for format, no causal evidence for performance.

The specification separates discovery metadata, activated instructions, and on-demand resources; recommends an entrypoint below 5,000 tokens and 500 lines; and encourages focused references. These are authoring guidelines, not experimentally established failure thresholds. **Implication:** use a concise core and explicit routes. **Boundary/counterweight:** E02 finds no detectable size effect in its tested range, and E12 shows retrieval can fail. A standards recommendation does not establish an ideal size for every task.

### E02 — Instruction adherence factorial experiment

**Source:** Damon McMillan, [Instruction Adherence in Coding Agent Configuration Files](https://arxiv.org/abs/2605.10039v1), [full PDF](https://arxiv.org/pdf/2605.10039v1), Tables 2 and 5 / limitations. **Date:** 2026-05-11, v1. **Quality:** controlled preprint; moderate, narrow applicability.

Across 1,650 Claude Code sessions, two TypeScript codebases, and five tasks, the experiment tests 25/100/250/500-line files, position, architecture, and adjacent conflict. None of seven corrected contrasts is detectable; size/conflict have affirmative-null Bayesian support. The target is a trivial function annotation; Opus 4.7 comparisons have a CLI-version confound. **Implication:** do not infer poor compliance from line count. **Counterweight:** E03 tests much longer inputs and different outcomes. This result does not prove conflicts harmless or all long documents equally effective.

### E03 — Length can hurt even when retrieval succeeds

**Source:** Yufeng Du et al., [Context Length Alone Hurts LLM Performance Despite Perfect Retrieval](https://arxiv.org/abs/2510.05381v1), [full text](https://arxiv.org/html/2510.05381v1). **Date:** 2025-10-06, v1; arXiv records acceptance at Findings of EMNLP 2025. **Quality:** controlled, moderate-to-strong within tested tasks; indirect for skills.

Five models on math, QA, and coding exhibit degradation as input grows, including conditions that suppress retrieval failure or distraction. The paper reports a broad 13.9%–85% degradation range across settings; it is not a predicted loss from any particular skill size. **Implication:** fitting the advertised context window is insufficient evidence that added context is free. **Counterweight:** E02 concerns short configuration files, so these findings do not establish a shared cutoff. Do not turn the range into an expected savings or accuracy claim.

### E04 — Repository context evaluation, updated conclusion

**Source:** Thibaud Gloaguen et al., [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988v3), [full text](https://arxiv.org/html/2602.11988v3), §4.2 and Table 3. **Dates:** first 2026-02-12; v3 2026-09-29. **Quality:** controlled preprint, multiple agents and two benchmarks; moderate-to-strong within scope.

The current revision finds no statistically significant success effect versus no context: generated files are slightly negative, developer files slightly positive. Generated files increase average costs 20% on SWE-bench and 23% on CTXbench; developer files outperform generated ones significantly. Outcomes concern issue resolution in the evaluated repositories, not all organizational constraints. **Implication:** test additional requirements and avoid assuming automatic repository summaries help. **Counterweight:** E05 measures efficiency differently; E06 is observational. **Correction:** the earlier conversation's “AGENTS.md reduces success” is too strong as a general conclusion; current success contrasts versus baseline are not significant.

### E05 — Efficiency improvement on PR tasks

**Source:** Jai Lal Lulla et al., [On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents](https://arxiv.org/abs/2601.20404), [author-hosted paper](https://assets.empirical-software.engineering/pdf/jaws26-agents.md-efficiency.pdf). **Date:** first submitted 2026-01-28; retrieved abstract and author PDF. **Quality:** comparative experiment; moderate for operational efficiency, weaker for correctness.

On 124 pull-request tasks from 10 repositories, context files are associated with 28.64% lower median runtime and 16.58% fewer median output tokens, with comparable completion behavior. Completion behavior is not comprehensive patch correctness. **Implication:** concise, useful instructions may reduce wasted exploration. **Counterweight:** E04 reports higher inference cost on different tasks/settings. Different agents, context contents, metrics, and experimental populations prevent averaging these percentages or declaring either result universal.

### E06 — Longer instructions correlate with some improvements

**Source:** Ali Arabat and Mohammed Sayagh, [Toward Instructions-as-Code](https://arxiv.org/abs/2606.13449v1), [publication DOI](https://doi.org/10.1145/3793302.3793601). **Dates:** MSR 2026 venue listed in arXiv; preprint 2026-06-11. **Quality:** observational; useful counterexample, weak causal inference.

Before/after analysis covers 15,549 agentic PRs across 148 projects. Outcomes vary; projects with improved merge rates tend to have longer, more structured instruction files. Adoption timing, task mix, project maturity, and review practices can confound that association. **Implication:** preserve useful structure and local knowledge; shortening is not itself a success criterion. **Counterweight:** this does not establish that adding length causes higher merge rates, nor override controlled findings in E04.

### E07 — SkillsBench, current and historical metrics

**Source:** Xiangyi Li et al., [SkillsBench v4](https://arxiv.org/abs/2602.12670v4), [full text](https://arxiv.org/html/2602.12670v4), §5 and Appendices D/F/N. **Dates:** first 2026-02-13; v4 2026-06-14. **Quality:** paired benchmark preprint, deterministic verifiers; moderate-to-strong within benchmark.

Current inventory: 87 tasks, 8 domains, 18 model/host configurations; pass rate 33.9% without skills versus 50.5% with curated skills (+16.6 percentage points). Thirteen tasks have negative deltas. Self-generated packs underperform in three diagnostic configurations, with discovery, effort, coverage, and creator/solver caveats. Length/module groups compare different tasks, so they do not isolate compression causally. **Implication:** validate curation, activation, and execution together. **Counterweight:** E08 controls presentation and finds uncertain contrasts. **Superseded:** the conversation's +16.2 pp and 16/84 negative-task figures refer to earlier reporting; do not combine them with v4 denominators.

### E08 — Controlled presentation-granularity study

**Source:** Xiaonan Xu and Wenjing Wu, [Skill Availability and Presentation Granularity](https://arxiv.org/abs/2605.31408v1). **Date:** 2026-05-29. **Quality:** controlled preprint; moderate, only 30 tasks/two model configurations.

The study uses six conditions and five trials per task/condition/model (1,800 rows), aggregating trials at task level. Skill availability has clear gains, but low versus high abstraction and adding one example produce smaller, uncertain, model-dependent differences; primary abstraction confidence intervals cross zero. **Implication:** useful knowledge is better supported than a universal presentation recipe. **Counterweight:** E07's module-count/length associations should not become “exactly two to three modules” or “remove all examples” requirements. A null contrast is not proof that every presentation choice is equivalent.

### E09 — First-party context and skills architecture

**Sources:** Anthropic, [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29; [Equipping agents with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills), 2025-10-16, update 2025-12-18. **Quality:** first-party engineering guidance, not independent controlled evidence.

The authors recommend high-signal context, just-in-time access, and layered skill resources. They also distinguish minimal sufficient instructions from simply short text. **Implication:** separate common decisions from optional procedures and execute reusable code where appropriate. **Counterweight:** E12 demonstrates that on-demand discovery can miss relevant documentation; actual activation and read traces matter more than folder structure. A vendor design pattern is a starting hypothesis, not proof of task success.

### E10 — OpenAI discovery behavior

**Source:** OpenAI, [Build skills](https://learn.chatgpt.com/docs/build-skills) (the former developers.openai.com/codex/skills URL redirects here). **Date:** undated live documentation, accessed 2026-10-07. **Quality:** normative for the documented product; version-sensitive.

The current page describes names/descriptions before full activation, plus Codex file paths. It documents a discovery-list budget of 2% of context or an 8,000-character fallback when context size is unknown, with shortening and possible omissions. This concerns the initial list, not a scientific limit on skill quality. **Implication:** keep descriptions precise and verify actual visibility when many skills are installed. **Counterweight:** host budgets differ (E11) and historical reports can be stale (E15). Do not hardcode these host settings into a universal optimizer threshold.

### E11 — Claude Code discovery and compaction

**Source:** Anthropic, [Extend Claude with skills](https://code.claude.com/docs/en/skills), sections on invocation and shortened descriptions. **Date:** undated live documentation, accessed 2026-10-07. **Quality:** normative, version-sensitive.

The current docs describe a 1% discovery-list budget with low-use descriptions dropped, configurable settings, and distinct post-compaction retention limits: first 5,000 tokens per invoked skill within a shared 25,000-token budget. **Implication:** initial discovery, full activation, and post-compaction availability are different failure surfaces. Keep essential constraints early and test the installed host. **Counterweight:** these values differ from older issue reports and E10; they are product behavior, not evidence that a given instruction length is optimal.

### E12 — Retrieval failure and useful passive context

**Source:** Jude Gao / Vercel, [AGENTS.md outperforms skills in our agent evals](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals). **Date:** 2026-01-27. **Quality:** first-party case study; useful operational counterexample, limited generalization.

On Next.js 16 evals, default skill use matches the 53% baseline; the skill is not invoked in 56% of cases. Explicit invocation guidance reaches 79%, while a compressed 8 KB docs index reaches 100%. This is a narrow vendor experiment, not a guarantee across agents or tasks. **Implication:** verify routing and retain a small always-visible index where it prevents demonstrated discovery failures. **Counterweight:** E09 recommends on-demand access, but it requires dependable selection. The 8 KB index is an observed design, not an 8,000-character cutoff.

### E13 — Context Rot experiments

**Source:** Kelly Hong, Anton Troynikov, Jeff Huber / Chroma, [Context Rot](https://www.trychroma.com/research/context-rot). **Date:** 2025-07-14, clarification noted 2025-07-16. **Quality:** controlled vendor technical report with replication code; moderate, indirect for skill authoring.

Experiments across an 18-model set investigate retrieval similarity, distractors, conversational memory, and repeated-word tasks; not every model appears in every experiment. Performance varies with context length and content. **Implication:** measure relevant loaded context and test realistic distractors. **Counterweight:** simplified tasks and older models do not establish a short-skill size threshold or a uniform slope of degradation. E02 tests a different regime.

### E14 — Context files evolve like configuration

**Source:** Worawalan Chatlatanagulchai et al., [Agent READMEs](https://arxiv.org/abs/2511.12884v2). **Dates:** first 2025-11-17; v2 2026-08-09. **Quality:** observational characterization; not an effectiveness experiment.

The corpus contains 2,303 files from 1,925 repositories. Frequent small changes and complex prose characterize maintenance; security and performance instructions are less prevalent than functional content. **Implication:** review additions and keep an evidence history rather than accumulating instructions indefinitely. **Counterweight:** prevalence does not identify which omitted rules would help; it does not justify injecting generic security/performance checklists into every skill.

### E15 — GitHub discovery-budget report

**Source:** [anthropics/claude-code issue #68135](https://github.com/anthropics/claude-code/issues/68135). **Date:** opened 2026-06-13; closed when inspected 2026-10-07. **Quality:** anecdotal, original user report; not independently reproduced here.

The reporter on version 2.1.153 describes 81 descriptions dropped and a listing-budget warning. This is evidence of a practical discovery failure report, not proof of current behavior on all versions or of the claimed resource impact. **Implication:** inspect actual exposed skill metadata before rewriting the skill body to fix activation. **Counterweight:** E11 is the current product reference; closed status alone does not prove a fix. Do not recommend raising budgets based solely on an issue.

### E16 — Reproducibility resources

**Sources:** [benchflow-ai/skillsbench](https://github.com/benchflow-ai/skillsbench), [agentskills/agentskills](https://github.com/agentskills/agentskills). **Date:** live repository READMEs inspected 2026-10-07; no commit was pinned or executed in this review. **Quality:** original implementation artifacts, not independent confirmations.

SkillsBench exposes task/oracle/verifier structure and matched skill conditions; the standards repository provides specification and validation tooling. **Implication:** use observable task verifiers and validate packaging independently of prose judgment. For replication, pin a commit, dependencies, task inventory, model/host, and scoring rules before running. **Counterweight:** a repository's current default branch can differ from a paper's frozen experiment. This package's local tests do not constitute a SkillsBench run.

### E17 — Practical AGENTS.md authoring case study

**Source:** Steve Kearns / AAIF, [Writing an effective AGENTS.md](https://aaif.io/blog/writing-an-effective-agents-md). **Date:** 2026-08-13. **Quality:** first-party engineering case study; small experiment plus synthesis.

The article describes a five-run comparison on one repository/agent and recommends documenting actionable local exceptions, commands, and completion criteria. **Implication:** specific navigation or environment information can earn its place. **Counterweight:** the small experiment cannot resolve the broader mixed results in E04–E06; its summaries of those studies are not independent evidence and should not be counted as additional replications.

## Content-focused research added in version 2

### E18 — ACE: brevity bias and information loss

**Source:** Qizheng Zhang et al., [Agentic Context Engineering v3](https://arxiv.org/abs/2510.04618v3), [full text](https://arxiv.org/html/2510.04618v3), §§2.2, 4, 5. **Dates:** first 2025-10-06; v3 2026-03-29; ICLR 2026 listed. **Quality:** peer-reviewed comparative experiments and ablations; moderate within evaluated agent/domain tasks. Full methods and limitations inspected.

ACE curates incremental playbook updates using execution feedback. Experiments show benefits over several adaptation baselines and an example of repeated summarization losing useful information and accuracy. Its authors also identify tasks that need only a concise reusable rule. Reflector quality remains a dependency. **Implication:** preserve useful mechanisms and trace edits to retained knowledge. **Counterweight:** does not show that longer files always help or that every rewrite collapses context; its method changes multiple components. Do not turn this into a prohibition on coherent restructuring.

### E19 — IFScale: many simultaneous inclusion requirements

**Source:** Daniel Jaroslawicz et al., [How Many Instructions Can LLMs Follow at Once?](https://arxiv.org/abs/2507.11538v1). **Date:** 2025-07-15. **Quality:** controlled preprint; abstract-level inspection in this refresh; indirect for agent Markdown.

Twenty models from seven providers are tested on a report-writing benchmark with up to 500 keyword-inclusion instructions; even the best reaches only 68% at maximum density. **Implication:** simultaneous requirements can be a source of failure worth testing. **Counterweight:** keyword inclusion is not semantic task execution, and obligation count is not line count or the frequency of “must.” This supplies no acceptable maximum number of instructions. Retain legitimate requirements and remove unrelated work based on task evidence, not this benchmark's counts.

### E20 — Prompt repetition can improve results

**Source:** Yaniv Leviathan et al., [Prompt Repetition Improves Non-Reasoning LLMs](https://arxiv.org/abs/2512.14982v1), [full text](https://arxiv.org/html/2512.14982v1), §2/Appendix A.2. **Date:** 2025-12-17; API experiments February–March 2025. **Quality:** controlled preprint; moderate for its tested prompting setup, indirect for skill edits.

Seven models, seven benchmarks, and multiple orderings test whole-input repetition. Non-reasoning comparisons favor repetition; reasoning-enabled results are mostly neutral. The reported significance criterion is p<0.1; latency has exceptions for long Anthropic requests, and input volume still grows. **Implication:** repetition is not intrinsically useless. **Counterweight:** this does not establish that duplicated policy paragraphs help current reasoning agents. Inspect function and scope, and test uncertain consolidation instead of automatically deleting detected duplicates.

### E21 — GEPA: optimize against task feedback

**Source:** Lakshya A. Agrawal et al., [GEPA v2](https://arxiv.org/abs/2507.19457v2), [paper PDF](https://arxiv.org/pdf/2507.19457v2), [implementation](https://github.com/gepa-ai/gepa). **Dates:** first 2025-07-25; v2 2026-02-14; ICLR 2026 Oral listed. **Quality:** peer-reviewed benchmark comparison; paper PDF and repository workflow inspected here, not independently replicated; HTML retrieval failed, so the PDF was used.

GEPA uses trajectories and natural-language feedback to propose, test, and select prompt changes; the paper reports gains over GRPO and MIPROv2 across six tasks. **Implication:** use concrete failures and outcome comparisons to decide between edits. **Counterweight:** not an evaluation of this Markdown optimizer or proof that reflection always improves a prompt; E22 reports regression conditions. The implementation is a reproducibility resource, not another independent study; no commit was executed in this review.

### E22 — Reflection can make a prompt worse

**Source:** Shiyan Liu et al., [Reflection in the Dark v2](https://arxiv.org/abs/2603.18388v2). **Dates:** first 2026-03-19; v2 2026-06-08; ACL SRW 2026 listed. **Quality:** comparative workshop study; methods, results, and limitations inspected in the [full text](https://arxiv.org/html/2603.18388v2); limited to its mathematics tasks and configurations.

With a defective GSM8K seed, the authors report a GEPA accuracy drop from 23.81% to 13.50%; their VISTA method separates hypotheses from rewriting and verifies candidates. **Implication:** a plausible explanation of an edit is not evidence of improvement; retain baselines and inspect regressions. **Counterweight:** two math benchmarks, one optimization random seed, and a defective output ordering do not establish GEPA's general failure. The authors note modern reasoning models may avoid that ordering defect. This does not require adopting VISTA. Local verification, not copying a new architecture, is the transferable hypothesis.

### E23 — Learned compression is not a license for arbitrary deletion

**Sources:** Zhuoshi Pan et al., [LLMLingua-2](https://aclanthology.org/2024.findings-acl.57/), Findings ACL, August 2024; Huiqiang Jiang et al., [LongLLMLingua](https://aclanthology.org/2024.acl-long.91/), ACL, August 2024. **Quality:** peer-reviewed compression experiments; publication abstracts inspected in this refresh; indirect for maintained instruction files.

LLMLingua-2 argues token entropy is an imperfect importance surrogate and learns compression from distilled data. LongLLMLingua targets key information and its placement in long-context tasks. **Implication:** compression quality depends on retained information and task outcomes, not a compression ratio alone. **Counterweight:** these are specialized algorithms with evaluated distributions, not evidence for stripping grammar, abbreviating identifiers, or making all Markdown terse. Neither validates this package's editorial rewrites. No paper's advertised performance or latency ratio is used as a target here.

### E24 — Official skill authoring practice

**Source:** Anthropic, [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), core principles and evaluation sections. **Date:** undated live docs, accessed 2026-10-07. **Quality:** first-party guidance; authoritative recommendations, not controlled performance evidence. Relevant sections inspected.

Guidance favors information the agent lacks, task-appropriate specificity, conditional resources, and evaluation from observed gaps before expanding documentation. It recommends observing whether fresh instances find and apply guidance. **Implication:** start with actual task needs and test selection as well as execution. **Counterweight:** vendor advice alone cannot establish a cross-model editing law; E08 reports uncertain presentation effects. Its authoring size suggestions are not review gates, and its checklist is not imported wholesale as mandatory project policy.

### E25 — Outcomes, traces, and graders

**Source:** Anthropic, [Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). **Date:** 2026-01-09. **Quality:** first-party engineering synthesis; not an independent controlled trial. Full article inspected.

The article distinguishes stated completion from actual outcomes, discusses repeated trials, trace inspection, and complementary deterministic/model/human graders. Brittle graders can reject valid behavior. **Implication:** inspect edited artifacts and downstream task results; a script passing regex checks cannot prove effective agent instructions. **Counterweight:** a model judge also needs calibration; this does not mandate a large evaluation system for a small verified correction. This release separates mechanical tests, author-reviewed examples, and unrun independent agent comparisons.

### E26 — A repository map can help navigation

**Source:** Ryan Lopopolo / OpenAI, [Harness engineering](https://openai.com/index/harness-engineering/). **Date:** 2026-02-11. **Quality:** first-party production case study; no isolated randomized comparison. Relevant repository-knowledge and verification sections inspected.

The team reports replacing a monolithic instruction manual with an entrypoint into maintained repository knowledge, alongside enforcement and feedback mechanisms. **Implication:** make authoritative facts findable and keep maintenance checks close to them. **Counterweight:** the cited roughly 100-line entrypoint is an implementation detail, not a quality boundary. Many environment changes coexist. E12 warns that optional retrieval can fail; verify it locally rather than prescribing a map for every small file.

### E27 — GitHub's analysis of agent instruction files

**Source:** Matt Nigh / GitHub, [Lessons from over 2,500 repositories](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/). **Dates:** 2025-11-19; updated 2025-11-25. **Quality:** first-party descriptive/engineering article; insufficient published experimental detail for causal ranking.

The author recommends specific commands, scope, boundaries, and examples over vague personas. **Implication:** inspect whether prose specifies a real decision rather than a generic aspiration. **Counterweight:** the article does not provide a matched controlled success experiment establishing its claimed best practices; its Copilot custom-agent setting also differs from repository-wide instructions. Do not require all six suggested sections or assume every command should move earlier. Check project facts and actual outcomes.

### E28 — UI absence is not necessarily failed loading

**Source:** [anthropics/claude-code issue #40031](https://github.com/anthropics/claude-code/issues/40031). **Dates:** opened 2026-03-27; closed as duplicate when inspected 2026-10-07. **Quality:** original anecdotal report, unreplicated here.

The reporter describes plugin skills absent from the UI list despite debug logs showing they loaded and worked. **Implication:** distinguish visibility, registration, invocation, and actual instruction reads before rewriting content to fix a loading symptom. **Counterweight:** user reports and inferred internal behavior are not current platform guarantees; closure does not verify resolution. E15 describes a different reported failure. Consult current product documentation and traces for the installed host.

### E29 — Emerging research on noisy optimizer selection

**Source:** Haoyue Liu et al., [BudgetAPO](https://arxiv.org/abs/2610.05671v1). **Date:** 2026-10-05. **Quality:** two-day-old preprint at review time; abstract-level inspection only; preliminary and unreplicated.

The authors study allocation of a tight prompt-optimization budget and noisy candidate comparisons, proposing shared paired evaluation slices and adaptive evaluation. **Implication:** candidate selection and evaluation budget deserve explicit reporting. **Counterweight:** no independent confirmation or transfer to agent Markdown was verified. Included as current evidence to monitor, not grounds for adding algorithmic requirements to SKILL.md or declaring a statistically justified trial count.

## Focused decision/followability refresh — version 3

This additional targeted pass on 2026-10-07 revisited E04 (current context-file results and ablations), E18 (context-loss counterevidence and limitations), E22 (optimizer regression results), E24 (task-dependent specificity), and E12 (actual discovery failures). Their earlier findings remain qualified as above. The remaining legacy entries were retained from the earlier review, not represented as independently reappraised during this pass.

Actual search families: “agent instruction optimization task specific context instructions contradictions minimal sufficient AGENTS evaluation 2026” and “LLM prompt optimization instruction applicability constraints benchmark regressions 2026.” Follow-up reading targeted the sources above and E30's methods, compiler results, and limitations. Instruction fine-tuning surveys and a newly surfaced chess-puzzle optimization paper were not pursued: neither was needed to decide this release's Markdown editing behavior. This is a decision-focused search, not a census of recent papers.

### E30 — Conflicts and rewriting benefits depend on the tested task

**Source:** Atul Anand and Sourav Chattaraj, [Instruction Stacking Collapse v1](https://arxiv.org/abs/2608.02639v1), [full text](https://arxiv.org/html/2608.02639v1), §§3–6. **Date:** HTML manuscript dated 2026-07-31; accessed 2026-10-07. **Quality:** unreplicated preprint; methods/results/limitations inspected, implementation not run.

The benchmark stacks verifiable constraints, separating logically impossible combinations from behavioral interference. A compiler groups, merges, and adds precedence notes. Benefits vary by target model; stronger-model results are essentially unchanged. **Limits:** machine-degraded baselines, one compiler model, partial verifier audit, and narrow task/grid coverage. Verifiers measure literal compliance rather than task quality; headline degradation includes unsatisfiable combinations. Reported set/pair counts and interval wording merit verification before quantitative reuse; no exact percentage is adopted here.

**Implication:** check compatibility and scope before attributing failure to document length. A rewrite cannot satisfy incompatible requirements. **Counterweight:** this does not justify inventing precedence, deleting binding constraints, a maximum rule count, or mandatory compilation. Conditional clarity and conflict handling are engineering choices to test on local tasks, not guaranteed improvements from this preprint.

### Changes justified by this refresh

- Make consequential decisions explicit enough to execute, with applicability in the rule itself (E24 guidance; engineering synthesis).
- Separate unresolved contradictory requirements from opportunities for independent edits (E30 plus task authority; no automatic deletion).
- Scale validation to uncertainty instead of the size of a rewrite (E21/E22 demonstrate why comparisons matter for performance claims; they do not require a full benchmark for routine corrections).
- Verify changed routes through actual task actions where feasible (E12); do not equate a working link or optimizer audit with runtime retrieval.

No source establishes a universally optimal wording or validates this optimizer as a whole. The local execution results and remaining gaps are in [VALIDATION.md](../VALIDATION.md).

## Conflicts and remaining uncertainty

| Apparent disagreement | Resolution for this skill |
|---|---|
| Long contexts hurt in some experiments (E03/E13); size has no detected effect in E02. | Different regimes and endpoints. No eligibility gate or universal cutoff follows. |
| Shortening can remove distraction (E23); summarization loses useful knowledge (E18). | Test which information survives and what behavior changes. Neither length direction proves quality. |
| Remove repetition (common advice); repetition helps in E20. | Distinguish duplicated obligations, scoped reminders, and whole-prompt repetition. No blanket deduplication rule. |
| Context costs more (E04); can improve efficiency (E05) or task success (E07/E08). | Content, task populations, agent settings, and measured endpoints differ. Do not pool percentages. |
| Longer instructions correlate with better results (E06); focused bundles correlate with gains (E07). | Neither association isolates length while preserving content. |
| Conditional loading recommended (E09/E24); passive index works better in E12. | Relevant instructions must actually be found. Test selection and task execution separately. |
| Reflective optimization works in E21; can regress in E22. | Hypotheses require outcome checks, held-out tasks, and a retained baseline. |
| Concrete prose advised (E24/E27); presentation contrasts uncertain (E08). | Treat clarity changes as conditional design judgments unless local testing demonstrates benefit. |

No reviewed study validates this package as a universally optimal Markdown optimizer. Unknowns include transfer across newer models/hosts, multilingual files, long-term maintenance, rare invariant failures, and interaction with system instructions. Minimality is relative to intended tasks and reliability requirements. Lack of detected regression in a small sample does not establish equivalence. This review rejects numeric size and lexical rule-density scores as decision criteria; it does not claim file size can never affect runtime.

## Refresh protocol

Search current primary papers and revisions, official docs, original issues/repositories, and engineering experiments. Explicitly seek null findings, failed optimizations, useful longer contexts, beneficial repetition, and retrieval failures. Use news for discovery; trace claims to the source. Read methods/limitations before adopting consequential quantitative claims; mark abstract-only entries and inaccessible sources. Record publication, revision, access date, population, comparator, outcome, quality, limits, and practical implication.

Reconcile revisions into existing entries and retain superseded-metric notes. Do not count a paper, its code, and summaries as independent replications. Map proposed rule changes through decision-rules.md and a relevant evaluation case. Update an existing rule only when evidence changes a practical decision; do not append advice simply because a new paper exists. Preserve known useful details during successive refreshes and record regressions. Keep speculative transfer labeled; do not fabricate local performance evidence. This package does not install or modify a scheduled automation.
