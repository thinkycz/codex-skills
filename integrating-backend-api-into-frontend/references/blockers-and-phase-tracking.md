# Blockers And Phase Tracking

Apply `traceable-delivery` first for the shared tracker structure, docs layout, status discipline, and verification closeout.

This reference adds the integration-specific blocker taxonomy and closeout rules for backend-supported frontend work.

Use this reference when the integration effort spans multiple modules or when backend support is incomplete.

## Required Blocker Statuses

Use these exact categories:
- `backend missing`
- `intentionally deferred`
- `runtime/framework issue`
- `cancelled`

Do not blur them together.

## How To Record A Blocker

Each blocker should say:
- the user-visible action or page that is affected
- what backend or runtime support is missing
- why the frontend should not fake completion
- what remains visible in the UI, if anything

Bad blocker note:
- "still not working"

Good blocker note:
- "partner pricing assignment remains blocked because the backend exposes relation reads but no attach/detach write endpoint"

## Progress Snapshots

Keep a high-level snapshot or index updated so another engineer can quickly tell:
- which phases are complete
- which phases are active
- which items are blocked or cancelled
- what the next recommended implementation slice is

## During Execution

After each meaningful slice:
- update the affected phase doc
- convert newly verified behavior into evidence
- reclassify any resolved blockers
- keep cancelled scope explicitly marked as cancelled, not backend blocked

## Closing A Phase

A phase can close when:
- the intended feature set is implemented and verified
- remaining gaps are outside the phase's promised surface
- blocker notes are current
- no "temporary" placeholders remain disguised as finished work

If the backend evolves later, revisit the phase and update its status based on the new contract.
