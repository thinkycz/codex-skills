---
name: migration-risk-audit
description: Use when an upgrade, migration, or broad refactor needs a read-only risk audit before code changes begin.
version: 1.1.0
category: quality
sources:
  - migration planning, shared-risk discovery, and rollout-aware preflight audits
use_when:
  - A framework, dependency, architecture, or broad refactor may create hidden breakpoints that should be mapped before implementation.
  - The team needs a migration preflight focused on risk, blast radius, and verification scope.
avoid_when:
  - The work is a small localized change with no meaningful migration or upgrade surface.
  - The main need is module-depth, seam, or locality improvement rather than rollout risk; use architecture-deepening-audit.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The audit inventories shared breakpoints, rollout hazards, and verification needs before changes begin.
---

# Migration Risk Audit

Audit upgrade and migration risk before changing code.

This skill is a read-only preflight for upgrades, broad refactors, framework migrations, and shared-layer changes. It maps blast radius, shared breakpoints, rollout hazards, and verification needs so the work does not start blind.

## When To Use

Use this skill when:

- a migration, upgrade, or broad refactor could affect many surfaces
- hidden shared dependencies or breakpoints would be costly to discover late
- the team needs a risk map before implementation starts

Do not use this skill when:

- the change is small and localized
- the next step is already a safe, narrow implementation slice
- the task is a debugging investigation rather than migration planning
- the dominant question is architecture depth, shallow modules, leaky seams, or low-locality abstractions; use `architecture-deepening-audit`

## Core Workflow

1. Ground in the migration surface.
   - Identify the framework, dependency, architecture, schema, or shared-layer change being proposed.
   - Inspect the codebase for reuse, wrappers, adapters, and likely blast radius.

2. Inventory breakpoints.
   - Look for:
     - shared components or helpers
     - config coupling
     - build or runtime assumptions
     - schema or serializer dependencies
     - user-visible flows likely to regress

3. Classify risk.
   - low-risk local changes
   - shared-layer hazards
   - rollout or sequencing risk
   - verification-heavy areas
   - blocked or unknown areas that need more evidence first

4. Recommend the migration shape.
   - Propose the safest decomposition, rollout order, and verification focus.
   - Make explicit what should stay read-only until more evidence exists.
   - Hand off to `systematic-debugging` when the audit uncovers an active failure that needs root cause before migration continues.
   - Hand off to `release-readiness` only after implementation and verification evidence exist for a go/no-go decision.

## Output

Produce a concise migration audit with:

- migration surface reviewed
- likely blast radius
- major breakpoints and hazards
- sequencing or rollout advice
- verification priorities before and after implementation

## Rules

- Keep the audit read-only.
- Prefer real reuse evidence over imagined risk.
- Focus on shared hazards and rollout traps, not exhaustive minor concerns.
- Make the verification burden explicit before code changes start.

## References

Read these only as needed:

- [references/risk-rubric.md](references/risk-rubric.md)
  Use for blast radius, dependency, rollout, and verification checks.
- [references/rollback-and-rollout.md](references/rollback-and-rollout.md)
  Use when migration sequencing or fallback posture matters.
