---
name: stateful-evidence-reasoning
description: Answer multi-document or large-corpus questions by tracking source-linked evidence, revisable conclusions, and unresolved gaps. Use when retrieval, conflicting versions, or calculations could cause an answer to drift from its sources.
---

# Stateful Evidence Reasoning

Use this workflow when the answer depends on evidence found across multiple searches, documents, versions, or calculations. For a straightforward question answered by one inspected passage, cite that passage directly and keep the workflow light. This skill adapts the **reasoning practice** in LongHarness; it does not provide that paper's controller, EvidenceBank API, or measured performance gains.

## Work from the decision

1. State the requested answer, relevant period, population, definitions, units, and output format. Identify the facts whose absence or correction could change it.
2. Search for those facts in the available corpus. Treat search results as leads; inspect the underlying passage, table, or original artifact before using a statement as evidence. Preserve a locator a reader can revisit (document and page, section, line, or stable URL).
3. When the work spans several interactions, keep a compact working record with two distinct parts:
   - **Evidence:** an ID, narrowly worded source statement, locator, applicable date/units/qualifiers, and `active`, `superseded`, or `retracted` status.
   - **Conclusion:** established claims and tentative hypotheses linked to active evidence IDs, plus open gaps phrased as facts that could change the answer.
   Use the available notes or files; no special storage system is required. Do not promote an inference, search snippet, or unsupported recollection into the evidence record.
4. Choose the next search or read because it could resolve a material open gap, distinguish competing explanations, or check a fragile source value. After reading, add only source-faithful statements. If new material corrects or invalidates an entry, mark the old entry inactive, record its replacement or retraction, and revisit conclusions and calculations that used it. Do not silently overwrite the old value.
5. For derived answers, record the formula and each operand's active evidence ID, period, and unit. Check that the operand matches the inspected source; use a deterministic calculation tool when useful. If a parsed table, scan, or chart is ambiguous and the original is available, check the original representation.
6. Before answering, follow every material claim and operand back to active source evidence. Resolve gaps that could change the result within the authorized time and access. If a material conflict or missing source remains, give a qualified answer or ask for the specific missing choice. Cite the inspected sources and state consequential uncertainty.

Stop searching when the material gaps are resolved, or when additional available searches are unlikely to change the answer within the task's constraints. Do not impose the paper's fixed turn, search, or token budgets on a different environment.

## When the loop stalls

- If two sources disagree, check whether period, definition, revision status, or units explain the difference. Keep both statements and the unresolved distinction until it is settled.
- If a citation cannot be reopened or a value cannot be verified beyond a snippet, label it unverified and avoid presenting it as established evidence.
- If a correction affects a prior calculation, recompute from active operands before finalizing.

Load [the evidence assessment](references/evidence.md) when adapting this workflow to another environment or making performance claims. Use [the evaluation cases](evals/cases.md) to test changes to its decision rules.
