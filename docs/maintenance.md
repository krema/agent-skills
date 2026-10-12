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
6. Increment `VERSION` for distributable changes and run `python3 scripts/catalog.py`. Use patch releases for compatible fixes and evidence maintenance, minor releases for compatible capabilities, deprecations, or approved new skills, and major releases for breaking identifier or contract changes. Compare required inputs, supported environments, output contracts, defaults, and side effects; Markdown instructions are product content, not automatically documentation-only changes. Include the before/after behavior and version rationale in the PR. Update `CHANGELOG.md`. When amending an unmerged PR, keep its pending release version unless the scope requires a larger bump.
7. Run structural validation, importer tests, and relevant skill tests. For plugin-layout changes, repeat native installation smoke tests. Review the final diff, including provenance. Do not equate installation checks with behavioral effectiveness.
8. Push a regular commit to the update branch and create or refresh one PR against `main`. Its description lists skill changes, evidence changes, checks, skipped packages, and remaining limitations. No force pushes, automatic merges, or publication to `main` by this job.

When nothing changed, do not create empty commits, releases, or PRs. Keep private screening notes outside the public repository. Existing source packages and user installations are not changed by publication.

## Commands

```sh
python3 scripts/sync_skills.py /path/outside/repository/sources.local.json
python3 scripts/sync_skills.py /path/outside/repository/sources.local.json --write
python3 scripts/catalog.py
python3 scripts/check_publication.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s skills/skill-refinement/evals -p 'test_*.py' -v
```

Only the source-map file contains machine-specific paths. `provenance.json` is public and deterministic: original names, titles, transformation description, and per-file SHA-256 values. It deliberately contains no timestamps that would create daily changes without content changes.

## Distribution manifests

`VERSION` and `scripts/catalog.py` generate all six manifests. Edit the generator instead of manually maintaining three independent catalogs. All point to the same repository-root plugin and `skills/` tree. The platform-specific manifest locations preserve compatibility with clients using the established Claude, Codex, and Copilot formats.

No hooks, MCP servers, accounts, or credentials are bundled. The Codex marketplace's `ON_INSTALL` policy follows its catalog schema; this skills-only plugin declares no authentication integration.

## Curated adaptations

All packages with an `origin.json` are maintained as separate portable source packages outside this repository, including privacy-reviewed adaptations. Their original source fingerprints and intentional changes are recorded in each package's `origin.json`. The importer hashes the curated source; it does not silently regenerate it from the original installed skill. Reconcile upstream changes and revalidate the adaptation before synchronizing. Ticket Craft derives from Write Work Item Descriptions and includes focused authoring corrections.

Only approved additions belong in the private source map. New packages do not automatically receive research schedules. The daily publication job can collect completed changes from these mapped packages using the same review process.

Before publication, inspect both file contents and the pending commit’s author/committer identity. The intended public identities krema, André Kremser, and gestro@krema.dev are allowed; a GitHub noreply address is also allowed. Verify the intended commit identity before pushing. File-level checks do not inspect Git identities. Do not rewrite published history as part of the recurring update job.

## Protected publication workflow

The main branch requires a pull request, a passing `validate` check from GitHub Actions, an up-to-date branch, and resolved review conversations. Force pushes and branch deletion are blocked, including for administrators. Independent approvals are not mandatory for this solo-maintainer repository; CODEOWNERS requests the maintainer's review of contributions. The daily publication job prepares PRs and does not merge them. Merges use squash commits; merged branches are deleted automatically. Release tags matching `v*` cannot be deleted or rewritten.

Validation uses read-only permissions, checkout without persisted credentials, pinned Actions revisions, and a bounded job runtime. Dependabot proposes weekly updates to the Actions pins. Repository policy permits only the two Actions used by this workflow. Changes needing another external action require an explicit allowlist update after review. Binary assets or symlinks require an explicit publication-check change and review before introduction.

The publication check reports selected path, link, filename, and credential patterns without exposing matched values. It complements GitHub secret scanning and push protection; contextual privacy review is still required. Run it on the staged/tracked publication files before pushing. A clean result is not proof of absence of private details.

## Automatic GitHub releases

The collection PR is the only version owner. GitHub Actions publishes its approved stable `vMAJOR.MINOR.PATCH` version after successful validation on `main`. `VERSION` supplies the tag and its unique, nonempty `CHANGELOG.md` section supplies the notes. The tag targets the exact validated commit. GitHub supplies source ZIP and tar archives; no additional installer bundle is generated. No separate commit-message-driven version writer is used.

### Version and artifact checks

`python3 scripts/release_policy.py --base origin/main` compares committed HEAD with the supplied baseline; it does not inspect uncommitted edits. Run it after preparing the local commit and before pushing. CI compares its tested checkout with the PR base or the push event's previous commit; manual dispatch compares with the parent. Checkout retrieves full history for these comparisons. An initial branch push without a baseline fails for explicit review.

Distribution scope is `skills/`, `.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/`, `.github/plugin/`, `LICENSE`, and `provenance.json`. Content, filenames, additions, deletions, and file modes count. Changed distribution content requires a new version; decreasing versions and editing the notes of an unchanged version fail. Internal repository scripts, CI and human maintenance docs can change without a collection bump. This scope describes the installed plugin; GitHub's source archive also contains repository tooling. A new distributed resource location must be added to this policy in the same reviewed change.

The existing catalog validator checks all six manifests against VERSION. The release policy checks progression and consistency, not whether a behavioral change deserves patch, minor, or major. That decision remains part of the reviewed collection PR. Recompute pending proposals against current main after concurrent merges.

### Trusted publication and queueing

Only the release job receives `contents: write`; PRs retain read access and never publish. The job depends on validation and checks the event, main ref, and checkout SHA. Main workflow runs have distinct concurrency groups; only superseded PR runs may be cancelled. Release jobs share a non-cancelling `queue: max` group. The GitHub queue holds up to 100 pending jobs; enqueue order does not guarantee commit order. The publisher prevents an older backfill from replacing a newer stable release as Latest. See [GitHub concurrency](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency).

Existing stable releases are skipped only after verifying their tag, ancestry, distribution content, version, and notes against the candidate. A later internal-only commit may reuse the same released content. A mismatched artifact, unrelated tag history, missing tag, draft, or prerelease stops publication. A tag without a release is reusable only at the exact validated candidate commit. API errors are failures, never evidence that a release is absent. After creating a release, the publisher re-reads the release and tag and verifies them before reporting success.

### Recovery

The first merge enabling this workflow publishes the current version if missing. Nothing is backfilled from pre-automation history automatically. The publisher reports missing earlier versions introduced since automation began, with their commits, as Actions warnings. Inspect these warnings and failed or cancelled runs; queueing is bounded and cannot replace recovery.

For an interrupted run, inspect its tag/release state and rerun the original main workflow at the original commit; do not substitute today's main for an older missed version. If that run's validation failed, fix the issue through a new PR rather than bypassing checks. A manual dispatch on main validates and publishes the version currently on main only. A partial tag at the correct candidate commit can be completed; conflicting tags are never moved. Older backfills explicitly use `--latest=false`. See [GitHub CLI release creation](https://cli.github.com/manual/gh_release_create).

No personal access token, additional external Action, direct main write, automatic merge, or force-push is needed. Tag protections remain in place. Offline tests use real temporary Git repositories and mocked GitHub responses; they do not establish live queue saturation behavior or successful publication. PR CI validates the workflow; actual release execution occurs only after an approved merge.
