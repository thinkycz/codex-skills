# Traceability And Progress

Use two core documents to keep delivery traceable:

- a requirement traceability matrix
- a phase tracker

## Requirement Traceability Matrix

Create this in `/docs/progress/YYYY-MM-DD-<topic>-traceability-matrix.md`.

Use a markdown table like this:

```md
| Req ID | Source | Requirement / Design Input | Phase | Tasks | Status | Verification | Notes |
|--------|--------|----------------------------|-------|-------|--------|--------------|-------|
| R1 | written spec | Admin can archive quiz sets | Phase 2 | T2.1, T2.2 | in progress | pending | waiting on backend field |
| D3 | figma | Results CTA stack matches node 12:44 | Phase 3 | T3.1 | verified | design-compliance.md#d3 | matched after spacing fix |
```

Rules:

- Give each row a stable ID.
- Distinguish written requirements from design requirements.
- Update status as work progresses.
- Link each requirement to a concrete phase and tasks.
- Record blockers instead of removing rows.

## Phase Tracker

Create this in `/docs/progress/YYYY-MM-DD-<topic>-phase-tracker.md`.

Suggested structure:

```md
# <Topic> Phase Tracker

## Status
- Current phase:
- Overall status:
- Last updated:

## Phase 1: <name>
- Goal:
- Status:
- Tasks:
  - [ ] ...
  - [ ] ...
- Blockers:

## Phase 2: <name>
...

## Decisions
- ...

## Deferred
- ...

## Next
- ...
```

## Phase Design Rules

- Split by vertical slice or workflow, not by abstract layer alone.
- Keep phases small enough to verify independently.
- Prefer phases that can be owned by one implementer or one coordinated subagent burst.
- Do not bury blockers inside the plan; surface them in the tracker.

## Progress Update Rules

- Update the tracker when a phase starts, stalls, completes, or changes shape.
- Keep wording factual and short.
- If a requirement is blocked, reflect that in both the matrix and tracker.
- If scope changes, record the decision instead of silently rewriting history.
