# Validation record

Revision: 1.0, 2026-10-07. This record separates package checks, author walkthroughs, isolated executions and unmeasured effectiveness.

## Structural checks

The initial seven Markdown files were checked for name/folder agreement, required metadata, valid lowercase hyphenated name, description length, local reference existence, paths remaining within the package, unfinished TODO markers, and machine-specific paths. All seven initial local links resolved. The entrypoint contains 665 whitespace-delimited words; this is descriptive, not a quality threshold or tokenizer measurement.

The host's quick_validate.py was attempted but could not start because its Python environment lacks PyYAML. No dependency was installed. A direct check of this package's restricted two-field, plain-string frontmatter and the structural invariants above passed. This does not claim execution of the official validator. There are no runtime scripts or external runtime dependencies in the skill.

Final distribution check: 11 Markdown files, 11 resolving internal Markdown links, no symlinks or machine-specific paths, and one top-level skill folder in the ZIP. Archive CRC, temporary extraction, link rechecks and byte-for-byte comparison with the source folder passed. Exact synthetic trial inputs are included; trial scratch and raw machine-specific action logs are excluded. External research URLs were accessed during review, not exhaustively rechecked during packaging.

## Author walkthroughs, not execution trials

| Case | Inspected decision path | Review result |
|---|---|---|
| C: small universal procedure | Establish the decision → direct loading unless a demonstrated problem justifies indirection | Supports declining arbitrary five-level fragmentation while addressing speed |
| D: unavailable guide | Sufficiency gap → expand/search → bounded result when unavailable | Does not permit fabricated prerequisites or infer no rules from no hit |
| E: compaction continuation | Retain completed actions and source locators; retrieval reference warns against reexecution | Supports checking the saved result before any repeat action |

These are author reasoning checks with the expected answers visible. They do not demonstrate a fresh agent taking the expected actions. Missing-guide runtime recovery and actual compaction continuation remain behaviorally untested.

## Isolated execution trials

Two fresh-context Codex subagents received the skill, a realistic request and the exact raw fixtures. They inherited the session's model configuration; no independent provider model-build identifier was recorded. They were instructed not to read this evaluation directory, other trials, or live services. The grading criteria were written before their runs and withheld. Both were explicitly given the skill, so automatic skill selection from its description was not tested.

The trials executed this skill's intended work: generating a refactored instruction set and a concrete RAG design. They did not execute the downstream migrations, exports, retrieval service or payment tools described in those designs. The parent inspected the generated artifacts against the original fixtures and outcome rubrics, rather than treating worker success reports as evidence by themselves.

| Trial | Actual resource path | Produced artifacts and parent findings | Result |
|---|---|---|---|
| A: instruction refactor | SKILL.md → instruction-design.md + three input files | Shared instructions, UI guide, stylesheet guide, database guide, billing guide and requirement map. Global local-only/tenant/authorization constraints preserved. Migration backup/rollback and invoice retention dependency remain discoverable. Aggregate-only exception preserved. All nine output Markdown links resolve. | Passed this artifact-generation trial |
| B: support RAG design | SKILL.md → retrieval-design.md + corpus | Concrete catalog, retrieval/recovery contracts, four worked traces, comparison plan and action log. Account-only route widens to billing; active B1 loads B2 despite lower ranking; archived B0 is excluded for current policy. Exact-code recovery, complete-inventory scope and schema loading are explicit. Injected approval is rejected. | Passed this design-generation trial |

Selected observed outputs:

- A's database guide directs an invoice migration to billing guidance before retention decisions. Its billing guide retains the explicit anonymized-analytics exception and does not reinterpret it as permission to delete stored invoice IDs.
- B concludes that the ten-day-old prepaid promotion is excluded from the ordinary refund policy, while preserving the duplicate-charge correction exception. It loads no payment schema for an explanation-only request.
- B's TS-999 draft explains an out-of-scope billing reference without identifying the other tenant. Its exhaustive answer is explicitly bounded to the supplied complete fixture.
- B compares direct, bundled and deferred loading with cache, retrieval, failure and latency costs; it does not claim measured savings.

Workers' own marker/preservation assertions and authored routing sequences were reviewed as structural checks and walkthroughs, not counted as extra behavioral trials. The parent found no demonstrated defect requiring a change to the operational skill. Evaluation records and exact-input links were completed afterward; operational instructions and references remained the tested revision.

## Effectiveness limits

No matched baseline comparison, repeated reliability study, production deployment, real retrieval engine, live tool call, prompt-cache benchmark or downstream task-success study was run. Published experiments were assessed but not reproduced. No performance improvement percentage is claimed for this package. Installation and automatic discovery in an installed host were not tested.

## Evidence refresh — 2026-10-08

The entrypoint and original fixtures remain unchanged. The October 7 isolated executions above are historical and were not rerun. This refresh changes conditional retrieval guidance, one host API contract clarification, cost accounting, and their evidence/synthesis records.

Author walkthroughs F–H were performed after their rubrics were written, with the expected outcomes visible. These are decision-path reviews, not independent execution trials:

| Probe | Reviewed response path | Outcome and limit |
|---|---|---|
| F | Inspect generated free-text arguments and matching; test language variants and supported fallback; keep AB-1 and AB1 distinct; leave ambiguous transliteration unresolved | Guidance supports the rubric; no retrieval backend was run |
| G | Read the current host contract; retain complete request schemas while deferring model exposure | Guidance rejects name-only registration; no live API call was made |
| H | Reject the session-count-to-total-cost inference; request matched construction, controller, lazy-generation, answer and cache accounting | Guidance supports full accounting; no cost benchmark was run |

Packaging was rechecked after these edits: restricted two-field frontmatter, name/folder agreement, internal links, package containment, absence of symlinks, unfinished markers and machine-specific paths, ZIP CRC, temporary extraction and byte-for-byte package equality. The official validator remains unexecuted because of the previously recorded missing PyYAML dependency. Detailed check counts and changed-file hashes are recorded outside the package in the dated research log and package manifest. No performance improvement is claimed.

## Evidence refresh — 2026-10-09

The entrypoint, fixtures and instruction-design reference remain unchanged. Historical execution trials were not rerun. New evidence E18–E20 qualifies evaluation and records alternatives; it does not establish improved package performance.

Probe I was written before an author walkthrough with its rubric visible. Reviewed response: reject the improvement claim based on zero forbidden exposure alone; record the permitted historical source that was lost; verify historical applicability; retain unknown permission as unresolved and seek authorized recovery. This preserves the existing permission boundary while assessing false exclusion. Result: the decision path satisfies the rubric in author review, not an independent agent execution. No retrieval backend, authorization service, installed-skill discovery or performance comparison was run.

Structural checks passed: restricted two-field metadata and folder/name agreement, internal Markdown links and containment, no symlinks or machine-specific paths, no unfinished line-leading markers, and no added runtime dependencies. ZIP CRC, exact member list, temporary extraction, extracted links and byte equality passed; the external SHA-256 manifest was regenerated and checked. The official validator was not rerun; its missing-PyYAML limitation remains recorded above.
