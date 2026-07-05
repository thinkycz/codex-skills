# Docs Layout

Apply `traceable-delivery` first for the shared `/docs` layout, tracker expectations, matrix discipline, and verification closeout.

This reference only covers the spec-driven files that are unique to delivery from client-provided source artifacts.

## Spec-Driven Overlays

### `/docs/specs/`

Prefer these files:

- `YYYY-MM-DD-<topic>-source-summary.md`
- `YYYY-MM-DD-<topic>-decisions.md`

Capture:

- artifact inventory
- what was provided vs missing
- normalized requirements
- source-of-truth decisions
- unresolved follow-up questions that are still safe to defer

### `/docs/plans/`

Prefer:

- `YYYY-MM-DD-<topic>-implementation-plan.md`

Keep the plan traceable to the source summary and decisions docs.

### `/docs/progress/`

Prefer:

- `YYYY-MM-DD-<topic>-traceability-matrix.md`
- `YYYY-MM-DD-<topic>-phase-tracker.md`

The matrix should distinguish written-spec rows from design rows.

### `/docs/verification/`

Add:

- `YYYY-MM-DD-<topic>-design-compliance.md` when design fidelity matters

Use the shared verification structure from `traceable-delivery`, then add requirement and design coverage details specific to the provided artifacts.
