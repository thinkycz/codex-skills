---
name: workflow-contract-builder
description: Specify a safe recurring personal workflow before scheduling or connecting external services.
version: 1.2.0
category: product-design
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Specify a safe recurring personal workflow before scheduling or connecting external services.
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

# Workflow Contract Builder

Clarify the useful outcome, inputs, ownership and actionable output before proposing infrastructure. Define trigger/cadence, permitted reads/writes, deduplication, failure/retry limits, state storage and stopping conditions. Keep credentials and private source content out of reusable instructions. Follow host automation mechanisms; a contract request does not authorize scheduling or service connection. For monitoring, preserve notification intent: unchanged/non-actionable state stays quiet unless periodic updates were requested. Notify meaningful change, completion, failure or required user action. Distinguish a working end-to-end workflow from a dashboard or scheduler that has not delivered its actual business outcome.

## Working evidence

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Automation Contract](references/automation-contract.md): for automation contract.
