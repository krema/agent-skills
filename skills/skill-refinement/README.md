# skill-refinement

Version **3.0.0** — evidence refreshed 2026-10-07.

An evidence-informed skill for improving the **content** of agent-facing Markdown at any size. The agent reviews and rewrites instructions; the bundled Python helper performs structural checks only. There is no size gate, target length, automatic bloat score, or rule-density score.

## Use

Unzip the whole directory into a skill location supported by your agent, or ask the agent to read its SKILL.md directly. This archive does not install itself or update a scheduler.

> Use skill-refinement to optimize /path/to/AGENTS.md and /path/to/my-skill. Review their content regardless of size, apply justified edits, preserve required behavior, and report the evidence and checks behind material changes.

“Optimize”, “improve”, and “rewrite” request actual edits. “Audit only” requests findings and proposed edits without mutation. A sound result may be shorter, longer, reorganized, or unchanged, depending on what the tasks require.

Material edits distinguish verified project facts, observed task outcomes, research-supported hypotheses, and editorial judgment. The [decision matrix](references/decision-rules.md) connects guidance to supporting and contradictory research. The [evidence ledger](references/evidence.md) contains 30 dated entries with source quality and transfer limits; it is not all loaded for ordinary edits.

## Package and verification

- [SKILL.md](SKILL.md): workflow and conditional resource routes.
- [patterns](references/patterns.md): concrete rewrite choices when needed.
- [measurement](references/measurement.md): structural CLI, limits, and optional metrics.
- [evals/cases.md](evals/cases.md): 20 case rubrics, preparation, and matched behavioral evaluation protocol.
- [worked revisions](evals/worked-rewrites.md): concrete outputs with explicit self-review limitations.
- [VALIDATION.md](VALIDATION.md): what was actually checked and what remains unmeasured.

Python 3.10+ is needed only for local tooling; no external packages, API keys, or network are required. From this directory:

```sh
python3 scripts/analyze_skill.py /path/to/target --strict
python3 scripts/analyze_skill.py /path/to/target --json
python3 scripts/analyze_skill.py /path/to/target --metrics
python3 -B -m unittest discover -s evals -p 'test_*.py' -v
python3 -B evals/run_cases.py
python3 -B evals/run_cases.py --prepare /path/to/new-evaluation-inputs
```

The analyzer is read-only. It cannot decide content relevance or prove performance. JSON schema 2 keeps measurements opt-in and always marks content review as required. Static tests are separate from execution trials and performance comparisons. This release runs fresh-agent editing trials and selected downstream tasks; see VALIDATION.md for exact results and limits. No matched performance improvement is claimed.

## Upgrade and provenance

Replace the previous package directory with this complete version; do not overlay it and retain obsolete thresholds.md. The skill's identifier stays the same for compatibility. Version 2 removed the analyzer-first size framing. Version 3 makes consequential editing decisions more explicit, preserves unresolved conflicts, and scales validation to uncertainty rather than diff size. See [changelog](CHANGELOG.md).

Version 1 was a reconstruction rather than a verified copy of an earlier package. Version 2 revises that reconstruction; unavailable earlier files were not reproduced or validated.
