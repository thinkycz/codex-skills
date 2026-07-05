# Flaky And Async Debugging

Flaky failures often come from guessing about timing instead of checking the real condition.

## Use This For

- tests that pass locally but fail in CI
- arbitrary waits or sleeps
- race conditions
- async state propagation bugs
- event ordering issues

## Default Rule

Wait for the condition you care about, not a guessed delay.

Prefer:

- polling for a state transition
- waiting for an event or emitted output
- checking file existence or count changes
- asserting on real readiness signals

Avoid:

- arbitrary `sleep`
- blind retries without new evidence
- increasing timeouts as a first response

## Investigation Moves

- compare timing-sensitive failing runs with stable runs
- capture the exact missing condition
- inspect whether stale cached state is being checked
- verify if the system is waiting on the wrong signal

## When Timeouts Are Legitimate

Only use fixed waits when the behavior under test is itself time-based, and document why the duration is correct.
