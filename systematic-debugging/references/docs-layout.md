# Docs Layout

Apply `traceable-delivery` first for the shared `/docs` layout, tracker expectations, blocker visibility, and verification closeout.

This reference only covers the debugging-specific artifacts that are unique to investigation work.

## Debugging Overlays

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

Use the shared verification structure from `traceable-delivery`, then add reproduction-before/reproduction-after details specific to debugging.
