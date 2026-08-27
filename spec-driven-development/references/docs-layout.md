# Docs Layout

Apply `traceable-delivery` first for repository-root preflight, the shared `/docs` layout, tracker expectations, matrix discipline, and verification closeout.

This reference only covers the spec-driven files that are unique to delivery from client-provided source artifacts.

## Tracked-Home Preflight

Before creating any file below, verify the intended docs home with `git rev-parse --show-toplevel` or the repository's equivalent. The target must be inside that root, not ignored, and visible to version control.

For a non-Git parent containing several repositories:

- use a tracked coordination repo only when its ownership of the cross-repo work is clear
- otherwise keep repo-specific artifacts in each affected repository and include links plus repo/commit mappings between them
- do not create a sibling parent-level `/docs` tree and call it durable by default
- if no tracked home is safely inferable, keep only minimal chat tracking until the user chooses a home

If the user explicitly chooses untracked workspace docs, label that limitation in the tracker and final handoff.

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
