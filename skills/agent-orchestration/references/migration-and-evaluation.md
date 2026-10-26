# Migrate a boundary and evaluate the result

Use this reference when changing existing orchestration or interpreting candidate-versus-baseline results. Its procedures are engineering synthesis, supported and qualified in [evidence.md](evidence.md).

## Preserve obligations before moving them

Map the current specialist's behavior to its destination. Record essential obligations that could disappear with the agent: domain procedure, data source, user constraints, side effects, authorization, output contract, state updates, and required checks.

| Responsibility | Likely destination |
|---|---|
| Occasional procedural judgment | A discoverable skill in the shared loop |
| Reference facts | A focused reference or retrieval interface, with freshness appropriate to the facts |
| Data access, validation, state changes | Tools and the services they call |
| Access restrictions or mandatory preconditions | An enforced tool, backend, or harness boundary |
| Adaptive work that benefits from isolation | A retained worker with a bounded input/output contract |
| Common conversational behavior | The main conversation's instructions, reconciling conflicts |

Do not concatenate all specialist prompts. Remove a rule only after checking whether it encodes a real requirement; age, repetition, or emphatic wording alone is not evidence that it is obsolete. Tools alone may suffice when no procedural judgment remains. Use the target host's current documentation for actual loading, context inheritance, tool registration, and permissions; these vary across products.

Keep the original implementation recoverable and make one attributable architectural change at a time. Preserve permission boundaries before enabling replacement access. Negative direct calls should exercise moved restrictions: a model choosing not to attempt an action cannot demonstrate that the tool would refuse it. Verify permitted operations still work as well.

## Compare completed tasks

Define success from observable outcomes, including important state changes and facts grounded in authoritative data. Reuse suitable end-to-end cases, add cases for the affected capability combinations and known incidents, and include absent data, partial results, and permission boundaries where relevant. Inspect adjacent capabilities that share newly available tools: gaining a lookup can cause the main agent to answer prematurely.

Keep task inputs, starting state, model/settings, tool responses, grader, and available budget comparable across variants. Record deliberate differences; a simultaneous model upgrade or larger budget prevents attributing the change to architecture alone. Reset test state between runs. Fit repetitions to variability and decision risk, repeating intermittent failures; no fixed sample size proves reliability.

Measure task completion and required invariants first. Also collect wall-clock latency, all participating agents' calls/tokens, and cost when available. Include retries and failed attempts; label missing measurements. Aggregate quality, cost per successful task, and tail latency can be useful when the sample supports them. They do not replace examining individual failures.

Inspect tasks that switch from success to failure, and investigate surprising new successes for grader artifacts. Tool or skill selection is diagnostic; an alternate path is acceptable if it satisfies the task and enforced requirements. Passing a prescribed route is not itself task completion.

## Decide and recover

- **Retain the change** when it meets the task's acceptance criteria and any relevant cost/latency constraints with adequate evidence.
- **Repair or revert** a violated requirement. A faster average or higher aggregate score does not excuse a mandatory-rule regression.
- **Gather targeted evidence** when variation or missing coverage prevents a decision. Say which case or measurement would resolve it, and keep the working baseline in the meantime.
- **Keep the separate worker** when isolation continues to earn its cost. A hybrid result is a valid endpoint.

Report the exact variant tested, data and checks used, regressions, uncertainty, and rollback point. A synthetic replay supports behavior only in that replay; it does not establish production improvement. Continue authorized local implementation without adding ceremonial approval stops; deployment and external effects follow the user's existing scope and the host's permissions.
