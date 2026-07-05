---
name: subagent-driven-development
description: "Use when implementation should run through a lead-worker pattern: the main agent keeps ownership of planning, decomposition, integration, and verification, while bounded subagents handle well-scoped implementation slices. Trigger when the work is large enough to benefit from context isolation, cost-aware delegation, or safe parallel execution."
version: 1.3.0
category: execution
sources:
  - worker/lead delegation rules in this skill package
  - capability selection and parallel safety references
use_when:
  - Implementation is large enough to benefit from bounded worker slices and explicit ownership.
  - Parallel work can reduce time without creating integration chaos.
avoid_when:
  - The task is small, blocked on one investigation, or too ambiguous to delegate safely.
  - Delegation would replace necessary lead-agent judgment.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The lead agent keeps planning, integration, and verification ownership.
  - Worker write scopes and responsibilities are explicit and disjoint where possible.
  - Delegation is reviewed and integrated before success is claimed.
---

# Subagent Driven Development

Use subagents as workers, not as a substitute for thinking.

This skill is for implementation work where a lead agent should keep the hard decisions and integration ownership while delegating bounded coding slices to fresh-context worker agents.

This is not a general orchestration skill. It is an execution pattern for code delivery.

## Core Promise

- Keep planning, architectural judgment, integration, and verification with the lead agent.
- Use worker agents for bounded implementation slices that benefit from fresh context.
- Improve throughput and cost-efficiency without losing coherence.
- Make delegation explicit, reviewable, and safe.

## Boundary

- Own the lead-worker execution pattern after the work is already clear enough to delegate.
- Do not replace `task-decomposition-and-resume` when slice boundaries or dependency order are still unclear.
- Do not replace `systematic-debugging` when the main problem is still unexplained.
- Keep final planning, integration, and verification with the lead path instead of turning delegation into full orchestration.

## When To Use

Use this skill when:

- the work is too large to execute efficiently in one agent context
- implementation can be split into bounded slices with clear ownership
- some slices are repetitive, mechanical, or lower-risk than the main integration path
- parallel execution would materially reduce time without creating integration chaos

Do not use this skill when:

- the task is small enough for one agent
- the next step is still blocked on one unresolved investigation
- the write boundaries are unclear
- the work is mostly product clarification, architecture design, or root-cause debugging

## Core Roles

Use [references/lead-vs-worker.md](references/lead-vs-worker.md) for the lead-versus-worker split and [references/delegation-ladder.md](references/delegation-ladder.md) for what should stay local versus move to workers.

## Capability Selection Guidance

Choose worker capability by task difficulty, not by habit.

Use [references/capability-selection.md](references/capability-selection.md) when you need the stronger-versus-cheaper worker guidance in detail.

## Core Workflow

### 1. Ground Locally First

Before delegating:

- inspect the repo and nearby conventions
- identify the real acceptance bar
- find the immediate blocking task
- decide what must stay on the lead path right now

Do not start by spawning workers just because the task is large.

### 2. Decompose Into Real Slices

Break work into slices that have:

- a clear goal
- a clear dependency order
- a bounded write scope
- a clear completion condition

Prefer slices aligned to behavior or subsystem, not arbitrary file batches.

### 3. Keep The Critical Path Local

Do not delegate the task if:

- the next lead step depends directly on its result
- the task is still ambiguous
- the task decides architecture or shared contracts
- the task is likely to reveal the actual shape of the rest of the work

Lead first, delegate second.

### 4. Delegate Only With Explicit Ownership

For each worker task, specify:

- the exact goal
- what files or subsystem it owns
- what it must not change
- whether it is alone in the codebase
- how its result will be reviewed
- what output is expected on completion
- when relevant, what approval boundary authorized the slice versus what work the worker actually executed

Every worker must know that other agents may be editing nearby code and should adapt rather than revert unexpected changes.

Use [references/delegation-rules.md](references/delegation-rules.md) for the checklist and [references/worker-brief-template.md](references/worker-brief-template.md) for a compact brief shape.

### 5. Parallelize Only When Safe

Parallel workers are appropriate only when:

- their write scopes are disjoint
- their tasks do not depend on each other
- the lead agent can continue meaningful non-overlapping work
- integration order is already understood

Do not use parallelism to avoid deciding dependencies.

### 6. Review And Integrate As Lead

When workers return:

- review their result quickly
- check for boundary violations
- integrate or refine centrally
- resolve cross-slice conflicts at the lead level
- avoid redoing the whole task unless the worker clearly failed

The lead agent remains responsible for coherence.

### 7. Verify Before Claiming Success

Delegated work is not done when a worker says it is done.

The lead agent must verify:

- the requested behavior
- relevant tests and checks
- integration across slices
- absence of obvious regressions
- docs or trackers if they are part of the workflow

## Delegation Rules

- Do not delegate without a bounded write scope.
- Do not delegate architecture decisions by accident.
- Do not let workers own final verification.
- Do not open many workers when one clear local step is still unresolved.
- Do not create overlapping worker ownership unless the overlap is intentional and tightly controlled.
- Do not turn subagents into unmanaged background noise.
- When history clarity matters, distinguish delegated authorization from actual worker actions in the handoff notes.

## Handoffs

- Use `task-decomposition-and-resume` before this skill when slice boundaries or dependency order are still unclear.
- Use `spec-driven-development` when the work still needs normalized planning or traceable execution setup.
- Use `docs-driven-execution` when the plan already exists and execution is underway.
- Use `verification-before-completion` and `release-readiness` for closeout.
- Use `systematic-debugging` when the main problem is still unexplained rather than merely unimplemented.

## References

Read these only as needed:

- `references/lead-vs-worker.md`
  Use for the ownership split between the lead path and worker slices.
- `references/delegation-ladder.md`
  Use for deciding what stays local, what can be delegated, and what should be escalated back.
- `references/delegation-rules.md`
  Use for what to delegate, what to keep local, and how to assign ownership.
- `references/capability-selection.md`
  Use for choosing stronger vs cheaper worker capability by task type.
- `references/parallel-safety.md`
  Use for deciding when parallel workers are actually safe.
- `references/integration-review.md`
  Use for lead-agent review and integration after worker completion.
- `references/worker-brief-template.md`
  Use for a compact worker brief when a slice is ready to delegate.
