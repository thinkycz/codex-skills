# Example Output

```md
# Spec Consistency Analysis

- Artifacts reviewed:
  `/docs/specs/billing-sync.md`
  `/docs/plans/billing-sync-plan.md`
  `/docs/tasks/billing-sync-tasks.md`

## Contradictions

- The spec says failed syncs must retry automatically every 15 minutes, but the task list only schedules manual retry tooling.

## Omissions

- The plan includes webhook signature verification, but there is no task covering secret rotation or failure logging.

## Drift

- The task list introduces CSV export support that is not present in the current spec or plan goals.

## Ambiguities

- "Recent sync history" is mentioned in the spec without a retention period or actor visibility rule.

## Recommended Next Action

- Route to `spec-driven-development` to refresh the plan and tasks after clarifying retry behavior and CSV scope.
```
