# Automation Contract

Use this schema to make a recurring workflow implementation-ready. Omit fields only when they genuinely do not apply.

## Identity and Outcome

- **Name:** short, action-oriented workflow name
- **Owner:** person accountable for the result
- **Desired outcome:** observable value created by a successful run
- **Current manual load:** frequency, minutes per occurrence, and estimated monthly hours

## Trigger and Scope

- **Trigger:** schedule, user action, or event
- **Cadence and timezone:** required for time-based work
- **In scope:** records, date range, projects, people, or folders included
- **Out of scope:** explicit exclusions that prevent overreach

## Inputs and Access

For every input, record:

- source system or file
- required fields or context
- freshness requirement
- access mode: read, draft, or write
- behavior when data is missing, stale, duplicated, or unavailable

## Processing and Decisions

- deterministic transformation steps
- decision rules and thresholds
- judgment calls that remain human-owned
- exception paths
- duplicate and idempotency behavior

## Output and Destination

- output format and required fields
- destination system, folder, task, or chat
- naming and organization rules
- who can see the result

## Approval and Side Effects

Choose one operating mode:

- **Draft first:** produce a reviewable artifact; a person performs the mutation.
- **Automatic:** perform the approved action when all contract conditions pass.
- **Always ask:** request approval immediately before every external mutation.

List every possible external side effect. Authorization for one side effect does not imply authorization for another.

## Failure and Safety

- failure signals
- retry limit and delay
- non-retryable errors
- notification destination
- stopping condition
- rollback or recovery path
- sensitive-data constraints and retention

## Observability

- last-run timestamp and result
- next scheduled run
- input scope processed
- output location
- failure or approval-needed state
- manual override or pause path

## Meaningful Changes And Notification State

- Define the initial baseline, comparison fields, and what qualifies as meaningful new information. The initial run establishes a baseline unless the user requested an initial digest or it reveals an actionable condition.
- Record the last observed result and last notified result separately, using stable source identifiers or a semantic fingerprint. Compare substance, not regenerated wording or timestamps alone.
- Persist the last-notified state only after confirmed delivery. Handle uncertain delivery without blindly duplicating a message; reconcile when the destination supports it.
- Notify on a material change, completion, a new failure, or newly required user action. Keep unchanged or non-actionable runs quiet unless periodic status reports were requested.
- The same unanswered question or unchanged blocker is not a new event. Retain the pending decision and resume when inputs change; do not repeatedly ask for the same information.
- Specify what a later resolution or recurrence should do, and how pause/reset affects the baseline. Use the active app's real automation tools and schema rather than invented scheduler directives.

## Acceptance and Dry Run

Define at least:

1. one normal representative case
2. one missing-input or unavailable-system case
3. one duplicate or repeated-run case
4. one approval or side-effect boundary case

The first execution should be a dry run with no external mutation unless the user explicitly approves otherwise. A schedule existing is not proof of reliability; require successful run evidence before calling the workflow operational.

For a system containing several workflows, demonstrate one useful workflow from representative source inputs through processing to a reviewable output before claiming working automation. Record remaining manual steps explicitly. A dashboard, contract builder, or successful scheduled wakeup demonstrates infrastructure only.

Also test a first baseline run, a materially changed result, an unchanged result, repeated identical blockers, and recovery. Confirm duplicate suppression across restarts using persisted state. For a draft-first contract, a useful verified draft is a valid output; sending it is not required unless authorized.

## Prioritization When Comparing Candidates

For each candidate, show:

- estimated monthly manual hours
- repeatability and exception rate
- input accessibility
- reversibility
- consequence of error
- recommended approval mode

Recommend the candidate with strong time savings and a low-risk, testable first version. Explain the tradeoff in plain language instead of presenting an unexplained composite score.
