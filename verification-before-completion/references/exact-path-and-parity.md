# Exact Path And Parity Verification

Use this reference when completion depends on the running artifact, the original user path, or a claim that multiple clients or surfaces are the same.

## Evidence Matrix

Record each applicable level as verified, missing, or not relevant:

| Level | Evidence |
| --- | --- |
| Source | The intended code, asset, schema, or configuration changed. |
| Checks | Targeted tests plus relevant lint, type, or build checks pass. |
| Artifact | The intended build is installed, deployed, or running. |
| Original path | The user's exact route, payload, role, data, and interaction are replayed. |
| Outcome | The final visible or persisted result is observed. |

Use the cheapest sufficient stopping point. Do not require installation for a static text-only change, and do not stop at source or build for a device-only, deployment-only, or async lifecycle bug.

## Exact Artifact Identity

When observable, compare one or more of:

- revision or build identifier
- artifact hash
- build/install time
- deployed migration or route state
- simulator/device package contents
- worker or server process version

## Original-Path Rule

Reproduce the same meaningful conditions that produced the report:

- account role and permissions
- endpoint and payload shape
- selected entity and state
- locale, device, viewport, or payment mode
- persisted or deployed data dependencies

A nearby happy path is useful confidence, but it does not replace the reported path.

## Parity Dimensions

For `same`, `matching`, or parity claims, check every dimension named or implied by the request:

- semantic mapping: the same enum or category selects the same meaning
- content: the intended assets or data are equivalent
- rendering: color, dimensions, fill, visibility, and state behavior match
- consumers: every named screen, platform, or client uses the corrected mapping

State which dimensions were verified. Do not collapse one matching dimension into a blanket parity claim.
