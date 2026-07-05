---
name: task-decomposition-and-resume
description: Break broad work into ordered, resumable slices with explicit dependencies, active state, and safe parallel boundaries. Use when implementation or planning is too large to execute as one unit or when ongoing work needs to resume from existing artifacts without rediscovery.
version: 1.4.0
category: execution-planning
sources:
  - active plans, progress trackers, and blockers
  - slice-boundary and dependency references in this skill package
  - vertical-slice guidance adapted from /Users/longdo/Downloads/skills-main
use_when:
  - Broad work needs explicit slice boundaries, dependency order, or resume context.
  - Existing artifacts exist but the next executable slice is unclear.
avoid_when:
  - The work is already narrow and easy to execute directly.
  - The main problem is domain-specific planning rather than execution shape.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Slice boundaries follow executable outcomes rather than arbitrary file lists.
  - Dependencies and safe parallel boundaries are explicit.
  - Resume context captures current slice, next slice, blockers, and existing evidence.
  - Agent-ready slices distinguish AFK work from HITL work when delegation or issue shaping is involved.
---

# Task Decomposition And Resume

Turn broad work into ordered slices that another agent can resume cleanly.

Use this skill when the main challenge is not domain knowledge but execution shape: what to split, what depends on what, what can run in parallel, and how to continue from existing artifacts without restarting.

This skill is an execution-shaping owner, not a replacement for domain-specific planning or implementation skills.

## Core Promise

- Break large work into slices with clear dependency order.
- Keep only one active slice by default unless parallel work is truly independent.
- Make resumption possible from durable artifacts instead of chat memory.
- Prevent broad tasks from turning into unstructured thrash.

## Boundary

- Own slice shaping and resumable execution order once the work is broad enough to need it.
- Do not replace `artifact-resume-audit` when the artifact trail itself cannot be trusted yet.
- Do not replace `docs-driven-execution` when the slices already exist and the main problem is active execution.
- Use this skill to decide shape and order, not to absorb domain planning or final verification work.

## When To Use

Use this skill when:

- a task is too large or entangled to execute safely in one pass
- work needs explicit dependency mapping before implementation fans out
- the user returns to partially completed work and resumption is the main problem
- plans or trackers exist, but the next executable slice is unclear

Do not use this skill when the work is already narrow, single-slice, and easy to execute directly.

Use `artifact-resume-audit` first when the artifact trail itself is untrustworthy or contradictory. Use `docs-driven-execution` instead when the slices already exist and steady execution is the real need.

## Core Workflow

### 1. Ground In Existing Artifacts

- Read the active plan, progress tracker, blockers, and verification notes first.
- Identify the latest trustworthy artifact state.
- Resume from the current documented state unless the docs are stale or contradictory.
- For ticket-board or sprint-batch work, read all provided descriptions and comments before slicing so ordering, hidden acceptance notes, and owner context are not lost.
- If another agent may already have made changes, inspect the worktree and verify the relevant behavior before assigning implementation work to a slice.
- If the artifact trail is messy enough that the safest restart point is unclear, hand off to `artifact-resume-audit` before decomposing fresh slices.

### 2. Find The Right Slice Boundary

Split work by executable outcomes, not by arbitrary file lists.

Good slice boundaries usually follow:

- one user-visible behavior
- one dependency milestone
- one verifiable integration step
- one coherent risk area

When the output will become agent-ready tasks or issue drafts, prefer thin end-to-end tracer bullets over horizontal frontend/backend/database slices. Mark each slice as AFK or HITL so the next owner knows whether more human judgment is required.

Use `references/vertical-agent-slices.md` when turning broad work into agent-ready slices.

Avoid slices that are too broad to verify or too tiny to matter.

### 3. Make Dependencies Explicit

For each slice, record:

- what must already be true
- what this slice changes
- what becomes unblocked next
- whether the slice is MVP, deferred, or blocked
- whether the slice is implementation, verification-only, or contract-summary work

### 4. Limit Parallelism Deliberately

- Default to one active slice.
- Only allow parallel slices when they have disjoint write scope or one does not block the other.
- If parallel work is allowed, record the boundaries explicitly.

### 5. Leave Resume Context

After decomposition or after finishing a slice, record:

- current active slice
- next recommended slice
- blockers or dependencies
- what evidence exists already
- what still needs verification

## Rules

- Do not decompose work just to create busywork.
- Do not use parallelism to avoid deciding dependency order.
- Do not resume from stale docs without marking the refresh problem explicitly.
- Do not keep execution state only in chat when artifacts already exist.
- Do not turn this skill into a substitute for domain planning, debugging, or verification.

## Handoffs

- Use `spec-driven-development` when the work still needs source-of-truth normalization or phased planning.
- Use `docs-driven-execution` when the slices already exist and the task is now active execution.
- Use `traceable-delivery` when durable docs and matrices are missing.
- Use `lifecycle-orchestrator` when the bigger question is what stage the project is in.

## References

Read these only as needed:

- `references/slice-boundaries.md`
  Use for choosing executable slice boundaries.
- `references/dependencies-and-parallelism.md`
  Use for deciding dependency order and when parallel work is safe.
- `references/vertical-agent-slices.md`
  Use for tracer-bullet slices and AFK versus HITL classification.
