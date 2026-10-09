# Content rewrite patterns

Use a pattern only when it addresses an identified problem. The evidence and limits for these choices are in [decision-rules](decision-rules.md); examples here are authored illustrations, not experimental results.

## Replace vague instructions with verified decisions

Before: “Test thoroughly with the usual tools.”
After, **only if the project confirms it**: “For parser changes, run `pnpm test:parser`. Integration tests require the local database.”

The gain is resolving what to do and when. A longer replacement may be better. Do not invent commands, mandatory checks, or infrastructure.

## Merge equivalent meanings, preserve conditions

Before: “Keep record IDs unchanged. Never alter identifiers during import. On ID collision, stop; do not overwrite.”
After: “Preserve record IDs during import; stop on collision without overwriting.”

Do not merge similar-looking rules that govern different stages, owners, or exceptions. Useful repetition near separate decision points may stay.

## Remove unrelated work from a simple workflow

Before: “Format the supplied CSV as a Markdown table. First research the market and create a product strategy.”
After, when the owner confirms a formatting-only purpose: “Convert the supplied CSV to a Markdown table, preserving its values and column order.”

The reason is task scope, regardless of length. Do not weaken an actual prerequisite merely because it seems inconvenient.

## Defer a real branch

Keep the mode selector and essential constraints in the entrypoint. Link a recovery procedure where its trigger occurs: “If the import reports duplicate IDs, read the collision procedure before retrying.” Confirm the referenced procedure exists and the relevant task finds it. Do not move useless prose into a reference just to make the core look clean. Small self-contained files need no split.

## Keep examples that resolve ambiguity

An exact input/output pair may encode escaping, field order, or a boundary case more clearly than a paragraph. Keep the necessary case; remove multiple examples only when they add no distinct information. Never assume examples are redundant because prose mentions the same topic.

## Reuse deterministic checks

Point to an existing tested validator with its inputs and failure handling when that is more reliable than prose. Do not build a script for semantic judgments such as whether advice is useful. Its output must not become an automatic “good content” verdict.

## Preserve a sufficient file

If every element has a task role, facts are current, routes work, and no useful change is justified, leave it intact and explain those findings. Do not pad the review with speculative improvements. This decision follows content inspection, never a small size or zero-warning result.

## Preserve the condition inside the rule

Before: “Always benchmark original and revised instructions after every edit.”
After: “For an uncertain behavior change, execute representative tasks; for performance claims, compare original and revised versions under matched conditions. Verify routine factual corrections against their source and affected behavior.”

This is a proportional verification choice, not a measured improvement. The caveat must appear in the instruction that controls the work, not only in its bibliography.

## Do not conceal an unresolved conflict

Suppose equally authoritative requirements demand only valid JSON and a Markdown paragraph outside that JSON. Rewording cannot make both true. Retain the unresolved format decision, explain the incompatible requirements, and continue independent improvements. Do not silently drop either demand or invent an approval requirement for unrelated work.

## Separate finding from executing

An optimizer may read both import and export references to review their interaction. The resulting export workflow should load import details only if the export task needs them. Verify a changed selector with a fresh export task and inspect its actual reads; do not infer runtime preloading from the optimizer's comprehensive audit.
