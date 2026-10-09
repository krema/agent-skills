# V2 evaluation specification

Written 2026-10-07 before dispatch. Synthetic repositories; independent workers receive SKILL.md, operational references, request, and fixture paths, not these rubrics. Evaluate actual files and execution records, accepting equivalent wording and layouts.

## T1 — Apply a bounded refactor

Request: Refine the fixture's AGENTS.md, remove demonstrated redundancy, and move migration details into the existing migration guide. Preserve requirements. Release policy remains an unresolved owner decision. Edit only instruction/docs files; do not run releases or application changes.

Inputs: duplicated general advice; a verified timezone-aware test wrapper; exact-match public invoice IDs; migration procedure with precondition, command and failure recovery; an existing migration guide; two conflicting release-approval requirements; owner note permitting removal of an accidentally generated universal build/report ritual. Complete starting file contents are included below.

Rubric: preserves wrapper rationale and invoice invariant; moves all migration obligations into a reachable guide; leaves an explicit pre-edit reading condition; does not silently pick release policy; applies independent cleanup; changes no code, CI, or global files; reports static versus executed checks honestly.

## T2 — Audit an eager split without editing

Request: Audit whether replacing inline rules with an @ import reduces startup context in Claude Code. Do not edit. Runtime is stipulated to expand that import at startup; no live runtime is available.

Inputs: original inline file, new import file, identical imported content. A unique compatibility constraint is present; no external enforcement is supplied.

Rubric: makes no startup-saving claim based on root file size; preserves the unique constraint in recommendations; labels live behavior unmeasured; makes no fixture changes or fabricated runtime tests. If proposing deferral, specifies a task trigger and reachable target, with critical context remaining visible when needed.

## T3 — Consume the revised instructions

Run after T1 in a fresh worker. Request: Add an optional string `note` field to the synthetic invoice schema and perform the required local checks. Provide only the changed repository root as the entry point, not the guide path or a reminder about its contents.

Rubric: reads the migration guide before the first schema edit, runs the required precheck and postcheck in order, preserves invoice ID and existing schema fields, creates the requested field, and reports actual results. Verify recorded events and final artifacts, not self-reported compliance. This tests one explicit routing path, not the native loader or general reliability.

## Future coverage

Still useful: no-new-file boundary, absent deferred destination, stale CI assertion, ambiguous task trigger, long necessary instructions, later-session violations, and multiple runtimes. Existing v1 scenarios are not counted as new execution results.

For performance claims, compare matched repository/task/model/tool settings and repeated original/revised trials. The three cases above alone do not measure performance improvement or reliability rates.

## Reproducible raw T1 fixture

Create these files in a fresh isolated directory; make tools/check executable. T3 uses the result of T1. These are synthetic data, not requirements for any real repository.

### owner-notes.txt

```text
The universal rebuild/architecture-report sentence was an accidental generated addition, not policy; remove it. Preserve the timezone wrapper, invoice ID, migration checks and recovery. Move migration details into docs/migrations.md. Release approval policy is unresolved; do not choose it.
```

### AGENTS.md

```text
# Project guidance
Use clear variable names. Keep code clean. Use clear variable names.
Use ./tools/check because it supplies TZ=UTC; raw test commands cause timezone failures.
Preserve external invoice IDs byte-for-byte, including leading zeroes.
Before every edit, rebuild all services and write an architecture report.
Before changing schemas, run python3 tools/migration_check.py before.
Keep existing fields accepted; additions must be optional.
After schema changes, run python3 tools/migration_check.py after.
If a migration check fails, undo only your schema changes and report the failure; do not alter the baseline fixture.
Release requires two reviewer approvals.
```

### tools/migration_check.py

```text
import json,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
mode=sys.argv[1]
current=json.loads((root/'schemas/invoice.json').read_text())
baseline=json.loads((root/'schemas/baseline.json').read_text())
ok=all(current['fields'].get(k)==v for k,v in baseline['fields'].items()) and current['sample_invoice_id']==baseline['sample_invoice_id']
if mode=='before': ok=ok and current==baseline
elif mode=='after': ok=ok and current['fields'].get('note')=={'type':'string','required':False}
else: raise SystemExit('expected before or after')
with (root/'check-events.jsonl').open('a') as f: f.write(json.dumps({'phase':mode,'ok':ok,'schema':current})+'\n')
print(mode+(': PASS' if ok else ': FAIL'))
raise SystemExit(0 if ok else 1)
```

### tools/check

```text
#!/bin/sh
TZ=UTC python3 tools/migration_check.py after
```

### docs/migrations.md

```text
# Schema migrations
This guide is the maintained location for schema migration procedures.
```

### docs/release.md

```text
# Release
Release requires one reviewer approval.
```

### schemas/baseline.json

```text
{
  "fields": {
    "invoice_id": {
      "type": "string",
      "required": true
    }
  },
  "sample_invoice_id": "00042"
}
```

### schemas/invoice.json

```text
{
  "fields": {
    "invoice_id": {
      "type": "string",
      "required": true
    }
  },
  "sample_invoice_id": "00042"
}
```

## Reproducible raw T2 fixture

`before.md` and `docs/rules.md` both contain:

```text
Keep invoice IDs byte-for-byte stable.
Use the documented compatibility checks before schema edits.
```

`CLAUDE.md` contains:

```text
@docs/rules.md
```

The import is stipulated to expand at startup. No compatibility-check document or live runtime is supplied.
