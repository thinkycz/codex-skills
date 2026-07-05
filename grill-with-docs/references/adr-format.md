# ADR Format

ADRs live in `docs/adr/` and use sequential numbering:

- `0001-short-slug.md`
- `0002-next-decision.md`

Create `docs/adr/` lazily, only when the first ADR is genuinely needed.

## When To Record An ADR

Create or offer an ADR only when all three are true:

- The decision is hard to reverse.
- The decision would be surprising without context.
- The decision was the result of a real tradeoff.

Skip the ADR when a decision is obvious, easy to reverse, or has no meaningful alternative.

## Template

```md
# {Short title of the decision}

{One to three sentences explaining the context, what was decided, and why.}
```

Optional sections are allowed only when they add value:

- `Status`: proposed, accepted, deprecated, or superseded
- `Considered Options`: only for rejected alternatives worth remembering
- `Consequences`: only for non-obvious downstream effects

## Numbering

Scan existing files in the target `docs/adr/` directory, find the highest numeric prefix, and increment it by one.

## Good ADR Subjects

- Architectural shape or context boundaries.
- Integration patterns between contexts.
- Technology choices with meaningful lock-in.
- Deliberate deviations from the obvious path.
- Constraints not visible in code.
- Rejected alternatives that future maintainers are likely to suggest again.
