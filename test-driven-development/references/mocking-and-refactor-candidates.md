# Mocking And Refactor Candidates

Use this reference when a TDD change touches external dependencies, hard-to-test seams, or post-green cleanup.

## Mock Boundaries

Mock system boundaries by default:

- external APIs such as payment, email, analytics, maps, or third-party services
- databases when a test database is unavailable or too slow for the target check
- time, randomness, filesystem, network, and platform APIs when deterministic control matters

Avoid mocking:

- internal modules the repo owns
- ordinary collaborators that can be reached through the behavior surface
- private helpers or implementation steps
- local domain logic that should be exercised directly

Follow established repo test conventions when they deliberately choose a different boundary, but call out the tradeoff.

## Designing For Boundary Tests

- Prefer dependency injection at external edges instead of constructing SDK clients deep inside domain logic.
- Prefer specific SDK-style wrappers such as `getUser` or `createOrder` over one generic fetcher that forces conditional mock logic.
- Keep fake responses close to the contract shape the production adapter returns, not the third-party raw payload unless that is the adapter under test.

## Refactor Candidates After Green

Once the test is green, look for:

- duplication that should become a shared helper or domain function
- long methods that can hide internal steps behind a clearer public interface
- shallow modules that should be combined or deepened
- feature envy where behavior belongs closer to the data it uses
- primitive obsession where a value object or named type would clarify rules
- tests that expose too many internals and should move to a deeper behavior surface

Do not bundle broad architecture work into the red-to-green step. Capture larger refactors as follow-up slices or hand off to `architecture-deepening-audit` when the structure question is bigger than the current behavior.
