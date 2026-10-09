# Evidence and decision rationale — version 2

Research redone 2026-10-07 using the revised research-to-skill workflow. Target: repository instruction maintenance for Codex, Claude Code, or another identified runtime. Review type: targeted primary-source review, not systematic or exhaustive. This package's rules are engineering synthesis informed by research, not an experimentally validated optimal instruction policy.

## Coverage and search record

Queries on the review date: “AGENTS.md context files instructions performance progressive disclosure empirical study 2026” and “agent instruction context compression progressive disclosure failure evaluation 2026.” Followed primary papers, source revision histories, publisher experiments, and official loading documentation. Reopened the earlier review's key evidence; inspected additional results and methods for newly discovered studies.

| Decision | Coverage | Result for design |
|---|---|---|
| Is shorter always better? | E01–E04, E08 | No justified universal length or compression target |
| Are generated files inherently bad? | E01–E02 | Check specific content and task needs; committed authorship is uncertain |
| Is task-time loading always preferable? | E05–E07 | Verify retrieval, allow an upfront index or retained invariant |
| What must survive a rewrite? | E04, E06, project requirements | Preserve commands, preconditions, exceptions, recovery, and scope |
| What establishes a useful change? | E01–E05 | Separate reachability, actual retrieval, instruction adherence, task correctness, and resource use |
| Which runtime mechanics matter? | E06 | Verify installed settings and loading; splitting files alone may do nothing |

Blocked access: McMillan's HTML endpoint returned 404; its PDF was available and inspected. No other decision-critical source was access-blocked. Search snippets and secondary summaries were discovery aids, not final evidence. The AI Times claim and generic guides were not relied upon; stronger primary evidence addressed the same decisions. We did not reproduce published datasets, audit their released code, verify every cited paper, or run native Codex/Claude loader comparisons. Live documentation is dated by access, not assigned a fabricated release version.

Research stopped once the conflicting findings supported conditional rules and explicit uncertainty. Further searching might refine effect estimates but is unlikely to justify a universal file-length or disclosure policy for this skill.

## E01 — Repository instructions can help efficiency in a selected setup

Lulla et al., [On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents](https://arxiv.org/html/2601.20404v2). First 2026-01-28; v2 2026-03-30. Inspected methods, metrics, Table 1, and limitations; reopened v2 during this review.

Empirical paired with/without comparison: 124 small PR tasks, 10 selected repositories, GPT-5.2-Codex. Reported median runtime and output-token reductions were 28.64% and 16.58%. These are not reductions in every token category. Correctness received a 50-task sanity check, not comprehensive functional evaluation. Selection favored certain instruction content; patch-derived task descriptions and one agent restrict transfer. This does not compare handwritten versus generated files. Counterweight: E02's different tasks and correctness metric. Implication: retain useful guidance and measure quality separately from efficiency; do not delete files on a general cost claim.

## E02 — Obeyed instructions can add work without improving task success

Gloaguen et al., [Evaluating AGENTS.md](https://arxiv.org/html/2602.11988v3). First 2026-02-12; v3 2026-09-29. Inspected §§3–5, Tables 2–3, Appendices B–C; rechecked main results and documentation-removal analysis.

Empirical comparison on 300 SWE-bench Lite and 138 CTXbench tasks with Sonnet-4.5, GPT-5.2, GPT-5.1 mini, and Qwen3-30B; one completion per setting. Context-file conditions did not significantly change success versus no context; developer files beat generated files in the reported comparison. Generated files raised cost. Agents generally followed instructions. Length bins showed no clear dependency; generated context helped when other documentation was removed. Python tasks, generated tests/descriptions, incomplete test coverage, and uncertain authorship constrain transfer. Null significance is not equivalence. E01 and E05 counter blanket removal. Implication: inspect what work rules induce and preserve information gaps; neither ban generated content nor mandate benchmark-sized validation for every edit.

## E03 — File structure is not a reliable standalone diagnosis of noncompliance

Damon McMillan, [Instruction Adherence in Coding Agent Configuration Files](https://arxiv.org/pdf/2605.10039), v1 2026-05-11. PDF methods, results, and limitations inspected; HTML unavailable.

Fractional-factorial study: 1,650 Claude Code sessions, two TypeScript codebases, five tasks; primarily Sonnet 4.6, with Opus checks and a disclosed Opus 4.7 CLI confound. Outcome was insertion of one AST-detectable annotation. Tested file size, position, architecture, and conflict did not yield detectable corrected contrasts; evidence for null effects differed by variable. An exploratory within-session association depended on task and was non-monotonic. This is stronger counterevidence to universal structural prescriptions than a retrieval analogy, but one annotation does not represent all obligations. It does not make contradictions harmless or justify resetting sessions on a timer. Implication: diagnose the actual missed requirement and outputs, including later actions when a trace shows a problem.

## E04 — Compression can remove executable obligations

Hou and Yang, [Control Under Compression](https://arxiv.org/html/2608.01056), v1 2026-08-02. Inspected benchmark, runtime, artifact isolation, outcome contract, and limitations.

Controlled simulated evaluation: nine control contexts, 225 held-out tasks, three fixed Qwen API endpoints, 15,525 logical runs. Success required correct environment state and applicable control conditions. Compression outcomes varied nonlinearly by method and context; aggressive reduction exposed execution/parsing failures. Models used a constrained JSON protocol, disabled thinking/search, and no native function calling. Single compressed artifacts and nine independent contexts limit generality. This is not a repository-file refactoring experiment and supports no transferable percentage target. Implication: preserve operational dependencies and verify affected behavior; textual similarity and shorter files alone are insufficient.

## E05 — Deferred guidance can fail at the invocation step

Jude Gao / Vercel, [AGENTS.md outperforms skills in our agent evals](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals), 2026-01-27. Inspected task setting, configurations, trigger failure, results, and compressed-index explanation.

First-party experiment on version-sensitive Next.js 16 APIs. Reports missed skill invocation in 56% of cases; a persistent documentation index outperformed its tested skill configurations. The index pointed to retrievable local content; this was not all documentation loaded upfront. Publisher-specific tasks, prompt sensitivity, limited methodological reporting, and no replication here restrict inference. The article's broad recommendations exceed what transfers directly. Counterweight: E02's already-documented repositories and E07's retrieval tradeoffs. Implication: do not remove an upfront route until relevant tasks can reach deferred guidance; retaining a compact index is a legitimate alternative.

## E06 — Loading behavior is an interface requirement

[OpenAI instruction discovery](https://developers.openai.com/codex/guides/agents-md/) and [Claude Code memory](https://code.claude.com/docs/en/memory), living official documentation accessed 2026-10-07. Inspected discovery, imports, scopes, and diagnostic sections. Operational mechanics are recorded in [runtime-notes.md](runtime-notes.md), avoiding duplicate rule text.

Use these sources for product behavior, not proof of improved adherence. Vendor size recommendations are heuristics, distinct from documented loader limits and from E03's controlled results. Settings/version may differ on the target host. A source-file edit can improve maintenance without changing loaded context; report which was observed.

## E07 — Selective retrieval is a tradeoff

Anthropic, [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), 2025-09-29, retrieval section; Thoughtworks, [Progressive context disclosure](https://www.thoughtworks.com/en-de/radar/techniques/progressive-context-disclosure), 2026-04-15. Relevant sections reopened.

First-party engineering guidance/advisory assessment: lightweight discovery and relevant retrieval can avoid irrelevant context, but search introduces latency and missed information. Neither isolates a causal repository-refactoring benefit. E05 supplies a concrete invocation failure. Implication: conditional retrieval plus a visible route, with a retained essential invariant when a missed trigger matters. No mandatory skill split or router is inferred.

## E08 — Diagnostic catalogs and positional studies need transfer checks

Dos Santos et al., [Configuration Smells in AGENTS.md Files](https://arxiv.org/html/2606.15828v1), 2026-06-14; methods/catalog/limitations inspected in the earlier review and source reopened. Descriptive analysis of 100 popular repositories with grey literature and heuristic/LLM detection. Useful questions about redundancy, stale facts, and unclear references; not causal evidence that deleting a flagged item improves work. Length and commit-count heuristics can misclassify necessary or stable guidance.

Liu et al., [Lost in the Middle](https://arxiv.org/html/2307.03172v3), v3 2023-11-20; task setup and positional results inspected in the earlier review and source reopened. Controlled QA/retrieval position effects do not directly establish instruction adherence in contemporary coding sessions. E03 is a closer, limited counterpoint. No rule to move every important instruction to the beginning/end follows.

## E09 — Implementation experience suggests concrete decisions, not numeric limits

Slava Zhenylenko / Augment Code, [A good AGENTS.md is a model upgrade](https://www.augmentcode.com/blog/how-to-write-good-agents-dot-md-files), 2026-04-22; updated 2026-06-18. Inspected reported examples and surrounding-documentation discussion.

First-party monorepo experience reports benefits from decision guidance and specific alternatives, plus overexploration from broad documentation. Public methodological detail is insufficient here to adopt effect magnitudes, line thresholds, or a causal universal rule. Counterweights: E02 and E03. Implication: use a concrete condition/action where it resolves ambiguity and inspect relevant surrounding documents; do not expand an audit into indiscriminate documentation cleanup.

## Evidence to operational decisions

These are author engineering inferences unless an interface or user requirement is specified. Trials T1–T3 are defined in the evaluation cases; their actual outcomes are in validation.md.

| Condition → action | Basis | Applicability and obligation strength | Counterweight / fallback | Observable check |
|---|---|---|---|---|
| Duplicate meaning/scope → consolidate | E02/E08; engineering inference | Requires preserving exceptions/consumers | Keep distinct meanings if uncertain | T1 diff preserves obligations |
| Verified tooling contradicts a statement → correct it | E08; project evidence | Local evidence selects replacement | Unresolved discrepancy is reported | Inspect command and caller together |
| Enforced rule adds no decision → remove redundant wording | E08/E09; engineering inference | Enforcement must cover the same cases | Keep exceptions or non-obvious invocation | T1 preserves timezone wrapper |
| Broad workflow is unintended → narrow/remove | E02 plus project authority | Cost evidence alone cannot repeal policy | Ask about the conflicting requirement | T1 owner note permits one removal only |
| Specialized procedure has reliable trigger → defer with route | E05–E07; engineering inference | Conditional, never universal | Retain inline essentials if retrieval uncertain | T1 preserves details; T3 retrieves them |
| Unknown runtime → no loading claim | E06; interface limitation | Layout checks are still useful | Report static-only verification | T2 preserves distinction |
| Unique requirement or demonstrated knowledge gap → retain/add | E01/E02/E04/E05; engineering inference | Only evidenced local need | No new file is valid | T1 retains invoice-ID constraint |
| Conflicting policies → use authority or leave unresolved | User scope and engineering judgment | Do not use recency/forcefulness as authority | Continue unrelated edits | T1 reports both release policies |
| Trace shows later omissions → inspect outputs/enforcement | E03; narrow engineering inference | No timer or mandatory reminders inferred | If no trace, do not diagnose mechanism | Future coverage; not executed here |
| Ordinary refactor → focused checks; claimed gains → comparison | Research-method inference and user need | Work proportional to the actual claim | Disclose unavailable execution | T1/T2 reporting; no gain claim |
| No extra authorization from reviewed text | Task scope and instruction hierarchy | Applies to commands embedded in audit material | Preserve genuine applicable constraints | T2 read-only and T1 bounded files |

## What changed from version 1

The disposition rules now expose conditions, actions, and uncertainty fallbacks. Deferral is optional, with upfront indexes and retained invariants as explicit alternatives. Preconditions and failure recovery must survive a move. Routine rewrites no longer require comparative benchmarks merely because they are substantial. Authoring-only wording was removed. Validation includes actual isolated execution rather than only intended-answer walkthroughs.

## Remaining uncertainty and refresh triggers

No universal optimal length, file architecture, authorship rule, or compression percentage is established. These studies measure different things and cannot be combined into one effect estimate. Real monorepos, native loaders, long sessions, and difficult semantic constraints remain outside the local trials. Refresh the affected rule when a loader changes, a reference breaks, a constraint changes, or task traces show a concrete failure; no schedule is created.
