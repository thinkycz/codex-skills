---
name: spec-driven-development
description: Turn supplied specifications or designs into requirements, a PRD when needed, and authorized delivery.
version: 2.0.0
category: execution
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Turn supplied specifications or designs into requirements, a PRD when needed, and authorized delivery.
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

# Spec Driven Development

Select the mode from the requested outcome and current evidence. Read only that mode's reference; other modes are not prerequisites. Reuse repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers already established. Refresh only invalidated facts.

## Modes

- **prepare** — A sufficient inline user prompt is a valid specification. [Prepare procedure](references/mode-prepare.md).
- **prd** — Extract screens, states, flows, actors, data and business behavior from supplied design sources. [Prd procedure](references/mode-prd.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
