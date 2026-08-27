---
name: playwright
description: Use for repository-owned Playwright test-suite work such as writing, updating, debugging, or running automated E2E checks. Do not use Playwright as the interactive browser-control surface; route visible navigation, screenshots, and runtime QA through the active host's canonical browser.
version: 2.1.0
category: browser-automation
sources:
  - repository-owned Playwright configuration, fixtures, scripts, and automated E2E tests
use_when:
  - The repository already owns Playwright tests and the task is to maintain, debug, or execute that automated suite.
  - A maintainer is auditing or migrating stale interactive-browser references.
avoid_when:
  - The task requires interactive navigation, authenticated session reuse, visual QA, screenshots, or visible runtime evidence through the host browser.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - assets/
  - scripts/
  - references/
quality_gates:
  - Playwright runs only through the repository's declared test tooling and configuration.
  - Interactive browser work is handed off to the active host's canonical visible browser.
  - Automated test evidence is not misreported as visible-browser or production-runtime evidence.
---


# Playwright Test Boundary

Playwright is an automated test-suite tool here, not the interactive browser-control surface.

Use repository-owned Playwright tests when the task is to add, maintain, debug, or run automated E2E coverage. Prefer the repository's package scripts, configuration, fixtures, and documented commands. Do not introduce or run the bundled compatibility wrapper as a substitute for project tooling.

For interactive navigation, authenticated session reuse, screenshots, responsive visual inspection, and runtime UI debugging, use the active host's canonical visible browser. In Synara, use the integrated browser and reserve Computer Use for desktop or system UI, or cases the browser surface cannot finish. In Codex, follow the current app-provided browser or Chrome policy.

When this skill is encountered:

1. Confirm the task is automated test-suite work rather than interactive browser control.
2. Read the repository's Playwright config, package scripts, fixtures, and existing tests before editing or running anything.
3. Use the repository's own command and preserve its generated-artifact, snapshot, trace, and shared-state conventions.
4. Route interactive browser work to the active host's canonical visible browser.
5. Route completion evidence to `verification-before-completion`, clearly separating automated-suite results from visible runtime evidence.
