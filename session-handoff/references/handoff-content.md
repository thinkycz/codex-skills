# Handoff Content

Use a handoff to preserve continuation context, not to rewrite every artifact.

## Include

- Continuation goal:
  What the next agent or session should accomplish.
- Current status:
  What is done, in progress, blocked, or unverified.
- Suggested skills:
  One primary next skill and any supporting skills, with short reasons.
- Touched files:
  Paths to files changed or inspected, grouped by purpose when useful.
- Existing artifacts:
  Paths or URLs to PRDs, plans, ADRs, tickets, diffs, commits, screenshots, or verification notes.
- Commands and evidence:
  Commands run, test/build status, browser checks, screenshots, logs, or manual verification.
- Blockers and risks:
  Missing credentials, failing checks, unclear requirements, dirty worktree cautions, or external dependencies.
- Next concrete step:
  The first action the next agent should take.

## Redact

- API keys, tokens, passwords, cookies, auth headers, private keys, and secret env values.
- Private URLs when the exact URL is not needed for continuation.
- Personal data that is not necessary for the next agent.
- Client-specific business facts that should not become reusable memory.

## Avoid

- Duplicating long PRDs, plans, or issue bodies.
- Claiming release readiness without evidence and a `release-readiness` pass.
- Hiding uncertainty. Mark assumptions and unverified claims plainly.
- Writing repo-tracked handoff files unless the user explicitly requested durable docs.
