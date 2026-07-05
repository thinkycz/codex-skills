---
name: architecture-deepening-audit
description: Use when an existing codebase needs a read-only architecture audit for shallow modules, leaky seams, low-locality abstractions, or deepening opportunities before broad refactor work.
version: 1.0.0
category: quality
sources:
  - current repo code, CONTEXT.md, ADRs, tests, and architecture docs
  - improve-codebase-architecture workflow adapted from /Users/longdo/Downloads/skills-main
use_when:
  - The user asks to improve architecture, find refactor opportunities, make code more testable, consolidate shallow modules, or audit module depth.
  - A broad refactor should be shaped by evidence before implementation begins.
avoid_when:
  - The task is primarily an upgrade, dependency, framework, or data migration risk review; use migration-risk-audit.
  - The task is a local bug investigation or active implementation; use systematic-debugging, test-driven-development, or the implementation owner.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The audit uses repo evidence and architecture vocabulary consistently.
  - Suggestions distinguish shallow modules from deepening candidates and avoid implementation by default.
  - Handoffs to grill-with-docs, migration-risk-audit, repo-convention-discovery, or test-driven-development are explicit.
---

# Architecture Deepening Audit

Find architecture improvements before broad refactor work starts.

Use this skill when the user wants a codebase architecture audit focused on module depth, locality, interface shape, and seams. The goal is to identify which refactors would reduce concept spread, simplify tests, and concentrate behavior behind better interfaces.

This skill is read-only by default. It may produce a chat report or a temporary artifact in the OS temp directory, but it should not create repo docs, diagrams, ADRs, or implementation files unless the user explicitly asks.

## Boundary

- Own read-only architecture audits for shallow modules, leaky seams, low-locality abstractions, and deepening opportunities.
- Do not replace `migration-risk-audit` when the main concern is upgrade, rollout, dependency, data migration, or compatibility risk.
- Do not replace `repo-convention-discovery` when the user only needs to learn repo layout and local patterns.
- Do not replace `grill-with-docs` when the user wants a one-question-at-a-time challenge session for an already-written plan.
- Do not replace `test-driven-development` when the next step is implementing a deepening candidate through executable checks.

## Workflow

### 1. Ground The Vocabulary

- Read repo-level guidance such as `CONTEXT.md`, `AGENTS.md`, `README`, ADRs, architecture docs, test guides, and package boundaries when present.
- Capture domain terms the code already uses; avoid renaming concepts during the audit.
- Use [references/architecture-language.md](references/architecture-language.md) to keep terms such as module, interface, depth, seam, adapter, leverage, and locality precise.

### 2. Map Candidate Areas

- Start with `repo-convention-discovery` habits: map relevant modules, callers, tests, config, external dependencies, and domain vocabulary before judging structure.
- Look for behavior spread across many files, repeated call choreography, duplicated normalization, fragile tests, mock-heavy integration points, and modules whose interface exposes too much implementation detail.
- Separate true external dependencies from local-substitutable dependencies before proposing seams.

Use [references/deepening-rubric.md](references/deepening-rubric.md) when classifying candidates.

### 3. Test For Depth

For each promising candidate, ask:

- What interface could hide more implementation detail?
- Would deleting this module force callers to re-learn too much choreography?
- Are tests checking the stable behavior surface or the internal steps?
- Is there one adapter because a seam is hypothetical, or multiple adapters because the seam is real?
- Would a deeper interface improve locality without creating an artificial abstraction?

### 4. Explore Interface Options

- For high-value candidates, sketch two or three interface directions rather than jumping to the first refactor.
- Compare each option by caller simplicity, test surface, dependency direction, migration effort, and blast radius.
- Use `grill-with-docs` if the user wants to interrogate one chosen direction against docs, ADRs, and domain language.

Use [references/interface-design.md](references/interface-design.md) for candidate exploration.

### 5. Report And Hand Off

Produce a concise audit with:

- repo evidence inspected
- strongest deepening candidates
- shallow modules or leaky seams observed
- recommended refactor order
- risks, unknowns, and non-goals
- next owner skill

Hand off to:

- `grill-with-docs` for plan interrogation before committing to a deep refactor
- `test-driven-development` when the candidate can be protected by a new behavior-level test
- `migration-risk-audit` if the audit reveals migration or rollout risk as the dominant issue
- `spec-driven-development` or `docs-driven-execution` only after the user approves an implementation plan

## Rules

- Keep the audit evidence-based and repo-local.
- Do not create durable repo artifacts unless the user asks.
- Do not recommend abstractions only because code is duplicated; require a clearer interface, locality, or testability win.
- Do not confuse architectural depth with file size or implementation complexity.
- Do not implement during the audit.

## References

Read these only as needed:

- [references/architecture-language.md](references/architecture-language.md)
  Use for shared architecture vocabulary and anti-terms.
- [references/deepening-rubric.md](references/deepening-rubric.md)
  Use for dependency categories, seams, and test strategy.
- [references/interface-design.md](references/interface-design.md)
  Use when comparing possible deep interfaces for a selected candidate.
