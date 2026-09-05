---
name: test-driven-development
description: Protect meaningful behavior with a failing test before an authorized implementation or bug fix.
version: 1.6.0
category: quality
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Protect meaningful behavior with a failing test before an authorized implementation or bug fix.
avoid_when:
  - The requested outcome belongs to another owner or exceeds the authorized scope.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Evidence supports the stated outcome and limitations.
  - Selected mode, references and actions remain within authorization.
---

# Test Driven Development

Identify an observable requirement or reproduced regression. Write the smallest test that fails for the intended reason, run it, implement the smallest correction, then rerun and refactor safely. Prefer public behavior and important boundaries over private implementation details or source-string assertions. A trivial presentation change need not gain a test that mirrors its markup; use existing checks and rendered inspection. Cover authorization, nullability, state isolation, concurrency and financial invariants when affected. Isolate shared fixtures and use the real relevant seam instead of mocking away the bug. Test requests alone do not authorize unrelated refactors; complete repository-required gates before handoff.

## Working evidence

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Ai Regression Coverage](references/ai-regression-coverage.md): for ai regression coverage.
- [Mocking And Refactor Candidates](references/mocking-and-refactor-candidates.md): for mocking and refactor candidates.
- [Red Green Refactor](references/red-green-refactor.md): for red green refactor.
- [Test Selection](references/test-selection.md): for test selection.
