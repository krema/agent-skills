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

## Evaluator reliability in open-ended trials

Kumar et al., [All Verdicts are Not Equal: Rethinking LLM Judge Reliability](https://aclanthology.org/2026.aacl-long.207/), published in the AACL-IJCNLP 2026 proceedings (November 6–10), accessed November 22, 2026. The authors audited six judges across four benchmarks, varying prompt format, response order, temperature, and repetitions. They report verdict changes across identical repetitions, substantial order sensitivity on some challenging examples, and a case where perfect repeat consistency coexisted with only 51% agreement with the reference. Their comparison of three scoring formats found format-dependent results; their limitations restrict the study to four English benchmarks and pairwise judgments, so transfer to rubric grading of skill trials is uncertain.

Verma et al., [AgentJudgeBench: A Multi-Difficulty Benchmark for Evaluating LLM Judges on Agentic Tool-Calling](https://aclanthology.org/2026.emnlp-main.659/), EMNLP 2026 proceedings (October), accessed November 22, 2026. Across workflow-DAG tool-calling cases, alignment worsened with task difficulty; providing ground truth was not uniformly beneficial, and structured rubrics improved alignment by up to 6.5 percentage points without uniform transfer across judge–generator pairs. This is specific to tool-calling workflow evaluation, not skill authoring.

Zhang et al., [SciWorkBench: A Benchmark for Real Scientific Workflows](https://arxiv.org/abs/2611.22490), arXiv v1 submitted November 17, 2026, accessed November 22, 2026. This preprint evaluates science workflows across multiple stages and reports procedural translation, multimodal evidence integration, and scientific self-correction as recurring weaknesses. It supports checking intermediate artifacts and evidence-to-conclusion links rather than treating task completion or a fluent final answer as sufficient. It does not evaluate this authoring workflow; its reported benchmark score is not a measure of skill quality.

The authoring implication is limited: when an LLM grader drives a material claim, check it against verifiable or independently established reference judgments where feasible, and disclose what was checked. A consistent score alone does not establish validity. The studies do not establish a universal calibration protocol, sample size, or requirement for human adjudication; use task-relevant checks proportionate to the claim.

## Answer exposure in tool-enabled synthesis trials

SciConBench compared agents synthesizing health evidence with open search and with access to reference conclusions filtered. Factual F1 fell under filtering, including for the additional open-weight models in the revised study. The filters differed across providers and could also affect retrieval of useful evidence. The comparison cannot identify how a particular answer was produced. First submitted June 9, 2026, revised November 10, accessed November 15. See sections 6, F.3 and I.1 of [Can AI Agents Synthesize Scientific Conclusions in Health?](https://arxiv.org/html/2606.11337v2).

For skill evaluations, inspecting tool-accessible answers is an engineering inference. It matters when independent synthesis is the capability being tested. The study did not evaluate this authoring workflow.
