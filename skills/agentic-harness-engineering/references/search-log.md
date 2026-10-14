# Research scope and selection

**Source access: 2026-10-13. Generalized skill and English edition: 2026-10-14.** The question concerns methods that let agentic development harnesses control execution reliably, enforce rules, verify functional results, and resume long-running tasks. Local project preferences and code-audit findings were not converted into general skill obligations.

The research is a targeted narrative synthesis with original-source tracing, version checks, and counterevidence. It is not a preregistered systematic review. Search snippets and third-party summaries aided discovery; they did not replace the stated inspection depth. The catalog counts only documents actually inspected through abstracts/metadata or relevant passages.

## Search families

| Family | Terms and title variants | Sources |
|---|---|---|
| Development agents and interfaces | SWE-agent, Agentless, SWE-Search, CodeAct, OpenHands, AutoCodeRover | P01–P04, P45, P58–P59 |
| Rules and guarantees | runtime enforcement, AgentSpec, FORGE/PCAS, AgentC, VIGIL, Progent, CaMeL, enforceable security policies | P17–P19, P31–P39, P44, P46–P49 |
| Quality and oracles | instruction following, constrained decoding, JSONSchemaBench, external critique, EvalPlus, DSPy Assertions | P06–P09, P20–P25, P40–P41, P68, P72 |
| Planning and decomposition | LLMCompiler, ADaPT, LATS, LLM+P, PlanBench, LLM-Modulo | P54–P56, P62–P65 |
| Continuity and context | long-running agent harness, context engineering, OpenHands SDK, workflow memory, AGENTS.md, AgentOccam | P22, P51, P57, P66, P69; runtime/engineering documents |
| Evaluation and counterevidence | tau-bench/pass^k, Harness-Bench, MTAC-IFBench, long software tasks, agent failures, infrastructure noise | P10–P16, P27–P30, P42–P43, P67 |
| Harness learning and portable policy | HarnessFix, MemoHarness, AFlow, Meta-Harness, Natural-Language Agent Harnesses, Self-Healing Harness | P35, P52–P53, P70, P74–P75 |
| Taxonomies and reporting | agent harness engineering survey, Control Agency Runtime, HarnessCard | S01–S04 |

The first research pass covered 65 documents; a later literature-focused pass added 30. The skill derives general decision conditions from these sources. No new effectiveness measurements or source access on 2026-10-14 are claimed. The search families are a summary, not a complete request log.

Important method inspections concern monitor assumptions, oracle coverage, replay/retry contracts, empirical comparison conditions, and generalization. A result involving one model or platform applies to the documented version, not automatically to current APIs or every other model.

## Versions and contradictions

AGENTS.md **2602.11988v3** uses CTXbench and different conclusion wording from earlier versions. FORGE **2602.16708v3** must be distinguished from earlier PCAS versions. HarnessFix **2606.06324v2**, NLAH **2603.25723v2**, and OpenHands SDK **2511.03690v2** are pinned in the catalog.

For Harness-Bench, the paper version covered 106 tasks, eight categories, and 5,194 traces; website figures differed. OpenHands SDK reports a maximum crash-recovery latency in its table that conflicts with a text claim. P32 has a documented date anomaly and supports no central skill rule. S02 is an unversioned author PDF without a reliably established publication date. The skill's creation date does not resolve these limits.

## Access and coverage

OpenReview pages for S01/S02 displayed a browser challenge. S02 was available as a public author PDF; S01 was inspected through journal metadata and abstract. The [MDPI page for ReliHarness](https://www.mdpi.com/2079-9292/15/18/4166) remained inaccessible through the web tool and was excluded from the 95 sources.

Selection favors public, predominantly English-language sources and software/terminal tasks. Proprietary implementations, every traditional textbook, and every recent study are not fully covered. Surveys support orientation; their reference lists were not counted as independently read full texts. Research stopped when material decisions had support or remaining uncertainty was explicit.
