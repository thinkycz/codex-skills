---
name: two-axis-review
description: Review a concrete diff against repository standards and the originating specification or issue.
version: 1.1.0
category: quality
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Review a concrete diff against repository standards and the originating specification or issue.
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

# Two Axis Review

Fix the review base and inspect the actual diff plus enough callers/tests to establish impact. Review independently along repository correctness/conventions and requested behavior/acceptance. Include omissions and unsupported additions, not just changed-line style. Report only actionable findings with evidence, location, severity and consequence; distinguish uncertainty. Review mode is read-only and does not authorize fixes, external comments or destructive test setup. Green tests are evidence, not proof against untested service authorization, shared state or runtime regressions. Keep final findings prioritized and acknowledge residual verification gaps.

## Working evidence

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Review Axes](references/review-axes.md): for review axes.
