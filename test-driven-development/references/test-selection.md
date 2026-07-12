# Test Selection

Choose the smallest test boundary that still proves the behavior the user cares about.

## Prefer

- unit tests for pure logic and branch-heavy rules
- integration tests for boundaries between modules, serializers, stores, and data layers
- UI or end-to-end tests only when the behavior truly depends on user-visible flows

## Visual And Asset Regressions

For missing icons, wrong color, distorted sizing, or interaction-state failures:

- use a component, widget, or browser-level assertion as the primary regression when the repo supports it
- use SVG attributes, asset hashes, mapping tables, or source strings only as supporting checks
- assert the consumer that failed, not merely that an asset file exists
- if automated rendering is unavailable, keep the source-level test and require an explicit runtime QA step before claiming the visual issue fixed

## Avoid

- brittle tests tied to incidental implementation details
- oversized integration tests when a smaller boundary would prove the same behavior
- using mocks so aggressively that the real behavior is no longer exercised
- proving only asset syntax when the user-visible defect occurs in rendering

## Confidence Ladder

After the first failing test goes green:

- run the targeted test
- run the nearest related file or suite
- run broader checks only when the touched surface or repo norms justify it
