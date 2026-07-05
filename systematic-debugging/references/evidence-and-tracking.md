# Evidence And Tracking

Keep debugging traceable by separating raw observations from conclusions.

## Debug Journal

Create this in `/docs/debugging/YYYY-MM-DD-<topic>-debug-journal.md`.

Suggested structure:

```md
# <Topic> Debug Journal

## Symptom
## Reproduction
## Evidence
## Working Theory
## Checks Run
## Hypotheses Rejected
## Current Hypothesis
## Next Probe
```

Rules:

- Record what was actually observed, not what you expected.
- Keep failed hypotheses visible; they prevent repeated dead ends.
- Update the current hypothesis when new evidence changes the picture.

## Debug Tracker

Use this when the investigation has multiple moving parts or spans multiple subsystems.

Create this in `/docs/progress/YYYY-MM-DD-<topic>-debug-tracker.md`.

Suggested structure:

```md
# <Topic> Debug Tracker

## Status
- Current phase:
- Current hypothesis:
- Overall status:

## Checks
- [ ] reproduce issue consistently
- [ ] compare with working example
- [ ] capture boundary evidence
- [ ] prove root cause
- [ ] add failing test
- [ ] implement fix
- [ ] verify fix

## Blockers
- ...

## Notes
- ...
```

## Root Cause Summary

Create a short root-cause note once proven:

```md
# <Topic> Root Cause

## Symptom
## Root Cause
## Why It Happened
## Fix Chosen
## Regression Protection
```

Do not write the root-cause summary until the cause is actually proven.
