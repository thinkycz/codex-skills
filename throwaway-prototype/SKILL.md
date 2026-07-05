---
name: throwaway-prototype
description: Use when a design, state model, API shape, or UI direction should be tested with a deliberately disposable prototype before production implementation.
version: 1.0.0
category: product-design
sources:
  - current repo conventions and runtime commands
  - prototype workflow adapted from /Users/longdo/Downloads/skills-main
use_when:
  - The user wants to prototype, sanity-check a state model, try UI variants, or let stakeholders play with a direction before committing.
  - The fastest way to answer the question is a disposable local artifact rather than a production implementation.
avoid_when:
  - The user wants production implementation, durable docs, or a committed feature rather than learning.
  - The question can be answered with product-brainstorming, a diagram, repo inspection, or tests without writing prototype code.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The prototype is clearly marked throwaway and answers one explicit question.
  - The user gets one command or URL to run it.
  - The result is deleted, left isolated, or consciously absorbed into production after the question is answered.
---

# Throwaway Prototype

Build a disposable prototype to answer a question quickly.

Use this skill when the user needs to try a state model, workflow, API shape, or UI direction before committing to production implementation. The prototype exists to learn. It should be easy to run, easy to discard, and clearly separate from shippable code.

## Boundary

- Own short-lived prototypes for logic/state models and UI variants.
- Do not replace `product-brainstorming` when no prototype is needed to clarify direction.
- Do not replace `spec-driven-development` when the user already wants production delivery.
- Do not replace `test-driven-development` for production behavior checks.
- Do not add durable docs, migrations, fixtures, or tests for the prototype shell unless the user explicitly asks.

## Core Rules

- State the prototype question before building.
- Mark files, routes, UI labels, or output as throwaway.
- Provide one command, URL, or entry point to run it.
- Keep the reusable idea portable while keeping the shell disposable.
- After the question is answered, either delete the prototype, leave it isolated by request, or absorb the useful logic into production through the proper owner skill.

## Workflow

### 1. Pick The Branch

- Use the logic/state branch when the question is about rules, transitions, data shapes, edge cases, or workflow state.
- Use the UI variant branch when the question is about layout, interaction model, hierarchy, navigation, or stakeholder preference.
- If both apply, build the smallest prototype that answers the riskiest question first.

### 2. Logic Or State Prototype

Follow [references/logic-prototype.md](references/logic-prototype.md).

- Put reusable logic in pure functions, reducers, state machines, or small domain modules.
- Keep the runner disposable: CLI, TUI, small script, local browser harness, or temporary route.
- Show enough sample inputs, states, and edge cases to make the decision visible.
- Avoid persistence unless the prototype question is specifically about persistence.

### 3. UI Variant Prototype

Follow [references/ui-variant-prototype.md](references/ui-variant-prototype.md).

- Prefer an existing route with `?variant=` over a standalone prototype route.
- Default to three structurally different variants when the user has not specified a number.
- Keep variants hidden from production navigation.
- Reuse existing design system components and assets where practical, but do not polish beyond the learning goal.

### 4. Close The Loop

Report:

- the question answered
- how to run or view the prototype
- what was learned
- which parts, if any, are worth absorbing
- what should be deleted or left isolated

Hand off to `product-brainstorming` if the result changes product direction, `spec-driven-development` for production delivery, or `test-driven-development` when the learned behavior should become a protected production contract.

## Rules

- Do not let prototype code silently become production code.
- Do not write tests for the disposable shell.
- Do not overfit architecture around a prototype.
- Do not create a new app or route when a query-param variant on an existing surface answers the UI question.
- Do not leave the user without a concrete way to try it.

## References

Read these only as needed:

- [references/logic-prototype.md](references/logic-prototype.md)
  Use for state, reducer, workflow, and data-shape prototypes.
- [references/ui-variant-prototype.md](references/ui-variant-prototype.md)
  Use for visual, interaction, and route-variant prototypes.
