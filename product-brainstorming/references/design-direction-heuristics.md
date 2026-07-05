# Design Direction Heuristics

Use this reference when a feature or redesign needs a clear UI direction instead of a generic "make it look better" answer.

## Product To Style Fit

- Match the visual direction to product type, audience confidence, and trust requirements before picking colors or effects.
- Trust-sensitive products such as finance, healthcare, legal, admin, and infrastructure usually want clarity, restraint, and obvious hierarchy over novelty.
- Creative, entertainment, youth, or brand-heavy products can support bolder typography, denser visual identity, and more expressive motion if usability stays intact.
- Internal tools and dashboards usually benefit from information clarity, strong spacing systems, and conservative ornamentation.
- When the product already has strong brand signals, extend them intentionally rather than replacing them with a trend-driven style.

## Anti-Pattern Framing

- Name what to avoid, not just what to pursue.
- Avoid product-inappropriate "AI-looking" gradients, glowing purple/pink defaults, or novelty-heavy chrome when the product needs trust, seriousness, or operational clarity.
- Avoid mixing multiple visual languages without a reason, such as flat controls next to glass panels next to skeuomorphic cards.
- Avoid decorative motion that distracts from task completion or makes the interface feel less trustworthy.
- Avoid relying on color alone to communicate state or priority.

## Icon Policy

- Do not use emoji as structural icons for navigation, settings, status, or controls.
- Use one coherent icon language across the feature or product.
- Treat icon choice as part of semantics and accessibility, not decoration.

## Color And Token Guidance

- Prefer semantic tokens such as `primary`, `surface`, `text`, `muted`, `success`, and `danger` over raw hex values in the design direction.
- Choose color families that reinforce the product mood without weakening readability.
- Test likely foreground/background pairings early when proposing a palette, especially for muted text, badges, and secondary actions.
- Dark mode, if included, should be a designed variant rather than an inverted afterthought.

## Typography Defaults

- Define the intended hierarchy, not just a font name.
- Keep body text readable first: sensible base size, relaxed line height, and enough contrast.
- Use display or expressive typography selectively where the brand benefits from it.
- Favor clear heading-to-body contrast so scanning works before any polish work begins.

## Early Accessibility Checks

Before locking the direction, sanity-check:

- text contrast expectations
- visible focus treatment
- reduced-motion expectations
- form and input clarity
- screen-reader and icon-label implications for critical controls
