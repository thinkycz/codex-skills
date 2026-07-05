# Rollback And Rollout

Use this when a migration needs sequencing advice.

## Questions

- Can the change be shipped incrementally?
- What has to move together?
- What would a rollback require?
- Which verification evidence is needed before wider rollout?

## Rule

- Prefer migration plans that fail narrowly and verify progressively over all-at-once cuts unless the architecture truly requires it.
