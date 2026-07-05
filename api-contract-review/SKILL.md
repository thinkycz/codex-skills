---
name: api-contract-review
description: Use when frontend assumptions, backend docs, schemas, or payload examples need a read-only contract review before integration or refactor work.
version: 1.3.0
category: quality
sources:
  - API contract comparison, payload review, and frontend-backend assumption checking
use_when:
  - The next safe step is to compare frontend expectations against backend contracts or payload evidence before coding.
  - A read-only contract review would reduce integration mistakes or schema drift.
avoid_when:
  - The task is already active implementation of a known-good contract.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The review stays read-only, compares assumptions against real contract evidence, and reports mismatches explicitly.
  - Missing consumer repos or unavailable payload evidence are reported as review limits, not silently filled with guesses.
---

# API Contract Review

Review API contracts and payload expectations before integration or refactor work begins.

This skill is a read-only preflight for contract-backed work. It compares frontend assumptions, backend docs, schemas, and payload evidence so integration does not start from guessed shapes or stale assumptions.

## Boundary

- Own read-only contract comparison before integration or refactor work.
- Do not edit code, schemas, generated clients, OpenAPI, or docs.
- Do not replace `integrating-backend-api-into-frontend` when implementation and runtime QA should begin.
- Do not replace `systematic-debugging` when a contract mismatch has become a runtime failure with unknown root cause.

## When To Use

Use this skill when:

- frontend behavior depends on an API contract that should be verified before coding
- schemas, payload examples, or docs may have drifted
- a read-only contract check would reduce integration mistakes, parsing bugs, or refactor risk
- the backend/API repo is present but the frontend, mobile app, generated client, or consumer repo is absent and needs a contract handoff

Do not use this skill when:

- implementation is already underway on a trusted, recently verified contract
- the work is backend architecture rather than consumer-side contract review
- there is no contract or payload evidence to compare yet
- the user wants the frontend/backend integration implemented; use `integrating-backend-api-into-frontend` after this read-only review if coding is needed

## Core Workflow

1. Gather the contract surfaces.
   - Read the OpenAPI, backend docs, JSON examples, schema files, or live payload samples that actually exist.
   - Ground in real evidence instead of summary prose when possible.
   - Record which expected consumer surfaces are absent or unavailable, such as mobile app, web app, generated client, screenshots, or live API credentials.

2. Compare consumer assumptions against provider evidence.
   - Check routes, methods, payload shapes, enums, optionality, relationships, pagination, validation errors, and state transitions.
   - Identify where the frontend is assuming more than the contract guarantees.
   - Pay special attention to enum backing types, JSON:API relationship shape, boolean values sent through `FormData`, nullable versus optional fields, and provider-prefixed namespaces that must not be merged into native fields.
   - When one field changes, check every consumer surface that can drift: create/edit forms, detail views, tables, admin resources, generated clients, locale keys, and notifications.
   - If a consumer repo is missing, translate the contract into an implementation handoff instead of implying the consumer behavior was verified.

3. Classify the mismatches.
   - confirmed alignment
   - ambiguous contract
   - stale docs
   - consumer-side assumption drift
   - provider-side missing support

4. Report what should happen next.
   - Recommend whether the next step is safe implementation, clarification, contract update, or deferred scope handling.

## Output

Produce a concise contract review with:

- contract surfaces reviewed
- assumptions checked
- confirmed alignments
- mismatches or ambiguities
- recommended next action
- handoff-only consumer work, when implementation cannot be verified from the current workspace

## Rules

- Keep the pass read-only.
- Do not edit frontend, backend, OpenAPI, generated clients, or docs as part of the review.
- Prefer real contract evidence over summaries.
- Distinguish stale docs from actual backend behavior when possible.
- Do not let guessed payload shapes quietly become implementation truth.
- Do not treat a single successful payload as full contract coverage when nearby states, roles, or relation variants use the same shape.
- Do not claim frontend or mobile integration is done when only backend contracts or docs were reviewed.

## References

Read these only as needed:

- [references/comparison-rubric.md](references/comparison-rubric.md)
  Use for route, payload, enum, validation, and relationship checks.
- [references/mismatch-types.md](references/mismatch-types.md)
  Use for classifying alignment, ambiguity, drift, and missing support.
