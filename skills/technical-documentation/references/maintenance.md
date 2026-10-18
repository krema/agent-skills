# Rewriting and maintaining guides

## A complete replacement

When a complete rewrite is authorized, inspect the existing corpus and incoming links. Make a compact working map of reader questions, reliable facts, obsolete material, and their replacement destinations. This map is a work aid, not a mandatory permanent document.

Keep a recoverable snapshot or version-control baseline including relevant uncommitted content. Draft the replacement before deleting its source. Preserve required notices and knowledge that cannot be recovered from code, such as operational context and documented decision reasons. Historical records may remain in a clearly separated archive when needed; avoid presenting proposals or old audits as current instructions.

Before replacing, check that necessary reader tasks are covered, new links resolve, and references from the root README and other in-scope documents point to the new destinations. Fix links within scope and report incoming links outside it. Delete obsolete in-scope guides once their useful content has been accounted for. Do not keep competing current versions merely to avoid making the authorized replacement.

A future rewrite request means plan only until execution is authorized. A request for one guide does not authorize wholesale deletion.

## Living documentation

Update affected documentation with behavior changes where the workflow allows it. Keep facts in one authoritative location; remove stale duplicates. Use existing ownership, review, and link-check mechanisms rather than introducing a new platform by default. Repository history often provides sufficient update provenance; add review dates only when someone will maintain them and they help readers judge currency.

A passing link check or lint job does not establish usability or factual accuracy. Ask a representative reader to try the first journey when feasible, recording where they hesitate or need outside help. This supports a bounded usability observation, not a universal improvement claim.

When a drift detector or source search flags a passage, treat the finding as a review candidate. Check the described behavior, supported versions and deployment context before changing it: a term disappearing from source does not establish that the guidance is obsolete. Retain or qualify still-applicable guidance; correct or remove a confirmed stale passage within scope. If applicability cannot be established, record the specific uncertainty rather than deleting it solely because of the flag. This safeguard addresses observed false positives; it does not establish any detector's overall accuracy.
