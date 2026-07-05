# Browser And Manual QA

Use this reference after implementation and whenever runtime behavior matters.

## Why Browser QA Is Required

Static verification catches type and build problems, but integration work often fails at runtime because of:
- wrong parameter shapes
- missing locale keys
- auth bootstrap issues
- broken redirects
- empty-state crashes from unexpected payloads
- real backend validation errors
- component rendering bugs that compile cleanly

## Minimum Verification Stack

Run:
- `npm run lint`
- `npm run ts`
- `npm run build`

Then manually verify the affected flows in the browser.

## Route Checks

For each touched module, verify as applicable:
- list page loads from live API
- filters/search state behaves correctly
- detail page renders mapped fields
- create page submits successfully
- edit page loads and updates successfully
- archive/delete action works and refreshes or redirects correctly
- relation tabs or panels render real related data
- empty states do not crash on `undefined` or empty arrays

## Auth And Locale Checks

Confirm when relevant:
- guest routes behave correctly when logged out
- logged-in users redirect away from guest-only entry routes
- logout returns the app to the expected login state
- localized routes stay localized after redirects or mutations
- both locale files cover any new strings

## Communication And File Flows

If the module includes messages or files, verify:
- existing history renders from live data
- sending a new message refreshes the thread
- generated document actions still work after related changes
- missing download support is clearly blocked instead of silently broken

## Evidence Recording

When you close work, capture:
- which commands passed
- which routes were exercised
- which mutations were confirmed
- which backend gaps are still blocking further behavior
