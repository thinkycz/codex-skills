---
name: frontend-redesign-audit
description: Use when an existing frontend needs an audit-first redesign plan to identify generic UI problems and prioritize the highest-impact fixes.
version: 1.2.0
category: design-quality
sources:
  - audit-first redesign and anti-slop frontend quality review
use_when:
  - The product already exists but the UI feels generic, sloppy, or under-designed and needs structured diagnosis before redesign work.
  - The next best step is to identify high-impact visual and UX fixes rather than jump straight into broad redesign edits.
avoid_when:
  - A design source already exists and the main need is direct fidelity matching rather than redesign auditing.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The audit separates diagnosis, priority, and redesign recommendations instead of blending everything into vague taste commentary.
---

# Frontend Redesign Audit

Audit the existing frontend before redesigning it so the redesign work starts from diagnosis instead of taste-only reactions.

This skill is for existing products whose UI feels generic, sloppy, inconsistent, or under-designed. It does not assume a design source exists, and it does not jump straight into 1:1 fidelity work. Its job is to identify what is wrong, what matters most, and what should change first.

It is not a parity workflow. If a confirmed target design already exists, route to `design-fidelity-polish`. If the audit shows the team still needs a new design direction rather than implementation fixes, route to `product-brainstorming`.

## Boundary

- Own diagnosis and prioritization for weak existing frontends before redesign work starts.
- Do not replace `design-fidelity-polish` when a confirmed target design already drives the work.
- Do not replace `product-brainstorming` when the main problem is still choosing a new product direction rather than auditing the current UI.
- Use this skill to explain what is wrong and what to fix first, not to implement the redesign itself.

## When To Use

Use this skill when:

- the frontend already exists but feels generic, weak, or unfinished
- the team wants a redesign plan grounded in current UI problems
- the next best move is diagnosis and prioritization, not broad redesign edits

Do not use this skill when:

- a confirmed design handoff already exists and the task is direct fidelity matching
- the UI is mostly implemented and only needs exactness polish
- the problem is primarily product ambiguity rather than redesign diagnosis

## Core Workflow

1. Audit the current UI first.
   - Inspect the live or current implementation before proposing redesign direction.
   - Ground in the repo, current UX patterns, and real screen coverage.

2. Classify the problems.
   - Separate issues into:
     - layout and hierarchy
     - typography and spacing
     - state design and completeness
     - component consistency
     - motion and interaction clarity
     - generic or AI-default visual patterns

3. Prioritize high-impact fixes.
   - Identify the lowest-risk, highest-signal redesign moves first.
   - Distinguish:
     - fast wins
     - structural redesign needs
     - blocked items that require new design source or product decisions

4. Recommend the redesign path.
   - If the work needs new design direction, route to `product-brainstorming`.
   - If the implementation already mostly matches a target design and just needs fidelity work, route to `design-fidelity-polish`.
   - If the redesign should proceed directly from the audit, provide a compact redesign roadmap.

## Output

Produce a concise redesign audit with:

- surfaces reviewed
- the main UI problems found
- anti-slop or generic-pattern findings
- highest-impact fixes first
- recommended next owner or redesign path

## Rules

- Audit before proposing a redesign direction.
- Separate diagnosis from prescription.
- Prefer a prioritized redesign path over a long complaint list.
- Keep this grounded in the current product, not generic visual taste alone.

## References

Read these only as needed:

- [references/audit-rubric.md](references/audit-rubric.md)
  Use for the main redesign diagnosis categories.
- [references/prioritization.md](references/prioritization.md)
  Use for distinguishing fast wins from structural redesign work.
