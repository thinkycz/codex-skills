---
name: clarify-before-plan
description: Use when a feature spec is real enough to inspect but still needs a few high-impact clarifications before planning.
version: 1.0.0
category: product-design
sources:
  - spec-quality review and ambiguity-reduction workflows
use_when:
  - A written feature spec exists, but unresolved ambiguity could materially change planning, testing, UX, or architecture.
  - The next safe step is to ask a small number of targeted clarification questions before plan creation.
avoid_when:
  - There is no usable spec yet and the work needs initial specification first.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Clarification questions stay few, high-impact, and tied to implementation or validation consequences.
---

# Clarify Before Plan

Clarify the spec before planning when ambiguity would materially change implementation, validation, or UX behavior.

This skill sits between initial specification and technical planning. It is not a brainstorming workflow and it is not a full implementation plan. Its job is to reduce rework by resolving the highest-impact unknowns while the spec is still cheap to correct.

## Boundary

- Own a small number of high-impact clarification questions before planning.
- Do not replace `product-brainstorming` when the product direction itself is still exploratory.
- Do not replace `grill-with-docs` when the user wants a sustained one-question-at-a-time challenge against repo docs and domain language.
- Do not create the implementation plan; hand off after the blocking ambiguity is reduced.

## When To Use

Use this skill when:

- a written feature spec already exists
- ambiguity remains around behavior, data, UX, non-functional expectations, or integrations
- a few well-chosen answers would materially change planning, task decomposition, testing, or acceptance criteria

Do not use this skill when:

- there is no usable spec yet
- product direction is still exploratory and needs broader design work; use `product-brainstorming` instead
- the user wants a deep one-question-at-a-time grilling session against code, docs, domain language, or ADR tradeoffs; use `grill-with-docs` instead
- the missing detail can be safely deferred to implementation without affecting architecture or validation

## Core Workflow

1. Read the active spec first.
   - Ground in the current feature spec and any adjacent docs.
   - Do not ask questions until the current written artifact has been inspected.

2. Scan for high-impact ambiguity.
   - Check for gaps in:
     - functional scope and out-of-scope lines
     - entities, states, and lifecycle rules
     - critical journeys and error or empty states
     - non-functional requirements
     - integrations and failure modes
     - edge cases and completion signals

3. Prioritize only the questions that matter.
   - Ask at most a small handful of questions.
   - Each question should materially affect architecture, data modeling, UX behavior, task decomposition, test strategy, or compliance/security treatment.
   - Prefer concise, answerable questions over open-ended discovery prompts.

4. Encode the answers back into the spec.
   - Update the working understanding so planning starts from clarified requirements instead of chat-only answers.
   - Distinguish confirmed requirements from remaining assumptions.

5. Hand off to planning.
   - Once the key ambiguities are reduced, route into `spec-driven-development` or the appropriate planning owner.
   - If the clarification pass reveals that the plan itself needs sustained challenge against repo language or documented decisions, hand off to `grill-with-docs`.

## Output

Produce a concise clarification summary with:

- the ambiguity categories reviewed
- the few questions that matter most
- the resolved decisions
- the assumptions that remain
- the recommended next planning step

## Rules

- Ask fewer, better questions.
- Do not use clarification as a substitute for reading the spec.
- Do not ask questions whose answers would not change implementation or validation.
- Keep the workflow spec-focused rather than drifting into broad product brainstorming.

## References

Read these only as needed:

- [references/ambiguity-taxonomy.md](references/ambiguity-taxonomy.md)
  Use when deciding whether a gap is material enough to justify a clarification.
- [references/question-prioritization.md](references/question-prioritization.md)
  Use when deciding which questions to ask first and which to defer.
