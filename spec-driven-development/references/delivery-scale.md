# Delivery Scale

Use this reference before creating traceability artifacts or loading helper skills.

## Small

Choose small when the request has one obvious slice, bounded acceptance, and little risk of losing state between turns.

- route directly to the implementation owner
- use the nearest behavior-level tests and a fresh verification closeout
- do not create spec, plan, tracker, matrix, and verification documents as separate files

Examples include a focused toggle, copy or layout correction, one contract branch, or a narrow bug fix with a clear reproducer.

## Medium

Choose medium when several surfaces must stay synchronized but the work still has one coherent execution path.

- use one combined plan/progress document when the repo benefits from durable tracking
- record requirements as a compact checklist inside that document
- add a verification record only when the repo convention or handoff value justifies it
- keep one primary implementation owner; add helpers only when they change the outcome materially

## Large

Choose large when the work has multiple independent phases, migrations or shared contracts, external prerequisites, broad role or client coverage, or likely interruption and resume.

- use the full normalized spec, phased plan, progress/traceability matrix, and verification record
- keep deferred integrations explicit
- use verification-before-completion when the result genuinely needs a go/no-go judgment

## Escalation Rule

Start with the lightest tier supported by the evidence. Escalate when scope, risk, or resume needs grow. Do not select the large tier merely because the user supplied a detailed plan or explicitly named the skill.
