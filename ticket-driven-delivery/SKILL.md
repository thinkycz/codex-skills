---
name: ticket-driven-delivery
description: Collect ticket evidence, plan or implement ticket changes, and post an explicitly requested closeout.
version: 2.0.0
category: execution
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Collect ticket evidence, plan or implement ticket changes, and post an explicitly requested closeout.
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

# Ticket Driven Delivery

Select the mode from the requested outcome and current evidence. Read only that mode's reference; other modes are not prerequisites. Reuse repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers already established. Refresh only invalidated facts.

## Modes

- **deliver** — Resolve exact tickets and repository scope, including attachments, comments and prior implementation claims. [Deliver procedure](references/mode-deliver.md).
- **intake** — Collect authoritative ticket details, dependencies, attachments and discussion before planning. [Intake procedure](references/mode-intake.md).
- **review** — Compare prior claims with diff, acceptance criteria and current evidence. [Review procedure](references/mode-review.md).
- **plan** — Build ordered ticket slices with dependencies, acceptance checks and blockers from collected evidence. [Plan procedure](references/mode-plan.md).
- **closeout** — Confirm the requested ticket and the scope of the already authorized comment. [Closeout procedure](references/mode-closeout.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
