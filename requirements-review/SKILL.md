---
name: requirements-review
description: Review requirements, compare specification artifacts, or resolve material ambiguity before planning.
version: 1.0.0
category: quality
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Review requirements, compare specification artifacts, or resolve material ambiguity before planning.
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

# Requirements Review

Select the mode from the requested outcome and current evidence. Read only that mode's reference; other modes are not prerequisites. Reuse repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers already established. Refresh only invalidated facts.

## Modes

- **review** — Review the supplied prompt or document against clarity, completeness, consistency, verifiability, exceptions and scope. [Review procedure](references/mode-review.md).
- **compare** — Compare specification, plan, tasks and acceptance checks bidirectionally. [Compare procedure](references/mode-compare.md).
- **clarify** — Ask only questions that materially change scope, architecture, safety or acceptance. [Clarify procedure](references/mode-clarify.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
