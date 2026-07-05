---
name: systematic-debugging
description: Investigate bugs, test failures, flaky behavior, build issues, runtime regressions, and integration problems by proving root cause before fixing anything. Use when the agent needs a disciplined debugging workflow with evidence gathering, traceable markdown notes under `/docs`, hypothesis tracking, helper-skill routing, and verification that the final fix actually resolves the underlying issue.
version: 1.4.0
category: debugging
sources:
  - failure evidence, logs, and reproduction steps
  - debugging, verification, and tracking references in this skill package
use_when:
  - A bug, test failure, build issue, or regression needs root-cause investigation.
  - The fastest safe path is evidence-driven debugging instead of stacking guesses.
avoid_when:
  - Expected behavior is still unclear and the task needs source clarification first.
  - The issue cannot yet be evidenced and the next step is still gathering basic repro data.
artifacts:
  - SKILL.md
  - agents/openai.yaml
  - agents/
  - references/
quality_gates:
  - The failure is reproduced or evidenced before fix proposals escalate.
  - Async, external-service, deployment, and lifecycle bugs are traced across every boundary before root cause is assigned.
  - Shared-versus-local root cause is checked after the first credible hypothesis.
  - Final fixes are verified and documented instead of assumed from inspection.
---

# Systematic Debugging

Debug from evidence, not instinct.

Use this skill when something is broken or unstable and the fastest path is to find the actual root cause, make the smallest justified fix, and verify the result instead of stacking guesses.

## Core Promise

- Investigate before fixing.
- Keep the debugging trail visible in markdown under the project’s `/docs` folder.
- Separate symptom, evidence, hypothesis, root cause, fix, and verification.
- Trace the full lifecycle of the user-visible outcome, not just the first successful response.
- Route specialized debugging work to the right helper skills when the issue touches design, API integration, or larger delivery flows.
- Do not claim a bug is fixed until the evidence proves it.
- Record reusable recurrence-prevention guidance when the root cause reveals a broader pattern worth remembering.

## Workflow

### 1. Ground In The Failure

- Capture the exact failure first: error message, failing test, broken screen, log excerpt, reproduction steps, or unexpected behavior.
- Reproduce the issue consistently before proposing fixes.
- Explore the repo, nearby code, recent changes, and existing docs to understand where the failure lives.
- If the user has logs, screenshots, failing commands, bug reports, or source specs/designs, ask for them directly.
- Confirm the actual product surface and repository before deep investigation: web, mobile, backend, worker, build pipeline, or deployment. If the user corrects the target surface, explicitly discard hypotheses derived from the wrong surface and re-ground from the corrected code path.

Before interpreting build or tooling failures as product defects, read the repository's declared runtime and package-manager requirements such as `.nvmrc`, `.tool-versions`, `engines`, lockfiles, or project scripts. Re-run the failing command with the supported toolchain when one is locally available, and keep toolchain mismatch separate from application behavior.

If the issue cannot yet be reproduced reliably, keep gathering evidence instead of jumping to a fix.

### 1.5 Build The Fastest Useful Feedback Loop

- Before fixing, create the quickest deterministic pass/fail signal that exercises the bug.
- Prefer, in order: a failing automated test, curl or HTTP script, CLI invocation with fixture data, browser automation, replayed trace, throwaway harness, property/fuzz loop, or bisection harness.
- Treat the feedback loop itself as part of the debugging work: make it faster, sharper, and more deterministic when the first loop is too broad or flaky.
- If a human must remain in the loop, structure the manual steps and captured output so each hypothesis still has a clear result.

Do not stare at code or stack speculative fixes when the missing piece is a reliable signal.

### 2. Create The Debugging Doc Set

Write markdown files under the project’s `/docs` folder only.

Default structure:

- `/docs/debugging/` for investigation journals, evidence, hypotheses, and root-cause notes
- `/docs/progress/` for live debugging tracker and blocker state when the investigation is non-trivial
- `/docs/verification/` for proof that the final fix resolves the issue without regressions

Do not create the debugging docs in the very first reply unless the user already provided enough concrete evidence to start a real investigation immediately. Use the early turns to gather the failing command, logs, reproduction steps, screenshots, or source expectations first.

Use [references/docs-layout.md](references/docs-layout.md) and [references/evidence-and-tracking.md](references/evidence-and-tracking.md) for the default structure and templates.

### 3. Investigate Root Cause Before Fixing

- Read error output carefully.
- Trace the data flow backward from the failure point to the source.
- Compare the broken path to a working example when one exists.
- Add the smallest instrumentation needed to learn where the behavior diverges.
- For multi-layer problems, gather evidence at each boundary instead of blaming the deepest symptom.
- For async or external-service flows, trace every handoff: incoming request, persisted state, queue/job creation, worker pickup, provider call, callback/webhook if present, stored result, and final user-visible behavior.
- Treat `2xx`, `204`, queued, or "sent" responses as intermediate signals until the intended lifecycle outcome is observed.
- Check runtime and deployment facts when code appears correct: route list, build artifact, migrations, worker process, queue name, environment, framework/runtime version, and stale server state.
- When the first failure comes from an unsupported local runtime or package manager, prove whether the same command passes under the repo-declared toolchain before investigating downstream application hypotheses.
- When an integration is intentionally caught by a test tool or sandbox, distinguish "captured in the test inbox" from "delivered to the real user."

Do not propose fixes before a concrete hypothesis exists.

Read these references when useful:

- [references/root-cause-tracing.md](references/root-cause-tracing.md)
- [references/flaky-and-async-debugging.md](references/flaky-and-async-debugging.md)

### 4. Run A Globalization Check Before Fixing

- After the first credible root-cause hypothesis exists, search the repo for the same pattern before treating the issue as local-only.
- Check for reuse of the same component, helper, mapper, schema, response parser, enum handling, async select pattern, or API shape in other features.
- Explicitly distinguish between:
  - a local defect caused by feature-specific logic
  - a shared defect caused by a reusable component, helper, mapper, schema, or convention
- If the evidence points to a shared layer, make that shared layer the default fix target instead of patching each symptom surface one by one.
- If the issue is confirmed to be local-only, record that the global search was performed and why the wider pattern does not apply.

Do not widen scope blindly. Widen only when the evidence shows a shared root cause or reusable anti-pattern.

### 5. Form And Test One Hypothesis At A Time

- Write down the current hypothesis in the debugging journal.
- Make the smallest possible change or diagnostic check to test that hypothesis.
- Change one variable at a time.
- If the hypothesis fails, update the evidence and form a new one instead of layering fixes.

If multiple attempted fixes have already failed, slow down and question the architecture or assumptions before continuing.
If the user says to try again after repeated failures, first compare the latest evidence against prior hypotheses so the next attempt is not just another speculative patch.

### 6. Route To The Right Helper Skills

Apply `custom-skill-routing` first to choose the right high-level owner when the issue may actually be a delivery, design, or ambiguity problem.

Use [references/skill-routing.md](references/skill-routing.md) for the debugging-specific routing rules that layer on top of that shared routing.

Default routing:

- Use `test-driven-development` when turning a bug or regression into a failing automated test before the final fix.
- Use `verification-before-completion` before saying the issue is fixed, passing, or resolved.
- Use `figma` or `google-stitch` when the bug is visual, design-fidelity-related, or tied to an active design source.
- Use `design-to-prd` when the investigation shows the problem is really that the design exists but no normalized written requirement was ever captured.
- Use `integrating-backend-api-into-frontend` when the bug crosses frontend and backend contract boundaries.
- Use `spec-driven-development` when the investigation reveals the issue is really a mismatch between code and the provided specification/design and needs traceable delivery work.
- Use `product-brainstorming` only when the root problem is unclear expected behavior rather than a technical bug.

### 7. Fix Only After Root Cause Is Proven

- Once the root cause is clear, add or update the failing test when possible.
- Implement the narrowest fix that addresses the source, not just the symptom.
- When the root cause lives in a shared layer, prefer one shared fix plus targeted verification on multiple affected surfaces over repetitive local patches.
- When a payload field, enum, translation key, empty string, or async state bug is found in one feature, search for the same mapper, serializer, normalizer, request helper, or UI state pattern before deciding the fix is local-only.
- Do not bundle refactors or unrelated cleanup into the fix unless they are required for correctness.
- Update the debugging notes to show exactly what was proven and what changed.
- When the investigation reveals a reusable failure pattern, add a short recurrence-prevention note to the debugging or verification artifacts.

### 8. Verify The Fix With Evidence

Verification is required before any completion claim.

Always verify:

- the original reproduction no longer fails
- the relevant tests now pass
- touched runtime flows behave correctly
- no obvious regressions were introduced
- at least one non-primary surface was checked when the fix touched shared logic or reusable infrastructure
- the debugging notes and verification report reflect the final outcome

If the bug involved a written spec or design expectation, verify against that source too.

Read [references/verification.md](references/verification.md) for the required verification layers and reporting expectations.

## Delivery Rules

- Do not guess the fix before proving the cause.
- Do not jump from symptom to patch without tracing backward.
- Do not combine multiple speculative fixes in one pass.
- Do not hide missing evidence or failed hypotheses.
- Do not write non-markdown status artifacts outside `/docs`.
- Do not trust agent reports of success without independent verification.

## Output Expectations

At the end of a successful debugging run, the project should have:

- a debugging journal under `/docs/debugging/`
- a live tracker under `/docs/progress/` when the issue is non-trivial
- a verification report under `/docs/verification/`
- a clear recorded root cause
- a justified fix tied to the proven cause
- fresh evidence showing the issue is resolved
- a short recurrence-prevention note when the root cause exposed a reusable pattern
