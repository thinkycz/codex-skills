# Backend-to-mobile handoff

- State which repositories/platforms changed and which were only inspected. Backend completion does not imply the mobile UI has been implemented or a new binary distributed.
- Describe the endpoint, method, relevant request fields and sanitized response examples, including state/error cases. Identify what clients should display, hide, enable or refresh and the source-of-truth rule behind it.
- Keep visibility, action eligibility, confirmation and entitlement fields distinct. Do not recommend using one boolean for a different decision without checking its actual semantics across states.
- Include migration/build/worker prerequisites and test roles/data, then executable scenarios with expected outcomes. Cover relevant cancellation/reopening, duplicate actions, push foreground/background/cold-start behavior and recovery after missed notifications.
- State what the backend guarantees versus what the client must persist or deduplicate. A backend dispatch attempt is not proof of real device delivery or a displayed prompt.
- In a requested stakeholder comment, use the requested language, give verified code/commit evidence and label deployment/mobile acceptance still pending. Avoid dumping local paths or secrets; link to maintained project documentation when useful.
