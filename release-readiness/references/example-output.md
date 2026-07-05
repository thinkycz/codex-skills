# Example Output

```md
# Release Readiness Review

- Scope reviewed: invite-flow rollout
- Verdict: not ready for release yet

## What Is Ready

- Core invite creation and acceptance flow is implemented
- Targeted tests pass for success and expired-token handling
- Progress docs are current through Phase 2

## Remaining Gaps

- Safari verification is still missing
- Admin resend flow has no fresh runtime evidence
- Deferred SSO invite variant is documented but not yet isolated clearly enough in the closeout notes

## Recommendation

- Route to `verification-before-completion` for cross-browser evidence and resend-flow proof before final release signoff.
```
