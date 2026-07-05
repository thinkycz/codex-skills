---
name: verification-before-completion
description: Require fresh evidence before claiming work is done, fixed, passing, or matched. Use when implementation, debugging, or fidelity work is mostly complete and the agent needs to verify the relevant tests, runtime behavior, design expectations, docs, and blockers before making a success claim.
version: 1.5.0
category: quality
sources:
  - fresh test, runtime, design, and docs evidence
  - verification-layer guidance in this skill package
use_when:
  - The work is mostly complete and the next step is proving the actual completion claim.
  - The user wants confidence that tests, runtime behavior, docs, or fidelity really hold.
avoid_when:
  - Implementation or debugging is still actively changing the claim.
  - There is no meaningful evidence surface to run yet.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The completion claim is restated before verification begins.
  - The right verification layers run for the claim instead of the easiest checks.
  - User-visible lifecycle paths are exercised when the claim depends on runtime flow, async work, or integration behavior.
  - Missing evidence is reported plainly instead of softened into success.
---

# Verification Before Completion

Do not let a success claim outrun the evidence.

Use this skill near the end of implementation, debugging, or design-fidelity work when the next step is to prove the result rather than continue coding.

## Core Promise

- Verify the thing that was actually requested, not just the easiest green check.
- Prove the actual completion claim at the highest useful level, such as the clicked link, page load, API route, queued job result, or browser flow the user cares about.
- Prefer fresh evidence over assumptions, stale logs, or “should be fixed now”.
- Check the most relevant technical and product-facing surfaces before claiming success.
- Leave a clear record of what was verified and what remains unverified.

## Boundary

- Own the proof step near the end of work, not the implementation or debugging itself.
- Do not replace `release-readiness` when the broader question is go or no-go judgment across a whole delivery slice.
- Do not replace `systematic-debugging` when verification fails and the root cause is still unknown.
- Use this skill to test the claim honestly, not to stretch incomplete evidence into completion.
- This skill proves a specific claim such as fixed, implemented, passing, visually matched, or docs-current. `release-readiness` decides whether the whole feature or fix is ready for handoff or release.

## Core Workflow

### 1. Restate The Completion Claim

Before verifying, state what is being claimed:

- fixed
- implemented
- passing
- visually matched
- ready for review

Tie the claim to the user request, spec, PRD, bug report, or design source rather than to a vague notion of progress.

### 2. Choose The Right Verification Layers

Select only the layers that actually matter for the touched surface:

- targeted automated tests
- nearest related suite
- lint or typecheck
- build or release check
- runtime/manual behavior
- API contract compliance
- design or fidelity comparison
- docs, blockers, and tracker freshness

Do not stop at static checks when the claim is about runtime behavior or visual parity.

Build a claim-specific rubric before or during verification when the acceptance bar is non-trivial. The rubric can stay lightweight, but it should make the evidence standard explicit.

### 3. Run Fresh Evidence

- Prefer running the exact command or test that proves the changed behavior.
- Then run the smallest broader confidence pass that makes regressions less likely.
- If a claim depends on browser or manual behavior, exercise the real flow.
- If a claim depends on async, queue, email, payment, upload, notification, or external-provider behavior, verify each required handoff or clearly report which handoff could not be observed.
- If the reported bug was a runtime/deploy mismatch, verify registered routes, migrations, build artifact, process/runtime version, or worker state as part of the claim.
- If a claim depends on a design or spec, verify against that source explicitly.
- Prefer the repo's own verification commands when they are documented or supplied by the user, such as `make fix`, `make check`, framework builds, local dev servers, and seeded login users.
- For frontend work, run a browser or runtime smoke on the touched route when the claim involves clicks, redirects, loading states, uploads, responsive layout, or language switching.

### 4. Compare Evidence To The Claim

- Confirm whether the evidence fully supports the claim, partially supports it, or contradicts it.
- Call out gaps directly:
  - tests passed but runtime not checked
  - build passed but fidelity not checked
  - local flow worked but docs or blockers are stale
  - bug no longer reproduces but no regression test was added
  - interrupted or resumed work appears correct, but process state, git state, or durable docs were not rechecked after the interruption
  - a low-level test passed, but the original user-visible path was not exercised
  - the current repo was verified, but another required repo or app was absent
- When useful, summarize the comparison as:
  - claim
  - evidence gathered
  - missing evidence
  - verdict

### 5. Close Honestly

- If the evidence is sufficient, say exactly what was verified.
- If the evidence is incomplete, say what is still missing.
- If the evidence fails, do not soften the result into a near-success.
- After major work, capture any reusable verification lesson in the relevant docs or closeout artifact instead of leaving it only in chat.
- If part of the supporting history or evidence trail is missing, record that as an explicit gap rather than implying complete verification provenance.

## Verification Rules

- Do not claim success from code inspection alone.
- Do not rely on stale command output from before the latest changes.
- Do not collapse “implemented”, “verified”, and “ready” into the same status.
- Do not ignore docs or blocker state when the workflow is traceable and multi-phase.
- Do not imply complete audit history when part of the evidence chain is missing.

## Handoffs

- Use `release-readiness` when broader go/no-go judgment is needed after verification.
- Use `systematic-debugging` when the verification fails and the result is not actually explained yet.
- Use `design-fidelity-polish` when the remaining failure is mostly visual parity.

## References

Read these only as needed:

- `references/verification-layers.md`
  Use for choosing the right mix of checks for the claim.
- `references/closeout-language.md`
  Use for reporting verified, partially verified, and not verified outcomes clearly.
