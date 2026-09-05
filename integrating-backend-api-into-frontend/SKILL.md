---
name: integrating-backend-api-into-frontend
description: Connect an existing frontend to a backend API while preserving agreed product behavior.
version: 1.4.0
category: execution
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Connect an existing frontend to a backend API while preserving agreed product behavior.
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

# Integrating Backend Api Into Frontend

Reuse repository conventions and map each accepted flow to actual endpoints, auth, payloads and states. Observed API behavior is evidence of current capability; it never silently supersedes agreed requirements. Flag material conflicts and ownership. Keep required inaccessible integrations blocked unless accepted scope permits deferral. Implement authorized vertical flows with real data, error/loading/empty handling and appropriate auth/session boundaries. Confirm test database, server identity and asset/runtime freshness before browser checks. Verify visible and service-level behavior, not only request success. Track proportionally and reuse unchanged evidence. Read only the reference matching the current contract, planning, blocker, runtime or browser question.

## Working evidence

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Api Contract Mapping](references/api-contract-mapping.md): for api contract mapping.
- [Blockers And Phase Tracking](references/blockers-and-phase-tracking.md): for blockers and phase tracking.
- [Browser And Manual Qa](references/browser-and-manual-qa.md): for browser and manual qa.
- [Planning](references/planning.md): for planning.
- [Runtime Debugging](references/runtime-debugging.md): for runtime debugging.
