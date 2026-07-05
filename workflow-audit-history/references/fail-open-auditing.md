# Fail-Open Auditing

Audit quality should improve trust, not block ordinary progress when the log is imperfect.

## Principle

If perfect audit capture is unavailable:

- continue the real work when safe
- record what is missing
- say what evidence still exists
- avoid pretending the record is complete

## Good Use

- multi-step work where some earlier context was lost
- delegated work that returned partial notes
- verification that is mostly complete but missing one supporting artifact

## Bad Use

- using "fail open" as an excuse to skip verification
- using "fail open" to ignore a material approval requirement
- using vague audit notes when specific gaps are knowable
