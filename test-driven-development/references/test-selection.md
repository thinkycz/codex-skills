# Test Selection

Choose the smallest test boundary that still proves the behavior the user cares about.

## Prefer

- unit tests for pure logic and branch-heavy rules
- integration tests for boundaries between modules, serializers, stores, and data layers
- UI or end-to-end tests only when the behavior truly depends on user-visible flows

## Avoid

- brittle tests tied to incidental implementation details
- oversized integration tests when a smaller boundary would prove the same behavior
- using mocks so aggressively that the real behavior is no longer exercised

## Confidence Ladder

After the first failing test goes green:

- run the targeted test
- run the nearest related file or suite
- run broader checks only when the touched surface or repo norms justify it
