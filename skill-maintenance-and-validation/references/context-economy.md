# Context Economy

Use this reference when a skill is growing noisy, overlapping, or too eager to load detail into the core file.

## Core Rule

- Treat context budget as a real design constraint.
- Keep only the highest-signal workflow guidance in `SKILL.md`.
- Push reusable detail, long examples, and checklists into `references/`.

## Smells

- the skill body explains basics the model already knows
- the same checklist appears across multiple skills
- one skill repeats downstream workflows instead of handing off
- metadata promises a smaller job than the body actually performs
- the core file keeps growing because the boundary is unclear

## Preferred Fixes

- shorten the core workflow to the essential decisions and steps
- move detailed heuristics into one-level-deep references
- keep one owner skill for each major workflow phase
- replace duplicated guidance with a single owner reference and a short handoff
- remove decorative prose that does not change model behavior
