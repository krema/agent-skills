# Evidence: stateful source-grounded reasoning

Initial review 12 October 2026; targeted refreshes 13 and 16 October 2026. Intended use: a general Codex-style agent answering multi-document and large-corpus questions with ordinary search, read, notes, and computation tools. Target outcome: fewer missed corrections, unsupported claims, and unnecessary follow-up searches. This is a targeted review of the user-supplied paper and decision-relevant primary sources, not a systematic review. No independent replication or test of this *skill* was located or performed.

## Research coverage

| Decision | Search/inspection scope (12–16 October 2026) | Result |
|---|---|---|
| Whether separate evidence and conclusion states help | LongHarness v1 method, Tables 1–3 and 9, Appendices B–E; search for official implementation | The authors report gains and ablation losses in their harness. A targeted search did not locate an official LongHarness code release. Transfer to a text skill is untested. |
| Whether source links and revisions are sufficient | LongHarness state contract and controller limits; OfficeQA Pro failure analysis | Source-reference validation does not ensure faithful extraction, correct operands, or correct parsing. |
| When a simpler path may work | ReContext methods/results/limitations; LedgerMind dispatcher and limitations; Lost in the Middle abstract | Other methods improve evidence use without the same persistent state. Extra reasoning can hurt simple tasks in another setting. |
| Benchmark transfer | OfficeQA Pro source paper and repository; LongHarness setup | The principal corpus is historical Treasury documents with numerical answers and revisable tables; direct-model and harness interfaces differ. |
| Selection bias and search coverage | 13 October: primary Search Shapes Conclusions v1 methods, results, and public-agent adapter; overlap searches from 11 October | E07 supports a scoped coverage safeguard as engineering inference. |
| Repeated records | 16 October: Memory Echo v1 method, setup, ablations, failure cases, limitations; repository README | E08 qualifies handling of repeated source material. |

## E01 — Coupled evidence and conclusion state helped in the reported harness

- Source: Huang et al., [LongHarness](https://arxiv.org/html/2610.13075v1), Sections 2–3, Tables 1–2, Appendix D.
- Dates/version: arXiv v1, 9 October 2026; inspected 12 October 2026.
- Inspection: Method, setup, ablations, repeated-run results, state contract, and case study.
- Type and design: Author-run benchmark comparison using OfficeQA Pro V1 (133 questions) and V2 (90), AA-LCR (100), and LongBench v2 Long (108). Two model backbones; main comparison one run per setting, with three GLM-5.3-Flash runs in Appendix D.
- Finding: GLM-5.3-Flash LongHarness exact match is 60.2% on OfficeQA Pro V1 and 61.1% on V2 in the main run. Removing conclusion coevolution yields 54.9% and 51.7%; append-only evidence yields 56.4% and 51.1%. These are component comparisons inside the same harness.
- Quality and limits: Moderately useful evidence for the *combined harness*, especially its ablations and repeated GLM runs. It is an author evaluation without independent replication here. Direct reasoning uses BM25-selected context in a 256K window; LongHarness has interactive access and state, so the direct comparison does not isolate the state mechanism. The exact percentages cannot be promised for another model or a prose skill.
- Counterevidence/alternatives: E04–E05. No matched trial isolates a simple skill implementation from the actual LongHarness controller.
- Skill implication: Use a lightweight separation of observed evidence, inferred conclusions, and open gaps for multi-step corpus work; do not claim the paper's gains for this package.

## E02 — Provenance checks still leave semantic and numeric failure modes

- Source: [LongHarness](https://arxiv.org/html/2610.13075v1), Sections 2.3–2.4 and Appendix B.2–B.3.
- Dates/version: v1, 9 October 2026; inspected 12 October 2026.
- Inspection: Full relevant method and state contract.
- Type and design: Interface specification for the paper's runtime.
- Finding: The controller verifies registered source references and active IDs, while the policy judges whether a statement faithfully represents its passage. The compute operation does not verify that literal operands match cited values. Superseding evidence does not automatically rewrite dependent conclusions.
- Quality and limits: Strong support for what that implementation validates; no independent guarantee of factual correctness.
- Counterevidence/alternatives: A strict external parser or verifier could automate some checks in another environment; this skill cannot assume one exists.
- Skill implication: Inspect source text, check numeric operands, and revisit dependent conclusions after corrections. These are engineering adaptations of explicit runtime gaps, not measured improvements of this skill.

## E03 — The benchmark has revision, parsing, and analytical hazards

- Source: Opsahl-Ong et al., [OfficeQA Pro](https://arxiv.org/html/2603.08655), Sections 2, 3, and 5; [benchmark repository](https://github.com/databricks/officeqa).
- Dates/version: arXiv v1, 9 March 2026; repository inspected 12 October 2026.
- Inspection: Dataset creation, evaluation, agent baselines, and failure-mode sections; repository README on corpus representations.
- Type and design: Benchmark source and author analyses.
- Finding: The corpus contains historical tables with preliminary and later revised values. The authors describe errors from parsing tables and scans, interpreting units, and numerical analysis. In their own agent evaluations, better parsed documents change accuracy substantially. Their Pro subset was selected partly by removing questions two development-time agents both answered correctly.
- Quality and limits: Directly relevant to the benchmark's hazards; it cannot establish their frequency in other corpora. Public questions and answers plus benchmark-specific construction limit generalization.
- Counterevidence/alternatives: Clean structured corpora may have much lower extraction risk; simple prose questions may need no ledger.
- Skill implication: Preserve period, units, revision status, and source representation; inspect originals for ambiguous extracted data when available. Do not mandate the same depth for every query.

## E04 — Evidence replay is a distinct alternative

- Source: Zhao et al., [ReContext](https://arxiv.org/html/2607.02509), method, results, and limitations.
- Dates/version: arXiv paper first posted 2 July 2026; inspected 12 October 2026.
- Inspection: Method summary, reported benchmark results, and limitations.
- Type and design: Author evaluation on long-context tasks using model-internal relevance signals and evidence replay, without external persistent memory.
- Finding: The authors report improved aggregate long-context performance across three open backbones, with exceptions on individual metrics. Their method requires internal relevance signals and adds latency, limiting direct use with closed APIs.
- Quality and limits: Supports an alternative evidence-use mechanism for supplied contexts, not a direct comparison of this skill with LongHarness on identical tools and tasks.
- Counterevidence/alternatives: E01 demonstrates benefits of persistent state within the tested corpus harness.
- Skill implication: If the answer is in a manageable inspected passage, re-reading and citing it can be sufficient; persistent records are conditional on task complexity.

## E05 — Extra reasoning depth can hurt easy questions in another setting

- Source: Du et al., [LedgerMind](https://arxiv.org/html/2607.28374), adaptive dispatcher ablation and limitations.
- Dates/version: arXiv paper first posted 30 July 2026; inspected 12 October 2026.
- Inspection: Dispatcher method, ablation discussion, limitations.
- Type and design: Author-run multimodal visual QA experiments with a structured evidence runtime.
- Finding: In their ablation, forcing every query through the full path lowers easy-question accuracy while hard-question performance is largely unchanged. Authors note evaluation on static image/text QA and leave long-horizon transfer open.
- Quality and limits: Different domain and implementation; only directional support for avoiding unnecessary process on simple questions.
- Counterevidence/alternatives: Complex, dispersed evidence may justify more explicit state (E01).
- Skill implication: Use the complete loop when source acquisition and reconciliation are material; answer a one-passage question directly.

## E06 — Long context alone may not guarantee access to relevant evidence

- Source: Liu et al., [Lost in the Middle](https://aclanthology.org/2024.tacl-1.9/), TACL 2024 abstract.
- Dates/version: 2024 publication; inspected 12 October 2026.
- Inspection: Publisher abstract only.
- Type and design: Empirical position-sensitivity study on multi-document QA and key-value retrieval.
- Finding: Reported performance degrades when relevant information appears in the middle of long input contexts for models they evaluated.
- Quality and limits: Abstract-level inspection only; older models and tasks. Does not prove that an external ledger is the best remedy for current agents.
- Counterevidence/alternatives: E04 uses evidence replay; more capable models may differ.
- Skill implication: Do not assume merely placing all documents in context ensures they will be used; inspect and surface decisive passages.

## E07 — Source support and search coverage are different checks

- Source: Xiao et al., [Search Shapes Conclusions](https://arxiv.org/html/2609.39026v1), Sections 2–4 and Appendices A, D.
- Version: v1, 30 September 2026; newly inspected 13 October 2026.
- Design: Author experiments on 200 MS2 questions with Qwen2.5-32B and OLMo3-7B, plus 36 PERSPECTRUM tasks using a modified public agent.
- Finding: Read-document estimates depend on search selection; their correction uses logged acquisition probabilities and a defined candidate pool.
- Limits: Pool-average evidence scores are not scientific truth; the controlled search adapter differs from unrestricted web search. No independent replication inspected.
- Implication: The coverage check is an engineering adaptation, not an implementation of CESS or a demonstrated remedy.

## E08 — Repeated records require source ancestry

- Source: Li et al., [Memory Echo](https://arxiv.org/html/2610.17763v1), Sections 3–6, limitations; [repository](https://github.com/OrcasSam/memory-echo-benchmark).
- Version: v1, 13 October 2026; inspected 16 October.
- Design: Author-controlled replay, 190 questions, four memory frameworks, two generators, model grading.
- Finding and counterweight: Repeated descendants can compete with corrections. Family filtering alone lowered accuracy; missing replacement evidence also harmed performance.
- Limits: Supplied provenance labels, frozen pools, answer-processing effects, no independent human audit. The repository excludes datasets/results; not reproduced here.
- Implication: Linking repeated summaries is an engineering adaptation. It does not justify deleting useful history or trusting unverified corrections.

## Evidence to behavior

| Condition and action | Basis | Applicability and inference | Counterweight / fallback | Check |
|---|---|---|---|---|
| Multi-document retrieval or revision risk → keep distinct evidence, conclusions, and open gaps | E01, E02 | Adaptation from a full harness, not direct empirical proof for a prose skill | For one inspected passage, answer directly (E04–E05) | Each material conclusion traces to active evidence; gaps drive next search |
| Search hit found → read actual passage before admission | E02, E03 | Engineering safeguard because IDs alone do not validate semantics | If unreadable, mark unverified | Every established fact has a revisitable source locator |
| New source contradicts old value → supersede/retract and recompute dependencies | E01–E03 | Matches paper lifecycle and benchmark revision hazards | Preserve genuine period/definition conflicts rather than assuming later is correct | Final operands cite active entries; old values absent from final computation |
| Remaining gap could change answer → search for that gap; stop when it cannot materially change decision within constraints | E01 | Paper ablation supports conclusion-guided search in its harness; transfer is inferred | Budget/access limits lead to qualified answer | Search has a stated purpose; unresolved material gaps are reported |
| Numerical or parsed evidence → verify units, source value, and formula | E02–E03 | Engineering inference from known validation and parsing failures | If original unavailable, state extraction uncertainty | Formula can be recomputed from cited active operands |
| Overall-evidence question → inspect opposing findings and relevant source groups | E07 | Engineering inference; source fidelity does not establish coverage | Qualify incomplete coverage; no statistical guarantee | Case 5 author walkthrough; behavior untested |
| Repeated source records → preserve ancestry | E08 | Engineering adaptation | Keep useful details | Case 6 author walkthrough; behavior untested |

## Open questions and refresh triggers

No independent skill-level performance test was run. An official code release was not located in the targeted search. The paper describes a prompt template and state contract, but this package does not reproduce its controller. Revisit the rules if code, independent replication, newer ablations, or matched trials of text-only skill adaptations become available. A change in the target agent's source-reading or persistent-state tools also warrants retesting.
