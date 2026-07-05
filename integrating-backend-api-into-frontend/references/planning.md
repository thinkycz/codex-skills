# Planning

Use this reference when the integration scope is larger than one safe implementation slice.

## When To Split Work Into Phases

Split the work when any of these are true:
- more than one feature area is involved
- the client spec is broader than the currently supported backend contract
- multiple list/detail/form flows must be connected
- the work includes open blockers that should stay isolated and traceable
- browser QA will need to be repeated module by module

## Phase Structure

Each phase should be a vertical slice, not a technical layer. Prefer:
- auth and entry flows
- admin foundation
- customers
- demands or inquiries
- offers and communications
- contracts and pricing
- stabilization and acceptance

Avoid phases like "all API files first" or "all forms later."

## What A Good Phase Must Contain

- a narrow feature scope
- exact user-visible behaviors to complete
- the backend contract or endpoints that support those behaviors
- the explicit blockers that remain outside the phase
- completion criteria that can be verified
- a note about locale parity if UI strings may change

## Phase Completion Standard

A phase is complete only when:
- the intended routes render from live backend data
- create/edit/archive or equivalent actions use real endpoints where supported
- validation and error handling are wired
- locale keys are present across supported languages
- lint, typecheck, and build are clean
- manual route checks were performed for the affected scope
- remaining gaps are classified, not hand-waved

## Revisit And Close Phases Honestly

When revisiting a phase:
- re-check the original blockers against the current backend reality
- confirm the route behavior still works after later changes
- convert resolved blockers into evidence
- move unresolved items into the correct blocker status
- only mark the phase completed when the remaining issues are genuinely outside the phase scope or backend-supported surface

## Plan Output Style

Keep plans implementation-ready:
- summarize the goal
- group key changes by behavior or subsystem
- list public interface or type changes only when they matter
- define test and manual verification scenarios
- state important assumptions explicitly

The implementer should not have to decide what "done" means.
