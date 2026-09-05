---
name: workflow-contract-builder
description: Turn recurring personal or knowledge-work activities into safe, implementation-ready automation contracts before scheduling or connecting services.
version: 1.1.0
category: automation-design
sources:
  - user descriptions of current recurring work
  - relevant files, connected systems, and existing workflow artifacts
use_when:
  - A repeated activity needs a clear trigger, inputs, decision rules, output, approval boundary, and failure behavior.
  - Several automation candidates need transparent prioritization before implementation.
avoid_when:
  - A fully specified task only needs its already-approved schedule created or updated.
  - The user needs an audit trail of actions already taken rather than a future workflow design.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The current process and desired outcome are explicit.
  - External side effects and human approval boundaries are unambiguous.
  - Failure handling, observability, and acceptance checks are testable.
  - No schedule, connector, message, or external mutation is created without authorization.
---

# Workflow Contract Builder

Design a recurring workflow that is safe to test, easy to review, and concrete enough to implement without rediscovery.

## Boundary

Own workflow discovery, prioritization, and contract design. Do not create a schedule, install or connect a service, send a message, change external data, or begin a materially different implementation unless the user has authorized that action.

Use `workflow-audit-history` when the need is a record of past actions and approvals. Use the app’s automation tooling only after the workflow and schedule are approved.

## Workflow

1. Ground the current process.
   - Capture the activity, trigger, frequency, time per occurrence, inputs, source systems, decisions, output, destination, and present pain.
   - Inspect available source artifacts before asking for details that can be discovered safely.

2. Define the automation boundary.
   - Separate deterministic transformations from judgment calls.
   - Default to read-only collection or draft generation when the user has not authorized external mutations.
   - Make sending, deletion, purchasing, publishing, financial action, and record changes explicit approval decisions.

3. Prioritize transparently when there is more than one candidate.
   - Estimate monthly manual load from frequency and time per occurrence.
   - Weigh repeatability, data availability, reversibility, exception rate, and consequence of error.
   - Recommend one first candidate and state why. Do not hide the choice behind an unexplained score.

4. Write the contract.
   - Read [references/automation-contract.md](references/automation-contract.md) and include every applicable field.
   - Record assumptions as assumptions, and keep unresolved decisions visible.

5. Design the dry run and operating evidence.
   - Specify representative inputs, expected outputs, success criteria, failure signals, retry limits, and the stopping condition.
   - Require a dry run without external mutation before enabling autonomous side effects, unless the user has already explicitly authorized the first live run.
   - Prove one useful workflow with representative source inputs and an inspectable output before describing the system as operational. A dashboard, scheduled wakeup, or contract form alone is infrastructure.
   - Define a comparison baseline and notify only on meaningful changes, new failures, completion, or newly required user action unless periodic updates were requested. An unchanged blocker must not repeat the same reminder.
   - Define the run state the user should see: last run, next run, result, and failure or approval-needed status.

6. Hand off deliberately.
   - For a time-based workflow, create or update a scheduled task only after cadence, timezone, prompt, and approval boundary are explicit.
   - For connected systems, identify the minimum required connector and request authorization before account access or mutation.
   - For implementation, provide the contract and acceptance checks as the source of truth.

## Output

Return:

- the recommended workflow and why it comes first
- a complete automation contract
- assumptions and unresolved decisions
- a dry-run and verification plan, distinguishing infrastructure, a demonstrated workflow, and ongoing operation
- the single next action, distinguishing design from any action that still needs authorization
