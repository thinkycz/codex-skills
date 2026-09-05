---
name: systematic-debugging
description: Prove the cause of a bug or failing flow before making an authorized fix.
version: 1.9.0
category: quality
sources:
  - Supplied task evidence and applicable project conventions
use_when:
  - Prove the cause of a bug or failing flow before making an authorized fix.
avoid_when:
  - The requested outcome belongs to another owner or exceeds the authorized scope.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Evidence supports the stated outcome and limitations.
  - Selected mode, references and actions remain within authorization.
---

# Systematic Debugging

Reproduce the actual symptom and record the expected result. Confirm app/server, build, environment and test-data identity before theorizing. Trace the failing boundary and form a falsifiable hypothesis; change one cause at a time. Compare working paths and inspect shared mechanisms when evidence shows the same failure across consumers. Diagnosis requests stop at the proven cause and proposed fix. For authorized fixes, protect meaningful behavior with a regression check and rerun the original exact path plus affected checks. After repeated failed hypotheses, widen evidence rather than stack speculative patches. For async/flaky failures inspect readiness, retries, worker runtime, shared fixtures, races and stale assets. Keep records proportional to complexity.

## Working evidence

Reuse existing repository identity, relevant changes, acceptance criteria, canonical examples, required checks and blockers. Refresh only invalidated facts. Stay within the requested scope and applicable permissions; report observed evidence and remaining gaps separately.

## Selected detail

Read only what the current task needs; supporting references do not mandate extra workflow stages.

- [Docs Layout](references/docs-layout.md): for docs layout.
- [Evidence And Tracking](references/evidence-and-tracking.md): for evidence and tracking.
- [Flaky And Async Debugging](references/flaky-and-async-debugging.md): for flaky and async debugging.
- [Repeated Failure Escalation](references/repeated-failure-escalation.md): for repeated failure escalation.
- [Root Cause Tracing](references/root-cause-tracing.md): for root cause tracing.
- [Skill Routing](references/skill-routing.md): for skill routing.
- [Verification](references/verification.md): for verification.
