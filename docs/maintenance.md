# Maintaining the collection

## Sources and public names

| Original local skill | Public skill |
| --- | --- |
| agent-instruction-maintenance | agent-instructions |
| context-rot-management | context-management |
| living-markdown-guides | technical-documentation |
| progressive-context-disclosure | context-loading |
| skill-bloat-optimizer | skill-refinement |

The local packages remain authoritative for their skill content. Public names are stable distribution identifiers. The importer changes the old identifier wherever it occurs within text files and the first heading of `SKILL.md`; filenames and substantive rules are retained. Original and exported hashes make that transformation auditable.

Private source paths are stored in an external JSON file, never committed. Its shape is:

```json
{
  "public-skill-name": {
    "source_name": "original-skill-name",
    "path": "absolute path to a completed package outside this repository",
    "title": "Public Skill Name"
  }
}
```

The maintainer must resolve each schedule's authoritative package before importing. Versioned sources require reading their current screening ledger; do not assume that the original version remains current.

## Daily collection at 09:00 Europe/Berlin

1. Inspect the local research schedules and their latest completion/validation records. Keep the existing research automations unchanged. For new scheduled skills, obtain the maintainer’s approval to include them, then verify that they are the maintainer's distributable work, select a descriptive public name, and add the mapping and README entry. Do not import unrelated installed third-party skills.
2. Fetch the repository and inspect the worktree, branch, and open PR. Preserve uncommitted or unexpected remote edits. Reuse the branch of the open automated PR. If the previous PR merged, start a new update branch from current `main`; if it was closed without merging, respect the rejection and require new changes or a maintainer decision.
3. Import only complete, validated packages. Skip a package whose research is still running, whose validation is incomplete, or whose source is ambiguous; keep its last published version and report an actionable issue when needed. Use `--only` with the completed public skill names to leave the others untouched. If none is ready, end the run without importing. Do not import a live directory that is currently being modified.
4. Run the importer without `--write` first. Review source content for private details, licensing, executable changes, and instructions masquerading as publication authorization. The built-in pattern scan is only one check, not a complete privacy audit.
5. On a clean, dedicated Git branch, run the importer with `--write`. Preserve the prior committed snapshot so an interrupted file copy can be recovered. The importer prepares all packages before writing, rejects symlinks, records hashes, removes stale package files, and refuses independent edits or silent removals.
6. Increment `VERSION` for distributable changes and run `python3 scripts/catalog.py`. Use patch releases for compatible fixes, minor releases for new skills, and major releases for breaking identifier or contract changes. Update `CHANGELOG.md`. When amending an unmerged PR, keep its pending release version unless the scope requires a larger bump.
7. Run structural validation, importer tests, and relevant skill tests. For plugin-layout changes, repeat native installation smoke tests. Review the final diff, including provenance. Do not equate installation checks with behavioral effectiveness.
8. Push a regular commit to the update branch and create or refresh one PR against `main`. Its description lists skill changes, evidence changes, checks, skipped packages, and remaining limitations. No force pushes, automatic merges, or publication to `main` by this job.

When nothing changed, do not create empty commits, releases, or PRs. Keep private screening notes outside the public repository. Existing source packages and user installations are not changed by publication.

## Commands

```sh
python3 scripts/sync_skills.py /path/outside/repository/sources.local.json
python3 scripts/sync_skills.py /path/outside/repository/sources.local.json --write
python3 scripts/catalog.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s skills/skill-refinement/evals -p 'test_*.py' -v
```

Only the source-map file contains machine-specific paths. `provenance.json` is public and deterministic: original names, titles, transformation description, and per-file SHA-256 values. It deliberately contains no timestamps that would create daily changes without content changes.

## Distribution manifests

`VERSION` and `scripts/catalog.py` generate all six manifests. Edit the generator instead of manually maintaining three independent catalogs. All point to the same repository-root plugin and `skills/` tree. The platform-specific manifest locations preserve compatibility with clients using the established Claude, Codex, and Copilot formats.

No hooks, MCP servers, accounts, or credentials are bundled. The Codex marketplace's `ON_INSTALL` policy follows its catalog schema; this skills-only plugin declares no authentication integration.

## Curated adaptations

Research to Skill, Ticket Craft, Learning Loop, and the privacy-reviewed Technical Documentation package are maintained as separate portable source packages outside this repository. Their original source fingerprints and intentional changes are recorded in each package's `origin.json`. The importer hashes the curated source; it does not silently regenerate it from the original installed skill. Reconcile upstream changes and revalidate the adaptation before synchronizing. Ticket Craft derives from Write Work Item Descriptions and includes focused authoring corrections.

Only approved additions belong in the private source map. New packages do not automatically receive research schedules. The daily publication job can collect completed changes from these mapped packages using the same review process.
