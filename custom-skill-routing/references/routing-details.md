# Routing Details

Use this when the compact route matrix is not enough to choose one primary owner.

## Planning And Product

- `product-brainstorming` owns fuzzy product direction, UX tradeoffs, and early design direction.
- `clarify-before-plan` owns a small number of high-impact questions against an otherwise usable spec.
- `grill-with-docs` owns deeper plan interrogation against repo code, domain docs, terminology, scenarios, and ADR-worthy tradeoffs.
- `ticket-batch-intake` owns Trello/Jira/board exports before implementation: read all comments, preserve order, identify prior-agent verification work, and produce summaries or contract notes.
- `architecture-deepening-audit` owns read-only audits for shallow modules, leaky seams, low-locality abstractions, and deepening opportunities before broad refactors.
- `throwaway-prototype` owns disposable logic/state or UI-variant prototypes when a small artifact can answer a question before production delivery.
- `design-to-prd` owns turning an existing design source into a written PRD.
- `spec-driven-development` owns traceable delivery from written specs, design handoffs, or normalized ticket inputs.

## Execution And Resume

- `traceable-delivery` creates and maintains durable delivery artifacts when progress, blockers, mappings, and verification would otherwise live only in chat.
- `docs-driven-execution` executes from an already-trusted plan and progress tracker under `/docs`.
- `task-decomposition-and-resume` owns slice boundaries, dependency order, and safe parallelism.
- `artifact-resume-audit` owns restart selection when old docs or exports may be stale or contradictory.
- `session-handoff` owns creating a fresh continuation handoff for another agent or future session from the current conversation and local evidence.
- `subagent-driven-development` owns lead-worker execution only after slice boundaries are clear.

## Design And Source Adapters

- `figma` and `google-stitch` own source acquisition only.
- `design-to-traversable-app` owns multi-screen implementation into a real app flow.
- `design-fidelity-polish` owns exact parity after screen coverage exists.
- `frontend-redesign-audit` owns diagnosing weak existing UI before redesign.
- `design-system-export` owns stable reusable visual guidance after the direction is settled.

## Integration, Debugging, And Verification

- `api-contract-review` is read-only contract comparison.
- `integrating-backend-api-into-frontend` owns implementation against a verified or partial backend contract plus browser QA and blockers.
- `systematic-debugging` owns root-cause discovery before fixing.
- `test-driven-development` owns red-green-refactor when a meaningful automated check can lead.
- `e2e-verification-handoff` writes an executable browser/API/manual verification plan for another agent.
- `two-axis-review` owns branch, PR, or WIP review against both documented repo standards and the originating spec, issue, PRD, or plan.
- `verification-before-completion` proves a specific completion claim.
- `release-readiness` decides final go/no-go across evidence, blockers, and docs.

## Skill Operations

- `skill-maintenance-and-validation` owns package correctness.
- `skill-stocktake` owns portfolio overlap, bloat, refresh, merge, keep, or retire decisions.
- `cross-tool-packaging` owns export shape, flattened bundles, catalogs, and compatibility.
