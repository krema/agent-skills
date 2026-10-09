# Refactoring instructions and skills

Use this reference when changing a prompt, AGENTS.md-style guidance, or a skill catalog. These are engineering patterns supported by E03, E05, E09–E10; they are not a claim that moving text between files always improves performance.

## Inspect the actual loading path

Identify which instructions are automatically inserted, which are read only after selection, and which inherit by directory or scope. Verify the target host's behavior through its documentation or a trace. A Markdown link alone does not guarantee automatic loading; an import directive may eagerly expand the supposedly deferred content. Preserve applicable host rules while refactoring within authorized files.

Classify each existing requirement by applicability and consequence of omission:

| Content | Candidate placement | What must survive |
|---|---|---|
| Requirements governing every action | Shared entrypoint | Meaning, scope, precedence |
| Domain-specific procedure | Cohesive reference | Observable activation condition and dependencies |
| Facts available in source files | Locator or focused reference | Discoverability, version, provenance |
| Rare recovery instructions | Linked recovery branch | Failure signal that leads to the branch |
| Repeated or contradictory rules | One canonical rule, or explicit scope distinction | Exceptions and legitimate differences |

Record important old-to-new mappings during substantial migrations. Check every moved obligation has an incoming path. Do not delete a requirement merely because it is long or inconvenient; distinguish redundancy from a non-obvious constraint.

## Make the route executable

Prefer descriptions that identify a decision: “Read migration guidance before changing persisted schemas” is more useful than “database tips.” If migration deployment also requires a backup procedure, the selected migration guide must point to that prerequisite before the deployment step. The shared entrypoint can carry the brief dependency warning without copying the entire backup procedure.

Overlap is sometimes correct. A billing export may need both billing and privacy guidance. Offer a way to load both instead of forcing one exclusive label. For ambiguous terms, inspect enough surrounding context to resolve them; ask for a genuinely missing user constraint only when it changes the work.

A compact skill generally needs no further router. A large catalog may require its own searchable index; the sum of all descriptions is still upfront context. Audit generic descriptions that trigger on nearly everything, aliases that collide, and stale entries pointing at removed resources.

## Example layout

An agent handling schema migrations, UI edits, and billing reports can retain global authorization and repository test conventions in its entrypoint, then link three substantive guides. Each guide holds its own specialist checks. A UI-only task should not need the billing guide; a migration affecting billing data should load the migration and billing prerequisites.

This is an illustrative design, not a required folder count or filename convention. Choose boundaries that match real requests and minimize missing prerequisites and unnecessary round trips.

## Acceptance and recovery

Try synonymous requests, cross-domain requests, and requests just outside each description's scope. Inspect actual reads and outputs. If a guide is missed, first fix the description or dependency. If it is nearly always needed, make it upfront. If reads fragment a coherent task, merge that unit. Preserve previous files until links and downstream callers have been updated and checked.
