# Card Contract Notes

Use this shape when the user needs frontend, backend, mobile, or stakeholder-facing contract information from a ticket batch.

## Per Card

- **Card**: ID and title.
- **Goal**: one sentence in the user's requested language.
- **Affected surfaces**: backend, web, mobile, admin, OpenAPI, docs, design, or verification-only.
- **Contract**: endpoint, route, payload, response, state, event, or UI contract that another team must know.
- **Verification**: the smallest evidence that proves the card.
- **Status**: implementation-needed, verification-only, blocked, or needs clarification.

## Rules

- Keep stakeholder summaries short and pasteable.
- Keep contract notes concrete but do not invent payload fields that are not in the ticket or repo evidence.
- If a card is already implemented by another agent, mark the contract as verified or needs-verification instead of rewriting the plan.
