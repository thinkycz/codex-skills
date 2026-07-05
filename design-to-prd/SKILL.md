---
name: design-to-prd
description: Turn design source material such as Figma or Google Stitch into a Product Requirements Document before implementation. Use when the agent needs to read screens, flows, and UI states from a design source, infer the intended product behavior, resolve ambiguities, and write a polished PRD under `/docs/specs/` that can hand off to planning or implementation.
version: 1.3.0
category: product-design
sources:
  - normalized design source material
  - current repo and product context
use_when:
  - A design exists but the written product document is missing or too weak for delivery.
  - The team needs a reviewable PRD before implementation planning.
avoid_when:
  - A trustworthy written spec already exists and implementation can proceed from it.
  - The design is too ambiguous and needs brainstorming before a PRD can be trusted.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The PRD distinguishes explicit design behavior from inference and unresolved ambiguity.
  - Source-of-truth conflicts are surfaced before delivery work continues.
  - The resulting PRD is written under `/docs/specs/` and is implementation-facing.
---

# Design To PRD

Use this skill when the design already exists and the missing artifact is the written Product Requirements Document.

This skill sits between visual design source material and execution. It does not implement the feature. It turns design inputs into a clear, reviewable PRD that captures product intent, flows, rules, scope, edge cases, open questions, and implementation-facing expectations.

## Core Promise

- Start from the actual design source, not a blank PRD template.
- Ground the PRD in repo and product context before writing.
- Distinguish what the design clearly specifies from what still needs confirmation.
- Ask for clarification when designs conflict with written inputs or leave important behavior ambiguous.
- Produce a polished markdown PRD under `/docs/specs/` that can hand off cleanly to planning or implementation.

## Boundary

- Own the conversion from design source material into a written PRD.
- Do not replace `product-brainstorming` when the design is too ambiguous to trust as a product source.
- Do not replace `spec-driven-development` when the written source of truth already exists and the next step is planning or execution.
- Use this skill when the missing artifact is the PRD itself, not when implementation is already underway.

## Position In The Workflow

Use this skill after design-source acquisition and before traceable implementation planning.

Typical flow:

- `figma` or `google-stitch`
- `design-to-prd`
- `spec-driven-development`

## Workflow

### 1. Gather The Right Inputs First

- Ask for the design source before drafting.
- Accept Figma links, node ids, Google Stitch project or screen ids, screenshots, exported designs, or other confirmed visual artifacts.
- If a written brief, client notes, or partial specification also exists, collect that too.
- Apply `repo-convention-discovery` before making product claims so the PRD reflects the current app, language, and adjacent flows instead of treating the design in isolation.

### 2. Normalize The Design Source

- Use `figma` when Figma is the source.
- Use `google-stitch` when Google Stitch is the source.
- Build a concise working summary of:
  - screen inventory
  - user flows and transitions
  - key states and variants
  - visible form fields and actions
  - apparent business rules or constraints
  - anything that is implied visually but not explicit

Do not treat every visual detail as a product requirement. Separate:

- clearly specified behavior
- strong inference from the design
- unresolved ambiguity

### 3. Resolve Source-Of-Truth Conflicts

- If the design conflicts with written notes, an existing spec, or current product behavior in a way that changes scope, fields, flows, or acceptance criteria, stop and ask the user which source has priority.
- If the design is too ambiguous to support a trustworthy PRD, route to `product-brainstorming` to clarify intent before writing.
- Record unresolved questions explicitly instead of hiding them in polished prose.

### 4. Write The PRD Under `/docs/specs/`

Write markdown only.

Default location:

- `docs/specs/YYYY-MM-DD-<topic>-prd.md`

Use a different path only if the user or repo conventions clearly require it.

### 5. Make The PRD Useful For Delivery

The PRD should help planning and implementation, not just summarize screens.

Include:

- summary and product goal
- target users or audience when inferable
- core flows
- functional requirements
- behavioral rules
- key states and edge cases
- non-goals or explicit out-of-scope notes when needed
- dependencies and integration considerations visible from the repo or source inputs
- open questions and assumptions
- validation or acceptance expectations

Keep the document crisp, but complete enough that `spec-driven-development` or planning can use it without re-deriving the design.

### 6. Hand Off Cleanly

- If the next step is structured implementation planning, hand off to `spec-driven-development`.
- If the next step is product clarification because the design is not trustworthy enough by itself, hand off to `product-brainstorming`.
- If the PRD is done and implementation is intentionally deferred, stop after delivering the document and the remaining open questions.

When handing off to `spec-driven-development`, treat the PRD as the normalized written source of truth unless the user says otherwise.

## Suggested PRD Structure

Use the structure and section intent in [references/prd-structure.md](references/prd-structure.md) unless the project already has a stronger house style.

## Quality Bar

- Do not hallucinate product logic from purely visual styling.
- Do not confuse layout details with requirement-level behavior unless the behavior clearly matters.
- Do not silently choose between conflicting visual and written sources.
- Prefer honest uncertainty over fake precision.
- Keep the PRD polished enough for stakeholders, but explicit enough for implementers.

## References

Read these only as needed:

- `references/prd-structure.md`
  Use for the section-by-section intent of the PRD.
- `references/source-normalization.md`
  Use for how to extract flows, rules, states, and ambiguities from visual design sources.
