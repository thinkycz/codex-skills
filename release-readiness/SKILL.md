---
name: release-readiness
description: Decide whether a feature or fix is truly ready for handoff, review, or release by checking verification evidence, blocker state, docs freshness, and remaining gaps. Use when implementation is mostly done and the agent needs to produce a final readiness assessment instead of assuming done.
version: 1.4.0
category: quality
sources:
  - verification evidence and blocker state from the current delivery artifacts
  - release and handoff decision patterns in this workspace
use_when:
  - Implementation is mostly done and the next step is a readiness decision.
  - The user wants an explicit handoff, review, or release assessment.
avoid_when:
  - Coding, debugging, or source clarification is still the main job.
  - There is no fresh evidence to assess yet.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - Readiness claims are tied to fresh verification evidence.
  - Remaining blockers and stale docs are called out explicitly.
  - The verdict distinguishes ready, not ready, and partially evidenced states honestly.
---

# Release Readiness

Turn “it seems done” into an explicit readiness decision.

Apply this skill near the end of delivery or debugging when code exists, checks have run, and you need to decide whether the work is actually ready for handoff, review, or release.

Use `verification-before-completion` first when the main need is to prove one specific claim. Use this skill when enough evidence exists to make the broader go/no-go call across verification, blockers, docs, source alignment, and remaining risk.

## Boundary

- Own the final readiness verdict across evidence, blockers, docs, source alignment, and known risk.
- Do not replace `verification-before-completion` when the current need is proving one specific completion claim.
- Do not replace `systematic-debugging` when verification failed and the cause is not understood.
- Do not reopen implementation planning unless the readiness verdict exposes a blocker that must route back to another owner.

## Checkpoints

- fresh verification evidence exists
- blockers and deferred items are current
- plans and progress docs match the actual delivered state
- any PRD, design doc, or written source of truth still matches the delivered behavior
- known gaps are explicit
- user-facing flows affected by the change were exercised appropriately
- source-of-truth requirements or design expectations were checked when relevant
- the readiness decision compares the claimed outcome against the evidence actually collected
- important approval boundaries or missing approval history are explicit when they affect release confidence
- interrupted or resumed work has been rechecked against current docs, worktree state, and fresh verification before the verdict

## Output

Produce a concise readiness summary covering:

- what is ready
- what is not ready
- known risks
- required follow-ups before release, if any
- any reusable lesson or new guardrail that should survive beyond this release decision
- whether the delivered behavior is fully verified, partially evidenced, or only statically checked

Use `references/example-output.md` when a concrete readiness-review shape would help.

## Rules

- Do not confuse “code written” with “release ready”.
- If docs, blockers, or verification are stale, call that out directly.
- If the build drifted from the PRD, design doc, or design source, call that out directly.
- Prefer an honest “not ready yet because…” over a soft-complete summary.
- Keep the readiness verdict tied to explicit evidence, not overall optimism.
- If part of the action or approval history is missing, call out the audit gap instead of quietly assuming it is fine.

## References

Read these only as needed:

- `references/example-output.md`
  Use for a concrete readiness-review shape when needed.
