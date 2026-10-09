# Publication privacy review

Review date: 2026-10-09. Scope: the eight distributable skill packages, supporting resources and fixtures, manifests, provenance, repository documentation, and publication tooling in the 1.1.0 working tree. The follow-up also screened the four commits and 120 unique file blobs reachable from the fetched main and feature branches at review time. Unreachable objects, GitHub caches, third-party clones, and external source contents are outside that coverage. Historical remediation status is tracked separately from release-candidate approval.

Pattern screening checked personal filesystem paths, email addresses, credential-shaped strings, private conversation references, internal service references, and potentially identifying account fields. Candidate locations and source/evaluation context were inspected. Public research citations and the intended public `krema` repository identity remain.

Findings:

- No actual credentials, personal contact details, private conversation links, or machine-specific source paths were found in the skill payloads.
- Candidate hits were synthetic fixture schemas, a package version, an `example.invalid` test email, and the publication tool's intentional private-path rejection test/pattern.
- Follow-up review generalized residual originating-request references in Context Loading, Context Management, Research to Skill, Learning Loop, and Ticket Craft. Skill Refinement also contained a historical conversation title and reconstruction narrative; these were replaced with a generic provenance limitation. Operational rules and recorded evaluation outcomes are preserved.
- Technical Documentation's evidence ledger included historical observations about a private documentation set and the original user's preferences. These were generalized to reusable design rationale. Its operational guidance is unchanged, and `origin.json` records the adaptation without private source locations.
- Research to Skill and Learning Loop contain original file fingerprints and adaptation notes, not original conversations. Learning Loop's record example is synthetic. Its operational records belong in private project storage outside the distributed package.
- The private source map, source paths, scratch material, and installed local copies are excluded from publication. The repository ignores `.agent-learnings/` as an additional accidental-commit guard; ignore rules do not remove files already tracked elsewhere.

Pattern checks and editorial inspection can miss secrets or identifying context. This report records the checks and findings actually obtained, not a guarantee of exhaustive detection. Repeat the review when importing new source content.

Final follow-up screening covered 96 release-candidate text files, including all 74 skill files. Only intentional detection patterns and synthetic test examples matched the private-path/contact-data checks. Future repository commits use the public maintainer handle with a GitHub noreply address. Clean current files do not establish that historical copies or commit metadata have been removed.
