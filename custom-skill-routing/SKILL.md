---
name: custom-skill-routing
description: Select a workflow owner when ownership or the next delivery stage is ambiguous.
version: 2.0.0
category: orchestration
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Select a workflow owner when ownership or the next delivery stage is ambiguous.
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

# Custom Skill Routing

Select the mode from the requested outcome and current evidence. Read only that mode's reference; other modes are not prerequisites. Reuse repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers already established. Refresh only invalidated facts.

## Modes

- **route** — Use the requested outcome and authorization to choose one owner. [Route procedure](references/mode-route.md).
- **stage** — Inspect existing acceptance criteria, implemented slices, test evidence and blockers. [Stage procedure](references/mode-stage.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
