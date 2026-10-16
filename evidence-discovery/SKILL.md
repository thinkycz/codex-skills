---
name: evidence-discovery
description: Research bounded questions, compare exact options, discover repository conventions or explain current product capabilities to clients. Separate source facts, runtime observations and inference.
version: 1.2.0
category: orchestration
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Research a bounded question, discover repository conventions or prepare an evidence-backed client product explanation.
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
- **explain** — Map current product/admin capabilities to user workflows for a client. [Explanation procedure](references/mode-explain.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
