---
name: docs-driven-execution
description: Execute an accepted multi-step plan with proportional tracking and resumable progress.
version: 2.0.0
category: execution
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Execute an accepted multi-step plan with proportional tracking and resumable progress.
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

# Docs Driven Execution

Select the mode from the requested outcome and current evidence. Read only that mode's reference; other modes are not prerequisites. Reuse repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers already established. Refresh only invalidated facts.

## Modes

- **execute** — Read the accepted plan and current evidence. [Execute procedure](references/mode-execute.md).
- **tracking** — Choose tracking by risk and resumption needs: inline for small work, one combined document for medium work, separate source/plan/tracker/evidence only where large work benefits. [Tracking procedure](references/mode-tracking.md).
- **decompose** — Split by observable vertical outcomes, dependency order and independently verifiable acceptance. [Decompose procedure](references/mode-decompose.md).
- **audit** — Record material actions, approvals, failures and evidence in the existing tracker. [Audit procedure](references/mode-audit.md).

## Boundaries

Audit, review, research and verification-plan modes are read-only. A mode change never grants authority for code edits, external messages, deployment or destructive checks. Reuse explicit authorization for the same action and scope; ask only for a material missing decision or new authority. Use inline tracking for small work, one combined document for medium work, and separate artifacts only where large work benefits. Report observed evidence separately from assumptions, blockers and unrun checks.
