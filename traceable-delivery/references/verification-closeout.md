# Verification Closeout

Traceability is incomplete without evidence.

Before calling delivery complete:

- update the tracker
- update the matrix or mapping
- link fresh verification evidence
- record remaining gaps honestly
- confirm docs are inside the intended repository root and are tracked or visible as non-ignored files ready to commit
- record cross-repo links and repo/commit mappings, or disclose an explicitly chosen untracked docs home

## Verification Report

Suggested structure:

```md
# <Topic> Verification

## Scope Verified
## Commands Run
## Runtime Checks
## Coverage Summary
## Known Gaps
## Final Status
```

## Rule

If the docs still show stale status or missing evidence, the delivery is not fully closed out.

If the docs live outside a tracked repository or are ignored without explicit user intent, they are not a durable closeout artifact.
