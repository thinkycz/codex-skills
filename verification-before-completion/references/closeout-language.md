# Closeout Language

Use direct status language that matches the evidence.

## Verified

Use when the evidence directly supports the claim and no important verification layer is knowingly missing.

## Partially Verified

Use when some important checks ran, but one or more meaningful layers are still unverified.

Prefer a precise implementation status when the missing layer is known:

- `Implemented, deployment required`
- `Implemented, runtime verification pending`
- `Built successfully; installed artifact not verified`

## Not Verified

Use when the relevant checks were not run, failed, or do not support the claim strongly enough.

Avoid vague language such as:

- should be fixed
- probably done
- looks good now
- seems matched
