# Writing and portable Markdown

Use a title and a short opening that establish purpose and audience. Prefer connected prose for explanation, numbered steps for sequence, and tables for genuinely comparable facts. Replace dense instruction matrices with a guided narrative when the reader must understand an order or causal relationship. Length alone is not a defect; missing context and repetition matter more.

Use plain language, active verbs, consistent terminology, sentence-case headings, and a logical heading hierarchy. Do not jump immediately from a heading into another heading when a framing sentence would help. Expand unfamiliar acronyms when first needed. Avoid words such as “simply” when they minimize a reader's difficulty. Preserve a project's established language variant unless asked to change it; Canonical's US-English house preference is not a universal requirement.

Introduce commands in prose. Use fenced blocks with a language, keep commands distinct from output, and explain what to observe. Identify placeholder values and where to obtain them; do not bury essential explanations in shell comments. Prefer focused examples to long dumps. Relevant safety or access constraints belong at the affected step, not in a repetitive wall of warnings.

Use ordinary Markdown headings, lists, fences, and descriptive relative links to repository files. Keep text usable in an editor and a repository viewer. Google-specific `[TOC]` directives and site-root paths do not transfer automatically; use explicit linked contents only when navigation benefits. Avoid MyST/Sphinx directives and generated-site features unless the target already requires them.

For diagrams, use the existing supported format. Mermaid can be useful in a compatible viewer; provide prose for essential meaning. Do not install a renderer merely to write a guide. Plain text flows are acceptable when clearer.

Keep deeper explanation one descriptive link away when practical, while retaining enough local context to finish the task. Avoid both copying whole prerequisites across files and forcing a reader through a chain of prerequisite links. Choose a canonical home for changing facts; short reminders may be repeated for comprehension.
