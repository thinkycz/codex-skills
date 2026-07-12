---
name: ticket-batch-intake
description: Use when the user provides Trello, Jira, Linear, or other ticket-board exports, links, or IDs and wants evidence-grounded planning, stakeholder summaries, implementation contracts, or verification-first triage before coding.
version: 1.4.0
category: execution-planning
sources:
  - ticket-board exports, card descriptions, comments, labels, and existing repo state
  - recent sprint-planning patterns from local Codex conversations
use_when:
  - The user asks to plan or summarize a batch of cards, sprint tickets, Todo items, or board-column work.
  - The user provides ticket links or short IDs and expects the agent to retrieve descriptions, comments, attachments, or checklists before planning.
  - Ticket comments, prior-agent changes, contract summaries, or stakeholder-facing summaries materially affect the plan.
avoid_when:
  - A single already-clarified ticket can be implemented directly by the relevant domain owner.
  - Active execution from an approved ticket plan is underway; use ticket-driven-delivery unless existing `/docs` plans and trackers already control execution.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - All provided descriptions, comments, attachments, and checklists that are available are read before planning.
  - Missing or inaccessible ticket evidence is called out instead of silently inferred.
  - Board order, prior-agent verification, and contract/stakeholder summaries are handled explicitly.
  - Cards are classified as implementable in this repo, handoff-only, verification-only, blocked, or clarification-needed.
  - The output hands off to the correct implementation or decomposition owner.
---

# Ticket Batch Intake

Turn ticket-board exports into reliable implementation intake.

Use this skill before implementation when the user provides Trello, Jira, Linear, or similar card batches and asks for plans, summaries, contract notes, or ordered sprint work.

This skill owns intake and planning normalization. It does not execute the tickets. Hand off to `ticket-driven-delivery`, `spec-driven-development`, `task-decomposition-and-resume`, or `docs-driven-execution` once the batch is clear.

## Boundary

- Own ticket-board intake, ordering, summaries, contract notes, and verification-first classification.
- Do not execute approved ticket plans; hand off to the implementation owner.
- Do not replace `api-contract-review` when the next step is only read-only API comparison.
- Do not replace `ticket-driven-delivery` once an approved ticket plan is ready for ordinary implementation, verification, and tracker closeout.
- Do not replace `docs-driven-execution` when trusted `/docs` plans and progress trackers already control the work.

## Core Promise

- Read every provided card description, comment, attachment, and checklist before planning when the source allows it.
- Preserve board or column order unless dependency evidence requires a different sequence.
- Detect when other agents may already have changed the code and mark those cards verification-first.
- Produce stakeholder-friendly summaries in the requested language.
- Extract frontend/backend/mobile contract notes when they help another team implement or verify safely.
- Separate what can be implemented in the current workspace from what must be handed off to a missing repo or another team.

## Workflow

### 1. Ingest The Board Evidence

- Read the full export or ticket source, including all descriptions, comments, labels, attachments, IDs, and column names.
- For Trello MCP links, resolve shortlinks with `trello_search` when a tool needs the internal 24-character card ID, then read card detail, comments/actions, attachments, and checklists before planning.
- Resolve independent cards concurrently, retain a shortlink-to-internal-ID map for the thread, and reuse those IDs for every later Trello call instead of searching again.
- Use the known-safe Trello search limits from `references/trello-mcp-workflow.md`; never send zero for board or member limits. If a call is rejected at schema validation, retry once with the safe shape, then report the blocker rather than repeating the same invalid request.
- If direct attachment content cannot be opened, record the available metadata and avoid claiming visual verification from the attachment.
- Identify the requested subset: first N cards, next N cards, specific IDs, a named column, or all sprint work.
- Keep card IDs and titles visible in the working plan so the user can map the output back to the board.
- Treat the latest QA, customer, or reviewer comment as higher-priority evidence than older title or description text when they conflict.
- Follow linked, blocking, duplicate, or dependency cards when the requested card relies on them for terminology, enum values, acceptance criteria, or current status. Keep this traversal bounded to dependencies that materially change the implementation contract.
- If the user asks for Czech output, write stakeholder summaries and contract notes in Czech.

Use `references/card-contract-notes.md` when producing implementation contracts.
Use `references/trello-mcp-workflow.md` when the source is Trello and MCP tools are available.

### 2. Check Repo And Prior-Agent State

- Inspect relevant repos and existing docs before assuming a card is unimplemented.
- If the user says another AI agent may have changed the work, default that card to verification-first until evidence shows implementation is missing.
- Verify current repo behavior or diffs before concluding another agent understood and implemented the card correctly.
- Preserve dirty worktree state and do not plan reversions unless the user explicitly asks.
- Mark each card as implementation-needed, verification-only, blocked, or needs clarification.
- If the implementation repo for a card is absent, classify the card or subtask as handoff-only and specify the backend/API/docs evidence that can still be verified locally.

### 3. Shape The Batch

- Preserve board order by default.
- Reorder only when a real dependency requires it, and say why.
- Group tightly coupled cards when separate implementation would create duplicate work.
- Split large cards into verifiable vertical slices when a single card spans backend, web, mobile, docs, and QA.

### 4. Extract Contracts And Summaries

For each card when useful, capture:

- affected surface: backend, web, mobile, admin, OpenAPI, docs, or design
- current workspace status: implementable here, handoff-only elsewhere, or mixed
- expected API/route/payload/response/state changes
- user-visible behavior
- verification expectation
- stakeholder summary in the requested language

Do not invent precise payload fields when the ticket does not establish them and repo evidence does not confirm them. Mark such items as implementation questions.

### 5. Hand Off Cleanly

- Use `spec-driven-development` when the batch becomes a traceable implementation plan from source artifacts.
- Use `task-decomposition-and-resume` when the main problem is ordering, safe slice boundaries, or prior-agent resume.
- Use `api-contract-review` when the next safe step is read-only contract comparison.
- Use `ticket-driven-delivery` when ticket evidence is normalized and the user approves implementation, verification, or ticket closeout.
- Use `docs-driven-execution` only when existing `/docs` plans and progress artifacts are the active execution control surface.

## Output

Produce a concise intake result with:

- cards in scope
- ordered implementation or verification plan
- card-by-card summaries
- contract notes when requested
- blockers, assumptions, and verification-first cards
- recommended next owner skill

## Rules

- Do not skip comments.
- Do not skip attachments or checklists when the ticket tool exposes them.
- Do not imply UI/mobile completion when only backend/API or handoff docs are present.
- Do not flatten card IDs away.
- Do not rework prior-agent changes before verifying them.
- Do not turn stakeholder summaries into implementation detail dumps.
- Do not let ticket intake swallow active implementation.
- Do not repeat successful shortlink resolution or serialize independent evidence requests without a real dependency.

## References

Read these only as needed:

- [references/card-contract-notes.md](references/card-contract-notes.md)
  Use for concise frontend/backend/mobile contract summaries.
- [references/trello-mcp-workflow.md](references/trello-mcp-workflow.md)
  Use for Trello shortlink resolution, evidence gathering order, and common MCP pitfalls.
