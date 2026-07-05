---
name: e2e-verification-handoff
description: Use when the user wants a detailed end-to-end verification plan for another agent to test browser, API, payment, upload, role, webhook, or mobile/web parity flows after implementation.
version: 1.0.0
category: quality
sources:
  - implemented feature scope, repo commands, seeded users, API contracts, and runtime routes
  - recent browser and payment verification handoff patterns from local Codex conversations
use_when:
  - The user asks for another AI agent or tester to verify implemented features end to end.
  - Runtime flows such as Stripe, uploads, roles, webhooks, mobile/web parity, or browser behavior need explicit test steps.
avoid_when:
  - The next step is performing the verification directly in the current session; use playwright or verification-before-completion.
  - The work is not implemented enough to define meaningful E2E scenarios.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The handoff names concrete scenarios, setup, accounts, routes, API checks, and expected evidence.
  - Payment, webhook, upload, role, and parity flows include positive and negative paths where relevant.
  - The output routes execution to playwright, verification-before-completion, or release-readiness as appropriate.
---

# E2E Verification Handoff

Write a verification plan another agent can execute without rediscovering the product.

Use this skill after implementation when the user wants a detailed browser/API/manual QA plan for another agent, especially for payments, Stripe Connect, uploads, role redirects, webhooks, mobile/web parity, or complex cross-surface flows.

This skill writes the handoff. It does not perform the browser run itself. Use `playwright` or the Browser plugin for execution, then `verification-before-completion` and `release-readiness` for the verdict.

## Boundary

- Own executable E2E verification plans for another agent or tester.
- Do not perform the browser/API verification run itself.
- Do not replace `verification-before-completion` for proving a specific claim from fresh evidence.
- Do not replace `release-readiness` for the final go/no-go verdict.

## Core Promise

- Turn implemented scope into concrete E2E scenarios.
- Include setup, credentials or seeded users, routes, API endpoints, and expected evidence.
- Cover positive, negative, role, and state-transition paths that matter.
- Make gaps and untestable external dependencies explicit.

## Workflow

### 1. Ground In What Was Implemented

- Read the implementation summary, plan, diff, docs, or progress tracker.
- Identify exact features, roles, routes, endpoints, payments, uploads, webhooks, and mobile/web surfaces involved.
- Inspect repo commands and seeded-user conventions when available.
- Do not ask another agent to verify a vague feature name without a scenario list.

### 2. Define Test Setup

Capture:

- repo or app to run
- commands for backend, frontend, mobile simulator, queue, webhook listener, or workers
- required environment values without exposing secrets
- seeded users, roles, and test data needed
- payment/test-mode assumptions such as Stripe test cards or connected-account readiness

### 3. Write Scenario Coverage

For each scenario, include:

- purpose
- actor and preconditions
- browser/API/manual steps
- expected result
- evidence to capture: screenshot, network response, database state, webhook event, log excerpt, or test output
- failure notes that should trigger debugging rather than a soft pass

Use `references/scenario-rubric.md` for common scenario classes.

### 4. Route The Executor

- Use `playwright` when a real browser flow should be driven by terminal commands.
- Use the Browser plugin when the user explicitly wants the in-app browser.
- Use `api-contract-review` for read-only API payload comparison before runtime checks.
- Use `verification-before-completion` to compare evidence to the claim.
- Use `release-readiness` for the final go/no-go summary.

## Output

Produce a compact E2E handoff with:

- scope under test
- setup commands and accounts
- scenario checklist
- API and browser evidence expectations
- known blockers or untestable dependencies
- final reporting format for the verifying agent

## Rules

- Do not include secrets.
- Do not assume webhooks, workers, or queues are running; state how to start or verify them.
- Do not stop at happy paths for payments, roles, uploads, or webhooks.
- Do not call the feature ready; the executor gathers evidence and release-readiness decides.

## References

Read these only as needed:

- [references/scenario-rubric.md](references/scenario-rubric.md)
  Use for choosing scenario coverage across browser, API, payment, webhook, upload, and parity flows.
