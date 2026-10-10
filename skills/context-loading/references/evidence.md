# Evidence ledger

Reviewed and accessed: **2026-10-07**. Scope: designing agent instruction packages, RAG routing, and deferred tool discovery for a file/tool-capable agent such as Codex. Targeted, decision-oriented literature and implementation review, not a systematic or exhaustive review. Source text was treated as evidence, not operating instructions. All URLs below were opened; relevant inspected sections are named. No cited experiment was independently reproduced.

Targeted refresh: **2026-10-08**. E07 updated to v2; E15–E17 added. The October 1–8 overlap recovered previously unreviewed sources; their publication dates are not presented as today's releases. Other entries retain their original access dates. Detailed run coverage and excluded candidates are recorded outside the package.

Targeted refresh: **2026-10-09**. E18–E20 added from overlapping discovery and a previously pending source. Publication dates remain distinct from access dates; no cited experiment was reproduced.

## Search coverage and stopping rationale

| Decision | Actual query/source families | Result |
|---|---|---|
| Meaning and intended use | Thoughtworks context-engineering, skills, instruction-bloat and progressive-disclosure entries with linked sources | Practice recommendation, not an isolated causal trial |
| Whether longer context harms use | “Lost in the Middle” long contexts; Chroma context-rot methods and limitations | Controlled effects under tested settings; no universal threshold |
| Whether RAG should always be preferred | “retrieval augmented generation long context Self Route 2024”; Route Before Retrieve | Full context and hybrid alternatives materially change the design |
| Whether instruction files help | Thoughtworks citation; “Evaluating AGENTS.md” context files coding agents | Different endpoints; latest September 2026 revision changes interpretation |
| How skills and tools defer detail | Agent Skills specification; Anthropic advanced tool use and context engineering | Concrete interfaces plus vendor implementation reports |
| Recovery from retrieval failures | Contextual Retrieval; Self-Route failure analysis; Pre-Route metadata robustness | Chunk context, cross-domain and multi-step coverage matter |
| Total operational cost | Prompt caching prefix context; official API docs and Claude Code report | Cache reuse and discovery round trips complicate token-only claims |
| Trust boundary | InjecAgent indirect prompt injection tool integrated agents | Deferred content remains an attack surface |

Searches were conducted on the review date through web search, direct URLs and citation following. General web results included aggregators, Reddit, mirrors, Wikipedia and surveys; these were discovery leads only and not evidence for operational rules. Relevant primary papers and official documents were opened instead. Older AGENTS.md v1 was inspected then superseded for current claims by v3. No relevant selected source was blocked; full auxiliary datasets, benchmark repositories and every appendix were not inspected. The optional Claude guide PDFs were search hits only and excluded from the evidence base.

Research stopped after the key design alternatives, direct interfaces, cost mechanisms and failure paths had support or explicit uncertainty. Remaining gaps require workload-specific experiments more than another general bibliography. Mechanistic explanations of attention degradation, current-model effect sizes, optimal granularity, production routing error rates, and comprehensive security defenses remain unresolved.

## E01 — Terminology and adoption judgment

Sources: Thoughtworks, [progressive context disclosure](https://www.thoughtworks.com/en-de/radar/techniques/context-loading), [context engineering](https://www.thoughtworks.com/en-de/radar/techniques/context-engineering), [Agent Skills](https://www.thoughtworks.com/en-de/radar/techniques/agent-skills), [instruction bloat](https://www.thoughtworks.com/en-de/radar/techniques/agent-instruction-bloat). April 2026 Radar; related context-engineering entry also includes November 2025 history. Inspected entry text and outgoing research links.

Type: practitioner synthesis and adoption recommendation. Provides vocabulary and use cases, not a controlled test of progressive loading. The instruction-bloat citation leads to E09, whose endpoint is efficiency, not comprehensive correctness. Implication: use these entries to frame the question; use underlying studies to qualify performance claims. Confidence: useful framing, limited causal support.

## E02 — Context length and relevance affect tested performance

Source: Hong, Troynikov and Huber, [Context Rot](https://www.trychroma.com/research/context-rot), July 14, 2025. Inspected NIAH variations, LongMemEval experiment, model list and limitations.

Type: vendor empirical report spanning 18 models, not every model in every experiment. LongMemEval subset: 306 cleaned prompts; approximately 113k-token full histories versus approximately 300-token focused inputs derived from labels/manual adjustment; model judging. Focused inputs perform better. This is close to an oracle selection comparison, not proof an autonomous router can find the same evidence. Synthetic probes and historical models constrain transfer; mechanism is not established. E06 provides a counterweight when retrieval loses information. Implication: test distractors and missed evidence together; do not promise to eliminate context rot.

## E03 — Just-in-time loading has navigation costs

Source: Anthropic Applied AI, [Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), September 29, 2025. Inspected context retrieval, hybrid approach and compaction sections.

Type: first-party engineering guidance. Lightweight locators enable runtime discovery; exploration can be slow and miss key information. Hybrid upfront plus on-demand loading is explicitly discussed. Compaction risks losing details. No controlled isolation of progressive disclosure. Implication: make routes actionable, retain source handles, and allow upfront loading when it is useful. The skill's sufficiency checks are engineering synthesis, not directly validated prescriptions.

## E04 — Position sensitivity is real in specific tasks

Source: Liu et al., [Lost in the Middle](https://arxiv.org/html/2307.03172v3), v3 November 20, 2023; TACL 2024 publication. Inspected multi-document QA design/results, key-value setup and appendix tables.

Type: controlled experiments varying relevant-information position and context length. Wikipedia QA uses a containing document and distractors; key-value retrieval is synthetic. Tested models include GPT-3.5, Claude 1.3, LongChat and MPT, with additional GPT-4/Llama-2 checks. Results demonstrate positional sensitivity, not a fixed safe context size for modern agents. Implication: include buried prerequisites and distributed evidence in evaluation. Reordering everything to the beginning is not an established universal remedy.

## E05 — Skills define staged loading interfaces

Source: [Agent Skills specification](https://agentskills.io/specification), live documentation accessed October 7, 2026; no immutable version established. Inspected frontmatter, progressive disclosure and file-reference sections.

Type: authoritative format/interface description, not effectiveness evidence. Metadata supports selection, the body is loaded on activation, and supporting resources are conditional. Folder/name agreement and resolvable references support interoperability. Token/line recommendations are authoring guidance, not empirically derived optima. Implication: expose discriminating metadata and conditional reference links; verify each host's actual behavior. Confidence: high for this document's format, conditional across implementations.

## E06 — Full context can outperform lossy retrieval

Source: Li et al., [RAG or Long-Context LLMs?](https://arxiv.org/html/2407.16833v2), v2 October 17, 2024; EMNLP Industry 2024. Inspected sections 3–5 and tables 1–2.

Type: empirical comparison using GPT-4o, GPT-3.5 Turbo and Gemini-1.5 Pro, seven English LongBench and two ∞Bench datasets, Contriever and Dragon. Full context generally beats their RAG baseline; self-routing recovers quality with fewer input tokens. Failure analysis includes multi-step, general, complex and implicit queries; classification partly uses an LLM. Retrieval and model choices limit transfer. No universal top-k follows. Implication: use broader source coverage or iterative retrieval when evidence is distributed; retain full-context fallback. This qualifies E02's oracle-focused results.

## E07 — Metadata routing is promising but not cost-free

Source: Chen et al., [Route Before Retrieve](https://arxiv.org/html/2605.10235v2), v2 May 12, 2026; accessed October 8. Previously reviewed v1. Inspected v2 section 3.3, routing-cost table, evaluation metrics and limitations.

Type: preprint experiments on LaRA and LongBench-v2 with Qwen3 families, DeepSeek-R1 and distilled routers. v2 includes a routing/answering cost decomposition and token-based routing estimates, so describing its cost evidence only as LC selection rate would be incomplete. Its evaluation still uses LC selection as a proxy; the larger router's rationale costs more than Self-Route's routing step, while a smaller distilled router costs less. Assumed prices and long-document comparisons do not establish deployment latency or universal savings. Small-router stability, source-specific grading and distillation constrain transfer. Implication remains: measure downstream quality and total cost locally, without mandating this algorithm.

## E08 — Chunk enrichment can improve retrieval recall

Source: Anthropic, [Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval), September 19, 2024. Inspected preprocessing, methodology, metric and reranking sections.

Type: vendor evaluation across code, fiction and papers. Context-enriched chunks, lexical retrieval and reranking reduced reported top-20 retrieval failure from 5.7% to 1.9% in the highlighted configuration. This is retrieval recall, not end-to-end answer accuracy; bundled techniques, preprocessing costs and selected configurations limit attribution. Implication: consider parent context, hybrid retrieval or reranking for demonstrated misses; test generated context against originals. The published configuration is not a universal chunk or top-k setting.

## E09 — Useful upfront instructions can save work

Source: Lulla et al., [Impact of AGENTS.md on Efficiency](https://arxiv.org/html/2601.20404v1), January 28, 2026. Inspected sections 3–4 and table 1.

Type: paired with/without study using gpt-5.2-codex, 124 tasks across ten selected repositories, small PRs; some task descriptions generated from diffs. Mean wall time and output tokens fell about 20%; input-token medians did not improve. Full functional correctness evaluation is explicitly outside scope; a 50-task manual sanity check is weaker. Selection and task size constrain transfer. Implication: preserve actionable repository guidance and measure total work; this cannot establish human-written superiority or prove shorter instructions cause better correctness. E10 measures a different outcome.

## E10 — More instruction-following need not improve resolution

Source: Gloaguen et al., [Evaluating AGENTS.md](https://arxiv.org/html/2602.11988v3), September 29, 2026; compared against [v1](https://arxiv.org/html/2602.11988v1), February 12, 2026. Inspected benchmark construction, sections 4.1–4.3, tables 2–3 and revision history.

Type: empirical study: 300 SWE-bench Lite and 138 CTXbench Python tasks; four agent/model configurations, one sampled completion per instance/setting. v3 distinguishes nonsignificant success changes versus no file from significant developer-versus-generated differences. Generated-file costs rise 20–23% on average. Tests and task construction partly use LLMs; nonfunctional benefits and modern-model transfer remain limited. It does not isolate file length or progressive disclosure. Implication: evaluate required behavior and task resolution separately from tokens. Do not prescribe deleting all context files or assert a causal “longer is worse” rule.

## E11 — Tool discovery has concrete implementation evidence

Source: Anthropic, [Advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use), November 24, 2025. Inspected Tool Search design and internal evaluation claims.

Type: vendor implementation report. Deferred definitions are discovered and expanded on demand; selected critical tools can remain upfront. Internal MCP evaluations report Opus 4 accuracy rising 49%→74% and Opus 4.5 79.5%→88.1%. Benchmark detail and independent replication are limited; these effects do not establish gains for document RAG or other hosts. Implication: use supported schema discovery, verify actual schemas before calls, and measure catalog recall plus execution errors. Savings vary with library and request mix.

## E12 — Caching and disclosure solve different costs

Source: Anthropic, [Prompt caching documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching), live documentation accessed October 7, 2026; no pinned release. Inspected exact-match behavior and stable-prefix guidance.

Type: authoritative API description. Reusing an identical prefix saves computation; the content remains logically available to the model. Implication: distinguish physical computation/billing from context occupancy; preserve stable prefixes where supported. Host details can change, so this package avoids copying model-specific pricing, thresholds or code. Caching does not demonstrate improved relevance or cure distraction.

## E13 — Dynamic loading must respect cache behavior

Source: Thariq Shihipar, [Lessons from building Claude Code](https://claude.dev/blog/lessons-from-building-claude-code-prompt-caching-is-everything/), April 30, 2026. Inspected prompt layout, tool-list stability and compaction discussion.

Type: first-party deployment experience, not a controlled comparison. Stable prompt prefixes matter operationally; changing early tool definitions can disrupt reuse. Implication: inspect the host's supported deferred-loading protocol instead of implementing discovery by rebuilding its initial tool list every turn. This is host-dependent; do not turn “never change tools” into a universal agent rule.

## E14 — Selected external content remains untrusted

Source: Zhan et al., [InjecAgent](https://arxiv.org/html/2403.02691v3), 2024, v3. Inspected abstract, benchmark design and limitations.

Type: controlled attack benchmark with 1,054 cases, 17 user tools and 62 attacker tools. Demonstrates indirect instruction attacks through external content. Single-turn/two-step assumptions and older agents limit present-day effect-size transfer. It does not evaluate this package or prove a prompt-only defense. Implication: preserve instruction/data separation and enforce permissions outside the model when building systems. Selective loading is not a security boundary.

## E15 — Free-text matching can defeat otherwise relevant routing

Source: Tantaroudas et al., [Tool-calling retrieval versus vector RAG](https://arxiv.org/html/2610.08205v1), October 6, 2026; accessed October 8. Inspected methods, normalization ablations, results and limitations.

Type: preprint; 198 record-derived questions, 148 answerable test items in 79 clusters, one Greek–English corpus and Haiku 4.5. Literal matching failed on generated language/script variants; normalization recovered some losses, while vector/full-context controls performed better. The tool system is reconstructed; batch contamination prompted post-hoc isolated regeneration, and residual inflation cannot be excluded. Each query was answered once; raw materials require author access. This supports a local diagnostic, not a universal backend ranking. Implication: test real user forms and inspect generated query arguments on misses; preserve exact-identifier semantics. E06 supplies broader alternatives.

## E16 — Layered memory has direct but bounded empirical support

Source: Fu et al., [APDMem](https://arxiv.org/html/2610.02472v1), October 1, 2026; accessed October 8. Inspected architecture, sections 4.1–4.4, cost accounting and ablation tables.

Type: preprint on 500 LongMemEval-S questions with GPT-4.1/mini, model judging and component ablations. It reports 87.8% accuracy for GPT-4.1 while drilling into roughly 8% of sessions. Many baseline scores come from prior work; bundled controller/hierarchy/synthesis choices and one benchmark limit transfer. Its cost comparison lacks baseline online costs and excludes the shared answer generator. Session selectivity is not total token savings. Implication: supports testing adaptive depth and retaining raw evidence, without requiring four layers; count preprocessing, lazy generation and answer costs. E06/E15 counterbalance extrapolation to other corpora.

## E17 — Deferred schemas remain registered with the API

Source: Anthropic, [Tool search documentation](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool), live documentation accessed October 8, 2026; no publication/revision date established. Inspected deferred loading, errors and caching sections.

Type: interface requirement. Complete tool definitions remain in the request; deferral changes model-visible context. This clarifies the lightweight-stub analogy in E13: do not translate it into incomplete API registration. Implication: verify registration separately from exposure and preserve the discovery tool. It establishes no cross-provider contract or performance gain.

## E18 — Additional eligibility gates can lose required evidence

Source: Wang et al., [The Right Memory in the Wrong Context](https://arxiv.org/html/2610.07309v1), October 5, 2026; accessed October 9. Inspected protocol, results and Appendix B.

Type: provisional preprint; 3,767 RHELM/MemOps queries, 72 verifier cases and separate controlled exposures. Trusted namespace selection helps, but text-based verification can reject required evidence. Scope labels are trusted; prohibited-status annotation agreement is weak, populations differ, and route-to-reader results are associational. Candidate counts do not establish latency savings. Implication: evaluate lost permitted evidence alongside improper exposure; retain unresolved status. This supports the existing permission boundary, not relaxing it or trusting model-inferred authorization.

## E19 — Loading and successful use are distinct evaluation stages

Source: Wang et al., [Agent Skill Evolution](https://arxiv.org/html/2610.04832v1), October 4, 2026; accessed October 9. Inspected sandbox protocol, on-demand results and threats to validity.

Type: provisional preprint; 80 tasks, 57 repositories, four sandbox agents. Revised instructions improve required actions in this selected set; on-demand loading retains only part of the upfront gain. Repositories use the newer commit, reads truncate bodies, repetition differs by model, and token-based compliance can reward repetition. Human artifact judgments carry the correctness claim; no universal benefit follows. Implication: existing metadata/discovery guidance remains appropriate; distinguish body selection, required action and final outcome in deployment evaluation. E10's broader task-resolution findings are not contradicted by this selected-rule study.

## E20 — Model-native selection is a candidate, not a universal routing rule

Source: Kinderman et al., [UNREAL](https://arxiv.org/html/2610.08463v1), October 6, 2026; accessed October 9. Inspected long-context results, limitations and Appendix D.

Type: provisional preprint using retrieval training on frozen-model representations. Sparse-evidence benchmarks favor selection in tested settings; Wikipedia training, random distractor construction and additional indexing costs limit transfer. Efficiency experiments use random weights/token IDs on an H100, separately from answer-quality experiments. They do not establish joint production quality and speed. Implication: retain selective/full-context comparisons and full-cost accounting; no backend requirement, universal break-even length or new operational rule is warranted. E06 addresses different tasks and retrieval configurations.

## E21 — Skill overhead includes induced work

Source: Dong et al., [Agent Skills Can Be Harmful](https://arxiv.org/html/2608.11888v1), August 12, 2026, v1; accessed October 10. Inspected study design, subjects, failure taxonomy and validity discussion.

Type: provisional preprint using paired skill configurations on SkillsBench and SWE-Skills-Bench, with manual attribution. Selected regression cases implicate excessive procedures as well as loaded text. Ambiguous cases are excluded; subjective attribution and benchmark/harness dependence preclude prevalence or universal causal claims. Implication: existing total-work measurement and task-specific guidance remain appropriate. This does not justify removing necessary checks; no additional rule adopted.

## E22 — Long-context failure is task and scaffold dependent

Source: [How Agent Skills Fail under Long Contexts](https://arxiv.org/html/2607.17937v1), July 20, 2026, v1; accessed October 10. Inspected workspace construction, checker design, boundary probes and validity discussion.

Type: bounded preprint case study with 24 artifact checks and ten valid runs per principal condition. Concrete checklists help the main case, but other task/model probes do not consistently degrade. Character-matched contexts differ beyond length; pilot-driven sample extension, infrastructure exclusions and sparse replications limit inference. Implication: existing workload-specific evaluation and requirement-preservation guidance stand. No universal context threshold or mandatory checklist follows.

## Evidence to behavior

The following rules are synthesis unless marked interface requirement. Tests refer to cases in the evaluation file; passing a case is not general validation.

| Condition → action | Support/type | Applicability and counterweight | Observable test |
|---|---|---|---|
| Small universal procedure → keep upfront | E03/E09; engineering inference | Avoid overhead; E10 cautions against redundant instructions | C, matched latency if claiming speed |
| Conditional procedures → meaningful descriptions and cohesive references | E05 interface; E03/E19 engineering | Selection and successful use differ | A, links and reads; installed discovery remains untested |
| Global obligation → shared entrypoint; conditional prerequisite → explicit pre-action route | Engineering requirement-preservation choice, E03/E14 | Disclosure must not alter semantics/permissions | A/B, missing-prerequisite checks |
| Ambiguous or cross-domain query → allow multiple candidates and expansion | E06/E07; inference | Exclusive routing loses recall | B, required-source coverage |
| Empty or incomplete retrieval → diagnose, broaden, or full-source fallback | E06/E08; inference | Absence of results is not evidence of absence | B/D, failure-state reporting |
| Global/exhaustive question → coverage plan rather than top-k completeness claim | E06; inference | Full context itself has E02/E04 limits | B, enumerate known source set |
| Deferred tool selected → load schema before invocation | E11 interface pattern | Host protocol differs | B, trace/schema correctness |
| External content selected → keep authority and access boundaries | E14/E18 plus host requirements | Additional gates can also exclude permitted evidence | B/I, exposure and evidence-preservation checks |
| Long task/compaction → retain source handles and completed actions | E03/E13; inference | Re-reading may be necessary after change | E, no duplicated side effect |
| Efficiency claim → matched quality and total-cost evaluation | E02/E06/E09/E10/E12/E13/E21; synthesis | Tokens alone confound results | Comparative protocol |
| Multilingual free-text misses → inspect generated arguments and test supported normalization/fallback | E15; conditional inference | Exact identifiers and ambiguous matches require preservation checks | F, authored diagnostic review; runtime untested |
| Claude deferred tools → retain complete API registration | E17; interface requirement | Other hosts may differ | G, contract review; live API untested |
| Layered-memory efficiency claim → include construction and all generation stages | E16; accounting inference | Session fraction is not a billing metric | H, authored accounting review |

October 10 review: E21–E22 provide additional bounded counterevidence; operational guidance and conclusions remain unchanged.

## Open questions and refresh triggers

No identified controlled study establishes a universal end-to-end benefit for the entire progressive-disclosure pattern across current coding agents, skill catalogs, RAG and tool discovery. Direct evidence is strongest for particular failure mechanisms and interfaces; transfer of the whole design is conditional.

Refresh affected claims when the target model/harness changes, a catalog grows enough to change selection, source permissions or versions change, new missed-prerequisite traces appear, or a matched benchmark contradicts the current choice. Revisit E10 when citing older summaries; use v3 statistical interpretation. No automatic schedule or installation is implied.
