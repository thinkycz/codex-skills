# Vertical Agent Slices

Use this reference when broad work should become agent-ready tasks, issue drafts, or resumable implementation slices.

## Tracer Bullet Slices

Prefer thin vertical slices that cut through the minimum necessary layers end to end. A good slice is independently demoable or verifiable.

Good slices:

- deliver one narrow behavior across the real surfaces it needs
- include enough backend, frontend, data, docs, or tests to prove the path works
- leave a clear acceptance check
- unblock a specific next slice

Avoid horizontal slices such as "build all database models", "write all API endpoints", or "make the whole UI shell" unless they are genuinely standalone milestones.

## AFK And HITL

Classify each slice when another agent may pick it up:

- AFK:
  The slice can be implemented by an agent without further human judgment. Requirements, acceptance checks, and dependencies are clear.
- HITL:
  The slice requires human-in-the-loop input such as product judgment, design review, credentials/access, policy approval, or unresolved architecture choice.

Prefer AFK slices where possible, but do not pretend a slice is AFK when a human decision is still the blocker.

## Issue Draft Shape

When drafting issue-like slices, include:

- title
- AFK or HITL classification
- blocked-by dependencies
- behavior to build
- acceptance criteria
- verification expectation

Keep file paths and code snippets out of the issue unless they encode a stable decision from the repo or a prototype. File-level details go stale quickly.
