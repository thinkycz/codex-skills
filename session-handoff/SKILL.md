---
name: session-handoff
description: Resume from durable evidence, write a continuation handoff, or capture reusable lessons.
version: 2.0.0
category: execution
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Resume from durable evidence, write a continuation handoff, or capture reusable lessons.
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

# Session Handoff

Select the mode from the requested outcome and current evidence. Read only that mode's reference; other modes are not prerequisites. Reuse repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers already established. Refresh only invalidated facts.

## Modes

- **handoff** — Write a compact continuation record with objective, current repository/branch identity, changes, completed evidence, unresolved decisions, blockers and next safe action. [Handoff procedure](references/mode-handoff.md).
- **resume** — Compare tracker claims with files, Git history, current tests and runtime identity as needed. [Resume procedure](references/mode-resume.md).
- **lessons** — Extract only reusable lessons supported by the completed work: a failure mechanism, effective guardrail and where it belongs. [Lessons procedure](references/mode-lessons.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
