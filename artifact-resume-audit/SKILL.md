---
name: artifact-resume-audit
description: Use when plans, progress docs, exports, prior Codex task histories, or other durable artifacts exist but the safest restart point is unclear.
version: 1.4.0
category: execution-planning
sources:
  - artifact-driven resumption, stale-doc detection, and restart-point auditing
  - accessible prior Codex task histories and their recorded claims
use_when:
  - Ongoing work has durable artifacts, but they may be stale, partial, contradictory, or abandoned.
  - The goal is to identify the single safest restart point before more planning or coding.
avoid_when:
  - The next slice is already clear from trustworthy current artifacts.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The audit identifies trustworthy artifacts, stale surfaces, and the safest restart point without replanning everything from scratch.
  - Prior-task claims are reconciled against current repo, runtime, and verification evidence before reuse.
---

# Artifact Resume Audit

Audit the existing artifacts to find the single safest restart point for ongoing work.

This skill is for messy resume situations where plans, progress docs, exports, notes, or verification artifacts exist but cannot all be trusted equally. Its job is to determine what is current, what is stale, and where execution should resume without starting over blindly.

It is narrower than `task-decomposition-and-resume`: audit trust first here, then decompose fresh slices only after the safest restart point is known.

## Boundary

- Own restart-point auditing when the artifact trail itself is untrustworthy.
- Do not replace `task-decomposition-and-resume` when the artifact trail is already trustworthy and the remaining problem is slice design.
- Do not replace `docs-driven-execution` when the next executable slice is already clear from current artifacts.
- Use this skill to establish trust and restart position, not to replan the whole project by default.

## When To Use

Use this skill when:

- durable artifacts exist, but they are partial, stale, contradictory, or abandoned
- the user references a prior Codex task ID whose conclusions or implementation should inform current work
- a previous agent turn was interrupted and commands or edits may have partially executed
- the next slice is unclear because the written trail is messy
- the safest restart point matters more than decomposing fresh work from scratch

Do not use this skill when:

- current artifacts are trustworthy and already point to the next slice clearly
- the work needs brand-new planning rather than resume auditing
- there is no durable artifact trail at all

## Core Workflow

1. Inventory the artifact trail.
   - Read the active plan, progress tracker, blockers, verification notes, exports, and any audit or handoff docs that exist.
   - When the user provides a Codex task ID, read that task with the native Codex task tools and extract its goal, claimed changes, touched surfaces, verification, blockers, and unfinished work.
   - Identify what artifacts are in play before choosing a restart point.
   - When interruption is part of the history, also inspect current git/worktree state and any still-running local processes relevant to the interrupted work.

2. Classify artifact trust.
   - trustworthy and current
   - partially useful but stale
   - contradictory
   - obsolete
   - Treat prior-task prose as a claim source, not proof. Prefer current repo state, deployed or installed artifact identity, fresh runtime evidence, and durable project docs when they disagree with the transcript.

3. Find the narrowest safe restart point.
   - Prefer the smallest slice that can resume with confidence.
   - Avoid restarting too early just because the artifact trail is messy.

4. Recommend the next owner.
   - Route to `docs-driven-execution`, `task-decomposition-and-resume`, `workflow-audit-history`, or a domain owner based on what the audit found.

## Output

Produce a concise resume audit with:

- artifacts reviewed
- trust classification
- contradictions or stale surfaces
- safest restart point
- recommended next owner

## Rules

- Resume from durable truth when possible, not chat reconstruction.
- Use native task history when the user explicitly references it, but reconcile it with current state before transferring decisions or code patterns.
- Prefer the narrowest trustworthy restart point.
- Distinguish stale from contradictory; they are not the same problem.
- Do not replan the whole project unless the artifact trail is truly unusable.

## References

Read these only as needed:

- [references/trust-rubric.md](references/trust-rubric.md)
  Use for rating artifact reliability.
- [references/restart-selection.md](references/restart-selection.md)
  Use for choosing the safest restart point without unnecessary rediscovery.
