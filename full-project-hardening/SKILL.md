---
name: full-project-hardening
description: Audit and harden an existing product across code, architecture, security, dependencies, data, API contracts, runtime flows, UI quality, documentation, and release evidence. Use when the user asks for a comprehensive project audit plus fixes, testing of every important flow, or a production-readiness hardening pass without a controlling external specification.
version: 1.0.0
category: execution
sources:
  - current repositories, project instructions, runtime evidence, and delivery artifacts
  - recurring whole-project audit and hardening patterns from recent Codex work
use_when:
  - The user wants a broad audit that should continue through prioritized fixes and integrated verification.
  - Correctness, security, backend, frontend, runtime, and release concerns must be assessed together.
avoid_when:
  - The request is a read-only focused architecture, migration, API-contract, or frontend audit.
  - A written specification or confirmed design is the controlling delivery source; use spec-driven-development.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The baseline, product-flow inventory, and verification gates are grounded in the actual repos before findings become fixes.
  - Findings are prioritized and implemented as bounded behavioral slices rather than one unreviewable mega-phase.
  - Broad or high-risk delivery receives an independent adversarial gap review before the release verdict.
  - Integrated verification covers the relevant code, runtime, browser, data, external-service, and documentation surfaces.
  - Closeout distinguishes implemented, locally verified, deployed, live-provider verified, and production ready.
---

# Full Project Hardening

Turn “audit the whole project and make it solid” into a bounded, evidence-driven delivery workflow.

This skill owns comprehensive assessment, prioritized fixes, integrated verification, and readiness handoff for an existing product when no external specification is the controlling source. It is deliberately broader than a focused read-only audit, but it must still keep scope, evidence, and completion claims precise.

## Boundary

- Own broad audit-to-fix hardening across repositories, layers, and user flows.
- Use `architecture-deepening-audit`, `migration-risk-audit`, `api-contract-review`, or `frontend-redesign-audit` when the user wants only that focused read-only assessment.
- Use `spec-driven-development` when a written spec or confirmed design must control the implementation.
- Use `systematic-debugging` for an unexplained failure uncovered during hardening, then return to this workflow after root cause is proven.
- Use `release-readiness` for the final go/no-go verdict; this skill prepares and verifies the evidence.

## Workflow

### 1. Establish Baseline Truth

- Identify every repository and product surface in scope before editing.
- Read project instructions, architecture docs, plans, trackers, and current verification guidance.
- Apply `repo-convention-discovery` to learn local structure, canonical examples, generated-file policy, and the exact full-project gate.
- Inspect worktree state and preserve unrelated or user-owned changes.
- Record the current build, test, lint, type, runtime, and deployment posture without treating pre-existing failures as task-created failures.
- Confirm which claims can be checked locally and which require a deployed environment, live provider, privileged account, or external coordination.

### 2. Inventory The Product And Its Evidence

- Map roles, routes, APIs, screens, background jobs, external providers, data stores, migrations, admin surfaces, and important state transitions.
- Identify the highest-value user journeys and the negative, permission, empty, failure, and recovery paths around them.
- Map current automated and manual coverage to those flows.
- Use [references/audit-matrix.md](references/audit-matrix.md) to keep coverage explicit and prevent a frontend-only or test-only audit from being mistaken for full-project coverage.

### 3. Audit Across The Whole Stack

Assess only evidence-backed concerns across:

- correctness and regression risk
- authentication, authorization, secrets exposure, input handling, and dependency security
- architecture, shared contracts, code locality, and generated artifacts
- schema, migrations, data integrity, serialization, and API compatibility
- queues, workers, scheduled tasks, webhooks, email, payment, upload, and other external handoffs
- UI completeness, responsiveness, accessibility, interaction states, and design consistency
- test quality, build/release tooling, observability, operational docs, and durable delivery state

Classify findings by severity, affected flow, evidence, likely root cause, fix owner, dependencies, and verification requirement. Do not inflate scope with taste-only cleanup or speculative findings.

### 4. Convert Findings Into Bounded Slices

- Prioritize P0 correctness, security, data-loss, and delivery-blocking gaps first; then high-value reliability and usability gaps; then polish.
- Group work by user-visible behavior or subsystem outcome, not arbitrary file batches.
- Give every slice an acceptance condition, write scope, do-not-touch areas, dependency contract, and exact verification gate.
- Use `test-driven-development` when a failing automated check can lead the fix.
- Use `task-decomposition-and-resume` when ordering or safe boundaries are still unclear.
- Use `traceable-delivery` when the work is broad enough to require durable plans, matrices, blockers, and verification artifacts.

### 5. Implement With Central Integration Ownership

- Make the smallest correct fix for each proven finding and preserve repository conventions.
- Keep shared contracts, architecture decisions, dependency ordering, and final integration on the lead path.
- Apply `subagent-driven-development` only after slices are bounded, dependencies are known, and write scopes are disjoint enough to delegate safely.
- Integrate centrally after every worker slice; worker reports are evidence inputs, not completion.
- Avoid broad destructive cleanup, data resets, or production mutations without explicit authority and exact targets.

### 6. Run An Independent Gap Review

For broad or high-risk multi-slice delivery, assign a fresh reviewer after integration and before the release claim.

- Keep the review read-only unless fixes are authorized as a separate slice.
- Provide the user request, acceptance artifacts, current diff, runtime evidence, and verification results without leading the reviewer toward the intended answer.
- Ask specifically for missing flows, contract gaps, false completion claims, untested boundaries, and P0/P1 release blockers.
- Resolve or explicitly defer every material finding before closeout.

Use [references/adversarial-gap-review.md](references/adversarial-gap-review.md) for the review contract.

### 7. Verify The Integrated Product

- Re-run targeted checks after each slice and the repository’s full required gate after integration.
- Exercise the highest-value user journeys and affected negative paths through the active host’s canonical visible browser or device surface when runtime behavior matters.
- Verify API, worker, queue, migration, schema, data, and external-provider boundaries when they participate in the claim.
- Verify that docs, trackers, blockers, and committed artifacts match the actual state.
- Apply `verification-before-completion`, then `release-readiness` for the final verdict.

## Closeout Status

Report each material outcome with the strongest status the evidence supports:

- `implemented`
- `locally verified`
- `deployed`
- `live-provider verified`
- `production ready`
- `blocked` or `deferred`, with the exact missing condition

Never collapse these states into a generic “done.”

## Rules

- Do not start broad edits before the product inventory and baseline gate are known.
- Do not let a comprehensive audit degrade into a list of lint warnings or visual opinions.
- Do not claim every flow was tested unless the flow inventory and evidence matrix support that statement.
- Do not treat a worker’s success report, a green unit suite, or a build alone as whole-product verification.
- Do not erase data, regenerate secrets, reset environments, or remove broad directories as incidental hardening.

## References

- [references/audit-matrix.md](references/audit-matrix.md)
  Use to inventory product surfaces, audit dimensions, findings, and verification coverage.
- [references/adversarial-gap-review.md](references/adversarial-gap-review.md)
  Use for the independent post-integration challenge pass before broad release claims.
