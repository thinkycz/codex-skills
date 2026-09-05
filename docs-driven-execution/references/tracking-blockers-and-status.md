# Blockers And Status

Blockers must be explicit and searchable.

## Status Principles

- separate `blocked`, `deferred`, `cancelled`, `in progress`, and `verified`
- never silently drop blocked items from the tracker
- record why the blocker exists and what source system owns it

## Good Blocker Note

- affected user-visible surface
- missing support or dependency
- why fake completion would be misleading
- next condition that would unblock the work

## Progress Snapshot

A good progress view lets another engineer answer quickly:

- what is complete
- what is active
- what is blocked
- what was intentionally deferred
- what should happen next
