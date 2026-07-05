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

## Response Behavior

- success payloads are stable enough to consume
- validation or error payloads are documented
- pagination, filtering, and sorting behavior are clear where relevant

## Relationships And State

- related entities and includes are supported consistently
- lifecycle or status transitions are explicit

## Rule

- If the frontend depends on behavior not confirmed by the contract, call it out before implementation starts.
