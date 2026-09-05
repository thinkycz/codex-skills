# Output Completeness

Use this when auditing whether the delivered UI work is actually complete.

## Incomplete Output Smells

- comments like "TODO", "add more later", or "implement if needed" in core user-facing paths
- placeholder sections standing in for real states
- missing loading, empty, or error handling
- missing responsive behavior for major breakpoints
- icons, images, or fonts left as obviously temporary substitutions without being documented as blockers

## Rules

- Do not present half-finished scaffolding as a finished UI pass.
- If something is intentionally deferred, name it explicitly in the docs or closeout.
- A design polish pass should reduce placeholders and ambiguity, not preserve them.
