# Browser QA

Use a fidelity matrix to keep the QA pass honest and repeatable.

Use the active host's canonical visible browser surface for interactive evidence. In Synara, that is the integrated browser; Computer Use is reserved for desktop or system UI, or cases the browser surface cannot finish. In Codex, follow the current app-provided browser or Chrome policy. Automated browser suites can add regression evidence but do not replace visible comparison.

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
