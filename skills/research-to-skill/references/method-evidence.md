# Basis and limits of this workflow

Reviewed 2026-10-07. This is a targeted design rationale, not a comprehensive study of research methods. The complete research-to-skill workflow has not been experimentally shown to be optimal. Source appraisal, traceability, and installation safeguards are engineering choices; local behavior checks are still needed.

## M01 — Skill format and conditional loading

[Agent Skills specification](https://agentskills.io/specification), live specification, accessed 2026-10-07; relevant format and resource sections inspected. Normative evidence for frontmatter, directory naming, and optional resources. It describes progressive disclosure, but does not experimentally establish an optimal instruction length. This skill uses the format and conditional references without treating the specification's length recommendations as a quality threshold.

## M02 — Evaluate observed outcomes with appropriate graders
[Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents), published 2026-01-09, accessed 2026-10-07; evaluation structure inspected. First-party engineering guidance, not an isolated causal study. Distinguishes trials, outcomes, traces, and graders; notes that a rigid evaluation can penalize valid behavior. Supports recording actual results and accepting valid alternatives. It does not prove that a particular generated skill improves performance or prescribe a universal number of trials.

## M03 — Generic self-correction is not reliable evidence of correctness
[Huang et al., Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798), ICLR 2024; first 2023-10-03, revision 2024-03-14; abstract/metadata inspected 2026-10-07. The abstract reports failures and degradation in intrinsic reasoning correction without external feedback. Abstract-only appraisal here: no effect estimate is adopted. Supports caution about self-certification, not a claim that all current models or all review methods fail. M04 is a relevant counterpoint.

## M04 — Verification method changes the result
[Wu et al., Large Language Models Can Self-Correct with Key Condition Verification](https://arxiv.org/abs/2405.14092), EMNLP 2024; first 2024-05-23, revision 2024-10-03; abstract/metadata inspected 2026-10-07. Reports gains from masking and predicting key conditions in reasoning tasks with GPT-3.5-Turbo. Abstract-only appraisal; this is not evidence of transfer to research synthesis or skill authoring. Together with M03, motivates testing specific verification behavior instead of blanket faith in, or rejection of, model review.

## M05 — More process can become unnecessary
[Anthropic: Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps), published 2026-03-24, accessed 2026-10-07. Relevant design discussion inspected. First-party experience with multiple coupled changes; not a clean experiment on contract text. Reports benefits and costs of orchestration and subsequent removal of sprint scaffolding with a newer model. Supports checking whether extra process earns its cost, not prescribing that every skill use or avoid separate reviewers.

## Local operational authority

The host's bundled `skill-creator` and `skill-installer` guidance was read on 2026-10-07. It supplies the supported local installation default and metadata-validation procedure. These are environment instructions, not empirical evidence of skill quality. No private absolute path is required by this package; future runs should consult available host guidance for changed behavior.

## Decision mapping

| Design decision | Basis | Limit / check |
|---|---|---|
| Metadata and conditional resources | M01; local authoring guidance | Validate structure and links; no length-based quality claim |
| Outcomes and actual trial records | M02 | Graders remain fallible; separate downstream performance from drafting |
| Do not equate self-review with proof | M03 and M04 | Methods differ; use observable checks and report uncertainty |
| Avoid mandatory review loops or extra agents | M05; engineering judgment | Add independent trials when justified by task uncertainty |
| Trace each material rule to its basis | Engineering synthesis and evidence-traceability objective | Citation presence alone does not verify the inference |
| Validate before installation and compare copies | Local operational guidance; engineering judgment | Correct copying does not demonstrate successful future invocation |

## Local revision rationale — 2026-10-07

Review of a generated instruction-maintenance skill found a disproportionate requirement for matched experiments after any substantial edit, authoring-only text in the operational entrypoint, and validation limited to intended-answer walkthroughs. These are local artifact observations, not a controlled effectiveness study. The revision makes condition/action/outcome synthesis explicit, checks the strength of obligations, and distinguishes focused execution from comparative effectiveness evaluation. Existing source claims were not refreshed. The new guidance is an engineering correction whose transfer beyond the recorded trial remains unproven.

## Shared origins in apparent corroboration

Zhou et al. compared matched search environments with one false page or several pages derived from a common origin. On 90 primary-model cases, the fraction of false claims published rose from 0.71 to 0.83. The magnitude varied across models, and access to counterevidence affected the result. The experiment used fictional claims. The natural-news test evaluated metadata classification only. Published October 2026, accessed November 8, 2026. See sections 6.1–6.4 and Limitations in [Evidence Laundering](https://aclanthology.org/2026.emnlp-main.509.pdf).

The authoring decision is an engineering inference. When agreement would justify stronger guidance, separate shared observations from independent ones and keep unknown origins explicit. A separate analysis of shared data can still contribute a distinct finding. Transfer to skill authoring has not been measured.
