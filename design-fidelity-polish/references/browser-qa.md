# Browser QA

Use a fidelity matrix to keep the QA pass honest and repeatable.

## Checklist Areas

- exact icons in all rendered states
- exact or documented-close fonts
- localized images and logos
- active and inactive nav states
- container widths and card heights
- overlay coverage and dismissal behavior
- slideover ownership and full-height behavior
- button sizing and text styling
- state-only interactions reachable from parent screens
- accessibility, interaction, typography, layout, and motion checks from `ui-quality-checklist.md`

## Status Language

Prefer explicit states such as:

- exact
- close
- blocked
- unresolved

Avoid a single flat `implemented` label for fidelity work.

## Closeout Rule

Do not say the app is 1:1 unless:

- the asset source is correct
- the key interactions behave like the design
- the UI quality checklist does not have unresolved critical failures
- the remaining deltas are either zero or explicitly documented as constraints
