# Matrices And Trackers

Use a matrix when the work must be traceable from source to implementation.

## Matrix Shapes

Examples:

- requirement -> phase -> tasks -> verification
- figma frame -> route/state interaction -> implementation status -> fidelity status
- module -> backend support -> blocker status -> verification

Use stable IDs or names so the mapping survives edits.

## Phase Tracker

Suggested structure:

```md
# <Topic> Tracker

## Status
- Current phase:
- Overall status:
- Last updated:

## Phase 1: <name>
- Goal:
- Status:
- Current State:
- Remaining:
- Blockers:
- Fidelity Status:
- Next Recommended Slice:

## Decisions
- ...

## Deferred
- ...

## Next
- ...
```

## Rules

- keep phases vertically meaningful
- keep remaining work short and actionable
- reflect status changes immediately after a meaningful slice
- when the work is design-driven, distinguish route coverage, parent-state coverage, traversability, fidelity polish, and verification instead of collapsing all of them into “implemented”
