# Logic Or State Prototype

Use this branch when the question is about rules rather than polish.

Good targets:

- workflow state machines
- reducers and transition rules
- scheduling, pricing, scoring, matching, filtering, or validation logic
- API payload shape experiments
- edge-case exploration before production tests exist

Structure:

- Put reusable logic in pure, portable code.
- Keep the runner disposable and thin.
- Seed representative examples directly in the prototype unless the user provides real fixtures.
- Print or render state transitions clearly enough that a human can compare outcomes.
- Avoid database writes, external side effects, auth setup, and durable storage by default.

Closeout:

- Name the behavior that should survive.
- Identify any production tests the real implementation should add later.
- Remove the runner or keep it isolated only if the user wants to keep exploring.
