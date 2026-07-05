# Verification

Apply `traceable-delivery` first for the shared verification closeout structure and status discipline.

Do not claim a bug is fixed without fresh evidence.

Apply `verification-before-completion` before any success claim.

## Debugging-Specific Verification Layers

### 1. Original symptom

Re-run the exact reproduction that demonstrated the bug.

Check:

- the original failure no longer occurs
- the result changed for the expected reason

### 2. Regression protection

Run the relevant failing test and surrounding tests.

When possible:

- add a failing test first
- verify it fails before the fix
- verify it passes after the fix

### 3. Runtime or integration behavior

When the bug affects runtime behavior, also verify:

- browser flow
- API-backed behavior
- admin flow
- empty or error states
- cross-component behavior

### 4. Source-expectation compliance

If the bug is really a mismatch with written requirements or design expectations, verify against that source too.

### 5. Debugging closeout

Before calling the issue resolved:

- update the debug journal
- write the root-cause summary
- ensure the shared verification report references the proven root cause and reproduction outcome

## Red Flags

- saying “fixed” without rerunning the original reproduction
- trusting a speculative patch because tests passed once
- verifying only the symptom path and not nearby regressions
- claiming success without recording the proven root cause
