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

## Live Runtime Parity

When the API, worker, scheduler, or provider path may be running different facts, record them side by side:

| Runtime fact | API or producer | Worker or consumer |
| --- | --- | --- |
| PID and process start time |  |  |
| Deployed commit or artifact identity |  |  |
| Executable and runtime version |  |  |
| Actual process environment source and relevant values |  |  |
| Loaded service unit and `ExecStart` |  |  |
| `WorkingDirectory`, user, and group |  |  |
| Last reload or restart time |  |  |
| Queue driver and queue name |  |  |
| Broker host, database/index, key prefix, and cluster mode |  |  |
| Route, migration, and live schema state |  |  |

Read the actual running process and loaded service definition. Do not infer parity from a shared `.env` file, source unit file, or deployment directory alone.

## Queue And External-Provider Lifecycle

Trace each boundary with timestamped evidence:

1. request handling reaches and awaits or commits the dispatch
2. the broker contains the intended message on the intended queue
3. the expected worker process picks up that message
4. the worker sends the expected provider request
5. the provider returns the observed status and schema
6. the application stores the intended outcome
7. callbacks or webhooks are processed when applicable
8. the final user-visible or externally observable result occurs

Capture request/response status and live schema at each handoff that can transform the payload. A `2xx`, `queued`, `sent`, broker insertion, or worker pickup is only an intermediate signal unless it is the requested outcome.

## When Timeouts Are Legitimate

Only use fixed waits when the behavior under test is itself time-based, and document why the duration is correct.
