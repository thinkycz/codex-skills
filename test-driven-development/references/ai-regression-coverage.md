# AI Regression Coverage

Use this when the failure involves model output handling, prompt-shaped inputs, structured parsing, or automation transitions.

## Common Regression Shapes

- prompt-shape drift
- structured-output parsing drift
- serializer or deserializer mismatch
- enum or schema evolution
- state-transition bugs in agent or workflow orchestration
- retry or fallback logic that behaves differently under slightly different outputs

## Good Test Targets

- the shared parser or adapter
- the serializer boundary
- the workflow transition that failed
- the narrow integration layer between application logic and model-facing code

## Rules

- Prefer testing the reusable boundary over duplicating several symptom-level tests.
- Say plainly when the regression test is backfilled after the bug rather than written truly first.
- Keep AI-specific regression coverage realistic and deterministic where possible.
