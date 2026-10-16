---
name: teacha-staff-scheduling
description: "Review or update Teacha staff shifts and availability requests for a specified branch and calendar period. Source-code scheduling changes belong to development workflows."
version: 1.0.0
category: operations
sources:
  - Reviewed user-confirmed workflows and source artifacts
use_when:
  - "The user asks to review availability, approve requests, add or replace Teacha shifts, or manage a requested month lock."
avoid_when:
  - "The task changes scheduling source code or concerns a personal calendar."
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - "Branch, period, worker and requested times match each persisted assignment."
  - "Existing assignments and conflicts are inspected before creation, replacement or retry."
---
# Teacha staff scheduling

Operate the requested branch roster through the available connected interface or logged-in browser. Read [the roster procedure](references/roster.md) for availability, assignment, replacement and verification. Review-only requests do not authorize roster changes.

- Establish branch, calendar month/year, employees, dates and requested hours from the current request. Prior shifts are examples, not defaults. Availability is a request, not an assignment.
- Keep a small branch/date/worker checklist for a batch. Reconfirm context after navigation or switching branches; do not carry the previous branch's selection into a write.
- A request to update shifts authorizes its specified assignments. Unspecified overlap overrides, request locks, payroll/rate edits and employee messages need their own scope.
- Verify persisted assignments after saving and report completed dates, conflicts and unresolved items. Do not claim a month is staffed from request visibility alone.
