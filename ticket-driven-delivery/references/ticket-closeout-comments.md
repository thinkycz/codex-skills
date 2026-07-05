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

## Comment Checklist

- The comment maps clearly to the ticket's user-visible issue.
- The fix summary is accurate even if the reader never sees the diff.
- Any known caveat is stated plainly.
- The wording does not overclaim if tests were blocked or only partial verification ran.
