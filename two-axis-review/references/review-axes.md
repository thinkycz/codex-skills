# Review Axes

Keep the two axes separate until the final summary.

## Standards Axis

Use when the changed work conflicts with documented or strongly established repo practice.

Examples:

- The repo requires generated clients, but the diff hand-writes API payload types.
- Nearby code uses a shared error boundary or result type, but the diff bypasses it.
- ADRs require domain adapters at an integration edge, but external payloads leak into UI state.
- Tests violate the repo's fixture or data-builder convention.
- Lint, type, formatting, build, routing, or package conventions are broken.

Do not flag a standards issue when the standard is only personal preference or an unsupported guess.

## Spec Axis

Use when the changed work does not match the requested behavior.

Examples:

- A ticket asked for admin-only access, but the implementation exposes the route to all authenticated users.
- A PRD required mobile/web parity, but only web was updated.
- A plan called for preserving existing dirty worktree changes, but the diff overwrote unrelated edits.
- A backend contract says a field is optional, but the frontend treats it as required.
- The feature implements extra behavior outside the agreed scope.

## Report Shape

Start with actionable findings:

```text
Standards
- [P1] path/to/file.ts:42 - The diff bypasses the repo's shared API client, so auth refresh and error mapping no longer match documented conventions.

Spec
- [P0] path/to/file.tsx:88 - The requested role gate is missing; non-admin users can still reach the protected action.
```

Then add open questions, test gaps, and a short summary. If an axis is clean, say so explicitly.
