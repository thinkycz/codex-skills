---
name: evidence-discovery
description: Answer a bounded research question or discover repository conventions before a concrete decision.
version: 1.0.0
category: orchestration
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Answer a bounded research question or discover repository conventions before a concrete decision.
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

# Evidence Discovery

Select the mode from the requested outcome and current evidence. Read only that mode's reference; other modes are not prerequisites. Reuse repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers already established. Refresh only invalidated facts.

## Modes

- **repository** — Identify repository, relevant changes and applicable project instructions. [Repository procedure](references/mode-repository.md).
- **research** — Define the question and search the narrowest authoritative source first. [Research procedure](references/mode-research.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
