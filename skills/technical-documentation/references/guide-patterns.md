# Patterns selected by reader need

These are adaptable writing prompts, not required headings. A developer guide can be a collection of several forms. A small document can contain clearly signposted sections when splitting would add needless navigation.

## Tutorial: a first success

State the tangible result and assumed starting state. Choose one supported route. Include prerequisites that can actually be checked, then lead through actions with expected observations. Explain only what the learner needs at that moment; link deeper discussion. Finish by recognizing the result, cleaning up any resources when appropriate, and offering a meaningful next task.

Avoid making beginners select between infrastructure variants before they understand the system. If environments genuinely differ, identify the applicable route before the lesson. An unavailable dependency is a disclosed blocker, not an invitation to invent a simulation and label it verified.

## How-to: a real task

Title the page with the intended outcome, such as “Diagnose a report that was not delivered.” State when it applies. Provide prerequisites, actions, necessary decision branches, and checks. Connect symptoms to evidence and next actions rather than listing every possible error. Link detailed settings separately; keep values necessary for this task nearby. Include rollback or cleanup when the task creates a relevant need.

For an observed or documented failure that can interrupt the task, place concise help near the relevant step or link directly to it: what the reader can notice, what evidence distinguishes likely causes, the supported correction, and how to check that they can continue. Prefer actual user stumbling points, issue reports, or tested behavior over speculative error catalogs. If recovery is unknown, state the gap and a supported next source of help. Do not deliberately induce failures or add warnings at a fixed frequency. This is a conditional design recommendation; more error text alone is not evidence of better learning.

## Explanation: a mental model

Start with the question the reader needs answered and enough domain context to understand it. Trace a representative journey across responsibilities. Explain boundaries, relationships, and supported reasons for choices; discuss alternatives only when they clarify the actual design. A resource inventory or directory table may support the explanation, but cannot replace it.

Synthetic example outline for an imaginary report system: what a scheduled report promises; how a saved definition differs from a schedule and a run; what happens when the schedule fires; where failure and retry occur; why the documented separation matters. These are illustrative questions, not facts about a particular project. If rationale is undocumented, distinguish observed behavior from a possible explanation.

## Reference: reliable lookup

Use consistent entries for settings, terms, supported environments, or commands. Include defaults, constraints, and scope only where verified. A compact table is useful for parallel facts. Link to the guide that uses them. Human guides are the primary deliverable; do not expand scope into exhaustive API or line-by-line documentation without a request.

## Test the reading path

Ask whether a newcomer can find the first action without prior knowledge of filenames. For a returning reader, ask whether a task can be reached without repeating onboarding. For architecture, ask whether responsibilities and interactions can be explained without enumerating source files. These are author checks until a reader actually tries them.

## Different levels of prior knowledge

Assess familiarity with the actual workflow from supplied context, existing usage, or a relevant question. A senior developer can be new to this product. For mixed audiences, name routes by prerequisites or intent, such as “First time running a report” and “Run another report,” rather than labels that imply rank. Keep common facts in one place and retain necessary permissions and verification in the direct route. If knowledge is unknown, expose a clear starting path and optional depth without inventing proficiency scores or requiring a placement test.

When evaluating documentation, inspect whether readers can accomplish the task or explain the relevant relationships. Satisfaction and confidence can supplement those observations but do not establish comprehension. Report overall outcomes as well as subgroup differences; a favorable subgroup in an uncontrolled study cannot establish that the guide caused improvement.
