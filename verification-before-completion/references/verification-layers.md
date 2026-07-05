# Verification Layers

Choose verification in layers based on the kind of claim being made.

## Common Layers

- targeted test
- nearby suite
- lint or typecheck
- build
- runtime or browser flow
- spec or PRD comparison
- design or fidelity comparison
- docs and blocker freshness

## Rule

The stronger the claim, the stronger the evidence should be.

- `fixed` usually needs reproduction proof plus regression confidence
- `implemented` usually needs tests and runtime confirmation
- `matched design` usually needs visual or interaction comparison
- `ready` usually needs docs, blockers, and broader readiness checks
