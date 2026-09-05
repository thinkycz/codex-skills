# Boundary Checks

Apply the rows relevant to the product inventory. Record evidence or `not checked`; do not create speculative findings or expand a focused task into a full audit.

| Boundary | Probe | Evidence needed |
| --- | --- | --- |
| Account, session, device | Open two independent sessions for one account; change the active workspace on one and submit from the other. Distinguish same-session tabs from independent devices. | Explicit owner and persistence scope for each preference; no unintended cross-device switch or stale-context write. |
| HTTP and direct calls | Trace the same mutation through controller, job, command, assistant/tool, and direct service entrypoints where present. | Authorization at the actual mutation boundary or an explicit trusted internal contract; denied calls leave no data or file changes. |
| Validation and domain inputs | Exercise omitted, null, empty, zero, false, and string-encoded values accepted by transport validation. | Domain constructors and assertions accept the validated contract or reject it with a controlled error. |
| Authentication lifecycle | Change/reset passwords, revoke access, disable an account, and revisit existing tokens and sessions. | Observed behavior matches the intended revocation policy across credential types; do not invent a new policy. |
| Archive and ownership | Compare list, search, ordering/neighbors, relation options, background work, and restore paths. | Prospective selectors exclude unavailable records consistently while historical references remain valid. |
| Business dates | Compare server UTC, business timezone, user-local display, and persisted timestamps near midnight and DST transitions. | Shared business-date rules where required; no naive date truncation or fixed-offset assumptions. |
| Concurrency and retries | Submit stale edits, race two writers, repeat a request, time out after an external effect, then retry. | Transactions/version checks and idempotency rules preserve invariants on the production database engine; an uncertain external result is reconciled before replay. |
| Historical money | Change current prices, tax, recipes, or rounding rules after creating a document. Reverse or reopen it through supported flows. | Historical snapshots and totals retain the agreed policy; no retroactive recalculation or data repair without scope. |

Use a small counterexample to establish a defect. A green suite, a controller policy, or a prior audit does not prove all entrypoints preserve these invariants. If implementation is authorized, group tests and fixes by the shared root cause rather than duplicating patches across callers.
