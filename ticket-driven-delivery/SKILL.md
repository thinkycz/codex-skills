---
name: ticket-driven-delivery
description: Use when implementing, verifying, or finishing code changes from Trello, Jira, Linear, GitHub Issues, or similar tickets, especially when the work includes prior-agent validation and stakeholder ticket comments after delivery.
version: 1.2.0
category: execution
sources:
  - ticket evidence, acceptance criteria, QA comments, and current repo state
  - implementation diffs, verification logs, and ticket-system closeout needs
use_when:
  - The user asks to implement an approved ticket plan or ticket batch.
  - The user asks to verify whether another agent correctly implemented tickets and then fix gaps.
  - The user asks to write ticket comments summarizing what was fixed and how.
avoid_when:
  - The ticket evidence has not been gathered yet; use ticket-batch-intake first.
  - The task is only a code review without implementation or ticket closeout; use two-axis-review.
  - The task needs durable multi-phase docs before coding; use traceable-delivery or docs-driven-execution.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Ticket evidence is compared against current repo behavior before coding or commenting.
  - Newest QA or customer comments override older assumptions.
  - Current-workspace fixes and handoff-only responsibilities are not blurred together.
  - Implementation, verification, and ticket closeout comments are kept distinct.
  - Ticket comments are stakeholder-friendly and written in the requested language.
---

# Ticket Driven Delivery

Turn ticket evidence into implemented, verified, and clearly closed-out work.

Use this skill after ticket evidence is known and the user wants implementation, verification of another agent's work, or comments back to the ticket system.

## Boundary

- Own ticket-driven implementation, verification, and closeout comments.
- Do not gather ticket batches from scratch; hand off to `ticket-batch-intake` when descriptions, comments, attachments, or checklists still need to be read.
- Do not replace `two-axis-review` for pure review findings.
- Do not replace `release-readiness` for final go/no-go decisions.

## Core Promise

- Compare ticket evidence against current repo behavior before changing code.
- Treat newest QA, customer, or reviewer comments as authoritative when they conflict with older text.
- Verify prior-agent work before trusting it.
- Keep implementation evidence separate from stakeholder closeout summaries.
- Write ticket comments that explain what changed without dumping internal diffs.
- When the needed app or repo is absent, close out only the work actually completed here and name the remaining handoff explicitly.

## Workflow

### 1. Confirm Evidence And Current State

- Start from the ticket plan, comments, attachments, and acceptance criteria already gathered.
- Inspect current repo state, dirty files, relevant code paths, and existing tests.
- Identify generated clients, serializers, localization outputs, codegen files, or other derived artifacts touched by the ticket. Check repository conventions to determine whether they are tracked, ignored, or regenerated only in CI.
- If another agent may have worked first, identify what is already implemented, what is partial, and what is still missing.
- Confirm which repos are present before claiming a web, mobile, admin, backend, or API change is implemented.
- Preserve unrelated dirty work; do not revert changes you did not make.

### 2. Implement The Smallest Correct Fix

- Follow repo conventions and nearby patterns.
- Keep changes scoped to the ticket behavior and shared contract implied by the evidence.
- When several tickets overlap, fix the shared root cause once and map it back to each ticket.
- Regenerate required derived outputs with the repository's canonical tooling. Do not hand-edit generated files unless the repository explicitly uses that workflow; if outputs are ignored, still regenerate them locally when needed to prove the source annotations and runtime contract are coherent.
- Do not encode ticket-system IDs into product code unless the repo already has that convention.

### 3. Verify Freshly

- Run focused checks for the changed surface.
- Verify generated output consistency when code generation is part of the touched surface, and report whether regenerated files are tracked, ignored, or expected from CI.
- Verify the user-visible lifecycle when practical, not only the lowest-level helper. For example, prefer the route/page/API flow that reproduces the ticket over a narrower unit assertion alone.
- Separate new failures from pre-existing repo warnings or broken starter tests.
- If full test suites are blocked, record the exact blocking failure and still run smaller useful checks when possible.
- Do not claim a ticket is fixed from code inspection alone when a cheap automated or manual check is available.

### 4. Close Out Tickets

- Write comments only after implementation and verification evidence exists, or clearly say the ticket is verification-only/no-code-change.
- Use the user's requested language.
- Prefer stakeholder-friendly structure:
  - what was wrong
  - how it was fixed
  - relevant verification or caveat
- For mixed-scope tickets, include what was fixed in this repo and what remains for another repo/team.
- Avoid internal patch dumps, stack traces, private paths, credentials, or speculative claims.

Use `references/ticket-closeout-comments.md` for reusable Czech and English comment templates.

## Output

When finishing in chat, include:

- tickets handled
- user-visible changes
- verification run and known pre-existing failures
- ticket comments posted or ready to post

## Rules

- Do not skip the repo-state check.
- Do not treat prior-agent completion claims as evidence.
- Do not let old ticket descriptions override newer QA comments.
- Do not comment "fixed" on tickets before the implementation and verification status is known.
- Do not paste long diffs or sensitive internal details into ticket comments.

## Handoffs

- Use `ticket-batch-intake` when ticket evidence still needs to be collected or normalized.
- Use `two-axis-review` when the user asks for findings only.
- Use `verification-before-completion` when the main risk is an unproven completion claim.
- Use `traceable-delivery` when the ticket set is broad enough to need durable docs.
