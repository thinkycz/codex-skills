# Runtime Debugging

Use this reference when the integration compiles but fails in practice, or when the repo behaves inconsistently during verification.

## Debugging Mindset

Treat runtime failures as contract or state mismatches until proven otherwise. Do not patch blindly.

Work in this order:
1. reproduce the issue
2. identify the exact route, action, or component involved
3. inspect the live payload or failing request
4. compare it to the frontend assumptions
5. fix the narrowest wrong assumption
6. rerun static and browser verification

## Common Runtime Problems In Integration Work

### Undefined collection crashes

Symptoms:
- `.map`, `.filter`, or `.length` throws at runtime

Typical cause:
- API returned `undefined`, missing data, or a differently nested structure

Response:
- normalize default arrays or defensive access where the feature expects a collection
- confirm whether the API layer or the component should own the fallback

### Missing locale keys

Symptoms:
- raw translation identifiers
- runtime i18n exceptions

Response:
- add the keys across all supported locales
- verify the route again after the locale fix

### Framework-generated artifact drift

Symptoms:
- typecheck fails on missing generated route types
- runtime references stale build output

Response:
- regenerate the framework artifacts with the normal build flow
- rerun typecheck after the build stabilizes
- do not misclassify this as a domain integration issue

### Component wrapper regressions

Symptoms:
- selects, comboboxes, placeholders, or labels render incorrectly
- form wrappers compile but behave badly at runtime

Response:
- inspect shared wrappers before patching individual pages
- fix the shared component once when the bug is systemic
- verify on at least one real affected route

### Contract mismatch on writes

Symptoms:
- `422`, `400`, or validation errors on create/edit despite apparently correct UI

Response:
- inspect the real request payload
- compare the exact field names, nesting, enums, and date serialization to backend expectations
- normalize in the feature API or mapping layer instead of ad hoc page fixes

## Completion Standard After A Fix

After a runtime fix:
- rerun the relevant static checks
- re-test the affected route or action
- record whether the root cause was contract, locale, wrapper, cache, or framework related
