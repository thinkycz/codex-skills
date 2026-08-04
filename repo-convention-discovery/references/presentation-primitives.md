# Presentation Primitive Discovery

Use this reference before implementing UI or email HTML in an existing repository.

## Search

Inventory:

- shared component directories and design-system packages
- button, link, tag, badge, chip, input, card, modal, and form primitives
- variant helpers, tokens, icon registries, and accessibility conventions
- email base layouts, renderers, partials/components, and style helpers
- all current consumers of the semantic pattern being changed

## Decide

- Reuse an existing primitive when its contract already fits.
- Extend the shared primitive with a named semantic variant when several consumers need the same behavior.
- Consolidate duplicated implementations when they represent the same product concept.
- Keep a local implementation only when the behavior is genuinely feature-specific; record the reason.
- Treat application UI and email HTML as parts of one visual language even when their rendering technology differs.

## Report

Summarize:

- the owner primitive or template
- variants and states already supported
- affected consumers
- inconsistencies or duplicates worth consolidating
- the safest shared edit point
