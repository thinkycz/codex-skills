---
name: spec-driven-development
description: Turn a written client specification, design input such as Figma or Google Stitch, or both into a traceable implementation workflow and delivered code. Use when the agent needs to implement backend/API work, admin panels, frontend screens, or mixed product slices from provided source artifacts while keeping markdown docs under `/docs`, splitting work into visible phases, routing to the right helper skills, and verifying the result against the specification and design before claiming completion.
version: 1.5.0
category: execution
sources:
  - client specifications and confirmed design inputs
  - traceability and verification references in this skill package
use_when:
  - The user already has written specs, design artifacts, or both and wants delivery from them.
  - The work needs phased implementation, progress tracking, and verification against source materials.
avoid_when:
  - Product intent is still too ambiguous and needs brainstorming or PRD work first.
  - The task is a trivial code edit with no need for traceable delivery.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Source conflicts are resolved before implementation proceeds.
  - Docs under `/docs` stay current as the execution control surface.
  - Final claims are verified against the specification and design, not just local code inspection.
---

# Spec Driven Development

Drive delivery from client-provided artifacts instead of starting from a blank slate.

Use this skill when the user already has a written specification, design files, or both, and wants implementation with visible progress, structured docs, and strict verification against the source materials.

## Core Promise

- Start from the source artifacts, not guesses.
- Keep progress visible through markdown docs in the project’s `/docs` folder.
- Split large work into small, traceable phases and bite-sized tasks.
- Route implementation to the right existing skills instead of handling every domain the same way.
- Do not claim completion until code, behavior, and design have been verified against the inputs.
- For end-to-end app changes, keep public surfaces synchronized instead of treating the first edited layer as complete.

## Boundary

- Own source normalization, planning, and the initial execution handoff when written specs or confirmed design inputs are the controlling artifact.
- Hand off to `docs-driven-execution` once the plan already exists and the main problem is steady slice-by-slice execution from `/docs`.
- Hand off to `clarify-before-plan` when only a few unresolved requirement questions still block safe planning.
- Hand off to `ticket-batch-intake` first when the source is a Trello/Jira/board export whose descriptions, comments, order, prior-agent state, or stakeholder contract summaries have not been normalized yet.
- Hand off to `spec-consistency-analysis` when spec, plan, and task artifacts already exist and need a read-only cross-check before more implementation.

## Workflow

### 1. Collect Artifacts And Ground In The Repo

- Ask the user for the written client specification, Figma or Google Stitch links/files, and any API contract or admin requirements that already exist.
- Accept partial inputs and keep moving with what exists.
- Apply `repo-convention-discovery` before locking plans or file structure so the work follows the local repo instead of inventing a new pattern.
- Explore the repo immediately to understand current architecture, conventions, feature boundaries, and likely implementation touchpoints.
- When the prompt names sibling frontend, backend, admin, or mobile repos, inspect those boundaries early and plan the change across all affected surfaces.
- Record missing artifacts explicitly instead of silently filling gaps.

If the user has not provided a source file yet, ask for it directly. Use [references/artifact-intake.md](references/artifact-intake.md) for the common source asks.

### 2. Normalize Sources Before Planning

- Summarize the artifacts into a clear working understanding before implementation begins.
- Treat the written client specification and provided design materials as source inputs that may disagree.
- If the written specification and the design source conflict in a way that changes scope, UX, fields, flows, or acceptance criteria, stop and ask the user which source has priority before planning or implementation continues.
- If the inputs are too ambiguous to implement safely, route to `product-brainstorming` first to clarify the intended behavior.
- Split the work into what is implementable now for the MVP and what is not yet implementable because third-party credentials, OAuth setup, vendor accounts, webhook secrets, or other external prerequisites are still missing.
- Treat credential-blocked integrations as deferred post-MVP work by default unless the user or source artifacts explicitly make them part of MVP acceptance.
- Do not stall the whole project on missing third-party access when the core app can be delivered first.

Read these references when needed:

- [references/source-of-truth-and-conflicts.md](references/source-of-truth-and-conflicts.md)
- [references/docs-layout.md](references/docs-layout.md)
- [references/mvp-vs-deferred.md](references/mvp-vs-deferred.md)
- Use `clarify-before-plan` after this step when the spec exists but a few unresolved ambiguities would materially change planning or validation.

### 3. Create The Traceable Doc Set

Write markdown files under the project’s `/docs` folder only.

Use [references/traceability-and-progress.md](references/traceability-and-progress.md) for the doc-set structure, state language, and traceability matrix.

### 4. Plan In Small Visible Phases

- Split work into phases that are meaningful to the user and safe to verify.
- Keep phases narrow enough that progress is obvious and blockers are local.
- For each phase, create bite-sized tasks and checklists suitable for execution by a focused agent or subagent.
- Keep plans concrete enough that the next execution slice is obvious, testable, and easy to verify.
- Break large work into smaller slices with visible dependency order before execution fans out.
- Call out the MVP slice separately from deferred post-MVP integrations when external prerequisites are unavailable.
- Require a follow-up markdown plan under `/docs/plans/` for deferred integrations so another agent can resume them later without rediscovery.

Each phase should be traceable from source artifact to implementation outcome. Avoid giant “do everything” phases.

Before implementation starts, use `spec-consistency-analysis` when spec, plan, and task artifacts all exist and a read-only cross-check would reduce rework.

### 5. Route To The Right Helper Skills

Do not treat all implementation work as the same kind of task.

Apply `custom-skill-routing` first to choose the right high-level owner and helper stack for the task.

Use [references/skill-routing.md](references/skill-routing.md) for the spec-driven delivery rules that layer on top of that shared routing.

Use [references/skill-routing.md](references/skill-routing.md) for the full helper-skill map. Keep the main rule simple: one dominant implementation owner, plus only the helper skills that change planning quality, delivery safety, or verification quality materially.

### 6. Execute With Visible Progress

- Keep `/docs/progress/` current as phases move from planned to active to verified.
- Mark blockers explicitly instead of hiding them in prose.
- Apply `docs-driven-execution` when moving from the written plan into active implementation so execution stays synced with the docs.
- Use `migration-risk-audit` before broad upgrades, refactors, or shared-layer migrations when the blast radius is not yet mapped.
- If tasks are separable, execute them in clearly bounded slices and keep the docs synchronized after each slice.
- Resume from the latest valid `/docs` artifact state whenever possible instead of reconstructing execution state from chat memory.
- Use `artifact-resume-audit` when existing artifacts are present but too stale, partial, or contradictory to trust for an immediate restart.
- Keep implementation tied back to the traceability matrix so a reader can see what is done, blocked, deferred, or awaiting verification.
- When a missing field, broken mapping, translation gap, enum mismatch, relationship parsing issue, or API-contract mismatch appears in one feature, inspect nearby features and shared layers before patching only the reported surface.
- If a backend contract change affects one form, check the other forms, tables, and detail views that consume the same JSON:API shapes, wrappers, or helpers.
- If a translation or enum rendering issue appears in one page, check the other pages using the same enum source, translation key family, or display helper.
- For Laravel-style API/admin work, include the expected end-to-end surfaces in the phase checklist when they exist: migration, model, validation request, controller/service, resource/serializer, OpenAPI, Nova/admin, translations, factories/seeders, tests, and frontend consumers.
- When user-provided acceptance requires a data-heavy edge case, prefer a reusable seeder or fixture over one-off manual database edits.
- For Trello, ticket-board, or sprint-batch work, read every provided card description and comment before planning; preserve the user's ordering unless dependency evidence requires a different order.
- When the user warns that another agent may have changed the work already, verify existing behavior first and avoid reworking completed items without evidence.
- When the user asks for contract summaries for ticket owners or frontend/backend counterparts, produce concise endpoint, payload, response, state, and verification notes in the requested language.
- Record in `/docs` whether the fix was intentionally applied app-wide or intentionally scoped after a wider search.

### 7. Verify Against The Right Source

Verification is required before any completion claim.

Always verify:

- implementation against the written client specification
- implementation against the design, when a design is part of the input
- test, build, lint, and runtime behavior as appropriate for the touched surfaces
- admin and API behavior against the real contract or backend support when relevant

Do not say work is complete because code was written. Require evidence.
Do not treat "screen exists" as sufficient completion if the relevant design, interaction, accessibility, or fidelity checks are still failing.

Read [references/verification.md](references/verification.md) for the required verification layers and reporting expectations.

Before a final handoff or “done” claim on broader work, apply `release-readiness`.

## Delivery Rules

- Do not invent missing requirements when the source files are unclear.
- Do not silently choose between conflicting written and visual sources.
- Do not write non-markdown status artifacts outside `/docs`.
- Do not collapse the entire project into one monolithic plan if phases can be separated.
- Do not skip TDD, traceability, or verification because a phase seems small.
- Do not trust agent success reports without independent verification evidence.
- Do not let planning quality gates and implementation quality gates blur together; both should be explicit in docs and closeout.

## Output Expectations

At the end of a successful run, the project should have:

- a normalized spec summary under `/docs/specs/`
- a phased implementation plan under `/docs/plans/`
- a live progress tracker and requirement matrix under `/docs/progress/`
- verification evidence under `/docs/verification/`
- implementation routed through the right helper skills for the relevant domain
- explicit resolution of any source-of-truth conflicts
- Use [references/output-artifacts.md](references/output-artifacts.md) when you need a concrete closeout shape for the expected `/docs` outputs.
