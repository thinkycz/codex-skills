# Example Output

```md
# Requirements Checklist Review

- Spec reviewed: `/docs/specs/invite-flow.md`
- Verdict: usable after a small clarification pass

## High-Impact Findings

- Clarity:
  The invite expiry rule says "short-lived" but does not define a duration or admin override behavior.
- Coverage:
  The spec covers successful invite acceptance but not expired-token, revoked-invite, or already-member states.
- Consistency:
  The acceptance section implies email is immutable, while the admin-edit section suggests it can be changed after invite creation.

## Clear Enough To Proceed

- Roles involved are explicit.
- Success path and admin ownership are clear.
- Audit logging requirement is specific enough for planning.

## Recommended Next Step

- Route to `clarify-before-plan` for the expiry rule, failure states, and email mutability decision.
```
