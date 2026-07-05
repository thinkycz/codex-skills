---
name: grill-with-docs
description: Stress-test a plan through a deep one-question-at-a-time grilling session grounded in the repo, domain language, CONTEXT.md, and ADRs. Use when the user wants to challenge a plan against code, docs, terminology, tradeoffs, and documented decisions before implementation.
version: 1.1.0
category: planning
sources:
  - local repo code, docs, CONTEXT.md, CONTEXT-MAP.md, and ADRs
  - adapted grill-with-docs workflow from /Users/longdo/Downloads/skills-main
use_when:
  - The user asks to grill, stress-test, challenge, or harden a plan before implementation.
  - A plan or design exists and needs deeper interrogation against repo reality and domain language.
avoid_when:
  - Only a few high-impact ambiguities need clearing before planning; use clarify-before-plan instead.
  - The task is active implementation from an approved plan; use docs-driven-execution or the relevant owner skill.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Repo-discoverable answers are explored before asking the user.
  - Material questions use the native interactive user-input tool when available and suitable.
  - Questions are asked one at a time and include a recommended answer.
  - Plans are grilled for lifecycle success signals, hard enforcement layers, and handoff-only work.
  - Terminology and durable decisions are captured only when mutation is allowed and the decision is worth preserving.
---

# Grill With Docs

Interrogate a plan until it is precise enough to trust.

Use this skill when the user already has a plan, design, ticket batch, or proposed implementation shape and wants it challenged against the existing codebase, project language, and documented decisions.

This is deeper than `clarify-before-plan`: it is a grilling session, not a short ambiguity pass. It is not an execution skill; once the plan is hardened, hand off to `spec-driven-development`, `task-decomposition-and-resume`, or `docs-driven-execution` as appropriate.

## Boundary

- Own deep plan interrogation against repo code, domain language, docs, scenarios, and durable decisions.
- Do not replace `clarify-before-plan` for a small number of high-impact clarification questions.
- Do not execute implementation work from the hardened plan.
- Do not replace `release-readiness` or `verification-before-completion` after implementation is complete.

## Core Promise

- Explore repo facts before asking questions the repo can answer.
- Walk the decision tree one branch at a time.
- Ask one question at a time, with a recommended answer, using native interactive user input when available and suitable.
- Challenge fuzzy, overloaded, or conflicting terminology.
- Check claims against code, `CONTEXT.md`, `CONTEXT-MAP.md`, and ADRs.
- Distinguish immediate success signals from full lifecycle success.
- Find the hard enforcement layer for important constraints, not just prompt guidance.
- Capture domain terms or ADRs only when the session has resolved something durable and file mutation is allowed.

## Workflow

### 1. Ground In Existing Material

- Read the plan, ticket, PRD, spec, or design summary being grilled.
- Apply `repo-convention-discovery` when repo shape, module ownership, tests, commands, or implementation conventions affect the plan.
- Look for `CONTEXT-MAP.md`, root or context-local `CONTEXT.md`, and `docs/adr/` before debating terminology or irreversible choices.
- If multiple contexts exist and the relevant context is unclear after exploration, ask the user to choose the context before recording terms.

### 2. Build The Question Tree

- Identify the decisions that could materially change implementation, UX, data shape, migration risk, test strategy, rollout, or verification.
- Order questions by dependency: ask the question whose answer unlocks the next branch.
- Do not dump the whole questionnaire at once.
- In Plan Mode, prefer `request_user_input` for material user decisions when the tool is available and the question fits a multiple-choice shape.
- When using `request_user_input`:
  - ask exactly one decision at a time
  - provide 2-3 meaningful mutually exclusive options
  - put the recommended option first and label it as recommended
  - use `autoResolutionMs` only for non-blocking questions where continuing with the recommended default is safe
  - omit `autoResolutionMs` when the answer is required before the plan can be trusted
- Fall back to concise plain-text only when the native tool is unavailable, the question cannot reasonably be expressed as multiple choice, or the active mode does not support the tool.

### 3. Grill One Question At A Time

For each question:

- state the uncertainty
- summarize any repo or docs evidence already found
- provide the recommended answer
- wait for the user's answer before moving to the next decision

If a question can be answered by code, docs, tests, schemas, or existing artifacts, inspect those sources instead of asking.

### 4. Challenge Language And Scenarios

- If the user uses a term that conflicts with `CONTEXT.md`, call out the conflict immediately.
- If a term is fuzzy or overloaded, propose a canonical term and an avoid-list.
- Stress-test relationships with concrete scenarios, especially edge cases that expose unclear ownership, state transitions, permissions, or lifecycle boundaries.
- Ask what full success means beyond the immediate response or UI event, especially for async or multi-step flows.
- Ask where important constraints are enforced if the plan, model, or user input is wrong: schema, service, validator, policy, queue worker, test guardrail, or operational check.
- Check whether the repository needed to implement a claimed fix is actually present. If it is missing, classify the item as handoff-only instead of implying it was implemented.
- Ask whether the plan needs a regression guardrail, diagnostic command, or explicit operational verification step.
- Cross-check important claims against code. If code and plan disagree, ask which source should change.

### 5. Capture Durable Outcomes Carefully

When mutation is allowed and the decision has crystallized:

- Add resolved domain language to the right `CONTEXT.md` using `references/context-format.md`.
- Keep `CONTEXT.md` to domain terms only; do not turn it into a spec or implementation notebook.
- Offer or create an ADR only when the decision is hard to reverse, surprising without context, and the result of a real tradeoff. Use `references/adr-format.md`.
- If mutation is not allowed, report the proposed docs updates in the handoff instead of editing files.

## Output

During the session, keep the conversation focused on the current question.

At the end, produce a compact closeout with:

- resolved decisions
- remaining assumptions or open questions
- any terminology added or proposed
- any ADRs added or proposed
- the recommended next owner skill for implementation or further planning

## Rules

- Explore first, ask second.
- Ask one question at a time.
- Provide a recommended answer for every question.
- Prefer native interactive user input for material Plan Mode decisions when available and suitable.
- Do not batch unresolved decisions into a giant checklist.
- Do not record secrets, private URLs, or one-off client facts in reusable docs.
- Do not create docs just because directories are missing; create them lazily when there is something durable to capture.
- Do not use this skill as a substitute for implementation, debugging, or final verification.

## References

Read these only as needed:

- [references/context-format.md](references/context-format.md)
  Use when resolved domain language should be captured in `CONTEXT.md`.
- [references/adr-format.md](references/adr-format.md)
  Use when a decision is durable enough to record as an ADR.
