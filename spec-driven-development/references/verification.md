# Verification

Apply `traceable-delivery` first for the shared verification closeout structure and documentation discipline.

Apply `verification-before-completion` before any success claim.

This reference adds the source-artifact-specific checks that are unique to spec-driven delivery.

## Spec-Driven Verification Layers

### 1. Requirement compliance

Verify the implementation against the written client specification.

Check:

- required behaviors exist
- omissions are called out explicitly
- scope changes or deferrals are documented

### 2. Design compliance

When a design is part of the input, verify the implementation against it.

Check:

- layout and hierarchy
- content structure
- states and interactions
- spacing, typography, color, and component parity when fidelity matters

Use Figma-oriented helper skills when needed.

### 3. Contract or backend compliance

When the work touches API or admin behavior, verify against the real backend support or contract too.

### 4. Traceability closeout

Before calling the work complete:

- update the traceability matrix statuses
- update the phase tracker
- ensure the shared verification report points back to the relevant spec and design rows

## Red Flags

- saying "done" without fresh command output
- trusting subagent reports without independent checks
- claiming design parity without comparing against the design
- treating tests as a substitute for requirement review
- treating lint/build as a substitute for runtime or source-of-truth checks
