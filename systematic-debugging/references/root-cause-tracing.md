# Root Cause Tracing

Fixing where the failure appears is often fixing the symptom, not the cause.

Trace backward through the call path, data flow, or state transitions until you reach the first bad assumption or input.

## Backward Tracing Loop

1. Observe the visible symptom.
2. Identify the immediate failing operation.
3. Ask what called it or supplied the bad value.
4. Repeat until you find the earliest incorrect state, input, or assumption.
5. Fix at that source.

## Evidence To Gather

- exact error message or failing assertion
- file and line information
- runtime values at the failing boundary
- call chain or stack trace
- equivalent working path for comparison

## Multi-Layer Systems

When the bug crosses boundaries such as UI → API → backend or test → app → dependency:

- instrument each boundary
- log what enters and exits
- compare expected vs actual propagation
- isolate the first boundary that diverges

## Rule

Never stop at the first place you can make the symptom disappear if you can still trace one step further back.
