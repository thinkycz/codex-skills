---
name: test-driven-development
description: Drive implementation or bug fixing from failing tests instead of code-first changes. Use when the work can be expressed as automated checks, when regressions need protection, or when the safest path is to write or update a failing test first, make the smallest passing change, and verify the result before broader refactoring.
version: 1.3.0
category: quality-engineering
sources:
  - existing test harnesses and nearby repo test patterns
  - red-green-refactor references in this skill package
  - boundary-mocking and refactor-candidate guidance adapted from /Users/longdo/Downloads/skills-main
use_when:
  - Expected behavior can be captured meaningfully as an automated test.
  - Regression protection is part of the safest path for the requested change.
avoid_when:
  - No meaningful automated test boundary exists yet.
  - The task first needs debugging or spec clarification before the right test can be written.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The workflow starts from a meaningful failing test when practical.
  - Production changes are the smallest ones needed to turn the test green.
  - Broader nearby verification runs before completion is claimed.
  - Mocks stay at system boundaries unless the repo's established pattern requires otherwise.
---

# Test Driven Development

Use tests as the control surface for behavior changes.

This skill is for work where the intended behavior can be captured as an automated test and the safest way to move is to prove failure first, then make the minimum change that turns the test green.

## Core Promise

- Turn expected behavior into an executable failing test before relying on implementation changes.
- Keep the change loop tight: red, green, refactor.
- Prefer the smallest justified code change that satisfies the test.
- Leave behind regression protection, not just passing chat claims.

## When To Use

Use this skill when the user:

- wants behavior implemented safely with regression protection
- has a bug that can be reproduced as a test
- needs confidence while changing risky logic, state transitions, serializers, parsers, or domain rules
- is working in a codebase that already has a viable test harness for the touched surface

Do not force TDD when the behavior cannot yet be expressed meaningfully as an automated test. In those cases, use the best adjacent workflow first, then return to tests as soon as the behavior becomes testable.

## Core Workflow

### 1. Ground In The Current Test Surface

- Inspect the existing test framework, naming conventions, fixtures, helpers, and nearby test patterns before writing anything new.
- Prefer extending the closest existing test style over inventing a new harness.
- If no realistic automated test surface exists yet, note that explicitly and choose the smallest viable test boundary.

### 2. Write Or Update A Failing Test First

- Capture the intended behavior in a test before broad implementation changes.
- Make the failure meaningful:
  - the assertion should describe real behavior, not internal trivia
  - the failure should be specific enough to guide the fix
  - the test should fail for the right reason
- When fixing a bug, reproduce the bug in a failing test if the harness makes that practical.
- Be suspicious of false-green tests that pass because the assertion is weak, the fixture is unrealistic, or the wrong code path is being exercised.
- Avoid horizontal TDD batches. Do not write all planned tests first and then all implementation afterward; that tends to test imagined behavior and unstable shapes.
- Prefer a vertical tracer loop: one behavior test, the smallest passing change, then the next behavior test based on what was just learned.

### 3. Make The Smallest Passing Change

- Change as little production code as possible to satisfy the failing test.
- Avoid bundling refactors, cleanup, or architecture work into the red-to-green step unless they are required for correctness.
- If multiple behaviors are changing, add tests incrementally instead of jumping to a large implementation pass.
- When the acceptance case needs many records, specific rankings, or role/state combinations, prefer reusable factories, seeders, or fixtures that make the edge case repeatable.

### 4. Refactor Only After Green

- Once the new or updated test passes, improve structure if needed without changing behavior.
- Keep the tests green while refactoring.
- Prefer follow-up cleanups that improve readability, duplication, naming, or shared helpers when they reduce future risk.
- After green, look for duplication, shallow modules, feature envy, primitive obsession, and test surfaces that should move to a deeper interface.
- Use `references/mocking-and-refactor-candidates.md` when mock boundaries or refactor candidates materially affect the TDD loop.

### 5. Verify Beyond One Test

- Run the most relevant targeted test first.
- Then run the surrounding suite or the smallest broader scope that gives useful confidence.
- For Laravel-style repos, pair focused tests with the project's standard `make fix` or `make check` command when that is the documented confidence gate.
- If lint, typecheck, or build are materially affected by the change, run them too.
- Do not stop at a single green test if nearby behavior could have regressed.

### 6. Add AI Regression Coverage When The Failure Pattern Demands It

- When the defect came from prompt shape, parser shape, serializer shape, model output handling, or an automation state transition, look for a reusable regression test instead of treating it as a one-off bug.
- Be explicit about the risk class:
  - ordinary business-logic regression
  - integration or automation regression
  - model-behavior or structured-output regression
- If a repeated failure pattern exists, add coverage at the shared boundary that would catch the same class of bug again.
- Do not force AI-flavored tests when the bug is clearly ordinary application logic with no model or automation boundary involved.

## TDD Rules

- Do not write broad implementation first and backfill tests afterward unless the harness makes true TDD impossible.
- Do not treat RED as "write every test in the plan"; RED should usually mean the next focused behavior is failing for the right reason.
- Do not keep a test that passes for the wrong reason.
- Do not over-mock behavior that should be exercised more directly.
- Do not mock internal collaborators the repo controls when a behavior-level test can exercise them through the public surface.
- Do not mistake backfilled regression coverage for true TDD; if you had to backfill, say so plainly.
- Do not turn tests into snapshots of unstable implementation details unless that is the accepted repo pattern.
- Do not skip the refactor step when the green implementation is obviously messy or duplicated.
- When repeated model or automation failures are possible, prefer regression coverage at the shared interface over duplicating symptom-level tests.

## Handoffs

- Use `systematic-debugging` when you cannot yet explain or reproduce the failure well enough to write the right test.
- Use `spec-driven-development` when the expected behavior itself is still unclear and needs source-of-truth normalization.
- Use `release-readiness` near the end when passing tests are only one part of the readiness decision.
- Use `search-first` before TDD when the real blocker is unresolved evidence about how the system or external source actually behaves.

## References

Read these only as needed:

- `references/red-green-refactor.md`
  Use for the default TDD loop and pacing rules.
- `references/test-selection.md`
  Use for choosing the right test boundary and confidence level.
- `references/mocking-and-refactor-candidates.md`
  Use for mock boundaries, dependency injection at external edges, and post-green refactor candidates.
