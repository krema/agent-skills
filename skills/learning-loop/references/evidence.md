# Evidence and design limits

Reviewed 2026-10-09. This is an engineering adaptation of an existing Copilot workflow-learning package, not an empirical study of continuous learning. Original file fingerprints and the adaptation scope are recorded in [origin.json](../origin.json). No original transcripts or private observations are distributed.

| Decision | Basis | Limit and check |
| --- | --- | --- |
| Separate observation, proposal, application, and validation | Retained design from the source package; engineering judgment | State labels do not prove behavior. Inspect the artifact and a relevant execution result. |
| Keep the core independent of host event formats | Portability design objective; interface differences | The neutral record contract is new design, not a universal host schema. Test adapters separately. |
| Distinguish turn completion from session termination | [Claude Code hook lifecycle](https://code.claude.com/docs/en/hooks), relevant lifecycle section inspected on the review date | Claude documents per-turn and per-session events. This does not establish transcript completeness or identical semantics elsewhere. |
| Consult each host's actual event reference | [GitHub Copilot hooks reference](https://docs.github.com/en/copilot/reference/hooks-reference), reference page inspected on the review date | Host-specific integration is optional and not implemented or validated by this package. |
| Require outcome evidence and preserve contradictory observations | Retained source design and engineering judgment | Repeated correlation is not proof of cause; no measured effectiveness gain is claimed. |
| Use minimal private records, stable IDs, and durable checkpoints | Engineering choices for privacy and replay recovery | Redaction is fallible; no automatic exhaustive secret detection is supplied. Operational adapters need failure tests. |
| Apply only within authorization and reconcile current targets | Retained source design; user scope | Frequency of feedback does not grant permission or justify broader scope. |

The original package's broader bibliography has not been revalidated for this adaptation and is not presented as fresh evidence. No claim of guaranteed capture, autonomous improvement, or model weight training follows from these instructions. Refresh this design when real trials show mistaken generalization, missed feedback, harmful rule accumulation, or changed host interfaces.
