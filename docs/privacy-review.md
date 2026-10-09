# Publication privacy review

Review date: 2026-10-09. Scope: the eight distributable skill packages, supporting resources and fixtures, manifests, provenance, repository documentation, and publication tooling in the 1.1.0 working tree. This is a content review of the release candidate, not a forensic audit of every historical Git object or external source.

Pattern screening checked personal filesystem paths, email addresses, credential-shaped strings, private conversation references, internal service references, and potentially identifying account fields. Candidate locations and source/evaluation context were inspected. Public research citations and the intended public `krema` repository identity remain.

Findings:

- No actual credentials, personal contact details, private conversation links, or machine-specific source paths were found in the skill payloads.
- Candidate hits were synthetic fixture schemas, a package version, an `example.invalid` test email, and the publication tool's intentional private-path rejection test/pattern.
- Technical Documentation's evidence ledger included historical observations about a private documentation set and the original user's preferences. These were generalized to reusable design rationale. Its operational guidance is unchanged, and `origin.json` records the adaptation without private source locations.
- Research to Skill and Learning Loop contain original file fingerprints and adaptation notes, not original conversations. Learning Loop's record example is synthetic. Its operational records belong in private project storage outside the distributed package.
- The private source map, source paths, scratch material, and installed local copies are excluded from publication. The repository ignores `.agent-learnings/` as an additional accidental-commit guard; ignore rules do not remove files already tracked elsewhere.

Pattern checks and editorial inspection can miss secrets or identifying context. This report records the checks and findings actually obtained, not a guarantee of exhaustive detection. Repeat the review when importing new source content.
