# Full Project Audit Matrix

Use one row per meaningful product surface, boundary, or user flow.

| Surface or flow | Roles and states | Repos or services | Audit dimensions | Existing evidence | Finding and severity | Fix slice | Verification | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

## Coverage Dimensions

- correctness and regression behavior
- authentication, authorization, input safety, secret handling, and dependency security
- architecture, shared contracts, generated artifacts, and repository conventions
- schema, migrations, persistence, serialization, and API compatibility
- workers, queues, schedules, webhooks, email, payments, uploads, and external providers
- UI completeness, responsive behavior, accessibility, interaction states, and design consistency
- tests, build/release gates, observability, operational docs, and recovery paths

## Finding Contract

For every actionable finding, record:

- direct evidence and reproduction path
- user or operational impact
- severity and why it earns that severity
- local versus shared root cause
- dependency order and bounded write scope
- required proof before the row can be closed

Keep `not checked`, `checked with no finding`, `finding open`, `implemented`, `verified`, `blocked`, and `deferred` distinct.
