# Requirements Checklists

Treat requirement checklists as quality tests for the written spec, not as implementation verification.

## Good Checklist Questions

- Are success criteria measurable?
- Are important empty, loading, and failure states defined?
- Are accessibility and localization expectations explicit where relevant?
- Are edge cases defined for the risky parts of the workflow?
- Are roles, permissions, or security boundaries explicit?

## Avoid

- checklist items that verify implementation behavior
- checklist items that belong in automated tests
- vague prompts that cannot fail clearly

## Use In Analysis

If a checklist exists:

- compare it against the spec for coverage
- use it to spot untestable wording
- use it to identify gaps the plan and tasks may have inherited
