---
name: integrating-backend-api-into-frontend
description: Use when connecting an existing frontend app to a published or partially published backend API, especially when the work includes phased delivery, missing page or form functionality, blocker tracking, browser QA, runtime debugging, plan/doc updates during execution, and traceable progress under `/docs`.
version: 1.3.0
category: integration
sources:
  - published or partially published backend API contracts
  - frontend repo conventions and QA flows
use_when:
  - An existing frontend must be wired to a real backend with visible delivery tracking.
  - Missing forms, pages, blockers, or unsupported states need to be integrated honestly.
avoid_when:
  - The work is greenfield backend architecture instead of frontend integration.
  - The task is a narrow local bug that does not involve API integration ownership.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - API contract mapping and unsupported behavior stay explicit.
  - Browser QA, runtime debugging, and blocker tracking are part of the workflow.
  - Deferred integrations remain visible instead of silently absorbed into MVP claims.
---

# Integrating Backend API Into Frontend

## Overview

This skill is for production integration work in an existing frontend repository. The goal is not just to "add API calls"; it is to make the real backend-supported behavior fit the repo cleanly, finish missing pages and forms, keep unsupported behavior explicit, and leave a traceable implementation record.

## Boundary

- Own frontend integration implementation, blocker tracking, runtime/browser QA, and docs updates.
- Do not replace `api-contract-review` when the next step is only read-only comparison of assumptions to contracts and payload evidence.
- Do not replace `spec-driven-development` when source normalization and phased planning are still missing.
- Do not replace `release-readiness` for the final handoff or release verdict.

Use this skill when the task sounds like:
- connect all pages or forms to the backend
- make an existing frontend fully functional
- finish missing backend-supported functionality
- integrate an OpenAPI or Swagger contract into an existing app
- deliver the work in phases and keep plans updated as progress changes

Do not use this skill for greenfield app creation.

## Required Workflow

1. Ground in repo conventions first.
   Apply `repo-convention-discovery`, then inspect route layout, feature folders, shared request helpers, form wrappers, validation, i18n, tables, and state before proposing changes.
2. Inspect the backend contract directly.
   Read the published OpenAPI or live API behavior before trusting stale docs or assumptions.
   Apply `api-contract-review` first when the contract, payload shape, or consumer assumptions need a read-only preflight before implementation begins.
   If the product definition itself is still unclear or design-first artifacts need normalization, hand off to `spec-driven-development` or `design-to-prd` before broad integration work.
3. Map user-visible behaviors to exact backend support.
   For each list, detail page, create/edit form, archive action, relation view, download, or message flow, identify the real backend operation that supports it.
   Separate what can ship now from what depends on missing third-party credentials, vendor setup, or other external prerequisites.
   For end-to-end field changes, map every affected surface before coding: backend validation/resources/OpenAPI, admin views, frontend forms, tables, detail screens, locale keys, notifications, and generated or typed client helpers.
4. Slice delivery by module or workflow.
   Implement vertically, one domain at a time, so blockers and verification stay easy to reason about.
   Apply `traceable-delivery` so plans, trackers, blockers, and verification evidence remain durable under `docs/`.
   Apply `docs-driven-execution` when carrying those phases into active implementation.
5. Reuse existing repo patterns.
   Prefer the app's current routing, API helpers, serializers, response transformers, form patterns, and locale structure over introducing new architecture.
6. Treat unsupported behavior as explicit blockers.
   Do not invent frontend-only success paths, fake local mutations, or placeholder data that looks complete.
   If an area is blocked only because external credentials, API keys, OAuth setup, webhook secrets, or vendor provisioning are not yet available, classify it as `intentionally deferred` for the MVP unless the source explicitly requires it now.
   Keep the core app moving on backend-supported or self-contained features, and tell the user which integrations are postponed until external access arrives.
7. Verify in layers.
   Run lint, typecheck, and build, then manually exercise the touched routes and key mutations in the browser.
   When the bug involved browser behavior, pending state, redirects, uploads, or loading screens, verify the real runtime path instead of stopping at static checks.
8. Keep progress traceable.
   Keep `traceable-delivery` active while implementation evolves.
   Update plans, phase docs, blocker notes, verification evidence, and locale parity as the implementation evolves.
9. Assess final readiness explicitly.
   Apply `release-readiness` before treating the integrated slice as fully ready for handoff or release.

## Unified Workflow Position

This skill usually sits after source normalization and written planning:

- `design-to-prd` when design needs to become a written product artifact
- `spec-driven-development` when implementation phases and delivery docs need to be set up
- `integrating-backend-api-into-frontend` during contract-backed frontend execution

## Read These References As Needed

- For phase-based planning and closeout criteria, read [references/planning.md](references/planning.md).
- For mapping OpenAPI and live payloads to frontend behavior, read [references/api-contract-mapping.md](references/api-contract-mapping.md).
- For browser-based validation and manual smoke testing, read [references/browser-and-manual-qa.md](references/browser-and-manual-qa.md).
- For blocker taxonomy, progress snapshots, and phase doc maintenance, read [references/blockers-and-phase-tracking.md](references/blockers-and-phase-tracking.md).
  Apply this after the shared `traceable-delivery` rules to keep the integration-specific blocker semantics consistent.
- For runtime regressions and framework-style debugging during integration, read [references/runtime-debugging.md](references/runtime-debugging.md).

## Default Delivery Rules

- Use the live API contract as the source of truth when written product specs and backend behavior disagree.
- Preserve the current route structure unless the task explicitly requires route changes.
- Add thin typed API modules and mapping helpers near the feature instead of inventing a new app-wide data framework.
- Keep shared enums and options aligned to backend-supported values.
- Preserve backend-owned namespaces exactly, such as external-provider field prefixes, and do not let frontend mappers overwrite or normalize them into native fields unless the contract explicitly says so.
- Be careful with `FormData`: booleans, empty strings, arrays, files, and nullable fields often need explicit request helpers or backend normalizers to avoid stringly typed drift.
- Sync locale keys across all supported languages whenever UI changes.
- Prefer relation-aware rendering when responses expose `relationships` and `included`.
- Validate real create/edit/archive/message flows in-browser, not just list rendering.
- When third-party integrations are unavailable, deliver the shippable MVP slice first and leave a durable markdown follow-up plan for the deferred integration work.

## Blocker Taxonomy

- `backend missing`: required endpoint, field, relationship, or file action is not supported
- `intentionally deferred`: valid follow-up work left out of the current slice
- `intentionally deferred due to missing external access`: valid follow-up work blocked only by unavailable third-party credentials, vendor setup, or external provisioning
- `runtime/framework issue`: build, framework, cache, or library behavior interfering with delivery
- `cancelled`: previously planned area removed by product or scope decision

## Do Not Do This

- Do not invent unsupported backend flows.
- Do not hide missing endpoints behind fake success messages or mock data that looks real.
- Do not stop at passing static checks when the change affects runtime behavior.
- Do not skip locale parity or plan/doc updates.
- Do not integrate the whole product area in one blind pass when a phased approach is feasible.

## Output Expectations

A strong result from this skill usually includes:
- a phased or module-based plan when the scope is broad
- implementation aligned to existing frontend conventions
- explicit blocker documentation for unsupported backend behavior
- verification evidence from lint, typecheck, build, and browser/manual QA
- updated progress tracking so the next engineer can see what is complete, blocked, deferred, or cancelled
