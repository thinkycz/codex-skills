# Comparison Rubric

Use this when comparing frontend expectations against contract evidence.

## Route Surface

- endpoint exists
- method matches expectation
- auth and permission assumptions are explicit

## Payload Shape

- field names and nesting match
- optional versus required fields are clear
- enums and value domains are explicit
- omitted, explicit `null`, empty string, and default values remain distinct where the provider treats them differently
- internal routing, discriminator, or UI-helper fields are removed unless the provider contract explicitly accepts them

## Transport Serialization

- multipart and `FormData` requests contain the expected wire values, not merely correct pre-serialization objects
- booleans, integers, timestamps, and enum-backed values are normalized to the provider's accepted scalar representation
- decimal timing or count values cannot leak into integer-only fields
- generated clients, request normalizers, and retry/outbox persistence preserve the same shape as the initial request
- Inertia or browser requests are compared using their real headers and complete payload when those affect response behavior

## Response Behavior

- success payloads are stable enough to consume
- validation or error payloads are documented
- pagination, filtering, and sorting behavior are clear where relevant

## Relationships And State

- related entities and includes are supported consistently
- lifecycle or status transitions are explicit

## Rule

- If the frontend depends on behavior not confirmed by the contract, call it out before implementation starts.
