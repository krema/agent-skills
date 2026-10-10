# Evidence and design decisions

Reviewed through 2026-10-10. Revision 3. Intended use: agent-authored human onboarding, architecture explanations, task guides, and supporting lookup material in ordinary Markdown repositories. Independent synthesis of Diátaxis, Google, and Canonical; not an official package from those organizations. Required instructions are included locally as original paraphrases; upstream websites and their publishing stacks are not runtime dependencies.

## Coverage and search limits

Targeted qualitative review of primary documentation guidance and selected empirical research; not a systematic review or comparative effectiveness study of this package. Evidence types and transfer limits are recorded below. Initial access for E01–E05: October 8, 2026. Live pages were inspected without immutable commit pins. No study establishes the effectiveness of this combined skill.

## E01: Reader needs and document forms

Sources: Daniele Procida, Diátaxis: [tutorials](https://diataxis.fr/tutorials/), [how-to guides](https://diataxis.fr/how-to-guides/), [explanation](https://diataxis.fr/explanation/), [reference](https://diataxis.fr/reference/). Source repository: https://github.com/evildmp/diataxis-documentation-framework.

Inspected definitions and writing principles, including visible tutorial results, task-oriented branching, explanatory context, and consistent lookup patterns. These are authoritative descriptions of the author's framework and expert prescriptive guidance, not controlled findings. They support selecting a form according to reader intent. Applying explanation to architecture is an engineering inference; architecture also has reference and operational aspects. A developer guide need not fit one category as a whole. Boundaries should clarify a journey without removing locally necessary context.

## E02: Limits of imposing structure

Source: [Diátaxis as a guide to work](https://diataxis.fr/how-to-use-diataxis/), especially “Use Diátaxis as a guide, not a plan,” “Don't worry about structure,” and “Just do something.” Relevant passages read directly.

The author favors incremental improvement and rejects empty four-section scaffolds and wholesale tear-down as defaults. This counters a simplistic folder-template interpretation. A complete replacement can still be supported when explicitly authorized, with recoverability and knowledge preservation. This is a scope-dependent engineering choice; migration mechanics are engineering safeguards, not evidence that rewrites outperform gradual improvement.

## E03: Maintainable Markdown and entry points

Sources: Google [best practices](https://github.com/google/styleguide/blob/gh-pages/docguide/best_practices.md), [README guidance](https://github.com/google/styleguide/blob/gh-pages/docguide/READMEs.md), and [Markdown style](https://github.com/google/styleguide/blob/gh-pages/docguide/style.md). Inspected best-practice and README text plus Markdown layout, headings, links, and portability guidance.

Expert engineering conventions support a useful maintained corpus, documentation changes alongside behavior changes, clear orientation, and removal of stale duplication. No controlled comparison was reported. Google's README placement, site-root link, and Gitiles table-of-contents conventions are environment-specific. This skill instead permits a docs entry point and relative repository links for portable local Markdown; it does not universally apply those house rules. Short contextual reminders can aid reading even when extensive duplicated facts should be consolidated.

## E04: Prose and examples

Sources: Canonical [repository](https://github.com/canonical/documentation-style-guide) and [published style guide](https://documentation.ubuntu.com/style-guide/). Inspected Diátaxis alignment, headings, contractions, command examples, placeholders, and plain-language passages.

Canonical's house style supports readable headings and prose surrounding commands, separates output from commands, and discourages large uninterpreted blocks. These are normative recommendations, not proof of cognitive benefit. Transfer is strongest for human technical guides. Branding, language-variant preferences, lint tooling, and Sphinx extensions are not universal requirements; none is installed by this skill. Use the existing project's language conventions. Portable Markdown is this skill's design scope, not a Canonical requirement.

## E05: Project grounding and scope

Basis: design scope and engineering inference. The skill targets human guides in portable Markdown, grounded in the three named public sources. Evidence inspection supports distinguishing a behavior observed in source from a command actually executed. Code can establish implementation but often cannot establish historical intent; label inferred rationale. Scope boundaries prevent a review or future plan from becoming an unsolicited rewrite. No empirical study was used to justify these requirements.

## Evidence to behavior

| Decision | Support and type | Counterweight or fallback | Observable check |
|---|---|---|---|
| Choose tutorial, task guide, explanation, or lookup by reader need | E01, expert framework | Small coherent pages need not be split | Reader purpose remains identifiable |
| Include visible tutorial progress and task-specific decisions | E01, normative | Exact outputs must be supported | Checkpoints match available evidence |
| Explain architecture through context and interactions | E01 plus engineering inference | Undocumented rationale remains unknown | Can describe flow without a file inventory |
| Avoid mandatory four-directory layouts | E02, explicit framework limit | Larger corpora may benefit from categories | No empty category padding |
| Provide entry path and portable links | E03 plus design scope | Adapt existing renderer and small scope | Start page and relevant links work |
| Use readable prose and contextual examples | E04, house style adapted | Tables and dense reference can be appropriate | Reader can distinguish action and observation |
| Maintain canonical facts with behavior changes | E03, engineering guidance | Brief reminders may be useful | No contradictory current guidance |
| Support authorized replacement with recoverability | E02 counterweight and engineering inference | Incremental improvement remains default for narrow tasks | Knowledge and links accounted for |
| Verify facts and label execution limits | E05, engineering inference | Missing runtime prevents execution claim | Report distinguishes inspection and execution |
| Install no documentation framework by default | Design scope | Existing optional tooling can still be used | Package operates from local text resources |

## Open questions and refresh

Actual reader success and the agent's reliability across complex migrations remain unestablished. Test onboarding with representative readers and track stumbling points before claiming better comprehension. Revisit affected sources when the framework changes, a Markdown renderer changes, or real use exposes missing context. Recheck operational project facts on each documentation task; this package cannot freeze those facts globally.

## E06: Assistance depends on prior knowledge

Tetzlaff, Simonsmeier, Peters, and Brod (2025), [A cornerstone of adaptivity](https://doi.org/10.1016/j.learninstruc.2025.102142); [repository full text](https://www.pedocs.de/volltexte/2026/34113/pdf/Learn_and_Instr_2025_Tetzlaff_u.a._A_cornerstone_of_adaptivity.pdf). Published online April 17, 2025; accessed October 9, 2026. Read methods, results, and limitations. The repository's 2026 path is not a new publication date.

Meta-analysis: 60 experimental studies, 5,924 participants, 176 effects. Higher assistance favored lower-knowledge learners (d=0.505, 95% CI 0.260–0.750); it disadvantaged higher-knowledge learners (d=-0.428, CI -0.647–-0.209). Heterogeneity was high (I² about 91% and 88%); domains, assessment, and educational status matter. Publication-bias tests were nonsignificant, not proof of absence. Mechanisms and Markdown-specific effects remain unresolved.

Inference: offer prerequisite-based routes when audiences differ, preserving essential checks. This does not justify universal expert shortcuts, assumed expertise from seniority, or removing all explanation. Evaluate case G and ultimately real reader performance; no direct documentation effect size is claimed.

## E07: Software onboarding results need cautious interpretation

Kumar and Choppella, [Early Results from Teaching Modelling for Software Comprehension in New-Hire Onboarding](https://arxiv.org/html/2510.07010v1), arXiv v1, October 8, 2025; accessed October 9, 2026. Read intervention, assessment, results, and discussion. Preliminary single-company study: five sessions, 35 interns, 31 paired records; no untreated control. Instructor-rubric assessments used different intended-comparable products.

Overall gain was 2.4 percentage points and nonsignificant. The lower-pretest subgroup improved, but selection by baseline makes regression to the mean a competing explanation (reviewer's inference). Self-reported satisfaction cannot substitute for learning outcomes. Transfer from a taught modelling course to standalone Markdown is uncertain.

Decision: retain architecture explanations without mandating LTS exercises. When evaluating guides, distinguish task/comprehension outcomes from satisfaction and report null overall results alongside subgroups. This is evaluation discipline, not evidence that this package improves onboarding.

## Additional evidence-to-behavior mappings

| Condition → action | Basis | Limits and observable check |
|---|---|---|
| Mixed task knowledge → optional guided and direct paths | E06 plus engineering inference | Retain prerequisites; case G checks senior-but-product-new readers |
| Claimed documentation benefit → inspect actual task/comprehension results | E07 plus methodological inference | Satisfaction alone insufficient; case H checks null and subgroup claims |

## E08: Error guidance needs task relevance

A.W. Lazonder (1994), [Minimalist computer documentation](https://ris.utwente.nl/ws/portalfiles/portal/6076161/thesis_Lazonder.pdf), chapters 4 and 6; accessed October 10, 2026. Read experimental methods, results, and discussion passages, not the entire thesis. Chapter 4 randomized 42 students; error guidance produced mixed results, including adverse outcomes. Chapter 6 randomized 50 adult beginners using WordPerfect 5.1, comparing manuals with and without revised error guidance. Corrective practice time fell by 38% (p<.05); constructive-skill improvement was not established. Some analyses excluded incomplete records. The studies differ in participants, materials, and context; their contrast cannot isolate the effect of a single revision.

Inference: select documented or observed failure points and connect recognition, diagnosis, correction, and a return to the task. Do not assume that more warnings improve learning. Old desktop-software experiments have limited transfer to modern developer guides; no universal warning density, length, or outcome benefit is prescribed. Test case I checks grounding; real reader outcomes remain necessary.

| Condition → action | Basis | Boundary and check |
|---|---|---|
| A supported failure can interrupt a procedure → provide relevant recognition and recovery nearby | E08 plus engineering inference | Do not invent failures or blanket warnings; case I checks grounding |

Publication scope: evidence summaries and explicitly synthetic examples are included. Private project descriptions, conversation history, and internal execution logs are excluded. Validation coverage is summarized separately.
