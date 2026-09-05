---
name: playwright
description: Maintain or run repository-owned Playwright automated tests; use the host browser for interactive QA.
version: 2.2.0
category: quality
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Maintain or run repository-owned Playwright automated tests; use the host browser for interactive QA.
avoid_when:
  - The requested outcome belongs to another owner or exceeds the authorized scope.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
  - assets/
  - scripts/
quality_gates:
  - Evidence supports the stated outcome and limitations.
  - Selected mode, references and actions remain within authorization.
---

# Playwright

Confirm this is automated suite work. Read the repository's Playwright config, package scripts, fixtures and existing tests before editing or running checks. Use its declared commands and preserve generated-artifact, snapshot and trace conventions. Confirm server identity, built assets and isolated test data; serialize checks that mutate shared fixtures. Do not substitute the bundled legacy wrapper for repository tooling. For interactive navigation, authenticated sessions, screenshots and visual QA, use the active host's canonical browser. Automated suite evidence does not establish visible live-browser, worker or installed-runtime behavior. Keep legacy CLI references as compatibility documentation only, not a default execution path.

## Working evidence

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Cli](references/cli.md): for cli.
- [Workflows](references/workflows.md): for workflows.
