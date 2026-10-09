# Contributing

Open an issue to propose a new skill or explain a concrete problem with an existing one. Pull requests should describe the affected task, the change, and the checks actually performed. Preserve useful conditions, exceptions, citations, and recovery guidance.

Current skills are synchronized from the maintainer's local research packages. Coordinate changes to these skills with the maintainer so the source package receives the same change. The importer refuses to overwrite public files that differ from its last recorded export.

New skills should have a descriptive kebab-case directory and matching `name` in `SKILL.md`, a useful `description`, and relative resource links. Keep instructions focused on observable task decisions. Evidence is welcome; unsupported claims of measured improvement are not.

Before submitting:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s skills/skill-refinement/evals -p 'test_*.py' -v
```

See [maintenance](docs/maintenance.md) for generated files and synchronization. If you change a synchronized skill directly, its provenance checks will intentionally fail until the maintainer reconciles the local source and regenerates the export. Do not fabricate source hashes to make checks pass.
