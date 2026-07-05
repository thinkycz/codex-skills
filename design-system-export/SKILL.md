---
name: design-system-export
description: Use when an agreed design direction or existing frontend needs to be turned into reusable design-system artifacts such as tokens, component rules, and exportable guidance.
version: 1.3.0
category: design-quality
sources:
  - design-system extraction, tokenization, and reusable UI guidance workflows
use_when:
  - A product or design direction is stable enough to codify into reusable design-system artifacts.
  - The next useful step is exporting tokens, component rules, or system guidance rather than designing another screen.
avoid_when:
  - The design direction is still too unstable or exploratory to codify into a shared system.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The exported design system reflects real product decisions, names constraints honestly, and stays useful for downstream implementation or generation.
---

# Design System Export

Turn an existing frontend or stabilized design direction into reusable design-system artifacts instead of leaving the rules trapped in individual screens.

This skill is for extracting tokens, component rules, layout principles, and style guidance into a reusable package that can support future implementation or design generation. It should start from real product decisions, not speculative visual taste.

Use this only after the direction is stable enough to export. It should not replace `frontend-redesign-audit` for diagnosing a weak UI and it should not replace `design-fidelity-polish` for screen-level parity work.

## Boundary

- Own the extraction of stable reusable rules from a product or settled design direction.
- Do not replace `frontend-redesign-audit` when the current UI still needs diagnosis before the direction is trusted.
- Do not replace `design-fidelity-polish` when the task is still screen-level or interaction-level parity.
- Use this skill when the output should be reusable system guidance, not just a better single screen.

## When To Use

Use this skill when:

- the design direction is stable enough to codify
- an existing frontend already demonstrates reusable visual rules
- the next best step is exporting system guidance rather than designing another one-off screen

Do not use this skill when:

- the visual direction is still too exploratory or inconsistent
- the task is direct screen fidelity work rather than system extraction
- the repo has not yet settled on meaningful tokens, components, or patterns

## Core Workflow

1. Ground in the real product first.
   - Read the current implementation, design docs, and agreed visual direction.
   - Do not invent a design system in isolation from the product.

2. Extract stable rules.
   - Identify:
     - color and semantic token patterns
     - typography hierarchy
     - spacing and density logic
     - component behavior rules
     - layout rhythm and responsive conventions
     - motion stance and restraint rules

3. Separate stable system rules from one-off screen decisions.
   - Promote only reusable patterns into the system.
   - Keep special-case screen decisions out unless they truly generalize.

4. Export practical artifacts.
   - Prefer artifacts that another implementer or generation workflow can actually reuse.
   - Keep constraints and unresolved inconsistencies explicit.

5. Route to the right downstream workflow.
   - Hand off to `design-fidelity-polish` for parity work using the exported system.
   - Hand off to generation-oriented workflows when a reusable design description is the main output.

## Output

Produce a concise design-system export with:

- token direction
- component and state rules
- layout and motion principles
- explicit anti-patterns
- unresolved inconsistencies or gaps

## Rules

- Export only what is stable enough to reuse.
- Distinguish reusable rules from one-off aesthetics.
- Keep anti-patterns explicit.
- Name system constraints honestly instead of polishing over inconsistency.

## References

Read these only as needed:

- [references/export-rubric.md](references/export-rubric.md)
  Use for deciding what belongs in the design system.
- [references/artifact-shapes.md](references/artifact-shapes.md)
  Use for choosing token docs, component guidance, or generation-oriented export formats.
