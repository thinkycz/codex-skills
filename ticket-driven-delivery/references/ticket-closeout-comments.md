# Ticket Closeout Comments

Use these templates when writing comments back to Trello, Jira, Linear, GitHub Issues, or a similar tracker after implementation or verification.

## Principles

- Write for stakeholders and QA, not for code reviewers.
- Use the language requested by the user or used in the ticket.
- Keep the comment pasteable and concise.
- Explain behavior, not internal implementation trivia.
- Mention verification only when it helps QA trust the handoff.
- Do not include private paths, credentials, long stack traces, or full diffs.

## Czech Template

```text
Opraveno.

Co bylo špatně:
- ...

Jak je to opravené:
- ...
- ...

Ověření:
- ...
```

For verification-only tickets:

```text
Zkontrolováno, bez nutnosti další úpravy kódu.

Co jsem ověřil:
- ...

Výsledek:
- ...
```

For implemented work that still requires deployment or runtime verification:

```text
Implementováno, čeká na nasazení / runtime ověření.

Co bylo špatně:
- ...

Jak je to opravené:
- ...

Zbývá:
- nasadit migraci / nový build / restartovat worker
- zopakovat konkrétní QA scénář
```

## English Template

```text
Fixed.

What was wrong:
- ...

How it was fixed:
- ...
- ...

Verification:
- ...
```

For verification-only tickets:

```text
Verified, no code change needed.

What I checked:
- ...

Result:
- ...
```

For implemented work that still requires deployment or runtime verification:

```text
Implemented; deployment / runtime verification pending.

What was wrong:
- ...

How it was fixed:
- ...

Remaining:
- deploy the migration / new build / restart the worker
- replay the exact QA scenario
```

## Comment Checklist

- Current ticket comments were read immediately before posting.
- No existing comment already communicates the same completed scope, remaining work, contract, and verification status.
- The comment maps clearly to the ticket's user-visible issue.
- The fix summary is accurate even if the reader never sees the diff.
- Any known caveat is stated plainly.
- The wording does not overclaim if tests were blocked or only partial verification ran.
- Deployment, migration, worker, or app-build requirements are explicit when the live environment was not verified.
- The posted comment was read back from the intended ticket and checked for language, status wording, and requested ordering.

## Idempotent Posting

- Compare meaning rather than exact text. A differently worded comment is still a duplicate when it communicates the same fix, verification, handoff, and remaining work.
- When an equivalent comment already exists, leave it unchanged and report that no new comment was needed.
- When posting several comments, preserve the requested ticket order and read each one back before moving on.
