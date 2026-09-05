# Shared Components And Email

Use this reference when a fidelity pass touches repeated UI elements or email HTML.

## Inventory First

Before editing, list the existing semantic primitives and their consumers:

- buttons and button-like links
- tags, badges, chips, and status pills
- inputs, selects, validation messages, and form actions
- cards, dialogs, drawers, and empty states
- email base layouts, headers, footers, CTA buttons, content sections, and typography helpers

Search every route, screen, and template that consumes the pattern. A reported mismatch is often evidence of a shared contract problem rather than one isolated page.

## Consolidation Rule

- One semantic pattern should have one shared implementation with explicit variants.
- Fix the shared component when consumers need the same behavior.
- Keep local wrappers only for composition, not for reimplementing size, color, focus, loading, disabled, icon, or spacing contracts.
- For email HTML, keep brand, typography, spacing, CTA, header, and footer rules in a shared layout or reusable partials.
- A true exception should state why the shared contract cannot represent it.

## Verification

For UI primitives, verify:

- every semantic variant
- default, hover, focus, pressed, loading, disabled, destructive, and empty states as applicable
- icon contrast on the rendered background
- all named consumer routes
- relevant desktop and mobile widths

For email HTML, verify:

- representative templates from each email family
- consistent brand, typography, spacing, CTA, header, and footer treatment
- narrow-client behavior and long-content wrapping
- links, accessible text, and plain-text fallback when the repo supports one

Use the active host's canonical visible browser surface for rendering and interaction checks. Repository-owned Playwright suites may add automated coverage, but they do not replace visible-browser evidence.
