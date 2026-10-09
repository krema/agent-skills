# Project instructions

Work on local copies. Production changes require explicit user authorization immediately before execution. Keep tenant data isolated.

For UI changes, ensure keyboard operation and visible focus. Check narrow and wide layouts. Stylesheet conventions are in styles.md. Report checks actually performed.

Run relevant tests after code changes. Don't report unrun checks as passing.

For stored-schema changes, follow database.md. Before applying a migration to production, verify a restorable backup and a written rollback procedure. A migration affecting invoice records also follows billing export retention requirements.

Billing exports must filter by tenant and exclude payment secrets. Retain invoice IDs for audit. A user explicitly requesting anonymized analytics instead receives aggregate totals without invoice IDs. Report the export's time range.

For UI changes run relevant tests. For schema changes run relevant tests. For billing export code changes run relevant tests.
