# Security policy

Report vulnerabilities privately through [GitHub private vulnerability reporting](https://github.com/krema/agent-skills/security/advisories/new). Include the affected skill or helper, revision, reproduction steps, and likely impact. Use synthetic inputs and omit live credentials or private transcripts. Do not post sensitive reports in public issues.

Security fixes target the latest main-branch version. Older releases may require upgrading; no response-time or backport guarantee is offered.

This collection distributes agent instructions and optional local Python helpers. Installing the collection does not deploy its maintainer's research schedules or enable a background observer. Review skills and executable helpers before use, and apply your agent's normal permission controls.

The publication check detects selected private-file names, machine paths, private conversation links, and credential patterns. It prints locations and categories without the matched values. It does not establish that all private data has been found or that instructions are safe. Review prose, provenance, examples, and proposed actions as well. Public maintainer identity and contact information are permitted.

If sensitive data is committed, stop further publication and assess the actual exposure. Revoke affected credentials where applicable. A normal deletion does not erase Git history or cached copies; coordinate any history rewrite explicitly with the maintainer. Automated update jobs must never bypass branch protection or rewrite history.
