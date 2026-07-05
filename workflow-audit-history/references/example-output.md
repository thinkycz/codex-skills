# Example Output

```md
# Workflow Audit Summary

## Actions Taken

- Read the active rollout plan and progress tracker.
- Implemented the API pagination fix in the admin list view.
- Ran the targeted test suite and browser smoke check.

## Approvals

- Product owner approved shipping the pagination fix before the export follow-up work.
- Lead agent approved delegating verification to a worker after the code path was stable.

## Explicit Gaps

- No durable record exists for the first failed attempt before the fix branch was recreated.
- Browser verification covers Chrome only; Safari evidence is still missing.

## Current Evidence

- Targeted tests pass for pagination and empty-state handling.
- Progress tracker shows the export follow-up as deferred, not completed.

## Recommended Next Step

- Route to `verification-before-completion` for cross-browser evidence before handoff.
```
