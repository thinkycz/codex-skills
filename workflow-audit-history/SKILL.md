---
name: workflow-audit-history
description: Use when a task needs a lightweight, durable audit trail of actions, approvals, gaps, and verification without implementing a full agent-history protocol.
version: 1.2.0
category: quality
sources:
  - lightweight workflow audit, gap reporting, and action-versus-approval tracking patterns
use_when:
  - The work is multi-step, delegated, high-stakes, or handoff-heavy enough that explicit action history would reduce ambiguity later.
  - A durable audit summary is needed without building runtime-level protocol infrastructure.
avoid_when:
  - The task is trivial and ordinary delivery docs already provide enough traceability.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Audit output distinguishes actions, approvals, gaps, and evidence without blocking execution on perfect logging.
---

# Workflow Audit History

Create a lightweight, durable audit trail for multi-step work without turning the skill library into a protocol runtime.

This skill is for situations where ordinary delivery docs are not quite enough and the team would benefit from an explicit summary of what happened, who approved key moves, where gaps exist, and what evidence supports the final state.

## When To Use

Use this skill when:

- work is delegated, high-stakes, handoff-heavy, or likely to be reviewed later
- explicit history of actions, approvals, gaps, and verification would reduce ambiguity
- the team needs auditability without building runtime logging infrastructure

Do not use this skill when:

- the task is small and ordinary delivery docs already provide enough traceability
- the real need is full compliance infrastructure, signing, or tamper-evident runtime history
- the work still lacks even basic plans, progress, or verification artifacts

## Core Workflow

1. Start from existing artifacts.
   - Read the available plans, progress docs, verification notes, and delegation records first.
   - Do not create an audit layer from chat memory alone when durable artifacts already exist.

2. Separate action, approval, and evidence.
   - Actions are things the agent or team actually did.
   - Approvals are explicit human or lead-agent decisions that authorized direction changes, delegation, or release.
   - Evidence is what proves the current state.

3. Record gaps explicitly.
   - If some history is missing, interrupted, or uncertain, record that as a gap instead of silently smoothing it over.
   - Prefer an honest partial audit trail over a polished but inaccurate one.
   - When a turn was interrupted, record what was known to have run, what may have partially executed, and what evidence was rechecked before continuing.

4. Fail open.
   - Missing audit detail should not block ordinary implementation or verification work.
   - When logging is incomplete, say what is missing, why it matters, and what can still be trusted.

5. Produce a compact audit summary.
   - Keep it useful for handoff, review, and later reconstruction.
   - Route back to `traceable-delivery`, `release-readiness`, or `verification-before-completion` as the owning workflow for the next action.

## Output

Produce a concise audit summary with:

- actions taken
- approvals or authorization boundaries
- explicit gaps or missing history
- current evidence and what it supports
- recommended next owner or next step

Use [references/example-output.md](references/example-output.md) when a concrete audit-summary shape would help the team stay consistent.

## Rules

- Do not pretend the history is complete when it is not.
- Distinguish action execution from approval or authorization.
- Prefer compact, trustworthy audit notes over exhaustive narration.
- Keep this as a workflow layer, not a protocol implementation.
- Do not infer approval from an implementation step; record explicit user approval or note the approval gap when it matters.

## References

Read these only as needed:

- [references/gap-reporting.md](references/gap-reporting.md)
  Use when some history is missing or uncertain and should be recorded honestly.
- [references/action-vs-approval.md](references/action-vs-approval.md)
  Use when separating what happened from who approved it.
- [references/fail-open-auditing.md](references/fail-open-auditing.md)
  Use when audit completeness is imperfect but execution must continue.
