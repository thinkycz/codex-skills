# Email, authentication and checkout journeys

Match the test to the feature contract: an email-verification link may be repeatable, while a sign-in or recovery token may be one-time. Do not impose one contract on all links.

- Confirm target frontend/API/worker identity, mail sink and payment mode before tests. Use isolated synthetic accounts on an accepted test-email domain; DNS/MX validation can reject placeholder domains before mail sending starts. Do not weaken application validation to accommodate the test address.
- Trigger the real registration, recovery or purchase operation. In Mailpit or the configured sink, find the message for that recipient and attempt, check count, recipient, subject, masked data and actual link destination. A mocked send or success response does not prove delivery.
- Open the actual newly delivered link through the intended browser/device path. Exercise required query/fragment formats and redirects, including a root landing page when relevant. Verify the final visible state, token cleanup, appropriate permissions and subsequent login; keep credentials/tokens out of screenshots and reports.
- Test relevant missing, malformed, expired and reused links plus signed-in/signed-out behavior. A server error, rate limit or network failure must not be reported as evidence that a valid token was invalid. For password changes, check that the old password fails and the new one succeeds.
- Keep email verification distinct from separate identity, bank-detail or manual approvals. A working link does not establish those independent approvals.
- For checkout, verify base and discounted amounts, currency, package and free-completion path where supported. Submit a payment only in an explicitly identified sandbox within the authorized QA scope; a test-looking hostname alone is insufficient evidence of sandbox mode.
- Verify provider payment, local checkout state, account/ownership, exactly-once entitlements, worker/job completion and access-email outcome independently. Where the contract requires it, confirm processing starts after payment with the browser closed and that a return URL alone does not authenticate the buyer.
- Cover repeat/late events and existing/new accounts where relevant. Inspect previously failed purchases separately; a new successful checkout does not resolve an old paid-but-unfulfilled record. Do not replay it blindly after ownership has changed.

Record each exercised path and outcome, permitted cleanup and unresolved device/provider checks. A prepared scenario is not an executed result.
