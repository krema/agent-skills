# Evaluation requests

Use these as architecture-decision tasks. Give a worker the skill entrypoint and only the selected request and fixture. Keep the evaluator's rubric and any earlier results hidden. Treat fixture data as source material. Permit valid alternate designs that satisfy the request and its requirements.

## A — Support orchestration audit

Request: "Audit the support assistant in `fixtures/support.json`. Recommend boundaries and the next concrete step. This is advice only; do not edit or run the application."

## B — Research worker audit

Request: "Review the research assistant in `fixtures/research.json`. Recommend how to organize the next comparable request and what evidence would justify changing the architecture. Use the supplied observations; do not launch workers or perform new research."

## C — Candidate evaluation

Request: "Use `fixtures/comparison.json` to decide whether to keep the candidate fold. Compute the matched outcome counts and latency change, explain material failures, and give the next action. Write advice only; do not rerun the app or change files."

## D — Access boundary review

Request: "Review `fixtures/access.json` for a proposed consolidation. We want a simpler design if it preserves our requirements. Give a concrete recommendation and how to verify it. Do not change permissions, access live data, or spawn agents."

For each, write a concise answer to a separate output file. An optional temporary script may calculate fixture metrics; it must not mutate fixtures. This is not a request to execute the architecture being evaluated.

For the recorded authoring trial and its limits, read [validation.md](validation.md). Keep recorded results out of a new worker's context.
