# Skill Routing

Apply `custom-skill-routing` first for the shared routing model across your local custom skills.

This reference only covers the debugging-specific routing choices that are unique to root-cause investigation.

## Default Routing

### Regression tests and bug reproduction

Use:

- `test-driven-development`

Choose this when:

- the bug can be expressed as a failing automated test
- the final fix should be protected from regressions

### Completion and proof

Use:

- `verification-before-completion`

Choose this always before claiming:

- fixed
- passing
- resolved
- matching expected behavior

### Visual or design-fidelity bugs

Use:

- `figma`
- `google-stitch`
- `design-to-prd`
- `design-fidelity-polish`

Choose this when:

- the bug is tied to layout, styling, interactions, or mismatch against the active design source

Use `design-to-prd` when the real issue is not pixel mismatch but the absence of a trustworthy written product interpretation of the design.

### Frontend/backend contract bugs

Use:

- `integrating-backend-api-into-frontend`

Choose this when:

- the failure spans API responses, form submission, backend support, or runtime integration behavior

### Spec/design mismatch mistaken for a bug

Use:

- `spec-driven-development`

Choose this when:

- the investigation reveals the code may be consistent, but the shipped behavior no longer matches the written specification or design source

### Ambiguous expected behavior

Use:

- `product-brainstorming`

Choose this when:

- the issue is really about deciding intended behavior, not finding a technical defect

## Routing Notes

- One investigation may use more than one helper skill.
- Route by dominant risk: regression, fidelity, integration, ambiguity, or scale.
