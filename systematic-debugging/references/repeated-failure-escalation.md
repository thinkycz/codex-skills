# Repeated Failure Escalation

Use this reference when the same user-visible issue persists after a prior fix or completion claim.

## Reset The Claim

- State that the previous evidence did not prove the live outcome.
- Keep the previous hypothesis in the journal, but mark it rejected, partial, or superseded.
- Do not stack another fix on top of an unobserved runtime path.

## High-Information Evidence Ladder

Choose the earliest available probe that observes the failing boundary directly:

1. exact device, browser, worker, or server log from the failing attempt
2. direct request or command replay against the same environment and data shape
3. focused automated regression reproducing that boundary
4. rebuilt and installed artifact replaying the original user path

Move down the ladder only when the earlier probe cannot establish the cause or prove the fix.

## Exact Artifact Check

Record the facts that identify what actually ran:

- source revision or diff
- build artifact and build time
- installed or deployed artifact identity when observable
- runtime, environment, database schema, migrations, and relevant feature flags
- exact request payload and response or stack trace

A successful source build does not prove that the simulator, device, browser, worker, or server is using it.

## A/B Root-Cause Check

Prefer a failing request and a control request that differ in one material input or boundary. Examples:

- payload with and without one suspect field
- request with and without an optional relationship
- deployed schema before and after one migration
- old and newly installed build against the same test data

Call the cause proven only when the observed difference matches the hypothesis and no nearer boundary explains it better.

## Closeout Rule

- `fixed`: the original path succeeds in the intended runtime or environment
- `implemented, runtime verification pending`: source and checks are green, but the running artifact was not observed
- `partially fixed`: one failure boundary was corrected, but the user's full path still has an unresolved failure
