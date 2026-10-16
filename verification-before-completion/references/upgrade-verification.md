# Fresh installation and deployed upgrades

Use when a change depends on schema evolution or works on a fresh database but fails on an existing deployment.

- Test a clean installation and an upgrade from the relevant previous schema as separate paths. Editing a historical migration already marked applied does not update an existing database; use the project's additive forward-migration convention.
- Build the old schema and representative existing records in an isolated disposable database, apply the new migration, and exercise the actual changed operation. Check the resulting columns, constraints, defaults and migration ledger. A ledger entry alone is not proof of the live schema.
- Assert preservation of relevant existing passwords, identifiers, ownership, credits, payment-provider identities and history. Include nullability changes and mixed old/new records where they affect the feature; do not reset a shared database to make tests pass.
- Confirm rollout order from the actual deployment entrypoint: compatible migration/application changes and required worker restarts. Verify the target database and worker build after an authorized deployment; successful fresh-install tests cannot establish upgrade acceptance.
- Treat records created by a failed older run separately. A schema fix does not replay a webhook, resend an email or repair ownership. Inspect original event, payment, entitlement and ownership before proposing a scoped retry; check idempotency and authorization before executing it.
