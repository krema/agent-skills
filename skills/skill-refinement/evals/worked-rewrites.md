# Worked content revisions

Examples and evaluation inputs in this file are synthetic.

These seven concrete outputs were produced and reviewed by the package author in the same session. They illustrate applying the revised workflow; they are **not independent trials, a blinded evaluation, or measured agent-performance gains**. Inputs are in [cases.json](cases.json); full changed-file contents, reasons, and inspection notes are in [worked-rewrites.json](worked-rewrites.json). Unlisted files are unchanged.

| Case | Actual decision | Basis | What was checked |
|---|---|---|---|
| compact_paraphrases | Merge two differently worded ID rules even with zero static findings. | Supplied semantic equivalence; editorial hypothesis. | Collision stop and no-overwrite retained. |
| needed_specificity | Expand a vague sentence into a scoped, runnable command. | package.json and OWNER.txt. | Command exists in metadata; integration coverage is not implied. Command itself was not run. |
| scope_sensitive_repetition | Share ID preservation; retain opposite import/export duplicate rules. | Supplied mode requirements. | Manual common and exception walkthrough. |
| short_overloaded | Delete research, repeated approvals, and redesign. | Owner explicitly identifies copied, non-policy steps. | Required identifier fidelity survives. |
| large_useful | Correct discovery wording; keep all 350 mappings. | Owner-required offline information and actual purpose. | Exact mapping and rejection text preserved. |
| rare_critical | Correct discovery wording; keep the entire body. | Owner-required recovery and authorization. | Every operative requirement retained byte-for-byte. |
| audit_only | Return proposed consolidation without editing. | Explicit audit-only request. | Full target byte equality. |

## A short file still gets edited

Before:

```text
Preserve record identifiers.
Do not change record IDs.
On a collision, stop without overwriting.
```

After:

```text
Preserve record IDs; on a collision, stop without overwriting.
```

## A useful revision can grow

Before: “Test appropriately before handing off.”

After: “For parser edits, run `pnpm test:parser` before handoff. This checks parser behavior, not database integration.”

The fixture's owner note and package metadata establish the command and scope. Research is not needed to invent or authorize those facts. There is no measured speed or accuracy claim.

## Similar content can encode different behavior

Before: separate import/export statements each preserve IDs; import rejects duplicates and export allows them.

After: “Preserve record IDs in both modes. Reject duplicate IDs on import; allow them on export.”

A blanket deduplication rule could lose that distinction. This example tests meaning and scope, not file length. Independent fresh-agent execution remains a separate validation step in [cases.md](cases.md).
