# Structural checks and optional measurements

Use the analyzer after a content review, or when diagnosing packaging. It cannot optimize prose or judge whether an instruction is useful. There is no size eligibility test, bloat score, rule-density score, or automatic semantic approval.

```sh
python3 scripts/analyze_skill.py /path/to/skill --strict
python3 scripts/analyze_skill.py /path/to/AGENTS.md --json
python3 scripts/analyze_skill.py /path/to/skill --metrics --loaded references/repair.md
```

Resolve the script from this optimizer's folder. Directory mode requires SKILL.md and inventories Markdown; standalone mode inspects only the specified document. JSON schema 2 always lists inspected files and `content_review` as `required`: zero findings never completes a content review. It lists only files successfully read; unreadable files are errors. The script never edits targets.

Checks cover basic frontmatter field presence, a subset of Markdown file links outside fences, exact repeated prose, potentially unconditional reference loading, and unreachable references. Review signals can be false positives. Inline code/quotes, paraphrases, condition scope, fragments, HTML links, complex destinations, external URLs, and full YAML/CommonMark semantics are not reliably validated. A duplicated line is a candidate for inspection, not a deletion instruction. A lexical match is not evidence of semantic equivalence.

Metrics are opt-in (`--metrics`), including in JSON. Counts use Unicode characters divided by four, rounded up; they are rough estimates, particularly for code and non-English text. `--loaded` selects existing local UTF-8 files for an optional hypothetical loading scenario; it never demonstrates that a model read them. Links alone do not add referenced contents to that scenario. Files are deduplicated within the estimate.

Distinguish discovery metadata, activated instructions, and conditionally loaded content. If runtime efficiency matters, measure actual input/output/cached tokens, tool calls, elapsed time, and success on matched tasks. Caching and failed retrieval can make smaller files more expensive overall. No token, line, or character count determines content quality.

Operational limits: Python 3.10+, standard library, no network. Files over 2 MB produce an inspection error to bound I/O; this is not an optimization threshold. Symlinks are not traversed. Hidden directories, .git, .venv, node_modules, and __pycache__ are excluded. Links outside the package are review signals, not permission to read outside scope; inspect legitimate project callers separately when authorized.

Exit codes: 0 = report produced; 1 = structural errors with `--strict`; 2 = invalid target, argument, or scenario selection. Exit 0 says nothing about instruction effectiveness. Full skill-format validation is separate from this helper.
