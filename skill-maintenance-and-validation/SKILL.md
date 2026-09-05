---
name: skill-maintenance-and-validation
description: Review, edit, validate or export the custom skill library without touching vendor-managed packages.
version: 3.0.0
category: skill-ops
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Review, edit, validate or export the custom skill library without touching vendor-managed packages.
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

# Skill Maintenance And Validation

Select the mode from the requested outcome and current evidence. Read only that mode's reference; other modes are not prerequisites. Reuse repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers already established. Refresh only invalidated facts.

## Modes

- **edit** — Read affected instructions, metadata, supporting resources and callers. [Edit procedure](references/mode-edit.md).
- **portfolio** — Inventory entry points and descriptions, then inspect overlapping owners and real usage evidence. [Portfolio procedure](references/mode-portfolio.md).
- **export** — Run the exporter from the chosen checkout with an explicit new destination. [Export procedure](references/mode-export.md).
- **validate** — Run package and owner/mode/dependency validation, regression tests and read-only generated-artifact checks. [Validate procedure](references/mode-validate.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
