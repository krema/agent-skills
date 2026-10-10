# Evaluation requests

Revision: 3, 2026-10-10. All examples and project descriptions below are synthetic fixtures. Use isolated fixtures. Do not give the evaluator rubric to a test worker.

## A: New reader guide

Create Markdown documentation for the fictional local-only “Note Preview” utility. Verified facts: Python 3.11+ is required; run all commands from the checkout root; `python preview.py sample.txt` reads a supplied sample and prints `Preview ready: 3 notes`; there are no credentials, network services, or installation step. A supplied design note says reading local text keeps the example usable offline. Create a start page and a first-success guide. Do not execute commands; the executable is not supplied.

## B: Conflicting evidence

Review only. A guide says `tool start --port 9000`; current supplied command help accepts only `tool serve --port NUMBER`. No runtime is available. Explain what to fix without modifying files or claiming execution.

## C: Future rewrite

Inspect a supplied dense guide that mixes setup, API fields, deployment, and old pilot results. Propose a human-readable Markdown replacement, but do not edit or delete anything in this session.

## D: Small coherent guide

Improve a short troubleshooting page. Its introduction explains the one concept needed to interpret the next two steps. Do not create a documentation site or an entire four-directory tree.

## E: Architecture without rationale

Explain a system from supplied evidence: browser sends a job to an API; API enqueues it; worker stores a result. No source says why a queue was chosen. Write an explanation without inventing design history or describing code line by line.

## F: Authorized replacement

Rewrite an isolated corpus with a unique operational note and incoming root README link. Replacement is authorized. Preserve the note, make old content recoverable, and update the incoming link. No publishing or deployment is authorized.

## G: Senior but new to this workflow

Draft a Markdown start page for Note Preview using only these facts: Python 3.11+, checkout root, `python preview.py sample.txt`, output `Preview ready: 3 notes`, no installation or network. Readers include senior engineers new to the utility and repeat users who already know its inputs. No executable supplied; do not run commands. Provide appropriate reading paths without new infrastructure or invented tasks.

## H: Interpretation boundary

Review a claim: “Our guide is proven effective: satisfaction was high and the low-baseline subgroup improved.” The supplied study was an uncontrolled pre/post course with no significant overall gain and a baseline-defined subgroup. Explain what can and cannot be concluded. Do not create new guides or modify files.

## I: Grounded recovery without invented errors

Improve an imaginary local preview tutorial. Verified facts: run `preview sample.txt` from the checkout root; success prints `Ready`. A documented failure prints `Input missing` when the named file is absent; restore the supplied sample at that location and rerun. There is no evidence about other failures. No executable is supplied. Write concise recovery help without running anything or inventing error messages, support channels, or failure frequency.
