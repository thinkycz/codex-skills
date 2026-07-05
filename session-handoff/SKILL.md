---
name: session-handoff
description: Use when the user wants the current conversation, work state, or implementation context compacted into a handoff document for a future agent or session.
version: 1.0.0
category: execution-planning
sources:
  - current conversation context, repo state, plans, diffs, commands, verification evidence, and existing artifacts
  - handoff workflow adapted from /Users/longdo/Downloads/skills-main
use_when:
  - The user asks to write a handoff, continuation note, next-agent brief, or compact summary for another session.
  - Current work needs to be preserved without duplicating existing PRDs, plans, ADRs, issues, commits, or docs.
avoid_when:
  - The task is to audit stale or contradictory existing artifacts before resuming; use artifact-resume-audit.
  - The user wants final release or go/no-go judgment; use release-readiness.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Handoffs include status, suggested skills, touched files, evidence, blockers, next step, and existing artifact references.
  - Secrets, credentials, private URLs, tokens, and unnecessary PII are redacted.
  - Default output goes to the OS temp directory unless the user explicitly requests a durable repo artifact.
---

# Session Handoff

Compact the current work state so another agent or future session can continue without rediscovery.

Use this skill when the user asks for a handoff, continuation note, next-agent brief, or compact summary of the current conversation and work. The handoff should capture what matters for continuation while referencing existing artifacts instead of copying them wholesale.

By default, write the handoff to the OS temp directory, not the project repo. Create a durable repo artifact only when the user explicitly asks.

## Boundary

- Own creation of a fresh continuation handoff from the current conversation and local evidence.
- Do not replace `artifact-resume-audit` when the main job is deciding which old artifacts are trustworthy.
- Do not replace `task-decomposition-and-resume` when the main job is breaking future work into slices.
- Do not replace `release-readiness` for final handoff or release go/no-go decisions.
- Do not duplicate PRDs, plans, ADRs, issue bodies, commits, or docs when a path, URL, or short pointer is enough.

## Workflow

### 1. Gather Current State

- Identify the user goal, current status, completed work, active files, pending work, and any blockers.
- Inspect local repo state when relevant, including `git status`, touched files, and recent command evidence.
- Reference existing durable artifacts by path or URL instead of pasting their full contents.
- If the user gives a target for the next session, tailor the handoff around that continuation goal.

### 2. Select Suggested Skills

- Recommend the likely next owner skill and any supporting skills.
- Prefer one primary skill plus explicit handoffs.
- Include why each suggested skill matters, briefly.

### 3. Redact Sensitive Material

- Remove or mask API keys, passwords, tokens, private URLs, credentials, personal data, and client-specific secrets.
- Do not include environment variable values unless they are public placeholders.
- If a secret is operationally relevant, say that it must be supplied through the normal secure channel.

Use [references/handoff-content.md](references/handoff-content.md) for content shape and redaction reminders.

### 4. Write The Handoff

Default structure:

- title and timestamp
- continuation goal
- current status
- suggested skills
- touched files or artifacts
- commands and verification evidence
- blockers, risks, and assumptions
- next concrete step

Write to an OS temp path unless the user explicitly requests a repo path. Tell the user where the handoff was written and summarize the next step.

## Rules

- Do not write into the project repo by default.
- Do not store secrets, private URLs, or unnecessary personal data.
- Do not copy long existing documents into the handoff; link or reference them.
- Do not claim work is ready for release; route readiness judgment to `release-readiness`.
- Do not use a handoff as a substitute for validating stale artifacts.

## References

Read these only as needed:

- [references/handoff-content.md](references/handoff-content.md)
  Use for handoff structure, evidence capture, suggested skills, and redaction guidance.
