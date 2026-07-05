---
name: requirements-checklist-review
description: Use when a written feature spec needs a checklist-style quality review before planning or implementation.
version: 1.1.0
category: quality
sources:
  - requirements quality review and checklist-based spec assessment
use_when:
  - A written spec exists and the next useful step is checking completeness, clarity, consistency, and coverage.
  - Checklist-style review would expose vague or untestable requirements before planning starts.
avoid_when:
  - There is no meaningful written spec yet to review.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Checklist findings stay focused on requirements quality, not implementation behavior.
---

# Requirements Checklist Review

Review the written spec like a test suite for requirement quality before planning or implementation begins.

This skill is for checklist-style assessment of the spec itself. It does not verify code, and it does not replace clarification or cross-artifact analysis. Its job is to expose weak requirement wording early while the document is still cheap to improve.

## When To Use

Use this skill when:

- a written spec already exists
- the next useful step is checking requirement quality before planning or coding
- the team wants a concise checklist-style report on completeness, clarity, consistency, and coverage

Do not use this skill when:

- there is no meaningful spec yet
- the real problem is still design direction or open product ambiguity
- the task is to compare multiple artifacts rather than review the spec itself

## Core Workflow

1. Read the active spec first.
   - Work from the current written artifact, not chat memory.
   - Do not ask questions until the document has been reviewed.

2. Check the spec against quality dimensions.
   - Completeness:
     are key journeys, states, and constraints present?
   - Clarity:
     is the language specific and testable?
   - Consistency:
     do the requirements agree with each other?
   - Coverage:
     are edge cases, failures, accessibility, and integrations addressed where relevant?

3. Flag only high-signal issues.
   - Focus on missing or weak requirements that would affect planning, testing, implementation scope, or acceptance.
   - Avoid nitpicks that do not materially change downstream work.

4. Recommend the right next step.
   - Route to `clarify-before-plan` when answers are still needed.
   - Route to `spec-consistency-analysis` when multiple downstream artifacts already exist.
   - Route to planning when the checklist passes cleanly enough.

## Output

Produce a concise checklist review with:

- spec reviewed
- checklist dimensions assessed
- high-impact findings
- what is clear enough
- recommended next step

Use [references/example-output.md](references/example-output.md) when the team needs a concrete example of a good checklist review shape.

## Rules

- Treat this as requirements review, not implementation verification.
- Prefer a short set of material findings over exhaustive checkbox noise.
- Keep the report actionable enough to tighten the spec quickly.

## References

Read these only as needed:

- [references/review-rubric.md](references/review-rubric.md)
  Use for the completeness, clarity, consistency, and coverage pass.
- [references/checklist-question-bank.md](references/checklist-question-bank.md)
  Use when the spec needs stronger checklist prompts before planning.
