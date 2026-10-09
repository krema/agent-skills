# Progressive context disclosure: research synthesis

Reviewed October 7, 2026. This report accompanies a practical design/refactoring skill. Source appraisal, versions, search scope and rule mapping are in [the evidence ledger](evidence.md).

Updated October 8: the overlap search adds two October preprints and clarifies a deferred-tool API contract. APDMem supplies direct evidence for one layered-memory implementation, with incomplete comparative online-cost accounting. The Greek–English retrieval study motivates testing user spelling and script variants, not universally preferring one retriever. Claude's current API documentation distinguishes full schema registration from deferred model exposure. E07 now reflects Pre-Route v2's cost analysis. See E15–E17 and E07 in the ledger for limitations and sources.

## Finding

Progressive context disclosure is a useful architecture when an agent's possible information needs exceed what a particular task requires. Its advantage depends on finding the right information reliably and cheaply enough. Treat it as a context-selection strategy with explicit recovery, not a guarantee that small prompts outperform large ones.

The pattern makes an information space navigable: expose enough metadata to choose a source, load the relevant procedure or evidence, check whether it covers the decision, and expand when needed. Thoughtworks places it within context engineering and connects it to RAG and skills. That is a practitioner recommendation, distinct from a controlled demonstration. [Thoughtworks](https://www.thoughtworks.com/en-de/radar/techniques/context-loading)

## What the evidence supports

There are three separate questions: whether irrelevant context can hurt, whether an agent can select the needed context, and whether the whole system becomes better after paying selection costs. Evidence for the first does not settle the other two.

Chroma's focused-history results use known relevant material, so they approximate a best-case selection step. They motivate relevance filtering but do not measure the cost or error rate of an autonomous selector. Lost in the Middle also demonstrates a failure mode rather than validating a complete routing architecture. [Chroma](https://www.trychroma.com/research/context-rot), [Liu et al.](https://arxiv.org/html/2307.03172v3)

Retrieval can discard necessary evidence. Full-context processing and hybrid routing outperform the tested RAG baseline in Li et al.; the newer Pre-Route work explores deciding from metadata before answering. These results favor testing alternatives rather than hard-coding “always retrieve less.” [Li et al.](https://arxiv.org/html/2407.16833v2), [Chen et al.](https://arxiv.org/html/2605.10235v1)

Instruction bloat is not merely a word-count problem. Redundancy, conflicting scope, and unnecessary activities can matter. The latest AGENTS.md study does not establish that shorter files causally improve success. Its results also differ from the efficiency-focused study linked by Thoughtworks because their tasks and endpoints differ. Retain useful constraints and compare outcomes. [Gloaguen et al., v3](https://arxiv.org/html/2602.11988v3), [Lulla et al.](https://arxiv.org/html/2601.20404v1)

## Choose a loading strategy

The table below is an engineering synthesis, not a benchmark ranking.

| Situation | Useful starting design | Main risk to test |
|---|---|---|
| Short procedure relevant to every task | Direct upfront loading | Redundancy or hidden ambiguity |
| Many independent specialist procedures | Metadata → selected guide → conditional references | Missed or misleading triggers |
| Narrow factual question over a large corpus | Retrieval with source/scope metadata | Missed evidence, decontextualized chunks |
| Multi-step or cross-domain question | Multiple routes and iterative retrieval | Premature domain exclusion |
| Global comparison or exhaustive list | Coverage plan, broader/full sources where feasible | False completeness, synthesis errors |
| Many rarely used tools | Supported deferred schema discovery | Wrong capability or arguments |
| Long-running task | Disclosure plus state retention and supported compaction | Lost decisions or repeated actions |

Layering is valuable only if an agent can traverse it. “More information is in the docs” is a weak route. “Before changing stored schemas, read the migration guide; it identifies rollback and backup prerequisites” makes the dependency visible at the relevant decision. This example is an author-designed pattern; it needs testing in the target environment.

## Distinguish related techniques

- **RAG** retrieves external evidence. Progressive disclosure can also select instructions, schemas and examples; RAG can operate without an explicit domain-discovery phase.
- **Prompt compression** changes the representation of information. Disclosure changes when it is selected and loaded. Either can lose decisive details.
- **Compaction** replaces or removes accumulated history through host support. Reading fewer new files does not remove already-loaded text.
- **Prompt caching** reuses computation for stable input. Cached material still participates in the logical context, so caching and relevance selection are complementary. [API documentation](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- **Delegation** partitions work across agents. It is optional and introduces coordination cost; the technique does not require extra agents.
- **Access control** governs which data/actions are allowed. Neither a router nor selected content can grant access or override governing instructions. [InjecAgent](https://arxiv.org/html/2403.02691v3)

## Design around the failure paths

An overly narrow description prevents activation; an overly broad one recreates bloat. Exclusive routing can omit a second domain. Chunk boundaries can remove an exception or table header. A stale index can hide a newer rule. A missing tool schema can cause guessed arguments. Excessive fragmentation can turn a simple task into many slow reads. A summary can drop completed-action state and cause duplicate execution.

The package therefore proposes an explicit recovery ladder: inspect the identified gap, expand the local unit, search another candidate or domain, and process the full relevant source where feasible. If evidence remains inaccessible, report the bounded result and unresolved dependency. Do not equate absence of retrieved evidence with evidence of absence. These are engineering inferences from the reviewed failure mechanisms, not empirically optimal universal steps.

## Operational economics

A useful accounting model is:

**Total work = initial context + discovery + loaded context + reasoning/output + recovery.**

This is an accounting aid, not a latency formula: caching, parallel calls and provider billing make the relationship non-linear. Measure wall time and actual billed categories. A tiny router that repeatedly misses can cost more than a larger stable prompt. Rebuilding an early tool list can also spoil cache reuse in some implementations. [Claude Code engineering report](https://claude.dev/blog/lessons-from-building-claude-code-prompt-caching-is-everything/)

## What counts as success

Test the complete path from user request to final artifact, including which resources were read and which requirements were omitted. Preserve required correctness, source coverage and authorization first; then compare cost and latency. Structural validity establishes that a package can be opened. Behavioral trials establish that particular requests can be followed. Only matched repeated evaluations support claims of improved effectiveness or reliability.

No universal token cap, hierarchy depth, confidence threshold or top-k is established by this review. The appropriate boundary depends on the task, information distribution, host behavior and model. The accompanying skill makes those choices explicit and testable.

## October 9 evidence refresh

E18 qualifies filter evaluation; E19 reinforces the distinction between discovery and successful use; E20 adds a model-native alternative with separate efficiency and quality experiments. These bounded results support targeted evaluation rather than additional universal loading rules.
