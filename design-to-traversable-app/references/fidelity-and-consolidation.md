# Fidelity And Consolidation

## Consolidation Rule

Every source screen should map to exactly one of:

- a standalone route or page
- a named interaction on a parent route or page

Do not leave screens in an ambiguous middle state.

## Consolidate By Default

Treat these as parent-state interactions unless the user explicitly wants separate URLs:

- dialogs
- drawers
- tab states
- joined or answer states
- review states
- slideovers

## Fidelity Rule

Preserve the visual intent of the source while translating into repo conventions.

- prefer exact assets over approximations when acceptance depends on fidelity
- localize unstable remote assets
- document remaining constraints honestly

## Overlay Rule

If an overlay visually covers the viewport, implement it at the viewport layer instead of clipping it to a local container.
