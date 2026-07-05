---
name: custom-skill-routing
description: Choose between the custom skills in this workspace and compose them cleanly when a task spans brainstorming, traceable delivery, design implementation, API integration, debugging, or verification. Use when the agent needs to decide which local custom skill or combination of skills should own a task.
version: 1.6.0
category: orchestration
sources:
  - internal skill library
  - lifecycle handoff rules in this workspace
use_when:
  - The user request could plausibly fit multiple local custom skills.
  - The main need is choosing a primary owner skill and clean handoffs.
avoid_when:
  - The current lifecycle stage is still unclear and lifecycle-orchestrator should decide first.
  - One skill is already the obvious owner without routing ambiguity.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Routing favors one primary owner skill over blended ownership.
  - Handoffs stay explicit and dependency order stays clear.
  - The skill does not replace lifecycle-orchestrator when stage detection is the real need.
---

# Custom Skill Routing

Use the local custom skills as a coordinated system, not as isolated islands.

Apply this skill when a task could reasonably fit more than one custom skill and you need to choose the right owner or handoff path.

If the main question is where the project currently sits in the broader product lifecycle or what stage should happen next, use `lifecycle-orchestrator` first. This skill is for within-stage or cross-cutting routing once the lifecycle stage is already known.

## Core Rule

Route by dominant risk first, then layer supporting skills only where they materially help.

Do not invoke multiple high-level skills in parallel just because they all seem relevant.
Do not take ownership of top-level lifecycle stage detection when `lifecycle-orchestrator` is the better fit.
Prefer specialized owner skills with fresh-context handoffs over blended ownership that keeps too many workflows alive at once.

## Boundary

- Own within-stage routing once the lifecycle stage is already known.
- Do not replace `lifecycle-orchestrator` when the main question is what stage the work is in or what should happen next.
- Do not replace the downstream owner once one skill clearly controls the current phase.
- Use this skill to choose and combine owners cleanly, not to re-explain every downstream workflow inline.

## Unified Workflow

- Choose one primary owner based on the dominant current risk:
  product ambiguity, source normalization, execution shape, debugging, or closeout.
- Add supporting skills only when they materially change execution quality.
- Keep the handoff direction forward-moving: shaping -> planning -> execution -> quality -> closeout.
- When the work is large, decompose it into ordered slices before fanning out execution.

Use [references/route-matrix.md](references/route-matrix.md) for the short owner map, [references/routing-details.md](references/routing-details.md) for boundary detail, and [references/combination-patterns.md](references/combination-patterns.md) for common multi-skill chains.

## Primary Routing

- Product direction unclear: `product-brainstorming`.
- Existing spec only needs a few high-impact questions: `clarify-before-plan`.
- Existing plan needs a deep one-question challenge against code and docs: `grill-with-docs`.
- Ticket-board export or sprint batch needs intake, comments, summaries, and contracts: `ticket-batch-intake`.
- Existing codebase needs module-depth, seam, locality, or refactor-opportunity audit: `architecture-deepening-audit`.
- Disposable state, workflow, API-shape, or UI-variant prototype would answer a question before production work: `throwaway-prototype`.
- Design exists but written PRD is missing: `design-to-prd`.
- Written spec or design handoff should drive phased delivery: `spec-driven-development`.
- Existing `/docs` plans and progress already control execution: `docs-driven-execution`.
- Durable tracking is missing for multi-step work: `traceable-delivery`.
- Slice boundaries, dependency order, or resume shape are unclear: `task-decomposition-and-resume`.
- Artifact trust is unclear: `artifact-resume-audit`.
- Current conversation or work state needs a continuation handoff for another agent/session: `session-handoff`.
- Figma or Google Stitch is the active design source: `figma` or `google-stitch`.
- Multi-screen design source needs a traversable app: `design-to-traversable-app`.
- Screen coverage exists and parity remains: `design-fidelity-polish`.
- Existing UI needs redesign diagnosis: `frontend-redesign-audit`.
- Stable visual rules should become reusable guidance: `design-system-export`.
- Existing frontend must align with real backend support: `integrating-backend-api-into-frontend`.
- Consumer assumptions need read-only API comparison: `api-contract-review`.
- Bug or regression needs root-cause evidence: `systematic-debugging`.
- Change should start from a failing automated check: `test-driven-development`.
- Another agent needs a concrete E2E verification plan: `e2e-verification-handoff`.
- Branch, PR, or WIP diff needs review against both repo standards and a source spec: `two-axis-review`.
- A specific completion claim needs proof: `verification-before-completion`.
- Final handoff or release needs go/no-go judgment: `release-readiness`.
- Completed work exposed reusable lessons: `reflection-and-learning`.
- Skill package correctness, portfolio health, or export shape is the task: `skill-maintenance-and-validation`, `skill-stocktake`, or `cross-tool-packaging`.

Read [references/routing-details.md](references/routing-details.md) when these quick rules are not enough.

## Routing Rules

- Pick one primary skill to own the task.
- Add supporting skills only when their specialized rules are actually needed.
- Prefer handoffs over blended mega-workflows when one phase is clearly complete.
- If the task shape changes midstream, re-route explicitly instead of quietly switching mental models.
- Treat screen implementation and screen fidelity as separate completion stages when design accuracy is part of acceptance.
- Use [references/route-matrix.md](references/route-matrix.md) instead of re-encoding the whole library inline when routing questions get broad.
