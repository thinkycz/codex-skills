---
name: local-tooling-maintenance
description: Safely change installed developer tools, plugins and layered local configuration within explicit scope.
version: 1.1.0
category: execution
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Safely change installed developer tools, plugins and layered local configuration within explicit scope.
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

# Local Tooling Maintenance

Map exact installations, registration layers, ownership, shared data and applicable host/project rules before mutation. Preserve user configuration, credentials and unrelated tools. Back up affected settings recoverably and redact secrets from output. Do not assume a missing configuration-guard skill exists; follow any applicable host guard when available. Synthetic configuration for an isolated authorized build may be created within permitted paths without overwriting real configuration, using no live credentials or production connections. Respect additional permission requirements. For removal, validate exact targets and prefer recoverable operations; do not recursively delete broad roots. Verify executable resolution, registrations, startup behavior and preserved shared state. Report precisely what changed, recovery path and unverified layers.

## Working evidence

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Inventory And Ownership](references/inventory-and-ownership.md): for inventory and ownership.
- [Verification](references/verification.md): for verification.
