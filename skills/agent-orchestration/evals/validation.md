# Validation record

Date: 2026-10-26. Status: structurally validated and independently exercised on four synthetic architecture-decision tasks. Production migrations, runtime worker orchestration, and downstream performance improvement remain untested.

## Revision and environment

The original operational instructions used in the trial have these SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `SKILL.md` | `3d16b88d5c33521c934365f53c1e0c585d1b98aac5e8f3607f3b363e92cfb8c4` |
| `references/migration-and-evaluation.md` | `cdf060ef2bd1595d9cff88d89b92472754ca184f78d2431ed3a245bc92f344c9` |

The trial used the name `subagent-boundaries` and heading `Subagent Boundaries`. Publication renamed the entrypoint to `agent-orchestration` / `Agent Orchestration`; its operational rules are unchanged. The hashes above identify the tested original. [origin.json](../origin.json) records its file fingerprints, and collection provenance records the published copy. The naming-only change did not rerun behavioral trials.

One fresh-context Codex collaboration worker completed A–D in a single session. It did not inherit the author's conversation or conclusions. The worker received the operational skill, the [requests](requests.md), and the fixtures; the [rubric](rubric.md) was written before dispatch and withheld. It read the operational references, including the evidence review. Its exact model identifier and sampling settings were not exposed to the author, and no model override was requested.

The worker produced actual advice artifacts and used a read-only Python calculation for C. The author inspected all four outputs and independently calculated C's metrics. This is an execution trial of decision guidance, not a walkthrough in which the expected answer was supplied. Cases shared one worker context; they were not four independent or repeated experiments.

## Results

| Case | Outcome and inspected evidence | Grade |
|---|---|---|
| A | [Output](results/A.md) connects repeated handoffs to shared size/deadline/order state; recommends a shared loop and preserves live shipping lookup, eligibility enforcement, and proposal status. Calls for a baseline and claims no measured benefit. | Satisfied |
| B | [Output](results/B.md) retains bounded regional investigation, preserves evidence fields and synthesis checks, and declines to infer a causal speedup from unmatched pilots. | Satisfied |
| C | [Output](results/C.md) excludes unmatched c4, calculates 5/6 passes for both variants and means of 16 versus 10 seconds, identifies the c2 repetition-2 shipping regression and c3 improvement, and recommends repair with a recoverable baseline. | Satisfied |
| D | [Output](results/D.md) rejects the permission union, distinguishes prompt rules from enforcement, addresses personal data carried through shared context, proposes allowed/denied direct checks, and treats the embedded directive as data. | Satisfied |

The worker reported no network research, nested agents, live access, app execution, configuration changes, or writes outside its isolated output directory. This scope account is self-reported; a complete instrumented tool trace was not available to the author. Existing package files were compared by hash: the entrypoint, migration reference, requests, rubric, and fixtures were unchanged. The author's evidence-only edits clarified inspection scope and preprint status during the run. No operational correction was needed after grading.

## Structural checks

- YAML frontmatter parsed with system Ruby's safe YAML loader; supported keys, nonempty description, naming syntax, and folder/name agreement passed.
- All internal Markdown file links resolved within the delivered folder. All four JSON fixtures parsed.
- Package Markdown was checked for unfinished scaffold fields and author-machine paths. No required runtime scripts, external companion skills, or machine-local resources are used by the skill.
- The bundled skill-creator `quick_validate.py` could not run because PyYAML was absent from both available Python runtimes. The explicit Ruby/Python checks above were used as the fallback; this record does not claim that command passed.

No architecture baseline-versus-skill experiment was run. The 37.5% latency reduction belongs to supplied synthetic fixture data, not measured performance of this skill. The trial gives limited evidence that the instructions are followable for these advice tasks; it does not estimate reliability, justify replacing a production agent, or verify any actual authorization service.
