# Evidence: context rot and agent context management

Reviewed through 2026-10-09. Intended environment: file- and tool-using assistants, particularly Codex research and coding workflows. Research window: 2026-01-01 through 2026-10-09. Twenty primary sources were examined for relevant methods, results, and limitations. E01–E16 were appraised on October 7; E17–E19 on October 8. E20 and selected version checks were reviewed October 9.

This is an extensive targeted review, not a systematic review or meta-analysis. Sources are predominantly preprints; peer review and independent replication were not established. Results are author-reported, not reproduced here. Older datasets or models inside a new 2026 experiment are allowed; older experimental findings are not used as support. No particular current Codex model is validated by this synthesis.

## Eligibility and search record

The [Chroma report](https://www.trychroma.com/research/context-rot) is explicitly dated July 14, 2025. It is excluded from empirical support. A 2026 crawl date, conference label, citation, or website update does not make a 2025 result eligible. To avoid laundering old findings, this review favors first-submitted 2026 papers and a dated 2026 primary engineering report. Older related-work sections in eligible papers are not evidence entries.

Actual web query families used on 2026-10-07:

| Decision | Queries used | Coverage |
|---|---|---|
| Is length the cause? | `2026 context rot long context degradation study arxiv`; `2026 long context reasoning distractors length controlled study` | Controlled distractors, long search, transcript monitoring, competing horizon explanation |
| Does compression help? | `2026 context compression agent memory evaluation loss information benchmark`; `site.arxiv.org 2026 context compression negative results agent observation masking` | Compaction, trimming, active management, recovery costs |
| Do recent results change guidance? | `site.arxiv.org 2026 long context benchmark September context rot recovery`; `site.arxiv.org 2026 context rot October` | September boundary attribution and stale-state experiments; October acronym false positive excluded |
| Retrieval or full context? | `site.arxiv.org 2026 retrieval versus long context reasoning context management` | Retrieval/archival alternatives; no universal winner established |
| What fails after shortening? | `site.arxiv.org 2026 Lost in Compaction`; `site.arxiv.org 2026 Less Context, Better Agents` | Constraint loss and domain-specific enterprise benefit |

Search results and secondary indexes were discovery aids only. Relevant primary HTML sections were opened and searched; the failed HTML rendering of E06 was recovered using its primary PDF. Primary metadata pages were additionally checked for several date/title ambiguities. Methods and numerical tables were inspected where used below. Repositories, raw trajectories, and complete appendices were not independently audited. No citation-count inclusion quota was used.

## E01 — Long search can degrade; deletion is not sufficient recovery

Source: Xia et al., [Diagnosing and Mitigating Context Rot in Long-horizon Search](https://arxiv.org/html/2606.29718v1), v1, June 29, 2026; §§3–4, Tables 1–2. Empirical preprint; relevant setup, taxonomy, pruning findings and management comparisons inspected.

Four open models (GLM-4.7/5.0, Qwen3.5-397B-A17B, MiniMax-M2.5), three search benchmarks, five repetitions, 100-turn cap. Length-associated giving-up and uncertain stopping were tested through pruning. Removing all accumulated context reduced the designated rot outcomes but increased unfinished trajectories. Combined trimming/compaction and isolation had different cost and model tradeoffs.

Confidence: useful search-specific evidence; length correlations alone are confounded by task difficulty. Outcome taxonomy uses a model judge, with reported human agreement on 300 trajectories. Closed-model transfer is untested. E06 supplies a competing explanation in dependent tasks; E07 cautions about compression itself. Operational inference: investigate stalled search and preserve task state rather than wiping history or treating uncertainty as a defect.

Version refresh (October 9): [v2, August 4](https://arxiv.org/html/2606.29718v2) reframes the outcome as premature termination, reports difficulty-controlled correlations and model-dependent cost tradeoffs. Its abstract and relevant diagnosis/management passages were checked; this is not a complete version diff. The v1 appraisal above remains explicitly versioned. No instruction to suppress justified uncertainty or automatically parallelize follows.

## E02 — Distractors and length must be disentangled

Source: Gao, Chen and Huang, [The First Drop of Ink](https://arxiv.org/html/2605.10828v1), May 11, 2026, v1; §§3.1–3.2, 6–7, Figures 2, 8–9. The v1 HTML title says “Misleading”; abstract-page title says “Distracting.” Relevant experimental methods, filtering controls and negative intervention result inspected.

Four QA datasets, 200 examples per setting, controlled distractor proportions; displayed 128K results include Llama-3.1-8B, Qwen2.5-7B and Qwen3-Next-80B. Initial hard distractors caused disproportionate losses. Filtering comparisons on two smaller models suggested much recovery came from shortening; attention-temperature sharpening worsened results.

Confidence: informative controlled experiment, limited model/task transfer and model-judged answers. Filtering arms also differ in starting composition. The simplified attention account is not a universal causal proof. Operational inference: select task evidence while preserving coverage; measure rather than assume a filtering benefit. This does not justify deleting contrary evidence, changing API sampling temperature, or adopting the paper's context lengths as limits. E06/E11 show why task structure matters.

Version status checked October 10: [v2](https://arxiv.org/html/2605.10828v2), August 20, 2026, is available. Abstract and experimental setup inspected; no full version diff or new v2 result is claimed here. The appraisal above remains explicitly tied to v1.

## E03 — Active correction differs from passive summarization

Source: Yao et al., [ARC: Active and Reflection-driven Context Management](https://arxiv.org/html/2601.12030v1), January 17, 2026, v1; §§3.2–4.2, Table 1. Empirical method paper; architecture, training and comparison setup inspected.

ARC updates interaction memory and a checklist with triggered reorganization. Five information-seeking benchmarks compare ReAct/ReSum with several Qwen actors and DeepSeek-v3.2; a GPT-OSS-120B context manager is trained separately. Results favor the bundled active approach across reported actor settings, though individual metrics have exceptions.

Confidence: promising within the tested framework, not isolated evidence for a single reflection prompt. Training, representation, and management policy change together. E07 suggests targeted boundary repairs; E04 warns of overhead. Operational inference: when repetition or contradictions appear, revise incorrect working assumptions and next actions, not merely shorten prose. Do not claim that a Markdown skill reproduces ARC's trained architecture or require a second agent.

## E04 — Recoverable information can still cost extra interactions

Source: Shuyu Liu, [What Does Context Compression Cost an Agent?](https://arxiv.org/html/2608.16370v1), August 17, 2026, v1; §§3–4.6. Empirical preprint; operator comparisons, oracle intervention, statistical protocol and null results inspected.

Controlled task environment, 24-turn horizon, full/fact-preserving/sliding context and restored-state conditions. DeepSeek-v4-flash, Qwen3.7-plus and GPT-5.5; 100 task observations per main model/condition with paired seeds. Sliding history raises retrieval cost in most corrected comparisons even when completion changes are not detected. Restoring dropped state reduces reacquisition.

Confidence: causal probe within a synthetic budgeted environment; interaction counts are not dollars or latency. No detected completion difference is not equivalence. Retention-choice nulls and budget interactions limit simple “keep the most important atoms” claims. E11/E14 provide beneficial compression settings. Operational inference: preserve execution state and evaluate retrieval burden alongside completion; archival recoverability alone is insufficient.

## E05 — External memory offers recovery, with infrastructure and training costs

Source: Li et al., [ACM: Agentic Context Management for Long Horizon Tasks](https://arxiv.org/html/2607.23809v1), July 26, 2026, v1; Table 1, §§5–6, Table 3. Framework and empirical preprint; archival definition, benchmarks, training and ablation inspected.

ACM exposes editing/offload/query tools and trains management behavior. Evaluations cover BrowseComp-Plus, DeepSearchQA and SWE-Bench Verified, including a Qwen3.5-9B student. Ablations show management and distillation effects vary by task, and better completion does not always mean fewer tool calls or lower peak tokens.

Confidence: useful feasibility evidence, with framework/training transfer limits. “Lossless” denotes preserved raw content for retrieval, not guaranteed downstream use or zero retrieval cost (E04). Operational inference: use working summaries plus recoverable originals when tools support them; test access before depending on offloading. Do not invent memory APIs or promise trained-policy performance from ordinary file storage.

## E06 — Dependent-step failures can worsen with bounded history

Source: Shubhra Mittal, [How Fast Do Agents Rot?](https://arxiv.org/pdf/2609.01660), v1; submission history August 31, 2026; §§3–5, Table 2. HTML unavailable; primary PDF methods, results and limitations inspected.

Nine models, four synthetic task families, 10,664 trajectories, exact simulator scoring. Paired natural, compressed and single-turn padded regimes probe alternative explanations. Bounded history performs worse in the reported streaming comparison. Agentic chain-following also degrades with horizon.

Confidence: a useful counterexample, not a general decay law. Models include older systems; synthetic tasks and incomplete longest-horizon collection restrict transfer. Compression changes available state, so it does not cleanly isolate token length. The prose about near-ceiling short-task performance conflicts with some Table 2 values; projected benchmark reliability is not adopted. E01/E11 support benefits in different tasks. Operational inference: retain necessary dependencies and test the actual task rather than assuming shortening fixes long-horizon errors.

## E07 — Evaluate the compression event, not just the final outcome

Source: Min et al., [Adapting Context Compression for Long-Horizon Agents with Counterfactual Continuations](https://arxiv.org/html/2609.36526v1), September 29, 2026; §§3–5, Appendix A. Empirical preprint; boundary design, samples, metrics, baseline matching and limitations inspected.

AppWorld, OfficeBench and tau2 retail experiments compare compressed methods and full history. A diagnostic study uses 90 training tasks and three runs; boundary analysis uses 197 events and nine continuations per condition. Reported recovery overhead is common while severe outcome harm concentrates at fewer events. PAIR adapts prompt sections using matched continuations.

Confidence: stronger local attribution than unrelated whole-run comparisons, but expensive, recent and task-specific. Offline adaptation needs restorable environments; stochastic uncertainty remains. Operational inference: check state at a compaction boundary and repair demonstrated omissions; for improvement claims use matched, repeated sandbox continuations. Never replay real irreversible actions merely to test compression. E04 supports measuring recovery cost; no universal threshold follows.

## E08 — Retention and correct use of updated state are distinct

Source: Guo et al., [When Context Changes: Understanding Update Failures in LLMs](https://arxiv.org/html/2609.38866v1), September 30, 2026; §§3–4, Table 1, Appendices F.1–F.5. Controlled benchmark/mechanistic preprint; update construction, matched wording/placement tests, interventions and positive controls inspected.

Tests separate current values, obsolete mentions and other variables; mechanisms are probed in small open models. Revised-constraint decisions are often correct for stronger reasoning models, while dependent operational histories are harder. Explicitly historical wording reduces some errors but is not uniformly effective.

Confidence: supports state-selection failure in tested settings, not a universal attention explanation. Original wording and mention counts partly confound initial contrasts; follow-up controls matter. Operational inference: track provenance, scope and actual update order; a late mention of old data is not a new assignment. A state record is an engineering response, not the paper's internal attention intervention. E13 concerns a different, external source of staleness.

## E09 — Long transcript review needs its own evaluation

Source: Martin and Roger, [Classifier Context Rot](https://arxiv.org/html/2605.12366v1), May 12, 2026; §§3–5, Figures 2–6. Controlled monitoring preprint; data construction, models, metrics and mitigation limits inspected.

80 benign coding transcripts and 148 short MonitorBench transcripts are used in insertion/padding experiments with Opus 4.6, GPT-5.4 Thinking and Gemini 3.1 Pro. Long inputs increase misses. Incremental monitoring helps; reminders improve obvious inserted-attack detection but not subtle MonitorBench cases. More reasoning is model/task dependent.

Confidence: strong within controlled monitor stress tests, with synthetic padding and narrow attack-family limitations. It does not establish that reminders cure general agent reasoning. Operational inference for authorized review tasks: retain exact action evidence and evaluate intermediate as well as final review opportunities; measure false positives and misses. No automatic monitoring installation or message sending is authorized by this evidence.

## E10 — Temporal anchors deserve explicit preservation when relevant

Source: [The Sleeping Agent: What Gist-Based Context Compression Loses and Why](https://arxiv.org/html/2608.11775v1), August 12, 2026, v1; §§5–7, Tables 1–3. Empirical preprint; matched coverage, models, results and limitations inspected.

Ten LoCoMo conversations, 1,935 matched text questions; primary aggregate excludes adversarial questions (1,501). Sonnet 4.6 answers; Haiku 4.5 compresses/judges. Temporal protection improves temporal-question accuracy over generic gist by 0.314, with reported paired 95% interval [0.254, 0.375].

Confidence: useful targeted result; only ten conversation clusters, model grading and a restricted full-context comparison. Preservation counts are verbatim proxies. Scheduling was not testable on this offline benchmark; open-domain intervals overlap. Operational inference: keep relevant dates and relative-time anchors rather than relying on gist. Do not claim equivalent benefits for all memory methods, or prescribe idle-time consolidation from these results.

## E11 — Selective retention can improve enterprise tool workflows

Source: Lodha et al., [Less Context, Better Agents](https://arxiv.org/html/2606.10209v1), June 8, 2026, v1; §§3.3–4.9, Tables 2–5. Empirical preprint; policy, matched configurations, results and failure taxonomy inspected.

Fifty hotel-expense tasks in D365 F&O, five runs, GPT-5. With the same simulated user, complete itemization rises from 71.0% with full history to 91.6% with recent interactions plus summary. Reported tokens fall 62.7%. The 8% no-user result is not a context-policy baseline: it changes another component.

Confidence: useful domain evidence with repeat runs and limited second-model/generalization checks; not independent replication or a coding benchmark. Recency pruning fits verbose, superseded form state. E06 provides a counterexample for dependent histories, and E12 cautions about omitted constraints. Operational inference: consider selective whole-interaction retention and summary, but do not universalize the study's five-pair window or the measured improvement.

## E12 — Session constraints can disappear during compaction

Source: Wang et al., [Lost in Compaction: Evaluating Side-Constraint Loss under Context Compaction](https://arxiv.org/html/2608.11242v1), v1; primary metadata reports July 31, 2026 submission despite August identifier. §§4–5, Table 2, Appendices C–D. Construction, retention/compliance metrics, model/prompt differences and robustness excerpts inspected.

CompInt crosses constraint types/framing/location with chat, agent and research contexts: 750 instances per condition. Reported retention varies sharply across compactors and prompts; an accompanying constraint extractor improves retention. GPT-5.4-mini tests differ in length/trial count from open-model conditions.

Confidence: compelling failure-mode evidence, not a universal loss rate. Retention relies on model judgments, with limited human validation; MCQ compliance differs from live action safety despite supplementary checks. Operational inference: preserve current constraints distinctly and verify their effect after compaction, including revocation and scope. A manual record is not a reproduced implementation of the extractor. E07 motivates boundary-specific testing.

## E13 — Repository-context staleness is a separate problem

Source: Treude and Baltes, [Context Rot in AI-Assisted Software Development](https://arxiv.org/html/2606.09090v1), June 8, 2026, v1; §3, Tables 1–3. Preliminary observational study/roadmap; sampling, two-snapshot detection and manual inspection read.

356 repositories, 612 configuration files; an existing reference checker flags stale elements in 23.0% of repositories. Only 32 of 50 manually inspected flags are genuine referential staleness. The detector also misses references introduced after the first snapshot.

Confidence: supports existence and checkability of outdated references, not a precise prevalence of harmful instructions or evidence of model attention decay. Operational inference: verify consequential paths, symbols and commands against the current checkout when contradictions arise; preserve normative instructions while correcting factual assumptions. E08 concerns stale selection inside a model's context, not obsolete source files. Neither justifies ignoring all project instructions.

## E14 — First-party compaction experience supports external evidence storage

Source: SentinelLABS, [Compaction & Agent Memory for Automated Malware Analysis](https://www.sentinelone.com/labs/context-engineering-compaction-agent-memory-for-automated-malware-analysis/), updated July 2, 2026. Engineering report; workflow, storage split, metrics and result discussion read.

Their binary-analysis harness compares native compaction against no compaction using reference analyses. It reports approximately 86% fewer input tokens and effectively unchanged aggregate quality, with exact artifacts retained in durable storage and working state condensed.

Confidence: practical implementation experience, weaker than a fully specified controlled study; inspected reporting does not provide enough sample/variance detail to establish equivalence or generalize the percentage. No OpenAI interface requirement is inferred from this third-party report. E04 cautions that reacquisition can consume budget. Operational inference: keep exact evidence recoverable separately from working summaries, and verify actual task outcomes rather than extrapolating token savings.

## E15 — Preserve item-level dependencies that broad plans omit

Source: Dixit et al., [FOCUS: Training-Free Decision-Preserving Context Compression for LLM Agents](https://arxiv.org/html/2609.37590v1), September 29, 2026, v1. Sections 4–5 and Appendices A.5–A.10 inspected on 2026-10-07.

Empirical preprint: five agent benchmarks, GPT-4.1 main experiments, draft-model dependency estimates and defensive retention. AppWorld uses 168 test tasks. Reported benefits vary by task and draft model; draft overhead can offset token or cost savings. A failure analysis shows generalized batch plans overlooking individual entity records.

Confidence: useful operational failure evidence; limited independent replication, model coverage and repeated-run evidence in the inspected main setup. Predicted dependencies are not guaranteed causal necessity. Engineering implication: check proposed omissions for task-critical failures and item records; retain the complete batch set and progress. Do not mandate draft agents or adopt reported thresholds. E07 supports continuation checks; E04 requires accounting for recovery overhead.

## E16 — Reversible hiding requires a real restoration mechanism

Source: Chaturvedi et al., [DTOC: Dynamic Tool Output Compression](https://arxiv.org/html/2609.26121v1), v1 HTML dated August 6, 2026 despite September identifier; §§3–6 inspected on 2026-10-07. Both date representations fall within the requested year; no precise September publication claim is made.

Empirical framework study: six DeepSWE tasks, five models, DTOC on/off. The orchestrator stores original outputs under stable identifiers and exposes enable/disable controls. Results differ across models; reversible restoration is compared with disable-only variants.

Confidence: six tasks, timeout exclusions with unequal denominators, and framework-dependent behavior limit transfer. The abstract’s disable-only degradation claim conflicts with the improved success shown in Table 4; that claim is not adopted. Author-reported model capacities are not treated as interface documentation. Engineering implication: consider reversible output hiding only if the actual host exposes it, and check restoration before exact-detail use. A file summary cannot modify a hidden prompt. E05 supports archival recovery; E04 warns that retrieving archived data has costs.

## E17 — Context edits have cache costs

Source: Su et al., [ReFold](https://arxiv.org/html/2610.07863v1), October 6, 2026, v1; §§3–4 and Appendix A.4 inspected October 8.

Empirical preprint: mini-swe-agent, two Qwen3.6 models, vLLM prefix caching, 50 tasks from each of five coding/terminal benchmarks. Comparisons retain full history or summarize under pressure. Reversible rendering preserves raw history and batches edits. Main resolved counts differ by −1 to +3/50; seven configurations repeated twice show substantial task flips. This does not establish equivalence. A single-trajectory ablation links frequent edits to lower cache reuse; it cannot identify a universal interval. Cost estimates use hosted rates, not actual invoices.

Engineering implication: evaluate edits using cache-aware total resources and restoration, conditional on real host support. No particular schedule or reported savings is promised. E04 remains a recovery-cost counterweight.

## E18 — Editable live context is a harness capability

Source: Shao et al., [Context Language Models](https://arxiv.org/html/2609.37725v1), September 29, 2026; §§3–6 inspected October 8.

Empirical preprint: live context-file synchronization, with zero-shot comparisons against summary, ACM, Self-Compact and RLM on a shared harness. Coding and BrowseComp-Plus evaluations include Qwen3.6-27B at 32K; separate experiments train policies and implement suffix-cache reuse. Reported performance/compute advantages depend on task and configuration. The compute metric explicitly accounts for re-prefilling; this is not a bill or a validation of this Markdown skill. Synthetic ContextBench isolates management, limiting ecological transfer. Independent reproduction was not established.

Engineering implication: require actual synchronization before claiming a file edit changes live context; count rewrite costs. Existing host-boundary guidance stands. The study does not authorize arbitrary context edits or prove a universal benefit from removing harness constraints.

## E19 — Decomposition needs boundary and merge checks

Source: Sandlund, [Trained Agentic Context Management](https://arxiv.org/html/2610.02404v1), October 1, 2026; §§1, 3–4, Tables 1–2 inspected October 8.

Empirical preprint: synthetic supervised training of Qwen3.6-35B-A3B with chunk reads and recursive calls. RULER uses 65 questions per length; OOLONG-synth 30. Baselines differ in context limits and decoding. Aggregate performance hides declining common-word and state-tracking results; classification and merge errors compound. Costs are not formally quantified. Untrained harness use and a subsequent RL attempt produced negative results. Claims of broad parity are stronger than uniform table-level support.

Engineering implication: preserve item boundaries, single ownership and temporal order; inspect intermediate results before merging. This is an adaptation, not evidence that prompting reproduces training. No default recursion, 8K budget, or smaller-model substitution follows. Counterweight: decomposition can itself lose information; retain originals and evaluate the target task.

## E20 — History cues do not establish a safe trigger

Source: Pakhomov and Nijkamp, [Does an Agent’s History Tell You When Compaction Will Hurt?](https://arxiv.org/html/2610.08722v1), October 6, 2026; §§2–5 inspected October 9.

New analysis of 590 TRACE boundaries on AppWorld; one agent/compressor, tight window, task-held-out policies, short replay horizons. Recent-history prediction is weak; a prior-write label is phase-confounded. Count advantages over random selection do not consistently imply burden-mass advantages. Missing token counts prevent a matched token-budget comparison. Rebuilt-state variability and noisy replay labels limit conclusions. This reuses a corpus, not an independent replication of its underlying compaction experiment.

Engineering implication: evaluate trigger cues rather than hard-code them; compare frequency and magnitude of recovery costs. This does not establish that learned timing cannot work.

## Evidence to behavior

These are conditional engineering translations. Empirical support does not itself establish an agent's authorization or a runtime interface.

| Rule | Support / category | Applicability and counterweight | Observable check |
|---|---|---|---|
| Diagnose before shortening | E01, E06, E08, E13; inference | Several distinct causes; no universal rot detector | Missing evidence, stale state, logic error or overload identified, or uncertainty retained |
| Select next-decision evidence | E02, E11; inference | Preserve contradictions and multi-hop dependencies | Answer/action supported and required corpus covered |
| No fixed context threshold | E01, E06, E11; inference from heterogeneity | Runtime hard limits remain real; percentages are not reliability limits | Policy tested on target tasks rather than adopted from a benchmark |
| Correct mistaken working assumptions | E03; inference | Does not reproduce trained context manager | Repeated unproductive action changes for an evidence-based reason |
| Preserve exact state and constraints | E04, E08, E10, E12; inference | Keep only applicable data; preserve revocations | Current values, chronology and constraints survive continuation |
| Offload only with recoverability | E05, E14; inference | E04: retrieval costs; missing tools prohibit offload dependence | Locator opens and needed content is usable |
| Verify and repair after compaction | E07; inference | No irreversible replay; failure may be unrelated | Next action succeeds or a specific omission is repaired |
| Specialized transcript review | E09; inference | Not a universal reminder ritual | Exact actions support findings; misses/false positives measured |
| Verify stale code references | E13; inference | No blanket rejection of project instructions | Current file/symbol/command establishes factual state |
| Protect batch membership and omitted failure state | E15; inference | Broad future plans can miss individual dependencies | All required IDs and per-item statuses remain recoverable |
| Use reversible output hiding selectively | E16; inference | Requires actual host support; effects vary by model | Exact original restores from stable handle |
| Account for edit/cache costs | E17, E18; inference | Requires telemetry or explicit uncertainty; no fixed interval | Compare total resources at matched correctness |
| Check partition boundaries and merges | E19; inference | Trained synthetic policy does not transfer automatically | No omitted/duplicated boundary item; ordered state updates |
| Evaluate trigger cues | E20; inference | Narrow offline corpus; no universal failure predictor | Harm count and total burden at matched opportunities |
| Preserve authorization and host limits | User/task constraints; engineering | No paper grants tools or permissions | No invented compaction, delegation, installation or external action |

## Exclusions, gaps and refresh triggers

- Excluded Chroma 2025, pre-2026 NoLiMa/context-length findings, and ACON's 2025 origin from direct support. A later conference label alone was insufficient.
- Survey/index/Reddit/TMLS/playbook results were discovery or framing leads, not empirical foundations. Recycled older experiments were not admitted by a 2026 webpage date.
- Screened but not used for rules: Context-Length Robustness (2603.15723), Logic Haystacks, DISCO (2609.33485), Addressable Recall Compaction (2607.25066), and the SSRN MCP-attrition lead. These need separate full method/date appraisal; no conclusion here relies on their snippets.
- No general architectural cure, universal context budget, benefit from automatic delegation, or superiority of retrieval over full context was established. KV-cache quantization is a different intervention and was outside scope.
- Search coverage is English-language and indexed-web dependent; October coverage ends October 9 (early-morning screening). This is not all 2026 work. No fabricated screened-record count, preregistration or exhaustive-review claim is made.
- Research stopped when each operational decision had support plus counterweights; more method papers were unlikely to justify stronger unconditional rules. Remaining important uncertainty is target-agent effectiveness, best trigger timing, repeated-summary behavior, and long-horizon aggregate tasks.
- Refresh when the target model/harness changes, a retention failure appears, or replicated evidence changes a decision. Recheck exact paper versions, matching baselines and source dates. This is not an automatic update schedule.
