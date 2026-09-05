---
name: verification-before-completion
description: Verify a completed change, assess release evidence, or prepare an executable tester handoff.
version: 2.0.0
category: quality
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Verify a completed change, assess release evidence, or prepare an executable tester handoff.
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

# Verification Before Completion

Select the mode from the requested outcome and current evidence. Read only that mode's reference; other modes are not prerequisites. Reuse repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers already established. Refresh only invalidated facts.

## Modes

- **verify** — Match each acceptance claim to evidence from the affected code and exact runtime. [Verify procedure](references/mode-verify.md).
- **readiness** — Assess evidence without changing code or deploying. [Readiness procedure](references/mode-readiness.md).
- **handoff** — Produce a tester-ready plan, not a claim that tests ran. [Handoff procedure](references/mode-handoff.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
