# Scenario Rubric

Use these categories to build an E2E handoff that is specific enough for another agent to execute.

## Browser Flow

- route
- actor and role
- preconditions
- clicks, forms, redirects, loading states, modals, uploads, and responsive checks
- screenshot or trace evidence

## API Flow

- endpoint, method, auth role, request shape, response shape, and expected error states
- network or curl evidence
- database or resource state evidence when relevant

## Payment Or Stripe Connect Flow

- onboarding readiness
- checkout creation
- platform fee or application fee expectation
- webhook event and resulting local state
- success, cancel, and blocked-account behavior

## Upload Or Media Flow

- file type and size assumptions
- preview, submit, storage, list/detail visibility, and permission behavior
- locked/protected-media checks when full URLs must not leak before purchase

## Mobile/Web Parity

- matching backend contract
- same state transitions on web and mobile
- enum, decimal/integer, repeated-submit, and pending-state parity

## Reporting

Each scenario should end with one of:

- passed with evidence
- failed with exact failure
- blocked with missing setup
- not tested with reason
