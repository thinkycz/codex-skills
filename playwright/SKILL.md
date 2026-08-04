---
name: playwright
description: Retired compatibility package. Do not use Playwright for browser work; use Chrome through Computer Use for navigation, interaction, screenshots, responsive verification, and UI debugging.
version: 2.0.0
category: browser-automation
sources:
  - playwright-cli wrapper workflows and browser snapshots
use_when:
  - A maintainer is auditing or removing legacy Playwright skill references; do not execute Playwright.
avoid_when:
  - Any browser navigation, form interaction, screenshot, UI-flow debugging, visual QA, responsive verification, or runtime evidence is required.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - assets/
  - scripts/
  - references/
quality_gates:
  - No Playwright command, wrapper, or test runner is invoked.
  - Browser work is handed off to Chrome through Computer Use.
---


# Playwright CLI — Retired

The workspace browser default is Chrome through Computer Use.

Do not invoke Playwright for browser navigation, screenshots, responsive checks, local UI testing, data extraction, or debugging. Use the Chrome control skill and Computer Use instead.

This package remains only as a compatibility tombstone so older catalogs and references fail safely. It does not own an executable browser workflow.

When this skill is encountered:

1. Do not run the bundled wrapper or any Playwright command.
2. Route interactive browser work to Chrome through Computer Use.
3. Route completion evidence to `verification-before-completion`.
4. Update stale neighboring skill references so they no longer recommend Playwright.
