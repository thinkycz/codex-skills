# Delegation Rules

## Delegate These

- bounded implementation slices
- repetitive edits
- straightforward tests
- isolated follow-up fixes
- narrow refactors with clear ownership

## Keep Local

- repo grounding
- architecture and shared contracts
- ambiguous bugs
- dependency ordering
- final integration
- final verification

## Worker Brief Must Include

- bounded behavioral goal and acceptance condition
- owned files or subsystem and forbidden areas
- prerequisite state, dependency contract, and downstream consumer
- canonical example files and non-obvious repository conventions
- generated-file policy plus canonical generator or scaffold command when applicable
- targeted checks and the exact full-project integration gate
- expected output and review mode

## Independent Gap Review

Use a fresh, read-only reviewer after integration for broad or high-risk multi-slice work. Give the reviewer the request, acceptance artifacts, integrated diff, and evidence, but not the intended verdict. Ask for missing flows, boundary failures, untested contracts, and P0/P1 blockers. Convert fixes into separately authorized worker slices; do not let the reviewer silently mutate the implementation.
