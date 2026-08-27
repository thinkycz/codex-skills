# Live And Presentation Closure

Use this reference when a ticket is reported broken in a live environment or changes repeated UI or email presentation.

## Live Artifact Matrix

Record only the fields relevant to the ticket:

- intended source branch and commit
- deployed server commit or artifact identity
- migration state
- generated client or asset build identity
- worker process and queue name
- installed mobile build identity
- exact newest QA path and observed result

Code, tests, and builds can establish `implemented`. A live ticket is `fixed` only after the intended artifact is running and the newest QA path succeeds there.

If the ticket still fails after an earlier completion claim, stop patching and route to `systematic-debugging` to compare the exact running artifact and boundary evidence.

## Shared Presentation Matrix

Before editing UI or email HTML, identify:

- the semantic primitive or template owner
- variants and states required
- all consuming routes, screens, or email families
- responsive widths or client constraints
- evidence required for each consumer

Use one shared component contract for repeated buttons, links, tags, badges, inputs, cards, and similar controls. Use one shared email base layout and reusable partials/components for repeated brand, typography, spacing, CTA, header, and footer behavior.

For interactive browser evidence, use the active host's canonical visible browser. Repository-owned Playwright suites may add automated evidence, but they do not replace replaying the live ticket path.
