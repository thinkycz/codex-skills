# Source Of Truth And Conflicts

This skill starts from user-provided artifacts, which may be incomplete or inconsistent.

## Source Inputs To Expect

- written client specification
- Figma links or node IDs
- screenshots or design exports
- OpenAPI or backend docs
- admin workflow notes

## Missing Artifact Rules

- Ask for missing artifacts directly.
- Continue exploring and planning with what exists when the missing input is not yet blocking.
- Record missing artifacts in `/docs/specs/` so the gap stays visible.
- Do not fabricate precise requirements to cover for missing source material.

## Conflict Rules

If the written specification and design disagree on any item that changes implementation, stop and ask the user which source has priority before planning or coding continues.

Common conflict categories:

- field presence or labels
- workflow order
- screen states
- CTA behavior
- permissions or admin behavior
- API expectations
- acceptance criteria

## Default Question

Use a direct question such as:

> The written specification and the design disagree on `<issue>`. Which source should I treat as the source of truth for this area?

## Decision Recording

Once the user answers:

- record the decision in `/docs/specs/...-decisions.md`
- update the traceability matrix if the conflict changes tasks or verification
- note any remaining follow-up risk

## When To Escalate Further

Escalate beyond a single priority question when:

- neither artifact is clearly current
- the conflict implies a major scope change
- backend constraints contradict both sources
- the repo already implements a third variant and migration impact is unclear
