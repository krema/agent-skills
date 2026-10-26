# Evidence for subagent boundary decisions

Reviewed 2026-10-26. Intended use: portable architecture advice, orchestration audits, and local migrations for tool-using agents, including Codex. The package does not depend on Claude commands or Anthropic's kit. The original instructions and evaluation fixtures are newly written; upstream code and prompts are not bundled.

This was a targeted, decision-led review, not a systematic review. Confidence is stronger in testing boundaries against task outcomes than in predicting which architecture will win for a new application. Most deployment evidence below comes from one vendor and is not independent replication.

## Coverage and search record

The starting article was read through its substantive sections, and its links to deployment comparisons, prior boundary guidance, and the migration kit were followed. All sources below were accessed on the review date.

| Decision | Search or inspection performed | Coverage result |
|---|---|---|
| When should shared context win? | Starting article; linked commerce comparison; January architecture guidance | Concrete mechanisms and deployment reports; missing controlled enterprise datasets |
| When do multiple agents help? | Web query `site.anthropic.com engineering multi-agent research system 90.2 15 times tokens`; original report | Useful opposing deployment experience; model/compute confounds |
| Does task structure moderate effects? | Web query `single agent multi agent empirical scaling principles coordination 2025 2026 arxiv`; latest paper's methods, results, and limitations | Controlled benchmark comparisons with material statistical limits |
| What fails at boundaries? | Web query `multi agent systems failure 14 failure modes MAST arxiv 2025`; latest methods and examples | Failure taxonomy; not an architecture-treatment experiment |
| How should a migration be checked? | Original kit README and `skill/steps/03-fold.md`; commerce evaluation sections | Concrete implementation experience, including admitted testing gaps |
| What can be assumed about isolation? | Current Claude Code documentation: context, permissions, and main-loop choice | Product-specific behavior; no basis for assuming identical Codex semantics |

Non-primary search hits were discovery aids only. The initially opened v2 papers were superseded by v3 after checking arXiv version histories. No inaccessible decision-critical source remained. The review did not reproduce upstream benchmarks, audit the entire kit, or search every agent framework.

## E01 — Folding is a candidate for coupled workflows

- Source: Diane Sarkis, [When to fold subagents into your main agent loop](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop), 2026-10-22; failure modes, progressive disclosure, migration sections inspected.
- Type: first-party engineering guidance and deployment observations. Reports shared-context benefits and one roughly twofold runtime improvement; does not publish a controlled sample, variance, or complete evaluation data.
- Implication: test folding coupled specialists; do not promise the reported speedup or assume every planner/router is redundant. E03 and E04 establish reasons to retain multiple contexts. Transfer confidence: plausible mechanism, uncertain application effect.

## E02 — Conversational coupling and enforcement are separate concerns

- Source: Ali Shazal and Matthew Koen, [The anatomy of effective commerce agents](https://claude.com/resources/articles/the-anatomy-of-effective-commerce-agents), 2026-09-02; architecture, enforcement, and evaluation sections inspected.
- Type: first-party deployment report and implementation recommendations. Shared cart/history motivate a common conversation; hard restrictions are enforced outside model instructions. Outcome and neighboring-capability cases detect failures missed by narrow domain scores.
- Limits: customer identities, comparative datasets, and causal controls are unavailable. Commerce's action-approval model is not a universal requirement for other domains.
- Implication: preserve effective restrictions during consolidation and check combined capabilities. This does not require approval of every reversible local edit.

## E03 — Independent research can benefit from separate contexts

- Source: Anthropic Engineering, [How we built our multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system), 2025-06-13; benefits, delegation, and evaluation sections inspected.
- Type: first-party production experience. An Opus 4 lead with Sonnet 4 workers reportedly exceeded single-agent Opus 4 on an internal research evaluation by 90.2%. Broad independent searches were a favorable case; dependent shared-context work was less favorable.
- Limits: different model composition and resource use confound architecture; task samples and uncertainty are not fully disclosed. The reported 15× token figure compares multi-agent runs with chats, not with single-agent runs.
- Implication: retain parallel exploration as a real alternative and include all worker usage in cost. Neither percentage transfers to this skill.

## E04 — Task structure changes the observed benefit

- Source: Yubin Kim et al., [Towards a Science of Scaling Agent Systems, v3](https://arxiv.org/html/2512.08296v3), 2026-04-08; architecture definitions, §4.1–4.2, robustness, limitations, and evaluation appendices inspected.
- Type: controlled benchmark preprint: 260 configurations, six benchmarks, three model families; standardized tools, prompts, and compute. Reported relative effects range from +80.8% in decomposable finance to −70% in sequential planning. This qualifies both universal single-agent and universal multi-agent claims.
- Limits: 50–100 tasks for four benchmarks, 20 each for coding/terminal subsets with wide intervals; prompts were not optimized per architecture. Several predictors lose significance under six-cluster robust inference. The v3 predictive fit is weaker than v2.
- Implication: use matched local comparisons. The empirical ~45% baseline threshold and tool-count relationships are not portable routing cutoffs; trace-level error amplification is not a task failure-rate multiplier.

## E05 — A verifier or handoff can itself fail

- Source: Mert Cemri et al., [Why Do Multi-Agent LLM Systems Fail?, v3](https://arxiv.org/html/2503.13657v3), 2025-10-26; §3 methods, taxonomy discussion, and failure examples inspected.
- Type: qualitative taxonomy developed from 150 traces examined by six experts, then expanded with model annotation to 1,642 traces. Human agreement reached κ=0.88; three categories cover design, coordination, and verification.
- Limits: selected systems and tasks, partially model-generated labels, older models, and overlapping causes. Agreement on labels does not establish causal prevalence or prove that deleting agents fixes failures.
- Implication: inspect actual artifacts and consequential evidence. A dedicated verifier's confidence is insufficient; retain verification that checks task requirements, regardless of topology.

## E06 — Separate contexts are an interface property, not automatic isolation

- Source: [Claude Code subagent documentation](https://code.claude.com/docs/en/sub-agents), live documentation without a page-wide revision date; main-conversation choice, tool filters, permissions, and context inheritance inspected.
- Type: authoritative product interface description. Subagents have distinct contexts; available tools, inherited settings, and context vary by mode and version.
- Limits: documentation specifies product behavior, not comparative effectiveness. These details cannot be transferred to Codex without checking Codex's actual tools and permissions.
- Implication: verify effective access before moving a boundary. Use runtime controls for restrictions and pass needed information explicitly when it is not inherited.

## E07 — Migration tooling supports testing, with narrow real-world validation

- Source: Anthropic, [single-agent-loop-kit](https://github.com/anthropics/single-agent-loop-kit/tree/c43796287b83bec847db923f07131d1cc8de750d), commit `c43796287b83bec847db923f07131d1cc8de750d`, 2026-10-21. README and [fold procedure](https://github.com/anthropics/single-agent-loop-kit/blob/c43796287b83bec847db923f07131d1cc8de750d/skill/steps/03-fold.md) inspected through the GitHub connector; commit metadata checked.
- Type: reference implementation and limited execution experience. The README discloses two real-model example runs and untested migration steps; offline stand-ins check plumbing rather than model quality.
- Implication: keep a recoverable baseline, inspect changed neighboring behavior, and exercise moved restrictions directly. The kit's fixed check-ins, dependencies, and sample sizes are not requirements here. No kit script was executed or copied.

## E08 — Context, parallelism, and specialization are hypotheses to test

- Source: Cara Phillips et al., [Building multi-agent systems: When and how to use them](https://claude.com/resources/articles/building-multi-agent-systems-when-and-how-to-use-them), 2026-01-23; context protection, verification, and decision sections inspected.
- Type: first-party engineering guidance. Gives context isolation, independent work, and persistent specialization failures as reasons for separate agents; warns that verifiers can stop after superficial checks.
- Limits: no controlled comparison supporting universal boundaries; illustrative code and thresholds are not production guarantees. E02 shows that specialization need not require a different agent.
- Implication: decompose by information needs, test the claimed benefit, and avoid fixed agent counts or mandatory reviewer loops.

## Evidence to behavior

These are engineering inferences unless marked as interface requirements. E01 motivated the research topic; that source selection does not establish an architecture preference.

| Decision | Basis | Applicability, counterweight, and check |
|---|---|---|
| Inspect information dependencies before choosing a boundary | E01, E03, E08 | For audits and design; missing traces leave a hypothesis. A readable boundary map must explain both retained and removed context separation. |
| Compare shared-loop procedures, direct tools, and bounded workers | E02, E03, E04 | These are alternatives, not a fixed ladder. Check task outcomes rather than agent count. |
| Give retained workers evidence-bearing contracts | E03, E05; engineering synthesis | Useful where information crosses a boundary. Check completeness and actual returned artifacts; permit task-specific result shapes. |
| Preserve effective restrictions and user's scope | E02, E06; interface requirement plus session authorization | Applies to access-changing migrations; test denied and allowed calls. If isolation cannot be retained, keep that boundary. |
| Use matched variants and investigate regressions | E04, E07 | Needed for causal improvement claims; unmatched or thin samples require qualified conclusions. |
| Preserve obligations, recover baseline, stop on a violated requirement | E05, E07; engineering synthesis | Applies to implementation, not every ordinary request. Success requires preserved task acceptance criteria, not merely a better average. |

## Open questions and refresh triggers

Local efficacy remains unknown until this skill is used on the target application's traces and task suite. Audit-decision trials do not validate a migrated production system. Refresh affected rules when the host's context or permission behavior changes, new controlled work materially contradicts the task-structure hypothesis, or local regressions reveal missing boundary conditions. No automatic schedule is created.
