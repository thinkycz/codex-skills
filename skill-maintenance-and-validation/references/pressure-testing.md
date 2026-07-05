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
