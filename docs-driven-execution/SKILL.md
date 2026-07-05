---
name: docs-driven-execution
description: Execute multi-phase implementation work from markdown plans and progress docs while keeping `/docs` artifacts current as the source of truth. Use when the agent already has a plan or tracker and needs to carry work through phase-by-phase execution, status updates, blocker maintenance, and verification handoff without letting the docs drift from reality.
version: 1.5.0
category: execution
sources:
  - active markdown plans and progress docs under `/docs`
  - phased execution and blocker-management patterns in this workspace
use_when:
  - A plan already exists and the work should advance slice by slice from docs.
  - The team needs progress, blockers, and verification evidence kept current during execution.
avoid_when:
  - The task is too small to justify docs-driven control.
  - Planning is not ready yet and the real need is to create or clarify the roadmap first.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
quality_gates:
  - Plans, progress, blockers, and verification are updated after each meaningful slice.
  - Only one active slice exists by default unless parallel work is clearly safe.
  - Dirty worktree, interrupted commands, missing repos, and pre-existing failures are recorded before status changes.
  - Docs stay aligned with reality before any phase is marked complete.
---

# Docs Driven Execution

Use docs as the execution control surface, not just as a kickoff artifact.

Apply this skill when a plan already exists under `/docs` and the work should proceed slice by slice while keeping plans, progress, blockers, and verification evidence in sync with reality.

## Boundary

- Own active execution from existing `/docs` artifacts.
- Do not replace `spec-driven-development` when source normalization, phased planning, or requirement shaping still needs to happen.
- Do not replace `task-decomposition-and-resume` when the real problem is finding cleaner slice boundaries or explicit dependency order before execution continues.
- Do not replace `traceable-delivery` when the repo lacks durable plans, progress trackers, blocker records, or verification artifact structure.
- Use `traceable-delivery` first when the missing piece is the tracking system itself; use this skill after the plan and tracker are trustworthy enough to execute from.
- Hand off to `release-readiness` when the work is substantially done and the main question is whether the evidence is strong enough to close out.

## Core Workflow

1. Read the active plan and progress docs before changing code.
2. Resume from the latest valid plan and progress state instead of replanning from memory.
   If the previous turn was interrupted or commands may have partially executed, inspect process state, git/worktree changes, and the active tracker before choosing the next slice.
   If the worktree is dirty, distinguish inherited changes, current-slice changes, generated artifacts, and unrelated local state before editing.
3. Pick the current phase or next actionable slice, not the whole roadmap at once.
4. Execute in small increments that can be verified independently.
5. After each meaningful slice:
   - update progress docs
   - reclassify blockers
   - link verification evidence
   - update fidelity and interaction status when those are part of acceptance
   - keep MVP-deliverable work separate from deferred post-MVP integrations
   - update any deferred integration plan when new information about required credentials, vendor setup, or resume steps becomes available
   - keep one active slice unless independent work is clearly safe to run in parallel
   - note interrupted, partially executed, or externally changed work as explicit resume context
   - record pre-existing test/tool failures separately from failures introduced by the current slice
   - classify absent frontend, mobile, backend, or integration repos as handoff-only scope instead of marking the slice complete
6. Do not mark a phase complete until its docs reflect the real state.
7. For broad design-driven delivery, prefer this execution order unless the user says otherwise:
   - source normalization or PRD alignment
   - roadmap and MVP-versus-deferred mappings
   - screen or page implementation
   - state consolidation
   - traversability wiring
   - asset localization
   - fidelity pass
   - final verification

## When To Use

- after `spec-driven-development` has produced a plan
- after `design-to-prd` has produced a PRD that is now driving implementation planning
- during `design-to-traversable-app` implementation
- during backend/frontend integration work with active phase trackers
- whenever `/docs/plans` and `/docs/progress` already exist and should drive execution

## Rules

- Treat `/docs/plans` and `/docs/progress` as live artifacts, not stale notes.
- Prefer one current phase and one next slice over broad parallel thrashing.
- Keep blockers explicit.
- Do not let generated artifacts, dirty-tree noise, or stale build outputs become invisible in the progress record.
- Keep dependency order explicit before splitting work into parallel slices.
- Do not stop at first-pass screen delivery when known fidelity or interaction gaps are still part of the requested acceptance bar.
- Do not mark phases complete while known visual or interaction mismatches remain in docs as unresolved.
- Hand off to `release-readiness` when implementation is functionally done and needs final closeout.
- When external credentials or vendor setup are missing, continue executing the MVP slice and keep the deferred integration plan ready for a later agent to resume.
