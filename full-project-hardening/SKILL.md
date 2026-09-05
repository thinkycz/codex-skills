---
name: full-project-hardening
description: Audit an existing product comprehensively or inspect architecture/migration risk; remediate only when requested.
version: 2.0.0
category: quality
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Audit an existing product comprehensively or inspect architecture/migration risk; remediate only when requested.
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

# Full Project Hardening

Select the mode from the requested outcome and current evidence. Read only that mode's reference; other modes are not prerequisites. Reuse repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers already established. Refresh only invalidated facts.

## Modes

- **audit** — Build a risk-based map across architecture, authorization, data integrity, contracts, runtime flows, UI and release evidence. [Audit procedure](references/mode-audit.md).
- **architecture** — Inspect interface depth, information hiding, locality of change and ownership. [Architecture procedure](references/mode-architecture.md).
- **migration** — Inventory source/target behavior, compatibility requirements, data transformations, deployment ordering and rollback constraints. [Migration procedure](references/mode-migration.md).
- **remediate** — Remediate only the authorized audit scope in verifiable slices. [Remediate procedure](references/mode-remediate.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
