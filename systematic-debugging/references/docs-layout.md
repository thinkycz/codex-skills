# Docs Layout

Use this layout only when the investigation is repeated, multi-boundary, long-running, likely to cross context compaction, or otherwise needs a durable handoff. Keep bounded single-turn investigations inline.

Reuse existing working evidence; consult `docs-driven-execution` only for an unresolved ownership or tracking question.

This reference only covers the debugging-specific artifacts that are unique to investigation work.

## Debugging Overlays

Use the smallest durable set that keeps the work resumable. A short journal alone is often sufficient; add progress and verification files only when they have distinct ongoing value.

### `/docs/debugging/`

Prefer:

- `YYYY-MM-DD-<topic>-debug-journal.md`
- `YYYY-MM-DD-<topic>-root-cause.md`

Capture:

- symptom summary
- reproduction steps
- evidence gathered
- hypotheses tested
- proven root cause
- chosen fix direction

### `/docs/progress/`

When the debugging work is broad enough to need visible tracking, prefer:

- `YYYY-MM-DD-<topic>-debug-tracker.md`

Use this for active hypothesis and next-probe tracking rather than generic feature-phase tracking.

### `/docs/verification/`

Prefer:

- `YYYY-MM-DD-<topic>-verification.md`

Use the shared verification structure from `docs-driven-execution`, then add reproduction-before/reproduction-after details specific to debugging.
