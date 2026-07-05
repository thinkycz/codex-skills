# Example Output

```md
# Delivery Tracker Summary

- Source summary: `/docs/specs/2026-03-22-billing-sync-summary.md`
- Active plan: `/docs/plans/2026-03-22-billing-sync-plan.md`
- Active tracker: `/docs/progress/2026-03-22-billing-sync-progress.md`

## Current State

- Phase 1: verified
- Phase 2: active
- Phase 3: deferred pending vendor webhook credentials

## Active Slice

- Implement retry handling for failed sync jobs
- Add verification notes for webhook signature failures

## Blockers

- Production webhook secret is still unavailable

## Evidence Linked

- Targeted retry tests pass
- Browser smoke check for the admin sync history view completed

## Next Recommended Slice

- Resume vendor integration work after credentials are available
```
