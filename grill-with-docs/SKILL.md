---
name: grill-with-docs
description: Stress-test a plan one material decision at a time when the user asks for a grilling session.
version: 1.3.0
category: product-design
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Stress-test a plan one material decision at a time when the user asks for a grilling session.
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

# Grill With Docs

Ground challenges in the supplied plan, repository and existing context/decision records. Ask one material question at a time, explain its consequence, and use the answer to select the next question. Do not bundle a questionnaire or invent domain terminology. Check existing answers before asking. Preserve agreed decisions and capture an ADR only for a durable architectural tradeoff when authorized. This mode does not authorize implementation. Stop when consequential uncertainty is resolved or the user ends the session; do not keep questioning to satisfy a quota.

## Working evidence

When using a native question tool, obey its actual schema and offer a clearly labelled recommendation when choices are supported. Do not invent timeout/default-submission fields or treat a preselected option, elapsed time or unanswered question as authorization. An unresolved permission decision stays pending.

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Adr Format](references/adr-format.md): for adr format.
- [Context Format](references/context-format.md): for context format.
