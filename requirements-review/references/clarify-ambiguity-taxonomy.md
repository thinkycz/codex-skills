# Ambiguity Taxonomy

Use this taxonomy to decide whether a spec gap deserves clarification before planning.

## High-Impact Categories

- functional scope and success criteria
- out-of-scope boundaries
- data entities, identity rules, and state transitions
- user journeys, empty states, and failure states
- non-functional expectations such as latency, reliability, observability, and security
- external services, integrations, and failure behavior
- measurable completion signals and acceptance expectations

## Usually Worth Clarifying

- a missing rule would change architecture
- a missing decision would change task sequencing
- a missing constraint would change test design
- a UX ambiguity would change a critical user flow

## Usually Safe To Defer

- wording polish that does not change behavior
- implementation detail that belongs naturally in planning
- low-risk edge cases with no visible acceptance impact
