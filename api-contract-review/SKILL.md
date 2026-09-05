---
name: api-contract-review
description: Review frontend assumptions against API schemas and observed payloads without modifying either side.
version: 1.5.0
category: quality
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Review frontend assumptions against API schemas and observed payloads without modifying either side.
avoid_when:
  - The requested outcome belongs to another owner or exceeds the authorized scope.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Evidence supports the stated outcome and limitations.
  - Selected mode, references and actions remain within authorization.
---

# Api Contract Review

Map methods, paths, auth, request/response shapes, nullability, pagination, errors and state transitions. Cite documented and observed evidence separately. Classify mismatches by user impact and ownership; current API behavior does not override agreed product requirements. Identify missing access and propose bounded validation. Stop at findings in review mode; do not patch code or mutate backend data. Read the comparison rubric for complex contracts and mismatch types when classifying findings.

## Working evidence

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Comparison Rubric](references/comparison-rubric.md): for comparison rubric.
- [Mismatch Types](references/mismatch-types.md): for mismatch types.
