# Pressure Testing

Use this reference when a skill should be validated through realistic behavior, not only metadata review.

## When To Use

- process or discipline skills
- routing or orchestration skills
- quality-gate or verification skills
- any skill where the main risk is rationalization, overreach, or skipped steps

## Checks

- use a realistic prompt that should trigger the skill
- confirm the skill takes ownership only of its intended phase
- confirm handoffs go to the correct downstream owner
- confirm the workflow still works when the prompt is ambiguous, rushed, or tempting shortcuts
- confirm examples describe real tool use instead of transcript formats the model might mimic

## Closeout

- report whether the validation was scenario-based, metadata-only, or blocked
- call out any skill that passes metadata review but still feels behaviorally weak

## Scenario And Evaluation Records

The library's [scenario fixtures](../../scripts/fixtures/skill-behavior-scenarios.json) define prompts, source packages, expected owners, required actions and prohibited actions. The [evidence checker](../../scripts/check_skill_behavior.py) checks definitions and [recorded results](../../scripts/fixtures/skill-behavior-results.json); it does not execute or judge a model. Static owner/mode/dependency validation remains separate.

To evaluate behavior:

1. Give an evaluator only the realistic prompt, available skill discovery, and necessary raw artifacts. Keep expected ownership and assertion lists out of its context. Use an independent agent when available and authorized; otherwise leave the independent evaluation `not_run` rather than synthesizing a success record.
2. Bound a dry run to decisions and proposed actions without live side effects. Label it `independent-dry-run`; reserve `observed-execution` for actual permitted task execution. Decision quality alone does not prove a real product flow.
3. Have a reviewer compare the actual response with every assertion. For required actions, `passed` means performed or appropriately proposed for the dry run. For prohibited actions, `passed` means avoided. Missing evidence is not a pass. Quote the supporting response exactly and explain any failure in the response/review context.
4. Record schema version 1 and an `evaluations` list. Each record contains `scenario_id`, `method`, `evaluator`, `reviewer`, timezone-aware `evaluated_at`, `source_fingerprint`, the exact `response`, `observed_owner`, `status`, and `checks` keyed by every assertion ID. Each check contains boolean `passed` and a supporting `evidence` quote. A `blocked` record instead requires a `blocker` reason.
5. Compute the scenario fingerprint using the evidence checker against the sources actually evaluated. It hashes the scenario and all declared skill-package files. Include all packages that materially influenced the evaluation in the scenario sources before evaluating; do not refresh hashes to make an old response look current.
6. Run `python3 scripts/check_skill_behavior.py --require-evaluated` from the library root for a current recorded-evaluation gate. Missing results are `not_run`; changed sources are `stale`; blocked, failed, stale, and unrun cases cannot satisfy this gate.

The checker confirms record completeness, ownership agreement, quoted evidence presence, and freshness. It cannot prove evaluator honesty or semantic sufficiency; that is the reviewer's responsibility. Tests of the checker are evidence-integrity tests, not skill behavioral results. Store only synthetic, sanitized cases and responses in reusable fixtures.
