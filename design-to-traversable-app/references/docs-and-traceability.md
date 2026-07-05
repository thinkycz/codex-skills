# Docs And Traceability

Apply `traceable-delivery` first for the shared docs layout, phase tracking, blocker visibility, and verification closeout.

This reference only covers the design-source-specific mapping rules unique to this workflow.

## Inventory Data Shape

Every source screen should map to data with at least:

- `id`
- `name`
- `slug`
- geometry or equivalent layout note
- `note`
- `href`
- `implementation` as `route`, `page`, or `state`
- `interaction`
- `implemented`
- `status` or equivalent progress state that can distinguish extraction, mapping, traversability, fidelity, and verification for non-trivial projects

## Mapping Rule

Every source screen must map to exactly one of:

- a standalone route or page
- a named interaction on a parent route or page

If the source changes, re-baseline the mapping and counts instead of layering corrections on stale numbers.

## QA Matrix Expectations

The fidelity matrix should:

- cover every top-level source screen
- note when a screen is represented by a parent-state interaction
- record known visual deltas
- record asset parity such as exact icons, localized images, and font parity
- record overlay and slideover parity when those behaviors are part of acceptance
- record known constraints such as missing fonts or placeholder content
- stay aligned with the shared progress and verification docs maintained by `traceable-delivery`
