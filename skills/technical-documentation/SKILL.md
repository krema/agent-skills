---
name: technical-documentation
description: Create, review, and rewrite human-readable onboarding tutorials, architecture explanations, developer how-to guides, and supporting reference in living Markdown files. Use when readers get lost in project documentation or need practical guides; applies Diátaxis, Google documentation guidance, and Canonical writing conventions.
---

# Technical Documentation

Help a person find a starting point, understand a system, and finish real work. Use Diátaxis to distinguish reader needs, Google guidance to maintain Markdown, and Canonical guidance to write clearly. This independent synthesis needs no framework installation, website, generator, or companion skill. Source links support the rules; normal use does not require browsing them.

## Establish the reader and scope

Determine whether the request is review, targeted improvement, new documentation, or complete replacement. Review-only and future planning requests do not authorize edits. Preserve a narrow scope; honor an explicitly requested rewrite without adding another approval gate. Documentation work does not itself authorize running deployments or other consequential commands described in the text.

Inspect the existing entry point, relevant guides, and authoritative project evidence. Identify the intended reader, assumed knowledge, concrete questions, and desired result. Use available context before asking; ask only when an unresolved audience or workflow would materially change the guide.

When audiences differ in task-specific knowledge, offer a guided first path and direct access for readers who already meet its prerequisites. Do not infer product familiarity from seniority or job title. Keep essential access requirements and correctness checks on both paths. This is a conditional design recommendation, not a proven improvement for every team; avoid extra routes when one coherent guide serves the audience.

For a rewrite, load [migration and maintenance](references/maintenance.md). Preserve unique operational knowledge and required notices in a recoverable source before removing old files. Verify facts against current configuration, supported commands, tests, or maintainers; do not trust old prose merely because it is detailed. Keep uncertain behavior and inferred rationale visibly qualified.

## Choose the kind of help

Classify the reader's immediate need, not the filename:

| Need | Form | Completion signal |
|---|---|---|
| Learn through a first successful experience | Tutorial | Reader reaches a visible result through a guided path |
| Accomplish an already-understood task | How-to | Reader can choose applicable steps and verify the result |
| Understand how and why the system works | Explanation | Reader can describe relationships and relevant tradeoffs |
| Look up a setting, term, or constraint | Reference | Reader finds a precise supported fact without following a lesson |

For the chosen form, load [guide patterns](references/guide-patterns.md). Split material when the audience or purpose changes enough to interrupt the journey. Short context needed to perform a step can stay with it. Do not enforce four directories, fill empty categories, or fragment a small coherent guide just to satisfy a taxonomy.

## Build a readable journey

Create or improve a clear entry point within scope. State what the system does, who the guides serve, and where a new reader should begin. Name links by the task or question they answer. Offer a recommended first path rather than an undifferentiated catalog. Existing readers should also reach common tasks directly.

Load [writing and Markdown](references/writing.md) before drafting. Introduce purpose before machinery, connect paragraphs, explain unfamiliar terms at first relevant use, and move optional depth behind descriptive links. Keep necessary prerequisites close enough that a reader does not have to assemble the procedure from several unrelated pages.

For architecture, build a mental model from a user scenario through the major responsibilities and interactions. Explain documented design reasons and tradeoffs, not each function or line of code. Distinguish current behavior from proposals and historical decisions. Use a diagram only when it clarifies relationships, with enough prose to understand the same essential idea without rendering it.

For procedures, distinguish commands, expected observations, and recovery. Identify working directory, required access, relevant environment, and user-supplied values when needed. Do not invent commands, exact output, compatibility, timings, or setup requirements. If facts are missing, write the supported portion and record the specific gap instead of producing a confident runnable recipe.

## Verify and deliver

Read the result in the intended order. Check whether the reader knows why they are here, what to do or understand next, and how to recognize completion. Check file links and relevant anchors in the intended Markdown renderer; avoid requiring website navigation or extensions.

For a tutorial or how-to, exercise representative commands only when available and authorized. Otherwise inspect their support and state that execution was not verified. Never call a command tested because it appeared in source. For explanations, trace the described flow against project evidence and flag unknown design rationale.

For broad rewrites, apply the migration checks. For small edits, check affected paths and facts. Resolve broken required links, contradictory instructions, missing prerequisites, and abandoned reader paths before delivery; report remaining blockers precisely.

Deliver the requested files or review findings, the entry point and reading order, actual checks, and unresolved factual or execution gaps. Keep audit logs and historical verification out of everyday guides unless the reader needs them. Do not claim improved human comprehension without observing readers.

## Supporting material

- Read [evidence](references/evidence.md) when assessing a rule's basis or refreshing the sources.
- Read [validation](references/validation.md) for this package's tested scope and limits.
- When evaluating the skill itself, use [requests](evals/requests.md); reserve [rubric](evals/rubric.md) for the evaluator.
