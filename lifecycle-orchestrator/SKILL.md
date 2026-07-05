---
name: lifecycle-orchestrator
description: Detect the current stage of a product delivery lifecycle, identify the next required stage, and route to the right local skill so work continues without restarting the process from scratch.
version: 1.3.0
category: orchestration
sources:
  - internal skill lifecycle stages and handoff patterns
  - existing repo artifacts that reveal current delivery state
use_when:
  - The main question is what stage the work is in or what should happen next.
  - A user is resuming ongoing work and the right next owner is unclear.
avoid_when:
  - A specific owner skill is already obvious.
  - The task is a bounded implementation slice rather than stage detection.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Lifecycle stage is grounded in evidence from the repo and artifacts.
  - The next owner skill is explicit and does not duplicate lower-level workflows.
  - Missing prerequisites or artifacts are surfaced before implementation continues.
---

# Lifecycle Orchestrator

Use this as the top-level workflow skill when the main question is what stage the project is in, what should happen next, or how to resume work that is already underway.

This skill is an orchestrator, not a mega-skill. It should detect lifecycle state, identify missing artifacts, choose the next stage, and hand off to the right specialized skill instead of duplicating the full workflows those skills already own.

## When To Use

Use this skill when the user:

- asks what to do next
- asks to plan or implement the next step after a previous phase, especially when existing docs or partial work may already define the current stage
- arrives with partial project artifacts and wants to continue
- has design, specs, docs, or implementation in an unclear combination
- wants guidance through the full product lifecycle step by step
- needs the agent to recognize the current stage automatically and keep progress moving

Do not use this skill as the primary owner for implementation details, design fidelity work, debugging, or release assessment. Route to the stage-specific skill once the lifecycle state is known.

## Core Promise

- Detect the current lifecycle stage from real artifacts, not guesses.
- Continue from the current stage instead of restarting earlier ones unnecessarily.
- Choose the earliest incomplete stage that unblocks the rest of the work.
- Route to the right specialized skill for execution inside that stage.
- Keep broad work grounded in `/docs` artifacts instead of leaving lifecycle state only in chat.
- Prefer resumable continuation from current artifact state over rediscovery when the docs are still trustworthy.

## Lifecycle Stages

Use these canonical stages:

1. brainstorming
2. source or design intake
3. spec or PRD
4. delivery planning
5. execution
6. fidelity and verification
7. release readiness
8. reflection and learning

Use [references/stage-detection.md](references/stage-detection.md) for the evidence cues and [references/handoff-map.md](references/handoff-map.md) for the default owner by stage.

## Required Workflow

### 1. Inspect Available Artifacts First

Before choosing a stage, inspect what already exists:

- the user prompt and recent thread context
- design links, screenshots, Figma URLs, or Stitch references
- written specs, PRDs, or client requirements
- existing `/docs/specs`, `/docs/plans`, `/docs/progress`, and `/docs/verification`
- current implementation status when code, screens, or routes already exist

Apply `repo-convention-discovery` before planning or coding in an unfamiliar repo.

### 2. Determine The Current Stage
- Ground the stage in artifacts, not chat-only impressions.
- If multiple stages are partially present, choose the earliest incomplete stage that would unblock the rest of the lifecycle.
- Prefer continuation from trustworthy artifacts over restarting earlier phases.

### 3. Choose The Next Stage And Owner Skill
- Pick one stage owner.
- Layer supporting skills only when a stage-specific gap remains, such as slice decomposition, domain-specific integration, or final verification.
- Use [references/handoff-map.md](references/handoff-map.md) for the default stage-to-owner map.

### 4. Handle Interruptions Without Losing Lifecycle State

- If a bug interrupts any stage, layer `systematic-debugging` without abandoning the broader lifecycle state.
- If docs exist but are stale relative to the prompt or source materials, route first to the skill that can refresh the source of truth.
- If third-party credentials or vendor setup are missing, keep the lifecycle moving with the MVP-first deferred-integration behavior already defined in `spec-driven-development`, `integrating-backend-api-into-frontend`, `traceable-delivery`, and `docs-driven-execution`.
- If the user returns after a pause or partial run, prefer resuming from the latest valid plan, tracker, or verification artifact instead of reconstructing the whole state from memory.
- If a prior run was interrupted, route through `artifact-resume-audit` or `docs-driven-execution` before continuing when the artifact or worktree state is uncertain.

### 5. Make The Lifecycle State Explicit

When using this skill, the agent should explicitly say:

- what stage the project is currently in
- what evidence supports that stage determination
- what the next stage is
- which skill should own that next stage
- what artifact is missing if the lifecycle cannot proceed cleanly
- whether the current work should resume, refresh, or decompose before execution continues

If the user returns later and artifacts already exist, continue from the last incomplete stage instead of rerunning earlier lifecycle steps.

## Boundaries

- `lifecycle-orchestrator` decides where the work currently is in the lifecycle and what stage comes next.
- `custom-skill-routing` decides how to combine skills inside that stage or when multiple specialized skills are simultaneously relevant.
- `traceable-delivery` owns durable cross-stage docs once work becomes broad enough to need them.
- Stage-specific execution still belongs to the downstream owner skill.
- Use the references in this package instead of expanding the full stage matrix inline.

## Delivery Rules

- Do not restart the lifecycle from brainstorming when later-stage artifacts already exist and are still valid.
- Do not skip back to earlier stages unless artifacts are missing, stale, contradictory, or insufficient for safe continuation.
- Do not keep lifecycle state only in chat when the work is broad enough to warrant `/docs`.
- Do not duplicate downstream skill workflows inside this skill.
- Do not let a bug or missing third-party credential erase the broader stage context.

## Output Expectations

At the end of a successful run, the agent should have:

- identified the current lifecycle stage
- identified the next required stage
- chosen the correct owner skill for that next stage
- explained the evidence behind that decision
- identified any missing artifact that blocks clean continuation
- ensured broad ongoing work stays aligned with `/docs` rather than chat-only state
