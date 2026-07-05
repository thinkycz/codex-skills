# API Contract Mapping

Use this reference when translating backend contracts into existing frontend behavior.

## Contract Inspection Order

1. Read the published OpenAPI or Swagger spec.
2. Check the live payload shape if the spec is incomplete, stale, or ambiguous.
3. Compare the contract to the current frontend route and form behavior.
4. Identify what is supported, partially supported, or unsupported.

## Map Behaviors, Not Just Endpoints

For each user-visible feature, map:
- list page -> exact index endpoint and filter/query params
- detail page -> exact show endpoint and response shape
- create/edit form -> exact store/update endpoint and payload shape
- archive/destroy action -> exact archive/delete endpoint
- tab or related section -> relationship or included data, or a secondary filtered fetch
- document/file action -> real download or generate endpoint, if any
- communication/message flow -> real list/history and post actions

## Preferred Frontend Pattern

- keep a thin typed API layer near the feature
- add mapping helpers between backend payloads and UI/form models
- reuse shared serialization and response normalization helpers
- preserve the repo's current routing and feature boundaries

Do not introduce a new global data framework just because the integration is broad.

## Relationships And Included Data

When the backend exposes `relationships` or `included`:
- prefer rendering from included resources when the data is already present
- if only related IDs are present, use a targeted filtered follow-up fetch
- do not fetch whole index collections just to filter client-side if the relation IDs can scope the request
- do not invent write actions for relations unless the backend exposes them

## Contract Truth Rules

- Prefer the live backend contract over stale written specs when they disagree.
- Prefer observed payloads over guessed schemas.
- Keep unsupported behavior explicit in UI and docs.
- If a field or enum is inconsistent, normalize deliberately in one place rather than spreading assumptions through the UI.

## Common Integration Gaps

Watch for:
- wrong query parameter shape causing `422`
- multipart vs JSON payload mismatches
- stale frontend enum options
- timezone-sensitive date fields
- missing relation support in detail pages
- write actions implied by the spec but absent from the live contract
- file actions that have metadata but no actual download endpoint

## Acceptance Standard

A contract mapping is trustworthy when:
- the request shape matches the real backend
- the response shape is normalized consistently
- the UI renders real live values
- unsupported actions are blocked explicitly
- real mutations succeed in-browser
