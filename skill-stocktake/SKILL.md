---
name: skill-stocktake
description: Use when auditing the local skill library for overlap, drift, stale triggers, and merge or retire candidates.
version: 1.3.0
category: skill-ops
sources:
  - local skill metadata, validator output, and package structure
use_when:
  - The problem is skill-library sprawl, overlap, or portfolio health rather than one broken package.
  - A maintainer needs an actionable audit of keep, merge, split, retire, or fix candidates.
avoid_when:
  - The task is only to validate or repair one specific skill package.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Stocktake output separates package correctness issues from portfolio-level redundancy and drift.
---

# Skill Stocktake

Audit the skill library as a portfolio, not just as a set of isolated packages.

This skill complements `skill-maintenance-and-validation`. Use it when the bigger question is whether the skill set is healthy, coherent, lean, and worth keeping in its current shape.

It does not own package repair work and it does not own bundle/export implementation. Use `skill-maintenance-and-validation` to fix one skill package. Use `cross-tool-packaging` to change how the library is exported or distributed.

## Boundary

- Own portfolio-level judgment across the skill library.
- Do not replace `skill-maintenance-and-validation` for package repair, metadata fixes, or reference cleanup in one skill.
- Do not replace `cross-tool-packaging` for export mechanics, flattened bundles, manifests, or compatibility decisions.
- Use this skill when the real question is keep, refresh, merge, split, or retire across the library as a whole.

## When To Use

Use this skill when:

- the library feels crowded, overlapping, stale, or uneven
- you need a keep, merge, split, retire, or refresh recommendation
- the question is about portfolio health, not just one broken skill
- packaging, export, catalog, or validation signals need to be interpreted at the library level

Do not use this skill when:

- the task is simply to fix one specific skill package
- validator output already identifies a straightforward package-level issue
- the work is to author a brand-new skill from scratch

## Core Workflow

1. Inventory the library first.
   - List the skills in scope, their categories, package shape, and support files.
   - Gather current validator, catalog, manifest, and export signals when those artifacts exist.
   - Include packaging and export workflows when the health question touches cross-tool distribution, flattened bundles, or compatibility drift.
   - If the library exists in mirrored editable roots, identify shared packages, root-specific packages, and any drift before recommending portfolio actions.

2. Separate correctness from portfolio quality.
   - Package correctness includes missing files, bad metadata, stale references, and broken prompts.
   - Portfolio quality includes overlap, weak boundaries, low-signal duplication, bloat, and outdated owners.

3. Check trigger and ownership overlap.
   - Identify skills whose `description`, `use_when`, or workflow body appear to compete for the same prompts.
   - Distinguish healthy handoff chains from accidental duplication.

4. Check context efficiency.
   - Flag bloated `SKILL.md` files.
   - Look for repeated checklists or repeated prose that should move to `references/`.
   - Prefer lean owner skills with reusable references over swollen core files.
   - Treat conversation-mined lessons as candidates, not automatic additions; promote only recurring reusable conventions to owner skills.

5. Produce an action-oriented portfolio decision.
   - For each notable skill or cluster, recommend one of:
     - keep
     - refresh
     - merge
     - split
     - retire
   - Explain the decision briefly and tie it to evidence.

## Output

Produce a concise stocktake report with:

- current inventory summary
- correctness issues versus portfolio issues
- major overlap or boundary findings
- context-budget findings
- recommended keep, merge, split, retire, or refresh actions

## Rules

- Do not confuse validation failures with portfolio redundancy.
- Prefer explicit handoffs over overlapping mega-skills.
- Flag repetition that should move into `references/` instead of growing `SKILL.md`.
- Keep the report actionable and prioritized.

## References

Read these only as needed:

- [references/stocktake-rubric.md](references/stocktake-rubric.md)
  Use for keep, refresh, merge, split, and retire decisions.
- [references/context-budget-heuristics.md](references/context-budget-heuristics.md)
  Use when judging whether a skill is lean, bloated, or repeating low-signal material.
