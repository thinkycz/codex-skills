---
name: product-brainstorming
description: Shape an ambiguous product direction or run a bounded disposable experiment before commitment.
version: 2.0.0
category: product-design
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Shape an ambiguous product direction or run a bounded disposable experiment before commitment.
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

# Product Brainstorming

Select the mode from the requested outcome and current evidence. Read only that mode's reference; other modes are not prerequisites. Reuse repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers already established. Refresh only invalidated facts.

## Modes

- **shape** — Inspect known context and identify the actual unresolved decision. [Shape procedure](references/mode-shape.md).
- **prototype** — Define the uncertainty, smallest experiment, success/failure signal, timebox and disposal boundary. [Prototype procedure](references/mode-prototype.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
