# Interface Design Exploration

Use this when one deepening candidate looks worth pursuing.

## Inputs

- Candidate module or behavior cluster.
- Current callers and tests.
- Current data shapes and domain terms.
- External dependencies and adapters involved.
- Constraints from ADRs, docs, framework conventions, or rollout needs.

## Compare Options

Sketch two or three materially different interfaces. For each one, capture:

- interface name and rough call shape
- what caller knowledge disappears
- what implementation complexity moves behind the interface
- how tests would change
- dependency direction and adapter placement
- migration cost and likely first slice
- risks or cases where the interface becomes too broad

## Selection Heuristics

Prefer the option that:

- reduces call choreography most clearly
- keeps domain language close to the rule it represents
- exposes stable behavior rather than intermediate steps
- supports meaningful tests at the interface
- avoids inventing an abstraction before there is a real second implementation or repeated concept

If the tradeoff is unclear, hand the candidate to `grill-with-docs` for a one-question-at-a-time challenge session before implementation.
