---
name: repo-convention-discovery
description: Discover the implementation conventions of the current repository before planning or coding. Use when the agent needs to inspect routing, feature structure, API helpers, forms, state, styling, i18n, docs, tests, or other local patterns so later work follows the repo instead of inventing a new architecture.
version: 1.2.0
category: repo-analysis
sources:
  - current repository structure and nearby implementation patterns
  - existing docs, helpers, and UI primitives in the repo
use_when:
  - Work in an existing repository should follow local conventions rather than inventing new ones.
  - Planning or implementation depends on understanding routing, state, docs, tests, or styling patterns.
avoid_when:
  - The task is a standalone conceptual answer that does not depend on repo context.
  - There is no meaningful repository surface to inspect.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
quality_gates:
  - Exploration happens before questions that the repo can answer.
  - The summary stays short, actionable, and convention-focused.
  - Strong local patterns are preferred over cleaner invented abstractions.
---

# Repo Convention Discovery

Start by learning how this repo already works.

Apply this skill before planning or implementation when matching existing conventions matters more than inventing a fresh pattern.

## What To Inspect

- route structure and navigation
- feature/module layout
- API clients, serializers, and request helpers
- form wrappers and validation
- state management and providers
- styling and design-system primitives
- i18n and content structure
- tests, fixtures, and QA helpers
- existing docs that define delivery or architecture rules
- repo-specific agent guides such as `AGENTS.md`, `guidelines.md`, client specifications, OpenAPI files, and architecture notes
- sibling frontend/backend/admin repos when the user request explicitly spans more than the current checkout
- project command conventions such as `make fix`, `make check`, local server commands, seeded users, and environment overrides
- shell-level ownership of global overlays, drawers, and slideovers
- whether overlays are viewport-level or mistakenly clipped to local containers
- current asset strategy such as remote URLs, `public/` assets, SVG registries, or icon libraries
- current font loading strategy and whether local or proprietary fonts can be added
- whether docs already track route/state/fidelity mappings
- whether navigation distinguishes true destinations from transient visual states

## Output

Produce a short working summary of:

- the key conventions that matter for the task
- the likely files or subsystems involved
- any strong repo patterns that should be reused
- any missing or conflicting patterns worth surfacing early
- any shell, overlay, asset, icon, or font constraints that could affect fidelity-sensitive work
- when the user needs a higher-level view, a map of the relevant modules, callers, entrypoints, and shared helpers using the repo's own domain vocabulary

When the user is new to the repo or needs fast onboarding, also include:

- likely entrypoints to read first
- important subsystems or seams
- the safest starting place to make the first edit
- known local traps, brittle areas, or conventions that are easy to violate

## Rules

- Explore first, ask second.
- Prefer existing patterns over cleaner new abstractions unless the current task clearly justifies a change.
- Keep the summary short and actionable.
- Keep onboarding guidance repo-grounded and concrete rather than generic architecture advice.
- When a repo guide names an authoritative source, such as `guidelines.md` or a client spec, treat that source as part of the discovery surface before planning.
