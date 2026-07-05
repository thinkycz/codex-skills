---
name: reflection-and-learning
description: Turn completed implementation, debugging, verification, or review work into durable lessons, guardrails, and reusable process improvements. Use when the work is mostly done and the agent should reflect on what happened, extract the highest-value insights, and store them in the right project artifacts without bloating chat or docs.
version: 1.1.0
category: quality
sources:
  - completed implementation, debugging, and verification artifacts
  - workspace guidance for durable learning capture
use_when:
  - Meaningful work is done enough to inspect honestly and capture reusable lessons.
  - The team wants guardrails or process improvements preserved beyond chat history.
avoid_when:
  - Verification or release readiness is still unresolved.
  - The work is too incomplete for lessons to be evidence-backed.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Lessons are backed by real evidence from completed work.
  - Storage location and audience are chosen intentionally.
  - Reflection stays concise and avoids bloating docs with low-signal recap.
---

# Reflection And Learning

Do not let useful lessons vanish into the scrollback.

Use this skill after meaningful work is complete enough to inspect honestly and extract reusable learning.

This skill is not the primary owner for verification, debugging, or release decisions. It is the follow-through step that captures what should persist after those workflows have produced real evidence.

## Core Promise

- Extract reusable lessons from real work, not hypothetical advice.
- Keep the learning loop lightweight and tied to evidence.
- Store insights in the right durable place instead of scattering them across chat.
- Avoid bloating project docs with low-value retrospectives.

## When To Use

Use this skill when:

- a feature, fix, or verification pass exposed a lesson worth preserving
- a debugging run revealed a recurring failure pattern or guardrail
- a release or review surfaced process improvements that should outlive the current task
- the user explicitly asks for reflection, lessons learned, or reusable takeaways

Do not use this skill for generic post-task praise, speculative retrospectives, or broad project management ceremony.

## Core Workflow

### 1. Reflect Only On Real Evidence

- Start from what actually happened: implementation notes, debugging evidence, verification results, review findings, or release readiness output.
- Prefer fresh artifacts over memory-based summaries.
- Ignore lessons that are obvious, generic, or unsupported by the work.

### 2. Identify What Is Reusable

Look for high-value takeaways such as:

- recurring bug patterns
- verification gaps that should become standard checks
- routing or workflow mistakes that caused rework
- project-specific conventions discovered during execution
- reusable safeguards, heuristics, or checklists

Prefer a few durable lessons over a long retrospective.

### 3. Decide The Right Home

Store the lesson in the narrowest durable place that will help future work:

- task or verification docs when the learning is task-local
- debugging or delivery docs when it explains a recurring pattern in the current project
- project memory or long-lived guidance when it should influence future tasks broadly

Do not promote a one-off lesson into global guidance unless the evidence supports it.

### 4. Write Compact Guardrails

- State the lesson in actionable language.
- Explain the trigger or condition where it applies.
- Prefer concrete guardrails over vague reflections.
- Link the lesson back to the evidence source when useful.

### 5. Close With Signal, Not Ceremony

- Summarize what was learned.
- Say where it was recorded.
- Call out what was intentionally not promoted because it was too local, too weak, or too noisy.

## Rules

- Do not invent lessons when the evidence is thin.
- Do not duplicate the full debugging, verification, or release summary.
- Do not turn every task into a retrospective.
- Do not store low-signal process notes in long-lived artifacts.
- Do not confuse reflection with reopening already-closed execution decisions.

## Handoffs

- Use `verification-before-completion` before reflection when the success claim itself is not yet proven.
- Use `systematic-debugging` when the issue is still not explained.
- Use `release-readiness` when the real question is go/no-go rather than learning capture.
- Use `skill-maintenance-and-validation` if the lesson implies a change to the skill system itself.

## References

Read these only as needed:

- `references/lesson-selection.md`
  Use for deciding which takeaways are worth preserving.
- `references/storage-decisions.md`
  Use for deciding where lessons should live and how broad they should become.
