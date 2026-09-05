---
name: frontend-design
description: Audit an existing frontend, implement confirmed visual changes, or export stable design rules.
version: 1.0.0
category: design-quality
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Audit an existing frontend, implement confirmed visual changes, or export stable design rules.
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

# Frontend Design

Select the mode from the requested outcome and current evidence. Read only that mode's reference; other modes are not prerequisites. Reuse repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers already established. Refresh only invalidated facts.

## Modes

- **audit** — Inspect representative screens, interaction states and canonical in-product examples. [Audit procedure](references/mode-audit.md).
- **implement** — Use confirmed design intent and canonical repository components. [Implement procedure](references/mode-implement.md).
- **export** — Extract stable, agreed rules from real components: tokens, typography, spacing, states, accessibility and usage boundaries. [Export procedure](references/mode-export.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
