# Audit Rubric

Use this rubric when reviewing an existing frontend before redesign work starts.

## Layout And Hierarchy

- Is the information rhythm intentional?
- Does the layout rely on generic centered-hero or repeated-card defaults?
- Does the page structure fit the product category?

## Typography And Spacing

- Is hierarchy clear without oversized headlines everywhere?
- Are spacing and density intentional?
- Does the type system feel default or product-specific?

## State Design

- Are loading, empty, error, disabled, and success states handled?
- Are important interactions understandable on touch and desktop?

## Consistency

- Do components feel like one system?
- Are cards, buttons, inputs, and navigational patterns coherent?

## Motion And Interaction

- Does motion add clarity or just decoration?
- Are transitions sane, performant, and restrained enough for the product?

## Simplification And Existing-Screen Parity

- If the user names an existing screen, compare its header, actions, navigation, spacing, form structure, and role-specific behavior. Preserve useful conventions and note necessary differences; do not invent a new shell by default.
- Inspect nested cards, panels inside panels, repeated headings, redundant borders, and competing toolbars. Recommend removing a container only when its grouping, semantics, or interaction purpose is unnecessary.
- Compare actual usable workspace at the user's normal window size and a smaller supported size. Large typography, permanent sidebars, and excessive gaps must earn their space; do not force compact styling on every product.
- Exercise short and long content. Check whether pagination and checkout/save actions remain reachable and occupy their intended position without hiding content, validation errors, or keyboard focus.
- Open overlays from each relevant trigger. Check backdrop coverage, clipping by parent containers, stacking, outside-click/Escape behavior, initial and restored focus, scroll locking, and accidental immediate dismissal.
- Capture before/after evidence at matching viewport, zoom, data, role, and state. For a desktop product, include native window sizes and platform conventions through `native-desktop-delivery` rather than treating a browser viewport as complete desktop proof.

Return a small ranked set of changes tied to observed friction. Keep decorative preferences separate from accessibility or functional defects.
