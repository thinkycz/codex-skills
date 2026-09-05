---
name: subagent-driven-development
description: Coordinate explicitly permitted bounded worker tasks with lead-owned integration and verification.
version: 1.5.0
category: orchestration
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Coordinate explicitly permitted bounded worker tasks with lead-owned integration and verification.
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

# Subagent Driven Development

Delegate only when permitted by the host/user and when an independent bounded task leaves useful local work for the lead. Do not spawn a worker merely to restate a question. Reuse existing discovery in briefs: repository identity, acceptance, canonical examples, owned files, interfaces, required checks and blockers. Avoid overlapping edits, shared test databases and fixture races. Choose capability proportional to risk within allowed model settings; never invent a model override. The lead retains decomposition, integration review, final repository gates and truth of completion claims. Independently review high-risk results where warranted; a worker report is evidence to inspect, not proof of completion.

## Working evidence

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Capability Selection](references/capability-selection.md): for capability selection.
- [Delegation Ladder](references/delegation-ladder.md): for delegation ladder.
- [Delegation Rules](references/delegation-rules.md): for delegation rules.
- [Integration Review](references/integration-review.md): for integration review.
- [Lead Vs Worker](references/lead-vs-worker.md): for lead vs worker.
- [Parallel Safety](references/parallel-safety.md): for parallel safety.
- [Worker Brief Template](references/worker-brief-template.md): for worker brief template.
